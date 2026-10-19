---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa
fetched_at: 2026-10-19T05:43:03.275019+00:00
title: "\u0627\u0633\u062a\u0646\u0628\u0627\u0637 \u0627\u0648\u0644\u0648\u06cc\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# استنباط اولویت

توضیحات: با نحوه بهینه‌سازی تأخیر بااستفاده از سطح استنتاج «اولویت» در Interactions API آشنا شوید

Gemini Priority API یک سطح استنتاج ممتاز است که برای
حجم‌های کاری حیاتی کسب‌وکار طراحی شده است که به تأخیر کمتر و بالاترین
قابلیت اطمینان با قیمت ممتاز نیاز دارند. ترافیک سطح اولویت بالاتر از ترافیک سطح Flex و
میانای برنامه‌سازی کاربردی استاندارد اولویت‌بندی می‌شود.

استنباط اولویت‌دار در سراسر نقاط پایانی «میانای برنامه‌سازی کاربردی تعاملات» دردسترس است.

## نحوه استفاده از «اولویت»

برای استفاده از سطح «اولویت»، فیلد `service_tier` را در درخواستتان روی `priority` تنظیم کنید. اگر فیلد حذف شود، سطح پیش‌فرض استاندارد است.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.8-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ServiceTier;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Perform a priority inference task."))
        .serviceTier(ServiceTier.PRIORITY)
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### رفتن

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:       interactions.Model("gemini-3.8-flash"),
            Input:       interactions.NewInteractionsInput("Perform a priority inference task."),
            ServiceTier: interactions.ServiceTierPriority.ToPointer(),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### استراحت

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## نحوه عملکرد استنتاج «اولویت»

استنتاج اولویت‌دار درخواست‌ها را به صف‌های محاسباتی با اهمیت بالا هدایت می‌کند و عملکردی قابل‌پیش‌بینی و سریع برای برنامه‌های سَمت کاربر ارائه می‌دهد. سازوکار اصلی آن تنزل تدریجی سمت سرور به پردازش استاندارد برای ترافیکی است که از محدودیت‌های پویا فراتر می‌رود، که این امر پایداری برنامه را به‌جای رد کردن درخواست تضمین می‌کند.

| ویژگی | اولویت | استاندارد | به‌رخ کشیدن | دسته |
| --- | --- | --- | --- | --- |
| **قیمت‌گذاری** | ‫۷۵ تا ۱۰۰٪ بیشتر از «استاندارد» | قیمت کامل | ‫٪۵۰ تخفیف | ‫٪۵۰ تخفیف |
| **تأخیر** | ثانیه | ثانیه به دقیقه | دقیقه (هدف ۱ تا ۱۵ دقیقه) | حداکثر ۲۴ ساعت |
| **قابلیت اطمینان** | زیاد (غیرقابل ریزش) | زیاد / متوسط روبه‌بالا | نهایت تلاش (قابل‌حذف) | بالا (برای توان گذرداد) |
| **میانا** | همگام | هم‌زمان | همگام | غیرهمگام |

### مزایای کلیدی

- **تأخیر کم**: برای زمان‌های پاسخ ثانیه‌ای برای ابزارهای هوش مصنوعی تعاملی و کاربرپسند طراحی شده است.
- **قابلیت اطمینان بالا**: ترافیک با بالاترین سطح اهمیت حیاتی درنظر گرفته می‌شود و
  به‌هیچ‌وجه نباید حذف شود.
- **تنزل متین**: جهش‌های ترافیکی که از حدود پویا فراتر می‌روند، به‌جای اینکه ناموفق شوند، به‌طور خودکار به سطح «استاندارد» برای پردازش تنزل می‌یابند تا از قطعی سرویس جلوگیری شود.
- **اصطکاک کم**: از همان روش هم‌زمان `create` به‌عنوان سطوح استاندارد و Flex استفاده می‌کند.

### موارد استفاده

پردازش اولویت‌دار برای گردش کارهای حیاتی کسب‌وکار که در آن‌ها عملکرد و قابلیت اطمینان اهمیت زیادی دارد ایده‌آل است.

- **برنامه‌های هوش مصنوعی تعاملی**: روبات‌های گپ خدمات مشتری و دستیارهای هوش مصنوعی که در آن‌ها کاربران هزینه ممتاز پرداخت می‌کنند و انتظار دارند پاسخ‌های سریع و یکنواخت دریافت کنند.
- **موتورهای تصمیم‌گیری هم‌زمان**: سیستم‌هایی که به نتایج بسیار قابل‌اعتماد و با تأخیر کم نیاز دارند، مانند اولویت‌بندی زنده درخواست‌های پشتیبانی یا تشخیص کلاهبرداری.
- **ویژگی‌های مشتری ممتاز**: توسعه‌دهندگانی که باید اهداف سطح خدمات (SLO) بالاتری را برای مشتریان پولی تضمین کنند.

### محدودیت‌های نرخ

مصرف اولویت‌دار حد نرخ خودش را دارد، هرچند که مصرف در
[حد نرخ ترافیک تعاملی کلی](https://aistudio.google.com/rate-limit?hl=fa) حساب می‌شود. حدود نرخ پیش‌فرض
برای استنباط «اولویت‌دار» **۰٫۳ برابر حد نرخ استاندارد برای «مدل / سطح»** است

### منطق تنزل ایمن

اگر محدودیت‌های «اولویت» به‌دلیل ازدحام فراتر رود، درخواست‌های سرریز به‌جای ناموفق شدن با خطای ۵۰۳ یا ۴۲۹، **به‌طور خودکار و به‌آرامی** به پردازش «استاندارد» تنزل می‌یابند. درخواست‌های تنزل‌یافته با نرخ استاندارد صورت‌حساب می‌شوند، نه نرخ ممتاز «اولویت».

### مسئولیت کارخواه

- **پایش پاسخ**: توسعه‌دهندگان باید `x-gemini-service-tier`
  سرایند در پاسخ API را پایش کنند تا تشخیص دهند آیا درخواست‌ها به‌طور مکرر به
  `standard` تنزل داده می‌شوند یا نه.
- **تلاش‌های مجدد**: کارخواه‌ها باید منطق تلاش مجدد/پس‌گیری نمایی را برای خطاهای استاندارد، مثل `DEADLINE_EXCEEDED`، پیاده‌سازی کنند.

## قیمت‌گذاری

قیمت استنباط اولویت ۷۵ تا ۱۰۰٪ بیشتر از [میانای برنامه‌سازی کاربردی استاندارد](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) است و براساس تعداد نشان صورت‌حساب می‌شود.

## مدل‌های پشتیبانی‌شده

مدل‌های زیر از استنتاج «اولویت‌دار» پشتیبانی می‌کنند:

| مدل | استنتاج اولویت‌دار |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa) | ✔️ |
| [‫Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=fa) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=fa) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=fa) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=fa) | ✔️ |
| [پیش‌نمایش Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=fa) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=fa) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=fa) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=fa) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=fa) | ✔️ |

## قدم بعدی چیست

- [استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa) برای کاهش هزینه.
- [کدها](https://ai.google.dev/gemini-api/docs/tokens?hl=fa): با کدها آشنا شوید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی."],[],[]]
