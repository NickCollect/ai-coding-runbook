---
type: entity
name: Headless-mode
aliases: [headless, headless mode, non-interactive]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 非交互式（脚本 / CI / SDK）调用模式

## 关键属性

- 通过 `-p` / `--print` flag 启用，本质是同款 agent loop / tools / context management 的非交互运行；曾用名 "headless mode"，glossary 现称 "Non-interactive mode" [[headless]] [[glossary]]
- 基本调用 `claude -p "prompt" --allowedTools "Read,Edit,Bash"`，可走 stdin pipe：`cat err.log | claude -p "explain"` [[headless]] [[common-workflows]]
- `--bare` flag 跳过 hooks / skills / plugins / MCP / auto-memory / CLAUDE.md 自动发现，启动更快、跨机器结果确定；只有 Bash + file read/edit 默认可用，Auth 必须靠 `ANTHROPIC_API_KEY` 或 `apiKeyHelper`（不读 keychain，也**不读 `CLAUDE_CODE_OAUTH_TOKEN`**）[[headless]] [[authentication]]
- Bare mode 是 CI 推荐配置，未来计划成为 `-p` 默认；额外 context 通过 `--append-system-prompt[-file]` / `--settings` / `--mcp-config` / `--agents` / `--plugin-dir` 注入 [[headless]]
- 输出格式 `--output-format text|json|stream-json`；`json` 给 `{result, session_id, total_cost_usd, ...}`；`stream-json` 配 `--verbose --include-partial-messages` 可拿到 token-level 流 [[headless]]
- 结构化输出：`--output-format json --json-schema '{"type":"object",...}'`，结果落在 `structured_output` 字段 [[headless]]
- 关键 stream event：`system/init`（含 `plugins` 与 `plugin_errors`，CI 可借后者 fail）、`system/api_retry`（含 attempt / retry_delay_ms / error 分类）、`system/plugin_install`（需 `CLAUDE_CODE_SYNC_PLUGIN_INSTALL`）[[headless]]
- 权限自动化两套：临时 `--allowedTools "Bash,Read,Edit"`；session-wide 用 `--permission-mode dontAsk`（仅 allow 列表+只读，CI 锁死）或 `acceptEdits`（自动通过 write + 常用 FS bash） [[headless]] [[permission-modes]]
- 权限规则前缀 match 关键：`Bash(git diff *)` 末尾要带空格 + `*`，否则 `Bash(git diff*)` 会误匹配 `git diff-index` [[headless]]
- 多轮：`--continue`（cwd 最近 session）/ `--resume <session-id>`（指定）/ `--from-pr <num|url>`（从 PR 续）；jq 抽 session_id：`session_id=$(claude -p "..." --output-format json | jq -r '.session_id')` [[headless]] [[cli-reference]]
- 用户调用的 skill（`/commit` 等）和 built-in slash command 在 `-p` 模式**不可用**，要直接用自然语言描述任务 [[headless]]
- Auto mode 在 headless 下 3 次连续被 classifier block 或共 20 次会**直接 abort**（无人可 prompt）[[permission-modes]]
- `claude ultrareview [target] --json --timeout` 是非交互形式的多 agent code review，stdout 出 findings 或 raw `bugs.json`，stderr 出进度 + live URL；exit code 0/1/130 区分完成 / 失败 / Ctrl-C [[ultrareview]] [[changelog]]
- 第三方 provider（Bedrock / Vertex / Foundry）走 `CLAUDE_CODE_USE_BEDROCK=1` 等环境变量，不需要 browser login，特别适合 CI [[authentication]] [[overview--agent-sdk]]
- Computer use 在 CLI 仅 interactive 模式可用，`-p` 下不可用 [[computer-use]]

## 出现来源

_14 summaries reference this entity_:

- [[authentication]]
- [[best-practices]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[cli-reference]]
- [[common-workflows]]
- [[computer-use]]
- [[desktop]]
- [[glossary]]
- [[headless]]
- [[permission-modes]]
- [[platforms]]
- [[settings]]
- [[ultrareview]]

## 相关

- [[Agent-SDK]] — Python / TS SDK 是 headless 调用的官方编程接口
- [[Permission-mode]] — `dontAsk` / `acceptEdits` / `auto` 是 headless 实操关键
- [[CI-integration]] — GitHub Actions / GitLab CI 都靠 headless mode 跑
- [[Auto-mode]] — headless 中 auto-mode 反复被 block 会 abort
- [[Native-interface]] — `claude -p` 是 CLI surface 的核心非交互入口
- [[Settings]] — `--settings` 和 `--bare` + `apiKeyHelper` 用来 CI 注入配置
