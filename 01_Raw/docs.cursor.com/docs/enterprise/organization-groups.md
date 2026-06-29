---
source_url: https://cursor.com/docs/enterprise/organization-groups
fetched_at: 2026-06-29T05:25:13.960533+00:00
fetch_method: mintlify_md
---

# Organization Groups

Organization Groups let Enterprise admins organize users across teams in the same Cursor Organization. Use them for cohorts such as Engineering, Contractors, Executives, or Pilot Users when the same set of people needs shared settings even if they belong to different teams.

Organization Groups are separate from [Billing Groups](https://cursor.com/docs/account/enterprise/billing-groups.md). Billing Groups help a team report and attribute spend. Organization Groups manage organization-level cohorts and the settings that apply to them.

## When to use Organization Groups

Use Organization Groups when you want to:

- Apply model access or usage controls to a cross-team cohort
- Manage a group from your identity provider through SCIM
- Give a pilot group access to a new model or setting before enabling it broadly
- Keep team defaults strict while allowing specific users more permissive settings
- Manage group membership through the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups)

## Create a group

In the dashboard, open your Organization and go to **Groups**.

You can create:

- **Manual groups**: Cursor admins add, remove, import, and move members in the dashboard or through the Organization API.
- **SCIM-synced groups**: Cursor maps the Organization Group to a directory group from your identity provider. Membership is managed in your identity provider and synced into Cursor.

For SCIM-synced groups, manage membership in your identity provider. Cursor
shows the synced members but disables manual membership changes that would be
overwritten by the next sync.

## Manage members

Open a group and select **Members** to view and manage membership.

For manual groups, admins can:

- Add existing Organization members
- Import members by CSV
- Move members to another Organization Group
- Remove members
- Search and sort the member list

SCIM-synced groups are read-only for membership. Admins can still manage Cursor-owned settings for the group, such as spend limits and model access.

## Configure group settings

Open a group and select **Settings** to manage group-level controls.

### Spend limits

Organization Groups can set per-user monthly spend limits. When a user belongs to multiple groups or has team-level limits, Cursor applies the most permissive applicable limit.

For example, if a team default is stricter and an Organization Group has a higher limit, the group limit applies to that user. If a group limit is lower than an already more permissive team setting, it does not make the user's access stricter.

### Model access

Use the **Models** tab to configure model access for a group. This is useful for controlled rollouts, approvals, or giving specific cohorts access to models that are not enabled for everyone.

Group model settings combine with team settings using a permissive model: set restrictive defaults at the team level, then use Organization Groups to widen access for selected cohorts.

### Auto-run and Smart Auto

Organization Groups can also carry group-level agent and model-routing controls, including auto-run and Smart Auto settings where available.

Because groups can include users from multiple teams, team-level restrictions still matter. If a user's team blocks a model required by a group setting, that team-level restriction can affect the user's experience.

## Organization Groups and SCIM

SCIM lets your identity provider control who belongs to a group. This is the recommended approach when the group mirrors an existing department, role, or access cohort in your IdP.

Before mapping SCIM groups, make sure [SCIM provisioning](https://cursor.com/docs/account/teams/scim.md) is configured for your Organization. Then create or edit an Organization Group and connect it to the matching directory group.

## API access

You can list groups, read members, and add or remove members through the [Organization API](https://cursor.com/docs/account/organizations/organization-admin-api.md#organization-groups).

Organization Group API routes use Organization API keys and group IDs with the `g_` prefix.

### Organization Groups are available on Enterprise

Contact our team to learn more about organization-level administration.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
