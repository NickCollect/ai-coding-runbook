---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=fa
fetched_at: 2026-11-02T07:15:34.641633+00:00
title: "\u202bGemini \u062f\u0631\u062d\u0627\u0644 \u0641\u06a9\u0631 \u06a9\u0631\u062f\u0646 \u0627\u0633\u062a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs/generate-content?hl=fa)

ارسال بازخورد

# ‫Gemini درحال فکر کردن است

[مدل‌های Gemini](https://ai.google.dev/gemini-api/docs/models?hl=fa) از یک «فرایند تفکر» داخلی استفاده می‌کنند که توانایی‌های استدلال و برنامه‌ریزی چندمرحله‌ای آن‌ها را به‌طور قابل‌توجهی بهبود می‌بخشد و آن‌ها را برای انجام تکالیف پیچیده مانند کدنویسی، ریاضیات پیشرفته، و تجزیه‌وتحلیل داده‌ها بسیار مؤثر می‌کند.

این راهنما به شما نشان می‌دهد که چگونه بااستفاده از Gemini API با قابلیت‌های تفکر Gemini کار کنید.

## تولید محتوا با تفکر

شروع درخواست با مدل اندیشگر مشابه هر درخواست تولید محتوای دیگری است. تفاوت اصلی در مشخص کردن یکی از
[مدل‌های دارای پشتیبانی از استدلال](#tools) در فیلد `model` است، همان‌طور که
در مثال [تولید نوشتار](https://ai.google.dev/gemini-api/docs/text-generation?hl=fa) زیر نشان داده شده است:

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example.";

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### رفتن

```
package main

import (
  "context"
  "fmt"
  "log"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  prompt := "Explain the concept of Occam's Razor and provide a simple, everyday example."
  model := "gemini-3.8-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
 -H "x-goog-api-key: $GEMINI_API_KEY" \
 -H 'Content-Type: application/json' \
 -X POST \
 -d '{
   "contents": [
     {
       "parts": [
         {
           "text": "Explain the concept of Occam'\''s Razor and provide a simple, everyday example."
         }
       ]
     }
   ]
 }'
 ```
```

## خلاصه‌های فکر

خلاصه‌های فکر نسخه‌های خلاصه شده از افکار خام مدل هستند و اطلاعات آماری درباره فرایند استدلال داخلی مدل ارائه می‌دهند. توجه داشته باشید که سطوح اندیشیدن و بودجه‌ها برای افکار خام مدل اعمال می‌شوند و نه برای خلاصه‌های افکار.

می‌توانید با تنظیم `includeThoughts` روی `true` در پیکربندی درخواستتان، خلاصه‌های فکری را فعال کنید. سپس می‌توانید با پیمایش در پارامتر
`response``parts` و بررسی مقدار بولی `thought` به خلاصه دسترسی پیدا کنید.

در اینجا نمونه‌ای از نحوه فعال کردن و بازیابی خلاصه افکار بدون جاری‌سازی آورده شده است که یک خلاصه فکر نهایی واحد را با پاسخ برمی‌گرداند:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.8-flash",
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "What is the sum of the first 50 prime numbers?",
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for (const part of response.candidates[0].content.parts) {
    if (!part.text) {
      continue;
    }
    else if (part.thought) {
      console.log("Thoughts summary:");
      console.log(part.text);
    }
    else {
      console.log("Answer:");
      console.log(part.text);
    }
  }
}

main();
```

### رفتن

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text("What is the sum of the first 50 prime numbers?")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for _, part := range resp.Candidates[0].Content.Parts {
    if part.Text != "" {
      if part.Thought {
        fmt.Println("Thoughts Summary:")
        fmt.Println(part.Text)
      } else {
        fmt.Println("Answer:")
        fmt.Println(part.Text)
      }
    }
  }
}
```

و در اینجا نمونه‌ای از استفاده از «تفکر با جاری‌سازی» ارائه شده است که درطول تولید، خلاصه افزایشی و چرخشی برمی‌گرداند:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
"""

thoughts = ""
answer = ""

for chunk in client.models.generate_content_stream(
    model="gemini-3.8-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
      thinking_config=types.ThinkingConfig(
        include_thoughts=True
      )
    )
):
  for part in chunk.candidates[0].content.parts:
    if not part.text:
      continue
    elif part.thought:
      if not thoughts:
        print("Thoughts summary:")
      print(part.text)
      thoughts += part.text
    else:
      if not answer:
        print("Answer:")
      print(part.text)
      answer += part.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. The person who lives in the red house owns a cat.
Bob does not live in the green house. Carol owns a dog. The green house is to
the left of the red house. Alice does not own a cat. Who lives in each house,
and what pet do they own?`;

let thoughts = "";
let answer = "";

async function main() {
  const response = await ai.models.generateContentStream({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      thinkingConfig: {
        includeThoughts: true,
      },
    },
  });

  for await (const chunk of response) {
    for (const part of chunk.candidates[0].content.parts) {
      if (!part.text) {
        continue;
      } else if (part.thought) {
        if (!thoughts) {
          console.log("Thoughts summary:");
        }
        console.log(part.text);
        thoughts = thoughts + part.text;
      } else {
        if (!answer) {
          console.log("Answer:");
        }
        console.log(part.text);
        answer = answer + part.text;
      }
    }
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
  "os"
  "google.golang.org/genai"
)

const prompt = `
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
The person who lives in the red house owns a cat.
Bob does not live in the green house.
Carol owns a dog.
The green house is to the left of the red house.
Alice does not own a cat.
Who lives in each house, and what pet do they own?
`

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  contents := genai.Text(prompt)
  model := "gemini-3.8-flash"

  resp := client.Models.GenerateContentStream(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      IncludeThoughts: true,
    },
  })

  for chunk := range resp {
    for _, part := range chunk.Candidates[0].Content.Parts {
      if len(part.Text) == 0 {
        continue
      }

      if part.Thought {
        fmt.Printf("Thought: %s\n", part.Text)
      } else {
        fmt.Printf("Answer: %s\n", part.Text)
      }
    }
  }
}
```

## کنترل کردن اندیشیدن

مدل‌های Gemini به‌طور پیش‌فرض درگیر تفکر پویا می‌شوند و به‌طور خودکار میزان تلاش برای استدلال را براساس پیچیدگی درخواست کاربر تنظیم می‌کنند.
بااین‌حال، اگر محدودیت‌های تأخیر خاصی دارید یا نیاز دارید که مدل در استدلال عمیق‌تر از حد معمول شرکت کند، می‌توانید به‌طور اختیاری از پارامترها برای کنترل رفتار تفکر استفاده کنید.

### سطوح «اندیشگر» (Gemini 4 و Gemini 3)

پارامتر `thinkingLevel` که برای Gemini 4 الزامی است و برای مدل‌های Gemini 3 توصیه می‌شود،
به شما امکان می‌دهد رفتار استدلال را کنترل کنید. ‫Gemini 4‏ (`gemini-4-argon`) از `low`،‏ `medium` (پیش‌فرض)، و `high` پشتیبانی می‌کند.

جدول زیر جزئیات تنظیمات `thinkingLevel` را برای هر نوع مدل نشان می‌دهد:

| سطح «اندیشگر» | Gemini 3.8 Flash | Gemini 3.6 Flash | Gemini 4 Argon | ‫Gemini 3.5 و 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | Gemini Robotics ER 2 | شرح |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | پشتیبانی نمی‌شود (خطا) | پشتیبانی‌شده | پشتیبانی نمی‌شود (خطا) | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده | پشتیبانی‌شده | برای اکثر پُرسمان‌ها با تنظیم «بدون فکر کردن» مطابقت دارد. توجه داشته باشید که `minimal` تضمین نمی‌کند که فکر کردن خاموش باشد، مدل ممکن است برای تکلیف‌های پیچیده بسیار کم استدلال کند. |
| **`low`** | پشتیبانی‌شده | پشتیبانی‌شده | پشتیبانی‌شده | پشتیبانی‌شده | پشتیبانی نمی‌شود | پشتیبانی‌شده | پشتیبانی‌شده | تأخیر و هزینه را به حداقل می‌رساند. |
| **`medium`** | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده (پیش‌فرض) | پشتیبانی‌شده | پشتیبانی نمی‌شود | پشتیبانی‌شده | پشتیبانی‌شده | اندیشیدن متوازن برای اکثر تکالیف. |
| **`high`** | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پویا) | پشتیبانی‌شده (پیش‌فرض، پویا) | پشتیبانی‌شده (پیش‌فرض، پویا) | عمق استدلال را به‌حداکثر می‌رساند. ممکن است مدل زمان بسیار بیشتری برای رسیدن به اولین کد خروجی (غیراندیشیدن) نیاز داشته باشد، اما خروجی با دقت بیشتری استدلال خواهد شد. |

مثال زیر نحوه تنظیم سطح اندیشیدن را نشان می‌دهد.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingLevel: ThinkingLevel.LOW,
      },
    },
  });

  console.log(response.text);
}

main();
```

### رفتن

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingLevelVal := "low"

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-3.8-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingLevel: &thinkingLevelVal,
    },
  })

fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingLevel": "low"
    }
  }
}'
```

نمی‌توانید اندیشیدن را برای Gemini 4 Argon غیرفعال کنید. ‫Gemini 3 Flash و Flash-Lite
هم از خاموش کردن کامل اندیشیدن پشتیبانی نمی‌کنند.
اگر سطح اندیشیدن را مشخص نکنید، Gemini از سطح اندیشیدن پیش‌فرض مدل استفاده خواهد کرد (برای نمونه، `"medium"` برای Gemini 4 Argon، ‏Gemini 3.8 Flash، و Gemini 3.6 Flash).

مدل‌های سری Gemini 2.5 از `thinkingLevel` پشتیبانی نمی‌کنند؛ به‌جای آن از `thinkingBudget` استفاده کنید.

### محدودیت‌های کد و `max_output_tokens`

پارامتر تولید [`max_output_tokens`](https://ai.google.dev/api/generate-content?hl=fa#v1beta.GenerationConfig)
حداکثر تعداد کدهای زبانی را که یک پاسخ می‌تواند تولید کند،
ازجمله کدهای زبانی فکری، تنظیم می‌کند.

وقتی تنظیم شود، این پارامتر به‌عنوان برش سخت‌گیرانه‌ای عمل می‌کند که زیرساخت آن را اعمال می‌کند
بدون اینکه نحوه تخصیص بودجه فکری مدل را تغییر دهد
(`thinking_level`).

اگر مدل درحین استدلال به این حد برسد، تولید را با
`finish_reason: MAX_TOKENS` متوقف می‌کند و خروجی ناقص یا خالی برمی‌گرداند (درحالی‌که همچنان
برای هر داده‌واحد اندیشیدن تولیدشده صورت‌حساب صادر می‌شود). برای کاهش هزینه یا تأخیر بدون کوتاه کردن پاسخ‌ها، به‌جای تنظیم `max_output_tokens` کوچک، `thinking_level` (`low` یا `medium`) را کاهش دهید.

برای مدل‌های Gemini 4 (`gemini-4-argon`)، محدودیت‌های بافت و برونداد زیر را درنظر داشته باشید:

- **پنجره زمینه‌ای مشترک ۱ میلیون داده‌واحد:** داده‌واحدهای ورودی، تفکر، و برونداد از یک پنجره زمینه‌ای ۱ میلیون داده‌واحدی (`1,048,576` داده‌واحد) استفاده می‌کنند. اگر داده‌واحدهای ورودی شما به‌علاوه `max_output_tokens` از ۱٬۰۴۸٬۵۷۶ داده‌واحد فراتر رود، «میانای برنامه‌سازی کاربردی» به‌طور خودکار حد خروجی را به فضای باقی‌مانده در پنجره زمینه‌ای (`1,048,576` منهای داده‌واحدهای ورودی شما) محدود می‌کند.
- **سقف برونداد برای هر درخواست (جاری‌سازی ۶۴ هزار / غیرجاری‌سازی ۳۲ هزار) و رمزگشایی طولانی (تا ۱ میلیون داده‌واحد):** یک درخواست جاری‌سازی (`streamGenerateContent`) حداکثر `65,536` داده‌واحد برمی‌گرداند و یک درخواست غیرجاری‌سازی (`generateContent`) حداکثر `32,768` داده‌واحد برمی‌گرداند. برای تولید فراتر از سقف هر درخواست (تا `1,048,576` کد به‌استثنای ورودی شما)، `max_output_tokens` را بالاتر از سقف تنظیم کنید. جدیدترین کیت‌های توسعه نرم‌افزار Google GenAI به‌طور پیش‌فرض به‌طور خودکار در سراسر پرش‌ها ادامه می‌دهند (`automatic_continuation=True`)، یا می‌توانید بااستفاده از `continuation_token` که هنگام توقف پرش با `finish_reason: "CONTINUATION"` برگردانده می‌شود، یک حلقه مشتری اجرا کنید. برای نمونه‌های کد، [رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=fa) را ببینید.

### درحال فکر کردن درباره بودجه‌ها

پارامتر `thinkingBudget` که با سری Gemini 2.5 معرفی شده است،
مدل را درباره تعداد مشخصی از داده‌واحدهای اندیشیدن که باید برای استدلال استفاده شود راهنمایی می‌کند.

در زیر، `thinkingBudget` جزئیات پیکربندی برای هر نوع مدل ارائه شده است.
می‌توانید با تنظیم `thinkingBudget` روی ۰، فکر کردن را غیرفعال کنید.
تنظیم `thinkingBudget` روی ۱-، **تفکر پویا** را روشن می‌کند، یعنی مدل بودجه را براساس پیچیدگی درخواست تنظیم خواهد کرد.

| مدل | تنظیم پیش‌فرض (بودجه تفکر تنظیم نشده است) | بُرد | غیرفعال کردن اندیشیدن | روشن کردن اندیشیدن پویا |
| --- | --- | --- | --- | --- |
| **‫۲.۵ Pro** | تفکر پویا | `128` به `32768` | N/A: Cannot disable thinking | ‫`thinkingBudget = -1` (پیش‌فرض) |
| **‫۲.۵ Flash** | تفکر پویا | `0` به `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (پیش‌فرض) |
| **‫‎2.5 Flash Preview** | تفکر پویا | `0` به `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (پیش‌فرض) |
| **‫۲.۵ Flash Lite** | مدل فکر نمی‌کند | `512` به `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **‫‎2.5 Flash Lite Preview** | مدل فکر نمی‌کند | `512` به `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | تفکر پویا | `0` به `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (پیش‌فرض) |
| **‫‎2.5 Flash Live Native Audio Preview (09-2025)** | تفکر پویا | `0` به `24576` | `thinkingBudget = 0` | ‫`thinkingBudget = -1` (پیش‌فرض) |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Provide a list of 3 famous physicists and their key contributions",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=1024)
        # Turn off thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=0)
        # Turn on dynamic thinking:
        # thinking_config=types.ThinkingConfig(thinking_budget=-1)
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "Provide a list of 3 famous physicists and their key contributions",
    config: {
      thinkingConfig: {
        thinkingBudget: 1024,
        // Turn off thinking:
        // thinkingBudget: 0
        // Turn on dynamic thinking:
        // thinkingBudget: -1
      },
    },
  });

  console.log(response.text);
}

main();
```

### رفتن

```
package main

import (
  "context"
  "fmt"
  "google.golang.org/genai"
  "os"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  thinkingBudgetVal := int32(1024)

  contents := genai.Text("Provide a list of 3 famous physicists and their key contributions")
  model := "gemini-2.5-flash"
  resp, _ := client.Models.GenerateContent(ctx, model, contents, &genai.GenerateContentConfig{
    ThinkingConfig: &genai.ThinkingConfig{
      ThinkingBudget: &thinkingBudgetVal,
      // Turn off thinking:
      // ThinkingBudget: int32(0),
      // Turn on dynamic thinking:
      // ThinkingBudget: int32(-1),
    },
  })

fmt.Println(resp.Text())
}
```

### استراحت

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [
    {
      "parts": [
        {
          "text": "Provide a list of 3 famous physicists and their key contributions"
        }
      ]
    }
  ],
  "generationConfig": {
    "thinkingConfig": {
          "thinkingBudget": 1024
    }
  }
}'
```

بسته به پیام‌واره، ممکن است مدل از بودجه توکن فراتر برود یا به آن نرسد.

## امضاهای فکری

‫Gemini API بی‌حالت است، بنابراین مدل با هر درخواست API به‌طور مستقل رفتار می‌کند و به بافت فکری از نوبت‌های قبلی در تعامل‌های چندنوبتی دسترسی ندارد.

برای فعال کردن حفظ بافت فکری در تعاملات چندنوبتی، Gemini امضاهای فکری را برمی‌گرداند که نمایش‌های رمزگذاری‌شده‌ای از فرایند فکری داخلی مدل هستند.

- **مدل‌های Gemini 2.5** وقتی تفکر فعال باشد و درخواست شامل [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa#thinking)، به‌ویژه [اعلام تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa#step-2) باشد، امضاهای تفکر را برمی‌گردانند.
- مدل‌های **Gemini 4 و Gemini 3** ممکن است امضاهای فکری را برای همه انواع
  [بخش‌ها](https://ai.google.dev/api/caching?hl=fa#Part) برگردانند. توصیه می‌کنیم همیشه همه امضاها را همان‌طور که دریافت شده‌اند برگردانید، اما این کار برای امضاهای فراخوانی تابع *الزامی* است. برای کسب اطلاعات بیشتر، صفحه
  [امضاهای فکری](https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures?hl=fa)
  را بخوانید.

محدودیت‌های دیگر استفاده که باید در تماس با تابع درنظر گرفته شود عبارت‌اند از:

- امضاها از مدل در بخش‌های دیگر پاسخ برگردانده می‌شوند،
  برای مثال، فراخوانی تابع یا بخش‌های نوشتاری.
  [کل پاسخ را](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa#step-4)
  با همه بخش‌ها در نوبت‌های بعدی به مدل برگردانید.
- بخش‌های دارای امضا را به‌هم متصل نکنید.
- بخشی را که امضا دارد با بخش دیگری که امضا ندارد ادغام نکنید.

## قیمت‌گذاری

وقتی اندیشیدن روشن باشد، قیمت پاسخ مجموع داده‌واحدهای برونداد و داده‌واحدهای اندیشیدن است. می‌توانید تعداد کل داده‌واحدهای اندیشیدن تولیدشده را از فیلد `thoughtsTokenCount` دریافت کنید.

### Python

```
# ...
print("Thoughts tokens:", response.usage_metadata.thoughts_token_count)
print("Output tokens:", response.usage_metadata.candidates_token_count)
```

### JavaScript

```
// ...
console.log(`Thoughts tokens: ${response.usageMetadata.thoughtsTokenCount}`);
console.log(`Output tokens: ${response.usageMetadata.candidatesTokenCount}`);
```

### رفتن

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

مدل‌های اندیشگر برای بهبود کیفیت پاسخ نهایی، اندیشه‌های کامل تولید می‌کنند و سپس [خلاصه‌هایی](#summaries) را به‌عنوان برونداد ارائه می‌دهند تا بینشی درباره فرایند اندیشیدن ارائه دهند. بنابراین، قیمت‌گذاری براساس نشانه‌های فکری کاملی است که مدل برای تولید خلاصه نیاز دارد، حتی اگر فقط خلاصه از API برونداد شود.

در راهنمای [شمارش نشان](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) می‌توانید درباره نشان‌ها بیشتر بدانید.

## روال‌های مطلوب

این بخش شامل چند راهنمایی برای استفاده کارآمد از مدل‌های اندیشگر است.
مثل همیشه، با دنبال کردن
[راهنمایی و روال‌های مطلوب پیام‌واره](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=fa)
بهترین نتایج را دریافت خواهید کرد.

### عیب‌یابی و هدایت

- **بازبینی استدلال**: وقتی پاسخ موردانتظارتان را از مدل‌های تفکر دریافت نمی‌کنید، تجزیه‌وتحلیل دقیق خلاصه‌های فکری Gemini می‌تواند کمک کند.
  می‌توانید ببینید که چگونه تکلیف را تجزیه کرده و به نتیجه رسیده است، و از آن اطلاعات برای اصلاح نتایج استفاده کنید.
- **ارائه راهنمایی در استدلال**: اگر انتظار خروجی بسیار طولانی دارید، ممکن است بخواهید در پیام‌واره خود راهنمایی ارائه دهید تا [میزان تفکر](#set-budget) مدل را محدود کنید. این کار به شما امکان می‌دهد تا مقدار بیشتری از خروجی توکن را برای پاسخ خود رزرو کنید.

### پیچیدگی تکلیف

- **تکالیف آسان (ممکن است «فکر کردن» خاموش باشد):** برای درخواست‌های ساده‌ای که به استدلال پیچیده نیاز ندارند، مثل بازیابی واقعیت یا طبقه‌بندی، به فکر کردن نیازی نیست. نمونه‌های آن عبارت‌اند از:
  - «DeepMind کجا تأسیس شد؟»
  - «آیا این ایمیل درخواست جلسه می‌کند یا فقط اطلاعات ارائه می‌دهد؟»
- **تکالیف متوسط (پیش‌فرض/کمی فکر کردن):** بسیاری از درخواست‌های رایج از پردازش گام‌به‌گام یا درک عمیق‌تر بهره‌مند می‌شوند. ‫Gemini می‌تواند به‌طور انعطاف‌پذیر
  از قابلیت تفکر برای کارهایی مثل موارد زیر استفاده کند:
  - فتوسنتز و رشد کردن را باهم مقایسه کن.
  - خودروهای برقی و خودروهای هیبریدی را مقایسه و هم‌سنجی کن.
- **تکالیف دشوار (حداکثر توانایی تفکر):** برای چالش‌های واقعاً پیچیده،
  مثل حل کردن مسائل پیچیده ریاضی یا تکالیف کدنویسی، توصیه می‌کنیم
  بودجه تفکر بالایی تنظیم کنید. این نوع تکالیف نیازمند این است که مدل از تمام قابلیت‌های استدلال و برنامه‌ریزی خود استفاده کند، اغلب شامل مراحل داخلی زیادی قبل‌از ارائه پاسخ است. برای نمونه:
  - مسئله ۱ در AIME 2025 را حل کن: مجموع همه پایه‌های عدد صحیح b > 9 را پیدا کن که برای آن‌ها 17b مقسوم‌علیه 97b است.
  - کد پایتون برای یک برنامه وب بنویس که داده‌های
    بازار سهام را به‌صورت هم‌زمان به‌تصویر می‌کشد، ازجمله اصالت‌سنجی کاربر. تا حد امکان کارآمد باشد.

## مدل‌ها، ابزارها، و قابلیت‌های پشتیبانی‌شده

ویژگی‌های «تفکر» در همه مدل‌های سری ۴، ۳، و ۲.۵ پشتیبانی می‌شود.
می‌توانید همه قابلیت‌های مدل را در صفحه
[نمای کلی مدل](https://ai.google.dev/gemini-api/docs/models?hl=fa) پیدا کنید.

‫مدل‌های اندیشگر با همه ابزارها و قابلیت‌های Gemini کار می‌کنند. این کار به مدل‌ها امکان می‌دهد با سیستم‌های خارجی تعامل داشته باشند، کد اجرا کنند، یا به اطلاعات هم‌زمان دسترسی داشته باشند و نتایج را در استدلال و پاسخ نهایی خود بگنجانند.

می‌توانید نمونه‌های استفاده از ابزارها با مدل‌های اندیشگر را در
[کتاب آشپزی اندیشگر][Colab] امتحان کنید.

## حالا چه می‌شود؟

- پوشش استدلال در راهنمای
  [سازگاری با OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fa#thinking) ما دردسترس است.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-14 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-14 به‌وقت ساعت هماهنگ جهانی."],[],[]]
