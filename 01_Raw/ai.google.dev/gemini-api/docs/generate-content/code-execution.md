---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=ru
fetched_at: 2026-11-02T07:11:30.384422+00:00
title: "\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u043a\u043e\u0434\u0430 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Доступна новая модель Gemini 4 Argon. [Попробовать](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ru)

![](https://ai.google.dev/_static/images/translated.svg?hl=ru)

Чтобы переводить контент на ваш предпочитаемый язык, Google использует технологии на основе искусственного интеллекта. Переводы от ИИ могут содержать ошибки.

- [Главная](https://ai.google.dev/?hl=ru)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ru)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=ru)
- [Документация](https://ai.google.dev/gemini-api/docs/generate-content?hl=ru)

Отправить отзыв

# Выполнение кода

В Gemini API есть инструмент для выполнения кода, который позволяет модели генерировать и выполнять код на Python. Затем модель может итеративно учиться на результатах выполнения кода, пока не придет к окончательному выводу. Выполнение кода можно использовать для создания приложений, в которых задействованы рассуждения на основе кода. Например, с помощью выполнения кода можно решать уравнения или обрабатывать текст. Вы также можете использовать [библиотеки](#supported-libraries), включенные в среду выполнения кода, для выполнения более специализированных задач.

Gemini может выполнять код только на Python. Вы по-прежнему можете попросить Gemini сгенерировать код на другом языке, но модель не сможет запустить его с помощью инструмента выполнения кода.

## Как включить выполнение кода

Чтобы включить выполнение кода, настройте инструмент выполнения кода в модели. Это позволяет модели генерировать и запускать код.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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

### Проложить маршрут

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
        "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

Вывод может выглядеть примерно так, как показано ниже (для удобства чтения он отформатирован):

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

Этот вывод объединяет несколько частей контента, которые модель возвращает при использовании выполнения кода:

- `text`: встроенный текст, сгенерированный моделью.
- `executableCode` – код, сгенерированный моделью и предназначенный для выполнения.
- `codeExecutionResult` – результат выполнения исполняемого кода.

Названия этих частей зависят от языка программирования.

## Выполнение кода с изображениями (Gemini 3)

Модель Gemini 3 Flash теперь может писать и выполнять код на Python, чтобы активно манипулировать изображениями и проверять их.

**Примеры использования**

- **Увеличение и проверка.** Модель неявно обнаруживает, когда детали слишком малы (например, при считывании показаний удаленного датчика), и пишет код для кадрирования и повторного изучения области с более высоким разрешением.
- **Визуальная математика.** Модель может выполнять многоэтапные вычисления с помощью кода, например суммировать позиции в чеке.
- **Аннотации к изображениям.** Модель может добавлять к изображениям аннотации, чтобы отвечать на вопросы, например рисовать стрелки, показывающие связи.

### Как включить выполнение кода с изображениями

Выполнение кода с изображениями официально поддерживается в Gemini 3 Flash. Чтобы активировать такое поведение, включите и выполнение кода, и рассуждение.

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Проложить маршрут

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
        "gemini-3.8-flash",
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
MODEL="gemini-3.8-flash"

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

## Как использовать выполнение кода в чате

Вы также можете использовать выполнение кода в чате.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash",
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
  model: "gemini-3.8-flash",
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

### Проложить маршрут

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
        "gemini-3.8-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## Ввод-вывод (I/O)

Выполнение кода поддерживает входные файлы и выходные графики. Используя эти возможности ввода и вывода, вы можете загружать CSV- и текстовые файлы, задавать вопросы о них и получать в ответе графики [Matplotlib](https://matplotlib.org/). Выходные файлы возвращаются в виде встроенных изображений в ответе.

### Цены на ввод-вывод

При использовании ввода-вывода для выполнения кода с вас взимается плата за входные и выходные токены:

**Входные токены:**

- Запрос пользователя

**Выходные токены:**

- Код, сгенерированный моделью
- Вывод выполнения кода в среде кода
- Токены мышления
- Сводка, созданная моделью

### Сведения о Google I/O

При работе с вводом-выводом для выполнения кода учитывайте следующие технические детали:

- Максимальное время выполнения кода в среде – 30 секунд.
- Если в среде выполнения кода возникает ошибка, модель может решить сгенерировать код заново. Это может произойти до пяти раз.
- Максимальный размер входного файла ограничен окном токенов модели. В AI Studio максимальный размер входного файла составляет 1 млн токенов (примерно 2 МБ для текстовых файлов поддерживаемых типов). Если вы попытаетесь загрузить слишком большой файл, AI Studio не позволит вам отправить его.
- Выполнение кода лучше всего работает с текстовыми файлами и файлами CSV.
- Входной файл можно передать в формате `part.inlineData` или `part.fileData` (загрузить с помощью [Files API](https://ai.google.dev/gemini-api/docs/files?hl=ru)), а выходной файл всегда возвращается в формате `part.inlineData`.

## Оплата

Дополнительная плата за выполнение кода с помощью Gemini API не взимается.
Плата будет взиматься по текущему тарифу за входные и выходные токены в зависимости от используемой модели Gemini.

Вот ещё несколько важных моментов, касающихся оплаты за выполнение кода:

- Вы платите только за входные токены, которые передаете модели, и за выходные токены, которые она возвращает.
- Токены, представляющие сгенерированный код, считаются выходными. Сгенерированный код может включать текст и мультимодальные выходные данные, например изображения.
- Результаты выполнения кода также считаются выходными токенами.

Модель оплаты показана на следующей схеме:

![модель оплаты за выполнение кода](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=ru)

- Плата взимается по текущему тарифу за входные и выходные токены в зависимости от используемой модели Gemini.
- Если Gemini использует выполнение кода при генерации ответа, исходный запрос, сгенерированный код и результат его выполнения помечаются как *промежуточные токены* и оплачиваются как *входные токены*.
- Затем Gemini генерирует сводку и возвращает сгенерированный код, результат его выполнения и итоговую сводку. Они оплачиваются как *выходные токены*.
- Gemini API включает количество промежуточных токенов в ответ API, чтобы вы знали, почему получаете дополнительные входные токены помимо исходного запроса.

## Ограничения

- Модель может только генерировать и выполнять код. Другие объекты, например медиафайлы, восстановить нельзя.
- В некоторых случаях включение выполнения кода может привести к регрессии в других областях выходных данных модели (например, при написании истории).
- Способность успешно выполнять код у разных моделей может различаться.

## Поддерживаемые комбинации инструментов

Инструмент выполнения кода можно комбинировать с [обоснованием с Google Поиском](https://ai.google.dev/gemini-api/docs/google-search?hl=ru), чтобы решать более сложные задачи.

Модели Gemini 4 и Gemini 3 поддерживают сочетание встроенных инструментов (например, выполнения кода) с пользовательскими инструментами (вызовом функций). Чтобы комбинация инструментов работала, необходимо передать поля `id` и `thought_signature`. Подробнее [о сочетаниях инструментов](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ru)…

## Поддерживаемые библиотеки

Среда выполнения кода включает следующие библиотеки:

- attrs
- шахматы
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
- numpy
- opencv-python
- openpyxl
- упаковка
- панды
- подушка
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
- шесть
- striprtf
- sympy
- табулировать
- tensorflow
- toolz
- xlrd

Устанавливать собственные библиотеки нельзя.

## Дальнейшие действия

- Попробуйте [Colab для выполнения кода](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=ru).
- Узнайте о других инструментах Gemini API:
  - [Вызов функций](https://ai.google.dev/gemini-api/docs/function-calling?hl=ru)
  - [Обоснование с Google Поиском](https://ai.google.dev/gemini-api/docs/grounding?hl=ru)

Отправить отзыв

Если не указано иное, контент на этой странице предоставляется по [лицензии Creative Commons "С указанием авторства 4.0"](https://creativecommons.org/licenses/by/4.0/), а примеры кода – по [лицензии Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Подробнее об этом написано в [правилах сайта](https://developers.google.com/site-policies?hl=ru). Java – это зарегистрированный товарный знак корпорации Oracle и ее аффилированных лиц.

Последнее обновление: 2026-10-13 UTC.

Хотите рассказать подробнее?

[[["Прост для понимания","easyToUnderstand","thumb-up"],["Помог мне решить мою проблему","solvedMyProblem","thumb-up"],["Другое","otherUp","thumb-up"]],[["Отсутствует нужная мне информация","missingTheInformationINeed","thumb-down"],["Слишком сложен/слишком много шагов","tooComplicatedTooManySteps","thumb-down"],["Устарел","outOfDate","thumb-down"],["Проблема с переводом текста","translationIssue","thumb-down"],["Проблемы образцов/кода","samplesCodeIssue","thumb-down"],["Другое","otherDown","thumb-down"]],["Последнее обновление: 2026-10-13 UTC."],[],[]]
