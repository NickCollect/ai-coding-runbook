---
source_url: https://cursor.com/docs/account/organizations/organization-admin-api
fetched_at: 2026-06-29T05:25:13.170844+00:00
fetch_method: mintlify_md
---

# Organization API

The Organization API lets you perform actions that apply across teams linked to an organization, such as moving users between those teams, reporting on pooled usage across teams, and managing organization groups. It uses an **Organization API key** and the same HTTP patterns as the [team Admin API](https://cursor.com/docs/account/teams/admin-api.md).

- The Organization API uses [Basic Authentication](https://cursor.com/docs/api.md#basic-authentication) with your API key as the username.
- For details on creating API keys, authentication methods, rate limits, and best practices, see the [API Overview](https://cursor.com/docs/api.md).

## Organization API keys vs Team API keys

Organization API keys are organization-scoped credentials. Team API keys are team-scoped credentials.

Use an **Organization API key** when calling organization-level endpoints like `/organizations/team-memberships/sync`, `/organizations/pooled-usage`, and `/organizations/groups`.

Use a **Team API key** when calling team-level endpoints under `/teams/*` (for example, `/teams/members` and `/teams/spend`).

### Key differences

- **Scope**: Organization API keys can act across teams linked to the same organization. Team API keys can only act within one team.
- **Endpoint compatibility**: Organization endpoints require Organization API keys. Team endpoints require Team API keys.
- **Key scopes**: Each route requires a specific scope on the key. Membership and group routes need **`members:*`**; usage routes need **`usage:*`**. Keys with **`admin:*`** work everywhere because admin implies the other scopes.
- **Authorization failures**: If the key scope does not match the endpoint scope, requests fail with authentication or authorization errors (typically `401` or `403`).

### How should I pass an Organization API key?

Pass it the same way as other Cursor API keys: Basic authentication with the key as the username and an empty password.

```bash
curl -X POST https://api.cursor.com/organizations/team-memberships/sync \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "organizationId": "org_abc123",
    "users": [
      { "userId": 12345, "destinationTeamId": 7 }
    ]
  }'
```

## Endpoints

### Sync Organization Team Memberships

/organizations/team-memberships/sync

Move one or more users between teams that are linked to your organization. For each requested move, the member’s team assignment within the organization is set to exactly the destination team, and they are removed from any other linked teams. This matches the bulk style of the CSV import API: you send an array of users and receive a result row for each one.

#### Request body

`organizationId` string Required

Public organization ID (for example `org_abc123`). Must match the organization for the Organization API key used to call the endpoint.

`users` array Required

Non-empty list of moves (at most 500 per request). Each element is an object with:

- `userId` number | string: ID of the user to move. Accepts either an integer numeric ID (for example `12345`) or a string ID (for example `"user_abc123"`).
- `destinationTeamId` number: Integer team ID for the destination. Must be a team linked to the organization.

#### Success response (HTTP 200)

`results` array

One entry per requested move, in order. Each object includes `userId`, `destinationTeamId`, and either `status: &quot;success&quot;` or `status: &quot;error&quot;` with `errorMessage` when that row failed.

`successCount` number

Number of rows with `status: &quot;success&quot;`.

`errorCount` number

Number of rows with `status: &quot;error&quot;`.

- **Availability**: Enterprise only
- **Authentication**: Organization API key (Basic auth). The key must include the **`members:*`** scope for this route; keys with **`admin:*`** also work because admin implies members.
- **Organization match**: The `organizationId` in the body must be the same organization as the API key; otherwise the request is rejected.
- The target user must already be a member of the organization for a move to succeed.
- The destination team must be linked to the organization for a move to succeed.
- If one move in `users` fails, others can still succeed; check each `results` entry’s `status` and `errorMessage`.
- **Batch size**: A single request may include up to 500 moves. Send additional batches in separate requests if needed.

```bash
curl -X POST https://api.cursor.com/organizations/team-memberships/sync \
  -u YOUR_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "organizationId": "org_abc123",
    "users": [
      { "userId": 12345, "destinationTeamId": 7 },
      { "userId": "user_abc123", "destinationTeamId": 8 }
    ]
  }'
```

**Response:**

```json
{
  "results": [
    {
      "userId": 12345,
      "destinationTeamId": 7,
      "status": "success"
    },
    {
      "userId": "user_abc123",
      "destinationTeamId": 8,
      "status": "success"
    }
  ],
  "successCount": 2,
  "errorCount": 0
}
```

**Error responses:**

Most thrown API errors use HTTP **401**, **403**, or **400** and a JSON body shaped like:

```json
{
  "code": "error",
  "message": "…"
}
```

**404: organization not found** (this route uses a different field name for the message):

```json
{
  "error": "Organization not found"
}
```

**401: invalid Organization API key** (wrong or missing key):

```json
{
  "code": "error",
  "message": "Invalid Organization API Key"
}
```

**401: missing required scope** (key is valid but does not include `members:*` or `admin:*`):

```json
{
  "code": "error",
  "message": "Organization API key missing required scope: members:*"
}
```

**403: organization does not match the key** (`organizationId` in the body is not the organization for this API key):

```json
{
  "code": "error",
  "message": "Not authorized"
}
```

**400: invalid request body** (examples; only one applies per failed request):

```json
{
  "code": "error",
  "message": "Request body is required"
}
```

```json
{
  "code": "error",
  "message": "organizationId is required"
}
```

```json
{
  "code": "error",
  "message": "users must be a non-empty array"
}
```

```json
{
  "code": "error",
  "message": "users must not contain more than 500 moves"
}
```

**Per-row failures (HTTP 200)**: Validation or business rules for a single move are returned in `results` with `status: "error"` and `errorMessage`. Invalid `userId` / `destinationTeamId` types use `0` for the invalid field in the row:

```json
{
  "results": [
    {
      "userId": 0,
      "destinationTeamId": 7,
      "status": "error",
      "errorMessage": "Invalid userId"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

```json
{
  "results": [
    {
      "userId": 12345,
      "destinationTeamId": 0,
      "status": "error",
      "errorMessage": "Invalid destinationTeamId"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

```json
{
  "results": [
    {
      "userId": 0,
      "destinationTeamId": 0,
      "status": "error",
      "errorMessage": "Invalid userId. Invalid destinationTeamId"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

**Per-row failures (HTTP 200)**: From the move logic when inputs are well-typed but the move cannot be applied:

```json
{
  "results": [
    {
      "userId": 12345,
      "destinationTeamId": 999,
      "status": "error",
      "errorMessage": "Team is not linked to this organization"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

```json
{
  "results": [
    {
      "userId": 12345,
      "destinationTeamId": 7,
      "status": "error",
      "errorMessage": "User is not a member of this organization"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

```json
{
  "results": [
    {
      "userId": 12345,
      "destinationTeamId": 7,
      "status": "error",
      "errorMessage": "User not found"
    }
  ],
  "successCount": 0,
  "errorCount": 1
}
```

## Usage

Report on usage across every team linked to your organization. These endpoints aggregate data from all teams in the [organization pool](https://cursor.com/docs/enterprise/pooled-usage.md), so you don't need a separate Team API key per team. For single-team reporting, use the team [Admin API](https://cursor.com/docs/account/teams/admin-api.md) usage endpoints instead.

- **Availability**: Enterprise only
- **Authentication**: Organization API key (Basic auth). The key must include the **`usage:*`** scope for these routes; keys with **`admin:*`** also work because admin implies usage.
- **Organization match**: The `organizationId` in the body must be the same organization as the API key; otherwise the request is rejected.
- **Team containment**: Any `teamId` (or entry in `teamIds`) must belong to the organization. Requests that reference a team outside the organization are rejected.
- **Polling**: Usage data is aggregated at the hourly level. Poll these endpoints at most once per hour. Rate limited to 20 requests per minute. See [rate limits and best practices](https://cursor.com/docs/api.md#rate-limits).

### Get Pooled Usage

/organizations/pooled-usage

Retrieve organization-pooled usage: the pool's spend limit, total usage across the organization, and a per-team breakdown. This powers the pooled-usage section of the dashboard. All monetary fields are in cents.

#### Request body

`organizationId` string Required

Public organization ID (for example `org_abc123`). Must match the organization for the Organization API key used to call the endpoint.

#### Response Fields

`pool` object

Pool-level totals for the current contract period:

- `limitCents` number - Pooled spend limit for the organization, in cents
- `usedCents` number - Total pooled usage consumed so far, in cents
- `remainingCents` number - Remaining pooled budget (`limitCents` minus `usedCents`), in cents
- `contractStartDate` string | null - ISO 8601 timestamp marking the start of the current contract period, or `null` when no contract dates are set
- `contractEndDate` string | null - ISO 8601 timestamp marking the end of the current contract period, or `null` when no contract dates are set

`teams` array

Per-team usage breakdown. The sum of every `usedCents` equals `pool.usedCents`. Each object contains:

- `teamId` number - Integer ID of a team linked to the organization
- `usedCents` number - Usage consumed by this team during the current contract period, in cents
- `budgetLimitCents` number | undefined - Per-team budget cap in cents. Present only when a budget is configured for the team.

```bash
curl -X POST https://api.cursor.com/organizations/pooled-usage \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "organizationId": "org_abc123"
  }'
```

**Response:**

```json
{
  "pool": {
    "limitCents": 5000000,
    "usedCents": 1862340,
    "remainingCents": 3137660,
    "contractStartDate": "2026-01-01T00:00:00.000Z",
    "contractEndDate": "2026-12-31T23:59:59.999Z"
  },
  "teams": [
    {
      "teamId": 7,
      "usedCents": 1440100,
      "budgetLimitCents": 2000000
    },
    {
      "teamId": 8,
      "usedCents": 422240
    }
  ]
}
```

### Get Usage Events

/organizations/filtered-usage-events

Retrieve detailed usage events across the teams linked to your organization. This is the organization-wide counterpart to the team [`/teams/filtered-usage-events`](https://cursor.com/docs/account/teams/admin-api.md#get-usage-events-data) endpoint: it returns the same event shape, with each event tagged by its owning `teamId`. Filtering and pagination run in the database, so large organizations page through results without in-memory aggregation.

By default, events from **all** teams in the organization pool are returned. Pass `teamId` or `teamIds` to restrict the response to specific teams.

**Cost Calculation**: Sum the `chargedCents` field across events to reconcile event-level costs with the per-team `usedCents` breakdown from [`/organizations/pooled-usage`](https://cursor.com/docs/account/organizations/organization-admin-api.md#get-pooled-usage). This field includes both the model cost and the Cursor Token Rate (if applicable).

The `cursorTokenFee` field represents the Cursor Token Rate and is only present for teams with Cursor Token Rate enabled. For request-based enterprise accounts, this field may not appear in the response.

#### Request body

`organizationId` string Required

Public organization ID (for example `org_abc123`). Must match the organization for the Organization API key used to call the endpoint.

`teamIds` number\[]

Optional set of integer team IDs to include. Each must belong to the organization. When omitted (and `teamId` is not set), all teams in the organization pool are included.

`teamId` number

Optional single team ID to include. Shorthand for a one-element `teamIds`. Must belong to the organization.

`startDate` number

Start date in epoch milliseconds. This bound is inclusive.

`endDate` number

End date in epoch milliseconds. This bound is inclusive.

`userId` number

Filter by specific user ID.

`email` string

Filter by user email address.

`serviceAccountId` string

Filter by service account ID.

`page` number

Page number (1-indexed). Default: `1`

`pageSize` number

Number of results per page. Default: `10`

#### Response Fields

Each object in `usageEvents` contains the same fields as the team endpoint, plus an owning-team tag:

- `teamId` number - Integer ID of the team that owns this event
- `timestamp` string - Event timestamp in epoch milliseconds (as a string)
- `userEmail` string - Email address of the user who made the request
- `serviceAccountId` string | undefined - ID of the service account that made the request. Omitted for human user events.
- `serviceAccountName` string | undefined - Display name of the service account that made the request. Omitted for human user events.
- `model` string - AI model used for the request
- `kind` string - Billing category (e.g., `Usage-based`, `Included in Business`)
- `maxMode` boolean - Whether the request used max mode
- `requestsCosts` number - Cost in request units
- `isTokenBasedCall` boolean - Whether the request was billed by token usage
- `isChargeable` boolean - Whether this event incurs a charge
- `isHeadless` boolean - Whether this request was made without a connected client (e.g., background agents)
- `tokenUsage` object | undefined - Token usage details (present when `isTokenBasedCall` is `true`):
  - `inputTokens` number - Input tokens consumed
  - `outputTokens` number - Output tokens generated
  - `cacheWriteTokens` number - Tokens written to cache
  - `cacheReadTokens` number - Tokens read from cache
  - `totalCents` number - Total model cost in cents
  - `discountPercentOff` number | undefined - Discount percentage applied, if any
- `chargedCents` number - Total amount charged in cents for this event (model cost + Cursor Token Rate if applicable)
- `cursorTokenFee` number | undefined - The Cursor Token Rate in cents (only present for teams with token rate enabled)

```bash
# Events across all teams in the organization pool
curl -X POST https://api.cursor.com/organizations/filtered-usage-events \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "organizationId": "org_abc123",
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "page": 1,
    "pageSize": 25
  }'

# Events restricted to specific teams
curl -X POST https://api.cursor.com/organizations/filtered-usage-events \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "organizationId": "org_abc123",
    "teamIds": [7, 8],
    "startDate": 1748411762359,
    "endDate": 1751003762359,
    "page": 1,
    "pageSize": 25
  }'
```

**Response:**

```json
{
  "totalUsageEventsCount": 113,
  "pagination": {
    "numPages": 12,
    "currentPage": 1,
    "pageSize": 10,
    "hasNextPage": true,
    "hasPreviousPage": false
  },
  "usageEvents": [
    {
      "teamId": 7,
      "timestamp": "1750979225854",
      "userEmail": "developer@company.com",
      "model": "claude-4.5-sonnet",
      "kind": "Usage-based",
      "maxMode": true,
      "requestsCosts": 5,
      "isTokenBasedCall": true,
      "isChargeable": true,
      "isHeadless": false,
      "tokenUsage": {
        "inputTokens": 126,
        "outputTokens": 450,
        "cacheWriteTokens": 6112,
        "cacheReadTokens": 11964,
        "totalCents": 20.18232
      },
      "chargedCents": 21.36232,
      "cursorTokenFee": 1.18
    },
    {
      "teamId": 8,
      "timestamp": "1750978339901",
      "userEmail": "admin@company.com",
      "model": "claude-4-sonnet-thinking",
      "kind": "Included in Business",
      "maxMode": true,
      "requestsCosts": 1.4,
      "isTokenBasedCall": false,
      "isChargeable": false,
      "isHeadless": false,
      "chargedCents": 8
    }
  ],
  "period": {
    "startDate": 1748411762359,
    "endDate": 1751003762359
  }
}
```

## Organization Groups

Organization groups organize members across teams linked to the same organization. For dashboard setup and group-level controls, see [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md).

- **Authentication**: Organization API key (Basic auth). Read routes require the **`members:*`** scope. Write routes also require **`members:*`**. Keys with **`admin:*`** also work because admin implies members.
- **Group IDs**: Organization group IDs use the `g_` prefix.
- **Pagination**: List routes accept `page` and `pageSize`. Both values must be positive integers.

### List Organization Groups

/organizations/groups

Retrieve organization groups for the organization attached to your API key.

#### Query parameters

`page` number

Page number. Defaults to the first page.

`pageSize` number

Number of groups per page.

```bash
curl -X GET "https://api.cursor.com/organizations/groups?page=1&pageSize=50" \
  -u YOUR_ORGANIZATION_API_KEY:
```

**Response:**

```json
{
  "groups": [
    {
      "id": "g_PDSPmvukpYgZEDXsoNirw3CFhy",
      "name": "Engineering",
      "createdAt": "2026-01-15T10:30:00.000Z",
      "updatedAt": "2026-01-20T14:22:00.000Z"
    },
    {
      "id": "g_kljUvI0ASZORvSEXf9hV0ydcso",
      "name": "Design",
      "createdAt": "2026-01-16T09:00:00.000Z",
      "updatedAt": "2026-01-16T09:00:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalCount": 2,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  }
}
```

### Get Organization Group

/organizations/groups/:groupId

Retrieve one organization group.

#### Parameters

`groupId` string Required

Organization group ID with the `g_` prefix.

```bash
curl -X GET https://api.cursor.com/organizations/groups/g_PDSPmvukpYgZEDXsoNirw3CFhy \
  -u YOUR_ORGANIZATION_API_KEY:
```

**Response:**

```json
{
  "group": {
    "id": "g_PDSPmvukpYgZEDXsoNirw3CFhy",
    "name": "Engineering",
    "createdAt": "2026-01-15T10:30:00.000Z",
    "updatedAt": "2026-01-20T14:22:00.000Z"
  }
}
```

### List Organization Group Members

/organizations/groups/:groupId/members

Retrieve members in an organization group.

#### Parameters

`groupId` string Required

Organization group ID with the `g_` prefix.

#### Query parameters

`page` number

Page number. Defaults to the first page.

`pageSize` number

Number of members per page.

```bash
curl -X GET "https://api.cursor.com/organizations/groups/g_PDSPmvukpYgZEDXsoNirw3CFhy/members?page=1&pageSize=50" \
  -u YOUR_ORGANIZATION_API_KEY:
```

**Response:**

```json
{
  "members": [
    {
      "userId": "user_abc123",
      "name": "Alex Developer",
      "email": "alex@company.com",
      "joinedAt": "2026-01-15T10:30:00.000Z"
    },
    {
      "userId": "user_def456",
      "name": "Sam Engineer",
      "email": "sam@company.com",
      "joinedAt": "2026-01-16T09:15:00.000Z"
    }
  ],
  "pagination": {
    "page": 1,
    "pageSize": 50,
    "totalCount": 2,
    "totalPages": 1,
    "hasNextPage": false,
    "hasPreviousPage": false
  }
}
```

### Add Organization Group Members

/organizations/groups/:groupId/members/bulk-add

Add members to an organization group.

#### Parameters

`groupId` string Required

Organization group ID with the `g_` prefix.

#### Request body

`userIds` string\[] Required

Array of public user IDs with the `user_` prefix. A single request may include up to 100 users.

```bash
curl -X POST https://api.cursor.com/organizations/groups/g_PDSPmvukpYgZEDXsoNirw3CFhy/members/bulk-add \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_abc123", "user_def456"]
  }'
```

**Response:**

```json
{
  "addedCount": 2
}
```

### Remove Organization Group Members

/organizations/groups/:groupId/members/bulk-remove

Remove members from an organization group.

#### Parameters

`groupId` string Required

Organization group ID with the `g_` prefix.

#### Request body

`userIds` string\[] Required

Array of public user IDs with the `user_` prefix. A single request may include up to 100 users.

```bash
curl -X POST https://api.cursor.com/organizations/groups/g_PDSPmvukpYgZEDXsoNirw3CFhy/members/bulk-remove \
  -u YOUR_ORGANIZATION_API_KEY: \
  -H "Content-Type: application/json" \
  -d '{
    "userIds": ["user_def456"]
  }'
```

**Response:**

```json
{
  "removedCount": 1
}
```


---

## Sitemap

[Overview of all docs pages](/llms.txt)
