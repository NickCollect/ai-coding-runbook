---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=th
fetched_at: 2026-05-05T20:47:17.329115+00:00
title: "\u0e23\u0e27\u0e21\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e21\u0e37\u0e2d\u0e43\u0e19\u0e15\u0e31\u0e27\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e1f\u0e31\u0e07\u0e01\u0e4c\u0e0a\u0e31\u0e19 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# รวมเครื่องมือในตัวและการเรียกใช้ฟังก์ชัน

Gemini ช่วยให้คุณสามารถรวม[เครื่องมือในตัว](https://ai.google.dev/gemini-api/docs/tools?hl=th) เช่น `google_search` และ[การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
(หรือที่เรียกว่า*เครื่องมือที่กำหนดเอง*) ไว้ในการสร้างครั้งเดียวได้โดยการเก็บรักษาและแสดงประวัติบริบทของการเรียกใช้เครื่องมือ การผสมผสานเครื่องมือในตัวและเครื่องมือที่กำหนดเองช่วยให้
เวิร์กโฟลว์ที่ซับซ้อนและมีเอเจนต์ทำงานได้ เช่น โมเดลสามารถอ้างอิง
ข้อมูลเว็บแบบเรียลไทม์ก่อนที่จะเรียกตรรกะทางธุรกิจที่เฉพาะเจาะจงของคุณ

ตัวอย่างที่เปิดใช้การผสมผสานเครื่องมือในตัวและเครื่องมือที่กำหนดเองด้วย
`google_search` และฟังก์ชันที่กำหนดเอง `getWeather` มีดังนี้

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

for part in response.candidates[0].content.parts:
    if part.tool_call:
        print(f"Tool call: {part.tool_call.tool_type} (ID: {part.tool_call.id})")
    if part.tool_response:
        print(f"Tool response: {part.tool_response.tool_type} (ID: {part.tool_response.id})")
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      # This flag needs to be enabled for built-in tool context circulation and tool combination
      include_server_side_tool_invocations=True
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.toolCall) {
            console.log(`Tool call: ${part.toolCall.toolType} (ID: ${part.toolCall.id})`);
        }
        if (part.toolResponse) {
            console.log(`Tool response: ${part.toolResponse.toolType} (ID: ${part.toolResponse.id})`);
        }
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3-flash-preview")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        case genai.ToolCallPart:
            fmt.Printf("Tool call: %s (ID: %s)\n", p.ToolType, p.ID)
        case genai.ToolResponsePart:
            fmt.Printf("Tool response: %s (ID: %s)\n", p.ToolType, p.ID)
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## วิธีการทำงาน

โมเดล Gemini 3 ใช้*การหมุนเวียนบริบทของเครื่องมือ*เพื่อเปิดใช้ชุดค่าผสมของเครื่องมือในตัวและเครื่องมือที่กำหนดเอง
การหมุนเวียนบริบทของเครื่องมือช่วยให้สามารถรักษาและแสดงบริบทของเครื่องมือในตัว รวมถึงแชร์กับเครื่องมือที่กำหนดเองในการเรียกใช้เดียวกันได้ตั้งแต่ต้นจนจบ

### เปิดใช้การรวมเครื่องมือ

- คุณต้องตั้งค่าแฟล็ก `include_server_side_tool_invocations` เป็น `true` เพื่อ
  เปิดใช้การหมุนเวียนบริบทของเครื่องมือ
- ใส่ [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=th#function-declarations) พร้อมกับเครื่องมือในตัวที่ต้องการใช้เพื่อเรียกใช้ลักษณะการทำงานร่วมกัน
  - หากคุณไม่รวม `function_declarations` การหมุนเวียนบริบทของเครื่องมือ
    จะยังคงทำงานกับเครื่องมือในตัวที่รวมไว้ ตราบใดที่ตั้งค่าสถานะไว้

### API แสดงผลชิ้นส่วน

ในคำตอบเดียว API จะแสดงผลส่วน `toolCall` และ `toolResponse`
สำหรับการเรียกเครื่องมือในตัว สำหรับการเรียกฟังก์ชัน (เครื่องมือที่กำหนดเอง) API จะ
แสดงส่วนการเรียก `functionCall` ซึ่งผู้ใช้จะระบุส่วน `functionResponse` ในรอบถัดไป

- `toolCall` และ `toolResponse`: API จะแสดงส่วนเหล่านี้เพื่อรักษาบริบทของเครื่องมือที่เรียกใช้ในฝั่งเซิร์ฟเวอร์ และผลลัพธ์ของการดำเนินการสำหรับรอบถัดไป
- `functionCall` และ `functionResponse`: API จะส่งการเรียกใช้ฟังก์ชันให้ผู้ใช้กรอกข้อมูล และผู้ใช้จะส่งผลลัพธ์กลับมาในการตอบกลับฟังก์ชัน (ส่วนเหล่านี้เป็นมาตรฐานสำหรับการ[เรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ทั้งหมดใน Gemini API ไม่ได้มีเฉพาะฟีเจอร์การรวมเครื่องมือ)
- (เครื่องมือ[การเรียกใช้โค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th)เท่านั้น)
  `executableCode` และ `codeExecutionResult`:
  เมื่อใช้เครื่องมือการเรียกใช้โค้ด แทนที่จะเป็น `functionCall` และ
  `functionResponse` API จะแสดง `executableCode` (โค้ดที่โมเดลสร้างขึ้น
  ซึ่งมีไว้สำหรับการเรียกใช้) และ `codeExecutionResult` (ผลลัพธ์ของโค้ดที่เรียกใช้ได้)

คุณต้องส่งคืนชิ้นส่วนทั้งหมด รวมถึง[ฟิลด์](#critical-fields)ทั้งหมดที่ชิ้นส่วนเหล่านั้นมี กลับไปยังโมเดลในแต่ละรอบเพื่อรักษาบริบทและเปิดใช้การรวมเครื่องมือ

### ฟิลด์ที่สำคัญในชิ้นส่วนที่ส่งคืน

[ชิ้นส่วนบางอย่างที่ API แสดงผล](#api-returns-parts)จะมีฟิลด์ `id`,
`tool_type` และ `thought_signature` ฟิลด์เหล่านี้มีความสําคัญต่อ
การรักษาบริบทของเครื่องมือ (และด้วยเหตุนี้จึงมีความสําคัญต่อการรวมเครื่องมือ) คุณต้อง
ส่งคืนชิ้นส่วนทั้งหมด*ตามที่ระบุไว้ในการตอบกลับ*ในคําขอที่ตามมา

- `id`: ตัวระบุที่ไม่ซ้ำกันซึ่งแมปการเรียกไปยังการตอบกลับ `id` จะ**ตั้งค่าเป็น
  การตอบกลับการเรียกใช้ฟังก์ชันทั้งหมด** ไม่ว่าบริบทของเครื่องมือจะหมุนเวียนหรือไม่ก็ตาม
  คุณ*ต้อง*ระบุ `id` เดียวกันในการตอบกลับของฟังก์ชัน ที่ API ระบุในการเรียกใช้ฟังก์ชัน เครื่องมือในตัวจะแชร์ `id` ระหว่างการเรียกใช้เครื่องมือและการตอบกลับเครื่องมือโดยอัตโนมัติ
  - พบในส่วนที่เกี่ยวข้องกับเครื่องมือทั้งหมด: `toolCall`, `toolResponse`,
    `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: ระบุเครื่องมือที่ใช้โดยเฉพาะ เครื่องมือในตัวที่แท้จริง
  หรือ (เช่น `URL_CONTEXT`) หรือชื่อฟังก์ชัน (เช่น `getWeather`)
  - พบในส่วน `toolCall` และ `toolResponse`
- `thought_signature`: บริบทที่เข้ารหัสจริงซึ่งฝังอยู่ใน**แต่ละ
  ส่วนที่ API แสดงผล** ระบบจะสร้างบริบทขึ้นใหม่ไม่ได้หากไม่มีลายเซ็นความคิด หากคุณไม่ส่งคืนลายเซ็นความคิดสำหรับทุกส่วนในทุกๆ เทิร์น โมเดลจะแสดงข้อผิดพลาด
  - พบได้ใน*ทุก*ส่วน

### ข้อมูลเฉพาะของเครื่องมือ

เครื่องมือในตัวบางอย่างจะแสดงอาร์กิวเมนต์ข้อมูลที่ผู้ใช้มองเห็นได้ซึ่งเจาะจงสำหรับประเภทเครื่องมือ

| เครื่องมือ | อาร์กิวเมนต์การเรียกใช้เครื่องมือที่ผู้ใช้มองเห็น (หากมี) | การตอบกลับของเครื่องมือที่ผู้ใช้มองเห็น (หากมี) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL ที่จะเรียกดู | `urls_metadata` `retrieved_url`: URL ที่เข้าชม `url_retrieval_status`: สถานะการเรียกดู |
| **FILE\_SEARCH** | ไม่มี | ไม่มี |

## ตัวอย่างโครงสร้างคำขอรวมเครื่องมือ

โครงสร้างคำขอต่อไปนี้แสดงโครงสร้างคำขอของพรอมต์ "เมืองที่อยู่เหนือสุดในสหรัฐอเมริกาคือเมืองอะไร
วันนี้อากาศที่นั่นเป็นยังไงบ้าง" โดยจะรวมเครื่องมือ 3 อย่าง ได้แก่ เครื่องมือ Gemini ในตัว `google_search`
และ `code_execution` รวมถึงฟังก์ชันที่กำหนดเอง `get_weather`

```
{
  "model": "models/gemini-3-flash-preview",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## โทเค็นและการกำหนดราคา

โปรดทราบว่าส่วน `toolCall` และ `toolResponse` ในคำขอจะนับรวมใน `prompt_token_count` เนื่องจากตอนนี้คุณสามารถเห็นขั้นตอนเครื่องมือระดับกลางเหล่านี้และระบบจะส่งคืนให้คุณ ขั้นตอนเหล่านี้จึงเป็นส่วนหนึ่งของประวัติการสนทนา ซึ่งจะเกิดขึ้นกับ*คำขอ*เท่านั้น ไม่ใช่*คำตอบ*

เครื่องมือ Google Search เป็นข้อยกเว้นของกฎนี้ Google Search ใช้โมเดลการกำหนดราคาของตัวเองที่ระดับคำค้นหาอยู่แล้ว จึงไม่มีการเรียกเก็บเงินจากโทเค็นซ้ำ (ดูหน้า[การกำหนดราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th))

อ่านข้อมูลเพิ่มเติมได้ที่หน้า[โทเค็น](https://ai.google.dev/gemini-api/docs/tokens?hl=th)

## ข้อจำกัด

- ค่าเริ่มต้นจะเป็นโหมด `VALIDATED` (ไม่รองรับโหมด `AUTO`) เมื่อเปิดใช้ฟีเจอร์ `include_server_side_tool_invocations`
- เครื่องมือในตัว เช่น `google_search` อาศัยข้อมูลตำแหน่งและเวลาปัจจุบัน ดังนั้นหาก `system_instruction` หรือ `function_declaration.description` มีข้อมูลตำแหน่งและเวลา ที่ขัดแย้งกัน ฟีเจอร์การรวมเครื่องมืออาจทำงานได้ไม่ดี

## เครื่องมือที่รองรับ

การหมุนเวียนบริบทของเครื่องมือมาตรฐานจะใช้กับเครื่องมือฝั่งเซิร์ฟเวอร์ (ในตัว)
การดำเนินการโค้ดเป็นเครื่องมือฝั่งเซิร์ฟเวอร์เช่นกัน แต่มีโซลูชันในตัวของตัวเองสำหรับ
การหมุนเวียนบริบท การใช้คอมพิวเตอร์และการเรียกใช้ฟังก์ชันเป็นเครื่องมือฝั่งไคลเอ็นต์
และยังมีโซลูชันในตัวสำหรับการหมุนเวียนบริบทด้วย

| เครื่องมือ | ฝั่งที่ดำเนินการ | การสนับสนุนการหมุนเวียนบริบท |
| --- | --- | --- |
| [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ |
| [การรันโค้ด](https://ai.google.dev/gemini-api/docs/code-execution?hl=th) | ฝั่งเซิร์ฟเวอร์ | รองรับ (ติดตั้งในตัว ใช้ชิ้นส่วน `executableCode` และ `codeExecutionResult`) |
| [การใช้คอมพิวเตอร์](https://ai.google.dev/gemini-api/docs/computer-use?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ติดตั้งในตัว ใช้ชิ้นส่วน `functionCall` และ `functionResponse`) |
| [ฟังก์ชันที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/function-calling?hl=th) | ฝั่งไคลเอ็นต์ | รองรับ (ติดตั้งในตัว ใช้ชิ้นส่วน `functionCall` และ `functionResponse`) |

## ขั้นตอนถัดไป

- ดูข้อมูลเพิ่มเติมเกี่ยวกับ[การเรียกฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)ใน Gemini API
- สำรวจเครื่องมือที่รองรับ
  - [Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=th)
  - [บริบท URL](https://ai.google.dev/gemini-api/docs/url-context?hl=th)
  - [การค้นหาไฟล์](https://ai.google.dev/gemini-api/docs/file-search?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-04-29 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-04-29 UTC"],[],[]]
