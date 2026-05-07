---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/workload-identity-federation.md
source_url: https://platform.claude.com/docs/en/build-with-claude/workload-identity-federation
title: "Workload Identity Federation"
summarized_at: 2026-05-07
entities_referenced: [Workload-Identity-Federation, Service-account, Federation-issuer, Federation-rule, API-key, Workspace, Messages-API]
concepts_referenced: [JWT]
---

Workload Identity Federation (WIF) lets workloads authenticate to the Claude API with short-lived OIDC tokens from an IdP they already operate (AWS IAM, Google Cloud, Azure Entra ID, GitHub Actions, Kubernetes, Okta), instead of long-lived `sk-ant-...` API keys. The minted access token is prefixed `sk-ant-oat01-...`.

## Three configured resources (in Claude Console → Settings → Workload identity)

- **Service account** (`svac_...`): non-human identity inside the org that the federated token acts as. Lives at org level, becomes active in a workspace via that workspace's Members page. No email, password, or Console login.
- **Federation issuer** (`fdis_...`): registers an OIDC IdP. Two configs: `issuer_url` (exact `iss` claim value) and `jwks_source` — `discovery` (default), `explicit_url`, or `inline`. Issuer/JWKS URLs must be `https`, port 443, public DNS, no IP literals (constraint applies only to URLs Anthropic dials).
- **Federation rule** (`fdrl_...`): bridges issuer → service account. Has `match` (any of `subject_prefix`, `audience`, exact `claims`, CEL `condition`; at least one of subject/claims/condition required, all populated matchers AND'd), `target` (the service account), and `authorization` (OAuth `scope` — at launch always `workspace:developer`; `token_lifetime_seconds` 60–86400, default 3600). Rules selected by ID, not searched.

## Token exchange flow

1. IdP issues JWT to workload (ambient on most platforms: K8s projected SA token, GCP metadata server, Azure IMDS, GitHub Actions OIDC endpoint).
2. SDK posts JWT to `POST /v1/oauth/token` using RFC 7523 `jwt-bearer` grant with `federation_rule_id`, `organization_id`, `service_account_id`. Anthropic verifies signature against JWKS, checks `exp`/`nbf`/`iat`, matches claims against rule. Returns standard OAuth 2.0 response with `access_token`, `expires_in`, etc.
3. SDK sends token as `Authorization: Bearer ...` and refreshes before expiry.

## SDK env vars (zero-arg client form)

`ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_IDENTITY_TOKEN_FILE` (or `ANTHROPIC_IDENTITY_TOKEN`). All four required for direct env-var federation.

## Credential precedence (5 tiers)

Constructor args → `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN` → explicit `ANTHROPIC_PROFILE` → federation env vars → active profile. **A leftover `ANTHROPIC_API_KEY` silently shadows federation** — biggest migration gotcha. `ant auth status` reports which source won.

## Token refresh (botocore-modeled)

- **Advisory**: expiry minus 120s. Failed refresh → continue serving cached token.
- **Mandatory**: expiry minus 30s. Failed refresh → raise error.
- Token lifetime = lesser of rule's `token_lifetime_seconds` and 2× remaining JWT lifetime, with 60s floor (prevents minted token outliving upstream identity).
- SDK re-reads `ANTHROPIC_IDENTITY_TOKEN_FILE` on every exchange (transparently picks up rotated K8s SA tokens).

## Migrate from API keys

1. Configure federation in parallel, leaving `ANTHROPIC_API_KEY` set.
2. `ant auth status` to confirm key still wins.
3. Unset `ANTHROPIC_API_KEY` everywhere (CI secrets, container env, shell profiles); confirm federation wins.
4. Revoke key in Console.

## Identity providers covered

AWS, Google Cloud, Azure, GitHub Actions, Kubernetes, Okta — each has dedicated provider guide. Console has presets for AWS and GCP plus a generic OIDC option.

## Security note

WIF removes static credentials from Anthropic's surface but is "not a complete security story on its own" — federated auth is only as strong as the upstream IdP. Pair with workload identity binding, conditional access, audit logging.
