---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=ar
fetched_at: 2026-07-06T05:20:27.083225+00:00
title: "\u0627\u0644\u0623\u0633\u0627\u0633\u064a\u0627\u062a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \"\u0628\u062d\u062b Google\" \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الأساسيات باستخدام "بحث Google"

تتيح ميزة "تحديد المصدر من خلال بحث Search" ربط نموذج Gemini بمحتوى الويب في الوقت الفعلي، وهي تعمل بجميع اللغات المتاحة. يتيح ذلك لـ Gemini تقديم إجابات أكثر دقة والإشارة إلى مصادر يمكن التحقّق منها بعد تاريخ آخر تحديث للبيانات.

تساعدك ميزة "تحديد المصدر" في إنشاء تطبيقات يمكنها إجراء ما يلي:

- **زيادة الدقة الوقائعية:** تقليل حالات الهلوسة في النموذج من خلال استناد الردود إلى معلومات واقعية
- **الوصول إلى المعلومات في الوقت الفعلي:** الإجابة عن الأسئلة حول الأحداث والمواضيع الحديثة
- **تقديم مراجع:** تعزيز ثقة المستخدمين من خلال عرض مصادر ادعاءات النموذج

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## طريقة عمل ميزة "تحديد المصدر من خلال بحث Google"

عند تفعيل أداة `google_search`، يتولّى النموذج تلقائيًا سير العمل الكامل للبحث عن المعلومات ومعالجتها والإشارة إليها.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ar)

1. **طلب المستخدم:** يرسل تطبيقك طلبًا من المستخدم إلى Gemini API مع تفعيل أداة `google_search`.
2. **تحليل الطلب:** يحلّل النموذج الطلب ويحدّد ما إذا كان بإمكان "بحث Google" تحسين الإجابة.
3. **بحث Google:** إذا لزم الأمر، ينشئ النموذج تلقائيًا طلب بحث واحدًا أو عدة طلبات بحث وينفّذها.
4. **معالجة نتائج البحث:** يعالج النموذج نتائج البحث ويجمع المعلومات ويصوغ ردًا.
5. **الرد المستند إلى نتائج البحث:** تعرض واجهة برمجة التطبيقات ردًا نهائيًا سهل الاستخدام يستند إلى نتائج البحث. يتضمّن هذا الردّ الإجابة النصية للنموذج مع `annotations` مضمّنة تحتوي على المراجع، بالإضافة إلى
   `google_search_call` و `google_search_result` اللتين تتضمّنان طلبات البحث والاقتراحات.

## فهم الردّ المستند إلى نتائج البحث

عندما يستند الردّ إلى نتائج البحث بنجاح، يتضمّن الناتج النصي للنموذج
مضمّنة `annotations`مباشرةً في كتلة المحتوى النصي. تقدّم هذه الشروح معلومات عن المراجع تربط أجزاء من الردّ بمصادرها.

```
{
  "steps": [
    {
      "type": "thought",
      "summary": [
        {
          "type": "text",
          "text": "The user is asking for the winner of Euro 2024. I need to search for the result of the Euro 2024 final."
        }
      ],
      "signature": "CoMDAXLI2nynRYojJIy6B1Jh9os2crpWLfB0..."
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
          "search_suggestions": "<!-- HTML and CSS for the search widget -->"
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.",
          "annotations": [
            {
              "type": "url_citation",
              "url": "https://www.aljazeera.com/sports/euro-2024-final",
              "title": "aljazeera.com",
              "start_index": 0,
              "end_index": 56
            },
            {
              "type": "url_citation",
              "url": "https://www.uefa.com/euro2024/news/spain-wins-euro-2024",
              "title": "uefa.com",
              "start_index": 57,
              "end_index": 124
            }
          ]
        }
      ]
    }
  ]
}
```

الحقول الرئيسية في الردّ:

- `google_search_call` : يحتوي على `queries` التي نفّذها النموذج.
- `google_search_result` : يحتوي على `search_suggestions`، وهي مقتطف HTML
  لعرض اقتراحات البحث في واجهة المستخدم. يتم تفصيل متطلبات الاستخدام الكاملة
  في [بنود الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search).
- `text` مع `annotations` : الإجابة التي جمعها النموذج مع مراجع مضمّنة
  يربط كل شرح `url_citation` جزءًا من النص (محدّدًا من خلال `start_index` و`end_index`) بعنوان URL للمصدر. هذا هو المفتاح لإنشاء مراجع مضمّنة.

يمكن أيضًا استخدام ميزة "تحديد المصدر من خلال بحث Google" مع أداة سياق [عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) لربط الردود ببيانات الويب العلنية وعناوين URL المحدّدة التي تقدّمها.

## الإشارة إلى المصادر باستخدام مراجع مضمّنة

تعرض واجهة برمجة التطبيقات شروح `url_citation` مضمّنة في كتلة المحتوى النصي، ما يمنحك تحكّمًا كاملاً في طريقة عرض المصادر في واجهة المستخدم.
يتضمّن كل شرح `start_index` و`end_index` لتحديد جزء النص الذي يشير إليه. إليك كيفية استخراجها وعرضها.

### Python

```
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nCitations:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            cited_text = content_block.text[annotation.start_index:annotation.end_index]
                            print(f"  [{annotation.title}]({annotation.url})")
                            print(f"    Cited text: \"{cited_text}\"")
```

### JavaScript

```
for (const step of interaction.steps) {
  if (step.type === 'model_output') {
    for (const contentBlock of step.content) {
      if (contentBlock.type === 'text') {
        console.log(contentBlock.text);
        if (contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              const citedText = contentBlock.text.slice(annotation.startIndex, annotation.endIndex);
              console.log(`  [${annotation.title}](${annotation.url})`);
              console.log(`    Cited text: "${citedText}"`);
            }
          }
        }
      }
    }
  }
}
```

سيعرض الناتج النص متبوعًا بمراجعه:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## الأسعار

عند استخدام ميزة "تحديد المصدر من خلال بحث Google" مع Gemini 3، يتم تحصيل رسوم من مشروعك مقابل كل طلب بحث يقرّر النموذج تنفيذه. إذا قرّر النموذج تنفيذ عدة طلبات بحث للإجابة عن طلب واحد (على سبيل المثال، البحث عن `"UEFA Euro 2024 winner"` و`"Spain vs England Euro 2024 final
score"` ضمن طلب بيانات من واجهة برمجة التطبيقات نفسه)، يتم احتساب ذلك على أنّه استخدامان قابلان للفوترة للأداة في هذا الطلب. لأغراض الفوترة، نتجاهل طلبات البحث الفارغة على الويب عند احتساب طلبات البحث الفريدة. لا ينطبق نموذج الفوترة هذا إلا على نماذج Gemini 3. عند استخدام ميزة "تحديد المصدر من خلال البحث" مع Gemini 2.5 أو النماذج الأقدم، يتم تحصيل رسوم من مشروعك لكل طلب.

للحصول على معلومات مفصّلة عن الأسعار، يُرجى الاطّلاع على صفحة [أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

يمكنك الاطّلاع على الإمكانات الكاملة في صفحة نظرة عامة على [النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | تحديد المصدر من خلال "بحث Search" |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## مجموعات الأدوات المتوافقة

يمكنك استخدام ميزة "تحديد المصدر من خلال بحث Google" مع أدوات أخرى، مثل
[تنفيذ الرموز البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و
[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) لتعزيز حالات الاستقدام الأكثر تعقيدًا.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل ميزة "تحديد المصدر من خلال بحث Google") والأدوات المخصّصة (استدعاء الدوال). مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar)

## الخطوات التالية

- مزيد من المعلومات حول الأدوات الأخرى المتاحة، مثل [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).
- كيفية زيادة الطلبات باستخدام عناوين URL محدّدة باستخدام أداة سياق عنوان URL .

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-22 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
