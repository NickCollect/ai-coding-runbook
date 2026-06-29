---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=ar
fetched_at: 2026-06-29T05:41:06.660146+00:00
title: "\u0627\u0644\u0627\u0633\u062a\u0646\u062a\u0627\u062c \u0627\u0644\u0645\u0631\u0646 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# الاستنتاج المرن

الوصف: تعرَّف على كيفية تحسين التكاليف باستخدام مستوى الاستدلال المرن

‫Gemini Flex API هو مستوى استدلال يقدّم خصمًا بنسبة% 50 على التكلفة مقارنةً بالأسعار العادية، مقابل وقت استجابة متغيّر وتوفّر بأفضل جهد. تم تصميم هذا المستوى لأحمال العمل التي تتحمّل وقت الاستجابة وتتطلّب معالجة متزامنة ولكنّها لا تحتاج إلى الأداء في الوقت الفعلي الذي يوفّره واجهة برمجة التطبيقات العادية.

## كيفية استخدام المستوى المرن

لاستخدام المستوى المرن، حدِّد `service_tier` على أنّه `flex` في نص الطلب. تستخدم الطلبات تلقائيًا المستوى العادي إذا تم حذف هذا الحقل.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Analyze this dataset for trends...",
        config={"service_tier": "flex"},
    )
    print(response.text)
except Exception as e:
    print(f"Flex request failed: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3.5-flash",
      contents: "Analyze this dataset for trends...",
      config: { serviceTier: "flex" },
    });
    console.log(response.text);
  } catch (e) {
    console.log(`Flex request failed: ${e}`);
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

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.5-flash",
        genai.Text("Analyze this dataset for trends..."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        log.Printf("Flex request failed: %v", err)
        return
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## كيفية عمل الاستدلال المرن

[يسدّ الاستدلال المرن في Gemini الفجوة بين واجهة برمجة التطبيقات العادية وواجهة برمجة التطبيقات المجمّعة التي تستغرق 24 ساعة
.](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) ويستخدِم هذا المستوى سعة الحوسبة "القابلة للتخفيض" في غير أوقات الذروة لتوفير حلّ فعّال من حيث التكلفة للمهام في الخلفية وسير العمل المتسلسل.

| الميزة | التعبير | الأولوية | خطة "الرزمة العادية" | مجمّعة |
| --- | --- | --- | --- | --- |
| **الأسعار** | خصم بنسبة% 50 | أكثر بنسبة %75 إلى %100 من خطة "الرزمة العادية" | السعر الكامل | خصم بنسبة% 50 |
| **وقت الاستجابة** | دقائق (الهدف من دقيقة إلى 15 دقيقة) | منخفض (ثوانٍ) | من ثوانٍ إلى دقائق | ما يصل إلى 24 ساعة |
| **الموثوقية** | بأفضل جهد (قابل للتخفيض) | عالية (غير قابلة للتخفيض) | عالية / متوسّطة إلى عالية | عالية (لمعدّل نقل البيانات) |
| **الواجهة** | متزامن | متزامن | متزامن | غير متزامن |

### المزايا الرئيسية

- **فعالية التكلفة**: وفورات كبيرة لعمليات التقييم غير الإنتاجية والوكلاء في الخلفية وإثراء البيانات
- **سهولة الاستخدام**: ما مِن حاجة إلى إدارة كائنات مجمّعة أو أرقام تعريف الوظائف أو عمليات الاقتراع، ما عليك سوى إضافة مَعلمة واحدة إلى طلباتك الحالية.
- **سير العمل المتزامن**: مثالي لسلاسل واجهات برمجة التطبيقات المتسلسلة حيث يعتمد الطلب التالي على ناتج الطلب السابق، ما يجعله أكثر مرونة من واجهة برمجة التطبيقات المجمّعة لسير عمل الوكلاء

### حالات الاستخدام

- **عمليات التقييم بلا إنترنت**: إجراء اختبارات الانحدار أو لوحات الصدارة "للنموذج اللغوي الكبير كحكم"
- **الوكلاء في الخلفية**: مهام متسلسلة، مثل تعديلات نظام إدارة علاقات العملاء أو إنشاء الملفات الشخصية أو الإشراف على المحتوى، حيث تكون دقائق التأخير مقبولة
- **الأبحاث المقيّدة بالميزانية**: التجارب الأكاديمية التي تتطلّب حجمًا كبيرًا من الرموز المميّزة بميزانية محدودة

### حدود معدّل الاستخدام

يتم احتساب عدد الزيارات الناتجة عن الاستدلال المرن ضمن حدود [معدّل الاستخدام](https://aistudio.google.com/rate-limit?hl=ar) العامة، ولا
يقدّم هذا المستوى حدودًا موسّعة لمعدّل الاستخدام مثل [واجهة برمجة التطبيقات المجمّعة](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar).

### السعة القابلة للتخفيض

يتم التعامل مع عدد الزيارات المرنة بأولوية أقل. في حال حدوث ارتفاع في عدد الزيارات العادية، قد يتم إيقاف طلبات المستوى المرن أو إزالتها لضمان توفير السعة للمستخدمين ذوي الأولوية العالية. إذا كنت تبحث عن استدلال ذي أولوية عالية، اطّلِع على
[الاستدلال ذي الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar)

### رموز الخطأ

عندما تكون سعة المستوى المرن غير متاحة أو يكون النظام مزدحمًا، ستعرض واجهة برمجة التطبيقات رموز الخطأ العادية:

- **\*\*503 الخدمة غير متاحة\*\***: يتلقّى النظام عدد طلبات كبير جدًا في الوقت الحالي.
- **429 Too Many Requests**: حدود معدّل الاستخدام أو استنفاد الموارد

### مسؤولية العميل

- **ما مِن خيار احتياطي من جهة الخادم**: لمنع حدوث رسوم غير متوقّعة، لن يرقّي النظام تلقائيًا طلبًا من المستوى المرن إلى المستوى العادي إذا كانت سعة المستوى المرن ممتلئة.
- **عمليات إعادة المحاولة**: عليك تنفيذ منطق إعادة المحاولة من جهة العميل باستخدام
  خوارزمية الرقود الأسي الثنائي.
- **مهلات الانتظار**: بما أنّ طلبات المستوى المرن قد تبقى في صفّ الانتظار، ننصحك بزيادة مهلات الانتظار من جهة العميل إلى 10 دقائق أو أكثر لتجنُّب إغلاق الاتصال قبل الأوان.

## تعديل فترات مهلة الانتظار

يمكنك ضبط مهلات الانتظار لكل طلب في REST API ومكتبات العميل، ومهلات الانتظار العامة فقط عند استخدام مكتبات العميل.

احرص دائمًا على أن تغطّي مهلة الانتظار من جهة العميل فترة الانتظار المقصودة من جهة الخادم (مثل 600 ثانية أو أكثر لقوائم انتظار المستوى المرن). تتوقّع حِزم تطوير البرامج (SDK) قيم مهلة الانتظار بالملّي ثانية.

### مهلات الانتظار لكل طلب

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="why is the sky blue?",
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 900000}
        },
    )
except Exception as e:
    print(f"Flex request failed: {e}")

# Example with streaming
try:
    response = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=["List 5 ideas for a sci-fi movie."],
        config={
            "service_tier": "flex",
            "http_options": {"timeout": 60000}
        }
        # Per-request timeout for the streaming operation
    )
    for chunk in response:
        print(chunk.text, end="")

except Exception as e:
    print(f"An error occurred during streaming: {e}")
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const client = new GoogleGenAI({});

 async function main() {
     try {
         const response = await client.models.generateContent({
             model: "gemini-3.5-flash",
             contents: "why is the sky blue?",
             config: {
               serviceTier: "flex",
               httpOptions: {timeout: 900000}
             },
         });
     } catch (e) {
         console.log(`Flex request failed: ${e}`);
     }

     // Example with streaming
     try {
         const response = await client.models.generateContentStream({
             model: "gemini-3.5-flash",
             contents: ["List 5 ideas for a sci-fi movie."],
             config: {
                 serviceTier: "flex",
                 httpOptions: {timeout: 60000}
             },
         });
         for await (const chunk of response.stream) {
             process.stdout.write(chunk.text());
         }
     } catch (e) {
         console.log(`An error occurred during streaming: ${e}`);
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
    "time"

    "google.golang.org/api/iterator"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer client.Close()

    timeoutCtx, cancel := context.WithTimeout(ctx, 900*time.Second)
    defer cancel()

    _, err = client.Models.GenerateContent(
        timeoutCtx,
        "gemini-3.5-flash",
        genai.Text("why is the sky blue?"),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    if err != nil {
        fmt.Printf("Flex request failed: %v\n", err)
    }

    // Example with streaming
    streamTimeoutCtx, streamCancel := context.WithTimeout(ctx, 60*time.Second)
    defer streamCancel()

    iter := client.Models.GenerateContentStream(
        streamTimeoutCtx,
        "gemini-3.5-flash",
        genai.Text("List 5 ideas for a sci-fi movie."),
        &genai.GenerateContentConfig{
            ServiceTier: "flex",
        },
    )
    for {
        response, err := iter.Next()
        if err == iterator.Done {
            break
        }
        if err != nil {
            fmt.Printf("An error occurred during streaming: %v\n", err)
            break
        }
        fmt.Print(response.Candidates[0].Content.Parts[0])
    }
}
```

### REST

عند إجراء طلبات REST، يمكنك التحكّم في مهلات الانتظار باستخدام مجموعة من عناوين HTTP وخيارات `curl`:

- **العنوان `X-Server-Timeout` (مهلة الانتظار من جهة الخادم)**: يشير هذا العنوان إلى مدة مهلة الانتظار المفضّلة (600 ثانية تلقائيًا) لخادم Gemini API. سيحاول الخادم الالتزام بذلك، ولكن ليس هناك ما يضمن ذلك. يجب أن تكون القيمة بالثواني.
- **`--max-time` في `curl` (مهلة الانتظار من جهة العميل)**: يضبط الخيار `curl --max-time
  <seconds>` حدًا أقصى للوقت الإجمالي (بالثواني) الذي ستنتظره `curl`
  حتى تكتمل العملية بأكملها. هذا إجراء وقائي من جهة العميل.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### مهلات الانتظار العامة

إذا كنت تريد أن تتضمّن جميع طلبات واجهة برمجة التطبيقات التي يتم إجراؤها من خلال مثيل `genai.Client` معيّن (مكتبات العميل فقط) مهلة انتظار تلقائية، يمكنك ضبط ذلك عند تهيئة العميل باستخدام `http_options` و`genai.types.HttpOptions`.

### Python

```
from google import genai
from google.genai import types

global_timeout_ms = 120000

client_with_global_timeout = genai.Client(
    http_options=types.HttpOptions(timeout=global_timeout_ms)
)

try:
    # Calling generate_content using global timeout...
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.5-flash",
        contents="Provide a very brief definition of machine learning.",
        config={
            "service_tier": "flex",
            "http_options":{"timeout": shorter_timeout}
        }  # Overrides the global timeout
    )

    print(response.text)

except TimeoutError:
    print(
        f"A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
    )
except Exception as e:
    print(f"An error occurred: {e}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const globalTimeoutMs = 120000;

const clientWithGlobalTimeout = new GoogleGenAI({httpOptions: {timeout: globalTimeoutMs}});

async function main() {
    try {
        // Calling generate_content using global timeout...
        const response1 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.5-flash",
            contents: "Provide a very brief definition of machine learning.",
            config: {
                serviceTier: "flex",
                httpOptions: {timeout: shorterTimeout}
            }  // Overrides the global timeout
        });

        console.log(response2.text());

    } catch (e) {
        if (e.name === 'TimeoutError' || e.message?.includes('timeout')) {
            console.log(
                "A GenerateContent call timed out. Check if the global or per-request timeout was exceeded."
            );
        } else {
            console.log(`An error occurred: ${e}`);
        }
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
     "time"

     "google.golang.org/genai"
 )

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     model := client.GenerativeModel("gemini-3.5-flash")

     // Go uses context for timeouts, not client options.
     // Set a default timeout for requests.
     globalTimeout := 120 * time.Second
     fmt.Printf("Using default timeout of %v seconds.\n", globalTimeout.Seconds())

     fmt.Println("Calling generate_content (using default timeout)...")
     ctx1, cancel1 := context.WithTimeout(ctx, globalTimeout)
     defer cancel1()
     resp1, err := model.GenerateContent(ctx1, genai.Text("Summarize the history of AI development since 2000."), &genai.GenerateContentConfig{ServiceTier: "flex"})
     if err != nil {
         log.Printf("Request 1 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 1 successful.")
         fmt.Println(resp1.Text())
     }

     // A different timeout can be used for other requests.
     shorterTimeout := 30 * time.Second
     fmt.Printf("\nCalling generate_content with a shorter timeout of %v seconds...\n", shorterTimeout.Seconds())
     ctx2, cancel2 := context.WithTimeout(ctx, shorterTimeout)
     defer cancel2()
     resp2, err := model.GenerateContent(ctx2, genai.Text("Provide a very brief definition of machine learning."), &genai.GenerateContentConfig{
         ServiceTier: "flex",
     })
     if err != nil {
         log.Printf("Request 2 failed: %v", err)
     } else {
         fmt.Println("GenerateContent 2 successful.")
         fmt.Println(resp2.Text())
     }
 }
```

## تنفيذ عمليات إعادة المحاولة

بما أنّ المستوى المرن قابل للتخفيض ويتعذّر استخدامه مع ظهور أخطاء 503، إليك مثال على تنفيذ منطق إعادة المحاولة اختياريًا لمتابعة الطلبات التي تعذّر إرسالها:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.5-flash",
                contents="Analyze this batch statement.",
                config={"service_tier": "flex"},
            )
        except Exception as e:
            # Check for 503 Service Unavailable or 429 Rate Limits
            print(e.code)
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt) # Exponential Backoff
                print(f"Flex busy, retrying in {delay}s...")
                time.sleep(delay)
            else:
                # Fallback to standard on last strike (Optional)
                print("Flex exhausted, falling back to Standard...")
                return client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents="Analyze this batch statement."
                )

# Usage
response = call_with_retry()
print(response.text)
```

### JavaScript

```
 import {GoogleGenAI} from '@google/genai';

 const ai = new GoogleGenAI({});

 async function sleep(ms) {
   return new Promise(resolve => setTimeout(resolve, ms));
 }

 async function callWithRetry(maxRetries = 3, baseDelay = 5) {
   for (let attempt = 0; attempt < maxRetries; attempt++) {
     try {
       console.log(`Attempt ${attempt + 1}: Calling Flex tier...`);
       const response = await ai.models.generateContent({
         model: "gemini-3.5-flash",
         contents: "Analyze this batch statement.",
         config: { serviceTier: 'flex' },
       });
       return response;
     } catch (e) {
       if (attempt < maxRetries - 1) {
         const delay = baseDelay * (2 ** attempt);
         console.log(`Flex busy, retrying in ${delay}s...`);
         await sleep(delay * 1000);
       } else {
         console.log("Flex exhausted, falling back to Standard...");
         return await ai.models.generateContent({
           model: "gemini-3.5-flash",
           contents: "Analyze this batch statement.",
         });
       }
     }
   }
 }

 async function main() {
     const response = await callWithRetry();
     console.log(response.text);
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
     "math"
     "time"

     "google.golang.org/genai"
 )

 func callWithRetry(ctx context.Context, client *genai.Client, maxRetries int, baseDelay time.Duration) (*genai.GenerateContentResponse, error) {
     modelName := "gemini-3.5-flash"
     content := genai.Text("Analyze this batch statement.")
     flexConfig := &genai.GenerateContentConfig{
         ServiceTier: "flex",
     }

     for attempt := 0; attempt < maxRetries; attempt++ {
         log.Printf("Attempt %d: Calling Flex tier...", attempt+1)
         resp, err := client.Models.GenerateContent(ctx, modelName, content, flexConfig)
         if err == nil {
             return resp, nil
         }

         log.Printf("Attempt %d failed: %v", attempt+1, err)

         if attempt < maxRetries-1 {
             delay := time.Duration(float64(baseDelay) * math.Pow(2, float64(attempt)))
             log.Printf("Flex busy, retrying in %v...", delay)
             time.Sleep(delay)
         } else {
             log.Println("Flex exhausted, falling back to Standard...")
             return client.Models.GenerateContent(ctx, modelName, content)
         }
     }
     return nil, fmt.Errorf("retries exhausted") // Should not be reached
 }

 func main() {
     ctx := context.Background()
     client, err := genai.NewClient(ctx, nil)
     if err != nil {
         log.Fatal(err)
     }
     defer client.Close()

     resp, err := callWithRetry(ctx, client, 3, 5*time.Second)
     if err != nil {
         log.Fatalf("Failed after retries: %v", err)
     }
     fmt.Println(resp.Text())
 }
```

## الأسعار

يتم تسعير الاستدلال المرن بنسبة% 50 من [واجهة برمجة التطبيقات العادية](https://ai.google.dev/gemini-api/docs/pricing?hl=ar)
ويتم تحصيل الرسوم لكل رمز مميّز.

## النماذج المتوافقة

تتوفّر ميزة الاستدلال المرن في النماذج التالية:

| الطراز | الاستدلال المرن |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=ar) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=ar) | ✔️ |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=ar) | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=ar) | ✔️ |
| [Gemini 3 Pro Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview?hl=ar) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=ar) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=ar) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=ar) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=ar) | ✔️ |

## الخطوات التالية

يمكنك الاطّلاع على خيارات [الاستدلال والتحسين](https://ai.google.dev/gemini-api/docs/optimization?hl=ar) الأخرى في Gemini:

- [الاستدلال ذي الأولوية](https://ai.google.dev/gemini-api/docs/priority-inference?hl=ar) لوقت استجابة فائق السرعة
- [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=ar) للمعالجة غير المتزامنة في غضون 24 ساعة
- [تخزين السياق مؤقتًا](https://ai.google.dev/gemini-api/docs/caching?hl=ar) لتقليل تكاليف الرموز المميّزة للإدخال

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
