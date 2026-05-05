---
type: cheatsheet
topic: plugin-install-and-marketplace
last_updated: 2026-05-05
based_on:
  - 02_Wiki/Entities/Plugin.md
  - 02_Wiki/Entities/Plugin-marketplace.md
  - 02_Wiki/Summaries/plugins.md
  - 02_Wiki/Summaries/plugins-reference.md
  - 02_Wiki/Summaries/discover-plugins.md
---

# Plugin Install & Marketplace Cheatsheet

> Plugin 是 Claude Code 唯一支持 **versioned distribution** 的扩展容器。完整 [[Plugin]] [[Plugin-marketplace]]。

---

## 命令速查

```bash
# 浏览
claude plugin marketplace list                  # 已知 marketplaces
claude plugin marketplace add <url-or-repo>     # 加新 marketplace
claude plugin search <keyword>                  # 搜可装 plugin

# 安装
claude plugin install <plugin>[@marketplace]    # 默认 user scope
claude plugin install <plugin> --scope project  # 写入 .claude/settings.json
claude plugin install <plugin> --scope local    # 写入 .claude/settings.local.json
claude plugin install <plugin> --scope managed  # 企业 read-only 路径

# 管理
claude plugin list
claude plugin info <plugin>
claude plugin update <plugin>
claude plugin uninstall <plugin>

# 本地开发 / 测试
claude --plugin-dir ./my-plugin                 # 不装直接用本地路径
/reload-plugins                                 # session 内重载（不重启）

# 发布
claude plugin tag --push                        # 打 tag 并推
                                                # tag 格式 {name}--v{version}
```

---

## Scope 选择

| scope | 写到哪 | 用于 |
|---|---|---|
| `user`（默认） | `~/.claude/settings.json` | 跨项目个人工具 |
| `project` | `.claude/settings.json`（commit） | **团队共用**：装这个 plugin 是项目要求 |
| `local` | `.claude/settings.local.json`（gitignored） | 我自己在这个项目装的额外工具 |
| `managed` | OS 管理路径（read-only） | 企业 IT 推下来 |

---

## Marketplace 是啥

Plugin 的发现 / 分发渠道。形式可以是：
- **Git repo**（推荐）：repo 里有 `marketplace.json` 列出可装 plugins
- **HTTP URL**：JSON manifest endpoint
- **本地目录**：开发 / 内部 marketplace

加 marketplace：
```bash
claude plugin marketplace add anthropics/claude-code        # GitHub repo
claude plugin marketplace add https://my-co.com/claude-mp.json
claude plugin marketplace add ./my-local-marketplace
```

`marketplace.json` 结构（示例）：
```json
{
  "name": "my-marketplace",
  "plugins": [
    {
      "name": "code-review",
      "source": { "type": "git", "url": "github.com/me/code-review-plugin" },
      "versions": ["1.0.0", "1.1.0"]
    }
  ]
}
```

---

## Plugin 内部结构

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json              # 唯一允许放 .claude-plugin/ 里的文件
│
├── skills/                      # 强制 namespace: /my-plugin:skill-name
│   └── pdf-summarizer/SKILL.md
├── commands/                    # /my-plugin:command-name
│   └── analyze.md
├── agents/                      # subagents (注意: hooks/mcpServers/permissionMode 字段被忽略)
│   └── reviewer.md
├── hooks/
│   └── hooks.json
├── mcp-servers/
│   └── server.json              # 或 plugin.json 里 inline mcpServers
├── output-styles/
│   └── concise.md
├── monitors/                    # background processes (v2.1.105+)
│   └── monitors.json
├── lsp-servers/                 # language servers
│   └── lsp.json
└── themes/                      # 颜色主题
    └── dark-pro.json
```

**关键规则**：
- 组件目录都在 plugin **根**而非 `.claude-plugin/` 下
- 路径必须 relative 且 `./` 开头，禁止 `../` 或绝对路径
- `name` 必须 kebab-case：`/^[a-z][a-z0-9]*(-[a-z0-9]+)*$/`

---

## plugin.json 字段

最小：
```json
{
  "name": "my-plugin"
}
```

完整：
```json
{
  "name": "my-plugin",
  "version": "1.2.3",
  "description": "...",
  "author": { "name": "your-name", "email": "your@email.com" },
  "homepage": "https://...",
  "repository": "github.com/me/my-plugin",
  "license": "MIT",
  "keywords": ["productivity", "git"],
  "$schema": "https://claude.com/plugin.schema.json",

  "skills":      ["./skills/foo"],
  "commands":    ["./commands/bar.md"],
  "agents":      ["./agents/baz.md"],
  "hooks":       "./hooks/hooks.json",
  "mcpServers":  "./mcp-servers/server.json",
  "outputStyles":["./output-styles/concise.md"],
  "monitors":    "./monitors/monitors.json",
  "lspServers":  "./lsp-servers/lsp.json",
  "themes":      ["./themes/dark-pro.json"],

  "dependencies": [
    { "name": "shared-utils", "version": "^2.0", "source": "..." }
  ]
}
```

---

## Versioning

- `version` 走 **semver**（`1.2.3`）
- **省略 version** = 用 git commit SHA → "每个 commit 都是新版本"模式
- 显式写 version → 必须 bump 才能让用户 `claude plugin update` 拉到新版

`claude plugin tag --push`：
- 自动按 plugin.json 的 `name` + `version` 打 tag `{name}--v{version}`
- 例：`name: pr-review-toolkit, version: 1.2.0` → tag `pr-review-toolkit--v1.2.0`
- cache dir 名带 12-char SHA suffix → 防止 tag force-move 影响已装版本

---

## Plugin 间依赖（v2.1.110+）

```json
{
  "name": "my-plugin",
  "dependencies": [
    { "name": "shared-utils", "version": "^2.0" }
  ]
}
```

semver range：`~2.1.0` / `^2.0` / `>=1.4` / `=2.1.0`

**Cross-marketplace** 默认 blocked：在 root marketplace 的 `allowCrossMarketplaceDependenciesOn` 显式列出。

---

## Plugin 的两个核心 env var

| var | 值 | 用途 |
|---|---|---|
| `${CLAUDE_PLUGIN_ROOT}` | plugin 当前安装路径 | 引用打包的 binary / config / hooks 脚本（**update 后会变** —— 别 hard-code） |
| `${CLAUDE_PLUGIN_DATA}` | `~/.claude/plugins/data/{id}/` | 跨 update 持久化（node_modules / venv / cache） |

例 hook 配置：
```json
{
  "type": "command",
  "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/check.py"
}
```

例 MCP server：
```json
{
  "command": "node",
  "args": ["${CLAUDE_PLUGIN_ROOT}/server/index.js"]
}
```

---

## 易踩的坑

- **Plugin 内 subagent 的 `hooks`/`mcpServers`/`permissionMode` 字段被忽略**（安全限制）
- **Skills 在 plugin 内强制 namespace**：`/plugin-name:skill-name` —— 引用时记得带 prefix
- **`path traversal `../` 在 cache 里失效** —— 想多 plugin 共享代码用 plugin 内 symlink
- **`.claude-plugin/` 目录只能放 `plugin.json`** —— skills/agents/hooks 等必须放 plugin **根**
- **本地 `--plugin-dir` 同名时覆盖已装版本** —— 调试时可能屏蔽 production 版本
- **Marketplace plugin update 后旧 cache 7 天后才 GC** —— 旧版本暂留磁盘
- **官方 marketplace（`anthropic-agent-skills`）的 plugin 不能用 git pull 直接更新** —— 走 `claude plugin update`

---

## Anthropic 官方 marketplace 速查

`anthropics/claude-code` repo 自带的 plugins（`./plugins/` 目录，本 wiki raw 已抓）：

| Plugin | 用途 |
|---|---|
| `claude-opus-4-5-migration` | 老 model ID 迁移 |
| `code-review` | PR / commit 审查 |
| `feature-dev` | TDD 流程辅助 |
| `frontend-design` | UI 设计辅助 |
| `learning-output-style` | 教学风格 output |
| `plugin-dev` | 写 plugin 的 plugin |
| `pr-review-toolkit` | GitHub PR 工具集 |
| `ralph-wiggum` | 故意 misaligned 的玩具 |
| `security-guidance` | Edit 前注入安全提醒 |

`anthropics/skills` repo（marketplace 名 `anthropic-agent-skills`）打包：
- `document-skills`：xlsx / docx / pptx / pdf
- `example-skills`：algorithmic-art / brand-guidelines / canvas-design / mcp-builder / skill-creator etc.
- `claude-api`：API 使用辅助

---

## 详细引用

- [[Plugin]] · [[Plugin-marketplace]] · [[Skill]] · [[Hooks]] · [[MCP-server]] · [[Subagent]]
- [[Settings]] —— scope 配置在 settings.json 里
