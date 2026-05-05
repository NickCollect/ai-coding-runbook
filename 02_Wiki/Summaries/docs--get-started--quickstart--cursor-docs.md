---
type: summary
source: 01_Raw/docs.cursor.com/docs--get-started--quickstart.md
source_url: https://cursor.com/docs/get-started/quickstart
title: "Quickstart 快速上手"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Cursor 从安装到第一次实质性代码改动的快速入门指南。

**安装平台**：macOS 12+（dmg，支持 Apple Silicon 和 Intel）、Windows 10+（exe）、Linux（推荐 Debian/Ubuntu apt 包或 RHEL/Fedora yum 包，也提供 AppImage 便携版）。

**四步工作流**：
1. **安装并登录**：下载 Cursor，打开后登录，选择项目文件夹
2. **理解代码库**：Cmd+I 打开 Agent，让 Cursor 解释代码库入口点和关键模块
3. **做一个小改动**：请 Cursor 建议 3 个安全改进，选一个执行（推荐从低风险改动开始）
4. **审查 diff 并验证**：查看 Agent 的变更差异，要求运行测试/类型检查/lint

**进阶**：复杂任务使用 Plan Mode（Shift+Tab 切换），Agent 将先调研代码库、提问澄清、生成方案后等待批准再执行。
