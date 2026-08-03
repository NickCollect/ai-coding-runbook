---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=vi
fetched_at: 2026-08-03T04:33:27.477625+00:00
title: "T\u01b0 duy c\u1ee7a Gemini \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tư duy của Gemini

[Các mô hình thuộc dòng Gemini 3 và 2.5](https://ai.google.dev/gemini-api/docs/models?hl=vi) sử dụng "quy trình tư duy" giúp cải thiện đáng kể khả năng suy luận và lập kế hoạch nhiều bước, nhờ đó, các mô hình này có hiệu quả cao đối với các tác vụ phức tạp như lập trình, toán học nâng cao và phân tích dữ liệu.

Khi bạn sử dụng mô hình tư duy, Gemini sẽ suy luận nội bộ trước khi trả lời. Interactions API cho thấy lý do này thông qua các bước `thought`, là các bước chuyên dụng xuất hiện theo trình tự thời gian cùng với các lệnh gọi hàm, dữ liệu đầu vào của người dùng hoặc dữ liệu đầu ra của mô hình trong mảng `steps`.

Mỗi bước suy nghĩ chứa 2 trường:

| Trường | Bắt buộc | Mô tả |
| --- | --- | --- |
| `signature` | ✅ Có | Một bản mã hoá biểu thị trạng thái suy luận nội bộ của mô hình. Luôn xuất hiện, ngay cả khi mô hình thực hiện suy luận tối thiểu. |
| `summary` | ❌ Không | Một mảng nội dung (văn bản và/hoặc hình ảnh) tóm tắt lý do. Có thể trống tuỳ thuộc vào cấu hình [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=vi), liệu mô hình có thực hiện đủ quy trình suy luận hay không hoặc loại nội dung (ví dụ: các thành phần tiềm ẩn của hình ảnh có thể không có bản tóm tắt bằng văn bản). |

## Tương tác với suy nghĩ

Việc bắt đầu tương tác với một mô hình tư duy cũng tương tự như mọi yêu cầu tương tác khác. Chỉ định một trong các [mô hình có hỗ trợ tư duy](#thinking-levels) trong trường `model`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Tóm tắt suy nghĩ

Bản tóm tắt suy nghĩ cung cấp thông tin chi tiết về quy trình suy luận nội bộ của mô hình.
Theo mặc định, chỉ kết quả đầu ra cuối cùng được trả về. Bạn có thể bật tính năng tóm tắt suy nghĩ bằng `thinking_summaries`:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Khối suy nghĩ có thể **chỉ chứa chữ ký mà không có nội dung tóm tắt** trong những trường hợp sau:

- Các yêu cầu đơn giản, trong đó mô hình không suy luận đủ để tạo bản tóm tắt
- `thinking_summaries: "none"`, trong đó tính năng tóm tắt bị tắt một cách rõ ràng
- Một số loại nội dung trong suy nghĩ, chẳng hạn như hình ảnh, có thể không có bản tóm tắt bằng văn bản

Mã của bạn phải luôn xử lý các khối suy nghĩ khi `summary` trống hoặc không có.

## Truyền phát trực tiếp có tư duy

Sử dụng tính năng truyền trực tuyến để nhận bản tóm tắt gia tăng về ý tưởng trong quá trình tạo.
Các khối suy nghĩ được phân phối bằng Sự kiện được gửi bởi máy chủ (SSE) với 2 loại delta riêng biệt:

| Loại Delta | Chứa | Thời điểm gửi |
| --- | --- | --- |
| `thought_summary` | Nội dung tóm tắt bằng văn bản hoặc hình ảnh | Một hoặc nhiều delta có bản tóm tắt gia tăng |
| `thought_signature` | Chữ ký mật mã | delta cuối cùng trước `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Phản hồi truyền trực tuyến sử dụng Sự kiện được gửi bởi máy chủ (SSE) và bao gồm các bước và sự kiện, ví dụ:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.6-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Tư duy kiểm soát

Theo mặc định, các mô hình Gemini tham gia vào quá trình tư duy linh hoạt bằng cách tự động điều chỉnh mức độ nỗ lực suy luận dựa trên độ phức tạp của yêu cầu. Bạn có thể kiểm soát hành vi này bằng cách sử dụng tham số `thinking_level`.

| Mô hình | Tư duy mặc định | Các cấp độ được hỗ trợ |
| --- | --- | --- |
| gemini-3.6-flash | Bật (trung bình) | tối thiểu, thấp, trung bình, cao |
| gemini-3.5-flash-lite | Bật (tối thiểu) | tối thiểu, thấp, trung bình, cao |
| gemini-3.1-pro-preview | Bật (cao) | thấp, trung bình, cao |
| gemini-3.1-flash-lite-image | Bật (tối thiểu) | tối thiểu, cao |
| gemini-3-flash-preview | Bật (cao) | tối thiểu, thấp, trung bình, cao |
| gemini-3-pro-preview | Bật (cao) | thấp, cao |
| gemini-3.5-flash | Bật (trung bình) | tối thiểu, thấp, trung bình, cao |
| gemini-2.5-pro | Bật | thấp, trung bình, cao |
| gemini-2.5-flash | Bật | thấp, trung bình, cao |
| gemini-2.5-flash-lite | Tắt | thấp, trung bình, cao |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Chữ ký của suy nghĩ

Chữ ký suy nghĩ là biểu thị được mã hoá về quá trình suy luận nội bộ của mô hình. Chúng phải duy trì tính liên tục của suy luận trong các lượt tương tác nhiều lượt.

Interactions API giúp việc xử lý chữ ký tư duy trở nên đơn giản hơn nhiều so với `generateContent` API.

### Chế độ có trạng thái (Nên dùng)

Theo mặc định, khi bạn sử dụng Interactions API ở chế độ có trạng thái (bằng cách đặt `store: true` và truyền `previous_interaction_id` trong các lượt tiếp theo), máy chủ sẽ tự động quản lý trạng thái cuộc trò chuyện, bao gồm tất cả các khối suy nghĩ và chữ ký. Ở chế độ này, bạn không cần làm gì liên quan đến chữ ký. Các yêu cầu này được xử lý hoàn toàn ở phía máy chủ.

### Chế độ không trạng thái

Nếu bạn tự quản lý trạng thái cuộc trò chuyện (chế độ không trạng thái) và truyền toàn bộ nhật ký đầu vào và đầu ra trong mỗi yêu cầu:

- Bạn **PHẢI** luôn gửi lại tất cả các khối `thought` giống hệt như khi nhận được từ mô hình.
- Bạn **KHÔNG** nên xoá hoặc sửa đổi các khối suy nghĩ trong nhật ký, vì chúng chứa chữ ký cần thiết để mô hình tiếp tục suy luận.
- Khi chuyển đổi mô hình trong một phiên, bạn vẫn nên gửi lại các khối suy nghĩ của mô hình trước đó. Phần phụ trợ quản lý khả năng tương thích.

## Giá

Khi tính năng suy nghĩ được bật, giá của câu trả lời là tổng số mã thông báo đầu ra và mã thông báo suy nghĩ. Bạn có thể lấy tổng số mã thông báo tư duy đã tạo từ trường `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Các mô hình tư duy tạo ra những suy nghĩ hoàn chỉnh để cải thiện chất lượng của câu trả lời cuối cùng, sau đó đưa ra [bản tóm tắt](#summaries) để cung cấp thông tin chi tiết về quy trình tư duy. Giá được tính dựa trên số lượng mã thông báo đầy đủ mà mô hình cần tạo, mặc dù API chỉ xuất ra bản tóm tắt.

Bạn có thể tìm hiểu thêm về mã thông báo trong hướng dẫn [Đếm mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi).

## Các phương pháp hay nhất

Sử dụng các mô hình tư duy một cách hiệu quả bằng cách làm theo các nguyên tắc sau.

- **Xem xét suy luận**: Phân tích bản tóm tắt suy nghĩ để hiểu rõ những điểm thất bại và cải thiện câu lệnh.
- **Kiểm soát ngân sách suy nghĩ**: Yêu cầu mô hình suy nghĩ ít hơn đối với các đầu ra dài để tiết kiệm mã thông báo.
- **Tác vụ đơn giản**: Sử dụng mức độ tư duy tối thiểu hoặc thấp để truy xuất hoặc phân loại thông tin (ví dụ: "DeepMind được thành lập ở đâu?").
- **Nhiệm vụ vừa phải**: Sử dụng tư duy mặc định để so sánh các khái niệm hoặc suy luận sáng tạo (ví dụ: So sánh xe điện và xe hybrid).
- **Nhiệm vụ phức tạp**: Sử dụng tối đa khả năng tư duy để lập trình nâng cao, giải toán hoặc lập kế hoạch nhiều bước (ví dụ: Giải các bài toán trong kỳ thi AIME).

## Bước tiếp theo

- [Tạo văn bản](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi): Câu trả lời cơ bản bằng văn bản
- [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi): Kết nối với các công cụ
- [Hướng dẫn về Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=vi): Các tính năng dành riêng cho mô hình

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
