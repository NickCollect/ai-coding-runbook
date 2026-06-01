---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=ja
fetched_at: 2026-06-01T05:56:45.447591+00:00
title: "\u30a8\u30f3\u30d9\u30c7\u30a3\u30f3\u30b0 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja) がプレビュー版で利用可能になりました。共同プランニング、可視化、MCP サポートなどが含まれています。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# エンベディング

Gemini API は、テキスト、画像、動画などのコンテンツのエンベディングを生成するエンベディング モデルを提供します。これらのエンベディングは、セマンティック検索、分類、クラスタリングなどのタスクに使用できます。キーワード ベースのアプローチよりも正確で、コンテキストを認識した結果が得られます。

最新のモデル `gemini-embedding-2` は、Gemini API の最初のマルチモーダル エンベディング モデルです。テキスト、画像、動画、音声、ドキュメントを統合されたエンベディング空間にマッピングし、100 以上の言語でクロスモーダル検索、分類、クラスタリングを可能にします。詳しくは、[マルチモーダル エンベディングのセクション](#multimodal)をご覧ください。テキストのみのユースケースでは、`gemini-embedding-001` は引き続き使用できます。

検索拡張生成（RAG）システムの構築は、AI プロダクトの一般的なユースケースです。エンベディングは、事実の正確性、一貫性、コンテキストの豊富さを向上させ、モデルの出力を大幅に強化するうえで重要な役割を果たします。マネージド RAG ソリューションを使用する場合は、RAG の管理を容易にし、費用対効果を高める [File Search](https://ai.google.dev/gemini-api/docs/file-search?hl=ja) ツールをご利用ください。

## エンベディングの生成

`embedContent` メソッドを使用してテキスト エンベディングを生成します。

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

## パフォーマンスを改善するためにタスクタイプを指定する

エンベディングは、分類からドキュメント検索まで、幅広いタスクに使用できます。適切なタスクタイプを指定すると、目的の関係に合わせてエンベディングを最適化し、精度と効率を最大限に高めることができます。

### Embeddings 2 を使用するタスクタイプ

`gemini-embedding-2` を使用するテキストのみのタスクでは、プロンプトにタスクの指示を追加することを強くおすすめします。これを行うには、クエリとドキュメントを正しいタスク接頭辞でフォーマットします。

次の表は、`gemini-embedding-2` モデルを使用して対称ユースケースと非対称ユースケースのクエリとドキュメントの形式を設定する方法の例を示しています。

**検索のユースケース（非対称形式）**

非対称のユースケースでは、クエリにタスク接頭辞を追加し、埋め込んで取得するコンテンツにドキュメント構造を適用します。

| ユースケース | クエリの構造 | ドキュメント構造 |
| --- | --- | --- |
| 検索クエリ | `task: search result | query: {content}` | `title: {title} | text: {content}` タイトルがない場合は、`title: none` を使用します。 |
| 質問応答 | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| ファクト チェック | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| コードの取得 | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**使用例**

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

**単一入力のユースケース（対称形式）**

対称的なユースケースでは、同じタスクに対して、クエリとドキュメントに同じ形式を使用します。

| ユースケース | 入力構造 |
| --- | --- |
| 分類 | `task: classification | query: {content}` |
| クラスタリング | `task: clustering | query: {content}` |
| 意味的類似度 | `task: sentence similarity | query: {content}` 検索や取得には使用しないでください。意味的テキスト類似性を目的としています。 |

**使用例**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

タスクを一貫して使用することが重要です。たとえば、ドキュメントが `f'task: classification | query: {content}'` でエンベディングされている場合、クエリもこのタスク形式に従ってエンベディングする必要があります。

### Embeddings 1 を使用するタスクタイプ

`gemini-embedding-001` の場合、`embedContent` メソッドで `task_type` を指定できます。サポートされているタスクタイプの完全なリストについては、[サポートされているタスクタイプ](#supported-task-types)の表をご覧ください。

次の例は、`SEMANTIC_SIMILARITY` を使用してテキスト文字列の意味の類似性を確認する方法を示しています。

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

コード スニペットを実行すると、テキストの各チャンクが互いにどの程度類似しているかがわかります。

#### サポートされているタスクの種類

`gemini-embedding-001` でサポートされているタスクの種類:

| Task type | 説明 | 例 |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | テキストの類似性を評価するために最適化されたエンベディング。 | レコメンデーション システム、重複検出 |
| **分類** | 事前設定されたラベルに従ってテキストを分類するように最適化されたエンベディング。 | 感情分析、スパム検出 |
| **クラスタリング** | 類似性に基づいてテキストをクラスタ化するように最適化されたエンベディング。 | ドキュメントの整理、市場調査、異常検出 |
| **RETRIEVAL\_DOCUMENT** | ドキュメント検索用に最適化されたエンベディング。 | 検索用に記事、書籍、ウェブページをインデックス登録する。 |
| **RETRIEVAL\_QUERY** | 一般的な検索クエリ用に最適化されたエンベディング。クエリには `RETRIEVAL_QUERY` を使用し、取得するドキュメントには `RETRIEVAL_DOCUMENT` を使用します。 | カスタム検索 |
| **CODE\_RETRIEVAL\_QUERY** | 自然言語クエリに基づくコードブロックの取得用に最適化されたエンベディング。クエリには `CODE_RETRIEVAL_QUERY`、取得するコードブロックには `RETRIEVAL_DOCUMENT` を使用します。 | コードの候補と検索 |
| **QUESTION\_ANSWERING** | 質問に回答するドキュメントの検索に最適化された、質問応答システムの質問のエンベディング。質問には `QUESTION_ANSWERING` を使用し、取得するドキュメントには `RETRIEVAL_DOCUMENT` を使用します。 | チャットボックス |
| **FACT\_VERIFICATION** | 検証が必要なステートメントのエンベディング。ステートメントを裏付ける証拠または反論する証拠を含むドキュメントの取得に最適化されています。ターゲット テキストには `FACT_VERIFICATION` を使用し、取得するドキュメントには `RETRIEVAL_DOCUMENT` を使用します。 | 自動ファクト チェック システム |

## エンベディング サイズの制御

`gemini-embedding-001` と `gemini-embedding-2` はどちらも、マトリョーシカ表現学習（MRL）手法を使用してトレーニングされます。この手法では、同じデータの有用でよりシンプルなバージョンである初期セグメント（またはプレフィックス）を持つ高次元のエンベディングを学習するようにモデルをトレーニングします。

`output_dimensionality` パラメータを使用して、出力エンベディング ベクトルのサイズを制御します。出力の次元数を小さくすると、ストレージ スペースを節約し、ダウンストリーム アプリケーションの計算効率を高めることができます。品質の低下はわずかです。デフォルトでは、どちらのモデルも 3,072 次元のエンベディングを出力しますが、品質を損なうことなくサイズを小さくして、ストレージ スペースを節約できます。出力ディメンションには 768、1536、3072 を使用することをおすすめします。

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

コード スニペットからの出力例:

```
Length of embedding: 768
```

## 小さい寸法での品質を確保する

デフォルトの 3,072 次元エンベディングは常に正規化されますが、Gemini Embedding 2 では、切り捨てられた次元（768、1,536 など）も自動的に正規化されます。これにより、セマンティック類似性が大きさではなくベクトルの方向で計算されるため、より正確な結果がすぐに得られます。

**古いモデル**: `gemini-embedding-001` を使用している場合は、3, 072 以外のディメンションを次のように手動で正規化する必要があります。

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

このコード スニペットの出力例:

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

次の表に、さまざまなディメンションの MTEB スコアを示します。MTEB スコアは、エンベディングで一般的に使用されるベンチマークです。特に、結果は、パフォーマンスがエンベディング ディメンションのサイズに厳密に結び付いていないことを示しています。ディメンションが小さい場合でも、ディメンションが大きい場合と同等のスコアを達成しています。

| MRL ディメンション | MTEB スコア（Gemini Embedding 001） |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## マルチモーダル エンベディング

`gemini-embedding-2` モデルはマルチモーダル入力をサポートしているため、テキストとともに画像、動画、音声、ドキュメントのコンテンツを埋め込むことができます。すべてのモダリティが同じエンベディング空間にマッピングされるため、クロスモーダル検索と比較が可能になります。

### サポートされているモダリティと制限事項

入力トークンの全体的な最大上限は 8,192 トークンです。

| モダリティ | 仕様と制限事項 |
| --- | --- |
| **テキスト** | 最大 8,192 個のトークンをサポートします。 |
| **画像** | リクエストごとに最大 6 枚の画像。サポートされている形式: PNG、JPEG。 |
| **音声** | 最大再生時間は 180 秒です。サポートされている形式: MP3、WAV。 |
| **動画** | 最大再生時間は 120 秒です。サポートされている形式: MP4、MOV。サポートされているコーデック: H264、H265、AV1、VP9。  システムは、動画あたり最大 32 フレームを処理します。短い動画（≤32 秒）は 1 fps でサンプリングされ、長い動画は 32 フレームに均等にサンプリングされます。動画ファイルでは音声トラックは処理されません。 |
| **ドキュメント（PDF）** | リクエストあたりのファイル数は最大 1 つ、ページ数は最大 6 ページです。 |

### 画像を埋め込む

次の例は、`gemini-embedding-2` を使用して画像を埋め込む方法を示しています。

画像は、インライン データとして、または [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を介してアップロードされたファイルとして提供できます。

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

### エンベディングの集計

マルチモーダル コンテンツを扱う場合、入力の構造はエンベディング出力に影響します。

- **複数の部分（集約）:** 複数の入力を `contents` パラメータに直接追加すると、すべての入力に対して 1 つの集約エンベディングが生成されます。
- **複数の `Content` オブジェクト（個別）:** 各入力を `Content` オブジェクトでラップし、`contents` パラメータで渡すと、エントリごとに個別のエンベディングが返されます。
- **投稿レベルの表現:** 複数のメディア アイテムを含むソーシャル メディア投稿などの複雑なオブジェクトの場合は、個別のエンベディングを（平均化するなどして）集約し、一貫性のある投稿レベルの表現を作成することをおすすめします。

次の例は、テキスト入力と画像入力に対して 1 つの集約エンベディングを作成する方法を示しています。`contents` パラメータに複数の入力を追加するだけです。

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

一方、`contents` パラメータ内で `Content` オブジェクトを使用すると、個別のエンベディングが返されます。この例では、1 回のエンベディング呼び出しで複数のエンベディングを作成します。

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

### 音声を埋め込む

次の例は、`gemini-embedding-2` を使用して音声ファイルを埋め込む方法を示しています。

音声ファイルは、インライン データとして提供することも、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を介してアップロードされたファイルとして提供することもできます。

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

### 動画の埋め込み

次の例は、`gemini-embedding-2` を使用して動画を埋め込む方法を示しています。

動画は、インライン データとして提供することも、[Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を介してアップロードされたファイルとして提供することもできます。

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

120 秒を超える動画を埋め込む必要がある場合は、動画を重複するセグメントに分割し、それらのチャンクを個別に埋め込むことができます。

### ドキュメントのエンベディング

PDF 形式のドキュメントは直接埋め込むことができます。モデルは、各ページのビジュアル コンテンツとテキスト コンテンツを処理します。

PDF は、インライン データとして、または [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ja) を介してアップロードされたファイルとして提供できます。

#### モデルによる PDF の処理方法

PDF を埋め込むと、モデルはビジュアル機能とテキスト機能の両方を使用してドキュメントを処理します。

- **視覚的な表現:** モデルは各ページを画像としてレンダリングします。これにより、ページごとに **258 個のトークン**が消費されます。
- **テキスト抽出:** モデルはドキュメントからテキストを抽出します。**ネイティブ PDF**（デジタル テキストを含む）の場合、モデルはテキストを直接抽出します。**スキャンされた PDF**（テキストの画像を含む）の場合、モデルは光学式文字認識（OCR）を自動的に実行してテキストを抽出します。

PDF の合計トークン数を計算するには、テキスト トークンにビジュアル トークン（1 ページあたり 258 個）を追加します。入力は、モデルの **8,192 トークン上限**（すべてのモダリティで共有）内に収まる必要があります。この上限を超える入力は、システムによって通知なしで切り捨てられます。

#### PDF の上限

- **リクエストあたりのファイル数:** 最大 1 つの PDF ファイルを送信できます。
- **ページの上限:** ファイル 1 つあたり最大 6 ページまで送信できます。最適な品質を確保するため、PDF 1 ページにつき 1 つのファイルを使用することを強くおすすめします。

次の例は、`gemini-embedding-2` を使用して PDF を埋め込む方法を示しています。

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

## ユースケース

テキスト エンベディングは、次のような一般的な AI のユースケースで重要です。

- **検索拡張生成（RAG）:** エンベディングは、関連情報を取得してモデルのコンテキストに組み込むことで、生成されたテキストの品質を高めます。
- **情報検索:** 入力テキストが与えられたときに、意味的に最も類似したテキストまたはドキュメントを検索します。

  [ドキュメント検索のチュートリアルtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **検索結果の再ランキング**: クエリに対して初期結果を意味的にスコアリングすることで、最も関連性の高いアイテムを優先します。

  [検索結果の再ランキングのチュートリアルtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **異常検出:** エンベディングのグループを比較すると、隠れた傾向や外れ値を特定できます。

  [異常検出チュートリアルbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **分類:** 感情分析やスパム検出など、コンテンツに基づいてテキストを自動的に分類します。

  [分類チュートリアルtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **クラスタリング:** エンベディングのクラスタと可視化を作成して、複雑な関係を効果的に把握します。

  [クラスタリングの可視化のチュートリアルbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## エンベディングの保存

エンベディングを本番環境に移行する場合は、**ベクトル データベース**を使用して、高次元エンベディングを効率的に保存、インデックス登録、取得するのが一般的です。Google Cloud には、この目的で使用できるマネージド データサービス（[Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=ja)、[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=ja)、[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=ja)、[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=ja) など）が用意されています。

次のチュートリアルでは、Gemini Embedding で他のサードパーティのベクトル データベースを使用する方法について説明します。

- [ChromaDB チュートリアルbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [QDrant チュートリアルbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [Weaviate チュートリアルbolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [Pinecone チュートリアルbolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## モデル バージョン

### Gemini Embedding 2

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `gemini-embedding-2` |
| save でサポートされるデータ型 | **入力**  テキスト、画像、動画、音声、PDF  **出力**  テキスト エンベディング |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  8,192  **出力ディメンションのサイズ**  柔軟、サポート: 128 ～ 3072、推奨: 768、1536、3072 |
| 123 バージョン | 詳細については、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#model-versions)をご覧ください。  - 安定版: `gemini-embedding-2` |
| calendar\_month最終更新日 | 2026 年 4 月 |

### Gemini エンベディング

| プロパティ | 説明 |
| --- | --- |
| id\_cardモデルコード | **Gemini API**  `gemini-embedding-001` |
| save でサポートされるデータ型 | **入力**  テキスト  **出力**  テキスト エンベディング |
| token\_autoトークンの上限[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=ja) | **入力トークンの上限**  2,048  **出力ディメンションのサイズ**  柔軟、サポート: 128 ～ 3072、推奨: 768、1536、3072 |
| 123 バージョン | 詳細については、[モデル バージョンのパターン](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ja#model-versions)をご覧ください。  - 安定版: `gemini-embedding-001` |
| calendar\_month最終更新日 | 2025 年 6 月 |

非推奨のエンベディング モデルについては、[非推奨](https://ai.google.dev/gemini-api/docs/deprecations?hl=ja)のページをご覧ください。

## gemini-embedding-001 からの移行

`gemini-embedding-001` と `gemini-embedding-2` の間のエンベディング スペースは**互換性がありません**。つまり、あるモデルで生成されたエンベディングを別のモデルで生成されたエンベディングと直接比較することはできません。`gemini-embedding-2` にアップグレードする場合は、既存のデータをすべて再埋め込む必要があります。

互換性がないだけでなく、この 2 つのモデルには次のような違いがあります。

- **タスクタイプの指定:** `gemini-embedding-001` では、`task_type` パラメータ（`SEMANTIC_SIMILARITY`、`RETRIEVAL_DOCUMENT` など）を使用してタスクタイプを指定します。`gemini-embedding-2` では、`task_type` パラメータは対象外です。代わりに、テキストのみのタスクのプロンプトにタスクの指示を直接含める必要があります。さまざまなユースケースのプロンプトの形式設定方法については、[Embeddings 2 を使用したタスクタイプ](#task-types-embeddings-2)をご覧ください。
- **エンベディングの集約:** `gemini-embedding-001` は、入力リスト内の各文字列に対して個別のエンベディングを生成します。一方、`gemini-embedding-2` は、複数の入力（テキストや画像など）が 1 つのリクエストで直接提供された場合、単一の集約されたエンベディングを生成します。個々の入力に対して個別のエンベディングを生成するには、各入力を `Content` オブジェクトでラップするか、[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja#batch-embedding) を使用します。詳細については、[エンベディングの集計](#embedding-aggregation)をご覧ください。
- **正規化:** `output_dimensionality` を使用して 3, 072 個未満のディメンションでエンベディングをリクエストすると、`gemini-embedding-2` はこれらの切り捨てられたエンベディングを自動的に正規化します。`gemini-embedding-001` では、3, 072 以外のディメンションに対して手動で正規化を行う必要があります。詳しくは、[小さいサイズの品質を確保する](#quality-for-smaller-dimensions)をご覧ください。

## バッチ エンベディング

レイテンシが問題にならない場合は、[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ja#batch-embedding) で Gemini エンベディング モデルを使用してみてください。これにより、デフォルトのエンベディング料金の 50% でスループットを大幅に向上させることができます。[Batch API クックブック](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)で、使用を開始する方法の例をご覧ください。

## 責任ある使用に関する通知

新しいコンテンツを作成する生成 AI モデルとは異なり、Gemini エンベディング モデルは、入力データの形式を数値表現に変換することのみを目的としています。Google は、入力データの形式をリクエストされた数値形式に変換するエンベディング モデルを提供する責任を負いますが、ユーザーは入力したデータと結果のエンベディングに対する全責任を負います。Gemini エンベディング モデルを使用すると、アップロードするコンテンツに対して必要な権利を有することを確認したと見なされます。他者の知的財産やプライバシーの権利を侵害するコンテンツを生成しないでください。このサービスのご利用には、Google の[禁止事項ポリシー](https://policies.google.com/terms/generative-ai/use-policy?hl=ja)と[利用規約](https://ai.google.dev/gemini-api/terms?hl=ja)が適用されます。

## エンベディングを使用して構築を開始する

[エンベディングのクイックスタート ノートブック](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)で、モデルの機能を確認し、エンベディングをカスタマイズして可視化する方法を学習します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-05-29 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-05-29 UTC。"],[],[]]
