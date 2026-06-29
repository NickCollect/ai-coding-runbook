---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi
fetched_at: 2026-06-29T05:28:24.138793+00:00
title: "K\u1ebft h\u1ee3p c\u00e1c c\u00f4ng c\u1ee5 t\u00edch h\u1ee3p v\u00e0 t\u00ednh n\u0103ng g\u1ecdi h\u00e0m \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Kết hợp các công cụ tích hợp và tính năng gọi hàm

Gemini cho phép kết hợp [các công cụ tích hợp](https://ai.google.dev/gemini-api/docs/tools?hl=vi), chẳng hạn như `google_search` và [lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) (còn gọi là *công cụ tuỳ chỉnh*) trong một lượt tương tác bằng cách duy trì và hiển thị nhật ký ngữ cảnh của các lệnh gọi công cụ. Các tổ hợp công cụ tích hợp và tuỳ chỉnh cho phép các quy trình làm việc phức tạp, dựa trên tác nhân, trong đó chẳng hạn như mô hình có thể tự căn cứ vào dữ liệu web theo thời gian thực trước khi gọi logic kinh doanh cụ thể của bạn.

Dưới đây là ví dụ cho phép kết hợp các công cụ tích hợp và tuỳ chỉnh bằng `google_search` và hàm tuỳ chỉnh `getWeather`:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.5-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## Cách hoạt động

Các mô hình Gemini 3 sử dụng *vòng tuần hoàn ngữ cảnh công cụ* để cho phép kết hợp các công cụ tuỳ chỉnh và công cụ tích hợp. Tính năng lưu thông ngữ cảnh công cụ giúp duy trì và hiển thị ngữ cảnh của các công cụ tích hợp, đồng thời chia sẻ ngữ cảnh đó với các công cụ tuỳ chỉnh trong cùng một hoạt động tương tác.

### Bật tính năng kết hợp công cụ

- Thêm [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#function-declarations), cùng với các công cụ tích hợp mà bạn muốn sử dụng, để kích hoạt hành vi kết hợp.

### API trả về các bước

Trong một phản hồi tương tác, API sẽ trả về các bước riêng biệt cho lệnh gọi công cụ tích hợp và lệnh gọi hàm (công cụ tuỳ chỉnh):

- **Các bước của công cụ tích hợp sẵn**: API tự động quản lý các bước này, duy trì ngữ cảnh trong các lượt tương tác.
- **Các bước gọi hàm**: API này trả về `function_call` bước cho các hàm tuỳ chỉnh của bạn. Bạn thực thi hàm và cung cấp kết quả.

### Các trường quan trọng trong các bước được trả về

Một số trường trong các bước được trả về là rất quan trọng để duy trì ngữ cảnh của công cụ và cho phép kết hợp các công cụ:

- **`id`**: Xuất hiện ở các bước `function_call` và `function_response`. Giá trị nhận dạng duy nhất liên kết một lệnh gọi với phản hồi của lệnh gọi đó.
- **`signature`**: Xuất hiện ở các bước `thought`, cũng như tất cả các bước gọi công cụ (ví dụ: `function_call`) và kết quả (ví dụ: `function_response`) cho các mô hình Gemini 3 trở lên. Bối cảnh được mã hoá này cho phép **lưu thông bối cảnh công cụ** trong các lượt tương tác.

**Quản lý các trường này:**

- **Chế độ có trạng thái (Nên dùng)**: Khi bạn sử dụng `previous_interaction_id`, máy chủ sẽ tự động xử lý cả hai trường `id` và `signature`.
- **Chế độ không trạng thái**: Khi quản lý nhật ký cuộc trò chuyện theo cách thủ công, bạn phải đảm bảo rằng bạn truyền cả trường `id` và `signature` trở lại mô hình trong các yêu cầu tiếp theo để xác thực tính xác thực và duy trì ngữ cảnh. Các SDK chính thức sẽ tự động xử lý việc này nếu bạn truyền toàn bộ đối tượng phản hồi trở lại nhật ký.

### Dữ liệu dành riêng cho công cụ

Một số công cụ tích hợp trả về các đối số dữ liệu mà người dùng có thể thấy, dành riêng cho loại công cụ.

| Công cụ | Đối số gọi công cụ mà người dùng nhìn thấy (nếu có) | Phản hồi của công cụ mà người dùng nhìn thấy (nếu có) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` URL cần duyệt xem | `status`: Trạng thái duyệt qua `retrieved_url`: URL đã duyệt qua |
| **file\_search** | Không có | Không có |

## Mã thông báo và giá

Xin lưu ý rằng các phần gọi công cụ tích hợp sẵn trong yêu cầu được tính vào `prompt_token_count`. Vì các bước trung gian của công cụ này hiện có thể nhìn thấy và được trả về cho bạn, nên chúng là một phần của nhật ký trò chuyện. Đây chỉ là trường hợp đối với *yêu cầu*, chứ không phải *phản hồi*.

Công cụ Google Tìm kiếm là một trường hợp ngoại lệ đối với quy tắc này. Google Tìm kiếm đã áp dụng mô hình định giá riêng ở cấp truy vấn, vì vậy, các mã thông báo sẽ không bị tính phí gấp đôi (xem trang [Định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi)).

Hãy đọc trang [Mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) để biết thêm thông tin.

## Các điểm hạn chế

- Chuyển về chế độ `validated` theo mặc định (chế độ `auto` không được hỗ trợ) khi bật tính năng lưu thông bối cảnh công cụ.
- Các công cụ tích hợp như `google_search` dựa vào thông tin vị trí và thời gian hiện tại. Vì vậy, nếu `system_instruction` hoặc `function_declaration.description` của bạn có thông tin vị trí và thời gian mâu thuẫn, thì tính năng kết hợp công cụ có thể không hoạt động hiệu quả.

## Các công cụ được hỗ trợ

Hoạt động lưu thông ngữ cảnh công cụ tiêu chuẩn áp dụng cho các công cụ phía máy chủ (được tích hợp sẵn).
Thực thi mã cũng là một công cụ phía máy chủ, nhưng có giải pháp tích hợp sẵn riêng để lưu thông ngữ cảnh. Computer Use và function calling là các công cụ phía máy khách, đồng thời có các giải pháp tích hợp để lưu thông ngữ cảnh.

| Công cụ | Bên thực thi | Hỗ trợ lưu thông theo bối cảnh |
| --- | --- | --- |
| [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) | Phía máy chủ | Được hỗ trợ (tích hợp sẵn, sử dụng các bước `code_execution` và `code_execution_result`) |
| [Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi) | Phía máy khách | Được hỗ trợ (tích hợp sẵn, sử dụng các bước `function_call` và `function_response`) |
| [Hàm tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) | Phía máy khách | Được hỗ trợ (tích hợp sẵn, sử dụng các bước `function_call` và `function_response`) |

## Bước tiếp theo

- Tìm hiểu thêm về tính năng [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) trong Gemini API.
- Khám phá các công cụ được hỗ trợ:
  - [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)
  - [Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)
  - [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
