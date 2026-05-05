---
source_url: https://cursor.com/docs/models-and-pricing
---

# Models & Pricing

Cursor supports all frontier coding models from OpenAI, Anthropic, Google, and more. Every individual plan includes two usage pools so you can pick the right balance of intelligence, speed, and cost.

## Usage pools

There are two separate usage pools for individual plans, each resetting with your monthly billing cycle:

- **Auto + Composer**: Significantly more included usage when Auto or Composer 2 is selected. Designed for everyday agentic coding at a lower cost.
- **API**: Charged at the model's API price. Individual plans include at least $20 of API usage each month (more on higher tiers) with the option to pay for additional usage as needed.

Both pools are visible in your editor settings and on your [usage dashboard](https://cursor.com/dashboard/usage).

## Auto + Composer pool

Auto allows Cursor to select models that balance intelligence, cost efficiency, and reliability. It is useful for everyday tasks.

### Auto pricing

| Token type          | Price per 1M tokens |
| :------------------ | :------------------ |
| Input + Cache Write | $1.25               |
| Output              | $6.00               |
| Cache Read          | $0.25               |

### Composer pricing

Composer 2 is Cursor's own model, trained to be highly capable for agentic coding. Both Auto and Composer 2 draw from this pool.

## API pool

When you select a specific model (or use Premium routing), usage is drawn from the API pool at that model's API rate.

### Model pricing

All prices are per million tokens, sourced from each provider's API pricing:

| Model                                                                                         | Provider  | Input | Cache write | Cache read | Output | Notes                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------- | --------- | ----- | ----------- | ---------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Claude 4 Sonnet](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Thinking variant counts as 2 requests in legacy pricing                                                                                                                                                                                                                                                                    |
| [Claude 4 Sonnet 1M](https://www.anthropic.com/claude/sonnet)                                 | Anthropic | $6    | $7.5        | $0.6       | $22.5  | Hidden by default; Thinking variant counts as 2 requests in legacy pricing; This model can be very expensive due to the large context window; The cost is 2x when the input exceeds 200k tokens                                                                                                                                               |
| [Claude 4.5 Haiku](https://www.anthropic.com/claude/haiku)                                    | Anthropic | $1    | $1.25       | $0.1       | $5     | Hidden by default; Bedrock/Vertex: regional endpoints +10% surcharge; Cache: writes 1.25x, reads 0.1x                                                                                                                                                                                                                                         |
| [Claude 4.5 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on request-based plans                                                                                                                                                                                                                                                                                   |
| [Claude 4.5 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Hidden by default; Requires Max Mode on request-based plans; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                |
| [Claude 4.6 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Hidden by default; Requires Max Mode on request-based plans; Up to 1M tokens in Max Mode at the same per-token rates (no long-context surcharge)                                                                                                                                                                                              |
| [Claude 4.6 Opus (Fast mode)](https://www.anthropic.com/claude/opus)                          | Anthropic | $30   | $37.5       | $3         | $150   | Hidden by default; Requires Max Mode on request-based plans; Limited research preview; Up to 1M tokens in Max Mode at the same per-token rates as shorter context                                                                                                                                                                             |
| [Claude 4.6 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | $3    | $3.75       | $0.3       | $15    | Requires Max Mode on request-based plans; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                   |
| [Claude 4.7 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | $5    | $6.25       | $0.5       | $25    | Requires Max Mode on request-based plans; Up to 1M tokens in Max Mode at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                 |
| [Composer 1](https://cursor.com)                                                              | Cursor    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Composer 1.5](https://cursor.com)                                                            | Cursor    | $3.5  | -           | $0.35      | $17.5  | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Composer 2](https://cursor.com/blog/composer-2)                                              | Cursor    | $0.5  | -           | $0.2       | $2.5   | -                                                                                                                                                                                                                                                                                                                                             |
| [Gemini 2.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/) | Google    | $0.3  | -           | $0.03      | $2.5   | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs)                                       | Google    | $0.5  | -           | $0.05      | $3     | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Pro](https://ai.google.dev/gemini-api/docs)                                         | Google    | $2    | -           | $0.2       | $12    | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs)                           | Google    | $2    | -           | $0.2       | $12    | Hidden by default; Native image generation model optimized for speed, flexibility, and contextual understanding; Text input and output priced the same as Gemini 3 Pro; Image output: $120/1M tokens (\~$0.134 per 1K/2K image, \~$0.24 per 4K image); Preview models may change before becoming stable and have more restrictive rate limits |
| [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs)                                       | Google    | $2    | -           | $0.2       | $12    | -                                                                                                                                                                                                                                                                                                                                             |
| [GPT-5](https://openai.com/index/gpt-5/)                                                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5-high                                                                                                                                                                                                                                       |
| [GPT-5 Fast](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $2.5  | -           | $0.25      | $20    | Hidden by default; Faster speed but 2x price; Available reasoning effort variants are gpt-5-high-fast, gpt-5-low-fast                                                                                                                                                                                                                         |
| [GPT-5 Mini](https://openai.com/index/gpt-5/)                                                 | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [GPT-5-Codex](https://platform.openai.com/docs/models/gpt-5-codex)                            | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.1 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.1 Codex Max](https://platform.openai.com/docs/models/gpt-5-codex)                      | OpenAI    | $1.25 | -           | $0.125     | $10    | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [GPT-5.1 Codex Mini](https://platform.openai.com/docs/models/gpt-5-codex)                     | OpenAI    | $0.25 | -           | $0.025     | $2     | Hidden by default; Agentic and reasoning capabilities; 4x rate limits compared to GPT-5.1 Codex                                                                                                                                                                                                                                               |
| [GPT-5.2](https://openai.com/index/gpt-5/)                                                    | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.2-high                                                                                                                                                                                                                                     |
| [GPT-5.2 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.3 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | $1.75 | -           | $0.175     | $14    | Requires Max Mode on request-based plans; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.3-codex-high                                                                                                                                                                                                        |
| [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)                              | OpenAI    | $2.5  | -           | $0.25      | $15    | Hidden by default; Requires Max Mode on request-based plans; Agentic and reasoning capabilities; 90% discount on cached input tokens; Fast mode is 15% faster with 2x pricing; Long context (Max Mode) supports up to 1M tokens with 2x input pricing                                                                                         |
| [GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)                    | OpenAI    | $0.75 | -           | $0.075     | $4.5   | Hidden by default; Smaller, faster variant of GPT-5.4; 90% discount on cached input tokens                                                                                                                                                                                                                                                    |
| [GPT-5.4 Nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)                    | OpenAI    | $0.2  | -           | $0.02      | $1.25  | Hidden by default; Smallest GPT-5.4 variant, optimized for cost; 90% discount on cached input tokens                                                                                                                                                                                                                                          |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)                              | OpenAI    | $5    | -           | $0.5       | $30    | Requires Max Mode on request-based plans; Agentic and reasoning capabilities; More token-efficient than GPT-5.4 on comparable tasks; Improved persistence on long-running tasks; Fast mode is available at higher rates; Long context (Max Mode) supports up to 1M tokens with 2x input pricing                                               |
| [Grok 4.20](https://docs.x.ai/docs/models#models-and-pricing)                                 | xAI       | $2    | -           | $0.2       | $6     | The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                                                             |
| Kimi K2.5                                                                                     | Moonshot  | $0.6  | -           | $0.1       | $3     | Hidden by default                                                                                                                                                                                                                                                                                                                             |

### Premium routing

Premium allows Cursor to select the most capable models for you, recommended for the most complex tasks. The Cursor team selects Premium models based on internal benchmarks, evaluations, and user feedback.

Premium pricing is based on the selected model's API rate. Check your [usage page](https://cursor.com/dashboard/usage) to see cost and model selection at the request level.

## Plans

All individual plans include unlimited tab completions, extended agent usage limits on all models, access to Bugbot, and access to Cloud Agents.

| Plan         | Price   | API usage included | Auto + Composer         |
| :----------- | :------ | :----------------- | :---------------------- |
| **Pro**      | $20/mo  | $20                | Generous included usage |
| **Pro Plus** | $60/mo  | $70                | Generous included usage |
| **Ultra**    | $200/mo | $400               | Generous included usage |

Since different models have different API costs, your model selection affects how quickly your included usage is consumed.

### How much usage do I need?

- **Daily Tab users**: Always stay within $20
- **Limited Agent users**: Often stay within the included $20
- **Daily Agent users**: Typically $60–$100/mo total usage
- **Power users (multiple agents/automation)**: Often $200+/mo total usage

### What happens when I reach my limit?

When you exceed your included monthly usage, you can either:

- **Add on-demand usage**: Continue at the same API rates with pay-as-you-go billing
- **Upgrade your plan**: Move to a higher tier for more included usage

On-demand usage is billed monthly at the same rates. Requests are never downgraded in quality or speed.

### Teams

There are two teams plans: Teams ($40/user/mo) and Enterprise (Custom).

Team plans provide additional features like privacy mode enforcement, admin dashboard with usage stats, centralized team billing, and SAML/OIDC SSO.

We recommend Teams for any customer that is happy self-serving. We recommend [Enterprise](https://cursor.com/contact-sales?source=docs-models-pricing) for customers that need priority support, pooled usage, invoicing, SCIM, or advanced security controls.

Learn more about [Teams pricing](https://cursor.com/docs/account/teams/pricing.md).

## Cursor Token Rate

On Teams plans, non-Auto agent requests include a Cursor Token Rate of $0.25 per million tokens. This rate applies on top of model API pricing for included usage, on-demand usage, and BYOK usage. Auto is exempt from the Cursor Token Rate.

## Max Mode

Max Mode extends the context window to the maximum a model supports. More context gives models deeper understanding of your codebase, leading to better results on complex tasks. The models table above shows each model's maximum context size.

Max Mode uses token-based pricing at the model's API rate, so it consumes usage faster than the default context window. On current individual plans, Max Mode is billed at the model's API rate. On Teams plans, non-Auto requests include the Cursor Token Rate. On legacy request-based plans, Max Mode adds a 20% surcharge.

## FAQ

### Where are models hosted?

Models are hosted on US, Canada, & Iceland based infrastructure by the model's provider, a trusted partner, or Cursor directly.

When Privacy Mode is enabled, neither Cursor nor model providers store your data. All data is deleted after each request. For details see our [Privacy Policy](https://cursor.com/privacy) and [Security](https://cursor.com/security) pages.

### Where can I find pricing terms?

For enterprise pricing details, billing terms, and fee calculations, see the [Pricing Policy](https://cursor.com/terms/pricing).


---

## Sitemap

[Overview of all docs pages](/llms.txt)
