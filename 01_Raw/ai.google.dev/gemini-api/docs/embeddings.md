---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=zh-CN
fetched_at: 2026-09-14T05:52:17.819749+00:00
title: "Embeddings \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash 现已推出。[试试看](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=zh-cn)。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Embeddings

Gemini API 提供嵌入模型，可为文本、图片、视频和其他内容生成嵌入。然后，这些生成的嵌入可用于语义搜索、分类和聚类等任务，与基于关键字的方法相比，可提供更准确、更贴合情境的结果。

最新模型 `gemini-embedding-2` 是 Gemini API 中的首个多模态嵌入模型。它将文本、图片、视频、音频和文档映射到统一的嵌入空间中，从而能够以 100 多种语言进行跨模态搜索、分类和聚类。如需了解详情，请参阅[多模态嵌入部分](#multimodal)。对于纯文字用例，`gemini-embedding-001` 仍然可用。

构建检索增强生成 (RAG) 系统是 AI 产品的一种常见使用场景。嵌入在显著提升模型输出方面发挥着关键作用，可提高事实准确性、连贯性和上下文丰富度。如果您想使用托管式 RAG 解决方案，我们构建了[文件搜索](https://ai.google.dev/gemini-api/docs/file-search?hl=zh-cn)工具，可让您更轻松地管理 RAG 并提高成本效益。

## 生成嵌入

使用 `embedContent` 方法生成文本嵌入：

### Python

```
from google import genai

client = genai.Client()

result = client.models.embed_content(
        model="gemini-embedding-2",
        contents="What is the meaning of life?"
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {

    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
    });

    console.log(response.embeddings);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### Go

```
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }
    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    embeddings, err := json.MarshalIndent(result.Embeddings, "", "  ")
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(string(embeddings))
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "model": "models/gemini-embedding-2",
        "content": {
        "parts": [{
            "text": "What is the meaning of life?"
        }]
        }
    }'
```

## 指定任务类型以提高性能

您可以将嵌入用于从分类到文档搜索的各种任务。指定正确的任务类型有助于针对预期关系优化嵌入，从而最大限度地提高准确性和效率。

### 使用 Embeddings 2 的任务类型

对于使用 `gemini-embedding-2` 的纯文本任务，我们强烈建议您在提示中添加任务指令。为此，您可以使用正确的任务前缀设置查询和文档的格式。

在[基于多模态输入生成单个嵌入](#embedding-aggregation)时，我们通常不建议在输入的文本部分添加任务指令作为前缀。在某些情况下，它可以提高性能，但在其他情况下，它会降低性能。

下表展示了如何使用 `gemini-embedding-2` 模型针对对称和非对称用例设置查询和文档的格式。

**检索用例（非对称格式）**

在非对称使用情形下，请向查询添加任务前缀，并为要嵌入和检索的内容应用文档结构。

| 使用场景 | 查询结构 | 文档结构 |
| --- | --- | --- |
| 搜索查询 | `task: search result | query: {content}` | `title: {title} | text: {content}` 如果没有标题，则使用 `title: none`。 |
| 问答 | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| 事实核查 | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| 代码检索 | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**使用示例**

### Python

```
# Generate embedding for a task's query. Use your correct task here:
def prepare_query(query):
    # return f"task: question answering | query: {query}"
    # return f"task: fact checking | query: {query}"
    # return f"task: code retrieval | query: {query}"
    return f"task: search result | query: {query}"

# Generate embedding for document of an asymmetric retrieval task:
def prepare_document(content, title=None):
    if title is None:
        title = "none"
    return f"title: {title} | text: {content}"
```

**单输入源用例（对称格式）**

在对称使用情形中，对于同一任务，请对查询和文档使用相同的格式。

| 使用场景 | 输入结构 |
| --- | --- |
| 分类 | `task: classification | query: {content}` |
| 聚簇 | `task: clustering | query: {content}` |
| 语义相似度 | `task: sentence similarity | query: {content}` 请勿将此方法用于搜索或检索。它旨在用于语义文本相似度。 |

**使用示例**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

请务必坚持使用该任务。例如，如果文档嵌入了 `f'task: classification | query: {content}'`，则查询也应按照此任务格式嵌入。

### 使用 Embeddings 1 的任务类型

对于 `gemini-embedding-001`，您可以在 `embedContent` 方法中指定 `task_type`。如需查看支持的任务类型的完整列表，请参阅[支持的任务类型](#supported-task-types)表格。

以下示例展示了如何使用 `SEMANTIC_SIMILARITY` 来检查文本字符串在含义上的相似程度。

### Python

```
from google import genai
from google.genai import types
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

texts = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
)

# Create a 3x3 table to show the similarity matrix
df = pd.DataFrame(
    cosine_similarity([e.values for e in result.embeddings]),
    index=texts,
    columns=texts,
)

print(df)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
// npm i compute-cosine-similarity
import * as cosineSimilarity from "compute-cosine-similarity";

async function main() {
    const ai = new GoogleGenAI({});

    const texts = [
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    ];

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-001',
        contents: texts,
        config: { taskType: 'SEMANTIC_SIMILARITY' },
    });

    const embeddings = response.embeddings.map(e => e.values);

    for (let i = 0; i < texts.length; i++) {
        for (let j = i + 1; j < texts.length; j++) {
            const text1 = texts[i];
            const text2 = texts[j];
            const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
            console.log(`Similarity between '${text1}' and '${text2}': ${similarity.toFixed(4)}`);
        }
    }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "math"

    "google.golang.org/genai"
)

// cosineSimilarity calculates the similarity between two vectors.
func cosineSimilarity(a, b []float32) (float64, error) {
    if len(a) != len(b) {
        return 0, fmt.Errorf("vectors must have the same length")
    }

    var dotProduct, aMagnitude, bMagnitude float64
    for i := 0; i < len(a); i++ {
        dotProduct += float64(a[i] * b[i])
        aMagnitude += float64(a[i] * a[i])
        bMagnitude += float64(b[i] * b[i])
    }

    if aMagnitude == 0 || bMagnitude == 0 {
        return 0, nil
    }

    return dotProduct / (math.Sqrt(aMagnitude) * math.Sqrt(bMagnitude)), nil
}

func main() {
    ctx := context.Background()
    client, _ := genai.NewClient(ctx, nil)
    defer client.Close()

    texts := []string{
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?",
    }

    var contents []*genai.Content
    for _, text := range texts {
        contents = append(contents, genai.NewContentFromText(text, genai.RoleUser))
    }

    result, _ := client.Models.EmbedContent(ctx,
        "gemini-embedding-001",
        contents,
        &genai.EmbedContentRequest{TaskType: genai.TaskTypeSemanticSimilarity},
    )

    embeddings := result.Embeddings

    for i := 0; i < len(texts); i++ {
        for j := i + 1; j < len(texts); j++ {
            similarity, _ := cosineSimilarity(embeddings[i].Values, embeddings[j].Values)
            fmt.Printf("Similarity between '%s' and '%s': %.4f\n", texts[i], texts[j], similarity)
        }
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-001:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
    "taskType": "SEMANTIC_SIMILARITY",
    "content": {
        "parts": [
        {
            "text": "What is the meaning of life?"
        },
        {
            "text": "How much wood would a woodchuck chuck?"
        },
        {
            "text": "How does the brain work?"
        }
        ]
    }
    }'
```

代码段将展示在运行时，不同的文本块彼此之间的相似程度。

#### 支持的任务类型

`gemini-embedding-001` 支持的任务类型：

| 任务类型 | 说明 | 示例 |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | 经过优化以评估文本相似度的嵌入。 | 推荐系统、重复内容检测 |
| **分类** | 经过优化的嵌入，可根据预设标签对文本进行分类。 | 情感分析、垃圾信息检测 |
| **聚类** | 经过优化的嵌入，可根据文本的相似性对文本进行聚类。 | 文档整理、市场调研、异常检测 |
| **RETRIEVAL\_DOCUMENT** | 针对文档搜索进行了优化的嵌入。 | 为搜索编制文章、图书或网页的索引。 |
| **RETRIEVAL\_QUERY** | 针对一般搜索查询进行了优化的嵌入。 使用 `RETRIEVAL_QUERY` 表示查询；使用 `RETRIEVAL_DOCUMENT` 表示要检索的文档。 | 自定义搜索 |
| **CODE\_RETRIEVAL\_QUERY** | 经过优化的嵌入，可根据自然语言查询检索代码块。 使用 `CODE_RETRIEVAL_QUERY` 表示查询；使用 `RETRIEVAL_DOCUMENT` 表示要检索的代码块。 | 代码建议和搜索 |
| **QUESTION\_ANSWERING** | 问答系统中问题的嵌入内容，经过优化，可用于查找回答问题的文档。 使用 `QUESTION_ANSWERING` 提出问题；使用 `RETRIEVAL_DOCUMENT` 指定要检索的文档。 | 聊天框 |
| **FACT\_VERIFICATION** | 需要验证的陈述的嵌入，针对检索包含支持或反驳陈述的证据的文档进行了优化。 使用 `FACT_VERIFICATION` 表示目标文本；使用 `RETRIEVAL_DOCUMENT` 表示要检索的文档 | 自动化事实核查系统 |

## 控制嵌入大小

`gemini-embedding-001` 和 `gemini-embedding-2` 均使用 Matryoshka Representation Learning (MRL) 技术进行训练，该技术可教导模型学习具有初始段（或前缀）的高维嵌入，这些初始段也是相同数据的有用且更简单的版本。

使用 `output_dimensionality` 参数控制输出嵌入向量的大小。选择较小的输出维度可以节省存储空间并提高下游应用的计算效率，同时在质量方面几乎不会有任何损失。默认情况下，这两个模型都会输出一个 3072 维的嵌入，但您可以将其截断为较小的尺寸，而不会损失质量，从而节省存储空间。建议使用 768、1536 或 3072 输出维度。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="What is the meaning of life?",
    config=types.EmbedContentConfig(output_dimensionality=768)
)

[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)

print(f"Length of embedding: {embedding_length}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: 'What is the meaning of life?',
        config: { outputDimensionality: 768 },
    });

    const embeddingLength = response.embeddings[0].values.length;
    console.log(`Length of embedding: ${embeddingLength}`);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // The client uses Application Default Credentials.
    // Authenticate with 'gcloud auth application-default login'.
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    contents := []*genai.Content{
        genai.NewContentFromText("What is the meaning of life?", genai.RoleUser),
    }

    result, err := client.Models.EmbedContent(ctx,
        "gemini-embedding-2",
        contents,
        &genai.EmbedContentRequest{OutputDimensionality: 768},
    )
    if err != nil {
        log.Fatal(err)
    }

    embedding := result.Embeddings[0]
    embeddingLength := len(embedding.Values)
    fmt.Printf("Length of embedding: %d\n", embeddingLength)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H 'Content-Type: application/json' \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -d '{
        "content": {"parts":[{ "text": "What is the meaning of life?"}]},
        "output_dimensionality": 768
    }'
```

代码段的输出示例：

```
Length of embedding: 768
```

## 确保较小尺寸的质量

虽然默认的 3072 维嵌入始终会进行归一化，但 Gemini Embedding 2 也会自动归一化截断的维度（例如 768、1536）。这可确保通过向量方向而非大小来计算语义相似度，从而提供更准确的开箱即用型结果。

**旧版模型**：如果您使用的是 `gemini-embedding-001`，则必须手动对非 3072 维度的维度进行归一化处理，如下所示：

### Python

```
import numpy as np
from numpy.linalg import norm

# Only for embeddings from `gemini-embedding-001`
embedding_values_np = np.array(embedding_obj.values)
normed_embedding = embedding_values_np / np.linalg.norm(embedding_values_np)

print(f"Normed embedding length: {len(normed_embedding)}")
print(f"Norm of normed embedding: {np.linalg.norm(normed_embedding):.6f}") # Should be very close to 1
```

此代码段的输出示例：

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

下表显示了不同维度下的 MTEB 分数（一种常用的嵌入模型基准）。值得注意的是，结果表明性能并不严格取决于嵌入维度的规模，较低维度可实现与较高维度相当的分数。

| MRL 维度 | MTEB 得分（Gemini Embedding 001） |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## 多模态嵌入

`gemini-embedding-2` 模型支持多模态输入，让您能够将图片、视频、音频和文档内容与文本一起嵌入。所有模态都映射到同一嵌入空间中，从而实现跨模态搜索和比较。

### 支持的模态和限制

输入词元的总数上限为 8,192 个。

| 模态 | 规范和限制 |
| --- | --- |
| **文本** | 支持最多 8,192 个 token。 |
| **Image** | 每个请求最多 6 张图片。支持的格式：PNG、JPEG。 |
| **音频** | 时长上限为 180 秒。支持的格式：MP3、WAV。 |
| **视频** | 时长上限为 120 秒。支持的格式：MP4、MOV。支持的编解码器：H264、H265、AV1、VP9。  系统最多处理每个视频 32 帧：短视频（≤32 秒）以 1 fps 的速率进行抽样，而较长的视频则均匀抽样为 32 帧。视频文件中的音轨不会被处理。 |
| **文档 (PDF)** | 每个请求最多包含 1 个文件，最多 6 页。 |

### 嵌入图片

以下示例展示了如何使用 `gemini-embedding-2` 嵌入图片。

图片可以通过内嵌数据或通过 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 上传的文件提供。

### Python

```
from google import genai
from google.genai import types

with open('example.png', 'rb') as f:
    image_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("example.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'image/png',
                data: imgBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
IMG_PATH="/path/to/your/image.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "image/png",
                    "data": "'"${IMG_BASE64}"'"
                }
            }]
        }
    }'
```

### 嵌入聚合

处理多模态内容时，输入内容的结构会影响嵌入输出：

- **多个部分（聚合）**：直接向 `contents` 参数添加多个输入会生成一个包含所有输入的聚合嵌入内容。
- **多个 `Content` 对象（单独）**：将每个输入内容封装在 `Content` 对象中，并通过 `contents` 参数传递这些对象，这样会为每个条目返回单独的嵌入内容。
- **帖子级表示法**：对于包含多个媒体项的社交媒体帖子等复杂对象，我们建议汇总单独的嵌入内容（例如通过求平均值），以创建连贯的帖子级表示法。

以下示例展示了如何为文本和图片输入创建一种聚合嵌入。只需向 `contents` 参数添加多个输入即可：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        "An image of a dog",
        types.Part.from_bytes(
            data=image_bytes,
            mime_type='image/png',
        ),
    ]
)

# This produces one embedding
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            'An image of a dog',
            {
                inlineData: {
                    mimeType: 'image/png',
                    data: imgBase64,
                },
            },
        ],
    });

    // This produces one embedding
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [
                {"text": "An image of a dog"},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": "'"${IMG_BASE64}"'"
                    }
                }
            ]
        }
    }'
```

另一方面，如果您在 `contents` 参数中使用 `Content` 对象，则会返回单独的嵌入内容。此示例在一个嵌入调用中创建多个嵌入：

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('dog.png', 'rb') as f:
    image_bytes = f.read()

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=[
        types.Content(parts=[types.Part.from_text(text="task: classification | query: An image of a dog")]),
        types.Content(
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png",
                ),
            ]
        ),
    ],
)

# This produces two embeddings
for embedding in result.embeddings:
    print(embedding.values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const imgBase64 = fs.readFileSync("dog.png", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [
            { parts: [{ text: 'task: classification | query: An image of a dog' }] },
            {
                parts: [{
                    inlineData: {
                        mimeType: 'image/png',
                        data: imgBase64,
                    },
                }],
            },
        ],
    });

    // This produces two embeddings
    for (const embedding of response.embeddings) {
        console.log(embedding.values);
    }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
IMG_PATH="/path/to/your/dog.png"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:batchEmbedContents" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "requests": [
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"text": "task: classification | query: An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### 嵌入音频

以下示例展示了如何使用 `gemini-embedding-2` 嵌入音频文件。

音频文件可以通过 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 以内嵌数据或上传文件的形式提供。

### Python

```
from google import genai
from google.genai import types

with open('example.mp3', 'rb') as f:
    audio_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=audio_bytes,
            mime_type='audio/mpeg',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const audioBase64 = fs.readFileSync("example.mp3", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'audio/mpeg',
                data: audioBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
AUDIO_PATH="/path/to/your/example.mp3"
AUDIO_BASE64=$(base64 -w0 "${AUDIO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "audio/mpeg",
                    "data": "'"${AUDIO_BASE64}"'"
                }
            }]
        }
    }'
```

### 嵌入视频

以下示例展示了如何使用 `gemini-embedding-2` 嵌入视频。

视频可以通过 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 以内嵌数据或上传文件的形式提供。

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

with open('example.mp4', 'rb') as f:
    video_bytes = f.read()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
    ]
)

print(result.embeddings[0].values)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const videoBase64 = fs.readFileSync("example.mp4", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'video/mp4',
                data: videoBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
VIDEO_PATH="/path/to/your/video.mp4"
VIDEO_BASE64=$(base64 -w0 "${VIDEO_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "video/mp4",
                    "data": "'"${VIDEO_BASE64}"'"
                }
            }]
        }
    }'
```

如果您需要嵌入时长超过 120 秒的视频，可以将视频分块为重叠的片段，然后单独嵌入这些片段。

### 嵌入文档

PDF 格式的文档可以直接嵌入。模型会处理每个网页的视觉和文本内容。

可以通过 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=zh-cn) 以内嵌数据或上传文件的形式提供 PDF。

#### 模型处理 PDF 的方式

嵌入 PDF 时，模型会同时使用视觉特征和文本特征来处理文档：

- **直观表示**：模型将每个网页渲染为图片，每个网页消耗 **258 个 token**。
- **文本提取**：模型从文档中提取文本。对于**原生 PDF**（包含数字文本），模型会直接提取文本。对于**扫描的 PDF**（其中包含文本图片），模型会自动运行光学字符识别 (OCR) 来提取文本。

如需计算 PDF 的总 token 数量，请将视觉 token（每页 258 个）与文本 token 相加。您的输入必须在模型的 **8,192 个词元限制**（适用于所有模态）范围内。系统会以静默方式截断超出此限制的输入。

#### PDF 限制

- **每个请求的文件数**：您最多可以提交 1 个 PDF 文件。
- **页数限制**：每个文件最多可提交 6 页。为了获得最佳质量，我们强烈建议每个 PDF 使用 1 个页面。

以下示例展示了如何使用 `gemini-embedding-2` 嵌入 PDF：

### Python

```
from google import genai
from google.genai import types

with open('example.pdf', 'rb') as f:
    pdf_bytes = f.read()

client = genai.Client()

result = client.models.embed_content(
    model='gemini-embedding-2',
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes,
            mime_type='application/pdf',
        ),
    ]
)

print(result.embeddings)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {
    const ai = new GoogleGenAI({});

    const pdfBase64 = fs.readFileSync("example.pdf", { encoding: "base64" });

    const response = await ai.models.embedContent({
        model: 'gemini-embedding-2',
        contents: [{
            inlineData: {
                mimeType: 'application/pdf',
                data: pdfBase64,
            },
        }],
    });

    console.log(response.embeddings);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.types.EmbedContentResponse;
import java.util.Collections;

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("text-embedding-004", "Why is the sky blue?", null);

response.embeddings().ifPresent(list -> {
  for (var emb : list) {
    System.out.println("Embedding values: " + emb.values().orElse(Collections.emptyList()));
  }
});
```

### REST

```
PDF_PATH="/path/to/your/example.pdf"
PDF_BASE64=$(base64 -w0 "${PDF_PATH}")

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent" \
    -H "Content-Type: application/json" \
    -H "x-goog-api-key: ${GEMINI_API_KEY}" \
    -d '{
        "content": {
            "parts": [{
                "inline_data": {
                    "mime_type": "application/pdf",
                    "data": "'"${PDF_BASE64}"'"
                }
            }]
        }
    }'
```

## 使用场景

文本嵌入对于各种常见的 AI 应用场景至关重要，例如：

- **检索增强生成 (RAG)**：通过检索相关信息并将其纳入模型的情境中，嵌入可提高生成文本的质量。
- **信息检索**：根据一段输入文本搜索语义上最相似的文本或文档。

  [文档搜索教程task](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **搜索结果重新排名**：根据初始结果与查询的语义相关性得分，优先显示最相关的项。

  [搜索重排名教程task](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **异常值检测**：比较嵌入群组有助于发现隐藏的趋势或离群点。

  [异常值检测教程bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **分类**：根据文本内容自动对文本进行分类，例如情感分析或垃圾信息检测

  [分类教程token](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **聚类**：通过创建嵌入的聚类和可视化图表，有效掌握复杂的关系。

  [聚类可视化教程bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## 存储嵌入

在将嵌入投入生产环境时，通常会使用**向量数据库**来高效存储、索引和检索高维嵌入。Google Cloud 提供可用于此目的的托管数据服务，包括 [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=zh-cn)、[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=zh-cn)、[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=zh-cn) 和 [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=zh-cn)。

以下教程展示了如何将其他第三方向量数据库与 Gemini Embedding 搭配使用。

- [ChromaDB 教程bolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant 教程bolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate 教程bolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone 教程bolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## 模型版本

### Gemini Embedding 2

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | **Gemini API**  `gemini-embedding-2` |
| 保存支持的数据类型 | **输入**  文本、图片、视频、音频、PDF  **输出**  文本嵌入 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  8192  **输出维度大小**  灵活，支持：128 - 3072，推荐：768、1536、3072 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 稳定版：`gemini-embedding-2` |
| calendar\_month最新更新 | 2026 年 4 月 |

### Gemini Embedding

| 属性 | 说明 |
| --- | --- |
| id\_card 模型代码 | **Gemini API**  `gemini-embedding-001` |
| 保存支持的数据类型 | **输入**  文本  **输出**  文本嵌入 |
| token\_auto令牌限制[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=zh-cn) | **输入 token 限制**  2048  **输出维度大小**  灵活，支持：128 - 3072，推荐：768、1536、3072 |
| 123 版本 | 如需了解详情，请参阅[模型版本模式](https://ai.google.dev/gemini-api/docs/models/gemini?hl=zh-cn#model-versions)。  - 稳定版：`gemini-embedding-001` |
| calendar\_month最新更新 | 2025 年 6 月 |

如需了解已弃用的嵌入模型，请访问[弃用](https://ai.google.dev/gemini-api/docs/deprecations?hl=zh-cn)页面

## 从 gemini-embedding-001 迁移

`gemini-embedding-001` 和 `gemini-embedding-2` 之间的嵌入空间**不兼容**。这意味着您无法直接比较一个模型生成的嵌入与另一个模型生成的嵌入。如果您要升级到 `gemini-embedding-2`，则必须重新嵌入所有现有数据。

除了不兼容之外，这两个模型之间还有其他几个显著的区别：

- **任务类型规范**：使用 `gemini-embedding-001` 时，您可以使用 `task_type` 参数（例如 `SEMANTIC_SIMILARITY`、`RETRIEVAL_DOCUMENT`）指定任务类型。使用 `gemini-embedding-2` 时，不支持 `task_type` 参数。您应直接在纯文本任务的提示中添加任务说明。如需详细了解如何针对不同的使用场景设置提示格式，请参阅[使用 Embeddings 2 的任务类型](#task-types-embeddings-2)。
- **嵌入汇总**： `gemini-embedding-001` 为输入列表中的每个字符串生成单独的嵌入。相比之下，当一个请求中直接提供多个输入（例如文本和图片）时，`gemini-embedding-2` 会生成单个聚合嵌入。如需为各个输入生成单独的嵌入内容，请将每个输入封装在 `Content` 对象中，或使用 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn#batch-embedding)。如需了解详情，请参阅[嵌入聚合](#embedding-aggregation)。
- **归一化**：如果您使用 `output_dimensionality` 请求维度数少于 3072 的嵌入内容，`gemini-embedding-2` 会自动对这些截断的嵌入内容进行归一化处理。使用 `gemini-embedding-001` 时，您需要对 3072 以外的维度执行手动归一化。如需了解详情，请参阅[确保较小尺寸的质量](#quality-for-smaller-dimensions)。

## 批量嵌入

如果延迟不是问题，请尝试使用 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=zh-cn#batch-embedding) 和 Gemini Embeddings 模型。这样一来，吞吐量可大幅提高，但价格仅为默认嵌入价格的 50%。如需查看有关如何开始使用批量 API 的示例，请参阅[批量 API 实战宝典](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)。

## 负责任的使用声明

与创建新内容的生成式 AI 模型不同，Gemini Embedding 模型仅用于将输入数据的格式转换为数值表示形式。虽然 Google 负责提供一种嵌入模型，将输入数据的格式转换为所需的数值格式，但用户仍需对他们输入的数据和生成的嵌入内容承担全部责任。使用 Gemini Embedding 模型，即表示您确认已拥有对所上传内容的必要权利。请勿生成会侵犯他人知识产权或隐私权的内容。使用此服务时，您必须遵守我们的[《使用限制政策》](https://policies.google.com/terms/generative-ai/use-policy?hl=zh-cn)和 [Google 的《服务条款》](https://ai.google.dev/gemini-api/terms?hl=zh-cn)。

## 开始使用嵌入模型进行构建

您可以查看[嵌入快速入门笔记本](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)，了解模型功能以及如何自定义和直观呈现嵌入。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-09-08。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-09-08。"],[],[]]
