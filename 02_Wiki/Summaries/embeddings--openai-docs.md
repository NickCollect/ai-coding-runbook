---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/embeddings.md
source_url: https://platform.openai.com/docs/guides/embeddings
title: "OpenAI — Vector Embeddings"
summarized_at: 2026-05-05
entities_referenced: [Embeddings]
concepts_referenced: []
---

## 核心要点

OpenAI text embeddings 将文本映射为浮点向量，向量间距离衡量语义相关性。

### 主要用途

- **搜索**：按相关性排序结果
- **聚类**：相似文本分组
- **推荐**：找相关内容
- **异常检测**：识别离群点
- **分类**：按最相似标签分类

### 调用示例

```python
from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)
print(response.data[0].embedding)
```

### 可用模型

| 模型 | ~页面/美元 | MTEB 性能 | 最大输入 |
|---|---|---|---|
| text-embedding-3-small | 62,500 | 62.3% | 8192 |
| text-embedding-3-large | 9,615 | 64.6% | 8192 |
| text-embedding-ada-002 | 12,500 | 61.0% | 8192 |

- 默认维度：`text-embedding-3-small` 1536，`text-embedding-3-large` 3072
- 通过 `dimensions` 参数可缩减维度（无需后处理归一化即可保持语义）

### 关键技术细节

- OpenAI embedding 已归一化到长度 1 → 余弦相似度 = 点积
- 推荐距离函数：**cosine similarity**
- 第三代模型（-3 后缀）不包含 2021 年 9 月后的知识
- 分词工具：`tiktoken`，第三代用 `cl100k_base` 编码

### 典型 use case 代码模式

```python
from openai.embeddings_utils import get_embedding, cosine_similarity

def search_reviews(df, product_description, n=3):
    embedding = get_embedding(product_description, model='text-embedding-3-small')
    df['similarities'] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))
    return df.sort_values('similarities', ascending=False).head(n)
```
