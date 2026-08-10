---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=vi
fetched_at: 2026-08-10T03:19:02.277788+00:00
title: "Th\u1ef1c thi m\u00e3 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Thực thi mã

Gemini API cung cấp một công cụ thực thi mã cho phép mô hình tạo và chạy mã Python. Sau đó, mô hình có thể học lặp đi lặp lại từ kết quả thực thi mã cho đến khi đạt được kết quả cuối cùng. Bạn có thể sử dụng tính năng thực thi mã để tạo các ứng dụng có lợi từ hoạt động suy luận dựa trên mã. Ví dụ: bạn có thể sử dụng tính năng thực thi mã để giải phương trình hoặc xử lý văn bản. Bạn cũng có thể sử dụng [các thư viện](#supported-libraries) có trong môi trường thực thi mã để thực hiện các tác vụ chuyên biệt hơn.

Gemini chỉ có thể thực thi mã bằng Python. Bạn vẫn có thể yêu cầu Gemini tạo mã bằng một ngôn ngữ khác, nhưng mô hình không thể sử dụng công cụ thực thi mã để kích hoạt mã đó.

## Bật tính năng thực thi mã

Để bật tính năng thực thi mã, hãy định cấu hình công cụ thực thi mã trên mô hình. Điều này cho phép mô hình tạo và chạy mã.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

Đầu ra có thể có dạng như sau (đã được định dạng để dễ đọc):

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

Đầu ra này kết hợp một số phần nội dung mà mô hình trả về khi sử dụng tính năng thực thi mã:

- `text`: Văn bản cùng dòng do mô hình tạo
- `executableCode`: Mã do mô hình tạo ra để thực thi
- `codeExecutionResult`: Kết quả của mã thực thi

Quy ước đặt tên cho các phần này sẽ khác nhau tuỳ theo ngôn ngữ lập trình.

## Thực thi mã với hình ảnh (Gemini 3)

Giờ đây, mô hình Gemini 3 Flash có thể viết và thực thi mã Python để chủ động thao tác và kiểm tra hình ảnh.

**Trường hợp sử dụng**

- **Thu phóng và kiểm tra**: Mô hình này tự động phát hiện khi các chi tiết quá nhỏ (ví dụ: đọc một đồng hồ đo ở xa) và viết mã để cắt cũng như kiểm tra lại khu vực ở độ phân giải cao hơn.
- **Phép tính trực quan**: Mô hình có thể chạy các phép tính nhiều bước bằng mã (ví dụ: cộng các mục hàng trên biên nhận).
- **Chú thích hình ảnh**: Mô hình có thể chú thích hình ảnh để trả lời câu hỏi, chẳng hạn như vẽ mũi tên để cho thấy mối quan hệ.

### Bật tính năng Thực thi mã bằng hình ảnh

Tính năng Thực thi mã với hình ảnh được hỗ trợ chính thức trong Gemini 3 Flash. Bạn có thể kích hoạt hành vi này bằng cách bật cả tính năng Thực thi mã như một công cụ và Tư duy.

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
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
MODEL="gemini-3.6-flash"

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

## Sử dụng tính năng thực thi mã trong cuộc trò chuyện

Bạn cũng có thể sử dụng tính năng thực thi mã trong cuộc trò chuyện.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
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
  model: "gemini-3.6-flash",
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
        "gemini-3.6-flash",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
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

## Đầu vào/đầu ra (I/O)

Tính năng thực thi mã hỗ trợ dữ liệu đầu vào là tệp và dữ liệu đầu ra là biểu đồ. Bằng cách sử dụng các khả năng đầu vào và đầu ra này, bạn có thể tải tệp CSV và tệp văn bản lên, đặt câu hỏi về các tệp và nhận được các biểu đồ [Matplotlib](https://matplotlib.org/) được tạo trong phần phản hồi. Các tệp đầu ra được trả về dưới dạng hình ảnh cùng dòng trong câu trả lời.

### Giá I/O

Khi sử dụng I/O thực thi mã, bạn sẽ bị tính phí cho mã thông báo đầu vào và mã thông báo đầu ra:

**Mã thông báo đầu vào:**

- Câu lệnh của người dùng

**Mã thông báo đầu ra:**

- Mã do mô hình tạo
- Kết quả thực thi mã trong môi trường mã
- Mã thông báo tư duy
- Bản tóm tắt do mô hình tạo

### Thông tin chi tiết về I/O

Khi bạn làm việc với I/O thực thi mã, hãy lưu ý đến các thông tin kỹ thuật sau:

- Thời gian chạy tối đa của môi trường mã là 30 giây.
- Nếu môi trường mã tạo ra lỗi, mô hình có thể quyết định tạo lại đầu ra mã. Điều này có thể xảy ra tối đa 5 lần.
- Kích thước tối đa của tệp đầu vào bị giới hạn bởi cửa sổ mã thông báo của mô hình. Trong AI Studio, kích thước tệp đầu vào tối đa là 1 triệu mã thông báo (khoảng 2 MB đối với tệp văn bản thuộc các loại đầu vào được hỗ trợ). Nếu bạn tải một tệp quá lớn lên, AI Studio sẽ không cho phép bạn gửi tệp đó.
- Tính năng thực thi mã hoạt động hiệu quả nhất với tệp văn bản và tệp CSV.
- Bạn có thể truyền tệp đầu vào trong `part.inlineData` hoặc `part.fileData` (được tải lên thông qua [Files API](https://ai.google.dev/gemini-api/docs/files?hl=vi)) và tệp đầu ra luôn được trả về dưới dạng `part.inlineData`.

## Thanh toán

Bạn không phải trả thêm phí khi bật tính năng thực thi mã từ Gemini API.
Bạn sẽ bị tính phí theo mức giá hiện tại của mã thông báo đầu vào và đầu ra dựa trên mô hình Gemini mà bạn đang sử dụng.

Sau đây là một số thông tin khác bạn cần biết về việc tính phí thực thi mã:

- Bạn chỉ bị tính phí một lần cho các mã thông báo đầu vào mà bạn truyền đến mô hình và bạn sẽ bị tính phí cho các mã thông báo đầu ra cuối cùng mà mô hình trả về cho bạn.
- Các mã thông báo đại diện cho mã được tạo sẽ được tính là mã thông báo đầu ra. Mã được tạo có thể bao gồm văn bản và kết quả đầu ra đa phương thức như hình ảnh.
- Kết quả thực thi mã cũng được tính là mã thông báo đầu ra.

Mô hình thanh toán được minh hoạ trong sơ đồ sau:

![mô hình thanh toán khi thực thi mã](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=vi)

- Bạn sẽ bị tính phí theo mức giá hiện tại của mã thông báo đầu vào và đầu ra dựa trên mô hình Gemini mà bạn đang sử dụng.
- Nếu Gemini sử dụng tính năng thực thi mã khi tạo câu trả lời cho bạn, thì câu lệnh ban đầu, mã được tạo và kết quả của mã đã thực thi sẽ được gắn nhãn là *mã thông báo trung gian* và được tính phí là *mã thông báo đầu vào*.
- Sau đó, Gemini sẽ tạo bản tóm tắt và trả về mã đã tạo, kết quả của mã đã thực thi và bản tóm tắt cuối cùng. Các mã thông báo này được tính phí dưới dạng *mã thông báo đầu ra*.
- Gemini API bao gồm số token trung gian trong phản hồi của API, nhờ đó bạn biết lý do nhận được token đầu vào bổ sung ngoài câu lệnh ban đầu.

## Các điểm hạn chế

- Mô hình này chỉ có thể tạo và thực thi mã. Phương thức này không thể trả về các cấu phần phần mềm khác như tệp nội dung nghe nhìn.
- Trong một số trường hợp, việc bật tính năng thực thi mã có thể dẫn đến sự hồi quy ở các khía cạnh khác của đầu ra của mô hình (ví dụ: viết một câu chuyện).
- Khả năng sử dụng thành công tính năng thực thi mã của các mô hình có sự khác biệt.

## Các cách kết hợp công cụ được hỗ trợ

Bạn có thể kết hợp công cụ thực thi mã với tính năng [Neo bám vào Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) để hỗ trợ các trường hợp sử dụng phức tạp hơn.

Các mô hình Gemini 3 hỗ trợ việc kết hợp các công cụ tích hợp (như Thực thi mã) với các công cụ tuỳ chỉnh (gọi hàm). Bạn phải truyền lại các trường `id` và `thought_signature` để tổ hợp công cụ hoạt động. Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Các thư viện được hỗ trợ

Môi trường thực thi mã bao gồm các thư viện sau:

- attrs
- cờ vua
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
- đóng gói ứng dụng
- gấu trúc
- cái gối
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
- sáu
- striprtf
- sympy
- lập bảng
- tensorflow
- toolz
- xlrd

Bạn không thể cài đặt thư viện của riêng mình.

## Bước tiếp theo

- Hãy thử [Colab thực thi mã](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=vi).
- Tìm hiểu về các công cụ khác của Gemini API:
  - [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
  - [Neo bám vào Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
