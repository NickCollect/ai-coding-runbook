---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=vi
fetched_at: 2026-05-25T05:26:01.933094+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ngữ cảnh URL

Công cụ bối cảnh URL cho phép bạn cung cấp thêm bối cảnh cho các mô hình dưới dạng URL. Bằng cách đưa URL vào yêu cầu, mô hình sẽ truy cập vào nội dung của những trang đó (chừng nào đó không phải là loại URL được liệt kê trong [phần hạn chế](#limitations)) để cung cấp thông tin và cải thiện phản hồi của mô hình.

Công cụ ngữ cảnh URL hữu ích cho những tác vụ như sau:

- **Trích xuất dữ liệu**: Lấy thông tin cụ thể như giá, tên hoặc phát hiện chính từ nhiều URL.
- **So sánh tài liệu**: Phân tích nhiều báo cáo, bài viết hoặc tệp PDF để xác định điểm khác biệt và theo dõi xu hướng.
- **Tổng hợp và tạo nội dung**: Kết hợp thông tin từ nhiều URL nguồn để tạo bản tóm tắt, bài đăng trên blog hoặc báo cáo chính xác.
- **Phân tích mã và tài liệu**: Chỉ đến một kho lưu trữ trên GitHub hoặc tài liệu kỹ thuật để giải thích mã, tạo hướng dẫn thiết lập hoặc trả lời câu hỏi.

Ví dụ sau đây cho thấy cách so sánh hai công thức nấu ăn từ các trang web khác nhau.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
  {"url_context": {}},
]

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

response = client.models.generate_content(
    model=model_id,
    contents=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)

# For verification, you can inspect the metadata to see which URLs the model retrieved
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    ],
    config: {
      tools: [{urlContext: {}}],
    },
  });
  console.log(response.text);

  // For verification, you can inspect the metadata to see which URLs the model retrieved
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          }
      ]
  }' > result.json

cat result.json
```

## Cách hoạt động

Công cụ Bối cảnh URL sử dụng quy trình truy xuất gồm hai bước để cân bằng tốc độ, chi phí và quyền truy cập vào dữ liệu mới. Khi bạn cung cấp một URL, công cụ này sẽ cố gắng tìm nạp nội dung từ bộ nhớ đệm chỉ mục nội bộ trước tiên. Thư mục này đóng vai trò là bộ nhớ đệm được tối ưu hoá cao. Nếu một URL không có trong chỉ mục (ví dụ: nếu đó là một trang rất mới), thì công cụ này sẽ tự động quay lại để thực hiện một lượt tìm nạp trực tiếp.
Thao tác này truy cập trực tiếp vào URL để truy xuất nội dung của URL đó theo thời gian thực.

## Kết hợp với các công cụ khác

Bạn có thể kết hợp công cụ bối cảnh URL với các công cụ khác để tạo quy trình làm việc hiệu quả hơn.

[Các mô hình Gemini 3](#supported-models) hỗ trợ việc kết hợp các công cụ tích hợp (như URL Context) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

### Bám sát nguồn bằng tính năng tìm kiếm

Khi cả ngữ cảnh URL và tính năng [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi) đều được bật, mô hình có thể sử dụng các chức năng tìm kiếm của mình để tìm thông tin liên quan trên mạng, sau đó sử dụng công cụ ngữ cảnh URL để hiểu rõ hơn về những trang mà mô hình tìm thấy. Phương pháp này rất hiệu quả đối với những câu lệnh yêu cầu cả tìm kiếm trên diện rộng và phân tích chuyên sâu các trang cụ thể.

### Python

```
from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch, UrlContext

client = genai.Client()
model_id = "gemini-3.5-flash"

tools = [
      {"url_context": {}},
      {"google_search": {}}
  ]

response = client.models.generate_content(
    model=model_id,
    contents="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    config=GenerateContentConfig(
        tools=tools,
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: [
        "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    ],
    config: {
      tools: [
        {urlContext: {}},
        {googleSearch: {}}
        ],
    },
  });
  console.log(response.text);
  // To get URLs retrieved for context
  console.log(response.candidates[0].urlContextMetadata)
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "contents": [
          {
              "parts": [
                  {"text": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute."}
              ]
          }
      ],
      "tools": [
          {
              "url_context": {}
          },
          {
              "google_search": {}
          }
      ]
  }' > result.json

cat result.json
```

## Hiểu rõ câu trả lời

Khi mô hình sử dụng công cụ bối cảnh URL, câu trả lời sẽ bao gồm một đối tượng `url_context_metadata`. Đối tượng này liệt kê các URL mà mô hình đã truy xuất nội dung và trạng thái của từng lần truy xuất. Điều này rất hữu ích cho việc xác minh và gỡ lỗi.

Sau đây là ví dụ về phần phản hồi đó (một số phần của phản hồi đã bị bỏ qua để cho ngắn gọn):

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "... \n"
          }
        ],
        "role": "model"
      },
      ...
      "url_context_metadata": {
        "url_metadata": [
          {
            "retrieved_url": "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          },
          {
            "retrieved_url": "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
            "url_retrieval_status": "URL_RETRIEVAL_STATUS_SUCCESS"
          }
        ]
      }
    }
  ]
}
```

Để biết thông tin chi tiết đầy đủ về đối tượng này , hãy xem [tài liệu tham khảo API `UrlContextMetadata`](https://ai.google.dev/api/generate-content?hl=vi#UrlContextMetadata).

### Kiểm tra an toàn

Hệ thống sẽ kiểm tra nội dung của URL để xác nhận rằng URL đó đáp ứng các tiêu chuẩn an toàn. Nếu URL bạn cung cấp không vượt qua được bước kiểm tra này, bạn sẽ nhận được `url_retrieval_status` trong số `URL_RETRIEVAL_STATUS_UNSAFE`.

### Số lượng mã thông báo

Nội dung được truy xuất từ các URL mà bạn chỉ định trong câu lệnh sẽ được tính là một phần của mã thông báo đầu vào. Bạn có thể xem số lượng token cho câu lệnh và mức sử dụng công cụ trong đối tượng [`usage_metadata`](https://ai.google.dev/api/generate-content?hl=vi#UsageMetadata) của đầu ra mô hình. Sau đây là một ví dụ về kết quả đầu ra:

```
'usage_metadata': {
  'candidates_token_count': 45,
  'prompt_token_count': 27,
  'prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 27}],
  'thoughts_token_count': 31,
  'tool_use_prompt_token_count': 10309,
  'tool_use_prompt_tokens_details': [{'modality': <MediaModality.TEXT: 'TEXT'>,
    'token_count': 10309}],
  'total_token_count': 10412
  }
```

Giá mỗi mã thông báo phụ thuộc vào mô hình được dùng, hãy xem trang [định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) để biết thông tin chi tiết.

## Mô hình được hỗ trợ

| Mô hình | Ngữ cảnh URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/gemini-3.1-flash-lite-preview?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Các phương pháp hay nhất

- **Cung cấp URL cụ thể**: Để có kết quả tốt nhất, hãy cung cấp URL trực tiếp đến nội dung mà bạn muốn mô hình phân tích. Mô hình này sẽ chỉ truy xuất nội dung từ những URL mà bạn cung cấp, chứ không phải nội dung từ các đường liên kết lồng nhau.
- **Kiểm tra khả năng tiếp cận**: Xác minh rằng các URL bạn cung cấp không dẫn đến những trang yêu cầu đăng nhập hoặc nằm sau tường phí.
- **Sử dụng URL đầy đủ**: Cung cấp URL đầy đủ, bao gồm cả giao thức (ví dụ: https://www.google.com thay vì chỉ google.com).

## Các điểm hạn chế

- Gọi hàm: Tính năng sử dụng công cụ (Ngữ cảnh URL, Bám sát nguồn bằng Google Tìm kiếm, v.v.) với tính năng gọi hàm hiện không được hỗ trợ.
- Giới hạn yêu cầu: Công cụ này có thể xử lý tối đa 20 URL cho mỗi yêu cầu.
- Kích thước nội dung URL: Kích thước tối đa cho nội dung được truy xuất từ một URL duy nhất là 34 MB.
- Khả năng truy cập công khai: Các URL phải truy cập được công khai trên web.
  Không được hỗ trợ địa chỉ máy chủ cục bộ (ví dụ: localhost, 127.0.0.1), mạng riêng tư và dịch vụ tạo đường hầm (ví dụ: ngrok, pinggy).
- Chỉ có trong Gemini API: Bối cảnh URL chỉ có trong Gemini API, chứ không có trong Nền tảng tác nhân Gemini Enterprise.

### Các loại nội dung được hỗ trợ và không được hỗ trợ

Công cụ này có thể trích xuất nội dung từ các URL có những loại nội dung sau:

- Văn bản (text/html, application/json, text/plain, text/xml, text/css, text/javascript , text/csv, text/rtf)
- Hình ảnh (image/png, image/jpeg, image/bmp, image/webp)
- PDF (application/pdf)

Các loại nội dung sau đây **không** được hỗ trợ:

- Nội dung có tường phí
- Video trên YouTube (Xem phần [hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#youtube) để tìm hiểu cách xử lý URL của YouTube)
- Các tệp trên Google Workspace như tài liệu hoặc bảng tính trên Google
- Tệp video và âm thanh

## Bước tiếp theo

- Hãy khám phá [sổ tay về ngữ cảnh URL](https://colab.sandbox.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Grounding.ipynb?hl=vi#url-context) để xem thêm ví dụ.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
