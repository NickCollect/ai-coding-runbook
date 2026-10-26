---
source_url: https://cursor.com/docs/account/pricing/legacy-cursor-plans
fetched_at: 2026-10-26T05:39:58.568016+00:00
fetch_method: mintlify_md
---

# Legacy Cursor plans

Legacy Cursor plans are the plans Cursor sold before [The X Subscription](https://cursor.com/docs/models-and-pricing.md): Hobby, Start, Pro, Pro+, Ultra, and Teams with Standard and Premium seats. They keep working as they are. New customers start on The X Subscription, and this page is for anyone still on a legacy plan who wants to know how it works and how it compares.

Switching to The X Subscription is optional and permanent. Your legacy plan, price, and features continue unless you change or cancel. See [What is The X Subscription?](https://cursor.com/help/the-x-subscription/overview.md) for eligibility and how to switch.

## Which plans are legacy Cursor plans?

| Legacy plan            | Price                  | Comparable plan on The X Subscription |
| :--------------------- | :--------------------- | :------------------------------------ |
| **Hobby**              | Free                   | Free                                  |
| **Start** (India only) | ₹649/mo, tax inclusive | Plus ($8/mo)                          |
| **Pro**                | $20/mo                 | Premium ($30/mo)                      |
| **Pro+**               | $60/mo                 | Super ($100/mo)                       |
| **Ultra**              | $200/mo                | Ultra ($200/mo)                       |
| **Teams Standard**     | $40/user/mo            | Teams, Premium seat ($30/user/mo)     |
| **Teams Premium**      | $120/user/mo           | Teams, Super seat ($100/user/mo)      |

Comparable means the closest tier, not an identical one. Each paid plan on The X Subscription includes at least twice as much coding usage with Cursor models as the legacy plan it replaces, and it adds Grok and X benefits. It also drops the included third-party model allowance; third-party models are billed separately. Compare both before you switch. Start to Plus is an analogy only: when a paid Cursor account switches, the unify flow offers Premium and above, and Pro, Pro+, Teams Standard, and Teams Premium default to the tiers shown.

Request-based plans, where usage was counted in requests rather than tokens, are an older generation still. See [Request-based pricing (legacy)](https://cursor.com/docs/account/pricing/request-based-legacy.md).

## How legacy plans differ from The X Subscription

|                          | Legacy Cursor plans                                                   | The X Subscription                                                              |
| :----------------------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| Included usage           | Two monthly pools: **Cursor Models** and **Other Models**             | One weekly pool for Cursor models, shared with Grok                             |
| Usage reset              | Monthly, with your billing cycle                                      | Weekly                                                                          |
| Third-party models       | Included through the Other Models pool on Pro, Pro+, Ultra, and Teams | Not included. Billed at API list price from prepaid credit on Premium and above |
| Extra usage              | **On-demand usage**, billed in arrears each month                     | **Top-ups** that add prepaid credit, with optional Auto Top-up                  |
| Spend controls           | On-demand spend limit                                                 | Monthly additional usage limit (spending cap)                                   |
| Grok and X               | Not included                                                          | Grok apps and X Premium benefits included                                       |
| Where you manage billing | [cursor.com/dashboard/billing](https://cursor.com/dashboard/billing)  | [grok.com/dashboard/billing](https://grok.com/dashboard/billing)                |

## Usage pools on legacy plans

Legacy plans split included usage into two pools. Both reset with your monthly billing cycle, and both are visible in your editor settings and on your [usage dashboard](https://cursor.com/dashboard/usage).

- **Cursor Models.** Included usage for Grok 4.7, Grok 4.6, Grok 4.5, and Composer 2.5. Every legacy plan includes this pool.
- **Other Models.** Included usage for third-party models, drawn down at each model's API price. Pro, Pro+, Ultra, and Teams include this pool. Start and Hobby don't.

Model choice affects how fast you use the pool. When you select a third-party model, or [Auto](https://cursor.com/docs/cursor-router.md) routes to one, the request draws from Other Models at that model's list price. Named third-party models in [subagents](https://cursor.com/docs/subagents.md#parent-model-and-usage-pools) draw from Other Models too, even when the parent chat is on Auto, Grok, or Composer.

## On-demand usage on legacy plans

On-demand usage lets you keep working after an included pool runs out. It's billed monthly in arrears at the same per-model rates as included usage, with no change in quality or speed.

- **Individual plans (Pro, Pro+, Ultra).** Off until you turn it on under **Spending** at [cursor.com/dashboard/spending](https://cursor.com/dashboard/spending). Set a monthly spend limit there.
- **Teams.** On by default. Admins can turn it off or set a team-wide spend limit from the team dashboard. Eligible third-party requests also carry the [Cursor Token Rate](https://cursor.com/docs/models-and-pricing.md#cursor-token-rate). The third-party models listed there are excluded.
- **Start and Hobby.** Not available. AI features pause until the pool resets.

See [Usage-based charges](https://cursor.com/help/account-and-billing/overages.md) and [Spend limits](https://cursor.com/help/account-and-billing/spend-limits.md) for how limits and credits behave.

## Plan details

### Hobby

Hobby is the free legacy plan. It includes Agent, Chat, and Tab with limited usage, and it doesn't include Cloud Agents, Bugbot, or Origin.

### Start (India only)

Start costs ₹649 per month, tax inclusive, billed monthly in INR with UPI, credit card, or debit card. It includes the Cursor Models pool, [Cloud Agents](https://cursor.com/docs/cloud-agent.md), [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md), plugins, MCP servers, hooks, and skills.

On Start, Grok 4.7, Grok 4.6, and Grok 4.5 run at a fixed medium effort level in standard speed, and Composer 2.5 runs in standard speed. You can't change effort levels or turn on Fast mode. Start doesn't include the Other Models pool, on-demand usage, Bugbot, Auto, Automations, or the Cursor SDK. Start can only be purchased while your account is on the free plan, so you can't switch back to it directly from another paid plan. See [Cursor Start](https://cursor.com/help/account-and-billing/cursor-start.md) for eligibility and payments.

### Pro, Pro+, and Ultra

Pro, Pro+, and Ultra include both usage pools, unlimited Tab completions, Bugbot, Cloud Agents, Automations, Origin, and the Cursor SDK. Pro+ and Ultra include more of each pool than Pro. Fast mode and Grok effort levels are available on all three.

Upgrades between these plans take effect immediately; downgrades apply at the end of the billing period. Manage them at [cursor.com/dashboard/billing](https://cursor.com/dashboard/billing). See [Pricing and plans](https://cursor.com/help/account-and-billing/pricing.md#how-do-i-change-plans-on-a-legacy-cursor-plan).

### Teams Standard and Premium

Legacy Teams seats come in two types. Standard ($40/user/mo) includes the standard Teams allowance of both pools, and Premium ($120/user/mo) includes 5x the Standard allowance. Usage is allocated per seat, doesn't transfer between members, and resets with the team billing cycle. Existing teams can still add seats or change a seat's type without switching. See [Team pricing](https://cursor.com/docs/account/teams/pricing.md#legacy-teams-seats).

## What changes when you switch

- Your eligible Cursor and Grok subscriptions are cancelled at checkout and you receive a prorated refund for unused time. Grok Bot subscriptions bought in the iOS or Android app are cancelled and refunded for unused time too. Only a Cursor subscription billed through the Apple App Store must be cancelled by you in your iPhone or iPad Settings.
- Any on-demand usage not yet invoiced is billed in one final invoice when you switch; the switch waits until it's paid.
- If your Grok account has more Grok Bot data than can be transferred yet, Unify asks you to try again later.
- Your usage moves from two monthly pools to one weekly pool for Cursor models, shared with Grok.
- Third-party models stop being included. They stay available in Cursor on Premium and above, billed at API list price from your prepaid credit.
- On-demand usage and its spend limit are replaced by top-ups and a monthly additional usage limit.
- Billing moves from cursor.com to [grok.com/dashboard/billing](https://grok.com/dashboard/billing).

Start with [What is The X Subscription?](https://cursor.com/help/the-x-subscription/overview.md), then [cursor.com/unify](https://cursor.com/unify) for individual plans or [cursor.com/unify/team](https://cursor.com/unify/team) for teams.

## Related

- [Models & Pricing](https://cursor.com/docs/models-and-pricing.md)
- [Team pricing](https://cursor.com/docs/account/teams/pricing.md)
- [Pricing and plans](https://cursor.com/help/account-and-billing/pricing.md)
- [Usage and limits](https://cursor.com/help/models-and-usage/usage-limits.md)
- [Request-based pricing (legacy)](https://cursor.com/docs/account/pricing/request-based-legacy.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
