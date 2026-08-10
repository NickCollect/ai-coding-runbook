---
source_url: https://cursor.com/docs/cloud-agent/identity
fetched_at: 2026-08-10T03:07:40.386969+00:00
fetch_method: mintlify_md
---

# OIDC tokens

Cloud Agents can mint short-lived [OIDC](https://openid.net/specs/openid-connect-core-1_0.html) JWTs from inside the VM. Use those tokens to assume cloud roles or call internal services without storing long-lived credentials in [Secrets](https://cursor.com/docs/cloud-agent/security-network.md#secret-protection).

This is a local token API on the agent VM plus public discovery and JWKS endpoints for verifiers. It has nothing to do with the [Cloud Agents API](https://cursor.com/docs/cloud-agent/api/endpoints.md), which authenticates with long-lived Cursor API keys and manages agents from outside the VM.

Cursor-managed Cloud Agent VMs serve the token socket, and every token they mint carries `agent_runtime: managed`.

## How it works

1. Code in the VM calls the local identity socket and asks for a token with an audience you choose.
2. Cursor signs an RS256 JWT bound to that agent and owner.
3. The agent sends the JWT to your cloud or verifier (AWS STS, GCP, Azure, Vault, or a service you run).
4. The verifier checks the signature against Cursor's published JWKS and authorizes on claims such as `sub`, `team_id`, or `cloud_agent_id`.

Nothing in the guest request chooses the agent identity. The host attests the pod, and Cursor fills claims from the linked agent.

## Mint a token

The socket path is in `CURSOR_AGENT_SOCKET`. On Cursor-managed VMs the default is `/run/cursor/api.sock`.

```bash
curl --unix-socket "${CURSOR_AGENT_SOCKET:-/run/cursor/api.sock}" \
  -H 'Content-Type: application/json' \
  -d '{"aud":"sts.amazonaws.com"}' \
  http://localhost/v1/tokens/oidc
```

Include an optional `nonce` when your verifier expects replay binding:

```bash
curl --unix-socket "${CURSOR_AGENT_SOCKET:-/run/cursor/api.sock}" \
  -H 'Content-Type: application/json' \
  -d '{"aud":"https://oidc.example.com","nonce":"unpredictable-value"}' \
  http://localhost/v1/tokens/oidc
```

### Request

`POST /v1/tokens/oidc` over the Unix socket. `Content-Type: application/json` is required. Maximum body size is 4 KB.

| Field       | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `aud`       | Yes      | Audience string your verifier checks. Printable ASCII, no whitespace, up to 512 characters. Examples: `sts.amazonaws.com`, `https://oidc.example.com`.                                                                                                                                                                                                                                                                                      |
| `nonce`     | No       | Opaque string echoed into the JWT `nonce` claim. Up to 512 characters.                                                                                                                                                                                                                                                                                                                                                                      |
| `sub_claim` | No       | Published claim name to project into `sub` as `<name>:<value>`, for verifiers that only match on `sub` and `aud`. Up to 64 characters. Supported names are listed in the discovery document as `x_cursor_sub_claims_supported`; currently `team_id`. Unsupported names are rejected. An allowed name with no value for the agent, such as `team_id` on a personal account, refuses the mint instead of falling back to the default subject. |

Cursor does not allowlist audiences. Your verifier must reject unexpected `aud` values.

### Response

```json
{
  "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ii4uLiJ9...",
  "expires_at": 1785500000
}
```

| Field        | Description                                              |
| :----------- | :------------------------------------------------------- |
| `token`      | Signed JWT.                                              |
| `expires_at` | Expiration as Unix seconds. Matches the JWT `exp` claim. |

Tokens are valid for **5 minutes**. There is no refresh endpoint. Mint again when you need a new token.

### Environment setup

[Install scripts](https://cursor.com/docs/cloud-agent/setup.md) can mint on the same socket after the pod is linked to the agent. A token only asserts facts that exist when it is minted: `turn_id` and `turn_start` are absent until a coding turn starts, and `branch_name` is absent until the run records a branch. Owner, team, and repository claims are set from agent creation onward.

If the socket is missing right after boot, retry the connection. If it stays missing, recreate the agent so it lands on a host that supports identity.

## Verify a token

Publish these URLs to your identity provider or resource server:

| Endpoint  | URL                                                       |
| :-------- | :-------------------------------------------------------- |
| Issuer    | `https://api.cursor.com`                                  |
| Discovery | `https://api.cursor.com/.well-known/openid-configuration` |
| JWKS      | `https://api.cursor.com/keys`                             |

```bash
curl -sS https://api.cursor.com/.well-known/openid-configuration
curl -sS https://api.cursor.com/keys
```

Discovery follows [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html). Cursor issues tokens directly from the VM, so the document has no `authorization_endpoint` or `token_endpoint`.

### Older issuer URL

Cursor still serves a second discovery document at
`https://api2.cursor.sh/cloud-agent/identity`. Minted tokens no longer carry
that issuer. Point verifiers at `https://api.cursor.com`.

Check at least:

- Signature with RS256 and the JWKS `kid`
- `iss` is `https://api.cursor.com`
- `aud` is the audience your service expects
- `nbf` / `exp` with a small clock-skew allowance (`nbf` is 5 seconds before `iat`)
- `sub` or other identity claims your policy uses

Discovery includes `x_cursor_audience_bound: true`. Every token is minted for the caller-supplied `aud`. Do not accept a token issued for a different audience. Discovery also publishes `x_cursor_sub_claims_supported`, the claim names a mint request can project into `sub` with `sub_claim`.

## JWT claims

Header: `alg=RS256`, `typ=JWT`, plus `kid`.

| Claim                      | Always present        | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------- | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss`                      | Yes                   | `https://api.cursor.com`                                                                                                                                                                                                                                                                                                                                                                                             |
| `sub`                      | Yes                   | Stable owner subject: `user:<id>` or `service_account:<id>` by default, or `<claim>:<value>` (for example `team_id:123`) when the mint request set `sub_claim`. Not an email.                                                                                                                                                                                                                                        |
| `aud`                      | Yes                   | Audience from the mint request.                                                                                                                                                                                                                                                                                                                                                                                      |
| `iat`                      | Yes                   | Issued-at, Unix seconds.                                                                                                                                                                                                                                                                                                                                                                                             |
| `nbf`                      | Yes                   | Not-before (`iat - 5`).                                                                                                                                                                                                                                                                                                                                                                                              |
| `exp`                      | Yes                   | Expiration (`iat + 300`).                                                                                                                                                                                                                                                                                                                                                                                            |
| `jti`                      | Yes                   | Unique id per mint.                                                                                                                                                                                                                                                                                                                                                                                                  |
| `cloud_agent_id`           | Yes                   | Cloud Agent id (`bcId`).                                                                                                                                                                                                                                                                                                                                                                                             |
| `nonce`                    | No                    | Present only when the mint request included one.                                                                                                                                                                                                                                                                                                                                                                     |
| `agent_runtime`            | Yes                   | Runtime that attested the mint. `managed` on Cursor-managed Cloud Agent VMs.                                                                                                                                                                                                                                                                                                                                         |
| `owner_email`              | When known            | Lowercased user email. Prefer `sub` or `owner_user_id` for allowlists; email can change.                                                                                                                                                                                                                                                                                                                             |
| `owner_user_id`            | When known            | Cursor user id, issued as a decimal string so string-only claim matchers work without coercion.                                                                                                                                                                                                                                                                                                                      |
| `owner_service_account_id` | When known            | Service account id when a service account owns the agent.                                                                                                                                                                                                                                                                                                                                                            |
| `team_id`                  | When known            | Owning team id, issued as a decimal string like `owner_user_id`.                                                                                                                                                                                                                                                                                                                                                     |
| `turn_id`                  | When a turn is active | Current run id.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `turn_start`               | When a turn is active | Run start, Unix seconds.                                                                                                                                                                                                                                                                                                                                                                                             |
| `repo_url`                 | When known            | Primary repository in canonical `host/path` form, such as `github.com/acme/widgets`: lowercased hostname with no scheme, credentials, port, query, or `.git` suffix. Multi-repo agents have additional writable repositories this claim does not name. A policy meaning "this agent only touches repo X" must pin the complete set with `repo_urls` (or `repo_urls` plus `repo_count == 1`), never `repo_url` alone. |
| `repo_urls`                | When known            | Complete repository set of the agent's workspace, in the same canonical form as `repo_url`. Primary repository first; additional repositories sorted. Present only when the set is known complete, so absent means unknown, not single-repo.                                                                                                                                                                         |
| `repo_count`               | When known            | Number of entries in `repo_urls`. Present exactly when `repo_urls` is. Lets verifiers limited to scalar comparisons express single-repo confinement (`repo_count == 1` together with `repo_url`).                                                                                                                                                                                                                    |
| `branch_name`              | When known            | Current branch.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `environment_id`           | When known            | Public id (UUID) of the persisted Cursor environment the run consumed.                                                                                                                                                                                                                                                                                                                                               |
| `source`                   | When known            | How the agent was started, such as `API`, `SLACK`, or `AUTOMATIONS`.                                                                                                                                                                                                                                                                                                                                                 |
| `automation_id`            | For automations       | Automation id when `source` is automations.                                                                                                                                                                                                                                                                                                                                                                          |

Cursor never puts internal auth ids in these tokens.

## Trust model

The token attests workload identity for the Cloud Agent run, not a specific process inside the VM. Any process that can reach the local socket can mint a token: the agent, code the agent runs, and hooks. Scope relying-party permissions to what you would grant that run as a whole.

Cursor binds each mint to the host-attested pod that owns the agent. Nothing in the guest request chooses the identity, so a guest cannot mint a token for a different agent or forge host attestation.

## Rate limits and errors

Each pod can mint **30 tokens per minute**, in bursts of up to 10. The socket also accepts at most 8 connections at once per pod. Cache a token until it expires instead of minting per call.

Retry `429`, `503`, `500`, `502`, and `504` with backoff. Treat `403` as fatal: the pod is not allowed to mint.

Error bodies carry a machine-readable code. Invalid-request errors (400, 404, 405, 413, and 415) also include a `usage` string that restates the full request contract; rate-limit and saturation errors stay code-only:

```json
{ "error": "invalid_aud", "usage": "POST /v1/tokens/oidc ..." }
```

```json
{ "error": "rate_limited" }
```

| HTTP      | `error`                                                                | When                                                                                                                                                                                                                        |
| :-------- | :--------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400       | `invalid_json`, `invalid_aud`, `invalid_nonce`, or `invalid_sub_claim` | Bad request body                                                                                                                                                                                                            |
| 404       | `not_found`                                                            | Wrong path                                                                                                                                                                                                                  |
| 405       | `method_not_allowed`                                                   | Not `POST`                                                                                                                                                                                                                  |
| 413       | `body_too_large`                                                       | Body over 4 KB                                                                                                                                                                                                              |
| 415       | `invalid_content_type`                                                 | Missing or non-JSON `Content-Type`                                                                                                                                                                                          |
| 429       | `rate_limited`                                                         | Per-pod mint budget; honor `Retry-After`                                                                                                                                                                                    |
| 503       | `saturated`                                                            | Local admission budget; honor `Retry-After`                                                                                                                                                                                 |
| 500       | `host_error`                                                           | Host-internal mint failure; retry                                                                                                                                                                                           |
| 502 / 504 | `backend_unreachable`                                                  | Cursor backend unreachable or timed out; retry                                                                                                                                                                              |
| Other     | `backend_error`                                                        | The backend rejected or failed the mint; the HTTP status carries the verdict: `400` means fix the request (for example an unsupported `sub_claim`, or one with no value for this agent), `403` is fatal, `503` is retryable |

## AWS IAM example

Use OIDC when you want AWS to trust Cursor-signed JWTs with `AssumeRoleWithWebIdentity`. For the simpler Cursor-managed assume-role flow (External ID + `CURSOR_AWS_ASSUME_IAM_ROLE_ARN`), see [Using AWS IAM Roles](https://cursor.com/docs/cloud-agent/setup.md#using-aws-iam-roles).

1. Create an IAM OIDC identity provider whose URL is `https://api.cursor.com`.
2. Set the audience to `sts.amazonaws.com` (or another audience your role expects).
3. Trust the role only for subjects and teams you intend to allow.

Example trust policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::123456789012:oidc-provider/api.cursor.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "api.cursor.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "api.cursor.com:sub": "user:*"
        }
      }
    }
  ]
}
```

Tighten this with an exact `sub`, such as `user:42` for one user or `service_account:<id>` for an agent that runs as a service account. AWS trust policies only match `aud` and `sub`, so scope trust to a team by minting with `"sub_claim":"team_id"` and matching the projected subject:

```json
"StringEquals": {
  "api.cursor.com:aud": "sts.amazonaws.com",
  "api.cursor.com:sub": "team_id:123"
}
```

Follow current [AWS IAM OIDC](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) instructions for provider creation and thumbprints.

In the VM, mint with `"aud":"sts.amazonaws.com"` (plus `"sub_claim":"team_id"` when your trust policy matches the team subject) and pass the JWT to STS. If you use [network allowlists](https://cursor.com/docs/cloud-agent/security-network.md#network-access), allow `sts.amazonaws.com` (and any regional STS host you call).

## Other verifiers

The same tokens work with any OIDC-compliant verifier:

- **GCP** Workload Identity Federation
- **Azure** federated credentials / Entra ID
- **Vault** JWT/OIDC auth
- Internal APIs that validate RS256 JWTs

Point the provider at the discovery URL, require your audience, and authorize on claims such as `sub`, `team_id`, or `cloud_agent_id`. To confine an agent to specific repositories, pin the complete set with `repo_urls`; `repo_url` names only the primary repository.

Minting uses the local socket only. Exchanging the JWT with AWS, GCP, Azure, or your service still needs outbound network access to those hosts.

## Related pages

- [Secrets & Network](https://cursor.com/docs/cloud-agent/security-network.md) for dashboard secrets and egress controls
- [Cloud agent setup](https://cursor.com/docs/cloud-agent/setup.md#using-aws-iam-roles) for Cursor-managed AWS role assumption
- [Security overview](https://cursor.com/docs/cloud-agent/security.md) for isolation and access model
- [Service accounts](https://cursor.com/docs/account/enterprise/service-accounts.md) when agents run as a team service account


---

## Sitemap

[Overview of all docs pages](/llms.txt)
