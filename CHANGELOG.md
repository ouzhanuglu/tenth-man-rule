# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
