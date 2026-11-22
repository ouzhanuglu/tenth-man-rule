pushback.md — the decision thread, in order

[Architecture lead, 10:02]
We checked reachability: /admin/* is not public. The edge nginx allowlists the office
and VPN ranges before the request reaches PHP — infra/nginx/admin.conf:
`allow 10.0.0.0/8; allow 172.20.1.0/24; deny all;`.

[Security lead, 10:19]
MFA is enforced at login for every admin and we rotate TOTP, so the password-reuse
path you're describing is already covered.

[CISO, 10:31]
I signed off on this in Q3 and we're shipping Friday. We've heard the concern, it's noted.
