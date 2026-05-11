---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=ar
fetched_at: 2026-05-11T05:00:22.015273+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تحديد المصدر من خلال "بحث Google"

يربط تحديد المصدر من خلال "بحث Google" نموذج Gemini بمحتوى الويب في الوقت الفعلي ويتوافق مع جميع اللغات المتاحة. ويسمح ذلك لـ Gemini بتقديم إجابات أكثر دقة والاستشهاد بمصادر يمكن التحقّق منها تتجاوز تاريخ آخر تحديث للبيانات.

يساعدك تحديد المصدر في إنشاء تطبيقات يمكنها إجراء ما يلي:

- **زيادة الدقة الوقائعية:** تقليل حالات الهلوسة في النموذج من خلال استناد الردود إلى معلومات واقعية.
- **الوصول إلى المعلومات في الوقت الفعلي:** الإجابة عن الأسئلة حول الأحداث والمواضيع الحديثة.
- **تقديم الاقتباسات:** تعزيز ثقة المستخدمين من خلال عرض مصادر ادعاءات النموذج.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

يمكنك الاطّلاع على مزيد من المعلومات من خلال تجربة دفتر ملاحظات [أداة "بحث Google"](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).

## طريقة عمل تحديد المصدر من خلال "بحث Google"

عند تفعيل أداة `google_search`، يعالج النموذج تلقائيًا سير العمل بالكامل للبحث عن المعلومات ومعالجتها والاستشهاد بها.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ar)

1. **طلب المستخدم:** يرسل تطبيقك طلبًا من المستخدم إلى Gemini API مع تفعيل أداة `google_search`.
2. **تحليل الطلب:** يحلّل النموذج الطلب ويحدّد ما إذا كان بإمكان "بحث Google" تحسين الإجابة.
3. **بحث Google:** إذا لزم الأمر، ينشئ النموذج تلقائيًا طلب بحث واحدًا أو أكثر وينفّذها.
4. **معالجة نتائج البحث:** يعالج النموذج نتائج البحث ويجمع المعلومات ويصوغ ردًا.
5. **الرد المستند إلى المصدر:** تعرض واجهة برمجة التطبيقات ردًا نهائيًا سهل الاستخدام يستند إلى نتائج البحث. يتضمّن هذا الرد الإجابة النصية للنموذج و`groundingMetadata` التي تتضمّن طلبات البحث ونتائج الويب والاقتباسات.

## فهم تحديد المصدر

عندما يتم تحديد مصدر الرد بنجاح، يتضمّن الرد حقل `groundingMetadata`. هذه البيانات المنظَّمة ضرورية للتحقّق من الادعاءات وإنشاء تجربة اقتباس غنية في تطبيقك.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

تعرض Gemini API المعلومات التالية مع `groundingMetadata`:

- `webSearchQueries` : مصفوفة من طلبات البحث المستخدَمة. تكون هذه الميزة مفيدة لتحديد الأخطاء وفهم عملية الاستدلال في النموذج.
- `searchEntryPoint` : يحتوي على HTML وCSS لعرض "اقتراحات البحث" المطلوبة. يتم تفصيل متطلبات الاستخدام الكاملة في [بنود
  الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search).
- `groundingChunks` : مصفوفة من الكائنات التي تحتوي على مصادر الويب (`uri` و`title`).
- `groundingSupports` : مصفوفة من الأجزاء لربط `text` الردّ من النموذج بالمصادر في `groundingChunks`. يربط كل جزء `segment` نصًا (محدّدًا من خلال `startIndex` و`endIndex`) بواحد أو أكثر من `groundingChunkIndices`. هذا هو المفتاح لإنشاء اقتباسات مضمّنة.

يمكن أيضًا استخدام تحديد المصدر من خلال "بحث Google" مع أداة سياق [عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) لتحديد مصدر الردود في كلّ من بيانات الويب
العلنية وعناوين URL المحدّدة التي تقدّمها.

## إسناد المصادر من خلال الاقتباسات المضمّنة

تعرض واجهة برمجة التطبيقات بيانات اقتباس منظَّمة، ما يمنحك تحكّمًا كاملاً في طريقة عرض المصادر في واجهة المستخدم. يمكنك استخدام الحقلَين `groundingSupports` و`groundingChunks` لربط عبارات النموذج مباشرةً بمصادرها. في ما يلي نمط شائع لمعالجة البيانات الوصفية لإنشاء ردّ يتضمّن اقتباسات مضمّنة قابلة للنقر.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

سيظهر الردّ الجديد الذي يتضمّن اقتباسات مضمّنة على النحو التالي:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## الأسعار

عند استخدام تحديد المصدر من خلال "بحث Google" مع Gemini 3، يتم تحصيل رسوم من مشروعك مقابل كل طلب بحث يقرّر النموذج تنفيذه. إذا قرّر النموذج تنفيذ طلبات بحث متعددة للردّ على طلب واحد (على سبيل المثال، البحث عن `"UEFA Euro 2024 winner"` و`"Spain vs England Euro 2024 final
score"` ضمن طلب بيانات من واجهة برمجة التطبيقات نفسه)، يتم احتساب ذلك كاستخدامَين قابلَين للفوترة للأداة لهذا الطلب. لأغراض الفوترة، نتجاهل طلبات البحث الفارغة على الويب عند احتساب الطلبات الفريدة. لا ينطبق نموذج الفوترة هذا إلا على نماذج Gemini 3. عند استخدام تحديد المصدر من خلال "بحث Google" مع Gemini 2.5 أو النماذج الأقدم، يتم تحصيل رسوم من مشروعك لكل طلب.

للحصول على معلومات مفصّلة عن الأسعار، يُرجى الاطّلاع على صفحة [أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

يمكنك الاطّلاع على الإمكانات الكاملة في صفحة نظرة عامة على [النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | تحديد المصدر من خلال "بحث Google" |
| --- | --- |
| Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 3.1 Flash Image Preview | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Image Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## مجموعات الأدوات المتوافقة

يمكنك استخدام تحديد المصدر من خلال "بحث Google" مع أدوات أخرى، مثل
[تنفيذ الرموز](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar) و
[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar) لتعزيز حالات الاستخدام الأكثر تعقيدًا.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل تحديد المصدر من خلال "بحث Google") والأدوات المخصّصة (استدعاء الدوال). مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar).

## الخطوات التالية

- [جرِّب تحديد المصدر من خلال "بحث Google" في Gemini API
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).
- تعرَّف على الأدوات الأخرى المتاحة، مثل [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).
- تعلَّف على كيفية زيادة الطلبات باستخدام عناوين URL محدّدة من خلال أداة [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-08 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-08 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
