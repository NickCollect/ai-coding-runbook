---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=th
fetched_at: 2026-10-26T05:56:42.495543+00:00
title: "\u0e01\u0e32\u0e23\u0e1d\u0e31\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การฝัง

Gemini API มีโมเดลการฝังเพื่อสร้างการฝังสำหรับข้อความ รูปภาพ
วิดีโอ และเนื้อหาอื่นๆ จากนั้นจะใช้การฝังที่ได้สำหรับงานต่างๆ เช่น การค้นหาเชิงความหมาย การจัดประเภท และการจัดกลุ่ม ซึ่งจะให้ผลลัพธ์ที่แม่นยำยิ่งขึ้นและรับรู้บริบทได้ดีกว่าแนวทางที่อิงตามคีย์เวิร์ด

โมเดลล่าสุดอย่าง `gemini-embedding-2` เป็นโมเดลการฝังแบบหลายรูปแบบตัวแรกใน Gemini API โดยจะแมปข้อความ รูปภาพ วิดีโอ เสียง และเอกสารลงในพื้นที่การฝังแบบรวม ซึ่งช่วยให้ค้นหา จัดประเภท และจัดกลุ่มข้ามโมดอลได้ในกว่า 100 ภาษา ดูข้อมูลเพิ่มเติมได้ที่[ส่วนการฝังแบบมัลติโมดัล](#multimodal) สำหรับกรณีการใช้งานที่มีเฉพาะข้อความ
`gemini-embedding-001` จะยังคงใช้งานได้

การสร้างระบบ Retrieval Augmented Generation (RAG) เป็น Use Case ทั่วไปสำหรับ
ผลิตภัณฑ์ AI Embedding มีบทบาทสำคัญในการปรับปรุงเอาต์พุตโมเดลอย่างมาก
ด้วยความถูกต้องตามข้อเท็จจริง ความสอดคล้อง และความสมบูรณ์เชิงบริบทที่ดียิ่งขึ้น หากต้องการใช้โซลูชัน RAG ที่มีการจัดการ เราได้สร้างเครื่องมือ[ค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)
ซึ่งช่วยให้การทำ RAG จัดการได้ง่ายขึ้นและคุ้มค่ากว่า

## การสร้างการฝัง

ใช้`embedContent`เพื่อสร้างการฝังข้อความ

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

Client client = new Client();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", null);

System.out.println(response.embeddings().orElse(null));
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

## ระบุประเภทงานเพื่อปรับปรุงประสิทธิภาพ

คุณสามารถใช้การฝังสำหรับงานที่หลากหลาย ตั้งแต่การจัดประเภทไปจนถึงการค้นหาเอกสาร
การระบุประเภทงานที่ถูกต้องจะช่วยเพิ่มประสิทธิภาพการฝังสำหรับ
ความสัมพันธ์ที่ต้องการ ซึ่งจะช่วยเพิ่มความแม่นยำและประสิทธิภาพ

### ประเภทงานที่มีการฝัง 2

สำหรับงานที่มีเฉพาะข้อความซึ่งมี `gemini-embedding-2` เราขอแนะนำอย่างยิ่งให้คุณ
เพิ่มวิธีการทำงานในพรอมต์ ซึ่งทำได้โดยการจัดรูปแบบ
คำค้นหาและเอกสารด้วยคำนำหน้างานที่ถูกต้อง

เมื่อสร้าง[การฝังรายการเดียวตามอินพุตแบบมัลติโมดอล](#embedding-aggregation) โดยทั่วไปเราไม่แนะนำให้เติมคำสั่งงานที่ส่วนข้อความของอินพุต ในบางกรณีจะช่วยปรับปรุง
ประสิทธิภาพ แต่ในบางกรณีจะลดประสิทธิภาพ

ตารางต่อไปนี้แสดงตัวอย่างวิธีจัดรูปแบบการค้นหาและเอกสารสำหรับ
กรณีการใช้งานแบบสมมาตรและอสมมาตรโดยใช้โมเดล `gemini-embedding-2`

**กรณีการใช้งานการดึงข้อมูล (รูปแบบอสมมาตร)**

ในกรณีการใช้งานแบบอสมมาตร ให้เพิ่มคำนำหน้างานไปยังคำค้นหาและใช้
โครงสร้างเอกสารกับเนื้อหาที่ต้องการฝังและดึงข้อมูล

| กรณีการใช้งาน | โครงสร้างการค้นหา | โครงสร้างเอกสาร |
| --- | --- | --- |
| คำค้นหา | `task: search result | query: {content}` | `title: {title} | text: {content}` หากไม่มีชื่อ ให้ใช้ `title: none` |
| การตอบคำถาม | `task: question answering | query: {content}` | `title: {title} | text: {content}` |
| การตรวจสอบข้อเท็จจริง | `task: fact checking | query: {content}` | `title: {title} | text: {content}` |
| การดึงข้อมูลโค้ด | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

**ตัวอย่างการใช้งาน**

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

**กรณีการใช้งานแบบอินพุตเดียว (รูปแบบสมมาตร)**

ในกรณีการใช้งานแบบสมมาตร สำหรับงานเดียวกัน ให้ใช้การจัดรูปแบบเดียวกัน
สำหรับคำค้นหาและเอกสาร

| กรณีการใช้งาน | โครงสร้างอินพุต |
| --- | --- |
| การจัดประเภท | `task: classification | query: {content}` |
| การจัดกลุ่ม | `task: clustering | query: {content}` |
| ความคล้ายคลึงกันเชิงความหมาย | `task: sentence similarity | query: {content}` อย่าใช้เพื่อการค้นหาหรือการดึงข้อมูล มีไว้สำหรับความคล้ายคลึงของข้อความเชิงความหมาย |

**ตัวอย่างการใช้งาน**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

คุณควรใช้ฟีเจอร์นี้อย่างสม่ำเสมอ เช่น หากฝังเอกสารด้วย `f'task: classification | query: {content}'` คำค้นหาควรฝังตามรูปแบบงานนี้ด้วย

### ประเภทงานที่มีการฝัง 1

สำหรับ `gemini-embedding-001` คุณระบุ `task_type` ได้ใน `embedContent`
method ดูรายการประเภทงานที่รองรับทั้งหมดได้ในตาราง[ประเภทงานที่รองรับ](#supported-task-types)

ตัวอย่างต่อไปนี้แสดงวิธีใช้ `SEMANTIC_SIMILARITY` เพื่อตรวจสอบว่าข้อความ 2 สตริงมีความหมายคล้ายกันมากน้อยเพียงใด

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
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;
import java.util.List;

Client client = new Client();

List<String> texts =
    Arrays.asList(
        "What is the meaning of life?",
        "What is the purpose of existence?",
        "How do I bake a cake?");

EmbedContentConfig config =
    EmbedContentConfig.builder().taskType("SEMANTIC_SIMILARITY").build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-001", texts, config);

List<ContentEmbedding> embeddings = response.embeddings().get();

for (int i = 0; i < texts.size(); i++) {
  for (int j = i + 1; j < texts.size(); j++) {
    List<Float> v1 = embeddings.get(i).values().get();
    List<Float> v2 = embeddings.get(j).values().get();
    double dotProduct = 0.0;
    double normA = 0.0;
    double normB = 0.0;
    for (int k = 0; k < v1.size(); k++) {
      dotProduct += v1.get(k) * v2.get(k);
      normA += v1.get(k) * v1.get(k);
      normB += v2.get(k) * v2.get(k);
    }
    double similarity = dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
    System.out.printf(
        "Similarity between '%s' and '%s': %.4f%n", texts.get(i), texts.get(j), similarity);
  }
}
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

ข้อมูลโค้ดจะแสดงให้เห็นว่าข้อความส่วนต่างๆ มีความคล้ายคลึงกันมากน้อยเพียงใดเมื่อเรียกใช้

#### ประเภทงานที่รองรับ

ประเภทงานที่รองรับสำหรับ `gemini-embedding-001`

| ประเภทงาน | คำอธิบาย | ตัวอย่าง |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | การฝังที่เพิ่มประสิทธิภาพเพื่อประเมินความคล้ายคลึงของข้อความ | ระบบการแนะนำ การตรวจหาเนื้อหาที่ซ้ำกัน |
| **การจัดประเภท** | การฝังที่เพิ่มประสิทธิภาพเพื่อจัดประเภทข้อความตามป้ายกำกับที่กำหนดไว้ล่วงหน้า | การวิเคราะห์ความเห็น การตรวจจับสแปม |
| **การจัดกลุ่ม** | การฝังที่ได้รับการเพิ่มประสิทธิภาพเพื่อจัดกลุ่มข้อความตามความคล้ายคลึงกัน | การจัดระเบียบเอกสาร การวิจัยตลาด การตรวจจับความผิดปกติ |
| **RETRIEVAL\_DOCUMENT** | การฝังที่เพิ่มประสิทธิภาพสำหรับการค้นหาเอกสาร | จัดทำดัชนีบทความ หนังสือ หรือหน้าเว็บสำหรับการค้นหา |
| **RETRIEVAL\_QUERY** | การฝังที่เพิ่มประสิทธิภาพสําหรับคําค้นหาทั่วไป ใช้ `RETRIEVAL_QUERY` สำหรับการค้นหา และ `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | โฆษณาการค้นหาที่กำหนดเอง |
| **CODE\_RETRIEVAL\_QUERY** | การฝังที่เพิ่มประสิทธิภาพสำหรับการดึงข้อมูลโค้ดบล็อกตามคำค้นหาที่เป็นภาษาธรรมชาติ ใช้ `CODE_RETRIEVAL_QUERY` สำหรับคำค้นหา และ `RETRIEVAL_DOCUMENT` สำหรับบล็อกโค้ดที่จะดึงข้อมูล | คำแนะนำและการค้นหาโค้ด |
| **QUESTION\_ANSWERING** | การฝังสำหรับคำถามในระบบตอบคำถาม ซึ่งได้รับการเพิ่มประสิทธิภาพเพื่อค้นหาเอกสารที่ตอบคำถาม ใช้ `QUESTION_ANSWERING` สำหรับคำถาม และ `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | แชทบ็อกซ์ |
| **FACT\_VERIFICATION** | การฝังสำหรับข้อความที่ต้องได้รับการยืนยัน ซึ่งได้รับการเพิ่มประสิทธิภาพสำหรับการดึงเอกสารที่มีหลักฐานที่สนับสนุนหรือหักล้างข้อความ ใช้ `FACT_VERIFICATION` สำหรับข้อความเป้าหมาย และ `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | ระบบตรวจสอบข้อเท็จจริงอัตโนมัติ |

## การควบคุมขนาดการฝัง

ทั้ง `gemini-embedding-001` และ `gemini-embedding-2` ได้รับการฝึกโดยใช้
เทคนิคการเรียนรู้ด้วยการแทน Matryoshka (MRL) ซึ่งสอนโมเดลให้
เรียนรู้การฝังที่มีมิติข้อมูลสูงซึ่งมีส่วนเริ่มต้น (หรือคำนำหน้า)
ซึ่งเป็นเวอร์ชันที่ง่ายกว่าและมีประโยชน์ของข้อมูลเดียวกัน

ใช้พารามิเตอร์ `output_dimensionality` เพื่อควบคุมขนาดของ
เวกเตอร์การฝังเอาต์พุต การเลือกมิติข้อมูลเอาต์พุตที่เล็กลงจะช่วยประหยัด
พื้นที่เก็บข้อมูลและเพิ่มประสิทธิภาพการคำนวณสำหรับแอปพลิเคชันดาวน์สตรีม
โดยที่คุณภาพไม่ลดลงมากนัก โดยค่าเริ่มต้น โมเดลทั้ง 2 จะแสดงผลเอาต์พุตโมเดลการฝังที่มีมิติข้อมูล 3072 แต่คุณสามารถตัดให้มีขนาดเล็กลงได้โดยไม่สูญเสียคุณภาพเพื่อประหยัดพื้นที่เก็บข้อมูล เราขอแนะนำให้ใช้ขนาดเอาต์พุต 768, 1536 หรือ 3072

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
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentConfig;
import com.google.genai.types.EmbedContentResponse;

Client client = new Client();

EmbedContentConfig config =
    EmbedContentConfig.builder().outputDimensionality(768).build();

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", "What is the meaning of life?", config);

ContentEmbedding embeddingObj = response.embeddings().get().get(0);
int embeddingLength = embeddingObj.values().get().size();

System.out.println("Length of embedding: " + embeddingLength);
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

ตัวอย่างเอาต์พุตจากข้อมูลโค้ด

```
Length of embedding: 768
```

## การดูแลคุณภาพสำหรับขนาดที่เล็กลง

แม้ว่าการฝังที่มีมิติข้อมูล 3072 ค่าเริ่มต้นจะได้รับการทำให้เป็นมาตรฐานเสมอ แต่ Gemini
Embedding 2 ยังทำให้มิติข้อมูลที่ถูกตัดทอนเป็นมาตรฐานโดยอัตโนมัติด้วย (เช่น 768, 1536) ซึ่งจะช่วยให้มั่นใจได้ว่าระบบจะคำนวณความคล้ายกันเชิงความหมายผ่านทิศทางเวกเตอร์แทนที่จะเป็นขนาด จึงให้ผลลัพธ์ที่แม่นยำยิ่งขึ้นตั้งแต่เริ่มต้น

**รุ่นเก่า**: หากใช้ `gemini-embedding-001` คุณต้องทําการปรับขนาดที่ไม่ใช่ 3072 ด้วยตนเองดังนี้

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

ตัวอย่างเอาต์พุตจากข้อมูลโค้ดนี้

```
Normed embedding length: 768
Norm of normed embedding: 1.000000
```

ตารางต่อไปนี้แสดงคะแนน MTEB ซึ่งเป็นเกณฑ์มาตรฐานที่ใช้กันโดยทั่วไปสำหรับ
การฝังสำหรับมิติข้อมูลต่างๆ ผลลัพธ์แสดงให้เห็นว่าประสิทธิภาพไม่ได้ขึ้นอยู่กับขนาดของมิติข้อมูลการฝังอย่างเคร่งครัด โดยมิติข้อมูลที่ต่ำกว่าจะให้คะแนนเทียบเท่ากับมิติข้อมูลที่สูงกว่า

| มิติข้อมูล MRL | คะแนน MTEB (การฝัง Gemini 001) |
| --- | --- |
| 2048 | 68.16 |
| 1536 | 68.17 |
| 768 | 67.99 |
| 512 | 67.55 |
| 256 | 66.19 |
| 128 | 63.31 |

## การฝังแบบหลายรูปแบบ

`gemini-embedding-2` โมเดลรองรับอินพุตแบบหลายรูปแบบ ซึ่งช่วยให้คุณ
ฝังเนื้อหารูปภาพ วิดีโอ เสียง และเอกสารควบคู่ไปกับข้อความได้ ระบบจะแมปรูปแบบข้อมูลทั้งหมด
ลงในพื้นที่การฝังเดียวกัน ซึ่งช่วยให้ค้นหาและ
เปรียบเทียบข้ามรูปแบบได้

### รูปแบบที่รองรับและขีดจำกัด

ขีดจำกัดโทเค็นอินพุตสูงสุดโดยรวมคือ 8,192 โทเค็น

| รูปแบบ | ข้อกำหนดและขีดจำกัด |
| --- | --- |
| **Text** | รองรับโทเค็นสูงสุด 8,192 รายการ |
| **รูปภาพ** | ส่งรูปภาพได้สูงสุด 6 รูปต่อคำขอ รูปแบบที่รองรับ ได้แก่ PNG, JPEG |
| **เสียง** | ระยะเวลาสูงสุด 180 วินาที รูปแบบที่รองรับ: MP3, WAV |
| **วิดีโอ** | ระยะเวลาสูงสุด 120 วินาที รูปแบบที่รองรับ: MP4, MOV ตัวแปลงรหัสที่รองรับ: H264, H265, AV1, VP9  ระบบจะประมวลผลเฟรมสูงสุด 32 เฟรมต่อวิดีโอ โดยวิดีโอสั้น (≤32 วินาที) จะสุ่มตัวอย่างที่ 1 FPS ส่วนวิดีโอที่ยาวกว่านั้นจะสุ่มตัวอย่างอย่างสม่ำเสมอเป็น 32 เฟรม ระบบจะไม่ประมวลผลแทร็กเสียงในไฟล์วิดีโอ |
| **เอกสาร (PDF)** | ส่งได้สูงสุด 1 ไฟล์ต่อคำขอ โดยมีได้สูงสุด 6 หน้า |

### การฝังรูปภาพ

ตัวอย่างต่อไปนี้แสดงวิธีฝังรูปภาพโดยใช้
`gemini-embedding-2`

คุณระบุรูปภาพเป็นข้อมูลแบบอินไลน์หรือเป็นไฟล์ที่อัปโหลดผ่าน [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) ได้

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
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("example.png"));

Content content = Content.fromParts(Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

### การรวมการฝัง

เมื่อทำงานกับเนื้อหาหลายรูปแบบ วิธีที่คุณจัดโครงสร้างอินพุตจะมีผลต่อเอาต์พุตการฝังดังนี้

- **หลายส่วน (รวม):** การเพิ่มอินพุตหลายรายการลงในพารามิเตอร์
  `contents` โดยตรงจะสร้างการฝังแบบรวม 1 รายการสำหรับอินพุตทั้งหมด
- **ออบเจ็กต์ `Content` หลายรายการ (แยกกัน):** การห่ออินพุตแต่ละรายการในออบเจ็กต์
  `Content` และการส่งผ่านในพารามิเตอร์ `contents` จะแสดงผล
  การฝังแยกกันสำหรับแต่ละรายการ
- **การแสดงระดับโพสต์:** สำหรับออบเจ็กต์ที่ซับซ้อน เช่น โพสต์โซเชียลมีเดีย
  ที่มีรายการสื่อหลายรายการ เราขอแนะนำให้รวบรวมการฝังแยกกัน
  (เช่น โดยการหาค่าเฉลี่ย) เพื่อสร้างการแสดงระดับโพสต์ที่สอดคล้องกัน

ตัวอย่างต่อไปนี้แสดงวิธีสร้างการฝังแบบรวมสำหรับอินพุตข้อความและรูปภาพ เพียงเพิ่มอินพุตหลายรายการลงในพารามิเตอร์ `contents` ดังนี้

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
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

Content content =
    Content.fromParts(
        Part.fromText("An image of a dog"),
        Part.fromBytes(imageBytes, "image/png"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

// This produces one embedding
for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
  System.out.println(embedding.values().orElse(Collections.emptyList()));
}
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

ในทางกลับกัน หากคุณใช้ออบเจ็กต์ `Content` ภายในพารามิเตอร์ `contents`
ระบบจะแสดงผลการฝังที่แยกกัน ตัวอย่างนี้สร้างการฝังหลายรายการในการเรียกใช้การฝังครั้งเดียว

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
import java.util.Arrays;
import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.ContentEmbedding;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("dog.png"));

List<Content> contents =
    Arrays.asList(
        Content.fromParts(Part.fromText("task: classification | query: An image of a dog")),
        Content.fromParts(Part.fromBytes(imageBytes, "image/png")));

// Embed each Content object separately to produce separate embeddings
for (Content content : contents) {
  EmbedContentResponse response =
      client.models.embedContent("gemini-embedding-2", content, null);
  for (ContentEmbedding embedding : response.embeddings().orElse(Collections.emptyList())) {
    System.out.println(embedding.values().orElse(Collections.emptyList()));
  }
}
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

### การฝังเสียง

ตัวอย่างต่อไปนี้แสดงวิธีฝังไฟล์เสียงโดยใช้
`gemini-embedding-2`

คุณระบุไฟล์เสียงเป็นข้อมูลแบบอินไลน์หรือเป็นไฟล์ที่อัปโหลดผ่าน [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) ได้

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
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] audioBytes = Files.readAllBytes(Paths.get("example.mp3"));

Content content = Content.fromParts(Part.fromBytes(audioBytes, "audio/mpeg"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

### การฝังวิดีโอ

ตัวอย่างต่อไปนี้แสดงวิธีฝังวิดีโอโดยใช้
`gemini-embedding-2`

คุณระบุวิดีโอเป็นข้อมูลแบบอินไลน์หรือเป็นไฟล์ที่อัปโหลดผ่าน [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) ได้

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
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Collections;

Client client = new Client();

byte[] videoBytes = Files.readAllBytes(Paths.get("example.mp4"));

Content content = Content.fromParts(Part.fromBytes(videoBytes, "video/mp4"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(
    response.embeddings().get().get(0).values().orElse(Collections.emptyList()));
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

หากต้องการฝังวิดีโอที่มีความยาวมากกว่า 120 วินาที คุณสามารถแบ่งวิดีโอออกเป็น
ส่วนที่ทับซ้อนกันและฝังแต่ละส่วนแยกกันได้

### การฝังเอกสาร

คุณฝังเอกสารในรูปแบบ PDF ได้โดยตรง โมเดลจะประมวลผลเนื้อหาภาพและข้อความ
ของแต่ละหน้า

คุณระบุ PDF เป็นข้อมูลแบบอินไลน์หรือเป็นไฟล์ที่อัปโหลดผ่าน [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th) ได้

#### วิธีที่โมเดลประมวลผล PDF

เมื่อฝัง PDF โมเดลจะประมวลผลเอกสารโดยใช้ทั้งฟีเจอร์ภาพและข้อความ

- **การแสดงภาพ:** โมเดลจะแสดงผลแต่ละหน้าเป็นรูปภาพ ซึ่งใช้โทเค็น **258 โทเค็น**ต่อหน้า
- **การแยกข้อความ:** โมเดลจะแยกข้อความจากเอกสาร สำหรับ **PDF เนทีฟ** (ซึ่งมีข้อความดิจิทัล) โมเดลจะดึงข้อความโดยตรง สำหรับ **PDF ที่สแกน** (ซึ่งมีรูปภาพของข้อความ) โมเดลจะเรียกใช้การรู้จำอักขระด้วยภาพ (OCR) โดยอัตโนมัติเพื่อดึงข้อความ

หากต้องการคำนวณจำนวนโทเค็นทั้งหมดสำหรับ PDF ให้เพิ่มโทเค็นภาพ (258 ต่อหน้า) ลงในโทเค็นข้อความ อินพุตของคุณต้องอยู่ภายใน**ขีดจำกัดโทเค็น 8,192 รายการ**ของโมเดล (ใช้ร่วมกันในทุกรูปแบบ) ระบบจะตัดอินพุตที่เกินขีดจำกัดนี้โดยไม่แจ้งให้ทราบ

#### ขีดจำกัดของ PDF

- **ไฟล์ต่อคำขอ:** คุณส่งไฟล์ PDF ได้สูงสุด 1 ไฟล์
- **ขีดจำกัดของหน้า:** คุณส่งได้สูงสุด 6 หน้าต่อไฟล์ เราขอแนะนำอย่างยิ่งให้ใช้ 1 หน้าต่อ PDF เพื่อคุณภาพที่ดีที่สุด

ตัวอย่างต่อไปนี้แสดงวิธีฝัง PDF โดยใช้ `gemini-embedding-2`

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
import com.google.genai.types.Content;
import com.google.genai.types.EmbedContentResponse;
import com.google.genai.types.Part;
import java.nio.file.Files;
import java.nio.file.Paths;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("example.pdf"));

Content content = Content.fromParts(Part.fromBytes(pdfBytes, "application/pdf"));

EmbedContentResponse response =
    client.models.embedContent("gemini-embedding-2", content, null);

System.out.println(response.embeddings().orElse(null));
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

## กรณีการใช้งาน

การฝังข้อความมีความสําคัญอย่างยิ่งสําหรับกรณีการใช้งาน AI ทั่วไปที่หลากหลาย เช่น

- **การสร้างผลลัพธ์ที่เสริมด้วยการดึงข้อมูล (RAG):** การฝังจะช่วยปรับปรุงคุณภาพ
  ของข้อความที่สร้างขึ้นโดยการดึงและรวมข้อมูลที่เกี่ยวข้องเข้ากับ
  บริบทของโมเดล
- **การดึงข้อมูล:** ค้นหาข้อความหรือเอกสารที่คล้ายกันมากที่สุดในเชิงความหมายเมื่อได้รับข้อความนำเข้า

  [บทแนะนำการค้นหาเอกสารtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **การจัดอันดับผลการค้นหาใหม่**: จัดลำดับความสำคัญของรายการที่เกี่ยวข้องที่สุดโดยใช้การให้คะแนนความหมายของผลลัพธ์เริ่มต้นเทียบกับคำค้นหา

  [บทแนะนำการจัดอันดับผลการค้นหาใหม่task](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **การตรวจจับความผิดปกติ:** การเปรียบเทียบกลุ่มการฝังจะช่วยระบุ
  แนวโน้มที่ซ่อนอยู่หรือค่าผิดปกติ

  [บทแนะนำการตรวจจับความผิดปกติbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **การแยกประเภท:** จัดหมวดหมู่ข้อความโดยอัตโนมัติตามเนื้อหา เช่น การวิเคราะห์ความเห็น หรือการตรวจจับสแปม

  [บทแนะนำการแยกประเภทtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **การจัดกลุ่ม:** ทำความเข้าใจความสัมพันธ์ที่ซับซ้อนได้อย่างมีประสิทธิภาพโดยการสร้างคลัสเตอร์
  และการแสดงภาพของข้อมูลฝัง

  [บทแนะนำการแสดงภาพคลัสเตอร์bubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## การจัดเก็บการฝัง

เมื่อนำการฝังไปใช้ในเวอร์ชันที่ใช้งานจริง คุณมักจะ
ใช้**ฐานข้อมูลเวกเตอร์**เพื่อจัดเก็บ จัดทำดัชนี และเรียกข้อมูล
การฝังที่มีมิติสูงอย่างมีประสิทธิภาพ Google Cloud มีบริการข้อมูลที่มีการจัดการซึ่ง
ใช้เพื่อวัตถุประสงค์นี้ได้ รวมถึง
[การค้นหาเวกเตอร์ 2.0 ของแพลตฟอร์มเอเจนต์ Gemini Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview?hl=th)
[BigQuery](https://cloud.google.com/bigquery/docs/introduction?hl=th)
[AlloyDB](https://cloud.google.com/alloydb/docs/overview?hl=th) และ
[Cloud SQL](https://cloud.google.com/sql/docs/postgres/introduction?hl=th)

บทแนะนำต่อไปนี้แสดงวิธีใช้ฐานข้อมูลเวกเตอร์ของบุคคลที่สามอื่นๆ
กับ Gemini Embedding

- [บทแนะนำ ChromaDBbolt](https://docs.trychroma.com/integrations/embedding-models/google-gemini)
- [บทแนะนำ QDrantbolt](https://qdrant.tech/documentation/embeddings/gemini/)
- [บทแนะนำ Weaviatebolt](https://docs.weaviate.io/weaviate/model-providers/google)
- [บทแนะนำเกี่ยวกับ Pineconebolt](https://github.com/google-gemini/cookbook/blob/main/examples/langchain/Gemini_LangChain_QA_Pinecone_WebLoad.ipynb)

## เวอร์ชันของโมเดล

### Gemini Embedding 2

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | **Gemini API**  `gemini-embedding-2` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ รูปภาพ วิดีโอ เสียง PDF  **เอาต์พุต**  การฝังข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  8,192  **ขนาดมิติข้อมูลเอาต์พุต**  ยืดหยุ่น รองรับ: 128 - 3072, แนะนำ: 768, 1536, 3072 |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - เสถียร: `gemini-embedding-2` |
| calendar\_monthการอัปเดตล่าสุด | เมษายน 2026 |

### การฝัง Gemini

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | **Gemini API**  `gemini-embedding-001` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ  **เอาต์พุต**  การฝังข้อความ |
| token\_autoขีดจำกัดของโทเค็น[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=th) | **ขีดจำกัดโทเค็นอินพุต**  2,048  **ขนาดมิติข้อมูลเอาต์พุต**  ยืดหยุ่น รองรับ: 128 - 3072, แนะนำ: 768, 1536, 3072 |
| 123เวอร์ชัน | อ่านรายละเอียดเพิ่มเติมได้ใน[รูปแบบเวอร์ชันของโมเดล](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#model-versions)  - เสถียร: `gemini-embedding-001` |
| calendar\_monthการอัปเดตล่าสุด | มิถุนายน 2025 |

สำหรับโมเดลการฝังที่เลิกใช้งานแล้ว โปรดไปที่หน้า[การเลิกใช้งาน](https://ai.google.dev/gemini-api/docs/deprecations?hl=th)

## การย้ายข้อมูลจาก gemini-embedding-001

Embedding Space ระหว่าง `gemini-embedding-001` กับ
`gemini-embedding-2` **ใช้ร่วมกันไม่ได้** ซึ่งหมายความว่าคุณไม่สามารถเปรียบเทียบการฝังที่โมเดลหนึ่งสร้างขึ้นกับการฝังที่อีกโมเดลหนึ่งสร้างขึ้นได้โดยตรง หากอัปเกรดเป็น `gemini-embedding-2` คุณต้อง
ฝังข้อมูลที่มีอยู่ทั้งหมดอีกครั้ง

นอกเหนือจากความเข้ากันไม่ได้แล้ว ยังมีความแตกต่างที่สำคัญอื่นๆ ระหว่าง
โมเดลทั้ง 2 ดังนี้

- **ข้อกำหนดประเภทงาน:** เมื่อใช้ `gemini-embedding-001` คุณจะระบุประเภทงานโดยใช้พารามิเตอร์ `task_type` (เช่น `SEMANTIC_SIMILARITY`, `RETRIEVAL_DOCUMENT`) เมื่อใช้ `gemini-embedding-2` ระบบจะไม่รองรับพารามิเตอร์ `task_type` แต่คุณควรใส่คำสั่งงาน
  ลงในพรอมต์โดยตรงสำหรับงานที่เป็นข้อความเท่านั้น ดูรายละเอียดเกี่ยวกับวิธีจัดรูปแบบพรอมต์สำหรับกรณีการใช้งานต่างๆ ได้ที่
  [ประเภทงานที่มีการฝัง 2](#task-types-embeddings-2)
- **การรวมการฝัง:** `gemini-embedding-001`สร้างการฝังแต่ละรายการ
  สำหรับสตริงแต่ละรายการในรายการอินพุต ในทางตรงกันข้าม
  `gemini-embedding-2` จะสร้างการฝังแบบรวมรายการเดียวเมื่อมีการระบุอินพุตหลายรายการ (เช่น ข้อความและรูปภาพ) ในคำขอเดียวโดยตรง หากต้องการสร้างการฝังแยกกันสำหรับอินพุตแต่ละรายการ ให้ห่ออินพุตแต่ละรายการใน`Content`ออบเจ็กต์ หรือใช้ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) ดูข้อมูลเพิ่มเติมได้ที่
  [การฝังการรวม](#embedding-aggregation)
- **การปรับให้เป็นมาตรฐาน:** หากคุณใช้ `output_dimensionality` เพื่อขอ Embedding
  ที่มีมิติน้อยกว่า 3072 มิติ `gemini-embedding-2` จะปรับ Embedding ที่ถูกตัดทอนเหล่านี้ให้เป็นมาตรฐานโดยอัตโนมัติ
  เมื่อใช้ `gemini-embedding-001` คุณ
  ต้องทําการปรับให้เป็นมาตรฐานด้วยตนเองสําหรับมิติข้อมูลอื่นๆ นอกเหนือจาก 3072 ดูรายละเอียดได้ที่
  [การรับประกันคุณภาพสำหรับขนาดที่เล็กลง](#quality-for-smaller-dimensions)

## การฝังแบบกลุ่ม

หากไม่กังวลเรื่องเวลาในการตอบสนอง ให้ลองใช้โมเดลการฝังของ Gemini กับ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) ซึ่ง
ช่วยให้มีปริมาณงานสูงขึ้นมากที่ 50% ของราคา Embedding เริ่มต้น
ดูตัวอย่างวิธีเริ่มต้นใช้งานได้ใน[สูตรการแก้ปัญหาของ Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)

## ประกาศเกี่ยวกับการใช้งานอย่างมีความรับผิดชอบ

โมเดลการฝัง Gemini มีไว้เพื่อเปลี่ยนรูปแบบข้อมูลอินพุตเป็นตัวแทนที่เป็นตัวเลขเท่านั้น
ซึ่งแตกต่างจากโมเดล Generative AI ที่สร้างเนื้อหาใหม่ แม้ว่า Google จะมีหน้าที่รับผิดชอบในการจัดหาโมเดลการฝัง
ที่แปลงรูปแบบของข้อมูลอินพุตเป็นรูปแบบตัวเลขที่ร้องขอ
แต่ผู้ใช้ยังคงมีหน้าที่รับผิดชอบอย่างเต็มที่ต่อข้อมูลที่ป้อนและเวกเตอร์
ที่ได้ การใช้โมเดลการฝังของ Gemini เป็นการยืนยันว่าคุณมีสิทธิ์ที่จำเป็นในเนื้อหาใดๆ ที่คุณอัปโหลด อย่าสร้างเนื้อหาที่ละเมิดสิทธิในทรัพย์สินทางปัญญาหรือสิทธิด้านความเป็นส่วนตัวของผู้อื่น การใช้บริการนี้เป็นไปตาม[นโยบายการใช้งานที่ไม่อนุญาต](https://policies.google.com/terms/generative-ai/use-policy?hl=th)และ[ข้อกำหนดในการให้บริการของ Google](https://ai.google.dev/gemini-api/terms?hl=th)

## เริ่มสร้างด้วยการฝัง

ดู[สมุดบันทึกการเริ่มต้นใช้งานฉบับย่อของ Embedding](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
เพื่อสำรวจความสามารถของโมเดลและดูวิธีปรับแต่งและแสดงภาพ
Embedding

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-09 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-09 UTC"],[],[]]
