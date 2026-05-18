---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=ar
fetched_at: 2026-05-18T05:15:58.110564+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# تنفيذ الرمز البرمجي

توفّر Gemini API أداة لتنفيذ الرموز البرمجية تتيح للنموذج إنشاء رموز Python البرمجية وتشغيلها. يمكن للنموذج بعد ذلك التعلّم بشكل متكرّر من نتائج تنفيذ الرموز البرمجية إلى أن يصل إلى ناتج نهائي. يمكنك استخدام أداة تنفيذ الرموز البرمجية لإنشاء تطبيقات تستفيد من الاستدلال المستند إلى الرموز البرمجية. على سبيل المثال، يمكنك استخدام أداة تنفيذ الرموز البرمجية لحلّ المعادلات أو معالجة النصوص. يمكنك
أيضًا استخدام [المكتبات](#supported-libraries) المضمّنة في بيئة تنفيذ الرموز البرمجية
لإجراء مهام أكثر تخصّصًا.

لا يمكن لـ Gemini تنفيذ الرموز البرمجية إلا بلغة Python. يمكنك مع ذلك أن تطلب من Gemini إنشاء رموز برمجية بلغة أخرى، ولكن لا يمكن للنموذج استخدام أداة تنفيذ الرموز البرمجية لتشغيلها.

## تفعيل أداة تنفيذ الرموز البرمجية

لتفعيل أداة تنفيذ الرموز البرمجية، عليك ضبطها على النموذج. يسمح ذلك للنموذج بإنشاء الرموز البرمجية وتشغيلها.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### انتقال

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
}'
```

قد يبدو الناتج على النحو التالي، وقد تم تنسيقه ليكون أكثر سهولة في القراءة:

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

يجمع هذا الناتج عدة أجزاء من المحتوى يعرضها النموذج عند استخدام أداة تنفيذ الرموز البرمجية:

- `text`: نص مضمّن من إنشاء النموذج
- `executableCode`: رمز من إنشاء النموذج يُفترض تنفيذه
- `codeExecutionResult`: نتيجة الرمز القابل للتنفيذ

تختلف اصطلاحات التسمية لهذه الأجزاء حسب لغة البرمجة.

## تنفيذ الرموز البرمجية باستخدام الصور (Gemini 3)

يمكن الآن لنموذج Gemini 3 Flash كتابة رموز Python البرمجية وتنفيذها لمعالجة الصور وفحصها بشكل نشط.

**حالات الاستخدام**

- **التكبير والفحص**: يرصد النموذج ضمنيًا متى تكون التفاصيل صغيرة جدًا (مثل قراءة مقياس بعيد)، ويكتب رمزًا لاقتصاص المنطقة وإعادة فحصها بدقة أعلى.
- **الرياضيات المرئية**: يمكن للنموذج إجراء عمليات حسابية متعددة الخطوات باستخدام الرمز (مثل
  جمع بنود في فاتورة).
- **إضافة تعليقات توضيحية إلى الصور**: يمكن للنموذج إضافة تعليقات توضيحية إلى الصور للإجابة عن الأسئلة، مثل
  رسم أسهم لإظهار العلاقات.

### تفعيل أداة تنفيذ الرموز البرمجية باستخدام الصور

تتوفّر أداة تنفيذ الرموز البرمجية باستخدام الصور رسميًا في Gemini 3 Flash. يمكنك تفعيل هذا السلوك من خلال تفعيل كل من "تنفيذ الرموز البرمجية" كأداة و"التفكير".

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
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
    "io"
    "log"
    "net/http"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3-flash-preview"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## استخدام أداة تنفيذ الرموز البرمجية في المحادثة

يمكنك أيضًا استخدام أداة تنفيذ الرموز البرمجية كجزء من محادثة.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3-flash-preview",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### انتقال

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3-flash-preview",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## الإدخال والإخراج

تتيح أداة تنفيذ الرموز البرمجية إدخال الملفات وإخراج الرسوم البيانية. باستخدام إمكانات الإدخال و
الإخراج هذه، يمكنك تحميل ملفات CSV وملفات نصية وطرح أسئلة حول الـ
ملفات، وإنشاء رسوم بيانية باستخدام [Matplotlib](https://matplotlib.org/) كجزء
من الردّ. يتم عرض ملفات الإخراج كصور مضمّنة في الردّ.

### تسعير الإدخال والإخراج

عند استخدام إمكانات الإدخال والإخراج في أداة تنفيذ الرموز البرمجية، يتم تحصيل رسوم منك مقابل الرموز المميّزة للإدخال والرموز المميّزة للإخراج:

**الرموز المميّزة للإدخال:**

- طلب المستخدم

**الرموز المميّزة للإخراج:**

- الرمز من إنشاء النموذج
- ناتج تنفيذ الرمز البرمجي في بيئة الرمز البرمجي
- الرموز المميّزة للتفكير
- الملخّص من إنشاء النموذج

### تفاصيل الإدخال والإخراج

عند استخدام إمكانات الإدخال والإخراج في أداة تنفيذ الرموز البرمجية، يجب الانتباه إلى التفاصيل الفنية التالية:

- الحد الأقصى لوقت تشغيل بيئة الرمز البرمجي هو 30 ثانية.
- إذا أدت بيئة الرمز البرمجي إلى حدوث خطأ، قد يقرّر النموذج إعادة إنشاء ناتج الرمز البرمجي. ويمكن أن يحدث ذلك ما يصل إلى 5 مرات.
- يتم تحديد الحد الأقصى لحجم ملف الإدخال من خلال نافذة الرموز المميّزة للنموذج. في AI Studio، يبلغ الحد الأقصى لحجم ملف الإدخال مليون رمز مميّز (حوالي 2 ميغابايت للملفات النصية من أنواع الإدخال المتوافقة). إذا حمّلت ملفًا كبيرًا جدًا، لن يسمح لك AI Studio بإرساله.
- تعمل أداة تنفيذ الرموز البرمجية بشكل أفضل مع الملفات النصية وملفات CSV.
- يمكن تمرير ملف الإدخال في `part.inlineData` أو `part.fileData` (الذي يتم تحميله
  من خلال [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ar))، ويتم دائمًا عرض ملف الإخراج على أنّه `part.inlineData`.

## الفوترة

لا يتم تحصيل أي رسوم إضافية مقابل تفعيل أداة تنفيذ الرموز البرمجية من Gemini API.
سيتم تحصيل رسوم منك بالسعر الحالي للرموز المميّزة للإدخال والإخراج استنادًا إلى نموذج Gemini الذي تستخدمه.

في ما يلي بعض المعلومات الأخرى التي يجب معرفتها حول الفوترة لتنفيذ الرموز البرمجية:

- يتم تحصيل رسوم منك مرة واحدة فقط مقابل الرموز المميّزة للإدخال التي تمرّرها إلى النموذج، ويتم تحصيل رسوم منك مقابل الرموز المميّزة للإخراج النهائي التي يعرضها لك النموذج.
- يتم احتساب الرموز المميّزة التي تمثّل الرمز البرمجي الذي تم إنشاؤه كرموز مميّزة للإخراج. يمكن أن يشمل الرمز البرمجي الذي تم إنشاؤه نصًا ونتائج متعددة الوسائط، مثل الصور.
- يتم أيضًا احتساب نتائج تنفيذ الرموز البرمجية كرموز مميّزة للإخراج.

يظهر نموذج الفوترة في الرسم البياني التالي:

![نموذج الفوترة الخاص بتنفيذ الرموز البرمجية](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=ar)

- سيتم تحصيل رسوم منك بالسعر الحالي للرموز المميّزة للإدخال والإخراج استنادًا إلى نموذج Gemini الذي تستخدمه.
- إذا استخدم Gemini أداة تنفيذ الرموز البرمجية عند إنشاء ردّك، يتم تصنيف الطلب الأصلي والرمز البرمجي الذي تم إنشاؤه ونتيجة الرمز البرمجي الذي تم تنفيذه على أنّها *رموز مميّزة وسيطة* ويتم تحصيل رسوم منك مقابلها كـ *رموز مميّزة للإدخال*.
- ينشئ Gemini بعد ذلك ملخّصًا ويعرض الرمز البرمجي الذي تم إنشاؤه ونتيجة الرمز البرمجي الذي تم تنفيذه والملخّص النهائي. ويتم تحصيل رسوم منك مقابل هذه العناصر كـ *رموز مميّزة للإخراج*.
- تتضمّن Gemini API عدد الرموز المميّزة الوسيطة في الردّ من واجهة برمجة التطبيقات، ما يتيح لك معرفة سبب حصولك على رموز مميّزة إضافية للإدخال بخلاف طلبك الأولي.

## القيود

- لا يمكن للنموذج سوى إنشاء الرموز البرمجية وتنفيذها. ولا يمكنه عرض عناصر أخرى، مثل ملفات الوسائط.
- في بعض الحالات، يمكن أن يؤدي تفعيل أداة تنفيذ الرموز البرمجية إلى حدوث تراجع في مجالات أخرى من مخرجات النموذج (على سبيل المثال، كتابة قصة).
- هناك بعض الاختلاف في قدرة النماذج المختلفة على استخدام أداة تنفيذ الرموز البرمجية بنجاح.

## مجموعات الأدوات المتوافقة

يمكن الجمع بين أداة تنفيذ الرموز البرمجية و
[تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/google-search?hl=ar) لـ
تقديم حالات استخدام أكثر تعقيدًا.

تتيح نماذج Gemini 3 الجمع بين الأدوات المضمّنة (مثل "تنفيذ الرموز البرمجية") والأدوات المخصّصة (استدعاء الدوال). عليك إعادة حقلَي `id` و`thought_signature` لكي يعمل الجمع بين الأدوات. مزيد من المعلومات على صفحة
[مجموعات الأدوات](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ar)

## المكتبات المتوافقة

تتضمّن بيئة تنفيذ الرموز البرمجية المكتبات التالية:

- attrs
- شطرنج
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- مكتبة نامبي
- opencv-python
- openpyxl
- حزمة محتوى التطبيق
- باندا
- وسادة
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- seaborn
- ستة
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

لا يمكنك تثبيت مكتباتك الخاصة.

## الخطوات التالية

- جرِّب أداة تنفيذ الرموز البرمجية في Colab.
- تعرَّف على أدوات Gemini API الأخرى:
  - [استدعاء الدوال](https://ai.google.dev/gemini-api/docs/function-calling?hl=ar)
  - [تحديد المصدر من خلال "بحث Google"](https://ai.google.dev/gemini-api/docs/grounding?hl=ar)

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-13 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
