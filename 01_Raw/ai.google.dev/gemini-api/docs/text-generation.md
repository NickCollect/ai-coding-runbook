---
source_url: https://ai.google.dev/gemini-api/docs/text-generation?hl=vi
fetched_at: 2026-06-29T05:29:37.329825+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo văn bản

Gemini API có thể tạo đầu ra là văn bản từ dữ liệu đầu vào là văn bản, hình ảnh, video và âm thanh.

Sau đây là một ví dụ cơ bản:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?"
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
    input: "How does AI work?",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?"
  }'
```

Các SDK AI tạo sinh của Google cung cấp các thuộc tính tiện lợi ngay trên đối tượng `Interaction` được trả về để truy cập vào phản hồi của mô hình.

Trợ giúp phổ biến nhất là **`interaction.output_text`** (String), trả về các khối văn bản cuối cùng trong câu trả lời của mô hình. Nếu câu trả lời được chia thành nhiều khối `TextContent` liên tiếp, thì câu trả lời đó sẽ tự động kết hợp các khối này.
Xin lưu ý rằng `.output_text` không bao gồm các khối văn bản trước đó được phân tách bằng nội dung không phải văn bản (chẳng hạn như suy nghĩ, hình ảnh, âm thanh hoặc lệnh gọi công cụ). Đối với các câu trả lời phức tạp hoặc xen kẽ nhiều phương thức, bạn phải lặp lại `steps` theo cách thủ công. Để tìm hiểu thêm về các thuộc tính khác liên quan đến sự thuận tiện của nội dung nghe nhìn, hãy xem phần [Tổng quan về lượt tương tác](https://ai.google.dev/gemini-api/docs/interactions?hl=vi#convenience-properties).

## Suy nghĩ cùng Gemini

Các mô hình Gemini thường được bật tính năng ["tư duy"](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=vi) theo mặc định. Tính năng này cho phép mô hình suy luận trước khi trả lời một yêu cầu.

Mỗi mô hình hỗ trợ các cấu hình tư duy khác nhau, giúp bạn kiểm soát chi phí, độ trễ và mức độ thông minh. Để biết thêm thông tin, hãy xem [hướng dẫn tư duy](https://ai.google.dev/gemini-api/docs/interactions/thinking?hl=vi#set-budget).

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="How does AI work?",
    generation_config={
        "thinking_level": "low"
    }
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
    input: "How does AI work?",
    generation_config: {
      thinking_level: "low",
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How does AI work?",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Hướng dẫn hệ thống và các cấu hình khác

Bạn có thể hướng dẫn hành vi của các mô hình Gemini bằng chỉ dẫn hệ thống. Truyền tham số `system_instruction` để định cấu hình hành vi của mô hình.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    system_instruction="You are a cat. Your name is Neko.",
    input="Hello there"
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
    input: "Hello there",
    system_instruction: "You are a cat. Your name is Neko.",
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "system_instruction": "You are a cat. Your name is Neko.",
    "input": "Hello there"
  }'
```

Bạn cũng có thể ghi đè các tham số tạo mặc định, chẳng hạn như nhiệt độ, bằng cách sử dụng tham số `generation_config`.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    generation_config={
        "temperature": 1.0
    }
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
    input: "Explain how AI works",
    generation_config: {
      temperature: 1.0,
    },
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "generation_config": {
      "temperature": 1.0
    }
  }'
```

Hãy tham khảo [Tài liệu tham khảo về Interactions API](https://ai.google.dev/api/interactions-api?hl=vi) để xem danh sách đầy đủ các tham số có thể định cấu hình và nội dung mô tả của các tham số đó.

## Thông tin đầu vào đa phương thức

Gemini API hỗ trợ dữ liệu đầu vào đa phương thức, cho phép bạn kết hợp văn bản với các tệp nội dung nghe nhìn. Ví dụ sau đây minh hoạ cách cung cấp hình ảnh:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="path/to/organ.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Tell me about this instrument"},
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const uploadedFile = await ai.files.upload({
    file: "path/to/organ.jpg",
    config: { mimeType: "image/jpeg" }
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      {type: "text", text: "Tell me about this instrument"},
      {
        type: "image",
        uri: uploadedFile.uri,
        mime_type: uploadedFile.mimeType
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### REST

```
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": [
      {"type": "text", "text": "Tell me about this instrument"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg"
      }
    ]
  }'
```

Để biết các phương thức thay thế để cung cấp hình ảnh và quy trình xử lý hình ảnh nâng cao hơn, hãy xem [hướng dẫn về việc hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=vi).
API này cũng hỗ trợ các dữ liệu đầu vào và thông tin [về tài liệu](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=vi), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=vi) và [âm thanh](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=vi).

## Hiện câu trả lời theo thời gian thực

Theo mặc định, mô hình chỉ trả về phản hồi sau khi toàn bộ quá trình tạo hoàn tất.

Để có các hoạt động tương tác mượt mà hơn, hãy sử dụng tính năng truyền trực tuyến để xử lý các đoạn phản hồi khi chúng được tạo. Để xem hướng dẫn toàn diện về các loại sự kiện, tính năng phát trực tuyến bằng công cụ, tư duy, tác nhân và tạo hình ảnh, hãy xem hướng dẫn chuyên biệt về [Tương tác phát trực tuyến](https://ai.google.dev/gemini-api/docs/interactions/streaming?hl=vi).

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain how AI works",
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

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain how AI works",
    "stream": true
  }'
```

## Cuộc trò chuyện nhiều lượt

Interactions API hỗ trợ các cuộc trò chuyện nhiều lượt bằng cách liên kết các lượt tương tác với nhau bằng cách sử dụng `previous_interaction_id`. Mỗi lượt là một lượt tương tác riêng biệt và API sẽ tự động quản lý nhật ký trò chuyện.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print(interaction2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
  });
  console.log("Response 2:", interaction2.output_text);
}

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')

INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have two dogs in my house. How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'"
  }'
```

Bạn cũng có thể dùng tính năng truyền trực tuyến cho các cuộc trò chuyện nhiều lượt bằng cách kết hợp `previous_interaction_id` với các phương thức truyền trực tuyến.

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    input="I have 2 dogs in my house.",
)
print(interaction1.output_text)

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
    stream=True
)
for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "I have 2 dogs in my house.",
  });
  console.log("Response 1:", interaction1.output_text);

  const stream = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "How many paws are in my house?",
    previous_interaction_id: interaction1.id,
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

await main();
```

### REST

```
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "I have 2 dogs in my house."
  }')
INTERACTION_ID=$(echo "$RESPONSE1" | jq -r '.id')

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "How many paws are in my house?",
    "previous_interaction_id": "'$INTERACTION_ID'",
    "stream": true
  }'
```

## Cuộc trò chuyện không trạng thái

Theo mặc định, Interactions API quản lý trạng thái cuộc trò chuyện phía máy chủ khi bạn sử dụng `previous_interaction_id`. Tuy nhiên, bạn cũng có thể hoạt động ở chế độ không trạng thái bằng cách tự quản lý nhật ký cuộc trò chuyện ở phía máy khách.

Cách sử dụng chế độ không trạng thái:
1. Đặt `store=false` trong yêu cầu của bạn để chọn không sử dụng bộ nhớ phía máy chủ.
2. Duy trì nhật ký trò chuyện dưới dạng một mảng **các bước** ở phía máy khách.
3. Trong các yêu cầu tiếp theo, hãy truyền các bước đã tích luỹ trong trường `input` và thêm lượt mới của bạn dưới dạng một bước `user_input`.

### Python

```
from google import genai

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "I have 2 dogs in my house."}]
    }
]

interaction1 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 1:", interaction1.steps[-1].content[0].text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({
    "type": "user_input",
    "content": [{"type": "text", "text": "How many paws are in my house?"}]
})

interaction2 = client.interactions.create(
    model="gemini-3.5-flash",
    store=False,
    input=history
)
print("Response 2:", interaction2.steps[-1].content[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "I have 2 dogs in my house." }]
    }
  ];

  const interaction1 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 1:", interaction1.steps.at(-1).content[0].text);

  history.push(...interaction1.steps);

  history.push({
    type: "user_input",
    content: [{ type: "text", text: "How many paws are in my house?" }]
  });

  const interaction2 = await ai.interactions.create({
    model: "gemini-3.5-flash",
    store: false,
    input: history
  });
  console.log("Response 2:", interaction2.steps.at(-1).content[0].text);
}

await main();
```

### REST

```
# Turn 1: Send request with store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "I have 2 dogs in my house."
      }
    ]
  }')

# Extract the steps from response
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Reconstruct the full history for Turn 2 by combining:
# 1. First user input
# 2. Model response steps
# 3. Second user input
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "I have 2 dogs in my house."}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --argjson second_input '[{"type": "user_input", "content": "How many paws are in my house?"}]' \
  "'"'"'$first_input + $model_steps + $second_input'"'"'")

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.5-flash\",
    \"store\": false,
    \"input\": $HISTORY
  }"
```

## Mẹo tạo câu lệnh

Hãy tham khảo [hướng dẫn về thiết kế câu lệnh](https://ai.google.dev/gemini/docs/prompting-strategies?hl=vi) của chúng tôi để biết các đề xuất về cách khai thác tối đa Gemini.

## Bước tiếp theo

- Dùng thử [Gemini trong Google AI Studio](https://aistudio.google.com?hl=vi).
- Thử nghiệm với [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/interactions/structured-output?hl=vi) cho các phản hồi tương tự như JSON.
- Khám phá các khả năng hiểu [hình ảnh](https://ai.google.dev/gemini-api/docs/interactions/image-understanding?hl=vi), [video](https://ai.google.dev/gemini-api/docs/interactions/video-understanding?hl=vi), [âm thanh](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=vi) và [tài liệu](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=vi) của Gemini.
- Tìm hiểu về [các chiến lược đưa ra câu lệnh bằng tệp đa phương thức](https://ai.google.dev/gemini-api/docs/interactions/files?hl=vi#prompt-guide).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
