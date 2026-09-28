---
source_url: https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar
fetched_at: 2026-09-28T06:32:05.466789+00:00
title: "\u0648\u0627\u062c\u0647\u0629 \u0628\u0631\u0645\u062c\u0629 \u0627\u0644\u062a\u0637\u0628\u064a\u0642\u0627\u062a Interactions API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# واجهة برمجة التطبيقات Interactions API

توفّر Interactions API أفضل طريقة لتصميم التطبيقات باستخدام نماذج Gemini ووكلاء Gemini. اعتبارًا من يونيو 2026، أصبحت هذه الميزة متاحة للجميع ويُنصح باستخدامها في جميع المشاريع الجديدة. على الرغم من أنّ واجهة برمجة التطبيقات الأصلية
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar) أصبحت قديمة،
إلا أنّها لا تزال متوافقة بشكل كامل.

## لماذا يجب استخدام Interactions API؟

- **واجهة عالمية لجميع التطبيقات**: تم تصميمها لتكون الواجهة العادية لكل حالات الاستخدام، بما في ذلك إنشاء النصوص في محادثة واحدة، وفهم الوسائط المتعددة، والنتائج المنظَّمة، وتنظيم الأدوات، وسير العمل المستند إلى الوكلاء.
- **واجهة برمجة تطبيقات واحدة للنماذج والوكلاء**: نقطة نهاية ونمط موحّدان
  لاستدعاء نماذج Gemini العادية والوكلاء المتخصّصين مباشرةً (مثل
  Deep Research والوكلاء المخصّصين المُدارين).
- **إمكانات جديدة جاهزة للاستخدام**: ميزات مثل حالة المحادثة الاختيارية من جهة الخادم باستخدام `previous_interaction_id`، وخطوات التنفيذ القابلة للمراقبة لتصحيح الأخطاء وعرض واجهة المستخدم، و[التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) للمهام الطويلة الأمد باستخدام `background=true`.
- **تكلفة أقل مع معدّلات أعلى لنتيجة ذاكرة التخزين المؤقت**: عند استخدام المحادثات المترابطة، تتيح إدارة الحالة الاختيارية من جهة الخادم تخزينًا مؤقتًا أكثر كفاءة للسياق على مستوى الأدوار، ما يقلّل من تكاليف الرموز المميزة.
- **مكان إطلاق الميزات الجديدة**: من الآن فصاعدًا، سيتم إطلاق جميع النماذج الجديدة والإمكانات والأدوات والميزات المستندة إلى وكيل الذكاء الاصطناعي على Interactions API.

تخزّن Interactions API الطلبات تلقائيًا حتى تتمكّن من الاستفادة من ميزات إدارة الحالة من جهة الخادم باستخدام `previous_interaction_id`. يمكنك تفعيل السلوك غير المرتبط بحالة معيّنة من خلال ضبط
`store=false`. راجِع قسم [الاحتفاظ بالبيانات](#data-storage-retention) لمعرفة التفاصيل.

## البدء

- **إعداد وكيل الترميز**: اربط وكيل الترميز **ببروتوكول MCP الخاص بـ &quot;مستندات Gemini&quot;** وثبِّت مهارة `gemini-api-dev` لمنح مساعدك إذن الوصول المباشر إلى أحدث مستندات المطوّرين وأفضل الممارسات. لمعرفة الخطوات التفصيلية، يُرجى الاطّلاع على
  [دليل إعداد وكيل الترميز](https://ai.google.dev/gemini-api/docs/coding-agents?hl=ar).
- **نقل البيانات من `generateContent`**: إذا كان لديك عملية دمج حالية، اتّبِع [دليل نقل البيانات](https://ai.google.dev/gemini-api/docs/migrate-to-interactions?hl=ar) للانتقال إلى Interactions API.
- **البدء**: اتّبِع الخطوات الواردة في [دليل "بدء استخدام Interactions API"](https://ai.google.dev/gemini-api/docs/get-started?hl=ar).

### أدلة الميزات

يمكنك الاطّلاع على الإمكانات المحدّدة لواجهة برمجة التطبيقات Interactions API من خلال هذه الأدلة. يمكنك استخدام زر التبديل في هذه الصفحات للتبديل بين generateContent وInteractions API:

- [إنشاء النصوص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar)
- [إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar)
- [فهم الصور](https://ai.google.dev/gemini-api/docs/image-understanding?hl=ar)
- [فهم الصوت](https://ai.google.dev/gemini-api/docs/audio?hl=ar)
- [فهم الفيديوهات](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar)
- [معالجة المستندات](https://ai.google.dev/gemini-api/docs/document-processing?hl=ar)
- [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
- [الناتج المنظَّم](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar)
- [وكيل Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)
- [الاستنتاج المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar)
- [استنتاج الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)

## طريقة عمل Interactions API

تتمحور واجهة Interactions API حول مورد أساسي هو [**`Interaction`**](https://ai.google.dev/api/interactions-api?hl=ar#Resource:Interaction). يمثّل `Interaction` دورة كاملة في محادثة أو مهمة. يعمل هذا السجلّ كسجلّ جلسة، ويتضمّن السجلّ الكامل لتفاعل ما كسلسلة زمنية من **خطوات التنفيذ**. تشمل هذه الخطوات أفكار النموذج، ونتائج طلبات الأدوات من جهة الخادم أو العميل (مثل `function_call` و`function_result`)، و`model_output` النهائي. يتضمّن المرجع المخزّن (الذي تم استرجاعه من خلال `interactions.get`) أيضًا خطوات `user_input` للحصول على السياق الكامل، على الرغم من أنّ ردّ `interactions.create` يعرض الخطوات التي أنشأها النموذج فقط.

عند إجراء مكالمة إلى
[`interactions.create`](https://ai.google.dev/api/interactions-api?hl=ar#CreateInteraction)، فإنّك
تنشئ مورد `Interaction` جديدًا:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Tell me a short story about a time-traveling lighthouse."
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

const interaction = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Tell me a short story about a time-traveling lighthouse.",
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
        .input(InteractionsInput.of("Tell me a short story about a time-traveling lighthouse."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Tell me a short story about a time-traveling lighthouse."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Tell me a short story about a time-traveling lighthouse."
  }'
```

### إدارة الحالة من جهة الخادم

يمكنك استخدام `id` لتفاعل مكتمل في مكالمة لاحقة باستخدام المَعلمة `previous_interaction_id` لمواصلة المحادثة. يستخدم الخادم هذا المعرّف لاسترداد سجلّ المحادثات، ما يوفّر عليك عناء إعادة إرسال سجلّ المحادثات بأكمله:

### Python

```
from google import genai

client = genai.Client()

# 1. First turn
turn1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Phil."
)

# 2. Second turn (chained using previous_interaction_id)
turn2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is my name?",
    previous_interaction_id=turn1.id
)

print(turn2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

// 1. First turn
const turn1 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "Hi, my name is Phil.",
});

// 2. Second turn (chained using previous_interaction_id)
const turn2 = await client.interactions.create({
  model: "gemini-3.8-flash",
  input: "What is my name?",
  previous_interaction_id: turn1.id,
});

console.log(turn2.output_text);
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

// 1. First turn
Interaction turn1 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("Hi, my name is Phil."))
                    .build()))
        .interaction()
        .get();

// 2. Second turn (chained using previousInteractionId)
Interaction turn2 =
    client
        .interactions
        .create(
            CreateInteractionRequestBody.of(
                CreateModelInteraction.builder()
                    .model(Model.of("gemini-3.8-flash"))
                    .input(InteractionsInput.of("What is my name?"))
                    .previousInteractionId(turn1.id().get())
                    .build()))
        .interaction()
        .get();

System.out.println(turn2.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. First turn
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Hi, my name is Phil."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // 2. Second turn (chained using PreviousInteractionID)
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            Input:                 interactions.NewInteractionsInput("What is my name?"),
            PreviousInteractionID: turn1.Interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

### REST

```
# Replace PREVIOUS_INTERACTION_ID with the id returned from the first turn
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is my name?",
    "previous_interaction_id": "PREVIOUS_INTERACTION_ID"
  }'
```

تحتفظ المَعلمة `previous_interaction_id` بسجلّ المحادثات فقط (المدخلات والمخرجات) باستخدام `previous_interaction_id`. المَعلمات الأخرى هي **مَعلمات على مستوى التفاعل**
ولا تنطبق إلا على التفاعل المحدّد الذي تُنشئه حاليًا:

- `tools`
- `system_instruction`
- ‫`generation_config` (بما في ذلك `thinking_level` و`temperature` وما إلى ذلك)

وهذا يعني أنّه عليك إعادة تحديد هذه المَعلمات في كل تفاعل جديد إذا كنت تريد تطبيقها. تكون إدارة الحالة من جهة الخادم اختيارية، ويمكنك أيضًا التشغيل في وضع بلا حالة من خلال إرسال سجلّ المحادثة الكامل في كل طلب.

### تخزين البيانات والاحتفاظ بها

تخزِّن واجهة برمجة التطبيقات تلقائيًا جميع عناصر Interaction (`store=true`) بهدف تسهيل استخدام ميزات إدارة الحالة من جهة الخادم (باستخدام `previous_interaction_id`) و[التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) (باستخدام `background=true`) ولأغراض إمكانية تتبّع البيانات.

- **المستوى المدفوع**: يحتفظ النظام بالتفاعلات لمدة **55 يومًا**.
- **المستوى المجاني**: يحتفظ النظام بالتفاعلات لمدة **يوم واحد**.

إذا كنت لا تريد ذلك، يمكنك ضبط `store=false` في طلبك. يختلف عنصر التحكّم هذا عن إدارة الحالة، ويمكنك إيقاف مساحة التخزين لأي تفاعل. يُرجى العِلم أنّ
`store=false` غير متوافق مع [التنفيذ في الخلفية](https://ai.google.dev/gemini-api/docs/background-execution?hl=ar) ويمنع استخدام
`previous_interaction_id` في الأدوار اللاحقة.

بالنسبة إلى مشاريع &quot;المستوى المدفوع&quot;، يمكنك ضبط فترة الاحتفاظ بالبيانات في [AI Studio](https://aistudio.google.com/logs?hl=ar) لوضع علامة تلقائيًا على السجلات ليتم حذفها من مساحة تخزين المشروع بعد 7 أو 14 أو 28 أو 55 يومًا. قد يؤثّر تقليل مدة الاحتفاظ بالبيانات في استرجاع المحادثات السابقة.

يمكنك حذف التفاعلات المخزّنة في أي وقت باستخدام طريقة [`delete`](https://ai.google.dev/api/interactions-api?hl=ar#deleteInteraction) آليًا، والتي تتطلّب معرّف التفاعل. يمكنك أيضًا عرض سجلّات التفاعلات المخزّنة وإدارتها، بما في ذلك حذفها من مساحة تخزين المشروع، في [AI Studio](https://aistudio.google.com/logs?hl=ar).

وبعد انتهاء فترة التخزين، سيتم حذف بياناتك تلقائيًا.

تتم معالجة عناصر التفاعل وفقًا [للبنود](https://ai.google.dev/gemini-api/terms?hl=ar).

### عرض التفاعلات في AI Studio

تخزّن واجهة برمجة التطبيقات طلبات Interactions API التي تم تنفيذها باستخدام `store=true` للمشاريع في "الفئة المدفوعة". يمكنك الاطّلاع عليها مباشرةً من
[صفحة "السجلات" في Google AI Studio](https://ai.google.dev/gemini-api/docs/www.aistudio.google.com/logs?hl=ar). اطّلِع على [دليل السجلات](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=ar) لمزيد من المعلومات.

## أفضل الممارسات

- **نسبة نتيجة ذاكرة التخزين المؤقت**: تتوفّر ميزة التخزين المؤقت الضمني في كل من الوضعين الثابت وعديم الحالة (راجِع [البدء السريع](https://ai.google.dev/gemini-api/docs/get-started?hl=ar#4_multi-turn_conversations)). يتيح استخدام
  `previous_interaction_id` (مع الاحتفاظ بالحالة) لمواصلة المحادثات للنظام الاستفادة بسهولة أكبر من التخزين المؤقت الضمني لسجلّ المحادثات، ما يحسّن الأداء ويقلّل التكاليف.
- **دمج التفاعلات**: يمكنك دمج تفاعلات الوكيل والنموذج ومطابقتها ضمن محادثة واحدة. على سبيل المثال، يمكنك استخدام وكيل متخصص، مثل وكيل &quot;البحث المعمّق&quot;، لجمع البيانات الأولية، ثم استخدام نموذج Gemini عادي لتنفيذ مهام المتابعة، مثل التلخيص أو إعادة التنسيق، وربط هذه الخطوات باستخدام `previous_interaction_id`.

## الطُرز والوكلاء المتوافقون

| اسم النموذج | النوع | رقم تعريف الطراز |
| --- | --- | --- |
| Gemini 3.8 Flash | الطراز | `gemini-3.8-flash` |
| Gemini 3.7 Flash | الطراز | `gemini-3.7-flash` |
| Gemini 3.6 Flash | الطراز | `gemini-3.6-flash` |
| Gemini 3.5 Flash | الطراز | `gemini-3.5-flash` |
| معاينة Gemini 3.1 Pro | الطراز | `gemini-3.1-pro-preview` |
| Gemini 3.5 Flash-Lite | الطراز | `gemini-3.5-flash-lite` |
| Gemini 3.1 Flash-Lite | الطراز | `gemini-3.1-flash-lite` |
| معاينة Gemini 3 Flash | الطراز | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | الطراز | `gemini-2.5-pro` |
| Gemini 2.5 Flash | الطراز | `gemini-2.5-flash` |
| ‫Gemini 2.5 Flash-lite | الطراز | `gemini-2.5-flash-lite` |
| صورة Gemini 3 Pro | الطراز | `gemini-3-pro-image` |
| صورة Gemini 3.1 Flash | الطراز | `gemini-3.1-flash-image` |
| معاينة ميزة "تحويل النص إلى كلام" في Gemini 3.1 Flash | الطراز | `gemini-3.1-flash-tts-preview` |
| Gemma 4 31B IT | الطراز | `gemma-4-31b-it` |
| Gemma 4 26B MoE IT | الطراز | `gemma-4-26b-a4b-it` |
| Lyria 3.5 | الطراز | `lyria-3.5` |
| معاينة مقطع Lyria 3 | الطراز | `lyria-3-clip-preview` |
| معاينة Lyria 3 Pro | الطراز | `lyria-3-pro-preview` |
| معاينة Deep Research | الوكيل | `deep-research-preview-04-2026` |
| معاينة Deep Research | الوكيل | `deep-research-max-preview-04-2026` |
| معاينة Antigravity | الوكيل | `antigravity-preview-09-2026` |

## حزم SDK

يمكنك استخدام أحدث إصدار من حِزم تطوير البرامج (SDK) من Google GenAI للوصول إلى واجهة برمجة التطبيقات Interactions API.

- في Python، هذه هي حزمة `google-genai` من الإصدار `2.3.0` والإصدارات الأحدث.
- في JavaScript، هذه هي حزمة `@google/genai` من الإصدار `2.3.0` والإصدارات الأحدث.
- على Go، هذه هي حزمة `google.golang.org/genai`.
- في Java، هذه هي حزمة `com.google.genai:google-genai`.

يمكنك الاطّلاع على مزيد من المعلومات حول كيفية تثبيت حِزم SDK في صفحة [المكتبات](https://ai.google.dev/gemini-api/docs/libraries?hl=ar).

## القيود

- **بروتوكول سياق النموذج (MCP) عن بُعد**: لا يتيح Gemini 3 استخدام بروتوكول سياق النموذج عن بُعد، ولكنّ هذه الميزة ستتوفّر قريبًا.
- **توافق النماذج المتعددة الجولات**: عند استخدام نماذج مختلفة في محادثة (سواء كانت تتضمّن حالة أو لا تتضمّن حالة)، يجب أن تتوافق النماذج اللاحقة مع أساليب الإخراج الخاصة بالنماذج السابقة كمدخلات. على سبيل المثال، إذا أنشأت صورة باستخدام `gemini-3.1-flash-image`، لا يمكنك مواصلة المحادثة مع نموذج لا يقبل إدخال الصور (مثل نموذج نصي فقط أو نموذج لإنشاء الموسيقى مثل Lyria).

تتوافق الميزات التالية مع واجهة
[`generateContent`](https://ai.google.dev/gemini-api/docs/generate-content/text-generation?hl=ar) API، ولكنها **غير متاحة بعد** في Interactions API:

- **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar)**
- **[استدعاء الدوال تلقائيًا (Python)](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=ar#automatic_function_calling_python_only)**
- **[التخزين المؤقت الصريح](https://ai.google.dev/gemini-api/docs/caching?hl=ar)**: يُرجى العِلم أنّ التخزين المؤقت الضمني من جهة الخادم متاح في Interactions API
  من خلال `previous_interaction_id`.
- **[إعدادات الأمان](https://ai.google.dev/gemini-api/docs/safety-settings?hl=ar)**: إعدادات الأمان المخصّصة غير متاحة في Interactions API.

## الملاحظات

تُعدّ ملاحظاتك مهمة جدًا لتطوير Interactions API.
يمكنك مشاركة أفكارك أو الإبلاغ عن أخطاء أو طلب ميزات في [منتدى مطوّري الذكاء الاصطناعي من Google](https://discuss.ai.google.dev/c/gemini-api/4?hl=ar).

## الخطوات التالية

- جرِّب [دفتر ملاحظات التشغيل السريع لواجهة Interactions API](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_interactions_api.ipynb?hl=ar).
- [مزيد من المعلومات حول وكيل Deep Research في Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-24 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
