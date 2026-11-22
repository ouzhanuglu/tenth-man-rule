#!/usr/bin/env python3
"""Validate a skill folder and package it for release.

Produces two archives next to each other:
  <name>.skill         SKILL.md plus content subdirectories (references/, assets/, scripts/),
                       excluding evals/, .github/ and repo-root docs
  <name>-evals.zip     the evals/ tree, if present

The split mirrors the skill format convention: evals are development artifacts and do not
belong in the installable package, but they are worth shipping alongside it.

Usage:
    python3 .github/scripts/package_skill.py <skill-dir> <out-dir> [--expect-version X.Y.Z]

Exit codes: 0 packaged, 1 validation or packaging error.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

EXCLUDED_DIRS = {"__pycache__", "node_modules", ".git"}
EXCLUDED_NAMES = {".DS_Store", "*.pyc"}
ROOT_ONLY_EXCLUDED = {"evals", ".github", ".git"}


def parse_frontmatter(text: str) -> dict:
    """Minimal YAML subset parser: top-level keys plus one level of nesting.

    Only scalars, lists-in-brackets and nested mappings are needed for skill frontmatter.
    Nested values are keyed by their parent (metadata.version, metadata.author, ...).
    """
    if not text.startswith("---"):
        raise SystemExit("error: SKILL.md must start with a YAML frontmatter block")
    end = text.find("\n---", 3)
    if end == -1:
        raise SystemExit("error: SKILL.md frontmatter is not closed")

    data: dict = {}
    stack: list[tuple[int, dict]] = [(-1, data)]

    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^(\s*)([A-Za-z0-9_.-]+):\s*(.*)$", line)
        if not match:
            continue
        indent = len(match.group(1))
        key, value = match.group(2), match.group(3).strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if value == "":
            node: dict = {}
            parent[key] = node
            stack.append((indent, node))
        else:
            parent[key] = value.strip("'\"")

    return data


def validate(skill_dir: Path, expected_version: str | None) -> tuple[str, str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        raise SystemExit(f"error: {skill_md} not found")

    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)

    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        raise SystemExit("error: frontmatter is missing 'name'")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name):
        raise SystemExit(f"error: name '{name}' must be lowercase letters, digits and hyphens")
    if not description:
        raise SystemExit("error: frontmatter is missing 'description'")
    if len(description) > 1024:
        raise SystemExit(f"error: description is {len(description)} chars, limit is 1024")

    nested = meta.get("metadata")
    version = nested.get("version", "") if isinstance(nested, dict) else ""

    if expected_version:
        want = re.match(r"^v?(\d+\.\d+\.\d+)", expected_version)
        have = re.match(r"^(\d+\.\d+\.\d+)", version or "")
        if not want:
            raise SystemExit(f"error: --expect-version '{expected_version}' is not version-like")
        if not have:
            raise SystemExit("error: --expect-version given but frontmatter has no metadata.version")
        if want.group(1) != have.group(1):
            raise SystemExit(
                f"error: tag says {want.group(1)} but metadata.version says {have.group(1)}; "
                "bump the version before tagging"
            )

    return name, version


def package(skill_dir: Path, out_dir: Path, name: str) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    produced: list[Path] = []
    # Never archive our own output: the build directory may sit inside the skill folder.
    out_resolved = out_dir.resolve()

    skill_path = out_dir / f"{name}.skill"
    with zipfile.ZipFile(skill_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(skill_dir)
            if out_resolved in path.resolve().parents:
                continue
            if rel.parts and rel.parts[0] in ROOT_ONLY_EXCLUDED:
                continue
            # Keep the package to skill content: SKILL.md plus subdirectories such as
            # references/, assets/ and scripts/. Repo-root docs stay in the repo.
            if len(rel.parts) == 1 and rel.name != "SKILL.md":
                continue
            if any(part in EXCLUDED_DIRS for part in rel.parts):
                continue
            if path.name in EXCLUDED_NAMES or path.suffix == ".pyc":
                continue
            archive.write(path, Path(name) / rel)
    produced.append(skill_path)

    evals_dir = skill_dir / "evals"
    if evals_dir.is_dir():
        evals_path = out_dir / f"{name}-evals.zip"
        with zipfile.ZipFile(evals_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(evals_dir.rglob("*")):
                if not path.is_file() or path.name in EXCLUDED_NAMES:
                    continue
                archive.write(path, path.relative_to(skill_dir))
        produced.append(evals_path)

    return produced


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--expect-version", default=None)
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    name, version = validate(skill_dir, args.expect_version)
    produced = package(skill_dir, args.out_dir.resolve(), name)

    print(f"validated {name} (metadata.version {version or 'unset'})")
    for path in produced:
        with zipfile.ZipFile(path) as archive:
            members = len(archive.namelist())
        print(f"packaged {path.name}: {members} files, {path.stat().st_size} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
