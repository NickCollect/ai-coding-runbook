---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=ko
fetched_at: 2026-05-05T20:07:36.130892+00:00
title: "\uc784\ubca0\ub529 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 임베딩

Gemini API는 텍스트, 이미지, 동영상, 기타 콘텐츠의 임베딩을 생성하는 임베딩 모델을 제공합니다. 이러한 결과 임베딩은 시맨틱 검색, 분류, 클러스터링과 같은 작업에 사용할 수 있으며, 키워드 기반 접근 방식보다 더 정확하고 맥락을 인식하는 결과를 제공합니다.

최신 모델인 `gemini-embedding-2`는 Gemini API의 첫 번째 멀티모달 임베딩 모델입니다. 텍스트, 이미지, 동영상, 오디오, 문서를 통합 임베딩 공간에 매핑하여 100개 이상의 언어로 교차 모달 검색, 분류, 클러스터링을 지원합니다. 자세한 내용은 [멀티모달 임베딩 섹션](#multimodal)을 참고하세요. 텍스트 전용 사용 사례의 경우 `gemini-embedding-001`를 계속 사용할 수 있습니다.

검색 증강 생성 (RAG) 시스템을 빌드하는 것은 AI 제품의 일반적인 사용 사례입니다. 임베딩은 사실 기반 정확도, 일관성, 상황별 풍부함이 개선된 모델 출력을 크게 향상하는 데 중요한 역할을 합니다. 관리형 RAG 솔루션을 사용하려면 RAG를 더 쉽게 관리하고 비용 효율적으로 수행할 수 있는 [파일 검색](https://ai.google.dev/gemini-api/docs/file-search?hl=ko) 도구를 사용하세요.

## 임베딩 생성

`embedContent` 메서드를 사용하여 텍스트 임베딩을 생성합니다.

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

### 자바스크립트

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

## 성능을 개선하기 위해 작업 유형 지정

분류부터 문서 검색까지 다양한 작업에 임베딩을 사용할 수 있습니다. 올바른 태스크 유형을 지정하면 의도한 관계에 맞게 임베딩을 최적화하여 정확성과 효율성을 극대화할 수 있습니다.

### 임베딩 2가 적용된 태스크 유형

`gemini-embedding-2`를 사용한 텍스트 전용 작업의 경우 프롬프트에 작업 지침을 추가하는 것이 좋습니다. 올바른 작업 접두사를 사용하여 질문과 문서의 형식을 지정하면 됩니다.

다음 표는 `gemini-embedding-2` 모델을 사용하여 대칭 및 비대칭 사용 사례에 맞게 쿼리와 문서를 포맷하는 방법을 보여줍니다.

**검색 사용 사례 (비대칭 형식)**

비대칭 사용 사례에서는 쿼리에 작업 접두사를 추가하고 삽입하고 검색하려는 콘텐츠에 문서 구조를 적용합니다.

| 사용 사례 | 쿼리 구조 | 문서 구조 |
| --- | --- | --- |
| 검색어 | `task: search result | query: {content}` | `title: {title} | text: {content}` 제목이 없으면 `title: none`을 사용합니다. |
| 질의 응답 | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| 사실확인 | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| 코드 검색 | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**사용 예**

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

**단일 입력 사용 사례 (대칭 형식)**

대칭 사용 사례에서는 동일한 작업에 대해 질문과 문서에 동일한 형식을 사용합니다.

| 사용 사례 | 입력 구조 |
| --- | --- |
| 분류 | `task: classification | query: {content}` |
| 클러스터링 | `task: clustering | query: {content}` |
| 의미론적 유사도 | `task: sentence similarity | query: {content}` 검색 또는 검색에는 사용하지 마세요. 의미론적 텍스트 유사성을 위한 것입니다. |

**사용 예**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

작업을 일관되게 사용하는 것이 중요합니다. 예를 들어 문서가 `f'task: classification | query: {content}'`로 삽입된 경우 쿼리도 이 작업 형식을 따라 삽입해야 합니다.

### 임베딩 1이 있는 태스크 유형

`gemini-embedding-001`의 경우 `embedContent` 메서드에서 `task_type`를 지정할 수 있습니다. 지원되는 작업 유형의 전체 목록은 [지원되는 작업 유형](#supported-task-types) 표를 참고하세요.

다음 예는 `SEMANTIC_SIMILARITY`를 사용하여 텍스트 문자열의 의미가 얼마나 유사한지 확인하는 방법을 보여줍니다.

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

### 자바스크립트

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

코드 스니펫은 실행 시 텍스트의 여러 청크가 서로 얼마나 유사한지 보여줍니다.

#### 지원되는 태스크 유형

`gemini-embedding-001`에 지원되는 작업 유형:

| 작업 유형 | 설명 | 예 |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | 텍스트 유사성을 평가하도록 최적화된 임베딩 | 추천 시스템, 중복 감지 |
| **분류** | 사전 설정된 라벨에 따라 텍스트를 분류하도록 최적화된 임베딩 | 감정 분석, 스팸 감지 |
| **클러스터링** | 유사성을 기반으로 텍스트를 클러스터링하는 데 최적화된 임베딩 | 문서 정리, 시장 조사, 이상 감지 |
| **RETRIEVAL\_DOCUMENT** | 문서 검색에 최적화된 임베딩입니다. | 검색을 위해 기사, 책 또는 웹페이지를 색인 생성합니다. |
| **RETRIEVAL\_QUERY** | 일반 검색어에 최적화된 임베딩 쿼리에는 `RETRIEVAL_QUERY`를 사용하고 검색할 문서에는 `RETRIEVAL_DOCUMENT`를 사용합니다. | 맞춤검색 |
| **CODE\_RETRIEVAL\_QUERY** | 자연어 쿼리를 기반으로 코드 블록을 검색하는 데 최적화된 임베딩입니다. 질문에는 `CODE_RETRIEVAL_QUERY`를 사용하고 검색할 코드 블록에는 `RETRIEVAL_DOCUMENT`를 사용하세요. | 코드 추천 및 검색 |
| **QUESTION\_ANSWERING** | 질의 응답 시스템의 질문 임베딩(질문에 답변하는 문서를 찾는 데 최적화됨) 질문에는 `QUESTION_ANSWERING`를 사용하고 검색할 문서에는 `RETRIEVAL_DOCUMENT`를 사용합니다. | 채팅 상자 |
| **FACT\_VERIFICATION** | 확인해야 하는 진술의 임베딩으로, 진술을 뒷받침하거나 반박하는 증거가 포함된 문서를 검색하는 데 최적화되어 있습니다. 타겟 텍스트에는 `FACT_VERIFICATION`를 사용하고 검색할 문서에는 `RETRIEVAL_DOCUMENT`를 사용합니다. | 자동 사실 확인 시스템 |

## 임베딩 크기 제어

`gemini-embedding-001`와 `gemini-embedding-2`는 모두 Matryoshka Representation Learning (MRL) 기법을 사용하여 학습됩니다. 이 기법은 모델에 동일한 데이터의 유용하고 더 간단한 버전인 초기 세그먼트 (또는 접두사)가 있는 고차원 삽입을 학습하도록 가르칩니다.

`output_dimensionality` 파라미터를 사용하여 출력 임베딩 벡터의 크기를 제어합니다. 더 작은 출력 크기를 선택하면 저장공간을 절약하고 다운스트림 애플리케이션의 계산 효율성을 높일 수 있으며 품질 면에서는 거의 손실이 없습니다. 기본적으로 두 모델 모두 3072차원 임베딩을 출력하지만 품질 손실 없이 더 작은 크기로 잘라 저장공간을 절약할 수 있습니다. 768, 1536 또는 3072 출력 크기를 사용하는 것이 좋습니다.

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

### 자바스크립트

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

코드 스니펫의 출력 예시:

```
Length of embedding: 768
```

## 더 작은 크기의 품질 보장

기본 3072차원 임베딩은 항상 정규화되지만 Gemini Embedding 2는 잘린 차원 (예: 768, 1536)도 자동 정규화합니다. 이렇게 하면 크기가 아닌 벡터 방향을 통해 의미 유사성이 계산되므로 기본적으로 더 정확한 결과를 얻을 수 있습니다.

**이전 모델**: `gemini-embedding-001`를 사용하는 경우 다음과 같이 3072가 아닌 차원을 수동으로 정규화해야 합니다.

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

이 코드 스니펫의 출력 예시:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

다음 표에는 다양한 차원에 대한 MTEB 점수가 나와 있습니다. MTEB는 임베딩에 흔히 사용되는 벤치마크입니다. 특히 결과에 따르면 성능이 임베딩 차원의 크기와 엄격하게 연결되어 있지 않으며, 낮은 차원이 높은 차원과 비슷한 점수를 달성합니다.

| MRL 측정기준 | MTEB 점수 (Gemini Embedding 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## 멀티모달 임베딩

`gemini-embedding-2` 모델은 멀티모달 입력을 지원하므로 텍스트와 함께 이미지, 동영상, 오디오, 문서 콘텐츠를 삽입할 수 있습니다. 모든 모달리티는 동일한 임베딩 공간에 매핑되어 교차 모달 검색 및 비교가 가능합니다.

### 지원되는 모달리티 및 한도

전체 최대 입력 토큰 한도는 8,192개입니다.

| 형식 | 사양 및 한도 |
| --- | --- |
| **텍스트** | 최대 8,192개의 토큰을 지원합니다. |
| **이미지** | 요청당 최대 6개의 이미지 지원되는 형식: PNG, JPEG |
| **오디오** | 최대 재생 시간은 180초입니다. 지원되는 형식: MP3, WAV |
| **동영상** | 최대 길이는 120초입니다. 지원되는 형식: MP4, MOV 지원되는 코덱: H264, H265, AV1, VP9  시스템은 동영상당 최대 32프레임을 처리합니다. 짧은 동영상 (≤32초)은 1fps로 샘플링되고 긴 동영상은 32프레임으로 균일하게 샘플링됩니다. 오디오 트랙은 동영상 파일에서 처리되지 않습니다. |
| **문서 (PDF)** | 최대 6페이지 |

### 이미지 삽입

다음 예에서는 `gemini-embedding-2`를 사용하여 이미지를 삽입하는 방법을 보여줍니다.

이미지는 인라인 데이터로 제공하거나 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 통해 업로드된 파일로 제공할 수 있습니다.

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

### 자바스크립트

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

### 임베딩 집계

멀티모달 콘텐츠로 작업할 때 입력 구조는 임베딩 출력에 영향을 미칩니다.

- **여러 부분 (집계됨):** `contents` 매개변수에 여러 입력을 직접 추가하면 모든 입력에 대해 하나의 집계된 임베딩이 생성됩니다.
- **여러 `Content` 객체 (별도):** 각 입력을 `Content` 객체로 래핑하고 `contents` 매개변수에 전달하면 각 항목에 대해 별도의 임베딩이 반환됩니다.
- **게시물 수준 표현:** 미디어 항목이 여러 개인 소셜 미디어 게시물과 같은 복잡한 객체의 경우 별도의 삽입을 집계(예: 평균)하여 일관된 게시물 수준 표현을 만드는 것이 좋습니다.

다음 예시는 텍스트 및 이미지 입력에 대해 하나의 집계된 임베딩을 만드는 방법을 보여줍니다. `contents` 매개변수에 여러 입력을 추가하기만 하면 됩니다.

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

### 자바스크립트

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

반면 `contents` 매개변수 내에서 `Content` 객체를 사용하면 별도의 임베딩이 반환됩니다. 이 예시에서는 하나의 임베딩 호출에서 여러 임베딩을 만듭니다.

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

### 자바스크립트

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

### 오디오 삽입

다음 예는 `gemini-embedding-2`를 사용하여 오디오 파일을 삽입하는 방법을 보여줍니다.

오디오 파일은 인라인 데이터로 제공하거나 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 통해 업로드된 파일로 제공할 수 있습니다.

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

### 자바스크립트

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

### 동영상 삽입

다음 예는 `gemini-embedding-2`를 사용하여 동영상을 삽입하는 방법을 보여줍니다.

동영상은 인라인 데이터로 제공하거나 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 통해 업로드된 파일로 제공할 수 있습니다.

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

### 자바스크립트

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

120초가 넘는 동영상을 삽입해야 하는 경우 동영상을 중복되는 세그먼트로 나누어 각 세그먼트를 개별적으로 삽입하면 됩니다.

### 문서 삽입

PDF 형식의 문서는 직접 삽입할 수 있습니다. 모델은 각 페이지의 시각적 콘텐츠와 텍스트 콘텐츠를 처리합니다.

PDF는 인라인 데이터로 제공하거나 [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 통해 업로드된 파일로 제공할 수 있습니다.

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

### 자바스크립트

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

## 사용 사례

텍스트 임베딩은 다음과 같은 다양한 일반적인 AI 사용 사례에 매우 중요합니다.

- **검색 증강 생성 (RAG):** 임베딩은 모델의 컨텍스트에서 관련 정보를 검색하고 통합하여 생성된 텍스트의 품질을 향상합니다.
- **정보 검색:** 입력 텍스트가 주어졌을 때 의미적으로 가장 유사한 텍스트 또는 문서를 검색합니다.

  [문서 검색 튜토리얼task](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **검색 재순위 지정**: 쿼리에 대해 초기 결과에 시맨틱 점수를 매겨 가장 관련성 높은 항목에 우선순위를 지정합니다.

  [검색 재순위 지정 튜토리얼task](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **이상 감지:** 임베딩 그룹을 비교하면 숨겨진 추세나 이상치를 식별할 수 있습니다.

  [이상 감지 튜토리얼bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **분류:** 감정 분석 또는 스팸 감지와 같은 콘텐츠를 기반으로 텍스트를 자동으로 분류합니다.

  [분류 튜토리얼token](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **클러스터링:** 임베딩의 클러스터와 시각화를 만들어 복잡한 관계를 효과적으로 파악합니다.

  [클러스터링 시각화 튜토리얼bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## 임베딩 저장

임베딩을 프로덕션에 적용할 때 **벡터 데이터베이스**를 사용하여 고차원 임베딩을 효율적으로 저장, 색인 생성, 검색하는 것이 일반적입니다. Google Cloud는 [Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=ko), [BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=ko), [AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=ko), [Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=ko) 등 이러한 용도로 사용할 수 있는 관리형 데이터 서비스를 제공합니다.

다음 튜토리얼에서는 Gemini Embedding과 함께 다른 서드 파티 벡터 데이터베이스를 사용하는 방법을 보여줍니다.

- [ChromaDB 튜토리얼bolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant 튜토리얼bolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate 튜토리얼bolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone 튜토리얼bolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## 모델 버전

### Gemini 임베딩 2

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `gemini-embedding-2` |
| save 지원 데이터 유형 | **입력**  텍스트, 이미지, 동영상, 오디오, PDF  **출력**  텍스트 임베딩 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  8,192  **출력 측정기준 크기**  유연함, 지원: 128~3072, 권장: 768, 1536, 3072 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 안정화 버전: `gemini-embedding-2` |
| calendar\_month최신 업데이트 | 2026년 4월 |

### Gemini 임베딩

| 속성 | 설명 |
| --- | --- |
| id\_card모델 코드 | **Gemini API**  `gemini-embedding-001` |
| save 지원 데이터 유형 | **입력**  텍스트  **출력**  텍스트 임베딩 |
| token\_auto토큰 한도[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ko) | **입력 토큰 한도**  2,048  **출력 측정기준 크기**  유연함, 지원: 128~3072, 권장: 768, 1536, 3072 |
| 123버전 | 자세한 내용은 [모델 버전 패턴](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ko#model-versions)을 참고하세요.  - 안정화 버전: `gemini-embedding-001` |
| calendar\_month최신 업데이트 | 2025년 6월 |

지원 중단된 임베딩 모델은 [지원 중단](https://ai.google.dev/gemini-api/docs/deprecations?hl=ko) 페이지를 참고하세요.

## gemini-embedding-001에서 이전

`gemini-embedding-001`와 `gemini-embedding-2` 사이의 삽입 공간은 **호환되지 않습니다**. 즉, 한 모델에서 생성된 임베딩을 다른 모델에서 생성된 임베딩과 직접 비교할 수 없습니다. `gemini-embedding-2`로 업그레이드하는 경우 기존 데이터를 모두 다시 삽입해야 합니다.

호환성 외에도 두 모델 간에는 몇 가지 주목할 만한 차이점이 있습니다.

- **작업 유형 지정:** `gemini-embedding-001`를 사용하면 `task_type` 매개변수 (예: `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`)를 사용하여 작업 유형을 지정합니다. `gemini-embedding-2`를 사용하면 `task_type` 매개변수가 지원되지 않습니다. 대신 텍스트 전용 작업의 프롬프트에 작업 안내를 직접 포함해야 합니다. 다양한 사용 사례에 맞게 프롬프트를 포맷하는 방법에 대한 자세한 내용은 [임베딩 2가 포함된 태스크 유형](#task-types-embeddings-2)을 참고하세요.
- **임베딩 집계:** `gemini-embedding-001`는 입력 목록에 있는 각 문자열에 대해 개별 임베딩을 생성합니다. 반면 `gemini-embedding-2`는 텍스트, 이미지와 같은 여러 입력이 하나의 요청에 직접 제공되는 경우 단일 집계 임베딩을 생성합니다. 개별 입력에 대해 별도의 임베딩을 생성하려면 각 입력을 `Content` 객체로 래핑하거나 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko#batch-embedding)를 사용하세요. 자세한 내용은 [삽입 집계](#embedding-aggregation)를 참고하세요.
- **정규화:** `output_dimensionality`를 사용하여 3072개 미만의 차원으로 임베딩을 요청하면 `gemini-embedding-2`가 잘린 임베딩을 자동으로 정규화합니다. `gemini-embedding-001`의 경우 3072 이외의 차원에 대해 수동 정규화를 실행해야 합니다. 자세한 내용은 [작은 크기의 품질 보장](#quality-for-smaller-dimensions)을 참고하세요.

## 일괄 임베딩

지연 시간이 문제가 되지 않는다면 [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ko#batch-embedding)와 함께 Gemini Embeddings 모델을 사용해 보세요. 이를 통해 기본 삽입 가격의 50% 로 훨씬 높은 처리량을 달성할 수 있습니다.
시작하는 방법의 예는 [Batch API 쿡북](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)을 참고하세요.

## 책임감 있는 사용 알림

새 콘텐츠를 생성하는 생성형 AI 모델과 달리 Gemini 임베딩 모델은 입력 데이터의 형식을 수치 표현으로 변환하는 데만 사용됩니다. Google은 입력 데이터의 형식을 요청된 숫자 형식으로 변환하는 삽입 모델을 제공할 책임이 있지만, 사용자는 입력한 데이터와 결과 삽입에 대한 모든 책임을 집니다. Gemini 임베딩 모델을 사용하면 업로드하는 모든 콘텐츠에 필요한 권리를 보유하고 있음을 확인하는 것으로 간주됩니다. 타인의 지식 재산 및 개인 정보 보호 권리를 침해하는 콘텐츠를 생성해서는 안 됩니다. 이 서비스 사용 시 Google의 [금지된 사용 정책](https://policies.google.com/terms/generative-ai/use-policy?hl=ko) 및 [Google 서비스 약관](https://ai.google.dev/gemini-api/terms?hl=ko)이 적용됩니다.

## 임베딩으로 빌드 시작

[임베딩 빠른 시작 노트북](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)을 확인하여 모델 기능을 살펴보고 임베딩을 맞춤설정하고 시각화하는 방법을 알아보세요.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-05-01(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-05-01(UTC)"],[],[]]
