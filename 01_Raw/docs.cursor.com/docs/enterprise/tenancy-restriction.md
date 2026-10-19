---
source_url: https://cursor.com/docs/enterprise/tenancy-restriction
fetched_at: 2026-10-19T05:32:44.515515+00:00
fetch_method: mintlify_md
---

# Tenancy Restriction

Your network can limit which Cursor organizations and teams a request may use. Do that by adding one HTTP header on traffic to Cursor. Cursor never sets this header, and the dashboard has no switch for it. If the header is absent, Cursor applies no restriction from this mechanism.

Cursor checks the header on the request in front of it. The value is not stored on the token. The same account, used off this network, is not limited by it.

For proxy, firewall, and encryption setup, see [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md). Device policies such as [Allowed Team IDs](https://cursor.com/docs/enterprise/identity-and-access-management.md#allowed-team-ids) are separate. This header is the network control.

## How to send the header

| Field | Value                                                                                                       |
| ----- | ----------------------------------------------------------------------------------------------------------- |
| Name  | `x-cursor-allowed-tenants`                                                                                  |
| Value | Plain ASCII, in the [format](https://cursor.com/docs/enterprise/tenancy-restriction.md#header-format) below |

Put the header on requests to Cursor's API (`api2.cursor.sh`, including sign-in) and to `cursor.com`. The desktop app, the CLI, and API keys talk to the API. The website talks to `cursor.com`. A header that reaches only the browser page does not cover the app or the CLI.

Add it on the network path, after the client has built the request. A TLS-terminating proxy is the reliable place. A managed-browser policy that makes the app itself send the header can fail the desktop sign-in check in the browser, before Cursor reads the header.

### Copy the ids

Copy each team id and organization id you want to allow. [Find the ids](https://cursor.com/docs/enterprise/tenancy-restriction.md#find-the-ids) below. Use the numeric ids, not names or slugs.

### Build one header value

Start with `v1.` and list the ids. An example that allows two organizations and one team is `v1.orgs=1001,1002;teams=70`.

### Inject the header on the proxy

Add `x-cursor-allowed-tenants` to requests for `api2.cursor.sh` and `cursor.com` after the client builds them.

You may send up to eight copies. Send them as repeated headers, or join them in one value with a comma immediately before the next `v1.`. Every copy must allow the request. A second proxy can only narrow the set.

A blank value is refused. Omitting the header is not. A value that breaks the format is refused too. Cursor does not treat a bad header as no restriction.

## Header format

One copy looks like this:

```text
v1.orgs=<org ids>;teams=<team ids>
```

Example: `v1.orgs=1001,1002;teams=70`

- The value starts with `v1.`. Any other version is refused.
- The only keys are `orgs` and `teams`. Either list may be left out. At least one list must contain an id. Each key may appear once.
- Ids in a list are separated by commas. Spaces around an id, a key, or `=` are ignored.
- An organization id is digits only: 1 to 19 digits, greater than zero, and at most `9223372036854775807`.
- A team id is digits only, greater than zero, and at most `9007199254740991`.
- Names, email addresses, domains, plus or minus signs, and decimals are refused. So are `0`, an empty list (`v1.orgs=`), and a repeated key (`v1.orgs=1001;orgs=1002`).
- One copy may list at most 32 ids, counting organizations and teams together, and may be at most 1024 bytes.

Teams only: `v1.teams=70`

Organizations only: `v1.orgs=1001,1002`

Two copies, joined: `v1.orgs=1001,1002, v1.teams=70`. The account must match organization `1001` or `1002`, and must also match team `70`.

## What the ids mean

`orgs` are Cursor organization ids. `teams` are Cursor team ids. Both are the numeric ids, not display names.

For a person, including a user API key, each copy allows the account when any one of these is true:

- They have an active membership in a listed team.
- They have a direct membership in a listed organization.
- They belong to a team that is linked to a listed organization.

Every copy must allow them. Inside one copy, any one match is enough.

If the Cursor client also sends `x-cursor-team-id`, that team must itself be listed, or linked to a listed organization, on every copy. Membership in an allowed team does not let the request act as a team that is not allowed. When the client has not chosen a team, and the account's current team is outside the list, Cursor drops that team from the request and continues with an allowed membership.

A team API key is allowed when its team is listed, or linked to a listed organization, on every copy. An organization API key is allowed only when its organization id is in `orgs` on every copy. A request that carries the header but no account is refused.

## Find the ids

### Copy the team id

On the dashboard, open that team's [Team settings](https://cursor.com/dashboard/team-settings). In the team profile, the row labeled **Team ID** is the number for `teams`. **Copy ID** copies it. On the organization overview, each team's actions menu has **Copy team ID**, which copies the same number. The team name and the slug are not the id.

### Read the organization id from the audit log

`orgs` needs the numeric organization id. The dashboard does not show that number in settings. The Organization ID on the organization overview is a public id: it starts with `org_` and then letters and digits. The header refuses that value. In the [audit log](https://cursor.com/dashboard/audit-log), open an event. If it lists Organization ID as a positive number, that number is the id for `orgs`. A missing field means that event did not record one. See [Accessing audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#accessing-audit-logs).

## What the client sees

When the account is outside the list, Cursor denies the request. The error key is `tenant_restriction_violation`. The message names the restriction and repeats the numeric ids from the header. Cursor does not look up names.

For `v1.orgs=1001,1002;teams=70` the message is:

> This network restricts Cursor to specific organizations. Your account is not a member of an organization or team allowed on this network (allowed org ids: 1001, 1002; team ids: 70). Sign in with an allowed account, or contact your network administrator.

If only one list was sent, only that list appears in the parentheses. A header that was refused as malformed uses the same two sentences, without the parentheses.

### On cursor.com

The person gets a page titled "This network restricts Cursor to specific organizations," the same allowed-ids sentence, the line "Sign in with your work account, or contact your network administrator," and a **Switch account** button.

A session check returns HTTP 403 with the response header `x-cursor-policy-violation: tenant_restriction_violation` and a JSON body whose `error` is `tenant_restriction_violation` and whose `message` is the text above.

### API calls

An API call is permission denied. The error is `ERROR_TENANT_RESTRICTION_VIOLATION`, the title is "Restricted network," and the detail is the message above. It is not a retry. When the lists parsed, the response also includes `x-cursor-tenant-allowed-orgs` and `x-cursor-tenant-allowed-teams`, each a comma-separated list of those same ids.

### Sign-in and refresh

Sign-in and refresh use the same error key:

- `POST /auth/poll` returns HTTP 403 with `{ "error": "tenant_restriction_violation", "message": "<the message>" }`. Cursor cancels that login.
- `POST /oauth/token` returns empty tokens, `shouldLogout: true`, the same `error`, and the same `message`. The status is HTTP 200. The sign-out signal is `shouldLogout`.
- `POST /exchange_user_api_key` returns HTTP 403 with the same `error` and `message`.

### Desktop app

cursor.com shows the page and session-check body above. The desktop app does not yet display this error. A blocked sign-in can stay on the waiting screen, and a blocked refresh signs the user out without the explanation.

## Related docs

- [Network configuration](https://cursor.com/docs/enterprise/network-configuration.md)
- [Identity and access](https://cursor.com/docs/enterprise/identity-and-access-management.md)
- [Organizations](https://cursor.com/docs/enterprise/organizations.md)
- [Audit logs](https://cursor.com/docs/enterprise/compliance-and-monitoring.md#accessing-audit-logs)
- [Security and privacy hardening](https://cursor.com/docs/enterprise/security-hardening.md)

### Need help restricting Cursor on your network?

Contact our team for deployment assistance and priority support.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
