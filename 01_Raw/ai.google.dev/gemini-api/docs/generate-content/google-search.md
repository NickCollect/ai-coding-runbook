---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=ar
fetched_at: 2026-10-26T06:01:40.940938+00:00
title: "\u0627\u0644\u0623\u0633\u0627\u0633\u064a\u0627\u062a \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \"\u0628\u062d\u062b Google\" \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon متاح الآن. [جرِّب هذه الميزة](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ar).

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)

إرسال ملاحظات

# الأساسيات باستخدام "بحث Google"

تتيح ميزة "تحديد المصدر من خلال بحث Search" ربط نموذج Gemini بمحتوى الويب في الوقت الفعلي، وهي تعمل بجميع اللغات المتاحة. يتيح ذلك لـ Gemini تقديم إجابات أكثر دقة والإشارة إلى مصادر يمكن التحقّق منها بعد تاريخ آخر تحديث للبيانات.

تساعدك ميزة "تحديد المصدر" في إنشاء تطبيقات يمكنها تنفيذ ما يلي:

- **زيادة الدقة الوقائعية:** تقليل حالات الهلوسة في النموذج من خلال استناد الردود إلى معلومات واقعية
- **الوصول إلى المعلومات في الوقت الفعلي:** الإجابة عن الأسئلة حول الأحداث والمواضيع الحديثة
- **تقديم مراجع:** تعزيز ثقة المستخدمين من خلال عرض مصادر ادعاءات النموذج

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
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## طريقة عمل ميزة "تحديد المصدر من خلال بحث Google"

عند تفعيل أداة `google_search`، يعالج النموذج تلقائيًا سير العمل بالكامل للبحث عن المعلومات ومعالجتها والإشارة إليها.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=ar)

1. **طلب المستخدم:** يرسل تطبيقك طلبًا من المستخدم إلى Gemini API مع تفعيل أداة `google_search`.
2. **تحليل الطلب:** يحلّل النموذج الطلب ويحدّد ما إذا كان بإمكان "بحث Google" تحسين الإجابة.
3. **بحث Google:** إذا لزم الأمر، ينشئ النموذج تلقائيًا طلب بحث واحدًا أو أكثر وينفّذها.
4. **معالجة نتائج البحث:** يعالج النموذج نتائج البحث ويجمع المعلومات ويصوغ ردًا.
5. **الرد المستند إلى المصدر:** تعرض واجهة برمجة التطبيقات ردًا نهائيًا سهل الاستخدام يستند إلى نتائج البحث. يتضمّن هذا الرد الإجابة النصية للنموذج و`groundingMetadata` مع طلبات البحث ونتائج الويب والمراجع.

## فهم الرد المستند إلى المصدر

عندما يستند الرد بنجاح إلى المصدر، يتضمّن حقل `groundingMetadata`. هذه البيانات المنظَّمة ضرورية للتحقّق من الادعاءات وإنشاء تجربة مراجع غنية في تطبيقك.

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

- `webSearchQueries` : مصفوفة من طلبات البحث المستخدَمة تفيد هذه الميزة في تحديد الأخطاء وفهم عملية استنتاج النموذج.
- `searchEntryPoint` : يحتوي على HTML وCSS لعرض "اقتراحات البحث" المطلوبة. يتم تفصيل متطلبات الاستخدام الكاملة في [بنود
  الخدمة](https://ai.google.dev/gemini-api/terms?hl=ar#grounding-with-google-search).
- `groundingChunks` : مصفوفة من الكائنات التي تحتوي على مصادر الويب (`uri` و`title`)
- `groundingSupports` : مصفوفة من الأجزاء لربط `text` ردّ النموذج بالمصادر في `groundingChunks` يربط كل جزء `segment` نصيًا (محدّدًا من خلال `startIndex` و`endIndex`) بواحد أو أكثر من `groundingChunkIndices`. هذا هو المفتاح لإنشاء مراجع مضمّنة.

يمكن أيضًا استخدام ميزة "تحديد المصدر من خلال بحث Google" مع أداة "[سياق
عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)" لربط الردود ببيانات الويب العلنية
وعناوين URL المحدّدة التي تقدّمها.

## الإشارة إلى المصادر باستخدام المراجع المضمّنة

تعرض واجهة برمجة التطبيقات بيانات مراجع منظَّمة، ما يمنحك تحكّمًا كاملاً في طريقة عرض المصادر في واجهة المستخدم. يمكنك استخدام الحقلَين `groundingSupports` و`groundingChunks` لربط عبارات النموذج مباشرةً بمصادرها. إليك نمط شائع لمعالجة البيانات الوصفية لإنشاء رد يتضمّن مراجع مضمّنة قابلة للنقر.

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

سيظهر الرد الجديد الذي يتضمّن مراجع مضمّنة على النحو التالي:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## الأسعار

عند استخدام ميزة "تحديد المصدر من خلال بحث Google" مع Gemini 3 والنماذج الأحدث، يتم تحصيل رسوم من مشروعك مقابل **كل** طلب بحث يقرّر النموذج تنفيذه.
يتضمّن نموذج الفوترة لكل طلب بحث 5,000 طلب بحث مجاني شهريًا تتم مشاركتها بين جميع نماذج Gemini 3 والنماذج الأحدث، ثم تبلغ التكلفة **14 دولارًا أمريكيًا لكل 1,000 طلب بحث**.

على سبيل المثال، إذا قرّر النموذج تنفيذ طلبات بحث متعددة للردّ على طلب واحد (مثل البحث عن `"UEFA Euro 2024 winner"` و`"Spain vs
England Euro 2024 final score"` ضمن طلب بيانات من واجهة برمجة التطبيقات نفسه)، يتم احتساب ذلك كاستخدامَين قابلَين للفوترة للأداة لهذا الطلب. لأغراض الفوترة، نتجاهل طلبات بحث الويب الفارغة عند احتساب الطلبات الفريدة.

عند استخدام ميزة "تحديد المصدر من خلال بحث Google" مع Gemini 2.5 أو النماذج الأقدم، يتم تحصيل رسوم من مشروعك لكل طلب.

للاطّلاع على معلومات مفصّلة عن الأسعار، يُرجى الانتقال إلى صفحة [أسعار Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=ar).

## النماذج المتوافقة

يمكنك الاطّلاع على الإمكانات الكاملة في صفحة نظرة عامة على [النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

| الطراز | تحديد المصدر من خلال "بحث Search" |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
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

يمكنك استخدام ميزة "تحديد المصدر من خلال بحث Google" مع أدوات أخرى، مثل
[تنفيذ التعليمات البرمجية](https://ai.google.dev/gemini-api/docs/code-execution?hl=ar)،
[سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar)، و
[تحديد المصدر من خلال خرائط Google](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=ar) (المتوفّرة في
Gemini 3.5 Flash-Lite والنماذج الأحدث) لتعزيز حالات الاستخدام الأكثر تعقيدًا.
تتيح نماذج Gemini 3 أيضًا الجمع بين هذه الأدوات المضمّنة والأدوات المخصّصة (استدعاء الدوال). مزيد من المعلومات في صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar)

## الخطوات التالية

- جرِّب ميزة ["تحديد المصدر من خلال بحث Google" في Gemini API
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=ar).
- تعرَّف على الأدوات الأخرى المتاحة، مثل [ميزة "استدعاء الدوال"](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar).
- تعرَّف على كيفية زيادة الطلبات باستخدام عناوين URL محدّدة باستخدام أداة [سياق عنوان URL](https://ai.google.dev/gemini-api/docs/url-context?hl=ar).

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-10-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
