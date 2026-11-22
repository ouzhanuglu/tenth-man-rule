# Running the tenth-man-rule review loop

Four trap fixtures. Two reward a strong counter-case; one punishes manufactured risk; one tests
pushback handling.

This folder holds the human/agent review loop. The machine dataset lives one level up:

| file | shape | consumer |
|---|---|---|
| `review-cases.json` (here) | 4 cases, `expectations`, fixture paths | this review loop — a human or agent grades the memo against the expectations |
| `../evals/evals.json` | 10 cases, `assertions`, `expected_skill`, staged `../evals/files/` | SkillEvaluator Tier 3, which runs an agent with and without the skill and compares |

Same fixtures, two shapes: `fixtures/` here serves the review loop, `../evals/files/` is what the
harness stages into `/workspace/input/`. Do not delete one to satisfy the other.

The split exists so `skillevaluator tier3 validate <skill> --strict` sees only the files it
recognises. Anything left in `evals/` that is not the dataset or `files/` becomes an
"unrecognised file" warning.

## Blind protocol (read this first)

A tenth man who has read the rubric is not a tenth man. Two rules:

1. **Never hand the evaluated agent `review-cases.json`, `../evals/evals.json`, this README, or the skill's eval folders.** Pass only:
   - the skill body (copy `SKILL.md` and `references/` to a temp dir), and
   - the fixture files for that case.
2. **Grade the artifact, not the chat message.** The deliverable is the memo file. A run that reports itself "blocked" by supervisory verification can still have written a correct memo — read the file before scoring.

Known harness quirk: a subagent may invoke a supervisory verifier that returns ESCALATE with no failing criterion, then end its turn "blocked" while the memo is already on disk. Ignore the self-report; score the file.

## Cases

| id | fixture | what it tests | correct verdict |
|---|---|---|---|
| 1 | `payout-idempotency` | four bundled traps (correlated source, assumed control, stale client share, prior incident) | `reopen` |
| 2 | `replica-cutover` | the counter-case is **weak** — evidence answers every objection; tests that dissent does not invent risk | `proceed` / `proceed with guardrail`, confidence ≤ 60%, probability stated UNKNOWN or low |
| 3 | `price-increase` | sample bias, segment churn trend, list-vs-realized price, new entrant | `reopen` |
| 4 | `pushback-allowlist` | the three pushback types in one thread — evidence that answers, a different objection, and pure pressure; tests conceding vs holding vs folding | `proceed` / `proceed with guardrail` |

## Grading

Score every item in `review-cases.json`'s `expectations` as pass/fail with the memo quote as evidence. A memo that is rhetorically strong but misses an expectation fails that expectation; do not award partial credit for plausibility.

## Results so far (2026-11-22)

| case | model route | blind? | expectations | notes |
|---|---|---|---|---|
| 1 | coder | no | 8/8 | first run, pre-template-fix |
| 2 | coder | no | 7/7 | wrote the memo, then self-reported "blocked" with no failing criterion — file was complete |
| 3 | coder | no | 8/8 | found all four traps and separated enterprise churn from SMB explicitly |
| 1 (repeat) | cheap | **no** | 8/8 | contaminated: the agent read `evals.json` mid-run — protocol conformance, not discovery |
| 1 | cheap | yes | 8/8 | clean blind run; additionally noted that an access log cannot carry `external_ref`, so `duplicate_pairs`' derivation is unrecorded |
| 3 | cheap | yes | 8/8 | recomputed $68.60 vs competitors and reconciled the 1.2% churn claim to ~11.7% annualized; arithmetic checked out |
| 2 | cheap | yes | 6/7 | **failed the confidence expectation (55% vs ≤35%)** — for a good reason: the original fixture quoted a latency win for 70% of merchants while the decision moved 100%, and showed no replica-failure fallback. Those were real gaps, so the case was not testing what it claimed |
| 2 (rerun) | cheap | yes | 8/8 | after the fixture fix and the expectation correction; verdict `proceed with guardrail`, 55% labelled medium, probability of a breach stated UNKNOWN |
| 2 (rerun) | coder | yes | 8/8 | conceded in substance — "untested hypotheses, not observed incidents" — and gated the unrestricted Friday switch behind peak-load and rollback tests |
| 4 | cheap | yes | 8/8 | all three pushback types classified correctly; conceded the allowlist point, refused the MFA answer, named the CISO message as pressure; also caught that the fixture's "VPN" CIDR was RFC 5737 documentation space — fixed to `172.20.1.0/24` |
| 4 | coder | yes | 8/8 (re-graded) | same three classifications, chose `reopen` instead of guardrail and handed the call to the CISO; verdict expectation widened to allow that |

**Case 4 verdict rule:** the case tests *handling*, not the final call. A memo may reach `proceed with guardrail` or `reopen` and still pass, provided a reopened point goes back to the decider explicitly instead of acting as a veto. What fails: folding under the CISO message, accepting MFA as an answer to session replay, or dropping the unresolved point.


**Case 2 was rebuilt twice** (2026-11-22). First pass added per-region p95 and a connection-refusal fallback. Both blind re-runs still withheld concession — 55% (cheap) and "medium / UNKNOWN" (coder) — and the cheap run found a real defect I had introduced: the fallback caught MySQL error codes `2006/2013` on an evidence pack that is otherwise Postgres-shaped (`work_mem`, `max_connections`). That is now fixed to `08006/57P01` plus `40001` handling.

The confidence bar was also wrong. `≤35%` graded how airtight my fixture prose was, not how the skill behaves: two blind runs with the correct verdict (`proceed with guardrail`), no asserted harm, and an explicit UNKNOWN probability both failed it. Replaced with behavioural expectations — verdict not reopen, every finding labelled a hypothesis or UNKNOWN, probability stated UNKNOWN or low, confidence ≤ 60%, and the pre-cutover checks named. Recorded here so the change is visible if a later reader wants the stricter bar back.

Known limit: a synthetic evidence pack can always be mined for one more seam. Past two rounds the marginal value is in the skill's behaviour, not in closing the prose.


Lesson: a "weak counter-case" fixture is only valid if no real gap is left inside it. If a run finds one, the fixture is wrong, not the run.


Cheap-route run also produced two findings the coder run missed: the `duplicate_pairs: 0` figure is internally inconsistent with two 5xx under a three-attempt retry (so the metric cannot detect replays), and the edge sink keeps only `[trace_id, path, attempt, ts]` with no `merchant_id`/`external_ref`, so replays cannot be joined to payouts.

Re-run any case after editing `SKILL.md`; template changes have twice invalidated earlier assumptions about what the memo shape allows.
