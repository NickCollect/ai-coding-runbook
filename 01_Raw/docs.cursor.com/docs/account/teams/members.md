---
source_url: https://cursor.com/docs/account/teams/members
fetched_at: 2026-10-19T05:32:42.846064+00:00
fetch_method: mintlify_md
---

# Members, Roles, and Seat Types

Cursor Teams use roles for permissions and seat tiers for usage limits.

## Roles

**Members** are the default role with full access to Cursor's paid features.

- Full access to Cursor's paid features
- No access to billing settings or admin dashboard
- Can see their own usage and remaining included usage

**Admins** control team management and security settings.

- Full access to Cursor's paid features
- Add/remove members, modify roles, set up SSO
- Configure top-ups and the team's monthly additional usage limit
- Access to team analytics

**Unpaid Admins** manage teams without using a paid seat - ideal for IT or finance staff who don't need Cursor access.

- Not billable, no paid Cursor features
- Same administrative capabilities as Admins

Unpaid Admins require at least one paid user on the team.

## Seat Tiers

On [The X Subscription](https://cursor.com/docs/account/teams/pricing.md), Teams offers three paid seat tiers, plus a Free seat. Each paid tier matches the individual plan of the same name in price and weekly usage.

**Premium seats** are for everyday coding agent users.

- $30/user/mo
- Includes the Premium weekly usage pool
- Can be assigned to Members or Admins

**Super seats** are for daily agent users who need more included usage.

- $100/user/mo
- Includes the Super weekly usage pool, 3.75x Premium
- Can be assigned to Members or Admins

**Ultra seats** are for power users running several agents or Automations.

- $200/user/mo
- Includes the Ultra weekly usage pool, 12.5x Premium
- Can be assigned to Members or Admins

**Free seats** are for members who don't need a team usage allowance, including IT, security, or finance admins who manage Cursor without using it.

- $0/user/mo
- No team usage allowance. The member's usage draws from their own personal plan, or the small free allowance if they have none
- Any Member or Admin can hold a Free seat
- Assigned through email invites or the Seat menu, not invite links

Teams created before The X Subscription use **Standard** ($40/user/mo) and **Premium** ($120/user/mo, 5x Standard) seats instead. Those teams keep their seat types until they switch. See [Legacy Teams seats](https://cursor.com/docs/account/teams/pricing.md#legacy-teams-seats).

### Change a seat tier

Admins change a paid user's seat tier from the member context menu, or from the **Seat** menu next to their name under **Members** at [grok.com/dashboard](https://grok.com/dashboard).

Upgrades take effect immediately, and the team's card is charged the pro-rated difference for the rest of the billing period. Downgrades apply at the end of the billing period; until then, the user keeps their current tier, and you can pick it again to cancel the change.

## Role Comparison

| Capability             |                                                    Member                                                    |                                                     Admin                                                    |                                                 Unpaid Admin                                                 |
| ---------------------- | :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| Use Cursor features    |                                                       ✓                                                      |                                                       ✓                                                      |                                                                                                              |
| Invite members         |                                                       ✓                                                      |                                                       ✓                                                      |                                                       ✓                                                      |
| Remove members         |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Change user role       |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Admin dashboard        |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Configure SSO/Security |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Manage Billing         |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| View Analytics         |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Manage Access          |                                                                                                              |                                                       ✓                                                      |                                                       ✓                                                      |
| Set usage controls     | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#what-types-of-spend-limits-are-available) | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#what-types-of-spend-limits-are-available) | ✓ [\*](https://cursor.com/help/account-and-billing/spend-limits.md#what-types-of-spend-limits-are-available) |
| Requires paid seat     |                                                       ✓                                                      |                                                       ✓                                                      |                                                                                                              |

## Managing members

### Add member

Add members in several ways:

1. **Email invitation**

   - Click `Invite Members`
   - Enter email addresses
   - Users receive email invites

2. **Invite link**

   - Click `Invite Members`
   - Copy `Invite Link`
   - Share with team members

3. **SSO**
   - Configure SSO in [admin dashboard](https://cursor.com/docs/account/teams/sso.md)
   - Users auto-join when logging in via SSO email

4. **Domain matching**
   - Teammates with a verified, matching email domain can join your team without an invite
   - Enable this in [team settings](https://cursor.com/dashboard/settings#domain-join)

Invite links have a long expiration date. Anyone with the link can join.
Revoke them regularly, or use [SSO](https://cursor.com/docs/account/teams/sso.md) or [domain restrictions](https://cursor.com/docs/account/teams/members.md#domain-settings) to control access.

### Remove member

Admins can remove members anytime via context menu → "Remove".

**Billing:**

- If a member has used any credits, their seat remains occupied until the end of the billing cycle
- Billing is automatically adjusted with pro-rated credit for removed members applied to the next invoice

Removing a member removes their access to the team. It does not delete their Cursor account or the data attached to that account.

- When an entire team is deleted, all associated data is permanently deleted
- There must be at least one Admin and one paid member on the team at all times

### Change role

Admins can change roles for other members by clicking the context menu and then use the "Change role" option.

There must be at least one Admin, and one paid member on the team at all times.

On a team that belongs to an [Organization](https://cursor.com/docs/enterprise/organizations.md), an org admin who is also on the team shows their team role, so you can change their role or remove them like any other member. Turn on **Show org admins** to also list org admins who aren't on the team. In that view, every org admin shows as a read-only **Org Admin**. Turn the switch off to edit their team role.

## Domain settings

Admins can configure two domain-based controls in [team settings](https://cursor.com/dashboard/settings#domain-join). Both require at least one verified domain and are available on Team and Enterprise plans for teams not using SCIM provisioning.

### Domain matching

When enabled, anyone with a verified, matching email domain can join your team directly from the dashboard, no invite needed. This is useful for letting teammates self-serve without admins manually sending invitations.

### Restrict invites to verified domains

When enabled, team members can only invite users whose email addresses match a verified domain. Invitations to email addresses outside your verified domains are blocked.

This prevents accidental or unauthorized additions and gives admins tighter control over who joins the team.

These settings are for teams that don't use SCIM provisioning. If your team uses SCIM, member management is handled through your identity provider.

## Security & SSO

SAML 2.0 Single Sign-On (SSO) is available on Team plans. Key features include:

- Configure SSO connections ([learn more](https://cursor.com/docs/account/teams/sso.md))
- Set up domain verification
- Automatic user enrollment
- SSO enforcement options
- Identity provider integration (Okta, etc)

Domain verification is required to enable SSO.

## Usage Controls

Access usage settings to:

- Buy prepaid credit and turn on Auto Top-up
- Set the team's monthly additional usage limit, the default per-member limit, and per-member overrides
- Set admin-only modifications
- Monitor team-wide usage

On legacy Teams plans, the same settings cover on-demand usage and the team spend limit. See [Spend limits](https://cursor.com/help/account-and-billing/spend-limits.md).

## Billing

When adding team members:

- Each member or admin adds a billable seat (see [pricing](https://cursor.com/pricing))
- New members are charged pro-rata for their remaining time in the billing period
- Unpaid admin seats aren't counted

Mid-month additions charge only for days used. The seat price depends on the user's seat tier. When removing members who have used credits, their seat remains occupied until the end of the billing cycle.

Role changes (e.g., Admin to Unpaid Admin) adjust billing from the change date. Choose monthly or yearly billing.

Monthly/yearly renewal occurs on your original signup date, regardless of member changes.

### Switch to Yearly billing

Save **20%** by switching from monthly to yearly:

1. Go to [cursor.com/dashboard/billing](https://cursor.com/dashboard/billing)
2. Click **Upgrade Now** on the green banner at the top

There is no way to switch from yearly to monthly mid-plan. You'll need to cancel, wait for the year to end, then re-subscribe on a monthly plan.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
