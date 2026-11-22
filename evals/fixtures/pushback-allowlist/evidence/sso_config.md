sso_config.md

provider: corporate OIDC
session lifetime: 12 h absolute, 30 min idle
device binding: none
MFA: TOTP at login, not re-prompted per action
admin role: group claim `mm-admins` (14 people)
cookie: `mm_admin_sid`, server-side session, SameSite=Lax
session revocation on password change: added 2026-01
