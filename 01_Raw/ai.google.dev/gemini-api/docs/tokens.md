---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=fa
fetched_at: 2026-10-26T05:42:25.206268+00:00
title: "\u062f\u0631\u06a9 \u0648 \u0634\u0645\u0627\u0631\u0634 \u0646\u0634\u0627\u0646\u200c\u0647\u0627 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# درک و شمارش نشان‌ها

‫Gemini و دیگر مدل‌های هوش مصنوعی زایا ورودی و خروجی را در سطح جزئیاتی به نام *نماد* پردازش می‌کنند.

**برای مدل‌های Gemini، یک نشان معادل حدود ۴ نویسه است.
‫۱۰۰ نشانه تقریباً برابر با ۶۰ تا ۸۰ کلمه انگلیسی است.**

## درباره داده‌واحدها

نشان‌ها می‌توانند نویسه‌های تکی مانند `z` یا کلمات کامل مانند `cat` باشند. کلمات طولانی
به چند کد تقسیم می‌شوند. مجموعه همه نشانه‌هایی که مدل استفاده می‌کند
واژگان نامیده می‌شود و فرایند تقسیم نوشتار به نشانه‌ها
*نشانه‌گذاری* نامیده می‌شود.

وقتی صورت‌حساب فعال باشد، [هزینه فراخوانی Gemini API](https://ai.google.dev/pricing?hl=fa) تاحدودی براساس تعداد کدهای ورودی و خروجی تعیین می‌شود، بنابراین دانستن نحوه شمارش کدها می‌تواند مفید باشد.

## شمارش داده‌واحدها

همه ورودی‌ها و خروجی‌های Gemini API، ازجمله نوشتار، فایل‌های تصویری، و دیگر حالت‌های غیرنوشتاری، نشان‌گذاری می‌شوند.

می‌توانید نشان‌ها را به روش‌های زیر بشمارید:

- **با ورودی درخواست، با `count_tokens` تماس بگیرید.** تعداد کل
  نشانه‌ها را *فقط در ورودی* برمی‌گرداند. این تماس را قبل‌از ارسال ورودی برقرار کنید
  تا اندازه درخواست‌هایتان را بررسی کنید.
- **از `usage` در پاسخ تعامل استفاده کنید.** تعداد داده‌واحد را برای ورودی (`total_input_tokens`)، خروجی (`total_output_tokens`)،
  تفکر (`total_thought_tokens`)، محتوای ذخیره‌شده در حافظه نهان
  (`total_cached_tokens`)، استفاده از ابزار (`total_tool_use_tokens`)،
  و کل (`total_tokens`) برمی‌گرداند.

### شمارش داده‌واحدهای نوشتار

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

# Count tokens before sending
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=prompt
)
print("total_tokens:", total_tokens.total_tokens)

# Get usage from interaction
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=prompt
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: prompt,
});
console.log(countResponse.totalTokens);

// Get usage from interaction
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: prompt,
});
console.log(interaction.usage);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.CountTokensResponse;

Client client = new Client();
String prompt = "The quick brown fox jumps over the lazy dog.";

// Count tokens before sending
CountTokensResponse countResponse =
    client.models.countTokens("gemini-3.8-flash", prompt, null);
System.out.println("total_tokens: " + countResponse.totalTokens().orElse(0));

// Get usage from interaction
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
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

    modelInfo, err := client.Models.Get(ctx, "gemini-3.8-flash", nil)
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Input token limit: %d\n", modelInfo.InputTokenLimit)
    fmt.Printf("Output token limit: %d\n", modelInfo.OutputTokenLimit)
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:countTokens" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents": [{"parts": [{"text": "The quick brown fox."}]}]}'
```

### شمردن داده‌واحدهای چندنوبتی

شمارش نشان‌ها در سابقه مکالمه بااستفاده از `previous_interaction_id`:

### Python

```
# This will only work for SDK newer than 2.0.0
# First interaction
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hi, my name is Bob"
)

# Second interaction continues the conversation
interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's my name?",
    previous_interaction_id=interaction1.id
)

# Usage includes tokens from both turns
print(f"Input tokens: {interaction2.usage.total_input_tokens}")
print(f"Output tokens: {interaction2.usage.total_output_tokens}")
print(f"Total tokens: {interaction2.usage.total_tokens}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
// First interaction
const interaction1 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Hi, my name is Bob"
});

// Second interaction continues the conversation
const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What's my name?",
    previous_interaction_id: interaction1.id
});

console.log(`Input tokens: ${interaction2.usage.total_input_tokens}`);
console.log(`Output tokens: ${interaction2.usage.total_output_tokens}`);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// First interaction
CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Hi, my name is Bob"))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Second interaction continues the conversation
CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What's my name?"))
        .previousInteractionId(interaction1.id().orElse(""))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Usage includes tokens from both turns
if (interaction2.usage().isPresent()) {
  Usage usage = interaction2.usage().get();
  System.out.println("Input tokens: " + usage.totalInputTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
  System.out.println("Total tokens: " + usage.totalTokens().orElse(0));
}
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

    prompt := "The quick brown fox jumps over the lazy dog."

    // Count input tokens before sending
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", genai.Text(prompt), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("total_tokens: %d\n", totalTokens.TotalTokens)

    // Create the interaction and inspect the returned usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(prompt),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil {
        if interaction.Usage.TotalInputTokens != nil {
            fmt.Printf("Input tokens: %d\n", *interaction.Usage.TotalInputTokens)
        }
        if interaction.Usage.TotalOutputTokens != nil {
            fmt.Printf("Output tokens: %d\n", *interaction.Usage.TotalOutputTokens)
        }
        if interaction.Usage.TotalThoughtTokens != nil {
            fmt.Printf("Thought tokens: %d\n", *interaction.Usage.TotalThoughtTokens)
        }
        if interaction.Usage.TotalTokens != nil {
            fmt.Printf("Total tokens: %d\n", *interaction.Usage.TotalTokens)
        }
    }
}
```

### شمارش داده‌واحدهای چندحالته

همه ورودی‌های Gemini API، ازجمله تصاویر، ویدیو، و صدا، نشان‌گذاری می‌شوند.
نکات کلیدی درباره نشانه‌گذاری:

- **تصاویر**: تصاویر ≤۳۸۴ پیکسل در هر دو بُعد به‌عنوان ۲۵۸ کد درنظر گرفته می‌شوند. تصاویر بزرگ‌تر به کاشی‌های ۷۶۸×۷۶۸ پیکسلی تقسیم می‌شوند و هر کاشی به‌عنوان ۲۵۸ نشانه محسوب می‌شود.
- **ویدیو**: ۲۶۳ واحد در ثانیه (برای پردازش ایستا اعمال می‌شود). برای پردازش
  عاملی، مصرف داده‌واحد متفاوت است. [استفاده از کد ویدیویی براساس حالت پردازش](#video-token-usage) را ببینید.
- **صدا**: ۳۲ داده‌واحد در ثانیه

#### نشانه‌های تصویر

### Python

```
# This will only work for SDK newer than 2.0.0
uploaded_file = client.files.upload(file="path/to/image.jpg")

# Count tokens for image + text
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Tell me about this image", uploaded_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with image
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Tell me about this image"},
        {"type": "image", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type}
    ]
)
print(interaction.usage)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const uploadedFile = await client.files.upload({
    file: "path/to/image.jpg",
    config: { mimeType: "image/jpeg" }
});

// Count tokens
const countResponse = await client.models.countTokens({
    model: "gemini-3.8-flash",
    contents: [
        { text: "Tell me about this image" },
        { fileData: { fileUri: uploadedFile.uri, mimeType: uploadedFile.mimeType } }
    ]
});
console.log(countResponse.totalTokens);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.Content;
import com.google.genai.types.CountTokensResponse;
import com.google.genai.types.File;
import com.google.genai.types.Part;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("path/to/image.jpg"),
        UploadFileConfig.builder().mimeType("image/jpeg").build());

// Count tokens for image + text
CountTokensResponse countResponse =
    client.models.countTokens(
        "gemini-3.8-flash",
        Arrays.asList(
            Content.fromParts(
                Part.fromText("Tell me about this image"),
                Part.fromUri(
                    uploadedFile.uri().orElse(""), uploadedFile.mimeType().orElse("image/jpeg")))),
        null);
System.out.println("Total tokens: " + countResponse.totalTokens().orElse(0));

// Generate with image
CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    TextContent.builder().text("Tell me about this image").build(),
                    ImageContent.builder()
                        .uri(uploadedFile.uri().orElse(""))
                        .mimeType(
                            ImageContentMimeType.of(uploadedFile.mimeType().orElse("image/jpeg")))
                        .build())))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.usage().orElse(null));
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
            Model:  interactions.Model("gemini-3.8-flash"),
            Input:  interactions.NewInteractionsInput("Explain the history of the internet in 3 paragraphs."),
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
        if completed := event.GetDataInteractionCompleted(); completed != nil {
            usage := completed.Interaction.Usage
            if usage != nil && usage.TotalTokens != nil {
                fmt.Printf("\nTotal tokens: %d\n", *usage.TotalTokens)
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

**نمونه داده‌های درون‌خطی:**

### Python

```
# This will only work for SDK newer than 2.0.0
import base64

with open('image.jpg', 'rb') as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode('utf-8'),
            "mime_type": "image/jpeg"
        }
    ]
)
print(interaction.usage)
```

#### داده‌واحدهای ویدیو

### Python

```
# This will only work for SDK newer than 2.0.0
import time

video_file = client.files.upload(file="path/to/video.mp4")

while not video_file.state or video_file.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    video_file = client.files.get(name=video_file.name)

# A 60-second video is approximately 100 * 60 = 6,000 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Summarize this video", video_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with video
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Summarize this video"},
        {"type": "video", "uri": video_file.uri, "mime_type": video_file.mime_type}
    ]
)
print(interaction.usage)
```

#### استفاده از کد ویدیویی براساس حالت پردازش

استفاده از نشان برای ویدیو به حالت پردازش بستگی دارد:

| **حالت پردازش** | **محاسبه داده‌واحد** | **استفاده معمول** |
| --- | --- | --- |
| **ثابت** (پیش‌فرض) | به‌طور پیش‌فرض حدود ۱۰۰ نشانه در ثانیه (وضوح پایین) یا حدود ۳۰۰ نشانه در ثانیه (وضوح بالا). همه فریم‌ها با نرخ ۱ فریم در ثانیه نمونه‌برداری شده‌اند. | قابل پیش‌بینی، متناسب با مدت‌زمان ویدیو. |
| **عاملی** | بسته به پیچیدگی محتوا متفاوت است. مدل فقط ترانویسی و/یا قاب‌ها و/یا صدای موردنیاز برای پاسخ دادن به پیام‌واره را بار می‌کند. | تا ۸۸٪ کمتر برای محتوای بلند. |

با پردازش عاملی، یک سخنرانی ۱ ساعته که در حالت ایستا از حدود ۱٫۰۸ میلیون نشانه استفاده می‌کند، بسته به پیام‌واره و محتوا، ممکن است از حدود ۱۰۸ هزار نشانه استفاده کند.

برای بررسی استفاده واقعی از نشان برای درخواست، `interaction.usage` را بازرسی کنید. نشان‌های ویدیو نماینده در فیلدهای زیر گزارش می‌شوند:

- **پیام‌واره اولیه** (مرجع ویدیو + پیام‌واره کاربر): `total_input_tokens`
- **تفکر پیمایش**: `total_thought_tokens`
- **ترانویسی، قاب‌ها، و صدا درصورت درخواست بار می‌شود**: `total_tool_use_tokens`
- **پاسخ نهایی**: `total_output_tokens`

#### نشان‌های صوتی

### Python

```
# This will only work for SDK newer than 2.0.0
audio_file = client.files.upload(file="path/to/audio.mp3")

# A 60-second audio clip is approximately 32 * 60 = 1,920 tokens
total_tokens = client.models.count_tokens(
    model="gemini-3.8-flash",
    contents=["Transcribe this audio", audio_file]
)
print(f"Total tokens: {total_tokens}")

# Generate with audio
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Transcribe this audio"},
        {"type": "audio", "uri": audio_file.uri, "mime_type": audio_file.mime_type}
    ]
)
print(interaction.usage)
```

### تعداد داده‌واحدهای دستورالعمل سیستم

دستورالعمل‌های سیستم به‌عنوان بخشی از داده‌واحدهای ورودی شمرده می‌شوند:

### Python

```
# This will only work for SDK newer than 2.0.0
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello!",
    system_instruction="You are a helpful assistant who speaks like a pirate."
)

# system_instruction tokens included in total_input_tokens
print(f"Input tokens: {interaction.usage.total_input_tokens}")
```

### شمارش داده‌واحدهای ابزار

ابزارها (تابع‌ها، اجرای کد، «جستجوی Google») نیز محاسبه می‌شوند:

### Python

```
# This will only work for SDK newer than 2.0.0
tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"}
            }
        }
    }
]

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What's the weather in Tokyo?",
    tools=tools
)

print(f"Input tokens: {interaction.usage.total_input_tokens}")
print(f"Tool use tokens: {interaction.usage.total_tool_use_tokens}")
```

## پنجره بافت

هر مدل Gemini حداکثر تعداد توکنی دارد که می‌تواند پردازش کند.

- **مدل‌های Gemini 4 (`gemini-4-argon`):** پنجره زمینه‌ای ۱ میلیون داده‌واحد (`1,048,576` داده‌واحد) را در داده‌واحد ورودی، داده‌واحد فکر کردن، و داده‌واحد برونداد هم‌رسانی می‌کنند. به‌طور پیش‌فرض، پاسخ‌های همگام (`background=False`، جاری‌سازی یا غیرجاری‌سازی) به `65,536` کد واحد خروجی محدود می‌شوند، یا می‌توانید بااستفاده از [رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/long-decode?hl=fa) تا `1,048,576` کد واحد تولید کنید. اگر داده‌واحدهای ورودی شما به‌علاوه `max_output_tokens` از ۱٬۰۴۸٬۵۷۶ داده‌واحد بیشتر شود، API به‌طور خودکار حد برونداد را به فضای باقی‌مانده در پنجره بافت (`1,048,576` منهای داده‌واحدهای ورودی شما) محدود می‌کند.
- **مدل‌های Gemini 3 و 2.5:** از بودجه‌های ورودی (`1,048,576` کد) و خروجی (`65,536` کد) جداگانه استفاده می‌کنند.

### دریافت اندازه پنجره زمینه‌ای به‌صورت برنامه‌ریزی‌شده

### Python

```
# This will only work for SDK newer than 2.0.0
model_info = client.models.get(model="gemini-3.8-flash")
print(f"Input token limit: {model_info.input_token_limit}")
print(f"Output token limit: {model_info.output_token_limit}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
const modelInfo = await client.models.get({ model: "gemini-3.8-flash" });
console.log(`Input token limit: ${modelInfo.inputTokenLimit}`);
console.log(`Output token limit: ${modelInfo.outputTokenLimit}`);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.types.Model;

Client client = new Client();

Model modelInfo = client.models.get("gemini-3.8-flash", null);
System.out.println("Input token limit: " + modelInfo.inputTokenLimit().orElse(0));
System.out.println("Output token limit: " + modelInfo.outputTokenLimit().orElse(0));
```

### رفتن

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    prompt := "Tell me about this instrument"
    imageBytes, err := os.ReadFile("/path/to/organ.jpg")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    // Count tokens before creating the interaction
    parts := []*genai.Part{
        genai.NewPartFromText(prompt),
        genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    }
    totalTokens, err := client.Models.CountTokens(ctx, "gemini-3.8-flash", []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Estimated input tokens: %d\n", totalTokens.TotalTokens)

    // Create the multimodal interaction and inspect the usage metadata
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImageJpeg.ToPointer(),
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Total tokens billed: %d\n", *interaction.Usage.TotalTokens)
    }
}
```

اندازه‌های پنجره بافت را در صفحه [مدل‌ها](https://ai.google.dev/gemini-api/docs/models?hl=fa) پیدا کنید.

## قدم بعدی چیست

- [تولید نوشتار](https://ai.google.dev/gemini-api/docs/text-generation?hl=fa): اصول تولید
- [ذخیره در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa): با ذخیره در حافظه نهان، هزینه‌ها را کاهش دهید
- [قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa): درک هزینه‌ها

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-13 به‌وقت ساعت هماهنگ جهانی."],[],[]]
