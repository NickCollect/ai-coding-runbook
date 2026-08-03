---
source_url: https://ai.google.dev/gemini-api/docs/background-execution?hl=ar
fetched_at: 2026-08-03T04:40:14.785792+00:00
title: "\u0627\u0644\u062a\u0646\u0641\u064a\u0630 \u0641\u064a \u0627\u0644\u062e\u0644\u0641\u064a\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# التنفيذ في الخلفية

بالنسبة إلى المهام التي تستغرق وقتًا طويلاً، مثل البحث المعمّق أو الاستدلال المعقّد أو عمليات التنفيذ المتعدّدة الخطوات للوكيل، يمكن أن تؤدي مهلات انتهاء الاتصال إلى مقاطعة طلبات HTTP العادية (التي يتم إغلاقها عادةً بعد 60 ثانية). توفّر [واجهة برمجة التطبيقات Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) ميزة **التنفيذ في الخلفية** لتشغيل هذه المهام بشكل غير متزامن.

للسماح بتنفيذ التفاعل إلى أن يكمل المهمة على الخادم، اضبط `"background": true` عند إنشاء التفاعل. تعرض واجهة برمجة التطبيقات على الفور معرّف تفاعل، ويمكن لتطبيقات العميل استخدامه للتحقّق من الحالة أو تقدّم البث أو إعادة الاتصال ببث تم قطع اتصاله.

تتوفّر ميزة التنفيذ في الخلفية لنماذج Gemini العادية (مثل `gemini-3.6-flash` و`gemini-3.1-pro-preview`) و"الوكلاء المُدارون" (مثل `antigravity-preview-05-2026`).

## إنشاء تفاعل في الخلفية

لبدء تفاعل في الخلفية، اضبط المَعلمة `background` على `true` عند إنشاء المورد.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Write a guide on space exploration.",
    background=True,
)
print(f"Created background interaction ID: {interaction.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Write a guide on space exploration.",
    background: true,
});
console.log(`Created background interaction ID: ${interaction.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Write a guide on space exploration.",
    "background": true
  }'
```

## طريقة عمل التنفيذ في الخلفية

عند إنشاء تفاعل في الخلفية، يتم تنفيذ المهمة بشكل غير متزامن على الخادم. تنتقل عملية التفاعل خلال حالات تنفيذ مختلفة:

- ‫`in_progress`: ينفّذ الخادم التفاعل بشكل نشط (مثل تشغيل الرمز أو البحث).
- `requires_action`: تم إيقاف التفاعل مؤقتًا وينتظر إدخال العميل (مثل تأكيد تنفيذ أداة أو الإجابة عن سؤال).
- `completed`: اكتمل التفاعل بنجاح وأصبح الناتج متاحًا.
- ‫`failed`: حدث خطأ أثناء التنفيذ (مثل تعذُّر استخدام الأداة أو تجاوز حدود المعدّل).
- ‫`cancelled`: أوقف طلب عميل عملية التنفيذ.

### حالات الاستخدام

استخدِم التنفيذ في الخلفية في الحالات التالية:

- **عمليات تنفيذ الوكيل:** المهام التي تتطلّب تطبيق الرموز البرمجية أو تصفّح الويب أو تنسيق الوكلاء الفرعيين (مثل `antigravity-preview-05-2026`).
- **البحث العميق:** يتم تنفيذه باستخدام `deep-research-preview-04-2026` أو `deep-research-max-preview-04-2026`، ويستغرق عدة دقائق.
- **الاستدلال الطويل:** المهام التي تتجاوز فيها خطوات تفكير النموذج حدود اتصال HTTP العادية.

## استرداد النتائج

يمكنك الحصول على نتائج التفاعل في الخلفية باستخدام **الاستقصاء** أو **البث**.

### نمط الاستطلاع (لا يسبب الحظر)

تتحقّق عملية الاقتراع من حالة التفاعل بشكل دوري باستخدام طلبات GET غير الحظر إلى أن تصل إلى حالة نهائية.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.get(id="YOUR_INTERACTION_ID")

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

let interaction = await client.interactions.get("YOUR_INTERACTION_ID");

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

if (interaction.status === "completed") {
    console.log(interaction.output_text);
} else {
    console.log(`Finished with status: ${interaction.status}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

### نمط البث

إذا أدّى انقطاع الشبكة إلى قطع البث، يمكن استئنافه من آخر حدث تم تلقّيه. يحتوي كل تغيير على `event_id` فريد في حمولته. يؤدي تمرير هذا المعرّف كـ `last_event_id` إلى استئناف البث من هذا الحدث.

### Python

```
import time
from google import genai

client = genai.Client()
interaction_id = "YOUR_INTERACTION_ID"

def stream_with_reconnect(interaction_id: str):
    last_event_id = None
    while True:
        try:
            # Retrieve the stream. If resuming, pass last_event_id
            stream = client.interactions.get(
                id=interaction_id,
                stream=True,
                last_event_id=last_event_id
            )

            for event in stream:
                # Log event updates and capture event_id if present
                if event.event_id:
                    last_event_id = event.event_id

                if event.event_type == "step.delta" and event.delta.type == "text":
                    print(event.delta.text, end="", flush=True)

                if event.event_type == "interaction.completed":
                    return

        except Exception as e:
            print(f"\n[Connection lost: {e}. Reconnecting in 3s...]")
            time.sleep(3)

stream_with_reconnect(interaction_id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const interactionId = "YOUR_INTERACTION_ID";

async function streamWithReconnect(id) {
    let lastEventId = undefined;
    while (true) {
        try {
            // Retrieve the stream. If resuming, pass last_event_id in options
            const stream = await client.interactions.get(id, {
                stream: true,
                last_event_id: lastEventId
            });

            for await (const event of stream) {
                // Capture event_id if present
                const idVal = event.event_id || event.id;
                if (idVal) {
                    lastEventId = idVal;
                }

                if (event.event_type === "step.delta" && event.delta?.type === "text") {
                    process.stdout.write(event.delta.text);
                }

                if (event.event_type === "interaction.completed") {
                    return;
                }
            }
        } catch (error) {
            console.log(`\n[Connection lost: ${error.message}. Reconnecting in 3s...]`);
            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }
}

await streamWithReconnect(interactionId);
```

### REST

```
curl -N -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID?stream=true&last_event_id=YOUR_LAST_EVENT_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## محادثات مترابطة

يمكن ربط التفاعلات اللاحقة بمحادثة في الخلفية باستخدام `previous_interaction_id`، مع مراعاة القيود التالية:

1. **يتم حظر عمليات التنفيذ النشطة:** يؤدي ربط تفاعل لاحق بتفاعل يحمل الحالة `in_progress` إلى عرض الخطأ `400 Bad Request`. انتظِر إلى أن يصل التفاعل إلى الحالة `completed` قبل بدء التفاعل التالي.
2. **مَعلمة البيئة الخاصة بـ "الوكلاء المُدارون":** عند ربط التفاعلات بـ "الوكلاء المُدارون" (مثل `antigravity-preview-05-2026`)، يجب أن تتضمّن الطلبات كلاً من `previous_interaction_id` و`environment`.

توضّح الأمثلة التالية كيفية ربط التفاعلات:

### Python

```
import time
from google import genai

client = genai.Client()
agent_model = "antigravity-preview-05-2026"

# First interaction: Provision sandbox environment and execute first instruction
interaction1 = client.interactions.create(
    model=agent_model,
    input="Create a folder named project/ and write hello.py inside.",
    environment="remote",
    background=True
)

# Wait for completion
while True:
    check = client.interactions.get(id=interaction1.id)
    if check.status != "in_progress":
        break
    time.sleep(2)

# Second interaction: Chain using previous_interaction_id and environment
interaction2 = client.interactions.create(
    model=agent_model,
    input="List all files in the project/ directory.",
    previous_interaction_id=interaction1.id,
    environment="remote",
    background=True
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const agentModel = "antigravity-preview-05-2026";

// First interaction: Provision sandbox environment and execute first instruction
const interaction1 = await client.interactions.create({
    model: agentModel,
    input: "Create a folder named project/ and write hello.py inside.",
    environment: "remote",
    background: true
});

// Wait for completion
while (true) {
    const check = await client.interactions.get(interaction1.id);
    if (check.status !== "in_progress") {
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 2000));
}

// Second interaction: Chain using previous_interaction_id and environment
const interaction2 = await client.interactions.create({
    model: agentModel,
    input: "List all files in the project/ directory.",
    previous_interaction_id: interaction1.id,
    environment: "remote",
    background: true
});
```

### REST

```
# Chain second interaction (Make sure FIRST_INTERACTION_ID has status 'completed')
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "antigravity-preview-05-2026",
    "input": "List all files in the project/ directory.",
    "previous_interaction_id": "FIRST_INTERACTION_ID",
    "environment": "remote",
    "background": true
  }'
```

## الإلغاء والحذف

التحكّم في عمليات التنفيذ الجارية وإدارة مساحة التخزين باستخدام طلبات الإلغاء والحذف:

- **إلغاء (`POST /interactions/{id}/cancel`):** لإيقاف المهمة الجارية تتغيّر الحالة إلى `cancelled`. يمكن أن تؤدي إجراءات التنظيف على الخادم إلى تأخير بسيط قبل تعديل الحالة في طلبات GET.
- **حذف (`DELETE /interactions/{id}`):** يؤدي إلى إزالة سجلّات التفاعل من الخادم. تعرض طلبات GET اللاحقة الخطأ `404 Not Found`.

### Python

```
from google import genai

client = genai.Client()

# Cancel a running interaction
client.interactions.cancel(id="YOUR_INTERACTION_ID")

# Delete the interaction record entirely
client.interactions.delete(id="YOUR_INTERACTION_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Cancel a running interaction
await client.interactions.cancel("YOUR_INTERACTION_ID");

// Delete the interaction record entirely
await client.interactions.delete("YOUR_INTERACTION_ID");
```

### REST

```
# Cancel the interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID/cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"

# Delete the interaction
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/interactions/YOUR_INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20"
```

## الخطوات التالية

- اطّلِع على [نظرة عامة على Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) للتعرّف على إدارة الجلسات والحالات.
- راجِع دليل [التفاعلات أثناء البث](https://ai.google.dev/gemini-api/docs/streaming?hl=ar) للاطّلاع على تفاصيل حول آخر الأخبار عن الأحداث في الوقت الفعلي.
- استكشِف [دليل البدء السريع الخاص بالوكلاء المُدارين](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar) لإنشاء وكلاء محادثة مترابطة مع الاحتفاظ بالحالة.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
