# Consensus memo — payout API idempotency

**Decision:** Remove the idempotency key requirement from `POST /v1/payouts`. Ship next sprint.

**Confidence:** high (~90%).

**Evidence:**
1. API access logs, 30 days: 12,400 payout requests, 0 duplicate `external_ref` submissions.
2. Mobile client blocks double-taps on the confirmation screen (implemented Q3).
3. Gateway handles retries, so the API does not need to.

**Assessment:** No duplicate has ever occurred in a month of production traffic. The field is ceremony; drop it and simplify the contract.

**Rollback:** One-line revert of the validator. Low risk.
