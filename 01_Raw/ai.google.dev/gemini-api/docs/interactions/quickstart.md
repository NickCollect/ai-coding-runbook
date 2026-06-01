---
source_url: https://ai.google.dev/gemini-api/docs/interactions/quickstart?hl=vi
fetched_at: 2026-06-01T05:57:28.564043+00:00
title: "B\u1eaft \u0111\u1ea7u nhanh API Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bắt đầu nhanh API Gemini

Hướng dẫn nhanh này sẽ hướng dẫn bạn cách cài đặt [các thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) của chúng tôi và đưa ra yêu cầu đầu tiên, hiện câu trả lời theo thời gian thực các phản hồi, xây dựng cuộc trò chuyện nhiều lượt và sử dụng các công cụ.

Bạn có thể dùng 2 cách để gửi yêu cầu đến Gemini API:

- ***(Nên dùng)*** [Interactions API](https://ai.google.dev/api/interactions-api?hl=vi) là một nguyên tắc cơ bản mới có hỗ trợ tích hợp cho việc sử dụng công cụ nhiều bước, điều phối và các luồng suy luận phức tạp thông qua các bước thực thi được nhập. Trong tương lai, các mô hình mới ngoài dòng chính cốt lõi, cùng với các khả năng của tác nhân AI và công cụ mới, sẽ chỉ ra mắt trên Interactions API.
- [`generateContent`](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi) cung cấp một cách để tạo phản hồi không trạng thái từ một mô hình. Mặc dù bạn nên sử dụng Interactions API, nhưng `generateContent` vẫn được hỗ trợ đầy đủ.

Phiên bản hướng dẫn nhanh này sử dụng Interactions API để gửi yêu cầu đến Gemini API.

## Trước khi bắt đầu

Để sử dụng Gemini API, bạn cần có khoá API để xác thực các yêu cầu, thực thi giới hạn bảo mật và theo dõi mức sử dụng cho tài khoản của bạn.

Hãy tạo một dự án trên AI Studio miễn phí để bắt đầu:

[Tạo khoá Gemini API](https://aistudio.google.com/app/apikey?hl=vi)

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

Sử dụng phương thức `interactions.create` để [tạo câu trả lời bằng văn bản](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in a few words",
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Hiện câu trả lời theo thời gian thực

Theo mặc định, mô hình chỉ trả về câu trả lời sau khi toàn bộ quy trình tạo hoàn tất. Để có trải nghiệm nhanh hơn và mang tính tương tác hơn, bạn có thể [truyền trực tuyến các phần phản hồi](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=vi) khi chúng được tạo.

### Python

```
stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in detail",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
```

### JavaScript

```
async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works in detail",
    stream: true,
  });

  for await (const event of stream) {
    if (event.event_type === "step.delta") {
      if (event.delta.type === "text") {
        process.stdout.write(event.delta.text);
      }
    }
  }
}

main();
```

### REST

```
# Use alt=sse for streaming
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works in detail",
    "stream": true
  }'
```

## Cuộc trò chuyện nhiều lượt

Gemini API có tính năng hỗ trợ tích hợp để tạo [cuộc trò chuyện nhiều lượt](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi#multi-turn-conversations).
Bạn chỉ cần truyền `id` được trả về từ lượt tương tác trước đó làm tham số `previous_interaction_id` và máy chủ sẽ tự động quản lý nhật ký cuộc trò chuyện.

### Python

```
interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house."
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id
)
print("Response 2:", interaction2.output_text)
```

### JavaScript

```
async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

main();
```

### REST

```
# Turn 1: Start the conversation
RESPONSE1=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "I have 2 dogs in my house."
  }')

# Extract the interaction ID
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

# Turn 2: Continue the conversation
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3-flash-preview\",
    \"input\": \"How many paws are in my house?\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
  }"
```

## Sử dụng công cụ

Mở rộng các chức năng của mô hình bằng cách [đưa ra câu trả lời dựa trên Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=vi) để truy cập vào nội dung trên web theo thời gian thực. Mô hình này tự động quyết định thời điểm tìm kiếm, thực hiện các truy vấn và tổng hợp câu trả lời kèm theo trích dẫn.

Ví dụ sau đây minh hoạ cách bật Google Tìm kiếm:

### Python

```
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Who won the euro 2024?",
    tools=[{"type": "google_search"}]
)

print(interaction.output_text)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text" and content_block.annotations:
                print("\nCitations:")
                for annotation in content_block.annotations:
                    if annotation.type == "url_citation":
                        print(f"  - [{annotation.title}]({annotation.url})")
```

### JavaScript

```
async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Who won the euro 2024?",
    tools: [{ type: "google_search" }]
  });

  console.log(interaction.output_text);

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text' && contentBlock.annotations) {
          console.log("\nCitations:");
          for (const annotation of contentBlock.annotations) {
            if (annotation.type === 'url_citation') {
              console.log(`  - [${annotation.title}](${annotation.url})`);
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "Who won the euro 2024?",
    "tools": [{"type": "google_search"}]
  }'
```

Gemini API cũng hỗ trợ các công cụ tích hợp khác:

- **[Thực thi mã](https://ai.google.dev/gemini-api/docs/interactions/code-execution?hl=vi)**: Cho phép mô hình viết và chạy mã Python để giải các bài toán phức tạp về toán học.
- **[Bối cảnh URL](https://ai.google.dev/gemini-api/docs/interactions/url-context?hl=vi)**: Cho phép bạn đưa ra câu trả lời dựa trên các URL cụ thể của trang web mà bạn cung cấp.
- **[Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/interactions/file-search?hl=vi)**: Cho phép bạn tải tệp lên và đưa ra câu trả lời dựa trên nội dung của tệp bằng tính năng tìm kiếm ngữ nghĩa.
- **[Google Maps](https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=vi)**: Cho phép bạn đưa ra câu trả lời dựa trên dữ liệu vị trí và tìm kiếm địa điểm, chỉ đường và bản đồ.
- **[Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/interactions/computer-use?hl=vi)**: Cho phép mô hình tương tác với màn hình, bàn phím và chuột ảo của máy tính để thực hiện các tác vụ.

## Gọi hàm tuỳ chỉnh

Sử dụng **[chức năng gọi](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi)** để kết nối các mô hình với các công cụ và API tuỳ chỉnh của bạn. Mô hình xác định thời điểm gọi hàm của bạn và trả về một bước `function_call` cùng với các đối số để ứng dụng của bạn thực thi.

Ví dụ này khai báo một hàm nhiệt độ mô phỏng và kiểm tra xem mô hình có muốn gọi hàm đó hay không.

### Python

```
import json

weather_function = {
    "type": "function",
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

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What's the temperature in London?",
    tools=[weather_function],
)

fc_step = None
for step in interaction.steps:
    if step.type == "function_call":
        fc_step = step
        break

if fc_step:
    print(f"Model requested function: {fc_step.name} with args {fc_step.arguments}")

    mock_result = {"temperature": "15C", "condition": "Cloudy"}

    final_interaction = client.interactions.create(
        model="gemini-3-flash-preview",
        input=[
            {
                "type": "function_result",
                "name": fc_step.name,
                "call_id": fc_step.id,
                "result": [{"type": "text", "text": json.dumps(mock_result)}],
            }
        ],
        tools=[weather_function],
        previous_interaction_id=interaction.id,
    )
    print("Final Response:", final_interaction.output_text)
```

### JavaScript

```
async function main() {
  const weatherFunction = {
    type: 'function',
    name: 'get_current_temperature',
    description: 'Gets the current temperature for a given location.',
    parameters: {
      type: 'object',
      properties: {
        location: {
          type: 'string',
          description: 'The city name, e.g. San Francisco',
        },
      },
      required: ['location'],
    },
  };

  const interaction = await ai.interactions.create({
    model: 'gemini-3-flash-preview',
    input: "What's the temperature in London?",
    tools: [weatherFunction],
  });

  const fcStep = interaction.steps.find(s => s.type === 'function_call');
  if (fcStep) {
    console.log(`Model requested function: ${fcStep.name}`);

    const mockResult = { temperature: "15C", condition: "Cloudy" };

    const finalInteraction = await ai.interactions.create({
      model: 'gemini-3-flash-preview',
      input: [{
        type: 'function_result',
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: 'text', text: JSON.stringify(mockResult) }]
      }],
      tools: [weatherFunction],
      previous_interaction_id: interaction.id,
    });

    console.log("Final Response:", finalInteraction.output_text);
  }
}

main();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Api-Revision: 2026-05-20" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-flash-preview",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

## Bước tiếp theo

Giờ đây, bạn đã bắt đầu sử dụng Gemini API, hãy khám phá các hướng dẫn sau để tạo các ứng dụng nâng cao hơn:

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/interactions/text-generation?hl=vi)
- [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/interactions/image-generation?hl=vi)
- [Hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=vi)
- [Tư duy](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=vi)
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/interactions/function-calling?hl=vi)
- [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/interactions/google-search?hl=vi)
- [Ngữ cảnh dài](https://ai.google.dev/gemini-api/docs/long-context?hl=vi)
- [Vectơ nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-28 UTC."],[],[]]
