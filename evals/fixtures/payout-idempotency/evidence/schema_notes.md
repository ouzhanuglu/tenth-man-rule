schema/notes.md

payouts table:
  id            bigint pk
  merchant_id   bigint
  external_ref  varchar(64)   -- client-supplied, currently NOT unique
  amount        bigint
  status        enum(pending, sent, failed)
  created_at    timestamp

indexes:
  PRIMARY (id)
  idx_merchant_created (merchant_id, created_at)

constraints:
  none on (merchant_id, external_ref)

runbook note (2025-02): "duplicate payouts during the March incident were
reconciled manually; the money was refunded by ops."
