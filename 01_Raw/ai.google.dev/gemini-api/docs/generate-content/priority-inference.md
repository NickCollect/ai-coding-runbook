---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=ar
fetched_at: 2026-08-03T04:37:11.733186+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u062f\u0644\u0627\u0644 \u062d\u0633\u0628 \u0627\u0644\u0623\u0648\u0644\u0648\u064a\u0629 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

تستخدم Google تكنولوجيا الذكاء الاصطناعي لترجمة المحتوى إلى لغتك المفضّلة، وقد تتضمّن بعض الأخطاء.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستدلال حسب الأولوية

الوصف: كيفية تحسين وقت الاستجابة باستخدام مستوى الاستدلال "الأولوية"

‫Gemini Priority API هو مستوى استدلال متميّز مصمّم لأحمال العمل الأساسية للمؤسسة التي تتطلّب وقت استجابة أقل وموثوقية أعلى بسعر متميّز. تتم معالجة الزيارات في مستوى "الأولوية" قبل الزيارات في واجهة برمجة التطبيقات العادية ومستوى "التعبير".

يتوفّر الاستدلال "الأولوية" لمستخدمي [المستوى 2 والمستوى 3](https://ai.google.dev/gemini-api/docs/billing?hl=ar#about-billing) في نقاط نهاية GenerateContent API
وInteractions API.

## كيفية استخدام مستوى "الأولوية"

لاستخدام مستوى "الأولوية"، اضبط حقل `service_tier` في نص الطلب على `priority`. المستوى التلقائي هو "عادي" إذا تم حذف الحقل.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Triage this critical customer support ticket immediately.",
        config={"service_tier": "priority"},
    )

    # Validate for graceful downgrade
    if response.sdk_http_response.headers.get("x-gemini-service-tier") == "standard":
        print("Warning: Priority limit exceeded, processed at Standard tier.")

    print(response.text)

except Exception as e:
    # Standard error handling (e.g., DEADLINE_EXCEEDED)
    print(f"Error during API call: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
      const result = await ai.models.generateContent({
          model: "gemini-3.6-flash",
          contents: "Triage this critical customer support ticket immediately.",
          config: {serviceTier: "priority"},
      });

      // Validate for graceful downgrade
      if (result.sdkHttpResponse.headers.get("x-gemini-service-tier") === "standard") {
          console.log("Warning: Priority limit exceeded, processed at Standard tier.");
      }

      console.log(result.text);

  } catch (e) {
      console.log(`Error during API call: ${e}`);
  }
}

await main();
```

### انتقال

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    resp, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("Triage this critical customer support ticket immediately."),
        &genai.GenerateContentConfig{
            ServiceTier: "priority",
        },
    )
    if err != nil {
        log.Fatalf("Error during API call: %v", err)
    }

    // Validate for graceful downgrade
    if resp.SDKHTTPResponse.Header.Get("x-gemini-service-tier") == "standard" {
        fmt.Println("Warning: Priority limit exceeded, processed at Standard tier.")
    }

    fmt.Println(resp.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## آلية عمل الاستدلال "الأولوية"

يوجّه الاستدلال "الأولوية" الطلبات إلى قوائم انتظار الحوسبة عالية الأهمية، ما يوفّر أداءً سريعًا يمكن التنبؤ به للتطبيقات التي يتفاعل معها المستخدمون. آليته الأساسية هي الرجوع السلس من جهة الخادم إلى المعالجة العادية للزيارات التي تتجاوز الحدود الديناميكية، ما يضمن استقرار التطبيق بدلاً من تعذُّر معالجة الطلب.

| الميزة | الأولوية | خطة "الرزمة العادية" | التعبير | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | أعلى بنسبة %75 إلى %100 من الخطة "الرزمة العادية" | السعر الكامل | خصم% 50 | خصم% 50 |
| **وقت الاستجابة** | الثواني | من الثواني إلى الدقائق | الدقائق (الهدف من دقيقة واحدة إلى 15 دقيقة) | ما يصل إلى 24 ساعة |
| **الموثوقية** | عالية (لا يمكن تقليلها) | عالية / متوسطة إلى عالية | بأفضل جهد (يمكن تقليلها) | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **وقت استجابة منخفض**: مصمّم لأوقات الاستجابة بالثواني لأدوات الذكاء الاصطناعي التفاعلية التي يتفاعل معها المستخدمون.
- **موثوقية عالية**: يتم التعامل مع الزيارات بأعلى درجة من الأهمية ولا يمكن
  تقليلها على الإطلاق.
- **التكيّف مع الإصدارات الأقدم**: يتم تلقائيًا الرجوع إلى مستوى "الرزمة العادية" لمعالجة الارتفاعات في الزيارات التي تتجاوز الحدود الديناميكية بدلاً من تعذُّر معالجتها، ما يمنع انقطاع الخدمة.
- **سهولة الاستخدام**: يستخدم الطريقة المتزامنة نفسها `generateContent` التي يستخدمها مستوى
  "الرزمة العادية" ومستوى "التعبير".

### حالات الاستخدام

تُعدّ المعالجة "الأولوية" مثالية لسير العمل الأساسي للمؤسسة حيث يكون الأداء والموثوقية في غاية الأهمية.

- **تطبيقات الذكاء الاصطناعي التفاعلية**: روبوتات الدردشة ومساعدو خدمة العملاء الذين
  يدفع المستخدمون سعرًا متميّزًا ويتوقّعون استجابات سريعة ومتّسقة.
- **محركات اتخاذ القرارات في الوقت الفعلي**: الأنظمة التي تتطلّب نتائج موثوقة جدًا ومنخفضة وقت الاستجابة
  ، مثل فرز التذاكر المباشر أو رصد الاحتيال.
- **ميزات العملاء المتميّزين**: المطوّرون الذين يحتاجون إلى ضمان أهداف أعلى لمستوى الخدمة
  للعملاء الذين يدفعون.

### حدود معدّل الاستخدام

[يحتفظ الاستهلاك "الأولوية" بحدود معدّل الاستخدام الخاصة به على الرغم من احتساب الاستهلاك ضمن حدود معدّل الاستخدام الإجمالية للزيارات التفاعلية.](https://aistudio.google.com/rate-limit?hl=ar) حدود معدّل الاستخدام التلقائية للاستدلال "الأولوية" هي **0.3 من حدّ معدّل الاستخدام العادي للنموذج / المستوى**

### تسلسل منطقي للرجوع السلس

إذا تم تجاوز حدود "الأولوية" بسبب الازدحام، يتم **تلقائيًا وبشكل سلس** الرجوع إلى المعالجة العادية للطلبات التي تتجاوز الحد بدلاً من تعذُّر معالجتها مع ظهور الخطأ 503 أو 429. تتم فوترة الطلبات التي تم الرجوع إليها بالسعر العادي، وليس بالسعر المتميّز لمستوى "الأولوية".

### مسؤولية العميل

- **مراقبة الردود**: على المطوّرين مراقبة `x-gemini-service-tier`
  العنوان في ردّ واجهة برمجة التطبيقات لرصد ما إذا كان يتم الرجوع بشكل متكرّر إلى
  `standard`.
- **إعادة المحاولات**: على العملاء تنفيذ تسلسل منطقي لإعادة المحاولة/التراجع الأسي للأخطاء العادية، مثل `DEADLINE_EXCEEDED`.

## الأسعار

يتم تسعير الاستدلال "الأولوية" بنسبة %75 إلى %100 أعلى من [واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) ويتم تحصيل الرسوم لكل رمز مميّز.

## النماذج المتوافقة

تسمح النماذج التالية بالاستدلال "الأولوية":

| الطراز | الاستدلال "الأولوية" |
| --- | --- |
| [‫Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=ar) | ‫✔️ |
| [‫Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=ar) | ‫✔️ |
| [‫Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ‫✔️ |
| [‫Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ‫✔️ |
| [‫Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ‫✔️ |
| [‫Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ‫✔️ |
| [‫Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ar) | ‫✔️ |
| [‫Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ‫✔️ |
| [‫Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ‫✔️ |
| [‫Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ar) | ‫✔️ |
| [‫Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ‫✔️ |

## الخطوات التالية

يمكنك الاطّلاع على خيارات [الاستدلال والتحسين](https://ai.google.dev/gemini-api/docs/optimization?hl=ar) الأخرى في Gemini:

- [الاستدلال "التعبير"](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar) لخفض التكلفة بنسبة% 50
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) للمعالجة غير المتزامنة في غضون 24 ساعة
- [تخزين السياق مؤقتًا](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل تكاليف الرموز المميّزة للإدخال

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-30 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
