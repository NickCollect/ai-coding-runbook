---
source_url: https://cursor.com/docs
---

# Cursor Documentation

Cursor is an AI editor and coding agent. Use it to understand your codebase, plan and build features, fix bugs, review changes, and work with the tools you already use.

![Welcome to Cursor, the AI editor and coding agent](/docs-static/images/agent/review.jpg)

## Start here

### Get started

Go from install to your first useful change in Cursor

### Models & Pricing

Compare models, usage pools, and plan pricing

### Changelog

Stay up to date with the latest features and improvements

## What you can do with Cursor

### Understand your code

Trace how a repo fits together and find the right places to start

### Plan and build features

Scope changes, use Plan Mode, and ship bigger work with confidence

### Find and fix bugs

Reproduce issues, narrow the root cause, and verify the fix

### Review changes

Inspect diffs, run checks, and catch problems before you merge

### Customize Cursor

Use rules, skills, and prompts that match how your team works

### Connect your workflow

Work with GitHub, GitLab, JetBrains, Slack, Linear, and more

## Models

See all model attributes on the [Models & Pricing](https://cursor.com/docs/models-and-pricing.md) page.

| Model                                                                                         | Provider  | Default context | Max mode | Capabilities            | Notes                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------- | --------- | --------------- | -------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Claude 4 Sonnet](https://www.anthropic.com/claude/sonnet)                                    | Anthropic | 200k            | -        | Agent, Thinking, Images | Hidden by default; Thinking variant counts as 2 requests in legacy pricing                                                                                                                                                                                                                                                                    |
| [Claude 4 Sonnet 1M](https://www.anthropic.com/claude/sonnet)                                 | Anthropic | -               | 1M       | Agent, Thinking, Images | Hidden by default; Thinking variant counts as 2 requests in legacy pricing; This model can be very expensive due to the large context window; The cost is 2x when the input exceeds 200k tokens                                                                                                                                               |
| [Claude 4.5 Haiku](https://www.anthropic.com/claude/haiku)                                    | Anthropic | 200k            | -        | Thinking, Images        | Hidden by default; Bedrock/Vertex: regional endpoints +10% surcharge; Cache: writes 1.25x, reads 0.1x                                                                                                                                                                                                                                         |
| [Claude 4.5 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 200k            | 200k     | Agent, Thinking, Images | Hidden by default; Requires Max Mode on request-based plans                                                                                                                                                                                                                                                                                   |
| [Claude 4.5 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | 200k            | 1M       | Agent, Thinking, Images | Hidden by default; Requires Max Mode on request-based plans; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                |
| [Claude 4.6 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 200k            | 1M       | Agent, Thinking, Images | Hidden by default; Requires Max Mode on request-based plans; Up to 1M tokens in Max Mode at the same per-token rates (no long-context surcharge)                                                                                                                                                                                              |
| [Claude 4.6 Opus (Fast mode)](https://www.anthropic.com/claude/opus)                          | Anthropic | 200k            | 1M       | Agent, Thinking, Images | Hidden by default; Requires Max Mode on request-based plans; Limited research preview; Up to 1M tokens in Max Mode at the same per-token rates as shorter context                                                                                                                                                                             |
| [Claude 4.6 Sonnet](https://www.anthropic.com/claude/sonnet)                                  | Anthropic | 200k            | 1M       | Agent, Thinking, Images | Requires Max Mode on request-based plans; The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                   |
| [Claude 4.7 Opus](https://www.anthropic.com/claude/opus)                                      | Anthropic | 200k            | 1M       | Agent, Thinking, Images | Requires Max Mode on request-based plans; Up to 1M tokens in Max Mode at the same per-token rates (no long-context surcharge)                                                                                                                                                                                                                 |
| [Composer 1](https://cursor.com)                                                              | Cursor    | 200k            | -        | Agent, Images           | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Composer 1.5](https://cursor.com)                                                            | Cursor    | 200k            | -        | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Composer 2](https://cursor.com/blog/composer-2)                                              | Cursor    | 200k            | -        | Agent, Thinking, Images | -                                                                                                                                                                                                                                                                                                                                             |
| [Gemini 2.5 Flash](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/) | Google    | 200k            | 1M       | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Flash](https://ai.google.dev/gemini-api/docs)                                       | Google    | 200k            | 1M       | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Pro](https://ai.google.dev/gemini-api/docs)                                         | Google    | 200k            | 1M       | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs)                           | Google    | 200k            | 1M       | Images                  | Hidden by default; Native image generation model optimized for speed, flexibility, and contextual understanding; Text input and output priced the same as Gemini 3 Pro; Image output: $120/1M tokens (\~$0.134 per 1K/2K image, \~$0.24 per 4K image); Preview models may change before becoming stable and have more restrictive rate limits |
| [Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs)                                       | Google    | 200k            | 1M       | Agent, Thinking, Images | -                                                                                                                                                                                                                                                                                                                                             |
| [GPT-5](https://openai.com/index/gpt-5/)                                                      | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5-high                                                                                                                                                                                                                                       |
| [GPT-5 Fast](https://openai.com/index/gpt-5/)                                                 | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Faster speed but 2x price; Available reasoning effort variants are gpt-5-high-fast, gpt-5-low-fast                                                                                                                                                                                                                         |
| [GPT-5 Mini](https://openai.com/index/gpt-5/)                                                 | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [GPT-5-Codex](https://platform.openai.com/docs/models/gpt-5-codex)                            | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.1 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.1 Codex Max](https://platform.openai.com/docs/models/gpt-5-codex)                      | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |
| [GPT-5.1 Codex Mini](https://platform.openai.com/docs/models/gpt-5-codex)                     | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; 4x rate limits compared to GPT-5.1 Codex                                                                                                                                                                                                                                               |
| [GPT-5.2](https://openai.com/index/gpt-5/)                                                    | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.2-high                                                                                                                                                                                                                                     |
| [GPT-5.2 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Agentic and reasoning capabilities                                                                                                                                                                                                                                                                                         |
| [GPT-5.3 Codex](https://platform.openai.com/docs/models/gpt-5-codex)                          | OpenAI    | 272k            | -        | Agent, Thinking, Images | Requires Max Mode on request-based plans; Agentic and reasoning capabilities; Available reasoning effort variant is gpt-5.3-codex-high                                                                                                                                                                                                        |
| [GPT-5.4](https://developers.openai.com/api/docs/models/gpt-5.4)                              | OpenAI    | 272k            | 1M       | Agent, Thinking, Images | Hidden by default; Requires Max Mode on request-based plans; Agentic and reasoning capabilities; 90% discount on cached input tokens; Fast mode is 15% faster with 2x pricing; Long context (Max Mode) supports up to 1M tokens with 2x input pricing                                                                                         |
| [GPT-5.4 Mini](https://developers.openai.com/api/docs/models/gpt-5.4-mini)                    | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Smaller, faster variant of GPT-5.4; 90% discount on cached input tokens                                                                                                                                                                                                                                                    |
| [GPT-5.4 Nano](https://developers.openai.com/api/docs/models/gpt-5.4-nano)                    | OpenAI    | 272k            | -        | Agent, Thinking, Images | Hidden by default; Smallest GPT-5.4 variant, optimized for cost; 90% discount on cached input tokens                                                                                                                                                                                                                                          |
| [GPT-5.5](https://developers.openai.com/api/docs/models/gpt-5.5)                              | OpenAI    | 272k            | 1M       | Agent, Thinking, Images | Requires Max Mode on request-based plans; Agentic and reasoning capabilities; More token-efficient than GPT-5.4 on comparable tasks; Improved persistence on long-running tasks; Fast mode is available at higher rates; Long context (Max Mode) supports up to 1M tokens with 2x input pricing                                               |
| [Grok 4.20](https://docs.x.ai/docs/models#models-and-pricing)                                 | xAI       | 200k            | 2M       | Agent, Thinking         | The cost is 2x when the input exceeds 200k tokens                                                                                                                                                                                                                                                                                             |
| Kimi K2.5                                                                                     | Moonshot  | 262k            | -        | Agent, Thinking, Images | Hidden by default                                                                                                                                                                                                                                                                                                                             |

## More resources

### Downloads

Get Cursor for your computer

### Help

Find answers to common questions and troubleshooting guides

For account and billing questions, contact our support team


---

## Sitemap

[Overview of all docs pages](/llms.txt)
