export_endpoint.md

GET /admin/exports/merchants.csv
  rows: 50,000
  fields: merchant_id, legal_name, tax_no, iban, contact_email, contact_phone
  rate limit: none
  audit log: one row per request with the admin id; no row count, no client IP
  response: streamed, 40-90 s for a full export
  caching: none
  writes: none
