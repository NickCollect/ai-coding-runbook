---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=ar
fetched_at: 2026-06-15T06:22:57.552292+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# ميزة "المفكِّر" في Gemini

تستخدم [نماذج Gemini 3 و2.5 سلسلة](https://ai.google.dev/gemini-api/docs/models?hl=ar) "عملية تفكير" داخلية تحسّن بشكل كبير قدراتها على الاستدلال والتخطيط المتعدد الخطوات، ما يجعلها فعّالة جدًا في المهام المعقّدة، مثل الترميز والرياضيات المتقدّمة وتحليل البيانات.

يوضّح لك هذا الدليل كيفية استخدام إمكانات "المفكِّر" في Gemini باستخدام Gemini API.

## إنشاء محتوى باستخدام ميزة "المفكِّر"

يشبه بدء طلب باستخدام نموذج "المفكِّر" أي طلب آخر لإنشاء المحتوى. [ويكمن الاختلاف الرئيسي في تحديد أحد النماذج التي تتوافق مع ميزة "المفكِّر" في الحقل `model`، كما هو موضّح في مثال [إنشاء النص](https://ai.google.dev/gemini-api/docs/text-generation?hl=ar#text-input) التالي:](#supported-models)

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

### انتقال

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

ملخّصات الأفكار هي إصدارات مُلخّصة من الأفكار الأولية للنموذج، وتقدّم إحصاءات حول عملية الاستدلال الداخلية للنموذج. يُرجى العِلم أنّ مستويات "المفكِّر" والميزانيات تنطبق على الأفكار الأولية للنموذج وليس على ملخّصات الأفكار.

يمكنك تفعيل ملخّصات الأفكار من خلال ضبط `includeThoughts` على `true` في إعدادات طلبك. بعد ذلك، يمكنك الوصول إلى الملخّص من خلال تكرار `parts` في المَعلمة `response` والتحقّق من القيمة المنطقية `thought`.

في ما يلي مثال يوضّح كيفية تفعيل ملخّصات الأفكار واستردادها بدون البث، ما يؤدي إلى عرض ملخّص نهائي واحد للأفكار مع الردّ:

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

### انتقال

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

في ما يلي مثال على استخدام ميزة "المفكِّر" مع البث، ما يؤدي إلى عرض ملخّصات متزايدة ومتجدّدة أثناء الإنشاء:

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

### انتقال

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

## التحكّم في ميزة "المفكِّر"

تستخدم نماذج Gemini ميزة "المفكِّر" الديناميكي تلقائيًا، ما يؤدي إلى تعديل مقدار جهد الاستدلال استنادًا إلى مدى تعقيد طلب المستخدم.
مع ذلك، إذا كانت لديك قيود معيّنة على وقت الاستجابة أو كنت تريد أن يستخدم النموذج استدلالاً أعمق من المعتاد، يمكنك اختياريًا استخدام مَعلمات للتحكّم في سلوك ميزة "المفكِّر".

### مستويات "المفكِّر" (Gemini 3)

تتيح لك المَعلمة `thinkingLevel`، التي ننصح باستخدامها مع نماذج Gemini 3 والإصدارات الأحدث، التحكّم في سلوك الاستدلال.

يوضّح الجدول التالي إعدادات `thinkingLevel` لكل نوع من أنواع النماذج:

| مستوى التفكير | Gemini 3.1 Pro | ‫Gemini 3.1 Flash-Lite | Gemini 3 Flash | Gemini 3.5 Flash | الوصف |
| --- | --- | --- | --- | --- | --- |
| **`minimal`** | غير متاح | متاح (تلقائي) | متاح | متاح | يتطابق مع إعداد "بدون تفكير" لمعظم طلبات البحث. قد يفكّر النموذج بشكل بسيط جدًا في مهام الترميز المعقّدة. يقلّل وقت الاستجابة لتطبيقات المحادثة أو التطبيقات التي تعالج البيانات بمعدّل أعلى لنقل البيانات. يُرجى العِلم أنّ ضبط `minimal` لا يضمن إيقاف ميزة "المفكِّر". |
| **`low`** | متاح | متاح | متاح | متاح | يقلّل وقت الاستجابة والتكلفة. الخيار الأفضل لتنفيذ التعليمات البسيطة أو المحادثة أو التطبيقات التي تعالج البيانات بسرعة كبيرة. |
| **`medium`** | متاح | متاح | متاح | متاح (تلقائي) | تفكير متوازن لمعظم المهام. |
| **`high`** | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | متاح (تلقائي، ديناميكي) | متاح (ديناميكي) | يزيد من عمق الاستدلال إلى أقصى حد. قد يستغرق النموذج وقتًا أطول بكثير للوصول إلى أول رمز مميّز للناتج (بدون تفكير)، ولكن سيكون الناتج أكثر استدلالاً بعناية. |

يوضّح المثال التالي كيفية ضبط مستوى "المفكِّر".

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

### انتقال

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

لا يمكنك إيقاف ميزة "المفكِّر" في Gemini 3.1 Pro. لا يتيح Gemini 3 Flash وFlash-Lite أيضًا إيقاف ميزة "المفكِّر" بالكامل، ولكن يعني الإعداد `minimal` أنّ النموذج من غير المرجّح أن يفكّر (على الرغم من أنّه لا يزال بإمكانه ذلك).
إذا لم تحدّد مستوى "المفكِّر"، سيستخدم Gemini مستوى "المفكِّر" التلقائي لنماذج Gemini 3 (مثلاً، `"high"` لـ Gemini 3.1 Pro و`"medium"` لـ Gemini 3.5 Flash).

لا تتوافق نماذج Gemini 2.5 سلسلة مع `thinkingLevel`، لذا استخدِم `thinkingBudget` بدلاً من ذلك.

### ميزانيات "المفكِّر"

توجّه المَعلمة `thinkingBudget`، التي تم طرحها مع Gemini 2.5 سلسلة، النموذج بشأن العدد المحدّد من الرموز المميّزة التي يجب استخدامها للاستدلال.

في ما يلي تفاصيل إعدادات `thinkingBudget` لكل نوع من أنواع النماذج.
يمكنك إيقاف ميزة "المفكِّر" من خلال ضبط `thinkingBudget` على 0.
يؤدي ضبط `thinkingBudget` على -1 إلى تفعيل
**ميزة "المفكِّر" الديناميكي**، ما يعني أنّ النموذج سيعدّل الميزانية استنادًا إلى مدى تعقيد الطلب.

| الطراز | الإعداد التلقائي (لم يتم ضبط ميزانية "المفكِّر") | النطاق | إيقاف ميزة "المفكِّر" | تفعيل ميزة "المفكِّر" الديناميكي |
| --- | --- | --- | --- | --- |
| ‫**2.5 Pro** | ميزة "المفكِّر" الديناميكي | `128` إلى `32768` | غير متاح: لا يمكن إيقاف ميزة "المفكِّر" | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash** | ميزة "المفكِّر" الديناميكي | `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Preview** | ميزة "المفكِّر" الديناميكي | `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Lite** | لا يفكّر النموذج | `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| ‫**2.5 Flash Lite Preview** | لا يفكّر النموذج | `512` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` |
| ‫**Robotics-ER 1.6 Preview** | ميزة "المفكِّر" الديناميكي | `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |
| ‫**2.5 Flash Live Native Audio Preview (09-2025)** | ميزة "المفكِّر" الديناميكي | `0` إلى `24576` | `thinkingBudget = 0` | `thinkingBudget = -1` (تلقائي) |

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

### انتقال

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

استنادًا إلى الطلب، قد يتجاوز النموذج ميزانية الرموز المميّزة أو لا يستخدمها بالكامل.

## توقيعات الأفكار

إنّ Gemini API غير احتفاظي، لذا يتعامل النموذج مع كل طلب بيانات من واجهة برمجة التطبيقات بشكل مستقل ولا يمكنه الوصول إلى سياق الأفكار من الأدوار السابقة في التفاعلات المتعدّدة الأدوار.

من أجل تفعيل الاحتفاظ بسياق الأفكار في التفاعلات المتعدّدة الأدوار، يعرض Gemini توقيعات الأفكار، وهي تمثيلات مشفّرة لعملية التفكير الداخلية للنموذج.

- **تعرض نماذج Gemini 2.5** توقيعات الأفكار عند تفعيل ميزة "المفكِّر" وتضمين الطلب [ميزة "استدعاء الدالة"](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#thinking)، وتحديدًا [إعلانات الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-2).
- [**قد تعرض نماذج Gemini 3 توقيعات الأفكار لجميع أنواع الأجزاء.**](https://ai.google.dev/api/caching?hl=ar#Part)
  ننصحك دائمًا بإعادة إرسال جميع التوقيعات كما تم استلامها، ولكن *يجب* ذلك لتوقيعات ميزة "استدعاء الدالة". يمكنك قراءة صفحة
  [توقيعات الأفكار](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=ar) لمعرفة المزيد.

تشمل قيود الاستخدام الأخرى التي يجب أخذها في الاعتبار مع ميزة "استدعاء الدالة" ما يلي:

- يتم عرض التوقيعات من النموذج ضمن أجزاء أخرى في الردّ، مثلاً أجزاء ميزة "استدعاء الدالة" أو الأجزاء النصية.
  [أعِد إرسال الردّ بالكامل](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar#step-4)
  مع جميع الأجزاء إلى النموذج في الأدوار اللاحقة.
- لا تدمِج الأجزاء التي تتضمّن توقيعات معًا.
- لا تدمِج جزءًا يتضمّن توقيعًا مع جزء آخر لا يتضمّن توقيعًا.

## الأسعار

عند تفعيل ميزة "المفكِّر"، يكون تسعير الردّ هو مجموع الرموز المميّزة للناتج ورموز "المفكِّر" المميّزة. يمكنك الحصول على إجمالي عدد الرموز المميّزة لـ "المفكِّر" التي تم إنشاؤها من الحقل `thoughtsTokenCount`.

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

### انتقال

```
// ...
fmt.Println("Thoughts tokens:", response.UsageMetadata.ThoughtsTokenCount)
fmt.Println("Output tokens:", response.UsageMetadata.CandidatesTokenCount)
```

تنشئ نماذج "المفكِّر" أفكارًا كاملة لتحسين جودة الردّ النهائي
، ثم تعرض [ملخّصات](#summaries) لتقديم إحصاءات حول عملية التفكير. لذا، يستند التسعير إلى الرموز المميّزة للأفكار الكاملة التي يحتاج النموذج إلى إنشائها لإنشاء ملخّص، على الرغم من أنّ واجهة برمجة التطبيقات تعرض الملخّص فقط.

يمكنك التعرّف أكثر على الرموز المميّزة في [دليل عدّ الرموز المميّزة](https://ai.google.dev/gemini-api/docs/tokens?hl=ar).

## أفضل الممارسات

يتضمّن هذا القسم بعض الإرشادات لاستخدام نماذج "المفكِّر" بكفاءة.
كما هو الحال دائمًا، سيساعدك اتّباع [إرشادات الطلبات وأفضل الممارسات](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=ar) في الحصول على أفضل النتائج.

### تصحيح الأخطاء والتوجيه

- **مراجعة الاستدلال**: عندما لا تحصل على الردّ المتوقّع من نماذج
  "المفكِّر"، قد يساعدك تحليل ملخّصات الأفكار في Gemini بعناية.
  يمكنك الاطّلاع على كيفية تقسيم النموذج للمهمة والوصول إلى استنتاجه، واستخدام هذه المعلومات لتصحيح النتائج والحصول على النتائج الصحيحة.
- **تقديم إرشادات في الاستدلال**: إذا كنت تأمل في الحصول على ناتج طويل بشكل خاص
  ، قد تحتاج إلى تقديم إرشادات في طلبك للحدّ من
  [مقدار التفكير](#set-budget) الذي يستخدمه النموذج. يتيح لك ذلك الاحتفاظ بمزيد من الرموز المميّزة للناتج لردّك.

### مدى تعقيد المهام

- **المهام السهلة (يمكن إيقاف ميزة "المفكِّر"):** بالنسبة إلى الطلبات البسيطة التي لا تتطلّب استدلالاً معقدًا، مثل استرداد الحقائق أو التصنيف، لا تكون ميزة "المفكِّر" مطلوبة. تشمل الأمثلة ما يلي:
  - "أين تم تأسيس DeepMind؟"
  - "هل يطلب هذا البريد الإلكتروني عقد اجتماع أم يقدّم معلومات فقط؟"
- **المهام المتوسطة (تلقائي/بعض التفكير):** تستفيد العديد من الطلبات الشائعة من درجة من المعالجة خطوة بخطوة أو فهم أعمق. يمكن أن يستخدم Gemini بمرونة ميزة "المفكِّر" لمهام مثل:
  - تشبيه التمثيل الضوئي بالنمو
  - مقارنة السيارات الكهربائية والسيارات الهجينة
- **المهام الصعبة (أقصى إمكانات "المفكِّر"):** بالنسبة إلى التحديات المعقدة حقًا، مثل حلّ مسائل الرياضيات المعقدة أو مهام الترميز، ننصحك بضبط ميزانية عالية لميزة "المفكِّر". تتطلّب هذه الأنواع من المهام أن يستخدم النموذج إمكاناته الكاملة في الاستدلال والتخطيط، وغالبًا ما تتضمّن العديد من الخطوات الداخلية قبل تقديم إجابة. تشمل الأمثلة ما يلي:
  - حلّ المسألة 1 في AIME 2025: أوجِد مجموع جميع الأسس الصحيحة b > 9 التي يكون فيها
    ‎17b قاسمًا لـ ‎97b.
  - اكتب رمز Python لتطبيق ويب يعرض بيانات سوق الأسهم في الوقت الفعلي، بما في ذلك مصادقة المستخدم. اجعل الرمز فعّالاً قدر الإمكان.

## النماذج والأدوات والإمكانات المتوافقة

تتوافق ميزات "المفكِّر" مع جميع نماذج السلسلتَين 3 و2.5.
يمكنك الاطّلاع على جميع إمكانات النموذج في صفحة
[نظرة عامة على النموذج](https://ai.google.dev/gemini-api/docs/models?hl=ar).

تعمل نماذج "المفكِّر" مع جميع أدوات وإمكانات Gemini. يتيح ذلك للنماذج التفاعل مع الأنظمة الخارجية أو تنفيذ الرموز أو الوصول إلى المعلومات في الوقت الفعلي، ودمج النتائج في عملية الاستدلال والردّ النهائي.

يمكنك تجربة أمثلة على استخدام الأدوات مع نماذج "المفكِّر" في [كتاب الطبخ الخاص بميزة "المفكِّر"][Colab].

## ما هي الخطوات التالية؟

- تتوفّر تغطية ميزة "المفكِّر" في دليل [التوافق مع OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=ar#thinking).

[Colab]: https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get\_started\_thinking.ipynb

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-06-04 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-06-04 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
