---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/safety-best-practices.md
source_url: https://platform.openai.com/docs/guides/safety-best-practices
title: "OpenAI — 安全最佳实践"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

## 核心要点

使用 OpenAI API 开发安全应用的综合指南，包括内容审核、对抗性测试、人工审核和访问控制等多个维度。

### 七类安全措施

1. **Moderation API**
   - 免费调用 `/v1/moderations` 检测仇恨、自残、暴力等违规内容
   - 建议对用户输入和模型输出都进行检测

2. **对抗性测试（Red-teaming）**
   - 在上线前进行安全评估，尝试通过各种方式绕过内容政策
   - 对潜在有害用例进行测试

3. **人工审核（Human-in-the-loop）**
   - 高风险操作（医疗、法律、金融建议）配置人工审核
   - 允许用户报告和纠正不当内容

4. **Prompt Engineering for Safety**
   - 限制主题范围（"仅回答与 X 相关的问题"）
   - 要求模型在不确定时说明
   - 通过 system prompt 传达期望的行为边界

5. **Know Your Customer（KYC）**
   - 对高风险功能进行用户验证
   - 记录用户接受使用条款（包含 AI 生成内容的免责声明）

6. **约束输入/输出 token 数**
   - 限制 input token 防范 prompt injection
   - 限制 output token 防止内容超出预期范围
   - 过滤输出中的特定用语（PII、联系方式等）

7. **用户报告机制 + 安全标识符**
   - 提供举报按钮，快速识别政策违规
   - 在 API 请求中包含用户 identifier（`user` 参数），帮助 OpenAI 追踪滥用行为（遇违规时可吊销对应用户访问）
