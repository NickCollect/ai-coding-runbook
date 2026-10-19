---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=fa
fetched_at: 2026-10-19T05:43:44.270803+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# Gemini Robotics ER

مدل‌های Gemini Robotics ER (استدلال تجسمی) مدل‌های زبان-دیداری
(VLMs) هستند که به روبات‌ها امکان می‌دهند
دنیای فیزیکی را درک کنند و با آن تعامل داشته باشند. این ربات‌ها داده‌های دیداری را تفسیر می‌کنند، استدلال فضایی و زمانی انجام می‌دهند، تکالیف چندمرحله‌ای را برنامه‌ریزی می‌کنند، و ربات‌ها و ابزارها را هماهنگ می‌کنند.

## مدل‌ها

مدل Gemini Robotics ER 2 جدیدترین مدل در Gemini Robotics است.
این مدل استدلالی به‌روزشده ما است که به روبات‌ها امکان می‌دهد محیط اطرافشان را به‌دقت درک کنند. این مدل در قابلیت‌های استدلال تجسمی، مثل هماهنگی عاملان روبات‌ها (برای نمونه، بااستفاده از VLAs)، درک ویدیو روبات شامل درک پیشرفت و تشخیص موفقیت، خواندن ابزار، اشاره کردن، و استدلال فضایی تخصص دارد.

مدل Gemini Robotics ER 2 دو نقطه پایانی مدل را معرفی می‌کند:

- **‫`gemini-robotics-er-2-preview`**: مدل استاندارد ER 2. برپایه
  Gemini 3.5 Flash با استدلال فضایی بهبودیافته، یافتن لحظات ویدیو،
  طبقه‌بندی پیشرفت ویدیو، هماهنگی چندروباتی، و استفاده از ابزار چندمرحله‌ای.
- **`gemini-robotics-er-2-streaming-preview`**: بهینه‌سازی‌شده برای جاری‌سازی هم‌زمان بااستفاده از [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fa). از این مدل برای عامل‌های روبات با تأخیر کم استفاده کنید که ورودی صوتی و ویدیویی پیوسته را پردازش می‌کنند.

‫Gemini Robotics ER 1.6 در
[۳۱ اوت ۲۰۲۶ منسوخ شد](https://ai.google.dev/gemini-api/docs/deprecations?hl=fa#robotics-models).
اگر هنوز از Gemini Robotics ER 1.6 استفاده می‌کنید، با جایگزین کردن `model="gemini-robotics-er-1.6-preview"` با
`model="gemini-robotics-er-2-preview"` یا
`model="gemini-robotics-er-2-streaming-preview"` در فراخوانی‌های API، به Gemini Robotics ER 2 ارتقا دهید.

[امتحان کردن Gemini Robotics ER 2 در Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=fa)

## قابلیت‌های روباتیک

‫Gemini Robotics ER از طیف وسیعی از قابلیت‌های استدلال تجسمی پشتیبانی می‌کند.
برای کسب اطلاعات بیشتر، قابلیتی را انتخاب کنید:

| قابلیت | شرح | راهنما |
| --- | --- | --- |
| استدلال فضایی | به اشیا اشاره کنید، آن‌ها را در ویدیو ردیابی کنید، با چارگوش‌های محدودکننده تشخیص دهید، مسیرها را برنامه‌ریزی کنید. | [استدلال فضایی](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=fa) |
| بینایی عامل‌گرا | با بهره‌گیری از ابزارهای دستکاری تصویر، از اجرای کد برای بهبود قابلیت‌های دیگر استفاده کنید. | [بینش عامل‌گرا](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=fa) |
| هماهنگ‌سازی تکلیف | برای انجام تکالیف بلندمدت، استدلال فضایی را با میاناهای برنامه‌سازی کاربردی روبات سفارشی ترکیب کنید. | [هماهنگی تکلیف](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=fa) |
| جاری‌سازی (فقط نقطه پایانی جاری‌سازی Gemini Robotics ER 2) | جاری‌سازی دوطرفه برای کارگزاران روبات هم‌زمان با تأخیر کم فراخوانی تابع. | [جاری‌سازی برای روباتیک](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fa) |
| پیشرفت ویدیو (فقط Gemini Robotics ER 2) | یافتن لحظه و طبقه‌بندی پیشرفت از فیدهای ویدیو پیوسته. | [درک ویدیو](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fa) |

## قبل‌از شروع

مدل‌های Gemini Robotics ER ازطریق **Gemini Developer
API** دردسترس هستند. برای شروع، از
[Google AI Studio](https://aistudio.google.com/apikey?hl=fa) یا
[کنسول Google Cloud](https://ai.google.dev/gemini-api/docs/api-key?hl=fa#cloud-console)، [کلید Gemini API](https://ai.google.dev/gemini-api/docs/api-key?hl=fa) ایجاد کنید و
[محیطتان را راه‌اندازی کنید](https://ai.google.dev/gemini-api/docs/api-key?hl=fa#setup-environment).

برای جزئیات مربوط به انواع کلید، امنیت، و نحوه پیکربندی کلید در
Python،‏ JavaScript، و زبان‌های دیگر، به
[استفاده از کلیدهای میانای برنامه‌سازی کاربردی Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=fa) مراجعه کنید.

## درحال شروع کردن

مثال زیر اشیای موجود در تصویر را پیدا می‌کند و مختصات و برچسب‌های دوبعدی عادی‌سازی‌شده آن‌ها را برمی‌گرداند. می‌توانید این برونداد را مستقیماً به میانای برنامه‌سازی کاربردی روباتیک یا مدل
VLA منتقل کنید تا کنش‌های روبات را تولید کند.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const PROMPT = `
  Point to no more than 10 items in the image. The label returned
  should be an identifying name for the object detected.
  The answer should follow the json format: [{"point": <point>,
  "label": <label1>}, ...]. The points are in [y, x] format
  normalized to 0-1000.
`;
const client = new GoogleGenAI();

const uploadedFile = await client.files.upload({ file: "my-image.png" });

const imageResponse = await client.interactions.create({
  model: "gemini-robotics-er-2-preview",
  input: [
    {
      type: "image",
      uri: uploadedFile.uri,
      mime_type: uploadedFile.mimeType,
    },
    { type: "text", text: PROMPT },
  ],
  generation_config: { thinking_level: "high" },
});

console.log(imageResponse.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.List;

Client client = new Client();

String prompt =
    "Point to no more than 10 items in the image. The label returned "
        + "should be an identifying name for the object detected. "
        + "The answer should follow the json format: [{\"point\": <point>, "
        + "\"label\": <label1>}, ...]. The points are in [y, x] format "
        + "normalized to 0-1000.";

File uploadedFile =
    client.files.upload(
        new java.io.File("my-image.png"),
        UploadFileConfig.builder().mimeType("image/png").build());

Content imageContent =
    ImageContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/png")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-robotics-er-2-preview"))
        .input(InteractionsInput.ofContent(List.of(imageContent, textContent)))
        .generationConfig(
            GenerationConfig.builder().thinkingLevel(ThinkingLevel.HIGH).build())
        .build();

Interaction imageResponse =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(imageResponse.outputText().orElse(""));
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

    prompt := `Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": <point>,
"label": <label1>}, ...]. The points are in [y, x] format
normalized to 0-1000.`

    uploadedFile, err := client.Files.UploadFromPath(ctx, "my-image.png", &genai.UploadFileConfig{
        MIMEType: "image/png",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-robotics-er-2-preview"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: genai.Ptr(interactions.ImageMimeTypeImagePng),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
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

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

برونداد آرایه JSON حاوی اشیایی خواهد بود که هرکدام دارای `point`
(مختصات `[y, x]` عادی‌سازی‌شده) و `label` شناسایی‌کننده شیء است.

### (قالب) JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

تصویر زیر نمونه‌ای از نحوه نمایش این نقاط است:

![مثالی که نقاط اشیا را در تصویر نشان می‌دهد](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=fa)

## روش کار

‫Gemini Robotics ER با پیام‌واره‌های زبان طبیعی ورودی تصویر، ویدیو، یا صدا را دریافت می‌کند. این ویژگی اشیا را شناسایی می‌کند، درباره بافت صحنه و روابط فضایی استدلال می‌کند، و برونداد ساختاریافته‌ای مثل مختصات یا چارگوش‌های محدودکننده برمی‌گرداند.

‫Gemini Robotics ER همچنین عامل است: این مدل تکالیف پیچیده را به تکالیف فرعی تقسیم می‌کند و
با فراخوانی کردن عملکردهای ربات شما یا اجرای کد تولیدشده، آن‌ها را اجرا می‌کند. برای مثال، «سیب را در کاسه بگذار» به توالی مراحل مکان‌یابی، گرفتن، و
قرار دادن تبدیل می‌شود.

برای جزئیات نحوه اجرای تماس‌های ابزار توسط Gemini، [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=fa#how-it-works) را ببینید.

## ایمنی

اگرچه Gemini Robotics ER با درنظر گرفتن ایمنی ساخته شده است، اما مسئولیت شما است که محیطی ایمن در اطراف ربات حفظ کنید. مدل‌های هوش مصنوعی زایا ممکن است اشتباه کنند و روبات‌های فیزیکی ممکن است آسیب برسانند. برای کسب اطلاعات بیشتر،
به
[صفحه ایمنی «روباتیک Gemini»](https://deepmind.google/models/gemini-robotics/safety?hl=fa) مراجعه کنید.

## روال‌های مطلوب

1. از زبان ساده و طبیعی استفاده کنید. کاری را که می‌خواهید روبات انجام دهد همان‌طور که به یک شخص می‌گویید توصیف کنید. اگر اصطلاحی کار نمی‌کند، مترادف رایجی را امتحان کنید.
2. ورودی دیداری را بهینه کنید. پیش‌از ارسال تصویر، اشیای کوچک یا نامشخص را برش دهید یا زوم‌پیش کنید. نور و کنتراست رنگ پایین می‌تواند روی تشخیص تأثیر بگذارد.
3. تکالیف پیچیده را به مراحل تقسیم کنید. هر مرحله را به‌عنوان پیام‌واره جداگانه‌ای ارسال کنید تا مدل متمرکز بماند و دقت بهبود یابد.
4. برای کارهای با دقت بالا، چندین بار پُرسمان کنید و نتایج را میانگین بگیرید. این رویکرد اجماعی باعث کاهش تغییرات در بروندادهای فضایی می‌شود.

## محدودیت‌ها

هنگام توسعه با Gemini Robotics ER، محدودیت‌های زیر را درنظر بگیرید:

- **محدودیت‌های کلید API:** «میانای برنامه‌سازی کاربردی Gemini» درخواست‌های کلیدهای API بدون محدودیت را نمی‌پذیرد و خطای `403 Forbidden` برمی‌گرداند. با افزودن محدودیت‌ها در [AI Studio](https://aistudio.google.com/api-keys?hl=fa)، کلید API خود را ایمن کنید.
  برای جزئیات، [کلیدهای API نامحدود ایمن](https://ai.google.dev/gemini-api/docs/api-key?hl=fa#secure-unrestricted-keys)
  را ببینید.
- **تأخیر دربرابر عملکرد:** پُرسمان‌های پیچیده، ورودی‌های با وضوح بالا، یا سطوح بالای
  تفکر می‌تواند منجر به افزایش زمان پردازش شود. برای سطح تفکر
  از متوسط برای ایجاد تعادل خوب بین تأخیر و عملکرد استفاده کنید.
- **توهمات:** مانند همه مدل‌های زبانی بزرگ، مدل‌های Gemini Robotics ER
  گاهی اوقات می‌توانند «توهم» داشته باشند یا اطلاعات نادرست ارائه دهند،
  به‌ویژه برای پیام‌واره‌های مبهم یا ورودی‌های خارج از توزیع.
- **وابستگی به کیفیت پیام‌واره:** کیفیت برونداد به وضوح پیام‌واره ورودی بستگی دارد. از پیام‌واره‌های مشخص و خوش‌ساخت استفاده کنید.
- **هزینه محاسباتی:** اجرای مدل، به‌ویژه با ورودی‌های ویدیویی یا
  `thinking_budget` بالا، منابع محاسباتی را مصرف می‌کند و هزینه‌هایی را به‌همراه دارد.
  برای جزئیات بیشتر، صفحه [تفکر](https://ai.google.dev/gemini-api/docs/thinking?hl=fa) را ببینید.
- **انواع ورودی:** برای جزئیات مربوط به محدودیت‌های هر حالت، موضوعات زیر را ببینید.
  - [ورودی‌های تصویر](https://ai.google.dev/gemini-api/docs/image-understanding?hl=fa#technical-details-image)
  - [ورودی‌های ویدیو](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa#supported-formats)
  - [ورودی‌های صوتی](https://ai.google.dev/gemini-api/docs/audio?hl=fa#supported-formats)

## اعلامیه حریم خصوصی

تصدیق می‌کنید که مدل‌های ارجاع‌شده در این سند («مدل‌های رباتیک») از داده‌های ویدیویی و صوتی برای عملکرد و حرکت سخت‌افزار شما مطابق با دستورالعمل‌هایتان استفاده می‌کنند. بنابراین ممکن است «مدل‌های رباتیک» را به‌گونه‌ای به‌کار ببرید که داده‌های افراد قابل‌شناسایی، مثل صدا، تصاویر، و داده‌های شباهت («داده‌های شخصی») توسط «مدل‌های رباتیک» جمع‌آوری شود. اگر انتخاب کنید «مدل‌های رباتیک» را به روشی که «داده‌های شخصی» را جمع‌آوری می‌کند اداره کنید، موافقت می‌کنید که به هیچ فرد قابل‌شناسایی اجازه ندهید با «مدل‌های رباتیک» تعامل داشته باشد یا در اطراف آن حضور داشته باشد، مگر اینکه و تا زمانی که به این افراد قابل‌شناسایی به‌اندازه کافی اطلاع داده شود و آن‌ها موافقت کنند که «داده‌های شخصی» آن‌ها ممکن است طبق آنچه در «شرایط خدمات تکمیلی Gemini API» در [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=fa) (این «شرایط») آمده است، ازجمله مطابق با بخش با عنوان «Google چگونه از داده‌های شما استفاده می‌کند»، به Google ارائه شود و Google از آن استفاده کند. تضمین می‌کنید که چنین
اعلامیه‌ای اجازه جمع‌آوری و استفاده از «داده‌های شخصی» را همان‌گونه که در «شرایط» ذکر شده است می‌دهد،
و تا حد امکان از تلاش‌های تجاری معقولی برای به‌حداقل رساندن جمع‌آوری و
توزیع «داده‌های شخصی» بااستفاده از فنونی مانند محو کردن چهره و
به‌کارگیری «مدل‌های رباتیک» در مناطقی که حاوی افراد قابل‌شناسایی نیستند استفاده خواهید کرد.

## قیمت‌گذاری

برای اطلاعات دقیق درباره قیمت‌گذاری و مناطق دردسترس، به صفحه
[قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa) مراجعه کنید.

## نقطه‌های پایان مدل

### پیش‌نمایش Gemini Robotics ER 2

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | `gemini-robotics-er-2-preview` |
| انواع داده‌های پشتیبانی‌شده برای ذخیره کردن | **ورودی‌ها**  نوشتار، تصاویر، ویدیو، صدا  **برونداد**  نوشتار |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **محدودیت داده‌واحد ورودی**  ۱۳۱٬۰۷۲  **محدودیت داده‌واحد برونداد**  ۶۵۵۳۶ |
| ‫handymanقابلیت‌ها | **[تولید صدا](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa)**  پشتیبانی نمی‌شود  **[ذخیره در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa)**  پشتیبانی‌شده  **[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)**  پشتیبانی‌شده  **[استفاده از رایانه](https://ai.google.dev/gemini-api/docs/computer-use?hl=fa)**  پشتیبانی‌شده  **[جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)**  پشتیبانی‌شده  **[فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)**  پشتیبانی‌شده  **[پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa)**  پشتیبانی‌شده  **[تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)**  پشتیبانی نمی‌شود  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=fa)**  پشتیبانی نمی‌شود  **[زمینه‌سازی جستجو](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)**  پشتیبانی‌شده  **[بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa)**  پشتیبانی‌شده  **[درحال فکر کردن](https://ai.google.dev/gemini-api/docs/thinking?hl=fa)**  پشتیبانی‌شده  **[بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)**  پشتیبانی‌شده |
| ‫speedگزینه‌های مصرف | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa)**  پشتیبانی‌شده  **[استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa)**  پشتیبانی نمی‌شود  **[استنباط اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa)**  پشتیبانی نمی‌شود |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa#model-versions) را بخوانید.  - پیش‌نمایش: `gemini-robotics-er-2-preview` |
| calendar\_monthآخرین به‌روزرسانی | ژوئیه ۲۰۲۶ |
| کارت id\_cardمدل | [کارت مدل](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fa) |

### پیش‌نمایش جاری‌سازی Gemini Robotics ER 2

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | `gemini-robotics-er-2-streaming-preview` |
| انواع داده‌های پشتیبانی‌شده برای ذخیره کردن | **ورودی‌ها**  نوشتار، تصاویر، ویدیو، صدا  **برونداد**  نوشتار |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **محدودیت داده‌واحد ورودی**  ۱۳۱٬۰۷۲  **محدودیت داده‌واحد برونداد**  ۶۵۵۳۶ |
| ‫handymanقابلیت‌ها | **[تولید صدا](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa)**  پشتیبانی نمی‌شود  **[ذخیره در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa)**  پشتیبانی نمی‌شود  **[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)**  پشتیبانی نمی‌شود  **[استفاده از رایانه](https://ai.google.dev/gemini-api/docs/computer-use?hl=fa)**  پشتیبانی نمی‌شود  **[جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)**  پشتیبانی نمی‌شود  **[فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)**  پشتیبانی‌شده  **[پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa)**  پشتیبانی نمی‌شود  **[تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)**  پشتیبانی نمی‌شود  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=fa)**  پشتیبانی‌شده  **[زمینه‌سازی جستجو](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)**  پشتیبانی‌شده  **[بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa)**  پشتیبانی نمی‌شود  **[درحال فکر کردن](https://ai.google.dev/gemini-api/docs/thinking?hl=fa)**  پشتیبانی‌شده  **[بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)**  پشتیبانی نمی‌شود |
| ‫speedگزینه‌های مصرف | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa)**  پشتیبانی نمی‌شود  **[استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa)**  پشتیبانی نمی‌شود  **[استنباط اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa)**  پشتیبانی نمی‌شود |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa#model-versions) را بخوانید.  - پیش‌نمایش: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthآخرین به‌روزرسانی | ژوئیه ۲۰۲۶ |
| کارت id\_cardمدل | [کارت مدل](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=fa) |

### پیش‌نمایش Gemini Robotics ER 1.6

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | `gemini-robotics-er-1.6-preview` |
| انواع داده‌های پشتیبانی‌شده برای ذخیره کردن | **ورودی‌ها**  نوشتار، تصاویر، ویدیو، صدا  **برونداد**  نوشتار |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **محدودیت داده‌واحد ورودی**  ۱۳۱٬۰۷۲  **محدودیت داده‌واحد برونداد**  ۶۵۵۳۶ |
| ‫handymanقابلیت‌ها | **[تولید صدا](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa)**  پشتیبانی نمی‌شود  **[ذخیره در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa)**  پشتیبانی‌شده  **[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)**  پشتیبانی‌شده  **[استفاده از رایانه](https://ai.google.dev/gemini-api/docs/computer-use?hl=fa)**  پشتیبانی‌شده  **[جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)**  پشتیبانی‌شده  **[فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)**  پشتیبانی‌شده  **[پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa)**  پشتیبانی‌شده  **[تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)**  پشتیبانی نمی‌شود  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=fa)**  پشتیبانی نمی‌شود  **[زمینه‌سازی جستجو](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)**  پشتیبانی‌شده  **[بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa)**  پشتیبانی‌شده  **[درحال فکر کردن](https://ai.google.dev/gemini-api/docs/thinking?hl=fa)**  پشتیبانی‌شده  **[بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)**  پشتیبانی‌شده |
| ‫speedگزینه‌های مصرف | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa)**  پشتیبانی‌شده  **[استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa)**  پشتیبانی نمی‌شود  **[استنباط اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa)**  پشتیبانی نمی‌شود |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models/gemini?hl=fa#model-versions) را بخوانید.  - پیش‌نمایش: `gemini-robotics-er-1.6-preview` |
| calendar\_monthآخرین به‌روزرسانی | دسامبر ۲۰۲۵ |
| cognition\_2تاریخ برش دانش | ژانویه ۲۰۲۵ |

## قدم بعدی چیست

- [استدلال فضایی](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=fa) — اشاره کردن، ردیابی کردن، چارگوش‌های محصورکننده، مسیرها.
- [قابلیت‌های عامل‌گرایی](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=fa) — اجرای کد، خواندن ابزار، حاشیه‌نویسی تصویر.
- [هماهنگ‌سازی تکلیف](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=fa) — تکالیف بلندمدت با APIهای سفارشی ربات.
- [روباتیک با جاری‌سازی](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=fa) — جاری‌سازی دوطرفه هم‌زمان (فقط Gemini Robotics ER 2).
- [درک ویدیو](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=fa) — یافتن لحظه و طبقه‌بندی پیشرفت (فقط Gemini Robotics ER 2).
- [ایمنی Gemini Robotics](https://deepmind.google/models/gemini-robotics/safety?hl=fa) — پژوهش ایمنی پشت خانواده مدل.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-06 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-06 به‌وقت ساعت هماهنگ جهانی."],[],[]]
