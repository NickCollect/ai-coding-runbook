---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar
fetched_at: 2026-08-03T04:28:07.261671+00:00
title: "\u0627\u0644\u062c\u0645\u0639 \u0628\u064a\u0646 \u0627\u0644\u0623\u062f\u0648\u0627\u062a \u0627\u0644\u0645\u0636\u0645\u0651\u0646\u0629 \u0648\u0627\u0633\u062a\u062f\u0639\u0627\u0621 \u0627\u0644\u062f\u0648\u0627\u0644 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الجمع بين الأدوات المضمّنة واستدعاء الدوال

يتيح Gemini الجمع بين [الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tools?hl=ar)، مثل `google_search`، وميزة [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) (المعروفة أيضًا باسم *الأدوات المخصّصة*) في تفاعل واحد من خلال الاحتفاظ بسجلّ سياق طلبات الأدوات وعرضه. تسمح مجموعات الأدوات المضمّنة والمخصّصة بإنشاء عمليات سير عمل معقّدة ووكيلية، حيث يمكن للنموذج، على سبيل المثال، أن يستند إلى بيانات الويب في الوقت الفعلي قبل استدعاء منطق نشاطك التجاري المحدّد.

في ما يلي مثال يوضّح كيفية تفعيل مجموعات الأدوات المضمّنة والمخصّصة باستخدام `google_search` ودالة مخصّصة `getWeather`:

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
-d '{
  "model": "gemini-3.6-flash",
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

تستخدم نماذج Gemini 3 ميزة *تداول سياق الأداة* لتفعيل مجموعات الأدوات المضمّنة والمخصّصة. تتيح ميزة تداول سياق الأداة الاحتفاظ بسياق الأدوات المضمّنة وعرضه ومشاركته مع الأدوات المخصّصة في التفاعل نفسه.

### تفعيل ميزة الجمع بين الأدوات

- يمكنك تضمين [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#function-declarations)، بالإضافة
  إلى الأدوات المضمّنة التي تريد استخدامها، لتفعيل سلوك الجمع بين الأدوات.

### الخطوات التي تعرضها واجهة برمجة التطبيقات

في ردّ التفاعل، تعرض واجهة برمجة التطبيقات خطوات منفصلة لطلبات الأدوات المضمّنة وطلبات الدوال (الأدوات المخصّصة):

- **خطوات الأداة المضمّنة**: تدير واجهة برمجة التطبيقات هذه الخطوات تلقائيًا، مع الاحتفاظ بـ
  السياق خلال الردود.
- **خطوات استدعاء الدالة**: تعرض واجهة برمجة التطبيقات خطوات `function_call` لدوالك المخصّصة. يمكنك تنفيذ الدالة وتقديم النتيجة مرة أخرى.

### الحقول المهمة في الخطوات المعروضة

تتسم بعض الحقول في الخطوات المعروضة بأهمية بالغة للحفاظ على سياق الأداة وتفعيل مجموعات الأدوات:

- **`id`**: يظهر في خطوات `function_call` و`function_response`. وهو معرّف فريد يربط الطلب بالردّ.
- **`signature`**: يظهر في خطوات `thought`، بالإضافة إلى جميع خطوات طلب الأداة (مثل `function_call`) وخطوات النتيجة (مثل `function_response`) لنماذج Gemini 3 والإصدارات الأحدث. يتيح هذا السياق المشفّر **تداول سياق الأداة** بين التفاعلات.

**إدارة هذه الحقول:**

- **الوضع الذي يحفظ الحالة (يُنصح به)**: عند استخدام `previous_interaction_id`، يعالج الخادم تلقائيًا كلاً من الحقلَين `id` و`signature`.
- **الوضع الذي لا يحفظ الحالة**: عند إدارة سجلّ المحادثات يدويًا، يجب التأكّد من تمرير الحقلَين `id` و`signature` مرة أخرى إلى النموذج في الطلبات اللاحقة للتحقق من صحة المحتوى والحفاظ على السياق. تتعامل حِزم تطوير البرامج الرسمية مع هذه الخطوة تلقائيًا إذا مرّرت عنصر الردّ الكامل مرة أخرى إلى السجلّ.

### البيانات الخاصة بالأداة

تعرض بعض الأدوات المضمّنة وسيطات بيانات مرئية للمستخدم خاصة بنوع الأداة.

| الأداة | وسيطات طلب الأداة المرئية للمستخدم (إن وُجدت) | ردّ الأداة المرئي للمستخدم (إن وُجد) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` عناوين URL التي سيتم تصفّحها | `status`: حالة التصفّح `retrieved_url`: عناوين URL التي تم تصفّحها |
| **file\_search** | بدون | بدون |

## الرموز والأسعار

يُرجى العِلم أنّ أجزاء طلبات الأدوات المضمّنة في الطلبات يتم احتسابها ضمن `prompt_token_count`. بما أنّ خطوات الأداة الوسيطة هذه أصبحت مرئية ومعروضة لك، فهي جزء من سجلّ المحادثات. ينطبق ذلك على *الطلبات* فقط، وليس *الردود*.

تُستثنى أداة "بحث Google" من هذه القاعدة. تطبّق "بحث Google" نموذج التسعير الخاص بها على مستوى طلب البحث، لذا لا يتم تحصيل رسوم مضاعفة على الرموز (راجِع صفحة [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)).

لمزيد من المعلومات، يُرجى قراءة صفحة [الرموز](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

## القيود

- يتم تلقائيًا استخدام وضع `validated` (وضع `auto` غير متاح) عند تفعيل ميزة تداول سياق الأداة.
- تعتمد الأدوات المضمّنة، مثل `google_search`، على معلومات الموقع الجغرافي والوقت الحالي، لذا إذا كانت `system_instruction` أو `function_declaration.description` تتضمّن معلومات متضاربة عن الموقع الجغرافي والوقت، قد لا تعمل ميزة الجمع بين الأدوات بشكل جيد.

## الأدوات المتوافقة

ينطبق تداول سياق الأداة العادي على الأدوات من جهة الخادم (المضمّنة).
تُعدّ ميزة "تنفيذ الرموز البرمجية" أيضًا أداة من جهة الخادم، ولكنها تتضمّن حلاً خاصًا بها لتداول السياق. تُعدّ ميزتا "استخدام الكمبيوتر" و"استدعاء الدوال" أداتَين من جهة العميل، وتتضمّنان أيضًا حلولاً مضمّنة لتداول السياق.

| الأداة | جهة التنفيذ | إتاحة تداول السياق |
| --- | --- | --- |
| [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) | جهة الخادم | متاح |
| [خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) | جهة الخادم | متاح |
| [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) | جهة الخادم | متاح |
| [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) | جهة الخادم | متاح |
| [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) | جهة الخادم | متاح (مضمّن، يستخدم خطوات `code_execution` و`code_execution_result`) |
| [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar) | من جهة العميل | متاح (مضمّن، يستخدم خطوات `function_call` و`function_response`) |
| [الدوال المخصّصة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) | من جهة العميل | متاح (مضمّن، يستخدم خطوات `function_call` و`function_response`) |

## الخطوات التالية

- مزيد من المعلومات عن [ميزة استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) في Gemini API
- استكشاف الأدوات المتوافقة:
  - [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)
  - [خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)
  - [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)
  - [البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
