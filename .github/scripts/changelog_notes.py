#!/usr/bin/env python3
"""Extract one version's section from CHANGELOG.md as a release-notes body.

Usage:
    changelog_notes.py CHANGELOG.md v1.2.3 > notes.md

Exit 0 with the notes on stdout when the section exists. Exit 2 when it does not, so the
release workflow can fall back to GitHub's generated notes instead of publishing an empty body.

The section is "## [1.2.3] — date" up to the next top-level "## " heading; the bracket and the
date are optional, and a pre-release tag like v1.2.3-rc1 is matched against the same label.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING = re.compile(r"^##\s+\[?v?([0-9][^\]\s]*)\]?")


def extract(text: str, tag: str) -> str | None:
    want = tag.lstrip("v")
    lines = text.splitlines()

    start = None
    for index, line in enumerate(lines):
        match = HEADING.match(line)
        if match and match.group(1) == want:
            start = index
            break

    if start is None:
        return None

    body: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        body.append(line)

    section = "\n".join(body).strip()
    if not section:
        return None

    return f"## {tag}\n\n{section}\n"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__, file=sys.stderr)
        return 1

    changelog, tag = Path(sys.argv[1]), sys.argv[2]
    if not changelog.is_file():
        print(f"error: {changelog} not found", file=sys.stderr)
        return 1

    notes = extract(changelog.read_text(encoding="utf-8"), tag)
    if notes is None:
        print(f"no CHANGELOG section for {tag}", file=sys.stderr)
        return 2

    sys.stdout.write(notes)
    return 0


if __name__ == "__main__":
    sys.exit(main())
