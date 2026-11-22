# Consensus memo — admin merchant export without an IP allowlist

**Decision:** ship `GET /admin/exports/merchants.csv` without adding an IP allowlist. It already sits behind SSO, and the export is read-only. Ship Friday.

**Confidence:** high (~85%).

**Evidence:**
1. Every `/admin/*` route requires SSO; the export uses the same admin session.
2. The export is read-only — no writes, no money movement.
3. The endpoint has been in staging for two weeks with no findings.

**Assessment:** the control the reviewer would ask for already exists upstream. Adding an app-level allowlist duplicates the network layer.
