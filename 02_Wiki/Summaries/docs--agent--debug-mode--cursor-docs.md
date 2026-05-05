---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--debug-mode.md
source_url: https://cursor.com/docs/agent/debug-mode
title: "Debug Mode"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Debug Mode 通过运行时证据（而非猜测）定位难以复现或理解的 Bug，适合标准 Agent 交互难以解决的棘手问题。

**适用场景**：能复现但原因不明的 Bug、竞争条件/时序问题、性能问题/内存泄漏、回归（曾经正常现在失效）。

**工作流程**：
1. **探索与假设**：Agent 遍历相关文件，建立多个根因假设
2. **添加插桩**：Agent 插入日志语句，数据发送至 Cursor 扩展中的本地 debug server
3. **复现 Bug**：Debug Mode 要求用户按指定步骤复现，保持用户在循环中
4. **分析日志**：Agent 审查收集到的日志，基于运行时证据定位真实根因
5. **精准修复**：通常只需修改几行代码的靶向修复
6. **验证并清理**：确认修复后，Agent 移除所有插桩代码

**使用技巧**：提供详细 Bug 描述和复现步骤；严格按 Agent 给出的步骤操作；对竞争条件可多次复现；明确说明期望行为与实际行为的差异。
