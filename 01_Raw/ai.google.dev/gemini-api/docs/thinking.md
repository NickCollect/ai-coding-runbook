---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=th
fetched_at: 2026-05-05T13:15:03.390758+00:00
title: "\u0e01\u0e33\u0e25\u0e31\u0e07\u0e04\u0e34\u0e14 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

- [หน้าแรก](https://ai.google.dev/gemini-api/docs/หน้าแรก)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [เอกสาร](https://ai.google.dev/gemini-api/docs/เอกสาร)

ส่งความคิดเห็น

# กำลังคิด

โมเดล [Gemini 3 และ 2.5 Series](https://ai.google.dev/gemini-api/docs/Gemini 3 และ 2.5 Series) ใช้
"กระบวนการคิด" ภายในที่ช่วยปรับปรุงความสามารถในการให้เหตุผลและการวางแผนหลายขั้นตอนได้อย่างมาก ทำให้โมเดลมีประสิทธิภาพสูงสำหรับงานที่ซับซ้อน เช่น
การเขียนโค้ด คณิตศาสตร์ขั้นสูง และการวิเคราะห์ข้อมูล

คู่มือนี้จะแสดงวิธีใช้ความสามารถด้านการคิดของ Gemini โดยใช้ Gemini API

## การสร้างเนื้อหาด้วยการคิด

การเริ่มคำขอด้วยโมเดลการคิดจะคล้ายกับการเริ่มคำขอสร้างเนื้อหาอื่นๆ [[ความแตกต่างที่สำคัญคือการระบุโมเดลที่รองรับการคิดในช่อง `model` ดังที่แสดงในตัวอย่างการสร้างข้อความต่อไปนี้](https://ai.google.dev/gemini-api/docs/[ความแตกต่างที่สำคัญคือการระบุโมเดลที่รองรับการคิดในช่อง `model` ดังที่แสดงในตัวอย่างการสร้างข้อความต่อไปนี้)](https://ai.google.dev/gemini-api/docs/text-generation?hl=th#text-input)

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });

  console.log(response.text);
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
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3-flash-preview"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## ข้อมูลสรุปความคิด

ข้อมูลสรุปความคิดคือเวอร์ชันสรุปของความคิดดิบของโมเดล และให้ข้อมูลเชิงลึกเกี่ยวกับกระบวนการให้เหตุผลภายในของโมเดล โปรดทราบว่าระดับการคิดและงบประมาณมีผลกับความคิดดิบของโมเดล ไม่ใช่ข้อมูลสรุปความคิด

คุณเปิดใช้ข้อมูลสรุปความคิดได้โดยตั้งค่า `includeThoughts` เป็น `true` ในการกำหนดค่าคำขอ จากนั้นคุณจะเข้าถึงข้อมูลสรุปได้โดยการวนซ้ำ `parts` ของพารามิเตอร์ `response` และตรวจสอบบูลีน `thought`

ตัวอย่างต่อไปนี้แสดงวิธีเปิดใช้และดึงข้อมูลสรุปความคิดโดยไม่ใช้การสตรีม ซึ่งจะแสดงข้อมูลสรุปความคิดสุดท้ายรายการเดียวพร้อมคำตอบ

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
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
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

และนี่คือตัวอย่างการใช้การคิดกับการสตรีม ซึ่งจะแสดงข้อมูลสรุปแบบเพิ่มทีละน้อยระหว่างการสร้าง

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3-flash-preview",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
  }
}

await main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3-flash-preview"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## การควบคุมการคิด

โมเดล Gemini จะคิดแบบไดนามิกโดยค่าเริ่มต้น ซึ่งจะปรับความพยายามในการให้เหตุผลโดยอัตโนมัติตามความซับซ้อนของคำขอของผู้ใช้
อย่างไรก็ตาม หากคุณมีข้อจำกัดด้านเวลาในการตอบสนองที่เฉพาะเจาะจงหรือต้องการให้โมเดลให้เหตุผลที่ลึกซึ้งกว่าปกติ คุณสามารถใช้พารามิเตอร์เพื่อควบคุมลักษณะการทำงานของการคิดได้

### ระดับการคิด (Gemini 3)

พารามิเตอร์ `thinkingLevel` ซึ่งแนะนำให้ใช้กับโมเดล Gemini 3 ขึ้นไป ช่วยให้คุณควบคุมลักษณะการทำงานของการให้เหตุผลได้

ตารางต่อไปนี้แสดงรายละเอียดการตั้งค่า `thinkingLevel` สำหรับโมเดลแต่ละประเภท

| ระดับการคิด | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | คำอธิบาย |
| --- | --- | --- | --- | --- |
| **`minimal`** | ไม่รองรับ | สิ่งที่ทำได้ (ค่าเริ่มต้น) | สิ่งที่ทำได้ | ตรงกับการตั้งค่า "ไม่คิด" สำหรับคำค้นหาส่วนใหญ่ โมเดลอาจคิดน้อยมากสำหรับงานเขียนโค้ดที่ซับซ้อน ลดเวลาในการตอบสนองสำหรับแอปพลิเคชันแชทหรือแอปพลิเคชันที่มีการส่งข้อความปริมาณมาก โปรดทราบว่า `minimal` ไม่ได้รับประกันว่าจะปิดการคิด |
| **`low`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | ลดเวลาในการตอบสนองและค่าใช้จ่าย เหมาะที่สุดสำหรับการทำตามคำแนะนำง่ายๆ การแชท หรือแอปพลิเคชันที่มีปริมาณงานสูง |
| **`medium`** | สิ่งที่ทำได้ | สิ่งที่ทำได้ | สิ่งที่ทำได้ | การคิดที่สมดุลสำหรับงานส่วนใหญ่ |
| **`high`** | สิ่งที่ทำได้ (ค่าเริ่มต้น, ไดนามิก) | สิ่งที่ทำได้ (ไดนามิก) | สิ่งที่ทำได้ (ค่าเริ่มต้น, ไดนามิก) | เพิ่มความลึกในการให้เหตุผลให้สูงสุด โมเดลอาจใช้เวลานานขึ้นอย่างมากในการ แสดงโทเค็นเอาต์พุตแรก (ที่ไม่ใช่การคิด) แต่เอาต์พุตจะได้รับการพิจารณาอย่างรอบคอบมากขึ้น |

ตัวอย่างต่อไปนี้แสดงวิธีตั้งค่าระดับการคิด

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3-flash-preview"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

คุณปิดใช้การคิดสำหรับ Gemini 3.1 Pro ไม่ได้ นอกจากนี้ Gemini 3 Flash และ Flash-Lite ยังไม่รองรับการปิดการคิดอย่างสมบูรณ์ แต่การตั้งค่า `minimal` หมายความว่าโมเดลอาจไม่คิด (แม้ว่ายังคงมีความเป็นไปได้ที่จะคิด)
หากคุณไม่ได้ระบุระดับการคิด Gemini จะใช้ระดับการคิดแบบไดนามิกเริ่มต้นของโมเดล Gemini 3
`"high"`

โมเดล Gemini 2.5 Series ไม่รองรับ `thinkingLevel` ให้ใช้ `thinkingBudget` แทน

### งบประมาณการคิด

พารามิเตอร์ `thinkingBudget` ซึ่งเปิดตัวพร้อมกับ Gemini 2.5 Series จะแนะนำโมเดลเกี่ยวกับจำนวนโทเค็นการคิดที่เฉพาะเจาะจงที่จะใช้ในการให้เหตุผล

รายละเอียดการกำหนดค่า `thinkingBudget` สำหรับโมเดลแต่ละประเภทมีดังนี้
คุณปิดใช้การคิดได้โดยตั้งค่า `thinkingBudget` เป็น 0
การตั้งค่า `thinkingBudget` เป็น -1 จะเปิด
**การคิดแบบไดนามิก** ซึ่งหมายความว่าโมเดลจะปรับงบประมาณตาม
ความซับซ้อนของคำขอ

| โมเดล | การตั้งค่าเริ่มต้น (ไม่ได้ตั้งค่า งบประมาณการคิด) | ช่วง | ปิดใช้การคิด | เปิดใช้การคิดแบบไดนามิก |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | การคิดแบบไดนามิก | `128` ถึง `32768` | ไม่มี: ปิดใช้การคิดไม่ได้ | `thinkingBudget = -1` (ค่าเริ่มต้น) |
| **2.5 Flash** | การคิดแบบไดนามิก | `0` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (ค่าเริ่มต้น) |
| **2.5 Flash เวอร์ชันตัวอย่าง** | การคิดแบบไดนามิก | `0` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (ค่าเริ่มต้น) |
| **2.5 Flash Lite** | โมเดลไม่คิด | `512` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite เวอร์ชันตัวอย่าง** | โมเดลไม่คิด | `512` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 เวอร์ชันตัวอย่าง** | การคิดแบบไดนามิก | `0` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (ค่าเริ่มต้น) |
| **2.5 Flash Live Native Audio เวอร์ชันตัวอย่าง (09-2025)** | การคิดแบบไดนามิก | `0` ถึง `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (ค่าเริ่มต้น) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### Go

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

โมเดลอาจใช้โทเค็นเกินงบประมาณหรือใช้โทเค็นน้อยกว่างบประมาณ ทั้งนี้ขึ้นอยู่กับพรอมต์

## ลายเซ็นความคิด

Gemini API เป็นแบบไม่เก็บสถานะ ดังนั้นโมเดลจะถือว่าคำขอ API แต่ละรายการเป็นอิสระและไม่มีสิทธิ์เข้าถึงบริบทความคิดจากรอบก่อนหน้าในการโต้ตอบหลายรอบ

Gemini จะแสดงลายเซ็นความคิด ซึ่งเป็นการแสดงกระบวนการคิดภายในของโมเดลที่เข้ารหัสไว้ เพื่อให้สามารถรักษาบริบทความคิดในการโต้ตอบหลายรอบ

- **โมเดล Gemini 2.5** จะแสดงลายเซ็นความคิดเมื่อเปิดใช้การคิดและ
  คำขอมีการเรียกใช้[ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/ฟังก์ชัน) โดยเฉพาะ[การประกาศฟังก์ชัน](https://ai.google.dev/gemini-api/docs/การประกาศฟังก์ชัน)
- **โมเดล Gemini 3** อาจแสดงลายเซ็นความคิดสำหรับ [ชิ้นส่วน](https://ai.google.dev/gemini-api/docs/ชิ้นส่วน) ทุกประเภท
  เราขอแนะนำให้ส่งลายเซ็นทั้งหมดกลับตามที่ได้รับเสมอ แต่การส่งลายเซ็นการเรียกใช้ฟังก์ชันกลับเป็นสิ่งที่ *จำเป็น* อ่านข้อมูลเพิ่มเติมได้ในหน้า
  [ลายเซ็นความคิด](https://ai.google.dev/gemini-api/docs/ลายเซ็นความคิด)

ข้อจำกัดในการใช้งานอื่นๆ ที่ควรพิจารณาเกี่ยวกับการเรียกใช้ฟังก์ชันมีดังนี้

- ระบบจะแสดงลายเซ็นจากโมเดลภายในชิ้นส่วนอื่นๆ ในคำตอบ เช่น ชิ้นส่วนการเรียกใช้ฟังก์ชันหรือชิ้นส่วนข้อความ
  [ส่งคำตอบทั้งหมด](https://ai.google.dev/gemini-api/docs/ส่งคำตอบทั้งหมด)
  พร้อมชิ้นส่วนทั้งหมดกลับไปยังโมเดลในรอบถัดไป
- อย่าเชื่อมชิ้นส่วนที่มีลายเซ็นเข้าด้วยกัน
- อย่าผสานชิ้นส่วนหนึ่งที่มีลายเซ็นกับอีกชิ้นส่วนหนึ่งที่ไม่มีลายเซ็น

## ราคา

เมื่อเปิดใช้การคิด ราคาคำตอบจะเป็นผลรวมของโทเค็นเอาต์พุตและโทเค็นการคิด คุณดูจำนวนโทเค็นการคิดทั้งหมดที่สร้างขึ้นได้จากช่อง `thoughtsTokenCount`

### Python

```
# ...
print("Thoughts tokens:",response.usage_metadata.thoughts_token_count)
print("Output tokens:",response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### Go

```
// ...
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println("Thoughts tokens:", string(usageMetadata.thoughts_token_count))
fmt.Println("Output tokens:", string(usageMetadata.candidates_token_count))
```

โมเดลการคิดจะสร้างความคิดทั้งหมดเพื่อปรับปรุงคุณภาพของคำตอบสุดท้าย
จากนั้นจะแสดงข้อมูลสรุปเพื่อแสดงข้อมูลเชิงลึกเกี่ยวกับกระบวนการคิด
ดังนั้น ราคาจึงอิงตามโทเค็นความคิดทั้งหมดที่โมเดลต้องสร้างขึ้นเพื่อสร้างข้อมูลสรุป แม้ว่า API จะแสดงเฉพาะข้อมูลสรุปก็ตาม

ดูข้อมูลเพิ่มเติมเกี่ยวกับโทเค็นได้ใน[คู่มือการนับโทเค็น](https://ai.google.dev/gemini-api/docs/คู่มือการนับโทเค็น)

## แนวทางปฏิบัติแนะนำ

ส่วนนี้มีคำแนะนำบางอย่างสำหรับการใช้โมเดลการคิดอย่างมีประสิทธิภาพ
เช่นเคย การทำตาม[คำแนะนำในการเขียนพรอมต์และแนวทางปฏิบัติแนะนำ](https://ai.google.dev/gemini-api/docs/คำแนะนำในการเขียนพรอมต์และแนวทางปฏิบัติแนะนำ)จะช่วยให้คุณได้ผลลัพธ์ที่ดีที่สุด

### การแก้ไขข้อบกพร่องและการควบคุม

- **ตรวจสอบการให้เหตุผล**: เมื่อคุณไม่ได้รับคำตอบที่คาดหวังจาก
  โมเดลการคิด การวิเคราะห์ข้อมูลสรุปความคิดของ Gemini อย่างละเอียดอาจช่วยได้
  คุณจะเห็นวิธีที่โมเดลแบ่งงานและได้ข้อสรุป และใช้ข้อมูลดังกล่าวเพื่อแก้ไขให้ได้ผลลัพธ์ที่ถูกต้อง
- **ให้คำแนะนำในการให้เหตุผล**: หากต้องการเอาต์พุตที่ยาวเป็นพิเศษ คุณอาจต้องให้คำแนะนำในพรอมต์เพื่อจำกัด[จำนวนการคิด](https://ai.google.dev/gemini-api/docs/จำนวนการคิด)ที่โมเดลใช้ ซึ่งจะช่วยให้คุณสงวนโทเค็นเอาต์พุตไว้สำหรับคำตอบได้มากขึ้น

### ความซับซ้อนของงาน

- **งานง่าย (อาจปิดการคิดได้):** สำหรับคำขอตรงไปตรงมาที่ไม่จำเป็นต้องมีการให้เหตุผลที่ซับซ้อน เช่น การดึงข้อมูลข้อเท็จจริงหรือการจัดประเภท ไม่จำเป็นต้องมีการคิด ตัวอย่างเช่น
  - "DeepMind ก่อตั้งขึ้นที่ไหน"
  - "อีเมลนี้ขอให้มีการประชุมหรือเพียงแค่ให้ข้อมูล"
- **งานปานกลาง (ค่าเริ่มต้น/การคิดบางส่วน):** คำขอทั่วไปหลายรายการได้รับประโยชน์จากการประมวลผลแบบทีละขั้นตอนหรือความเข้าใจที่ลึกซึ้งยิ่งขึ้น Gemini สามารถใช้ความสามารถด้านการคิดได้อย่างยืดหยุ่นสำหรับงานต่างๆ เช่น
  - เปรียบเทียบการสังเคราะห์แสงกับการเติบโต
  - เปรียบเทียบความเหมือนและความแตกต่างของรถยนต์ไฟฟ้าและรถยนต์ไฮบริด
- **งานยาก (ความสามารถด้านการคิดสูงสุด):** สำหรับความท้าทายที่ซับซ้อนอย่างแท้จริง เช่น การแก้ปัญหาคณิตศาสตร์ที่ซับซ้อนหรืองานเขียนโค้ด เราขอแนะนำให้ตั้งงบประมาณการคิดไว้สูง งานประเภทนี้กำหนดให้โมเดลต้องใช้ความสามารถด้านการให้เหตุผลและการวางแผนอย่างเต็มที่ ซึ่งมักเกี่ยวข้องกับขั้นตอนภายในหลายขั้นตอนก่อนที่จะให้คำตอบ ตัวอย่างเช่น
  - แก้ปัญหาข้อที่ 1 ใน AIME 2025: หาผลรวมของฐานจำนวนเต็มทั้งหมด b > 9 สำหรับ
    ซึ่ง 17b เป็นตัวหารของ 97b
  - เขียนโค้ด Python สำหรับเว็บแอปพลิเคชันที่แสดงข้อมูลตลาดหุ้นแบบเรียลไทม์ รวมถึงการตรวจสอบสิทธิ์ของผู้ใช้ ทำให้มีประสิทธิภาพมากที่สุด

## โมเดล เครื่องมือ และความสามารถที่รองรับ

ฟีเจอร์การคิดรองรับในโมเดล 3 และ 2.5 Series ทั้งหมด
คุณดูความสามารถทั้งหมดของโมเดลได้ในหน้า
[ภาพรวมของโมเดล](https://ai.google.dev/gemini-api/docs/ภาพรวมของโมเดล)

โมเดลการคิดทำงานร่วมกับเครื่องมือและความสามารถทั้งหมดของ Gemini ซึ่งช่วยให้โมเดลโต้ตอบกับระบบภายนอก ดำเนินการโค้ด หรือเข้าถึงข้อมูลแบบเรียลไทม์ โดยรวมผลลัพธ์ไว้ในการให้เหตุผลและคำตอบสุดท้าย

คุณลองดูตัวอย่างการใช้เครื่องมือกับโมเดลการคิดได้ใน
[คู่มือการคิด](https://ai.google.dev/gemini-api/docs/คู่มือการคิด)

## ขั้นตอนต่อไปคืออะไร

- ความครอบคลุมของการคิดมีอยู่ในคู่มือ[ความเข้ากันได้กับ OpenAI](https://ai.google.dev/gemini-api/docs/ความเข้ากันได้กับ OpenAI)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://ai.google.dev/gemini-api/docs/ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://ai.google.dev/gemini-api/docs/ใบอนุญาต Apache 2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://ai.google.dev/gemini-api/docs/นโยบายเว็บไซต์ Google Developers) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม
