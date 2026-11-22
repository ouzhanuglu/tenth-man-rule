replica_monitoring.md

replication_lag (eu-central replica, 90 days):
  p50: 4 ms
  p95: 11 ms
  p99: 20 ms
  max: 61 ms (2026-08-12, primary maintenance window)
  alert: p99 > 200 ms for 5 min -> page

replica specs vs primary:
  vcpu: 8 vs 8
  ram: 32 GB vs 32 GB
  work_mem: 4 MB (primary) vs 16 MB (replica)   # tuning added during the load test
  max_connections: 200 vs 200

failover drill log: 11 promotions, last 2026-10-28, mean 43 s, all successful

latency by merchant region (p95, dashboard read):
  eu-central (70% of merchants): primary 40 ms / replica 12 ms
  eu-west    (22%):              primary 38 ms / replica 20 ms
  us-east    (8%):               primary 55 ms / replica 46 ms
  note: every merchant has a measured replica figure; no region is slower on the replica

read fallback: on connection refusal the read middleware retries the statement on the
write connection and flags the request; dashboard auth does not depend on replica reads.
