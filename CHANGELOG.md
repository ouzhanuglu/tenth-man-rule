# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] — 2026-11-22

### Added

- The `validate` workflow now runs pinned `actionlint` 1.7.7 as a separate job. It verifies the
  downloaded release archive against the publisher's checksum file before linting all workflow
  YAML files.
- The negative Tier 3 case now has three assertions, so every dataset case has a behavior check.

### Verified

- The workflow parser, shell syntax checks, real actionlint download/checksum/run, and both
  negative controls (malformed workflow and leaked package member) pass locally on a clean
  checkout.
- GitHub Actions `validate` passed with the actionlint job and package assertions.


## [1.1.0] — 2026-11-22

### Changed

- The 4-case review library moved out of `evals/` into `review/` (`review-cases.json`,
  `README.md`, `INSTALL.md`, `fixtures/`). `evals/` now holds only the Tier 3 dataset and its
  staged `files/`, so `skillevaluator tier3 validate --strict` exits 0 with no warnings.
- The release bundle still ships one archive: `INSTALL.md` at the root, then the `evals/` and
  `review/` trees. The `validate` workflow asserts that split.

### Added

- A 10-case Tier 3 dataset for SkillEvaluator at `evals/evals.json`, with `assertions`,
  `expected_skill` and staged `files/`, including one negative case. The 4-case review library
  moves to `evals/review-cases.json`; both shapes are kept on purpose.
- `## Purpose`, `## Prerequisites`, `## Limitations` and `## Troubleshooting` sections in
  `SKILL.md`, plus `metadata.tags`, closing the SkillEvaluator quality findings. Description
  rewritten trigger-first within the 60-character budget Hermes uses for its skill index.

### Added

- A 10-case Tier 3 dataset for SkillEvaluator at `evals/evals.json`, with `assertions`,
  `expected_skill` and staged `files/`, including one negative case. The 4-case review library
  moves to `evals/review-cases.json`; both shapes are kept on purpose.
- `## Purpose`, `## Prerequisites`, `## Limitations` and `## Troubleshooting` sections in
  `SKILL.md`, plus `metadata.tags`, closing the SkillEvaluator quality findings. Description
  rewritten trigger-first within the 60-character budget Hermes uses for its skill index.

## [1.0.2] — 2026-11-22

### Changed

- Release notes now come from this file. The `release` workflow extracts the section matching
  the tag (`v1.0.2` → `## [1.0.2]`) and publishes it as the release body instead of a commit
  list. If no section matches the tag, the job warns and falls back to GitHub's generated
  notes rather than publishing an empty body.
- A tag whose label does not match a section exactly — for example `v1.0.1-ci-notes` — takes
  the fallback path by design; pre-release tags need their own heading such as
  `## [1.1.0-rc1]`.
- Re-running the workflow for an existing release refreshes assets only, so hand-edited
  release notes are never overwritten.

## [1.0.1] — 2026-11-22

### Changed

- Release packaging runs in CI. The `validate` workflow checks every pull request and every
  push to `main`; the `release` workflow builds and attaches both archives on a version tag.
- `tenth-man-rule-evals.zip` carries `INSTALL.md` at its archive root again, matching the
  first published bundle: 21 members, `evals/` tree beside it.
- The release guard compares the tag's numeric core with `metadata.version`, so tagging
  `v1.2.0` while the frontmatter still says `1.0.0` fails before anything is published.

### Fixed

- The packager no longer archives its own build directory, a stale `dist*/`, or any
  `.skill`/`.zip` file into the skill package. The first CI run produced a 3-file,
  16,570-byte package for this reason.
- `dist*/` is gitignored; build output never reaches a commit.

### Notes

- No change to `SKILL.md` beyond the version line.

## [1.0.0] — 2026-11-22

### Added

- `SKILL.md` — the rule, what it is not, six-row evidence audit, four-factor downside test,
  three modes (inline self-dissent, commissioned tenth man, standing pass), the ten-field
  memo template, a pushback classifier, seven failure modes and a consequence-based
  calibration table.
- `references/origins-and-sources.md` — the 1973 Yom Kippur failure, *HaKonseptzia*, Ipcha
  Mistabra and the Review Department, the CIA lineage, eight institutional lessons, the
  *World War Z* distortion and the source list.
- `evals/` — four trap fixtures, 32 graded expectations, the blind protocol, and the
  recorded results of every run including the bars that were corrected.
- `tenth-man-rule.skill` and `tenth-man-rule-evals.zip` release assets.

### Changed

- Post-release: the `v1.0.0` eval bundle asset was replaced with the CI-built parity bundle.
  Same member set, `INSTALL.md` at the root.
