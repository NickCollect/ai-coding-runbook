---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/fine-tuning.md
source_url: https://platform.openai.com/docs/guides/fine-tuning
title: "OpenAI — 模型优化与 Fine-tuning"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

## 核心要点

Fine-tuning 是在 prompt engineering 之上进一步优化模型行为的手段，主要有三种方法。

### 优化工作流

1. 写 eval 建立 baseline → 2. Prompt 工程 → 3. 可选 fine-tuning → 4. 用代表性数据跑 eval → 5. 根据反馈调整 → 6. 持续迭代

### 三种 Fine-tuning 方法

| 方法 | 适用场景 | 支持模型 |
|---|---|---|
| **SFT**（Supervised）| 分类、翻译、特定格式生成、修正指令遵循失败 | `gpt-4.1-2025-04-14` 系列 |
| **DPO**（Direct Preference Optimization）| 文本摘要风格、对话语气调整 | `gpt-4.1-2025-04-14` 系列 |
| **RFT**（Reinforcement Fine-Tuning）| 复杂领域任务（医疗诊断、法律案例分析）| `o4-mini-2025-04-16` |

### Fine-tuning 流程

1. 收集训练数据集
2. 上传到 OpenAI（JSONL 格式）
3. 创建 fine-tuning job（dashboard 或 API）
4. RFT：定义 grader 评分模型行为
5. 评估结果

### 相对 prompting 的优势

- 提供比 context window 能容纳更多的示例
- 用更短 prompt 达到相同效果（节省 token 成本）
- 使用专有/敏感数据而无需每次请求都包含
- 训练更小、更快、更便宜的专用模型

### 最佳实践

**Fine-tune 前先尝试 prompt engineering**：提供相关 context、清晰指令、few-shot 示例。
