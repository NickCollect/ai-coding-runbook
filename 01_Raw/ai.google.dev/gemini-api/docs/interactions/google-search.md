---
source_url: https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=ar
fetched_at: 2026-06-01T06:07:46.391316+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تحديد المصدر من خلال "بحث Google"

تتيح ميزة تحديد المصدر من خلال "بحث Google" ربط نموذج Gemini بمحتوى على الويب في الوقت الفعلي، وهي متوافقة مع جميع اللغات المتاحة. يتيح ذلك لـ Gemini تقديم إجابات أكثر دقة والاستشهاد بمصادر يمكن التحقّق منها تتجاوز تاريخ آخر تحديث للبيانات.

تساعدك عملية التأسيس على إنشاء تطبيقات يمكنها إجراء ما يلي:

- **زيادة الدقة الواقعية:** يمكنك تقليل حالات الهلوسة في النموذج من خلال الاستناد إلى معلومات واقعية عند إنشاء الردود.
- **الوصول إلى معلومات في الوقت الفعلي:** الإجابة عن أسئلة حول الأحداث والمواضيع الحديثة
- **توفير اقتباسات:** يمكنك كسب ثقة المستخدمين من خلال عرض مصادر المعلومات التي يقدّمها النموذج.

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
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

## طريقة عمل ميزة "تحديد المصدر من خلال بحث Google"

عند تفعيل أداة `google_search`، يتولّى النموذج تلقائيًا سير العمل الكامل المتمثل في البحث عن المعلومات ومعالجتها والاقتباس منها.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ar)

1. **طلب المستخدم:** يرسل تطبيقك طلب المستخدم إلى Gemini API مع تفعيل الأداة `google_search`.
2. **تحليل الطلب:** يحلّل النموذج الطلب ويحدّد ما إذا كان بإمكان &quot;بحث Google&quot; تحسين الإجابة.
3. **بحث Google:** إذا لزم الأمر، ينشئ النموذج تلقائيًا طلب بحث واحدًا أو أكثر وينفّذها.
4. **معالجة نتائج البحث:** يعالج النموذج نتائج البحث، ويصنّف المعلومات، ويصوغ ردًا.
5. **الردّ المستند إلى معلومات موثوقة:** تعرض واجهة برمجة التطبيقات ردًا نهائيًا سهل الاستخدام يستند إلى نتائج البحث. تتضمّن هذه الاستجابة الإجابة النصية التي قدّمها النموذج مع `annotations` مضمّنة تحتوي على الاقتباسات، بالإضافة إلى الخطوتَين `google_search_call` و`google_search_result` اللتين تتضمّنان طلبات البحث واقتراحات البحث.

## فهم الردّ المستند إلى معلومات خارجية

عندما يتم استناد الردّ بنجاح إلى المستند المصدر، يتضمّن الناتج النصي للنموذج `annotations` مضمّنًا مباشرةً في مقطع المحتوى النصي. توفّر هذه التعليقات التوضيحية معلومات الاقتباس التي تربط أجزاء الرد بمصادرها.

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

- ‫`google_search_call` : يحتوي على طلب البحث `queries` الذي نفّذه النموذج.
- ‫`google_search_result` : يحتوي على `search_suggestions`، وهو مقتطف HTML
  لعرض اقتراحات البحث في واجهة المستخدم. يمكن الاطّلاع على متطلبات الاستخدام الكاملة في [بنود الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search).
- ‫`text` مع `annotations` : الإجابة التي تم إنشاؤها بواسطة النموذج مع الاقتباسات المضمّنة يربط كل تعليق توضيحي من النوع `url_citation` مقطعًا نصيًا (محدّدًا بواسطة `start_index` و`end_index`) بعنوان URL للمصدر. هذا هو مفتاح
  إنشاء الاقتباسات المضمّنة.

يمكن أيضًا استخدام ميزة "تحديد المصدر من خلال "بحث Search"" مع [أداة سياق عنوان URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar) لتحديد المصدر من كلّ من بيانات الويب العلنية وعناوين URL المحدّدة التي تقدّمها.

## تحديد مصادر المحتوى من خلال اقتباسات مضمّنة

تعرض واجهة برمجة التطبيقات تعليقات توضيحية `url_citation` مضمّنة في كتلة المحتوى النصي، ما يمنحك تحكّمًا كاملاً في طريقة عرض المصادر في واجهة المستخدم.
تتضمّن كل تعليق توضيحي `start_index` و`end_index` لتحديد الجزء الذي يشير إليه من النص. في ما يلي كيفية استخراجها وعرضها.

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

ستعرض النتائج النص متبوعًا بالاقتباسات:

```
Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title.

Citations:
  [aljazeera.com](https://www.aljazeera.com/sports/euro-2024-final)
    Cited text: "Spain won Euro 2024, defeating England 2-1 in the final."
  [uefa.com](https://www.uefa.com/euro2024/news/spain-wins-euro-2024)
    Cited text: "This victory marks Spain's record fourth European Championship title."
```

## الأسعار

عند استخدام ميزة "الاستناد إلى مصادر خارجية" مع "بحث Google" في Gemini 3، يتم تحصيل رسوم من مشروعك مقابل كل طلب بحث يقرّر النموذج تنفيذه. إذا قرر النموذج تنفيذ طلبات بحث متعددة للإجابة عن طلب واحد (على سبيل المثال، البحث عن `"UEFA Euro 2024 winner"` و`"Spain vs England Euro 2024 final
score"` ضمن طلب بيانات واحد من واجهة برمجة التطبيقات)، سيتم احتساب ذلك كاستخدامَين قابلَين للفوترة للأداة لهذا الطلب. لأغراض الفوترة، نتجاهل طلبات البحث الفارغة على الويب عند احتساب طلبات البحث الفريدة. لا ينطبق نموذج الفوترة هذا إلا على نماذج Gemini 3، وعند استخدام ميزة "الاستناد إلى البحث" مع Gemini 2.5 أو النماذج الأقدم، تتم فوترة مشروعك لكل طلب.

للحصول على معلومات مفصّلة حول الأسعار، يُرجى الاطّلاع على [صفحة أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

يمكنك الاطّلاع على الإمكانات الكاملة في صفحة [نظرة عامة على الطراز](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | تحديد المصدر من خلال "بحث Google" |
| --- | --- |
| ‫Gemini 3.5 Flash | ✔️ |
| معاينة Gemini 3.1 Flash Image | ✔️ |
| معاينة Gemini 3.1 Pro | ✔️ |
| معاينة الصور في Gemini 3 Pro | ✔️ |
| معاينة Gemini 3 Flash | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| ‫Gemini 2.5 Flash-Lite | ✔️ |
| ‫Gemini 2.0 Flash | ✔️ |

## مجموعات الأدوات المتوافقة

يمكنك استخدام ميزة تحديد المصدر من خلال "بحث Search" مع أدوات أخرى، مثل [تنفيذ الرمز](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=ar) و[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar)، لتفعيل المزيد من حالات الاستخدام المعقّدة.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل ميزة "تحديد المصدر" باستخدام "بحث Google") والأدوات المخصّصة (استدعاء الدوال البرمجية). يمكنك الاطّلاع على مزيد من المعلومات في صفحة [مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/interactions/tool-combination?hl=ar).

## الخطوات التالية

- يمكنك التعرّف على الأدوات الأخرى المتاحة، مثل [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=ar).
- تعرَّف على كيفية تحسين الطلبات باستخدام عناوين URL محدّدة من خلال [أداة "سياق عنوان URL"](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
