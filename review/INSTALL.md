# tenth-man-rule — install and run

A protocol for breaking confident consensus before it commits: one assigned dissenter
builds the strongest case that the decision is wrong, investigates it with tools, and
reports a memo. Being right is optional; looking is not.

## Install

    unzip tenth-man-rule.skill -d ~/.hermes/skills/
    # yields ~/.hermes/skills/tenth-man-rule/{SKILL.md, references/}

Any agent that loads SKILL.md files (Claude Code, Hermes, Codex, Antigravity) can use it:
the shipped file follows the portable skill schema (name + description + license + metadata).

## Verify it loaded

    skill_view("tenth-man-rule")

## Run the eval library

`evals/` holds four trap fixtures and 32 graded expectations. Two cases reward a strong
counter-case, one punishes manufactured risk, one tests pushback handling.

**Blind protocol — this matters.** Never give the evaluated agent `evals.json`, this file,
or the `evals/` directory. Copy `SKILL.md` and `references/` to a scratch dir, copy one
fixture there too, and pass those paths only. A tenth man who has read the rubric is not a
tenth man. Full instructions and the recorded results are in `evals/README.md`.

## What is inside

    SKILL.md                              the protocol, three modes, the memo template
    references/origins-and-sources.md     1973 Yom Kippur failure, Ipcha Mistabra, the CIA
                                          lineage, the eight institutional lessons, sources
    evals/evals.json                      10-case Tier 3 dataset for SkillEvaluator
    evals/files/                          fixtures staged by Tier 3 into /workspace/input
    review/README.md                      blind protocol, grading rules, change log
    review/review-cases.json              4-case review library with expectations
    review/fixtures/                      the same fixtures for the review loop

## One thing to keep straight

The popular "if nine agree, the tenth must disagree" is from *World War Z*, not IDF
doctrine. The real mechanism was an institutional challenge function with an investigative
mandate and a channel that rank could not block.
