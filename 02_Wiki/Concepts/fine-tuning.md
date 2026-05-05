---
name: Fine-tuning
type: concept
aliases: [Model Fine-tuning, SFT, DPO, RFT, Model Customization, RLHF]
vendors: [Claude, OpenAI, Gemini]
created: 2026-05-05
---

# Fine-tuning（模型微调）

通过在特定数据集上继续训练预训练模型的权重，使其内化特定行为、风格或领域知识的技术。与 prompt engineering 的区别在于：修改的是模型参数而非输入文本。

## 核心机制

Fine-tuning 工作流（以 OpenAI 为例）：

1. **建立 baseline**：先写 eval，量化当前模型的基准表现
2. **Prompt Engineering 先行**：提供 context、清晰指令、few-shot 示例——若能解决问题则无需微调
3. **准备训练数据**：JSONL 格式的 input/output 配对（SFT）或偏好对（DPO）
4. **提交微调任务**：上传数据 → 创建 fine-tuning job → 等待完成
5. **评估**：在代表性数据上跑 eval，与 baseline 对比
6. **迭代**：根据结果调整数据或超参数

**三种主要范式**：
- **SFT（Supervised Fine-Tuning）**：标注输入/输出对，直接优化 cross-entropy 损失
- **DPO（Direct Preference Optimization）**：提供"好的回答"vs"差的回答"偏好对，优化风格/语气
- **RFT（Reinforcement Fine-Tuning）**：用可验证的 reward 函数训练复杂推理任务（如医疗诊断、法律分析）

## 跨厂商实现

**Claude**：Anthropic 于 2024 年推出 Claude 3 Haiku fine-tuning（有限 beta）。目前不对外开放常规 fine-tuning；Constitutional AI 是 Anthropic 训练模型的核心方法，不暴露给开发者。

**OpenAI**：最成熟的生态。支持 `gpt-4.1-2025-04-14` 系列的 SFT 和 DPO；支持 `o4-mini` 的 RFT；通过 Dashboard 或 API 发起任务。

**Gemini**：通过 Google AI Studio 提供 Model Tuning（Supervised Fine-Tuning）；支持 Gemini 1.5 Flash 等模型；Vertex AI 提供企业级管道。

## 关键参数 / API 表面

| 参数 | 说明 |
|---|---|
| 训练数据量 | SFT 通常需 50–1000 条以上高质量样本 |
| Epochs | 训练轮次；过多易过拟合 |
| Learning rate multiplier | 微调时的学习率倍数 |
| Validation split | 用于监控过拟合的验证集比例 |

## 使用场景

**优先选 fine-tuning**：
- 示例数量超出 context window 容量
- 需要稳定内化私有词汇/格式（无需每次 prompt 携带）
- 生产路径对 latency/cost 极度敏感（短 prompt 替代长 few-shot）
- Prompt 无法稳定修正的指令遵循失败

**不选 fine-tuning**（先用 prompt engineering）：
- 知识截止日期问题（fine-tuning 不注入新知识，用 RAG 解决）
- 任务/需求仍在快速变化
- 数据集太小（<50 条）

## 相关

- [[prompt-engineering]] — fine-tuning 前的必要步骤
- [[few-shot-learning]] — fine-tuning 可内化 few-shot 示例的效果
- [[rag]] — 注入新知识用 RAG，改变行为用 fine-tuning

## 出现来源

- [[fine-tuning--openai-docs]]
- [[model-tuning--gemini-docs]]
- [[fine-tune-claude-3-haiku--anthropic-news]]
