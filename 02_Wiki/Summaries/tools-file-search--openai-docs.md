---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/tools-file-search.md
source_url: https://platform.openai.com/docs/guides/tools-file-search
title: "OpenAI — File Search 工具"
summarized_at: 2026-05-05
entities_referenced: [Files-API]
concepts_referenced: [Tool-use]
---

## 核心要点

File search 是 Responses API 的托管工具，通过 vector store 实现语义搜索和关键词搜索，无需自行实现检索逻辑。

### 设置流程

1. 上传文件到 Files API
2. 创建 vector store
3. 将文件添加到 vector store
4. 轮询直到 `status: "completed"`

### 调用示例

```python
response = client.responses.create(
    model="gpt-5.5",
    input="What is deep research by OpenAI?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["<vector_store_id>"]
    }]
)
```

### 响应结构

模型响应包含两个输出：
1. `file_search_call`：搜索调用 ID
2. `message`：带文件引用 annotation 的模型回答（`content[0].annotations`）

### 检索定制

- **限制结果数**：减少 token 用量和延迟（可能降低质量）
- **包含搜索结果**：用 `include` 参数获取搜索结果
- **元数据过滤**：按文件属性过滤（上传时设置属性，查询时定义过滤条件）

### 支持格式

.c .cpp .cs .css .doc .docx .go .html .java .js .json .md .pdf .php .pptx .py .rb .sh .tex .ts .txt

文本文件编码需为 utf-8、utf-16 或 ascii。

### 速率限制

| 层级 | 限制 |
|---|---|
| Tier 1 | 100 RPM |
| Tier 2/3 | 500 RPM |
| Tier 4/5 | 1000 RPM |

File search（Responses API）是 Assistants API file search 的现代替代，新集成推荐使用 Responses API。
