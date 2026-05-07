---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/wif-providers/okta.md
source_url: https://platform.claude.com/docs/en/build-with-claude/wif-providers/okta
title: "Use WIF with Okta"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, Workspace]
concepts_referenced: [JWT]
---

Okta acts as workload IdP by issuing OIDC access tokens to a **service application** via OAuth 2.0 `client_credentials` grant. Workload authenticates to Okta (typically with `private_key_jwt` — no shared secret), receives signed JWT, exchanges with Anthropic.

Okta authorization server URL: `https://<your-domain>.okta.com/oauth2/<auth-server-id>` (built-in default uses `/oauth2/default`).

**Must use a custom authorization server** (incl. the `default` one). Tokens from Okta org auth server (`/oauth2/v1/token` with no auth-server ID) cannot be validated externally — Okta does not publish signing keys for them.

## Prerequisites

- Okta org with **API Access Management** enabled (required for custom auth servers).
- Workload that can request token from Okta `/v1/token` endpoint and reach `api.anthropic.com`.

## Configure Okta (high level)

1. Create **API Services** (OIDC machine-to-machine) app integration. Note **Client ID**.
2. Configure client auth: **Public key / Private key** (`private_key_jwt`) recommended; register workload's public JWK. (Alternative: client secret if env can store securely.) For example may need to disable DPoP requirement; ensure prod adheres to org security.
3. Set audience on custom auth server to `https://api.anthropic.com` (Anthropic validates `aud` against this fixed value).
4. Grant a scope (e.g., `anthropic.access`) — Okta rejects `client_credentials` requests without granted scope.
5. Create access policy with rule allowing service app to request the scope.
6. (Optional) Add custom claims via auth server's **Claims** tab if matching on something other than client ID.

For service apps using `client_credentials`, Okta sets `sub` = app's Client ID, `iss` = auth server's issuer URL.

## Configure Anthropic

- **Issuer**: Okta custom auth server URL with `discovery` mode. Anthropic reads `.well-known/openid-configuration` and fetches JWKS from advertised `jwks_uri`.
- **Rule**: match `subject_prefix` = service app's Client ID, `audience: https://api.anthropic.com`. Match on custom claims via `claims` map / CEL if needed.

## Acquisition

Unlike platform-native providers (AWS/GCP/K8s) where token is ambient, Okta requires the workload to **call Okta's `/v1/token` endpoint**:

```bash
curl "https://acme.okta.com/oauth2/aus.../v1/token" \
  -d grant_type=client_credentials \
  -d scope=anthropic.access \
  -d client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer \
  --data-urlencode client_assertion="$SIGNED_CLIENT_ASSERTION"
```

Pass returned JWT to Anthropic SDK as identity token. SDK re-invokes the Okta fetcher whenever Anthropic access token approaches expiry — fetcher must return fresh token, not cache one indefinitely. CLI re-reads `ANTHROPIC_IDENTITY_TOKEN_FILE` on each exchange — refresh on a timer for long-running shells.

## Verification + scope hardening

- Most common Okta failure: `issuer_url` mismatch — must include `/oauth2/<auth-server-id>` path; org auth server not usable.
- Scope: pin exact Client ID (no trailing `*`); pin audience; match on custom claims for finer scoping; one rule per service app.
