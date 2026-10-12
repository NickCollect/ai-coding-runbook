---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/priority-inference?hl=fa
fetched_at: 2026-10-12T06:50:05.853865+00:00
title: "\u0627\u0633\u062a\u0646\u0628\u0627\u0637 \u0627\u0648\u0644\u0648\u06cc\u062a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash اکنون در دسترس است. [آن را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fa) .

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# استنباط اولویت

شرح: با لایه استنباط «اولویت‌دار»، نحوه بهینه‌سازی تأخیر را بیاموزید

‫Gemini Priority API سطح استنباط ممتاز است که برای حجم‌های کاری حیاتی کسب‌وکار طراحی شده است و در ازای قیمت ممتاز، تأخیر پایین‌تر و بالاترین قابلیت اطمینان را ارائه می‌دهد. ترافیک سطح اولویت بالاتر از ترافیک سطح Flex و
میانای برنامه‌سازی کاربردی استاندارد اولویت‌بندی می‌شود.

استنباط اولویت برای کاربران [سطح ۲ و سطح ۳](https://ai.google.dev/gemini-api/docs/billing?hl=fa#about-billing) در سراسر نقاط پایانی «میانای برنامه‌سازی کاربردی GenerateContent»
و «میانای برنامه‌سازی کاربردی Interactions» دردسترس است.

## نحوه استفاده از «اولویت»

برای استفاده از سطح «اولویت‌دار»، فیلد `service_tier` را در بدنه درخواست روی
`priority` تنظیم کنید. اگر این فیلد حذف شود، سطح پیش‌فرض استاندارد است.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
          model: "gemini-3.8-flash",
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

### رفتن

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
        "gemini-3.8-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Analyze user sentiment in real time"}]
  }],
  "service_tier": "priority"
}'
```

## نحوه عملکرد استنباط «اولویت»

استنتاج اولویت درخواست‌ها را به صف‌های محاسباتی با اهمیت بالا هدایت می‌کند و
عملکرد سریع و قابل‌پیش‌بینی برای برنامه‌های سَمت کاربر ارائه می‌دهد. سازوکار اصلی آن
تنزل سطح سمت سرور به‌صورت تدریجی به پردازش استاندارد برای ترافیکی است که
از حدود پویا فراتر می‌رود، و به‌جای رد کردن درخواست، پایداری برنامه را تضمین می‌کند.

| ویژگی | اولویت | استاندارد | به‌رخ کشیدن | دسته |
| --- | --- | --- | --- | --- |
| **قیمت‌گذاری** | ‫۷۵ تا ۱۰۰٪ بیشتر از «استاندارد» | قیمت کامل | ‫٪۵۰ تخفیف | ‫٪۵۰ تخفیف |
| **تأخیر** | ثانیه | ثانیه به دقیقه | دقیقه (هدف ۱ تا ۱۵ دقیقه) | حداکثر ۲۴ ساعت |
| **قابلیت اطمینان** | زیاد (غیرقابل ریزش) | زیاد / متوسط روبه‌بالا | نهایت تلاش (قابل‌حذف) | بالا (برای توان گذرداد) |
| **میانای** | هم‌زمان | هم‌زمان | هم‌زمان | غیرهمگام |

### مزایای کلیدی

- **تأخیر کم**: برای زمان‌های پاسخ ثانیه‌ای برای ابزارهای هوش مصنوعی تعاملی و کاربرپسند طراحی شده است.
- **قابلیت اطمینان بالا**: ترافیک با بالاترین سطح اهمیت حیاتی درنظر گرفته می‌شود و
  به‌هیچ‌وجه نباید حذف شود.
- **تنزل تدریجی**: افزایش ناگهانی ترافیک که از حدود پویا فراتر می‌رود به‌طور خودکار به سطح «استاندارد» برای پردازش تنزل داده می‌شود و از خرابی جلوگیری می‌کند و مانع از قطعی سرویس می‌شود.
- **اصطکاک کم**: از همان روش هم‌زمان `generateContent` به‌عنوان سطوح استاندارد و Flex استفاده می‌کند.

### موارد استفاده

پردازش اولویت‌دار برای گردش کارهای حیاتی کسب‌وکار که در آن‌ها عملکرد و قابلیت اطمینان اهمیت زیادی دارد ایده‌آل است.

- **برنامه‌های هوش مصنوعی تعاملی**: روبات‌های گپ خدمات مشتری و دستیارهای هوش مصنوعی که در آن‌ها کاربران هزینه ممتاز پرداخت می‌کنند و انتظار دارند پاسخ‌های سریع و یکنواخت دریافت کنند.
- **موتورهای تصمیم‌گیری هم‌زمان**: سیستم‌هایی که به نتایج بسیار قابل‌اعتماد و با تأخیر کم نیاز دارند، مانند اولویت‌بندی زنده درخواست‌های پشتیبانی یا تشخیص کلاهبرداری.
- **ویژگی‌های مشتری ممتاز**: توسعه‌دهندگانی که باید اهداف سطح خدمات (SLO) بالاتری را برای مشتریان پولی تضمین کنند.

### محدودیت‌های نرخ

مصرف اولویت‌دار نرخ محدودیت‌های خود را دارد، حتی اگر مصرف در [محدودیت‌های نرخ ترافیک تعاملی کلی](https://aistudio.google.com/rate-limit?hl=fa) محاسبه شود. حدود نرخ پیش‌فرض
برای استنباط «اولویت‌دار» **۰٫۳ برابر حد نرخ استاندارد برای «مدل / سطح»** است

### منطق تنزل ایمن

اگر به‌دلیل ازدحام، از حدود «اولویت» فراتر بروید، درخواست‌های سرریز به‌جای اینکه با خطای ۵۰۳ یا ۴۲۹ ناموفق شوند، **به‌طور خودکار و به‌نحوی مناسب** به پردازش «استاندارد» تنزل داده می‌شوند. هزینه درخواست‌های تنزل‌یافته براساس نرخ استاندارد محاسبه می‌شود، نه نرخ ممتاز «اولویت‌دار».

### مسئولیت کارخواه

- **پایش پاسخ**: توسعه‌دهندگان باید `x-gemini-service-tier`
  سرایند در پاسخ API را پایش کنند تا تشخیص دهند آیا درخواست‌ها به‌طور مکرر به
  `standard` تنزل داده می‌شوند یا نه.
- **تلاش‌های مجدد**: کارخواه‌ها باید منطق تلاش مجدد/پس‌گیری نمایی را برای خطاهای استاندارد، مثل `DEADLINE_EXCEEDED`، پیاده‌سازی کنند.

## قیمت‌گذاری

قیمت استنباط اولویت ۷۵ تا ۱۰۰٪ بیشتر از [میانای برنامه‌سازی کاربردی استاندارد](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) است و براساس تعداد نشان صورت‌حساب می‌شود.

## مدل‌های پشتیبانی‌شده

مدل‌های زیر از «استنباط اولویت‌دار» پشتیبانی می‌کنند:

| مدل | استنباط اولویت |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fa) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fa) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fa) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fa) | ✔️ |
| [پیش‌نمایش تصویر Gemini 3 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=fa) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fa) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fa) | ✔️ |
| [تصویر Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=fa) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fa) | ✔️ |

## قدم بعدی چیست

درباره سایر گزینه‌های [استنباط و بهینه‌سازی](https://ai.google.dev/gemini-api/docs/optimization?hl=fa) Gemini بخوانید:

- برای کاهش ۵۰٪ هزینه، از [استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa) استفاده کنید.
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa) برای پردازش ناهمزمان در عرض ۲۴ ساعت.
- [ذخیره کردن بافت در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa) برای کاهش هزینه‌های کد ورودی.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی."],[],[]]
