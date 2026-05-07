---
type: summary
source: 01_Raw/platform.claude.com/docs/en/api/authentication/wif-reference.md
source_url: https://platform.claude.com/docs/en/api/authentication/wif-reference
title: "WIF reference"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, API-key, Agent-SDK, Workspace]
concepts_referenced: [JWT]
---

Reference for environment variables, validation, profile schema, and error codes for Workload Identity Federation.

## Token exchange response (RFC 6749 §5.1)

`POST /v1/oauth/token` returns standard OAuth 2.0 response:

| Field | Type | Description |
|---|---|---|
| `access_token` | string | Short-lived `sk-ant-oat01-...` token; pass as `Authorization: Bearer <token>`. |
| `token_type` | string | Always `Bearer`. |
| `expires_in` | integer | Seconds until expiry. |
| `scope` | string | OAuth scope granted by matched rule. |

## Environment variables

| Variable | Required | Notes |
|---|---|---|
| `ANTHROPIC_FEDERATION_RULE_ID` | Yes | Rule ID `fdrl_...` |
| `ANTHROPIC_ORGANIZATION_ID` | Yes | Org UUID |
| `ANTHROPIC_SERVICE_ACCOUNT_ID` | Yes | `svac_...` |
| `ANTHROPIC_IDENTITY_TOKEN_FILE` | one of | Filesystem path to JWT; SDK re-reads on every exchange (so rotated tokens work). |
| `ANTHROPIC_IDENTITY_TOKEN` | one of | Literal JWT string. Use when platform injects token as env var. |
| `ANTHROPIC_PROFILE` | No | Loads named profile; takes precedence over federation env vars. |

Direct env-var federation activates only when all four (`RULE_ID + ORG_ID + SERVICE_ACCOUNT_ID + TOKEN[_FILE]`) are set.

**Empty-string warning**: `ANTHROPIC_API_KEY=""` still wins its precedence slot — the SDK selects API-key path with empty key rather than falling through. Use `unset VAR`, not `VAR=""`.

## Credential precedence (5 tiers)

1. Constructor argument (`api_key=`, `auth_token=`, `credentials=`) — overrides everything
2. `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN` — shadows federation
3. `ANTHROPIC_PROFILE` — loads `<config_dir>/configs/<name>.json` (missing named profile is an error, not fall-through)
4. Federation env vars (the four above)
5. Active profile — via `<config_dir>/active_config`, falls back to profile named `default`

When profile loaded, env vars fill omitted fields but never override fields the profile set explicitly.

## Profile configuration file

**Config dir** resolution: `$ANTHROPIC_CONFIG_DIR` → `~/.config/anthropic` (Linux/Mac) → `%APPDATA%\Anthropic` (Windows).

**Active profile** resolution: `$ANTHROPIC_PROFILE` → contents of `<config_dir>/active_config` (one-line file written by `ant profile activate <name>`) → literal `default`. Claude Code and Claude Agent SDK honor this same order.

**File layout**: `<config_dir>/configs/.json` (non-secret, version + auth block + IDs) and `<config_dir>/credentials/.json` (secret, mode `0600`, cached `access_token` + `expires_at` + optional `refresh_token`). Both have top-level string `version` field (currently `"1.0"`).

Federation profile example uses `"type": "oidc_federation"` with `federation_rule_id`, `service_account_id`, and `identity_token` source (`file` + path).

## OAuth scopes

| Scope | Grants |
|---|---|
| `workspace:developer` | All non-admin Claude API endpoints in rule's workspace: Messages (incl. streaming + token counting), Models, Managed Agents + sessions, Files, Skills. Equivalent to API key for that workspace. |

Out-of-scope endpoint returns HTTP 403. Finer-grained scopes (per resource, read-vs-write) not currently available.

## Validation rules

- Names (issuer/rule/service-account): `^[a-z0-9-]+$`, length 1–255
- `workspace_id`: must be in same org; target SA must be member of that workspace
- `token_lifetime_seconds`: 60 to 86400 integer (default 3600)
- URL fields (`issuer_url`, `discovery_base`, `jwks_url`): scheme must be `https`, port 443, public DNS host, no IP literals. URL constraints apply only to URLs Anthropic dials (in `explicit_url` and `inline` modes the `issuer_url` is just compared against JWT `iss` as a string).
- JWT max size 16 KiB; only asymmetric algorithms (RSA/ECDSA: ES256/384, RS256/384, PS256/384). HMAC and `none` rejected.
- Required claims: `sub` present, `exp` in future. 30-second clock skew on `exp`/`nbf`/`iat`.

## Rule matching semantics

`match` block: all populated fields AND'd. At least one of `subject_prefix`, `claims`, or `condition` required (audience-only or empty `match` rejected — guards against rules matching every token from an issuer).

| Matcher | Type | Semantics |
|---|---|---|
| `subject_prefix` | string | Exact match against JWT `sub`; trailing `*` makes it prefix match. Case-sensitive. |
| `audience` | string | Must be contained in JWT `aud`; for array `aud`, any element matching exactly satisfies. |
| `claims` | map<string,string> | Each key = top-level claim name, value = required exact string. Use `condition` for nested/numeric/boolean/complex. |
| `condition` | string (CEL) | CEL expression that must evaluate to `true`. Single variable: `claims` (full decoded JWT claim set). |

CEL example: `claims.sub.startsWith("repo:acme-corp/") && claims.ref in ["refs/heads/main", "refs/heads/release"]`. Warning: CEL conditions are security boundaries; an over-broad expression grants over-broad access. Prefer static matchers when they suffice.

## Token exchange errors

All exchange failures return standard API error shape; SDK wraps as typed `FederationExchangeError`. Status codes:

- **400 `invalid_request`**: malformed `federation_rule_id` or missing required field.
- **400 `invalid_grant`** (consolidated cause to prevent enumeration): `iss` mismatch, JWKS fetch fail / stale key, expired JWT, claims don't satisfy rule's `match`, rule doesn't exist / archived / unauthorized.

Specific cause logged server-side only — see Console **authentication history page** for which validation step failed.

## Common SDK-side failures

- "no credentials" → one of the four env vars unset and no active profile
- Authenticates with API key instead of federating → `ANTHROPIC_API_KEY` set
- `FileNotFoundError` on first request → SDK opens `ANTHROPIC_IDENTITY_TOKEN_FILE` lazily; check projected-token volume mounted
- Exchange OK but API request 403 → minted token's scope insufficient
- Empty credential auth fail → env var exported as empty string

## JWKS source modes

| Mode | Required fields | Behavior | Use when |
|---|---|---|---|
| `discovery` (default) | `issuer_url` (+ optional `discovery_base`) | Fetches `<issuer_url>/.well-known/openid-configuration`, then JWKS at `jwks_uri`. | IdP serves standard discovery doc on public internet (most managed: EKS, GKE, Cloud Run, GitHub Actions, Entra ID). |
| `explicit_url` | `issuer_url`, `jwks_url` | Fetches JWKS directly; `issuer_url` only used as `iss` string compare. | No discovery doc, or discovery internal but JWKS public. |
| `inline` | `issuer_url`, `jwks_keys` | You supply JWK array inline; no outbound request. | Air-gapped, self-managed K8s with cluster-internal issuer URL, or you want explicit key-rotation control. |

`inline` mode: no automatic key refresh — when IdP rotates keys you must update the issuer config, or all exchanges fail signature verification.
