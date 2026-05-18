---
source_url: https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar
fetched_at: 2026-05-18T05:16:20.725765+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تفاعلات البث

عند إنشاء Interaction، يمكنك ضبط `stream: true` لبث الردّ تدريجيًا باستخدام [الأحداث التي يرسلها الخادم](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) (SSE).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Count to from 1 to 25.",
    stream=True,
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Count to from 1 to 25.",
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Count to from 1 to 25.",
    "stream": true
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"1, 2, 3, 4, 5, 6, ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"7, 8, 9, 10, 11, 12, 13,","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":346,"total_input_tokens":11,"input_tokens_by_modality":[{"modality":"text","tokens":11}],"total_cached_tokens":0,"total_output_tokens":90,"total_tool_use_tokens":0,"total_thought_tokens":245},"created":"2026-05-12T18:44:51Z","updated":"2026-05-12T18:44:51Z","service_tier":"standard","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## أنواع الأحداث

يتضمّن كل حدث يتم إرساله من الخادم `event_type` باسم وبيانات JSON مرتبطة. تستخدم Interactions API نموذج بث متماثلًا يتدفّق فيه كل المحتوى، بما في ذلك النصوص واستدعاءات الأدوات والتفكير، من خلال حدث **قائم على الخطوات** ثابت.

يتّبع كل مصدر بيانات تدفّق الأحداث التالي:

1. ‫`interaction.created`: تم إنشاء التفاعل ويتضمّن بيانات وصفية (المعرّف والنموذج والحالة).
2. سلسلة من **الخطوات**، تتألف كل منها مما يلي:
   - حدث `step.start`، يشير إلى نوع الخطوة (مثل `model_output` أو `thought` أو `function_call`).
   - حدث واحد أو أكثر من أحداث `step.delta` مع بيانات متزايدة لتلك الخطوة
   - حدث `step.stop` يشير إلى أنّ الخطوة مكتملة.
3. `interaction.completed` حدث يتضمّن إحصاءات `usage` نهائية

عند ضبط `stream: false`، تعرض واجهة برمجة التطبيقات عنصر `interaction` واحدًا مع مصفوفة `steps`. كل عنصر في `steps` هو النسخة المجمّعة بالكامل من دورة `step.start` → `step.delta` → `step.stop`.

### `interaction.created`

يتم إرسال هذا الحدث عند إنشاء التفاعل لأول مرة. يحتوي على رقم تعريف التفاعل والنموذج والحالة الأولية.

```
event: interaction.created
data: {"interaction": {"id": "...", "model": "gemini-3-flash-preview", "status": "in_progress", "object": "interaction"}, "event_type": "interaction.created"}
```

### `interaction.status_update`

تشير إلى انتقال الحالة على مستوى التفاعل. قد تظهر بين الخطوات.

```
event: interaction.status_update
data: {"interaction_id": "...", "status": "in_progress", "event_type": "interaction.status_update"}
```

### `step.start`

تحدّد هذه السمة بداية خطوة جديدة. يتضمّن الخطوتَين `type` و`index`. يحدّد نوع الخطوة أنواع الدلتا المتوقّعة وكيفية ظهور الخطوة في استجابة غير متدفقة:

| نوع الخطوة | أنواع دلتا المتوقّعة | الوصف |
| --- | --- | --- |
| `model_output` | ‫`text`، `image`، `audio` | محتوى الردّ النهائي للنموذج. |
| `thought` | ‫`thought_signature`، `thought_summary` | الاستدلال بسلسلة الأفكار لا يظهر `summary` إلا عندما يكون `thinking_summaries` مفعَّلاً. |
| `function_call` | `arguments_delta` | طلب من العميل تنفيذ دالة تضبط هذه السمة حالة التفاعل على `requires_action`. |
| الأدوات من جهة الخادم | يختلف حسب الأداة | الأدوات التي يتم تنفيذها من خلال واجهة برمجة التطبيقات (مثل `google_search_call` و`google_search_result` و`code_execution_call` و`code_execution_result`) |

يمكنك الاطّلاع على [مرجع واجهة برمجة التطبيقات الخاصة بالتفاعلات](https://ai.google.dev/api/interactions?hl=ar) للحصول على القائمة الكاملة.

```
event: step.start
data: {"index": 0, "step": {"type": "model_output"}, "event_type": "step.start"}
```

بالنسبة إلى استدعاءات الدوال، تتضمّن الخطوة اسم الدالة ومعرّفها ووسيطات فارغة `{}`

```
event: step.start
data: {"index": 0, "step": {"type": "function_call", "id":"un6k8t18", "name": "get_weather", "arguments":{}}, "event_type": "step.start"}
```

### `step.delta`

البيانات التزايدية للخطوة الحالية يحتوي الكائن `delta` على الحقل `type` الذي يحدّد شكله.

**أمثلة:**

**`text`:** رمز مميّز نصي تدريجي من خطوة `model_output`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": "Hello, my name is Phil"}, "event_type": "step.delta"}

event: step.delta
data: {"index": 0, "delta": {"type": "text", "text": ", and I live in Germany." }, "event_type": "step.delta"}
```

استبدِل **`image`** ببيانات الصورة بترميز Base64 من خطوة `model_output`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg..."}, "event_type": "step.delta"}
```

**`thought_summary`:** ملخّص التفكير من خطوة `thought`:

```
event: step.delta
data: {"index": 0, "delta": {"type": "thought_summary", "content": {"type": "text", "text": "I need to find the GCD..."}}, "event_type": "step.delta"}
```

**`arguments_delta`:** سلسلة JSON (جزئية) لوسيطات استدعاء الدالة يجب أن يتم تجميعها على مستوى التغييرات:

```
event: step.delta
data: {"index": 0, "delta": {"type": "arguments_delta", "arguments": "{\"location\": \"San Francisco, CA\"}"}, "event_type": "step.delta"}
```

في ما يلي بعض أنواع التغييرات الأكثر شيوعًا. للاطّلاع على القائمة الكاملة بجميع أنواع التغييرات، يُرجى الرجوع إلى [مرجع واجهة برمجة التطبيقات Interactions](https://ai.google.dev/api/interactions?hl=ar).

### `step.stop`

تحدّد هذه السمة نهاية الخطوة. يحتوي على الخطوة `index`.

```
event: step.stop
data: {"index": 0, "event_type": "step.stop"}
```

### `interaction.completed`

يتم إرسال هذا الحدث عند انتهاء التفاعل. يحتوي على عنصر التفاعل النهائي مع إحصاءات `usage`. في الوضع غير المتدفّق، يكون هذا هو عنصر الاستجابة ذو المستوى الأعلى نفسه. لا يتضمّن `steps` في الردّ.

```
event: interaction.completed
data: {"interaction": {"id": "v1_abc123", "status": "completed", "usage": {"total_input_tokens": 7, "total_output_tokens": 12, "total_tokens": 19}}, "event_type": "interaction.completed"}
```

### `error`

يتم إرسال هذا الحدث عند حدوث خطأ أثناء التفاعل. يحتوي على عنصر خطأ يتضمّن رسالة ورمزًا.

```
event: error
data: {"error":{"message":"Deadline expired before operation could complete.","code":"gateway_timeout"},"event_type":"error"}
```

## البث المباشر باستخدام أدوات

تتيح واجهة برمجة التطبيقات Interactions API إمكانية البث باستخدام كلّ من الأدوات من جهة العميل (استدعاء الدوال) والأدوات من جهة الخادم (مثل "بحث Google" و"تنفيذ الرموز" وما إلى ذلك) في طلب واحد. أثناء البث، تظهر استدعاءات الأدوات كخطوات مكتوبة في سلسلة الأحداث. بالنسبة إلى استدعاءات الدوال، يقدّم الحدث `step.start` اسم الدالة، وتعمل أحداث `step.delta` على بث الوسيطات كسلاسل JSON (`arguments_delta`). يجب تجميع هذه التغييرات للحصول على الوسيطات الكاملة. يتم تنفيذ الأدوات من جهة الخادم، مثل &quot;بحث Google&quot;، تلقائيًا من خلال واجهة برمجة التطبيقات، ما يؤدي إلى إنشاء الخطوتَين `google_search_call` و`google_search_result`.

### البث باستخدام ميزة "استدعاء الدالة"

لإجراء عملية استدعاء الدالة باستخدام البث، يجب أن يتعامل العميل مع محادثة متعدّدة الجولات:
1. **الجولة 1 (طلب الدالة):** استدعِ الدالة `interactions.create` مع `stream: true` و`tools` الذي حدّدته. ستبث واجهة برمجة التطبيقات خطوة `function_call`. يجب تجميع سلاسل JSON للوسيطة المتزايدة (`arguments_delta`) من أحداث `step.delta` إلى أن يكتمل التفاعل بالحالة `requires_action`.
2. **الجولة 2 (إرسال النتيجة):** اتّصِل بالدالة `interactions.create` مرة أخرى، مع تمرير `previous_interaction_id` (مطابقة معرّف التفاعل الأول) وإرسال حزمة `function_result` ضمن مصفوفة `input`. يؤدي ذلك إلى استئناف البث، ما يسمح للنموذج بإنشاء الرد النهائي.

### Python

```
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA"
            }
        },
        "required": ["location"]
    }
}

# Turn 1: Request function call
stream = client.interactions.create(
    model="gemini-3-flash-preview",
    tools=[weather_tool],
    input="What is the weather in Paris right now?",
    stream=True,
)

first_interaction_id = None
func_call_id = None
func_call_name = None
func_args_accumulated = ""

for event in stream:
    if event.event_type == "interaction.created":
        first_interaction_id = event.interaction.id
    elif event.event_type == "step.start":
        step = event.step
        if step.type == "function_call":
            func_call_id = step.id
            func_call_name = step.name
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments_delta":
            func_args_accumulated += event.delta.arguments

# Turn 2: Execute tool and send the result back to resume stream
if func_call_id:
    # Execute weather_tool using accumulated arguments
    # args = json.loads(func_args_accumulated)
    dummy_result = {
        "content": [{"type": "text", "text": '{"weather": "Sunny and 22°C"}'}]
    }

    stream2 = client.interactions.create(
        model="gemini-3-flash-preview",
        previous_interaction_id=first_interaction_id,
        input=[{
            "type": "function_result",
            "name": func_call_name,
            "call_id": func_call_id,
            "result": dummy_result
        }],
        stream=True,
    )

    for event in stream2:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const weatherTool = {
    type: "function",
    name: "get_weather",
    description: "Get the current weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// Turn 1: Request function call
const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    tools: [weatherTool],
    input: "What is the weather in Paris right now?",
    stream: true,
});

let firstInteractionId = null;
let funcCallId = null;
let funcCallName = null;
let funcArgsAccumulated = "";

for await (const event of stream) {
    if (event.event_type === "interaction.created") {
        firstInteractionId = event.interaction.id;
    } else if (event.event_type === "step.start") {
        const step = event.step;
        if (step.type === "function_call") {
            funcCallId = step.id;
            funcCallName = step.name;
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "arguments_delta") {
            funcArgsAccumulated += event.delta.arguments;
        }
    }
}

// Turn 2: Execute tool and send the result back to resume stream
if (funcCallId && firstInteractionId && funcCallName) {
    // const args = JSON.parse(funcArgsAccumulated);
    const dummyResult = {
        content: [{ type: "text", text: '{"weather": "Sunny and 22°C"}' }]
    };

    const stream2 = await client.interactions.create({
        model: "gemini-3-flash-preview",
        previous_interaction_id: firstInteractionId,
        input: [{
            type: "function_result",
            name: funcCallName,
            call_id: funcCallId,
            result: dummyResult
        }],
        stream: true,
    });

    for await (const event of stream2) {
        if (event.event_type === "step.delta") {
            if (event.delta.type === "text") {
                process.stdout.write(event.delta.text);
            }
        }
    }
}
```

### REST

**الجولة 1:** طلب استدعاء الدالة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the weather in Paris right now?",
    "stream": true,
    "tools": [
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

**الجولة 2:** أرسِل نتيجة الدالة باستخدام `previous_interaction_id` و`call_id` من الجولة 1

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "v1_ChdGUVFJYXBXVUdLVEF4TjhQ...",
    "stream": true,
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "CALL_ID",
        "result": {
          "content": [
            {
              "type": "text",
              "text": "{\"weather\": \"Sunny and 22°C\"}"
            }
          ]
        }
      }
    ]
  }'
```

### البث باستخدام أدوات متعددة

يستخدم المثال التالي كلاً من أداة `function` و`google_search` في طلب واحد:

### Python

```
from google import genai

client = genai.Client()

tools = [
    {"type": "google_search"},
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA"
                }
            },
            "required": ["location"]
        }
    }
]

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    tools=tools,
    input="Search what it the largest mountain in Europe and what the weather is there right now?",
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        step = event.step
        print(f"\n--- Step {event.index}: {step.type} ---")
        # Show details for tool steps
        if step.type == "google_search_call":
            print(f"  Search ID: {step.id}")
        elif step.type == "google_search_result":
            print(f"  Result for: {step.call_id}")
        elif step.type == "function_call":
            print(f"  Function: {step.name}({step.arguments})")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "google_search_call":
            print(f"  Queries: {event.delta.arguments}")
        elif event.delta.type == "arguments_delta":
            print(f"  Args chunk: {event.delta.arguments}", end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nStatus: {event.interaction.status}")
        if event.interaction.status == "requires_action":
            print("Action required: provide function call results to continue.")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const tools = [
    { type: "google_search" },
    {
        type: "function",
        name: "get_weather",
        description: "Get the current weather in a given location",
        parameters: {
            type: "object",
            properties: {
                location: {
                    type: "string",
                    description: "The city and state, e.g. San Francisco, CA"
                }
            },
            required: ["location"]
        }
    }
];

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    tools: tools,
    input: "Search what it the largest mountain in Europe and what the weather is there right now?",
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        const step = event.step;
        console.log(`\n--- Step ${event.index}: ${step.type} ---`);
        // Show details for tool steps
        if (step.type === "google_search_call") {
            console.log(`  Search ID: ${step.id}`);
        } else if (step.type === "google_search_result") {
            console.log(`  Result for: ${step.call_id}`);
        } else if (step.type === "function_call") {
            console.log(`  Function: ${step.name}(${JSON.stringify(step.arguments)})`);
        }
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "google_search_call") {
            console.log(`  Queries: ${JSON.stringify(event.delta.arguments?.queries)}`);
        } else if (event.step.type === "google_search_result") {
            console.log(`  Result for: ${event.step.call_id}`);
        } else if (event.delta.type === "arguments_delta") {
            process.stdout.write(`  Args chunk: ${event.delta.arguments}`);
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nStatus: ${event.interaction.status}`);
        if (event.interaction.status === "requires_action") {
            console.log("Action required: provide function call results to continue.");
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Search what it the largest mountain in Europe and what the weather is there right now?",
    "stream": true,
    "tools": [
      { "type": "google_search" },
      {
        "type": "function",
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"id":"mkutnkgn","signature":"","type":"google_search_call"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"google_search_call","arguments":{"queries":["largest mountain in Europe"]}},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"call_id":"mkutnkgn","signature":"","type":"google_search_result"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"google_search_result","is_error":false},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"id":"ktr5aysg","type":"function_call","name":"get_weather","arguments":{}},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"arguments":"{\"location\":\"Mount Elbrus, Russia\"}","type":"arguments_delta"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"requires_action","usage":{"total_tokens":299,"total_input_tokens":138,"input_tokens_by_modality":[{"modality":"text","tokens":138}],"total_cached_tokens":0,"total_output_tokens":20,"total_tool_use_tokens":0,"total_thought_tokens":141},"created":"2026-05-12T17:24:26Z","updated":"2026-05-12T17:24:26Z","service_tier":"standard","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## البث مع ميزة "التفكير بصوت عالٍ"

عندما يستخدم النموذج التفكير، ستتلقّى خطوات `thought` بنوعَين مختلفَين من دلتا: `thought_summary` (محتوى ملخّص نصي أو مرئي تدريجي) و`thought_signature` (تمثيل مشفّر لعملية الاستدلال الداخلية للنموذج، يتم إرساله كآخر دلتا قبل `step.stop`). إذا كانت `thinking_summaries` مفعّلة، ستعرض دلتا `thought_summary` ملخّصًا لعملية الاستدلال التي أجراها النموذج. لمزيد من التفاصيل حول التفكير، اطّلِع على [دليل التفكير](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the greatest common divisor of 1071 and 462?",
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True,
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is the greatest common divisor of 1071 and 462?",
    generation_config: {
        thinking_summaries: "auto",
    },
    stream: true,
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        } else if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What is the greatest common divisor of 1071 and 462?",
    "stream": true,
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3-flash-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"**Implementing Euclidean Algorithm**\n\nI've just worked through a detailed example applying the Euclidean algorithm to find the GCD of 1071 and 462, confirming its step-by-step nature. The calculations went smoothly, tracking the remainders until zero. My focus is now solidifying the implementation logic, ensuring accuracy and considering potential edge cases. I'll translate this example into code.\n\n\n","type":"text"},"type":"thought_summary"},"event_type":"step.delta"}

event: step.delta
data: {"index":0,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

...
```

## بث المحتوى باستخدام الوكلاء

تتيح واجهة Interactions API استخدام وكلاء، مثل Deep Research. تستخدم البرامج الآلية `background=True` وتعرض النتائج بشكل غير متزامن، ولكن يمكنك أيضًا بث تفاعلات البرنامج الآلي لتلقّي آخر الأخبار حول مستوى التقدّم والخطوات الوسيطة فور حدوثها. لمزيد من التفاصيل، يُرجى الاطّلاع على [دليل Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="deep-research-preview-04-2026",
    input="Research the latest advances in quantum computing.",
    stream=True,
    background=True,
    agent_config={
        "type": "deep-research",
        "thinking_summaries": "auto"
    }
)
for event in stream:
    if event.event_type == "step.start":
        print(f"\n--- Step: {event.step.type} ---")
    elif event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "thought_summary":
            if event.delta.content.type == "text":
                print(event.delta.content.text, end="", flush=True)
    elif event.event_type == "interaction.completed":
        print(f"\n\nTotal Tokens: {event.interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "deep-research-preview-04-2026",
    input: "Research the latest advances in quantum computing.",
    stream: true,
    background: true,
    agent_config: {
        type: "deep-research",
        thinking_summaries: "auto"
    }
});
for await (const event of stream) {
    if (event.event_type === "step.start") {
        console.log(`\n--- Step: ${event.step.type} ---`);
    } else if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "thought_summary") {
            if (event.delta.content.type === "text") {
                process.stdout.write(event.delta.content.text);
            }
        }
    } else if (event.event_type === "interaction.completed") {
        console.log(`\n\nTotal Tokens: ${event.interaction.usage.total_tokens}`);
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "agent": "deep-research-preview-04-2026",
    "input": "Research the latest advances in quantum computing.",
    "stream": true,
    "background": true,
    "agent_config": {
      "type": "deep-research",
      "thinking_summaries": "auto"
    }
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"content":{"text":"***Generating research plan***\n\nTo best answer your request, I'm starting by constructing a comprehensive research plan. This will outline the key areas I need to investigate and the strategy I'll use to connect them."},"type":"thought_summary"},"event_type":"step.delta"}

... (additional thought steps) ...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"# The Quantum Inflection Point: Exhaustive Analysis of Hardware, Algorithms, and Market Dynamics in 2026\n\n## Executive Summary\n\n..."},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":1117031,"total_input_tokens":428865,"total_output_tokens":22294,"total_thought_tokens":26213},"created":"2026-05-12T17:24:27Z","updated":"2026-05-12T17:24:27Z","object":"interaction","agent":"deep-research-preview-04-2026"},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## إنشاء الصور أثناء البث

تتيح Interactions API بث وسائط إخراج متعددة في الوقت نفسه. من خلال طلب كل من `text` و`image` في `response_format`، يمكنك تلقّي نص متداخل وصور من إنشاء الذكاء الاصطناعي في البث نفسه.

يستخدم المثال التالي `gemini-3.1-flash-image-preview` (Nano Banana 2) للبحث عن معلومات وإنشاء قصة تتضمّن رسومات توضيحية متداخلة.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.1-flash-image-preview",
    tools=[{"type": "google_search", "search_types": ["web_search", "image_search"]}],
    input="Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format=[
        {"type": "text"},
        {"type": "image"}
    ],
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
        elif event.delta.type == "image":
            print(f"\n[Image chunk: {len(event.delta.data)} bytes]", end="", flush=True)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3.1-flash-image-preview",
    tools: [{ type: "google_search", search_types: ["web_search", "image_search"] }],
    input: "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    response_format: [
        { type: "text" },
        { type: "image" }
    ],
    stream: true,
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "text") {
            process.stdout.write(event.delta.text);
        } else if (event.delta.type === "image") {
            console.log(`\n[Image chunk: ${event.delta.data.length} bytes]`);
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.1-flash-image-preview",
    "input": "Search for the history of the Colosseum and write a short illustrated story about a gladiator named Marcus. Interleave text and generated images.",
    "stream": true,
    "tools": [
      { "type": "google_search",
        "search_types": ["web_search", "image_search"]
      }
    ],
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "response_format": [
      { "type": "text" }, { "type": "image"}
    ]
  }'
```

```
event: interaction.created
data: {"interaction":{"id":"v1_...","status":"in_progress","object":"interaction","model":"gemini-3.1-flash-image-preview"},"event_type":"interaction.created"}

event: interaction.status_update
data: {"interaction_id":"v1_...","status":"in_progress","event_type":"interaction.status_update"}

event: step.start
data: {"index":0,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"text":"Here is a short illustrated story about the Colosseum...\n\n### Part 1: The New Flavian Amphitheater\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: step.start
data: {"index":2,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":2,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCg...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":2,"delta":{"text":"### Part 2: The Hypogeum and the Wait\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":2,"event_type":"step.stop"}

event: step.start
data: {"index":3,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":3,"delta":{"signature":"...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":3,"event_type":"step.stop"}

event: step.start
data: {"index":4,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":4,"delta":{"mime_type":"image/jpeg","data":"/9j/4AAQSkZJRgABAQAAAQABAAD/...","type":"image"},"event_type":"step.delta"}

event: step.delta
data: {"index":4,"delta":{"text":"### Part 3: The Moment of Spectacle\n\n...","type":"text"},"event_type":"step.delta"}

...

event: step.stop
data: {"index":4,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_...","status":"completed","usage":{"total_tokens":6128,"total_input_tokens":29,"total_output_tokens":6099,"output_tokens_by_modality":[{"modality":"image","tokens":4480}]}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## التعامل مع الأحداث غير المعروفة

وفقًا لسياسة تحديد الإصدارات لواجهة برمجة التطبيقات، قد تتم إضافة أنواع جديدة من الأحداث وأنواع التغييرات بمرور الوقت. يجب أن يتعامل الرمز البرمجي مع أنواع الأحداث غير المعروفة بشكلٍ سليم، أي أنّه يجب تسجيل أي أحداث لا تتعرّف عليها وتخطّيها بدلاً من عرض خطأ.

## الخطوات التالية

- [مزيد من المعلومات حول Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=ar)
- استكشاف [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar) باستخدام الأدوات
- [مزيد من المعلومات حول ميزة "التفكير"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=ar) لتحسين عملية الاستدلال
- جرِّب [وكيل Deep Research](https://ai.google.dev/gemini-api/docs/interactions/deep-research?hl=ar) للمهام الطويلة المدى.
- راجِع [مرجع واجهة برمجة التطبيقات الخاصة بالتفاعلات](https://ai.google.dev/api/interactions?hl=ar) للاطّلاع على جميع أنواع الأحداث وأنواع التغيير.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
