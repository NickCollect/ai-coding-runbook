---
name: OpenAI Batch API
type: entity
vendor: OpenAI
aliases: ["Batch API", "OpenAI Batch"]
created: 2026-05-05
---

# OpenAI Batch API

OpenAI 的异步批量推理接口，适合对延迟不敏感的大批量任务；提供相比同步 API 的价格折扣（*待确认*：具体折扣比例）。

## 关键属性

| 属性 | 值 |
|---|---|
| Vendor | OpenAI |
| 执行方式 | 异步，非实时 |
| 价格折扣 | *待确认*：50% off *（来自任务描述，未在已读 raw 文件中找到原文）* |
| 完成时间 | *待确认*：通常 24 小时内 |
| 主要用途 | 大批量文本生成、评估、分类任务 |

## 核心功能

Batch API 适合以下场景：
- 大规模评估（evals）和测试
- 批量文本分类、翻译、摘要
- 对实时响应无要求的数据处理流水线

### 工作流程

1. 将请求打包为 JSONL 文件上传
2. 创建 batch job，指定模型和请求列表
3. 轮询 job 状态（pending → in_progress → completed）
4. 下载结果文件

## API 示例

```python
# 上传 JSONL 请求文件
batch_input_file = client.files.create(
    file=open("requests.jsonl", "rb"),
    purpose="batch"
)

# 创建 batch job
batch = client.batches.create(
    input_file_id=batch_input_file.id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
)

# 检查状态
batch = client.batches.retrieve(batch.id)
print(batch.status)  # pending / in_progress / completed / failed
```

## 与 Claude 对应物

[[Batches-API]] — Anthropic 的 Message Batches API，功能定位相同：异步批量推理，最多 100K 请求/batch，24 小时完成窗口，50% 价格折扣。

## 出现来源

*注：当前 raw 文件中无专属 OpenAI Batch API 文档。本条目结构参照 [[Batches-API]] 对应物及通用批量处理模式构建，具体 OpenAI 参数以官方文档为准。*

## 相关

- [[OpenAI-Responses-API]] — 同步版接口
- [[Batches-API]] — Claude 对应物
