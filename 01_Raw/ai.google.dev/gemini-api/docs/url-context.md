---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=ar
fetched_at: 2026-09-21T05:57:13.621525+00:00
title: "\u0633\u064a\u0627\u0642 \u0639\u0646\u0648\u0627\u0646 URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# سياق عنوان URL

تتيح لك أداة "سياق عنوان URL" توفير سياق إضافي للنماذج في الـ
شكل عناوين URL. من خلال تضمين عناوين URL في طلبك، سيتمكّن النموذج من الوصول إلى
المحتوى من تلك الصفحات (طالما أنّه ليس نوع عنوان URL مدرَجًا في الـ
[قسم القيود](#limitations)) لإعلام
ردّه وتحسينه.

تكون أداة "سياق عنوان URL" مفيدة في مهام مثل ما يلي:

- **استخراج البيانات**: يمكنك سحب معلومات معيّنة، مثل الأسعار أو الأسماء أو النتائج الرئيسية
  ، من عناوين URL متعدّدة.
- **مقارنة المستندات**: يمكنك تحليل تقارير أو مقالات أو ملفات PDF متعدّدة لتحديد الاختلافات وتتبُّع المؤشرات.
- **تجميع المحتوى وإنشاؤه**: يمكنك دمج المعلومات من عدة عناوين URL مصدر لإنشاء ملخّصات أو منشورات مدوّنة أو تقارير دقيقة.
- **تحليل الرموز والمستندات**: يمكنك الإشارة إلى مستودع GitHub أو مستندات فنية لشرح الرموز أو إنشاء تعليمات الإعداد أو الإجابة عن الأسئلة.

يوضّح المثال التالي كيفية مقارنة وصفتَين من موقعَين إلكترونيَين مختلفَين.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### Javascript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## آلية العمل

تستخدم أداة "سياق عنوان URL" عملية استرداد من خطوتَين لتحقيق التوازن بين السرعة والتكلفة والوصول إلى البيانات الحديثة. عند تقديم عنوان URL، تحاول الأداة أولاً جلب المحتوى من ذاكرة تخزين مؤقت لفهرس داخلي. تعمل هذه الذاكرة كذاكرة تخزين مؤقت محسّنة إلى حد كبير. إذا لم يكن عنوان URL متاحًا في الفهرس (على سبيل المثال، إذا كانت صفحة جديدة جدًا)، تعود الأداة تلقائيًا إلى إجراء عملية جلب مباشرة.
يؤدي ذلك إلى الوصول مباشرةً إلى عنوان URL لاسترداد محتواه في الوقت الفعلي.

## الجمع مع أدوات أخرى

يمكنك الجمع بين أداة "سياق عنوان URL" وأدوات أخرى لإنشاء مهام أكثر فعالية.

[تتيح نماذج Gemini 3](#supported-models) الجمع بين الأدوات المضمّنة
(مثل "سياق عنوان URL") والأدوات المخصّصة (استدعاء الدوال). مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar)

### تحديد المصدر باستخدام "بحث Google"

عند تفعيل كلّ من "سياق عنوان URL" و
[ميزة تحديد المصدر باستخدام "بحث Google"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)، يمكن للنموذج استخدام إمكانات البحث للعثور على
معلومات ذات صلة على الإنترنت، ثم استخدام أداة "سياق عنوان URL" للحصول على فهم أكثر
تفصيلاً للصفحات التي يعثر عليها. يكون هذا النهج فعّالاً في حال كانت التعليمات البرمجية تتطلّب كلاً من البحث على نطاق واسع والتحليل المتعمّق لصفحات معيّنة.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### Javascript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.6-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## فهم الردّ

عندما يستخدم النموذج أداة "سياق عنوان URL"، يتضمّن ردّه النصي تعليقات توضيحية مضمّنة `url_citation` في كتلة المحتوى النصي. يربط كل تعليق توضيحي جزءًا من نص الردّ (من خلال `start_index` و`end_index`) بعنوان URL المصدر الذي تم استخلاص المعلومات منه. هذه هي الطريقة الأساسية لعرض الاقتباسات في تطبيقك
. اطّلِع على [المثال الرئيسي أعلاه](#get-started) لمعرفة كيفية استخراجها.

يتضمّن الردّ أيضًا خطوة `url_context_result` تتضمّن بيانات وصفية حول كل محاولة لاسترداد عنوان URL (الحالة، عنوان URL الذي تم استرداده). ويكون ذلك مفيدًا بشكل أساسي لتحديد المشاكل وحلّها.

### عمليات فحص الأمان

يُجري النظام فحصًا للإشراف على المحتوى في عناوين URL للتأكّد من استيفائها لمعايير الأمان. إذا لم يستوفِ عنوان URL هذا الفحص، ستعرض الخطوة المقابلة
`url_context_result` `status` بقيمة `"unsafe"`.

### عدد الرموز المميّزة

يتم احتساب المحتوى الذي يتم استرداده من عناوين URL التي تحدّدها في التعليمات البرمجية كجزء من الرموز المميّزة للإدخال. يمكنك الاطّلاع على عدد الرموز المميّزة في الكائن `usage` للتفاعل. في ما يلي مثال:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

يعتمد السعر لكل رمز مميّز على النموذج المستخدَم، اطّلِع على
[صفحة الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) للحصول على التفاصيل.

## النماذج المتوافقة

| الطراز | سياق عنوان URL |
| --- | --- |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## أفضل الممارسات

- **توفير عناوين URL محدّدة**: للحصول على أفضل النتائج، قدِّم عناوين URL مباشرةً إلى
  المحتوى الذي تريد أن يحلّله النموذج. لن يستردّ النموذج سوى المحتوى من عناوين URL التي تقدّمها، وليس أي محتوى من الروابط المضمّنة.
- **التحقّق من إمكانية الوصول**: تأكَّد من أنّ عناوين URL التي تقدّمها لا تؤدي إلى
  صفحات تتطلّب تسجيل الدخول أو تكون محجوبة بنظام حظر الاشتراك غير المدفوع.
- **استخدام عنوان URL الكامل**: قدِّم عنوان URL كاملاً، بما في ذلك البروتوكول
  (على سبيل المثال، https://www.google.com بدلاً من google.com فقط).

## القيود

- حدّ الطلب: يمكن للأداة معالجة ما يصل إلى 20 عنوان URL لكل طلب.
- حجم محتوى عنوان URL: الحد الأقصى لحجم المحتوى الذي يتم استرداده من عنوان URL واحد هو 34 ميغابايت.
- إمكانية الوصول للجميع: يجب أن تكون عناوين URL متاحة للجميع على الإنترنت.
  لا تتوافق عناوين localhost (مثل localhost و127.0.0.1) والشبكات الخاصة وخدمات الأنفاق (مثل ngrok وpinggy).
- Gemini API فقط: لا تتوفّر ميزة "سياق عنوان URL" إلا في Gemini API، وليس من خلال Gemini Enterprise Agent Platform.

### أنواع المحتوى المتوافقة وغير المتوافقة

يمكن للأداة استخراج المحتوى من عناوين URL التي تتضمّن أنواع المحتوى التالية:

- النص (text/html وapplication/json وtext/plain وtext/xml وtext/css وtext/javascript وtext/csv وtext/rtf)
- الصورة (image/png وimage/jpeg وimage/bmp وimage/webp)
- ملف PDF ‏ (application/pdf)

أنواع المحتوى التالية **غير** متوافقة:

- محتوى مدفوع
- فيديوهات YouTube (اطّلِع على
  [فهم الفيديو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=ar#youtube) لمعرفة
  كيفية معالجة عناوين URL لفيديوهات YouTube)
- ملفات Google Workspace، مثل مستندات Google أو جداول البيانات
- ملفات الفيديو والصوت

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-09-12 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
