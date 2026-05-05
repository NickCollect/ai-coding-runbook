---
type: entity
name: Plugin-marketplace
aliases: [plugin marketplace, marketplace]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Plugin 的发现 / 分发渠道

## 关键属性

- 是 plugin 的发现 / 分发渠道：catalog 列出多个 plugin + 来源，user 先 `add` 一个 marketplace，再 `/plugin install <name>@<marketplace-name>` 装具体 plugin [[plugin-marketplaces]] [[discover-plugins]]
- **官方 marketplace `claude-plugins-official` 自动可用**，不用手动 add；浏览通过 `/plugin` Discover tab 或 [claude.com/plugins](https://claude.com/plugins)；提交 plugin 走 claude.ai / platform.claude.com 表单 [[discover-plugins]]
- Demo marketplace `claude-code-plugins`（来自 anthropics/claude-code 仓库）需手动 `/plugin marketplace add anthropics/claude-code` —— 含 13 个示例 plugin（agent-sdk-dev / commit-commands / code-review / hookify / plugin-dev / pr-review-toolkit / explanatory-output-style / learning-output-style / ralph-wiggum / security-guidance / feature-dev / frontend-design / claude-opus-4-5-migration） [[marketplace--claude-code-repo]]
- `marketplace.json` 必填字段：`name`（kebab-case）、`owner.name`、`plugins[]`；可选 `description` / `version` / `metadata.pluginRoot` / `allowCrossMarketplaceDependenciesOn` [[plugin-marketplaces]]
- 保留 marketplace 名（不能用，防止冒充）：`claude-code-marketplace`、`claude-code-plugins`、`claude-plugins-official`、`anthropic-marketplace`、`anthropic-plugins`、`agent-skills`、`knowledge-work-plugins`、`life-sciences` [[plugin-marketplaces]]
- Plugin 来源 source 类型：inline 字符串 `"./plugins/foo"` / `{source: "github", repo: "..."}` / git URL / local path / hosted `marketplace.json` URL [[plugin-marketplaces]] [[discover-plugins]]
- 版本机制 gotcha：`plugin.json` 设 `version` → 显式版本模式（**user 仅在你 bump 该字段才会更新**）；省略 `version` → 每个 commit 都视作新版本（更新可能噪音化） [[plugin-marketplaces]] [[plugins-reference]]
- 安装命令支持的 marketplace 引用方式：GitHub `owner/repo`（找 `.claude-plugin/marketplace.json`）、git URL（GitLab/Bitbucket/self-hosted）、local 目录或 `marketplace.json` 路径、远程 hosted URL；shortcuts: `/plugin market` / `rm` 等 [[discover-plugins]]
- 官方 marketplace 类目：**Code intelligence**（LSP plugins，每个语言要单独装 language-server binary，如 `pyright-langserver`）、**External integrations**（pre-configured MCP servers：github / gitlab / atlassian / asana / linear / notion / figma / vercel / firebase / supabase / slack / sentry）、**Development workflows**、**Output styles** [[discover-plugins]]
- Plugin 安装后路径：marketplace plugin 被复制到 `~/.claude/plugins/cache`（每版本独立）；旧版本在更新/卸载 7 天后标记 orphaned；**跨 plugin 文件引用如 `../shared-utils` 无效**，要用 plugin 根内的 symlink [[plugin-marketplaces]] [[plugins-reference]]
- 安装 scope 三选：User（跨所有项目）/ Project（合作者也启用）/ Local（只本人本仓库）；安装后跑 `/reload-plugins` 激活 [[discover-plugins]]
- Plugin 命名空间：plugin 内 skill 自动 namespaced 为 `plugin-name:skill-name`（如 `commit-commands:commit`） [[discover-plugins]]
- 企业级管理：managed settings 用 `blockedMarketplaces` 黑名单 / `strictKnownMarketplaces` 白名单 / `pluginTrustMessage` 自定义信任提示，**仅 managed scope 生效** [[permissions--claude-code]]
- LSP 排错：若 `/plugin` Errors tab 报 "Executable not found in $PATH"，需安装表里列的 language-server binary [[discover-plugins]]
- Marketplace-grade 命令设计要点：跨平台 `case $(uname)` 探测 / 命名空间防冲突 / 用 `${VAR:-default}` sensible default / 明确 deprecation 路径 / `KEYWORDS:` HTML 注释让市场搜索发现 [[marketplace-considerations]]

## 出现来源

_26 summaries reference this entity_:

- [[README--examples-settings]]
- [[README--plugin-dev]]
- [[admin-setup]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[channels-reference]]
- [[code-review]]
- [[commands]]
- [[create-plugin]]
- [[discover-plugins]]
- [[features-overview]]
- [[github-enterprise-server]]
- [[marketplace--claude-code-repo]]
- [[marketplace-considerations]]
- [[permissions--claude-code]]
- [[plugin-dependencies]]
- [[plugin-marketplaces]]
- [[plugins]]
- [[plugins--agent-sdk]]
- [[plugins-reference]]
- [[settings]]
- [[settings-lax--claude-code-repo]]
- [[settings-strict]]
- [[skills--marketplace]]
- [[skills--repo-readme]]
- [[vs-code]]

## 相关

- [[Plugin]] — marketplace 是 plugin 的发现 / 分发渠道，分发的就是 plugin
- [[Skill]] — plugin 主要打包内容之一是 skill，跨 marketplace 安装后 namespaced 为 `plugin-name:skill-name`
- [[Settings]] — `enabledPlugins` / `blockedMarketplaces` / `strictKnownMarketplaces` 在 settings.json 控制 marketplace 可用性
- [[MCP-server]] — 官方 marketplace "External integrations" 类目核心是 pre-configured MCP servers
- [[Slash-command]] — plugin 通过 marketplace 分发的 slash command 需考虑命名空间冲突 / 跨平台兼容
