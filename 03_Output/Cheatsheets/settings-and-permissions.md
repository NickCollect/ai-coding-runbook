---
type: cheatsheet
topic: settings-and-permissions
last_updated: 2026-05-05
based_on:
  - 02_Wiki/Entities/Settings.md
  - 02_Wiki/Entities/Permission-mode.md
  - 02_Wiki/Entities/Sandboxing.md
  - 02_Wiki/Entities/Auto-mode.md
---

# Settings & Permissions Quick Reference

> Claude Code 的配置是**多层 cascading**。这份 cheatsheet 速查"哪个 setting 写哪儿、谁覆盖谁、怎么调权限"。

---

## Settings 加载顺序（高优先 → 低优先）

| 层 | 路径 | 谁 commit | 用途 |
|---|---|---|---|
| **managed** | OS 特定（macOS `/Library/...`、Linux `/etc/claude-code/`、Windows reg） | 企业管理员，**read-only** | 公司硬性 policy（lockdown / allowed-plugins） |
| **CLI flag** | 命令行 | session-only | `--allowedTools` `--permissionMode` 等 |
| **project local** | `.claude/settings.local.json` | **gitignored** | 个人在该项目的私设（凭据） |
| **project shared** | `.claude/settings.json` | **commit 进 repo** | 团队共识（hooks / 规范） |
| **user** | `~/.claude/settings.json` | 个人 | 跨项目偏好（model / output-style） |
| **default** | 内置 | — | Anthropic 默认值 |

冲突规则：**字段级 deep-merge，高优先覆盖低优先**。`hooks` / `permissions` 这种**多 entry 字段是合并**（不是覆盖）。

---

## 常用 setting 速查

```json
// ~/.claude/settings.json — 全局个人偏好
{
  "model": "sonnet",                  // 默认对话模型
  "outputStyle": "default",           // 输出风格
  "permissionMode": "default",        // 默认权限模式
  "autoUpdates": true,
  "telemetry": false,
  "memory": {
    "autoMemoryEnabled": true         // /memory 自动记
  }
}
```

```json
// .claude/settings.json — 项目共识（commit）
{
  "permissions": {
    "allow": ["Bash(npm:*)", "Bash(git:*)", "Edit(src/**)"],
    "deny":  ["Bash(rm -rf:*)", "Edit(.env*)"]
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash", "hooks": [{"type": "command", "command": "scripts/lint-bash.sh"}] }
    ]
  },
  "enabledMcpServers": ["github", "filesystem"],
  "skills": {
    "disableSkillShellExecution": false
  }
}
```

```json
// .claude/settings.local.json — 个人本地（gitignored）
{
  "permissions": {
    "allow": ["Bash(docker:*)"]      // 我本地装了 docker，团队没都装
  },
  "envOverrides": {
    "DEBUG": "true"
  }
}
```

---

## Permission Modes

| mode | tool 调用怎么处理 | 适合场景 |
|---|---|---|
| `default` | 每个 tool 都问；记忆"always allow this rule" | 新仓 / 不熟悉的项目 |
| `acceptEdits` | Edit/Write 自动通过；其他还是问；**不绕过 deny rule** | 熟悉的项目，写代码为主 |
| `auto` | 用户配的 allow rules 自动过；剩下问 / 拒；可配 `autoMode` 详细 | 长任务、CI |
| `bypassPermissions` | **全部自动通过**（除非 deny rule / managed deny） | **危险**：仅 sandbox 环境用 |
| `plan` | 只读模式（写操作全拒）+ 生成 plan 后停 | 让 Claude 计划改动，自己 review |

切换：`/permissions` 进交互式管理；或启动时 `--permissionMode <mode>`；或 `--dangerously-skip-permissions` = `bypassPermissions`。

---

## Permission Rule 语法

```
Bash(git *)          # tool name + 参数 glob
Bash(git commit *)   # 更细
Edit(*.ts)           # tool + 文件 glob
Edit(src/**)         # 递归 glob
Read(/etc/**)        # 文件路径
mcp__github__*       # MCP tool wildcard 整 server 放过
WebFetch(https://example.com/*)   # URL pattern
Skill(my-skill)      # 单个 skill
Skill(my-skill *)    # skill 任意 args
```

放在 settings 的 `permissions.allow` / `permissions.deny`。**deny 永远胜出**（即使 `bypassPermissions`）。

---

## Auto-mode 配置

`auto` 模式下，配 `autoMode` 字段精细控制：

```json
{
  "permissionMode": "auto",
  "autoMode": {
    "allow": ["Bash(npm:*)", "Edit(src/**)"],   // 这些自动过
    "ask":   ["Bash(git push *)"],              // 这些弹框
    "deny":  ["Bash(rm -rf *)"]                 // 这些拒
  }
}
```

`auto` 比 `acceptEdits` 更细：可以精确说"哪些 Bash 命令自动过、哪些要确认"。

---

## Sandboxing

Claude Code 跑 Bash 命令的 sandbox 选项（[[Sandboxing]]）：

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowedReads":  ["~/repos/*", "/tmp/**"],
      "allowedWrites": ["~/repos/myproject/**"]
    },
    "network": "deny" | "allow" | { "allowedHosts": ["github.com"] }
  }
}
```

或者用 `npx @anthropic-ai/sandbox-runtime <cmd>` 在 sandbox 里跑某条特定命令（也用于 MCP server 隔离）。

---

## Memory & Auto-memory

```json
{
  "memory": {
    "autoMemoryEnabled": true,
    "autoMemoryPolicies": {
      "user": "include",      // ~/.claude/CLAUDE.md 自动注入
      "project": "include",   // ./CLAUDE.md
      "local": "include"      // .claude/local-memory.md
    }
  }
}
```

详见 [[Memory]]。Memory 跟 Settings 是不同机制，但配置入口都在 settings.json。

---

## 跨产品 / Enterprise

| 想干 | 在哪配 |
|---|---|
| 锁定团队只能用某些 plugin | managed `enabledPlugins: [...]` + `allowManagedHooksOnly` |
| 走公司的 LLM gateway（不直连 Anthropic API） | `~/.claude/settings.json` 的 `apiBaseUrl` + `apiKey` |
| 用 AWS Bedrock | `apiProvider: "bedrock"` + AWS 凭据 |
| 用 GCP Vertex AI | `apiProvider: "vertex"` + GCP 凭据 |
| 用 Microsoft Foundry | `apiProvider: "azure"` + Azure 凭据 |
| 关掉 telemetry | `telemetry: false` |
| 关 auto-update | `autoUpdates: false` |

---

## 调试

- `/config` 交互看当前 effective settings
- `claude --debug-config` 一次性 dump merged settings JSON
- `~/.claude/logs/` 看启动日志（哪些 settings file 被加载）
- 改了 settings 不生效 → 多半是 `.claude/settings.local.json` 覆盖了

---

## 易踩的坑

- **`.claude/settings.local.json` 必须 gitignored**（含密钥时尤其） —— 默认 gitignore 模板里
- **`bypassPermissions` ≠ "无视所有限制"** —— managed deny rule 仍生效
- **deny 永远胜 allow**（多个 hook 命中时也是这个规则）
- **`hooks` 和 `permissions` 字段 merge 不覆盖** —— 写到 user settings 跟 project settings 会**叠加**而不是 user 被 project 覆盖
- **MCP tool 默认必须显式 `allowedTools` 才能调用** —— wildcard `mcp__github__*` 放过整 server

---

## 详细引用

- [[Settings]] · [[Permission-mode]] · [[Sandboxing]] · [[Auto-mode]] · [[Memory]]
- [[Enterprise-gateway]] —— Bedrock / Vertex / Foundry / LLM Gateway
- [[Hooks]] —— 与 permissions 的交互
