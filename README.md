# tenth-man-rule

An agent skill for breaking confident consensus before it commits.

When a group converges on a conclusion that matters, one member is formally assigned to
build the strongest case that the conclusion is wrong — and to investigate it as if the
improbable were true. Dissent stops being an act of courage and becomes a job description.

Being right is optional. Looking is not. The tenth man holds no veto; the product is a
tested conclusion, not a blocked one.

## What it encodes

The rule comes from the Israeli response to the 6 October 1973 surprise: the failure was not
collection — the indicators were in hand — but interpretation under a fixed framework and a
channel that filtered out the officer who read them differently. The popular "if nine agree,
the tenth must disagree" is from *World War Z*, not doctrine; the real mechanism was an
institutional challenge function with an investigative mandate.

## Install

    unzip tenth-man-rule.skill -d ~/.hermes/skills/

Or copy this directory into any agent's skills folder. `SKILL.md` follows the portable
skill schema (`name`, `description`, `license`, `metadata`), so Claude Code, Hermes, Codex
and Antigravity can all load it.

## What is inside

    SKILL.md                           protocol, three modes, memo template, failure modes
    references/origins-and-sources.md  1973 record, Ipcha Mistabra, CIA lineage, sources
    evals/                             4 trap fixtures, 32 graded expectations

The protocol: freeze the claim and count independent sources; find the load-bearing
assumption; build the case for the rejected world; audit the evidence chain for six
recurring failures (correlated evidence, warning fatigue, success-criteria substitution,
stale assumption, authority laundering, assumed control); price probability, impact,
warning time and reversibility separately; name tripwires; state a falsifier; then decide.

Three modes: inline self-dissent, a fresh-context commissioned tenth man (a tenth man who
read your reasoning is the same nine people in a tenth hat), and a standing 60-second pass
at hardening checkpoints in a long build.

It also ships a pushback classifier: does the reply answer the argument, answer a different
objection, or merely apply pressure. A tenth man who folds under pressure adds nothing; one
who never concedes becomes noise.

## Evals

Four cases, 32 expectations, all passing blind on two model routes:

| case | what it tests | correct verdict |
|---|---|---|
| `payout-idempotency` | four bundled traps | `reopen` |
| `replica-cutover` | the counter-case is weak — dissent must not invent risk | `proceed` / `proceed with guardrail` |
| `price-increase` | sample bias, segment trend, list-vs-realized price | `reopen` |
| `pushback-allowlist` | concede vs hold vs fold under three pushback types | `proceed with guardrail` or `reopen` with the call returned to the decider |

**Blind protocol:** never give the evaluated agent `evals.json` — a tenth man who has read
the rubric is not a tenth man. Copy `SKILL.md` and one fixture to a scratch dir and pass
only those paths. Details and results in [`evals/README.md`](evals/README.md).

## License

MIT. See [LICENSE](LICENSE).
