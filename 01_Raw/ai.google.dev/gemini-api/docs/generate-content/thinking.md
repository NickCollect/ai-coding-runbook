---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=hi
fetched_at: 2026-07-06T05:11:34.642489+00:00
title: "Gemini \u0915\u0947 \u092c\u093e\u0930\u0947 \u092e\u0947\u0902 \u0938\u094b\u091a \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=hi)

सुझाव भेजें

# Gemini के बारे में सोच

The [Gemini 3 and 2.5 series models](https://ai.google.dev/gemini-api/docs/models?hl=hi) इंटरनल "गहराई से विचार" का इस्तेमाल करते हैं. इससे उनकी गहराई से विश्लेषण और मल्टी-स्टेप प्लानिंग की क्षमताओं में काफ़ी सुधार होता है. इस वजह से, ये मॉडल कोडिंग, ऐडवांस लेवल की गणित, और डेटा विश्लेषण जैसे मुश्किल टास्क के लिए बहुत कारगर साबित होते हैं.

इस गाइड में, Gemini API का इस्तेमाल करके, Gemini की थिंकिंग क्षमताओं के साथ काम करने का तरीका बताया गया है.

## थिंकिंग मॉडल का इस्तेमाल करके कॉन्टेंट जनरेट करना

थिंकिंग मॉडल के साथ अनुरोध शुरू करना, कॉन्टेंट जनरेट करने के किसी अन्य अनुरोध की तरह ही होता है. [मुख्य अंतर, `model` फ़ील्ड में, थिंकिंग की सुविधा वाले किसी
[मॉडल](#supported-models) को तय करने में होता है. इसे कॉन्टेंट जनरेट करने के इस
उदाहरण में दिखाया गया है:](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#text-input)

### Python

```
from google import genai

client = genai.Client()
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
    contents: prompt,
  });

  console.log(response.text);
}

main();
```

### ऐप पर जाएं

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
  model := "gemini-3.5-flash"

  resp, _ := client.Models.GenerateContent(ctx, model, genai.Text(prompt), nil)

  fmt.Println(resp.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

## थिंकिंग मॉडल से मिले जवाबों की खास जानकारी

थिंकिंग मॉडल से मिले जवाबों की खास जानकारी, मॉडल के रॉ थॉट का सारांश होती है. इससे मॉडल की इंटरनल रीज़निंग प्रोसेस के बारे में अहम जानकारी मिलती है. ध्यान दें कि थिंकिंग लेवल और बजट, मॉडल के रॉ थॉट पर लागू होते हैं. ये थिंकिंग मॉडल से मिले जवाबों की खास जानकारी पर लागू नहीं होते.

अनुरोध के कॉन्फ़िगरेशन में `includeThoughts` को `true` पर सेट करके, थिंकिंग मॉडल से मिले जवाबों की खास जानकारी पाने की सुविधा चालू की जा सकती है. इसके बाद, `response` पैरामीटर के `parts` में जाकर, खास जानकारी ऐक्सेस की जा सकती है. साथ ही, `thought` बूलियन की जांच की जा सकती है.

यहां एक उदाहरण दिया गया है, जिसमें स्ट्रीमिंग के बिना, थिंकिंग मॉडल से मिले जवाबों की खास जानकारी पाने और उसे चालू करने का तरीका दिखाया गया है. इससे जवाब के साथ, थिंकिंग मॉडल से मिले जवाबों की एक और आखिरी खास जानकारी मिलती है:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### ऐप पर जाएं

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
  model := "gemini-3.5-flash"
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

यहां स्ट्रीमिंग के साथ थिंकिंग का इस्तेमाल करने का एक उदाहरण दिया गया है. इससे जनरेट होने के दौरान, खास जानकारी के रोलिंग और इंक्रीमेंटल वर्शन मिलते हैं:

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
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### ऐप पर जाएं

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
  model := "gemini-3.5-flash"

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

## थिंकिंग को कंट्रोल करना

Gemini मॉडल, डिफ़ॉल्ट रूप से डाइनैमिक थिंकिंग में शामिल होते हैं. ये उपयोगकर्ता के अनुरोध की मुश्किल के हिसाब से, रीज़निंग के लिए ज़रूरी कोशिश को अपने-आप अडजस्ट करते हैं.
हालांकि, अगर आपको इंतज़ार के समय से जुड़ी खास पाबंदियां लागू करनी हैं या मॉडल से सामान्य से ज़्यादा गहराई से रीज़निंग करानी है, तो थिंकिंग के व्यवहार को कंट्रोल करने के लिए, पैरामीटर का इस्तेमाल किया जा सकता है.

### थिंकिंग लेवल (Gemini 3)

`thinkingLevel` पैरामीटर, Gemini 3 और इसके बाद के मॉडल के लिए इस्तेमाल करने का सुझाव दिया जाता है. इसकी मदद से, रीज़निंग के व्यवहार को कंट्रोल किया जा सकता है.

यहां दी गई टेबल में, हर मॉडल टाइप के लिए `thinkingLevel` सेटिंग के बारे में जानकारी दी गई है:

| थिंकिंग लेवल | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3.1 Flash-Lite Image | Gemini 3 Flash | ब्यौरा |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | काम करता है | काम नहीं करता है | काम करता है (डिफ़ॉल्ट) | काम करता है (डिफ़ॉल्ट) | काम करता है | ज़्यादातर क्वेरी के लिए, "नो थिंकिंग" सेटिंग के मुताबिक काम करता है. ध्यान दें, `minimal` का मतलब यह नहीं है कि थिंकिंग बंद है. मॉडल, मुश्किल टास्क के लिए बहुत कम रीज़निंग कर सकता है. |
| **`low`** | काम करता है | काम करता है | काम करता है | काम नहीं करता है | काम करता है | इससे इंतज़ार का समय और लागत कम होती है. |
| **`medium`** | काम करता है (डिफ़ॉल्ट) | काम करता है | काम करता है | काम नहीं करता है | काम करता है | ज़्यादातर टास्क के लिए, बैलेंस थिंकिंग. |
| **`high`** | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डाइनैमिक) | काम करता है (डिफ़ॉल्ट, डाइनैमिक) | इससे रीज़निंग की गहराई बढ़ जाती है. मॉडल को पहला (बिना थिंकिंग वाला) आउटपुट टोकन जनरेट करने में काफ़ी समय लग सकता है. हालांकि, आउटपुट ज़्यादा सावधानी से रीज़न किया जाएगा. |

यहां दिए गए उदाहरण में, थिंकिंग लेवल सेट करने का तरीका बताया गया है.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
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
    model: "gemini-3.5-flash",
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

### ऐप पर जाएं

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
  model := "gemini-3.5-flash"
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

Gemini 3.1 Pro के लिए, थिंकिंग की सुविधा बंद नहीं की जा सकती. Gemini 3 Flash और Flash-Lite
में भी, थिंकिंग की सुविधा पूरी तरह से बंद नहीं की जा सकती.
अगर कोई थिंकिंग लेवल तय नहीं किया जाता है, तो Gemini, Gemini 3 मॉडल के
डिफ़ॉल्ट थिंकिंग लेवल का इस्तेमाल करेगा. जैसे, Gemini 3.1 Pro के लिए `"high"` और Gemini 3.5 Flash के लिए `"medium"`.

Gemini 2.5 सीरीज़ के मॉडल, `thinkingLevel` के साथ काम नहीं करते. इसके बजाय, `thinkingBudget` का इस्तेमाल करें.

### थिंकिंग बजट

`thinkingBudget` पैरामीटर, जिसे Gemini 2.5 सीरीज़ के साथ लॉन्च किया गया था, मॉडल को गहराई से विश्लेषण के लिए इस्तेमाल किए जाने वाले थिंकिंग टोकन की खास संख्या के बारे में बताता है.

यहां हर मॉडल टाइप के लिए, `thinkingBudget` के कॉन्फ़िगरेशन की जानकारी दी गई है.
`thinkingBudget` को 0 पर सेट करके, थिंकिंग की सुविधा बंद की जा सकती है.
`thinkingBudget` को -1 पर सेट करने से,
**डाइनैमिक थिंकिंग** चालू हो जाती है. इसका मतलब है कि मॉडल, अनुरोध की
मुश्किल के हिसाब से बजट को अडजस्ट करेगा.

| मॉडल | डिफ़ॉल्ट सेटिंग (थिंकिंग बजट सेट नहीं है) | रेंज | थिंकिंग की सुविधा बंद करें | डाइनैमिक थिंकिंग की सुविधा चालू करें |
| --- | --- | --- | --- | --- |
| **2.5 Pro** | डाइनैमिक थिंकिंग | `128` से `32768` | लागू नहीं: थिंकिंग की सुविधा बंद नहीं की जा सकती | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash Preview** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash Lite** | मॉडल, थिंकिंग की सुविधा के बिना काम करता है | `512` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **2.5 Flash Lite Preview** | मॉडल, थिंकिंग की सुविधा के बिना काम करता है | `512` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **Robotics-ER 1.6 Preview** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |
| **2.5 Flash Live Native Audio Preview (09-2025)** | डाइनैमिक थिंकिंग | `0` से `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (डिफ़ॉल्ट) |

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

### ऐप पर जाएं

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

### REST

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

प्रॉम्प्ट के हिसाब से, मॉडल टोकन बजट से ज़्यादा या कम टोकन इस्तेमाल कर सकता है.

## थिंकिंग मॉडल से मिले जवाबों के सिग्नेचर

Gemini API, स्टेटलेस है. इसलिए, मॉडल हर एपीआई अनुरोध को अलग-अलग प्रोसेस करता है. साथ ही, सिलसिलेवार बातचीत में, मॉडल के पास पिछले टर्न के थॉट कॉन्टेक्स्ट का ऐक्सेस नहीं होता.

सिलसिलेवार बातचीत के दौरान, थॉट कॉन्टेक्स्ट को बनाए रखने के लिए, Gemini, थॉट सिग्नेचर दिखाता है. ये मॉडल की इंटरनल थॉट प्रोसेस के एन्क्रिप्ट किए गए वर्शन होते हैं.

- **Gemini 2.5 मॉडल** , थिंकिंग की सुविधा चालू होने पर और
  अनुरोध में [फ़ंक्शन कॉलिंग](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#thinking) शामिल होने पर, थिंकिंग मॉडल से मिले जवाबों के सिग्नेचर दिखाते हैं.
  खास तौर पर, [फ़ंक्शन के एलान](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-2) शामिल होने पर.
- **Gemini 3 मॉडल** सभी तरह के [पार्ट](https://ai.google.dev/api/caching?hl=hi#Part) के लिए, थिंकिंग मॉडल से मिले जवाबों के सिग्नेचर दिखा सकते हैं.
  हमारा सुझाव है कि आपको मिले सभी सिग्नेचर को वापस भेजें. हालांकि, फ़ंक्शन कॉलिंग सिग्नेचर के लिए यह *ज़रूरी* है. ज़्यादा जानने के लिए,
  [थिंकिंग मॉडल से मिले जवाबों के सिग्नेचर](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=hi) पेज
  पढ़ें.

फ़ंक्शन कॉलिंग के साथ इस्तेमाल से जुड़ी अन्य पाबंदियों में ये शामिल हैं:

- सिग्नेचर, जवाब में अन्य पार्ट के साथ मॉडल से मिलते हैं. जैसे, फ़ंक्शन कॉलिंग या टेक्स्ट पार्ट.
  [इसके बाद के टर्न में,](https://ai.google.dev/gemini-api/docs/function-calling?hl=hi#step-4)
  सभी पार्ट के साथ पूरा जवाब मॉडल को वापस भेजें.
- सिग्नेचर वाले पार्ट को एक साथ न जोड़ें.
- सिग्नेचर वाले किसी पार्ट को, बिना सिग्नेचर वाले किसी अन्य पार्ट के साथ न मिलाएं.

## कीमत

थिंकिंग की सुविधा चालू होने पर, जवाब की कीमत, आउटपुट टोकन और थिंकिंग टोकन के योग के बराबर होती है. `thoughtsTokenCount` फ़ील्ड से, जनरेट किए गए थिंकिंग टोकन की कुल संख्या पाई जा सकती है.

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

### ऐप पर जाएं

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

थिंकिंग मॉडल, जवाब की क्वालिटी बेहतर बनाने के लिए, पूरी तरह से सोच-समझकर जवाब जनरेट करते हैं. इसके बाद, थॉट प्रोसेस के बारे में जानकारी देने के लिए, [खास जानकारी](#summaries) आउटपुट करते हैं. इसलिए, कीमत, मॉडल को खास जानकारी जनरेट करने के लिए ज़रूरी पूरी तरह से सोच-समझकर दिए गए जवाबों के टोकन के आधार पर तय की जाती है. भले ही, एपीआई से सिर्फ़ खास जानकारी आउटपुट की गई हो.

टोकन के बारे में ज़्यादा जानने के लिए, [टोकन की गिनती करने की](https://ai.google.dev/gemini-api/docs/tokens?hl=hi)
गाइड पढ़ें.

## सबसे सही तरीके

इस सेक्शन में, थिंकिंग मॉडल का असरदार तरीके से इस्तेमाल करने के लिए कुछ दिशा-निर्देश दिए गए हैं.
हमेशा की तरह, प्रॉम्प्टिंग के लिए हमारे [दिशा-निर्देशों और सबसे सही तरीकों](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=hi) को फ़ॉलो करने से, आपको सबसे अच्छे नतीजे मिलेंगे.

### डीबग करना और स्टीयरिंग

- **रीज़निंग की समीक्षा करना**: जब आपको
  थिंकिंग मॉडल से उम्मीद के मुताबिक जवाब नहीं मिल रहा है, तो Gemini के थिंकिंग मॉडल से मिले जवाबों की खास जानकारी का ध्यान से विश्लेषण करना मददगार साबित हो सकता है.
  इससे यह देखा जा सकता है कि मॉडल ने टास्क को कैसे बांटा और नतीजे पर कैसे पहुंचा. साथ ही, इस जानकारी का इस्तेमाल करके, सही नतीजे पाए जा सकते हैं.
- [**गहराई से विश्लेषण में दिशा-निर्देश देना**: अगर आपको खास तौर पर लंबा
  जवाब चाहिए, तो अपने प्रॉम्प्ट में दिशा-निर्देश दिए जा सकते हैं. इससे मॉडल के इस्तेमाल की जाने वाली गहराई से विचार की मात्रा को सीमित किया जा सकता है.](#set-budget) इससे, जवाब के लिए ज़्यादा टोकन आउटपुट रिज़र्व किया जा सकता है.

### टास्क की मुश्किल

- **आसान टास्क (थिंकिंग की सुविधा बंद की जा सकती है):** सीधे-सीधे अनुरोधों के लिए, जिनमें मुश्किल गहराई से विश्लेषण की ज़रूरत नहीं होती, थिंकिंग की सुविधा की ज़रूरत नहीं होती. जैसे, फ़ैक्ट रिट्रीवल या क्लासिफ़िकेशन. उदाहरण के लिए:
  - "DeepMind की स्थापना कहां हुई थी?"
  - "क्या इस ईमेल में मीटिंग के लिए कहा गया है या सिर्फ़ जानकारी दी गई है?"
- **मीडियम टास्क (डिफ़ॉल्ट/कुछ थिंकिंग):** कई सामान्य अनुरोधों को चरण-दर-चरण प्रोसेस करने या ज़्यादा गहराई से समझने की ज़रूरत होती है. Gemini, इन टास्क के लिए थिंकिंग की सुविधा का इस्तेमाल कर सकता है:
  - प्रकाश संश्लेषण और बड़े होने की तुलना करना.
  - इलेक्ट्रिक कारों और हाइब्रिड कारों की तुलना करना.
- **मुश्किल टास्क (ज़्यादा से ज़्यादा थिंकिंग की सुविधा):** मुश्किल चुनौतियों के लिए, जैसे कि गणित की मुश्किल समस्याओं को हल करना या कोडिंग टास्क, हमारा सुझाव है कि थिंकिंग बजट को ज़्यादा पर सेट करें. इस तरह के टास्क के लिए, मॉडल को अपनी पूरी रीज़निंग और प्लानिंग की क्षमताओं का इस्तेमाल करना पड़ता है. अक्सर, जवाब देने से पहले, इसमें कई इंटरनल चरण शामिल होते हैं. उदाहरण के लिए:
  - AIME 2025 में समस्या 1 को हल करें: सभी पूर्णांक आधारों b > 9 का योग निकालें, जिनके लिए
    17b, 97b का भाजक है.
  - किसी वेब ऐप्लिकेशन के लिए Python कोड लिखें, जो रीयल-टाइम शेयर बाज़ार के डेटा को विज़ुअलाइज़ करता है. इसमें उपयोगकर्ता की पुष्टि करने की सुविधा भी शामिल हो. इसे ज़्यादा से ज़्यादा असरदार बनाएं.

## काम करने वाले मॉडल, टूल, और सुविधाएं

थिंकिंग की सुविधाएं, 3 और 2.5 सीरीज़ के सभी मॉडल पर काम करती हैं.
मॉडल की सभी क्षमताओं के बारे में,
[मॉडल की खास जानकारी वाले](https://ai.google.dev/gemini-api/docs/models?hl=hi) पेज पर जाकर जाना जा सकता है.

थिंकिंग मॉडल, Gemini के सभी टूल और सुविधाओं के साथ काम करते हैं. इससे मॉडल, बाहरी सिस्टम के साथ इंटरैक्ट कर सकते हैं, कोड एक्ज़ीक्यूट कर सकते हैं या रीयल-टाइम जानकारी ऐक्सेस कर सकते हैं. साथ ही, नतीजों को अपनी रीज़निंग और आखिरी जवाब में शामिल कर सकते हैं.

[थिंकिंग कुकबुक][Colab] में, थिंकिंग मॉडल के साथ टूल इस्तेमाल करने के उदाहरण देखे जा सकते हैं.

## आगे क्या करना है?

- OpenAI के साथ काम करने की सुविधा के बारे में जानकारी, हमारी [OpenAI के साथ काम करने की सुविधा](https://ai.google.dev/gemini-api/docs/openai?hl=hi#thinking) वाली गाइड में उपलब्ध है.

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-06-30 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-06-30 (UTC) को अपडेट किया गया."],[],[]]
