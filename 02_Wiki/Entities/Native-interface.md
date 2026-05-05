---
type: entity
name: Native-interface
aliases: [native interface, Claude Code interfaces]
category: integration
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 的多种入口（CLI / Desktop / Web / Slack）

## 关键属性

- 六大入口：Terminal CLI / VS Code / JetBrains / Desktop（macOS、Windows）/ Web (`claude.ai/code`) / Slack / 移动端 (iOS、Android)；Linux 仅 CLI 可用 [[platforms]] [[overview--claude-code]]
- **CLI 是最完整 surface**：唯一支持 Agent SDK / 第三方 provider / `--print`/scripting / Agent teams 等高级特性 [[platforms]] [[desktop]]
- 各 surface 共享同一 engine + 同一 CLAUDE.md / settings / MCP / hooks / skills（local surfaces 之间） [[platforms]] [[desktop-quickstart]]
- Desktop 三 tab：**Chat**（claude.ai 对话）/ **Cowork**（云 VM 后台 agent / Dispatch）/ **Code**（带本地文件访问） [[desktop]] [[desktop-quickstart]]
- Desktop Code tab Environment 选项：**Local**（本机文件）/ **Remote**（Anthropic 云 VM，关 app 仍跑）/ **SSH**（首次连远端时自动安装 Claude Code） [[desktop]] [[desktop-quickstart]]
- Desktop 面板可 drag/resize：chat / diff / preview / terminal / file / plan / tasks / subagent；Cmd/Ctrl+\\ 关焦点面板（v1.2581.0+） [[desktop]]
- Web (`claude.ai/code`) **Research preview**：限 Pro / Max / Team / 高级 Enterprise；Anthropic 管理云 VM 克隆 repo；session 跨设备持久 [[claude-code-on-the-web]] [[web-quickstart]]
- Web cloud VM 资源：4 vCPU / 16 GB RAM / 30 GB disk；预装 Python 3.x / Node 20-22 / Ruby 3.1-3.3 / PHP 8.4 / Java 21 / Go / Rust / Docker / PostgreSQL 16 / Redis 7；`gh` 不预装 [[claude-code-on-the-web]]
- Web 不支持的 permission mode：仅 Auto-accept-edits 与 Plan 可用；无 Ask / Auto / Bypass [[claude-code-on-the-web]] [[web-quickstart]]
- **Slack 集成**：通过 Claude for Slack app；`@Claude` mention 含编程意图 → 路由到 Web 上的 Claude Code session；**只在 channel（公/私）工作，DM 不行** [[slack]]
- Slack 路由模式：**Code only**（全部 @mention 走 Code）或 **Code + Chat**（按意图分流，可手动 Retry as Code） [[slack]]
- **Remote Control**：从 claude.ai/code 或移动端驱动本地 session，session 仍跑在本机不上云；研究预览，需 Claude Code v2.1.51+ [[remote-control]] [[platforms]]
- Remote Control 三种启动：`claude remote-control` server 模式（持续，可多 session，spacebar 显 QR） / `claude --remote-control`/`--rc` 交互模式 / `/remote-control` slash command；VS Code v2.1.79+ 也可用 [[remote-control]]
- Remote Control 限制：每交互进程一 session；本机进程必须保持运行（关终端 = session 结束）；~10 min 网络断 → 超时退出；Ultraplan 与 Remote Control 互斥（都占 claude.ai/code） [[remote-control]]
- Remote Control 阻断条件：`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_TELEMETRY` / 第三方 provider (`CLAUDE_CODE_USE_BEDROCK`/`VERTEX`/`FOUNDRY`) 全部禁用 Remote Control [[remote-control]]
- Cross-surface 切换：`/desktop`（CLI → Desktop）/ `claude --remote` (本地 → Web，clone GitHub 或 bundle local repo 至 100MB) / `claude --teleport`、`/teleport`、`/tp`（Web → 本地终端，需同 claude.ai 账号 + 干净 git + 同 repo + 推过分支） [[desktop]] [[claude-code-on-the-web]] [[remote-control]]
- 移动端职责：作 cloud session 瘦客户端 / Remote Control 驱动本地 / Dispatch 派发到 Desktop（Pro/Max） [[platforms]]
- Desktop session 隔离：Git repo 默认在 `<project-root>/.claude/worktrees/` 起 worktree；`.worktreeinclude` 列 gitignored 文件（如 `.env`）拷入；PR 合后可选 auto-archive [[desktop]]
- Desktop 不可用功能：第三方 provider（Bedrock / Foundry；Vertex 仅企业 managed settings）/ Linux / inline code suggestion / Agent teams（CLI/SDK 才有）/ `--print`/scripting [[desktop]]
- 安装方式（CLI）：macOS/Linux/WSL `curl -fsSL https://claude.ai/install.sh | bash`；Windows PowerShell `irm https://claude.ai/install.ps1 | iex`；Homebrew `brew install --cask claude-code`；WinGet `winget install Anthropic.ClaudeCode`；Linux 还有 apt/dnf/apk [[overview--claude-code]]

## 出现来源

_32 summaries reference this entity_:

- [[2026-w17]]
- [[README--claude-code-repo]]
- [[authentication]]
- [[changelog]]
- [[chrome]]
- [[claude-code-on-the-web]]
- [[cli-reference]]
- [[commands]]
- [[computer-use]]
- [[deep-links]]
- [[desktop]]
- [[desktop-quickstart]]
- [[desktop-scheduled-tasks]]
- [[errors]]
- [[github-enterprise-server]]
- [[glossary]]
- [[how-claude-code-works]]
- [[interactive-mode]]
- [[overview--claude-code]]
- [[platforms]]
- [[quickstart--claude-code]]
- [[remote-control]]
- [[routines]]
- [[settings]]
- [[setup]]
- [[slack]]
- [[troubleshoot-install]]
- [[ultraplan]]
- [[ultrareview]]
- [[voice-dictation]]
- [[web-quickstart]]
- [[whats-new]]

## 相关

- [[IDE-integration]] — VS Code / JetBrains / Chrome 扩展属于另一类入口，与 native interface 互补
- [[Channel]] — Channel 让 native interface 接收 Telegram / Discord / 自有服务器的外部事件
- [[Computer-use]] — Desktop（macOS/Windows，Pro/Max）开启后可通过 Native interface 控制 GUI
- [[Settings]] — `sshConfigs` / `disableDeepLinkRegistration` 等 native interface 行为受 settings 控制
- [[Headless-mode]] — `claude -p` 仅在 CLI surface 支持
- [[Routine]] — 云端定时器从 web surface 触发
- [[Scheduled-task]] — Desktop 自带的本地定时调度
