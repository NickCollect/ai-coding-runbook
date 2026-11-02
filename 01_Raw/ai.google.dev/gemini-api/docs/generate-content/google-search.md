---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/google-search?hl=fa
fetched_at: 2026-11-02T07:01:17.394858+00:00
title: "\u067e\u0627\u06cc\u0647\u200c\u0645\u0646\u062f\u0633\u0627\u0632\u06cc \u0628\u0627 \u00ab\u062c\u0633\u062a\u062c\u0648\u06cc Google\u00bb \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# پایه‌مندسازی با «جستجوی Google»

«پایه‌مندسازی با جستجوی Google» مدل Gemini را به محتوای وب هم‌زمان متصل می‌کند
و با همه زبان‌های دردسترس کار می‌کند. این کار به Gemini امکان می‌دهد پاسخ‌های دقیق‌تری ارائه دهد و به منابع قابل‌تأیید فراتر از تاریخ برش دانش خود ارجاع دهد.

زمینه‌سازی به شما کمک می‌کند برنامه‌هایی بسازید که می‌توانند:

- **افزایش دقت واقعی:** با قرار دادن اطلاعات دنیای واقعی به‌عنوان مبنای پاسخ‌ها، توهمات مدل را کاهش دهید.
- **دسترسی به اطلاعات هم‌زمان:** پاسخ دادن به سؤالات درباره رویدادها و موضوعات اخیر.
- **ارائه نقل‌قول:** با نشان دادن منابع ادعاهای مدل، اعتماد کاربر را جلب کنید.

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

### استراحت

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

با امتحان کردن [دفتر یادداشت ابزار «جستجو»](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=fa) می‌توانید اطلاعات بیشتری کسب کنید.

## نحوه عملکرد پایه‌مندسازی با «جستجوی Google»

وقتی ابزار `google_search` را فعال می‌کنید، مدل کل گردش کار جستجو، پردازش، و نقل‌قول اطلاعات را به‌طور خودکار انجام می‌دهد.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=fa)

1. **پیام‌واره کاربر:** برنامه شما پیام‌واره کاربر را به Gemini API
   با ابزار `google_search` فعال‌شده ارسال می‌کند.
2. **تحلیل پیام‌واره:** مدل پیام‌واره را تحلیل می‌کند و تعیین می‌کند که آیا «جستجوی Google» می‌تواند پاسخ را بهبود بخشد یا نه.
3. **جستجوی Google:** درصورت نیاز، مدل به‌طور خودکار یک یا چند پرسمان جستجو تولید و اجرا می‌کند.
4. **پردازش نتایج جستجو:** مدل نتایج جستجو را پردازش می‌کند،
   اطلاعات را ترکیب می‌کند، و پاسخی را فرمول‌بندی می‌کند.
5. **پاسخ پایه‌مند:** میانای برنامه‌سازی کاربردی پاسخ نهایی کاربرپسندی را برمی‌گرداند که
   مبتنی بر نتایج جستجو است. این پاسخ شامل پاسخ نوشتاری مدل و `groundingMetadata` با پُرسمان‌های جستجو، نتایج وب، و استنادها است.

## آشنایی با پاسخ مستندسازی

وقتی پاسخ با موفقیت زمینه‌سازی شود، پاسخ شامل فیلد `groundingMetadata` خواهد بود. این داده‌های ساختاریافته برای درستی‌سنجی ادعاها و ایجاد تجربه ارجاع غنی در برنامه‌تان ضروری است.

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

‫Gemini API اطلاعات زیر را با `groundingMetadata` برمی‌گرداند:

- ‫`webSearchQueries` : آرایه پرسمان‌های جستجوی استفاده‌شده. این کار برای اشکال‌زدایی و درک فرایند استدلال مدل مفید است.
- `searchEntryPoint` : حاوی HTML و CSS برای ارائه «پیشنهادهای جستجو» الزامی است. الزامات کامل استفاده در [شرایط خدمات](https://ai.google.dev/gemini-api/terms?hl=fa#grounding-with-google-search) به‌طور دقیق شرح داده شده است.
- `groundingChunks` : آرایه‌ای از اشیاء حاوی منابع وب (`uri` و
  `title`).
- `groundingSupports` : آرایه تکه‌ها برای متصل کردن پاسخ مدل `text` به
  منابع در `groundingChunks`. هر بخش، نوشتار `segment` (تعریف‌شده
  توسط `startIndex` و `endIndex`) را به یک یا چند `groundingChunkIndices` پیوند می‌دهد. این
  کلید ساختن نقل‌قول‌های درون‌خطی است.

از «پایه‌مندسازی با جستجوی Google» می‌توان در ترکیب با [ابزار بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa) نیز استفاده کرد تا پاسخ‌ها هم براساس داده‌های وب عمومی و هم براساس نشانی‌های وب خاصی که ارائه می‌دهید پایه‌مندسازی شوند.

## ارجاع دادن به منابع با استنادهای به‌خط

این API داده‌های نقل‌قول ساختاریافته را برمی‌گرداند و به شما کنترل کامل می‌دهد تا نحوه نمایش منابع را در میانای کاربر خود تعیین کنید. می‌توانید از فیلدهای `groundingSupports`
و `groundingChunks` برای پیوند دادن مستقیم اظهارات مدل به
منابع آن‌ها استفاده کنید. در اینجا الگویی رایج برای پردازش فراداده برای ایجاد
پاسخ با استنادهای درون‌خطی و قابل‌کلیک ارائه شده است.

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

پاسخ جدید با استنادهای درون‌خطی به این شکل خواهد بود:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## قیمت‌گذاری

وقتی از «پایه‌مندسازی با جستجوی Google» با Gemini 3 و مدل‌های جدیدتر استفاده می‌کنید،
پروژه شما برای **هر** پرسمان جستجویی که مدل تصمیم به اجرای آن می‌گیرد صورت‌حساب دریافت می‌کند.
این مدل صورت‌حساب براساس پُرسمان شامل ۵٬۰۰۰ درخواست جستجوی رایگان در ماه است که بین همه مدل‌های Gemini 3 و جدیدتر مشترک است و سپس **۱۴ دلار به‌ازای هر ۱٬۰۰۰ درخواست جستجو** هزینه دارد.

برای مثال، اگر مدل تصمیم بگیرد برای پاسخ دادن به یک پیام‌واره چند پرسمان جستجو اجرا کند (مثلاً جستجو برای `"UEFA Euro 2024 winner"` و `"Spain vs
England Euro 2024 final score"` در یک فراخوانی میانای برنامه‌سازی کاربردی)، این به‌عنوان دو استفاده قابل‌صورت‌حساب از ابزار برای آن درخواست محسوب می‌شود. برای اهداف صورت‌حساب،
پُرسمان‌های جستجوی وب خالی را هنگام شمارش پُرسمان‌های یکتا نادیده می‌گیریم.

وقتی از زمینه‌سازی جستجو با Gemini 2.5 یا مدل‌های قدیمی‌تر استفاده می‌کنید، پروژه شما
به‌ازای هر پیام‌واره صورت‌حساب دریافت می‌کند.

برای اطلاعات دقیق درباره قیمت‌گذاری، به [صفحه قیمت‌گذاری Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) مراجعه کنید.

## مدل‌های پشتیبانی‌شده

می‌توانید قابلیت‌های کامل را در صفحه [نمای کلی
مدل](https://ai.google.dev/gemini-api/docs/models?hl=fa) پیدا کنید.

| مدل | پایه‌مندسازی با «جستجوی Google» |
| --- | --- |
| Gemini 4 Argon | ✔️ |
| Gemini 3.8 Flash | ✔️ |
| Gemini 3.6 Flash | ✔️ |
| Gemini 3.5 Flash-Lite | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| پیش‌نمایش تصویر Gemini 3.1 Flash | ✔️ |
| Gemini 3.1 Pro Preview | ✔️ |
| پیش‌نمایش تصویر Gemini 3 Pro | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 3.1 Flash-Lite Preview | ✔️ |
| ‫Gemini 2.5 Pro | ✔️ |
| ‫Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## ترکیب‌های ابزار پشتیبانی‌شده

می‌توانید از «پایه‌مندسازی با جستجوی Google» به‌همراه ابزارهای دیگر مثل
[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)،
[بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)، و
[پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa) (پشتیبانی‌شده در
Gemini 3.5 Flash-Lite و مدل‌های جدیدتر) برای تقویت موارد استفاده پیچیده‌تر استفاده کنید.
مدل‌های Gemini 3 از ترکیب این ابزارهای داخلی با ابزارهای سفارشی (فراخوانی تابع) نیز پشتیبانی می‌کنند. در صفحه
[ترکیب‌های ابزار](https://ai.google.dev/gemini-api/docs/tool-combination?hl=fa) بیشتر بدانید.

## قدم بعدی چیست

- [پایه‌مندسازی با «جستجوی Google» در Gemini API
  Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=fa) را امتحان کنید.
- با ابزارهای دردسترس دیگر، مثل [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)، آشنا شوید.
- بااستفاده از [ابزار بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)، با نحوه تقویت پیام‌واره‌ها با نشانی‌های وب خاص آشنا شوید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-29 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-29 به‌وقت ساعت هماهنگ جهانی."],[],[]]
