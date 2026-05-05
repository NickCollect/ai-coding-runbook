---
type: entity
name: Enterprise-gateway
aliases: [Amazon Bedrock, Google Vertex AI, Microsoft Foundry, LLM Gateway]
category: integration
status: ga
created: 2026-05-05
---

## 一句话定义

通过企业 LLM gateway 接入 Claude Code（AWS Bedrock / GCP Vertex / Azure Foundry / 自建 LLM Gateway）

## 关键属性

- 四种支持的企业接入方式：Amazon Bedrock、Google Vertex AI、Microsoft Foundry（Azure）、自建 LLM gateway proxy [[amazon-bedrock]] [[google-vertex-ai]] [[microsoft-foundry]] [[llm-gateway]]
- Bedrock 启用：`CLAUDE_CODE_USE_BEDROCK=1` + `AWS_REGION`（必须显式设，不读 `.aws/config`）；交互式向导 `/setup-bedrock`；IAM 需 `bedrock:InvokeModel`、`InvokeModelWithResponseStream`、`ListInferenceProfiles`、`GetInferenceProfile`、`aws-marketplace:Subscribe` [[amazon-bedrock]]
- Vertex 启用：`CLAUDE_CODE_USE_VERTEX=1` + `CLOUD_ML_REGION`（接受 `global` / multi-region `eu`/`us` / 具体如 `us-east5`）+ `ANTHROPIC_VERTEX_PROJECT_ID`；向导 `/setup-vertex`；IAM 需 `roles/aiplatform.user` [[google-vertex-ai]]
- Foundry 启用：`CLAUDE_CODE_USE_FOUNDRY=1` + `ANTHROPIC_FOUNDRY_RESOURCE`（或 `ANTHROPIC_FOUNDRY_BASE_URL`）；auth 走 `ANTHROPIC_FOUNDRY_API_KEY` 或 Entra ID 默认凭证链；RBAC 需 `Azure AI User` + `Cognitive Services User` [[microsoft-foundry]]
- 在所有 enterprise gateway 下 `/login` 和 `/logout` 都被禁用——auth 走 cloud provider 自身机制 [[amazon-bedrock]] [[google-vertex-ai]] [[microsoft-foundry]]
- Model pinning **关键**：不 pin 时 `sonnet`/`opus`/`haiku` 别名解析到最新版，可能尚未在客户账号开通；用 `ANTHROPIC_DEFAULT_OPUS_MODEL` / `..._SONNET_MODEL` / `..._HAIKU_MODEL` 钉死特定 ID（不 pin opus 时默认是 Opus 4.6 而非 4.7） [[amazon-bedrock]] [[google-vertex-ai]] [[microsoft-foundry]]
- 1M context window 在 Opus 4.7 / Opus 4.6 / Sonnet 4.6 上支持，写法是 model ID 后追加 `[1m]`（Bedrock 和 Vertex 都通） [[amazon-bedrock]] [[google-vertex-ai]]
- Prompt caching 默认开启；`ENABLE_PROMPT_CACHING_1H=1` 切到 1h TTL（写费率更高）；Vertex 上 `DISABLE_PROMPT_CACHING=1` 可关闭 [[amazon-bedrock]] [[google-vertex-ai]] [[microsoft-foundry]]
- Bedrock Mantle endpoint（v2.1.94+）：`CLAUDE_CODE_USE_MANTLE=1` 启用原生 Anthropic API shape 经 Bedrock 服务，model ID 用 `anthropic.` 前缀；可与 Invoke API 并存，按 ID 自动路由；`CLAUDE_CODE_SKIP_MANTLE_AUTH=1` 给 LLM-gateway 注入凭证场景 [[amazon-bedrock]]
- Vertex 上 MCP tool search 默认禁用（endpoint 不接受所需 beta header），所有 MCP tool defs 上来就全量加载；`ENABLE_TOOL_SEARCH=true` opt in [[google-vertex-ai]]
- Computer use 在 enterprise gateway 下**不可用**——仅支持 direct Anthropic API plan（Pro/Max/Team/Enterprise） [[computer-use]] [[chrome]]
- Chrome 集成同样**不支持** Bedrock/Vertex/Foundry——third-party provider 用户需另起 claude.ai 帐号 [[chrome]]
- LLM gateway 必须暴露至少一种格式：Anthropic Messages（`/v1/messages`、`/v1/messages/count_tokens`）、Bedrock InvokeModel（`/invoke`、`/invoke-with-response-stream`）、或 Vertex rawPredict（`:rawPredict`、`:streamRawPredict`、`/count-tokens:rawPredict`）；用 Anthropic Messages 格式经 Bedrock/Vertex 时设 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` [[llm-gateway]]
- Gateway model discovery（v2.1.126+）：设了 `ANTHROPIC_BASE_URL` 后启动时查 `/v1/models`，加到 `/model` picker 标 "From gateway"，过滤 `claude` / `anthropic` 前缀，缓存到 `~/.claude/cache/gateway-models.json` [[llm-gateway]]
- LiteLLM 警告：PyPI 1.82.7 / 1.82.8 被植入了凭证窃取恶意代码——升级 + rotate 凭证；LiteLLM 是第三方，非 Anthropic 背书 [[llm-gateway]]
- Auto mode 不支持任何 enterprise gateway——仅限 direct Anthropic API plan [[permission-modes]] [[auto-mode-config]]

## 出现来源

_31 summaries reference this entity_:

- [[2026-w15]]
- [[admin-setup]]
- [[amazon-bedrock]]
- [[authentication]]
- [[changelog--claude-code-repo]]
- [[chrome]]
- [[claude-api-php]]
- [[code-review]]
- [[computer-use]]
- [[data-usage]]
- [[desktop]]
- [[devcontainer]]
- [[env-vars]]
- [[errors]]
- [[fast-mode]]
- [[github-actions]]
- [[gitlab-ci-cd]]
- [[google-vertex-ai]]
- [[legal-and-compliance]]
- [[llm-gateway]]
- [[microsoft-foundry]]
- [[model-config]]
- [[network-config]]
- [[secure-deployment]]
- [[server-managed-settings]]
- [[settings]]
- [[setup]]
- [[third-party-integrations]]
- [[troubleshoot-install]]
- [[ultrareview]]
- [[vs-code]]

## 相关

- [[Settings]] — gateway 通过 env vars + `apiKeyHelper` / `awsAuthRefresh` / `awsCredentialExport` / `modelOverrides` 等 settings 字段配置
- [[Prompt-caching]] — gateway 下 caching 默认开启，但 `ENABLE_PROMPT_CACHING_1H` 切 TTL；attribution header 影响第三方 gateway 的 caching key
- [[Computer-use]] — computer use 不支持 enterprise gateway，是 direct Anthropic plan 独占
- [[Auto-mode]] — auto mode 同样不支持 Bedrock/Vertex/Foundry，仅 Anthropic API
- [[MCP-server]] — Vertex 默认禁 MCP tool search；gateway 不影响 MCP 但影响 tool list 加载策略
- [[CI-integration]] — GitHub Actions / GitLab CI 跑 Claude Code 时也可走 gateway，env vars 同样适用
