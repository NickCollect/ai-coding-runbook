---
source_url: https://ai.google.dev/gemini-api/docs/embeddings?hl=th
fetched_at: 2026-06-22T06:30:56.357450+00:00
title: "\u0e01\u0e32\u0e23\u0e1d\u0e31\u0e07 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การฝัง

Gemini API มีโมเดลการฝังเพื่อสร้างการฝังสำหรับข้อความ รูปภาพ
วิดีโอ และเนื้อหาอื่นๆ จากนั้นจะใช้การฝังที่ได้เหล่านี้สำหรับงานต่างๆ
เช่น การค้นหาเชิงความหมาย การจัดประเภท และการจัดกลุ่ม ซึ่งให้ผลลัพธ์ที่แม่นยำมากขึ้น
และรับรู้บริบทได้ดีกว่าแนวทางที่อิงตามคีย์เวิร์ด

โมเดลล่าสุดอย่าง `gemini-embedding-2` เป็นโมเดลการฝังแบบหลายรูปแบบตัวแรกใน Gemini API โดยจะแมปข้อความ รูปภาพ วิดีโอ เสียง และเอกสารลงในพื้นที่การฝังแบบรวม ซึ่งช่วยให้ค้นหา จัดประเภท และจัดกลุ่มข้ามโมดอลได้ในกว่า 100 ภาษา ดูข้อมูลเพิ่มเติมได้ที่[ส่วนการฝังมัลติโมดัล](#multimodal) สำหรับกรณีการใช้งานที่มีเฉพาะข้อความ
`gemini-embedding-001` จะยังคงใช้งานได้

การสร้างระบบ Retrieval Augmented Generation (RAG) เป็น Use Case ทั่วไปสำหรับ
ผลิตภัณฑ์ AI Embedding มีบทบาทสำคัญในการปรับปรุงเอาต์พุตของโมเดลอย่างมาก
ด้วยความถูกต้องตามข้อเท็จจริง ความสอดคล้อง และความสมบูรณ์ตามบริบทที่ดียิ่งขึ้น หากต้องการใช้โซลูชัน RAG ที่มีการจัดการ เราได้สร้างเครื่องมือ[ค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)
ซึ่งช่วยให้การจัดการ RAG ง่ายขึ้นและประหยัดค่าใช้จ่ายมากขึ้น

## การสร้างการฝัง

ใช้`embedContent` วิธีการต่อไปนี้เพื่อสร้างการฝังข้อความ

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

## ระบุประเภทงานเพื่อปรับปรุงประสิทธิภาพ

คุณใช้การฝังสำหรับงานที่หลากหลายได้ ตั้งแต่การจัดประเภทไปจนถึงการค้นหาเอกสาร
การระบุประเภทงานที่ถูกต้องจะช่วยเพิ่มประสิทธิภาพการฝังสำหรับ
ความสัมพันธ์ที่ต้องการ ซึ่งจะช่วยเพิ่มความแม่นยำและประสิทธิภาพ

### ประเภทงานที่มี Embeddings 2

สำหรับงานที่มีเฉพาะข้อความซึ่งมี `gemini-embedding-2` เราขอแนะนำให้คุณ
เพิ่มวิธีการทำงานในพรอมต์ ซึ่งทำได้โดยการจัดรูปแบบ
คำค้นหาและเอกสารด้วยคำนำหน้าของงานที่ถูกต้อง

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
| การดึงข้อมูลรหัส | `task: code retrieval | query: {content}` | `title: {title} | text: {content}` |

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

**Use Case แบบอินพุตเดียว (รูปแบบสมมาตร)**

ในกรณีการใช้งานแบบสมมาตร ให้ใช้การจัดรูปแบบเดียวกันสำหรับคำค้นหาและเอกสารในงานเดียวกัน

| กรณีการใช้งาน | โครงสร้างอินพุต |
| --- | --- |
| การจัดประเภท | `task: classification | query: {content}` |
| การคลัสเตอร์ | `task: clustering | query: {content}` |
| ความคล้ายคลึงกันเชิงความหมาย | `task: sentence similarity | query: {content}` อย่าใช้เพื่อการค้นหาหรือการดึงข้อมูล มีไว้สำหรับความคล้ายคลึงกันของข้อความเชิงความหมาย |

**ตัวอย่างการใช้งาน**

### Python

```
# Generate embedding for query & document of your task.
def prepare_query_and_document(content):
    # return f'task: clustering | query: {content}'
    # return f'task: sentence similarity | query: {content}'
    return f'task: classification | query: {content}'
```

สิ่งสำคัญคือต้องใช้ฟีเจอร์งานอย่างสม่ำเสมอ เช่น หากฝังเอกสารด้วย `f'task: classification | query: {content}'` การค้นหาก็ควรฝังตามรูปแบบงานนี้ด้วย

### ประเภทงานที่มีการฝัง 1

สำหรับ `gemini-embedding-001` คุณระบุ `task_type` ในเมธอด `embedContent`
ได้ ดูรายการประเภทงานที่รองรับทั้งหมดได้ที่ตาราง[ประเภทงานที่รองรับ](#supported-task-types)

ตัวอย่างต่อไปนี้แสดงวิธีใช้ `SEMANTIC_SIMILARITY` เพื่อตรวจสอบว่าสตริงข้อความมีความหมายคล้ายกันมากน้อยเพียงใด

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

ข้อมูลโค้ดจะแสดงให้เห็นว่าข้อความแต่ละส่วนมีความคล้ายคลึงกันมากน้อยเพียงใดเมื่อเรียกใช้

#### ประเภทงานที่รองรับ

ประเภทงานที่รองรับสำหรับ `gemini-embedding-001` มีดังนี้

| ประเภทงาน | คำอธิบาย | ตัวอย่าง |
| --- | --- | --- |
| **SEMANTIC\_SIMILARITY** | การฝังที่เพิ่มประสิทธิภาพเพื่อประเมินความคล้ายคลึงของข้อความ | ระบบการแนะนำ การตรวจหาเนื้อหาที่ซ้ำกัน |
| **การจัดประเภท** | การฝังที่เพิ่มประสิทธิภาพเพื่อจัดประเภทข้อความตามป้ายกำกับที่ตั้งค่าไว้ล่วงหน้า | การวิเคราะห์ความเห็น การตรวจจับสแปม |
| **การจัดกลุ่ม** | การฝังที่ได้รับการเพิ่มประสิทธิภาพเพื่อจัดกลุ่มข้อความตามความคล้ายคลึงกัน | การจัดระเบียบเอกสาร การวิจัยตลาด การตรวจจับความผิดปกติ |
| **RETRIEVAL\_DOCUMENT** | การฝังที่เพิ่มประสิทธิภาพสำหรับการค้นหาเอกสาร | จัดทำดัชนีบทความ หนังสือ หรือหน้าเว็บสำหรับการค้นหา |
| **RETRIEVAL\_QUERY** | การฝังที่เพิ่มประสิทธิภาพสําหรับคําค้นหาทั่วไป ใช้ `RETRIEVAL_QUERY` สำหรับการค้นหา และ `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | โฆษณาการค้นหาที่กำหนดเอง |
| **CODE\_RETRIEVAL\_QUERY** | การฝังที่เพิ่มประสิทธิภาพสำหรับการดึงข้อมูลโค้ดบล็อกตามคำค้นหาที่เป็นภาษาธรรมชาติ ใช้ `CODE_RETRIEVAL_QUERY` สำหรับคำค้นหา และ `RETRIEVAL_DOCUMENT` สำหรับบล็อกโค้ดที่จะดึงข้อมูล | คำแนะนำและการค้นหาโค้ด |
| **QUESTION\_ANSWERING** | การฝังสำหรับคำถามในระบบตอบคำถาม ซึ่งได้รับการเพิ่มประสิทธิภาพเพื่อค้นหาเอกสารที่ตอบคำถาม ใช้ `QUESTION_ANSWERING` สำหรับคำถาม และ `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | แชทบ็อกซ์ |
| **FACT\_VERIFICATION** | การฝังสำหรับข้อความที่ต้องได้รับการยืนยัน ซึ่งได้รับการเพิ่มประสิทธิภาพเพื่อดึงเอกสารที่มีหลักฐานสนับสนุนหรือหักล้างข้อความ ใช้ `FACT_VERIFICATION` สำหรับข้อความเป้าหมาย `RETRIEVAL_DOCUMENT` สำหรับเอกสารที่จะดึงข้อมูล | ระบบตรวจสอบข้อเท็จจริงอัตโนมัติ |

## การควบคุมขนาดการฝัง

ทั้ง `gemini-embedding-001` และ `gemini-embedding-2` ได้รับการฝึกโดยใช้เทคนิค Matryoshka Representation Learning (MRL) ซึ่งสอนโมเดลให้
เรียนรู้การฝังที่มีมิติสูงซึ่งมีส่วนเริ่มต้น (หรือคำนำหน้า) ที่
เป็นเวอร์ชันที่ง่ายกว่าและมีประโยชน์เช่นกันของข้อมูลเดียวกัน

ใช้พารามิเตอร์ `output_dimensionality` เพื่อควบคุมขนาดของ
เวกเตอร์การฝังเอาต์พุต การเลือกมิติข้อมูลเอาต์พุตที่เล็กลงจะช่วยประหยัด
พื้นที่เก็บข้อมูลและเพิ่มประสิทธิภาพการคำนวณสำหรับแอปพลิเคชันดาวน์สตรีม
โดยที่คุณภาพไม่ลดลงมากนัก โดยค่าเริ่มต้น โมเดลทั้ง 2 จะแสดงผลการฝังที่มีมิติ 3072 แต่คุณสามารถตัดให้มีขนาดเล็กลงได้โดยไม่สูญเสียคุณภาพเพื่อประหยัดพื้นที่เก็บข้อมูล เราขอแนะนำให้ใช้ขนาดเอาต์พุต 768, 1536 หรือ 3072

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

ตัวอย่างเอาต์พุตจากข้อมูลโค้ด

```
Length of embedding: 768
```

## การดูแลคุณภาพสำหรับขนาดที่เล็กลง

แม้ว่าการฝังที่มีมิติข้อมูล 3072 ค่าเริ่มต้นจะได้รับการทำให้เป็นมาตรฐานเสมอ แต่ Gemini
Embedding 2 จะทำให้มิติข้อมูลที่ถูกตัดทอนเป็นมาตรฐานโดยอัตโนมัติด้วย (เช่น 768, 1536) ซึ่งจะช่วยให้มั่นใจได้ว่าระบบจะคำนวณความคล้ายกันเชิงความหมายผ่านทิศทางเวกเตอร์แทนที่จะเป็นขนาด จึงให้ผลลัพธ์ที่แม่นยำยิ่งขึ้นตั้งแต่เริ่มต้น

**รุ่นเก่า**: หากใช้ `gemini-embedding-001` คุณต้องปรับขนาดที่ไม่ใช่ 3072 ด้วยตนเองโดยทำดังนี้

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
การฝังสำหรับมิติข้อมูลต่างๆ ผลลัพธ์แสดงให้เห็นว่าประสิทธิภาพ
ไม่ได้เชื่อมโยงกับขนาดของมิติข้อมูลการฝังอย่างเคร่งครัด โดยมิติข้อมูลที่ต่ำกว่า
จะให้คะแนนเทียบเท่ากับมิติข้อมูลที่สูงกว่า

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
ลงในพื้นที่ฝังเดียวกัน ซึ่งช่วยให้ค้นหาและ
เปรียบเทียบข้ามรูปแบบได้

### รูปแบบที่รองรับและขีดจำกัด

ขีดจำกัดโทเค็นอินพุตสูงสุดโดยรวมคือ 8,192 โทเค็น

| รูปแบบ | ข้อกำหนดและขีดจำกัด |
| --- | --- |
| **Text** | รองรับโทเค็นสูงสุด 8,192 รายการ |
| **รูปภาพ** | สูงสุด 6 รูปภาพต่อคำขอ รูปแบบที่รองรับ ได้แก่ PNG, JPEG |
| **เสียง** | ระยะเวลาสูงสุด 180 วินาที รูปแบบที่รองรับ ได้แก่ MP3, WAV |
| **วิดีโอ** | ระยะเวลาสูงสุด 120 วินาที รูปแบบที่รองรับ ได้แก่ MP4, MOV ตัวแปลงรหัสที่รองรับ: H264, H265, AV1, VP9  ระบบจะประมวลผลเฟรมสูงสุด 32 เฟรมต่อวิดีโอ โดยวิดีโอ Shorts (≤32 วินาที) จะสุ่มตัวอย่างที่ 1 FPS ส่วนวิดีโอที่ยาวกว่านั้นจะสุ่มตัวอย่างอย่างสม่ำเสมอเป็น 32 เฟรม ระบบจะไม่ประมวลผลแทร็กเสียงในไฟล์วิดีโอ |
| **เอกสาร (PDF)** | สูงสุด 1 ไฟล์ต่อคำขอ ไม่เกิน 6 หน้า |

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

เมื่อทำงานกับเนื้อหาหลายรูปแบบ โครงสร้างของอินพุตจะส่งผลต่อ
เอาต์พุตการฝังดังนี้

- **หลายส่วน (รวม):** การเพิ่มอินพุตหลายรายการลงในพารามิเตอร์
  `contents` โดยตรงจะสร้างการฝังแบบรวม 1 รายการสำหรับอินพุตทั้งหมด
- **ออบเจ็กต์ `Content` หลายรายการ (แยกกัน):** การรวมอินพุตแต่ละรายการไว้ในออบเจ็กต์
  `Content` และการส่งผ่านอินพุตเหล่านั้นในพารามิเตอร์ `contents` จะส่งคืน
  การฝังแยกกันสำหรับแต่ละรายการ
- **การแสดงระดับโพสต์:** สำหรับออบเจ็กต์ที่ซับซ้อน เช่น โพสต์โซเชียลมีเดีย
  ที่มีรายการสื่อหลายรายการ เราขอแนะนำให้รวบรวมการฝังแยกกัน
  (เช่น โดยการหาค่าเฉลี่ย) เพื่อสร้างการแสดงระดับโพสต์ที่สอดคล้องกัน

ตัวอย่างต่อไปนี้แสดงวิธีสร้างการฝังแบบรวมสำหรับข้อความและ
อินพุตรูปภาพ เพียงเพิ่มอินพุตหลายรายการลงในพารามิเตอร์ `contents` ดังนี้

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

ในทางกลับกัน หากคุณใช้วัตถุ `Content` ภายในพารามิเตอร์ `contents`
ระบบจะแสดงผลการฝังแยกกัน ตัวอย่างนี้สร้างการฝังหลายรายการในการเรียกใช้การฝังครั้งเดียว

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

หากต้องการคำนวณจำนวนโทเค็นทั้งหมดสำหรับ PDF ให้เพิ่มโทเค็นภาพ (258 ต่อหน้า) ลงในโทเค็นข้อความ อินพุตต้องอยู่ภายใน**ขีดจำกัดโทเค็น 8,192 รายการ**ของโมเดล (แชร์ในทุกรูปแบบ) ระบบจะตัดอินพุตที่เกินขีดจำกัดนี้โดยไม่แจ้งให้ทราบ

#### ขีดจำกัดของ PDF

- **ไฟล์ต่อคำขอ:** คุณส่งไฟล์ PDF ได้สูงสุด 1 ไฟล์
- **ขีดจํากัดหน้า:** คุณส่งได้สูงสุด 6 หน้าต่อไฟล์ เราขอแนะนำอย่างยิ่งให้ใช้ 1 หน้าต่อ PDF เพื่อคุณภาพที่ดีที่สุด

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

- **การสร้างผลลัพธ์ที่เสริมด้วยการดึงข้อมูล (RAG):** การฝังจะช่วยเพิ่มคุณภาพ
  ของข้อความที่สร้างขึ้นโดยการดึงและรวมข้อมูลที่เกี่ยวข้องเข้ากับ
  บริบทของโมเดล
- **การดึงข้อมูล:** ค้นหาข้อความหรือเอกสารที่มีความคล้ายคลึงกันทางความหมายมากที่สุดเมื่อได้รับข้อความนำเข้า

  [บทแนะนำการค้นหาเอกสารtask](https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb)
- **การจัดอันดับผลการค้นหาใหม่**: จัดลำดับความสำคัญของรายการที่เกี่ยวข้องที่สุดโดยใช้การให้คะแนนความหมายของผลลัพธ์เริ่มต้นเทียบกับคำค้นหา

  [บทแนะนำการจัดอันดับใหม่ของการค้นหาtask](https://github.com/google-gemini/cookbook/blob/main/examples/Search_reranking_using_embeddings.ipynb)
- **การตรวจจับความผิดปกติ:** การเปรียบเทียบกลุ่มการฝังจะช่วยระบุ
  แนวโน้มที่ซ่อนอยู่หรือค่าผิดปกติ

  [บทแนะนำการตรวจจับความผิดปกติbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/Anomaly_detection_with_embeddings.ipynb)
- **การจัดประเภท:** จัดหมวดหมู่ข้อความโดยอัตโนมัติตามเนื้อหา เช่น การวิเคราะห์ความเห็นหรือการตรวจจับสแปม

  [บทแนะนำการจัดประเภทtoken](https://github.com/google-gemini/cookbook/blob/main/examples/Classify_text_with_embeddings.ipynb)
- **การจัดกลุ่ม:** ทำความเข้าใจความสัมพันธ์ที่ซับซ้อนได้อย่างมีประสิทธิภาพโดยการสร้างคลัสเตอร์
  และการแสดงภาพการฝัง

  [บทแนะนำการแสดงภาพการจัดกลุ่มbubble\_chart](https://github.com/google-gemini/cookbook/blob/main/examples/clustering_with_embeddings.ipynb)

## การจัดเก็บ Embedding

เมื่อนำการฝังไปใช้ในเวอร์ชันที่ใช้งานจริง คุณมักจะใช้**ฐานข้อมูลเวกเตอร์**เพื่อจัดเก็บ จัดทำดัชนี และดึงข้อมูลการฝังที่มีมิติสูงได้อย่างมีประสิทธิภาพ
Google Cloud มีบริการข้อมูลที่มีการจัดการซึ่ง
ใช้เพื่อวัตถุประสงค์นี้ได้ ซึ่งรวมถึง
[Gemini Enterprise Agent Platform Vector Search 2.0](https://docs.cloud.google.com/gemini-enterprise-agent-platform/BUILD/vector-search-2?hl=th)
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

### การฝัง Gemini 2

| พร็อพเพอร์ตี้ | คำอธิบาย |
| --- | --- |
| รหัสโมเดล id\_card | **Gemini API**  `gemini-embedding-2` |
| บันทึกประเภทข้อมูลที่รองรับ | **อินพุต**  ข้อความ, รูปภาพ, วิดีโอ, เสียง, PDF  **เอาต์พุต**  การฝังข้อความ |
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

พื้นที่ฝังระหว่าง `gemini-embedding-001` กับ
`gemini-embedding-2` **ใช้ร่วมกันไม่ได้** ซึ่งหมายความว่าคุณไม่สามารถเปรียบเทียบการฝังที่โมเดลหนึ่งสร้างขึ้นกับการฝังที่อีกโมเดลหนึ่งสร้างขึ้นได้โดยตรง หากอัปเกรดเป็น `gemini-embedding-2` คุณต้อง
ฝังข้อมูลที่มีอยู่ทั้งหมดอีกครั้ง

นอกเหนือจากความเข้ากันไม่ได้แล้ว ยังมีความแตกต่างที่สำคัญอื่นๆ ระหว่าง
ทั้ง 2 รุ่น ดังนี้

- **ข้อกำหนดประเภทงาน:** ด้วย `gemini-embedding-001` คุณจะระบุ
  ประเภทงานโดยใช้พารามิเตอร์ `task_type` (เช่น `SEMANTIC_SIMILARITY`,
  `RETRIEVAL_DOCUMENT`) ด้วย `gemini-embedding-2` ระบบจะไม่รองรับพารามิเตอร์ `task_type`
  แต่คุณควรระบุวิธีการทำงาน
  ในพรอมต์สำหรับงานที่เป็นข้อความเท่านั้นโดยตรง ดูรายละเอียดเกี่ยวกับวิธีจัดรูปแบบพรอมต์สำหรับกรณีการใช้งานต่างๆ ได้ที่
  [ประเภทงานที่มีการฝัง 2](#task-types-embeddings-2)
- **การรวมการฝัง:** `gemini-embedding-001` สร้างการฝังแต่ละรายการ
  สำหรับแต่ละสตริงในรายการอินพุต ในทางตรงกันข้าม
  `gemini-embedding-2` จะสร้างการฝังแบบรวมรายการเดียวเมื่อมีการระบุอินพุตหลายรายการ (เช่น ข้อความและรูปภาพ) โดยตรงในคำขอเดียว หากต้องการ
  สร้างการฝังแยกกันสำหรับอินพุตแต่ละรายการ ให้ห่ออินพุตแต่ละรายการใน
  `Content` ออบเจ็กต์ หรือใช้
  [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) ดูข้อมูลเพิ่มเติมได้ที่
  [การฝังการรวม](#embedding-aggregation)
- **การปรับให้เป็นมาตรฐาน:** หากใช้ `output_dimensionality` เพื่อขอ Embedding
  ที่มีมิติน้อยกว่า 3072 มิติ `gemini-embedding-2` จะปรับ Embedding ที่ถูกตัดทอนเหล่านี้ให้เป็นมาตรฐานโดยอัตโนมัติ
  เมื่อใช้ `gemini-embedding-001` คุณ
  ต้องทําการปรับมิติข้อมูลอื่นๆ นอกเหนือจาก 3072 ให้เป็นมาตรฐานด้วยตนเอง ดูรายละเอียดได้ที่
  [การรับประกันคุณภาพสำหรับขนาดที่เล็กลง](#quality-for-smaller-dimensions)

## การฝังแบบกลุ่ม

หากไม่กังวลเรื่องเวลาในการตอบสนอง ให้ลองใช้โมเดลการฝัง Gemini กับ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th#batch-embedding) ซึ่งช่วยให้มีอัตราการส่งข้อมูลที่สูงขึ้นมากที่ 50% ของราคาการฝังเริ่มต้น
ดูตัวอย่างวิธีเริ่มต้นใช้งานได้ใน[สูตรการใช้ Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)

## ประกาศเกี่ยวกับการใช้งานอย่างมีความรับผิดชอบ

โมเดลการฝัง Gemini มีไว้เพื่อเปลี่ยนรูปแบบข้อมูลที่คุณป้อนให้เป็นการแสดงตัวเลขเท่านั้น
ซึ่งแตกต่างจากโมเดล Generative AI ที่สร้างเนื้อหาใหม่
แม้ว่า Google จะมีหน้าที่รับผิดชอบในการจัดหาโมเดลการฝัง
ที่แปลงรูปแบบของข้อมูลอินพุตเป็นรูปแบบตัวเลขที่ร้องขอ
แต่ผู้ใช้ยังคงมีหน้าที่รับผิดชอบอย่างเต็มที่ต่อข้อมูลที่ป้อนและการฝังที่ได้
การใช้โมเดล Gemini Embedding เป็นการยืนยันว่าคุณมีสิทธิ์ที่จำเป็นในเนื้อหาใดๆ ที่คุณอัปโหลด อย่าสร้างเนื้อหาที่
ละเมิดสิทธิในทรัพย์สินทางปัญญาหรือสิทธิด้านความเป็นส่วนตัวของผู้อื่น การใช้บริการนี้เป็นไปตาม[นโยบายการใช้งานที่ไม่อนุญาต](https://policies.google.com/terms/generative-ai/use-policy?hl=th)และ[ข้อกำหนดในการให้บริการของ Google](https://ai.google.dev/gemini-api/terms?hl=th)

## เริ่มสร้างด้วยการฝัง

ดู[สมุดบันทึกการเริ่มต้นใช้งานอย่างรวดเร็วของ Embedding](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Embeddings.ipynb)
เพื่อสำรวจความสามารถของโมเดลและดูวิธีปรับแต่งและแสดงภาพ
Embedding

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-06-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-06-19 UTC"],[],[]]
