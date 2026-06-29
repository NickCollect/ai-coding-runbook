---
source_url: https://ai.google.dev/gemini-api/docs/url-context?hl=vi
fetched_at: 2026-06-29T05:32:27.724075+00:00
title: "Ng\u1eef c\u1ea3nh URL \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ngữ cảnh URL

Công cụ bối cảnh URL cho phép bạn cung cấp thêm bối cảnh cho các mô hình dưới dạng URL. Bằng cách đưa URL vào yêu cầu, mô hình sẽ truy cập vào nội dung của những trang đó (miễn là đó không phải là loại URL được liệt kê trong [phần hạn chế](#limitations)) để cung cấp thông tin và cải thiện câu trả lời của mô hình.

Công cụ ngữ cảnh URL rất hữu ích cho những tác vụ như sau:

- **Trích xuất dữ liệu**: Lấy thông tin cụ thể như giá, tên hoặc phát hiện chính từ nhiều URL.
- **So sánh tài liệu**: Phân tích nhiều báo cáo, bài viết hoặc tệp PDF để xác định điểm khác biệt và theo dõi xu hướng.
- **Tổng hợp và tạo nội dung**: Kết hợp thông tin từ nhiều URL nguồn để tạo bản tóm tắt, bài đăng trên blog hoặc báo cáo chính xác.
- **Phân tích mã và tài liệu**: Chỉ đến một kho lưu trữ trên GitHub hoặc tài liệu kỹ thuật để giải thích mã, tạo hướng dẫn thiết lập hoặc trả lời câu hỏi.

Ví dụ sau đây cho thấy cách so sánh hai công thức nấu ăn trên các trang web khác nhau.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

url1 = "https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592"
url2 = "https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/"

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Compare the ingredients and cooking times from the recipes at {url1} and {url2}",
    tools=[{"type": "url_context"}]
)

# Print the model's text response and its source annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "url_citation":
                            print(f"  - {annotation.title}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
    tools: [{ type: "url_context" }]
  });

  // Print the model's text response and its source annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'url_citation') {
                console.log(`  - ${annotation.title}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Compare the ingredients and cooking times from the recipes at https://www.foodnetwork.com/recipes/ina-garten/perfect-roast-chicken-recipe-1940592 and https://www.allrecipes.com/recipe/21151/simple-whole-roast-chicken/",
      "tools": [{"type": "url_context"}]
  }'
```

## Cách hoạt động

Công cụ Bối cảnh URL sử dụng quy trình truy xuất gồm hai bước để cân bằng tốc độ, chi phí và quyền truy cập vào dữ liệu mới. Khi bạn cung cấp một URL, công cụ này sẽ cố gắng tìm nạp nội dung từ bộ nhớ đệm chỉ mục nội bộ trước tiên. Thư mục này đóng vai trò là một bộ nhớ đệm được tối ưu hoá cao. Nếu một URL không có trong chỉ mục (ví dụ: nếu đó là một trang rất mới), thì công cụ này sẽ tự động quay lại để tìm nạp trực tiếp.
Thao tác này truy cập trực tiếp vào URL để truy xuất nội dung của URL đó theo thời gian thực.

## Kết hợp với các công cụ khác

Bạn có thể kết hợp công cụ bối cảnh URL với các công cụ khác để tạo quy trình làm việc hiệu quả hơn.

[Các mô hình Gemini 3](#supported-models) hỗ trợ việc kết hợp các công cụ tích hợp sẵn (chẳng hạn như URL Context) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

### Bám sát nguồn bằng tính năng tìm kiếm

Khi cả ngữ cảnh URL và tính năng [Bám sát nguồn bằng Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi) đều được bật, mô hình có thể sử dụng các khả năng tìm kiếm của mình để tìm thông tin liên quan trên mạng, sau đó sử dụng công cụ ngữ cảnh URL để hiểu rõ hơn về các trang mà mô hình tìm thấy. Phương pháp này rất hiệu quả đối với những câu lệnh yêu cầu cả tìm kiếm trên diện rộng và phân tích chuyên sâu các trang cụ thể.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools=[
        {"type": "url_context"},
        {"type": "google_search"}
    ]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
    tools: [
      { type: "url_context" },
      { type: "google_search" }
    ]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
  }
}

await main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
      "model": "gemini-3.5-flash",
      "input": "Give me three day events schedule based on YOUR_URL. Also let me know what needs to taken care of considering weather and commute.",
      "tools": [
          {"type": "url_context"},
          {"type": "google_search"}
      ]
  }'
```

## Hiểu rõ câu trả lời

Khi mô hình sử dụng công cụ ngữ cảnh URL, câu trả lời bằng văn bản của mô hình sẽ có chú thích `url_citation` nội tuyến trên khối nội dung văn bản. Mỗi chú thích liên kết một đoạn văn bản phản hồi (thông qua `start_index` và `end_index`) với URL nguồn mà đoạn văn bản đó được lấy từ. Đây là cách chính để hiển thị trích dẫn trong ứng dụng của bạn – hãy xem [ví dụ chính ở trên](#get-started) để biết cách trích xuất các trích dẫn này.

Phản hồi cũng bao gồm một bước `url_context_result` có siêu dữ liệu về từng lần truy xuất URL (trạng thái, URL đã truy xuất). Điều này chủ yếu hữu ích cho việc gỡ lỗi.

### Kiểm tra an toàn

Hệ thống sẽ kiểm tra nội dung của các URL để xác nhận rằng các URL đó đáp ứng các tiêu chuẩn an toàn. Nếu một URL không vượt qua được bước kiểm tra này, bước `url_context_result` tương ứng sẽ cho thấy `status` của `"unsafe"`.

### Số lượng mã thông báo

Nội dung được truy xuất từ các URL mà bạn chỉ định trong câu lệnh sẽ được tính là một phần của mã thông báo đầu vào. Bạn có thể xem số lượng mã thông báo trong đối tượng `usage` của lượt tương tác. Sau đây là một ví dụ:

```
'usage': {
  'output_tokens': 45,
  'input_tokens': 27,
  'input_tokens_details': [{'modality': 'TEXT', 'token_count': 27}],
  'thoughts_tokens': 31,
  'tool_use_input_tokens': 10309,
  'tool_use_input_tokens_details': [{'modality': 'TEXT', 'token_count': 10309}],
  'total_tokens': 10412
}
```

Giá mỗi mã thông báo phụ thuộc vào mô hình được sử dụng, hãy xem trang [định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) để biết thông tin chi tiết.

## Mô hình được hỗ trợ

| Mô hình | Ngữ cảnh URL |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Các phương pháp hay nhất

- **Cung cấp URL cụ thể**: Để có kết quả tốt nhất, hãy cung cấp URL trực tiếp đến nội dung mà bạn muốn mô hình phân tích. Mô hình này sẽ chỉ truy xuất nội dung từ những URL mà bạn cung cấp, chứ không truy xuất nội dung từ các đường liên kết lồng nhau.
- **Kiểm tra khả năng tiếp cận**: Xác minh rằng các URL bạn cung cấp không dẫn đến những trang yêu cầu đăng nhập hoặc nằm sau tường phí.
- **Sử dụng URL đầy đủ**: Cung cấp URL đầy đủ, bao gồm cả giao thức (ví dụ: https://www.google.com thay vì chỉ google.com).

## Các điểm hạn chế

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

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
