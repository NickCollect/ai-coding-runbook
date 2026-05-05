---
type: qa
topic: safety-and-limits
created: 2026-05-05
sources:
  - 02_Wiki/Entities/Rate-limit-API.md
  - 02_Wiki/Entities/Permission-mode.md
  - 02_Wiki/Entities/Computer-use.md
  - 02_Wiki/Summaries/safety-settings--gemini-docs.md
  - 02_Wiki/Summaries/safety-best-practices--openai-docs.md
  - 02_Wiki/Summaries/prompt-injection-defenses--anthropic-research.md
  - 02_Wiki/Summaries/rate-limits--openai-docs.md
  - 02_Wiki/Summaries/rate-limits-api--bwc.md
---

# Safety & Limits Q&A

## Q: Claude 的 rate limit 层级是怎么算的？
**A:** Anthropic Rate Limits API 将限制分为 6 个 **group_type**：`model_group`（按模型分组）、`batch`（Message Batches）、`token_count`、`files`（Files API）、`skills`（Skills API）、`web_search`。每组 limiter 类型包括 `requests_per_minute`、`input_tokens_per_minute`、`output_tokens_per_minute`、`enqueued_batch_requests` 等。限制在 **org 级别**设置，Workspace 可 override（通过 Admin API 查询）。具体 RPM/TPM 数值按账户层级和 plan 不同，*具体 tier 数值待确认（数据截至 2026-05-05，需核实 console.anthropic.com/limits）*。
*来源：[[Rate-limit-API]]、[[rate-limits-api--bwc]]*

---

## Q: 什么是 prompt injection？如何防御？
**A:** Prompt injection 是将恶意指令隐藏在不可信内容中（如网页白色文字、邮件隐藏文本），让 agent 在处理该内容时执行攻击者意图的操作（如转发邮件、泄露数据）。防御策略：(1) 仅连接可信 MCP server（第三方 server 均为 Anthropic 未验证）；(2) 用 Permission mode 限制工具权限（`plan` 或 `acceptEdits` 而非 `bypassPermissions`）；(3) 用 Hooks 的 `PreToolUse` 拦截危险操作；(4) 最小权限原则——agent 仅获得完成任务所需的工具；(5) 对 browser agent，尽量限制可访问的网站范围。Anthropic 在 Claude Opus 4.5 launch 时做了重大 prompt injection 鲁棒性改进，但此问题尚未完全解决。
*来源：[[prompt-injection-defenses--anthropic-research]]、[[mcp-integration-guide]]*

---

## Q: Claude 的 computer use 有哪些安全限制？
**A:** 三层安全控制：(1) **App tier**：browsers/交易平台 = view-only；terminals/IDEs（Terminal、iTerm、VS Code、Warp）= click-only；其他 = full control；Finder/System Settings 有 sentinel 警告；(2) **机器级 lock**：同一时间只能一个 Claude session 控制电脑，crash 自动释放；(3) **Session 授权**：每次 session 需逐 app 授权，仅当前 session 有效。终端从截图中排除（Claude 看不到自己的输出）。Esc 任意位置可立即中止并释放。仅支持 direct Anthropic plan（不支持 Bedrock / Vertex / Foundry）。仅 interactive 模式可用（无 headless `-p`）。
*来源：[[Computer-use]]*

---

## Q: Gemini 的 safety settings 怎么配置？
**A:** 通过 `types.SafetySetting` 配置 4 个类别：`HARM_CATEGORY_HARASSMENT`、`HARM_CATEGORY_HATE_SPEECH`、`HARM_CATEGORY_SEXUALLY_EXPLICIT`、`HARM_CATEGORY_DANGEROUS_CONTENT`。每类别可设置阈值：`BLOCK_LOW_AND_ABOVE`、`BLOCK_MEDIUM_AND_ABOVE`（默认）、`BLOCK_ONLY_HIGH`、`BLOCK_NONE`。部分核心危害（如儿童安全）永远不可调整，始终 block。检测：响应 `candidate.finish_reason == "SAFETY"` 表示被拦截，`candidate.safety_ratings` 显示具体类别。
*来源：[[safety-settings--gemini-docs]]*

---

## Q: OpenAI 的 content moderation API 是什么？
**A:** `/v1/moderations` endpoint，**免费调用**，检测用户输入或模型输出中的违规内容（仇恨、自残、暴力等）。OpenAI 推荐对用户输入和模型输出**都**进行检测。可搭配 `user` 参数传入用户标识符，帮助 OpenAI 追踪滥用行为（违规时可吊销对应用户访问）。建议用于高风险应用（医疗、法律、金融）时配合人工审核（human-in-the-loop）。
*来源：[[safety-best-practices--openai-docs]]*

---

## Q: Claude 的 permission mode 有哪些级别？
**A:** 共 **6 种**（由严到宽）：`plan`（只读 + 规划，无任何写操作）→ `default`（仅读不问，写操作 prompt 确认）→ `acceptEdits`（自动批 edits + 常用 FS bash，protected paths 仍 prompt）→ `dontAsk`（仅 pre-approved 工具，完全 non-interactive）→ `auto`（classifier 决策，v2.1.83+ research preview，连续 3 次或累计 20 次 block 后暂停；仅 Max/Team/Enterprise/API plan）→ `bypassPermissions`（一切放行，需显式 `--dangerously-skip-permissions` 启动）。切换：CLI `Shift+Tab` 循环前 3 种，或 `--permission-mode <mode>` 指定。
*来源：[[Permission-mode]]*
