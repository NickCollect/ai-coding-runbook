---
source_url: https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ar
fetched_at: 2026-05-25T05:28:41.716098+00:00
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

# الجمع بين الأدوات المضمّنة واستدعاء الدوال

يتيح Gemini الجمع بين [الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)، مثل `google_search`، و[استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar) (المعروفة أيضًا باسم *الأدوات المخصّصة*) في تفاعل واحد من خلال الاحتفاظ بسجلّ سياق استدعاءات الأدوات وعرضه. تتيح مجموعات الأدوات المضمّنة والمخصّصة إمكانية إنشاء سير عمل معقّد يعتمد على الذكاء الاصطناعي، حيث يمكن للنموذج، على سبيل المثال، الاستناد إلى بيانات الويب في الوقت الفعلي قبل استدعاء منطق عملك المحدّد.

في ما يلي مثال يتيح استخدام توليفات الأدوات المضمّنة والمخصّصة مع `google_search` ودالة مخصّصة `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
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

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
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

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
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

## آلية العمل

تستخدم نماذج Gemini 3 *تداول سياق الأدوات* لتفعيل مجموعات الأدوات المضمّنة والمخصّصة. تتيح ميزة "تداول سياق الأداة" الحفاظ على سياق الأدوات المضمّنة وعرضه ومشاركته مع الأدوات المخصّصة في التفاعل نفسه.

### تفعيل دمج الأدوات

- أدرِج [`function_declarations`](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar#function-declarations) مع الأدوات المضمّنة التي تريد استخدامها لتفعيل السلوك المجمّع.

### الخطوات التي تعرضها واجهة برمجة التطبيقات

في ردّ التفاعل، تعرض واجهة برمجة التطبيقات خطوات منفصلة لطلبات البيانات من الأدوات المضمّنة وطلبات البيانات من الدوال (الأدوات المخصّصة):

- **خطوات الأداة المضمّنة**: تدير واجهة برمجة التطبيقات هذه الخطوات تلقائيًا، مع الحفاظ على السياق في كل خطوة.
- **خطوات استدعاء الدوال**: تعرض واجهة برمجة التطبيقات `function_call` خطوة لدوالك المخصّصة. يمكنك تنفيذ الدالة وتقديم النتيجة مرة أخرى.

### الحقول المهمة في الخطوات التي تم عرضها

تُعدّ بعض الحقول في الخطوات التي يتم إرجاعها ضرورية للحفاظ على سياق الأداة وإتاحة استخدام مجموعات من الأدوات:

- **`id`**: تظهر في الخطوتَين `function_call` و`function_response`. معرّف فريد يربط طلبًا بردّه.
- **`signature`**: تظهر في خطوات `thought`، بالإضافة إلى جميع خطوات طلب الأداة (مثل `function_call`) ونتيجتها (مثل `function_response`) لنماذج Gemini 3 والإصدارات الأحدث. يتيح هذا السياق المشفّر **تداول سياق الأداة** في جميع التفاعلات.

**إدارة هذه الحقول:**

- **الوضع ذو الحالة (مُقترَح)**: عند استخدام `previous_interaction_id`، يعالج الخادم تلقائيًا الحقلَين `id` و`signature`.
- **وضع عدم الاحتفاظ بالحالة**: عند إدارة سجلّ المحادثات يدويًا، يجب التأكّد من إعادة تمرير الحقلَين `id` و`signature` إلى النموذج في الطلبات اللاحقة للتحقّق من صحة البيانات والحفاظ على السياق. تتعامل حِزم SDK الرسمية مع ذلك تلقائيًا إذا أرسلت عنصر الردّ الكامل إلى السجلّ.

### البيانات الخاصة بالأداة

تعرض بعض الأدوات المضمّنة وسيطات بيانات مرئية للمستخدم خاصة بنوع الأداة.

| الأداة | وسيطات استدعاء الأداة المرئية للمستخدم (إن وُجدت) | ردّ الأداة المرئي للمستخدم (إن وُجد) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` عناوين URL التي سيتم تصفّحها | ‫`status`: حالة التصفّح `retrieved_url`: عناوين URL التي تم تصفّحها |
| **file\_search** | بدون | بدون |

## الرموز المميزة والأسعار

يُرجى العِلم أنّ أجزاء طلبات استدعاء الأدوات المضمّنة يتم احتسابها ضمن
`prompt_token_count`. بما أنّ خطوات الأدوات الوسيطة هذه أصبحت مرئية
ويتم إرجاعها إليك، فهي تشكّل جزءًا من سجلّ المحادثات. ينطبق ذلك على *الطلبات* فقط، وليس على *الردود*.

تُستثنى أداة "بحث Google" من هذه القاعدة. يستخدم محرّك بحث Google نموذج التسعير الخاص به على مستوى طلب البحث، لذا لن يتم تحصيل رسوم مضاعفة مقابل الرموز المميزة (راجِع صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)).

يمكنك الاطّلاع على صفحة [الرموز المميزة](https://ai.google.dev/gemini-api/docs/interactions/tokens?hl=ar) للحصول على مزيد من المعلومات.

## القيود

- يتم ضبط الوضع التلقائي على `validated` (الوضع `auto` غير متاح) عند تفعيل ميزة "تداول سياق الأداة".
- تعتمد الأدوات المضمّنة، مثل `google_search`، على معلومات الموقع الجغرافي والوقت الحالي، لذا إذا كان `system_instruction` أو `function_declaration.description` يتضمّن معلومات متضاربة حول الموقع الجغرافي والوقت، قد لا تعمل ميزة دمج الأدوات بشكل جيد.

## الأدوات المتوافقة

يتم تطبيق تداول سياق الأداة العادي على الأدوات من جهة الخادم (المضمّنة).
&quot;تنفيذ التعليمات البرمجية&quot; هي أيضًا أداة من جهة الخادم، ولكنّها تتضمّن حلاً مدمجًا خاصًا بها لتداول السياق. إنّ استخدام الكمبيوتر واستدعاء الدوال هما أداتان من جهة العميل،
وتتضمّنان أيضًا حلولاً مدمجة لتداول السياق.

| الأداة | جهة التنفيذ | إتاحة تداول السياق |
| --- | --- | --- |
| [بحث Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar) | من جهة الخادم | متاح |
| [خرائط Google](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ar) | من جهة الخادم | متاح |
| [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar) | من جهة الخادم | متاح |
| [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ar) | من جهة الخادم | متاح |
| [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar) | من جهة الخادم | متوافق (مضمّن، يستخدم الخطوتَين `code_execution` و`code_execution_result`) |
| [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=ar) | من جهة العميل | متوافق (مضمّن، يستخدم الخطوتَين `function_call` و`function_response`) |
| [الدوال المخصّصة](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar) | من جهة العميل | متوافق (مضمّن، يستخدم الخطوتَين `function_call` و`function_response`) |

## الخطوات التالية

- [مزيد من المعلومات حول ميزة "استدعاء الدوال"](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar) في Gemini API
- استكشاف الأدوات المتوافقة:
  - [بحث Google](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar)
  - [خرائط Google](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=ar)
  - [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar)
  - [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-19 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
