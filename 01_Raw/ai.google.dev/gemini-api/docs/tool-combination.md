---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar
fetched_at: 2026-06-15T06:30:48.181385+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الجمع بين الأدوات المضمّنة وميزة "استدعاء الدوال"

يسمح Gemini بالجمع بين [الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)، مثل `google_search`، وميزة [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) (المعروفة أيضًا باسم *الأدوات المخصّصة*) في عملية إنشاء واحدة من خلال الاحتفاظ بسجلّ سياق استدعاءات الأدوات وعرضه. تسمح مجموعات الأدوات المضمّنة والمخصّصة بسير عمل معقّد ومستقل، حيث يمكن للطراز، على سبيل المثال، أن يستند إلى بيانات الويب في الوقت الفعلي قبل استدعاء منطق نشاطك التجاري المحدّد.

في ما يلي مثال يوضّح كيفية تفعيل مجموعات الأدوات المضمّنة والمخصّصة باستخدام `google_search` ودالة مخصّصة `getWeather`:

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
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

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
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
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
        model: "gemini-3.5-flash",
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

### انتقال

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

    model := client.GenerativeModel("gemini-3.5-flash")
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## آلية العمل

تستخدم طُرز Gemini 3 ميزة *تداول سياق الأداة* لتفعيل مجموعات الأدوات المضمّنة والمخصّصة. تتيح ميزة "تداول سياق الأداة" الاحتفاظ بسياق الأدوات المضمّنة وعرضه ومشاركته مع الأدوات المخصّصة في نفس الاستدعاء من دور إلى آخر.

### تفعيل ميزة "الجمع بين الأدوات"

- يجب ضبط العلامة `include_server_side_tool_invocations` على `true` لتفعيل ميزة "تداول سياق الأداة".
- يجب تضمين [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#function-declarations)، بالإضافة إلى الأدوات المضمّنة التي تريد استخدامها، لتفعيل سلوك الجمع بين الأدوات.
  - إذا لم يتم تضمين `function_declarations`، ستظل ميزة "تداول سياق الأداة" تعمل على الأدوات المضمّنة المضمّنة، طالما تم ضبط العلامة.

### الأجزاء التي تعرضها واجهة برمجة التطبيقات

في ردّ واحد، تعرض واجهة برمجة التطبيقات الجزأين `toolCall` و`toolResponse` لاستدعاء الأداة المضمّنة. بالنسبة إلى استدعاء الدالة (الأداة المخصّصة)، تعرض واجهة برمجة التطبيقات جزء استدعاء `functionCall`، الذي يقدّم المستخدم له جزء `functionResponse` في الدور التالي.

- `toolCall` و`toolResponse`: تعرض واجهة برمجة التطبيقات هذين الجزأين للاحتفاظ بسياق الأدوات التي يتم تشغيلها من جهة الخادم ونتيجة تنفيذها في الدور التالي.
- `functionCall` و`functionResponse`: ترسل واجهة برمجة التطبيقات استدعاء الدالة إلى
  المستخدم لملء البيانات، ويرسل المستخدم النتيجة مرة أخرى في
  ردّ الدالة (هذه الأجزاء عادية لجميع ميزات [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في Gemini API، وليست فريدة لميزة
  الجمع بين الأدوات).
- ([أداة تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) فقط)
  `executableCode` و`codeExecutionResult`:
  عند استخدام أداة تنفيذ الرموز البرمجية، بدلاً من `functionCall` و
  `functionResponse`، تعرض واجهة برمجة التطبيقات `executableCode` (الرمز البرمجي الذي تم إنشاؤه
  بواسطة الطراز والمقصود تنفيذه) و`codeExecutionResult` (الـ
  نتيجة الرمز البرمجي القابل للتنفيذ).

يجب إعادة جميع الأجزاء، بما في ذلك جميع الـ [حقول](#critical-fields) التي
تحتوي عليها، إلى الطراز في كل دور للحفاظ على السياق وتفعيل ميزة "الجمع بين الأدوات"
.

### الحقول المهمة في الأجزاء المعروضة

ستتضمّن بعض [الأجزاء التي تعرضها واجهة برمجة التطبيقات](#api-returns-parts) الحقول `id` و
`tool_type` و`thought_signature`. تُعدّ هذه الحقول مهمة للحفاظ على سياق الأداة (وبالتالي مهمة لميزة "الجمع بين الأدوات")؛ ويجب إعادة جميع الأجزاء *كما هي موضّحة في الردّ* في طلباتك اللاحقة.

- `id`: معرّف فريد يربط استدعاءً بردّه. `id` يتم **ضبطه في
  جميع ردود استدعاء الدالة**، بغض النظر عن ميزة "تداول سياق الأداة".
  يجب *تقديم* `id` نفسه في ردّ الدالة
  الذي تقدّمه واجهة برمجة التطبيقات في استدعاء الدالة. تشارك الأدوات المضمّنة تلقائيًا `id` بين استدعاء الأداة وردّ الأداة.
  - يظهر في جميع الأجزاء ذات الصلة بالأداة: `toolCall` و`toolResponse` و`functionCall` و`functionResponse` و`executableCode` و `codeExecutionResult`
- `tool_type`: يحدّد الأداة المحدّدة المستخدَمة، أي اسم الأداة المضمّنة الحرفي (مثل `URL_CONTEXT`) أو اسم الدالة (مثل `getWeather`).
  - يظهر في الجزأين `toolCall` و`toolResponse`.
- `thought_signature`: السياق المشفّر الفعلي المضمّن في **كل جزء تعرضه واجهة برمجة التطبيقات**. لا يمكن إعادة إنشاء السياق بدون توقيعات الأفكار؛ وإذا لم يتم عرض توقيعات الأفكار لجميع الأجزاء في كل دور، سيحدث خطأ في الطراز.
  - يظهر في *جميع* الأجزاء.

### البيانات الخاصة بالأداة

تعرض بعض الأدوات المضمّنة وسيطات بيانات مرئية للمستخدم خاصة بنوع الأداة.

| الأداة | وسيطات استدعاء الأداة المرئية للمستخدم (إن وُجدت) | ردّ الأداة المرئي للمستخدم (إن وُجد) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` عناوين URL التي سيتم تصفّحها | `urls_metadata` `retrieved_url`: عناوين URL التي تم تصفّحها `url_retrieval_status`: حالة التصفّح |
| **FILE\_SEARCH** | بدون | بدون |

## مثال على بنية طلب الجمع بين الأدوات

تعرض بنية الطلب التالية بنية طلب الرسالة الفورية: "ما هي المدينة الواقعة في أقصى شمال الولايات المتحدة؟ وما حالة الطقس فيها اليوم؟". يجمع هذا الطلب بين ثلاث أدوات: الأداتان المضمّنتان في Gemini `google_search` و`code_execution`، ودالة مخصّصة `get_weather`.

```
{
  "model": "models/gemini-3.5-flash",
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

## الرموز المميّزة والأسعار

يُرجى العِلم أنّ الجزأين `toolCall` و`toolResponse` في الطلبات يتم احتسابهما ضمن `prompt_token_count`. بما أنّ خطوات الأداة الوسيطة هذه أصبحت مرئية ويتم عرضها لك، فهي جزء من سجلّ المحادثة. ينطبق ذلك على *الطلبات* فقط، وليس *الردود*.

تُستثنى أداة "بحث Google" من هذه القاعدة. تطبّق "بحث Google" نموذج التسعير الخاص بها على مستوى طلب البحث، لذا لا يتم تحصيل رسوم مضاعفة على الرموز المميّزة (راجِع صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)).

يُرجى قراءة صفحة [الرموز المميّزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar) لمزيد من المعلومات.

## القيود

- يتم تلقائيًا استخدام وضع `VALIDATED` (وضع `AUTO` غير متاح) عند تفعيل العلامة `include_server_side_tool_invocations`
- تعتمد الأدوات المضمّنة، مثل `google_search`، على معلومات الموقع الجغرافي والوقت الحالي، لذا إذا كانت `system_instruction` أو `function_declaration.description` تتضمّن معلومات متضاربة عن الموقع الجغرافي والوقت، قد لا تعمل ميزة "الجمع بين الأدوات" بشكل جيد.

## الأدوات المتاحة

ينطبق التداول العادي لسياق الأداة على الأدوات من جهة الخادم (المضمّنة).
تُعدّ أداة تنفيذ الرموز البرمجية أيضًا أداة من جهة الخادم، ولكنّها تتضمّن حلاً مضمّنًا خاصًا بها لتداول السياق. تُعدّ أداة استخدام الكمبيوتر وميزة "استدعاء الدوال" أدوات من جهة العميل، وتتضمّنان أيضًا حلولاً مضمّنة لتداول السياق.

| الأداة | جهة التنفيذ | إتاحة ميزة "تداول السياق" |
| --- | --- | --- |
| [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) | جهة الخادم | متاحة |
| [خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) | جهة الخادم | متاحة |
| [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) | جهة الخادم | متاحة |
| [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) | جهة الخادم | متاحة |
| [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) | جهة الخادم | متاحة (مضمّنة، تستخدم الجزأين `executableCode` و`codeExecutionResult`) |
| [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar) | من جهة العميل | متاحة (مضمّنة، تستخدم الجزأين `functionCall` و`functionResponse`) |
| [الدوال المخصّصة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) | من جهة العميل | متاحة (مضمّنة، تستخدم الجزأين `functionCall` و`functionResponse`) |

## الخطوات التالية

- مزيد من المعلومات عن [ميزة "استدعاء الدوال"](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في Gemini API
- استكشاف الأدوات المتاحة:
  - [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)
  - [خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)
  - [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)
  - [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-29 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
