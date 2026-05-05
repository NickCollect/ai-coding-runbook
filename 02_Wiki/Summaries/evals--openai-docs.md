---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/evals.md
source_url: https://platform.openai.com/docs/guides/evals
title: "OpenAI — Working with Evals（评估）"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

## 核心要点

Evals 是测试模型输出是否符合预定标准的工具，类似 BDD，先定义行为再实现和测试。

### 三步流程

1. 将任务描述为 eval
2. 用测试输入运行 eval（prompt + 输入数据）
3. 分析结果，迭代优化 prompt

### 创建 eval（API）

关键参数：
- `data_source_config`：测试数据的 JSON schema
- `testing_criteria`：判断模型输出是否正确的 grader

```python
eval_obj = client.evals.create(
    name="IT Ticket Categorization",
    data_source_config={
        "type": "custom",
        "item_schema": {
            "type": "object",
            "properties": {
                "ticket_text": {"type": "string"},
                "correct_label": {"type": "string"},
            },
            "required": ["ticket_text", "correct_label"],
        },
        "include_sample_schema": True,
    },
    testing_criteria=[
        {
            "type": "string_check",
            "name": "Match output to human label",
            "input": "{{ sample.output_text }}",
            "operation": "eq",
            "reference": "{{ item.correct_label }}",
        }
    ],
)
```

### 模板语法

- `{{ item.field_name }}`：来自测试数据集的字段值
- `{{ sample.output_text }}`：模型生成的输出

### 上传测试数据

JSONL 格式，purpose 设为 `"evals"`：

```json
{ "item": { "ticket_text": "My monitor won't turn on!", "correct_label": "Hardware" } }
```

### 创建 eval run

指定 `eval_id`、`model`、`input_messages` 模板、`source`（file_id）。Run 异步执行，支持 webhook 通知（`eval.run.succeeded` 等事件）。

### 结果结构

`result_counts`（total/errored/failed/passed）、`per_model_usage`（token 使用）、`per_testing_criteria_results`（各 grader 通过率）、`report_url`（dashboard 链接）。
