---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=ar
fetched_at: 2026-07-20T04:46:54.458067+00:00
title: "\u062a\u0641\u0643\u064a\u0631 Gemini \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تفكير Gemini

تستخدم [نماذج سلسلة Gemini 3 و2.5](https://ai.google.dev/gemini-api/docs/models?hl=ar) "عملية تفكير" داخلية تحسّن بشكل كبير قدراتها على الاستدلال والتخطيط المتعدّد الخطوات، ما يجعلها فعّالة للغاية في المهام المعقّدة، مثل الترميز والرياضيات المتقدّمة وتحليل البيانات.

يوضّح هذا الدليل كيفية الاستفادة من إمكانات التفكير في Gemini باستخدام Gemini API.

## إنشاء محتوى مع التفكير

إنّ بدء طلب باستخدام نموذج تفكير يشبه أي طلب آخر لإنشاء المحتوى. يكمن الاختلاف الرئيسي في تحديد أحد [النماذج التي تتضمّن ميزة التفكير](#supported-models) في الحقل `model`، كما هو موضّح في مثال [إنشاء النص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#text-input) التالي:

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

### Go

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

## ملخّصات الأفكار

ملخّصات الأفكار هي إصدارات موجزة من الأفكار الأولية التي يعرضها النموذج، وهي تقدّم
إحصاءات حول عملية الاستدلال الداخلية التي يجريها النموذج. يُرجى العِلم أنّ مستويات التفكير والميزانيات تنطبق على الأفكار الأولية للنموذج وليس على ملخّصات الأفكار.

يمكنك تفعيل ملخّصات الأفكار من خلال ضبط `includeThoughts` على `true` في إعدادات الطلب. يمكنك بعد ذلك الوصول إلى الملخّص من خلال تكرار المعلَمة `response`، والتحقّق من القيمة المنطقية `thought`.`parts`

في ما يلي مثال يوضّح كيفية تفعيل ملخّصات الأفكار واستردادها بدون بث، ما يؤدي إلى عرض ملخّص نهائي واحد للأفكار مع الردّ:

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

### Go

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

في ما يلي مثال على استخدام ميزة "التفكير أثناء البث"، والتي تعرض ملخّصات متزايدة ومتجدّدة أثناء عملية الإنشاء:

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

### Go

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

## التحكّم في التفكير

تعتمد نماذج Gemini التفكير الديناميكي تلقائيًا، ما يعني أنّها تعدّل تلقائيًا مقدار الجهد المبذول في الاستدلال استنادًا إلى مدى تعقيد طلب المستخدم.
ومع ذلك، إذا كانت لديك قيود معيّنة بشأن وقت الاستجابة أو كنت تحتاج إلى أن يشارك النموذج في عملية استدلال أعمق من المعتاد، يمكنك اختياريًا استخدام المَعلمات للتحكّم في سلوك التفكير.

### مستويات التفكير (Gemini 3)

تتيح لك المَعلمة `thinkingLevel`، التي يُنصح باستخدامها مع نماذج Gemini 3 والإصدارات الأحدث، التحكّم في سلوك الاستدلال.

يوضّح الجدول التالي إعدادات `thinkingLevel` لكل نوع من أنواع النماذج:

| مستوى التفكير | Gemini 3.5 Flash | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | صورة Gemini 3.1 Flash-Lite | Gemini 3 Flash | الوصف |
| --- | --- | --- | --- | --- | --- | --- |
| **`minimal`** | متاح | غير متاح | متاح (تلقائي) | متاح (تلقائي) | متاح | يتطابق هذا الخيار مع الإعداد "بدون تفكير" لمعظم طلبات البحث. يُرجى العِلم أنّ `minimal` لا يضمن إيقاف التفكير، فقد يقدّم النموذج أسبابًا بسيطة جدًا للمهام المعقّدة. |
| **`low`** | متاح | متاح | متاح | غير متاح | متاح | يقلّل من زمن الانتقال والتكلفة. |
| **`medium`** | متاح (تلقائي) | متاح | متاح | غير متاح | متاح | التفكير المتوازن لمعظم المهام |
| **`high`** | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | زيادة عمق الاستدلال إلى أقصى حد قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى الرمز المميز الأول للناتج (غير المرتبط بالتفكير)، ولكن سيتم التفكير في الناتج بعناية أكبر. |

يوضّح المثال التالي كيفية ضبط مستوى التفكير.

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

### Go

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

لا يمكنك إيقاف ميزة "أفكّر" في Gemini 3.1 Pro. لا يتيح Gemini 3 Flash وFlash-Lite إيقاف التفكير بالكامل أيضًا. وإذا لم تحدّد مستوى التفكير، سيستخدم Gemini مستوى التفكير التلقائي لنماذج Gemini 3 (على سبيل المثال، `"high"` لنموذج Gemini 3.1 Pro و`"medium"` لنموذج Gemini 3.5 Flash).

لا تتوافق سلسلة نماذج Gemini 2.5 مع `thinkingLevel`، لذا يُرجى استخدام `thinkingBudget` بدلاً من ذلك.

### التفكير في الميزانيات

توجّه المَعلمة `thinkingBudget`، التي تم طرحها مع سلسلة Gemini 2.5، النموذج بشأن العدد المحدّد من الرموز المميزة التي يجب استخدامها للاستدلال.

في ما يلي `thinkingBudget` تفاصيل الإعداد لكل نوع من أنواع النماذج.
يمكنك إيقاف التفكير من خلال ضبط `thinkingBudget` على 0.
يؤدي ضبط قيمة `thinkingBudget` على -1 إلى تفعيل **الاستدلال الديناميكي**، ما يعني أنّ النموذج سيعدّل الميزانية استنادًا إلى مدى تعقيد الطلب.

| الطراز | الإعداد التلقائي (لم يتم ضبط ميزانية التفكير) | النطاق | إيقاف التفكير | تفعيل التفكير الديناميكي |
| --- | --- | --- | --- | --- |
| ‫**2.5 Pro** | التفكير الديناميكي | من `128` إلى `32768` | لا ينطبق: لا يمكن إيقاف التفكير | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| **معاينة ‎2.5 Flash** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| **2.5 Flash Lite** | النموذج لا يفكّر | من `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **معاينة 2.5 Flash Lite** | النموذج لا يفكّر | من `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| **الإصدار التجريبي من Robotics-ER 1.6** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| **معاينة الصوت الأصلي المباشر في 2.5 Flash (‫09-2025)** | التفكير الديناميكي | من `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |

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

### Go

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

استنادًا إلى الطلب، قد يتجاوز النموذج ميزانية الرموز المميزة أو لا يبلغها.

## توقيعات الأفكار

‫Gemini API هو واجهة برمجة تطبيقات لا تحتفظ بأي حالة، لذا يتعامل النموذج مع كل طلب من طلبات واجهة برمجة التطبيقات بشكل مستقل، ولا يمكنه الوصول إلى سياق الأفكار من الأدوار السابقة في التفاعلات المتعددة الأدوار.

لإتاحة الحفاظ على سياق الأفكار خلال المحادثات المتعددة الأدوار، يعرض Gemini توقيعات الأفكار، وهي تمثيلات مشفّرة لعملية معالجة الأفكار الداخلية في النموذج.

- تعرض **نماذج Gemini 2.5** توقيعات الأفكار عندما تكون ميزة التفكير مفعّلة ويتضمّن الطلب [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#thinking)، وتحديدًا [تعريفات الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-2).
- قد تعرض **نماذج Gemini 3** توقيعات فكرية لجميع أنواع [الأجزاء](https://ai.google.dev/api/caching?hl=ar#Part).
  ننصحك دائمًا بإعادة جميع التواقيع كما تم استلامها، ولكن هذا الإجراء *إلزامي* لتواقيع استدعاء الدوال. يمكنك الاطّلاع على صفحة [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) لمعرفة المزيد.

تشمل القيود الأخرى على الاستخدام التي يجب مراعاتها عند استخدام ميزة "استدعاء الدوال" ما يلي:

- يتم عرض التواقيع من النموذج ضمن أجزاء أخرى في الردّ، مثل استدعاء الدوال أو الأجزاء النصية.
  [أعِد الردّ بأكمله](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-4)
  مع جميع الأجزاء إلى النموذج في الجولات اللاحقة.
- لا تدمج الأجزاء التي تتضمّن توقيعات معًا.
- لا تدمج جزءًا من مستند يتضمّن توقيعًا مع جزء آخر لا يتضمّن توقيعًا.

## الأسعار

عند تفعيل ميزة "التفكير"، يكون سعر الردّ هو مجموع الرموز المميزة للناتج والرموز المميزة للتفكير. يمكنك الحصول على إجمالي عدد الرموز المميزة التي تم إنشاؤها من حقل `thoughtsTokenCount`.

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

### Go

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

تنشئ نماذج التفكير أفكارًا كاملة لتحسين جودة الرد النهائي، ثم تعرض [ملخّصات](#summaries) لتقديم نظرة ثاقبة حول عملية التفكير. لذلك، يستند التسعير إلى الرموز المميزة الكاملة التي يحتاج إليها النموذج لإنشاء ملخّص، على الرغم من أنّ الملخّص هو الناتج الوحيد من واجهة برمجة التطبيقات.

يمكنك الاطّلاع على مزيد من المعلومات حول الرموز المميزة في دليل [احتساب الرموز المميزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

## أفضل الممارسات

يتضمّن هذا القسم بعض الإرشادات لاستخدام نماذج التفكير بكفاءة.
وكالعادة، سيساعدك اتّباع [إرشادات كتابة الطلبات وأفضل الممارسات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar) في الحصول على أفضل النتائج.

### تصحيح الأخطاء والتوجيه

- **مراجعة الأسباب**: عندما لا تحصل على الردّ المتوقّع من نماذج التفكير، قد يساعدك ذلك في تحليل ملخّصات أفكار Gemini بعناية.
  يمكنك الاطّلاع على كيفية تقسيم المهمة والوصول إلى الاستنتاج، واستخدام هذه المعلومات لتصحيح النتائج.
- **تقديم إرشادات بشأن طريقة التفكير**: إذا كنت تأمل في الحصول على ناتج طويل بشكل خاص، يمكنك تقديم إرشادات في طلبك للحدّ من [مقدار التفكير](#set-budget) الذي يستخدمه النموذج. يتيح لك ذلك حجز المزيد من الرموز المميزة لردّك.

### مدى تعقيد المهمة

- **المهام السهلة (قد يكون التفكير غير مفعّل):** لا يتطلّب الأمر التفكير في الطلبات المباشرة التي لا تحتاج إلى استنتاج معقّد، مثل استرجاع الحقائق أو التصنيف. تشمل الأمثلة ما يلي:
  - "أين تأسّست شركة DeepMind؟"
  - "هل تطلب هذه الرسالة الإلكترونية عقد اجتماع أم أنّها تقدّم معلومات فقط؟"
- **المهام المتوسطة (الإعدادات التلقائية/بعض التفكير):** تستفيد العديد من الطلبات الشائعة من المعالجة خطوة بخطوة أو الفهم الأعمق. يمكن لـ Gemini استخدام قدرات التفكير بمرونة لتنفيذ مهام مثل:
  - قدِّم تشبيهًا بين عملية التمثيل الضوئي والنمو.
  - تحديد أوجه الاختلاف والتشابه بين السيارات الكهربائية والسيارات الهجينة
- **المهام الصعبة (الحد الأقصى لقدرة التفكير):** بالنسبة إلى التحديات المعقدة حقًا، مثل حلّ مسائل رياضية معقدة أو مهام الترميز، ننصحك بتحديد ميزانية تفكير عالية. تتطلّب هذه الأنواع من المهام أن يستفيد النموذج من جميع إمكاناته في التفكير والتخطيط، وغالبًا ما تتضمّن العديد من الخطوات الداخلية قبل تقديم إجابة. تشمل الأمثلة ما يلي:
  - حلّ المسألة 1 في مسابقة AIME لعام 2025: أوجد مجموع جميع الأعداد الصحيحة b > 9 التي يكون فيها 17b قاسمًا لـ 97b.
  - اكتب رمز Python لتطبيق ويب يعرض بيانات سوق الأسهم في الوقت الفعلي، بما في ذلك مصادقة المستخدم. يجب أن يكون هذا الإجراء بأكبر قدر ممكن من الفعالية.

## النماذج والأدوات والإمكانات المتوافقة

تتوفّر ميزات التفكير على جميع طُرز السلسلة 3 و2.5.
يمكنك العثور على جميع إمكانات النموذج في صفحة
[النظرة العامة على النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

تعمل النماذج المفكِّرة مع جميع أدوات Gemini وقدراته. يتيح ذلك للنماذج التفاعل مع الأنظمة الخارجية أو تنفيذ الرموز أو الوصول إلى المعلومات في الوقت الفعلي، ودمج النتائج في عملية الاستدلال والرد النهائي.

يمكنك تجربة أمثلة على استخدام الأدوات مع نماذج التفكير في
[Thinking cookbook][Colab].

## ما هي الخطوات التالية؟

- تتوفّر معلومات حول التغطية في دليل [التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-07 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-07 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
