---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=vi
fetched_at: 2026-07-27T04:47:22.646297+00:00
title: "M\u1ee5c nh\u00fang \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Mục nhúng

Gemini API cung cấp các mô hình nhúng để tạo các mục nhúng cho văn bản, hình ảnh, video và nội dung khác. Sau đó, bạn có thể dùng các vectơ nhúng thu được cho những tác vụ như tìm kiếm ngữ nghĩa, phân loại và phân cụm, mang lại kết quả chính xác hơn và nhận biết được ngữ cảnh so với các phương pháp dựa trên từ khoá.

Mô hình mới nhất, `gemini-embedding-2`, là mô hình nhúng đa phương thức đầu tiên trong Gemini API. Mô hình này ánh xạ văn bản, hình ảnh, video, âm thanh và tài liệu vào một không gian nhúng thống nhất, cho phép tìm kiếm, phân loại và phân cụm đa phương thức trên hơn 100 ngôn ngữ. Hãy xem [phần về các vectơ nhúng đa phương thức](#multimodal) để tìm hiểu thêm. Đối với các trường hợp sử dụng chỉ có văn bản, bạn vẫn có thể dùng `gemini-embedding-001`.

Xây dựng hệ thống Tạo sinh tăng cường truy xuất (RAG) là một trường hợp sử dụng phổ biến cho các sản phẩm AI. Dữ liệu nhúng đóng vai trò quan trọng trong việc cải thiện đáng kể kết quả của mô hình nhờ độ chính xác về thông tin thực tế, tính nhất quán và mức độ phong phú về ngữ cảnh được cải thiện. Nếu bạn muốn sử dụng một giải pháp RAG được quản lý, chúng tôi đã tạo công cụ [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) để giúp bạn quản lý RAG dễ dàng hơn và tiết kiệm chi phí hơn.

## Tạo các vectơ nhúng

Dùng phương thức `embedContent` để tạo các vectơ nhúng văn bản:

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

## Chỉ định loại việc cần làm để cải thiện hiệu suất

Bạn có thể sử dụng các vectơ nhúng cho nhiều tác vụ, từ phân loại đến tìm kiếm tài liệu. Việc chỉ định đúng loại tác vụ sẽ giúp tối ưu hoá các mục nhúng cho các mối quan hệ dự kiến, tối đa hoá độ chính xác và hiệu quả.

### Các loại nhiệm vụ có Embeddings 2

Đối với các tác vụ chỉ có văn bản có `gemini-embedding-2`, bạn nên thêm hướng dẫn cho tác vụ vào câu lệnh. Bạn có thể thực hiện việc này bằng cách định dạng truy vấn và tài liệu bằng tiền tố nhiệm vụ chính xác.

Các bảng sau đây cho thấy ví dụ về cách định dạng truy vấn và tài liệu cho các trường hợp sử dụng đối xứng và bất đối xứng bằng mô hình `gemini-embedding-2`.

**Trường hợp sử dụng truy xuất (Định dạng bất đối xứng)**

Trong các trường hợp sử dụng không đối xứng, hãy thêm tiền tố tác vụ vào truy vấn và áp dụng cấu trúc tài liệu cho nội dung bạn muốn nhúng và truy xuất.

| Trường hợp sử dụng | Cấu trúc truy vấn | Cấu trúc tài liệu |
| --- | --- | --- |
| Truy vấn tìm kiếm | `task: search result | query: {content}` | `title: {title} | text: {content}` Nếu không có tiêu đề, hãy dùng `title: none`. |
| Trả lời câu hỏi | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| Kiểm chứng thông tin | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| Truy xuất mã | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**Ví dụ về cách sử dụng**

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

**Trường hợp sử dụng một đầu vào (Định dạng đối xứng)**

Trong các trường hợp sử dụng đối xứng, đối với cùng một tác vụ, hãy sử dụng cùng một định dạng cho cụm từ tìm kiếm và tài liệu.

| Trường hợp sử dụng | Cấu trúc đầu vào |
| --- | --- |
| Phân loại | `task: classification | query: {content}` |
| Tạo cụm | `task: clustering | query: {content}` |
| Tính tương đồng về mặt ngữ nghĩa | `task: sentence similarity | query: {content}` Không dùng mã này để tìm kiếm hoặc truy xuất. Mô hình này được thiết kế để đo mức độ tương đồng về ngữ nghĩa giữa các văn bản. |

**Ví dụ về cách sử dụng**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

Điều quan trọng là bạn phải sử dụng tác vụ này một cách nhất quán. Ví dụ: nếu tài liệu được nhúng bằng `f'task: classification | query: {content}'`, thì truy vấn cũng phải được nhúng theo định dạng tác vụ này.

### Các loại nhiệm vụ có tính năng Nhúng 1

Đối với `gemini-embedding-001`, bạn có thể chỉ định `task_type` trong phương thức `embedContent`. Để biết danh sách đầy đủ các loại tác vụ được hỗ trợ, hãy xem bảng [Các loại tác vụ được hỗ trợ](#supported-task-types).

Ví dụ sau đây cho thấy cách bạn có thể dùng `SEMANTIC_SIMILARITY` để kiểm tra mức độ tương đồng về ý nghĩa của các chuỗi văn bản.

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

Các đoạn mã sẽ cho biết mức độ tương đồng giữa các khối văn bản khi chạy.

#### Các loại việc cần làm được hỗ trợ

Các loại nhiệm vụ được hỗ trợ cho `gemini-embedding-001`:

| Loại việc cần làm | Mô tả | Ví dụ |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | Các vectơ nhúng được tối ưu hoá để đánh giá mức độ tương đồng của văn bản. | Hệ thống đề xuất, phát hiện nội dung trùng lặp |
| **PHÂN LOẠI** | Các vectơ nhúng được tối ưu hoá để phân loại văn bản theo nhãn đặt sẵn. | Phân tích cảm xúc, phát hiện tin nhắn rác |
| **PHÂN CỤM** | Các vectơ nhúng được tối ưu hoá để phân cụm văn bản dựa trên mức độ tương đồng. | Sắp xếp tài liệu, nghiên cứu thị trường, phát hiện điểm bất thường |
| **RETRIEVAL\_DOCUMENT** | Các vectơ nhúng được tối ưu hoá cho tính năng tìm kiếm tài liệu. | Lập chỉ mục các bài viết, sách hoặc trang web để tìm kiếm. |
| **RETRIEVAL\_QUERY** | Các vectơ được tối ưu hoá cho các cụm từ tìm kiếm chung. Sử dụng `RETRIEVAL_QUERY` cho các truy vấn; `RETRIEVAL_DOCUMENT` cho các tài liệu cần truy xuất. | Tìm kiếm tùy chỉnh |
| **CODE\_RETRIEVAL\_QUERY** | Các vectơ nhúng được tối ưu hoá để truy xuất các khối mã dựa trên truy vấn bằng ngôn ngữ tự nhiên. Sử dụng `CODE_RETRIEVAL_QUERY` cho các câu hỏi; `RETRIEVAL_DOCUMENT` cho các khối mã cần truy xuất. | Đề xuất và tìm kiếm mã |
| **QUESTION\_ANSWERING** | Các vectơ nhúng cho câu hỏi trong hệ thống trả lời câu hỏi, được tối ưu hoá để tìm tài liệu trả lời câu hỏi. Sử dụng `QUESTION_ANSWERING` cho câu hỏi; `RETRIEVAL_DOCUMENT` cho tài liệu cần truy xuất. | Hộp trò chuyện |
| **FACT\_VERIFICATION** | Các câu cần được xác minh sẽ được nhúng, tối ưu hoá để truy xuất những tài liệu có bằng chứng hỗ trợ hoặc bác bỏ câu đó. Sử dụng `FACT_VERIFICATION` cho văn bản mục tiêu; `RETRIEVAL_DOCUMENT` cho tài liệu cần truy xuất | Hệ thống kiểm chứng tự động |

## Kiểm soát kích thước nhúng

Cả `gemini-embedding-001` và `gemini-embedding-2` đều được huấn luyện bằng kỹ thuật Học biểu diễn Matryoshka (MRL), giúp dạy một mô hình học các mục nhúng có nhiều chiều có các phân đoạn ban đầu (hoặc tiền tố) cũng là các phiên bản đơn giản hơn và hữu ích của cùng một dữ liệu.

Sử dụng tham số `output_dimensionality` để kiểm soát kích thước của vectơ nhúng đầu ra. Việc chọn một chiều đầu ra nhỏ hơn có thể giúp tiết kiệm dung lượng lưu trữ và tăng hiệu quả tính toán cho các ứng dụng hạ nguồn, đồng thời ít ảnh hưởng đến chất lượng. Theo mặc định, cả hai mô hình đều xuất ra một mục nhúng 3072 chiều, nhưng bạn có thể cắt bớt mục nhúng này thành kích thước nhỏ hơn mà không làm giảm chất lượng để tiết kiệm dung lượng lưu trữ. Bạn nên sử dụng kích thước đầu ra là 768, 1536 hoặc 3072.

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

Ví dụ về đầu ra của đoạn mã:

```
Length of embedding: 768
```

## Đảm bảo chất lượng cho các kích thước nhỏ hơn

Mặc dù các mục nhúng 3072 chiều mặc định luôn được chuẩn hoá, nhưng Gemini Embedding 2 cũng tự động chuẩn hoá các chiều bị cắt (ví dụ: 768, 1536). Điều này đảm bảo rằng mức độ tương đồng về ngữ nghĩa được tính toán thông qua hướng vectơ thay vì độ lớn, mang lại kết quả chính xác hơn ngay từ đầu.

**Các mô hình cũ**: Nếu đang dùng `gemini-embedding-001`, bạn phải chuẩn hoá các phương diện không phải 3072 theo cách thủ công như sau:

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

Ví dụ về đầu ra từ đoạn mã này:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

Bảng sau đây cho thấy điểm MTEB (một điểm chuẩn thường dùng cho các mục nhúng) cho nhiều phương diện. Đáng chú ý là kết quả cho thấy hiệu suất không hoàn toàn phụ thuộc vào kích thước của phương diện nhúng, với các phương diện thấp hơn đạt được điểm số tương đương với các phương diện cao hơn.

| Phương diện MRL | Điểm MTEB (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68,16 |
| 1536 | 68,17 |
| 768 | 67,99 |
| 512 | 67,55 |
| 256 | 66,19 |
| 128 | 63,31 |

## Nhúng đa phương thức

Mô hình `gemini-embedding-2` hỗ trợ dữ liệu đầu vào đa phương thức, cho phép bạn nhúng nội dung hình ảnh, video, âm thanh và tài liệu cùng với văn bản. Tất cả các phương thức đều được ánh xạ vào cùng một không gian nhúng, cho phép tìm kiếm và so sánh đa phương thức.

### Các phương thức và giới hạn được hỗ trợ

Giới hạn tổng số mã thông báo đầu vào tối đa là 8192 mã thông báo.

| Phương thức | Quy cách và giới hạn |
| --- | --- |
| **Văn bản** | Hỗ trợ tối đa 8.192 mã thông báo. |
| **Image** | Tối đa 6 hình ảnh cho mỗi yêu cầu. Các định dạng được hỗ trợ: PNG, JPEG. |
| **Âm thanh** | Thời lượng tối đa là 180 giây. Các định dạng được hỗ trợ: MP3, WAV. |
| **Video** | Thời lượng tối đa là 120 giây. Các định dạng được hỗ trợ: MP4, MOV. Các bộ mã hoá và giải mã được hỗ trợ: H264, H265, AV1, VP9.  Hệ thống xử lý tối đa 32 khung hình cho mỗi video: video ngắn (≤32 giây) được lấy mẫu ở tốc độ 1 khung hình/giây, trong khi video dài hơn được lấy mẫu đồng đều thành 32 khung hình. Các tệp video không xử lý bản âm thanh. |
| **Tài liệu (PDF)** | Mỗi yêu cầu có tối đa 1 tệp, tối đa 6 trang. |

### Nhúng hình ảnh

Ví dụ sau đây cho thấy cách nhúng hình ảnh bằng `gemini-embedding-2`.

Bạn có thể cung cấp hình ảnh dưới dạng dữ liệu nội tuyến hoặc dưới dạng tệp đã tải lên thông qua [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

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

### Tổng hợp dữ liệu nhúng

Khi làm việc với nội dung đa phương thức, cách bạn cấu trúc dữ liệu đầu vào sẽ ảnh hưởng đến kết quả nhúng:

- **Nhiều phần (được tổng hợp):** Việc thêm nhiều dữ liệu đầu vào trực tiếp vào tham số `contents` sẽ tạo ra một vectơ nhúng tổng hợp cho tất cả dữ liệu đầu vào.
- **Nhiều đối tượng `Content` (riêng biệt):** Việc bao bọc từng đầu vào trong một đối tượng `Content` và truyền các đối tượng đó vào tham số `contents` sẽ trả về các mục nhúng riêng biệt cho từng mục.
- **Biểu diễn ở cấp bài đăng:** Đối với các đối tượng phức tạp như bài đăng trên mạng xã hội có nhiều mục nội dung nghe nhìn, bạn nên tổng hợp các mục nhúng riêng biệt (ví dụ: bằng cách tính trung bình) để tạo một biểu diễn nhất quán ở cấp bài đăng.

Ví dụ sau đây cho thấy cách tạo một vectơ nhúng tổng hợp cho văn bản và dữ liệu đầu vào là hình ảnh. Bạn chỉ cần thêm nhiều dữ liệu đầu vào vào tham số `contents`:

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

Mặt khác, nếu bạn sử dụng các đối tượng `Content` bên trong tham số `contents`, thì hàm này sẽ trả về các mục nhúng riêng biệt. Ví dụ này tạo nhiều mục nhúng trong một lệnh gọi nhúng:

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
        types.Content(parts=[types.Part.from_text(text="An image of a dog")]),
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
            { parts: [{ text: 'An image of a dog' }] },
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
                "content": {"parts": [{"text": "An image of a dog"}]}
            },
            {
                "model": "models/gemini-embedding-2",
                "content": {"parts": [{"inline_data": {"mime_type": "image/png", "data": "'"${IMG_BASE64}"'"}}]}
            }
        ]
    }'
```

### Nhúng âm thanh

Ví dụ sau đây cho biết cách nhúng một tệp âm thanh bằng `gemini-embedding-2`.

Bạn có thể cung cấp tệp âm thanh dưới dạng dữ liệu nội tuyến hoặc dưới dạng tệp được tải lên thông qua [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

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

### Nhúng video

Ví dụ sau đây cho thấy cách nhúng video bằng `gemini-embedding-2`.

Bạn có thể cung cấp video dưới dạng dữ liệu nội tuyến hoặc dưới dạng tệp được tải lên thông qua [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

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

Nếu cần nhúng video dài hơn 120 giây, bạn có thể chia video thành các đoạn chồng chéo và nhúng từng đoạn.

### Nhúng tài liệu

Bạn có thể nhúng trực tiếp tài liệu ở định dạng PDF. Mô hình này xử lý nội dung trực quan và văn bản của từng trang.

Bạn có thể cung cấp tệp PDF dưới dạng dữ liệu nội tuyến hoặc dưới dạng tệp được tải lên thông qua [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi).

#### Cách mô hình xử lý tệp PDF

Khi bạn nhúng một tệp PDF, mô hình sẽ xử lý tài liệu bằng cả tính năng hình ảnh và văn bản:

- **Biểu diễn trực quan:** Mô hình kết xuất mỗi trang dưới dạng một hình ảnh, tiêu thụ **258 mã thông báo** cho mỗi trang.
- **Trích xuất văn bản:** Mô hình trích xuất văn bản từ tài liệu. Đối với **tệp PDF gốc** (chứa văn bản kỹ thuật số), mô hình sẽ trích xuất văn bản trực tiếp. Đối với **tệp PDF được quét** (chứa hình ảnh văn bản), mô hình sẽ tự động chạy công nghệ nhận dạng ký tự quang học (OCR) để trích xuất văn bản.

Để tính tổng số mã thông báo cho một tệp PDF, hãy cộng số mã thông báo trực quan (258 mã thông báo cho mỗi trang) với số mã thông báo văn bản. Thông tin đầu vào của bạn phải nằm trong **giới hạn 8.192 mã thông báo** của mô hình (được chia sẻ trên tất cả các phương thức). Hệ thống sẽ tự động cắt bớt những nội dung đầu vào vượt quá giới hạn này.

#### Giới hạn về tệp PDF

- **Số lượng tệp trên mỗi yêu cầu:** Bạn có thể gửi tối đa 1 tệp PDF.
- **Giới hạn về số trang:** Bạn có thể gửi tối đa 6 trang cho mỗi tệp. Để có chất lượng tốt nhất, bạn nên sử dụng 1 trang cho mỗi tệp PDF.

Ví dụ sau đây cho thấy cách nhúng một tệp PDF bằng `gemini-embedding-2`:

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

## Trường hợp sử dụng

Vectơ hoá văn bản là yếu tố quan trọng đối với nhiều trường hợp sử dụng AI phổ biến, chẳng hạn như:

- **Tạo sinh tăng cường khả năng truy xuất (RAG):** Các vectơ nhúng giúp nâng cao chất lượng của văn bản được tạo bằng cách truy xuất và kết hợp thông tin liên quan vào ngữ cảnh của một mô hình.
- **Truy xuất thông tin:** Tìm kiếm văn bản hoặc tài liệu có ngữ nghĩa tương tự nhất dựa trên một đoạn văn bản đầu vào.

  [Hướng dẫn tìm kiếm tài liệutask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **Sắp xếp lại kết quả tìm kiếm**: Ưu tiên các mục phù hợp nhất bằng cách tính điểm ngữ nghĩa cho kết quả ban đầu dựa trên cụm từ tìm kiếm.

  [Hướng dẫn về việc sắp xếp lại kết quả tìm kiếmtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **Phát hiện điểm bất thường:** Việc so sánh các nhóm vectơ nhúng có thể giúp xác định các xu hướng hoặc điểm ngoại lệ bị ẩn.

  [Hướng dẫn phát hiện hoạt động bất thườngbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **Phân loại:** Tự động phân loại văn bản dựa trên nội dung, chẳng hạn như phân tích cảm xúc hoặc phát hiện tin nhắn rác

  [Hướng dẫn phân loạitoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **Phân cụm:** Nắm bắt hiệu quả các mối quan hệ phức tạp bằng cách tạo các cụm và hình ảnh trực quan về các thành phần nhúng.

  [Hướng dẫn về hình ảnh trực quan của việc phân cụmbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## Lưu trữ mục nhúng

Khi đưa các mục nhúng vào sản xuất, bạn thường sử dụng **cơ sở dữ liệu vectơ** để lưu trữ, lập chỉ mục và truy xuất các mục nhúng có nhiều chiều một cách hiệu quả. Google Cloud cung cấp các dịch vụ dữ liệu được quản lý có thể dùng cho mục đích này, bao gồm [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=vi), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=vi), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=vi) và [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=vi).

Các hướng dẫn sau đây cho biết cách sử dụng các cơ sở dữ liệu vectơ của bên thứ ba khác với Gemini Embedding.

- [Hướng dẫn về ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [Hướng dẫn về QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Hướng dẫn về Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Hướng dẫn về Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## Phiên bản mô hình

### Gemini Embedding 2

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `gemini-embedding-2` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản, hình ảnh, video, âm thanh, PDF  **Đầu ra**  Mục nhúng văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  8.192  **Kích thước phương diện đầu ra**  Linh hoạt, hỗ trợ: 128 – 3072, Nên dùng: 768, 1536, 3072 |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Ổn định: `gemini-embedding-2` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 4 năm 2026 |

### Gemini Embedding

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | **Gemini API**  `gemini-embedding-001` |
| saveCác loại dữ liệu được hỗ trợ | **Input**  Văn bản  **Đầu ra**  Mục nhúng văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  2.048  **Kích thước phương diện đầu ra**  Linh hoạt, hỗ trợ: 128 – 3072, Nên dùng: 768, 1536, 3072 |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Ổn định: `gemini-embedding-001` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 6 năm 2025 |

Đối với các mô hình Nhúng không dùng nữa, hãy truy cập trang [Ngừng cung cấp](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi)

## Di chuyển từ gemini-embedding-001

Các khoảng trống nhúng giữa `gemini-embedding-001` và `gemini-embedding-2` là **không tương thích**. Điều này có nghĩa là bạn không thể so sánh trực tiếp các vectơ nhúng do một mô hình tạo ra với các vectơ nhúng do mô hình khác tạo ra. Nếu đang nâng cấp lên `gemini-embedding-2`, bạn phải nhúng lại tất cả dữ liệu hiện có.

Ngoài sự không tương thích, còn có một số điểm khác biệt đáng chú ý khác giữa hai mô hình này:

- **Quy cách về loại tác vụ:** Với `gemini-embedding-001`, bạn chỉ định loại tác vụ bằng cách sử dụng tham số `task_type` (ví dụ: `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`). Với `gemini-embedding-2`, tham số `task_type` không được hỗ trợ. Thay vào đó, bạn nên đưa hướng dẫn về nhiệm vụ trực tiếp vào câu lệnh cho các nhiệm vụ chỉ có văn bản. Hãy xem [Các loại nhiệm vụ có Embeddings 2](#task-types-embeddings-2) để biết thông tin chi tiết về cách định dạng câu lệnh cho các trường hợp sử dụng khác nhau.
- **Tổng hợp mục nhúng:** `gemini-embedding-001` tạo các mục nhúng riêng lẻ cho từng chuỗi trong danh sách dữ liệu đầu vào. Ngược lại, `gemini-embedding-2` tạo ra một vectơ nhúng tổng hợp duy nhất khi nhiều dữ liệu đầu vào (chẳng hạn như văn bản và hình ảnh) được cung cấp trực tiếp trong một yêu cầu. Để tạo các vectơ nhúng riêng biệt cho từng đầu vào, hãy bao bọc từng đầu vào trong một đối tượng `Content` hoặc sử dụng [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi#batch-embedding). Hãy xem phần [Nhúng tính năng tổng hợp](#embedding-aggregation) để biết thêm thông tin.
- **Chuẩn hoá:** Nếu bạn dùng `output_dimensionality` để yêu cầu các mục nhúng có ít hơn 3072 phương diện, thì `gemini-embedding-2` sẽ tự động chuẩn hoá các mục nhúng bị cắt bớt này. Với `gemini-embedding-001`, bạn cần thực hiện chuẩn hoá thủ công cho các phương diện khác ngoài 3072. Hãy xem phần [Đảm bảo chất lượng cho các kích thước nhỏ hơn](#quality-for-smaller-dimensions) để biết thông tin chi tiết.

## Nhúng hàng loạt

Nếu không lo ngại về độ trễ, hãy thử sử dụng các mô hình Gemini Embeddings với [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi#batch-embedding). Điều này cho phép công suất cao hơn nhiều ở mức 50% giá Nhúng mặc định.
Bạn có thể tìm thấy các ví dụ về cách bắt đầu trong [sổ tay về Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

## Thông báo về việc sử dụng có trách nhiệm

Không giống như các mô hình AI tạo sinh tạo ra nội dung mới, Mô hình nhúng Gemini chỉ nhằm mục đích chuyển đổi định dạng dữ liệu đầu vào của bạn thành một biểu diễn bằng số. Mặc dù Google chịu trách nhiệm cung cấp một mô hình nhúng giúp chuyển đổi định dạng dữ liệu đầu vào của bạn sang định dạng số được yêu cầu, nhưng người dùng vẫn hoàn toàn chịu trách nhiệm về dữ liệu mà họ nhập và các mục nhúng thu được. Khi sử dụng mô hình Gemini Embedding, bạn xác nhận rằng bạn có các quyền cần thiết đối với mọi nội dung mình tải lên. Đừng tạo nội dung vi phạm quyền tài sản trí tuệ hoặc quyền riêng tư của người khác. Khi sử dụng dịch vụ này, bạn phải tuân thủ [Chính sách về các hành vi bị cấm khi sử dụng](https://policies.google.com/terms/generative-ai/use-policy?hl=vi) và [Điều khoản dịch vụ của Google](https://ai.google.dev/gemini-api/terms?hl=vi).

## Bắt đầu xây dựng bằng các thành phần nhúng

Hãy xem [notebook bắt đầu nhanh về các vectơ nhúng](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb) để khám phá các chức năng của mô hình và tìm hiểu cách tuỳ chỉnh cũng như trực quan hoá các vectơ nhúng.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
