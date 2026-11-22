gateway_policy.md

retry:
  on_status: [502, 503, 504]
  attempts: 3
  backoff: 200ms, 900ms
  payload: identical bytes resent
  idempotency_header: NOT forwarded (stripped at edge, added 2024-06, never re-enabled)

timeouts:
  upstream_read_timeout: 30s
  on_timeout: request is replayed once to the same upstream by the edge worker

edge_timeout_sink:
  retention: 7 days
  fields: [trace_id, path, attempt, ts]

cli_versions_30d.txt (mobile telemetry, distinct installs):
  3.6.x: 61%
  3.5.x: 17%
  3.4.x: 22%   <- double-tap suppression ships only in >= 3.5
