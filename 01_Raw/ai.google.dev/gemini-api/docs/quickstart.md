---
source_url: https://ai.google.dev/gemini-api/docs/quickstart?hl=vi
fetched_at: 2026-06-22T06:26:20.100141+00:00
title: "B\u1eaft \u0111\u1ea7u nhanh API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bắt đầu nhanh API Gemini

Hướng dẫn khởi động nhanh này sẽ hướng dẫn bạn cách cài đặt [các thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) của chúng tôi và đưa ra yêu cầu đầu tiên, truyền trực tuyến các phản hồi, xây dựng cuộc trò chuyện nhiều lượt và sử dụng các công cụ bằng phương thức `generateContent` tiêu chuẩn.

## Trước khi bắt đầu

Để sử dụng Gemini API, bạn cần có khoá API để xác thực các yêu cầu, thực thi giới hạn bảo mật và theo dõi mức sử dụng cho tài khoản của bạn.

Hãy tạo một dự án trên AI Studio miễn phí để bắt đầu:

[Tạo khoá Gemini API](https://aistudio.google.com/apikey?hl=vi)

## Cài đặt Google GenAI SDK

### Python

Khi dùng [Python 3.9 trở lên](https://www.python.org/downloads/), hãy cài đặt gói [`google-genai`](https://pypi.org/project/google-genai/) bằng [lệnh pip](https://packaging.python.org/en/latest/tutorials/installing-packages/) sau:

```
pip install -q -U google-genai
```

### JavaScript

Sử dụng [Node.js phiên bản 18 trở lên](https://nodejs.org/en/download/package-manager), hãy cài đặt [Google Gen AI SDK cho TypeScript và JavaScript](https://www.npmjs.com/package/@google/genai) bằng [lệnh npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) sau:

```
npm install @google/genai
```

## Tạo văn bản

Sử dụng phương thức `models.generate_content` để [tạo câu trả lời bằng văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi).

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in a few words",
  });

  console.log(response.text);
}

main();
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
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## Hiện câu trả lời theo thời gian thực

Theo mặc định, mô hình chỉ trả về câu trả lời sau khi toàn bộ quy trình tạo hoàn tất. Để có trải nghiệm nhanh hơn và mang tính tương tác hơn, bạn có thể [truyền trực tuyến các phần phản hồi](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#stream) khi chúng được tạo.

### Python

```
response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents="Explain how AI works in detail"
)

for chunk in response:
    print(chunk.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const responseStream = await ai.models.generateContentStream({
    model: "gemini-3.5-flash",
    contents: "Explain how AI works in detail",
  });

  for await (const chunk of responseStream) {
    process.stdout.write(chunk.text);
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in detail"
          }
        ]
      }
    ]
  }'
```

## Cuộc trò chuyện nhiều lượt

Đối với các cuộc trò chuyện nhiều lượt, các SDK cung cấp một trình trợ giúp có trạng thái `chats` để tạo [trải nghiệm trò chuyện nhiều lượt](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#chat) tự động quản lý nhật ký trò chuyện.

### Python

```
chat = client.chats.create(model="gemini-3.5-flash")

response1 = chat.send_message("I have 2 dogs in my house.")
print("Response 1:", response1.text)

response2 = chat.send_message("How many paws are in my house?")
print("Response 2:", response2.text)
```

### JavaScript

```
async function main() {
  const chat = ai.chats.create({ model: "gemini-3.5-flash" });

  let response = await chat.sendMessage({ message: "I have 2 dogs in my house." });
  console.log("Response 1:", response.text);

  response = await chat.sendMessage({ message: "How many paws are in my house?" });
  console.log("Response 2:", response.text);
}

main();
```

### REST

```
# REST is stateless. You must pass the full conversation history in the request.
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [{"text": "I have 2 dogs in my house."}]
      },
      {
        "role": "model",
        "parts": [{"text": "That is nice! Two dogs mean you have plenty of company."}]
      },
      {
        "role": "user",
        "parts": [{"text": "How many paws are in my house?"}]
      }
    ]
  }'
```

## Sử dụng công cụ

Mở rộng các chức năng của mô hình bằng cách [đưa ra câu trả lời dựa trên Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) để truy cập vào nội dung trên web theo thời gian thực. Mô hình này tự động quyết định thời điểm tìm kiếm, thực hiện các truy vấn và tổng hợp câu trả lời.

### Python

```
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config
)

print(response.text)

metadata = response.candidates[0].grounding_metadata
if metadata.web_search_queries:
    print("\nSearch queries executed:")
    for query in metadata.web_search_queries:
        print(f" - {query}")

if metadata.grounding_chunks:
    print("\nSources:")
    for chunk in metadata.grounding_chunks:
        print(f" - [{chunk.web.title}]({chunk.web.uri})")
```

### JavaScript

```
async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "Who won the euro 2024?",
    config: {
      tools: [{ googleSearch: {} }]
    }
  });

  console.log(response.text);

  const metadata = response.candidates[0]?.groundingMetadata;
  if (metadata?.webSearchQueries) {
    console.log("\nSearch queries executed:");
    for (const query of metadata.webSearchQueries) {
      console.log(` - ${query}`);
    }
  }
  if (metadata?.groundingChunks) {
    console.log("\nSources:");
    for (const chunk of metadata.groundingChunks) {
      console.log(` - [${chunk.web.title}](${chunk.web.uri})`);
    }
  }
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Gemini API cũng hỗ trợ các công cụ tích hợp khác:

- **[Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)**: Cho phép mô hình viết và chạy mã Python để giải các bài toán phức tạp về toán học.
- **[Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)**: Cho phép bạn đưa ra câu trả lời dựa trên các URL cụ thể của trang web mà bạn cung cấp.
- **[Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)**: Cho phép bạn tải tệp lên và đưa ra câu trả lời dựa trên nội dung của tệp bằng tính năng tìm kiếm ngữ nghĩa.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)**: Cho phép bạn đưa ra câu trả lời dựa trên dữ liệu vị trí và tìm kiếm địa điểm, chỉ đường và bản đồ.
- **[Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)**: Cho phép mô hình tương tác với màn hình, bàn phím và chuột ảo của máy tính để thực hiện các tác vụ.

## Gọi hàm tuỳ chỉnh

Sử dụng tính năng **[gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)** để kết nối các mô hình với các công cụ và API tuỳ chỉnh của bạn. Mô hình sẽ xác định thời điểm gọi hàm của bạn và trả về một `functionCall` trong phản hồi để ứng dụng của bạn thực thi.

Ví dụ này khai báo một hàm nhiệt độ mô phỏng và kiểm tra xem mô hình có muốn gọi hàm đó hay không.

### Python

```
from google import genai
from google.genai import types

weather_function = {
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

tools = types.Tool(function_declarations=[weather_function])
config = types.GenerateContentConfig(tools=[tools])

contents = ["What's the temperature in London?"]

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=contents,
    config=config,
)

part = response.candidates[0].content.parts[0]
if part.function_call:
    fc = part.function_call
    print(f"Model requested function: {fc.name} with args {fc.args}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    contents.append(response.candidates[0].content)

    fn_response_part = types.Part.from_function_response(
        name=fc.name,
        response=mock_result,
        id=fc.id
    )
    contents.append(types.Content(role="user", parts=[fn_response_part]))

    final_response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config,
    )
    print("Final Response:", final_response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

async function main() {
  const weatherFunction = {
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: Type.OBJECT,
      properties: {
        location: {
          type: Type.STRING,
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const contents = [{
    role: 'user',
    parts: [{ text: "What's the temperature in London?" }]
  }];

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: contents,
    config: {
      tools: [{ functionDeclarations: [weatherFunction] }],
    },
  });

  if (response.functionCalls && response.functionCalls.length > 0) {
    const fc = response.functionCalls[0];
    console.log(`Model requested function: ${fc.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    contents.push(response.candidates[0].content);

    contents.push({
      role: 'user',
      parts: [{
        functionResponse: {
          name: fc.name,
          response: mockResult,
          id: fc.id
        }
      }]
    });

    const finalResponse = await ai.models.generateContent({
      model: 'gemini-3.5-flash',
      contents: contents,
      config: {
        tools: [{ functionDeclarations: [weatherFunction] }],
      },
    });
    console.log("Final Response:", finalResponse.text);
  }
}

main();
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
        "role": "user",
        "parts": [{"text": "What'\''s the temperature in London?"}]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "get_current_temperature",
            "description": "Gets the current temperature for a given location.",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city name, e.g. San Francisco"
                }
              },
              "required": ["location"]
            }
          }
        ]
      }
    ]
  }'
```

## Bước tiếp theo

Giờ đây, bạn đã bắt đầu sử dụng Gemini API, hãy khám phá các hướng dẫn sau để tạo các ứng dụng nâng cao hơn:

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi)
- [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)
- [Hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi)
- [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
- [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)
- [Ngữ cảnh dài](https://ai.google.dev/gemini-api/docs/long-context?hl=vi)
- [Vectơ nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-19 UTC."],[],[]]
