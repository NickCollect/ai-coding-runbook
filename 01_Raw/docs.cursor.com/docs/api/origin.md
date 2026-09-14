---
source_url: https://cursor.com/docs/api/origin
fetched_at: 2026-09-14T05:36:10.789763+00:00
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

Responses carry fields that sit at their default value rather than dropping them, so a `false` boolean, a `0` number, an empty string, and an empty array are all present in the body. Read the value itself instead of treating a missing key as the default. Fields documented as absent or omitted are optional in the contract and stay out of the body when they are unset.

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

Both modes cover mirrored repositories as well as native Origin ones, so a mirror appears in `GET /installation/repos` and can be selected. A mirror is read-only until it becomes a stable outbound mirror: see [Mirrored repositories](#mirrored-repositories).

Use `GET /installation/repos` with an installation token to discover the repositories available to that installation. App JWT endpoints can list, inspect, and delete the app's installations. Deleting an installation prevents new tokens from being minted.

### [Installation receipt](#installation-receipt)

`installation_receipt` is a short-lived compact JWT signed by Origin. It proves the installation approval came from Origin rather than a forged redirect and carries everything the callback needs. Cursor refuses to redirect without one, so external callbacks always carry it.

JOSE header:

```
{  "alg": "EdDSA",  "kid": "origin-key-id",  "typ": "origin-installation-receipt+jwt"}
```

Claims:

```
{  "iss": "https://api.cursor.com/v1/origin",  "aud": "app_01...",  "sub": "i_01...",  "namespace_id": "ns_01...",  "iat": 1786465200,  "exp": 1786465500,  "jti": "RECEIPT_UUID",  "installedBy": {    "id": "user_01...",    "email": "installer@example.com",    "displayName": "Jane Doe"  },  "state": "ORIGINAL_VALUE"}
```

- `aud` is your app ID and `sub` is the installation ID to use when minting installation access tokens.
- `namespace_id` is the stable ID of the namespace the app was installed into.
- `installedBy` identifies the user who performed this install or re-consent. It describes the current action, so on a re-consent it can differ from the durable `installedBy` on [Get App Installation](#get-app-installation). It carries `displayName` when the account has a name, and never carries `handle`; read the handle from a REST response or a webhook payload instead.
- Receipts expire five minutes after issuance. `jti` is unique per receipt.
- `state` is present only when the install URL carried a non-empty `state`, and echoes that value. Match it against the anti-forgery value you generated before redirecting.

Verify the receipt before trusting the callback: resolve the signing key from the [JWKS](#discovery-and-signing-keys) by the `kid` header, require `alg` `EdDSA` and `typ` `origin-installation-receipt+jwt`, and validate the signature, `iss`, `aud`, and `exp`. Reject the callback when verification fails.

The receipt is not an installation access token. Never send it as a Bearer credential; mint installation tokens through [Create Installation Access Token](#create-installation-access-token) instead.

## [Authentication](#authentication)

Send REST credentials with the Bearer scheme. Each endpoint's **Auth** badges list the credential types it accepts:

```
curl --request GET \  --url https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME \  --header "Authorization: Bearer $ORIGIN_BEARER_TOKEN"
```

Cursor API keys are not Origin Bearer tokens. For user-authenticated requests, use the [Origin CLI](#user-authenticated-cli-requests), which exchanges a personal user API key for the short-lived access token that Origin accepts. Do not put a Cursor API key directly in the `Authorization` header.

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

On a mirrored repository, an installation token clones, fetches, and pulls, and Origin rejects `git push` with `403` until the mirror becomes a stable outbound mirror. See [Mirrored repositories](#mirrored-repositories).

### [User-authenticated CLI requests](#user-authenticated-cli-requests)

Use `origin api` for user-authenticated requests. For an interactive session, sign in through your browser:

```
origin auth loginorigin api /repos/OWNER_SLUG/REPO_NAME/pulls
```

For a non-interactive session, provide a personal user API key from [Cursor Dashboard → API Keys](https://cursor.com/dashboard/api):

```
export CURSOR_API_KEY="YOUR_PERSONAL_USER_API_KEY"origin api /repos/OWNER_SLUG/REPO_NAME/pulls
```

The CLI exchanges the personal API key for a short-lived user access token, then sends that token in the `Authorization` header. Do not send the API key itself to an Origin endpoint. App integrations should use app JWTs and installation access tokens instead.

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

Cache the JWKS. `/keys` sends `Cache-Control: public, max-age=600, stale-if-error=600`, so reuse a cached response for 10 minutes, then refresh; if a refresh fails, keep the last good keys for at most another 10 minutes before failing verification. Also refresh on a signature that no key verifies, which drops a retired key ID. Keys rotate weekly.

Webhook signatures do not carry a key ID, so verification should try each active Ed25519 key. Installation receipts carry the signing key's `kid` in their JOSE header, so receipt verification can resolve the key directly.

## [Scopes](#scopes)

Request only the minimum scopes your app needs. `repository:metadata:read` and app or installation metadata access are granted automatically and should not be added separately to installation URLs.

| Scope | Allows |
| --- | --- |
| `repository:metadata:read` | Read repository metadata and mirror transition jobs. Added automatically. |
| `repository:contents:read` | Read commits, branches, contents, comparison files, and low-level Git objects. Download a repository archive. Clone, fetch, and pull over Git HTTPS. Sync a mirrored repository from its upstream source. |
| `repository:contents:write` | Push over Git HTTPS. Merge pull requests. Create branches and commit file changes through the Git data endpoints. Re-request a check run. |
| `repository:pull_requests:read` | Read pull requests, changed files, pull request commits, and assigned labels. |
| `repository:pull_requests:write` | Create and update pull requests. Assign and remove pull request labels. |
| `repository:pull_requests:reviews:read` | Read pull request comments, comment threads, submitted reviews, and requested reviewers. |
| `repository:pull_requests:reviews:write` | Create and update comments; resolve and reopen comment threads; create, update, and dismiss reviews; request and remove reviewers. |
| `repository:checks:read` | Read check suites, runs, and check run annotations. |
| `repository:checks:write` | Create and update check suites and runs. Append check run annotations. |
| `repository:labels:read` | Read the label definitions a repository owns. |
| `repository:labels:write` | Create, update, and delete repository label definitions. |
| `repository:rulesets:read` | Read repository rulesets. |
| `repository:rulesets:write` | Create, update, and delete repository rulesets. |
| `repository:settings:read` | Read the grants held directly on a repository. |
| `repository:settings:write` | Update repository settings: the default branch, visibility, merge methods, and automatic head-branch deletion. Upsert and delete grants on a repository. |
| `namespace:settings:read` | Read the grants held directly on an owner. |
| `namespace:settings:write` | Upsert and delete grants on an owner. |

Requesting a `:write` scope also grants the matching `:read` scope, so `repository:labels:write` covers `repository:labels:read` and you do not have to list both. The reverse does not hold: a read scope never grants writes.

The installation token can only narrow these grants. It cannot add a scope or repository the workspace admin did not approve.

Mirror-state changes sit outside this table. [Transition Repo Mirror](#transition-repo-mirror), [Force Repo Mirror Cutover](#force-repo-mirror-cutover), and [Detach Repo Mirror](#detach-repo-mirror) take `repository:mirror:write` or `repository:mirror:delete`, which an app cannot request at installation: they are carried by a Cursor user credential, and the caller must also administer the repository on the mirror's upstream source.

App management sits outside it for the same reason. [Create App](#create-app) takes `namespace:apps:create`, [List Namespace Apps](#list-namespace-apps) takes `namespace:apps:read`, [Get App](#get-app) takes `app:settings:read`, and [Update App](#update-app), [Add App Signing Key](#add-app-signing-key), and [Revoke App Signing Key](#revoke-app-signing-key) take `app:settings:write`. A publisher holds these on a Cursor user credential; an app cannot request them for itself.

The table covers the scopes an app requests at installation. To look up the scope a single operation requires, read its `x-origin-scopes` extension in the [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml). That extension covers every operation, including the `app`, `installation`, and `namespace` scopes that come with the credential itself rather than from an installation grant. An operation whose scopes all come with the credential marks its extension `ambient: true`: there is nothing to request for it, and presenting the right credential is enough.

### [Mirrored repositories](#mirrored-repositories)

An installation uses every scope it holds on a native Origin repository and on a stable outbound mirror. On a repository in any other mirror state, only two scopes apply:

- `repository:metadata:read`
- `repository:contents:read`

Every other scope returns `403` on that repository, whatever the workspace admin approved. Over the REST API, repository and contents reads, commit comparison, and [Sync Mirror](#sync-mirror) keep working, and Origin rejects pull requests, reviews, comments, checks, rulesets, and every write. Over Git HTTPS, clone, fetch, pull, and LFS download keep working, and Origin rejects push and LFS upload.

Moving a repository out of that state is a user-credential operation rather than something an installation can do: [Transition Repo Mirror](#transition-repo-mirror) advances the mirror direction, [Force Repo Mirror Cutover](#force-repo-mirror-cutover) cuts over to the upstream source without pushing divergent refs back, and [Detach Repo Mirror](#detach-repo-mirror) disconnects the mirror for good.

The `mirror` object on a repository does not tell you whether writes are allowed. A mirror partway through a transition can report `mirror.status` as `outbound` and still be read-only, so treat the `403` as authoritative rather than branching on `mirror.status`.

## [Rate limits](#rate-limits)

The Origin API uses a shared per-principal point budget that resets on a rolling one-minute window. Each authenticated principal kind has its own budget:

| Principal | Default budget |
| --- | --- |
| Installation access token | 3,000 points/minute |
| App JWT | 6,000 points/minute |
| Cursor user or service account | 600 points/minute |

Every endpoint charges a fixed cost against that budget before the handler runs. Authentication and authorization failures are not charged.

| Cost | Operations |
| --- | --- |
| 0 | [Get Rate Limit](#get-rate-limit). Status only; does not consume points. |
| 1 | Most read endpoints, plus [Create Installation Access Token](#create-installation-access-token) |
| 5 | Ordinary writes, plus these heavier reads: [Get Commit](#get-commit), [List Commit Files](#list-commit-files), [List Comparison Files](#list-comparison-files), [List Pull Request Files](#list-pull-request-files), and [Get Repo Tarball](#get-repo-tarball) |
| 10 | [Create App](#create-app), [Create Repo](#create-repo), [Create Commit From Files](#create-commit-from-files), [Merge Pull Request](#merge-pull-request), [Transition Repo Mirror](#transition-repo-mirror), and [Force Repo Mirror Cutover](#force-repo-mirror-cutover) |

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

Origin retries transport errors, `429`, and `5xx` responses up to seven total attempts. Retry delays are 5 seconds, 30 seconds, 1 minute, 2 minutes, 4 minutes, and 8 minutes. Other `4xx` responses are terminal.

To confirm a receiver works before any real event reaches it, call [Ping Webhook](#ping-webhook).

Origin delivers events for mirrored repositories, and installation event payloads list them in the selected repository arrays. Delivery does not widen what the installation can call: see [Mirrored repositories](#mirrored-repositories).

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
| `repository.created` | A repository is created. |
| `repository.deleted` | A repository is deleted. |
| `repository.pushed` | One or more refs change in a push. |
| `repository.metadata.updated` | A repository's default branch changes. |
| `pull_request.created` | A pull request opens. |
| `pull_request.head_ref.pushed` | The pull request head advances. |
| `pull_request.base_ref.updated` | The base ref or resolved base commit changes. |
| `pull_request.metadata.updated` | The title or description changes. |
| `pull_request.closed` | A pull request closes without merging, including when Origin closes it because a push left its head with no history in common with its base. |
| `pull_request.merged` | A pull request merges. |
| `pull_request.reopened` | A closed pull request reopens. |
| `pull_request.published` | A draft becomes open. |
| `pull_request.comment.created` | A visible pull request comment is created. |
| `pull_request.review.submitted` | A review is submitted with any verdict. |
| `pull_request.review.dismissed` | A submitted review is dismissed, explicitly or by being superseded. |
| `pull_request.reviewer.added` | A reviewer is requested. |
| `pull_request.reviewer.removed` | A reviewer is removed. |
| `pull_request.reviewer.rerequested` | A reviewer is requested again. |
| `repository.check_run.created` | A check run is created. |
| `repository.check_run.completed` | A check run completes. |
| `repository.check_run.rerequested` | A completed check run is re-requested. Delivered only to the app that owns the run. |
| `installation.created` | The app is installed. |
| `installation.updated` | Scopes, repository selection, or the owner namespace slug change. |
| `installation.suspended` | The installation is suspended. |
| `installation.unsuspended` | A suspended installation is restored. |
| `installation.deleted` | The app is uninstalled. |

Every event's payload shape is documented field by field in [Event payloads](#event-payloads).

The five `installation.*` events go to the app itself rather than to a repository subscription. Origin always sends them, so they do not appear in the app's selectable event list. Every other event in this table is a repository-scoped subscription.

Origin does not deliver `repository.pushed` for a repository it mirrors from GitHub. GitHub owns those pushes and sends its own push webhooks, so an Origin delivery would duplicate them. Pushes to native Origin repositories and to outbound mirrors are delivered as usual, and the mirror state does not affect any other event. `repository.deleted` is delivered for a repository mirrored from GitHub: stopping the sync deletes the Cursor-side repository only, and GitHub sends nothing for it.

### [Event payloads](#event-payloads)

Each event's [envelope](#delivery-envelope) carries the event's payload object in `payload`. Events that share a shape share a payload family; each family below documents the events that deliver it, its fields, and a sample payload, generated from the [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml).

### [Repository Created](#repository-created)

EVENT`repository.created`

#### [Payload Fields](#payload-fields)

`repository` object

The created repository.

`repository.id` string

`repository.name` string Required

The repo name, unique to its owner. Required on create.

`repository.fullName` string

"{owner.login}/{name}". Derived.

`repository.owner` object

The owning entity. Determined by the parent on create; not settable directly.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`repository.defaultBranch` string

Default branch name. Always set on responses. On create, omitting this field or leaving it empty defaults to "main".

`repository.createdAt` string

RFC 3339 timestamp.

`repository.updatedAt` string

RFC 3339 timestamp.

`repository.pushedAt` string

Most-recent-push timestamp on any branch; absent until the first push. RFC 3339 timestamp.

`repository.cloneUrl` string

HTTPS URL for cloning the repository.

`repository.mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`repository.mirror.source` string

One of `github`.

`repository.mirror.sourceId` string

Opaque repository identifier assigned by the source.

`repository.mirror.status` string

Effective direction during a transition, until cutover completes. One of `inbound`, `outbound`.

`repository.visibility` string

Repository visibility, `internal` or `private`. One of `internal`, `private`.

`repository.allowMergeCommit` boolean

Whether pull requests may land as merge commits.

`repository.allowSquashMerge` boolean

Whether pull requests may land as squash merges.

`repository.deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "main",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-01T09:30:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git"  }}
```

### [Repository Deleted](#repository-deleted)

EVENT`repository.deleted`

#### [Payload Fields](#payload-fields-1)

`repository` object

The repository that was deleted. A reference only: the repository no longer resolves through the API once deleted.

`repository.id` string

`repository.name` string

`repository.owner` object

The owner of a repo.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`deletedAt` string

When the repository was deleted. RFC 3339 timestamp.

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "deletedAt": "2026-08-03T08:15:00Z"}
```

### [Repository Push](#repository-push)

EVENT`repository.pushed`

One atomic push, which may update several refs. There is no commits array; each ref update carries best-effort tip metadata only.

#### [Payload Fields](#payload-fields-2)

`repository` object

The repository the push targeted.

`repository.id` string

`repository.name` string

`repository.owner` object

The owner of a repo.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`refUpdates` array

Refs included from this push, capped at 100.

`refUpdates[].ref` string

The full git ref that was pushed. Example: `refs/heads/main` or `refs/tags/v3.14.1`.

`refUpdates[].before` string

The SHA of the most recent commit on `ref` before the push. All-zero (`0000000000000000000000000000000000000000`) when the ref was just created.

`refUpdates[].after` string

The SHA of the most recent commit on `ref` after the push. All-zero (`0000000000000000000000000000000000000000`) when the ref was deleted.

`refUpdates[].created` boolean

Whether this push created the ref.

`refUpdates[].deleted` boolean

Whether this push deleted the ref.

`refUpdates[].forced` boolean

Whether this push rewrote history: a non-fast-forward update of an existing ref (the new tip is not a descendant of the old tip). False for ref creates, deletes, fast-forward updates, and pushes observed before Origin tracked force-push status.

`refUpdates[].headCommit` object

Best-effort metadata for the commit at the peeled new tip. Unset for deletions, non-commit refs, historical pushes, and extraction failures.

`refUpdates[].headCommit.sha` string

`refUpdates[].headCommit.author` object

Git identity and timestamp for a commit's author or committer. This is the identity recorded in the commit object, not a linked user account.

`refUpdates[].headCommit.author.name` string

`refUpdates[].headCommit.author.email` string

`refUpdates[].headCommit.author.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`refUpdates[].headCommit.committer` object

Git identity and timestamp for a commit's author or committer. This is the identity recorded in the commit object, not a linked user account.

`refUpdates[].headCommit.committer.name` string

`refUpdates[].headCommit.committer.email` string

`refUpdates[].headCommit.committer.date` string

ISO-8601 timestamp preserving the git signature's original timezone offset (e.g. "2014-11-07T22:01:45+01:00").

`refUpdates[].headCommit.message` string

`pushedAt` string

When Origin observed the push. RFC 3339 timestamp.

`pusher` object

The principal that performed the push, as verified by Origin. Absent when Origin itself performed the push, such as the merge push that advances the base ref when a pull request merges.

`pusher.user` object

`pusher.user.id` string

`pusher.user.email` string Required

`pusher.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`pusher.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`pusher.app` object

`pusher.app.id` string

`pusher.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`pusher.serviceAccount` object

`pusher.serviceAccount.id` string

`refUpdatesCount` integer

Number of ref updates in the atomic push. ref\_updates may be shorter when the producer capped the list.

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "refUpdates": [    {      "ref": "refs/heads/add-telemetry",      "before": "5c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d",      "after": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "created": false,      "deleted": false,      "forced": false,      "headCommit": {        "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "author": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "committer": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "message": "Add launch telemetry"      }    }  ],  "pushedAt": "2026-08-02T14:45:00Z",  "pusher": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "refUpdatesCount": 1}
```

### [Repository Metadata Updated](#repository-metadata-updated)

EVENT`repository.metadata.updated`

Carries the full repository snapshot with no delta and no updating actor. Compare successive snapshots or refetch the repository to see what changed.

#### [Payload Fields](#payload-fields-3)

`repository` object

The full repository snapshot after the update.

`repository.id` string

`repository.name` string Required

The repo name, unique to its owner. Required on create.

`repository.fullName` string

"{owner.login}/{name}". Derived.

`repository.owner` object

The owning entity. Determined by the parent on create; not settable directly.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`repository.defaultBranch` string

Default branch name. Always set on responses. On create, omitting this field or leaving it empty defaults to "main".

`repository.createdAt` string

RFC 3339 timestamp.

`repository.updatedAt` string

RFC 3339 timestamp.

`repository.pushedAt` string

Most-recent-push timestamp on any branch; absent until the first push. RFC 3339 timestamp.

`repository.cloneUrl` string

HTTPS URL for cloning the repository.

`repository.mirror` object

Mirror metadata. Absent for a native repository and before a mirror's initial sync is ready.

`repository.mirror.source` string

One of `github`.

`repository.mirror.sourceId` string

Opaque repository identifier assigned by the source.

`repository.mirror.status` string

Effective direction during a transition, until cutover completes. One of `inbound`, `outbound`.

`repository.visibility` string

Repository visibility, `internal` or `private`. One of `internal`, `private`.

`repository.allowMergeCommit` boolean

Whether pull requests may land as merge commits.

`repository.allowSquashMerge` boolean

Whether pull requests may land as squash merges.

`repository.deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "release",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-03T08:15:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",    "pushedAt": "2026-08-02T14:45:00Z"  }}
```

### [Pull Request Events](#pull-request-events)

EVENT`pull_request.created``pull_request.published``pull_request.reopened``pull_request.closed``pull_request.merged``pull_request.metadata.updated``pull_request.head_ref.pushed``pull_request.base_ref.updated`

A pull request lifecycle change. The lifecycle action is the envelope's `event.type`; there is no separate action field.

#### [Payload Fields](#payload-fields-4)

`pullRequest` object

The pull request snapshot. Assigned labels are omitted; read them with `GetPullRequest`.

`pullRequest.id` string

Stable Origin pull request identifier.

`pullRequest.number` string

Pull request number within its repository.

`pullRequest.state` string

"open" or "closed". A draft is "open"; merged and closed pull requests are both "closed".

`pullRequest.draft` boolean

Whether the pull request is still a draft.

`pullRequest.merged` boolean

Whether the pull request has been merged.

`pullRequest.title` string

Pull request title.

`pullRequest.body` string

Pull request description.

`pullRequest.head` object

The source side of the pull request - what is being merged in.

`pullRequest.head.ref` string

The ref this side points at, as Origin records it.

`pullRequest.head.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequest.base` object

The target side of the pull request — what it merges into.

`pullRequest.base.ref` string

The ref this side points at, as Origin records it.

`pullRequest.base.sha` string

Tip commit SHA of this side at the change's latest version.

`pullRequest.author` object

The principal that opened the pull request.

`pullRequest.author.user` object

`pullRequest.author.user.id` string

`pullRequest.author.user.email` string Required

`pullRequest.author.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`pullRequest.author.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`pullRequest.author.app` object

`pullRequest.author.app.id` string

`pullRequest.author.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`pullRequest.author.serviceAccount` object

`pullRequest.author.serviceAccount.id` string

`pullRequest.createdAt` string

When the pull request was opened. RFC 3339 timestamp.

`pullRequest.updatedAt` string

When the pull request was last updated. RFC 3339 timestamp.

`pullRequest.closedAt` string

When the pull request was closed or merged; unset while open. RFC 3339 timestamp.

`pullRequest.mergedAt` string

When the pull request was merged; unset unless merged. RFC 3339 timestamp.

`pullRequest.mergeCommitSha` string

SHA of the resulting merge commit; set once merged.

`pullRequest.additions` integer

Lines added by the pull request's latest version.

`pullRequest.deletions` integer

Lines deleted by the pull request's latest version.

`pullRequest.changedFiles` integer

Files changed by the pull request's latest version.

`pullRequest.version` object

The pull request's latest version.

`pullRequest.version.number` string

Monotonic version number within the change (1-based).

`pullRequest.version.headSha` string

Head commit SHA for this version.

`pullRequest.version.baseSha` string

Base commit SHA this version is diffed against.

`pullRequest.version.createdAt` string

When this version was created. RFC 3339 timestamp.

`repository` object

The repository the pull request belongs to.

`repository.id` string

`repository.name` string

`repository.owner` object

The owner of a repo.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

**Sample `event.payload`:**

```
{  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "state": "open",    "draft": false,    "merged": false,    "title": "Add launch telemetry",    "body": "Adds structured launch telemetry to the ignition path.",    "head": {      "ref": "add-telemetry",      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"    },    "base": {      "ref": "main",      "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"    },    "author": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "additions": 128,    "deletions": 46,    "changedFiles": 5,    "version": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    }  },  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  }}
```

### [Pull Request Comment](#pull-request-comment)

EVENT`pull_request.comment.created`

A comment created on a pull request. Comments filed with a review are delivered when the review submits, one event per comment.

#### [Payload Fields](#payload-fields-5)

`pullRequest` object

The pull request the comment was filed on.

`pullRequest.id` string

Immutable Origin change id.

`pullRequest.number` string

`pullRequest.repository` object

Repository reference for this pull request.

`pullRequest.repository.id` string

`pullRequest.repository.name` string

`pullRequest.repository.owner` object

The owner of a repo.

`pullRequest.repository.owner.slug` string

Unique URL-friendly name of the owner.

`pullRequest.repository.owner.id` string

Unique ID of the owner namespace.

`pullRequest.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`comment` object

The created comment. A comment that opened its thread carries the thread's diff anchor inline; a reply carries only `comment.thread.id`. Thread resolution state is not part of the event; read it with `GetPullRequestComment`.

`comment.id` string

`comment.thread` object

The thread this comment belongs to, including its diff anchor and resolution state.

`comment.thread.id` string

`comment.thread.version` object

The pull request version the thread was filed against, including its head and base SHAs (see `PullRequestReview.pull_request_version`).

`comment.thread.version.number` string

Monotonic version number within the change (1-based).

`comment.thread.version.headSha` string

Head commit SHA for this version.

`comment.thread.version.baseSha` string

Base commit SHA this version is diffed against.

`comment.thread.version.createdAt` string

When this version was created. RFC 3339 timestamp.

`comment.thread.path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`comment.thread.side` string

Diff side of the anchor. Unset for general-discussion threads. One of `left`, `right`.

`comment.thread.startLine` integer

First line of the anchored range in the `side` version of the file. 0 for file-level and general-discussion threads.

`comment.thread.endLine` integer

Inclusive last line of the anchored range. 0 when the anchor is a single line or has no line range.

`comment.thread.resolvedAt` string

When the thread was resolved. Unset while the thread is open. RFC 3339 timestamp.

`comment.thread.createdAt` string

RFC 3339 timestamp.

`comment.thread.updatedAt` string

RFC 3339 timestamp.

`comment.body` string

`comment.author` object

A user, app, or service account that performed an externally visible action.

`comment.author.user` object

`comment.author.user.id` string

`comment.author.user.email` string Required

`comment.author.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`comment.author.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`comment.author.app` object

`comment.author.app.id` string

`comment.author.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`comment.author.serviceAccount` object

`comment.author.serviceAccount.id` string

`comment.createdAt` string

RFC 3339 timestamp.

`comment.updatedAt` string

RFC 3339 timestamp.

**Sample `event.payload`:**

```
{  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    }  },  "comment": {    "id": "cmt_01k2ja2000e0080000000000e5",    "thread": {      "id": "cth_01k2ja2000e0080000000000s6",      "version": {        "number": "3",        "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",        "createdAt": "2026-08-01T09:30:00Z"      },      "path": "src/telemetry/retry.ts",      "side": "right",      "startLine": 42,      "endLine": 45,      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z"    },    "body": "Should the retry budget be configurable?",    "author": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z"  }}
```

### [Pull Request Review Events](#pull-request-review-events)

EVENT`pull_request.review.submitted``pull_request.review.dismissed`

#### [Payload Fields](#payload-fields-6)

`pullRequest` object

The pull request the review was filed on.

`pullRequest.id` string

Immutable Origin change id.

`pullRequest.number` string

`pullRequest.repository` object

Repository reference for this pull request.

`pullRequest.repository.id` string

`pullRequest.repository.name` string

`pullRequest.repository.owner` object

The owner of a repo.

`pullRequest.repository.owner.slug` string

Unique URL-friendly name of the owner.

`pullRequest.repository.owner.id` string

Unique ID of the owner namespace.

`pullRequest.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`review` object

The review that was submitted or dismissed. On a dismissal, `review.dismissal` is set.

`review.id` string

Stable Origin review identifier.

`review.author` object

The principal that authored the review.

`review.author.user` object

`review.author.user.id` string

`review.author.user.email` string Required

`review.author.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`review.author.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`review.author.app` object

`review.author.app.id` string

`review.author.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`review.author.serviceAccount` object

`review.author.serviceAccount.id` string

`review.verdict` string

One of `approve`, `request_changes`, `comment`.

`review.body` string

Free-text review summary. Empty when the reviewer left no summary.

`review.submittedAt` string

When the review was submitted. Unset for an unsubmitted draft review. RFC 3339 timestamp.

`review.pullRequestVersion` object

The pull request version and head SHA the verdict applies to.

`review.pullRequestVersion.number` string

Monotonic version number within the change (1-based).

`review.pullRequestVersion.headSha` string

Head commit SHA for this version.

`review.pullRequestVersion.baseSha` string

Base commit SHA this version is diffed against.

`review.pullRequestVersion.createdAt` string

When this version was created. RFC 3339 timestamp.

`review.dismissal` object

Set once the review has been dismissed; absent while the verdict still counts toward the pull request's review state.

`review.dismissal.dismissedBy` object

The principal that dismissed the review. Absent when the dismissal was recorded under an actor kind this API does not expose.

`review.dismissal.dismissedBy.user` object

`review.dismissal.dismissedBy.user.id` string

`review.dismissal.dismissedBy.user.email` string Required

`review.dismissal.dismissedBy.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`review.dismissal.dismissedBy.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`review.dismissal.dismissedBy.app` object

`review.dismissal.dismissedBy.app.id` string

`review.dismissal.dismissedBy.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`review.dismissal.dismissedBy.serviceAccount` object

`review.dismissal.dismissedBy.serviceAccount.id` string

`review.dismissal.dismissedAt` string

When the review was dismissed. RFC 3339 timestamp.

`review.dismissal.message` string

Reason recorded with the dismissal. Reviews retired automatically because their author submitted a newer verdict carry a server-generated reason.

**Sample `event.payload`:**

```
{  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    }  },  "review": {    "id": "rev_01k2ja2000e0080000000000f6",    "author": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "verdict": "approve",    "body": "Approving. The telemetry schema matches the spec.",    "submittedAt": "2026-08-02T15:00:00Z",    "pullRequestVersion": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    }  }}
```

### [Pull Request Reviewer Events](#pull-request-reviewer-events)

EVENT`pull_request.reviewer.added``pull_request.reviewer.removed``pull_request.reviewer.rerequested`

A change to the pull request's requested reviewers. Read the current pending set with `ListPullRequestRequestedReviewers`.

#### [Payload Fields](#payload-fields-7)

`pullRequest` object

The pull request whose requested reviewers changed.

`pullRequest.id` string

Immutable Origin change id.

`pullRequest.number` string

`pullRequest.repository` object

Repository reference for this pull request.

`pullRequest.repository.id` string

`pullRequest.repository.name` string

`pullRequest.repository.owner` object

The owner of a repo.

`pullRequest.repository.owner.slug` string

Unique URL-friendly name of the owner.

`pullRequest.repository.owner.id` string

Unique ID of the owner namespace.

`pullRequest.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`reviewer` object

The requested reviewer the event is about.

`reviewer.user` object

`reviewer.user.id` string

`reviewer.user.email` string Required

`reviewer.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`reviewer.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`reviewer.group` object

Public Origin group identity (`grp_…`). Currently id-only.

`reviewer.group.id` string

`createdVia` string

How the review request was created. One of `manual`, `codeowners`.

`createdBy` object

The principal that created the review request, when known.

`createdBy.user` object

`createdBy.user.id` string

`createdBy.user.email` string Required

`createdBy.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`createdBy.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`createdBy.app` object

`createdBy.app.id` string

`createdBy.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`createdBy.serviceAccount` object

`createdBy.serviceAccount.id` string

`createdAt` string

When the review request was created. RFC 3339 timestamp.

**Sample `event.payload`:**

```
{  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    }  },  "reviewer": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdVia": "codeowners",  "createdAt": "2026-08-02T14:45:00Z"}
```

### [Check Run Events](#check-run-events)

EVENT`repository.check_run.created``repository.check_run.completed`

Committed snapshot for an Origin check-run lifecycle event.

#### [Payload Fields](#payload-fields-8)

`repository` object

The repository the check run belongs to.

`repository.id` string

`repository.name` string

`repository.owner` object

The owner of a repo.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkSuite` object

The suite the check run belongs to.

`checkSuite.id` string

Server-assigned unique ID of the suite.

`checkSuite.repository` object

Repository the suite belongs to.

`checkSuite.repository.id` string

`checkSuite.repository.name` string

`checkSuite.repository.owner` object

The owner of a repo.

`checkSuite.repository.owner.slug` string

Unique URL-friendly name of the owner.

`checkSuite.repository.owner.id` string

Unique ID of the owner namespace.

`checkSuite.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkSuite.sha` string

Resolved head commit SHA the suite is attached to (lowercase hex).

`checkSuite.key` string

App-chosen idempotency key for the suite.

`checkSuite.name` string

Human-facing suite name.

`checkSuite.detailsUrl` string

Link to more detail about the suite as a whole, if set.

`checkSuite.createdAt` string

RFC 3339 timestamp.

`checkSuite.updatedAt` string

RFC 3339 timestamp.

`checkSuite.externalId` string

Provider-assigned immutable identity for this suite attempt.

`checkSuite.actor` object

Principal that produced the suite.

`checkSuite.actor.user` object

`checkSuite.actor.user.id` string

`checkSuite.actor.user.email` string Required

`checkSuite.actor.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkSuite.actor.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkSuite.actor.app` object

`checkSuite.actor.app.id` string

`checkSuite.actor.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkSuite.actor.serviceAccount` object

`checkSuite.actor.serviceAccount.id` string

`checkRun` object

The check run snapshot at this lifecycle point.

`checkRun.id` string

Server-assigned unique ID of the check run.

`checkRun.repository` object

Repository the check run belongs to.

`checkRun.repository.id` string

`checkRun.repository.name` string

`checkRun.repository.owner` object

The owner of a repo.

`checkRun.repository.owner.slug` string

Unique URL-friendly name of the owner.

`checkRun.repository.owner.id` string

Unique ID of the owner namespace.

`checkRun.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkRun.checkSuite` object

Suite this check run belongs to.

`checkRun.checkSuite.id` string

`checkRun.sha` string

Resolved head commit SHA the check run is attached to (lowercase hex).

`checkRun.key` string

App-chosen idempotency key for the check run.

`checkRun.name` string

Human-facing check-run name.

`checkRun.status` string

One of `queued`, `in_progress`, `completed`.

`checkRun.conclusion` string

Present iff `status == completed`. One of `success`, `failure`, `neutral`, `cancelled`, `skipped`, `timed_out`, `action_required`, `stale`.

`checkRun.detailsUrl` string

Link to more detail about this specific check run, if set.

`checkRun.externalUpdatedAt` string

The external system's last-update time used for ordering. RFC 3339 timestamp.

`checkRun.startedAt` string

When the check run started, if reported. RFC 3339 timestamp.

`checkRun.completedAt` string

When the check run completed, if reported. RFC 3339 timestamp.

`checkRun.createdAt` string

RFC 3339 timestamp.

`checkRun.updatedAt` string

RFC 3339 timestamp.

`checkRun.externalId` string

Provider-assigned immutable identity for this check attempt.

`checkRun.actor` object

Principal that produced the check run.

`checkRun.actor.user` object

`checkRun.actor.user.id` string

`checkRun.actor.user.email` string Required

`checkRun.actor.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkRun.actor.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkRun.actor.app` object

`checkRun.actor.app.id` string

`checkRun.actor.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkRun.actor.serviceAccount` object

`checkRun.actor.serviceAccount.id` string

`checkRun.output` object

Human-readable output for this check run, if set.

`checkRun.output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRun.output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.deadlineAt` string

Optional deadline. Omitted or unset means no expiration. RFC 3339 timestamp.

`checkRun.isRerequestable` boolean

Whether the reporting app declared this run re-requestable (`CheckRunInput.is_rerequestable`).

`checkRun.rerequestedAt` string

Set while a re-request is outstanding; cleared when the provider posts again. Unset means no re-request is pending. While set, the run stays in the commit's CI state as pending (`status` and `conclusion` are the superseded result); the owning app answers by posting the run it committed to by declaring `is_rerequestable` — a new run for the same `key`, or an update of this run (which clears this field) — after which the run may be re-requested again. RFC 3339 timestamp.

`checkRun.rerequestedBy` object

Principal that re-requested the run. Present iff `rerequested_at` is set; cleared together with it when the owning app answers.

`checkRun.rerequestedBy.user` object

`checkRun.rerequestedBy.user.id` string

`checkRun.rerequestedBy.user.email` string Required

`checkRun.rerequestedBy.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkRun.rerequestedBy.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkRun.rerequestedBy.app` object

`checkRun.rerequestedBy.app.id` string

`checkRun.rerequestedBy.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkRun.rerequestedBy.serviceAccount` object

`checkRun.rerequestedBy.serviceAccount.id` string

`actor` object

The principal that produced the check run.

`actor.user` object

`actor.user.id` string

`actor.user.email` string Required

`actor.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`actor.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`actor.app` object

`actor.app.id` string

`actor.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`actor.serviceAccount` object

`actor.serviceAccount.id` string

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "externalId": "build-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    }  },  "checkRun": {    "id": "cr_01k2ja2000e0080000000000g7",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "checkSuite": {      "id": "crg_01k2ja2000e0080000000000h8"    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842-unit-tests",    "name": "unit-tests",    "status": "completed",    "conclusion": "success",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalUpdatedAt": "2026-08-02T14:44:30Z",    "startedAt": "2026-08-02T14:40:00Z",    "completedAt": "2026-08-02T14:44:30Z",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "externalId": "run-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "output": {      "title": "Unit tests",      "summary": "128 tests passed.",      "text": "All suites green."    }  },  "actor": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  }}
```

### [Check Run Rerequested](#check-run-rerequested)

EVENT`repository.check_run.rerequested`

repository.check\_run.rerequested webhook payload, delivered only to the app that owns the check run. Answer by posting a fresh run for the same head SHA and key — a new run (new external\_id) or an update of the re-requested run — the stamped run's status is never reset by Origin, and the answering post clears `rerequested_at`. Each accepted re-request emits one event, and a run may be re-requested again once answered, so dedupe redeliveries on the event id alone; `check_run.rerequested_at` carries the outstanding stamp. The payload carries no pull request context (check runs attach to `(repository, sha)`): a consumer that needs the pull request resolves it from `check_run.sha` via its own head mapping, or `ListPullRequests` filtered to the head branch it built.

#### [Payload Fields](#payload-fields-9)

`repository` object

The repository the check run belongs to.

`repository.id` string

`repository.name` string

`repository.owner` object

The owner of a repo.

`repository.owner.slug` string

Unique URL-friendly name of the owner.

`repository.owner.id` string

Unique ID of the owner namespace.

`repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkSuite` object

The suite the check run belongs to.

`checkSuite.id` string

Server-assigned unique ID of the suite.

`checkSuite.repository` object

Repository the suite belongs to.

`checkSuite.repository.id` string

`checkSuite.repository.name` string

`checkSuite.repository.owner` object

The owner of a repo.

`checkSuite.repository.owner.slug` string

Unique URL-friendly name of the owner.

`checkSuite.repository.owner.id` string

Unique ID of the owner namespace.

`checkSuite.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkSuite.sha` string

Resolved head commit SHA the suite is attached to (lowercase hex).

`checkSuite.key` string

App-chosen idempotency key for the suite.

`checkSuite.name` string

Human-facing suite name.

`checkSuite.detailsUrl` string

Link to more detail about the suite as a whole, if set.

`checkSuite.createdAt` string

RFC 3339 timestamp.

`checkSuite.updatedAt` string

RFC 3339 timestamp.

`checkSuite.externalId` string

Provider-assigned immutable identity for this suite attempt.

`checkSuite.actor` object

Principal that produced the suite.

`checkSuite.actor.user` object

`checkSuite.actor.user.id` string

`checkSuite.actor.user.email` string Required

`checkSuite.actor.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkSuite.actor.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkSuite.actor.app` object

`checkSuite.actor.app.id` string

`checkSuite.actor.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkSuite.actor.serviceAccount` object

`checkSuite.actor.serviceAccount.id` string

`checkRun` object

The re-requested check run; `check_run.rerequested_at` records the stamp and `check_run.rerequested_by` the principal that asked.

`checkRun.id` string

Server-assigned unique ID of the check run.

`checkRun.repository` object

Repository the check run belongs to.

`checkRun.repository.id` string

`checkRun.repository.name` string

`checkRun.repository.owner` object

The owner of a repo.

`checkRun.repository.owner.slug` string

Unique URL-friendly name of the owner.

`checkRun.repository.owner.id` string

Unique ID of the owner namespace.

`checkRun.repository.owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`checkRun.checkSuite` object

Suite this check run belongs to.

`checkRun.checkSuite.id` string

`checkRun.sha` string

Resolved head commit SHA the check run is attached to (lowercase hex).

`checkRun.key` string

App-chosen idempotency key for the check run.

`checkRun.name` string

Human-facing check-run name.

`checkRun.status` string

One of `queued`, `in_progress`, `completed`.

`checkRun.conclusion` string

Present iff `status == completed`. One of `success`, `failure`, `neutral`, `cancelled`, `skipped`, `timed_out`, `action_required`, `stale`.

`checkRun.detailsUrl` string

Link to more detail about this specific check run, if set.

`checkRun.externalUpdatedAt` string

The external system's last-update time used for ordering. RFC 3339 timestamp.

`checkRun.startedAt` string

When the check run started, if reported. RFC 3339 timestamp.

`checkRun.completedAt` string

When the check run completed, if reported. RFC 3339 timestamp.

`checkRun.createdAt` string

RFC 3339 timestamp.

`checkRun.updatedAt` string

RFC 3339 timestamp.

`checkRun.externalId` string

Provider-assigned immutable identity for this check attempt.

`checkRun.actor` object

Principal that produced the check run.

`checkRun.actor.user` object

`checkRun.actor.user.id` string

`checkRun.actor.user.email` string Required

`checkRun.actor.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkRun.actor.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkRun.actor.app` object

`checkRun.actor.app.id` string

`checkRun.actor.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkRun.actor.serviceAccount` object

`checkRun.actor.serviceAccount.id` string

`checkRun.output` object

Human-readable output for this check run, if set.

`checkRun.output.title` string

Short headline for the output. Maximum length: 255 characters.

`checkRun.output.summary` string

Summary of the output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.output.text` string

Detailed output. May contain Markdown. Maximum UTF-8 size: 65535 bytes.

`checkRun.deadlineAt` string

Optional deadline. Omitted or unset means no expiration. RFC 3339 timestamp.

`checkRun.isRerequestable` boolean

Whether the reporting app declared this run re-requestable (`CheckRunInput.is_rerequestable`).

`checkRun.rerequestedAt` string

Set while a re-request is outstanding; cleared when the provider posts again. Unset means no re-request is pending. While set, the run stays in the commit's CI state as pending (`status` and `conclusion` are the superseded result); the owning app answers by posting the run it committed to by declaring `is_rerequestable` — a new run for the same `key`, or an update of this run (which clears this field) — after which the run may be re-requested again. RFC 3339 timestamp.

`checkRun.rerequestedBy` object

Principal that re-requested the run. Present iff `rerequested_at` is set; cleared together with it when the owning app answers.

`checkRun.rerequestedBy.user` object

`checkRun.rerequestedBy.user.id` string

`checkRun.rerequestedBy.user.email` string Required

`checkRun.rerequestedBy.user.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`checkRun.rerequestedBy.user.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`checkRun.rerequestedBy.app` object

`checkRun.rerequestedBy.app.id` string

`checkRun.rerequestedBy.app.displayName` string

The app's registered display name, never empty when present. Omitted on payloads whose app could not be resolved and on the first-party Cursor facade actor.

`checkRun.rerequestedBy.serviceAccount` object

`checkRun.rerequestedBy.serviceAccount.id` string

**Sample `event.payload`:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:10:00Z",    "externalId": "build-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    }  },  "checkRun": {    "id": "cr_01k2ja2000e0080000000000g7",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "checkSuite": {      "id": "crg_01k2ja2000e0080000000000h8"    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842-unit-tests",    "name": "unit-tests",    "status": "completed",    "conclusion": "failure",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalUpdatedAt": "2026-08-02T14:44:30Z",    "startedAt": "2026-08-02T14:40:00Z",    "completedAt": "2026-08-02T14:44:30Z",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:10:00Z",    "externalId": "run-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "output": {      "title": "Unit tests",      "summary": "1 of 129 tests failed.",      "text": "FAIL telemetry.spec.ts > flushes queued events on shutdown"    },    "isRerequestable": true,    "rerequestedAt": "2026-08-02T15:10:00Z",    "rerequestedBy": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    }  }}
```

### [Installation Created](#installation-created)

EVENT`installation.created`

#### [Payload Fields](#payload-fields-10)

`installation` object

The installation snapshot at the time of the event.

`installation.id` string

`installation.appId` string

The installed app's identifier; the same value as `app.id` on the payload.

`installation.target` object

The owner of a repo.

`installation.target.slug` string

Unique URL-friendly name of the owner.

`installation.target.id` string

Unique ID of the owner namespace.

`installation.target.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.repoSelectionMode` string

One of `all`, `selected`.

`installation.repositories` array

Empty when repository\_selection is "all". Capped at 5,000; see repositories\_count for the true total.

`installation.repositories[].id` string

`installation.repositories[].name` string

`installation.repositories[].owner` object

The owner of a repo.

`installation.repositories[].owner.slug` string

Unique URL-friendly name of the owner.

`installation.repositories[].owner.id` string

Unique ID of the owner namespace.

`installation.repositories[].owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.scopes` array

`installation.repositoriesCount` integer

True total; 0 when repository\_selection is "all".

`installation.createdAt` string

RFC 3339 timestamp.

`installation.updatedAt` string

RFC 3339 timestamp.

`installation.deletedAt` string

RFC 3339 timestamp.

`installation.suspendedAt` string

Set while the installation is suspended; unset when it is active. RFC 3339 timestamp.

`installation.installedBy` object

User who originally installed the app.

`installation.installedBy.id` string

`installation.installedBy.email` string Required

`installation.installedBy.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`installation.installedBy.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`app` object

The app the installation belongs to.

`app.id` string

`app.displayName` string

The app's registered display name, never empty when present. Omitted when enqueue-time hydration could not resolve the app.

**Sample `event.payload`:**

```
{  "installation": {    "id": "inst_01k2ja2000e0080000000000b2",    "appId": "app_01k2ja2000e0080000000000a1",    "target": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "repoSelectionMode": "selected",    "repositories": [      {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      }    ],    "scopes": [      "repository:contents:read",      "repository:pull_requests:read"    ],    "repositoriesCount": 1,    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-01T09:30:00Z",    "installedBy": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "app": {    "id": "app_01k2ja2000e0080000000000a1",    "displayName": "CI Status Bot"  }}
```

### [Installation Updated](#installation-updated)

EVENT`installation.updated`

#### [Payload Fields](#payload-fields-11)

`installation` object

The installation snapshot at the time of the event.

`installation.id` string

`installation.appId` string

The installed app's identifier; the same value as `app.id` on the payload.

`installation.target` object

The owner of a repo.

`installation.target.slug` string

Unique URL-friendly name of the owner.

`installation.target.id` string

Unique ID of the owner namespace.

`installation.target.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.repoSelectionMode` string

One of `all`, `selected`.

`installation.repositories` array

Empty when repository\_selection is "all". Capped at 5,000; see repositories\_count for the true total.

`installation.repositories[].id` string

`installation.repositories[].name` string

`installation.repositories[].owner` object

The owner of a repo.

`installation.repositories[].owner.slug` string

Unique URL-friendly name of the owner.

`installation.repositories[].owner.id` string

Unique ID of the owner namespace.

`installation.repositories[].owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.scopes` array

`installation.repositoriesCount` integer

True total; 0 when repository\_selection is "all".

`installation.createdAt` string

RFC 3339 timestamp.

`installation.updatedAt` string

RFC 3339 timestamp.

`installation.deletedAt` string

RFC 3339 timestamp.

`installation.suspendedAt` string

Set while the installation is suspended; unset when it is active. RFC 3339 timestamp.

`installation.installedBy` object

User who originally installed the app.

`installation.installedBy.id` string

`installation.installedBy.email` string Required

`installation.installedBy.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`installation.installedBy.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`app` object

The app the installation belongs to.

`app.id` string

`app.displayName` string

The app's registered display name, never empty when present. Omitted when enqueue-time hydration could not resolve the app.

**Sample `event.payload`:**

```
{  "installation": {    "id": "inst_01k2ja2000e0080000000000b2",    "appId": "app_01k2ja2000e0080000000000a1",    "target": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "repoSelectionMode": "selected",    "repositories": [      {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      }    ],    "scopes": [      "repository:contents:read",      "repository:pull_requests:read"    ],    "repositoriesCount": 1,    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "installedBy": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "app": {    "id": "app_01k2ja2000e0080000000000a1",    "displayName": "CI Status Bot"  }}
```

### [Installation Suspended](#installation-suspended)

EVENT`installation.suspended`

#### [Payload Fields](#payload-fields-12)

`installation` object

The installation snapshot at the time of the event.

`installation.id` string

`installation.appId` string

The installed app's identifier; the same value as `app.id` on the payload.

`installation.target` object

The owner of a repo.

`installation.target.slug` string

Unique URL-friendly name of the owner.

`installation.target.id` string

Unique ID of the owner namespace.

`installation.target.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.repoSelectionMode` string

One of `all`, `selected`.

`installation.repositories` array

Empty when repository\_selection is "all". Capped at 5,000; see repositories\_count for the true total.

`installation.repositories[].id` string

`installation.repositories[].name` string

`installation.repositories[].owner` object

The owner of a repo.

`installation.repositories[].owner.slug` string

Unique URL-friendly name of the owner.

`installation.repositories[].owner.id` string

Unique ID of the owner namespace.

`installation.repositories[].owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.scopes` array

`installation.repositoriesCount` integer

True total; 0 when repository\_selection is "all".

`installation.createdAt` string

RFC 3339 timestamp.

`installation.updatedAt` string

RFC 3339 timestamp.

`installation.deletedAt` string

RFC 3339 timestamp.

`installation.suspendedAt` string

Set while the installation is suspended; unset when it is active. RFC 3339 timestamp.

`installation.installedBy` object

User who originally installed the app.

`installation.installedBy.id` string

`installation.installedBy.email` string Required

`installation.installedBy.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`installation.installedBy.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`app` object

The app the installation belongs to.

`app.id` string

`app.displayName` string

The app's registered display name, never empty when present. Omitted when enqueue-time hydration could not resolve the app.

**Sample `event.payload`:**

```
{  "installation": {    "id": "inst_01k2ja2000e0080000000000b2",    "appId": "app_01k2ja2000e0080000000000a1",    "target": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "repoSelectionMode": "selected",    "repositories": [      {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      }    ],    "scopes": [      "repository:contents:read",      "repository:pull_requests:read"    ],    "repositoriesCount": 1,    "createdAt": "2026-08-01T09:30:00Z",    "installedBy": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    },    "suspendedAt": "2026-08-03T08:15:00Z"  },  "app": {    "id": "app_01k2ja2000e0080000000000a1",    "displayName": "CI Status Bot"  }}
```

### [Installation Unsuspended](#installation-unsuspended)

EVENT`installation.unsuspended`

#### [Payload Fields](#payload-fields-13)

`installation` object

The installation snapshot at the time of the event.

`installation.id` string

`installation.appId` string

The installed app's identifier; the same value as `app.id` on the payload.

`installation.target` object

The owner of a repo.

`installation.target.slug` string

Unique URL-friendly name of the owner.

`installation.target.id` string

Unique ID of the owner namespace.

`installation.target.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.repoSelectionMode` string

One of `all`, `selected`.

`installation.repositories` array

Empty when repository\_selection is "all". Capped at 5,000; see repositories\_count for the true total.

`installation.repositories[].id` string

`installation.repositories[].name` string

`installation.repositories[].owner` object

The owner of a repo.

`installation.repositories[].owner.slug` string

Unique URL-friendly name of the owner.

`installation.repositories[].owner.id` string

Unique ID of the owner namespace.

`installation.repositories[].owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.scopes` array

`installation.repositoriesCount` integer

True total; 0 when repository\_selection is "all".

`installation.createdAt` string

RFC 3339 timestamp.

`installation.updatedAt` string

RFC 3339 timestamp.

`installation.deletedAt` string

RFC 3339 timestamp.

`installation.suspendedAt` string

Set while the installation is suspended; unset when it is active. RFC 3339 timestamp.

`installation.installedBy` object

User who originally installed the app.

`installation.installedBy.id` string

`installation.installedBy.email` string Required

`installation.installedBy.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`installation.installedBy.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`app` object

The app the installation belongs to.

`app.id` string

`app.displayName` string

The app's registered display name, never empty when present. Omitted when enqueue-time hydration could not resolve the app.

**Sample `event.payload`:**

```
{  "installation": {    "id": "inst_01k2ja2000e0080000000000b2",    "appId": "app_01k2ja2000e0080000000000a1",    "target": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "repoSelectionMode": "selected",    "repositories": [      {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      }    ],    "scopes": [      "repository:contents:read",      "repository:pull_requests:read"    ],    "repositoriesCount": 1,    "createdAt": "2026-08-01T09:30:00Z",    "installedBy": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "app": {    "id": "app_01k2ja2000e0080000000000a1",    "displayName": "CI Status Bot"  }}
```

### [Installation Deleted](#installation-deleted)

EVENT`installation.deleted`

#### [Payload Fields](#payload-fields-14)

`installation` object

The installation snapshot at the time of the event.

`installation.id` string

`installation.appId` string

The installed app's identifier; the same value as `app.id` on the payload.

`installation.target` object

The owner of a repo.

`installation.target.slug` string

Unique URL-friendly name of the owner.

`installation.target.id` string

Unique ID of the owner namespace.

`installation.target.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.repoSelectionMode` string

One of `all`, `selected`.

`installation.repositories` array

Empty when repository\_selection is "all". Capped at 5,000; see repositories\_count for the true total.

`installation.repositories[].id` string

`installation.repositories[].name` string

`installation.repositories[].owner` object

The owner of a repo.

`installation.repositories[].owner.slug` string

Unique URL-friendly name of the owner.

`installation.repositories[].owner.id` string

Unique ID of the owner namespace.

`installation.repositories[].owner.type` string

`team` or `user`. Output-only; unset when unknown. One of `team`, `user`.

`installation.scopes` array

`installation.repositoriesCount` integer

True total; 0 when repository\_selection is "all".

`installation.createdAt` string

RFC 3339 timestamp.

`installation.updatedAt` string

RFC 3339 timestamp.

`installation.deletedAt` string

RFC 3339 timestamp.

`installation.suspendedAt` string

Set while the installation is suspended; unset when it is active. RFC 3339 timestamp.

`installation.installedBy` object

User who originally installed the app.

`installation.installedBy.id` string

`installation.installedBy.email` string Required

`installation.installedBy.displayName` string

Human-readable display name: the account's first and last name, each trimmed, joined with a space — exactly the name the product UI renders. Omitted when the account has no name; never synthesized from the email, the id, or any other field. May also be absent on webhook payloads whose actor could not be resolved.

`installation.installedBy.handle` string

The user's claimed profile handle (the identity behind cursor.com /@handle), without the @ prefix. Present only while the user's profile is publicly visible; omitted for users without a claimed handle and for non-public profiles.

`app` object

The app the installation belongs to.

`app.id` string

`app.displayName` string

The app's registered display name, never empty when present. Omitted when enqueue-time hydration could not resolve the app.

**Sample `event.payload`:**

```
{  "installation": {    "id": "inst_01k2ja2000e0080000000000b2",    "appId": "app_01k2ja2000e0080000000000a1",    "target": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "repoSelectionMode": "selected",    "repositories": [      {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      }    ],    "scopes": [      "repository:contents:read",      "repository:pull_requests:read"    ],    "repositoriesCount": 1,    "createdAt": "2026-08-01T09:30:00Z",    "installedBy": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    },    "deletedAt": "2026-08-03T08:15:00Z"  },  "app": {    "id": "app_01k2ja2000e0080000000000a1",    "displayName": "CI Status Bot"  }}
```

### [Recovery](#recovery)

Use an app JWT to query [`GET /app/webhook/deliveries`](#list-webhook-deliveries). Filter by delivery status, event type, installation, time range, or page token. `delivered=false` returns every delivery the receiver has never acknowledged with `2xx`. Deliveries stay listable for seven days, so recover within that window.

Use [`POST /app/webhook/deliveries:batchRedeliver`](#batch-redeliver-webhook-deliveries) to queue redelivery for up to 100 delivery IDs. The operation deduplicates IDs and reports the result for each delivery.

An owner can pause an app's webhook delivery from the app's settings. While delivery is paused, redelivery requests return `FailedPrecondition` (HTTP 400) and nothing is queued; resume delivery first. Clearing the app's `webhookUrl` through [Update App](#update-app) has a stronger effect: it cancels the pending deliveries outright, and setting a URL again does not bring them back.

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

A `404` never distinguishes a resource that does not exist from one your app cannot reach. Read it as "not available to this installation" rather than as proof the resource is absent.

`details` carries typed entries: `google.rpc.BadRequest` field violations on an invalid argument, and a `google.rpc.RequestInfo` entry on every error. Origin can add detail types at any time, so ignore entries your integration does not recognize.

Every error response carries the request ID twice: in an `X-Request-ID` response header, and as a `google.rpc.RequestInfo` entry in `details`. Origin echoes the `x-request-id` you sent, or generates one when you send none. The `RequestInfo` entry is present even when `message` is an opaque internal error, so quote the request ID when you contact Cursor about a failed call.

Unmatched paths under `/v1/origin`, and requests that use the wrong method on a known path, return this same body rather than a generic router error. The message names the method and path and never echoes the query string.

### [Repository paths](#repository-paths)

Repository-scoped paths take the owner slug and repository name as `{ownerSlug}/{repoName}`. Both segments resolve case-insensitively, so any casing addresses the repository. Responses return the stored name and slug rather than the casing you sent, and Git HTTPS URLs resolve the same way. Compare repository names case-insensitively, and read the canonical casing from [Get Repo](#get-repo).

Every repository-scoped path also accepts the repository's stable ID in place of the pair: send `_` as the owner slug and the ID as the repository name, as in `GET /v1/origin/repos/_/REPO_ID`. Read the ID from the `id` field on [Get Repo](#get-repo). The sentinel `_` cannot be claimed as an owner slug, so the two forms never collide. In a Connect or JSON request, set `ownerSlug` to `_` and `name` to the ID.

The ID form survives a rename, which makes it the stable way to address a repository. It grants nothing on its own: after Origin resolves the ID to a repository, your app still needs the same scope on that repository. An ID your app cannot reach returns the same `404` body as an ID that does not exist, so a response never confirms that a repository exists. A malformed ID returns `400`. [Create Repo](#create-repo) takes an owner slug alone and rejects `_`.

### [Resource references](#resource-references)

Resource snapshots contain the resource's current fields. Container context uses compact references instead of duplicating complete resources:

- `RepositoryReference` identifies a repository.
- `PullRequestReference` identifies a pull request and nests its repository reference.
- `ThreadReference` identifies the thread containing a pull request comment.
- `OriginActor` identifies a public actor as one of `user`, `app`, or `serviceAccount`. Exactly one variant is present; read the identity from that variant.

## [Current limitations](#current-limitations)

- Namespace-wide repository listing and repository creation are not part of the partner API. Discover repositories through the installation.
- Commit comparison returns summary data rather than an embedded commit list. Changed files have their own paginated endpoint, [List Comparison Files](#list-comparison-files).
- Threads are addressable only for resolution. There is no endpoint that lists threads directly; read them from the comments they contain.
- Push webhooks do not include a complete commit list.
- Pull request merge supports native Origin repositories. Mirrored repositories are rejected.
- A mirrored repository is read-only for an installation until it becomes a stable outbound mirror. See [Mirrored repositories](#mirrored-repositories).

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

Download the [OpenAPI specification](https://cursor.com/docs/api/origin/openapi.yaml) for the complete component schemas. The document declares `https://api.cursor.com` as its server and a `bearerAuth` HTTP bearer security scheme, and each operation lists the response codes that operation can return, plus a request and response example. Every operation also carries an `x-origin-scopes` extension: `scopes` holds the scope the operation requires, and `tokenTypes` holds the credential kinds it accepts. Path parameters carry the same names the URLs use, `ownerSlug` and `repoName`. Every operation carries a unique `operationId`; where one operation answers two URL shapes, the second shape's id takes a `_2` suffix, as in `OriginService_GetRepoTarball_2`.

The JSON snippets show schema-shaped placeholder values. Response field descriptions reflect the OpenAPI schema and current platform contract.

## [Apps and installations](#apps-and-installations)

### [Get Rate Limit](#get-rate-limit)

GET`/v1/origin/rate_limit`

AuthApp JWTInstallation tokenUser access token

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
{  "resources": {    "core": {      "limit": 6000,      "remaining": 5994,      "reset": 1785682800,      "used": 6    }  },  "rate": {    "limit": 6000,    "remaining": 5994,    "reset": 1785682800,    "used": 6  }}
```

### [Get Authenticated App](#get-authenticated-app)

GET`/v1/origin/app`

AuthApp JWT

Returns metadata for the authenticated app.

#### [Response Fields](#response-fields-1)

`id` string

Origin app identifier used as the JWT issuer and key ID.

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

`namespaceSlug` string

Slug of the namespace that owns the app.

`description` string

Publisher-provided app description. Empty when unset.

`websiteUrl` string

Publisher website. Empty when unset.

`defaultScopes` array

Default scopes offered when the app is installed, as catalog scope strings.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "app_01k2ja2000e0080000000000a1",  "displayName": "CI Status Bot",  "webhookUrl": "https://ci.acme.dev/webhooks/origin",  "events": [    "pull_request.created",    "pull_request.merged"  ],  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "installationRedirectUris": [    "https://ci.acme.dev/origin/setup"  ],  "namespaceSlug": "acme",  "description": "Posts CI status on pull requests.",  "websiteUrl": "https://ci.acme.dev",  "defaultScopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}
```

### [List App Installations](#list-app-installations)

GET`/v1/origin/app/installations`

AuthApp JWT

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

`installations[].installedBy` object

The user who originally installed the app, not the most recent re-consent actor. Output-only. Absent when that user record can no longer be read.

`installations[].installedBy.id` string

Public identifier for the user, prefixed `user_`.

`installations[].installedBy.email` string

Email address of the user.

`installations[].installedBy.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`installations[].installedBy.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`installations[].suspendedAt` string

RFC 3339 timestamp set while the installation is suspended. Omitted while the installation is active.

`installations[].deletedAt` string

RFC 3339 timestamp for the installation's deletion. Carried only on the `installation.deleted` webhook snapshot; a deleted installation no longer resolves through the API, so this endpoint never returns it.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app/installations' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "installations": [    {      "id": "inst_01k2ja2000e0080000000000b2",      "appId": "app_01k2ja2000e0080000000000a1",      "target": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      },      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "repoSelectionMode": "selected",      "scopes": [        "repository:contents:read",        "repository:pull_requests:read"      ]    }  ]}
```

### [Get App Installation](#get-app-installation)

GET`/v1/origin/app/installations/{installationId}`

AuthApp JWT

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

`installedBy` object

The user who originally installed the app, not the most recent re-consent actor. Output-only. Absent when that user record can no longer be read.

`installedBy.id` string

Public identifier for the user, prefixed `user_`.

`installedBy.email` string

Email address of the user.

`installedBy.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`installedBy.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`suspendedAt` string

RFC 3339 timestamp set while the installation is suspended. Omitted while the installation is active.

`deletedAt` string

RFC 3339 timestamp for the installation's deletion. Carried only on the `installation.deleted` webhook snapshot; a deleted installation no longer resolves through the API, so this endpoint never returns it.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "inst_01k2ja2000e0080000000000b2",  "appId": "app_01k2ja2000e0080000000000a1",  "target": {    "slug": "acme",    "id": "ns_01k2ja2000e0080000000000p3",    "type": "team"  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "repoSelectionMode": "selected",  "scopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}
```

### [Delete App Installation](#delete-app-installation)

DELETE`/v1/origin/app/installations/{installationId}`

AuthApp JWT

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

AuthApp JWT

Creates an installation access token for the authenticated app.

Requires app signing-JWT authentication, like GetAuthenticatedApp. The token is scoped to the named installation, which must belong to the authenticated app. Callers may attenuate the token to a subset of the installation's accepted scopes and accessible repositories.

`repositoryIds` can name a mirrored repository. The resulting token carries the installation's scopes, and Origin still applies the mirror ceiling on each request: see [Mirrored repositories](#mirrored-repositories).

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID/access_tokens' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "scopes": [    "repository:contents:read",    "repository:pull_requests:read"  ],  "repositoryIds": [    "repo_01k2ja2000e0080000000000q4"  ]}'
```

**Response shape:**

```
{  "token": "oit_2v8xkq4m1c7p9t3w5y0z6r4b",  "expiresAt": "2026-08-01T10:30:00Z"}
```

### [List App Installation Repositories](#list-app-installation-repositories)

GET`/v1/origin/installation/repos`

AuthInstallation token

Lists repositories accessible to the authenticated app installation.

Requires an installation access token (`oit_`) minted by CreateInstallationAccessToken.

Partners discover their repositories through this endpoint. List entries are sparse repository summaries; use [Get Repo](#get-repo) for full timestamps. [Get Repo](#get-repo) includes the output-only `cloneUrl`.

Results include mirrored repositories. A mirror is read-only until it becomes a stable outbound mirror: see [Mirrored repositories](#mirrored-repositories).

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

`repositories[].visibility` string

Repository visibility. Allowed values: `internal`, `private`.

`repositories[].allowMergeCommit` boolean

Whether pull requests can land as merge commits.

`repositories[].allowSquashMerge` boolean

Whether pull requests can land as squash merges.

`repositories[].deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

`repoSelectionMode` string

Reports whether the installation grants all repositories or only selected repositories.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/installation/repos' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "repositories": [    {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "fullName": "acme/rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      },      "defaultBranch": "main",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "pushedAt": "2026-08-02T14:45:00Z",      "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git"    }  ],  "repoSelectionMode": "selected"}
```

### [List Webhook Deliveries](#list-webhook-deliveries)

GET`/v1/origin/app/webhook/deliveries`

AuthApp JWT

Lists webhook deliveries for the authenticated app, newest first.

A delivery is one event owed to one app; its id is the `webhook-id` header value the receiver sees. `delivered=false` is the recovery predicate: it selects every delivery that has never received a `2xx`, including deliveries whose retry ladder ran out during an outage.

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

Stable delivery identifier and the `webhook-id` value the receiver sees; use it as the idempotency key.

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
{  "deliveries": [    {      "id": "whd_01k2ja2000e0080000000000j9",      "event": {        "id": "evt_01k2ja2000e0080000000000r5",        "type": "pull_request.created"      },      "installation": {        "id": "inst_01k2ja2000e0080000000000b2",        "target": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      },      "createdAt": "2026-08-01T09:30:00Z",      "deliveredAt": "2026-08-02T14:45:05Z",      "lastAttempt": {        "id": "wha_01k2ja2000e0080000000000k0",        "deliveryId": "whd_01k2ja2000e0080000000000j9",        "trigger": "automatic",        "responseStatusCode": 200,        "latencyMs": 182,        "attemptedAt": "2026-08-02T14:45:05Z"      }    }  ]}
```

### [Batch Redeliver Webhook Deliveries](#batch-redeliver-webhook-deliveries)

POST`/v1/origin/app/webhook/deliveries:batchRedeliver`

AuthApp JWT

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/app/webhook/deliveries:batchRedeliver' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "deliveryIds": [    "whd_01k2ja2000e0080000000000j9"  ]}'
```

**Response shape:**

```
{  "results": [    {      "deliveryId": "whd_01k2ja2000e0080000000000j9",      "outcome": "queued"    }  ]}
```

### [Ping Webhook](#ping-webhook)

POST`/v1/origin/app/webhook/pings`

AuthApp JWT

Sends a test delivery to the authenticated app's webhook URL and reports what the receiver answered.

Use it to verify a receiver while you set an app up, instead of waiting for a real event. Requires app signing-JWT authentication, like [Get Authenticated App](#get-authenticated-app).

The receiver sees the production shape: the same [headers](#headers) and `v1ed` signature, verifiable against the [signing keys](#discovery-and-signing-keys), with `webhook-event-type` set to `ping` and a payload naming the app. A ping belongs to no installation, so the `webhook-installation-id` header and the envelope's `installationId` are both absent.

Origin sends the ping once, synchronously, and reports the outcome in the response. There are no retries, and a ping is not a domain event: it never appears in [List Webhook Deliveries](#list-webhook-deliveries) and cannot be redelivered. A receiver that fails is reported in the response rather than as an error. An app with no webhook URL configured returns `FailedPrecondition` (HTTP 400).

#### [Request Body](#request-body-2)

The request takes no fields. Send an empty JSON object.

#### [Response Fields](#response-fields-9)

`deliveryId` string

The test delivery's `webhook-id`, matching the header the receiver saw.

`eventId` string

Event ID inside the signed envelope, the same value as `event.id`.

`delivered` boolean

True when the receiver answered with a `2xx` status before the delivery timeout. Always present.

`responseStatusCode` integer

HTTP status the receiver answered with, or `0` when no response arrived because the connection failed or timed out. Always present.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/app/webhook/pings' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{}'
```

**Response shape:**

```
{  "deliveryId": "whd_01k2ja2000e0080000000000j9",  "eventId": "evt_01k2ja2000e0080000000000r5",  "delivered": true,  "responseStatusCode": 200}
```

### [Get App](#get-app)

GET`/v1/origin/apps/{appId}`

Scope[app:settings:read](#scopes)AuthUser access token

Returns a single app by its identifier. This is the management read for app publishers; [Get Authenticated App](#get-authenticated-app) is the equivalent self-read for the app's own JWT credential.

#### [Path Parameters](#path-parameters-3)

`appId` string Required

App identifier, prefixed `app_`.

#### [Response Fields](#response-fields-10)

`id` string

Globally unique app identifier, prefixed `app_`.

`displayName` string

Human-facing app name.

`webhookUrl` string

Registered HTTPS URL that receives the app's webhook deliveries. Empty when the app receives no deliveries.

`events` array

Webhook event subscriptions configured for the app.

`createdAt` string

RFC 3339 timestamp for app creation.

`updatedAt` string

RFC 3339 timestamp for the latest app metadata update.

`installationRedirectUris` array

OAuth install callback allowlist: redirect URIs an app-initiated install can return to, matched exactly at authorize time.

`namespaceSlug` string

Slug of the namespace that owns the app.

`description` string

Publisher-provided app description. Empty when unset.

`websiteUrl` string

Publisher website. Empty when unset.

`defaultScopes` array

Default scopes offered when the app is installed, as catalog scope strings.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/apps/{appId}' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "app_01k2ja2000e0080000000000a1",  "displayName": "CI Status Bot",  "webhookUrl": "https://ci.acme.dev/webhooks/origin",  "events": [    "pull_request.created",    "pull_request.merged"  ],  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "installationRedirectUris": [    "https://ci.acme.dev/origin/setup"  ],  "namespaceSlug": "acme",  "description": "Posts CI status on pull requests.",  "websiteUrl": "https://ci.acme.dev",  "defaultScopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}
```

### [Update App](#update-app)

PATCH`/v1/origin/apps/{appId}`

Scope[app:settings:write](#scopes)AuthUser access token

Updates an app's settings. Omitted fields are left unchanged, and at least one settable field must be provided. Clearing `webhookUrl` by sending an empty string disables outbound webhook delivery and cancels the app's pending deliveries; setting a URL again does not resurrect cancelled deliveries.

#### [Path Parameters](#path-parameters-4)

`appId` string Required

App identifier, prefixed `app_`.

#### [Request Body](#request-body-3)

`displayName` string

New human-facing app name. Must not be empty when provided.

`webhookUrl` string

New outbound webhook delivery URL, an absolute HTTPS URL. An empty string disables webhook delivery and cancels the app's pending deliveries.

`events` object

Clean replace of the webhook event subscriptions. Omit to leave them unchanged.

`events.events` array

The app's complete new set of webhook event subscriptions. An empty list clears them.

`description` string

New app description. Omit to leave it unchanged; an empty string clears it.

`websiteUrl` string

New publisher website. Omit to leave it unchanged; an empty string clears it.

`installationRedirectUris` object

Clean replace of the OAuth install callback allowlist. Omit to leave it unchanged.

`installationRedirectUris.installationRedirectUris` array

The complete new allowlist. An empty list clears it.

`defaultScopes` object

Clean replace of the app's default install scopes. Omit to leave them unchanged.

`defaultScopes.scopes` array

The complete new set of default install scopes. An empty list clears them.

#### [Response Fields](#response-fields-11)

`id` string

Globally unique app identifier, prefixed `app_`.

`displayName` string

Human-facing app name.

`webhookUrl` string

Registered HTTPS URL that receives the app's webhook deliveries. Empty when the app receives no deliveries.

`events` array

Webhook event subscriptions configured for the app.

`createdAt` string

RFC 3339 timestamp for app creation.

`updatedAt` string

RFC 3339 timestamp for the latest app metadata update.

`installationRedirectUris` array

OAuth install callback allowlist: redirect URIs an app-initiated install can return to, matched exactly at authorize time.

`namespaceSlug` string

Slug of the namespace that owns the app.

`description` string

Publisher-provided app description. Empty when unset.

`websiteUrl` string

Publisher website. Empty when unset.

`defaultScopes` array

Default scopes offered when the app is installed, as catalog scope strings.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/apps/APP_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "webhookUrl": "https://ci.acme.dev/webhooks/origin-v2",  "events": {    "events": [      "pull_request.created",      "pull_request.merged",      "repository.pushed"    ]  }}'
```

**Response shape:**

```
{  "id": "app_01k2ja2000e0080000000000a1",  "displayName": "CI Status Bot",  "webhookUrl": "https://ci.acme.dev/webhooks/origin-v2",  "events": [    "pull_request.created",    "pull_request.merged",    "repository.pushed"  ],  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "installationRedirectUris": [    "https://ci.acme.dev/origin/setup"  ],  "namespaceSlug": "acme",  "description": "Posts CI status on pull requests.",  "websiteUrl": "https://ci.acme.dev",  "defaultScopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}
```

### [Add App Signing Key](#add-app-signing-key)

POST`/v1/origin/apps/{appId}/signing_keys`

Scope[app:settings:write](#scopes)AuthUser access token

Adds a signing key to an app. Apps hold a bounded set of active signing keys; adding a key beyond the limit returns `FailedPrecondition` (HTTP 400) until another key is revoked. A key that is already registered returns `AlreadyExists` (HTTP 409 Conflict).

#### [Path Parameters](#path-parameters-5)

`appId` string Required

App identifier, prefixed `app_`.

#### [Request Body](#request-body-4)

`publicKey` string Required

PEM SPKI Ed25519 public key to add to the app's signing key set.

#### [Response Fields](#response-fields-12)

`kid` string

Key ID: the base64url-encoded SHA-256 digest of the key's SPKI DER encoding. Use it as the JWT `kid` header and to revoke the key.

`createdAt` string

RFC 3339 timestamp for when the key was registered.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/apps/APP_ID/signing_keys' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "publicKey": "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAq9zTf3hL6wXe1cVj0bYs5mKR8uDnG2oAaPp4NiEkKlM=\n-----END PUBLIC KEY-----"}'
```

**Response shape:**

```
{  "kid": "3q2xW9dK5fJm8vB1nY6cT0aZrQpLh4eGkVsN7uMxOdI",  "createdAt": "2026-08-02T14:45:00Z"}
```

### [Revoke App Signing Key](#revoke-app-signing-key)

DELETE`/v1/origin/apps/{appId}/signing_keys/{kid}`

Scope[app:settings:write](#scopes)AuthUser access token

Revokes an app signing key by its key ID. App JWTs signed with a revoked key stop authenticating. The last active signing key cannot be revoked; that request returns `FailedPrecondition` (HTTP 400). The response body is empty.

#### [Path Parameters](#path-parameters-6)

`appId` string Required

App identifier, prefixed `app_`.

`kid` string Required

Key ID of the signing key to revoke.

#### [Response Fields](#response-fields-13)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/apps/{appId}/signing_keys/{kid}' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [List Namespace Apps](#list-namespace-apps)

GET`/v1/origin/namespaces/{namespaceSlug}/apps`

Scope[namespace:apps:read](#scopes)AuthUser access token

Lists the apps a namespace owns, newest first. Responses carry display metadata only; read one app's webhook configuration with [Get App](#get-app).

#### [Path Parameters](#path-parameters-7)

`namespaceSlug` string Required

Slug of the namespace whose apps to list.

#### [Query Parameters](#query-parameters-3)

`pageSize` integer

Max apps to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-14)

`apps` array

Page of apps the namespace owns.

`apps[].id` string

Globally unique app identifier, prefixed `app_`.

`apps[].displayName` string

Human-facing app name.

`apps[].description` string

Publisher-provided description. Empty when unset.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/namespaces/{namespaceSlug}/apps' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "apps": [    {      "id": "app_01k2ja2000e0080000000000a1",      "displayName": "CI Status Bot",      "description": "Posts CI status on pull requests."    },    {      "id": "app_01k2ja2000e0080000000000a2",      "displayName": "Deploy Bot",      "description": ""    }  ],  "nextPageToken": ""}
```

### [Create App](#create-app)

POST`/v1/origin/namespaces/{namespaceSlug}/apps`

Scope[namespace:apps:create](#scopes)AuthUser access token

Creates an app owned by a namespace. Apps are created private. Generate the Ed25519 key pair locally and send only the public key; Origin stores it to verify the app's JWTs. Invalid webhook URLs, event types, redirect URIs, or scopes return `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-8)

`namespaceSlug` string Required

Slug of the namespace that will own the app.

#### [Request Body](#request-body-5)

`displayName` string Required

Human-facing app name. Must not be empty.

`publicKey` string Required

PEM SPKI Ed25519 public key for the app's signing key pair. See [Generate an app signing key](#generate-an-app-signing-key).

`webhookUrl` string

Outbound webhook delivery URL, an absolute HTTPS URL. Empty means the app receives no webhook deliveries.

`events` array

Webhook event subscriptions, as event slugs from [Events](#events). Unknown event types are rejected.

`description` string

Short app description.

`websiteUrl` string

Publisher website, an absolute HTTPS URL.

`installationRedirectUris` array

OAuth install callback allowlist: absolute HTTPS URIs without a fragment, matched exactly at authorize time.

`defaultScopes` array

Default scopes offered when the app is installed, as catalog scope strings such as `repository:contents:read`. Installs still accept scopes explicitly.

#### [Response Fields](#response-fields-15)

`id` string

Globally unique app identifier, prefixed `app_`.

`displayName` string

Human-facing app name.

`webhookUrl` string

Registered HTTPS URL that receives the app's webhook deliveries. Empty when the app receives no deliveries.

`events` array

Webhook event subscriptions configured for the app.

`createdAt` string

RFC 3339 timestamp for app creation.

`updatedAt` string

RFC 3339 timestamp for the latest app metadata update.

`installationRedirectUris` array

OAuth install callback allowlist: redirect URIs an app-initiated install can return to, matched exactly at authorize time.

`namespaceSlug` string

Slug of the namespace that owns the app.

`description` string

Publisher-provided app description. Empty when unset.

`websiteUrl` string

Publisher website. Empty when unset.

`defaultScopes` array

Default scopes offered when the app is installed, as catalog scope strings.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/namespaces/NAMESPACE_SLUG/apps' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "displayName": "CI Status Bot",  "publicKey": "-----BEGIN PUBLIC KEY-----\nMCowBQYDK2VwAyEAv7wFoV1bC9yKq3nZ8dQmXh5uJb2tR4sEwG6aP0iN8kY=\n-----END PUBLIC KEY-----",  "webhookUrl": "https://ci.acme.dev/webhooks/origin",  "events": [    "pull_request.created",    "pull_request.merged"  ],  "description": "Posts CI status on pull requests.",  "websiteUrl": "https://ci.acme.dev",  "installationRedirectUris": [    "https://ci.acme.dev/origin/setup"  ],  "defaultScopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}'
```

**Response shape:**

```
{  "id": "app_01k2ja2000e0080000000000a1",  "displayName": "CI Status Bot",  "webhookUrl": "https://ci.acme.dev/webhooks/origin",  "events": [    "pull_request.created",    "pull_request.merged"  ],  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-01T09:30:00Z",  "installationRedirectUris": [    "https://ci.acme.dev/origin/setup"  ],  "namespaceSlug": "acme",  "description": "Posts CI status on pull requests.",  "websiteUrl": "https://ci.acme.dev",  "defaultScopes": [    "repository:contents:read",    "repository:pull_requests:read"  ]}
```

## [Repositories](#repositories)

`cloneUrl` is an output-only HTTPS clone URL. [Get Repo](#get-repo) includes `cloneUrl`.

Partners discover their repositories through [List App Installation Repositories](#list-app-installation-repositories). Namespace-wide repository listing and creation are not part of the partner API.

### [List Repos](#list-repos)

GET`/v1/origin/repos/{ownerSlug}`

Scope[namespace:repositories:read](#scopes)AuthUser access token

Lists repos belonging to an owner entity.

#### [Path Parameters](#path-parameters-9)

`ownerSlug` string Required

Parent owner entity slug.

#### [Query Parameters](#query-parameters-4)

`pageSize` integer

Max repos to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

`filter` string

Optional case-insensitive substring filter.

#### [Response Fields](#response-fields-16)

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

`repositories[].visibility` string

Repository visibility. Allowed values: `internal`, `private`.

`repositories[].allowMergeCommit` boolean

Whether pull requests can land as merge commits.

`repositories[].allowSquashMerge` boolean

Whether pull requests can land as squash merges.

`repositories[].deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "repositories": [    {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "fullName": "acme/rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      },      "defaultBranch": "main",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "pushedAt": "2026-08-02T14:45:00Z",      "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git"    }  ]}
```

### [Get Repo](#get-repo)

GET`/v1/origin/repos/{ownerSlug}/{repoName}`

Scope[repository:metadata:read](#scopes)AuthInstallation tokenUser access token

Returns a single repo by its `(owner_id, name)` identifier.

`cloneUrl` is an output-only HTTPS clone URL. Get repository includes `cloneUrl`.

#### [Path Parameters](#path-parameters-10)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-17)

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

`visibility` string

Repository visibility. Allowed values: `internal`, `private`.

`allowMergeCommit` boolean

Whether pull requests can land as merge commits.

`allowSquashMerge` boolean

Whether pull requests can land as squash merges.

`deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "repo_01k2ja2000e0080000000000q4",  "name": "rocket",  "fullName": "acme/rocket",  "owner": {    "slug": "acme",    "id": "ns_01k2ja2000e0080000000000p3",    "type": "team"  },  "defaultBranch": "main",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "pushedAt": "2026-08-02T14:45:00Z",  "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git"}
```

### [Update Repo](#update-repo)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}`

Scope[repository:settings:write](#scopes)AuthInstallation tokenUser access token

Updates repository settings. Omitted fields are left unchanged, and at least one settable field must be provided.

Settings apply as independent groups in a fixed order: default branch, automatic head-branch deletion, visibility, then merge methods. The update is not atomic across groups. When a group is rejected, the groups before it in that order are already applied and stay applied, so retry with the rejected group corrected to converge on the state you asked for. The response carries the repository as of the last group applied.

A request that sets no field returns `InvalidArgument` (HTTP 400). A concurrent change to the default branch returns `409 Conflict`.

#### [Path Parameters](#path-parameters-11)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-6)

`defaultBranch` string

New default branch. Must name an existing branch. Supported only on repositories that neither pull from nor push to an upstream source; other repositories return `FailedPrecondition` (HTTP 400).

`allowMergeCommit` boolean

Whether pull requests can land as merge commits. Must be sent together with `allowSquashMerge`, and at least one of the two must be `true`. Sending one without the other returns `InvalidArgument` (HTTP 400).

`allowSquashMerge` boolean

Whether pull requests can land as squash merges. Must be sent together with `allowMergeCommit`, and at least one of the two must be `true`. Sending one without the other returns `InvalidArgument` (HTTP 400).

`deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge. Supported only on repositories whose pull requests live on this API; a repository that pulls from an upstream source returns `FailedPrecondition` (HTTP 400).

`visibility` string

New repository visibility. Allowed values: `internal`, `private`. Omit it to leave the visibility unchanged.

#### [Response Fields](#response-fields-18)

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

`visibility` string

Repository visibility. Allowed values: `internal`, `private`.

`allowMergeCommit` boolean

Whether pull requests can land as merge commits.

`allowSquashMerge` boolean

Whether pull requests can land as squash merges.

`deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "defaultBranch": "main",  "allowMergeCommit": false,  "allowSquashMerge": true,  "deleteBranchOnMerge": true,  "visibility": "private"}'
```

**Response shape:**

```
{  "id": "repo_01k2ja2000e0080000000000q4",  "name": "rocket",  "fullName": "acme/rocket",  "owner": {    "slug": "acme",    "id": "ns_01k2ja2000e0080000000000p3",    "type": "team"  },  "defaultBranch": "main",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "pushedAt": "2026-08-02T14:45:00Z",  "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",  "visibility": "private",  "allowMergeCommit": false,  "allowSquashMerge": true,  "deleteBranchOnMerge": true}
```

### [Create Repo](#create-repo)

POST`/v1/origin/repos/{ownerSlug}`

Scope[namespace:new\_repository:write](#scopes)AuthUser access token

Creates a repo belonging to an owner.

The owner must be eligible to write to Origin when the request is made. A user owner must be on a Pro, Pro Student, Pro+, Ultra, or Start plan. A team owner must have an active paid team plan, must not be on Privacy Mode (Legacy), and must not have Origin turned off by a team admin. An ineligible owner returns `FailedPrecondition` (HTTP 400). Reading existing repositories does not carry this requirement.

Repository names are claimed case-insensitively. A name that differs only in case from a repository the owner already has is rejected, so `widgets` and `Widgets` cannot coexist in one namespace. The name you send is stored as you send it.

The first push to a new repo can retarget its default branch. When that push only creates branches and none of them is the repo's stored default branch, Origin sets the default branch to the created branch, or to `main` or `master` when the push creates several and one of those names is among them. The default branch is otherwise unchanged. Read the current value from [Get Repo](#get-repo).

#### [Path Parameters](#path-parameters-12)

`ownerSlug` string Required

Parent owner entity's slug.

#### [Request Body](#request-body-7)

`name` string Required

The repo name, unique to its owner. Required on create.

`defaultBranch` string

Default branch name. Always set on responses. On create, omitting this field or leaving it empty defaults to "main".

#### [Response Fields](#response-fields-19)

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

`visibility` string

Repository visibility. Allowed values: `internal`, `private`.

`allowMergeCommit` boolean

Whether pull requests can land as merge commits.

`allowSquashMerge` boolean

Whether pull requests can land as squash merges.

`deleteBranchOnMerge` boolean

Whether the head branch is deleted automatically on merge.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "rocket",  "defaultBranch": "main"}'
```

**Response shape:**

```
{  "id": "repo_01k2ja2000e0080000000000q4",  "name": "rocket",  "fullName": "acme/rocket",  "owner": {    "slug": "acme",    "id": "ns_01k2ja2000e0080000000000p3",    "type": "team"  },  "defaultBranch": "main",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "pushedAt": "2026-08-02T14:45:00Z",  "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git"}
```

### [List Branches](#list-branches)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/branches`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists the repo's branches and tip commits in ascending name order, paginated with `page_size` and `page_token`.

#### [Path Parameters](#path-parameters-13)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-5)

`pageSize` integer

Max branches to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the page offset, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-20)

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
{  "branches": [    {      "name": "main",      "commit": {        "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"      }    }  ]}
```

### [Get Repo Tarball](#get-repo-tarball)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/tarball/{ref}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Downloads a gzip-compressed tar of the repository tree at `ref`.

Origin keys the archive on the repository and the commit `ref` resolves to. The first request for a given commit responds `200` with `Content-Type: application/gzip` and streams the archive as the response body. Later requests for the same commit respond `302` with an empty body and a signed download URL in `Location`, valid for 15 minutes; follow the redirect to fetch the bytes. Archive entries sit at the root of the tar, with no wrapping directory. An empty repository returns `ABORTED` (HTTP 409 Conflict), and a ref that does not resolve returns `404`.

Send the ref as a query parameter instead of a path segment to address a ref containing "/": `GET /v1/origin/repos/{ownerSlug}/{repoName}/tarball?ref=refs/heads/main`. Omit it to archive the repository's default branch.

#### [Path Parameters](#path-parameters-14)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`ref` string Required

Commit SHA (full or abbreviated hex), bare branch or tag name, fully qualified `refs/heads/...` or `refs/tags/...`, or symbolic `HEAD`. Not a glob or revspec, so `<rev>~3` is rejected. Empty uses the repository default branch.

#### [Response Fields](#response-fields-21)

`sha` string

Resolved commit object ID: 40- or 64-character hex. Returned to Connect and JSON callers; over REST, read it from the archive filename or the signed URL.

`downloadUrl` string

Short-lived signed download URL, valid for 15 minutes. Empty when the response streams the archive inline, which is the first request for this repository and commit. Over REST the same URL is sent as the `Location` header on the `302`.

```
curl --request GET --location --output repo.tar.gz \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/tarball/HEAD' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "downloadUrl": "https://artifacts.origin.cursor.com/tarballs/0192f7a4-6c1e-7b3a-9f21-3d54c9a7e6b0/9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4.tar.gz?Expires=1767225600&Signature=EXAMPLE&Key-Pair-Id=KEXAMPLE123",  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"}
```

### [Sync Mirror](#sync-mirror)

POST`/v1/origin/repos/{ownerSlug}/{repoName}:syncMirror`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Synchronizes one ref of a mirrored repository from its upstream source. Returns HTTP `200` when the sync target is satisfied, or HTTP `202` when the sync is still pending. `wait=false` (the default) schedules the sync and usually returns `202`; it returns `200` immediately when `sha` is already reachable from `ref`. `wait=true` blocks until satisfied or the wait budget (~2 minutes) expires; expiry still returns `202` and the sync continues in the background. Repositories that do not pull from an upstream source are rejected.

#### [Path Parameters](#path-parameters-15)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-8)

`ref` string Required

Full git ref name to fetch. Must start with `refs/` and name a ref after that prefix, for example `refs/heads/main` or `refs/tags/v1`. Short names such as `main` are rejected with `INVALID_ARGUMENT`.

`wait` boolean

When true, block until synced or the wait budget expires. Defaults to false.

`sha` string

Optional full commit object ID: 40- or 64-character hex. Omit or leave empty to wait on the tip of `ref`. When set and reachable from `ref`, the call returns early without waiting for other mirror work to drain. Other values are rejected with `INVALID_ARGUMENT`.

#### [Response Fields](#response-fields-22)

`synced` boolean

True when the sync target is known to be satisfied, false while the sync is still pending. Always present, mirroring the HTTP status: `200` when true, `202` when false.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME:syncMirror' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "ref": "refs/heads/main",  "wait": true}'
```

**Response shape:**

```
{  "synced": true}
```

### [Detach Repo Mirror](#detach-repo-mirror)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/mirror`

Scope[repository:mirror:delete](#scopes)AuthUser access token

Permanently disconnects a mirrored repository from its upstream source. The repository keeps its current contents and becomes a native repository, syncing stops in both directions, and the mirror's deploy credential is deleted. The response body is empty.

Detaching is not reversible through this API. A repository that never had a mirror returns `FailedPrecondition` (HTTP 400); detaching an already-detached repository succeeds without effect.

#### [Path Parameters](#path-parameters-16)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-23)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [Get Mirror Transition Job](#get-mirror-transition-job)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs/{jobId}`

Scope[repository:metadata:read](#scopes)AuthInstallation tokenUser access token

Returns one mirror transition job by id. An unknown job id returns `404`.

#### [Path Parameters](#path-parameters-17)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`jobId` string Required

Identifier of the transition job, as returned in `job.id`.

#### [Response Fields](#response-fields-24)

`id` string

Unique identifier of the job.

`transition` string

The mirror-direction change this job performs. Allowed values: `initial_to_inbound`, `inbound_to_outbound`, `outbound_to_inbound`.

`status` string

Lifecycle state. Allowed values: `queued`, `running`, `succeeded`, `failed_rolled_back`, `requires_attention`, `superseded`. `succeeded`, `failed_rolled_back`, and `superseded` are terminal. `requires_attention` needs operator intervention or a forced cutover.

`phase` string

Progress detail within `status`, for display and debugging. One of `queued`, `starting`, `draining-writes`, `initializing-mirror-fetch`, `finalizing-mirror-fetch`, `finalizing-mirror-push`, `snapshotting-refs`, `verifying-integrity`, `reopening-inbound-mirror`, `committing-target-status`, `rolling-back`, or `completed`. New phases can appear as the transition process evolves, so poll `status` for completion rather than matching on phases.

`attemptCount` integer

Number of times this job has been attempted.

`drainUntil` string

RFC 3339 timestamp of when the write-drain window of an in-progress transition ends. Absent outside the draining phase.

`lastErrorCode` string

Stable code identifying why the job last failed, such as `InboundMirrorDrainTimeout` or `MirrorIntegrityMismatch`. Absent while the job has not failed.

`lastErrorMessage` string

Human-readable detail for `lastErrorCode`. Absent while the job has not failed.

`startedAt` string

RFC 3339 timestamp of when the job started running. Absent while queued.

`completedAt` string

RFC 3339 timestamp of when the job reached a terminal status. Absent until then.

`createdAt` string

RFC 3339 job creation timestamp.

`updatedAt` string

RFC 3339 job update timestamp.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs/JOB_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "rmt_01k2ja2000e0080000000000m3",  "transition": "inbound_to_outbound",  "status": "succeeded",  "phase": "completed",  "attemptCount": 1,  "startedAt": "2026-08-02T15:00:00Z",  "completedAt": "2026-08-02T15:12:00Z",  "createdAt": "2026-08-02T14:59:30Z",  "updatedAt": "2026-08-02T15:12:00Z"}
```

### [Get Active Mirror Transition Job](#get-active-mirror-transition-job)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/mirror/transition-jobs:active`

Scope[repository:metadata:read](#scopes)AuthInstallation tokenUser access token

Returns the repository's currently active mirror transition job and its most recent terminal one. Both fields are optional, so a repository that has never transitioned returns an empty object. Poll this endpoint to follow a transition: once `activeJob` disappears, `lastJob` tells you how it ended.

#### [Path Parameters](#path-parameters-18)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-25)

`activeJob` object

The currently active transition job, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Absent when no transition is in progress.

`lastJob` object

The most recent job that reached a terminal status, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Absent when the repository has never completed a transition.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror/transition-jobs:active' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "activeJob": {    "id": "rmt_01k2ja2000e0080000000000m4",    "transition": "outbound_to_inbound",    "status": "running",    "phase": "draining-writes",    "attemptCount": 1,    "drainUntil": "2026-08-02T15:05:00Z",    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  },  "lastJob": {    "id": "rmt_01k2ja2000e0080000000000m3",    "transition": "inbound_to_outbound",    "status": "succeeded",    "phase": "completed",    "attemptCount": 1,    "startedAt": "2026-08-01T10:00:00Z",    "completedAt": "2026-08-01T10:12:00Z",    "createdAt": "2026-08-01T09:59:30Z",    "updatedAt": "2026-08-01T10:12:00Z"  }}
```

### [Force Repo Mirror Cutover](#force-repo-mirror-cutover)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/mirror:forceCutover`

Scope[repository:mirror:write](#scopes)AuthUser access token

Forces an `outbound_to_inbound` cutover without pushing this host's divergent state back to the upstream source. The source is adopted as the source of truth as it stands, and refs that exist only on this host are snapshotted and abandoned. Returns the job tracking the forced cutover.

Accepted only for a repository in `outbound` status, or one stuck in an outbound-to-inbound transition whose active job reports `requires_attention`, in which case that job is superseded. Any other state, including a queued or running transition job, returns `FailedPrecondition` (HTTP 400). The caller must administer the repository on the mirror's upstream source; a caller without that access returns `403`.

#### [Path Parameters](#path-parameters-19)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-9)

The request takes no fields. Send an empty JSON object.

#### [Response Fields](#response-fields-26)

`repository` object

The repository, reflecting its transitioning mirror state. Carries the same fields as [Get Repo](#get-repo).

`job` object

The job tracking the transition, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Poll it until it reaches a terminal status.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror:forceCutover' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{}'
```

**Response shape:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "main",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:00:00Z",    "pushedAt": "2026-08-02T14:45:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",    "mirror": {      "source": "github",      "sourceId": "R_kgDOAbc123",      "status": "outbound"    }  },  "job": {    "id": "rmt_01k2ja2000e0080000000000m4",    "transition": "outbound_to_inbound",    "status": "running",    "phase": "snapshotting-refs",    "attemptCount": 1,    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  }}
```

### [Transition Repo Mirror](#transition-repo-mirror)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/mirror:transition`

Scope[repository:mirror:write](#scopes)AuthUser access token

Starts a mirror-state transition on a mirrored repository and returns the job tracking it. The repository enters a transitioning mirror status while the job runs, so poll [Get Active Mirror Transition Job](#get-active-mirror-transition-job) or [Get Mirror Transition Job](#get-mirror-transition-job) until the job reaches a terminal status.

A repository that is not in the transition's expected start state, or that already has an active transition job, returns `FailedPrecondition` (HTTP 400). The caller must administer the repository on the mirror's upstream source; a caller without that access returns `403`.

#### [Path Parameters](#path-parameters-20)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-10)

`transition` string Required

The mirror-state change to start. Allowed values: `initial_to_inbound`, `inbound_to_outbound`, `outbound_to_inbound`.

#### [Response Fields](#response-fields-27)

`repository` object

The repository, reflecting its transitioning mirror state. Carries the same fields as [Get Repo](#get-repo).

`job` object

The job tracking the transition, carrying the same fields as [Get Mirror Transition Job](#get-mirror-transition-job). Poll it until it reaches a terminal status.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/mirror:transition' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "transition": "inbound_to_outbound"}'
```

**Response shape:**

```
{  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "fullName": "acme/rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    },    "defaultBranch": "main",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T15:00:00Z",    "pushedAt": "2026-08-02T14:45:00Z",    "cloneUrl": "https://origin.cursor.com/git/acme/rocket.git",    "mirror": {      "source": "github",      "sourceId": "R_kgDOAbc123",      "status": "inbound"    }  },  "job": {    "id": "rmt_01k2ja2000e0080000000000m3",    "transition": "inbound_to_outbound",    "status": "running",    "phase": "draining-writes",    "attemptCount": 1,    "drainUntil": "2026-08-02T15:05:00Z",    "startedAt": "2026-08-02T15:00:00Z",    "createdAt": "2026-08-02T14:59:30Z",    "updatedAt": "2026-08-02T15:01:00Z"  }}
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

Scope[repository:checks:write](#scopes)AuthInstallation token

Upserts a check suite + check run using an installation access token with `repository:checks:write`. The write is attributed to the app that owns the authenticated installation. A repeated call with the same `(repo, head_sha, suite.key, check.key)` updates the existing check run in place rather than creating a duplicate.

The endpoint atomically resolves or creates the suite attempt and upserts one run attempt. `externalUpdatedAt` orders updates to the same run identity; stale retries cannot overwrite newer state.

`deadlineAt` records an optional deadline on the run. Origin stores it, returns it on reads, and clears it once the run reaches `completed`. A deadline more than 24 hours in the future is rejected with `InvalidArgument` (HTTP 400) rather than clamped.

When the deadline passes on a run still `in_progress`, Origin completes the run itself with a `timed_out` conclusion and delivers `repository.check_run.completed`. Expiry runs as a periodic sweep rather than on a per-run timer, so a run can sit past its deadline briefly before Origin closes it. A `queued` run never expires, and neither does a run that carries no `deadlineAt`. Completing the run yourself before the deadline clears it. Origin leaves the run's `externalUpdatedAt` untouched when it times a run out, so a later completion from your provider can still overwrite the `timed_out` conclusion.

#### [Path Parameters](#path-parameters-21)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-11)

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

`checkRun.deadlineAt` string

Deadline for the check run, as an RFC 3339 timestamp. Values more than 24 hours in the future are rejected with `InvalidArgument` (HTTP 400) rather than clamped. Omit it on a create to record no deadline; omit it on an update to leave the stored deadline unchanged.

`checkRun.isRerequestable` boolean

Declares that the run can be run again on request. Setting it to `true` commits your app to subscribing to [`repository.check_run.rerequested`](#events) and answering each delivery by posting a fresh run for the same head SHA and `key`: either a new run under a new `externalId`, which keeps the old attempt as history, or an update of the re-requested run under the same `externalId`, which refreshes it in place. Until that fresh post arrives the re-requested run reads as pending in the commit's latest check state, so a required check blocks merging and the pull request shows the run as awaiting its re-run; declaring re-requestability without answering strands the check. Origin does not verify the subscription when you post. Omit it to keep the stored value, which is `false` on a new run; send `false` to withdraw the declaration.

#### [Response Fields](#response-fields-28)

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

`checkSuite.actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkSuite.actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkSuite.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuite.actor.app.id` string

Public identifier for the app.

`checkSuite.actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRun.actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkRun.actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkRun.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRun.actor.app.id` string

Public identifier for the app.

`checkRun.actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRun.deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`checkRun.isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`checkRun.rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`checkRun.rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "checkSuite": {    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalId": "build-8842"  },  "checkRun": {    "key": "ci-8842-unit-tests",    "name": "unit-tests",    "status": "completed",    "conclusion": "success",    "externalUpdatedAt": "2026-08-02T14:44:30Z",    "startedAt": "2026-08-02T14:40:00Z",    "completedAt": "2026-08-02T14:44:30Z",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalId": "run-8842",    "output": {      "title": "Unit tests",      "summary": "128 tests passed.",      "text": "All suites green."    }  }}'
```

**Response shape:**

```
{  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "externalId": "build-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    }  },  "checkRun": {    "id": "cr_01k2ja2000e0080000000000g7",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "checkSuite": {      "id": "crg_01k2ja2000e0080000000000h8"    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842-unit-tests",    "name": "unit-tests",    "status": "completed",    "conclusion": "success",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalUpdatedAt": "2026-08-02T14:44:30Z",    "startedAt": "2026-08-02T14:40:00Z",    "completedAt": "2026-08-02T14:44:30Z",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "externalId": "run-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "output": {      "title": "Unit tests",      "summary": "128 tests passed.",      "text": "All suites green."    }  }}
```

### [Batch Upsert Check Runs](#batch-upsert-check-runs)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs:batchUpsert`

Scope[repository:checks:write](#scopes)AuthInstallation token

Atomically upserts several check runs belonging to one suite. The request accepts at most 10 runs and rejects duplicate `(external_id, key)` identities. Every run is committed or the entire request is rolled back.

Each run accepts the same optional `deadlineAt` as [Post Check Run](#post-check-run).

#### [Path Parameters](#path-parameters-22)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-12)

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

`checkRuns[0].deadlineAt` string

Deadline for the check run, as an RFC 3339 timestamp. Values more than 24 hours in the future are rejected with `InvalidArgument` (HTTP 400) rather than clamped. Omit it on a create to record no deadline; omit it on an update to leave the stored deadline unchanged.

`checkRuns[0].isRerequestable` boolean

Declares that the run can be run again on request. Setting it to `true` commits your app to subscribing to [`repository.check_run.rerequested`](#events) and answering each delivery by posting a fresh run for the same head SHA and `key`: either a new run under a new `externalId`, which keeps the old attempt as history, or an update of the re-requested run under the same `externalId`, which refreshes it in place. Until that fresh post arrives the re-requested run reads as pending in the commit's latest check state, so a required check blocks merging and the pull request shows the run as awaiting its re-run; declaring re-requestability without answering strands the check. Origin does not verify the subscription when you post. Omit it to keep the stored value, which is `false` on a new run; send `false` to withdraw the declaration.

#### [Response Fields](#response-fields-29)

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

`checkSuite.actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkSuite.actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkSuite.actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuite.actor.app.id` string

Public identifier for the app.

`checkSuite.actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRuns[].actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkRuns[].actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRuns[].deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`checkRuns[].isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`checkRuns[].rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`checkRuns[].rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs:batchUpsert' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "checkSuite": {    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "externalId": "build-8842"  },  "checkRuns": [    {      "key": "ci-8842-unit-tests",      "name": "unit-tests",      "status": "completed",      "conclusion": "success",      "externalUpdatedAt": "2026-08-02T14:44:30Z",      "startedAt": "2026-08-02T14:40:00Z",      "completedAt": "2026-08-02T14:44:30Z",      "detailsUrl": "https://ci.acme.dev/runs/8842",      "externalId": "run-8842",      "output": {        "title": "Unit tests",        "summary": "128 tests passed.",        "text": "All suites green."      }    }  ]}'
```

**Response shape:**

```
{  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    },    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "key": "ci-8842",    "name": "CI",    "detailsUrl": "https://ci.acme.dev/runs/8842",    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "externalId": "build-8842",    "actor": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    }  },  "checkRuns": [    {      "id": "cr_01k2ja2000e0080000000000g7",      "repository": {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      },      "checkSuite": {        "id": "crg_01k2ja2000e0080000000000h8"      },      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "key": "ci-8842-unit-tests",      "name": "unit-tests",      "status": "completed",      "conclusion": "success",      "detailsUrl": "https://ci.acme.dev/runs/8842",      "externalUpdatedAt": "2026-08-02T14:44:30Z",      "startedAt": "2026-08-02T14:40:00Z",      "completedAt": "2026-08-02T14:44:30Z",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "externalId": "run-8842",      "actor": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "output": {        "title": "Unit tests",        "summary": "128 tests passed.",        "text": "All suites green."      }    }  ]}
```

### [Get Check Run](#get-check-run)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs/{checkRunId}`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Returns a single check run by server-assigned id (`cr_...`).

#### [Path Parameters](#path-parameters-23)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkRunId` string Required

Server-assigned check-run id (`cr_...`).

#### [Response Fields](#response-fields-30)

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

`actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`actor.app` object

App variant of the actor. Set when an app performed the action.

`actor.app.id` string

Public identifier for the app.

`actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs/CHECK_RUN_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "cr_01k2ja2000e0080000000000g7",  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8"  },  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "key": "ci-8842-unit-tests",  "name": "unit-tests",  "status": "completed",  "conclusion": "success",  "detailsUrl": "https://ci.acme.dev/runs/8842",  "externalUpdatedAt": "2026-08-02T14:44:30Z",  "startedAt": "2026-08-02T14:40:00Z",  "completedAt": "2026-08-02T14:44:30Z",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "externalId": "run-8842",  "actor": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "output": {    "title": "Unit tests",    "summary": "128 tests passed.",    "text": "All suites green."  }}
```

### [List Check Run Annotations](#list-check-run-annotations)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs/{checkRunId}/annotations`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Lists a check run's annotations in ascending ID order.

Annotation IDs are time-sortable, so ascending ID order is also creation order. A page token fixes the page size and scope for the rest of the sequence, so `pageSize` is ignored once you send one.

#### [Path Parameters](#path-parameters-24)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkRunId` string Required

Server-assigned check run ID.

#### [Query Parameters](#query-parameters-6)

`pageSize` integer

Maximum annotations to return. Defaults to 30 when omitted or zero; values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `nextPageToken`. Omit for the first page.

#### [Response Fields](#response-fields-31)

`annotations` array

Page of annotations, in ascending ID order.

`annotations[].id` string

Stable Origin annotation ID. IDs are time-sortable.

`annotations[].checkRunId` string

ID of the check run the annotation belongs to.

`annotations[].annotationLevel` string

Severity of the annotation. Allowed values: `notice`, `warning`, `failure`.

`annotations[].message` string

Annotation message.

`annotations[].title` string

Annotation title. Absent when the annotation has none.

`annotations[].rawDetails` string

Raw detail text. Absent when the annotation has none.

`annotations[].createdAt` string

When the annotation was created (RFC 3339).

`annotations[].updatedAt` string

When the annotation was last updated (RFC 3339).

`annotations[].location` object

Source location. Absent for a run-level annotation.

`annotations[].location.path` string

Canonical repository-relative file path.

`annotations[].location.startLine` integer

First line of the range. 1-based and inclusive.

`annotations[].location.endLine` integer

Last line of the range. 1-based and inclusive.

`annotations[].location.columns` object

Column range. Absent unless the annotation covers a single line.

`annotations[].location.columns.startColumn` integer

First column of the range. 1-based and inclusive.

`annotations[].location.columns.endColumn` integer

Last column of the range. 1-based and inclusive.

`nextPageToken` string

Opaque cursor for the next page. Empty when there are no more results.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs/CHECK_RUN_ID/annotations' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "annotations": [    {      "id": "cra_01k2ja2000e0080000000000v1",      "checkRunId": "cr_01k2ja2000e0080000000000g7",      "annotationLevel": "warning",      "message": "Deprecated API usage; migrate to the v2 client.",      "title": "Deprecated API",      "createdAt": "2026-08-02T14:45:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "location": {        "path": "src/telemetry.ts",        "startLine": 42,        "endLine": 42      }    }  ]}
```

### [Create Check Run Annotations](#create-check-run-annotations)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs/{checkRunId}/annotations`

Scope[repository:checks:write](#scopes)AuthInstallation token

Appends between 1 and 25 annotations to a check run in a single atomic batch.

A check run holds at most 100 annotations. A batch that would take it past that limit is rejected with `ResourceExhausted` (HTTP 429) and nothing is written; a batch outside the 1 to 25 range is rejected with `InvalidArgument` (HTTP 400). The operation is append-only and is not idempotent, so retrying after an ambiguous transport failure can append duplicates and consume capacity. Identical content is allowed.

#### [Path Parameters](#path-parameters-25)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkRunId` string Required

Server-assigned check run ID.

#### [Request Body](#request-body-13)

`annotations` array Required

The batch to append. Must contain between 1 and 25 entries.

`annotations[].annotationLevel` string Required

Severity of the annotation. Allowed values: `notice`, `warning`, `failure`.

`annotations[].message` string Required

Annotation message. Must be non-empty. Maximum 65,535 bytes of UTF-8.

`annotations[].title` string

Annotation title. Maximum length: 255 Unicode characters.

`annotations[].rawDetails` string

Raw detail text. Maximum 65,535 bytes of UTF-8.

`annotations[].location` object

Source location the annotation points at. Omit for a run-level annotation that is not tied to a line of code.

`annotations[].location.path` string Required

Canonical repository-relative file path. Maximum 4,096 bytes of UTF-8.

`annotations[].location.startLine` integer Required

First line of the range. 1-based and inclusive.

`annotations[].location.endLine` integer Required

Last line of the range. 1-based and inclusive, and at or after `startLine`.

`annotations[].location.columns` object

Column range within the line. Supported only when `startLine` and `endLine` are the same line, and both columns must be sent together.

`annotations[].location.columns.startColumn` integer

First column of the range. 1-based and inclusive.

`annotations[].location.columns.endColumn` integer

Last column of the range. 1-based and inclusive, and at or after `startColumn`.

#### [Response Fields](#response-fields-32)

`annotations` array

The annotations created by this request.

`annotations[].id` string

Stable Origin annotation ID. IDs are time-sortable.

`annotations[].checkRunId` string

ID of the check run the annotation belongs to.

`annotations[].annotationLevel` string

Severity of the annotation. Allowed values: `notice`, `warning`, `failure`.

`annotations[].message` string

Annotation message.

`annotations[].title` string

Annotation title. Absent when the annotation has none.

`annotations[].rawDetails` string

Raw detail text. Absent when the annotation has none.

`annotations[].createdAt` string

When the annotation was created (RFC 3339).

`annotations[].updatedAt` string

When the annotation was last updated (RFC 3339).

`annotations[].location` object

Source location. Absent for a run-level annotation.

`annotations[].location.path` string

Canonical repository-relative file path.

`annotations[].location.startLine` integer

First line of the range. 1-based and inclusive.

`annotations[].location.endLine` integer

Last line of the range. 1-based and inclusive.

`annotations[].location.columns` object

Column range. Absent unless the annotation covers a single line.

`annotations[].location.columns.startColumn` integer

First column of the range. 1-based and inclusive.

`annotations[].location.columns.endColumn` integer

Last column of the range. 1-based and inclusive.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs/CHECK_RUN_ID/annotations' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "annotations": [    {      "annotationLevel": "warning",      "message": "Deprecated API usage; migrate to the v2 client.",      "title": "Deprecated API",      "location": {        "path": "src/telemetry.ts",        "startLine": 42,        "endLine": 42      }    }  ]}'
```

**Response shape:**

```
{  "annotations": [    {      "id": "cra_01k2ja2000e0080000000000v1",      "checkRunId": "cr_01k2ja2000e0080000000000g7",      "annotationLevel": "warning",      "message": "Deprecated API usage; migrate to the v2 client.",      "title": "Deprecated API",      "createdAt": "2026-08-02T14:45:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "location": {        "path": "src/telemetry.ts",        "startLine": 42,        "endLine": 42      }    }  ]}
```

### [Rerequest Check Run](#rerequest-check-run)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/check-runs/{checkRunId}/rerequest`

Scope[repository:contents:write](#scopes)AuthInstallation tokenUser access token

Asks the app that reported a check run to run it again. Origin records the request on the run as `rerequestedAt` and notifies the owning app with [`repository.check_run.rerequested`](#events). The app answers by posting a fresh run for the same head SHA and `key`, either a new run or an update of this one, which clears `rerequestedAt`. The call never changes the run's own `status` or `conclusion`.

The run must be `completed`, must carry `isRerequestable`, must be the current attempt for its `key`, and must sit on the current head of an open pull request. Anything else returns `FailedPrecondition` (HTTP 400).

One re-request can be outstanding per run. A repeat request while `rerequestedAt` is set returns `AlreadyExists` (HTTP 409 Conflict), and the run becomes re-requestable again once the owning app has answered. Any principal holding [`repository:contents:write`](#scopes) can re-request any re-requestable run, whichever app reported it. A `checkRunId` that is unknown, or that belongs to another repository, returns `404`.

#### [Path Parameters](#path-parameters-26)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkRunId` string Required

Server-assigned check-run id (`cr_...`).

#### [Request Body](#request-body-14)

The request takes no fields. Send an empty JSON object.

#### [Response Fields](#response-fields-33)

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

`actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`actor.app` object

App variant of the actor. Set when an app performed the action.

`actor.app.id` string

Public identifier for the app.

`actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-runs/CHECK_RUN_ID/rerequest' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{}'
```

**Response shape:**

```
{  "id": "cr_01k2ja2000e0080000000000g7",  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "checkSuite": {    "id": "crg_01k2ja2000e0080000000000h8"  },  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "key": "ci-8842-unit-tests",  "name": "unit-tests",  "status": "completed",  "conclusion": "failure",  "detailsUrl": "https://ci.acme.dev/runs/8842",  "externalUpdatedAt": "2026-08-02T14:44:30Z",  "startedAt": "2026-08-02T14:40:00Z",  "completedAt": "2026-08-02T14:44:30Z",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T15:02:10Z",  "externalId": "run-8842",  "actor": {    "app": {      "id": "app_01k2ja2000e0080000000000a1",      "displayName": "Acme CI"    }  },  "output": {    "title": "Unit tests",    "summary": "3 of 128 tests failed."  },  "isRerequestable": true,  "rerequestedAt": "2026-08-02T15:02:10Z",  "rerequestedBy": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  }}
```

### [Get Check Suite](#get-check-suite)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-suites/{checkSuiteId}`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Returns check suite metadata by server-assigned id (`crg_...`). Does not embed check runs; use `ListCheckRunsForSuite` for the suite's runs.

#### [Path Parameters](#path-parameters-27)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkSuiteId` string Required

Server-assigned check suite id (`crg_...`).

#### [Response Fields](#response-fields-34)

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

`actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`actor.app` object

App variant of the actor. Set when an app performed the action.

`actor.app.id` string

Public identifier for the app.

`actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`actor.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`actor.serviceAccount.id` string

Public identifier for the service account.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-suites/CHECK_SUITE_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "crg_01k2ja2000e0080000000000h8",  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "key": "ci-8842",  "name": "CI",  "detailsUrl": "https://ci.acme.dev/runs/8842",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "externalId": "build-8842",  "actor": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  }}
```

### [List Check Runs For Suite](#list-check-runs-for-suite)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/check-suites/{checkSuiteId}/check-runs`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Lists a suite's current check runs. When a run key was reported more than once in the suite, only the latest attempt for that key is returned; superseded attempts are omitted. A run that has been re-requested stays in the listing and reads as pending, with `rerequestedAt` set and its superseded `status` and `conclusion` unchanged, until the app that owns it answers. Read a superseded attempt by its own id with [Get Check Run](#get-check-run). Paginated.

#### [Path Parameters](#path-parameters-28)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`checkSuiteId` string Required

Server-assigned check suite id (`crg_...`).

#### [Query Parameters](#query-parameters-7)

`pageSize` integer

Max check runs to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-run id scoped to this suite, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-35)

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

`checkRuns[].actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkRuns[].actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRuns[].deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`checkRuns[].isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`checkRuns[].rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`checkRuns[].rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/check-suites/CHECK_SUITE_ID/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "checkRuns": [    {      "id": "cr_01k2ja2000e0080000000000g7",      "repository": {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      },      "checkSuite": {        "id": "crg_01k2ja2000e0080000000000h8"      },      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "key": "ci-8842-unit-tests",      "name": "unit-tests",      "status": "completed",      "conclusion": "success",      "detailsUrl": "https://ci.acme.dev/runs/8842",      "externalUpdatedAt": "2026-08-02T14:44:30Z",      "startedAt": "2026-08-02T14:40:00Z",      "completedAt": "2026-08-02T14:44:30Z",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "externalId": "run-8842",      "actor": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "output": {        "title": "Unit tests",        "summary": "128 tests passed.",        "text": "All suites green."      }    }  ]}
```

### [List Check Runs For Commit](#list-check-runs-for-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/check-runs`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Lists a commit's current check runs across all suites: only runs belonging to each suite's latest attempt, and within each suite only the latest attempt per run key. Superseded attempts are omitted. A run that has been re-requested stays in the listing and reads as pending, with `rerequestedAt` set and its superseded `status` and `conclusion` unchanged, until the app that owns it answers. Read a superseded attempt by its own id with [Get Check Run](#get-check-run). Optionally filtered by check name and status. Paginated.

Filters apply to the collapsed set, so a run matches on its latest attempt's status and a filter never resurfaces a superseded attempt. Page tokens embed the filters they were minted under, so a token replayed under different filters is rejected; restart pagination when a filter changes.

#### [Path Parameters](#path-parameters-29)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Commit SHA (40- or 64-char hex) to list check runs for.

#### [Query Parameters](#query-parameters-8)

`pageSize` integer

Max check runs to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-run id scoped to this commit and to the filters below, so `page_size` on a follow-up request is ignored when a token is supplied, and reusing a token under different filters returns `InvalidArgument` (HTTP 400).

`checkName` string

Optional exact check-run name filter, matched against `checkRuns[].name`. Omit to list runs under any name.

`status` string

Optional status filter. Allowed values: `queued`, `in_progress`, `completed`. Any other value returns `InvalidArgument` (HTTP 400). Omit to list runs in any status.

#### [Response Fields](#response-fields-36)

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

`checkRuns[].actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkRuns[].actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkRuns[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkRuns[].actor.app.id` string

Public identifier for the app.

`checkRuns[].actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`checkRuns[].deadlineAt` string

Deadline recorded for the check run, as an RFC 3339 timestamp. Absent when the run has no deadline, including after the run completes.

`checkRuns[].isRerequestable` boolean

Whether the reporting app declared this run re-requestable.

`checkRuns[].rerequestedAt` string

RFC 3339 timestamp of the outstanding re-request. Absent when no re-request is pending, and cleared when the app that owns the run posts again. While it is set the run stays in the commit's latest check state and reads as pending, even though `status` and `conclusion` still carry the superseded result, so a required check blocks merging until the app answers.

`checkRuns[].rerequestedBy` object

Principal that asked for the re-run, carrying the same actor variants as `actor`. Present whenever `rerequestedAt` is set, and cleared together with it.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/commits/SHA/check-runs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "checkRuns": [    {      "id": "cr_01k2ja2000e0080000000000g7",      "repository": {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      },      "checkSuite": {        "id": "crg_01k2ja2000e0080000000000h8"      },      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "key": "ci-8842-unit-tests",      "name": "unit-tests",      "status": "completed",      "conclusion": "success",      "detailsUrl": "https://ci.acme.dev/runs/8842",      "externalUpdatedAt": "2026-08-02T14:44:30Z",      "startedAt": "2026-08-02T14:40:00Z",      "completedAt": "2026-08-02T14:44:30Z",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "externalId": "run-8842",      "actor": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "output": {        "title": "Unit tests",        "summary": "128 tests passed.",        "text": "All suites green."      }    }  ]}
```

### [List Check Suites For Commit](#list-check-suites-for-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/check-suites`

Scope[repository:checks:read](#scopes)AuthInstallation tokenUser access token

Lists check suites reported against a commit. Returns only the latest attempt of each suite, per reporting actor and suite key; superseded attempts are omitted. Read a superseded attempt by its own id with [Get Check Suite](#get-check-suite). Returns suite metadata only (no embedded runs). Paginated.

#### [Path Parameters](#path-parameters-30)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Commit SHA (40- or 64-char hex) to list suites for.

#### [Query Parameters](#query-parameters-9)

`pageSize` integer

Max suites to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the last-seen check-suite id scoped to this commit, so `page_size` on a follow-up request is ignored when a token is supplied.

#### [Response Fields](#response-fields-37)

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

`checkSuites[].actor.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`checkSuites[].actor.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`checkSuites[].actor.app` object

App variant of the actor. Set when an app performed the action.

`checkSuites[].actor.app.id` string

Public identifier for the app.

`checkSuites[].actor.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
{  "checkSuites": [    {      "id": "crg_01k2ja2000e0080000000000h8",      "repository": {        "id": "repo_01k2ja2000e0080000000000q4",        "name": "rocket",        "owner": {          "slug": "acme",          "id": "ns_01k2ja2000e0080000000000p3",          "type": "team"        }      },      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "key": "ci-8842",      "name": "CI",      "detailsUrl": "https://ci.acme.dev/runs/8842",      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "externalId": "build-8842",      "actor": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      }    }  ]}
```

## [Commits and contents](#commits-and-contents)

A commit separates git-object metadata under `commit` from top-level repository relationships. List responses omit `stats`; [Get Commit](#get-commit) includes whole-commit aggregate `stats`. Changed files are returned only by the paginated [List Commit Files](#list-commit-files) collection. `author` and `committer` are git identities recorded in the commit, not Origin user objects.

A comparison is a summary only: it never embeds commit lists or file diffs. `status` is exactly `identical`, `ahead`, `behind`, or `diverged`; `aheadBy` and `behindBy` are commit counts. `baseCommit`, `headCommit`, and `mergeBaseCommit` use the sparse commit projection (no `stats` or files).

### [List Commits](#list-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists commits on a branch or starting ref.

List results omit `stats`. Use [Get Commit](#get-commit) for aggregate stats and [List Commit Files](#list-commit-files) for the paginated file diff.

#### [Path Parameters](#path-parameters-31)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-10)

`sha` string

SHA, branch, tag, or symbolic ref (for example `HEAD`) to start listing from. Empty means the repo's default branch.

`pageSize` integer

Max commits to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. Encodes the starting ref and page, so `sha`/`page_size` on a follow-up request are ignored when a token is supplied.

#### [Response Fields](#response-fields-38)

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
{  "commits": [    {      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "commit": {        "author": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "committer": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "message": "Add launch telemetry",        "tree": {          "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"        }      },      "parents": [        {          "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"        }      ],      "stats": {        "additions": 128,        "deletions": 46,        "total": 174      }    }  ]}
```

### [Get Commit](#get-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns a single commit by SHA or ref with whole-commit aggregate `stats`. It does not include changed files; use [List Commit Files](#list-commit-files).

`author` and `committer` are git identities recorded in the commit, not Origin user objects.

#### [Path Parameters](#path-parameters-32)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

SHA, branch, tag, or symbolic ref (for example `HEAD`) of the commit to fetch.

#### [Response Fields](#response-fields-39)

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
{  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "commit": {    "author": {      "name": "Jane Doe",      "email": "jane@acme.dev",      "date": "2026-08-01T09:30:00Z"    },    "committer": {      "name": "Jane Doe",      "email": "jane@acme.dev",      "date": "2026-08-01T09:30:00Z"    },    "message": "Add launch telemetry",    "tree": {      "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"    }  },  "parents": [    {      "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"    }  ],  "stats": {    "additions": 128,    "deletions": 46,    "total": 174  }}
```

### [List Commit Files](#list-commit-files)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/commits/{sha}/files`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists the files changed by a commit.

`sha` may be a commit SHA, branch, tag, or symbolic ref such as `HEAD`. Results default to 30 files and are capped at 100. A page token fixes the resolved commit, page size, and file cursor; on later requests, `sha` and `pageSize` must match the token. Each file includes `filename`, `status`, `additions`, `deletions`, `changes`, `patch`, and `previousFilename` when renamed or copied. `patch` is empty for binary files.

#### [Path Parameters](#path-parameters-33)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

SHA, branch, tag, or symbolic ref (for example `HEAD`) of the commit whose files should be listed.

#### [Query Parameters](#query-parameters-11)

`pageSize` integer

Max changed files to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token fixes the resolved commit, page size, and file cursor, so `sha` and `page_size` on a follow-up request must match the token.

#### [Response Fields](#response-fields-40)

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
{  "files": [    {      "filename": "src/telemetry.ts",      "status": "modified",      "additions": 6,      "deletions": 3,      "changes": 9,      "patch": "@@ -12,6 +12,9 @@\n import { ignite } from \"./ignition\";\n+import { emitLaunchTelemetry } from \"./telemetry\";\n"    }  ]}
```

### [Compare Commits](#compare-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/compare/{basehead}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Compares commits, refs, or tags relative to their merge base. `basehead` is `"{base}...{head}"`; refs containing "/" must use their SHA.

`base` and `head` may each be a SHA, branch, tag, or symbolic ref such as `HEAD`. The response is an unpaginated summary: `status` is `identical`, `ahead`, `behind`, or `diverged`; the three commit objects are sparse and omit `stats` and files. No `totalCommits`, embedded `commits`, or `files` fields are returned. Unrelated histories return `404`.

#### [Path Parameters](#path-parameters-34)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`basehead` string Required

`"{base}...{head}"`, where either revision may be a SHA, branch, tag, or symbolic ref such as `HEAD`.

#### [Response Fields](#response-fields-41)

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
{  "status": "ahead",  "aheadBy": 2,  "behindBy": 0,  "baseCommit": {    "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "commit": {      "author": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "committer": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "message": "Add launch telemetry",      "tree": {        "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"      }    },    "parents": [      {        "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"      }    ],    "stats": {      "additions": 128,      "deletions": 46,      "total": 174    }  },  "headCommit": {    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "commit": {      "author": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "committer": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "message": "Add launch telemetry",      "tree": {        "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"      }    },    "parents": [      {        "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"      }    ],    "stats": {      "additions": 128,      "deletions": 46,      "total": 174    }  },  "mergeBaseCommit": {    "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "commit": {      "author": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "committer": {        "name": "Jane Doe",        "email": "jane@acme.dev",        "date": "2026-08-01T09:30:00Z"      },      "message": "Add launch telemetry",      "tree": {        "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"      }    },    "parents": [      {        "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"      }    ],    "stats": {      "additions": 128,      "deletions": 46,      "total": 174    }  }}
```

### [List Comparison Files](#list-comparison-files)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/compare/{basehead}/files`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists the files changed by a comparison: the diff of `head` against the merge base of `base` and `head`.

`basehead` is `"{base}...{head}"`; refs containing "/" must use their SHA. The file list always agrees with the summary from [Compare Commits](#compare-commits), so an `identical` or `behind` comparison returns an empty list, and unrelated histories return `404`. Results default to 30 files and are capped at 100. Each file carries the same fields as [List Commit Files](#list-commit-files).

#### [Path Parameters](#path-parameters-35)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`basehead` string Required

`"{base}...{head}"`, where either revision may be a SHA, branch, tag, or symbolic ref such as `HEAD`.

#### [Query Parameters](#query-parameters-12)

`pageSize` integer

Max changed files to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token is bound to the resolved comparison, page size, and file cursor, so `basehead` and `page_size` on a follow-up request must match the token. Origin re-resolves the comparison on every page; when its commits have moved since the token was issued, the request returns `InvalidArgument` (HTTP 400) and listing must restart from the first page.

#### [Response Fields](#response-fields-42)

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

Opaque cursor for the next page; empty when there are no more files.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/compare/BASE...HEAD/files' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "files": [    {      "filename": "src/telemetry.ts",      "status": "modified",      "additions": 6,      "deletions": 3,      "changes": 9,      "patch": "@@ -12,6 +12,9 @@\n import { ignite } from \"./ignition\";\n+import { emitLaunchTelemetry } from \"./telemetry\";\n"    }  ]}
```

### [Get Contents](#get-contents)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/contents`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns file or directory contents at a ref. The file path is passed as the `path` query parameter (supports nested paths); omit or leave empty for the repository root directory. Files larger than 1 MiB (decoded) are rejected with `FailedPrecondition` (HTTP 400).

Files contain base64 content. Directories contain immediate children in `entries`. Directory entries are sparse children containing `type`, `name`, `path`, `sha`, and `size`; fetch a child path to read its content.

#### [Path Parameters](#path-parameters-36)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-13)

`path` string

Path to the file or directory relative to the repository root. Empty requests the root directory.

`ref` string

Commit, branch, tag, or symbolic ref (for example `HEAD`) to read from. Empty means the repository's default branch.

#### [Response Fields](#response-fields-43)

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
{  "type": "file",  "encoding": "base64",  "size": "312",  "name": "telemetry.ts",  "path": "src/telemetry.ts",  "sha": "c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0",  "content": "Y29uc29sZS5sb2coImxhdW5jaCIpOwo="}
```

### [Batch Get Contents](#batch-get-contents)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/contents:batchGet`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns the contents of several explicit paths at a ref in one request. Each requested path yields a result marking whether it was found; a found path carries the same `Content` shape as `GetContents` (files as base64, directories as immediate `entries`, symlinks as files). Paths are matched exactly, with no globs or patterns, and at most 20 may be requested; duplicates are removed. Response results preserve first-seen request order. A single file larger than the [Get Contents](#get-contents) 1 MiB cap fails the whole batch with `FailedPrecondition` (HTTP 400). Uses POST because the path list travels in the request body.

#### [Path Parameters](#path-parameters-37)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-15)

`paths` array Required

Exact paths to fetch, relative to the repository root (no globs or patterns). At most 20 entries; duplicates are removed. An empty string requests the repository root directory.

`ref` string

Commit, branch, tag, or symbolic ref (for example `HEAD`) to read from. Empty means the repository's default branch.

#### [Response Fields](#response-fields-44)

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/contents:batchGet' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "paths": [    "src/telemetry.ts"  ],  "ref": "main"}'
```

**Response shape:**

```
{  "results": [    {      "path": "src/telemetry.ts",      "found": true,      "content": {        "type": "file",        "encoding": "base64",        "size": "312",        "name": "telemetry.ts",        "path": "src/telemetry.ts",        "sha": "c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0",        "content": "Y29uc29sZS5sb2coImxhdW5jaCIpOwo="      }    }  ],  "resolvedCommitSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"}
```

## [Git data](#git-data)

Low-level git objects. Reads need `repository:contents:read`, and an empty repository returns `409`. [Create Commit From Files](#create-commit-from-files) and [Create Git Ref](#create-git-ref) write git objects and need `repository:contents:write`.

### [Get Blob](#get-blob)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/blobs/{sha}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns a Git blob object by SHA. Default response is JSON with MIME-wrapped base64 `content`. Pass `Accept: application/vnd.origin.raw+json` (or `application/vnd.origin.raw`) on the REST surface to receive raw blob bytes instead. Blobs larger than 4 MiB (decoded) are rejected; fetch larger files by cloning the repository over [Git HTTPS](#git-https-authentication). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-38)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the blob object.

#### [Response Fields](#response-fields-45)

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
{  "sha": "c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0",  "size": 312,  "encoding": "base64",  "content": "Y29uc29sZS5sb2coImxhdW5jaCIpOwo="}
```

### [Get Git Commit](#get-git-commit)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/commits/{sha}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns a Git commit object by SHA (or resolvable revision). This is the low-level Git Database commit shape (flat author/message/tree), not the higher-level `GetCommit` resource under `/commits/{sha}`. `sha` accepts a commit SHA, branch, tag, or symbolic ref such as `HEAD`. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-39)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the commit object, or a branch, tag, or symbolic ref such as `HEAD`.

#### [Response Fields](#response-fields-46)

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
{  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "author": {    "name": "Jane Doe",    "email": "jane@acme.dev",    "date": "2026-08-01T09:30:00Z"  },  "committer": {    "name": "Jane Doe",    "email": "jane@acme.dev",    "date": "2026-08-01T09:30:00Z"  },  "message": "Add launch telemetry",  "tree": {    "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"  },  "parents": [    {      "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"    }  ]}
```

### [Create Commit From Files](#create-commit-from-files)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/git/commits:createFromFiles`

Scope[repository:contents:write](#scopes)AuthInstallation tokenUser access token

Creates a commit on a branch from inline file changes and advances the branch to it.

The changes apply to the tree at `expectedHeadSha`, which becomes the new commit's parent. A branch that has moved or does not exist, a set of changes that leaves the tree unchanged, a delete of a path the tree does not hold, a write a push ruleset blocks, and a repository whose contents are mirrored from another host each return `FailedPrecondition` (HTTP 400).

One request carries at most 1,000 file changes, 8 MiB per file, and 32 MiB of content in total. Exceeding a limit, repeating a path, or sending a malformed field returns `InvalidArgument` (HTTP 400), with `google.rpc.BadRequest` field violations naming the offending `files[i]` entry.

The branch must already exist. Create it with [Create Git Ref](#create-git-ref) first, then commit onto it.

#### [Path Parameters](#path-parameters-40)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-16)

`targetBranch` string Required

Branch that receives the commit, as `<branch>`, `heads/<branch>`, or `refs/heads/<branch>`. The branch must already exist. `HEAD` is rejected in every spelling.

`expectedHeadSha` string Required

Full hex SHA the target branch must currently point at. It becomes the new commit's parent. The all-zeros SHA is rejected.

`message` string Required

Commit message.

`author` object Required

Commit author. Timestamps are assigned by the server.

`author.name` string Required

Name recorded in the Git identity.

`author.email` string Required

Email recorded in the Git identity.

`committer` object

Commit committer. Defaults to `author` when omitted.

`committer.name` string

Name recorded in the Git identity. Required when `committer` is present.

`committer.email` string

Email recorded in the Git identity. Required when `committer` is present.

`files` array Required

File changes applied to the branch tip's tree. At least one change is required, and paths must be unique within a request.

`files[].path` string Required

Repository-relative path using `/` separators, for example `docs/changelog.md`.

`files[].content` string

New file contents, encoded per `files[].encoding`. Creates the file or replaces its contents. Set exactly one of `files[].content` and `files[].delete`.

`files[].delete` boolean

Removes the file. Must be `true` when set. Set exactly one of `files[].content` and `files[].delete`.

`files[].encoding` string

Encoding of `files[].content`. Allowed values: `utf-8` (default), `base64`. Ignored for a delete.

`files[].mode` string

File mode for `files[].content`. Allowed values: `file` (default), `executable`, `symlink`, where the contents are the link target. Ignored for a delete.

#### [Response Fields](#response-fields-47)

`sha` string

SHA of the new commit, now the branch tip.

`treeSha` string

SHA of the new commit's root tree.

`previousHeadSha` string

Branch tip before the write; the new commit's parent.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/commits:createFromFiles' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "targetBranch": "feature/login",  "expectedHeadSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "message": "Add login telemetry",  "author": {    "name": "Jane Doe",    "email": "jane@acme.dev"  },  "files": [    {      "path": "src/login/telemetry.ts",      "content": "export const LOGIN_EVENT = 1;"    },    {      "path": "assets/login.png",      "content": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==",      "encoding": "base64"    },    {      "path": "src/login/legacy.ts",      "delete": true    }  ]}'
```

**Response shape:**

```
{  "sha": "5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d",  "treeSha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8",  "previousHeadSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"}
```

### [Get Git Ref](#get-git-ref)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/ref/{ref}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns a single Git reference by name. `ref` is typically `heads/<branch>` or `tags/<tag>` (with or without a leading `refs/`), or the symbolic `HEAD`. Exact match only; use ListMatchingGitRefs for prefixes. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-41)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`ref` string Required

Git reference name. Typically `heads/<branch>` or `tags/<tag>`; a leading `refs/` is accepted and normalized. The symbolic `HEAD` is also accepted (returned as `ref: "HEAD"` with the tip commit). Exact match on the full ref name.

#### [Response Fields](#response-fields-48)

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
{  "ref": "refs/heads/main",  "object": {    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "type": "commit"  }}
```

### [Create Git Ref](#create-git-ref)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/git/refs`

Scope[repository:contents:write](#scopes)AuthInstallation tokenUser access token

Creates a branch reference pointing at an existing commit.

Only branch references can be created. A tag or any other reference namespace, and a `sha` that is not the full hex SHA of a commit in the repository, return `InvalidArgument` (HTTP 400). Creating a branch that already points at `sha` succeeds and returns the existing reference; a branch that exists at any other commit returns `AlreadyExists` (HTTP 409 Conflict). A create a push ruleset blocks, or one on a repository whose contents are mirrored from another host, returns `FailedPrecondition` (HTTP 400).

#### [Path Parameters](#path-parameters-42)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-17)

`ref` string Required

Branch reference to create, as `refs/heads/<branch>` or `heads/<branch>`.

`sha` string Required

Full hex SHA of an existing commit that the new branch points at.

#### [Response Fields](#response-fields-49)

`ref` string

Full ref name, e.g. "refs/heads/main".

`object` object

Object this ref points at directly (unpeeled). For a branch, `object.type` is "commit".

`object.sha` string

Hex SHA of the target object.

`object.type` string

One of "commit", "tree", "blob", or "tag".

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/git/refs' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "ref": "refs/heads/feature/login",  "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"}'
```

**Response shape:**

```
{  "ref": "refs/heads/feature/login",  "object": {    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "type": "commit"  }}
```

### [List Matching Git Refs](#list-matching-git-refs)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/matching-refs`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists Git references whose names start with the given prefix. REST responses unwrap to a JSON array (via `response_body`). A trailing slash on `ref` is preserved (`heads/` → `refs/heads/`). The symbolic `HEAD` is matched exactly (it is not under `refs/`). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-43)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-14)

`ref` string

Prefix to match. Typically `heads/<prefix>` or `tags/<prefix>`; a leading `refs/` is accepted and normalized. Empty lists all refs (REST binding without a trailing path segment).

#### [Response Fields](#response-fields-50)

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
{  "refs": [    {      "ref": "refs/heads/main",      "object": {        "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "type": "commit"      }    }  ]}
```

### [List Matching Git Refs by Path](#list-matching-git-refs-by-path)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/matching-refs/{ref}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Lists Git references whose names start with the given prefix. REST responses unwrap to a JSON array (via `response_body`). A trailing slash on `ref` is preserved (`heads/` → `refs/heads/`). The symbolic `HEAD` is matched exactly (it is not under `refs/`). Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-44)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`ref` string Required

Prefix to match. Typically `heads/<prefix>` or `tags/<prefix>`; a leading `refs/` is accepted and normalized. Empty lists all refs (REST binding without a trailing path segment).

#### [Response Fields](#response-fields-51)

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
{  "refs": [    {      "ref": "refs/heads/main",      "object": {        "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "type": "commit"      }    }  ]}
```

### [Get Tag](#get-tag)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/tags/{sha}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns an annotated Git tag object by SHA. Lightweight tags are not tag objects and return NotFound. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-45)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Full or abbreviated hex SHA of the annotated tag object.

#### [Response Fields](#response-fields-52)

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
{  "sha": "e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2",  "tag": "v1.2.0",  "message": "Release v1.2.0",  "tagger": {    "name": "Jane Doe",    "email": "jane@acme.dev",    "date": "2026-08-01T09:30:00Z"  },  "object": {    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "type": "commit"  }}
```

### [Get Tree](#get-tree)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/git/trees/{sha}`

Scope[repository:contents:read](#scopes)AuthInstallation tokenUser access token

Returns a Git tree object by SHA or resolvable revision. `sha` accepts a tree SHA, commit SHA, branch, tag, or symbolic ref such as `HEAD`. Set `recursive=true` (or `1`) to walk the whole tree; omitting the parameter or passing any other value lists immediate children only. Recursive listings truncate at 100,000 entries or 7 MiB and set `truncated=true`. Empty repositories return 409 Conflict.

#### [Path Parameters](#path-parameters-46)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`sha` string Required

Tree SHA, commit SHA, branch, tag, or symbolic ref such as `HEAD`.

#### [Query Parameters](#query-parameters-15)

`recursive` boolean

When true, returns the full recursive walk of the tree. Query values `true` and `1` enable recursion; omitting the parameter or passing any other value (including `false` and `0`) lists immediate children only.

#### [Response Fields](#response-fields-53)

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
{  "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8",  "tree": [    {      "path": "src/telemetry.ts",      "mode": "100644",      "type": "blob",      "sha": "c9d8e7f6a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0",      "size": 312    }  ],  "truncated": false}
```

## [Grants](#grants)

A grant binds one principal to one repository or one owner with one permission. These endpoints read, set, and remove the grants held directly on a resource, so access changes can be scripted and reviewed like code. Writes reuse the checks behind the Codebase permissions UI and record the same `repository.access_changed` and `namespace.access_changed` audit events. For the principal kinds, the two permission ladders, and how owner-level grants interact with repository-level ones, read [Origin Grants API](https://cursor.com/docs/api/origin/grants-api).

### [List Repository Grants](#list-repository-grants)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/grants`

Scope[repository:settings:read](#scopes)AuthInstallation tokenUser access token

Lists the users, groups, and owning-team groups holding a permission granted directly on a repository. Permissions inherited from the repository's owner are not included.

#### [Path Parameters](#path-parameters-47)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-16)

`pageSize` integer

Max grants to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100. Ignored when `pageToken` is set.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-54)

`grants` array

Grants held directly on the repository, ordered by principal kind (groups, owning-team admins, owning-team members, users) and then by id. A principal that no longer resolves to an active user, group, or owning team is omitted, so a page can hold fewer than `pageSize` grants.

`grants[].user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`grants[].user.id` string

Public identifier for the user, prefixed `user_`.

`grants[].user.email` string

Email address of the user.

`grants[].user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`grants[].user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`grants[].group` object

A Cursor organization group principal.

`grants[].group.id` string

Public identifier for the group, prefixed `grp_`.

`grants[].teamGroup` object

One of the owning team's built-in groups, granted on the repository itself and distinct from the one inherited from the owner.

`grants[].teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`grants[].permission` string

Permission the principal holds on the repository. Allowed values: `read`, `write`, `admin`, `custom`. `custom` reports a custom policy, which [Upsert Repository Grant](#upsert-repository-grant) does not accept.

`repository` object

The repository every grant in this response belongs to. Carries the same fields as [Get Repo](#get-repo).

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/{ownerSlug}/{repoName}/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "grants": [    {      "group": {        "id": "grp_01k2ja2000e0080000000000n2"      },      "permission": "admin"    },    {      "teamGroup": {        "kind": "admins"      },      "permission": "admin"    },    {      "teamGroup": {        "kind": "members"      },      "permission": "write"    },    {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      },      "permission": "read"    }  ],  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  },  "nextPageToken": ""}
```

### [Upsert Repository Grant](#upsert-repository-grant)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/grants`

Scope[repository:settings:write](#scopes)AuthInstallation tokenUser access token

Sets the permission a user, group, or owning-team group holds directly on a repository, replacing any permission granted directly to that principal before. Repeating a grant the principal already holds succeeds without change. A user must be an active member of the repository owner's team or organization, and a group an active group of that organization; otherwise the request returns `FailedPrecondition` (HTTP 400).

#### [Path Parameters](#path-parameters-48)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-18)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups, granted on the repository itself and distinct from the one inherited from the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`permission` string Required

Permission to grant. Allowed values: `read`, `write`, `admin`. `custom` returns `InvalidArgument` (HTTP 400); custom policies are outside this API.

#### [Response Fields](#response-fields-55)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups, granted on the repository itself and distinct from the one inherited from the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`permission` string

Permission the principal now holds on the repository.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "user": {    "id": "user_01k2ja2000e0080000000000c3"  },  "permission": "write"}'
```

**Response shape:**

```
{  "user": {    "id": "user_01k2ja2000e0080000000000c3",    "email": "jane@acme.dev"  },  "permission": "write"}
```

### [Delete Repository Grant](#delete-repository-grant)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/grants`

Scope[repository:settings:write](#scopes)AuthInstallation tokenUser access token

Removes the permission a user, group, or owning-team group holds directly on a repository. Permissions inherited from the repository's owner are unaffected, so an owning-team group falls back to its owner-level default. Removing a permission the principal does not hold directly succeeds without change. The response body is empty.

#### [Path Parameters](#path-parameters-49)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-19)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups, granted on the repository itself and distinct from the one inherited from the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

#### [Response Fields](#response-fields-56)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "group": {    "id": "grp_01k2ja2000e0080000000000n2"  }}'
```

**Response:**

```
204 No Content
```

### [List Namespace Grants](#list-namespace-grants)

GET`/v1/origin/owners/{ownerSlug}/grants`

Scope[namespace:settings:read](#scopes)AuthInstallation tokenUser access token

Lists who has been granted access to an owner: users, groups, and the owning team's built-in admin and member groups. Each grant carries the permission it confers on every repository under the owner. Grants made on individual repositories are not included; read those with [List Repository Grants](#list-repository-grants).

#### [Path Parameters](#path-parameters-50)

`ownerSlug` string Required

Slug of the owner whose grants to list.

#### [Query Parameters](#query-parameters-17)

`pageSize` integer

Max grants to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100. Ignored when `pageToken` is set.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page.

#### [Response Fields](#response-fields-57)

`grants` array

Grants on this page. Admin grants come first; within each run, grants are ordered by principal kind (groups, owning-team admins, owning-team members, users) and then by id. A principal that no longer resolves to an active user, group, or owning team is omitted, so a page can hold fewer than `pageSize` grants.

`grants[].user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`grants[].user.id` string

Public identifier for the user, prefixed `user_`.

`grants[].user.email` string

Email address of the user.

`grants[].user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`grants[].user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`grants[].group` object

A Cursor organization group principal.

`grants[].group.id` string

Public identifier for the group, prefixed `grp_`.

`grants[].teamGroup` object

One of the owning team's built-in groups: the team's default access to the owner.

`grants[].teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`grants[].permission` string

Permission the principal holds on every repository under the owner. Allowed values: `PERMISSION_READ`, `PERMISSION_CONTRIBUTOR`, `PERMISSION_WRITE`, `PERMISSION_ADMIN`, `PERMISSION_CUSTOM`. `PERMISSION_CUSTOM` reports a custom policy, which [Upsert Namespace Grant](#upsert-namespace-grant) does not accept.

`nextPageToken` string

Opaque cursor for the next page; empty when there are no more pages.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/owners/{ownerSlug}/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "grants": [    {      "group": {        "id": "grp_01k2ja2000e0080000000000n2"      },      "permission": "PERMISSION_ADMIN"    },    {      "teamGroup": {        "kind": "admins"      },      "permission": "PERMISSION_ADMIN"    },    {      "teamGroup": {        "kind": "members"      },      "permission": "PERMISSION_CONTRIBUTOR"    },    {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      },      "permission": "PERMISSION_WRITE"    }  ],  "nextPageToken": ""}
```

### [Upsert Namespace Grant](#upsert-namespace-grant)

POST`/v1/origin/owners/{ownerSlug}/grants`

Scope[namespace:settings:write](#scopes)AuthInstallation tokenUser access token

Sets the permission a user, group, or owning-team group holds directly on an owner, replacing any permission granted directly to that principal before. Repeating a grant the principal already holds succeeds without change. The request returns `FailedPrecondition` (HTTP 400) when the user is not an active member of the owning team or its organization, when the group is not an active group of that organization, or when the write would leave the owner without an admin.

#### [Path Parameters](#path-parameters-51)

`ownerSlug` string Required

Owner slug.

#### [Request Body](#request-body-20)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups: the team's default access to the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`permission` string Required

Permission to grant. Allowed values: `PERMISSION_READ`, `PERMISSION_CONTRIBUTOR`, `PERMISSION_WRITE`, `PERMISSION_ADMIN`. `PERMISSION_READ`, `PERMISSION_CONTRIBUTOR`, and `PERMISSION_WRITE` confer that level on the owner's internal repositories, and `PERMISSION_ADMIN` administers the owner itself. `PERMISSION_CUSTOM` returns `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-58)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups: the team's default access to the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

`permission` string

Permission the principal now holds on every repository under the owner.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/owners/OWNER_SLUG/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "user": {    "id": "user_01k2ja2000e0080000000000c3"  },  "permission": "PERMISSION_WRITE"}'
```

**Response shape:**

```
{  "user": {    "id": "user_01k2ja2000e0080000000000c3",    "email": "jane@acme.dev"  },  "permission": "PERMISSION_WRITE"}
```

### [Delete Namespace Grant](#delete-namespace-grant)

DELETE`/v1/origin/owners/{ownerSlug}/grants`

Scope[namespace:settings:write](#scopes)AuthInstallation tokenUser access token

Removes the permission a user, group, or owning-team group holds directly on an owner. Per-repository grants are unaffected. Removing a permission the principal does not hold directly succeeds without change, and a removal that would leave the owner without an admin returns `FailedPrecondition` (HTTP 400). The response body is empty.

#### [Path Parameters](#path-parameters-52)

`ownerSlug` string Required

Owner slug.

#### [Request Body](#request-body-21)

`user` object

A user principal. Exactly one of `user`, `group`, or `teamGroup` is present.

`user.id` string

Public identifier for the user, prefixed `user_`.

`user.email` string

Email address of the user.

`user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`group` object

A Cursor organization group principal.

`group.id` string

Public identifier for the group, prefixed `grp_`.

`teamGroup` object

One of the owning team's built-in groups: the team's default access to the owner.

`teamGroup.kind` string

Which built-in group holds the grant. Allowed values: `members`, `admins`.

#### [Response Fields](#response-fields-59)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/owners/OWNER_SLUG/grants' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "group": {    "id": "grp_01k2ja2000e0080000000000n2"  }}'
```

**Response:**

```
204 No Content
```

## [Labels](#labels)

A label definition belongs to one repository and is addressed by its name. Assigning labels to a pull request is a separate surface; see [Set Pull Request Labels](#set-pull-request-labels).

### [List Labels](#list-labels)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/labels`

Scope[repository:labels:read](#scopes)AuthInstallation tokenUser access token

Lists the labels defined on a repository, ordered by name.

Page tokens are bound to the repository they were minted for. A token replayed against a different repository, or any other malformed token, returns `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-53)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-18)

`pageSize` integer

Maximum labels to return. Defaults to 30 when omitted or zero; values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `nextPageToken`. Omit for the first page.

#### [Response Fields](#response-fields-60)

`labels` array

Page of label definitions, ordered by name.

`labels[].id` string

Public identifier for the label.

`labels[].name` string

Label name, unique within the repository. Names address the label in the read and write endpoints.

`labels[].color` string

Six-character hex color without a leading `#`.

`labels[].description` string

Label description. Absent when the label has none.

`nextPageToken` string

Opaque cursor for the next page. Empty when there are no more results.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ]}
```

### [Create Label](#create-label)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/labels`

Scope[repository:labels:write](#scopes)AuthInstallation tokenUser access token

Creates a label on a repository.

A name already used by another label on the repository returns `AlreadyExists` (HTTP 409 Conflict). A `color` that is not six hexadecimal characters, a `name` longer than 50 characters, or a `description` longer than 255 characters returns `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-54)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-22)

`name` string Required

Label name. Leading and trailing whitespace is trimmed. Maximum length: 50 characters.

`color` string Required

Six-character hex color without a leading `#`. Uppercase input is stored lowercase.

`description` string

Label description. Maximum length: 255 characters.

#### [Response Fields](#response-fields-61)

`id` string

Public identifier for the label.

`name` string

Label name, unique within the repository. Names address the label in the read and write endpoints.

`color` string

Six-character hex color without a leading `#`.

`description` string

Label description. Absent when the label has none.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "bug",  "color": "d73a4a",  "description": "Something isn'\''t working"}'
```

**Response shape:**

```
{  "id": "lbl_01k2ja2000e0080000000000m1",  "name": "bug",  "color": "d73a4a",  "description": "Something isn't working"}
```

### [Get Label](#get-label)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/labels/{labelName}`

Scope[repository:labels:read](#scopes)AuthInstallation tokenUser access token

Returns a single repository label by name.

An unknown name returns `404`. An empty `labelName` returns `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-55)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`labelName` string Required

Label name. Leading and trailing whitespace is trimmed before lookup.

#### [Response Fields](#response-fields-62)

`id` string

Public identifier for the label.

`name` string

Label name, unique within the repository. Names address the label in the read and write endpoints.

`color` string

Six-character hex color without a leading `#`.

`description` string

Label description. Absent when the label has none.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/labels/LABEL_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "id": "lbl_01k2ja2000e0080000000000m1",  "name": "bug",  "color": "d73a4a",  "description": "Something isn't working"}
```

### [Delete Label](#delete-label)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/labels/{labelName}`

Scope[repository:labels:write](#scopes)AuthInstallation tokenUser access token

Deletes a repository label by name. The response body is empty.

Deleting a label also removes it from every pull request it was assigned to. An unknown name returns `404`. An empty `labelName` returns `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-56)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`labelName` string Required

Label name. Leading and trailing whitespace is trimmed before lookup.

#### [Response Fields](#response-fields-63)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/labels/LABEL_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

### [Update Label](#update-label)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/labels/{labelName}`

Scope[repository:labels:write](#scopes)AuthInstallation tokenUser access token

Updates a repository label identified by its current name.

Omitted fields are left unchanged, and a request that omits all three returns the label as it stands. Renaming to a name another label already uses returns `AlreadyExists` (HTTP 409 Conflict). An unknown `labelName` returns `404`.

#### [Path Parameters](#path-parameters-57)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`labelName` string Required

Current label name. Leading and trailing whitespace is trimmed before lookup.

#### [Request Body](#request-body-23)

`name` string

New label name. Leading and trailing whitespace is trimmed. Maximum length: 50 characters. Omit to leave unchanged.

`color` string

Six-character hex color without a leading `#`. Omit to leave unchanged.

`description` string

Label description. Maximum length: 255 characters. Omit to leave unchanged.

#### [Response Fields](#response-fields-64)

`id` string

Public identifier for the label.

`name` string

Label name, unique within the repository. Names address the label in the read and write endpoints.

`color` string

Six-character hex color without a leading `#`.

`description` string

Label description. Absent when the label has none.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/labels/LABEL_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "color": "b60205"}'
```

**Response shape:**

```
{  "id": "lbl_01k2ja2000e0080000000000m1",  "name": "bug",  "color": "b60205",  "description": "Something isn't working"}
```

## [Pull requests](#pull-requests)

Closed or merged pull requests may additionally include `closedAt`, `mergedAt`, and `mergeCommitSha`. Treat `head.ref` and `base.ref` as opaque Origin ref strings; they may be short branch names or fully qualified `refs/heads/…` values.

Review `verdict` is `approve`, `request_changes`, or `comment`. `submittedAt` is absent for an unsubmitted draft review. `dismissal` is absent while the verdict remains active. Dismissed reviews remain visible in review listings. Reviews automatically superseded by a newer decision carry a server-generated message.

Comments expose a `thread` reference for grouping. Create-comment requests still accept the scalar `threadId` command parameter when replying. Resolve or reopen a thread with [Update Pull Request Thread](#update-pull-request-thread).

### [List Pull Requests](#list-pull-requests)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls`

Scope[repository:pull\_requests:read](#scopes)AuthInstallation tokenUser access token

Lists pull requests in a repo, optionally filtered by head branch, base branch, author, creation-time range, and state. Each pull request includes its assigned labels.

Results come back in creation order, newest first. Set `direction=asc` for oldest first. Page tokens embed the filters they were minted under, so a token replayed with different filters is rejected; restart pagination when a filter changes.

#### [Path Parameters](#path-parameters-58)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Query Parameters](#query-parameters-19)

`head` string

Optional exact branch (head-ref) filter. Omit to list across every branch.

`state` string

"open" | "closed" | "all". Defaults to "open".

`pageSize` integer

Maximum results to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque cursor from a previous response's `nextPageToken`. Omit it for the first page.

`author` string

Optional author filter. Pass a public actor ID exactly as this endpoint returns it in `pullRequests[].author.user.id`, `pullRequests[].author.app.id`, or `pullRequests[].author.serviceAccount.id` (`user_…`, `app_…`, or `sa_…`), or the exact email address of a user. Email matching is case-insensitive. Apps and service accounts have no email identity, so only user authors can be selected that way. An author with no pull requests returns an empty list, as does an email that resolves to no single user. Any other value, including the shared `origin-cursor-managed-actor` ID, returns `InvalidArgument` (HTTP 400).

`base` string

Optional exact base-branch filter. Accepts a short name (`main`) or a fully qualified ref (`refs/heads/main`). Omit to list across every base.

`direction` string

Sort direction by creation order. `"desc"` returns newest first and is the default; `"asc"` returns oldest first. Any other value returns `InvalidArgument` (HTTP 400).

`since` string

Optional inclusive lower bound on creation time, as an RFC 3339 timestamp such as `2026-08-01T00:00:00Z`. Returns only pull requests created at or after that instant. A malformed timestamp returns `InvalidArgument` (HTTP 400).

`until` string

Optional inclusive upper bound on creation time, in the same RFC 3339 format as `since`. Returns only pull requests created at or before that instant. A malformed timestamp returns `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-65)

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

`pullRequests[].author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`pullRequests[].author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`pullRequests[].author.app` object

App variant of the actor. Set when an app performed the action.

`pullRequests[].author.app.id` string

Public identifier for the app.

`pullRequests[].author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
{  "pullRequests": [    {      "id": "pr_01k2ja2000e0080000000000d4",      "number": "17",      "state": "open",      "draft": false,      "merged": false,      "title": "Add launch telemetry",      "body": "Adds structured launch telemetry to the ignition path.",      "head": {        "ref": "add-telemetry",        "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"      },      "base": {        "ref": "main",        "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"      },      "author": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z",      "additions": 128,      "deletions": 46,      "changedFiles": 5,      "labels": [        {          "id": "lbl_01k2ja2000e0080000000000m1",          "name": "bug",          "color": "d73a4a",          "description": "Something isn't working"        }      ],      "version": {        "number": "3",        "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",        "createdAt": "2026-08-01T09:30:00Z"      }    }  ]}
```

### [Get Pull Request](#get-pull-request)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}`

Scope[repository:pull\_requests:read](#scopes)AuthInstallation tokenUser access token

Returns a single pull request, including its assigned labels.

Closed or merged pull requests may additionally include `closedAt`, `mergedAt`, and `mergeCommitSha`. Treat `head.ref` and `base.ref` as opaque Origin ref strings; they may be short branch names or fully qualified `refs/heads/…` values.

#### [Path Parameters](#path-parameters-59)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-66)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
{  "id": "pr_01k2ja2000e0080000000000d4",  "number": "17",  "state": "open",  "draft": false,  "merged": false,  "title": "Add launch telemetry",  "body": "Adds structured launch telemetry to the ignition path.",  "head": {    "ref": "add-telemetry",    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"  },  "base": {    "ref": "main",    "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"  },  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "additions": 128,  "deletions": 46,  "changedFiles": 5,  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ],  "version": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  }}
```

### [Create Pull Request](#create-pull-request)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls`

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Creates a pull request from `head` into `base`.

Optional `parent_pull_number` stacks this change on another open or draft pull request in the same repository.

A `title` longer than 256 characters, or a `body` longer than 65,536 characters, returns `InvalidArgument` (HTTP 400). Both limits count Unicode code points.

A `head` with no history in common with `base` returns `InvalidArgument` (HTTP 400) and creates nothing. If a later push leaves an open pull request's head disjoint from its base, Origin closes the pull request and delivers [`pull_request.closed`](#events); a subsequent related push does not reopen it.

#### [Path Parameters](#path-parameters-60)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-24)

`title` string Required

Pull request title. Maximum length: 256 characters.

`body` string

Pull request body / description. Can be empty. Maximum length: 65,536 characters.

`head` string Required

Source branch name (the head of the change). Must resolve in the repo at call time.

`base` string Required

Target branch name (what the change merges into). Must name a branch that exists in the repo at call time. A commit SHA, a tag name, or a branch that does not exist returns `InvalidArgument` (HTTP 400).

`draft` boolean

When true, create as a draft. When false or omitted, create as open (ready for review).

`parentPullNumber` string

Optional parent pull request number when stacking this change on another open/draft change in the same repository.

#### [Response Fields](#response-fields-67)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "title": "Add launch telemetry",  "body": "Adds structured launch telemetry to the ignition path.",  "head": "add-telemetry",  "base": "main",  "draft": false}'
```

**Response shape:**

```
{  "id": "pr_01k2ja2000e0080000000000d4",  "number": "17",  "state": "open",  "draft": false,  "merged": false,  "title": "Add launch telemetry",  "body": "Adds structured launch telemetry to the ignition path.",  "head": {    "ref": "add-telemetry",    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"  },  "base": {    "ref": "main",    "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"  },  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "additions": 128,  "deletions": 46,  "changedFiles": 5,  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ],  "version": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  }}
```

### [Update Pull Request](#update-pull-request)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}`

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Updates a pull request's title, body, base branch, and/or lifecycle state.

Omitted fields are unchanged. Present fields are applied in order: metadata, then reopen/draft/ready-for-review, then base, then close. Close runs last so a same-request retarget can still see an open change; reopen runs before base so a closed pull can be retargeted. If a later step fails, earlier steps may already have been committed.

A `title` longer than 256 characters, or a `body` longer than 65,536 characters, returns `InvalidArgument` (HTTP 400). Both limits count Unicode code points.

#### [Path Parameters](#path-parameters-61)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-25)

`title` string

New title. Omitted fields are left unchanged. Maximum length: 256 characters.

`body` string

New body / description. An empty string clears the body. Maximum length: 65,536 characters.

`state` string

`"open"` or `"closed"`. `"closed"` closes the pull request. `"open"` without `draft: true` marks it ready for review, including publishing an existing draft. Merged is not writable. use `MergePullRequest`.

`draft` boolean

`true` marks the pull request draft; `false` marks it ready for review (and reopens it if currently closed). Ignored when `state` is `"closed"`.

`base` string

New base branch. Retargets the pull request and can update stack parentage when the new base is another change's head (or the default branch). Must name a branch that exists in the repo at call time; a commit SHA, a tag name, or a branch that does not exist returns `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-68)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "title": "Add launch telemetry",  "body": "Adds structured launch telemetry to the ignition path.",  "state": "open",  "draft": false,  "base": "main"}'
```

**Response shape:**

```
{  "id": "pr_01k2ja2000e0080000000000d4",  "number": "17",  "state": "open",  "draft": false,  "merged": false,  "title": "Add launch telemetry",  "body": "Adds structured launch telemetry to the ignition path.",  "head": {    "ref": "add-telemetry",    "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"  },  "base": {    "ref": "main",    "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"  },  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z",  "additions": 128,  "deletions": 46,  "changedFiles": 5,  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ],  "version": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  }}
```

### [List Pull Request Comments](#list-pull-request-comments)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/comments`

Scope[repository:pull\_requests:reviews:read](#scopes)AuthInstallation tokenUser access token

Lists every comment on a pull request in chronological order, optionally bounded to a creation-time window. Each comment carries its full thread: id, diff anchor, and resolution state. Group the flat response by `thread.id` without a second request.

Page tokens embed the filters they were minted under, so a token replayed with different filters is rejected; restart pagination when a filter changes.

#### [Path Parameters](#path-parameters-62)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-20)

`pageSize` integer

Maximum comments to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque cursor from a previous response's `nextPageToken`. Omit it for the first page.

`since` string

Optional inclusive lower bound on comment creation time, as an RFC 3339 timestamp such as `2026-08-01T00:00:00Z`. Returns only comments created at or after that instant. A malformed timestamp returns `InvalidArgument` (HTTP 400).

`until` string

Optional inclusive upper bound on comment creation time, in the same RFC 3339 format as `since`. Returns only comments created at or before that instant. A malformed timestamp returns `InvalidArgument` (HTTP 400).

`threadIds` array

Optional thread IDs that restrict the listing to comments in those threads. Omit to return every comment on the pull request. Duplicates are ignored, so the limit of 20 applies to distinct IDs. A longer list, or an empty ID, returns `InvalidArgument` (HTTP 400).

#### [Response Fields](#response-fields-69)

`comments` array

Visible general and inline comments as one flat chronological list; group them by thread.id.

`comments[].id` string

Stable pull request comment identifier.

`comments[].thread` object

The thread this comment belongs to, including its diff anchor and resolution state.

`comments[].thread.id` string

Stable identity of the thread. Group comments in one discussion by this value.

`comments[].thread.version` object

Pull request version the thread was filed against, including its head and base SHAs. The anchor is fixed to this version and does not move as the pull request gains versions.

`comments[].thread.version.number` string

Monotonic pull request version number encoded as a JSON string.

`comments[].thread.version.headSha` string

Head SHA captured by this pull request version.

`comments[].thread.version.baseSha` string

Base SHA captured by this pull request version.

`comments[].thread.version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`comments[].thread.path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`comments[].thread.side` string

Diff side of the anchor. Allowed values: `left`, `right`. Unset for general-discussion threads.

`comments[].thread.startLine` integer

First line of the anchored range in the `side` version of the file. `0` for file-level and general-discussion threads.

`comments[].thread.endLine` integer

Inclusive last line of the anchored range. `0` when the anchor is a single line or has no line range.

`comments[].thread.resolvedAt` string

RFC 3339 timestamp for when the thread was resolved. Unset while the thread is open.

`comments[].thread.createdAt` string

RFC 3339 thread creation timestamp.

`comments[].thread.updatedAt` string

RFC 3339 timestamp for the latest thread update.

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

`comments[].author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`comments[].author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`comments[].author.app` object

App variant of the actor. Set when an app performed the action.

`comments[].author.app.id` string

Public identifier for the app.

`comments[].author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

Opaque cursor for the next page; empty when there are no more comments.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/comments' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "comments": [    {      "id": "cmt_01k2ja2000e0080000000000e5",      "thread": {        "id": "cth_01k2ja2000e0080000000000s6",        "version": {          "number": "3",          "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",          "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",          "createdAt": "2026-08-01T09:30:00Z"        },        "path": "src/telemetry/retry.ts",        "side": "right",        "startLine": 42,        "endLine": 45,        "createdAt": "2026-08-01T09:30:00Z",        "updatedAt": "2026-08-02T14:45:00Z"      },      "body": "Should the retry budget be configurable?",      "author": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "createdAt": "2026-08-01T09:30:00Z",      "updatedAt": "2026-08-02T14:45:00Z"    }  ],  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    }  }}
```

### [Get Pull Request Comment](#get-pull-request-comment)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/comments/{commentId}`

Scope[repository:pull\_requests:reviews:read](#scopes)AuthInstallation tokenUser access token

Returns a single pull request comment by its stable Origin id. A comment outside the authorized repository, or a pending-review comment not visible to the caller, returns `404`.

#### [Path Parameters](#path-parameters-63)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`commentId` string Required

#### [Response Fields](#response-fields-70)

`id` string

Stable pull request comment identifier.

`thread` object

The thread this comment belongs to, including its diff anchor and resolution state.

`thread.id` string

Stable identity of the thread. Group comments in one discussion by this value.

`thread.version` object

Pull request version the thread was filed against, including its head and base SHAs. The anchor is fixed to this version and does not move as the pull request gains versions.

`thread.version.number` string

Monotonic pull request version number encoded as a JSON string.

`thread.version.headSha` string

Head SHA captured by this pull request version.

`thread.version.baseSha` string

Base SHA captured by this pull request version.

`thread.version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`thread.path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`thread.side` string

Diff side of the anchor. Allowed values: `left`, `right`. Unset for general-discussion threads.

`thread.startLine` integer

First line of the anchored range in the `side` version of the file. `0` for file-level and general-discussion threads.

`thread.endLine` integer

Inclusive last line of the anchored range. `0` when the anchor is a single line or has no line range.

`thread.resolvedAt` string

RFC 3339 timestamp for when the thread was resolved. Unset while the thread is open.

`thread.createdAt` string

RFC 3339 thread creation timestamp.

`thread.updatedAt` string

RFC 3339 timestamp for the latest thread update.

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
{  "id": "cmt_01k2ja2000e0080000000000e5",  "thread": {    "id": "cth_01k2ja2000e0080000000000s6",    "version": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    },    "path": "src/telemetry/retry.ts",    "side": "right",    "startLine": 42,    "endLine": 45,    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z"  },  "body": "Should the retry budget be configurable?",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z"}
```

### [Create Pull Request Comment](#create-pull-request-comment)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/comments`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Creates a comment on an Origin pull request. The comment targets exactly one of four things: `threadId` replies to an existing thread, general-discussion and inline alike; `inline` opens a new thread anchored to a line range in the pull request version's diff; `file` opens a new thread on a whole file in that diff; supplying none of them opens a new general-discussion thread. Bodies longer than 65,536 characters are rejected with `InvalidArgument` (HTTP 400).

An `inline` anchor must reference the version's diff. The `path` must be part of that diff, and the `side` must have content there, so anchoring `left` on an added file or `right` on a deleted file is rejected with `InvalidArgument` (HTTP 400). Any line of a changed file anchors, and the range is not restricted to the diff's hunks. The range must fit the file on the anchored side, which `left` reads at the base commit and `right` at the head: a range running past the last line is rejected with `InvalidArgument` (HTTP 400). Origin never falls back to a general-discussion comment when an anchor is invalid.

A `file` anchor carries the path alone. Origin derives the side from the file's change kind, the base version for a deleted file and the head version otherwise, and returns it on `thread.side`. Send the deleted path for a deletion and the head path for every other change. A path outside the diff is rejected with `InvalidArgument` (HTTP 400), as is a renamed file's pre-rename source path.

#### [Path Parameters](#path-parameters-64)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-26)

`body` string Required

Comment text. Maximum length: 65,536 characters, counted as Unicode code points.

`threadId` string

Existing thread id to reply to. Omit to open a new thread. Cannot be combined with `versionNumber`.

`inline` object

Diff anchor for a new inline thread. Cannot be combined with `threadId`.

`inline.path` string Required

File path in the pull request version's diff.

`inline.side` string Required

Diff side of the anchor. Allowed values: `left` for the base version of the file, `right` for the head version.

`inline.startLine` integer Required

First 1-based line of the anchored range in the `side` version of the file. The range must not run past the end of that file.

`inline.endLine` integer

Inclusive last line of the anchored range. Must be greater than or equal to `startLine`. Omit for a single-line anchor.

`file` object

Anchor for a new file-level thread on a whole file in the pull request version's diff. Cannot be combined with `threadId` or `inline`.

`file.path` string Required

File path in the pull request version's diff: the deleted path for a deletion, the head path otherwise.

`versionNumber` string

Pull request version number to file a new thread against. `0` or unset means the latest version at call time. Only meaningful for new threads.

#### [Response Fields](#response-fields-71)

`id` string

Stable pull request comment identifier.

`thread` object

The thread this comment belongs to. A reply carries the thread id only, and a new general-discussion thread carries the id and timestamps; a new inline thread carries the full anchor. Read [Get Pull Request Comment](#get-pull-request-comment) or [List Pull Request Comments](#list-pull-request-comments) for complete thread state.

`thread.id` string

Stable identity of the thread. Group comments in one discussion by this value.

`thread.version` object

Pull request version the thread was filed against, including its head and base SHAs. The anchor is fixed to this version and does not move as the pull request gains versions.

`thread.version.number` string

Monotonic pull request version number encoded as a JSON string.

`thread.version.headSha` string

Head SHA captured by this pull request version.

`thread.version.baseSha` string

Base SHA captured by this pull request version.

`thread.version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`thread.path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`thread.side` string

Diff side of the anchor. Allowed values: `left`, `right`. Unset for general-discussion threads.

`thread.startLine` integer

First line of the anchored range in the `side` version of the file. `0` for file-level and general-discussion threads.

`thread.endLine` integer

Inclusive last line of the anchored range. `0` when the anchor is a single line or has no line range.

`thread.resolvedAt` string

RFC 3339 timestamp for when the thread was resolved. Unset while the thread is open.

`thread.createdAt` string

RFC 3339 thread creation timestamp.

`thread.updatedAt` string

RFC 3339 timestamp for the latest thread update.

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 comment creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest comment edit.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/comments' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "Should the retry budget be configurable?"}'
```

**Response shape:**

```
{  "id": "cmt_01k2ja2000e0080000000000e5",  "thread": {    "id": "cth_01k2ja2000e0080000000000s6",    "version": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    },    "path": "src/telemetry/retry.ts",    "side": "right",    "startLine": 42,    "endLine": 45,    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z"  },  "body": "Should the retry budget be configurable?",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z"}
```

### [Update Pull Request Comment](#update-pull-request-comment)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/comments/{commentId}`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Updates a pull request comment by its stable Origin id.

Replaces the comment body. The comment must belong to the repository in the path, be visible to the caller, and have been authored by that caller. Cross-repository and hidden pending-review comments return `404`; a visible comment owned by another actor returns `403`. Bodies longer than 65,536 characters are rejected with `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-65)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`commentId` string Required

#### [Request Body](#request-body-27)

`body` string Required

Replacement comment text. Maximum length: 65,536 characters, counted as Unicode code points.

#### [Response Fields](#response-fields-72)

`id` string

Stable pull request comment identifier.

`thread` object

The thread this comment belongs to, including its diff anchor and resolution state.

`thread.id` string

Stable identity of the thread. Group comments in one discussion by this value.

`thread.version` object

Pull request version the thread was filed against, including its head and base SHAs. The anchor is fixed to this version and does not move as the pull request gains versions.

`thread.version.number` string

Monotonic pull request version number encoded as a JSON string.

`thread.version.headSha` string

Head SHA captured by this pull request version.

`thread.version.baseSha` string

Base SHA captured by this pull request version.

`thread.version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`thread.path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`thread.side` string

Diff side of the anchor. Allowed values: `left`, `right`. Unset for general-discussion threads.

`thread.startLine` integer

First line of the anchored range in the `side` version of the file. `0` for file-level and general-discussion threads.

`thread.endLine` integer

Inclusive last line of the anchored range. `0` when the anchor is a single line or has no line range.

`thread.resolvedAt` string

RFC 3339 timestamp for when the thread was resolved. Unset while the thread is open.

`thread.createdAt` string

RFC 3339 thread creation timestamp.

`thread.updatedAt` string

RFC 3339 timestamp for the latest thread update.

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`author.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`author.serviceAccount.id` string

Public identifier for the service account.

`createdAt` string

RFC 3339 comment creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest comment edit.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/comments/COMMENT_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "Should the retry budget be configurable?"}'
```

**Response shape:**

```
{  "id": "cmt_01k2ja2000e0080000000000e5",  "thread": {    "id": "cth_01k2ja2000e0080000000000s6",    "version": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    },    "path": "src/telemetry/retry.ts",    "side": "right",    "startLine": 42,    "endLine": 45,    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z"  },  "body": "Should the retry budget be configurable?",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-02T14:45:00Z"}
```

### [Update Pull Request Thread](#update-pull-request-thread)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/threads/{threadId}`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Resolves or reopens a pull request comment thread and returns the thread's updated state. Resolving an already-resolved thread, or reopening an already-open one, is a no-op.

The thread must belong to the repository in the path; a thread stored on another repository returns `404`. Replying to a resolved thread with [Create Pull Request Comment](#create-pull-request-comment) is allowed and does not reopen it.

#### [Path Parameters](#path-parameters-66)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`threadId` string Required

Stable Origin thread ID.

#### [Request Body](#request-body-28)

`resolved` boolean Required

Target resolution state. `true` resolves the thread; `false` reopens it.

#### [Response Fields](#response-fields-73)

`id` string

Stable identity of the thread. Group comments in one discussion by this value.

`version` object

Pull request version the thread was filed against, including its head and base SHAs. The anchor is fixed to this version and does not move as the pull request gains versions.

`version.number` string

Monotonic pull request version number encoded as a JSON string.

`version.headSha` string

Head SHA captured by this pull request version.

`version.baseSha` string

Base SHA captured by this pull request version.

`version.createdAt` string

RFC 3339 timestamp for creation of this pull request version.

`path` string

File path of the thread's diff anchor. Empty for general-discussion threads.

`side` string

Diff side of the anchor. Allowed values: `left`, `right`. Unset for general-discussion threads.

`startLine` integer

First line of the anchored range in the `side` version of the file. `0` for file-level and general-discussion threads.

`endLine` integer

Inclusive last line of the anchored range. `0` when the anchor is a single line or has no line range.

`resolvedAt` string

RFC 3339 timestamp for when the thread was resolved. Unset while the thread is open.

`createdAt` string

RFC 3339 thread creation timestamp.

`updatedAt` string

RFC 3339 timestamp for the latest thread update.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/threads/THREAD_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "resolved": true}'
```

**Response shape:**

```
{  "id": "cth_01k2ja2000e0080000000000s6",  "version": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  },  "path": "src/telemetry/retry.ts",  "side": "right",  "startLine": 42,  "endLine": 45,  "resolvedAt": "2026-08-03T10:00:00Z",  "createdAt": "2026-08-01T09:30:00Z",  "updatedAt": "2026-08-03T10:00:00Z"}
```

### [List Pull Request Commits](#list-pull-request-commits)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/commits`

Scope[repository:pull\_requests:read](#scopes)AuthInstallation tokenUser access token

Lists the commits in a pull request.

Returns the pull request's commits as sparse `Commit` objects (no `stats`). Results default to 30 and are capped at 100, with at most 250 commits visible overall. A page token fixes the pull request version, page size, and commit cursor; `pageSize` must match the token on later requests, and a token that no longer matches the current head or base returns `400`.

#### [Path Parameters](#path-parameters-67)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-21)

`pageSize` integer

Max commits to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token is bound to the repository, pull request version, page size, and commit offset.

#### [Response Fields](#response-fields-74)

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
{  "commits": [    {      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "commit": {        "author": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "committer": {          "name": "Jane Doe",          "email": "jane@acme.dev",          "date": "2026-08-01T09:30:00Z"        },        "message": "Add launch telemetry",        "tree": {          "sha": "a7b6c5d4e3f2a1b0c9d8e7f6a5b4c3d2e1f0a9b8"        }      },      "parents": [        {          "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"        }      ],      "stats": {        "additions": 128,        "deletions": 46,        "total": 174      }    }  ]}
```

### [List Pull Request Files](#list-pull-request-files)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/files`

Scope[repository:pull\_requests:read](#scopes)AuthInstallation tokenUser access token

Lists the files changed in a pull request.

Returns filename, status, line counts, patch, and optional previous filename. Results default to 30 files and are capped at 100. A page token fixes the pull request version, page size, and file cursor; `pageSize` must match the token on later requests, and a token that no longer matches the current head or base returns `400`.

#### [Path Parameters](#path-parameters-68)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-22)

`pageSize` integer

Max changed files to return. Defaults to 30 when unset or 0. Values above 100 are clamped to 100.

`pageToken` string

Opaque cursor from a previous response's `next_page_token`. Empty for the first page. The token is bound to the repository, pull request version, page size, and changed-file cursor.

#### [Response Fields](#response-fields-75)

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
{  "files": [    {      "filename": "src/telemetry.ts",      "status": "modified",      "additions": 6,      "deletions": 3,      "changes": 9,      "patch": "@@ -12,6 +12,9 @@\n import { ignite } from \"./ignition\";\n+import { emitLaunchTelemetry } from \"./telemetry\";\n"    }  ]}
```

### [List Pull Request Labels](#list-pull-request-labels)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Scope[repository:pull\_requests:read](#scopes)AuthInstallation tokenUser access token

Lists every label assigned to a pull request, ordered by name.

The response carries the full assigned list rather than a page of it, so this endpoint takes no pagination parameters. A pull request can have at most 100 labels. An unknown pull request returns `404`.

#### [Path Parameters](#path-parameters-69)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-76)

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
{  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ]}
```

### [Set Pull Request Labels](#set-pull-request-labels)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Replaces every label assigned to a pull request with the labels you name.

An empty list removes every assigned label. The labels must already exist in the repository; an unknown name or an unknown pull request returns `404`. A pull request can have at most 100 labels, so naming more than 100 returns `FailedPrecondition` (HTTP 400). The response lists the labels assigned after the replacement, ordered by name.

#### [Path Parameters](#path-parameters-70)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-29)

`labels` array

Label names to assign. Maximum 100. An empty list removes every assigned label. Duplicate names are ignored.

#### [Response Fields](#response-fields-77)

`labels` array

Labels assigned after the replacement, ordered by name. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "labels": [    "bug"  ]}'
```

**Response shape:**

```
{  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ]}
```

### [Add Pull Request Labels](#add-pull-request-labels)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Adds existing repository labels to a pull request.

Labels already assigned to the pull request stay assigned. The labels must already exist in the repository; an unknown name or an unknown pull request returns `404`. The request must name between 1 and 100 labels, and a pull request can have at most 100 labels in total, so a request that would take it past that limit returns `FailedPrecondition` (HTTP 400). The response lists the labels you named, not the pull request's full set; read the full set with [List Pull Request Labels](#list-pull-request-labels).

#### [Path Parameters](#path-parameters-71)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-30)

`labels` array Required

Label names to add. Maximum 100. Duplicate names are ignored.

#### [Response Fields](#response-fields-78)

`labels` array

Labels named in the request. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "labels": [    "bug"  ]}'
```

**Response shape:**

```
{  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ]}
```

### [Remove All Pull Request Labels](#remove-all-pull-request-labels)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/labels`

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Removes every label from a pull request.

The request succeeds when the pull request has no labels. An unknown pull request returns `404`. The response body is empty.

#### [Path Parameters](#path-parameters-72)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Response Fields](#response-fields-79)

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

Scope[repository:pull\_requests:write](#scopes)AuthInstallation tokenUser access token

Removes one label from a pull request.

A label that is not assigned to the pull request returns `404`, as does an unknown pull request. The response lists the labels remaining on the pull request, ordered by name.

#### [Path Parameters](#path-parameters-73)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`labelName` string Required

Name of the label to remove.

#### [Response Fields](#response-fields-80)

`labels` array

Labels remaining on the pull request, ordered by name. Each entry carries `id`, `name`, `color`, and `description`.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/labels/LABEL_NAME' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "labels": [    {      "id": "lbl_01k2ja2000e0080000000000m1",      "name": "bug",      "color": "d73a4a",      "description": "Something isn't working"    }  ]}
```

### [Merge Pull Request](#merge-pull-request)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/merge`

Scope[repository:contents:write](#scopes)AuthInstallation tokenUser access token

Merges a pull request into its base.

For a stacked pull request, merges the entire root-to-target prefix ending at this pull number. not only this pull. Supported only on native Origin repositories; mirrored repositories are rejected.

#### [Path Parameters](#path-parameters-74)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

Pull number to merge. When this pull is stacked, the merge lands every pull from the stack root through this number.

#### [Request Body](#request-body-31)

`expectedHeadSha` string

Guard against merging a head your app has not seen: the full commit SHA (40 or 64 hexadecimal characters) expected to be the pull request's current head. When the head has moved, the merge is rejected with `ABORTED` (HTTP 409 Conflict) and nothing merges. Values that are not a full commit SHA are rejected with `InvalidArgument` (HTTP 400). Omit to merge whatever the current head is. Not evaluated when the pull request is already merged, which returns idempotent success.

`mergeMethod` string

How the pull request lands. Allowed values: `merge`, which writes a merge commit, and `squash`, which writes a single squash commit. A method the repository does not allow is rejected with `FailedPrecondition` (HTTP 400), and any other value with `InvalidArgument` (HTTP 400). Omit it to use the repository's default: a merge commit when the repository allows one, otherwise a squash, and a squash when the base branch requires linear history.

#### [Response Fields](#response-fields-81)

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

`pullRequest.author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`pullRequest.author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`pullRequest.author.app` object

App variant of the actor. Set when an app performed the action.

`pullRequest.author.app.id` string

Public identifier for the app.

`pullRequest.author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/merge' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "expectedHeadSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",  "mergeMethod": "squash"}'
```

**Response shape:**

```
{  "mergeCommitSha": "5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d",  "mergedPullNumbers": [    "17"  ],  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "state": "closed",    "draft": false,    "merged": true,    "title": "Add launch telemetry",    "body": "Adds structured launch telemetry to the ignition path.",    "head": {      "ref": "add-telemetry",      "sha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4"    },    "base": {      "ref": "main",      "sha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8"    },    "author": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "createdAt": "2026-08-01T09:30:00Z",    "updatedAt": "2026-08-02T14:45:00Z",    "closedAt": "2026-08-03T10:15:00Z",    "mergedAt": "2026-08-03T10:15:00Z",    "mergeCommitSha": "5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9a8b7c6d",    "additions": 128,    "deletions": 46,    "changedFiles": 5,    "labels": [      {        "id": "lbl_01k2ja2000e0080000000000m1",        "name": "bug",        "color": "d73a4a",        "description": "Something isn't working"      }    ],    "version": {      "number": "3",      "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",      "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",      "createdAt": "2026-08-01T09:30:00Z"    }  }}
```

### [List Pull Request Requested Reviewers](#list-pull-request-requested-reviewers)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/requested_reviewers`

Scope[repository:pull\_requests:reviews:read](#scopes)AuthInstallation tokenUser access token

Lists the users and groups whose review is currently requested on a pull request.

A direct request clears when that user submits a review, and a group request clears when any current member of the group submits. Unsubmitted draft reviews leave the request pending, and requesting review again after a submission returns the reviewer to this list. Groups without a readable public identifier are omitted.

#### [Path Parameters](#path-parameters-75)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

Repository-local pull request number.

#### [Response Fields](#response-fields-82)

`users` array

Users whose review is requested. Empty when none are pending.

`users[].id` string

Encoded user identifier (`user_…`), the same format the organization API uses.

`users[].email` string

Email address of the user. Empty when the account has none.

`users[].displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`users[].handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`groups` array

Groups whose review is requested. Empty when none are pending.

`groups[].id` string

Group public identifier (`grp_…`).

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/requested_reviewers' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "users": [    {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  ],  "groups": [    {      "id": "grp_01k2ja2000e0080000000000n2"    }  ]}
```

### [Request Pull Request Reviewers](#request-pull-request-reviewers)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/requested_reviewers`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Requests reviews from the given users and groups on a pull request, and returns the reviewers this call requested.

Identifiers resolve against the repository's reviewer candidates by public id, user email, or group slug. Display names do not resolve. An unknown or ambiguous identifier returns `InvalidArgument` (HTTP 400) naming the identifier, and at least one non-empty entry is required across `users` and `groups`.

Requesting an already-requested reviewer bumps the request timestamp, so a reviewer who had submitted a review reappears as pending. A reviewer who is not a candidate for the repository returns `PermissionDenied` (HTTP 403).

#### [Path Parameters](#path-parameters-76)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

Repository-local pull request number.

#### [Request Body](#request-body-32)

`users` array

User identifiers to request. Each entry must uniquely match a user candidate for the repository by public `user_…` id or email.

`groups` array

Group identifiers to request. Each entry must uniquely match a group candidate for the repository by public `grp_…` id, qualified group slug, or group slug.

#### [Response Fields](#response-fields-83)

`users` array

Users this call requested.

`users[].id` string

Encoded user identifier (`user_…`), the same format the organization API uses.

`users[].email` string

Email address of the user. Empty when the account has none.

`users[].displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`users[].handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`groups` array

Groups this call requested.

`groups[].id` string

Group public identifier (`grp_…`).

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/requested_reviewers' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "users": [    "user_01k2ja2000e0080000000000c3"  ],  "groups": [    "grp_01k2ja2000e0080000000000n2"  ]}'
```

**Response shape:**

```
{  "users": [    {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  ],  "groups": [    {      "id": "grp_01k2ja2000e0080000000000n2"    }  ]}
```

### [Remove Pull Request Requested Reviewers](#remove-pull-request-requested-reviewers)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/requested_reviewers`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Removes requested reviews from the given users and groups on a pull request. The response body is empty.

Identifiers resolve against the repository's reviewer candidates by public id, user email, or group slug. Display names do not resolve. An unknown or ambiguous identifier returns `InvalidArgument` (HTTP 400) naming the identifier, and at least one non-empty entry is required across `users` and `groups`.

Removing a user or group that is not currently requested is a no-op. An identifier that is no longer a reviewer candidate is still accepted when it is a stable public id (`user_…` or `grp_…`), so a reviewer who left the repository can be cleared.

#### [Path Parameters](#path-parameters-77)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

Repository-local pull request number.

#### [Request Body](#request-body-33)

`users` array

User identifiers to remove. Each entry must uniquely match a user candidate for the repository by public `user_…` id or email.

`groups` array

Group identifiers to remove. Each entry must uniquely match a group candidate for the repository by public `grp_…` id, qualified group slug, or group slug.

#### [Response Fields](#response-fields-84)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/requested_reviewers' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "users": [    "user_01k2ja2000e0080000000000c3"  ],  "groups": [    "grp_01k2ja2000e0080000000000n2"  ]}'
```

**Response:**

```
204 No Content
```

### [List Pull Request Reviews](#list-pull-request-reviews)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews`

Scope[repository:pull\_requests:reviews:read](#scopes)AuthInstallation tokenUser access token

Lists submitted reviews on a pull request, ordered by `submitted_at` ascending. Pending reviews are omitted.

#### [Path Parameters](#path-parameters-78)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Query Parameters](#query-parameters-23)

`pageSize` integer

Maximum reviews to return. Defaults to 30; maximum 100.

`pageToken` string

Opaque cursor from a previous response's `nextPageToken`. Omit it for the first page.

#### [Response Fields](#response-fields-85)

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

`reviews[].author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`reviews[].author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`reviews[].author.app` object

App variant of the actor. Set when an app performed the action.

`reviews[].author.app.id` string

Public identifier for the app.

`reviews[].author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`reviews[].dismissal.dismissedBy.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`reviews[].dismissal.dismissedBy.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`reviews[].dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`reviews[].dismissal.dismissedBy.app.id` string

Public identifier for the app.

`reviews[].dismissal.dismissedBy.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

Opaque cursor for the next page; empty when there are no more reviews.

```
curl --request GET \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response shape:**

```
{  "reviews": [    {      "id": "rev_01k2ja2000e0080000000000f6",      "author": {        "user": {          "id": "user_01k2ja2000e0080000000000c3",          "email": "jane@acme.dev"        }      },      "verdict": "approve",      "body": "Approving. The telemetry schema matches the spec.",      "submittedAt": "2026-08-02T15:00:00Z",      "pullRequestVersion": {        "number": "3",        "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",        "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",        "createdAt": "2026-08-01T09:30:00Z"      }    }  ],  "pullRequest": {    "id": "pr_01k2ja2000e0080000000000d4",    "number": "17",    "repository": {      "id": "repo_01k2ja2000e0080000000000q4",      "name": "rocket",      "owner": {        "slug": "acme",        "id": "ns_01k2ja2000e0080000000000p3",        "type": "team"      }    }  }}
```

### [Create Pull Request Review](#create-pull-request-review)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Creates and submits a review on a pull request, optionally together with its comments in one atomic request. Each comment takes the same targets [Create Pull Request Comment](#create-pull-request-comment) takes: `comments[].inline` for a line range, `comments[].file` for a whole file, `comments[].threadId` for a reply, and none of them for general discussion.

The review is submitted immediately. A new `approve` or `request_changes` review supersedes the caller's prior live decision review on the same pull request, which is dismissed. Pull request authors cannot `approve` their own pull request. Fails with FAILED\_PRECONDITION while the caller has an unsubmitted draft review on the pull request.

When `comments` is set, every anchor is validated against the reviewed version's diff before anything is written, using the same in-diff check as [Create Pull Request Comment](#create-pull-request-comment). If one comment fails, the whole request fails with `InvalidArgument` (HTTP 400) and nothing is published. Comments become visible atomically with the review: no comment or event is observable until the review submits, and then each comment emits its own [pull\_request.comment.created](#events) webhook alongside the review's event.

The operation carries no idempotency key, so a retry after an ambiguous transport failure can create a second review. Call [List Pull Request Reviews](#list-pull-request-reviews) before retrying.

#### [Path Parameters](#path-parameters-79)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

#### [Request Body](#request-body-34)

`verdict` string Required

The review decision. Allowed values: `PULL_REQUEST_REVIEW_VERDICT_UNSPECIFIED`, `approve`, `request_changes`, `comment`.

`body` string

Free-text review summary. May be empty.

`versionNumber` string

Pull request version number the review applies to (see `PullRequestVersion.number`). Omit to review the latest version at call time. Comments anchor against this same version.

`comments` array

Comments published atomically with the review. Maximum 50 per request.

`comments[].body` string Required

Comment text. Must contain a non-whitespace character.

`comments[].inline` object

Diff anchor for a new inline thread on the reviewed version's diff. Same shape and validation as `inline` on [Create Pull Request Comment](#create-pull-request-comment). Cannot be combined with `comments[].threadId`.

`comments[].inline.path` string Required

File path in the reviewed version's diff.

`comments[].inline.side` string Required

Diff side of the anchor. Allowed values: `left` for the base version of the file, `right` for the head version.

`comments[].inline.startLine` integer Required

First 1-based line of the anchored range in the `side` version of the file. The range must not run past the end of that file.

`comments[].inline.endLine` integer

Inclusive last line of the anchored range. Must be greater than or equal to `startLine`. Omit for a single-line anchor.

`comments[].threadId` string

Existing thread id on this pull request to reply to. The reply stays hidden until the review publishes. Omit `comments[].inline`, `comments[].file`, and this field to open a new general-discussion thread.

`comments[].file` object

Anchor for a new file-level thread on a whole file in the reviewed version's diff. Same shape, side derivation, and validation as `file` on [Create Pull Request Comment](#create-pull-request-comment). Cannot be combined with `comments[].inline` or `comments[].threadId`.

`comments[].file.path` string Required

File path in the reviewed version's diff: the deleted path for a deletion, the head path otherwise.

#### [Response Fields](#response-fields-86)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`dismissal.dismissedBy.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`dismissal.dismissedBy.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "verdict": "approve",  "body": "Approving. The telemetry schema matches the spec.",  "versionNumber": "3"}'
```

**Response shape:**

```
{  "id": "rev_01k2ja2000e0080000000000f6",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "verdict": "approve",  "body": "Approving. The telemetry schema matches the spec.",  "submittedAt": "2026-08-02T15:00:00Z",  "pullRequestVersion": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  }}
```

### [Update Pull Request Review](#update-pull-request-review)

PATCH`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews/{reviewId}`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Updates the body of a review. Only the review author can update it; other callers receive PERMISSION\_DENIED. A review that does not belong to the named pull request returns NOT\_FOUND.

Unsubmitted draft reviews can be updated too; a draft's response has no `submitted_at`.

#### [Path Parameters](#path-parameters-80)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`reviewId` string Required

#### [Request Body](#request-body-35)

`body` string Required

Replacement review summary text; replaces the prior body in full. Must contain a non-whitespace character; INVALID\_ARGUMENT otherwise.

#### [Response Fields](#response-fields-87)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`dismissal.dismissedBy.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`dismissal.dismissedBy.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request PATCH \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews/REVIEW_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "body": "Approving. The telemetry schema matches the spec."}'
```

**Response shape:**

```
{  "id": "rev_01k2ja2000e0080000000000f6",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "verdict": "approve",  "body": "Approving. The telemetry schema matches the spec.",  "submittedAt": "2026-08-02T15:00:00Z",  "pullRequestVersion": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  }}
```

### [Dismiss Pull Request Review](#dismiss-pull-request-review)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/pulls/{pullNumber}/reviews/{reviewId}/dismissals`

Scope[repository:pull\_requests:reviews:write](#scopes)AuthInstallation tokenUser access token

Dismisses a submitted review so its verdict no longer counts toward the pull request's review state. The review itself is retained and keeps appearing in ListPullRequestReviews, with `dismissal` set.

Dismissing does not require having authored the review; write permission on the repository's pull request reviews is sufficient.

Only `approve` and `request_changes` reviews can be dismissed, and only once: a `comment` review, an unsubmitted draft review, or an already-dismissed review returns FAILED\_PRECONDITION, and repeating the call leaves the first dismissal in place. A review that does not belong to the named pull request returns NOT\_FOUND.

#### [Path Parameters](#path-parameters-81)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`pullNumber` string Required

`reviewId` string Required

Stable Origin review identifier, as returned by ListPullRequestReviews.

#### [Request Body](#request-body-36)

`message` string Required

Reason recorded with the dismissal. Must contain a non-whitespace character; INVALID\_ARGUMENT otherwise.

#### [Response Fields](#response-fields-88)

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

`author.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`author.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`author.app` object

App variant of the actor. Set when an app performed the action.

`author.app.id` string

Public identifier for the app.

`author.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

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

`dismissal.dismissedBy.user.displayName` string

Display name of the user: the account's first and last name joined with a space, the same name the product renders. Omitted when the account has no name.

`dismissal.dismissedBy.user.handle` string

The user's claimed profile handle, without the `@` prefix. Present only while that profile is publicly visible; omitted otherwise.

`dismissal.dismissedBy.app` object

App variant of the actor. Set when an app performed the action.

`dismissal.dismissedBy.app.id` string

Public identifier for the app.

`dismissal.dismissedBy.app.displayName` string

The app's registered display name. Omitted when the app cannot be resolved and on Cursor's first-party managed actor.

`dismissal.dismissedBy.serviceAccount` object

Service account variant of the actor. Set when a service account performed the action.

`dismissal.dismissedBy.serviceAccount.id` string

Public identifier for the service account.

`dismissal.dismissedAt` string

RFC 3339 dismissal timestamp.

`dismissal.message` string

Dismissal reason; automatic supersession uses a server-generated message.

```
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/pulls/PULL_NUMBER/reviews/REVIEW_ID/dismissals' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "message": "Superseded by a newer review."}'
```

**Response shape:**

```
{  "id": "rev_01k2ja2000e0080000000000f6",  "author": {    "user": {      "id": "user_01k2ja2000e0080000000000c3",      "email": "jane@acme.dev"    }  },  "verdict": "approve",  "body": "Approving. The telemetry schema matches the spec.",  "submittedAt": "2026-08-02T15:00:00Z",  "pullRequestVersion": {    "number": "3",    "headSha": "9a41f0c3d2b8e7f6a5c4d3e2f1b0a9c8d7e6f5a4",    "baseSha": "3b1f9c2d8a7e6f5049c8b7a6d5e4f3a2b1c0d9e8",    "createdAt": "2026-08-01T09:30:00Z"  },  "dismissal": {    "dismissedBy": {      "user": {        "id": "user_01k2ja2000e0080000000000c3",        "email": "jane@acme.dev"      }    },    "dismissedAt": "2026-08-02T15:00:00Z",    "message": "Superseded by a newer review."  }}
```

## [Rulesets](#rulesets)

### [List Rulesets](#list-rulesets)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets`

Scope[repository:rulesets:read](#scopes)AuthInstallation tokenUser access token

Lists every ruleset configured on a repository.

Rulesets per repository are bounded configuration, so the full set comes back in one response and this endpoint does not paginate. `repository` is hoisted once and describes the repository shared by every ruleset in the response.

#### [Path Parameters](#path-parameters-82)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Response Fields](#response-fields-89)

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
{  "rulesets": [    {      "id": "rs_01k2ja2000e0080000000000t7",      "name": "require-review",      "description": "Require an approving review before merging to main.",      "enforcement": "active",      "kind": "merge_branch",      "includedRefNames": [        "refs/heads/main"      ],      "rules": [        {          "id": "rsr_01k2ja2000e0080000000000v8",          "ruleType": "pull_request",          "parameters": {            "requiredApprovingReviewCount": 1          }        }      ],      "bypassActors": [        {          "id": "rsba_01k2ja2000e0080000000000w9",          "bypassMode": "always",          "user": {            "id": "act_01k2ja2000e0080000000000x0"          }        }      ]    }  ],  "repository": {    "id": "repo_01k2ja2000e0080000000000q4",    "name": "rocket",    "owner": {      "slug": "acme",      "id": "ns_01k2ja2000e0080000000000p3",      "type": "team"    }  }}
```

### [Create Ruleset](#create-ruleset)

POST`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets`

Scope[repository:rulesets:write](#scopes)AuthInstallation tokenUser access token

Creates a repository ruleset.

The response carries the stored ruleset, including the IDs Origin assigns to each rule and bypass actor. An empty `name` is rejected with `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-83)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

#### [Request Body](#request-body-37)

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

#### [Response Fields](#response-fields-90)

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
curl --request POST \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "require-review",  "description": "Require an approving review before merging to main.",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "refs/heads/main"  ],  "rules": [    {      "ruleType": "pull_request",      "parameters": {        "requiredApprovingReviewCount": 1      }    }  ],  "bypassActors": [    {      "bypassMode": "always",      "user": {        "id": "act_01k2ja2000e0080000000000x0"      }    }  ]}'
```

**Response shape:**

```
{  "id": "rs_01k2ja2000e0080000000000t7",  "name": "require-review",  "description": "Require an approving review before merging to main.",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "refs/heads/main"  ],  "rules": [    {      "id": "rsr_01k2ja2000e0080000000000v8",      "ruleType": "pull_request",      "parameters": {        "requiredApprovingReviewCount": 1      }    }  ],  "bypassActors": [    {      "id": "rsba_01k2ja2000e0080000000000w9",      "bypassMode": "always",      "user": {        "id": "act_01k2ja2000e0080000000000x0"      }    }  ]}
```

### [Get Ruleset](#get-ruleset)

GET`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`

Scope[repository:rulesets:read](#scopes)AuthInstallation tokenUser access token

Returns a single repository ruleset by its stable Origin ID.

An unknown repository and an unknown ruleset both return `404`; the message distinguishes them.

#### [Path Parameters](#path-parameters-84)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`rulesetId` string Required

Stable Origin ruleset ID.

#### [Response Fields](#response-fields-91)

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
{  "id": "rs_01k2ja2000e0080000000000t7",  "name": "require-review",  "description": "Require an approving review before merging to main.",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "refs/heads/main"  ],  "rules": [    {      "id": "rsr_01k2ja2000e0080000000000v8",      "ruleType": "pull_request",      "parameters": {        "requiredApprovingReviewCount": 1      }    }  ],  "bypassActors": [    {      "id": "rsba_01k2ja2000e0080000000000w9",      "bypassMode": "always",      "user": {        "id": "act_01k2ja2000e0080000000000x0"      }    }  ]}
```

### [Update Ruleset](#update-ruleset)

PUT`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`

Scope[repository:rulesets:write](#scopes)AuthInstallation tokenUser access token

Updates an existing repository ruleset.

The request replaces the whole ruleset configuration. `rules` and `bypassActors` are replaced in full rather than merged, and Origin assigns new IDs to the stored entries, so send every rule and bypass actor you want to keep.

#### [Path Parameters](#path-parameters-85)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`rulesetId` string Required

Stable Origin ruleset ID.

#### [Request Body](#request-body-38)

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

#### [Response Fields](#response-fields-92)

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
curl --request PUT \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets/RULESET_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN' \  --header 'Content-Type: application/json' \  --data '{  "name": "require-review",  "description": "Require an approving review before merging to main.",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "refs/heads/main"  ],  "rules": [    {      "ruleType": "pull_request",      "parameters": {        "requiredApprovingReviewCount": 1      }    }  ],  "bypassActors": [    {      "bypassMode": "always",      "user": {        "id": "act_01k2ja2000e0080000000000x0"      }    }  ]}'
```

**Response shape:**

```
{  "id": "rs_01k2ja2000e0080000000000t7",  "name": "require-review",  "description": "Require an approving review before merging to main.",  "enforcement": "active",  "kind": "merge_branch",  "includedRefNames": [    "refs/heads/main"  ],  "rules": [    {      "id": "rsr_01k2ja2000e0080000000000v8",      "ruleType": "pull_request",      "parameters": {        "requiredApprovingReviewCount": 1      }    }  ],  "bypassActors": [    {      "id": "rsba_01k2ja2000e0080000000000w9",      "bypassMode": "always",      "user": {        "id": "act_01k2ja2000e0080000000000x0"      }    }  ]}
```

### [Delete Ruleset](#delete-ruleset)

DELETE`/v1/origin/repos/{ownerSlug}/{repoName}/rulesets/{rulesetId}`

Scope[repository:rulesets:write](#scopes)AuthInstallation tokenUser access token

Deletes a repository ruleset by its stable Origin ID. The response body is empty.

An unknown repository and an unknown ruleset both return `404`; the message distinguishes them. A ruleset stored on a different repository reads as an unknown ruleset. An empty `rulesetId` returns `InvalidArgument` (HTTP 400).

#### [Path Parameters](#path-parameters-86)

`ownerSlug` string Required

Owning entity's unique slug.

`repoName` string Required

Repo name, unique to the owner entity.

`rulesetId` string Required

Stable Origin ruleset ID.

#### [Response Fields](#response-fields-93)

Successful requests return no response body.

```
curl --request DELETE \  --url 'https://api.cursor.com/v1/origin/repos/OWNER_SLUG/REPO_NAME/rulesets/RULESET_ID' \  --header 'Authorization: Bearer YOUR_ORIGIN_TOKEN'
```

**Response:**

```
204 No Content
```

English

- English
- 简体中文
- Русский
- 日本語
- Português
- Español
