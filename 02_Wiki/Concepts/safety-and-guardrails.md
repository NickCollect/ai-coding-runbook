---
name: Safety and Guardrails
type: concept
aliases: [Content Safety, Harm Avoidance, Content Filtering, Moderation, Refusals]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Safety 与 Guardrails（安全机制与护栏）

防止 LLM 生成有害、违规或危险内容的多层防御体系，包括模型训练层面的价值对齐、推理层面的内容过滤、以及应用层面的安全工程实践。

## 核心机制

安全机制分为三层：

**1. 训练层（模型内嵌）**
- 价值对齐训练（RLHF、Constitutional AI、DPO）使模型在训练阶段学习拒绝有害请求
- 某些类别（如 CSAM、大规模武器）为硬编码拒绝，不可通过任何 prompt 绕过

**2. 推理层（实时过滤）**
- Moderation API / Safety Filter：对输入和输出内容进行分类，触发阈值则拦截或警告
- 可配置阈值（部分类别可关闭，核心类别不可关闭）

**3. 应用层（开发者工程）**
- System prompt 限制主题范围
- 输入/输出 token 限制（防止 prompt injection、防止超范围内容）
- Human-in-the-loop 审核高风险操作
- 用户身份验证（KYC）和行为记录

## 跨厂商实现

**Claude**：Constitutional AI 是核心方法；分为 Anthropic 层（不可绕过）、Operator 层（system prompt 定义的业务规则）、User 层（对话中的用户指令）；operator 可拓展部分限制（如成人内容平台），也可收窄（限制主题）。有专门的 Prompt Injection 防护研究，Claude Opus 4.5 是重大改进节点。

**OpenAI**：提供免费 Moderation API（`/v1/moderations`）；7 大安全措施：内容审核、红队测试、人工审核、prompt 工程、KYC、token 限制、用户举报。4 个可调整害处类别，其余为固定限制。

**Gemini**：4 个可调整 harm category（harassment、hate speech、sexually explicit、dangerous content）；threshold 可配置；核心安全（儿童保护等）不可调整；鼓励 Safety Development Cycle（理解→修改→测试→监控）。

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| Safety settings / thresholds | Gemini：每个 harm category 的触发阈值 |
| `/v1/moderations` | OpenAI：免费内容审核端点 |
| `system` prompt 边界定义 | 所有厂商：通过 system prompt 指定业务范围 |
| `user` identifier | OpenAI：追踪滥用行为，违规时可精准吊销 |

## 使用场景

**必须配置**：面向公众的应用、处理敏感话题（医疗/法律/金融）、用户生成内容场景。

**最佳实践**：
- 输入和输出都做 moderation，不只检查输入
- 高风险操作（执行命令、支付、医疗建议）加 human-in-the-loop
- Prompt 层面先限制主题范围（防御性 system prompt）
- 记录用户接受 AI 免责声明

## 相关

- [[prompt-injection]] — 针对 safety 边界的攻击向量
- [[grounding]] — 通过检索事实减少有害幻觉
- [[system-prompt]] — safety 规则的主要注入点
- [[agents-guardrails--openai-docs]] — OpenAI agents 层面的 guardrail 设计

## 出现来源

- [[safety-best-practices--openai-docs]]
- [[safety-guidance--gemini-docs]]
- [[safety-settings--gemini-docs]]
- [[prompt-injection-defenses--anthropic-research]]
- [[frontier-threats-red-teaming-for-ai-safety--anthropic-news]]
