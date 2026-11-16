---
source_url: https://cursor.com/docs/models/claude-fable-5-2
fetched_at: 2026-11-16T07:30:45.698047+00:00
fetch_method: mintlify_md
---

Claude Fable 5.2 is Anthropic's latest Mythos-class model and replaces [Fable 5.1](https://cursor.com/docs/models/claude-fable-5-1.md). It plans, delegates to subagents, and works through ambiguous, multi-step problems for hours when a task calls for it. Input and output cost 20% less than Fable 5.1.

## Enabling Fable 5.2

Fable 5.2 has the same privacy considerations as other Fable models because of how Anthropic handles data retention. If Privacy Mode is enabled for your account, team, or organization, you'll need to approve Fable 5.2's Data Retention Policy in the Cursor Dashboard before you can use the model. You can view the policy in the [Cursor Dashboard](https://cursor.com/dashboard/restricted_models/claude-fable-5).

For Teams accounts, approving the model policy applies to the entire Team.

For Enterprise accounts, model availability is approved at the Organization level but continues to be controlled at the team and group level in the [Model Access controls](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

Head to [Team Settings](https://cursor.com/dashboard/restricted_models/claude-fable-5) to enable Fable 5.2 for your Team, Organization, or account.

## Limitations

- Same Anthropic data-retention opt-in as other Fable models. Privacy Mode and Enterprise customers need admin approval before use.
- Input and output rates are about 2x [Claude Opus 5.5](https://cursor.com/docs/models/claude-opus-5-5.md).

## Effort and thinking

Fable 5.2 always thinks before it answers. It decides how long to think on its own, so there's no thinking toggle. The effort setting controls depth: low, medium, high, extra high, and max.

Start with high. Fable 5.2's effort levels behave differently from Fable 5.1's, so don't carry over your Fable 5.1 setting. Save extra high and max for your hardest long-running tasks, where the extra time and tokens pay off.

## Data retention

Anthropic's policy for Fable models is described in detail [here](https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) and as follows:

- Retained customer data is being deleted after 30 days, automatically and permanently, unless subject to a safety investigation or legal hold
- Retained customer data is not readable by any person by default
- Retained enterprise data is not being used to train Claude
- Retained customer data is not being shared with other customers

Enabling and using Fable 5.2 does not change your Privacy Mode settings or Cursor's own retention of your data.

Because of how Fable 5.2 handles data, it is off by default in every Team that has Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) enabled *and* for every Enterprise customer, regardless of Cursor Privacy Mode settings.

Fable 5.2 is on by default for every personal or Team account with Cursor Privacy Mode disabled.

For customers on the Enterprise plan or with Cursor Privacy Mode enabled, it requires explicit opt-in and the model won't be available until an admin enables it. Here's what to know before enabling it:

- **Data retention.** When Fable 5.2 is used, regardless of your Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) settings, Anthropic stores agent input and output data to support automated and human harm-prevention processes. This data is not used to train or improve Anthropic's models or products.
- **Opt-in is team-wide.** Enabling Fable 5.2 requires opting in to Anthropic's data retention terms, and this applies to your entire team. Enterprise admins can restrict which user groups are able to use the model with [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

## Automatic fallback to Opus

Fable 5.2 runs with tight security guardrails. When a request trips one of those guardrails, Cursor routes it to Claude Opus automatically so your work continues without an error. You don't need to retry or switch models yourself.

## Tools

Fable 5.2 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Fable 5.2 is a third-party model, so it isn't part of the usage included with Cursor [plans](https://cursor.com/docs/models-and-pricing.md#third-party-models). On The X Subscription it's billed at the rates below from your prepaid credit. On legacy Cursor plans it draws from the **Other Models** pool. All prices are per million tokens.

Fable 5.2 bills at $8 per million input tokens and $40 per million output tokens, down from $10 and $50 on Fable 5.1. Prompt-cache reads are $0.20 per million tokens and cache writes are $10 per million tokens.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
