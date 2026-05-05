---
type: entity
name: Settings
aliases: [settings.json, user settings, project settings]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 配置文件（user / project / managed 三层）

## 关键属性

- 五层 scope 优先级（高→低）：**Managed**（不可覆盖）→ CLI args（临时）→ **Local**（`.claude/settings.local.json`，gitignored）→ **Project**（`.claude/settings.json`，committed）→ **User**（`~/.claude/settings.json`） [[settings]] [[glossary]]
- 数组类（如 `permissions.allow`/`deny`、`sandbox.filesystem.allowWrite`）跨 scope **合并**；scalar 被高优先级覆盖 [[settings]]
- Managed 来源多渠道：server-managed（Claude.ai admin console，Teams/Enterprise）、macOS plist `com.anthropic.claudecode`、Windows registry `HKLM\SOFTWARE\Policies\ClaudeCode\Settings`、文件 `managed-settings.json`（macOS `/Library/Application Support/ClaudeCode/`，Linux `/etc/claude-code/`，Windows `C:\Program Files\ClaudeCode\`）、drop-in 目录 `managed-settings.d/` 按字母合并 [[settings]] [[managed-settings]]
- Server-managed vs endpoint-managed：**同 tier 内 server 优先，且 source 不 merge** —— server-managed 一旦下发任何 key，endpoint-managed 整体忽略；用 `/status` 查谁生效 [[server-managed-settings]]
- `~/.claude.json` ≠ `~/.claude/settings.json`：前者存 OAuth session、MCP user/local 配置、per-project state（trust、allowed tools）、cache，**permissions / hooks / env 不在这里** [[settings]]
- `$schema` 字段 `https://json.schemastore.org/claude-code-settings.json` 启用编辑器自动补全和校验；自动保留最近 5 个 timestamped 备份 [[settings]]
- 关键 key 类目：`permissions.{allow,deny,ask}` + `allowManagedPermissionRulesOnly` / `disableBypassPermissionsMode` / `disableAutoMode`；`autoMode.{environment,allow,soft_deny}`；`sandbox.{filesystem,network,...}`；`hooks` + `disableAllHooks` / `allowedHttpHookUrls` / `allowManagedHooksOnly`；`enabledPlugins` / `blockedMarketplaces` / `strictKnownMarketplaces`；`statusLine` / `subagentStatusLine`；`model` / `availableModels` / `effortLevel` / `alwaysThinkingEnabled` [[settings]]
- 部分 key **只在 managed 生效**：`channelsEnabled` / `allowedChannelPlugins` / `allowManagedHooksOnly` / `allowManagedMcpServersOnly` / `allowManagedPermissionRulesOnly` / `blockedMarketplaces` / `strictKnownMarketplaces` / `pluginTrustMessage` / `forceRemoteSettingsRefresh` / `sandbox.filesystem.allowManagedReadPathsOnly` / `sandbox.network.allowManagedDomainsOnly` / `wslInheritsWindowsSettings` [[permissions--claude-code]] [[settings]]
- 安全护栏：`autoMode` **不读** shared `.claude/settings.json`（防止仓库注入 classifier 规则）；`autoMemoryDirectory` 不接受 project/local（防止 redirect 写入敏感路径） [[settings]] [[auto-mode-config]]
- `cleanupPeriodDays`（默认 30，最小 1）扫除 session / tasks / shell-snapshots / backups [[settings]]
- 其他可调：`editorMode`（normal|vim）、`autoUpdatesChannel`（stable|latest）、`apiKeyHelper`、`awsAuthRefresh`、`attribution.commit/pr`（git commit/PR 模板）、`disableDeepLinkRegistration`、`disableSkillShellExecution`、`agent`（主线程作为 named subagent 跑）、`defaultShell`（bash|powershell） [[settings]]
- Per-feature 文件分布：subagents 在 `agents/`、CLAUDE.md 在 `CLAUDE.md` 或 `.claude/CLAUDE.md`、MCP servers 在 `~/.claude.json` / `.mcp.json`、plugins 在各 settings.json 的 `enabledPlugins` [[settings]]
- 编辑入口：`/config` 打开 tabbed Settings UI 交互编辑；多数 key 也可在 UI 改 [[settings]]
- Server-managed 在 Bedrock/Vertex/Foundry/`ANTHROPIC_BASE_URL`（LLM gateway）下**完全不可用**，需直连 `api.anthropic.com` [[server-managed-settings]]
- MDM 最小模板示例：`{"permissions":{"disableBypassPermissionsMode":"disable"}}` —— 防止 user 用 `--dangerously-skip-permissions`，是企业部署最常见起点 [[managed-settings]]
- Server-managed fail-closed：`forceRemoteSettingsRefresh: true` 启动时阻塞直到刷新成功，CLI 在 fetch 失败时退出（自我延续，因为 cached 后续也强制） [[server-managed-settings]]

## 出现来源

_74 summaries reference this entity_:

- [[2026-w13]]
- [[2026-w15]]
- [[2026-w16]]
- [[2026-w17]]
- [[README--examples-settings]]
- [[admin-setup]]
- [[agent-teams]]
- [[amazon-bedrock]]
- [[authentication]]
- [[auto-mode-config]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[channels]]
- [[claude-code-features]]
- [[claude-code-on-the-web]]
- [[claude-directory]]
- [[cli-reference]]
- [[commands]]
- [[costs]]
- [[create-settings-command]]
- [[data-usage]]
- [[debug-your-config]]
- [[deep-links]]
- [[desktop]]
- [[devcontainer]]
- [[env-vars]]
- [[errors]]
- [[example-settings--plugin-dev]]
- [[fast-mode]]
- [[fullscreen]]
- [[github-enterprise-server]]
- [[glossary]]
- [[google-vertex-ai]]
- [[hook-development--SKILL]]
- [[hooks]]
- [[hooks-guide]]
- [[how-claude-code-works]]
- [[llm-gateway]]
- [[managed-settings]]
- [[mdm--repo-readme]]
- [[memory]]
- [[microsoft-foundry]]
- [[migration-guide]]
- [[model-config]]
- [[modifying-system-prompts]]
- [[monitoring-usage]]
- [[network-config]]
- [[output-styles]]
- [[parsing-techniques--plugin-settings]]
- [[permission-modes]]
- [[permissions]]
- [[permissions--claude-code]]
- [[plugin-settings--skill]]
- [[plugins]]
- [[plugins-reference]]
- [[real-world-examples]]
- [[sandboxing]]
- [[security]]
- [[server-managed-settings]]
- [[settings]]
- [[settings-bash-sandbox]]
- [[settings-lax--claude-code-repo]]
- [[settings-strict]]
- [[setup]]
- [[skills]]
- [[statusline]]
- [[sub-agents]]
- [[terminal-config]]
- [[third-party-integrations]]
- [[tools-reference]]
- [[troubleshoot-install]]
- [[voice-dictation]]
- [[vs-code]]
- [[zero-data-retention]]

## 相关

- [[Permission-mode]] — `permissions.*` / `disableBypassPermissionsMode` 等 settings key 决定 permission 行为
- [[Hooks]] — `hooks` key + `disableAllHooks` / `allowedHttpHookUrls` / `allowManagedHooksOnly` 在 settings 中配置
- [[Auto-mode]] — `autoMode.{environment, allow, soft_deny}` 在 settings 中声明，但**不**从 shared project settings 读取
- [[Sandboxing]] — `sandbox.*` 子树在 settings 中声明 OS 级 FS / network 隔离规则
- [[MCP-server]] — `enableAllProjectMcpServers` / `enabledMcpjsonServers` / `disabledMcpjsonServers` 等 MCP key
- [[Plugin]] — `enabledPlugins` / `blockedMarketplaces` / `strictKnownMarketplaces` 控制 plugin 启用与 marketplace
- [[Enterprise-gateway]] — Bedrock/Vertex/Foundry 下 server-managed settings 不可用，需走 endpoint-managed
