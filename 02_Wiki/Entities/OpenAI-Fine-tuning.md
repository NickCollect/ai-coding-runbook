---
name: OpenAI Fine-tuning
type: entity
vendor: OpenAI
aliases: ["Fine-tuning", "SFT", "DPO", "RFT", "model fine-tuning"]
created: 2026-05-05
---

# OpenAI Fine-tuning

在 prompt engineering 基础上进一步优化模型行为的训练机制，支持三种方法：SFT（监督学习）、DPO（偏好优化）、RFT（强化微调）。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| 支持方法 | SFT / DPO / RFT |
| SFT/DPO 支持模型 | `gpt-4.1-2025-04-14` 系列 |
| RFT 支持模型 | `o4-mini-2025-04-16` |
| 数据格式 | JSONL |
| 主要优势 | 超出 context window 的样本量、更短 prompt、专有数据训练 |

## 核心功能

### 三种 Fine-tuning 方法

| 方法 | 全称 | 适用场景 |
|---|---|---|
| **SFT** | Supervised Fine-Tuning | 分类、翻译、特定格式生成、修正指令遵循失败 |
| **DPO** | Direct Preference Optimization | 文本摘要风格、对话语气调整 |
| **RFT** | Reinforcement Fine-Tuning | 复杂领域任务（医疗诊断、法律案例分析） |

### 推荐工作流

1. 写 eval 建立 baseline
2. Prompt 工程优化
3. 可选 fine-tuning
4. 用代表性数据跑 eval
5. 根据反馈调整
6. 持续迭代

**最佳实践**：fine-tune 前先尝试 prompt engineering（相关 context + 清晰指令 + few-shot 示例）。

### 相对纯 prompting 的优势

- 提供比 context window 容纳更多的训练示例
- 用更短 prompt 达到相同效果（节省 token 成本）
- 使用专有或敏感数据而无需每次请求包含
- 训练更小、更快、更便宜的专用模型

## API 示例

```python
# 上传训练数据
training_file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# 创建 fine-tuning job（SFT）
job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model="gpt-4.1-2025-04-14",
)

# RFT 需额外定义 grader
```

## 与 Claude 对应物

Anthropic 目前提供 Claude 3 Haiku 的 fine-tuning（详见 [[fine-tune-claude-3-haiku--anthropic-news]]），支持 SFT，定位与 OpenAI SFT 相同。

## 出现来源

- [[fine-tuning--openai-docs]]

## 相关

- [[OpenAI-Responses-API]] — fine-tuned 模型通过 Responses API 调用
- [[Structured-outputs]] — fine-tuning 常用于强化特定输出格式
