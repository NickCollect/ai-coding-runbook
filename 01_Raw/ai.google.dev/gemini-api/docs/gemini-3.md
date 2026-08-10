---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=ar
fetched_at: 2026-08-10T03:21:52.251684+00:00
title: "\u062f\u0644\u064a\u0644 \u0627\u0644\u0645\u0637\u0648\u0651\u0631\u064a\u0646 \u0641\u064a Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)

إرسال ملاحظات

# دليل المطوّرين في Gemini 3

‫Gemini 3 هي عائلة النماذج الأكثر ذكاءً لدينا حتى الآن، وهي تستند إلى أساس متقدّم في مجال الاستدلال. تم تصميم هذا النموذج لتحويل أي فكرة إلى واقع من خلال إتقان مهام سير العمل المستندة إلى الذكاء الاصطناعي الوكيل، والترميز المستقل، والمهام المعقّدة المتعدّدة الوسائط.
يتناول هذا الدليل الميزات الرئيسية لعائلة نماذج Gemini 3 وكيفية الاستفادة منها إلى أقصى حد.

استكشِف [مجموعة تطبيقات Gemini 3](https://aistudio.google.com/app/apps?source=showcase&%3BshowcaseTag=gemini-3&hl=ar) لمعرفة كيف يتعامل النموذج مع الاستدلال المتقدّم والترميز الذاتي ومهام الوسائط المتعددة المعقّدة.

ابدأ ببضعة أسطر من الرموز البرمجية:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(interaction.output_text);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Find the race condition in this multi-threaded C++ snippet: [code here]"
  }'
```

## التعرّف على سلسلة Gemini 3

يُعدّ Gemini 3.1 Pro الخيار الأفضل للمهام المعقّدة التي تتطلب معرفة واسعة بالعالم واستدلالاً متقدّمًا في مختلف الوسائط.

‫Gemini 3 Flash هو أحدث نموذج من السلسلة 3، ويتميّز بذكاء على مستوى Pro وبسرعة Flash وأسعاره.

‫Nano Banana Pro (المعروف أيضًا باسم Gemini 3 Pro Image) هو نموذجنا الأعلى جودة لإنشاء الصور، وNano Banana 2 (المعروف أيضًا باسم Gemini 3.1 Flash Image) هو النموذج المكافئ الذي يتيح إنشاء عدد كبير من الصور بكفاءة عالية وبتكلفة أقل.

‫Gemini 3.1 Flash-Lite هو نموذجنا الأكثر كفاءةً والمصمَّم ليكون فعالاً من حيث التكلفة ولإنجاز المهام الكبيرة.

تتوفّر جميع نماذج Gemini 3 حاليًا في إصدار تجريبي.

| رقم تعريف الطراز | قدرة الاستيعاب (ضمن الفترة الزمنية / خارج الفترة الزمنية) | تاريخ آخر تحديث للبيانات | التسعير (الإدخال / الإخراج)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite** | 1M / 64k | يناير 2025 | ‫0.25 دولار أمريكي (نص أو صورة أو فيديو)، أو 0.50 دولار أمريكي (ملف صوتي) / 1.50 دولار أمريكي |
| **gemini-3.1-flash-image-preview** | ‫128 ألف / 32 ألف | يناير 2025 | ‫0.25 دولار أمريكي (إدخال نصي) / 0.067 دولار أمريكي (إخراج صورة)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | يناير 2025 | ‫2 دولار أمريكي / 12 دولار أمريكي (أقل من 200 ألف رمز مميّز)   4 دولار أمريكي / 18 دولار أمريكي (أكثر من 200 ألف رمز مميّز) |
| **gemini-3-flash-preview** | 1M / 64k | يناير 2025 | 0.50 دولار أمريكي / 3 دولار أمريكي |
| **gemini-3-pro-image-preview** | ‫65 ألف / 32 ألف | يناير 2025 | ‫2 دولار أمريكي (إدخال النص) / 0.134 دولار أمريكي (إخراج الصورة)\*\* |

*\* الأسعار لكل مليون رمز مميز ما لم يُذكر خلاف ذلك.*
*\*\* يختلف سعر الصورة حسب الدقة. يمكنك الاطّلاع على [صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) للحصول على التفاصيل.*

للاطّلاع على الحدود التفصيلية والأسعار والمعلومات الإضافية، يُرجى الانتقال إلى [صفحة النماذج](https://ai.google.dev/gemini-api/docs/models/gemini?hl=ar).

## ميزات جديدة في واجهة برمجة التطبيقات Gemini 3

يقدّم Gemini 3 مَعلمات جديدة مصمَّمة لمنح المطوّرين مزيدًا من التحكّم في وقت الاستجابة والتكلفة ودقة الوسائط المتعددة.

### مستوى التفكير

تستخدم نماذج سلسلة Gemini 3 ميزة &quot;التفكير الديناميكي&quot; تلقائيًا للاستدلال من خلال الطلبات. يمكنك استخدام المَعلمة `thinking_level` التي تتحكّم في **الحد الأقصى** لعمق عملية الاستدلال الداخلية للنموذج قبل أن ينتج ردًا. يتعامل Gemini 3 مع هذه المستويات على أنّها حدود نسبية للتفكير، وليس كضمانات صارمة للرموز المميزة.

إذا لم يتم تحديد `thinking_level`، سيتم تلقائيًا ضبط Gemini 3 على `high`. للحصول على ردود أسرع وبزمن استجابة أقل عندما لا يكون الاستنتاج المعقّد مطلوبًا، يمكنك حصر مستوى التفكير في النموذج على `low`.

| مستوى التفكير | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | الوصف |
| --- | --- | --- | --- | --- |
| **`minimal`** | غير متاح | متاح (تلقائي) | متاح | يتطابق مع إعداد "بدون تفكير" لمعظم طلبات البحث. قد يفكّر النموذج بشكل محدود جدًا لإنجاز مهام الترميز المعقّدة. يقلّل من وقت الاستجابة للتطبيقات التي تتضمّن محادثات أو تتطلّب معدّل أعلى لنقل البيانات. يُرجى العِلم أنّ `minimal` لا يضمن إيقاف ميزة "أفكر بصوت عالٍ". |
| **`low`** | متاح | متاح | متاح | يقلّل من زمن الانتقال والتكلفة. الأفضل للتطبيقات التي تتطلّب اتّباع تعليمات بسيطة أو إجراء محادثات أو معالجة البيانات بسرعة كبيرة. |
| **`medium`** | متاح | متاح | متاح | التفكير المتوازن لمعظم المهام |
| **`high`** | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | زيادة عمق الاستدلال إلى أقصى حد قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى الرمز المميز الأول (غير الخاص بالتفكير) في الناتج، ولكن سيتم التفكير في الناتج بعناية أكبر. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="How does AI work?",
    generation_config={"thinking_level": "low"},
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### درجة الحرارة

بالنسبة إلى جميع طُرز Gemini 3، ننصح بشدة بإبقاء مَعلمة درجة العشوائية عند قيمتها التلقائية البالغة `1.0`.

في حين أنّ النماذج السابقة كانت تستفيد غالبًا من ضبط درجة العشوائية للتحكّم في مستوى الإبداع مقابل الحتمية، تم تحسين قدرات الاستدلال في Gemini 3 للإعداد التلقائي. قد يؤدي تغيير درجة العشوائية (ضبطها على قيمة أقل من 1.0) إلى سلوك غير متوقّع، مثل التكرار أو انخفاض الأداء، خاصةً في المهام الرياضية أو الاستدلال المعقدة.

### توقيعات الأفكار

تستخدم نماذج Gemini 3 توقيعات الأفكار للحفاظ على سياق الاستدلال في جميع طلبات البيانات من واجهة برمجة التطبيقات. هذه التواقيع هي تمثيلات مشفّرة لعملية التفكير الداخلية التي يجريها النموذج.

- **الوضع مع حفظ الحالة (يُنصح به)**: عند استخدام Interactions API في الوضع مع حفظ الحالة (توفير `previous_interaction_id`)، يدير الخادم تلقائيًا سجلّ المحادثات وتوقيعات الأفكار.
- **الوضع غير المرتبط بحالة**: إذا كنت تدير سجلّ المحادثات يدويًا، يجب تضمين كتل الأفكار مع توقيعاتها في الطلبات اللاحقة للتحقّق من صحتها.

للحصول على معلومات تفصيلية، يُرجى الاطّلاع على صفحة [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thinking?hl=ar).

### النتائج المنظَّمة باستخدام الأدوات

تتيح لك نماذج Gemini 3 الجمع بين [النتائج المنظَّمة](https://ai.google.dev/gemini-api/docs/structured-output?hl=ar) والأدوات المضمَّنة، بما في ذلك
[تحديد المصدر من خلال بحث Search](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[سياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) و[تطبيق الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[استدعاء الدالة](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-pro-preview",
    input="Search for all details for the latest Euro.",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"}
    ],
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": MatchResult.model_json_schema()
    },
)

result = MatchResult.model_validate_json(interaction.output_text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as z from "zod";

const matchJsonSchema = {
  type: "object",
  properties: {
    winner: { type: "string", description: "The name of the winner." },
    final_match_score: { type: "string", description: "The final score." },
    scorers: {
      type: "array",
      items: { type: "string" },
      description: "The name of the scorer."
    }
  },
  required: ["winner", "final_match_score", "scorers"]
};

const matchSchema = z.fromJSONSchema(matchJsonSchema);

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3.1-pro-preview",
    input: "Search for all details for the latest Euro.",
    tools: [
      { type: "google_search" },
      { type: "url_context" }
    ],
    response_format: {
        type: "text",
        mime_type: "application/json",
        schema: matchJsonSchema
    },
  });

  const match = matchSchema.parse(JSON.parse(interaction.output_text));
  console.log(match);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "input": "Search for all details for the latest Euro.",
    "tools": [
      {"type": "google_search"},
      {"type": "url_context"}
    ],
    "response_format": {
        "type": "text",
        "mime_type": "application/json",
        "schema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### إنشاء الصور

تتيح لك أداتا Gemini 3.1 Flash Image وGemini 3 Pro Image إنشاء الصور وتعديلها من خلال طلبات نصية. يستخدم هذا النموذج ميزة "الاستدلال" "للتفكير" في الطلب، ويمكنه استرداد بيانات في الوقت الفعلي، مثل توقعات الطقس أو الرسوم البيانية للأسهم، قبل استخدام ميزة [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar)، وذلك قبل إنشاء صور عالية الدقة.

**الإمكانات الجديدة والمحسّنة:**

- **عرض النص بدقة 4K:** يمكنك إنشاء نص ورسوم بيانية واضحة وسهلة القراءة بدقة تصل إلى 2K و4K.
- **إنشاء المحتوى استنادًا إلى مصادر موثوقة:** استخدِم أداة `google_search` للتحقّق من الحقائق وإنشاء صور استنادًا إلى معلومات واقعية. تتوفّر ميزة "الاستناد إلى مصادر خارجية" باستخدام *بحث الصور* من Google في Gemini 3.1 Flash Image.
- **التعديل الحواري:** تعديل الصور في محادثة مترابطة من خلال طلب إجراء تغييرات (مثلاً، "اجعل الخلفية غروب الشمس"). يعتمد سير العمل هذا على
  **التوقيعات الفكرية** للحفاظ على السياق المرئي بين الأدوار.

للحصول على تفاصيل كاملة حول نسب العرض إلى الارتفاع، وسير عمل التعديل، وخيارات الإعداد، يُرجى الاطّلاع على [دليل إنشاء الصور](https://ai.google.dev/gemini-api/docs/image-generation?hl=ar).

### Python

```
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-pro-image-preview",
    input="Generate an infographic of the current weather in Tokyo.",
    tools=[{"type": "google_search"}],
    response_format={
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
)

from PIL import Image
import io

generated_image = interaction.output_image
if generated_image:
    image_data = base64.b64decode(generated_image.data)
    image = Image.open(io.BytesIO(image_data))
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const client = new GoogleGenAI({});

async function run() {
  const interaction = await client.interactions.create({
    model: "gemini-3-pro-image-preview",
    input: "Generate a visualization of the current weather in Tokyo.",
    tools: [{ type: "google_search" }],
    response_format: {
      type: "image",
      aspect_ratio: "16:9",
      image_size: "4K"
    }
  });

  const buffer = Buffer.from(interaction.output_image.data, 'base64');

  fs.writeFileSync('weather_tokyo.png', buffer);
}

run();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "input": "Generate a visualization of the current weather in Tokyo.",
    "tools": [{"type": "google_search"}],
    "response_format": {
        "type": "image",
        "aspect_ratio": "16:9",
        "image_size": "4K"
    }
  }'
```

**مثال على الرد**

![Weather Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=ar)

### تنفيذ الرموز البرمجية باستخدام الصور

يمكن أن يتعامل Gemini 3 Flash مع الرؤية على أنّها تحقيق نشط، وليس مجرد نظرة سريعة. من خلال الجمع بين الاستدلال و[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)، يضع النموذج خطة، ثم يكتب وينفّذ رموز Python البرمجية لتكبير الصور أو اقتصاصها أو إضافة تعليقات توضيحية إليها أو معالجتها بطريقة أخرى خطوة بخطوة لتحديد إجاباته بصريًا.

**حالات الاستخدام:**

- **التكبير والتدقيق:** يرصد النموذج ضمنيًا الحالات التي تكون فيها التفاصيل صغيرة جدًا (مثل قراءة مقياس أو رقم تسلسلي بعيدَين) ويكتب رمزًا برمجيًا لاقتصاص المنطقة وإعادة فحصها بدقة أعلى.
- **الرياضيات المرئية والرسم البياني:** يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرموز البرمجية (مثل جمع بنود الإيصال أو إنشاء رسم بياني باستخدام Matplotlib من البيانات المستخرَجة).
- **التعليق التوضيحي على الصور:** يمكن للنموذج رسم أسهم أو مربّعات محيطة أو تعليقات توضيحية أخرى مباشرةً على الصور للإجابة عن أسئلة مكانية مثل "أين يجب وضع هذا العنصر؟".

لتفعيل التفكير المرئي، اضبط [تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) كأداة. سيستخدم النموذج تلقائيًا الرمز البرمجي لمعالجة الصور عند الحاجة.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io
import base64

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
    tools=[{"type": "code_execution"}],
)

from IPython.display import display
from PIL import Image
import io

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                 display(Image.open(io.BytesIO(base64.b64decode(content_block.data))))
    elif step.type == "code_execution_call":
        print(step.code)
    elif step.type == "code_execution_result":
        print(step.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: [
      {
        type: "image",
        mime_type: "image/jpeg",
        data: base64ImageData,
      },
      {
        type: "text",
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    tools: [{ type: "code_execution" }],
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log("Code:", step.code);
    } else if (step.type === "code_execution_result") {
      console.log("Output:", step.output);
    }
  }
}

main();
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "'$MODEL'",
      "input": [
            {
              "type": "image",
              "mime_type":"'"$MIME_TYPE"'",
              "data": "'"$IMAGE_B64"'"
            },
            {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
      ],
      "tools": [{"type": "code_execution"}]
    }'
```

لمزيد من التفاصيل حول تطبيق الرموز البرمجية باستخدام الصور، يُرجى الاطّلاع على [تطبيق الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar#images).

### استجابات الوظائف المتعددة الوسائط

تتيح [ميزة "استدعاء الدوال" المتعددة الوسائط](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#multimodal) للمستخدمين الحصول على ردود تتضمّن كائنات متعددة الوسائط، ما يتيح الاستفادة بشكل أفضل من إمكانات استدعاء الدوال في النموذج. تتيح ميزة "استدعاء الدوال" العادية الردود المستندة إلى النصوص فقط:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai
import requests
import base64

client = genai.Client()

# 1. Define the tool
get_image_tool = {
    "type": "function",
    "name": "get_image",
    "description": "Retrieves the image file reference for a specific order item.",
    "parameters": {
        "type": "object",
        "properties": {
            "item_name": {
                "type": "string",
                "description": "The name or description of the item ordered (e.g., 'instrument')."
            }
        },
        "required": ["item_name"],
    },
}

# 2. Send the request with tools
interaction_1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Show me the instrument I ordered last month.",
    tools=[get_image_tool],
)

# 3. Find the function call step
fc_step = next(s for s in interaction_1.steps if s.type == "function_call")
print(f"Tool Call: {fc_step.name}({fc_step.arguments})")

# Execute tool (fetch image)
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# 4. Send multimodal function result back
interaction_2 = client.interactions.create(
    model="gemini-3-flash-preview",
    previous_interaction_id=interaction_1.id,
    input=[{
        "type": "function_result",
        "name": fc_step.name,
        "call_id": fc_step.id,
        "result": [
            {"type": "text", "text": "instrument.jpg"},
            {
                "type": "image",
                "mime_type": "image/jpeg",
                "data": image_b64,
            }
        ]
    }],
    tools=[get_image_tool]
)

print(f"\nFinal model response: {interaction_2.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getImageTool = {
    type: 'function',
    name: 'get_image',
    description: 'Retrieves the image file reference for a specific order item.',
    parameters: {
        type: 'object',
        properties: {
            item_name: {
                type: 'string',
                description: "The name or description of the item ordered (e.g., 'instrument').",
            },
        },
        required: ['item_name'],
    },
};

const interaction1 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: 'Use the get_image tool to show me the instrument I ordered last month.',
    tools: [getImageTool],
});

const fcStep = interaction1.steps.find(s => s.type === 'function_call');
console.log(`Tool Call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`);

const imageUrl = 'https://goo.gle/instrument-img';
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const interaction2 = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    previous_interaction_id: interaction1.id,
    input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }],
    tools: [getImageTool]
});

console.log(`\nFinal model response: ${interaction2.output_text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# 1. First interaction (triggers function call)
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -H 'Content-Type: application/json' \
#   -d '{ "model": "gemini-3-flash-preview", "input": "Show me the instrument I ordered last month.", "tools": [...] }'

# 2. Send multimodal function result back (Replace INTERACTION_ID and CALL_ID)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [{
      "type": "function_result",
      "name": "get_image",
      "call_id": "CALL_ID",
      "result": [
        { "type": "text", "text": "instrument.jpg" },
        {
          "type": "image",
          "mime_type": "'"$MIME_TYPE"'",
          "data": "'"$IMAGE_B64"'"
        }
      ]
    }]
  }'
```

### الجمع بين الأدوات المضمّنة واستدعاء الدوال

يتيح Gemini 3 استخدام أدوات مضمّنة (مثل &quot;بحث Google&quot; وسياق عناوين URL و[المزيد](https://ai.google.dev/gemini-api/docs/tools?hl=ar)) وأدوات [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) المخصّصة في طلب بيانات من واجهة برمجة التطبيقات واحد، ما يتيح إعداد مهام سير عمل أكثر تعقيدًا.

### Python

```
from google import genai
from google.genai import types

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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather
    ],
)

fc_step = next((s for s in interaction.steps if s.type == "function_call"), None)

if fc_step:
    result = {"response": "Very cold. 22 degrees Fahrenheit."}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {"type": "function_result", "name": fc_step.name, "call_id": fc_step.id, "result": result}
        ],
        tools=[
            {"type": "google_search"},
            getWeather
        ],
        previous_interaction_id=interaction.id,
    )

    print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherDeclaration = {
  type: 'function',
  name: 'getWeather',
  description: 'Gets the weather for a requested city.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      city: {
        type: Type.STRING,
        description: 'The city and state, e.g. Utqiaġvik, Alaska',
      },
    },
    required: ['city'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3-flash-preview',
  input: "What is the northernmost city in the United States? What's the weather like there today?",
  tools: [
    { type: "google_search" },
    getWeatherDeclaration
  ],
});

const fcStep = interaction.steps.find(s => s.type === 'function_call');

if (fcStep) {
  const result = { response: "Very cold. 22 degrees Fahrenheit." };

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: 'function_result', name: fcStep.name, call_id: fcStep.id, result: result }
    ],
    tools: [
      { type: "google_search" },
      getWeatherDeclaration
    ],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
}
```

## نقل البيانات من Gemini 2.5

‫Gemini 3 هي مجموعة النماذج الأكثر تطورًا لدينا حتى الآن، وهي تقدّم تحسينًا تدريجيًا مقارنةً بـ Gemini 2.5. عند نقل البيانات، يجب مراعاة ما يلي:

- **التفكير:** إذا كنت تستخدم سابقًا هندسة الطلبات المعقّدة (مثل سلسلة الأفكار) لإجبار Gemini 2.5 على التفكير، جرِّب Gemini 3 مع `thinking_level: "high"` وطلبات مبسطة.
- **إعدادات درجة العشوائية:** إذا كان الرمز الحالي يضبط درجة العشوائية بشكل صريح (خاصةً على قيم منخفضة للحصول على نتائج خوارزمية حتمية)، ننصحك بإزالة هذا المَعلمة واستخدام القيمة التلقائية 1.0 في Gemini 3 لتجنُّب المشاكل المحتملة في التكرار أو انخفاض الأداء في المهام المعقّدة.
- **فهم مستندات PDF والمستندات الأخرى:**
  إذا كنت تعتمد على سلوك معيّن لتحليل المستندات الكثيفة، اختبِر الإعداد الجديد
  `media_resolution_high` لضمان استمرار الدقة.
- **استخدام الرموز المميزة:** قد يؤدي الانتقال إلى الإعدادات التلقائية في Gemini 3 إلى **زيادة** استخدام الرموز المميزة لملفات PDF، ولكن **تقليل** استخدام الرموز المميزة للفيديو. إذا تجاوزت الطلبات الآن قدرة الاستيعاب بسبب زيادة الدقة التلقائية، ننصحك بتقليل دقة الوسائط بشكل صريح.
- **تقسيم الصور:** لا تتوفّر إمكانات تقسيم الصور (عرض أقنعة على مستوى البكسل للكائنات) في Gemini 3 Pro أو Gemini 3 Flash. بالنسبة إلى أحمال العمل التي تتطلّب تقسيم الصور المضمّن، ننصحك بمواصلة استخدام Gemini 2.5 Flash مع إيقاف ميزة "التفكير".
- **استخدام الكمبيوتر:** يتوافق Gemini 3 Pro وGemini 3 Flash مع [استخدام الكمبيوتر](https://ai.google.dev/gemini-api/docs/computer-use?hl=ar). على عكس السلسلة 2.5، لن تحتاج إلى استخدام نموذج منفصل للوصول إلى أداة &quot;استخدام الكمبيوتر&quot;.
- **التوافق مع الأدوات**: تتوافق الآن نماذج Gemini 3 مع [الجمع بين الأدوات المضمّنة وميزة استدعاء الدالة](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar). تتوفّر الآن أيضًا ميزة [الربط بالواقع في "خرائط Google"](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) في نماذج Gemini 3.

## التوافق مع OpenAI

بالنسبة إلى المستخدمين الذين يستفيدون من [طبقة التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar)، يتم تلقائيًا ربط المَعلمات العادية (`reasoning_effort` من OpenAI) بمثيلاتها في Gemini (`thinking_level`).

## أفضل الممارسات المتعلّقة بإنشاء الطلبات

‫Gemini 3 هو نموذج للاستدلال، ما يغيّر طريقة تقديم الطلبات.

- **تعليمات دقيقة:** يجب أن تكون طلبات الإدخال موجزة. يستجيب Gemini 3 بشكل أفضل للتعليمات المباشرة والواضحة. قد تفرط في تحليل أساليب هندسة الطلبات المطوّلة أو المعقّدة جدًا المستخدَمة مع النماذج القديمة.
- **مستوى التفصيل في الإجابات:** يكون Gemini 3 أقل تفصيلاً بشكل تلقائي، ويفضّل تقديم إجابات مباشرة وفعّالة. إذا كانت حالة الاستخدام تتطلّب شخصية أكثر حوارية أو "ثرثارة"، عليك توجيه النموذج بشكل صريح في الطلب (على سبيل المثال، "اشرح هذا الموضوع بأسلوب ودود ومحادث").
- **إدارة السياق:** عند العمل على مجموعات بيانات كبيرة (مثل الكتب الكاملة أو قواعد الرموز أو الفيديوهات الطويلة)، ضَع تعليماتك أو أسئلتك المحدّدة في نهاية الطلب، بعد سياق البيانات. يمكنك ربط استنتاج النموذج بالبيانات المقدَّمة من خلال بدء سؤالك بعبارة مثل "استنادًا إلى المعلومات السابقة...".

يمكنك الاطّلاع على مزيد من المعلومات حول استراتيجيات تصميم الطلبات في [دليل هندسة الطلبات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar).

## الأسئلة الشائعة

1. **ما هو تاريخ آخر تحديث للبيانات لـ Gemini 3؟** تتضمّن نماذج Gemini 3 بيانات حتى تاريخ آخر تحديث للبيانات وهو يناير 2025. للحصول على معلومات أحدث، استخدِم أداة [البحث عن المستندات الأساسية](https://ai.google.dev/gemini-api/docs/google-search?hl=ar).
2. **ما هي الحدود القصوى لقدرة الاستيعاب؟** تتيح نماذج Gemini 3 قدرة استيعاب تصل إلى مليون رمز مميّز، كما تتيح إخراج ما يصل إلى 64 ألف رمز مميّز.
3. **هل تتوفّر فئة مجانية من Gemini 3؟** يتضمّن Gemini 3 Flash
   `gemini-3-flash-preview` فئة مجانية في Gemini API. يمكنك تجربة Gemini 3.1 Pro و3 Flash بدون أي تكلفة في Google AI Studio، ولكن لا تتوفّر طبقة مجانية من `gemini-3.1-pro-preview` في Gemini API.
4. **هل سيظلّ رمز `thinking_budget` القديم صالحًا؟** نعم، لا يزال `thinking_budget` متاحًا للتوافق مع الأنظمة القديمة، ولكن ننصحك بالانتقال إلى `thinking_level` لتحقيق أداء أكثر قابلية للتوقّع. لا تستخدِم كليهما في الطلب نفسه.
5. **هل يتوافق Gemini 3 مع Batch API؟** نعم، يتوافق Gemini 3 مع
   [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).
6. **هل تتوفّر ميزة "التخزين المؤقت للسياق"؟** نعم، تتوافق [ميزة "التخزين المؤقت للسياق"](https://ai.google.dev/gemini-api/docs/caching?hl=ar) مع Gemini 3.
7. **ما هي الأدوات المتوافقة مع Gemini 3؟** يتوافق Gemini 3 مع
   [بحث Google](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) و[استخدام "خرائط Google" كمصدر](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) و[البحث عن الملفات](https://ai.google.dev/gemini-api/docs/file-search?hl=ar) و[تطبيق الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و[سياق عناوين URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar). يتيح أيضًا استخدام [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar) العادي مع أدواتك المخصّصة، و[بالتزامن مع الأدوات المضمّنة](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).
8. **ما هي `gemini-3.1-pro-preview-customtools`؟** إذا كنت تستخدم
   `gemini-3.1-pro-preview` وتجاهل النموذج أدواتك المخصّصة لصالح أوامر bash، جرِّب النموذج `gemini-3.1-pro-preview-customtools` بدلاً من ذلك.
   مزيد من المعلومات [هنا][customtools-model].

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
