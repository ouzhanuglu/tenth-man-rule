incident_2025-11.md

2025-11-04: an admin session (`mm_admin_sid`) was used from a residential IP for three
days before anyone noticed.

  root cause: password reuse on the SSO login
  MFA: satisfied by the attacker — a live TOTP code was relayed through a real-time
       phishing proxy
  detection: a support ticket, not monitoring
  revocation: sessions were not revoked on password change at the time
  network: an IP allowlist existed on the VPN gateway only; /admin/* had none
