---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar
fetched_at: 2026-06-01T05:59:09.865140+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u062f\u0644\u0627\u0644 \u062d\u0633\u0628 \u0627\u0644\u0623\u0648\u0644\u0648\u064a\u0629 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستدلال حسب الأولوية

‫Gemini Priority API هي طبقة استنتاج مميزة مصمّمة لأحمال العمل الأساسية التي تتطلّب وقت استجابة أقل وموثوقية أعلى بسعر مميز. تحظى الزيارات إلى طبقة الأولوية بأولوية أعلى من الزيارات إلى واجهة برمجة التطبيقات العادية والطبقة المرنة.

يتوفّر الاستنتاج ذو الأولوية لمستخدمي [الطبقة 2 والطبقة 3](https://ai.google.dev/gemini-api/docs/billing?hl=ar#about-billing) من خلال نقطتَي نهاية GenerateContent API
وInteractions API.

## كيفية استخدام الأولوية

لاستخدام طبقة الأولوية، اضبط حقل `service_tier` في نص الطلب على `priority`. الطبقة التلقائية هي الطبقة العادية إذا تم حذف الحقل.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
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
          model: "gemini-3.5-flash",
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
        "gemini-3.5-flash",
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

### راحة

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## آلية عمل الاستنتاج ذي الأولوية

يوجّه الاستنتاج ذو الأولوية الطلبات إلى قوائم انتظار الحوسبة عالية الأهمية، ما يوفّر أداءً سريعًا يمكن التنبؤ به للتطبيقات التي يتفاعل معها المستخدمون. آليته الأساسية هي الرجوع السلس من جهة الخادم إلى المعالجة العادية للزيارات التي تتجاوز الحدود الديناميكية، ما يضمن استقرار التطبيق بدلاً من تعذُّر معالجة الطلب.

| الميزة | الأولوية | خطة "الرزمة العادية" | التعبير | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | أكثر بنسبة %75 إلى %100 من خطة "الرزمة العادية" | السعر الكامل | خصم بنسبة% 50 | خصم بنسبة% 50 |
| **وقت الاستجابة** | الثواني | من الثواني إلى الدقائق | الدقائق (من دقيقة واحدة إلى 15 دقيقة كحد أقصى) | ما يصل إلى 24 ساعة |
| **الموثوقية** | عالية (لا يمكن تقليلها) | عالية / متوسطة عالية | بأفضل جهد (يمكن تقليلها) | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **وقت استجابة منخفض**: مصمّم لأوقات الاستجابة بالثواني لأدوات الذكاء الاصطناعي التفاعلية التي يتفاعل معها المستخدمون.
- **موثوقية عالية**: يتم التعامل مع الزيارات بأعلى درجة من الأهمية ولا يمكن تقليلها على الإطلاق.
- **التكيّف مع الإصدارات الأقدم**: يتم تلقائيًا الرجوع إلى الطبقة العادية لمعالجة الزيارات التي تتجاوز الحدود الديناميكية بدلاً من تعذُّر معالجتها، ما يمنع انقطاع الخدمة.
- **الحد الأدنى من المشاكل**: تستخدم الطريقتان العادية والمرنة طريقة `generateContent` المتزامنة نفسها.

### حالات الاستخدام

تُعد المعالجة ذات الأولوية مثالية لسير العمل الأساسي الذي تكون فيه الأولوية للأداء والموثوقية.

- **تطبيقات الذكاء الاصطناعي التفاعلية**: روبوتات الدردشة و"المساعدون" لخدمة العملاء حيث يدفع المستخدمون سعرًا مميزًا ويتوقعون استجابات سريعة ومتسقة.
- **محركات اتخاذ القرارات في الوقت الفعلي**: الأنظمة التي تتطلب نتائج موثوقة جدًا ومنخفضة وقت الاستجابة
  ، مثل فرز التذاكر المباشر أو كشف الاحتيال.
- **ميزات العملاء المميزين**: المطوّرون الذين يحتاجون إلى ضمان أهداف مستوى خدمة أعلى للعملاء الذين يدفعون رسومًا.

### الحدود القصوى لمعدّل الاستخدام

[تخضع عمليات الاستهلاك ذات الأولوية لحدود قصوى لمعدّل الاستخدام خاصة بها، على الرغم من احتساب عمليات الاستهلاك ضمن الحدود القصوى لمعدّل استخدام الزيارات التفاعلية بشكل عام.](https://aistudio.google.com/rate-limit?hl=ar) الحدود القصوى التلقائية لمعدّل استخدام الاستنتاج ذي الأولوية هي **0.3 ضعف الحد الأقصى لمعدّل الاستخدام العادي للطراز / الطبقة**

### منطق الرجوع السلس

إذا تم تجاوز الحدود القصوى للأولوية بسبب الازدحام، يتم **تلقائيًا وبشكل سلس** الرجوع إلى المعالجة العادية للطلبات التي تتجاوز الحد الأقصى بدلاً من تعذُّر معالجتها بسبب ظهور الخطأ 503 أو 429. تتم فوترة الطلبات التي تم الرجوع إلى معالجتها بالسعر العادي، وليس بالسعر المميز للأولوية.

### مسؤولية العميل

- **مراقبة الردود**: على المطوّرين مراقبة `x-gemini-service-tier`
  العنوان في ردّ واجهة برمجة التطبيقات للكشف عمّا إذا كان يتم الرجوع بشكل متكرر إلى
  `standard`.
- **إعادة المحاولات**: على العملاء تنفيذ منطق إعادة المحاولة/التراجع الأسي لـ
  الأخطاء العادية، مثل `DEADLINE_EXCEEDED`.

## الأسعار

يتم تسعير الاستنتاج ذي الأولوية بنسبة %75 إلى %100 أكثر من [واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar) ويتم تحصيل الرسوم لكل رمز مميز.

## الطُرز المتوافقة

تسمح الطُرز التالية بالاستنتاج ذي الأولوية:

| الطراز | الاستنتاج ذو الأولوية |
| --- | --- |
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

يمكنك الاطّلاع على خيارات [الاستنتاج والتحسين](https://ai.google.dev/gemini-api/docs/optimization?hl=ar) الأخرى في Gemini:

- [الاستنتاج المرن](https://ai.google.dev/gemini-api/docs/flex-inference?hl=ar) لخفض التكلفة بنسبة% 50
- [واجهة برمجة التطبيقات المجمّعة](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) للمعالجة غير المتزامنة في غضون 24 ساعة
- [التخزين المؤقت للسياق](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل تكاليف الرموز المميّزة للإدخال

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-28 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
