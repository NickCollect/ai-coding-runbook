---
source_url: https://ai.google.dev/gemini-api/docs/flex-inference?hl=th
fetched_at: 2026-06-15T06:32:48.227100+00:00
title: "\u0e01\u0e32\u0e23\u0e2d\u0e19\u0e38\u0e21\u0e32\u0e19\u0e41\u0e1a\u0e1a\u0e22\u0e37\u0e14\u0e2b\u0e22\u0e38\u0e48\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การอนุมานแบบยืดหยุ่น

Gemini Flex API เป็นระดับการอนุมานที่ช่วยลดต้นทุนได้ 50% เมื่อเทียบกับอัตรามาตรฐาน โดยแลกกับการตอบสนองที่ผันแปรและความพร้อมใช้งาน
ตามความพยายามอย่างเต็มที่ ออกแบบมาสำหรับภาระงานที่ยอมรับเวลาในการตอบสนองได้ซึ่งต้องมีการประมวลผลแบบ
ซิงโครนัส แต่ไม่จำเป็นต้องใช้ประสิทธิภาพแบบเรียลไทม์ของ
API มาตรฐาน

## วิธีใช้ Flex

หากต้องการใช้ระดับ Flex ให้ระบุ `service_tier` เป็น `flex` ใน
เนื้อหาคำขอ โดยค่าเริ่มต้น คำขอจะใช้ระดับมาตรฐานหากละเว้นช่องนี้

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## วิธีการทำงานของการอนุมาน Flex

การอนุมาน Gemini Flex ช่วยลดช่องว่างระหว่าง API มาตรฐานกับเวลาในการตอบกลับ 24 ชั่วโมงของ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) โดยจะใช้ความสามารถในการประมวลผลในช่วงนอกเวลาทําการที่ "ลดได้" เพื่อมอบโซลูชันที่คุ้มค่าสําหรับงานเบื้องหลังและเวิร์กโฟลว์แบบลําดับ

| ฟีเจอร์ | พับ | ลำดับความสำคัญ | มาตรฐาน | กลุ่ม |
| --- | --- | --- | --- | --- |
| **การกำหนดราคา** | ส่วนลด 50% | มากกว่ารุ่น Standard 75-100% | ตั๋วราคาเต็ม | ส่วนลด 50% |
| **เวลาในการตอบสนอง** | นาที (เป้าหมาย 1-15 นาที) | ต่ำ (วินาที) | วินาทีถึงนาที | สูงสุด 24 ชั่วโมง |
| **ความน่าเชื่อถือ** | ดีที่สุดเท่าที่ทำได้ (ลดภาระได้) | สูง (ไม่หลุดร่วง) | สูง / สูงปานกลาง | สูง (สำหรับปริมาณงาน) |
| **อินเทอร์เฟซ** | ซิงโครนัส | ซิงโครนัส | ซิงโครนัส | แบบอะซิงโครนัส |

### ประโยชน์สำคัญ

- **ประสิทธิภาพด้านต้นทุน**: ประหยัดค่าใช้จ่ายได้อย่างมากสำหรับการประเมินที่ไม่ใช่การผลิต, เอเจนต์พื้นหลัง และการเพิ่มคุณค่าของข้อมูล
- **ใช้งานง่าย**: ไม่ต้องจัดการออบเจ็กต์แบบกลุ่ม รหัสงาน หรือการสำรวจ เพียงเพิ่มพารามิเตอร์เดียวลงในคำขอที่มีอยู่
- **เวิร์กโฟลว์แบบซิงโครนัส**: เหมาะสำหรับเชน API แบบลำดับที่คำขอถัดไปขึ้นอยู่กับเอาต์พุตของคำขอก่อนหน้า ซึ่งทำให้มีความยืดหยุ่นมากกว่า Batch สำหรับเวิร์กโฟลว์ของเอเจนต์

### กรณีการใช้งาน

- **การประเมินแบบออฟไลน์**: การเรียกใช้การทดสอบการถดถอยหรือลีดเดอร์บอร์ด "LLM ในฐานะผู้พิพากษา"
- **ตัวแทนเบื้องหลัง**: งานตามลำดับ เช่น การอัปเดต CRM การสร้างโปรไฟล์ หรือการกลั่นกรองเนื้อหาที่ยอมรับความล่าช้าได้
- **การวิจัยที่ถูกจำกัดด้วยงบประมาณ**: การทดลองทางวิชาการที่ต้องใช้โทเค็นจำนวนมากโดยมีงบประมาณจำกัด

### ขีดจำกัดอัตรา

การเข้าชมการอนุมานแบบยืดหยุ่นจะนับรวมใน[ขีดจำกัดอัตรา](https://aistudio.google.com/rate-limit?hl=th)ทั่วไปของคุณ โดยจะไม่มีขีดจำกัดอัตราเพิ่มเติมเหมือนกับ [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th)

### ความจุที่ลดลงได้

ระบบจะถือว่าการเข้าชมแบบยืดหยุ่นมีความสำคัญต่ำกว่า หากมีการเข้าชมมาตรฐานเพิ่มขึ้นอย่างรวดเร็ว ระบบอาจขัดจังหวะหรือนำคำขอ Flex ออกเพื่อให้มั่นใจว่ามีพื้นที่ว่างสำหรับผู้ใช้ที่มีลำดับความสำคัญสูง หากกำลังมองหาการอนุมานที่มีลำดับความสำคัญสูง ให้ดู[การอนุมานที่มีลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)

### รหัสข้อผิดพลาด

เมื่อความจุแบบยืดหยุ่นไม่พร้อมใช้งานหรือระบบมีปริมาณการใช้งานสูง API จะ
แสดงรหัสข้อผิดพลาดมาตรฐาน

- **503 ไม่พร้อมให้บริการ**: ขณะนี้ระบบมีผู้ใช้เต็มแล้ว
- **429 มีคำขอมากเกินไป**: ขีดจำกัดอัตราหรือทรัพยากรหมด

### ความรับผิดชอบของลูกค้า

- **ไม่มีการสำรองข้อมูลฝั่งเซิร์ฟเวอร์**: เพื่อป้องกันการเรียกเก็บเงินที่ไม่คาดคิด ระบบจะไม่
  อัปเกรดคำขอ Flex เป็นระดับมาตรฐานโดยอัตโนมัติหากความจุของ Flex เต็ม
- **การลองใหม่**: คุณต้องใช้ตรรกะการลองใหม่ฝั่งไคลเอ็นต์ของคุณเองด้วย
  Exponential Backoff
- **การหมดเวลา**: เนื่องจากคำขอ Flex อาจอยู่ในคิว เราจึงแนะนำให้
  เพิ่มการหมดเวลาฝั่งไคลเอ็นต์เป็น 10 นาทีขึ้นไปเพื่อหลีกเลี่ยงการปิด
  การเชื่อมต่อก่อนเวลา

## ปรับกรอบเวลาหมดเวลา

คุณสามารถกำหนดค่าการหมดเวลาต่อคำขอสำหรับ REST API และไลบรารีของไคลเอ็นต์
และการหมดเวลาส่วนกลางได้เมื่อใช้ไลบรารีของไคลเอ็นต์เท่านั้น

ตรวจสอบเสมอว่าการหมดเวลาฝั่งไคลเอ็นต์ครอบคลุมช่วงเวลาที่เซิร์ฟเวอร์ตั้งใจรอ (เช่น 600 วินาทีขึ้นไปสำหรับคิวรอแบบยืดหยุ่น) SDK คาดหวังค่าการหมดเวลาเป็นมิลลิวินาที

### การหมดเวลาต่อคำขอ

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.5-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.5-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.5-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.5-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

เมื่อทำการเรียก REST คุณจะควบคุมการหมดเวลาได้โดยใช้ส่วนหัว HTTP
และ`curl` ตัวเลือกต่อไปนี้ร่วมกัน

- ส่วนหัว **`X-Server-Timeout` (การหมดเวลาฝั่งเซิร์ฟเวอร์)**: ส่วนหัวนี้แนะนำระยะเวลาการหมดเวลาที่ต้องการ (ค่าเริ่มต้นคือ 600 วินาที) ให้กับเซิร์ฟเวอร์ Gemini API เซิร์ฟเวอร์ จะพยายามปฏิบัติตามคำขอนี้ แต่ก็ไม่รับประกันว่าจะทำได้ ค่าควรเป็นวินาที
- **`--max-time` ใน `curl` (การหมดเวลาฝั่งไคลเอ็นต์)**: ตัวเลือก `curl --max-time
  <seconds>` จะกำหนดขีดจำกัดที่แน่นอนสำหรับเวลาทั้งหมด (เป็นวินาที) ที่ `curl`
  จะรอให้การดำเนินการทั้งหมดเสร็จสมบูรณ์ นี่คือการป้องกันฝั่งไคลเอ็นต์

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### การหมดเวลาทั่วโลก

หากต้องการให้การเรียก API ทั้งหมดที่ทำผ่านอินสแตนซ์ `genai.Client` ที่เฉพาะเจาะจง
(เฉพาะไลบรารีของไคลเอ็นต์) มีการหมดเวลาเริ่มต้น คุณสามารถกำหนดค่านี้ได้เมื่อ
เริ่มต้นไคลเอ็นต์โดยใช้ `http_options` และ `genai.types.HttpOptions`

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.5-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## ใช้การลองใหม่

เนื่องจาก Flex สามารถลดขนาดได้และจะล้มเหลวพร้อมข้อผิดพลาด 503 ต่อไปนี้คือตัวอย่างการใช้ตรรกะการลองใหม่โดยไม่บังคับเพื่อดำเนินการต่อกับคำขอที่ไม่สำเร็จ

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.5-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.5-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.5-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.5-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## ราคา

การอนุมานแบบยืดหยุ่นมีราคาอยู่ที่ 50% ของ [API มาตรฐาน](https://ai.google.dev/gemini-api/docs/pricing?hl=th)
และเรียกเก็บเงินต่อโทเค็น

## โมเดลที่รองรับ

รุ่นต่อไปนี้รองรับการอนุมานแบบยืดหยุ่น

| รุ่น | การอนุมานแบบยืดหยุ่น |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=th) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=th) | ✔️ |
| [ตัวอย่าง Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=th) | ✔️ |
| [ตัวอย่างรูปภาพ Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=th) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=th) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=th) | ✔️ |
| [รูปภาพ Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=th) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=th) | ✔️ |

## ขั้นตอนถัดไป

อ่านเกี่ยวกับตัวเลือก[การอนุมานและการเพิ่มประสิทธิภาพ](https://ai.google.dev/gemini-api/docs/optimization?hl=th)อื่นๆ ของ Gemini

- [การอนุมานลำดับความสำคัญ](https://ai.google.dev/gemini-api/docs/priority-inference?hl=th)สำหรับเวลาในการตอบสนองต่ำมาก
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=th) สำหรับการประมวลผลแบบไม่พร้อมกันภายใน 24 ชั่วโมง
- [การแคชบริบท](https://ai.google.dev/gemini-api/docs/caching?hl=th)เพื่อลดต้นทุนโทเค็นอินพุต

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-28 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-28 UTC"],[],[]]
