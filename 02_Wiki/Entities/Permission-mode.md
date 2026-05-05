---
type: entity
name: Permission-mode
aliases: [permission mode, permission modes]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude Code 工具调用授权策略（plan / accept-edits / bypass-permissions / default 等）

## 关键属性

- 控制 Claude Code 何时为文件编辑 / shell 命令 / 网络请求 prompt 用户；共 6 种模式：`default`（仅读不问）、`acceptEdits`（自动批 edits + 常用 FS bash）、`plan`（只读 + 规划）、`auto`（classifier 把关）、`dontAsk`（仅 pre-approved 工具，全静音）、`bypassPermissions`（一切放行） [[permission-modes]]
- 切换：CLI 用 `Shift+Tab` 循环 `default → acceptEdits → plan`（开了 bypass / auto 也插入循环），`--permission-mode <mode>` 启动指定，`defaultMode` 设置持久化 [[permission-modes]]
- `acceptEdits` 自动批 `mkdir`/`touch`/`mv`/`cp`/`rm`/`rmdir`/`sed` 及包了 `LANG=C`/`NO_COLOR=1`/`timeout`/`nice`/`nohup` 的等价命令；只对 cwd 或 `additionalDirectories` 内路径生效，protected paths 仍 prompt [[permission-modes]]
- Plan mode 完全只读，进入方式：`Shift+Tab` / `/plan` 前缀 / `--permission-mode plan`；批准菜单可一键转 auto / accept-edits / 手工 review；`Ctrl+G` 在编辑器开 plan 直接改 [[permission-modes]]
- Auto mode（v2.1.83+，research preview）：classifier model 评估每次工具调用，连续 3 次或累计 20 次 block 后自动暂停回到 prompt；headless `-p` 在重复 block 后中止 [[permission-modes]]
- Auto mode 仅限 Max / Team / Enterprise / API plan（不支持 Pro），且只用 Sonnet 4.6 / Opus 4.6 / Opus 4.7（Max 仅 Opus 4.7），且仅 Anthropic API（不支持 Bedrock / Vertex / Foundry） [[permission-modes]] [[auto-mode-config]]
- Auto mode 默认 block：`curl|bash`、外发敏感数据、prod deploy/migration、批量云删除、IAM 改动、shared infra 改动、不可逆删除 pre-session 文件、force push、push 到 `main` [[permission-modes]]
- Auto mode 进入时丢弃 blanket `Bash(*)` / `PowerShell(*)` / 通配解释器 / `Agent` 规则，离开时恢复；subagent `permissionMode` frontmatter 在 auto mode 下被忽略 [[permission-modes]]
- `dontAsk` 把 `ask` 规则当 deny；非 `permissions.allow` + 只读 bash 之外的全拒；完全 non-interactive [[permission-modes]]
- `bypassPermissions` 必须用 `--permission-mode bypassPermissions` / `--dangerously-skip-permissions` / `--allow-dangerously-skip-permissions` 启动；v2.1.126+ 连 protected paths 都跳过，但 `rm -rf /` 和 `rm -rf ~` 仍 prompt 作 circuit breaker [[permission-modes]]
- Protected paths（除 bypass 外永不自动批）：`.git`、`.vscode`、`.idea`、`.husky`、`.claude`（除 `commands`/`agents`/`skills`/`worktrees`），文件 `.gitconfig`、`.gitmodules`、shell rc、`.ripgreprc`、`.mcp.json`、`.claude.json` [[permission-modes]]
- Agent SDK 评估顺序：hooks → deny rules → permission mode → allow rules → `canUseTool` callback；deny 永远赢，即使 `bypassPermissions` [[permissions]]
- Subagent 在父级是 bypass / acceptEdits / auto 时**强制继承且无法 override**——bypass + 宽松 system prompt 可能给 subagent 完整自主访问 [[permissions]]
- Desktop UI 把模式显示为 *Ask permissions* / *Auto accept edits* / *Plan mode* / *Auto* / *Bypass permissions*；Remote sessions 仅支持 Auto-accept-edits + Plan mode；`dontAsk` 仅 CLI [[permission-modes]]
- 可中途变更：TS `setPermissionMode()` / Python `set_permission_mode()`；常见 pattern 是先严后松（启动 strict，看到初始动作没问题再放宽） [[permissions]]

## 出现来源

_67 summaries reference this entity_:

- [[2026-w14]]
- [[2026-w15]]
- [[2026-w16]]
- [[README--examples-settings]]
- [[admin-setup]]
- [[agent-loop]]
- [[agent-sdk-verifier-py]]
- [[agent-sdk-verifier-ts]]
- [[agent-teams]]
- [[auto-mode-config]]
- [[best-practices]]
- [[champion-kit]]
- [[changelog]]
- [[changelog--claude-code-repo]]
- [[channels]]
- [[claude-code-on-the-web]]
- [[claude-issue-triage]]
- [[cli-reference]]
- [[commands]]
- [[common-workflows]]
- [[communications-kit]]
- [[costs]]
- [[custom-tools--agent-sdk]]
- [[debug-your-config]]
- [[desktop]]
- [[desktop-quickstart]]
- [[desktop-scheduled-tasks]]
- [[devcontainer]]
- [[errors]]
- [[file-checkpointing]]
- [[gitlab-ci-cd]]
- [[glossary]]
- [[headless]]
- [[hooks]]
- [[hooks--agent-sdk]]
- [[hooks-guide]]
- [[how-claude-code-works]]
- [[interactive-mode]]
- [[jetbrains]]
- [[keybindings]]
- [[managed-settings]]
- [[mcp--agent-sdk]]
- [[mdm--repo-readme]]
- [[model_behavior]]
- [[overview--agent-sdk]]
- [[permission-modes]]
- [[permissions]]
- [[permissions--claude-code]]
- [[python]]
- [[quickstart--agent-sdk]]
- [[remote-control]]
- [[sandboxing]]
- [[secure-deployment]]
- [[security]]
- [[server-managed-settings]]
- [[settings]]
- [[settings-bash-sandbox]]
- [[settings-lax--claude-code-repo]]
- [[settings-strict]]
- [[sub-agents]]
- [[subagents--agent-sdk]]
- [[tools-reference]]
- [[typescript--agent-sdk]]
- [[ultraplan]]
- [[user-input]]
- [[vs-code]]
- [[web-quickstart]]

## 相关

- [[Auto-mode]] — `auto` 是 permission mode 的一种，由 classifier model 决策，规则全在 `autoMode.environment`
- [[Sandboxing]] — sandbox 与 permissions 互补：permissions 管"哪些工具 / 哪些输入"，sandbox 管"Bash + 子进程的 OS 级访问"
- [[Hooks]] — `PreToolUse` 在 deny rules 之前评估，可 allow / deny / 通过；`PermissionDenied` hook 可程序化反应
- [[Settings]] — `permissions.allow/deny`、`defaultMode`、`autoMode` 等都在 settings.json 配置，作用域可叠加
- [[Subagent]] — 父级 bypass/acceptEdits/auto 时 subagent 强制继承，frontmatter `permissionMode` 失效
- [[Agent-SDK]] — SDK 用 `permissionMode` 选项 + `canUseTool` callback 实现同套语义
- [[Headless-mode]] — `-p` 模式无人交互，auto mode 重复 block 时直接中止，不能像 CLI 那样 fallback 到 prompt
