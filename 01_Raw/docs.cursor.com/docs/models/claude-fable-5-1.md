---
source_url: https://cursor.com/docs/models/claude-fable-5-1
fetched_at: 2026-09-07T05:31:29.474291+00:00
fetch_method: mintlify_md
---

Claude Fable 5.1 is Anthropic's latest Mythos-class model and replaces [Fable 5](https://cursor.com/docs/models/claude-fable-5.md). It is built for long-running, complex, and asynchronous coding and knowledge work. Input and output rates match Fable 5. Prompt-cache reads are 75% cheaper.

## Enabling Fable 5.1

Fable 5.1 has the same privacy considerations as other Fable models because of how Anthropic handles data retention. If Privacy Mode is enabled for your account, team, or organization, you will need to approve Fable 5.1's Data Retention Policy in the Cursor Dashboard before you can use the model. You can view the policy in the [Cursor Dashboard](https://cursor.com/dashboard/restricted_models/claude-fable-5-1).

For Teams accounts, approving the model policy applies to the entire Team.

For Enterprise accounts, model availability is approved at the Organization level but continues to be controlled at the team and group level in the [Model Access controls](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

Head to [Team Settings](https://cursor.com/dashboard/restricted_models/claude-fable-5-1) to enable Fable 5.1 for your Team, Organization, or account.

## Strengths

- Cleaner communication than Fable 5 on long-running agent sessions.
- Built for autonomous, multi-step work. It holds intent across long sessions and drives tasks to completion with fewer check-ins.
- Deep reasoning. A thinking variant is available for problems that reward extra deliberation.

## Limitations

- Same Anthropic data-retention opt-in as other Fable models. Privacy Mode and Enterprise customers need admin approval before use.
- Input and output rates stay at about twice [Claude Opus 5](https://cursor.com/docs/models/claude-opus-5.md).

## Data retention

Anthropic's policy for Fable models is described in detail [here](https://trust.anthropic.com/resources?s=7ksqkied5hn0pocsj206m\&name=%5Banthropic%5D-security-and-privacy-design-of-anthropic-data-retention-and-review) and as follows:

- Retained customer data is being deleted after 30 days, automatically and permanently, unless subject to a safety investigation or legal hold
- Retained customer data is not readable by any person by default
- Retained enterprise data is not being used to train Claude
- Retained customer data is not being shared with other customers

Enabling and using Fable 5.1 does not change your Privacy Mode settings or Cursor's own retention of your data.

Because of how Fable 5.1 handles data, it is off by default in every Team that has Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) enabled *and* for every Enterprise customer, regardless of Cursor Privacy Mode settings.

Fable 5.1 is on by default for every individual customer or Team account for which Cursor Privacy Mode is disabled.

For customers on the Enterprise plan or with Cursor Privacy Mode enabled, it requires explicit opt-in and the model won't be available until an admin explicitly enables it. Here's what to know before enabling it:

- **Data retention.** When Fable 5.1 is used, regardless of your Cursor [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) settings, Anthropic stores agent input and output data to support automated and human harm-prevention processes. This data is not used to train or improve Anthropic's models or products.
- **Opt-in is team-wide.** Enabling Fable 5.1 requires opting in to Anthropic's data retention terms, and this applies to your entire team. Enterprise admins can restrict which user groups are able to use the model with [model access control](https://cursor.com/docs/enterprise/model-and-integration-management.md#model-access-control).

## Automatic fallback to Opus

Fable 5.1 runs with tight security guardrails. When a request trips one of those guardrails, Cursor routes it to Claude Opus automatically so your work continues without an error. You don't need to retry or switch models yourself.

## Tools

Fable 5.1 has access to all agent tools when used with Cursor including:

Learn more about [how tools work](https://cursor.com/docs/agent/overview.md#tools) and [tool calling fundamentals](https://cursor.com/learn/tool-calling.md).

## Pricing

Cursor [plans](https://cursor.com/docs/models-and-pricing.md) include two usage pools. Fable 5.1 draws from the third-party **Other Models** pool, which charges at the rates below. All prices are per million tokens.

Fable 5.1 bills at $10 per million input tokens and $50 per million output tokens, the same as Fable 5. Prompt-cache reads are $0.25 per million tokens, 75% below Fable 5's $1.00 cache-read rate. Cache writes stay at $12.50 per million tokens.

Fable 5.1 supports a thinking variant for deeper reasoning. We recommend the high thinking variant for the strongest results.


---

## Sitemap

[Overview of all docs pages](/llms.txt)
