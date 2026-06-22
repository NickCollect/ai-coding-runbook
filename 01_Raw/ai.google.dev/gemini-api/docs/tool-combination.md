---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi
fetched_at: 2026-06-22T06:33:05.627965+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Kết hợp các công cụ tích hợp và tính năng gọi hàm

Gemini cho phép kết hợp [các công cụ tích hợp](https://ai.google.dev/gemini-api/docs/tools?hl=vi), chẳng hạn như `google_search` và [lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) (còn gọi là *công cụ tuỳ chỉnh*) trong một thế hệ bằng cách duy trì và hiển thị nhật ký ngữ cảnh của các lệnh gọi công cụ. Các tổ hợp công cụ tích hợp và tuỳ chỉnh cho phép các quy trình làm việc phức tạp, dựa trên tác nhân, trong đó, chẳng hạn như mô hình có thể tự căn cứ vào dữ liệu web theo thời gian thực trước khi gọi logic kinh doanh cụ thể của bạn.

Dưới đây là ví dụ cho phép kết hợp các công cụ tích hợp và tuỳ chỉnh bằng `google_search` và hàm tuỳ chỉnh `getWeather`:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3.5-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.5-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## Cách hoạt động

Các mô hình Gemini 3 sử dụng *vòng tuần hoàn ngữ cảnh công cụ* để cho phép kết hợp các công cụ tuỳ chỉnh và được tích hợp sẵn. Tính năng lưu chuyển ngữ cảnh công cụ giúp duy trì và hiển thị ngữ cảnh của các công cụ tích hợp, đồng thời chia sẻ ngữ cảnh đó với các công cụ tuỳ chỉnh trong cùng một lệnh gọi từ lượt này sang lượt khác.

### Bật tính năng kết hợp công cụ

- Bạn phải đặt cờ `include_server_side_tool_invocations` thành `true` để bật tính năng lưu chuyển ngữ cảnh công cụ.
- Bao gồm [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#function-declarations), cùng với các công cụ tích hợp mà bạn muốn sử dụng, để kích hoạt hành vi kết hợp.
  - Nếu bạn không thêm `function_declarations`, hoạt động lưu thông bối cảnh công cụ vẫn sẽ tác động đến các công cụ tích hợp sẵn được thêm, miễn là bạn đặt cờ này.

### API trả về các phần

Trong một phản hồi duy nhất, API sẽ trả về các phần `toolCall` và `toolResponse` cho lệnh gọi công cụ tích hợp. Đối với lệnh gọi hàm (công cụ tuỳ chỉnh), API sẽ trả về phần lệnh gọi `functionCall` mà người dùng cung cấp phần `functionResponse` trong lượt tiếp theo.

- `toolCall` và `toolResponse`: API trả về những phần này để duy trì ngữ cảnh về những công cụ được chạy ở phía máy chủ và kết quả thực thi của chúng cho lượt tiếp theo.
- `functionCall` và `functionResponse`: API gửi lệnh gọi hàm cho người dùng điền thông tin và người dùng gửi kết quả trở lại trong phản hồi hàm (các phần này là tiêu chuẩn đối với tất cả [lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) trong Gemini API, không chỉ dành riêng cho tính năng kết hợp công cụ).
- (Chỉ công cụ [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)) `executableCode` và `codeExecutionResult`: Khi sử dụng công cụ Thực thi mã, thay vì `functionCall` và `functionResponse`, API sẽ trả về `executableCode` (mã do mô hình tạo ra nhằm mục đích thực thi) và `codeExecutionResult` (kết quả của mã thực thi).

Bạn phải trả về tất cả các phần, bao gồm cả tất cả [các trường](#critical-fields) mà chúng chứa, cho mô hình ở mỗi lượt để duy trì ngữ cảnh và cho phép kết hợp các công cụ.

### Các trường quan trọng trong các phần được trả về

Một số [phần do API trả về](#api-returns-parts) sẽ bao gồm các trường `id`, `tool_type` và `thought_signature`. Những trường này rất quan trọng để duy trì ngữ cảnh của công cụ (do đó, rất quan trọng đối với các tổ hợp công cụ); bạn cần trả về tất cả các phần *như trong phản hồi* trong các yêu cầu tiếp theo.

- `id`: Giá trị nhận dạng duy nhất liên kết một lệnh gọi với phản hồi của lệnh gọi đó. `id` được **đặt trên tất cả các phản hồi lệnh gọi hàm**, bất kể việc lưu chuyển ngữ cảnh công cụ.
  Bạn *phải* cung cấp cùng một `id` trong phản hồi của hàm mà API cung cấp trong lệnh gọi hàm. Các công cụ tích hợp sẽ tự động chia sẻ `id` giữa lệnh gọi công cụ và phản hồi công cụ.
  - Có trong tất cả các phần liên quan đến công cụ: `toolCall`, `toolResponse`, `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Xác định công cụ cụ thể đang được sử dụng; công cụ hoặc (ví dụ: `URL_CONTEXT`) hoặc tên hàm (ví dụ: `getWeather`) theo nghĩa đen được tích hợp sẵn.
  - Có trong phần `toolCall` và `toolResponse`.
- `thought_signature`: Nội dung thực tế đã mã hoá được nhúng trong **mỗi phần do API trả về**. Không thể tái tạo ngữ cảnh nếu không có chữ ký tư duy; nếu bạn không trả về chữ ký tư duy cho tất cả các phần trong mỗi lượt, mô hình sẽ gặp lỗi.
  - Có ở *tất cả* các bộ phận.

### Dữ liệu dành riêng cho công cụ

Một số công cụ tích hợp trả về các đối số dữ liệu mà người dùng có thể thấy, dành riêng cho loại công cụ.

| Công cụ | Đối số gọi công cụ mà người dùng nhìn thấy (nếu có) | Phản hồi của công cụ mà người dùng nhìn thấy (nếu có) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` URL cần duyệt xem | `urls_metadata` `retrieved_url`: URL được duyệt qua `url_retrieval_status`: Trạng thái duyệt qua |
| **FILE\_SEARCH** | Không có | Không có |

## Ví dụ về cấu trúc yêu cầu kết hợp công cụ

Cấu trúc yêu cầu sau đây cho thấy cấu trúc yêu cầu của câu lệnh: "Thành phố cực bắc ở Hoa Kỳ là thành phố nào? Thời tiết ở đó hôm nay thế nào?". Công cụ này kết hợp 3 công cụ: các công cụ Gemini tích hợp sẵn `google_search` và `code_execution`, cùng một hàm tuỳ chỉnh `get_weather`.

```
{
  "model": "models/gemini-3.5-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Mã thông báo và giá

Xin lưu ý rằng các phần `toolCall` và `toolResponse` trong yêu cầu được tính vào `prompt_token_count`. Vì các bước trung gian của công cụ này hiện có thể nhìn thấy và được trả về cho bạn, nên chúng là một phần của nhật ký trò chuyện. Điều này chỉ áp dụng cho *yêu cầu*, chứ không áp dụng cho *phản hồi*.

Công cụ Google Tìm kiếm là một trường hợp ngoại lệ đối với quy tắc này. Google Tìm kiếm đã áp dụng mô hình định giá riêng ở cấp truy vấn, vì vậy, các mã thông báo sẽ không bị tính phí gấp đôi (xem trang [Định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi)).

Hãy đọc trang [Mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) để biết thêm thông tin.

## Các điểm hạn chế

- Chuyển về chế độ `VALIDATED` theo mặc định (chế độ `AUTO` không được hỗ trợ) khi cờ `include_server_side_tool_invocations` được bật
- Các công cụ tích hợp như `google_search` dựa vào thông tin vị trí và thời gian hiện tại. Vì vậy, nếu `system_instruction` hoặc `function_declaration.description` của bạn có thông tin vị trí và thời gian mâu thuẫn, thì tính năng kết hợp công cụ có thể không hoạt động hiệu quả.

## Các công cụ được hỗ trợ

Việc lưu thông ngữ cảnh công cụ tiêu chuẩn áp dụng cho các công cụ phía máy chủ (được tích hợp sẵn).
Thực thi mã cũng là một công cụ phía máy chủ, nhưng có giải pháp tích hợp sẵn riêng để lưu hành bối cảnh. Computer Use và function calling là các công cụ phía máy khách, đồng thời có các giải pháp tích hợp để lưu thông ngữ cảnh.

| Công cụ | Bên thực thi | Hỗ trợ lưu thông theo bối cảnh |
| --- | --- | --- |
| [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) | Phía máy chủ | Được hỗ trợ |
| [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) | Phía máy chủ | Được hỗ trợ (tích hợp sẵn, sử dụng các phần `executableCode` và `codeExecutionResult`) |
| [Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi) | Phía máy khách | Được hỗ trợ (tích hợp sẵn, sử dụng các phần `functionCall` và `functionResponse`) |
| [Hàm tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) | Phía máy khách | Được hỗ trợ (tích hợp sẵn, sử dụng các phần `functionCall` và `functionResponse`) |

## Bước tiếp theo

- Tìm hiểu thêm về tính năng [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) trong Gemini API.
- Khám phá các công cụ được hỗ trợ:
  - [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)
  - [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)
  - [Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)
  - [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-19 UTC."],[],[]]
