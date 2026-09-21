---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=ar
fetched_at: 2026-09-21T05:50:28.340469+00:00
title: "\u0627\u0644\u0628\u062f\u0621 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البدء

يساعدك هذا الدليل في بدء استخدام Gemini API من خلال [واجهة Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar). ستُجري أول طلب بيانات من واجهة برمجة التطبيقات في أقل من دقيقة، وستستكشف ميزات فهم المحتوى المتعدّد الوسائط، وإنشاء الصور، والناتج المنظَّم، والأدوات، واستدعاء الدوال، والوكلاء، والتنفيذ في الخلفية.

تتوفّر واجهة Interactions API من خلال حزمتَي تطوير البرامج (SDK) [Python](https://github.com/googleapis/python-genai) و[JavaScript](https://github.com/googleapis/js-genai)، بالإضافة إلى REST.

## 1. الحصول على مفتاح واجهة برمجة تطبيقات

لاستخدام Gemini API، يجب أن يكون لديك مفتاح واجهة برمجة تطبيقات للمصادقة على طلباتك وفرض حدود الأمان وتتبُّع الاستخدام في حسابك.

- ينشئ Google AI Studio تلقائيًا مشروعًا ومفتاح واجهة برمجة تطبيقات للمستخدمين الجدد.
  يمكنك نسخه من [صفحة مفاتيح واجهة برمجة التطبيقات](https://aistudio.google.com/api-keys?hl=ar).
- إذا كنت بحاجة إلى مفتاح جديد، انقر على **إنشاء مفتاح واجهة برمجة تطبيقات** في AI Studio واتّبِع مربع الحوار لإضافة زوج جديد من المفتاح والمشروع.

[إنشاء مفتاح Gemini API](https://aistudio.google.com/apikey?hl=ar)

اضبط مفتاحك كمتغيّر بيئة:

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

### الترقية إلى الفئة المدفوعة

تؤدي الترقية إلى الفئة المدفوعة إلى زيادة حدود معدّل الطلبات وتتطلّب إعداد Cloud Billing.

- انقر على **إعداد الفوترة** في صفحة [مفاتيح واجهة برمجة التطبيقات](https://aistudio.google.com/api-keys?hl=ar) أو [المشاريع](https://aistudio.google.com/projects?hl=ar) في AI Studio.
- اتّبِع تعليمات مربّع الحوار "الفوترة في Cloud" لإنشاء حساب فوترة أو ربطه، وإضافة طريقة دفع، ودفع مبلغ مسبق لا يقل عن 5 دولار أمريكي (أو ما يعادله بالعملة المحلية) في شكل أرصدة مدفوعة.
- يمكنك الاطّلاع على استخدامك لواجهة برمجة التطبيقات في [Google AI Studio](https://aistudio.google.com/usage?hl=ar)
  ضمن **لوحة البيانات** > **الاستخدام**.

لمزيد من المعلومات، يُرجى الاطّلاع على [صفحة الفوترة](https://ai.google.dev/gemini-api/docs/billing?hl=ar).

## 2. تثبيت حزمة تطوير البرامج (SDK) وإجراء مكالمتك الأولى

ثبِّت حزمة تطوير البرامج (SDK) وأنشئ نصًا من خلال طلب واحد من واجهة برمجة التطبيقات.

### Python

ثبِّت حزمة تطوير البرامج (SDK) باتّباع الخطوات التالية:

```
pip install -U google-genai
```

إعداد العميل وإرسال طلب:

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

ثبِّت حزمة تطوير البرامج (SDK) باتّباع الخطوات التالية:

```
npm install @google/genai
```

إعداد العميل وإرسال طلب:

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works in a few words",
});
console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few words"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

**الردّ:**

```
{
  "id": "v1_ChdpQUFvYXI...",
  "status": "completed",
  "usage": {
    "total_tokens": 197,
    "total_input_tokens": 8,
    "total_output_tokens": 12
  },
  "created": "2026-06-09T12:01:25Z",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4FAQw..."
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "AI learns patterns from data, then uses those patterns to make predictions or decisions on new data."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

عند استخدام REST، تعرض واجهة برمجة التطبيقات مورد `Interaction` الكامل الذي يحتوي على البيانات الوصفية وإحصاءات الاستخدام وسجلّ الخطوات التفصيلية للرد.

في حين تعرض حِزم تطوير البرامج (SDK) الرد الكامل، فإنّها توفّر أيضًا خصائص ملائمة، مثل `interaction.output_text` و`interaction.output_image`، للوصول إلى النتائج النهائية مباشرةً. يمكنك الاطّلاع على مزيد من المعلومات حول بنية الرد في [نظرة عامة على التفاعلات](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) أو قراءة [دليل إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar) للحصول على تفاصيل حول تعليمات النظام وإعدادات الإنشاء.

## 3- عرض الرد تدريجيًا

للحصول على تفاعلات أكثر سلاسة، يمكنك بث الردّ أثناء إنشائه. يقدّم كل حدث `step.delta` جزءًا من النص يمكنك عرضه على الفور.

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const stream = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Explain how AI works",
  stream: true,
});

for await (const event of stream) {
  console.log(event);
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works"))
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent event : stream) {
    System.out.println(event);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

عند البث، يستجيب الخادم بتدفق أحداث Server-Sent Events (SSE). يتضمّن كل حدث نوعًا وبيانات JSON.

**الردّ:**

```
event: interaction.created
data: {"interaction":{"id":"v1_Chd...","status":"in_progress","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EvEFCu4F...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":"AI ","type":"text"},"event_type":"step.delta"}

event: step.delta
data: {"index":1,"delta":{"text":"works ","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_Chd...","status":"completed","usage":{"total_tokens":197}},"event_type":"interaction.completed"}
```

لإلقاء نظرة تفصيلية على كيفية التعامل مع أحداث البث وأنواع التغييرات، يُرجى الاطّلاع على [دليل التفاعلات مع البث](https://ai.google.dev/gemini-api/docs/streaming?hl=ar).

## 4. محادثات مترابطة

تتيح Interactions API إجراء محادثات مترابطة بطريقتَين:

- **الاحتفاظ بالحالة (يُنصح به)**: مواصلة محادثة على الخادم باستخدام `previous_interaction_id` خيار مثالي لمعظم عمليات الدردشة وسير العمل بالذكاء الاصطناعي الوكيل التي تريد أن يدير فيها الخادم السجلّ ويحسّن التخزين المؤقت.
- **عدم الاحتفاظ بالحالة**: يمكنك إدارة سجلّ المحادثات على جهاز العميل من خلال تمرير جميع الجوانب السابقة (بما في ذلك خطوات التفكير والأدوات الوسيطة للنموذج) في كل طلب.

### حالة مستمرة (مُقترَحة)

يمكنك ربط التفاعلات من خلال تمرير `previous_interaction_id`. يتولّى الخادم إدارة سجلّ المحادثات الكامل نيابةً عنك.

### Python

```
from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Server-side state (recommended)
const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "I have 2 dogs in my house.",
});
console.log("Response 1:", interaction1.output_text);

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "How many paws are in my house?",
  previous_interaction_id: interaction1.id,
});
console.log("Response 2:", interaction2.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// Server-side state (recommended)
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("I have 2 dogs in my house."))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("How many paws are in my house?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
echo "Interaction 1 ID: $INTERACTION_ID"

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

### بلا حالة

ضبط `store=false` وإدارة سجلّ المحادثات من جهة العميل يجب الاحتفاظ بجميع الخطوات التي تم إنشاؤها بواسطة النموذج (بما في ذلك الخطوتان `thought` و`function_call`) وإعادة إرسالها تمامًا كما تم استلامها.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "I have 2 dogs in my house." }]
  }
];

const interaction1 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

history.push(...interaction1.steps);

history.push({
  type: "user_input",
  content: [{ type: "text", text: "How many paws are in my house?" }]
});

const interaction2 = await ai.interactions.create({
  model: "gemini-3.8-flash",
  store: false,
  input: history
});
console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("I have 2 dogs in my house.").build()))
        .build());

CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println("Response 1: " + interaction1.outputText().orElse(""));

interaction1.steps().ifPresent(history::addAll);

history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("How many paws are in my house?").build()))
        .build());

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .store(false)
        .input(InteractionsInput.ofStep(history))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();
System.out.println("Response 2: " + interaction2.outputText().orElse(""));
```

### REST

```
# Turn 1: Send with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Turn 2: Build full history
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  '$first_input + $model_steps + $second_input')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

**الردّ:**

```
{
  "id": "v2_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 240,
    "total_input_tokens": 60,
    "total_output_tokens": 20
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "There are 8 paws in your house. 2 dogs \u00d7 4 paws = 8 paws."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

تعرض التفاعلات الثانية كائن استجابة كاملاً يتضمّن الخطوات الجديدة فقط، ولكنّه يستند إلى سياق المحادثة السابقة. يمكنك الاطّلاع على مزيد من المعلومات حول الحفاظ على الحالة في [دليل المحادثات المترابطة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#multi-turn-conversations)، أو استكشاف [الوضع غير الاحتفاظ بالحالة](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#stateless-conversations) لإدارة السجلّ من جهة العميل.

## 5- فهم المحتوى المتعدّد الوسائط

تستطيع نماذج Gemini فهم الصور والمحتوى الصوتي والفيديوهات والمستندات بشكلٍ مباشر. تمرير الوسائط إلى جانب النص في طلب واحد

### Python

```
import base64
from google import genai

client = genai.Client()

# Load a local image
with open("sample.jpg", "rb") as f:
    image_bytes = f.read()
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Compare this local image and this remote audio file."},
        {
            "type": "image",
            "data": image_b64,
            "mime_type": "image/jpeg"
        },
        {
            "type": "audio",
            "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
            "mime_type": "audio/mp3"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import fs from "fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Load a local image
const imageBytes = fs.readFileSync("sample.jpg");
const imageB64 = imageBytes.toString("base64");

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Compare this local image and this remote audio file." },
    {
      type: "image",
      data: imageB64,
      mime_type: "image/jpeg"
    },
    {
      type: "audio",
      uri: "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
      mime_type: "audio/mp3"
    }
  ],
});
console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AudioContent;
import com.google.genai.gaos.models.interactions.AudioContentMimeType;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Base64;

Client client = new Client();

// Load a local image
byte[] imageBytes = Files.readAllBytes(Path.of("sample.jpg"));
String imageB64 = Base64.getEncoder().encodeToString(imageBytes);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder()
                        .text("Compare this local image and this remote audio file.")
                        .build(),
                    ImageContent.builder()
                        .data(imageB64)
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .build(),
                    AudioContent.builder()
                        .uri("https://storage.googleapis.com/generativeai-downloads/data/sample.mp3")
                        .mimeType(AudioContentMimeType.AUDIO_MP3)
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Base64-encode local image
BASE64_IMAGE=$(base64 -w 0 sample.jpg)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions"   -H "x-goog-api-key: $GEMINI_API_KEY"   -H 'Content-Type: application/json'   -H "Api-Revision: 2026-05-20"   -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "text",
        "text": "Compare this local image and this remote audio file."
      },
      {
        "type": "image",
        "data": "'$BASE64_IMAGE'",
        "mime_type": "image/jpeg"
      },
      {
        "type": "audio",
        "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.mp3",
        "mime_type": "audio/mp3"
      }
    ]
  }'
```

**الردّ:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "usage": {
    "total_tokens": 300
  },
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The local image displays a pipe organ while the remote audio file is a sample MP3 clip..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

يمكنك الاطّلاع على كيفية تمرير الصور والفيديوهات والملفات الصوتية في [دليل فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar).

[hearing

فهم الصوت

تحويل الملفات الصوتية إلى نص أو تلخيصها أو الإجابة عن أسئلة بشأنها](https://ai.google.dev/gemini-api/docs/audio?hl=ar)
[videocam

فهم الفيديوهات

تحليل محتوى الفيديو وتحديد الأحداث ووصف الإجراءات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)
[description

معالجة المستندات

استخراج المعلومات من ملفات PDF وتنسيقات المستندات الأخرى](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar)

## 6. إنشاء محتوى متعدد الوسائط

يمكن لـ Gemini إنشاء الصور بشكلٍ أصلي باستخدام نماذج الصور [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-image",
    input="Generate an image of a futuristic city skyline at sunset",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-image",
  input: "Generate an image of a futuristic city skyline at sunset",
});

const generatedImage = interaction.output_image;
if (generatedImage) {
  const buffer = Buffer.from(generatedImage.data, "base64");
  fs.writeFileSync("generated_image.png", buffer);
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Base64;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.1-flash-image"))
        .input(InteractionsInput.of("Generate an image of a futuristic city skyline at sunset"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.outputImage().isPresent()) {
  ImageContent generatedImage = interaction.outputImage().get();
  if (generatedImage.data().isPresent()) {
    byte[] imageBytes = Base64.getDecoder().decode(generatedImage.data().get());
    Files.write(Path.of("generated_image.png"), imageBytes);
  }
}
```

### REST

```
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-flash-image",
    "input": [
      {"type": "text", "text": "Generate an image of a futuristic city skyline at sunset"}
    ]
  }'
```

**الردّ:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "image",
          "data": "BASE64_ENCODED_IMAGE",
          "mime_type": "image/png"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.1-flash-image",
}
```

عندما ينشئ النموذج صورة، يعرض بيانات الصورة المشفّرة بتنسيق base64 في خطوة ضمن مصفوفة `steps`، وكذلك من خلال السمة `output_image`. اطّلِع على [دليل إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar) للتعرّف على نسب العرض إلى الارتفاع وتعديل الصور والمراجع.

[record\_voice\_over

إنشاء الكلام

إنشاء كلام معبّر ومتعدد المتحدثين باستخدام تكنولوجيا تحويل النص إلى كلام في Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/speech-generation?hl=ar)
[music\_note

إنشاء الموسيقى

يمكنك إنشاء مقاطع وأغانٍ كاملة باستخدام Lyria 3.5.](https://ai.google.dev/gemini-api/docs/music-generation?hl=ar)

## 7. استخدام ناتج منظَّم

اضبط النموذج لعرض JSON يطابق مخططًا تحدّده. تعمل المخرجات المنظَّمة مع [Pydantic](https://docs.pydantic.dev/latest/) (بايثون) و[Zod](https://zod.dev/) (جافاسكريبت).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    recipe_name: str = Field(description="Name of the recipe.")
    ingredients: List[str] = Field(description="List of ingredients.")
    prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Give me a recipe for banana bread",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Recipe.model_json_schema()
    },
)

recipe = Recipe.model_validate_json(interaction.output_text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const ai = new GoogleGenAI({});

const recipeJsonSchema = {
  type: "object",
  properties: {
    recipe_name: { type: "string", description: "Name of the recipe." },
    ingredients: {
      type: "array",
      items: { type: "string" },
      description: "List of ingredients."
    },
    prep_time_minutes: {
      type: "integer",
      description: "Prep time in minutes."
    }
  },
  required: ["recipe_name", "ingredients"]
};

const recipeSchema = z.fromJSONSchema(recipeJsonSchema);

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Give me a recipe for banana bread",
  response_format: {
    type: "text",
    mime_type: "application/json",
    schema: recipeJsonSchema
  },
});

const recipe = recipeSchema.parse(JSON.parse(interaction.output_text));
console.log(recipe);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.CreateModelInteractionResponseFormat;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormat;
import com.google.genai.gaos.models.interactions.TextResponseFormatMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> recipeNameProp = new HashMap<>();
recipeNameProp.put("type", "string");
recipeNameProp.put("description", "Name of the recipe.");

Map<String, Object> itemsProp = new HashMap<>();
itemsProp.put("type", "string");

Map<String, Object> ingredientsProp = new HashMap<>();
ingredientsProp.put("type", "array");
ingredientsProp.put("items", itemsProp);
ingredientsProp.put("description", "List of ingredients.");

Map<String, Object> prepTimeProp = new HashMap<>();
prepTimeProp.put("type", "integer");
prepTimeProp.put("description", "Prep time in minutes.");

Map<String, Object> properties = new HashMap<>();
properties.put("recipe_name", recipeNameProp);
properties.put("ingredients", ingredientsProp);
properties.put("prep_time_minutes", prepTimeProp);

Map<String, Object> recipeJsonSchema = new HashMap<>();
recipeJsonSchema.put("type", "object");
recipeJsonSchema.put("properties", properties);
recipeJsonSchema.put("required", Arrays.asList("recipe_name", "ingredients"));

CreateModelInteractionResponseFormat format =
    CreateModelInteractionResponseFormat.of(
        ResponseFormat.of(
            TextResponseFormat.builder()
                .mimeType(TextResponseFormatMimeType.APPLICATION_JSON)
                .schema(recipeJsonSchema)
                .build()));

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Give me a recipe for banana bread"))
        .responseFormat(format)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Give me a recipe for banana bread",
    "response_format": {
      "type": "text",
      "mime_type": "application/json",
      "schema": {
        "type": "object",
        "properties": {
          "recipe_name": { "type": "string", "description": "Name of the recipe." },
          "ingredients": {
            "type": "array",
            "items": { "type": "string" },
            "description": "List of ingredients."
          },
          "prep_time_minutes": {
            "type": "integer",
            "description": "Prep time in minutes."
          }
        },
        "required": ["recipe_name", "ingredients"]
      }
    }
  }'
```

**الردّ:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"recipe_name\": \"Classic Banana Bread\",\n  \"ingredients\": [\n    \"3 ripe bananas, mashed\",\n    \"1/3 cup melted butter\",\n    \"3/4 cup sugar\",\n    \"1 egg, beaten\",\n    \"1 teaspoon vanilla extract\",\n    \"1 teaspoon baking soda\",\n    \"Pinch of salt\",\n    \"1.5 cups all-purpose flour\"\n  ],\n  \"prep_time_minutes\": 15\n}"
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

يحتوي قسم النص الناتج على سلسلة JSON صالحة تتوافق تمامًا مع المخطط المطلوب. لمعرفة كيفية تحديد بنى أكثر تعقيدًا ومخططات متكررة، يُرجى الاطّلاع على [دليل الإخراج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar).

## 8. استخدام الأدوات

تحديد مصدر ردّ النموذج من خلال معلومات في الوقت الفعلي باستخدام "بحث Google" تبحث واجهة برمجة التطبيقات تلقائيًا عن الاقتباسات وتعالج النتائج وتعرضها.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

# Print citations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  [{annotation.title}]({annotation.url})")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Who won the euro 2024?",
  tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);

// Print citations
for (const step of interaction.steps) {
  if (step.type === "model_output") {
    for (const contentBlock of step.content) {
      if (contentBlock.type === "text" && contentBlock.annotations) {
        console.log("\nCitations:");
        for (const annotation of contentBlock.annotations) {
          if (annotation.type === "url_citation") {
            console.log(`  [${annotation.title}](${annotation.url})`);
          }
        }
      }
    }
  }
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.URLCitation;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Who won the euro 2024?"))
        .tools(Arrays.asList(new GoogleSearch()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));

// Print citations
for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent && textContent.annotations().isPresent()) {
        System.out.println("\nCitations:");
        for (Annotation annotation : textContent.annotations().get()) {
          if (annotation instanceof URLCitation citation) {
            System.out.printf("  [%s](%s)%n", citation.title().orElse(""), citation.url().orElse(""));
          }
        }
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

**الردّ:**

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "thought",
      "signature": "EvEFCu4F..."
    },
    {
      "type": "google_search_call",
      "arguments": {
        "queries": ["UEFA Euro 2024 winner"]
      }
    },
    {
      "type": "google_search_result",
      "call_id": "search_001",
      "result": [
        {
          "search_suggestions": "<!-- HTML and CSS search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024",
              "title": "uefa.com",
              "start_index": 0,
              "end_index": 56
            }
          ]
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

يتم تفصيل خطوات البحث ضمن سجلّ التفاعل، ويتضمّن الناتج النهائي اقتباسات مضمّنة تشير إلى مصادر الويب.

يمكنك التعرّف على كيفية استخراج الاقتباسات من نتائج البحث في [دليل التأسيس في "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)، أو الاطّلاع على كيفية دمج أدوات متعددة في [دليل دمج الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

[code

تنفيذ الرموز البرمجية

تشغيل رمز Python البرمجي في بيئة Borg آمنة ومحمية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)
[link

سياق عناوين URL

تمرير عناوين URL الخاصة بالويب المتاحة للجميع مباشرةً لتأسيس الردود على محتوى صفحات الويب](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)
[search

البحث عن ملف

فهرسة المستندات وملفات الوسائط التي تم تحميلها والبحث فيها](https://ai.google.dev/gemini-api/docs/file-search?hl=ar)
[map

خرائط Google

تستند الردود إلى بيانات جغرافية مكانية وبيانات مواقع جغرافية من العالم الواقعي.](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar)
[computer

استخدام الكمبيوتر

التفاعل الآلي مع المتصفّح والشاشة](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar)

## 9. استدعاء الدوال الخاصة بك

تتيح لك ميزة "استدعاء الدوال" ربط النموذج بالرمز البرمجي. عليك تحديد اسم الدالة ومَعلماتها، ويقرّر النموذج وقت استدعائها ويعرض وسيطات منظَّمة، ثم تنفّذها محليًا وتعيد النتيجة.

### حالة مستمرة (مُقترَحة)

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

user_input = "What is the temperature in London?"
previous_id = None

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=user_input,
        tools=[weather_tool],
        previous_interaction_id=previous_id,
    )

    function_results = []
    for step in interaction.steps:
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            })

    if not function_results:
        break

    user_input = function_results
    previous_id = interaction.id

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

let input = "What is the temperature in London?";
let previousId = null;
let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input,
    tools: [weatherTool],
    previous_interaction_id: previousId,
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      functionResults.push({
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      });
    }
  }

  if (functionResults.length === 0) break;

  input = functionResults;
  previousId = interaction.id;
}

console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

InteractionsInput userInput = InteractionsInput.of("What is the temperature in London?");
String previousId = null;
Interaction interaction = null;

while (true) {
  CreateModelInteraction.Builder paramsBuilder =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(userInput)
          .tools(Arrays.asList(weatherTool));
  if (previousId != null) {
    paramsBuilder.previousInteractionId(previousId);
  }

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(paramsBuilder.build())).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      functionResults.add(
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build());
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }

  userInput = InteractionsInput.ofStep(functionResults);
  previousId = interaction.id().orElse(null);
}

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Turn 1: Send prompt with function declaration
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Turn 2: Send function result back
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "input": [{
      "type": "function_result",
      "name": "'$FC_NAME'",
      "call_id": "'$FC_ID'",
      "result": [{"type": "text", "text": "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"}]
    }],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### بلا حالة

يمكنك أيضًا استخدام ميزة "استدعاء الدوال" في الوضع غير الاحتفاظ بالحالة من خلال إدارة سجلّ المحادثات من جهة العميل وتعيين `store=false`. في الوضع غير المرتبط بحالة، يجب تمرير السجلّ الكامل للمحادثة في الحقل `input` لكل طلب لاحق. يجب أن يتضمّن هذا السجلّ ما يلي:

1. الخطوة `user_input` الأولية
2. جميع الخطوات التي أنشأها النموذج والتي تم عرضها في الجولة الأولى (بما في ذلك الخطوتان `thought` و`function_call`) كما تم تلقّيها تمامًا
3. الخطوة `function_result` التي تحتوي على ناتج الدالة التي تم تنفيذها

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

available_functions = {
    "get_current_temperature": lambda location: {
        "location": location, "temperature": "22", "unit": "celsius"
    },
}

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "What is the temperature in London?"}]
    }
]

while True:
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        store=False,
        input=history,
        tools=[weather_tool],
    )

    function_results = []
    for step in interaction.steps:
        history.append(step.model_dump())
        if step.type == "function_call":
            result = available_functions[step.name](**step.arguments)
            print(f"Called {step.name}({step.arguments}) → {result}")
            fn_result = {
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}],
            }
            function_results.append(fn_result)
            history.append(fn_result)

    if not function_results:
        break

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const weatherTool = {
  type: "function",
  name: "get_current_temperature",
  description: "Gets the current temperature for a given location.",
  parameters: {
    type: "object",
    properties: {
      location: {
        type: "string",
        description: "The city name, e.g. San Francisco",
      },
    },
    required: ["location"],
  },
};

const availableFunctions = {
  get_current_temperature: ({ location }) => ({
    location, temperature: "22", unit: "celsius"
  }),
};

const history = [
  {
    type: "user_input",
    content: [{ type: "text", text: "What is the temperature in London?" }]
  }
];

let interaction;

while (true) {
  interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    store: false,
    input: history,
    tools: [weatherTool],
  });

  const functionResults = [];
  for (const step of interaction.steps) {
    history.push(step);
    if (step.type === "function_call") {
      const result = availableFunctions[step.name](step.arguments);
      console.log(`Called ${step.name}(${JSON.stringify(step.arguments)}) →`, result);
      const fnResult = {
        type: "function_result",
        name: step.name,
        call_id: step.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      };
      functionResults.push(fnResult);
      history.push(fnResult);
    }
  }

  if (functionResults.length === 0) break;
}

console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.UserInputStep;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

Client client = new Client();

Map<String, Object> locationProp = new HashMap<>();
locationProp.put("type", "string");
locationProp.put("description", "The city name, e.g. San Francisco");

Map<String, Object> properties = new HashMap<>();
properties.put("location", locationProp);

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");
parameters.put("properties", properties);
parameters.put("required", Arrays.asList("location"));

Function weatherTool =
    Function.builder()
        .name("get_current_temperature")
        .description("Gets the current temperature for a given location.")
        .parameters(parameters)
        .build();

List<Step> history = new ArrayList<>();
history.add(
    UserInputStep.builder()
        .content(Arrays.asList(TextContent.builder().text("What is the temperature in London?").build()))
        .build());

Interaction interaction = null;

while (true) {
  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .store(false)
          .input(InteractionsInput.ofStep(history))
          .tools(Arrays.asList(weatherTool))
          .build();

  interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

  List<Step> functionResults = new ArrayList<>();
  for (Step step : interaction.steps().orElse(Collections.emptyList())) {
    history.add(step);
    if (step instanceof FunctionCallStep fcStep) {
      String resultJson = "{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}";
      System.out.printf(
          "Called %s(%s) -> %s%n",
          fcStep.name().orElse(""), fcStep.arguments().orElse(Collections.emptyMap()), resultJson);
      FunctionResultStep fnResult =
          FunctionResultStep.builder()
              .name(fcStep.name().orElse(""))
              .callId(fcStep.id().orElse(""))
              .result(
                  FunctionResultStepResultUnion.of(
                      Arrays.asList(TextContent.builder().text(resultJson).build())))
              .build();
      functionResults.add(fnResult);
      history.add(fnResult);
    }
  }

  if (functionResults.isEmpty()) {
    break;
  }
}

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "What is the temperature in London?"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')
echo "Function: $FC_NAME, Call ID: $FC_ID"

# Assume local execution returns:
RESULT="{\"location\": \"London\", \"temperature\": \"22\", \"unit\": \"celsius\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "What is the temperature in London?"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.8-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"get_current_temperature\",
      \"description\": \"Gets the current temperature for a given location.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"location\": {\"type\": \"string\", \"description\": \"The city name\"}
        },
        \"required\": [\"location\"]
      }
    }]
  }"
```

**الردّ:**

خلال الجولة الأولى، يعرض النموذج ردًا بالحالة `requires_action` والخطوة `function_call`:

```
{
  "id": "v1_Chd...",
  "status": "requires_action",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

بعد تشغيل الدالة محليًا وإرسال النتيجة (الجولة 2)، يعرض التفاعل النهائي المكتمل ما يلي:

```
{
  "id": "v1_Chd...",
  "status": "completed",
  "steps": [
    {
      "type": "function_call",
      "id": "call_abc123",
      "name": "get_current_temperature",
      "arguments": {
        "location": "London"
      }
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The temperature in London is currently 22°C."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

للحصول على ميزات متقدّمة، مثل استدعاء الدوال المتوازية أو أوضاع اختيار الدوال، يمكنك الاطّلاع على [دليل استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).

## 10. تشغيل وكيل مُدار

تعمل البرامج الوسيطة المُدارة في بيئة اختبار معزولة عن بُعد مع إمكانية الوصول إلى أدوات مثل تنفيذ الرموز البرمجية وإدارة الملفات. مرِّر `agent` بدلاً من `model` واضبط `environment="remote"`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)
print(f"Environment: {interaction.environment_id}")
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
  environment: "remote",
});
console.log(`Environment: ${interaction.environment_id}`);
console.log(interaction.output_text);
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params =
    CreateAgentInteraction.builder()
        .agent("antigravity-preview-09-2026")
        .input(
            InteractionsInput.of(
                "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."))
        .environment(CreateAgentInteractionEnvironment.of("remote"))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment: " + interaction.environmentId().orElse(""));
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    "environment": "remote"
  }'
```

يمكنك أيضًا تحديد [عملاء مخصّصين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar) وحفظهم مع تعليماتك ومهاراتك ومصادر البيانات الخاصة بك.

[rocket\_launch

البدء السريع

يمكنك إجراء مكالمة مع وكيلك الأول، وبث الردود، وإنشاء وكيل مخصّص.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar)
[smart\_toy

وكيل Antigravity

الإمكانات والأدوات والإدخال المتعدد الوسائط والأسعار للوكيل التلقائي](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar)
[experiment

الوكلاء في AI Studio

مساحة تجريبية مرئية لإنشاء نماذج أوّلية للوكلاء بدون كتابة رموز برمجية](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=ar)

## 11. تنفيذ المهام في الخلفية

اضبط `background=True` لتنفيذ المهام الطويلة بشكل غير متزامن. استطلاع حول النتائج التي تتضمّن `interactions.get()` لمزيد من التفاصيل، يُرجى الاطّلاع على [دليل التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar).

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    background=True,
)
print(f"Started background task: {interaction.id}")
print(f"Status: {interaction.status}")

# Poll for completion
while True:
    result = client.interactions.get(interaction.id)
    print(f"Status: {result.status}")
    if result.status == "completed":
        print(f"\nResult:\n{result.output_text}")
        break
    elif result.status == "failed":
        print(f"Failed: {result.error}")
        break
    time.sleep(5)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
  background: true,
});
console.log(`Started background task: ${interaction.id}`);
console.log(`Status: ${interaction.status}`);

// Poll for completion
while (true) {
  const result = await ai.interactions.get(interaction.id);
  console.log(`Status: ${result.status}`);
  if (result.status === "completed") {
    console.log(`\nResult:\n${result.output_text}`);
    break;
  } else if (result.status === "failed") {
    console.log(`Failed: ${result.error}`);
    break;
  }
  await new Promise(r => setTimeout(r, 5000));
}
```

### جافا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Write a detailed analysis of the impact of artificial intelligence on modern healthcare."))
        .background(true)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
String interactionId = interaction.id().orElse("");
System.out.println("Started background task: " + interactionId);
System.out.println("Status: " + interaction.status().map(InteractionStatus::value).orElse(""));

// Poll for completion
while (true) {
  Interaction result =
      client.interactions.get(new GetInteractionByIdRequest(interactionId)).interaction().get();
  String status = result.status().map(InteractionStatus::value).orElse("");
  System.out.println("Status: " + status);
  if ("completed".equals(status)) {
    System.out.println("\nResult:\n" + result.outputText().orElse(""));
    break;
  } else if ("failed".equals(status)) {
    System.out.println("Failed: " + result.errors().orElse(null));
    break;
  }
  Thread.sleep(5000);
}
```

### REST

```
# Start a background task
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Write a detailed analysis of the impact of artificial intelligence on modern healthcare.",
    "background": true
  }')

INTERACTION_ID=$(echo "$RESPONSE" | jq -r '.id')
echo "Started background task: $INTERACTION_ID"

# Poll for completion
while true; do
  RESULT=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Api-Revision: 2026-05-20")
  STATUS=$(echo "$RESULT" | jq -r '.status')
  echo "Status: $STATUS"
  if [ "$STATUS" = "completed" ]; then
    echo "$RESULT" | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="text") | .text'
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "Failed"
    break
  fi
  sleep 5
done
```

**الردّ:**

يتم عرض الردّ الأوّلي على الفور مع الحالة `in_progress`:

```
{
  "id": "v1_abc123",
  "status": "in_progress",
  "object": "interaction",
  "model": "gemini-3.8-flash"
}
```

بعد تنفيذ مهمة الخلفية بالكامل، ستعرض حالة التفاعل ما يلي:

```
{
  "id": "v1_abc123",
  "status": "completed",
  "steps": [
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Artificial intelligence has transformed modern healthcare in several..."
        }
      ]
    }
  ],
  "object": "interaction",
  "model": "gemini-3.8-flash",
}
```

يمكنك الاطّلاع على [دليل التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) لمعرفة المزيد عن تشغيل النماذج والوكلاء بشكل غير متزامن.

## الخطوات التالية

- [التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar): تنفيذ المهام الطويلة المدى بشكل غير متزامن وإدارة الحالة
- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar): تعليمات النظام وإعدادات الإنشاء وأنماط النصوص المتقدّمة
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar): نِسب العرض إلى الارتفاع وتعديل الصور والمراجع المتعلقة بالأنماط
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar): التصنيف ورصد العناصر والأسئلة والأجوبة المرئية
- [التفكير](https://ai.google.dev/gemini-api/docs/thinking?hl=ar): استخدام أسلوب "سلسلة الأفكار" للاستدلال في المهام المعقّدة
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar): أوضاع الدوال المتوازية والتركيبية والمقيّدة
- [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar): التأسيس والاقتباسات واقتراحات البحث
- [الوكلاء المُدارون](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): وكلاء مُعدّون مسبقًا مع إمكانية تنفيذ الرموز البرمجية وإدارة الملفات.
- [‫Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar): بحث مستقل ومتعدّد الخطوات مع التخطيط والتجميع
- [الإخراج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar): مخطّطات JSON، والتعدادات، وتعريفات الأنواع المتكرّرة

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-18 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
