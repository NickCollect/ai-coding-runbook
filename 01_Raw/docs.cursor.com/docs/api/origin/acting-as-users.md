---
source_url: https://cursor.com/docs/api/origin/acting-as-users
fetched_at: 2026-09-28T06:10:41.057017+00:00
fetch_method: mintlify_md
---

# Acting on behalf of users

Origin is in Early Beta and subject to change.

Origin Apps use installation user tokens to act on behalf of members of the namespace they're installed in. Each request is limited to permissions held by both the installation and the user.

Use the [Origin API](https://cursor.com/docs/api/origin.md) base URL and [error model](https://cursor.com/docs/api/origin/reference/errors.md). Mint tokens with an [app JWT](https://cursor.com/docs/api/origin/reference/app-jwt.md).

## How it works

1. A workspace admin approves the `namespace:user_tokens:write` scope for your app's installation.
2. Optionally, [confirm the user's Cursor identity](https://cursor.com/docs/api/origin/acting-as-users.md#user-confirmation). Origin returns a signed receipt with their `user_…` ID.
3. Sign an app JWT and [mint an installation user token](https://cursor.com/docs/api/origin/acting-as-users.md#mint-an-installation-user-token) for the user's ID or email.
4. Use the installation user token with the REST API or Git over HTTPS until `expiresAt`, then mint another.

## Request the scope

Add `namespace:user_tokens:write` to the `scope` parameter of the [installation URL](https://cursor.com/docs/api/origin/reference/installation.md). For an existing installation, also send `include_granted_scopes=true` so the admin approves only the addition.

```text
https://cursor.com/codebase/apps/install
  ?client_id=APP_ID
  &scope=namespace:user_tokens:write%20repository:pull_requests:write
  &redirect_uri=REGISTERED_CALLBACK
  &state=RANDOM_ANTI_FORGERY_VALUE
  &include_granted_scopes=true
```

This scope lets the installation mint tokens for any active namespace member. It can't be included in a token's `scopes`. Other admin-approved scopes still cap each token's permissions.

## When to confirm a user

User confirmation is optional: the admin's approval of `namespace:user_tokens:write` covers every namespace member.

Confirm a user to link an account in your product to their Cursor account, or to verify an identity instead of trusting a typed email address. The receipt proves the signed-in user's `user_…` ID, email, and namespace membership at confirmation time.

Receipts prove identity and grant no permissions. Create Installation User Token neither accepts nor requires one.

## User confirmation

### Send the user to Origin

Open this URL in the user's browser:

```text
https://cursor.com/codebase/apps/user-confirmation
  ?installation_id=INSTALLATION_ID
  &redirect_uri=REGISTERED_CALLBACK
  &state=RANDOM_ANTI_FORGERY_VALUE
```

| Parameter         | Required             | Description                                                                                                                                                       |
| ----------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `installation_id` | Yes                  | The `i_…` ID of your app's active installation in the user's namespace.                                                                                           |
| `redirect_uri`    | Yes                  | Callback URI. Must exactly match an entry in the app's `installationRedirectUris`, the installation flow's allowlist.                                             |
| `state`           | Strongly recommended | Random anti-forgery value, echoed as the `state` claim of the [confirmation receipt](https://cursor.com/docs/api/origin/acting-as-users.md#confirmation-receipt). |

Send each parameter at most once. Missing required parameters or repeated parameters produce an error after sign-in.

### What the user sees

Signed-out users sign in to Cursor, then return to the same link with its parameters. Origin validates parameters after sign-in, so even malformed links go through sign-in before showing an error.

Origin shows your app's name, icon, and description alongside the installation's namespace. It also lists the details your app will receive:

- Cursor user ID (`user_…`)
- Email
- Origin namespace slug and ID

The page explains that confirmation shares identity and current namespace membership without granting repository access. The user chooses **Confirm** or **Cancel**.

Only active members of the owning team, or the owner of a personal namespace, can confirm.

### Callback

On confirmation, Origin redirects to your callback:

```text
https://app.example.com/origin/confirm?confirmation_receipt=RECEIPT_JWT&state=RANDOM_ANTI_FORGERY_VALUE
```

Verify the [confirmation receipt](https://cursor.com/docs/api/origin/acting-as-users.md#confirmation-receipt) before reading its user claims. The callback includes `state` only if the confirmation URL supplied a non-empty value. Trust the signed `state` claim rather than the query parameter.

Canceling or failing to confirm sends no callback or redirect. Treat a missing callback as "not confirmed" and let the user restart.

### Confirmation receipt

`confirmation_receipt` is a compact JWT signed by Origin with the same keys as [installation receipts](https://cursor.com/docs/api/origin/reference/installation-receipt.md).

JOSE header:

```json
{
  "alg": "EdDSA",
  "kid": "origin-key-id",
  "typ": "origin-user-confirmation-receipt+jwt"
}
```

Claims:

```json
{
  "iss": "https://api.cursor.com/v1/origin",
  "aud": "app_01...",
  "sub": "user_01...",
  "installation_id": "i_01...",
  "namespace_id": "ns_01...",
  "email": "user@example.com",
  "iat": 1786465200,
  "exp": 1786465500,
  "jti": "RECEIPT_UUID",
  "state": "ORIGINAL_VALUE"
}
```

- `aud` is your app ID; `sub` is the confirmed user's `user_…` ID, used as `userId` when minting.
- `installation_id` and `namespace_id` identify the installation and namespace where membership was confirmed.
- `email` is the user's account email at confirmation time.
- Receipts expire five minutes after issuance. `jti` is unique per receipt.
- `state` is included only if the confirmation URL supplied a non-empty value.

Verify the receipt before trusting the callback:

1. Resolve the signing key from the [JWKS](https://cursor.com/docs/api/origin/reference/discovery-and-signing-keys.md) by the `kid` header.
2. Require `alg: EdDSA` and `typ: origin-user-confirmation-receipt+jwt` to distinguish confirmation receipts from installation receipts and access tokens.
3. Validate the signature, `iss`, `aud`, and `exp`.
4. Match `installation_id` and the signed `state` to the values you sent.

Reject the callback when any check fails.

### Confirmation errors

Failures stay on the Cursor page without calling your callback.

| Error                   | Cause                                                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Invalid link            | `installation_id` or `redirect_uri` is missing or empty, or a parameter is repeated.                                                                                                 |
| Not authorized          | The installation doesn't exist or isn't active, `redirect_uri` isn't registered for the app, or the user isn't a member of the installation's namespace. The page doesn't say which. |
| Temporarily unavailable | Origin couldn't sign the receipt after confirmation. The user can retry.                                                                                                             |

## Mint an installation user token

Call [Create Installation User Token](https://cursor.com/docs/api/origin/reference/create-installation-user-token.md), `POST /v1/origin/app/installations/{installationId}/user_access_tokens`, with an [app JWT](https://cursor.com/docs/api/origin/reference/app-jwt.md). Set exactly one of `userId` or `userEmail`.

```bash
curl --request POST \
  --url 'https://api.cursor.com/v1/origin/app/installations/INSTALLATION_ID/user_access_tokens' \
  --header 'Authorization: Bearer APP_JWT' \
  --header 'Content-Type: application/json' \
  --data '{
  "userId": "user_01...",
  "scopes": [
    "repository:pull_requests:write"
  ],
  "repositoryIds": [
    "repo_01..."
  ]
}'
```

```json
{
  "token": "YOUR_INSTALLATION_USER_TOKEN",
  "expiresAt": "2026-01-01T00:15:00Z"
}
```

| Field           | Description                                                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `userId`        | The user's `user_…` ID from a confirmation receipt's `sub` or an actor payload.                                                                                                                                          |
| `userEmail`     | The user's account email. It must match exactly one active member of the installation's namespace.                                                                                                                       |
| `scopes`        | Optional limit. Values must be unique and approved for the installation. `namespace:user_tokens:write` and scopes prefixed with `app:` or `installation:` can't be delegated. Empty or omitted uses current permissions. |
| `repositoryIds` | Optional limit of up to 50 unique repository IDs accessible to the installation. Empty or omitted uses current permissions.                                                                                              |

The user must have an active Cursor account and meet the [namespace membership rules](https://cursor.com/docs/api/origin/acting-as-users.md#what-the-user-sees). Unknown users, non-members, and emails matching several members return the same `403`.

With both `scopes` and `repositoryIds` set, minting succeeds only if the installation and user each hold every requested scope on every listed repository. With fewer limits, permissions are checked on each request instead.

### Lifetime

`expiresAt` is at most 15 minutes after minting and never later than the app JWT's `exp`, as with [installation access tokens](https://cursor.com/docs/api/origin/reference/installation-access-token.md). There's no refresh token: mint another with a fresh app JWT after expiry. Each mint costs 1 point against the app JWT's [rate limit](https://cursor.com/docs/api/origin/reference/rate-limits.md).

### Use the token

Treat installation user tokens as opaque: don't inspect or parse their contents. Send the token as a Bearer credential to the REST API, or as the password for [Git over HTTPS](https://cursor.com/docs/api/origin/reference/git-https-authentication.md) with the username `x-access-token`:

```text
Authorization: Bearer YOUR_INSTALLATION_USER_TOKEN
```

Each request must fit the installation's approved scopes and repository selection, the user's Origin grants, and the token's limits. Otherwise it returns `403`, or `404` if the resource isn't visible.

Actor fields name the user and can include `performedVia.app` with your app's `id` and optional `displayName`. Attribution applies to the action that field describes: on a comment's author, it identifies the app that created the comment. It doesn't identify an app that later edited or deleted it. `performedVia` is absent for direct user actions and can be absent when delegation data is unavailable.

### Mint errors

| HTTP status | Cause                                                                                                                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`       | The request doesn't set exactly one of `userId` or `userEmail`, uses an invalid `user_…` ID or email address, includes duplicate, malformed, or non-delegable scopes, or includes duplicate repository IDs or more than 50. |
| `401`       | The app JWT is invalid or expired, or the installation doesn't exist, belongs to another app, or is suspended.                                                                                                              |
| `403`       | The installation lacks `namespace:user_tokens:write`, the requested limits exceed the installation's grant, the user isn't eligible, or a request with both limits includes a permission the installation or user lacks.    |
| `429`       | The app JWT's rate limit is exhausted. See [Exceeding the limit](https://cursor.com/docs/api/origin/reference/exceeding-the-limit.md).                                                                                      |
| `503`       | Origin couldn't look up the user or sign the token. Retry with backoff.                                                                                                                                                     |

## Revocation

Individual tokens can't be revoked. These changes affect token access:

- Uninstalling or deleting the app invalidates its user tokens before `expiresAt`. Requests return `401`.
- Closing the user's Cursor account invalidates their tokens. Requests return `401`.
- Removing `namespace:user_tokens:write` or suspending the installation stops new mints. Issued tokens expire at `expiresAt`.
- Changes to the installation's or the user's grants apply no later than `expiresAt`.

## Security notes

- Mint just in time with the smallest `scopes` and `repositoryIds` needed. Treat tokens like passwords; don't store or log them.
- Key linked accounts on `sub`, not `email`: the user's `user_…` ID is stable; their email can change.
- Verify email addresses before minting with `userEmail`. A typed address can name a different member.
- Use each receipt once. Record its `jti` and reject repeats within its five-minute lifetime.
- A receipt isn't a credential: don't send it as a Bearer token or log it, since it contains the user's email.
- Receipts describe membership at confirmation time. Each mint rechecks membership, so a stored receipt doesn't let you mint for someone who left.


---

## Sitemap

[Origin API docs index](https://cursor.com/docs/api/origin/llms.txt)
