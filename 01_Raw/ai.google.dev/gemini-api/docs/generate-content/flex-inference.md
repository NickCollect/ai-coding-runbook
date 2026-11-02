---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/flex-inference?hl=hi
fetched_at: 2026-11-02T07:04:30.827481+00:00
title: "Flex inference \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon अब उपलब्ध है. [इसे आज़माएं](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=hi).

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# Flex inference

जानकारी: Flex inference टियर की मदद से, लागत को ऑप्टिमाइज़ करने का तरीका जानें

Gemini Flex API, inference टियर है. यह स्टैंडर्ड दरों के मुकाबले, 50% कम लागत पर उपलब्ध है. हालांकि, इसमें लेटेंसी में बदलाव हो सकता है और उपलब्धता की गारंटी नहीं होती. इसे ऐसे वर्कलोड के लिए डिज़ाइन किया गया है जिनमें लेटेंसी से जुड़ी कोई समस्या नहीं होती. साथ ही, जिनमें सिंक्रोनस प्रोसेसिंग की ज़रूरत होती है, लेकिन स्टैंडर्ड एपीआई की रीयल-टाइम परफ़ॉर्मेंस की ज़रूरत नहीं होती.

## Flex का इस्तेमाल करने का तरीका

Flex टियर का इस्तेमाल करने के लिए, अनुरोध के मुख्य हिस्से में `service_tier` को `flex` के तौर पर तय करें. अगर इस फ़ील्ड को छोड़ दिया जाता है, तो डिफ़ॉल्ट तौर पर अनुरोधों में स्टैंडर्ड टियर का इस्तेमाल किया जाता है.

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
      model: "gemini-3.8-flash",
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

### ऐप पर जाएं

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
        "gemini-3.8-flash",
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
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "contents": [{
    "parts":[{"text": "Summarize the latest research on quantum computing."}]
  }],
  "service_tier": "flex"
}'
```

## Flex inference के काम करने का तरीका

Gemini Flex inference, स्टैंडर्ड एपीआई और [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) के 24 घंटे के
टर्नअराउंड के बीच का अंतर कम करता है. यह ऑफ़-पीक, "शेड किए जा सकने वाले" कंप्यूट क्षमता का इस्तेमाल करके, बैकग्राउंड टास्क और सीक्वेंशियल वर्कफ़्लो के लिए लागत के हिसाब से बेहतर समाधान उपलब्ध कराता है.

| सुविधा | Flex | प्राथमिकता | स्टैंडर्ड | बैच |
| --- | --- | --- | --- | --- |
| **कीमत** | 50% की छूट | स्टैंडर्ड से 75 से 100% ज़्यादा | फ़ुल टिकट | 50% की छूट |
| **लेटेंसी** | मिनट (1–15 मिनट का टारगेट) | कम (सेकंड) | सेकंड से मिनट | 24 घंटे लग सकते हैं |
| **भरोसेमंद होना** | बेस्ट-एफ़र्ट (शेड किया जा सकता है) | ज़्यादा (शेड नहीं किया जा सकता) | ज़्यादा / मीडियम-ज़्यादा | ज़्यादा (थ्रूपुट के लिए) |
| **इंटरफ़ेस** | सिंक्रोनस | सिंक्रोनस | सिंक्रोनस | एसिंक्रोनस |

### मुख्य फ़ायदे

- **लागत के हिसाब से बेहतर**: प्रोडक्शन के अलावा अन्य कामों के लिए, बैकग्राउंड एजेंट, और डेटा एनरिचमेंट में काफ़ी बचत होती है.
- **कम मुश्किल**: बैच ऑब्जेक्ट, जॉब आईडी या पोलिंग को मैनेज करने की ज़रूरत नहीं होती. बस, मौजूदा अनुरोधों में एक पैरामीटर जोड़ना होता है.
- **सिंक्रोनस वर्कफ़्लो**: यह एपीआई चेन के लिए सबसे सही है. इसमें अगला अनुरोध, पिछले अनुरोध के आउटपुट पर निर्भर करता है. इसलिए, यह एजेंटिक वर्कफ़्लो के लिए बैच से ज़्यादा फ़्लेक्सिबल है.

### इस्तेमाल के उदाहरण

- **ऑफ़लाइन आकलन**: "एलएलएम-एज़-अ-जज" रिग्रेशन टेस्ट या लीडरबोर्ड चलाना.
- **बैकग्राउंड एजेंट**: सीक्वेंशियल टास्क, जैसे कि सीआरएम अपडेट, प्रोफ़ाइल बनाना या कॉन्टेंट मॉडरेट करना. इनमें कुछ मिनट की देरी स्वीकार की जा सकती है.
- **सीमित बजट में रिसर्च**: ऐसे ऐकेडमिक एक्सपेरिमेंट जिनमें सीमित बजट में ज़्यादा टोकन वॉल्यूम की ज़रूरत होती है.

### अनुरोध संख्या सीमित करना

Flex inference ट्रैफ़िक, आपकी सामान्य [रेट लिमिट](https://aistudio.google.com/rate-limit?hl=hi) में गिना जाता है. इसमें
[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi) की तरह, ज़्यादा रेट लिमिट नहीं मिलती.

### शेड की जा सकने वाली क्षमता

Flex ट्रैफ़िक को कम प्राथमिकता दी जाती है. अगर स्टैंडर्ड ट्रैफ़िक में बढ़ोतरी होती है, तो ज़्यादा प्राथमिकता वाले उपयोगकर्ताओं के लिए क्षमता पक्का करने के लिए, Flex के अनुरोधों को रोका या हटाया जा सकता है. अगर आपको ज़्यादा प्राथमिकता वाली inference चाहिए, तो
[प्राथमिकता वाली inference](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi) देखें

### गड़बड़ी के कोड

अगर Flex की क्षमता उपलब्ध नहीं है या सिस्टम में ज़्यादा ट्रैफ़िक है, तो एपीआई स्टैंडर्ड गड़बड़ी के कोड दिखाएगा:

- **503 कोड वाली गड़बड़ी: सेवा उपलब्ध नहीं है**: इस्तेमाल करने की मौजूदा सीमा पूरी हो गई है.
- **429 कोड वाली गड़बड़ी: बहुत ज़्यादा अनुरोध**: अनुरोध संख्या सीमित करना या रिसॉर्स खत्म हो गए हैं.

### क्लाइंट की ज़िम्मेदारी

- **सर्वर-साइड फ़ॉलबैक नहीं**: अनचाहे शुल्क से बचने के लिए, अगर Flex की क्षमता पूरी हो जाती है, तो सिस्टम Flex के अनुरोध को स्टैंडर्ड टियर में अपने-आप अपग्रेड नहीं करेगा.
- **फिर से कोशिश करना**: आपको
  एक्सपोनेन्शियल बैकऑफ़ के साथ, क्लाइंट-साइड पर फिर से कोशिश करने का लॉजिक लागू करना होगा.
- **टाइम आउट**: ऐसा हो सकता है कि Flex के अनुरोध, क्यू में हों. इसलिए, हमारा सुझाव है कि कनेक्शन को समय से पहले बंद होने से बचाने के लिए, क्लाइंट-साइड टाइम आउट को 10 मिनट या उससे ज़्यादा कर दें.

## टाइम आउट विंडो को अडजस्ट करना

REST API और क्लाइंट लाइब्रेरी के लिए, हर अनुरोध के हिसाब से टाइम आउट कॉन्फ़िगर किए जा सकते हैं. वहीं, ग्लोबल टाइम आउट सिर्फ़ क्लाइंट लाइब्रेरी का इस्तेमाल करते समय कॉन्फ़िगर किए जा सकते हैं.

हमेशा पक्का करें कि आपके क्लाइंट-साइड टाइम आउट में, सर्वर की इंतज़ार करने की तय विंडो शामिल हो (उदाहरण के लिए, Flex की इंतज़ार करने वाली क्यू के लिए 600 सेकंड से ज़्यादा). एसडीके, टाइम आउट की वैल्यू को मिलीसेकंड में लेते हैं.

### हर अनुरोध के हिसाब से टाइम आउट

### Python

```
from google import genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
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
        model="gemini-3.8-flash",
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
             model: "gemini-3.8-flash",
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
             model: "gemini-3.8-flash",
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

### ऐप पर जाएं

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
        "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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

REST कॉल करते समय, एचटीटीपी हेडर और `curl` विकल्पों के कॉम्बिनेशन का इस्तेमाल करके, टाइम आउट को कंट्रोल किया जा सकता है:

- **`X-Server-Timeout` हेडर (सर्वर-साइड टाइम आउट)**: यह हेडर, Gemini API सर्वर को पसंदीदा टाइम आउट अवधि (डिफ़ॉल्ट तौर पर 600 सेकंड) के बारे में बताता है. सर्वर, इसका पालन करने की कोशिश करेगा. हालांकि, इसकी कोई गारंटी नहीं है. वैल्यू सेकंड में होनी चाहिए.
- **`--max-time` में `curl` (क्लाइंट-साइड टाइम आउट)**: `curl --max-time
  <seconds>` विकल्प, कुल समय (सेकंड में) की एक हार्ड लिमिट सेट करता है. इस लिमिट के बाद, `curl`
  पूरी कार्रवाई के पूरा होने का इंतज़ार नहीं करेगा. यह क्लाइंट-साइड सुरक्षा है.

```
 # Set a server timeout hint of 120 seconds and a client-side curl timeout of 125 seconds.
 curl --max-time 125 \
   -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key=$GEMINI_API_KEY" \
   -H "Content-Type: application/json" \
   -H "X-Server-Timeout: 120" \
   -d '{
   "contents": [{
     "parts":[{"text": "Summarize the latest research on quantum computing."}]
   }],
   "service_tier": "flex"
 }'
```

### ग्लोबल टाइम आउट

अगर आपको किसी खास `genai.Client` इंस्टेंस (सिर्फ़ क्लाइंट लाइब्रेरी) के ज़रिए किए गए सभी एपीआई कॉल के लिए, डिफ़ॉल्ट टाइम आउट सेट करना है, तो `http_options` और `genai.types.HttpOptions` का इस्तेमाल करके, क्लाइंट को शुरू करते समय इसे कॉन्फ़िगर किया जा सकता है.

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
        model="gemini-3.8-flash",
        contents="Summarize the history of AI development since 2000.",
        config={"service_tier": "flex"},
    )
    print(response.text)

    # A per-request timeout will *override* the global timeout for that specific call.
    shorter_timeout = 30000
    response = client_with_global_timeout.models.generate_content(
        model="gemini-3.8-flash",
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
            model: "gemini-3.8-flash",
            contents: "Summarize the history of AI development since 2000.",
            config: { serviceTier: "flex" },
        });
        console.log(response1.text());

        // A per-request timeout will *override* the global timeout for that specific call.
        const shorterTimeout = 30000;
        const response2 = await clientWithGlobalTimeout.models.generateContent({
            model: "gemini-3.8-flash",
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

### ऐप पर जाएं

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

     model := client.GenerativeModel("gemini-3.8-flash")

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

## फिर से कोशिश करने की सुविधा लागू करना

Flex को शेड किया जा सकता है और इसमें 503 कोड वाली गड़बड़ियां आ सकती हैं. इसलिए, यहां फ़ेल हुए अनुरोधों को जारी रखने के लिए, फिर से कोशिश करने के लॉजिक को लागू करने का एक उदाहरण दिया गया है:

### Python

```
import time
from google import genai

client = genai.Client()

def call_with_retry(max_retries=3, base_delay=5):
    for attempt in range(max_retries):
        try:
            return client.models.generate_content(
                model="gemini-3.8-flash",
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
                    model="gemini-3.8-flash",
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
         model: "gemini-3.8-flash",
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
           model: "gemini-3.8-flash",
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

### ऐप पर जाएं

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
     modelName := "gemini-3.8-flash"
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

## कीमत

Flex inference की कीमत, [स्टैंडर्ड एपीआई](https://ai.google.dev/gemini-api/docs/pricing?hl=hi)
की कीमत का 50% होती है. इसका बिलिंग, हर टोकन के हिसाब से किया जाता है.

## इस्तेमाल किए जा सकने वाले मॉडल

यहां दिए गए मॉडल, Flex inference के साथ काम करते हैं:

| मॉडल | Flex inference |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=hi) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=hi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=hi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=hi) | ✔️ |
| [Gemini 3.1 Pro का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=hi) | ✔️ |
| [Gemini 3 Flash का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=hi) | ✔️ |
| [Gemini 3 Pro Image का प्रीव्यू](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=hi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=hi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=hi) | ✔️ |
| [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image?hl=hi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=hi) | ✔️ |

## आगे क्या करना है

Gemini के अन्य [inference और ऑप्टिमाइज़ेशन](https://ai.google.dev/gemini-api/docs/optimization?hl=hi) विकल्पों के बारे में पढ़ें:

- [लाइव स्ट्रीमिंग करने और उसके दिखने के बीच इंतज़ार का समय बहुत कम रखने के लिए, प्राथमिकता वाली inference](https://ai.google.dev/gemini-api/docs/priority-inference?hl=hi).
- [24 घंटे के अंदर एसिंक्रोनस प्रोसेसिंग के लिए, Batch API.](https://ai.google.dev/gemini-api/docs/batch-api?hl=hi)
- इनपुट टोकन की लागत कम करने के लिए, [कॉन्टेक्स्ट कैशिंग](https://ai.google.dev/gemini-api/docs/caching?hl=hi).

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-10-13 (UTC) को अपडेट किया गया."],[],[]]
