---
type: entity
name: Computer-use
aliases: [computer use, computer-use tool]
category: feature
status: ga
created: 2026-05-05
---

## 一句话定义

Claude 控制鼠标/键盘/屏幕的 tool

## 关键属性

- 内置 MCP server `computer-use`，让 Claude 在真实桌面控制鼠标 / 键盘 / 截屏；CLI 端为 research preview，**仅 macOS**，需 Pro/Max plan，Claude Code v2.1.85+，且只在 interactive mode 工作（无 `-p`） [[computer-use]]
- 所属"工具调用 tier"在 Claude 的优先策略里是最广也最慢——Claude 优先尝试 MCP server for the service → Bash → Chrome（如启用）→ Computer use；仅当目标无 API/CLI 时才落到 computer use [[computer-use]]
- 启用：CLI `/mcp` → 找 `computer-use`（per-project）→ Enable；首次需授 macOS Accessibility（点击/输入/滚动）+ Screen Recording（看屏幕）权限，Screen Recording 后可能需重启 Claude Code [[computer-use]]
- Per-app session 授权：启用 server 不等于授权所有 app；首次需要某 app 时终端 prompt 列出哪些 app + 额外权限（剪贴板等）+ 会被隐藏的 app 数；授权仅当前 session 有效 [[computer-use]]
- App tier 控制（与 Desktop 一致）：browsers / 交易平台 = view-only；terminals / IDEs = click-only（含 Terminal、iTerm、VS Code、Warp）；其他 = full control；Finder / System Settings 等敏感 app 有额外 sentinel 警告 [[computer-use]] [[desktop]]
- 机器级 lock——一次只能一个 Claude session 控制电脑；session crash 自动释放 [[computer-use]]
- 工作期间其他 app 自动隐藏，只与已授权 app 交互；终端始终可见且**从截图中排除**（Claude 看不到自己的输出）；turn 结束恢复 [[computer-use]]
- 截图自动降采样（16" MBP Retina 3456×2234 → ~1372×887），无配置项调整；如果文字 / 控件太小读不到，**应在应用内放大字号**而非改显示分辨率 [[computer-use]]
- macOS 通知 "Claude is using your computer · press Esc to stop"；**Esc**（任意位置）或 **Ctrl+C**（终端）立即中止释放 lock + 恢复隐藏 app；Esc 按键被消费防 prompt injection 用它关对话框 [[computer-use]]
- **不**通过 enterprise gateway 提供——Bedrock / Vertex / Foundry 用户不可用，需 direct Anthropic plan [[computer-use]]
- Desktop 端范围更广：macOS + Windows，Pro/Max（不含 Team/Enterprise），Settings → General 切换；可配置 denied apps 列表 + "结束后恢复隐藏 app" toggle [[desktop]]
- CLI vs Desktop 差异：Desktop 有 denied apps 配置 + Dispatch 集成；CLI 无 denied apps 配置但 auto-unhide 总是开 [[computer-use]] [[desktop]]
- Trust boundary 不同于 sandboxed Bash——computer use 跑在真实桌面无 sandbox；防护靠 per-app 授权 + sentinel 警告 + 终端排除 + global Esc + lock 文件 [[computer-use]] [[sandboxing]]
- 与 Chrome 集成的区别：Computer-use 面向 native macOS app；`Claude in Chrome` 面向浏览器（DOM-aware，更快），由独立的 `claude-in-chrome` MCP server 实现 [[computer-use]] [[chrome]]
- 排错：lock-held 报错（其他 session 占用）、permission 反复 prompt（重启 Claude Code、查 System Settings）、`/mcp` 看不到 `computer-use`（非 macOS / 旧版 / plan 不对 / 第三方 provider / 非 interactive 模式） [[computer-use]]

## 出现来源

_8 summaries reference this entity_:

- [[2026-w13]]
- [[2026-w14]]
- [[chrome]]
- [[computer-use]]
- [[desktop]]
- [[platforms]]
- [[sandboxing]]
- [[whats-new]]

## 相关

- [[MCP-server]] — Computer-use 实现为内置 MCP server `computer-use`，调用接口与其他 MCP 工具一致
- [[Sandboxing]] — Computer use 跑在真实桌面无 sandbox；与 Bash 的 OS 级 sandbox 是不同的 trust boundary
- [[Native-interface]] — Computer use 是 Claude 接触 CLI / Desktop 之外应用的最广泛通道
- [[IDE-integration]] — VS Code 扩展若装了 Chrome extension 也暴露 browser automation；computer-use 与 IDE 同属 Claude 触达外部环境的工具集
- [[Enterprise-gateway]] — computer use 不支持 enterprise gateway，仅 direct Anthropic plan
- [[Headless-mode]] — computer use 仅 interactive，`-p` headless 模式下不可用
