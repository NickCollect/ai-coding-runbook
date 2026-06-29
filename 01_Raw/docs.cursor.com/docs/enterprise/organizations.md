---
source_url: https://cursor.com/docs/enterprise/organizations
fetched_at: 2026-06-29T05:25:13.965464+00:00
fetch_method: mintlify_md
---

# Organizations

Organizations are the top-level container for Enterprise customers. They sit above teams and give you one place to manage shared identity, administration, and organization-wide settings.

## Organizations model

Organizations can include multiple teams, created around departments, business units, regions, or roles. Each team defines its own membership, roles, usage views, privacy settings, usage controls, and other team-level settings. Organizations sit above those teams and provide shared identity, administration, and org-wide settings.

Each Organization has a default team that acts as a stable home team for login and routing.

Users can belong to multiple teams in the same Organization, and their role can differ by team. For example, one person can be an admin in one team, a member in another, and not belong to a third team.

## Identity model

Organizations support org-level SSO with your identity provider integration. This is the recommended model when you want one login setup across the company.

Team-level SSO is still supported for team-specific identity requirements. Organizations add a shared identity layer, but they do not remove team-level SSO options.

## Usage and contract boundaries

Usage can be tracked at the team level for day-to-day reporting. With organization-pooled billing, teams can draw from a shared committed pool.

See [Pooled usage](https://cursor.com/docs/enterprise/pooled-usage.md) for details.

## Groups

Organization Groups help you organize users across teams. Organization Groups are useful for org-wide cohorts such as Engineering, Contractors, or Pilot Users. Members can belong to multiple teams, so organization admins can apply settings to the same cohort regardless of each user's team membership.

See [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md) for setup, SCIM mapping, membership management, and group-level controls.

## How limits and permissions combine

Users may have different effective settings, such as usage limits and allowed models, across organization-level groups and team-level directory groups. Cursor reconciles these settings with a "most permissive wins" model.

For example, if a user is in an organization-level group and a team, Cursor uses the highest spend limit setting between the two.

| Layer                 | What it controls                         | How multiple sources combine                                                                 |
| --------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| Team default          | Baseline per-user spend caps             | Used only when nothing more specific is set                                                  |
| Per-user on team      | Override for one user                    | Wins over team defaults and directory group settings                                         |
| Directory Group(s)    | SCIM-synced spend caps and team policies | Spend limits use the highest value; policy behavior is generally most permissive             |
| Organization Group(s) | Org-level allowances and policy          | Across org groups, highest value applies; compared with team baseline, highest value applies |

When choosing between team-level settings and Organization Group-level settings, use a bottom-up model from least permissive to most permissive. Set the strictest defaults at the team level, then use Organization Groups to give specific user cohorts more permissive settings.

## Roles

Organizations add org-level administration on top of team-level roles. Org admins can manage organization settings, organization membership, shared identity configuration, and view teams in the Organization. Team admins and team owners manage settings and members for their own teams.

Team admin access does not automatically grant org admin access. Users can also have different roles at each layer. For example, a user can be an org admin while only being a member of specific teams.

## Organization API

For org-level automation, use the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md).

## Related docs

- [Enterprise overview](https://cursor.com/docs/enterprise.md)
- [Organization Groups](https://cursor.com/docs/enterprise/organization-groups.md)
- [Identity & access management](https://cursor.com/docs/enterprise/identity-and-access-management.md)
- [SCIM](https://cursor.com/docs/account/teams/scim.md)
- [Admin API](https://cursor.com/docs/account/teams/admin-api.md)
- [Billing groups](https://cursor.com/docs/account/enterprise/billing-groups.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
