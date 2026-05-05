---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=ko
fetched_at: 2026-05-05T20:09:54.127351+00:00
title: "\ucf54\ub4dc \uc2e4\ud589 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=ko)를 이제 공동 계획, 시각화, MCP 지원 등과 함께 미리보기로 이용할 수 있습니다.

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 코드 실행

Gemini API는 모델이 Python 코드를 생성하고 실행할 수 있는 코드 실행 도구를 제공합니다. 그런 다음 모델은 최종 출력을 도출할 때까지 코드 실행 결과를 통해 반복적으로 학습할 수 있습니다. 코드 실행을 사용하여 코드 기반 추론의 이점을 활용하는 애플리케이션을 빌드할 수 있습니다. 예를 들어 코드 실행을 사용하여 방정식을 풀거나 텍스트를 처리할 수 있습니다. 코드 실행 환경에 포함된 [라이브러리](#supported-libraries)를 사용하여 더 전문적인 작업을 실행할 수도 있습니다.

Gemini는 Python으로만 코드를 실행할 수 있습니다. Gemini에 다른 언어로 코드를 생성해 달라고 요청할 수는 있지만 모델이 코드 실행 도구를 사용하여 코드를 실행할 수는 없습니다.

## 코드 실행 사용 설정

코드 실행을 사용 설정하려면 모델에서 코드 실행 도구를 구성하세요. 이를 통해 모델이 코드를 생성하고 실행할 수 있습니다.

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

### 자바스크립트

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

### Go

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

출력은 가독성을 위해 서식이 지정된 다음과 같이 표시될 수 있습니다.

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

이 출력은 코드 실행을 사용할 때 모델이 반환하는 여러 콘텐츠 부분을 결합합니다.

- `text`: 모델에서 생성된 인라인 텍스트
- `executableCode`: 실행 목적으로 모델에서 생성된 코드
- `codeExecutionResult`: 실행 가능한 코드의 결과

이러한 부분의 이름 지정 규칙은 프로그래밍 언어에 따라 다릅니다.

## 이미지를 사용한 코드 실행 (Gemini 3)

이제 Gemini 3 Flash 모델이 Python 코드를 작성하고 실행하여 이미지를 적극적으로 조작하고 검사할 수 있습니다.

**사용 사례**

- **확대/축소 및 검사**: 모델은 세부정보가 너무 작을 때(예: 멀리 있는 게이지를 읽는 경우) 이를 암시적으로 감지하고 더 높은 해상도로 영역을 잘라 다시 검사하는 코드를 작성합니다.
- **시각적 수학**: 모델은 코드를 사용하여 다단계 계산을 실행할 수 있습니다 (예: 영수증의 항목 합계).
- **이미지 주석**: 모델은 질문에 답하기 위해 이미지를 주석으로 달 수 있습니다(예: 관계를 보여주는 화살표를 그림).

### 이미지를 사용한 코드 실행 사용 설정

이미지를 사용한 코드 실행은 Gemini 3 Flash에서 공식적으로 지원됩니다. 도구로서의 코드 실행과 사고를 모두 사용 설정하면 이 동작을 활성화할 수 있습니다.

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

### 자바스크립트

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

### Go

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

## 채팅에서 코드 실행 사용

채팅의 일부로 코드 실행을 사용할 수 있습니다.

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

### 자바스크립트

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

### Go

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

## 입력/출력 (I/O)

코드 실행은 파일 입력과 그래프 출력을 지원합니다. 이러한 입력 및 출력 기능을 사용하면 CSV 파일과 텍스트 파일을 업로드하고 파일에 대해 질문하고 대답의 일부로 [Matplotlib](https://matplotlib.org/) 그래프를 생성할 수 있습니다. 출력 파일은 응답에 인라인 이미지로 반환됩니다.

### I/O 가격 책정

코드 실행 I/O를 사용하면 입력 토큰과 출력 토큰에 대한 요금이 청구됩니다.

**입력 토큰:**

- 사용자 프롬프트

**출력 토큰:**

- 모델에서 생성된 코드
- 코드 환경의 코드 실행 출력
- 사고 토큰
- 모델에서 생성된 요약

### I/O 세부정보

코드 실행 I/O를 사용할 때는 다음 기술 세부정보에 유의하세요.

- 코드 환경의 최대 런타임은 30초입니다.
- 코드 환경에서 오류가 발생하면 모델이 코드 출력을 재생성할 수 있습니다. 이러한 상황은 최대 5번까지 발생할 수 있습니다.
- 최대 파일 입력 크기는 모델 토큰 창에 의해 제한됩니다. AI Studio에서 최대 입력 파일 크기는 100만 토큰입니다 (지원되는 입력 유형의 텍스트 파일의 경우 약 2MB). 너무 큰 파일을 업로드하면 AI Studio에서 전송할 수 없습니다.
- 코드 실행은 텍스트 및 CSV 파일에서 가장 잘 작동합니다.
- 입력 파일은 `part.inlineData` 또는 `part.fileData` ([Files API](https://ai.google.dev/gemini-api/docs/files?hl=ko)를 통해 업로드됨)로 전달할 수 있으며 출력 파일은 항상 `part.inlineData`로 반환됩니다.

## 결제

Gemini API에서 코드 실행을 사용 설정하는 데에는 추가 비용이 발생하지 않습니다.
사용 중인 Gemini 모델에 따라 입력 및 출력 토큰의 현재 요율로 비용이 청구됩니다.

코드 실행의 청구에 대해 몇 가지 중요한 사항은 다음과 같습니다.

- 모델에 전달하는 입력 토큰에 대해서는 비용이 한 번만 청구되며, 모델에서 사용자에게 반환하는 최종 출력 토큰에 대해서는 비용이 청구됩니다.
- 생성된 코드를 나타내는 토큰은 출력 토큰으로 계산됩니다. 생성된 코드에는 텍스트 및 멀티모달 출력(예: 이미지)이 포함될 수 있습니다.
- 코드 실행 결과도 출력 토큰으로 집계됩니다.

결제 모델은 다음 다이어그램에 나와 있습니다.

![코드 실행 청구 모델](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=ko)

- 사용 중인 Gemini 모델에 따라 입력 및 출력 토큰의 현재 요율로 비용이 청구됩니다.
- 응답을 생성할 때 Gemini에 코드 실행이 사용되는 경우 원본 프롬프트, 생성된 코드, 실행된 코드 결과가 *중간 토큰* 라벨로 표시되고 *입력 토큰*으로 청구됩니다.
- 그런 후 Gemini가 요약을 생성하고 생성된 코드, 실행된 코드 결과, 최종 요약을 반환합니다. 이러한 토큰은 *출력 토큰*으로 청구됩니다.
- Gemini API에는 API 응답에 중간 토큰 수가 포함되기 때문에 초기 프롬프트 이상으로 추가된 입력 토큰이 발생하는 이유를 알 수 있습니다.

## 제한사항

- 모델은 코드를 생성 및 실행할 수만 있습니다. 미디어 파일과 같은 다른 아티팩트는 반환할 수 없습니다.
- 일부 경우에 코드 실행을 사용 설정하면 모델 출력의 다른 영역(예: 스토리 작성)에서 성능이 저하될 수 있습니다.
- 모델마다 코드 실행을 성공적으로 사용하는 기능에 약간의 차이가 있습니다.

## 지원되는 도구 조합

코드 실행 도구를 [Google 검색을 사용한 그라운딩](https://ai.google.dev/gemini-api/docs/google-search?hl=ko)과 결합하여 더 복잡한 사용 사례를 지원할 수 있습니다.

Gemini 3 모델은 코드 실행과 같은 기본 제공 도구와 맞춤 도구(함수 호출)의 조합을 지원합니다. 도구 조합이 작동하려면 `id` 및 `thought_signature` 필드를 다시 전달해야 합니다. [도구 조합](https://ai.google.dev/gemini-api/docs/tool-combination?hl=ko) 페이지에서 자세히 알아보세요.

## 지원되는 라이브러리

코드 실행 환경에는 다음 라이브러리가 포함됩니다.

- attrs
- 체스
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
- 패키징
- pandas
- pillow
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
- 육
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

사용자의 고유 라이브러리는 설치할 수 없습니다.

## 다음 단계

- [코드 실행 Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=ko)을 사용해 보세요.
- 다른 Gemini API 도구 알아보기:
  - [함수 호출](https://ai.google.dev/gemini-api/docs/function-calling?hl=ko)
  - [Google 검색으로 그라운딩](https://ai.google.dev/gemini-api/docs/grounding?hl=ko)

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-04-29(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-04-29(UTC)"],[],[]]
