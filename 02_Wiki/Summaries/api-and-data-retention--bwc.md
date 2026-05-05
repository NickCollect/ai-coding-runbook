---
type: summary
source: 01_Raw/platform.claude.com/docs/en/build-with-claude/api-and-data-retention.md
source_url: https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention
title: "API and data retention"
summarized_at: 2026-05-05
entities_referenced: [Messages-API, Token-counting, Web-search-tool, Web-fetch-tool, Advisor-tool, Memory-tool, Compaction, Context-editing, Fast-mode, Adaptive-thinking, Citations-API, Effort, Extended-thinking, PDF-support, Search-results, Bash-tool-API, Text-editor-tool, Computer-use-tool-API, Prompt-caching, Structured-outputs, Tool-search-tool-API, Batches-API, Code-execution-tool, Files-API, Skill-API, Enterprise-gateway]
concepts_referenced: [Context-window]
---

Anthropic offers two privacy arrangements for the Claude API: **Zero Data Retention (ZDR)** and **HIPAA readiness** (with signed BAA). This page documents which features are eligible and the policies that govern them.

## ZDR scope

Customer data is **not stored at rest** after the API response is returned, except where required by law or for misuse prevention.

**Covered:**
- Claude Messages API and Token Counting API.
- Claude Code with Commercial org API keys, or via Claude Enterprise (per-org enablement; not auto-applied to new orgs).

**NOT covered:** Console/Workbench, Claude Managed Agents (stateful), Claude consumer plans (Free/Pro/Max), Claude Teams, Claude Enterprise non-Code interfaces, third-party integrations, Claude for Excel.

## HIPAA readiness

For PHI handling. Requires signed BAA + HIPAA-enabled org (provisioned by Anthropic). Replaces previous ZDR-required model. Org-level enforcement: API returns `400 invalid_request_error` if non-eligible features used. Use **separate orgs** for HIPAA vs general workloads.

**NOT covered by HIPAA:** consumer plans, Console/Workbench, Bedrock, Vertex AI, Claude Code, beta features (unless explicitly listed).

**PHI restrictions in JSON schemas:** With Structured Outputs or strict tools, schemas are cached separately. **Do not include PHI in** schema property names, `enum` values, `const` values, `pattern` regex.

## Feature eligibility table

| Feature | ZDR | HIPAA |
|---|---|---|
| Messages API | Yes | Yes |
| Token counting | Yes | Yes |
| Web search | Yes¹ | Yes¹ |
| Web fetch | Yes¹² | No |
| Advisor tool | Yes | No |
| Memory tool | Yes | Yes |
| Compaction | Yes | No |
| Context editing | Yes | No |
| Fast mode | Yes | Yes |
| 1M context window | Yes | Yes |
| Adaptive thinking | Yes | Yes |
| Citations | Yes | Yes |
| Data residency | Yes | Yes |
| Effort | Yes | Yes |
| Extended thinking | Yes | Yes |
| PDF support | Yes | Yes (inline only, not via Files API) |
| Search results | Yes | Yes |
| Bash tool | Yes | Yes |
| Text editor tool | Yes | Yes |
| Computer use | Yes | No |
| Fine-grained tool streaming | Yes | Yes |
| Prompt caching | Yes | Yes |
| Structured outputs | Yes (qualified) | Yes³ |
| Tool search | Yes | No |
| Batch processing | No | No (29-day retention) |
| Code execution | No | No (≤30 days) |
| Programmatic tool calling | No | No |
| Files API | No | No (until deleted) |
| Agent skills | No | No |
| MCP connector | No | No |

¹ Dynamic filtering (web search) not ZDR/HIPAA. ² Web fetch publishers may retain request data. ³ PHI must not appear in JSON schema.

## Limitations

- **CORS not supported under ZDR** — must use backend proxy; never expose API keys in browser JS.
- Even under ZDR/HIPAA, data flagged for Usage Policy violations may be retained up to **2 years**.

## FAQ highlights

- Bedrock/Vertex are not eligible for ZDR/HIPAA — refer to those platforms' policies.
- Claude Code metrics logging (productivity stats) is exempt from ZDR.
- Existing structured-outputs JSON schemas are cached up to **24 hours since last use**.
