---
source_url: https://cursor.com/docs/api/origin/grants-api
fetched_at: 2026-09-14T05:36:05.628516+00:00
title: "Origin Grants API | Cursor Docs"
---

API

# Origin Grants API

Origin is in Early Beta and subject to change.

A grant binds one principal to one repository or namespace with one permission. The grants API lists the grants held directly on a resource, upserts the grant a principal holds, and deletes it, so access changes can be scripted and reviewed as code. Writes reuse the access checks behind the Codebase permissions UI and record the same `repository.access_changed` and `namespace.access_changed` audit events.

The six endpoints live in the [Grants](https://cursor.com/docs/api/origin#grants) group of the Origin API reference: [List Repository Grants](https://cursor.com/docs/api/origin#list-repository-grants), [Upsert Repository Grant](https://cursor.com/docs/api/origin#upsert-repository-grant), [Delete Repository Grant](https://cursor.com/docs/api/origin#delete-repository-grant), [List Namespace Grants](https://cursor.com/docs/api/origin#list-namespace-grants), [Upsert Namespace Grant](https://cursor.com/docs/api/origin#upsert-namespace-grant), and [Delete Namespace Grant](https://cursor.com/docs/api/origin#delete-namespace-grant). They share the [Origin API](https://cursor.com/docs/api/origin) base URL, [authentication](https://cursor.com/docs/api/origin#authentication), [pagination](https://cursor.com/docs/api/origin#pagination), and [error model](https://cursor.com/docs/api/origin#errors). This page covers the concepts behind them.

## [Principals](#principals)

Each grant names exactly one principal.

| Principal | Field | Identifies |
| --- | --- | --- |
| `user` | `user.id` | A Cursor user, by the encoded `user_…` id the organization API uses. |
| `group` | `group.id` | A Cursor organization group, by its public `grp_…` id. |
| `teamGroup` | `teamGroup.kind` | One of the owning team's built-in groups: `members` (every team member) or `admins` (team admins). |

A team-group grant is the floor every member of that built-in group holds on the resource. On a namespace it is the team's namespace floor. On a repository it is the team's per-repository override, and deleting it returns the repository to the namespace floor.

Users and groups must belong to the owner's organization. The write endpoints answer a user or group that does not exist exactly like one outside the organization, so a response never confirms that a principal exists. List responses omit principals that no longer resolve to an active user, group, or the owning team.

## [Permissions](#permissions)

Repository grants and namespace grants use different permission ladders. Both map to the presets the Codebase permissions UI offers.

| Resource | `permission` values |
| --- | --- |
| Repository | `read`, `write`, `admin` |
| Namespace | `PERMISSION_READ`, `PERMISSION_CONTRIBUTOR`, `PERMISSION_WRITE`, `PERMISSION_ADMIN` |

`PERMISSION_READ`, `PERMISSION_CONTRIBUTOR`, and `PERMISSION_WRITE` grant that level on the namespace's internal repositories. `PERMISSION_ADMIN` administers the namespace itself.

List responses report `custom` (repository) or `PERMISSION_CUSTOM` (namespace) for a grant that holds a custom policy. The upsert endpoints reject those values with `InvalidArgument` (HTTP 400); custom policies are outside the grants API.

## [Scopes](#scopes)

Four scopes cover the grants API, all of them listed in [Scopes](https://cursor.com/docs/api/origin#scopes): `repository:settings:read` and `repository:settings:write` for repository grants, `namespace:settings:read` and `namespace:settings:write` for namespace grants.

App installations can hold all four, so a robot calls the grants API with an installation access token. User access tokens work too. Requesting a `:write` scope also grants the matching `:read` scope. List endpoints cost 1 point and writes cost 5 against the budget in [Rate limits](https://cursor.com/docs/api/origin#rate-limits).

## [Upserts and deletes](#upserts-and-deletes)

Upsert is a `POST` that creates or replaces the grant a principal holds on the resource. Each principal holds one grant per resource, so repeating a request leaves the same grant in place and a different `permission` replaces the earlier one. Delete names the principal in the request body and returns `204 No Content`.

A namespace always keeps at least one admin. An upsert or delete that would leave the owner without one returns `FailedPrecondition` (HTTP 400).

English

- English
- 简体中文
- Русский
- 日本語
- Português
- Español
