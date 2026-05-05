---
type: summary
source: 01_Raw/docs.cursor.com/docs--agent--tools--browser.md
source_url: https://cursor.com/docs/agent/tools/browser
title: "Browser Tool"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Agent 内置浏览器工具，可控制浏览器进行测试、视觉编辑、无障碍审计、设计转代码等，无需额外安装配置。

**浏览器能力**：Navigate（访问 URL）、Click（点击/双击/悬停）、Type（表单填写）、Scroll（页面滚动）、Screenshot（截图）、Console Output（控制台日志）、Network Traffic（网络请求监控，当前仅 Agent 面板支持）。

**设计侧边栏（Design sidebar）**：可直接在 Cursor 内对网页进行可视化编辑，包含位置/布局、尺寸、颜色、外观（阴影/透明度/圆角）、主题切换（亮/暗）。点击 apply 触发 Agent 将视觉修改转为代码变更，也可选中多个元素并行处理。

**会话持久化**：Cookie、localStorage、IndexedDB 在 Agent 会话间保持（按工作区隔离）。

**安全**：Token 认证、Tab 隔离、每次会话令牌刷新；工具默认需手动审批；支持白名单/黑名单配置；Cursor 内置浏览器经多家外部安全机构审计。

**企业**：通过 MCP 控制台管理浏览器功能的启用，可配置 Origin 白名单限制 Agent 可自动导航的域名范围。

**推荐模型**：Sonnet 4.5、GPT-5、Auto。
