# Consensus memo — dashboard reads to the eu-central replica

**Decision:** move all merchant-dashboard read traffic from the primary to the new eu-central read replica. Ship Friday.

**Confidence:** high (~85%).

**Evidence:**
1. Dashboard p95 read latency on the primary is 40 ms; the replica measures 12 ms for the 70% of merchants in that region.
2. Replication lag is small: p99 20 ms across 90 days of monitoring.
3. Replica promotion drill runs monthly and passed 11 of 11 times.

**Assessment:** latency win with no meaningful consistency cost. Balance screen already pins to the primary, so read-after-write is unaffected.
