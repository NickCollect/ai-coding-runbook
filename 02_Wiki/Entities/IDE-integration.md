---
type: entity
name: IDE-integration
aliases: [IDE integration, VS Code integration, JetBrains integration]
category: integration
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 在 IDE 里的集成（VS Code / JetBrains / Chrome 浏览器）

## 关键属性

- 三大集成：**VS Code 扩展**（也支持 Cursor）/ **JetBrains plugin**（IntelliJ / PyCharm / WebStorm / PhpStorm / GoLand / Android Studio）/ **Claude in Chrome 扩展** [[vs-code]] [[jetbrains]] [[chrome]]
- VS Code 扩展要求：VS Code 1.98.0+；通过 Marketplace 搜索 "Claude Code" 或 `vscode:extension/anthropic.claude-code` URI 安装；**捆绑了 CLI** 可在内置终端用 [[vs-code]]
- VS Code 面板入口 4 处：编辑器右上 Spark 图标 (✱) / Activity Bar / Command Palette → "Claude Code" / Status Bar 右下 [[vs-code]]
- VS Code 选区共享：Claude 自动看到高亮文本；`Option+K` / `Alt+K` 插入 `@file.ts#5-10` 引用；眼睛图标可隐藏选区 [[vs-code]]
- VS Code 关键 settings：`useTerminal` / `initialPermissionMode` / `preferredLocation` (sidebar/panel) / `respectGitIgnore` / `usePythonEnvironment` / `allowDangerouslySkipPermissions` / `claudeProcessWrapper` 等；与 CLI 共享 `~/.claude/settings.json` [[vs-code]]
- VS Code 内建 IDE MCP server (`ide`，`/mcp` 列表里隐藏)：在 `127.0.0.1:random-port`，每次激活生成 fresh auth token 写到 `~/.claude/ide/` lock file (0600/0700)；暴露 `mcp__ide__getDiagnostics`（read-only Problems panel）+ `mcp__ide__executeCode`（Jupyter cell exec） [[vs-code]]
- VS Code `executeCode` 安全模型：每次执行前都强制弹原生 Quick Pick 让用户选 Execute/Cancel，独立于 `PreToolUse` hook；非 Python kernel / 无 active notebook 拒绝执行 [[vs-code]]
- VS Code URI handler：`vscode://anthropic.claude-code/open?prompt=...&session=...` 从 shell/script 打开新 tab；`prompt` 不会自动提交；`session` 必须属于当前 workspace [[vs-code]]
- JetBrains 入口：`Cmd+Esc`（Mac）/ `Ctrl+Esc`（Win/Linux）快速启动；从内置终端跑 `claude` 或外部终端跑 `claude` + `/ide` 连接 [[jetbrains]]
- JetBrains 设置位 Settings → Tools → Claude Code [Beta]：可定制 Claude command path（`claude` / 绝对路径 / `npx @anthropic-ai/claude-code` / WSL `wsl -d Ubuntu -- bash -lic "claude"`） [[jetbrains]]
- JetBrains Remote Development：plugin 装在 **远程 host**，不是本地 client（Settings → Plugin (Host)） [[jetbrains]]
- JetBrains WSL2 "No available IDEs detected"：默认 NAT networking + Windows Firewall 挡住 WSL2↔IDE；解法用 Firewall rule 或 WSL2 mirrored networking（Win 11 22H2+，`.wslconfig` 加 `[wsl2] networkingMode=mirrored`） [[jetbrains]]
- JetBrains 安全注意：auto-edit 启用时 Claude 可改 IDE 配置文件，可能被 IDE 自动执行绕过 Bash permission；敏感场景用 manual approval [[jetbrains]]
- **Chrome 集成**（beta，不是 Computer-use）：通过 Claude in Chrome extension 驱动真实浏览器；built-in MCP server `claude-in-chrome`；只支持 Chrome / Edge（Brave / Arc / 其他 Chromium 不行；WSL 不行） [[chrome]]
- Chrome 集成版本要求：扩展 v1.0.36+ / Claude Code v2.0.73+；仅直接 Anthropic plan（Pro/Max/Team/Enterprise）支持，不可用于 Bedrock/Vertex/Foundry [[chrome]]
- Chrome 启用方式：`claude --chrome` 启动或 session 内 `/chrome`；后者还可设 "Enabled by default"（警告：常驻会增加 context 占用） [[chrome]]
- Chrome native messaging host config 在首次启用时安装；扩展未检测到时往往需重启 Chrome；MV3 service worker idle 会断长 session 连接 [[chrome]]
- VS Code 也可用 Chrome 自动化（`@browser` 前缀），无需 `--chrome` flag [[vs-code]] [[chrome]]
- Dev Container 集成：通过 Claude Code Dev Container Feature `ghcr.io/anthropics/devcontainer-features/claude-code:1.0` 安装；VS Code 扩展自动一并装；用 named volume `claude-code-config` 持久化 `~/.claude` 跨 rebuild [[devcontainer]]
- Voice dictation 在 VS Code 扩展支持，但 **VS Code Remote (SSH/Dev Containers/Codespaces) 不支持** [[voice-dictation]]
- 跨进程 deep link 系统：`claude-cli://open?q=&cwd=&repo=` URL scheme 在首次启动 interactive `claude` 时注册 OS-wide；VS Code 扩展另有 `vscode://anthropic.claude-code/open` scheme [[deep-links]] [[vs-code]]

## 出现来源

_24 summaries reference this entity_:

- [[2026-w17]]
- [[changelog]]
- [[chrome]]
- [[cli-reference]]
- [[commands]]
- [[communications-kit]]
- [[computer-use]]
- [[deep-links]]
- [[desktop]]
- [[devcontainer]]
- [[how-claude-code-works]]
- [[jetbrains]]
- [[network-config]]
- [[overview--claude-code]]
- [[platforms]]
- [[quickstart--claude-code]]
- [[remote-control]]
- [[security]]
- [[settings]]
- [[setup]]
- [[tools-reference]]
- [[voice-dictation]]
- [[vs-code]]
- [[whats-new]]

## 相关

- [[Native-interface]] — IDE 集成与 CLI / Desktop / Web 是 Claude Code 的另一类入口
- [[MCP-server]] — VS Code 内建 `ide` MCP server / Chrome 内建 `claude-in-chrome` MCP server
- [[Computer-use]] — Chrome 集成是浏览器内 DOM-aware 自动化，与 native macOS app 控制的 Computer-use 互补
- [[Settings]] — VS Code / JetBrains / Chrome 行为很多通过 `~/.claude/settings.json` 共享
- [[Sandboxing]] — Dev Container 提供另一层隔离运行环境
- [[Checkpointing]] — VS Code 中 hover message 即可 fork / rewind code
