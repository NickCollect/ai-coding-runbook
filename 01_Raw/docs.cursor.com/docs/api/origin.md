---
source_url: https://cursor.com/docs/api/origin
fetched_at: 2026-08-24T02:18:38.234299+00:00
title: "Origin API | Cursor Docs"
---

API

# Origin API

Origin is in Early Beta and subject to change. Review the OpenAPI specification when updating an integration.

Origin is Cursor's code forge. Its public REST API lets apps and tools work with Origin repositories, commits, checks, pull requests, and app installations.

- Origin Apps authenticate with app JWTs and installation access tokens. See [Authentication](#authentication).
- View the full [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml) for detailed schemas and examples.
- Agents can load the [llms.txt index](https://cursor.com/docs/api/origin/llms.txt) or the complete reference as Markdown at [llms-full.txt](https://cursor.com/docs/api/origin/llms-full.txt).

## [Overview](#overview)

Origin apps implement an OAuth-style installation consent and GitHub App–style authentication model:

1. The app signs a short-lived EdDSA JWT with its Ed25519 private key.
2. The app exchanges that JWT and an installation ID for a short-lived installation access token (`oit_…`).
3. The installation token calls repository APIs and authenticates Git over HTTPS within the installation's approved repositories and scopes.
4. Origin sends signed webhook deliveries to the app's registered webhook URL.

### [Base URL](#base-url)

```
https://api.cursor.com/v1/origin
```

Endpoint paths in the [reference](#endpoint-reference) include the full `/v1/origin` prefix.

### [Protocol conventions](#protocol-conventions)

Requests and responses use `application/json`. JSON field names are **camelCase**. Timestamps are RFC 3339 strings. Protobuf 64-bit integers, including pull request numbers and version numbers, are encoded as JSON strings.

## [Getting started](#getting-started)

### [Origin access](#origin-access)

- Browse Origin at [cursor.com/codebase](https://cursor.com/codebase).
- Manage app settings at [cursor.com/codebase/settings/apps](https://cursor.com/codebase/settings/apps).
- [Generate an app signing key](#generate-an-app-signing-key) and register only the public key.

### [Origin CLI](#origin-cli)

Install the Origin CLI and sign in:

```
curl -fsSL https://downloads.cursor.com/origin/install.sh | shorigin auth login
```

Clone an existing repository:

```
origin repo clone '{ownerSlug}/{repoName}'# or use git directlygit clone 'https://origin.cursor.com/{ownerSlug}/{repoName}.git'
```

Apps clone using [Git HTTPS authentication](#git-https-authentication) with an installation access token, not a user login.

## [Installation](#installation)

Send a customer workspace admin to:

```
https://cursor.com/codebase/apps/install  ?client_id=APP_ID  &scope=SPACE_SEPARATED_SCOPES  &redirect_uri=REGISTERED_CALLBACK  &state=RANDOM_ANTI_FORGERY_VALUE  &summary=SHORT_REASON_FOR_ACCESS  &include_granted_scopes=true
```

| Parameter | Required | Description |
| --- | --- | --- |
| `client_id` | Yes | Origin App ID. |
| `scope` | Yes | Space-separated scopes. `repository:metadata:read` is added automatically. |
| `redirect_uri` | Yes for partner-initiated installs | Exact registered callback URI. |
| `state` | Strongly recommended | Random anti-forgery value echoed as the `state` claim of the [installation receipt](#installation-receipt). Generate it before redirecting and verify the claim on callback. |
| `summary` | No | Short explanation displayed during consent. |
| `include_granted_scopes` | No | When `true`, retain existing grants and request only additions. |

The workspace admin chooses the target owner, approved scopes, and either all repositories or selected repositories. The customer, not the app, controls repository access.

After approval, Origin redirects to the registered callback:

```
https://ci.example.com/origin/callback?installation_receipt=RECEIPT_JWT
```

Verify the [installation receipt](#installation-receipt), then store the installation ID from its `sub` claim. You need it whenever you mint an installation access token.

Installations use one of two repository-selection modes:

- `all`: the installation can access every repository owned by the selected target.
- `selected`: the installation can access only repositories selected by the workspace admin.

Neither mode covers a repository that Origin mirrors in from GitHub. An installation reaches native Origin repositories and repositories Origin mirrors out to GitHub. A repository mirrored in from GitHub stays outside the installation, so it never appears in `GET /installation/repos`, and a request that names it returns `403`.

Use `GET /installation/repos` with an installation token to discover the repositories available to that installation. App JWT endpoints can list, inspect, and delete the app's installations. Deleting an installation prevents new tokens from being minted.

### [Installation receipt](#installation-receipt)

`installation_receipt` is a short-lived compact JWT signed by Origin. It proves the installation approval came from Origin rather than a forged redirect and carries everything the callback needs. Cursor refuses to redirect without one, so external callbacks always carry it.

JOSE header:

```
{  "alg": "EdDSA",  "kid": "origin-key-id",  "typ": "origin-installation-receipt+jwt"}
```

Claims:

```
{  "iss": "https://api.cursor.com/v1/origin",  "aud": "app_01...",  "sub": "i_01...",  "namespace_id": "ns_01...",  "iat": 1786465200,  "exp": 1786465500,  "jti": "RECEIPT_UUID",  "state": "ORIGINAL_VALUE"}
```

- `aud` is your app ID and `sub` is the installation ID to use when minting installation access tokens.
- `namespace_id` is the stable ID of the namespace the app was installed into.
- Receipts expire five minutes after issuance. `jti` is unique per receipt.
- `state` is present only when the install URL carried a non-empty `state`, and echoes that value. Match it against the anti-forgery value you generated before redirecting.

Verify the receipt before trusting the callback: resolve the signing key from the [JWKS](#discovery-and-signing-keys) by the `kid` header, require `alg` `EdDSA` and `typ` `origin-installation-receipt+jwt`, and validate the signature, `iss`, `aud`, and `exp`. Reject the callback when verification fails.

The receipt is not an installation access token. Never send it as a Bearer credential; mint installation tokens through [Create Installation Access Token](#create-installation-access-token) instead.

## [Authentication](#authentication)

Send REST credentials as Bearer tokens:

```
curl --request GET \  --url https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME \  --header "Authorization: Bearer $ORIGIN_TOKEN"
```

### [Generate an app signing key](#generate-an-app-signing-key)

Origin Apps authenticate with an Ed25519 key pair. Generate the pair locally, then register only the public key at [cursor.com/codebase/settings/apps](https://cursor.com/codebase/settings/apps). An app can hold up to 10 active signing keys.

The private key must stay secret. Do not upload it, paste it into app settings, commit it to a repository, or share it. Store it in a secrets manager. Cursor stores only the public key.

Create a PKCS#8 private key and a PEM SPKI public key with OpenSSL:

```
openssl genpkey -algorithm ED25519 -out origin-app-private.pemopenssl pkey -in origin-app-private.pem -pubout -out origin-app-public.pem
```

The public key file starts with `-----BEGIN PUBLIC KEY-----`. Paste that PEM when you add a signing key. Use the matching private key only to [sign app JWTs](#app-jwt).

### [App JWT](#app-jwt)

Sign a short-lived JWT with the Ed25519 private key paired with one of the app's active signing keys. Generate that pair as described in [Generate an app signing key](#generate-an-app-signing-key).

JOSE header:

```
{  "alg": "EdDSA",  "kid": "app_01...",  "typ": "JWT"}
```

Claims:

```
{  "iss": "app_01...",  "aud": "origin-apps",  "iat": 1782928800,  "exp": 1782929100}
```

Set `iss` and `kid` to the app ID. Use a lifetime of approximately five minutes.

```
Authorization: Bearer APP_JWT
```

Use an app JWT for app-level operations such as reading app metadata, managing installations, minting installation tokens, and recovering webhook deliveries.

### [Installation access token](#installation-access-token)

Call [`POST /app/installations/{installationId}/access_tokens`](#create-installation-access-token) with an app JWT. Installation tokens begin with `oit_`.

```
Authorization: Bearer oit_...
```

The response includes `expiresAt`. Mint tokens just in time, refresh them before expiration, treat them like passwords, and never log them.

Removing the installation, or deleting the app, invalidates its installation tokens before `expiresAt`. The REST API and Git over HTTPS then reject the token with `401`. Do not retry with the same token; the app must be reinstalled before it can mint a working one.

An installation token cannot exceed the installation's approved scopes or repository access. You can attenuate a token to fewer `scopes` or `repositoryIds`. Empty or omitted arrays inherit the complete installation grant.

Use installation tokens for repository-scoped operations, including pull requests, check-run writes, and [Git over HTTPS](#git-https-authentication).

### [Git HTTPS authentication](#git-https-authentication)

Installation access tokens authenticate Git over HTTPS. The Git endpoint uses HTTP Basic authentication: the password is the installation token, and the username is `x-access-token`. Bearer credentials belong on the REST API; Git HTTPS rejects them.

Mint a token from [Create Installation Access Token](#create-installation-access-token) immediately before the Git operation. Tokens expire after at most 15 minutes.

Clone, fetch, and pull require [`repository:contents:read`](#scopes). Push requires [`repository:contents:write`](#scopes). The token must include the target repository in its grant.

Pushing also requires the repository's owner to be eligible to write to Origin, the same requirement [Create Repo](#create-repo) carries. A user owner must be on a Pro, Pro Student, Pro+, Ultra, or Start plan. A team owner must have an active paid team plan, must not be on Privacy Mode (Legacy), and must not have Origin turned off by a team admin. A push to a repository whose owner is ineligible returns `403`. Clone, fetch, and pull do not carry this requirement.

Read `cloneUrl` from [Get Repo](#get-repo) or [List App Installation Repositories](#list-app-installation-repositories). Both the GitHub-shaped path (`https://origin.cursor.com/OWNER_SLUG/REPO_NAME.git`) and the legacy `/git/` path clone.

```
git clone "https://x-access-token:${INSTALLATION_TOKEN}@origin.cursor.com/OWNER_SLUG/REPO_NAME.git"
```

Embedding the token in the URL stores it in `.git/config`. After a successful clone, rewrite the remote so later commands do not reuse an expired secret:

```
git remote set-url origin "https://origin.cursor.com/OWNER_SLUG/REPO_NAME.git"
```

To keep the token out of the remote URL, supply it through Git's credential helper:

```
git -c credential.helper="!f() { echo username=x-access-token; echo password=${INSTALLATION_TOKEN}; }; f" \  clone "https://origin.cursor.com/OWNER_SLUG/REPO_NAME.git"
```

The Origin CLI credential helper is for user logins. App integrations pass the installation token as shown here. Treat the token like a password, never log it, and mint a fresh one before `expiresAt` when a job still needs Git access.

### [User-authenticated CLI requests](#user-authenticated-cli-requests)

After signing in with the [Origin CLI](#origin-cli), use `origin api` for user-authenticated requests. The CLI resolves the user's credential and sends it as a Bearer token. App integrations should use app JWTs and installation access tokens instead.

### [Discovery and signing keys](#discovery-and-signing-keys)

Origin publishes unauthenticated discovery metadata and its active signing keys. The same keys sign webhook deliveries and [installation receipts](#installation-receipt).

Discovery metadata identifies the issuer and `jwks_uri`:

```
curl https://api.cursor.com/v1/origin/.well-known/openid-configuration
```

```
{  "issuer": "https://api.cursor.com/v1/origin",  "jwks_uri": "https://api.cursor.com/v1/origin/keys",  "response_types_supported": ["id_token"],  "subject_types_supported": ["public"],  "id_token_signing_alg_values_supported": ["EdDSA"]}
```

`/keys` returns active Ed25519 JWKs:

```
curl https://api.cursor.com/v1/origin/keys
```

```
{  "keys": [    {      "kty": "OKP",      "crv": "Ed25519",      "use": "sig",      "alg": "EdDSA",      "kid": "origin-key-id",      "x": "PUBLIC_KEY_MATERIAL"    }  ]}
```

Cache the JWKS. Webhook signatures do not carry a key ID, so verification should try each active Ed25519 key. Installation receipts carry the signing key's `kid` in their JOSE header, so receipt verification can resolve the key directly.

## [Scopes](#scopes)

Request only the minimum scopes your app needs. `repository:metadata:read` and app or installation metadata access are granted automatically and should not be added separately to installation URLs.

| Scope | Allows |
| --- | --- |
| `repository:metadata:read` | Read repository metadata. Added automatically. |
| `repository:contents:read` | Read commits, branches, contents, and low-level Git objects. Clone, fetch, and pull over Git HTTPS. Sync a mirrored repository from its upstream source. |
| `repository:contents:write` | Push over Git HTTPS. Merge pull requests. |
| `repository:pull_requests:read` | Read pull requests, changed files, pull request commits, and assigned labels. |
| `repository:pull_requests:write` | Create and update pull requests. Assign and remove pull request labels. |
| `repository:pull_requests:reviews:read` | Read pull request comments and submitted reviews. |
| `repository:pull_requests:reviews:write` | Create and update comments; create, update, and dismiss reviews. |
| `repository:checks:read` | Read check suites and runs. |
| `repository:checks:write` | Create and update check suites and runs. |
| `repository:rulesets:read` | Read repository rulesets. |
| `repository:rulesets:write` | Create and update repository rulesets. |

The installation token can only narrow these grants. It cannot add a scope or repository the workspace admin did not approve.

## [Rate limits](#rate-limits)

The Origin API uses a shared per-principal point budget that resets on a rolling one-minute window. Each authenticated principal kind has its own budget:

| Principal | Default budget |
| --- | --- |
| Installation access token | 3,000 points/minute |
| App JWT | 6,000 points/minute |
| User or team service-account API key | 600 points/minute |

Every endpoint charges a fixed cost against that budget before the handler runs. Authentication and authorization failures are not charged.

| Cost | Operations |
| --- | --- |
| 0 | [Get Rate Limit](#get-rate-limit). Status only; does not consume points. |
| 1 | Most read endpoints, plus [Create Installation Access Token](#create-installation-access-token) |
| 5 | Ordinary writes, plus these heavier reads: [Get Commit](#get-commit), [List Commit Files](#list-commit-files), and [List Pull Request Files](#list-pull-request-files) |
| 10 | [Create Repo](#create-repo) and [Merge Pull Request](#merge-pull-request) |

Cursor can raise per-app minute budgets for design partners. Contact Cursor if your integration needs a higher limit.

### [Response headers](#response-headers)

Charged responses and [Get Rate Limit](#get-rate-limit) include:

| Header | Description |
| --- | --- |
| `X-RateLimit-Limit` | Points available in the current window for this principal |
| `X-RateLimit-Remaining` | Points left in the current window |
| `X-RateLimit-Used` | Points consumed in the current window |
| `X-RateLimit-Reset` | Unix timestamp (UTC seconds) when the window resets |
| `X-RateLimit-Resource` | Always `core` for the shared public API budget |

`X-RateLimit-Reset` advertises a full 60-second window from the response time. The counter's window starts at the first charged request in a burst, not on a calendar-minute boundary.

### [Exceeding the limit](#exceeding-the-limit)

When a request would exceed the budget, the API returns HTTP `429` with:

- `Retry-After`: seconds to wait before retrying (`60`)
- The same `X-RateLimit-*` headers, with `X-RateLimit-Remaining` set to `0`

```
{  "code": 8,  "message": "Rate limit exceeded: 3000 points per minute for this installation. Retry after 60s.",  "details": []}
```

Wait for `Retry-After`, or until `X-RateLimit-Reset`, before retrying. Use backoff with jitter when concurrent callers share one installation token.

### [Checking remaining quota](#checking-remaining-quota)

Call [Get Rate Limit](#get-rate-limit) to read the current budget without consuming points. The response body mirrors the `X-RateLimit-*` headers for the shared `core` resource.

## [Webhooks](#webhooks)

Origin sends signed HTTP `POST` requests to the app's registered HTTPS webhook URL with `content-type: application/json`.

Delivery is at least once. Deduplicate retries with `webhook-id`, durably accept the request, return `2xx` quickly, and process the event asynchronously.

Origin retries transport errors, `429`, and `5xx` responses up to six total attempts. Retry delays are 30 seconds, 1 minute, 2 minutes, 4 minutes, and 8 minutes. Other `4xx` responses are terminal.

Origin sends no events for a repository mirrored in from GitHub, and installation event payloads leave those repositories out of the selected repository arrays.

### [Headers](#headers)

| Header | Description |
| --- | --- |
| `content-type` | `application/json` |
| `user-agent` | `Cursor-Origin-Webhook/1.0` |
| `webhook-id` | Stable delivery ID and idempotency key. |
| `webhook-timestamp` | Unix timestamp included in the signature. |
| `webhook-signature` | `v1ed,BASE64_SIGNATURE` |
| `webhook-event-type` | Event slug for routing. |
| `webhook-event-id` | Underlying Origin event ID mirrored from the signed body. |
| `webhook-app-id` | Target app ID. |
| `webhook-installation-id` | Target installation ID. |

Routing headers are conveniences. After signature verification, the body is authoritative.

### [Signature verification](#signature-verification)

Use the raw request body before parsing it. Construct:

```
lowercaseHex(SHA-256("<webhook-id>.<webhook-timestamp>.<raw-request-body>"))
```

Verify the Ed25519 signature over the UTF-8 bytes of that hexadecimal digest against an active Origin JWKS key. Reject timestamps more than five minutes from the current time.

```
import {  createHash,  createPublicKey,  verify,  type JsonWebKeyInput,} from "node:crypto";export async function verifyOriginWebhook(  body: Buffer,  headers: Record<string, string | undefined>): Promise<boolean> {  const id = headers["webhook-id"];  const timestamp = Number(headers["webhook-timestamp"]);  const signature = headers["webhook-signature"]    ?.split(/\s+/)    .find((value) => value.startsWith("v1ed,"));  const now = Math.floor(Date.now() / 1000);  if (    !id ||    !signature ||    !Number.isInteger(timestamp) ||    Math.abs(now - timestamp) > 300  ) {    return false;  }  const digest = createHash("sha256")    .update(`${id}.${timestamp}.`)    .update(body)    .digest("hex");  // Cache this response in production.  const { keys } = await fetch(    "https://api.cursor.com/v1/origin/keys"  ).then((response) => response.json()) as {    keys: JsonWebKeyInput[];  };  return keys.some((jwk) => {    try {      return verify(        null,        Buffer.from(digest),        createPublicKey({ key: jwk, format: "jwk" }),        Buffer.from(signature.slice(5), "base64")      );    } catch {      return false;    }  });}
```

### [Delivery envelope](#delivery-envelope)

Each request wraps the event payload with delivery, app, and installation identity:

```
{  "deliveryId": "whd_01...",  "appId": "app_01...",  "installationId": "i_01...",  "event": {    "id": "evt_01...",    "type": "pull_request.comment.created",    "eventTime": "2026-07-01T10:03:00Z",    "payload": {}  }}
```

`deliveryId` is stable across retries. `event.id` identifies the underlying domain event.

### [Events](#events)

| Event | Delivered when |
| --- | --- |
| `repository.pushed` | One or more refs change in a push. |
| `pull_request.created` | A pull request opens. |
| `pull_request.head_ref.pushed` | The pull request head advances. |
| `pull_request.base_ref.updated` | The base ref or resolved base commit changes. |
| `pull_request.metadata.updated` | The title or description changes. |
| `pull_request.closed` | A pull request closes without merging. |
| `pull_request.merged` | A pull request merges. |
| `pull_request.reopened` | A closed pull request reopens. |
| `pull_request.published` | A draft becomes open. |
| `pull_request.comment.created` | A visible pull request comment is created. |
| `pull_request.review.submitted` | A review is submitted with any verdict. |
| `pull_request.reviewer.added` | A reviewer is requested. |
| `pull_request.reviewer.removed` | A reviewer is removed. |
| `pull_request.reviewer.rerequested` | A reviewer is requested again. |
| `repository.check_run.created` | A check run is created. |
| `repository.check_run.completed` | A check run completes. |
| `installation.created` | The app is installed. |
| `installation.updated` | Scopes or repository selection change. |
| `installation.deleted` | The app is uninstalled. |

### [Payload families](#payload-families)

- Pull request lifecycle events contain a `pullRequest` snapshot and `repository` reference. Route on `event.type`; there is no separate action field. The snapshot omits the pull request's assigned `labels`; read them from [Get Pull Request](#get-pull-request) or [List Pull Requests](#list-pull-requests).
- Comment events contain a `pullRequest` reference and the affected `comment`.
- Review events contain a `pullRequest` reference and the submitted `review`.
- Reviewer events contain a `pullRequest` reference, a user or group `reviewer`, how the request was created, an optional actor, and a timestamp. The reviewer `id` is the encoded user ID (`user_…`, the same format as the organization API) when `kind` is `user`, and the group public ID (`grp_…`) when `kind` is `group`. There is no public HTTP API to add, remove, or rerequest reviewers.
- Check events contain `repository`, `checkSuite`, `checkRun`, and `actor`.
- Push events contain one repository snapshot and up to 100 `refUpdates`. `refUpdatesCount` is authoritative. Optional tip metadata is best effort and does not provide a complete commits array.
- Installation events contain the installation snapshot and app identity. Selected repository arrays may be capped at 5,000; `repositoriesCount` is authoritative.

### [Recovery](#recovery)

Use an app JWT to query [`GET /app/webhook/deliveries`](#list-webhook-deliveries). Filter by delivery status, event type, installation, time range, or page token. `delivered=false` returns every delivery the receiver has never acknowledged with `2xx`. Deliveries stay listable for seven days, so recover within that window.

Use [`POST /app/webhook/deliveries:batchRedeliver`](#batch-redeliver-webhook-deliveries) to queue redelivery for up to 100 delivery IDs. The operation deduplicates IDs and reports the result for each delivery.

## [Common conventions](#common-conventions)

### [Pagination](#pagination)

Paginated endpoints accept:

- `pageSize`: defaults to 30 and is capped at 100.
- `pageToken`: opaque token returned by the preceding page. Do not inspect or construct it.

Responses use a resource-specific collection field and `nextPageToken`. It is empty when no next page exists. Public list responses do not include total counts. Page tokens are bound to their originating resource and filters. Restart pagination when filters change. Invalid or mismatched non-empty tokens return `400`.

### [Errors](#errors)

Errors use a Google RPC-style body:

```
{  "code": 5,  "message": "resource not found",  "details": []}
```

Common HTTP statuses are `400`, `401`, `403`, `404`, `429`, `500`, and `503`. Some Git-database operations also return `409` for repository-state conflicts. See [Rate limits](#rate-limits) for `429` headers and retry behavior.

Use the HTTP status and `code` to branch on errors. Treat `message` as developer-facing text.

### [Repository paths](#repository-paths)

Repository-scoped paths take the owner slug and repository name as `{ownerSlug}/{repoName}`. Both segments resolve case-insensitively, so any casing addresses the repository. Responses return the stored name and slug rather than the casing you sent, and Git HTTPS URLs resolve the same way. Compare repository names case-insensitively, and read the canonical casing from [Get Repo](#get-repo).

### [Resource references](#resource-references)

Resource snapshots contain the resource's current fields. Container context uses compact references instead of duplicating complete resources:

- `RepositoryReference` identifies a repository.
- `PullRequestReference` identifies a pull request and nests its repository reference.
- `ThreadReference` identifies the thread containing a pull request comment.
- `OriginActor` identifies a public actor as one of `user`, `app`, or `serviceAccount`. Exactly one variant is present; read the identity from that variant.

## [Current limitations](#current-limitations)

- Namespace-wide repository listing and repository creation are not part of the partner API. Discover repositories through the installation.
- Commit comparison returns summary data rather than a paginated compare-file or compare-commit stream.
- Pull request comments expose thread IDs, but there is no first-class thread or resolution API.
- Reviewer add, remove, and rerequest operations are webhook-only.
- Push webhooks do not include a complete commit list.
- Pull request merge supports native Origin repositories. Mirrored repositories are rejected.
- Apps cannot reach a repository that Origin mirrors in from GitHub. Origin leaves those repositories out of installations, installation access tokens, and webhook deliveries.

## [Implementation checklist](#implementation-checklist)

- Store the Ed25519 private key in a secrets manager and rotate keys deliberately. See [Generate an app signing key](#generate-an-app-signing-key).
- Verify the [installation receipt](#installation-receipt) on install callbacks and read the installation ID and `state` from its claims.
- Use short-lived app JWTs and mint installation tokens just in time.
- Use installation tokens, not app JWTs, for repository-scoped APIs, check-run writes, and Git HTTPS.
- Request the minimum scopes and repository access.
- Treat page tokens as opaque and restart pagination when filters change.
- Keep check `key` values stable and readable. Use a new immutable `externalId` for each retry and increasing `externalUpdatedAt` values for updates.
- Verify webhook signatures against the raw request body before parsing.
- Deduplicate deliveries with `webhook-id` and process asynchronously after returning `2xx`.
- Ignore unknown JSON fields for forward compatibility.
- Honor `Retry-After` and `X-RateLimit-*` headers. Use [Get Rate Limit](#get-rate-limit) to monitor remaining points without consuming them.

## [Endpoint reference](#endpoint-reference)

Download the [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml) for the complete component schemas.

Generated OpenAPI path bindings such as `identifier.ownerSlug` and `identifier.name` appear here as `ownerSlug` and `repoName`. The URL segments and request behavior are unchanged.

The JSON snippets show schema-shaped placeholder values. Response field descriptions reflect the OpenAPI schema and current platform contract.

## [Apps and installations](#apps-and-installations)

### [Get Rate Limit](#get-rate-limit)

GET`/v1/origin/rate_limit`

Returns the authenticated principal's current public API rate limit status.

Accessing this endpoint does not consume rate limit points. The response covers the shared per-minute point budget used by other public API endpoints for this principal. See [Rate limits](#rate-limits).

#### [Response Fields](#response-fields)

`resources` object

Rate limit resources for the authenticated principal.

`resources.core` object

Shared per-minute point budget for public API endpoints.

`resources.core.limit` integer

Maximum points available in the current window.

`resources.core.remaining` integer

Points remaining in the current window.

`resources.core.reset` integer

Unix timestamp (UTC seconds) when the current window resets.

`resources.core.used` integer

Points consumed in the current window.

`rate` object

Alias of `resources.core`. Prefer `resources.core` in new clients.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/rate_limit' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "resources": {    "core": {      "limit": 0,      "remaining": 0,      "reset": 0,      "used": 0    }  },  "rate": {    "limit": 0,    "remaining": 0,    "reset": 0,    "used": 0  }}
```

### [Get Authenticated App](#get-authenticated-app)

GET`/v1/origin/app`

Returns metadata for the authenticated app.

#### [Response Fields](#response-fields-1)

`id` string

Origin app identifier used as the JWT issuer and key ID.

`slug` string

Unique app slug.

`displayName` string

Human-readable app display name.

`webhookUrl` string

Registered HTTPS URL that receives the app's webhook deliveries.

`events` array

Webhook event subscriptions configured for the app.

`createdAt` string

RFC 3339 timestamp for app creation.

`updatedAt` string

RFC 3339 timestamp for the latest app metadata update.

`installationRedirectUris` array

Registered installation callback URIs; non-local callbacks must match exactly and use HTTPS.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "slug": "string",  "displayName": "string",  "webhookUrl": "string",  "events": [    "string"  ],  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "installationRedirectUris": [    "string"  ]}
```

### [List App Installations](#list-app-installations)

GET`/v1/origin/app/installations`

Lists installations for the authenticated app.

#### [Query Parameters](#query-parameters)

`pageSize` integer

Max installations to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-2)

`installations` array

Page of installations owned by the authenticated app.

`installations[].id` string

Installation identifier that the app stores and uses to mint installation access tokens.

`installations[].appId` string

Identifier of the installed app.

`installations[].target` object

Owner selected by the customer for this installation.

`installations[].target.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`installations[].target.id` string

Origin owner identifier.

`installations[].target.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`installations[].createdAt` string

RFC 3339 installation creation timestamp.

`installations[].updatedAt` string

RFC 3339 timestamp for the latest installation update.

`installations[].repoSelectionMode` string

Repository grant mode; exactly all or selected.

`installations[].scopes` array

Scopes approved for the installation.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app/installations' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "installations": [    {      "id": "string",      "appId": "string",      "target": {        "slug": "string",        "id": "string",        "type": "team"      },      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "repoSelectionMode": "all",      "scopes": [        "string"      ]    }  ],  "nextPageToken": "string"}
```

### [Get App Installation](#get-app-installation)

GET`/v1/origin/app/installations/{installationId}`

Returns a single installation for the authenticated app.

`repoSelectionMode` is `all` or `selected`.

#### [Path Parameters](#path-parameters)

`installationId` string Required

Installation identifier.

#### [Response Fields](#response-fields-3)

`id` string

Installation identifier that the app stores and uses to mint installation access tokens.

`appId` string

Identifier of the installed app.

`target` object

Owner selected by the customer for this installation.

`target.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`target.id` string

Origin owner identifier.

`target.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`createdAt` string

RFC 3339 installation creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest installation update.

`repoSelectionMode` string

Repository grant mode; exactly all or selected.

`scopes` array

Scopes approved for the installation.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "appId": "string",  "target": {    "slug": "string",    "id": "string",    "type": "team"  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "repoSelectionMode": "all",  "scopes": [    "string"  ]}
```

### [Delete App Installation](#delete-app-installation)

DELETE`/v1/origin/app/installations/{installationId}`

Deletes an installation that belongs to the authenticated app and prevents new installation tokens from being minted. Already-issued short-lived tokens may remain valid until they expire (at most 15 minutes). The response body is empty.

#### [Path Parameters](#path-parameters-1)

`installationId` string Required

The unique identifier of the installation to delete. Bound from the URL path; the installation must belong to the authenticated app.

#### [Response Fields](#response-fields-4)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [Create Installation Access Token](#create-installation-access-token)

POST`/v1/origin/app/installations/{installationId}/access_tokens`

Creates an installation access token for the authenticated app.

Requires app signing-JWT authentication, like GetAuthenticatedApp. The token is scoped to the named installation, which must belong to the authenticated app. Callers may attenuate the token to a subset of the installation's accepted scopes and accessible repositories.

Origin rejects a request whose `repositoryIds` names a repository mirrored in from GitHub, because that repository is not accessible to the installation.

#### [Path Parameters](#path-parameters-2)

`installationId` string Required

The unique identifier of the installation to scope the token to. Bound from the URL path; the installation must belong to the authenticated app.

#### [Request Body](#request-body)

`scopes` array

Scope strings to grant the token. Values must be unique and included in the installation's accepted scopes. Empty or omitted inherits the full scope grant.

`repositoryIds` array

Repository IDs to grant the token. Values must be unique, accessible to the installation, and contain at most 50 entries. Empty or omitted inherits all accessible repositories.

#### [Response Fields](#response-fields-5)

`token` string

Short-lived installation credential with the oit\_ prefix.

`expiresAt` string

RFC 3339 expiration time; the token expires after at most 15 minutes and never outlives the app JWT used to mint it.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID/access_tokens' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{}'
```

**Response shape:**

```
{  "token": "string",  "expiresAt": "2026-01-01T00:00:00Z"}
```

### [List App Installation Repositories](#list-app-installation-repositories)

GET`/v1/origin/installation/repos`

Lists repositories accessible to the authenticated app installation.

Requires an installation access token (`oit_`) minted by CreateInstallationAccessToken.

Partners discover their repositories through this endpoint. List entries are sparse repository summaries; use [Get Repo](#get-repo) for full timestamps. [Get Repo](#get-repo) includes the output-only `cloneUrl`.

Results leave out repositories that Origin mirrors in from GitHub, because an installation cannot reach them.

#### [Query Parameters](#query-parameters-1)

`pageSize` integer

Max repositories to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-6)

`repositories` array

Sparse repository summaries; use get-repository for full timestamps.

`repositories[].id` string

Origin repository identifier.

`repositories[].name` string

Repository name within its owner.

`repositories[].fullName` string

Combined owner and repository name, such as acme/api.

`repositories[].owner` object

Owner reference for the repository.

`repositories[].owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`repositories[].owner.id` string

Origin owner identifier.

`repositories[].owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`repositories[].defaultBranch` string

Repository default branch name.

`repositories[].mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`repositories[].mirror.source` string

Mirror source. Allowed value: `github`.

`repositories[].mirror.sourceId` string

Opaque repository identifier assigned by the source.

`repositories[].mirror.status` string

Effective mirror direction during a transition, until cutover completes. Allowed values: `inbound`, `outbound`.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

`repoSelectionMode` string

Reports whether the installation grants all repositories or only selected repositories.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/installation/repos' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "repositories": [    {      "id": "string",      "name": "string",      "fullName": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      },      "defaultBranch": "string",      "mirror": {        "source": "github",        "sourceId": "string",        "status": "inbound"      }    }  ],  "nextPageToken": "string",  "repoSelectionMode": "all"}
```

### [List Webhook Deliveries](#list-webhook-deliveries)

GET`/v1/origin/app/webhook/deliveries`

Lists webhook deliveries for the authenticated app, newest first.

A delivery is one event owed to one app; its id is the Standard Webhooks `webhook-id` header the receiver sees. `delivered=false` is the recovery predicate: it selects every delivery that has never received a `2xx`, including deliveries whose retry ladder ran out during an outage.

Deliveries are listable for seven days after they are created, and only while your app has an active installation in the delivery's namespace. App-targeted lifecycle events such as `installation.deleted` stay visible after the uninstall they describe.

#### [Query Parameters](#query-parameters-2)

`delivered` boolean

Compares against `delivered_at`. `delivered=false` is the recovery predicate: it is evaluated server-side, so it cannot miss a delivery whose retry ladder exhausted mid-outage the way a caller-supplied time window silently does.

`eventType` string

Exact event type, e.g. `pull_request.created`.

`installationId` string

Narrow to one installation (`WebhookDelivery.installation.id`).

`createdAfter` string

Bound the delivery's creation time. For browsing, not for recovery.

`createdBefore` string

`pageSize` integer

Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-7)

`deliveries` array

Webhook deliveries for the authenticated app, ordered newest first. Each delivery ID is the webhook-id seen by the receiver.

`deliveries[].id` string

Stable delivery identifier and Standard Webhooks webhook-id value; use it as the idempotency key.

`deliveries[].event` object

The event this delivery carries.

`deliveries[].event.id` string

Underlying Origin event identifier. It may also be present alongside the stable delivery ID but is not the idempotency key.

`deliveries[].event.type` string

Event slug carried by the delivery for routing.

`deliveries[].installation` object

The installation this delivery belongs to. `id` is the current active installation for the target owner; unset when none exists (possible only for app-targeted lifecycle events after an uninstall).

`deliveries[].installation.id` string

Installation identifier associated with a webhook delivery list item.

`deliveries[].installation.target` object

Owner targeted by the installation.

`deliveries[].installation.target.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`deliveries[].installation.target.id` string

Origin owner identifier.

`deliveries[].installation.target.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`deliveries[].createdAt` string

Delivery creation timestamp used by createdAfter and createdBefore browsing filters.

`deliveries[].deliveredAt` string

Absence corresponds to delivered=false: the receiver has never acknowledged this delivery with a 2xx response.

`deliveries[].lastAttempt` object

The most recent HTTP attempt, when one exists: its response status code, latency, transport error, trigger, and time.

`deliveries[].lastAttempt.id` string

Webhook delivery attempt identifier.

`deliveries[].lastAttempt.deliveryId` string

Stable delivery identifier associated with this attempt.

`deliveries[].lastAttempt.trigger` string

Reason this delivery attempt was sent. Allowed values: `automatic`, `manual`.

`deliveries[].lastAttempt.responseStatusCode` integer

Unset when the POST produced no HTTP response (transport error, timeout).

`deliveries[].lastAttempt.latencyMs` integer

Delivery attempt latency in milliseconds.

`deliveries[].lastAttempt.errorMessage` string

Transport error detail when there was no HTTP response; empty otherwise.

`deliveries[].lastAttempt.attemptedAt` string

RFC 3339 timestamp for this delivery attempt.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app/webhook/deliveries' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "deliveries": [    {      "id": "string",      "event": {        "id": "string",        "type": "string"      },      "installation": {        "id": "string",        "target": {          "slug": "string",          "id": "string",          "type": "team"        }      },      "createdAt": "2026-01-01T00:00:00Z",      "deliveredAt": "2026-01-01T00:00:00Z",      "lastAttempt": {        "id": "string",        "deliveryId": "string",        "trigger": "automatic",        "responseStatusCode": 0,        "latencyMs": 0,        "errorMessage": "string",        "attemptedAt": "2026-01-01T00:00:00Z"      }    }  ],  "nextPageToken": "string"}
```

### [Batch Redeliver Webhook Deliveries](#batch-redeliver-webhook-deliveries)

POST`/v1/origin/app/webhook/deliveries:batchRedeliver`

Asks Origin to send deliveries again.

The request means "ensure a send is in flight for each of these", not "add another send". It returns one result per unique input rather than failing the batch on a bad entry, so a single expired ID cannot block the rest of a recovery page. A `202` means the sends are queued; delivery itself is asynchronous, so poll [List Webhook Deliveries](#list-webhook-deliveries) for outcomes.

#### [Request Body](#request-body-1)

`deliveryIds` array Required

Deliveries to send again. At most 100 unique entries, matching the `pageSize` ceiling on [List Webhook Deliveries](#list-webhook-deliveries). Duplicates are removed, keeping first-seen order. An empty list, or more than 100 unique entries, returns `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-8)

`results` array

Accepted asynchronous redelivery results, one per unique delivery ID, with queued, already\_in\_flight, or not\_found outcomes.

`results[].deliveryId` string

Requested stable delivery ID corresponding to this batch result.

`results[].outcome` string

Redelivery disposition: `queued` when a send was created, `already_in_flight` when a send was already running, and `not_found` otherwise. `already_in_flight` is a success, not an error. `not_found` covers unknown IDs, IDs older than the seven-day retention window, and namespaces where your app is no longer installed.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/app/webhook/deliveries:batchRedeliver' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "deliveryIds": [    "DELIVERY_ID"  ]}'
```

**Response shape:**

```
{  "results": [    {      "deliveryId": "string",      "outcome": "queued"    }  ]}
```

## [Repositories](#repositories)

`cloneUrl` is an output-only HTTPS clone URL. [Get Repo](#get-repo) includes `cloneUrl`.

Partners discover their repositories through [List App Installation Repositories](#list-app-installation-repositories). Namespace-wide repository listing and creation are not part of the partner API.

### [List Repos](#list-repos)

GET`/v1/origin/repos/{ownerSlug}`

Lists repos belonging to an owner entity.

#### [Path Parameters](#path-parameters-3)

`ownerSlug` string Required

Parent owner entity slug.

#### [Query Parameters](#query-parameters-3)

`pageSize` integer

Max repos to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

`filter` string

Optional case-insensitive substring filter.

#### [Response Fields](#response-fields-9)

`repositories` array

Repositories belonging to the requested owner.

`repositories[].id` string

Origin repository identifier.

`repositories[].name` string

Repository name within its owner.

`repositories[].fullName` string

Combined owner and repository name, such as acme/api.

`repositories[].owner` object

Owner reference for the repository.

`repositories[].owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`repositories[].owner.id` string

Origin owner identifier.

`repositories[].owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`repositories[].defaultBranch` string

Repository default branch name.

`repositories[].createdAt` string

RFC 3339 repository creation timestamp.

`repositories[].updatedAt` string

RFC 3339 repository update timestamp.

`repositories[].pushedAt` string

RFC 3339 timestamp of the most recent push shown by the full repository response.

`repositories[].cloneUrl` string

Output-only HTTPS clone URL; the get-repository response includes it.

`repositories[].mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`repositories[].mirror.source` string

Mirror source. Allowed value: `github`.

`repositories[].mirror.sourceId` string

Opaque repository identifier assigned by the source.

`repositories[].mirror.status` string

Effective mirror direction during a transition, until cutover completes. Allowed values: `inbound`, `outbound`.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "repositories": [    {      "id": "string",      "name": "string",      "fullName": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      },      "defaultBranch": "string",      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "pushedAt": "2026-01-01T00:00:00Z",      "cloneUrl": "string",      "mirror": {        "source": "github",        "sourceId": "string",        "status": "inbound"      }    }  ],  "nextPageToken": "string"}
```

### [Get Repo](#get-repo)

GET`/v1/origin/repos/{ownerSlug}/{repoName}`

Returns a single repo by its `(owner_id, name)` identifier.

`cloneUrl` is an output-only HTTPS clone URL. Get repository includes `cloneUrl`.

#### [Path Parameters](#path-parameters-4)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-10)

`id` string

Origin repository identifier.

`name` string

Repository name within its owner.

`fullName` string

Combined owner and repository name, such as acme/api.

`owner` object

Owner reference for the repository.

`owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`owner.id` string

Origin owner identifier.

`owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`defaultBranch` string

Repository default branch name.

`createdAt` string

RFC 3339 repository creation timestamp.

`updatedAt` string

RFC 3339 repository update timestamp.

`pushedAt` string

RFC 3339 timestamp of the most recent push shown by the full repository response.

`cloneUrl` string

Output-only HTTPS clone URL; the get-repository response includes it.

`mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`mirror.source` string

Mirror source. Allowed value: `github`.

`mirror.sourceId` string

Opaque repository identifier assigned by the source.

`mirror.status` string

Effective mirror direction during a transition, until cutover completes. Allowed values: `inbound`, `outbound`.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "name": "string",  "fullName": "string",  "owner": {    "slug": "string",    "id": "string",    "type": "team"  },  "defaultBranch": "string",  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "pushedAt": "2026-01-01T00:00:00Z",  "cloneUrl": "string",  "mirror": {    "source": "github",    "sourceId": "string",    "status": "inbound"  }}
```

### [Create Repo](#create-repo)

POST`/v1/origin/repos/{ownerSlug}`

Creates a repo belonging to an owner.

The owner must be eligible to write to Origin when the request is made. A user owner must be on a Pro, Pro Student, Pro+, Ultra, or Start plan. A team owner must have an active paid team plan, must not be on Privacy Mode (Legacy), and must not have Origin turned off by a team admin. An ineligible owner returns `FailedPrecondition` (HTTP 400). Reading existing repositories does not carry this requirement.

Repository names are claimed case-insensitively. A name that differs only in case from a repository the owner already has is rejected, so `widgets` and `Widgets` cannot coexist in one namespace. The name you send is stored as you send it.

The first push to a new repo can retarget its default branch. When that push only creates branches and none of them is the repo's stored default branch, Origin sets the default branch to the created branch, or to `main` or `master` when the push creates several and one of those names is among them. The default branch is otherwise unchanged. Read the current value from [Get Repo](#get-repo).

#### [Path Parameters](#path-parameters-5)

`ownerSlug` string Required

Parent owner entity's slug.

#### [Request Body](#request-body-2)

`name` string Required

The repo name, unique to its owner. Required on create.

`defaultBranch` string

Default branch name. Always set on responses. On create, omitting this field or leaving it empty defaults to "main".

#### [Response Fields](#response-fields-11)

`id` string

Origin repository identifier.

`name` string

Repository name within its owner.

`fullName` string

Combined owner and repository name, such as acme/api.

`owner` object

Owner reference for the repository.

`owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`owner.id` string

Origin owner identifier.

`owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`defaultBranch` string

Repository default branch name.

`createdAt` string

RFC 3339 repository creation timestamp.

`updatedAt` string

RFC 3339 repository update timestamp.

`pushedAt` string

RFC 3339 timestamp of the most recent push shown by the full repository response.

`cloneUrl` string

Output-only HTTPS clone URL; the get-repository response includes it.

`mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`mirror.source` string

Mirror source. Allowed value: `github`.

`mirror.sourceId` string

Opaque repository identifier assigned by the source.

`mirror.status` string

Effective mirror direction during a transition, until cutover completes. Allowed values: `inbound`, `outbound`.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "NAME"}'
```

**Response shape:**

```
{  "id": "string",  "name": "string",  "fullName": "string",  "owner": {    "slug": "string",    "id": "string",    "type": "team"  },  "defaultBranch": "string",  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "pushedAt": "2026-01-01T00:00:00Z",  "cloneUrl": "string",  "mirror": {    "source": "github",    "sourceId": "string",    "status": "inbound"  }}
```

### [List Branches](#list-branches)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/branches`

Lists the repo's branches and tip commits in ascending name order, paginated with `page_size` and `page_token`.

#### [Path Parameters](#path-parameters-6)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-4)

`pageSize` integer

Max branches to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the page offset, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-12)

`branches` array

Paginated branch records containing branch name and tip commit SHA.

`branches[].name` string

Branch name.

`branches[].commit` object

The commit at the tip of the branch.

`branches[].commit.sha` string

Full hex SHA of the commit at the tip of the branch.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/branches' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "branches": [    {      "name": "string",      "commit": {        "sha": "string"      }    }  ],  "nextPageToken": "string"}
```

### [Sync Mirror](#sync-mirror)

POST`/v1/origin/repos/{ownerSlug}/{repoName}:syncMirror`

Synchronizes one ref of a mirrored repository from its upstream source. Returns HTTP `200` when the sync target is satisfied, or HTTP `202` when the sync is still pending. `wait=false` (the default) schedules the sync and usually returns `202`; it returns `200` immediately when `sha` is already reachable from `ref`. `wait=true` blocks until satisfied or the wait budget (~2 minutes) expires; expiry still returns `202` and the sync continues in the background. Repositories that do not pull from an upstream source are rejected.

#### [Path Parameters](#path-parameters-7)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-3)

`ref` string Required

Full git ref name to fetch. Must start with `refs/` and name a ref after that prefix, for example `refs/heads/main` or `refs/tags/v1`. Short names such as `main` are rejected with `INVALID_ARGUMENT`.

`wait` boolean

When true, block until synced or the wait budget expires. Defaults to false.

`sha` string

Optional full commit object ID: 40- or 64-character hex. Omit or leave empty to wait on the tip of `ref`. When set and reachable from `ref`, the call returns early without waiting for other mirror work to drain. Other values are rejected with `INVALID_ARGUMENT`.

#### [Response Fields](#response-fields-13)

`synced` boolean

True when the sync target is known to be satisfied. Prefer the HTTP status (`200` vs `202`): proto3 JSON omits this field when false.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME:syncMirror' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "ref": "refs/heads/main",  "wait": true}'
```

**Response shape:**

```
{  "synced": true}
```

## [Checks](#checks)

- The first run upsert creates its suite automatically.
- Required checks match the installing app plus the suite `key`, and optionally a run `key`. `name` is display-only and is not used for matching.
- Keep `key` values stable across attempts and readable for users, since required-check configuration is keyed on them.
- Reuse `externalId` to update an attempt; use a new `externalId` for a retry.
- Use `checkRun.output` for human-readable results:
  - `title`: short result headline, up to 255 characters.
  - `summary`: primary Markdown summary, up to 65,535 UTF-8 bytes.
  - `text`: extended Markdown details, up to 65,535 UTF-8 bytes.
- Use `detailsUrl` for a link to the provider's external results page.

### [Post Check Run](#post-check-run)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs`

Upserts a check suite + check run using an installation access token with `repository:checks:write`. The write is attributed to the app that owns the authenticated installation. A repeated call with the same `(repo, head_sha, suite.key, check.key)` updates the existing check run in place rather than creating a duplicate.

The endpoint atomically resolves or creates the suite attempt and upserts one run attempt. `externalUpdatedAt` orders updates to the same run identity; stale retries cannot overwrite newer state.

#### [Path Parameters](#path-parameters-8)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-4)

`headSha` string Required

Head commit SHA the check run is reported against (40- or 64-char hex).

`checkSuite` object Required

The suite the check run belongs to; upserted alongside the check run.

`checkSuite.key` string Required

Stable, app-chosen key identifying the logical suite across attempts.

`checkSuite.name` string Required

Human-facing suite name.

`checkSuite.detailsUrl` string

Optional link to more detail about the suite as a whole.

`checkSuite.externalId` string Required

Provider-assigned immutable identity for this suite attempt.

`checkRun` object Required

The check run to upsert.

`checkRun.key` string Required

Stable, app-chosen key identifying the logical check across attempts.

`checkRun.name` string Required

Human-facing check-run name.

`checkRun.status` string Required

Allowed values: `CHECK_RUN_LIFECYCLE_STATUS_UNSPECIFIED`, `queued`, `in_progress`, `completed`.

`checkRun.conclusion` string

Required iff `status == completed`. Allowed values: `CHECK_RUN_CONCLUSION_UNSPECIFIED`, `success`, `failure`, `neutral`, `cancelled`, `skipped`, `timed_out`, `action_required`, `stale`.

`checkRun.externalUpdatedAt` string Required

The external system's last-update time. Used to order concurrent updates so a stale retry can't overwrite newer state.

`checkRun.startedAt` string

When the check run started.

`checkRun.completedAt` string

When the check run completed.

`checkRun.detailsUrl` string

Optional link to more detail about this specific check run (e.g. the provider's job/build URL).

`checkRun.externalId` string Required

Provider-assigned immutable identity for this check attempt.

`checkRun.output` object

Human-readable output for this check run.

`checkRun.output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRun.output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

#### [Response Fields](#response-fields-14)

`checkSuite` object

The upserted check suite.

`checkSuite.id` string

Server-assigned check suite identifier.

`checkSuite.repository` object

Repository reference for the suite.

`checkSuite.repository.id` string

Repository identifier in a container reference.

`checkSuite.repository.name` string

Repository name in a container reference.

`checkSuite.repository.owner` object

Owner reference for the repository.

`checkSuite.repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkSuite.repository.owner.id` string

Origin owner identifier.

`checkSuite.repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkSuite.sha` string

Commit SHA to which the suite is attached.

`checkSuite.key` string

Stable app-chosen required-check identity. Required checks match on app plus this key, not name.

`checkSuite.name` string

Display-only suite name; it is not used for required-check matching.

`checkSuite.detailsUrl` string

Optional link to the provider's suite-level results.

`checkSuite.createdAt` string

RFC 3339 suite creation timestamp.

`checkSuite.updatedAt` string

RFC 3339 timestamp for the latest suite update.

`checkSuite.externalId` string

Provider identity for this suite attempt.

`checkSuite.actor` object

Public actor that produced the suite.

`checkSuite.actor.user` object

User variant of the actor. Set when a user performed the action.

`checkSuite.actor.user.id` string

Public identifier for the user.

`checkSuite.actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkSuite.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuite.actor.app.id` string

Public identifier for the app.

`checkSuite.actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkSuite.actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkSuite.actor.serviceAccount.id` string

Public identifier for the service account.

`checkRun` object

The upserted check run.

`checkRun.id` string

Server-assigned check run identifier.

`checkRun.repository` object

Repository reference for the run.

`checkRun.repository.id` string

Repository identifier in a container reference.

`checkRun.repository.name` string

Repository name in a container reference.

`checkRun.repository.owner` object

Owner reference for the repository.

`checkRun.repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkRun.repository.owner.id` string

Origin owner identifier.

`checkRun.repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkRun.checkSuite` object

Reference to the containing check suite.

`checkRun.checkSuite.id` string

Server-assigned identifier of the containing check suite.

`checkRun.sha` string

Commit SHA to which the run is attached.

`checkRun.key` string

Stable app-chosen logical run identity; required checks may match on app, suite key, and this key.

`checkRun.name` string

Display-only run name; it is not used for required-check matching.

`checkRun.status` string

Lifecycle status; queued, in\_progress, or completed.

`checkRun.conclusion` string

Required for a completed run; success, failure, neutral, cancelled, skipped, timed\_out, action\_required, or stale.

`checkRun.detailsUrl` string

Separate link to the provider's full result page.

`checkRun.externalUpdatedAt` string

External update timestamp used to order updates so stale retries cannot replace newer state.

`checkRun.startedAt` string

Provider-reported RFC 3339 start time when supplied.

`checkRun.completedAt` string

Provider-reported RFC 3339 completion time when supplied.

`checkRun.createdAt` string

RFC 3339 run creation timestamp.

`checkRun.updatedAt` string

RFC 3339 timestamp for the latest persisted run update.

`checkRun.externalId` string

Provider identity for one attempt. Reuse it to update that attempt and use a new value for a retry.

`checkRun.actor` object

Public actor that produced the run.

`checkRun.actor.user` object

User variant of the actor. Set when a user performed the action.

`checkRun.actor.user.id` string

Public identifier for the user.

`checkRun.actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkRun.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRun.actor.app.id` string

Public identifier for the app.

`checkRun.actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkRun.actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkRun.actor.serviceAccount.id` string

Public identifier for the service account.

`checkRun.output` object

Human-readable result object containing title, summary, and longer text when supplied.

`checkRun.output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRun.output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "headSha": "HEAD_SHA",  "checkSuite": {    "key": "KEY",    "name": "NAME",    "externalId": "EXTERNAL_ID"  },  "checkRun": {    "key": "KEY",    "name": "NAME",    "status": "queued",    "externalUpdatedAt": "2026-01-01T00:00:00Z",    "externalId": "EXTERNAL_ID"  }}'
```

**Response shape:**

```
{  "checkSuite": {    "id": "string",    "repository": {      "id": "string",      "name": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      }    },    "sha": "string",    "key": "string",    "name": "string",    "detailsUrl": "string",    "createdAt": "2026-01-01T00:00:00Z",    "updatedAt": "2026-01-01T00:00:00Z",    "externalId": "string",    "actor": {      "user": {        "id": "string",        "email": "string"      }    }  },  "checkRun": {    "id": "string",    "repository": {      "id": "string",      "name": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      }    },    "checkSuite": {      "id": "string"    },    "sha": "string",    "key": "string",    "name": "string",    "status": "queued",    "conclusion": "success",    "detailsUrl": "string",    "externalUpdatedAt": "2026-01-01T00:00:00Z",    "startedAt": "2026-01-01T00:00:00Z",    "completedAt": "2026-01-01T00:00:00Z",    "createdAt": "2026-01-01T00:00:00Z",    "updatedAt": "2026-01-01T00:00:00Z",    "externalId": "string",    "actor": {      "user": {        "id": "string",        "email": "string"      }    },    "output": {      "title": "string",      "summary": "string",      "text": "string"    }  }}
```

### [Batch Upsert Check Runs](#batch-upsert-check-runs)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs:batchUpsert`

Atomically upserts several check runs belonging to one suite. The request accepts at most 10 runs and rejects duplicate `(external_id, key)` identities. Every run is committed or the entire request is rolled back.

#### [Path Parameters](#path-parameters-9)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-5)

`headSha` string Required

Head commit SHA the check runs are reported against (40- or 64-char hex).

`checkSuite` object Required

The suite shared by every check run in this request.

`checkSuite.key` string Required

Stable, app-chosen key identifying the logical suite across attempts.

`checkSuite.name` string Required

Human-facing suite name.

`checkSuite.detailsUrl` string

Optional link to more detail about the suite as a whole.

`checkSuite.externalId` string Required

Provider-assigned immutable identity for this suite attempt.

`checkRuns` array Required

Check runs to upsert, in response order. Must contain 1-10 entries with unique `(external_id, key)` identities.

`checkRuns[0].key` string Required

Stable, app-chosen key identifying the logical check across attempts.

`checkRuns[0].name` string Required

Human-facing check-run name.

`checkRuns[0].status` string Required

Allowed values: `CHECK_RUN_LIFECYCLE_STATUS_UNSPECIFIED`, `queued`, `in_progress`, `completed`.

`checkRuns[0].conclusion` string

Required iff `status == completed`. Allowed values: `CHECK_RUN_CONCLUSION_UNSPECIFIED`, `success`, `failure`, `neutral`, `cancelled`, `skipped`, `timed_out`, `action_required`, `stale`.

`checkRuns[0].externalUpdatedAt` string Required

The external system's last-update time. Used to order concurrent updates so a stale retry can't overwrite newer state.

`checkRuns[0].startedAt` string

When the check run started.

`checkRuns[0].completedAt` string

When the check run completed.

`checkRuns[0].detailsUrl` string

Optional link to more detail about this specific check run (e.g. the provider's job/build URL).

`checkRuns[0].externalId` string Required

Provider-assigned immutable identity for this check attempt.

`checkRuns[0].output` object

Human-readable output for this check run.

`checkRuns[0].output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRuns[0].output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRuns[0].output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

#### [Response Fields](#response-fields-15)

`checkSuite` object

The persisted suite shared by all returned check runs.

`checkSuite.id` string

Server-assigned check suite identifier.

`checkSuite.repository` object

Repository reference for the suite.

`checkSuite.repository.id` string

Repository identifier in a container reference.

`checkSuite.repository.name` string

Repository name in a container reference.

`checkSuite.repository.owner` object

Owner reference for the repository.

`checkSuite.repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkSuite.repository.owner.id` string

Origin owner identifier.

`checkSuite.repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkSuite.sha` string

Commit SHA to which the suite is attached.

`checkSuite.key` string

Stable app-chosen required-check identity. Required checks match on app plus this key, not name.

`checkSuite.name` string

Display-only suite name; it is not used for required-check matching.

`checkSuite.detailsUrl` string

Optional link to the provider's suite-level results.

`checkSuite.createdAt` string

RFC 3339 suite creation timestamp.

`checkSuite.updatedAt` string

RFC 3339 timestamp for the latest suite update.

`checkSuite.externalId` string

Provider identity for this suite attempt.

`checkSuite.actor` object

Public actor that produced the suite.

`checkSuite.actor.user` object

User variant of the actor. Set when a user performed the action.

`checkSuite.actor.user.id` string

Public identifier for the user.

`checkSuite.actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkSuite.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuite.actor.app.id` string

Public identifier for the app.

`checkSuite.actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkSuite.actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkSuite.actor.serviceAccount.id` string

Public identifier for the service account.

`checkRuns` array

Persisted check runs in the same order as the request.

`checkRuns[].id` string

Server-assigned check run identifier.

`checkRuns[].repository` object

Repository reference for the run.

`checkRuns[].repository.id` string

Repository identifier in a container reference.

`checkRuns[].repository.name` string

Repository name in a container reference.

`checkRuns[].repository.owner` object

Owner reference for the repository.

`checkRuns[].repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkRuns[].repository.owner.id` string

Origin owner identifier.

`checkRuns[].repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkRuns[].checkSuite` object

Reference to the containing check suite.

`checkRuns[].checkSuite.id` string

Server-assigned identifier of the containing check suite.

`checkRuns[].sha` string

Commit SHA to which the run is attached.

`checkRuns[].key` string

Stable app-chosen logical run identity; required checks may match on app, suite key, and this key.

`checkRuns[].name` string

Display-only run name; it is not used for required-check matching.

`checkRuns[].status` string

Lifecycle status; queued, in\_progress, or completed.

`checkRuns[].conclusion` string

Required for a completed run; success, failure, neutral, cancelled, skipped, timed\_out, action\_required, or stale.

`checkRuns[].detailsUrl` string

Separate link to the provider's full result page.

`checkRuns[].externalUpdatedAt` string

External update timestamp used to order updates so stale retries cannot replace newer state.

`checkRuns[].startedAt` string

Provider-reported RFC 3339 start time when supplied.

`checkRuns[].completedAt` string

Provider-reported RFC 3339 completion time when supplied.

`checkRuns[].createdAt` string

RFC 3339 run creation timestamp.

`checkRuns[].updatedAt` string

RFC 3339 timestamp for the latest persisted run update.

`checkRuns[].externalId` string

Provider identity for one attempt. Reuse it to update that attempt and use a new value for a retry.

`checkRuns[].actor` object

Public actor that produced the run.

`checkRuns[].actor.user` object

User variant of the actor. Set when a user performed the action.

`checkRuns[].actor.user.id` string

Public identifier for the user.

`checkRuns[].actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkRuns[].actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkRuns[].actor.serviceAccount.id` string

Public identifier for the service account.

`checkRuns[].output` object

Human-readable result object containing title, summary, and longer text when supplied.

`checkRuns[].output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRuns[].output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRuns[].output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs:batchUpsert' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "headSha": "HEAD_SHA",  "checkSuite": {    "key": "KEY",    "name": "NAME",    "externalId": "EXTERNAL_ID"  },  "checkRuns": [    {      "key": "KEY",      "name": "NAME",      "status": "queued",      "externalUpdatedAt": "2026-01-01T00:00:00Z",      "externalId": "EXTERNAL_ID"    }  ]}'
```

**Response shape:**

```
{  "checkSuite": {    "id": "string",    "repository": {      "id": "string",      "name": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      }    },    "sha": "string",    "key": "string",    "name": "string",    "detailsUrl": "string",    "createdAt": "2026-01-01T00:00:00Z",    "updatedAt": "2026-01-01T00:00:00Z",    "externalId": "string",    "actor": {      "user": {        "id": "string",        "email": "string"      }    }  },  "checkRuns": [    {      "id": "string",      "repository": {        "id": "string",        "name": "string",        "owner": {          "slug": "string",          "id": "string",          "type": "team"        }      },      "checkSuite": {        "id": "string"      },      "sha": "string",      "key": "string",      "name": "string",      "status": "queued",      "conclusion": "success",      "detailsUrl": "string",      "externalUpdatedAt": "2026-01-01T00:00:00Z",      "startedAt": "2026-01-01T00:00:00Z",      "completedAt": "2026-01-01T00:00:00Z",      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "externalId": "string",      "actor": {        "user": {          "id": "string",          "email": "string"        }      },      "output": {        "title": "string",        "summary": "string",        "text": "string"      }    }  ]}
```

### [Get Check Run](#get-check-run)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs/{checkRunId}`

Returns a single check run by server-assigned id (`cr_...`).

#### [Path Parameters](#path-parameters-10)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkRunId` string Required

Server-assigned check-run id (`cr_...`).

#### [Response Fields](#response-fields-16)

`id` string

Server-assigned check run identifier.

`repository` object

Repository reference for the run.

`repository.id` string

Repository identifier in a container reference.

`repository.name` string

Repository name in a container reference.

`repository.owner` object

Owner reference for the repository.

`repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`repository.owner.id` string

Origin owner identifier.

`repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkSuite` object

Reference to the containing check suite.

`checkSuite.id` string

Server-assigned identifier of the containing check suite.

`sha` string

Commit SHA to which the run is attached.

`key` string

Stable app-chosen logical run identity; required checks may match on app, suite key, and this key.

`name` string

Display-only run name; it is not used for required-check matching.

`status` string

Lifecycle status; queued, in\_progress, or completed.

`conclusion` string

Required for a completed run; success, failure, neutral, cancelled, skipped, timed\_out, action\_required, or stale.

`detailsUrl` string

Separate link to the provider's full result page.

`externalUpdatedAt` string

External update timestamp used to order updates so stale retries cannot replace newer state.

`startedAt` string

Provider-reported RFC 3339 start time when supplied.

`completedAt` string

Provider-reported RFC 3339 completion time when supplied.

`createdAt` string

RFC 3339 run creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest persisted run update.

`externalId` string

Provider identity for one attempt. Reuse it to update that attempt and use a new value for a retry.

`actor` object

Public actor that produced the run.

`actor.user` object

User variant of the actor. Set when a user performed the action.

`actor.user.id` string

Public identifier for the user.

`actor.user.email` string

Email address of the user. Always set when the user variant is present.

`actor.app` object

App variant of the actor. Set when an app performed the action.

`actor.app.id` string

Public identifier for the app.

`actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`actor.serviceAccount.id` string

Public identifier for the service account.

`output` object

Human-readable result object containing title, summary, and longer text when supplied.

`output.title` string

Short headline for the output. Maximum length: 255 characters.

`output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs/CHECK_RUN_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "repository": {    "id": "string",    "name": "string",    "owner": {      "slug": "string",      "id": "string",      "type": "team"    }  },  "checkSuite": {    "id": "string"  },  "sha": "string",  "key": "string",  "name": "string",  "status": "queued",  "conclusion": "success",  "detailsUrl": "string",  "externalUpdatedAt": "2026-01-01T00:00:00Z",  "startedAt": "2026-01-01T00:00:00Z",  "completedAt": "2026-01-01T00:00:00Z",  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "externalId": "string",  "actor": {    "user": {      "id": "string",      "email": "string"    }  },  "output": {    "title": "string",    "summary": "string",    "text": "string"  }}
```

### [Get Check Suite](#get-check-suite)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-suites/{checkSuiteId}`

Returns check suite metadata by server-assigned id (`crg_...`). Does not embed check runs; use `ListCheckRunsForSuite` for the suite's runs.

#### [Path Parameters](#path-parameters-11)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkSuiteId` string Required

Server-assigned check suite id (`crg_...`).

#### [Response Fields](#response-fields-17)

`id` string

Server-assigned check suite identifier.

`repository` object

Repository reference for the suite.

`repository.id` string

Repository identifier in a container reference.

`repository.name` string

Repository name in a container reference.

`repository.owner` object

Owner reference for the repository.

`repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`repository.owner.id` string

Origin owner identifier.

`repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`sha` string

Commit SHA to which the suite is attached.

`key` string

Stable app-chosen required-check identity. Required checks match on app plus this key, not name.

`name` string

Display-only suite name; it is not used for required-check matching.

`detailsUrl` string

Optional link to the provider's suite-level results.

`createdAt` string

RFC 3339 suite creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest suite update.

`externalId` string

Provider identity for this suite attempt.

`actor` object

Public actor that produced the suite.

`actor.user` object

User variant of the actor. Set when a user performed the action.

`actor.user.id` string

Public identifier for the user.

`actor.user.email` string

Email address of the user. Always set when the user variant is present.

`actor.app` object

App variant of the actor. Set when an app performed the action.

`actor.app.id` string

Public identifier for the app.

`actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`actor.serviceAccount.id` string

Public identifier for the service account.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-suites/CHECK_SUITE_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "repository": {    "id": "string",    "name": "string",    "owner": {      "slug": "string",      "id": "string",      "type": "team"    }  },  "sha": "string",  "key": "string",  "name": "string",  "detailsUrl": "string",  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "externalId": "string",  "actor": {    "user": {      "id": "string",      "email": "string"    }  }}
```

### [List Check Runs For Suite](#list-check-runs-for-suite)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-suites/{checkSuiteId}/check-runs`

Lists check runs belonging to a suite. Paginated.

#### [Path Parameters](#path-parameters-12)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkSuiteId` string Required

Server-assigned check suite id (`crg_...`).

#### [Query Parameters](#query-parameters-5)

`pageSize` integer

Max check runs to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-run id scoped to this suite, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-18)

`checkRuns` array

Paginated check runs belonging to the named suite.

`checkRuns[].id` string

Server-assigned check run identifier.

`checkRuns[].repository` object

Repository reference for the run.

`checkRuns[].repository.id` string

Repository identifier in a container reference.

`checkRuns[].repository.name` string

Repository name in a container reference.

`checkRuns[].repository.owner` object

Owner reference for the repository.

`checkRuns[].repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkRuns[].repository.owner.id` string

Origin owner identifier.

`checkRuns[].repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkRuns[].checkSuite` object

Reference to the containing check suite.

`checkRuns[].checkSuite.id` string

Server-assigned identifier of the containing check suite.

`checkRuns[].sha` string

Commit SHA to which the run is attached.

`checkRuns[].key` string

Stable app-chosen logical run identity; required checks may match on app, suite key, and this key.

`checkRuns[].name` string

Display-only run name; it is not used for required-check matching.

`checkRuns[].status` string

Lifecycle status; queued, in\_progress, or completed.

`checkRuns[].conclusion` string

Required for a completed run; success, failure, neutral, cancelled, skipped, timed\_out, action\_required, or stale.

`checkRuns[].detailsUrl` string

Separate link to the provider's full result page.

`checkRuns[].externalUpdatedAt` string

External update timestamp used to order updates so stale retries cannot replace newer state.

`checkRuns[].startedAt` string

Provider-reported RFC 3339 start time when supplied.

`checkRuns[].completedAt` string

Provider-reported RFC 3339 completion time when supplied.

`checkRuns[].createdAt` string

RFC 3339 run creation timestamp.

`checkRuns[].updatedAt` string

RFC 3339 timestamp for the latest persisted run update.

`checkRuns[].externalId` string

Provider identity for one attempt. Reuse it to update that attempt and use a new value for a retry.

`checkRuns[].actor` object

Public actor that produced the run.

`checkRuns[].actor.user` object

User variant of the actor. Set when a user performed the action.

`checkRuns[].actor.user.id` string

Public identifier for the user.

`checkRuns[].actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkRuns[].actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkRuns[].actor.serviceAccount.id` string

Public identifier for the service account.

`checkRuns[].output` object

Human-readable result object containing title, summary, and longer text when supplied.

`checkRuns[].output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRuns[].output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRuns[].output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-suites/CHECK_SUITE_ID/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "checkRuns": [    {      "id": "string",      "repository": {        "id": "string",        "name": "string",        "owner": {          "slug": "string",          "id": "string",          "type": "team"        }      },      "checkSuite": {        "id": "string"      },      "sha": "string",      "key": "string",      "name": "string",      "status": "queued",      "conclusion": "success",      "detailsUrl": "string",      "externalUpdatedAt": "2026-01-01T00:00:00Z",      "startedAt": "2026-01-01T00:00:00Z",      "completedAt": "2026-01-01T00:00:00Z",      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "externalId": "string",      "actor": {        "user": {          "id": "string",          "email": "string"        }      },      "output": {        "title": "string",        "summary": "string",        "text": "string"      }    }  ],  "nextPageToken": "string"}
```

### [List Check Runs For Commit](#list-check-runs-for-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/check-runs`

Lists every check run reported against a commit, across all suites. Paginated.

#### [Path Parameters](#path-parameters-13)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Commit SHA (40- or 64-char hex) to list check runs for.

#### [Query Parameters](#query-parameters-6)

`pageSize` integer

Max check runs to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-run id scoped to this commit, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-19)

`checkRuns` array

Paginated check runs attached to the resolved commit SHA.

`checkRuns[].id` string

Server-assigned check run identifier.

`checkRuns[].repository` object

Repository reference for the run.

`checkRuns[].repository.id` string

Repository identifier in a container reference.

`checkRuns[].repository.name` string

Repository name in a container reference.

`checkRuns[].repository.owner` object

Owner reference for the repository.

`checkRuns[].repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkRuns[].repository.owner.id` string

Origin owner identifier.

`checkRuns[].repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkRuns[].checkSuite` object

Reference to the containing check suite.

`checkRuns[].checkSuite.id` string

Server-assigned identifier of the containing check suite.

`checkRuns[].sha` string

Commit SHA to which the run is attached.

`checkRuns[].key` string

Stable app-chosen logical run identity; required checks may match on app, suite key, and this key.

`checkRuns[].name` string

Display-only run name; it is not used for required-check matching.

`checkRuns[].status` string

Lifecycle status; queued, in\_progress, or completed.

`checkRuns[].conclusion` string

Required for a completed run; success, failure, neutral, cancelled, skipped, timed\_out, action\_required, or stale.

`checkRuns[].detailsUrl` string

Separate link to the provider's full result page.

`checkRuns[].externalUpdatedAt` string

External update timestamp used to order updates so stale retries cannot replace newer state.

`checkRuns[].startedAt` string

Provider-reported RFC 3339 start time when supplied.

`checkRuns[].completedAt` string

Provider-reported RFC 3339 completion time when supplied.

`checkRuns[].createdAt` string

RFC 3339 run creation timestamp.

`checkRuns[].updatedAt` string

RFC 3339 timestamp for the latest persisted run update.

`checkRuns[].externalId` string

Provider identity for one attempt. Reuse it to update that attempt and use a new value for a retry.

`checkRuns[].actor` object

Public actor that produced the run.

`checkRuns[].actor.user` object

User variant of the actor. Set when a user performed the action.

`checkRuns[].actor.user.id` string

Public identifier for the user.

`checkRuns[].actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkRuns[].actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkRuns[].actor.serviceAccount.id` string

Public identifier for the service account.

`checkRuns[].output` object

Human-readable result object containing title, summary, and longer text when supplied.

`checkRuns[].output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRuns[].output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRuns[].output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits/SHA/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "checkRuns": [    {      "id": "string",      "repository": {        "id": "string",        "name": "string",        "owner": {          "slug": "string",          "id": "string",          "type": "team"        }      },      "checkSuite": {        "id": "string"      },      "sha": "string",      "key": "string",      "name": "string",      "status": "queued",      "conclusion": "success",      "detailsUrl": "string",      "externalUpdatedAt": "2026-01-01T00:00:00Z",      "startedAt": "2026-01-01T00:00:00Z",      "completedAt": "2026-01-01T00:00:00Z",      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "externalId": "string",      "actor": {        "user": {          "id": "string",          "email": "string"        }      },      "output": {        "title": "string",        "summary": "string",        "text": "string"      }    }  ],  "nextPageToken": "string"}
```

### [List Check Suites For Commit](#list-check-suites-for-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/check-suites`

Lists check suites reported against a commit. Returns suite metadata only (no embedded runs). Paginated.

#### [Path Parameters](#path-parameters-14)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Commit SHA (40- or 64-char hex) to list suites for.

#### [Query Parameters](#query-parameters-7)

`pageSize` integer

Max suites to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-suite id scoped to this commit, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-20)

`checkSuites` array

Paginated check suites attached to the resolved commit SHA.

`checkSuites[].id` string

Server-assigned check suite identifier.

`checkSuites[].repository` object

Repository reference for the suite.

`checkSuites[].repository.id` string

Repository identifier in a container reference.

`checkSuites[].repository.name` string

Repository name in a container reference.

`checkSuites[].repository.owner` object

Owner reference for the repository.

`checkSuites[].repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`checkSuites[].repository.owner.id` string

Origin owner identifier.

`checkSuites[].repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`checkSuites[].sha` string

Commit SHA to which the suite is attached.

`checkSuites[].key` string

Stable app-chosen required-check identity. Required checks match on app plus this key, not name.

`checkSuites[].name` string

Display-only suite name; it is not used for required-check matching.

`checkSuites[].detailsUrl` string

Optional link to the provider's suite-level results.

`checkSuites[].createdAt` string

RFC 3339 suite creation timestamp.

`checkSuites[].updatedAt` string

RFC 3339 timestamp for the latest suite update.

`checkSuites[].externalId` string

Provider identity for this suite attempt.

`checkSuites[].actor` object

Public actor that produced the suite.

`checkSuites[].actor.user` object

User variant of the actor. Set when a user performed the action.

`checkSuites[].actor.user.id` string

Public identifier for the user.

`checkSuites[].actor.user.email` string

Email address of the user. Always set when the user variant is present.

`checkSuites[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuites[].actor.app.id` string

Public identifier for the app.

`checkSuites[].actor.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`checkSuites[].actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`checkSuites[].actor.serviceAccount.id` string

Public identifier for the service account.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits/SHA/check-suites' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "checkSuites": [    {      "id": "string",      "repository": {        "id": "string",        "name": "string",        "owner": {          "slug": "string",          "id": "string",          "type": "team"        }      },      "sha": "string",      "key": "string",      "name": "string",      "detailsUrl": "string",      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "externalId": "string",      "actor": {        "user": {          "id": "string",          "email": "string"        }      }    }  ],  "nextPageToken": "string"}
```

## [Commits and contents](#commits-and-contents)

A commit separates git-object metadata under `commit` from top-level repository relationships. List responses omit `stats`; [Get Commit](#get-commit) includes whole-commit aggregate `stats`. Changed files are returned only by the paginated [List Commit Files](#list-commit-files) collection. `author` and `committer` are git identities recorded in the commit, not Origin user objects.

A comparison is a summary only: it never embeds commit lists or file diffs. `status` is exactly `identical`, `ahead`, `behind`, or `diverged`; `aheadBy` and `behindBy` are commit counts. `baseCommit`, `headCommit`, and `mergeBaseCommit` use the sparse commit projection (no `stats` or files).

### [List Commits](#list-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits`

Lists commits on a branch or starting ref.

List results omit `stats`. Use [Get Commit](#get-commit) for aggregate stats and [List Commit Files](#list-commit-files) for the paginated file diff.

#### [Path Parameters](#path-parameters-15)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-8)

`sha` string

SHA, branch, tag, or symbolic ref (for example `HEAD`) to start listing from. Empty means the repo's default branch.

`pageSize` integer

Max commits to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the starting ref and page, so `sha`/`page_size` on a follow-up request are ignored when a token is supplied.

#### [Response Fields](#response-fields-21)

`commits` array

Sparse commits with no stats; changed files are not embedded.

`commits[].sha` string

Full commit SHA.

`commits[].commit` object

Git-object metadata nested separately from top-level repository relationships.

`commits[].commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`commits[].commit.author.name` string

Name recorded in the Git author identity.

`commits[].commit.author.email` string

Email recorded in the Git author identity.

`commits[].commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`commits[].commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`commits[].commit.committer.name` string

Name recorded in the Git identity.

`commits[].commit.committer.email` string

Email recorded in the Git identity.

`commits[].commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`commits[].commit.message` string

Commit message.

`commits[].commit.tree` object

Tree referenced by the commit.

`commits[].commit.tree.sha` string

SHA of the tree referenced by the commit.

`commits[].parents` array

Parent commit references, each containing a SHA.

`commits[].parents[].sha` string

Parent commit SHA.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "commits": [    {      "sha": "string",      "commit": {        "author": {          "name": "string",          "email": "string",          "date": "string"        },        "committer": {          "name": "string",          "email": "string",          "date": "string"        },        "message": "string",        "tree": {          "sha": "string"        }      },      "parents": [        {          "sha": "string"        }      ]    }  ],  "nextPageToken": "string"}
```

### [Get Commit](#get-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}`

Returns a single commit by SHA or ref with whole-commit aggregate `stats`. It does not include changed files; use [List Commit Files](#list-commit-files).

`author` and `committer` are git identities recorded in the commit, not Origin user objects.

#### [Path Parameters](#path-parameters-16)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

SHA, branch, tag, or symbolic ref (for example `HEAD`) of the commit to fetch.

#### [Response Fields](#response-fields-22)

`sha` string

Full commit SHA.

`commit` object

Git-object metadata nested separately from top-level repository relationships.

`commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`commit.author.name` string

Name recorded in the Git author identity.

`commit.author.email` string

Email recorded in the Git author identity.

`commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`commit.committer.name` string

Name recorded in the Git identity.

`commit.committer.email` string

Email recorded in the Git identity.

`commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`commit.message` string

Commit message.

`commit.tree` object

Tree referenced by the commit.

`commit.tree.sha` string

SHA of the tree referenced by the commit.

`parents` array

Parent commit references, each containing a SHA.

`parents[].sha` string

Parent commit SHA.

`stats` object

Whole-commit aggregate additions, deletions, and total; included by get-commit and omitted by list projections.

`stats.additions` integer

Aggregate added lines for the commit.

`stats.deletions` integer

Aggregate deleted lines for the commit.

`stats.total` integer

Aggregate additions plus deletions for the commit.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits/SHA' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "sha": "string",  "commit": {    "author": {      "name": "string",      "email": "string",      "date": "string"    },    "committer": {      "name": "string",      "email": "string",      "date": "string"    },    "message": "string",    "tree": {      "sha": "string"    }  },  "parents": [    {      "sha": "string"    }  ],  "stats": {    "additions": 0,    "deletions": 0,    "total": 0  }}
```

### [List Commit Files](#list-commit-files)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/files`

Lists the files changed by a commit.

`sha` may be a commit SHA, branch, tag, or symbolic ref such as `HEAD`. Results default to 30 files and are capped at 100. A page token fixes the resolved commit, page size, and file cursor; on later requests, `sha` and `pageSize` must match the token. Each file includes `filename`, `status`, `additions`, `deletions`, `changes`, `patch`, and `previousFilename` when renamed or copied. `patch` is empty for binary files.

#### [Path Parameters](#path-parameters-17)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

SHA, branch, tag, or symbolic ref (for example `HEAD`) of the commit whose files should be listed.

#### [Query Parameters](#query-parameters-9)

`pageSize` integer

Max changed files to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token fixes the resolved commit, page size, and file cursor, so `sha` and `page_size` on a follow-up request must match the token.

#### [Response Fields](#response-fields-23)

`files` array

Paginated changed files with filename, status, line counts, patch, and previousFilename for renamed or copied files. Binary patches are empty.

`files[].filename` string

Path of the changed file.

`files[].status` string

Change status; added, removed, modified, renamed, or copied.

`files[].additions` integer

Added line count for the file.

`files[].deletions` integer

Deleted line count for the file.

`files[].changes` integer

Total changed line count for the file.

`files[].patch` string

Unified patch; empty for binary files.

`files[].previousFilename` string

Previous path when the file was renamed or copied.

`nextPageToken` string

Token fixes the resolved commit, page size, and file cursor; subsequent sha and pageSize values must match it.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits/SHA/files' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "files": [    {      "filename": "string",      "status": "string",      "additions": 0,      "deletions": 0,      "changes": 0,      "patch": "string",      "previousFilename": "string"    }  ],  "nextPageToken": "string"}
```

### [Compare Commits](#compare-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/compare/{basehead}`

Compares commits, refs, or tags relative to their merge base. `basehead` is `"{base}...{head}"`; refs containing "/" must use their SHA.

`base` and `head` may each be a SHA, branch, tag, or symbolic ref such as `HEAD`. The response is an unpaginated summary: `status` is `identical`, `ahead`, `behind`, or `diverged`; the three commit objects are sparse and omit `stats` and files. No `totalCommits`, embedded `commits`, or `files` fields are returned. Unrelated histories return `404`.

#### [Path Parameters](#path-parameters-18)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`basehead` string Required

`"{base}...{head}"`, where either revision may be a SHA, branch, tag, or symbolic ref such as `HEAD`.

#### [Response Fields](#response-fields-24)

`status` string

Comparison state; exactly identical, ahead, behind, or diverged.

`aheadBy` integer

Number of commits by which the head is ahead.

`behindBy` integer

Number of commits by which the head is behind.

`baseCommit` object

Sparse resolved base commit with no stats or files.

`baseCommit.sha` string

Full commit SHA.

`baseCommit.commit` object

Git-object metadata nested separately from top-level repository relationships.

`baseCommit.commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`baseCommit.commit.author.name` string

Name recorded in the Git author identity.

`baseCommit.commit.author.email` string

Email recorded in the Git author identity.

`baseCommit.commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`baseCommit.commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`baseCommit.commit.committer.name` string

Name recorded in the Git identity.

`baseCommit.commit.committer.email` string

Email recorded in the Git identity.

`baseCommit.commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`baseCommit.commit.message` string

Commit message.

`baseCommit.commit.tree` object

Tree referenced by the commit.

`baseCommit.commit.tree.sha` string

SHA of the tree referenced by the commit.

`baseCommit.parents` array

Parent commit references, each containing a SHA.

`baseCommit.parents[].sha` string

Parent commit SHA.

`headCommit` object

Sparse resolved head commit with no stats or files.

`headCommit.sha` string

Full commit SHA.

`headCommit.commit` object

Git-object metadata nested separately from top-level repository relationships.

`headCommit.commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`headCommit.commit.author.name` string

Name recorded in the Git author identity.

`headCommit.commit.author.email` string

Email recorded in the Git author identity.

`headCommit.commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`headCommit.commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`headCommit.commit.committer.name` string

Name recorded in the Git identity.

`headCommit.commit.committer.email` string

Email recorded in the Git identity.

`headCommit.commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`headCommit.commit.message` string

Commit message.

`headCommit.commit.tree` object

Tree referenced by the commit.

`headCommit.commit.tree.sha` string

SHA of the tree referenced by the commit.

`headCommit.parents` array

Parent commit references, each containing a SHA.

`headCommit.parents[].sha` string

Parent commit SHA.

`mergeBaseCommit` object

Sparse merge-base commit with no stats or files.

`mergeBaseCommit.sha` string

Full commit SHA.

`mergeBaseCommit.commit` object

Git-object metadata nested separately from top-level repository relationships.

`mergeBaseCommit.commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`mergeBaseCommit.commit.author.name` string

Name recorded in the Git author identity.

`mergeBaseCommit.commit.author.email` string

Email recorded in the Git author identity.

`mergeBaseCommit.commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`mergeBaseCommit.commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`mergeBaseCommit.commit.committer.name` string

Name recorded in the Git identity.

`mergeBaseCommit.commit.committer.email` string

Email recorded in the Git identity.

`mergeBaseCommit.commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`mergeBaseCommit.commit.message` string

Commit message.

`mergeBaseCommit.commit.tree` object

Tree referenced by the commit.

`mergeBaseCommit.commit.tree.sha` string

SHA of the tree referenced by the commit.

`mergeBaseCommit.parents` array

Parent commit references, each containing a SHA.

`mergeBaseCommit.parents[].sha` string

Parent commit SHA.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/compare/BASE...HEAD' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "status": "identical",  "aheadBy": 0,  "behindBy": 0,  "baseCommit": {    "sha": "string",    "commit": {      "author": {        "name": "string",        "email": "string",        "date": "string"      },      "committer": {        "name": "string",        "email": "string",        "date": "string"      },      "message": "string",      "tree": {        "sha": "string"      }    },    "parents": [      {        "sha": "string"      }    ]  },  "headCommit": {    "sha": "string",    "commit": {      "author": {        "name": "string",        "email": "string",        "date": "string"      },      "committer": {        "name": "string",        "email": "string",        "date": "string"      },      "message": "string",      "tree": {        "sha": "string"      }    },    "parents": [      {        "sha": "string"      }    ]  },  "mergeBaseCommit": {    "sha": "string",    "commit": {      "author": {        "name": "string",        "email": "string",        "date": "string"      },      "committer": {        "name": "string",        "email": "string",        "date": "string"      },      "message": "string",      "tree": {        "sha": "string"      }    },    "parents": [      {        "sha": "string"      }    ]  }}
```

### [Get Contents](#get-contents)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/contents`

Returns file or directory contents at a ref. The file path is passed as the `path` query parameter (supports nested paths); omit or leave empty for the repository root directory. Files larger than 1 MiB (decoded) are rejected with `FailedPrecondition` (HTTP 400).

Files contain base64 content. Directories contain immediate children in `entries`. Directory entries are sparse children containing `type`, `name`, `path`, `sha`, and `size`; fetch a child path to read its content.

#### [Path Parameters](#path-parameters-19)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-10)

`path` string

Path to the file or directory relative to the repository root. Empty requests the root directory.

`ref` string

Commit, branch, tag, or symbolic ref (for example `HEAD`) to read from. Empty means the repository's default branch.

#### [Response Fields](#response-fields-25)

`type` string

Content kind; file or dir.

`encoding` string

File encoding; file responses use base64.

`size` string

Decoded content size in bytes, encoded as a JSON string under the API's 64-bit integer convention. File payloads larger than 1 MiB are rejected.

`name` string

Base name of the file or directory.

`path` string

Path relative to the repository root.

`sha` string

Blob SHA for a file or tree SHA for a directory.

`content` string

Base64-encoded file body; present for a fetched file.

`entries` array

Immediate sparse children of a directory. Entries contain type, name, path, sha, and size; fetch a child path to read its content.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/contents' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "type": "string",  "encoding": "string",  "size": "string",  "name": "string",  "path": "string",  "sha": "string",  "content": "string",  "entries": [    {      "type": "string",      "encoding": "string",      "size": "string",      "name": "string",      "path": "string",      "sha": "string",      "content": "string",      "entries": [        {          "type": "string",          "encoding": "string",          "size": "string",          "name": "string",          "path": "string",          "sha": "string",          "content": "string",          "entries": [            {}          ]        }      ]    }  ]}
```

### [Batch Get Contents](#batch-get-contents)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/contents:batchGet`

Returns the contents of several explicit paths at a ref in one request. Each requested path yields a result marking whether it was found; a found path carries the same `Content` shape as `GetContents` (files as base64, directories as immediate `entries`, symlinks as files). Paths are matched exactly, with no globs or patterns, and at most 20 may be requested; duplicates are removed. Response results preserve first-seen request order. A single file larger than the [Get Contents](#get-contents) 1 MiB cap fails the whole batch with `FailedPrecondition` (HTTP 400). Uses POST because the path list travels in the request body.

#### [Path Parameters](#path-parameters-20)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-6)

`paths` array Required

Exact paths to fetch, relative to the repository root (no globs or patterns). At most 20 entries; duplicates are removed. An empty string requests the repository root directory.

`ref` string

Commit, branch, tag, or symbolic ref (for example `HEAD`) to read from. Empty means the repository's default branch.

#### [Response Fields](#response-fields-26)

`results` array

One result per returned exact path, preserving first-seen request order.

`results[].path` string

Requested path corresponding to this result.

`results[].found` boolean

Whether the requested path exists at the resolved commit.

`results[].content` object

Content value when found is true; omitted when found is false.

`results[].content.type` string

Content kind; file or dir.

`results[].content.encoding` string

File encoding; file responses use base64.

`results[].content.size` string

Decoded content size in bytes, encoded as a JSON string under the API's 64-bit integer convention. File payloads larger than 1 MiB are rejected.

`results[].content.name` string

Base name of the file or directory.

`results[].content.path` string

Path relative to the repository root.

`results[].content.sha` string

Blob SHA for a file or tree SHA for a directory.

`results[].content.content` string

Base64-encoded file body; present for a fetched file.

`results[].content.entries` array

Immediate sparse children of a directory. Entries contain type, name, path, sha, and size; fetch a child path to read its content.

`resolvedCommitSha` string

Commit SHA to which the requested ref resolved.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/contents:batchGet' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "paths": [    "PATH"  ]}'
```

**Response shape:**

```
{  "results": [    {      "path": "string",      "found": false,      "content": {        "type": "string",        "encoding": "string",        "size": "string",        "name": "string",        "path": "string",        "sha": "string",        "content": "string",        "entries": [          {}        ]      }    }  ],  "resolvedCommitSha": "string"}
```

## [Git data](#git-data)

Low-level git objects. Scope: `repository:contents:read`. Empty repositories return `409`.

### [Get Blob](#get-blob)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/blobs/{sha}`

Returns a Git blob object by SHA. Default response is JSON with MIME-wrapped base64 `content`. Pass `Accept: application/vnd.origin.raw+json` (or `application/vnd.origin.raw`) on the REST surface to receive raw blob bytes instead. Blobs larger than 4 MiB (decoded) are rejected; fetch larger files by cloning the repository over [Git HTTPS](#git-https-authentication). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-21)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the blob object.

#### [Response Fields](#response-fields-27)

`sha` string

Git blob object SHA.

`size` integer

Decoded blob size as a JSON number; blobs larger than 4 MiB are rejected by the JSON endpoint.

`encoding` string

JSON blob responses use base64 encoding.

`content` string

Base64-encoded blob bytes; callers may request raw bytes with Accept: application/vnd.origin.raw.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/blobs/SHA' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "sha": "string",  "size": 0,  "encoding": "string",  "content": "string"}
```

### [Get Git Commit](#get-git-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/commits/{sha}`

Returns a Git commit object by SHA (or resolvable revision). This is the low-level Git Database commit shape (flat author/message/tree), not the higher-level `GetCommit` resource under `/commits/{sha}`. `sha` accepts a commit SHA, branch, tag, or symbolic ref such as `HEAD`. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-22)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the commit object, or a branch, tag, or symbolic ref such as `HEAD`.

#### [Response Fields](#response-fields-28)

`sha` string

Full hex commit SHA.

`author` object

Author signature from the git object.

`author.name` string

Name recorded in the Git identity.

`author.email` string

Email recorded in the Git identity.

`author.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`committer` object

Committer signature from the git object.

`committer.name` string

Name recorded in the Git identity.

`committer.email` string

Email recorded in the Git identity.

`committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`message` string

Full commit message.

`tree` object

Tree this commit points at.

`tree.sha` string

SHA of the tree referenced by the commit.

`parents` array

Parent commit SHAs (empty for a root commit).

`parents[].sha` string

Parent commit SHA.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/commits/SHA' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "sha": "string",  "author": {    "name": "string",    "email": "string",    "date": "string"  },  "committer": {    "name": "string",    "email": "string",    "date": "string"  },  "message": "string",  "tree": {    "sha": "string"  },  "parents": [    {      "sha": "string"    }  ]}
```

### [Get Git Ref](#get-git-ref)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/ref/{ref}`

Returns a single Git reference by name. `ref` is typically `heads/<branch>` or `tags/<tag>` (with or without a leading `refs/`), or the symbolic `HEAD`. Exact match only; use ListMatchingGitRefs for prefixes. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-23)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`ref` string Required

Git reference name. Typically `heads/<branch>` or `tags/<tag>`; a leading `refs/` is accepted and normalized. The symbolic `HEAD` is also accepted (returned as `ref: "HEAD"` with the tip commit). Exact match on the full ref name.

#### [Response Fields](#response-fields-29)

`ref` string

Full ref name, e.g. "refs/heads/main".

`object` object

Object this ref points at directly (unpeeled). For annotated tags, `object.type` is "tag" and `object.sha` is the tag object SHA.

`object.sha` string

Hex SHA of the target object.

`object.type` string

One of "commit", "tree", "blob", or "tag".

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/ref/REF' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "ref": "string",  "object": {    "sha": "string",    "type": "string"  }}
```

### [List Matching Git Refs](#list-matching-git-refs)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/matching-refs`

Lists Git references whose names start with the given prefix. REST responses unwrap to a JSON array (via `response_body`). A trailing slash on `ref` is preserved (`heads/` → `refs/heads/`). The symbolic `HEAD` is matched exactly (it is not under `refs/`). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-24)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-11)

`ref` string

Prefix to match. Typically `heads/<prefix>` or `tags/<prefix>`; a leading `refs/` is accepted and normalized. Empty lists all refs (REST binding without a trailing path segment).

#### [Response Fields](#response-fields-30)

The response is an array. Each item contains:

`ref` string

Full ref name, e.g. "refs/heads/main".

`object` object

Object this ref points at directly (unpeeled). For annotated tags, `object.type` is "tag" and `object.sha` is the tag object SHA.

`object.sha` string

Hex SHA of the target object.

`object.type` string

One of "commit", "tree", "blob", or "tag".

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/matching-refs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
[  {    "ref": "string",    "object": {      "sha": "string",      "type": "string"    }  }]
```

### [List Matching Git Refs by Path](#list-matching-git-refs-by-path)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/matching-refs/{ref}`

Lists Git references whose names start with the given prefix. REST responses unwrap to a JSON array (via `response_body`). A trailing slash on `ref` is preserved (`heads/` → `refs/heads/`). The symbolic `HEAD` is matched exactly (it is not under `refs/`). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-25)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`ref` string Required

Prefix to match. Typically `heads/<prefix>` or `tags/<prefix>`; a leading `refs/` is accepted and normalized. Empty lists all refs (REST binding without a trailing path segment).

#### [Response Fields](#response-fields-31)

The response is an array. Each item contains:

`ref` string

Full ref name, e.g. "refs/heads/main".

`object` object

Object this ref points at directly (unpeeled). For annotated tags, `object.type` is "tag" and `object.sha` is the tag object SHA.

`object.sha` string

Hex SHA of the target object.

`object.type` string

One of "commit", "tree", "blob", or "tag".

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/matching-refs/REF' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
[  {    "ref": "string",    "object": {      "sha": "string",      "type": "string"    }  }]
```

### [Get Tag](#get-tag)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/tags/{sha}`

Returns an annotated Git tag object by SHA. Lightweight tags are not tag objects and return NotFound. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-26)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the annotated tag object.

#### [Response Fields](#response-fields-32)

`sha` string

Tag object SHA (hex).

`tag` string

Tag name, e.g. "v1.0".

`message` string

Tag message.

`tagger` object

Tagger signature from the tag object.

`tagger.name` string

Name recorded in the Git identity.

`tagger.email` string

Email recorded in the Git identity.

`tagger.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`object` object

Object this tag points at.

`object.sha` string

Hex SHA of the target object.

`object.type` string

One of "commit", "tree", "blob", or "tag".

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/tags/SHA' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "sha": "string",  "tag": "string",  "message": "string",  "tagger": {    "name": "string",    "email": "string",    "date": "string"  },  "object": {    "sha": "string",    "type": "string"  }}
```

### [Get Tree](#get-tree)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/trees/{sha}`

Returns a Git tree object by SHA or resolvable revision. `sha` accepts a tree SHA, commit SHA, branch, tag, or symbolic ref such as `HEAD`. Set `recursive=true` (or `1`) to walk the whole tree; omitting the parameter or passing any other value lists immediate children only. Recursive listings truncate at 100,000 entries or 7 MiB and set `truncated=true`. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-27)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Tree SHA, commit SHA, branch, tag, or symbolic ref such as `HEAD`.

#### [Query Parameters](#query-parameters-12)

`recursive` boolean

When true, returns the full recursive walk of the tree. Query values `true` and `1` enable recursion; omitting the parameter or passing any other value (including `false` and `0`) lists immediate children only.

#### [Response Fields](#response-fields-33)

`sha` string

Tree object SHA (hex).

`tree` array

Entries under this tree (immediate children, or the full recursive walk).

`tree[].path` string

Path relative to the requested tree root.

`tree[].mode` string

Git mode as an octal string: "100644", "100755", "040000", "120000", "160000".

`tree[].type` string

One of "blob", "tree", or "commit" (gitlink/submodule).

`tree[].sha` string

Object SHA (hex).

`tree[].size` integer

Blob size in bytes. Unset for trees and gitlinks. `int32` ensures REST JSON emits a number; individual blobs over 2 GiB are not representable.

`truncated` boolean

May be true when a recursive tree listing is truncated.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/trees/SHA' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "sha": "string",  "tree": [    {      "path": "string",      "mode": "string",      "type": "string",      "sha": "string",      "size": 0    }  ],  "truncated": false}
```

## [Pull requests](#pull-requests)

Closed or merged pull requests may additionally include `closedAt`, `mergedAt`, and `mergeCommitSha`. Treat `head.ref` and `base.ref` as opaque Origin ref strings; they may be short branch names or fully qualified `refs/heads/…` values.

Review `verdict` is `approve`, `request_changes`, or `comment`. `submittedAt` is absent for an unsubmitted draft review. `dismissal` is absent while the verdict remains active. Dismissed reviews remain visible in review listings. Reviews automatically superseded by a newer decision carry a server-generated message.

Comments expose a `thread` reference for grouping. Create-comment requests still accept the scalar `threadId` command parameter when replying. First-class thread resources and resolution APIs are not part of this release.

### [List Pull Requests](#list-pull-requests)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls`

Lists pull requests in a repo, optionally filtered by head branch and state. Each pull request includes its assigned labels.

#### [Path Parameters](#path-parameters-28)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-13)

`head` string

Optional exact branch (head-ref) filter. Omit to list across every branch.

`state` string

"open" | "closed" | "all". Defaults to "open".

`pageSize` integer

Maximum results to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque token from the preceding page.

#### [Response Fields](#response-fields-34)

`pullRequests` array

Page of PullRequest snapshots; response numbers and version numbers are JSON strings.

`pullRequests[].id` string

Stable Origin pull request identifier.

`pullRequests[].number` string

Repository-local pull request number encoded as a JSON string.

`pullRequests[].state` string

Pull request state; open or closed. Merged pull requests are closed with merged set true.

`pullRequests[].draft` boolean

Whether the pull request is a draft.

`pullRequests[].merged` boolean

Whether the pull request has merged.

`pullRequests[].title` string

Pull request title.

`pullRequests[].body` string

Pull request description body.

`pullRequests[].head` object

The source side of the change - what is being merged in.

`pullRequests[].head.ref` string

The ref this side points at, as Origin records it.

`pullRequests[].head.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequests[].base` object

The target side of the change — what it merges into.

`pullRequests[].base.ref` string

The ref this side points at, as Origin records it.

`pullRequests[].base.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequests[].author` object

Public actor that opened the pull request.

`pullRequests[].author.user` object

User variant of the actor. Set when a user performed the action.

`pullRequests[].author.user.id` string

Public identifier for the user.

`pullRequests[].author.user.email` string

Email address of the user. Always set when the user variant is present.

`pullRequests[].author.app` object

App variant of the actor. Set when an app performed the action.

`pullRequests[].author.app.id` string

Public identifier for the app.

`pullRequests[].author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`pullRequests[].author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`pullRequests[].author.serviceAccount.id` string

Public identifier for the service account.

`pullRequests[].createdAt` string

RFC 3339 pull request creation timestamp.

`pullRequests[].updatedAt` string

RFC 3339 timestamp for the latest pull request update.

`pullRequests[].closedAt` string

RFC 3339 close timestamp; may appear on closed or merged pull requests.

`pullRequests[].mergedAt` string

RFC 3339 merge timestamp; may appear on merged pull requests.

`pullRequests[].mergeCommitSha` string

Merge commit SHA; may appear after merge.

`pullRequests[].additions` integer

Added lines in the current pull request version.

`pullRequests[].deletions` integer

Deleted lines in the current pull request version.

`pullRequests[].changedFiles` integer

Changed file count in the current pull request version.

`pullRequests[].labels` array

Labels currently assigned to the pull request, sorted by name. Empty when none are assigned.

`pullRequests[].labels[].id` string

Public identifier for the label.

`pullRequests[].labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`pullRequests[].labels[].color` string

Six-character hex color without a leading `#`.

`pullRequests[].labels[].description` string

Label description. Absent when the label has none.

`pullRequests[].version` object

Current numbered pull request version and its head/base SHAs.

`pullRequests[].version.number` string

Monotonic pull request version number encoded as a JSON string.

`pullRequests[].version.headSha` string

Head SHA captured by this pull request version.

`pullRequests[].version.baseSha` string

Base SHA captured by this pull request version.

`pullRequests[].version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`nextPageToken` string

Opaque continuation token returned by a list response; an empty string means there is no next page. Do not inspect or construct it, and restart pagination when repository or filters change.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "pullRequests": [    {      "id": "string",      "number": "string",      "state": "string",      "draft": false,      "merged": false,      "title": "string",      "body": "string",      "head": {        "ref": "string",        "sha": "string"      },      "base": {        "ref": "string",        "sha": "string"      },      "author": {        "user": {          "id": "string",          "email": "string"        }      },      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z",      "closedAt": "2026-01-01T00:00:00Z",      "mergedAt": "2026-01-01T00:00:00Z",      "mergeCommitSha": "string",      "additions": 0,      "deletions": 0,      "changedFiles": 0,      "labels": [        {          "id": "string",          "name": "string",          "color": "string",          "description": "string"        }      ],      "version": {        "number": "string",        "headSha": "string",        "baseSha": "string",        "createdAt": "2026-01-01T00:00:00Z"      }    }  ],  "nextPageToken": "string"}
```

### [Get Pull Request](#get-pull-request)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}`

Returns a single pull request, including its assigned labels.

Closed or merged pull requests may additionally include `closedAt`, `mergedAt`, and `mergeCommitSha`. Treat `head.ref` and `base.ref` as opaque Origin ref strings; they may be short branch names or fully qualified `refs/heads/…` values.

#### [Path Parameters](#path-parameters-29)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-35)

`id` string

Stable Origin pull request identifier.

`number` string

Repository-local pull request number encoded as a JSON string.

`state` string

Pull request state; open or closed. Merged pull requests are closed with merged set true.

`draft` boolean

Whether the pull request is a draft.

`merged` boolean

Whether the pull request has merged.

`title` string

Pull request title.

`body` string

Pull request description body.

`head` object

The source side of the change - what is being merged in.

`head.ref` string

The ref this side points at, as Origin records it.

`head.sha` string

Tip commit SHA of this side at the change's latest version.

`base` object

The target side of the change — what it merges into.

`base.ref` string

The ref this side points at, as Origin records it.

`base.sha` string

Tip commit SHA of this side at the change's latest version.

`author` object

Public actor that opened the pull request.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 pull request creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest pull request update.

`closedAt` string

RFC 3339 close timestamp; may appear on closed or merged pull requests.

`mergedAt` string

RFC 3339 merge timestamp; may appear on merged pull requests.

`mergeCommitSha` string

Merge commit SHA; may appear after merge.

`additions` integer

Added lines in the current pull request version.

`deletions` integer

Deleted lines in the current pull request version.

`changedFiles` integer

Changed file count in the current pull request version.

`labels` array

Labels currently assigned to the pull request, sorted by name. Empty when none are assigned.

`labels[].id` string

Public identifier for the label.

`labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`labels[].color` string

Six-character hex color without a leading `#`.

`labels[].description` string

Label description. Absent when the label has none.

`version` object

Current numbered pull request version and its head/base SHAs.

`version.number` string

Monotonic pull request version number encoded as a JSON string.

`version.headSha` string

Head SHA captured by this pull request version.

`version.baseSha` string

Base SHA captured by this pull request version.

`version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "number": "string",  "state": "string",  "draft": false,  "merged": false,  "title": "string",  "body": "string",  "head": {    "ref": "string",    "sha": "string"  },  "base": {    "ref": "string",    "sha": "string"  },  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "closedAt": "2026-01-01T00:00:00Z",  "mergedAt": "2026-01-01T00:00:00Z",  "mergeCommitSha": "string",  "additions": 0,  "deletions": 0,  "changedFiles": 0,  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ],  "version": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  }}
```

### [Create Pull Request](#create-pull-request)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls`

Creates a pull request from `head` into `base`.

Optional `parent_pull_number` stacks this change on another open or draft pull request in the same repository.

#### [Path Parameters](#path-parameters-30)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-7)

`title` string Required

Pull request title.

`body` string

Pull request body / description. May be empty.

`head` string Required

Source branch name (the head of the change). Must resolve in the repo at call time.

`base` string Required

Target branch name (what the change merges into). Must resolve in the repo at call time.

`draft` boolean

When true, create as a draft. When false or omitted, create as open (ready for review).

`parentPullNumber` string

Optional parent pull request number when stacking this change on another open/draft change in the same repository.

#### [Response Fields](#response-fields-36)

`id` string

Stable Origin pull request identifier.

`number` string

Repository-local pull request number encoded as a JSON string.

`state` string

Pull request state; open or closed. Merged pull requests are closed with merged set true.

`draft` boolean

Whether the pull request is a draft.

`merged` boolean

Whether the pull request has merged.

`title` string

Pull request title.

`body` string

Pull request description body.

`head` object

The source side of the change - what is being merged in.

`head.ref` string

The ref this side points at, as Origin records it.

`head.sha` string

Tip commit SHA of this side at the change's latest version.

`base` object

The target side of the change — what it merges into.

`base.ref` string

The ref this side points at, as Origin records it.

`base.sha` string

Tip commit SHA of this side at the change's latest version.

`author` object

Public actor that opened the pull request.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 pull request creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest pull request update.

`closedAt` string

RFC 3339 close timestamp; may appear on closed or merged pull requests.

`mergedAt` string

RFC 3339 merge timestamp; may appear on merged pull requests.

`mergeCommitSha` string

Merge commit SHA; may appear after merge.

`additions` integer

Added lines in the current pull request version.

`deletions` integer

Deleted lines in the current pull request version.

`changedFiles` integer

Changed file count in the current pull request version.

`labels` array

Labels currently assigned to the pull request, sorted by name. Empty when none are assigned.

`labels[].id` string

Public identifier for the label.

`labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`labels[].color` string

Six-character hex color without a leading `#`.

`labels[].description` string

Label description. Absent when the label has none.

`version` object

Current numbered pull request version and its head/base SHAs.

`version.number` string

Monotonic pull request version number encoded as a JSON string.

`version.headSha` string

Head SHA captured by this pull request version.

`version.baseSha` string

Base SHA captured by this pull request version.

`version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "title": "TITLE",  "head": "HEAD_BRANCH",  "base": "BASE_BRANCH"}'
```

**Response shape:**

```
{  "id": "string",  "number": "string",  "state": "string",  "draft": false,  "merged": false,  "title": "string",  "body": "string",  "head": {    "ref": "string",    "sha": "string"  },  "base": {    "ref": "string",    "sha": "string"  },  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "closedAt": "2026-01-01T00:00:00Z",  "mergedAt": "2026-01-01T00:00:00Z",  "mergeCommitSha": "string",  "additions": 0,  "deletions": 0,  "changedFiles": 0,  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ],  "version": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  }}
```

### [Update Pull Request](#update-pull-request)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}`

Updates a pull request's title, body, base branch, and/or lifecycle state.

Omitted fields are unchanged. Present fields are applied in order: metadata, then reopen/draft/ready-for-review, then base, then close. Close runs last so a same-request retarget can still see an open change; reopen runs before base so a closed pull can be retargeted. If a later step fails, earlier steps may already have been committed.

#### [Path Parameters](#path-parameters-31)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-8)

`title` string

New title. Omitted fields are left unchanged.

`body` string

New body / description. An empty string clears the body.

`state` string

`"open"` or `"closed"`. `"closed"` closes the pull request. `"open"` without `draft: true` marks it ready for review, including publishing an existing draft. Merged is not writable. use `MergePullRequest`.

`draft` boolean

`true` marks the pull request draft; `false` marks it ready for review (and reopens it if currently closed). Ignored when `state` is `"closed"`.

`base` string

New base branch. Retargets the pull request and may update stack parentage when the new base is another change's head (or the default branch).

#### [Response Fields](#response-fields-37)

`id` string

Stable Origin pull request identifier.

`number` string

Repository-local pull request number encoded as a JSON string.

`state` string

Pull request state; open or closed. Merged pull requests are closed with merged set true.

`draft` boolean

Whether the pull request is a draft.

`merged` boolean

Whether the pull request has merged.

`title` string

Pull request title.

`body` string

Pull request description body.

`head` object

The source side of the change - what is being merged in.

`head.ref` string

The ref this side points at, as Origin records it.

`head.sha` string

Tip commit SHA of this side at the change's latest version.

`base` object

The target side of the change — what it merges into.

`base.ref` string

The ref this side points at, as Origin records it.

`base.sha` string

Tip commit SHA of this side at the change's latest version.

`author` object

Public actor that opened the pull request.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 pull request creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest pull request update.

`closedAt` string

RFC 3339 close timestamp; may appear on closed or merged pull requests.

`mergedAt` string

RFC 3339 merge timestamp; may appear on merged pull requests.

`mergeCommitSha` string

Merge commit SHA; may appear after merge.

`additions` integer

Added lines in the current pull request version.

`deletions` integer

Deleted lines in the current pull request version.

`changedFiles` integer

Changed file count in the current pull request version.

`labels` array

Labels currently assigned to the pull request, sorted by name. Empty when none are assigned.

`labels[].id` string

Public identifier for the label.

`labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`labels[].color` string

Six-character hex color without a leading `#`.

`labels[].description` string

Label description. Absent when the label has none.

`version` object

Current numbered pull request version and its head/base SHAs.

`version.number` string

Monotonic pull request version number encoded as a JSON string.

`version.headSha` string

Head SHA captured by this pull request version.

`version.baseSha` string

Base SHA captured by this pull request version.

`version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "title": "TITLE"}'
```

**Response shape:**

```
{  "id": "string",  "number": "string",  "state": "string",  "draft": false,  "merged": false,  "title": "string",  "body": "string",  "head": {    "ref": "string",    "sha": "string"  },  "base": {    "ref": "string",    "sha": "string"  },  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z",  "closedAt": "2026-01-01T00:00:00Z",  "mergedAt": "2026-01-01T00:00:00Z",  "mergeCommitSha": "string",  "additions": 0,  "deletions": 0,  "changedFiles": 0,  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ],  "version": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  }}
```

### [List Pull Request Comments](#list-pull-request-comments)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/comments`

Lists every comment on a pull request in chronological order. Each comment includes its thread id so clients can group the flat response into threads.

#### [Path Parameters](#path-parameters-32)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-14)

`pageSize` integer

Maximum comments to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque token from the preceding page.

#### [Response Fields](#response-fields-38)

`comments` array

Visible general and inline comments as one flat chronological list; group them by thread.id.

`comments[].id` string

Stable pull request comment identifier.

`comments[].thread` object

Thread reference used to group related comments.

`comments[].thread.id` string

Identifier used to group comments in one pull request discussion thread.

`comments[].body` string

Comment text.

`comments[].author` object

Public actor that authored the comment.

`comments[].author.user` object

User variant of the actor. Set when a user performed the action.

`comments[].author.user.id` string

Public identifier for the user.

`comments[].author.user.email` string

Email address of the user. Always set when the user variant is present.

`comments[].author.app` object

App variant of the actor. Set when an app performed the action.

`comments[].author.app.id` string

Public identifier for the app.

`comments[].author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`comments[].author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`comments[].author.serviceAccount.id` string

Public identifier for the service account.

`comments[].createdAt` string

RFC 3339 comment creation timestamp.

`comments[].updatedAt` string

RFC 3339 timestamp for the latest comment edit.

`pullRequest` object

Container PullRequestReference included alongside the comments page.

`pullRequest.id` string

Stable pull request identifier.

`pullRequest.number` string

Repository-local pull request number encoded as a JSON string.

`pullRequest.repository` object

Repository container reference for the pull request.

`pullRequest.repository.id` string

Repository identifier in a container reference.

`pullRequest.repository.name` string

Repository name in a container reference.

`pullRequest.repository.owner` object

Owner reference for the repository.

`pullRequest.repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`pullRequest.repository.owner.id` string

Origin owner identifier.

`pullRequest.repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`nextPageToken` string

Empty when there are no more comments.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/comments' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "comments": [    {      "id": "string",      "thread": {        "id": "string"      },      "body": "string",      "author": {        "user": {          "id": "string",          "email": "string"        }      },      "createdAt": "2026-01-01T00:00:00Z",      "updatedAt": "2026-01-01T00:00:00Z"    }  ],  "pullRequest": {    "id": "string",    "number": "string",    "repository": {      "id": "string",      "name": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      }    }  },  "nextPageToken": "string"}
```

### [Get Pull Request Comment](#get-pull-request-comment)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/comments/{commentId}`

Returns a single pull request comment by its stable Origin id. A comment outside the authorized repository, or a pending-review comment not visible to the caller, returns `404`.

#### [Path Parameters](#path-parameters-33)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`commentId` string Required

#### [Response Fields](#response-fields-39)

`id` string

Stable pull request comment identifier.

`thread` object

Thread reference used to group related comments.

`thread.id` string

Identifier used to group comments in one pull request discussion thread.

`body` string

Comment text.

`author` object

Public actor that authored the comment.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 comment creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest comment edit.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/comments/COMMENT_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "thread": {    "id": "string"  },  "body": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z"}
```

### [Create Pull Request Comment](#create-pull-request-comment)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/comments`

Creates a general-discussion comment or reply on an Origin pull request. Omitting `thread_id` starts a new thread; providing it replies to that thread. These are general-discussion comments, not diff-anchored review comments.

#### [Path Parameters](#path-parameters-34)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-9)

`body` string Required

`threadId` string

Existing thread id to reply to. Omit to create a new general-discussion thread.

#### [Response Fields](#response-fields-40)

`id` string

Stable pull request comment identifier.

`thread` object

Thread reference used to group related comments.

`thread.id` string

Identifier used to group comments in one pull request discussion thread.

`body` string

Comment text.

`author` object

Public actor that authored the comment.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 comment creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest comment edit.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/comments' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "BODY"}'
```

**Response shape:**

```
{  "id": "string",  "thread": {    "id": "string"  },  "body": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z"}
```

### [Update Pull Request Comment](#update-pull-request-comment)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/comments/{commentId}`

Updates a pull request comment by its stable Origin id.

Replaces the comment body. The comment must belong to the repository in the path, be visible to the caller, and have been authored by that caller. Cross-repository and hidden pending-review comments return `404`; a visible comment owned by another actor returns `403`.

#### [Path Parameters](#path-parameters-35)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`commentId` string Required

#### [Request Body](#request-body-10)

`body` string Required

#### [Response Fields](#response-fields-41)

`id` string

Stable pull request comment identifier.

`thread` object

Thread reference used to group related comments.

`thread.id` string

Identifier used to group comments in one pull request discussion thread.

`body` string

Comment text.

`author` object

Public actor that authored the comment.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 comment creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest comment edit.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/comments/COMMENT_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "BODY"}'
```

**Response shape:**

```
{  "id": "string",  "thread": {    "id": "string"  },  "body": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "createdAt": "2026-01-01T00:00:00Z",  "updatedAt": "2026-01-01T00:00:00Z"}
```

### [List Pull Request Commits](#list-pull-request-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/commits`

Lists the commits in a pull request.

Returns the pull request's commits as sparse `Commit` objects (no `stats`). Results default to 30 and are capped at 100, with at most 250 commits visible overall. A page token fixes the pull request version, page size, and commit cursor; `pageSize` must match the token on later requests, and a token that no longer matches the current head or base returns `400`.

#### [Path Parameters](#path-parameters-36)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-15)

`pageSize` integer

Max commits to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token is bound to the repository, pull request version, page size, and commit offset.

#### [Response Fields](#response-fields-42)

`commits` array

Sparse commits with no stats, with at most 250 commits visible overall.

`commits[].sha` string

Full commit SHA.

`commits[].commit` object

Git-object metadata nested separately from top-level repository relationships.

`commits[].commit.author` object

Git author identity recorded in the commit, not an Origin user object.

`commits[].commit.author.name` string

Name recorded in the Git author identity.

`commits[].commit.author.email` string

Email recorded in the Git author identity.

`commits[].commit.author.date` string

RFC 3339 date recorded in the Git author identity.

`commits[].commit.committer` object

Git committer identity recorded in the commit, not an Origin user object.

`commits[].commit.committer.name` string

Name recorded in the Git identity.

`commits[].commit.committer.email` string

Email recorded in the Git identity.

`commits[].commit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`commits[].commit.message` string

Commit message.

`commits[].commit.tree` object

Tree referenced by the commit.

`commits[].commit.tree.sha` string

SHA of the tree referenced by the commit.

`commits[].parents` array

Parent commit references, each containing a SHA.

`commits[].parents[].sha` string

Parent commit SHA.

`nextPageToken` string

Token fixes the pull request version, page size, and commit cursor; a token stale against the current head or base returns 400.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/commits' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "commits": [    {      "sha": "string",      "commit": {        "author": {          "name": "string",          "email": "string",          "date": "string"        },        "committer": {          "name": "string",          "email": "string",          "date": "string"        },        "message": "string",        "tree": {          "sha": "string"        }      },      "parents": [        {          "sha": "string"        }      ]    }  ],  "nextPageToken": "string"}
```

### [List Pull Request Files](#list-pull-request-files)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/files`

Lists the files changed in a pull request.

Returns filename, status, line counts, patch, and optional previous filename. Results default to 30 files and are capped at 100. A page token fixes the pull request version, page size, and file cursor; `pageSize` must match the token on later requests, and a token that no longer matches the current head or base returns `400`.

#### [Path Parameters](#path-parameters-37)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-16)

`pageSize` integer

Max changed files to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token is bound to the repository, pull request version, page size, and changed-file cursor.

#### [Response Fields](#response-fields-43)

`files` array

Changed-file records for the current pull request version.

`files[].filename` string

Path of the changed pull request file.

`files[].status` string

Change status; added, removed, modified, renamed, or copied.

`files[].additions` integer

Added line count for the file.

`files[].deletions` integer

Deleted line count for the file.

`files[].changes` integer

Total changed line count for the file.

`files[].patch` string

Unified patch for the file.

`files[].previousFilename` string

Previous path when the file was renamed or copied.

`nextPageToken` string

Token fixes pull request version, page size, and file cursor; a token stale against the current head or base returns 400.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/files' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "files": [    {      "filename": "string",      "status": "string",      "additions": 0,      "deletions": 0,      "changes": 0,      "patch": "string",      "previousFilename": "string"    }  ],  "nextPageToken": "string"}
```

### [List Pull Request Labels](#list-pull-request-labels)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Lists every label assigned to a pull request, ordered by name.

The response carries the full assigned list rather than a page of it, so this endpoint takes no pagination parameters. A pull request can have at most 100 labels. An unknown pull request returns `404`.

#### [Path Parameters](#path-parameters-38)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-44)

`labels` array

Every label currently assigned to the pull request, sorted by name.

`labels[].id` string

Public identifier for the label.

`labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`labels[].color` string

Six-character hex color without a leading `#`.

`labels[].description` string

Label description. Absent when the label has none.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ]}
```

### [Set Pull Request Labels](#set-pull-request-labels)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Replaces every label assigned to a pull request with the labels you name.

An empty list removes every assigned label. The labels must already exist in the repository; an unknown name or an unknown pull request returns `404`. A pull request can have at most 100 labels, so naming more than 100 returns `FailedPrecondition` (HTTP 400). The response lists the labels assigned after the replacement, ordered by name.

#### [Path Parameters](#path-parameters-39)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-11)

`labels` array

Label names to assign. Maximum 100. An empty list removes every assigned label. Duplicate names are ignored.

#### [Response Fields](#response-fields-45)

`labels` array

Labels assigned after the replacement, ordered by name. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "labels": [    "LABEL_NAME"  ]}'
```

**Response shape:**

```
{  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ]}
```

### [Add Pull Request Labels](#add-pull-request-labels)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Adds existing repository labels to a pull request.

Labels already assigned to the pull request stay assigned. The labels must already exist in the repository; an unknown name or an unknown pull request returns `404`. The request must name between 1 and 100 labels, and a pull request can have at most 100 labels in total, so a request that would take it past that limit returns `FailedPrecondition` (HTTP 400). The response lists the labels you named, not the pull request's full set; read the full set with [List Pull Request Labels](#list-pull-request-labels).

#### [Path Parameters](#path-parameters-40)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-12)

`labels` array Required

Label names to add. Maximum 100. Duplicate names are ignored.

#### [Response Fields](#response-fields-46)

`labels` array

Labels named in the request. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "labels": [    "LABEL_NAME"  ]}'
```

**Response shape:**

```
{  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ]}
```

### [Remove All Pull Request Labels](#remove-all-pull-request-labels)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Removes every label from a pull request.

The request succeeds when the pull request has no labels. An unknown pull request returns `404`. The response body is empty.

#### [Path Parameters](#path-parameters-41)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-47)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [Remove Pull Request Label](#remove-pull-request-label)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels/{labelName}`

Removes one label from a pull request.

A label that is not assigned to the pull request returns `404`, as does an unknown pull request. The response lists the labels remaining on the pull request, ordered by name.

#### [Path Parameters](#path-parameters-42)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`labelName` string Required

Name of the label to remove.

#### [Response Fields](#response-fields-48)

`labels` array

Labels remaining on the pull request, ordered by name. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels/LABEL_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "labels": [    {      "id": "string",      "name": "string",      "color": "string",      "description": "string"    }  ]}
```

### [Merge Pull Request](#merge-pull-request)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/merge`

Merges a pull request into its base.

For a stacked pull request, merges the entire root-to-target prefix ending at this pull number. not only this pull. Supported only on native Origin repositories; mirrored repositories are rejected.

#### [Path Parameters](#path-parameters-43)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

Pull number to merge. When this pull is stacked, the merge lands every pull from the stack root through this number.

#### [Request Body](#request-body-13)

`expectedHeadSha` string

Guard against merging a head your app has not seen: the full commit SHA (40 or 64 hexadecimal characters) expected to be the pull request's current head. When the head has moved, the merge is rejected with `ABORTED` (HTTP 409 Conflict) and nothing merges. Values that are not a full commit SHA are rejected with `InvalidArgument` (HTTP 400). Omit to merge whatever the current head is. Not evaluated when the pull request is already merged, which returns idempotent success.

#### [Response Fields](#response-fields-49)

`mergeCommitSha` string

SHA of the merge commit written to the base.

`mergedPullNumbers` array

JSON-string pull request numbers merged from stack root through the target.

`pullRequest` object

Target PullRequest after merge; the declared response type is the full resource even though the example is abbreviated.

`pullRequest.id` string

Stable Origin pull request identifier.

`pullRequest.number` string

Repository-local pull request number encoded as a JSON string.

`pullRequest.state` string

Pull request state; open or closed. Merged pull requests are closed with merged set true.

`pullRequest.draft` boolean

Whether the pull request is a draft.

`pullRequest.merged` boolean

Whether the pull request has merged.

`pullRequest.title` string

Pull request title.

`pullRequest.body` string

Pull request description body.

`pullRequest.head` object

The source side of the change - what is being merged in.

`pullRequest.head.ref` string

The ref this side points at, as Origin records it.

`pullRequest.head.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequest.base` object

The target side of the change — what it merges into.

`pullRequest.base.ref` string

The ref this side points at, as Origin records it.

`pullRequest.base.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequest.author` object

Public actor that opened the pull request.

`pullRequest.author.user` object

User variant of the actor. Set when a user performed the action.

`pullRequest.author.user.id` string

Public identifier for the user.

`pullRequest.author.user.email` string

Email address of the user. Always set when the user variant is present.

`pullRequest.author.app` object

App variant of the actor. Set when an app performed the action.

`pullRequest.author.app.id` string

Public identifier for the app.

`pullRequest.author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`pullRequest.author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`pullRequest.author.serviceAccount.id` string

Public identifier for the service account.

`pullRequest.createdAt` string

RFC 3339 pull request creation timestamp.

`pullRequest.updatedAt` string

RFC 3339 timestamp for the latest pull request update.

`pullRequest.closedAt` string

RFC 3339 close timestamp; may appear on closed or merged pull requests.

`pullRequest.mergedAt` string

RFC 3339 merge timestamp; may appear on merged pull requests.

`pullRequest.mergeCommitSha` string

Merge commit SHA; may appear after merge.

`pullRequest.additions` integer

Added lines in the current pull request version.

`pullRequest.deletions` integer

Deleted lines in the current pull request version.

`pullRequest.changedFiles` integer

Changed file count in the current pull request version.

`pullRequest.labels` array

Labels currently assigned to the pull request, sorted by name. Empty when none are assigned.

`pullRequest.labels[].id` string

Public identifier for the label.

`pullRequest.labels[].name` string

Label name, unique within the repository. Names address the label in the write endpoints.

`pullRequest.labels[].color` string

Six-character hex color without a leading `#`.

`pullRequest.labels[].description` string

Label description. Absent when the label has none.

`pullRequest.version` object

Current numbered pull request version and its head/base SHAs.

`pullRequest.version.number` string

Monotonic pull request version number encoded as a JSON string.

`pullRequest.version.headSha` string

Head SHA captured by this pull request version.

`pullRequest.version.baseSha` string

Base SHA captured by this pull request version.

`pullRequest.version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/merge' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{    "expectedHeadSha": "EXPECTED_HEAD_SHA"  }'
```

**Response shape:**

```
{  "mergeCommitSha": "string",  "mergedPullNumbers": [    "string"  ],  "pullRequest": {    "id": "string",    "number": "string",    "state": "string",    "draft": false,    "merged": false,    "title": "string",    "body": "string",    "head": {      "ref": "string",      "sha": "string"    },    "base": {      "ref": "string",      "sha": "string"    },    "author": {      "user": {        "id": "string",        "email": "string"      }    },    "createdAt": "2026-01-01T00:00:00Z",    "updatedAt": "2026-01-01T00:00:00Z",    "closedAt": "2026-01-01T00:00:00Z",    "mergedAt": "2026-01-01T00:00:00Z",    "mergeCommitSha": "string",    "additions": 0,    "deletions": 0,    "changedFiles": 0,    "labels": [      {        "id": "string",        "name": "string",        "color": "string",        "description": "string"      }    ],    "version": {      "number": "string",      "headSha": "string",      "baseSha": "string",      "createdAt": "2026-01-01T00:00:00Z"    }  }}
```

### [List Pull Request Reviews](#list-pull-request-reviews)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews`

Lists submitted reviews on a pull request, ordered by `submitted_at` ascending. Pending reviews are omitted.

#### [Path Parameters](#path-parameters-44)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-17)

`pageSize` integer

Maximum reviews to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque token from the preceding page.

#### [Response Fields](#response-fields-50)

`reviews` array

Submitted reviews ordered by submittedAt ascending; unsubmitted draft reviews are omitted.

`reviews[].id` string

Stable review identifier.

`reviews[].author` object

Public actor that authored the review.

`reviews[].author.user` object

User variant of the actor. Set when a user performed the action.

`reviews[].author.user.id` string

Public identifier for the user.

`reviews[].author.user.email` string

Email address of the user. Always set when the user variant is present.

`reviews[].author.app` object

App variant of the actor. Set when an app performed the action.

`reviews[].author.app.id` string

Public identifier for the app.

`reviews[].author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`reviews[].author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`reviews[].author.serviceAccount.id` string

Public identifier for the service account.

`reviews[].verdict` string

Review verdict; approve, request\_changes, or comment.

`reviews[].body` string

Review summary text.

`reviews[].submittedAt` string

RFC 3339 submission timestamp; absent for an unsubmitted draft review.

`reviews[].pullRequestVersion` object

Pull request version to which the review applies.

`reviews[].pullRequestVersion.number` string

Monotonic pull request version number encoded as a JSON string.

`reviews[].pullRequestVersion.headSha` string

Head SHA captured by this pull request version.

`reviews[].pullRequestVersion.baseSha` string

Base SHA captured by this pull request version.

`reviews[].pullRequestVersion.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`reviews[].dismissal` object

Present after a review is dismissed; dismissed reviews remain visible in listings.

`reviews[].dismissal.dismissedBy` object

Public actor that dismissed the review when exposed.

`reviews[].dismissal.dismissedBy.user` object

User variant of the actor. Set when a user performed the action.

`reviews[].dismissal.dismissedBy.user.id` string

Public identifier for the user.

`reviews[].dismissal.dismissedBy.user.email` string

Email address of the user. Always set when the user variant is present.

`reviews[].dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`reviews[].dismissal.dismissedBy.app.id` string

Public identifier for the app.

`reviews[].dismissal.dismissedBy.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`reviews[].dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`reviews[].dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`reviews[].dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`reviews[].dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

`pullRequest` object

Container PullRequestReference included alongside the reviews page.

`pullRequest.id` string

Stable pull request identifier.

`pullRequest.number` string

Repository-local pull request number encoded as a JSON string.

`pullRequest.repository` object

Repository container reference for the pull request.

`pullRequest.repository.id` string

Repository identifier in a container reference.

`pullRequest.repository.name` string

Repository name in a container reference.

`pullRequest.repository.owner` object

Owner reference for the repository.

`pullRequest.repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`pullRequest.repository.owner.id` string

Origin owner identifier.

`pullRequest.repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

`nextPageToken` string

Opaque token for the next page; empty when there are no more reviews.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "reviews": [    {      "id": "string",      "author": {        "user": {          "id": "string",          "email": "string"        }      },      "verdict": "approve",      "body": "string",      "submittedAt": "2026-01-01T00:00:00Z",      "pullRequestVersion": {        "number": "string",        "headSha": "string",        "baseSha": "string",        "createdAt": "2026-01-01T00:00:00Z"      },      "dismissal": {        "dismissedBy": {          "user": {            "id": "string",            "email": "string"          }        },        "dismissedAt": "2026-01-01T00:00:00Z",        "message": "string"      }    }  ],  "pullRequest": {    "id": "string",    "number": "string",    "repository": {      "id": "string",      "name": "string",      "owner": {        "slug": "string",        "id": "string",        "type": "team"      }    }  },  "nextPageToken": "string"}
```

### [Create Pull Request Review](#create-pull-request-review)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews`

Creates and submits a review on a pull request.

The review is submitted immediately. A new `approve` or `request_changes` review supersedes the caller's prior live decision review on the same pull request, which is dismissed. Pull request authors cannot `approve` their own pull request. Fails with FAILED\_PRECONDITION while the caller has an unsubmitted draft review on the pull request.

#### [Path Parameters](#path-parameters-45)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-14)

`verdict` string Required

The review decision. Allowed values: `PULL_REQUEST_REVIEW_VERDICT_UNSPECIFIED`, `approve`, `request_changes`, `comment`.

`body` string

Free-text review summary. May be empty.

`versionNumber` string

Pull request version number the review applies to (see `PullRequestVersion.number`). Omit to review the latest version at call time.

#### [Response Fields](#response-fields-51)

`id` string

Stable review identifier.

`author` object

Public actor that authored the review.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`verdict` string

Review verdict; approve, request\_changes, or comment.

`body` string

Review summary text.

`submittedAt` string

RFC 3339 submission timestamp; absent for an unsubmitted draft review.

`pullRequestVersion` object

Pull request version to which the review applies.

`pullRequestVersion.number` string

Monotonic pull request version number encoded as a JSON string.

`pullRequestVersion.headSha` string

Head SHA captured by this pull request version.

`pullRequestVersion.baseSha` string

Base SHA captured by this pull request version.

`pullRequestVersion.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`dismissal` object

Present after a review is dismissed; dismissed reviews remain visible in listings.

`dismissal.dismissedBy` object

Public actor that dismissed the review when exposed.

`dismissal.dismissedBy.user` object

User variant of the actor. Set when a user performed the action.

`dismissal.dismissedBy.user.id` string

Public identifier for the user.

`dismissal.dismissedBy.user.email` string

Email address of the user. Always set when the user variant is present.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "verdict": "approve"}'
```

**Response shape:**

```
{  "id": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "verdict": "approve",  "body": "string",  "submittedAt": "2026-01-01T00:00:00Z",  "pullRequestVersion": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  },  "dismissal": {    "dismissedBy": {      "user": {        "id": "string",        "email": "string"      }    },    "dismissedAt": "2026-01-01T00:00:00Z",    "message": "string"  }}
```

### [Update Pull Request Review](#update-pull-request-review)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews/{reviewId}`

Updates the body of a review. Only the review author can update it; other callers receive PERMISSION\_DENIED. A review that does not belong to the named pull request returns NOT\_FOUND.

Unsubmitted draft reviews can be updated too; a draft's response has no `submitted_at`.

#### [Path Parameters](#path-parameters-46)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`reviewId` string Required

#### [Request Body](#request-body-15)

`body` string Required

Replacement review summary text; replaces the prior body in full. Must contain a non-whitespace character; INVALID\_ARGUMENT otherwise.

#### [Response Fields](#response-fields-52)

`id` string

Stable review identifier.

`author` object

Public actor that authored the review.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`verdict` string

Review verdict; approve, request\_changes, or comment.

`body` string

Review summary text.

`submittedAt` string

RFC 3339 submission timestamp; absent for an unsubmitted draft review.

`pullRequestVersion` object

Pull request version to which the review applies.

`pullRequestVersion.number` string

Monotonic pull request version number encoded as a JSON string.

`pullRequestVersion.headSha` string

Head SHA captured by this pull request version.

`pullRequestVersion.baseSha` string

Base SHA captured by this pull request version.

`pullRequestVersion.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`dismissal` object

Present after a review is dismissed; dismissed reviews remain visible in listings.

`dismissal.dismissedBy` object

Public actor that dismissed the review when exposed.

`dismissal.dismissedBy.user` object

User variant of the actor. Set when a user performed the action.

`dismissal.dismissedBy.user.id` string

Public identifier for the user.

`dismissal.dismissedBy.user.email` string

Email address of the user. Always set when the user variant is present.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews/REVIEW_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "BODY"}'
```

**Response shape:**

```
{  "id": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "verdict": "approve",  "body": "string",  "submittedAt": "2026-01-01T00:00:00Z",  "pullRequestVersion": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  },  "dismissal": {    "dismissedBy": {      "user": {        "id": "string",        "email": "string"      }    },    "dismissedAt": "2026-01-01T00:00:00Z",    "message": "string"  }}
```

### [Dismiss Pull Request Review](#dismiss-pull-request-review)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews/{reviewId}/dismissals`

Dismisses a submitted review so its verdict no longer counts toward the pull request's review state. The review itself is retained and keeps appearing in ListPullRequestReviews, with `dismissal` set.

Dismissing does not require having authored the review; write permission on the repository's pull request reviews is sufficient.

Only `approve` and `request_changes` reviews can be dismissed, and only once: a `comment` review, an unsubmitted draft review, or an already-dismissed review returns FAILED\_PRECONDITION, and repeating the call leaves the first dismissal in place. A review that does not belong to the named pull request returns NOT\_FOUND.

#### [Path Parameters](#path-parameters-47)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`reviewId` string Required

Stable Origin review identifier, as returned by ListPullRequestReviews.

#### [Request Body](#request-body-16)

`message` string Required

Reason recorded with the dismissal. Must contain a non-whitespace character; INVALID\_ARGUMENT otherwise.

#### [Response Fields](#response-fields-53)

`id` string

Stable review identifier.

`author` object

Public actor that authored the review.

`author.user` object

User variant of the actor. Set when a user performed the action.

`author.user.id` string

Public identifier for the user.

`author.user.email` string

Email address of the user. Always set when the user variant is present.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`verdict` string

Review verdict; approve, request\_changes, or comment.

`body` string

Review summary text.

`submittedAt` string

RFC 3339 submission timestamp; absent for an unsubmitted draft review.

`pullRequestVersion` object

Pull request version to which the review applies.

`pullRequestVersion.number` string

Monotonic pull request version number encoded as a JSON string.

`pullRequestVersion.headSha` string

Head SHA captured by this pull request version.

`pullRequestVersion.baseSha` string

Base SHA captured by this pull request version.

`pullRequestVersion.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`dismissal` object

Present after a review is dismissed; dismissed reviews remain visible in listings.

`dismissal.dismissedBy` object

Public actor that dismissed the review when exposed.

`dismissal.dismissedBy.user` object

User variant of the actor. Set when a user performed the action.

`dismissal.dismissedBy.user.id` string

Public identifier for the user.

`dismissal.dismissedBy.user.email` string

Email address of the user. Always set when the user variant is present.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.slug` string

URL-friendly name of the app. Always set when the app variant is present.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews/REVIEW_ID/dismissals' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "message": "MESSAGE"}'
```

**Response shape:**

```
{  "id": "string",  "author": {    "user": {      "id": "string",      "email": "string"    }  },  "verdict": "approve",  "body": "string",  "submittedAt": "2026-01-01T00:00:00Z",  "pullRequestVersion": {    "number": "string",    "headSha": "string",    "baseSha": "string",    "createdAt": "2026-01-01T00:00:00Z"  },  "dismissal": {    "dismissedBy": {      "user": {        "id": "string",        "email": "string"      }    },    "dismissedAt": "2026-01-01T00:00:00Z",    "message": "string"  }}
```

## [Rulesets](#rulesets)

### [List Rulesets](#list-rulesets)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets`

Lists every ruleset configured on a repository.

Rulesets per repository are bounded configuration, so the full set comes back in one response and this endpoint does not paginate. `repository` is hoisted once and describes the repository shared by every ruleset in the response.

#### [Path Parameters](#path-parameters-48)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-54)

`rulesets` array

Rulesets configured on the repository.

`rulesets[].id` string

Stable Origin ruleset ID.

`rulesets[].name` string

Ruleset name.

`rulesets[].description` string

Ruleset description.

`rulesets[].enforcement` string

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`rulesets[].kind` string

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`rulesets[].includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`.

`rulesets[].excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language as `rulesets[].includedRefNames`.

`rulesets[].rules` array

Protection rules in this ruleset.

`rulesets[].rules[].id` string

Stable Origin ID for this rule.

`rulesets[].rules[].ruleType` string

Rule type, for example `pull_request`, `require_status_checks`, `require_branch_up_to_date`, `deletion`, or `non_fast_forward`.

`rulesets[].rules[].parameters` object

Type-specific parameters as a JSON object. The shape depends on `rulesets[].rules[].ruleType`.

`rulesets[].bypassActors` array

Principals that can bypass this ruleset. A bypass actor whose stored identity cannot be read is omitted from the response.

`rulesets[].bypassActors[].id` string

Stable Origin ID for this bypass actor.

`rulesets[].bypassActors[].bypassMode` string

When the bypass applies. Allowed values: `always`, `pull_request_only`.

`rulesets[].bypassActors[].user` object

A user principal. Exactly one of `user`, `team`, `app`, or `originRole` is present.

`rulesets[].bypassActors[].user.id` string

Numeric Cursor user ID encoded as a decimal string.

`rulesets[].bypassActors[].team` object

A team principal.

`rulesets[].bypassActors[].team.organizationPublicId` string

Immutable organization public ID.

`rulesets[].bypassActors[].team.groupPublicId` string

Immutable group public ID.

`rulesets[].bypassActors[].app` object

An app principal.

`rulesets[].bypassActors[].app.id` string

App ID, prefixed `app_`.

`rulesets[].bypassActors[].originRole` object

A principal holding an Origin role.

`rulesets[].bypassActors[].originRole.role` string

Allowed values: `namespace_admin`, `repository_admin`, `repository_write`.

`repository` object

Repository shared by every ruleset in this response.

`repository.id` string

Repository identifier in a container reference.

`repository.name` string

Repository name in a container reference.

`repository.owner` object

Owner reference for the repository.

`repository.owner.slug` string

URL-facing owner slug used with the owner ID to identify the repository owner.

`repository.owner.id` string

Origin owner identifier.

`repository.owner.type` string

Owner namespace type. Output-only. Allowed values: `team`, `user`. Omitted when unknown.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "rulesets": [    {      "id": "string",      "name": "string",      "description": "string",      "enforcement": "active",      "kind": "merge_branch",      "includedRefNames": [        "string"      ],      "excludedRefNames": [        "string"      ],      "rules": [        {          "id": "string",          "ruleType": "string",          "parameters": {}        }      ],      "bypassActors": [        {          "id": "string",          "bypassMode": "always",          "user": {            "id": "string"          }        }      ]    }  ],  "repository": {    "id": "string",    "name": "string",    "owner": {      "slug": "string",      "id": "string",      "type": "team"    }  }}
```

### [Create Ruleset](#create-ruleset)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets`

Creates a repository ruleset.

The response carries the stored ruleset, including the IDs Origin assigns to each rule and bypass actor. An empty `name` is rejected with `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-49)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-17)

`name` string Required

Ruleset name.

`description` string

Ruleset description.

`enforcement` string Required

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`kind` string Required

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`. Values above 64 entries are rejected with `InvalidArgument` (HTTP 400).

`excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language and 64-entry cap as `includedRefNames`.

`rules` array

Protection rules to store. Each entry carries `ruleType` and optional `parameters`; Origin assigns each rule's `id`. Values above 20 entries are rejected with `InvalidArgument` (HTTP 400).

`bypassActors` array

Bypass principals to store. Each entry carries `bypassMode` and exactly one of `user`, `team`, `app`, or `originRole`; Origin assigns each actor's `id`. Values above 15 entries are rejected with `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-55)

`id` string

Stable Origin ruleset ID.

`name` string

Ruleset name.

`description` string

Ruleset description.

`enforcement` string

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`kind` string

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`.

`excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language as `includedRefNames`.

`rules` array

Protection rules in this ruleset.

`rules[].id` string

Stable Origin ID for this rule.

`rules[].ruleType` string

Rule type, for example `pull_request`, `require_status_checks`, `require_branch_up_to_date`, `deletion`, or `non_fast_forward`.

`rules[].parameters` object

Type-specific parameters as a JSON object. The shape depends on `rules[].ruleType`.

`bypassActors` array

Principals that can bypass this ruleset. A bypass actor whose stored identity cannot be read is omitted from the response.

`bypassActors[].id` string

Stable Origin ID for this bypass actor.

`bypassActors[].bypassMode` string

When the bypass applies. Allowed values: `always`, `pull_request_only`.

`bypassActors[].user` object

A user principal. Exactly one of `user`, `team`, `app`, or `originRole` is present.

`bypassActors[].user.id` string

Numeric Cursor user ID encoded as a decimal string.

`bypassActors[].team` object

A team principal.

`bypassActors[].team.organizationPublicId` string

Immutable organization public ID.

`bypassActors[].team.groupPublicId` string

Immutable group public ID.

`bypassActors[].app` object

An app principal.

`bypassActors[].app.id` string

App ID, prefixed `app_`.

`bypassActors[].originRole` object

A principal holding an Origin role.

`bypassActors[].originRole.role` string

Allowed values: `namespace_admin`, `repository_admin`, `repository_write`.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "RULESET_NAME",  "description": "RULESET_DESCRIPTION",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "~DEFAULT_BRANCH"  ],  "excludedRefNames": [],  "rules": [    {      "ruleType": "pull_request",      "parameters": {}    }  ],  "bypassActors": [    {      "bypassMode": "always",      "app": {        "id": "APP_ID"      }    }  ]}'
```

**Response shape:**

```
{  "id": "string",  "name": "string",  "description": "string",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "string"  ],  "excludedRefNames": [    "string"  ],  "rules": [    {      "id": "string",      "ruleType": "string",      "parameters": {}    }  ],  "bypassActors": [    {      "id": "string",      "bypassMode": "always",      "user": {        "id": "string"      }    }  ]}
```

### [Get Ruleset](#get-ruleset)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`

Returns a single repository ruleset by its stable Origin ID.

An unknown repository and an unknown ruleset both return `404`; the message distinguishes them.

#### [Path Parameters](#path-parameters-50)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`rulesetId` string Required

Stable Origin ruleset ID.

#### [Response Fields](#response-fields-56)

`id` string

Stable Origin ruleset ID.

`name` string

Ruleset name.

`description` string

Ruleset description.

`enforcement` string

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`kind` string

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`.

`excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language as `includedRefNames`.

`rules` array

Protection rules in this ruleset.

`rules[].id` string

Stable Origin ID for this rule.

`rules[].ruleType` string

Rule type, for example `pull_request`, `require_status_checks`, `require_branch_up_to_date`, `deletion`, or `non_fast_forward`.

`rules[].parameters` object

Type-specific parameters as a JSON object. The shape depends on `rules[].ruleType`.

`bypassActors` array

Principals that can bypass this ruleset. A bypass actor whose stored identity cannot be read is omitted from the response.

`bypassActors[].id` string

Stable Origin ID for this bypass actor.

`bypassActors[].bypassMode` string

When the bypass applies. Allowed values: `always`, `pull_request_only`.

`bypassActors[].user` object

A user principal. Exactly one of `user`, `team`, `app`, or `originRole` is present.

`bypassActors[].user.id` string

Numeric Cursor user ID encoded as a decimal string.

`bypassActors[].team` object

A team principal.

`bypassActors[].team.organizationPublicId` string

Immutable organization public ID.

`bypassActors[].team.groupPublicId` string

Immutable group public ID.

`bypassActors[].app` object

An app principal.

`bypassActors[].app.id` string

App ID, prefixed `app_`.

`bypassActors[].originRole` object

A principal holding an Origin role.

`bypassActors[].originRole.role` string

Allowed values: `namespace_admin`, `repository_admin`, `repository_write`.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets/RULESET_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "string",  "name": "string",  "description": "string",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "string"  ],  "excludedRefNames": [    "string"  ],  "rules": [    {      "id": "string",      "ruleType": "string",      "parameters": {}    }  ],  "bypassActors": [    {      "id": "string",      "bypassMode": "always",      "user": {        "id": "string"      }    }  ]}
```

### [Update Ruleset](#update-ruleset)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`

Updates an existing repository ruleset.

The request replaces the whole ruleset configuration. `rules` and `bypassActors` are replaced in full rather than merged, and Origin assigns new IDs to the stored entries, so send every rule and bypass actor you want to keep.

#### [Path Parameters](#path-parameters-51)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`rulesetId` string Required

Stable Origin ruleset ID.

#### [Request Body](#request-body-18)

`name` string Required

Ruleset name.

`description` string

Ruleset description.

`enforcement` string Required

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`kind` string Required

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`. Values above 64 entries are rejected with `InvalidArgument` (HTTP 400).

`excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language and 64-entry cap as `includedRefNames`.

`rules` array

Protection rules to store. Each entry carries `ruleType` and optional `parameters`; Origin assigns each rule's `id`. Values above 20 entries are rejected with `InvalidArgument` (HTTP 400).

`bypassActors` array

Bypass principals to store. Each entry carries `bypassMode` and exactly one of `user`, `team`, `app`, or `originRole`; Origin assigns each actor's `id`. Values above 15 entries are rejected with `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-57)

`id` string

Stable Origin ruleset ID.

`name` string

Ruleset name.

`description` string

Ruleset description.

`enforcement` string

How Origin enforces the ruleset. Allowed values: `active`, `evaluate`, `disabled`.

`kind` string

The operation the ruleset protects. Allowed values: `merge_branch`, `push_branch`, `push_tag`, `push_repository`.

`includedRefNames` array

Ref name patterns this ruleset includes. Supports globs and the tokens `~ALL` and `~DEFAULT_BRANCH`.

`excludedRefNames` array

Ref name patterns this ruleset excludes. Same pattern language as `includedRefNames`.

`rules` array

Protection rules in this ruleset.

`rules[].id` string

Stable Origin ID for this rule.

`rules[].ruleType` string

Rule type, for example `pull_request`, `require_status_checks`, `require_branch_up_to_date`, `deletion`, or `non_fast_forward`.

`rules[].parameters` object

Type-specific parameters as a JSON object. The shape depends on `rules[].ruleType`.

`bypassActors` array

Principals that can bypass this ruleset. A bypass actor whose stored identity cannot be read is omitted from the response.

`bypassActors[].id` string

Stable Origin ID for this bypass actor.

`bypassActors[].bypassMode` string

When the bypass applies. Allowed values: `always`, `pull_request_only`.

`bypassActors[].user` object

A user principal. Exactly one of `user`, `team`, `app`, or `originRole` is present.

`bypassActors[].user.id` string

Numeric Cursor user ID encoded as a decimal string.

`bypassActors[].team` object

A team principal.

`bypassActors[].team.organizationPublicId` string

Immutable organization public ID.

`bypassActors[].team.groupPublicId` string

Immutable group public ID.

`bypassActors[].app` object

An app principal.

`bypassActors[].app.id` string

App ID, prefixed `app_`.

`bypassActors[].originRole` object

A principal holding an Origin role.

`bypassActors[].originRole.role` string

Allowed values: `namespace_admin`, `repository_admin`, `repository_write`.

```
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets/RULESET_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "RULESET_NAME",  "description": "RULESET_DESCRIPTION",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "~DEFAULT_BRANCH"  ],  "excludedRefNames": [],  "rules": [    {      "ruleType": "pull_request",      "parameters": {}    }  ],  "bypassActors": [    {      "bypassMode": "always",      "app": {        "id": "APP_ID"      }    }  ]}'
```

**Response shape:**

```
{  "id": "string",  "name": "string",  "description": "string",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "string"  ],  "excludedRefNames": [    "string"  ],  "rules": [    {      "id": "string",      "ruleType": "string",      "parameters": {}    }  ],  "bypassActors": [    {      "id": "string",      "bypassMode": "always",      "user": {        "id": "string"      }    }  ]}
```

English

- English
- 简体中文
- Русский
- 日本語
- Português
- Español
