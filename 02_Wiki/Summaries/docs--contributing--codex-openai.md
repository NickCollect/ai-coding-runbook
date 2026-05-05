---
type: summary
source: 01_Raw/github/openai/codex/docs/contributing.md
source_url: https://github.com/openai/codex/blob/main/docs/contributing.md
title: "Codex CLI 贡献指南"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Codex CLI 项目的贡献政策及受邀贡献者工作流。

**核心政策**：**外部代码贡献仅限受邀**。未经 Codex 团队成员明确邀请的 PR 将被关闭且不做 review。原因是团队认为社区最有价值的贡献是问题分析、复现细节、根因假设等讨论，而非直接提交代码。

**如何参与**：建议通过开 Issue 提 feature 请求或 bug 报告；若系统受邀，则按以下流程：从 `main` 建 topic 分支 → 专注单一改动 → 保证测试通过、lint 无警告。

**受邀贡献规范**：先在 issue 对齐方案 → 新增/更新测试（bug fix 要有覆盖） → 更新用户文档（如影响行为） → 每个 commit 可独立编译通过 → PR 填写 What/Why/How 模板并链接 issue。

**模型元数据更新**：涉及模型目录或元数据变更时，须显式设置 `input_modalities`，并覆盖不支持图片的行为路径测试。

**审查流程**：一位 maintainer 指派为主要 reviewer；超出已讨论范围的 PR 可能被关闭；达成共识后 squash-and-merge。

**CLA**：所有贡献者在 PR 中粘贴 "I have read the CLA Document and I hereby sign the CLA" 即完成签署；CLA-Assistant bot 自动记录。

**社区行为准则**：遵循 Contributor Covenant；安全漏洞发送至 security@openai.com。
