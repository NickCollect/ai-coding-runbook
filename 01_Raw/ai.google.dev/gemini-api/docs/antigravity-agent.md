---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar
fetched_at: 2026-07-20T04:44:15.617781+00:00
title: "Antigravity Agent \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# Antigravity Agent

‫وكيل Antigravity هو وكيل مُدار للأغراض العامة على Gemini API. يمنحك طلب واحد من واجهة برمجة التطبيقات وكيلاً يمكنه التفكير وتنفيذ الرموز البرمجية وإدارة الملفات وتصفّح الويب داخل بيئة الاختبار المعزولة الآمنة المستندة إلى Linux والتي تستضيفها Google.

يستند إلى Gemini 3.5 Flash ويستخدم واجهة برمجة التطبيقات نفسها المستخدَمة في Antigravity IDE. يمكنك الاستفادة من هذه الميزة من خلال [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) و[Google AI Studio](https://aistudio.google.com?hl=ar).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## الإمكانات

يمكن لكل مكالمة توفير بيئة اختبارية لنظام التشغيل Linux وبدء حلقة استخدام الأدوات. يخطّط الوكيل وينفّذ ويراقب النتائج ويكرّر العملية إلى أن يتم إنجاز المهمة.

- **تنفيذ الرموز البرمجية:** يمكنك تنفيذ أوامر Bash وPython وNode.js. تثبيت الحِزم وإجراء الاختبارات وإنشاء التطبيقات
- **إدارة الملفات:** قراءة الملفات وكتابتها وتعديلها والبحث فيها وإدراجها في وضع الحماية تظل الملفات متوفّرة خلال التفاعلات.
- **الوصول إلى الويب:** تستخدم "بحث Google" وعملية جلب عناوين URL للحصول على البيانات.
- **ضغط السياق:** يتم ضغط السياق تلقائيًا (عند حوالي 135 ألف رمز مميز) لدعم الجلسات الطويلة والمحادثة المترابطة بدون فقدان السياق أو تجاوز حدود الرموز المميزة.

يمكنك الاطّلاع على [دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar) لمعرفة كيفية استخدام المحادثات المترابطة والبث.

## الأدوات المتوافقة

بشكلٍ تلقائي، يمكن للوكيل الوصول إلى `code_execution` و`google_search` و`url_context`. يتم تفعيل أدوات نظام الملفات تلقائيًا عند تحديد المَعلمة `environment`. يمكنك أيضًا تحديد **وظائف مخصّصة** لربط الوكيل بواجهات برمجة التطبيقات والأدوات الخاصة بك. ما عليك سوى تحديد المَعلمة `tools` عند تخصيص المجموعة التلقائية أو حصرها، أو عند إضافة وظائف مخصّصة.

| الأداة | كتابة قيمة | الوصف |
| --- | --- | --- |
| تنفيذ الرموز البرمجية | `code_execution` | تنفيذ أوامر shell (مثل bash وPython وNode) مع إمكانية تسجيل stdout/stderr |
| بحث Google | `google_search` | البحث في شبكة الويب المتاحة للجميع |
| سياق عناوين URL | `url_context` | جلب صفحات الويب وقراءتها |
| نظام الملفات | *(مفعَّلة من خلال `environment`)* | قراءة الملفات وكتابتها وتعديلها والبحث فيها وإدراجها في وضع الحماية لا يوجد نوع أداة منفصل، ويتم تفعيله تلقائيًا عند ضبط `environment`. |
| الدوال المخصّصة | `function` | تحديد دوال مخصّصة يمكن للوكيل طلب تنفيذها يُرجى الاطّلاع على [استدعاء الدالة](#function-calling). |
| خادم MCP البعيد | `mcp_server` | تسجيل خوادم بروتوكول سياق النموذج (MCP) الخارجية كأدوات اطّلِع على [خوادم MCP](#mcp-servers). |

لحصر وصول الوكيل إلى أدوات معيّنة، مرِّر الأدوات التي تحتاج إليها فقط:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## الإدخال المتعدد الوسائط

يتوافق وكيل Antigravity مع الإدخالات المتعدّدة الوسائط. في الوقت الحالي، لا تتوفّر سوى المدخلات `text` و`image`. يجب تقديم الصور كسلاسل مضمّنة بترميز base64 (`data`).

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### REST

```
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## استدعاء الدالة

تتيح لك ميزة "استدعاء الدوال" ربط وكيل Antigravity بواجهات برمجة التطبيقات وقواعد البيانات الخارجية من خلال تحديد أدوات مخصّصة يمكن للوكيل استدعاؤها. للاطّلاع على المفاهيم العامة، يُرجى الرجوع إلى [استدعاء الدوال باستخدام Gemini API](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar).

يوضّح المثال التالي تفاعلاً من خطوتين. يطلب الوكيل أولاً إجراء استدعاء دالة مخصّصة `get_weather`، وينفّذه العميل ويعرض النتيجة في الجولة الثانية.

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-05-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Define the custom function
const get_weather_tool = {
  type: "function",
  name: "get_weather",
  description: "Gets the current weather for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city and country, e.g. San Francisco, USA",
      },
    },
    required: ["location"],
  },
};

// 2. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-05-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    get_weather_tool,
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    interaction.steps
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = interaction.steps.filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

    // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
    const functionResult = {
      temperature: 23,
      unit: "celsius"
    };

    const finalInteraction = await client.interactions.create({
      agent: "antigravity-preview-05-2026",
      previous_interaction_id: interaction.id, // Reference the interaction ID
      environment: interaction.environment_id,
      input: [
        {
          type: "function_result",
          name: fcStep.name,
          call_id: fcStep.id,
          result: functionResult,
        }
      ],
    }, { timeout: 300000 });

    console.log(finalInteraction.output_text);
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## خوادم MCP

يمكنك ربط وكيل Antigravity بأدوات خارجية من خلال تسجيل خوادم بروتوكول سياق النموذج (MCP) البعيدة. يتيح العامل استخدام خوادم MCP البعيدة عبر HTTP القابل للبث.

عند تسجيل خادم MCP، يجب تحديد الحقول التالية في مصفوفة `tools`:

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `type` | سلسلة | نعم | يجب أن تكون `"mcp_server"`. |
| `name` | سلسلة | نعم | هي معرّف فريد للخادم. يجب أن تكون الأحرف صغيرة وأبجدية رقمية (مطابقة للنمط `^[a-z0-9_-]+$`). |
| `url` | سلسلة | نعم | عنوان URL لنقطة نهاية خادم MCP البعيد |
| `headers` | عنصر | لا | العناوين المخصّصة (مثل المصادقة) التي يتم إرسالها مع الطلبات |
| `allowed_tools` | صفيف | لا | قائمة بأسماء الأدوات المسموح بتنفيذها. في حال عدم تحديد أي أداة، سيتم السماح بجميع الأدوات. |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## تخصيص الوكيل

يمكنك توسيع نطاق عمل وكيل Antigravity من خلال تخصيص تعليماته وأدواته وبيئته. يتيح لك البرنامج المساعد استخدام طريقة مخصّصة لنظام الملفات: يمكنك تحميل ملفات مثل `AGENTS.md` للحصول على التعليمات والمهارات ضمن `.agents/skills/` مباشرةً إلى وضع الحماية، أو تمرير الإعدادات المضمّنة في وقت التفاعل. يمكنك تكرار عملية الإعداد بشكل مضمّن ثم حفظها كوكيل مُدار عندما تكون مستعدًا.

للحصول على التفاصيل الكاملة حول كيفية إنشاء وكلاء مخصّصين، يُرجى الاطّلاع على [إنشاء وكلاء مُدارين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar).

## التنفيذ في الخلفية

قد تستغرق مهام الوكيل التي تتضمّن الاستدلال المتعدّد الخطوات أو تطبيق الرموز البرمجية أو عمليات الملفات عدة دقائق لإكمالها. استخدِم `background=True` لتنفيذ التفاعل بشكل غير متزامن. تعرض واجهة برمجة التطبيقات على الفور معرّف تفاعل يمكنك استخدامه في طلبات البحث إلى أن تصبح الحالة `completed` أو `failed`.

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

يتطلّب التنفيذ في الخلفية `store=True`، وهو الإعداد التلقائي. للاطّلاع على آخر المعلومات عن التقدّم في الوقت الفعلي أثناء التنفيذ في الخلفية، راجِع [تفاعلات البث في الخلفية](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=ar#streaming-background).

يمكنك إلغاء تفاعل قيد التشغيل في الخلفية باستخدام الطريقة `cancel`.

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**محادثة مترابطة مع التنفيذ في الخلفية**

عندما يتضمّن تفاعل في الخلفية أدوات ذات حالة (مثل تطبيق الرموز البرمجية في بيئة الاختبار)، استخدِم `environment_id` من التفاعل المكتمل للمتابعة في البيئة نفسها. يضمن ذلك أن يتابع الوكيل من حيث توقّف مع الاحتفاظ بجميع الملفات والحالة.

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-05-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## البيئات

ينشئ كل طلب أو يعيد استخدام بيئة اختبار Linux. تتخذ المَعلمة `environment` ثلاثة أشكال:

| النموذج | الوصف |
| --- | --- |
| `"remote"` | توفير وضع حماية جديد مع الإعدادات التلقائية |
| `"env_abc123"` | إعادة استخدام بيئة حالية من خلال رقم التعريف، مع الاحتفاظ بجميع الملفات والحالة |
| `{...}` | `EnvironmentConfig` كاملة مع مصادر وقواعد شبكة مخصّصة |

اطّلِع على [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar) للحصول على تفاصيل حول المصادر (Git وGCS والمضمّنة) والشبكات ودورة الحياة وحدود الموارد.

## العوامل التي تؤدي إلى الظهور

تتيح لك المشغّلات جدولة وكيل ليتم تشغيله تلقائيًا وفقًا لجدول زمني. يربط المشغّل بين وكيل وبيئة وطلب وجدول زمني في مورد ثابت يتم تشغيله بدون تدخل يدوي. تعيد كل عملية تنفيذ استخدام البيئة نفسها، لذا تظل الملفات التي تم إنشاؤها في عملية تنفيذ واحدة محفوظة ويمكن رؤيتها في عملية التنفيذ التالية.

### إنشاء مشغِّل

أنشئ مشغّلاً من خلال تحديد جدول cron والمنطقة الزمنية وإعدادات التفاعل. يبدأ المشغّل بالحالة `active` وسيتم تشغيله في وقت cron التالي المطابق. احفظ `id` الذي تم عرضه لإدارة مشغّل الإجراء في المكالمات اللاحقة.

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-05-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "transform": {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                        },
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-05-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        transform: {
                            "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                        },
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-05-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "transform": {
                              "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                          }
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

يقبل طلب `CreateTrigger` الحقول التالية:

| الحقل | النوع | مطلوب | الوصف |
| --- | --- | --- | --- |
| `schedule` | سلسلة | نعم | تعبير Cron (مثل `0 * * * *` كل ساعة، و`0 9 * * 1-5` لصباح أيام الأسبوع) |
| `time_zone` | سلسلة | نعم | المنطقة الزمنية التابعة لهيئة IANA (مثل `UTC` أو `America/Argentina/Buenos_Aires`) |
| `display_name` | سلسلة | لا | اسم عامل التشغيل الذي يمكن للمستخدم قراءته. |
| `max_consecutive_failures` | عدد صحيح | لا | الحد الأقصى لعدد حالات الفشل قبل إيقاف المشغّل مؤقتًا تلقائيًا القيمة التلقائية: 5 |
| `execution_timeout_seconds` | عدد صحيح | لا | مهلة لكل عملية تنفيذ بالثواني. القيمة التلقائية: 600 |
| `interaction` | عنصر | نعم | `CreateInteractionRequest` يحدّد الوكيل والمدخلات والأدوات والبيئة. |

تتضمّن الاستجابة حقول المفاتيح التالية:

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `id` | سلسلة | المعرّف الفريد للمشغّل. استخدِم هذا المعرّف في جميع العمليات اللاحقة. |
| `status` | سلسلة | الحالة الحالية: `active` أو `paused` أو `disabled` |
| `next_run_time` | سلسلة | الطابع الزمني بتنسيق ISO 8601 لعملية التنفيذ المُجدوَلة التالية |
| `consecutive_failure_count` | عدد صحيح | عدد عمليات التنفيذ المتتالية التي تعذّر إجراؤها منذ آخر عملية ناجحة |

### أحداث تشغيل القائمة

استرداد جميع المشغّلات المرتبطة بمشروعك

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### الحصول على مشغّل

استرجاع الإعداد الكامل والحالة الحالية لمشغّل واحد

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### الإيقاف المؤقت والاستئناف

يمكنك إيقاف مشغّل مؤقتًا لإيقاف عمليات التنفيذ المجدوَلة، واستئنافه لإعادة تفعيل الجدول الزمني. لا يؤثّر الإيقاف المؤقت في عمليات التنفيذ اليدوية.

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### حذف مشغّل

إزالة مشغّل نهائيًا لا يتم حذف سجلّ عمليات التنفيذ السابقة.

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### تشغيل مشغّل على الفور

تفعيل مشغّل عند الطلب بدون انتظار الوقت المُجدوَل التالي يعمل هذا الإجراء حتى إذا تم إيقاف المشغّل مؤقتًا.

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### عمليات التنفيذ المدرَجة

عرض سجلّ التنفيذ لمشغّل يتضمّن كل تنفيذ `status` وطوابع زمنية و`interaction_id` يمكنك استخدامه لجلب ناتج التفاعل الكامل و`environment_id` يؤكّد أنّ جميع عمليات التشغيل تشترك في بيئة وضع الحماية نفسها.

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## التوفّر والأسعار

يتوفّر وكيل Antigravity في إصدار تجريبي من خلال
[واجهة Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) في Google AI Studio
وGemini API لكل من المشاريع ضمن المستوى المجاني والمستوى المدفوع.

تستند الأسعار إلى [نموذج الدفع حسب الاستخدام](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#pricing-for-agents)
استنادًا إلى الرموز المميزة لنموذج Gemini الأساسي والأدوات التي يستخدمها الوكيل. على عكس طلبات الدردشة العادية التي تنتج مخرجات فردية، فإنّ التفاعل مع Antigravity هو سير عمل قائم على الوكلاء. يؤدي طلب واحد إلى تشغيل حلقة مستقلة من الاستدلال وتنفيذ الأدوات وتشغيل الرموز البرمجية وإدارة الملفات. تتضمّن مشاريع المستوى المجاني حدًا مجانيًا لعدد الطلبات في الدقيقة وحصة استخدام.

تُشغّل تفاعلات Antigravity حلقات مستقلة في محادثة مترابطة ويمكنها استهلاك عدد كبير من الرموز المميزة. اضبط [عناصر التحكّم في الميزانية](#budget-controls) على طلبك للحدّ من استخدام الرموز المميزة. يمكنك أيضًا تتبُّع مستوى التقدّم في الوقت الفعلي باستخدام
[البث المباشر من خلال أحداث يتم إرسالها من الخادم](https://ai.google.dev/gemini-api/docs/streaming?hl=ar)، أو إلغاء الطلبات الجارية.

### عناصر التحكّم في الميزانية

اضبط `max_total_tokens` داخل `agent_config` (مع `"type": "antigravity"`) للحدّ من إجمالي عدد الرموز المميزة (المدخلات + المخرجات + التفكير) التي يمكن أن يستهلكها تفاعل معيّن.
لا يتم احتساب الرموز المميزة المخزّنة مؤقتًا ضمن هذا الحدّ. عندما يبلغ الوكيل الحدّ الأقصى، تتوقف المحادثة ويعود الردّ مع `status: "incomplete"`. الحدّ الأقصى هو أفضل ما يمكن تقديمه، وقد يتجاوزه الاستخدام الفعلي بشكل طفيف حسب الوقت الذي يتحقّق فيه الوكيل من الميزانية بين الخطوات.

اضبط الميزانية على طلب التفاعل في `agent_config` بجانب `agent` و`input`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage.total_tokens}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### مواصلة تفاعل غير مكتمل

عندما تعرض تفاعلاً `status: "incomplete"`، يتم الاحتفاظ بعمل الموظف وسياقه. أرسِل تفاعلاً جديدًا يشير إلى التفاعل الأصلي `id` و`environment_id` لمتابعة المحادثة من حيث توقّفت، وسيتم تخصيص ميزانية `max_total_tokens` للتفاعل الجديد.

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: 50000
    }
});
console.log(`Status: ${continuation.status}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-05-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### التكاليف المقدَّرة

تختلف التكاليف حسب مدى تعقيد المهمة. يحدّد الوكيل بشكل مستقل عدد استدعاءات الأدوات وعمليات تنفيذ الرموز البرمجية وعمليات الملفات المطلوبة. تستند التقديرات التالية إلى عمليات التشغيل.

| فئة المهمة | الرموز المميّزة المدخَلة | الرموز المميّزة الناتجة | التكلفة العادية |
| --- | --- | --- | --- |
| **البحث وتجميع المعلومات** | ‫100 ألف إلى 500 ألف | ‫10 آلاف إلى 40 ألف | ‫0.30–1.00 دولار أمريكي |
| **إنشاء المستندات والمحتوى** | ‫100 ألف إلى 500 ألف | ‫15,000 إلى 50,000 | ‫0.30–1.30 دولار أمريكي |
| **تصميم العمليات والأنظمة** | ‫100 ألف إلى 400 ألف | ‫10 آلاف إلى 30 ألف | ‫0.25–0.80 دولار أمريكي |
| **معالجة البيانات وتحليلها** | ‫300 ألف - 3 ملايين | ‫30 ألفًا إلى 150 ألفًا | ‫0.70–3.25 دولار أمريكي |

يتم عادةً تخزين %50 إلى %70 من الرموز المميزة للإدخال مؤقتًا. يمكن أن تتراكم في عمليات سير العمل المعقّدة التي تتضمّن العديد من استدعاءات الأدوات ما بين 3 و5 ملايين رمز مميز في تفاعل واحد، بتكاليف تصل إلى 5 دولارات أمريكية تقريبًا.

**لا يتم تحصيل رسوم** مقابل **حوسبة البيئة** (وحدة المعالجة المركزية والذاكرة والتنفيذ في وضع الحماية) خلال فترة المعاينة.

## القيود

- **حالة المعاينة:** وكيل Antigravity وواجهة Interactions API قد تتغيّر الميزات والمخططات.
- **إعدادات إنشاء غير صالحة:** المعلمات التالية غير صالحة وتعرض الخطأ 400: `temperature` و`top_p` و`top_k` و`stop_sequences` و`max_output_tokens`.
- **الناتج المنظَّم:** لا يتيح وكيل Antigravity النواتج المنظَّمة.
- **الأدوات غير المتاحة:** لا تتوفّر الأدوات `file_search` و`computer_use` و`google_maps` بعد.
- **قيود MCP عن بُعد:** لا تتوفّر إمكانية نقل البيانات باستخدام أحداث Server-Sent Events (SSE) (استخدِم Streamable HTTP). بالإضافة إلى ذلك، يجب أن يكون الخادم `name` بأحرف صغيرة وأبجدية رقمية فقط (يؤدي استخدام الأحرف الكبيرة إلى ظهور الخطأ العام `400 Bad Request`).
- **أداة نظام الملفات:** لا تتوفّر أداة نظام الملفات في الوقت الحالي. وهي جزء من `environment`.
- **متطلبات المتجر:** يتطلّب تنفيذ الوكيل باستخدام `background=True` توفّر `store=True`.
- **استدعاء الدوال في الوضع الثابت فقط:** لا يمكن استدعاء الدوال إلا في الوضع الثابت. يجب استخدام `previous_interaction_id` لمواصلة المحادثة، إذ لا يمكن إعادة إنشاء السجلّ يدويًا (وضع بلا حالة).
- **أنواع الوسائط المتعددة غير المتوافقة** لا تتوافق هذه الميزة مع ملفات الصوت والفيديو والمستندات في الوقت الحالي. يُسمح فقط بالنصوص والصور.

## الخطوات التالية

- [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): المحادثات المترابطة والبث
- [إنشاء وكلاء مخصّصين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar): تعليمات ومهارات مخصّصة وحفظ الوكلاء
- [البيئات](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar): إعدادات وضع الحماية والمصادر والشبكات
- [‫Deep Research Agent](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar): مهام البحث الطويلة
- [واجهة برمجة التطبيقات Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar): هي واجهة برمجة التطبيقات الأساسية.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-16 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
