---
source_url: https://ai.google.dev/gemini-api/docs/gemini-3?hl=vi
fetched_at: 2026-05-05T13:10:13.577938+00:00
title: "H\u01b0\u1edbng d\u1eabn cho nh\u00e0 ph\u00e1t tri\u1ec3n Gemini 3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/Tính năng Nghiên cứu chuyên sâu của Gemini) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

- [Trang chủ](https://ai.google.dev/gemini-api/docs/Trang chủ)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/Tài liệu)

Gửi ý kiến phản hồi

# Hướng dẫn cho nhà phát triển Gemini 3

Gemini 3 là bộ mô hình thông minh nhất của chúng tôi cho đến nay, được xây dựng dựa trên nền tảng suy luận tiên tiến. Gemini Pro được thiết kế để biến mọi ý tưởng thành hiện thực bằng cách thành thạo quy trình làm việc dựa trên tác nhân, lập trình tự động và các tác vụ đa phương thức phức tạp.
Hướng dẫn này trình bày các tính năng chính của nhóm mô hình Gemini 3 và cách khai thác tối đa nhóm mô hình này.

[Dùng thử Gemini 3.1 Pro (bản dùng thử)](https://ai.google.dev/gemini-api/docs/Dùng thử Gemini 3.1 Pro (bản dùng thử))
[Dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/Dùng thử Gemini 3 Flash)
[Dùng thử Nano Banana 2](https://ai.google.dev/gemini-api/docs/Dùng thử Nano Banana 2)

Khám phá [bộ sưu tập các ứng dụng Gemini 3](https://ai.google.dev/gemini-api/docs/bộ sưu tập các ứng dụng Gemini 3) để xem cách mô hình này xử lý khả năng suy luận nâng cao, lập trình tự động và các nhiệm vụ phức tạp liên quan đến nhiều phương thức.

Bắt đầu bằng một vài dòng mã:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Find the race condition in this multi-threaded C++ snippet: [code here]",
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Find the race condition in this multi-threaded C++ snippet: [code here]"}]
    }]
  }'
```

## Làm quen với dòng mô hình Gemini 3

Gemini 3.1 Pro phù hợp nhất với những nhiệm vụ phức tạp đòi hỏi kiến thức rộng lớn về thế giới và khả năng suy luận nâng cao trên nhiều phương thức.

Gemini 3 Flash là mô hình mới nhất thuộc dòng 3, có trí thông minh cấp Pro với tốc độ và mức giá của Flash.

Nano Banana Pro (còn gọi là Gemini 3 Pro Image) là mô hình tạo hình ảnh có chất lượng cao nhất của chúng tôi, còn Nano Banana 2 (còn gọi là Gemini 3.1 Flash Image) là mô hình tương đương có hiệu suất cao, số lượng lớn và mức giá thấp hơn.

Gemini 3.1 Flash-Lite là mô hình chủ lực của chúng tôi, được xây dựng để mang lại hiệu quả chi phí và xử lý các nhiệm vụ có khối lượng lớn.

Tất cả các mô hình Gemini 3 hiện đang ở giai đoạn dùng thử.

| Mã kiểu máy | Cửa sổ ngữ cảnh (Vào / Ra) | Điểm cắt kiến thức | Giá (Đầu vào / Đầu ra)\* |
| --- | --- | --- | --- |
| **gemini-3.1-flash-lite-preview** | 1M / 64k | Tháng 1 năm 2025 | 0,25 USD (văn bản, hình ảnh, video), 0,5 USD (âm thanh) / 1,5 USD |
| **gemini-3.1-flash-image-preview** | 128k / 32k | Tháng 1 năm 2025 | 0,25 USD (Đầu vào là văn bản) / 0,067 USD (Đầu ra là hình ảnh)\*\* |
| **gemini-3.1-pro-preview** | 1M / 64k | Tháng 1 năm 2025 | 2 USD / 12 USD (<200.000 token)   4 USD / 18 USD (>200.000 token) |
| **gemini-3-flash-preview** | 1M / 64k | Tháng 1 năm 2025 | 0,5 USD / 3 USD |
| **gemini-3-pro-image-preview** | 65.000 / 32.000 | Tháng 1 năm 2025 | 2 USD (Nhập văn bản) / 0,134 USD (Xuất hình ảnh)\*\* |

*\* Giá được tính cho mỗi 1 triệu mã thông báo, trừ phi có quy định khác.*
*\*\* Giá hình ảnh thay đổi theo độ phân giải. Hãy xem [trang giá](https://ai.google.dev/gemini-api/docs/trang giá) để biết thông tin chi tiết.*

Để biết thông tin chi tiết về giới hạn, giá cả và thông tin bổ sung, hãy xem [trang mô hình](https://ai.google.dev/gemini-api/docs/trang mô hình).

## Các tính năng mới của API trong Gemini 3

Gemini 3 giới thiệu các tham số mới được thiết kế để giúp nhà phát triển kiểm soát độ trễ, chi phí và độ trung thực của nhiều phương thức hiệu quả hơn.

### Cấp độ tư duy

Theo mặc định, các mô hình Gemini 3 sử dụng tư duy linh hoạt để suy luận thông qua các câu lệnh. Bạn có thể sử dụng tham số `thinking_level` để kiểm soát độ sâu **tối đa** của quy trình suy luận nội bộ của mô hình trước khi mô hình tạo ra một câu trả lời. Gemini 3 coi những cấp độ này là hạn mức tương đối cho hoạt động tư duy thay vì đảm bảo nghiêm ngặt về số lượng mã thông báo.

Nếu bạn không chỉ định `thinking_level`, Gemini 3 sẽ mặc định là `high`. Để có câu trả lời nhanh hơn và có độ trễ thấp hơn khi không cần suy luận phức tạp, bạn có thể giới hạn mức độ suy nghĩ của mô hình ở `low`.

| Cấp độ tư duy | Gemini 3.1 Pro | Gemini 3.1 Flash-Lite | Gemini 3 Flash | Mô tả |
| --- | --- | --- | --- | --- |
| **`minimal`** | Không được hỗ trợ | Được hỗ trợ (Mặc định) | Được hỗ trợ | Phù hợp với chế độ cài đặt "không cần suy nghĩ" cho hầu hết các câu hỏi. Mô hình có thể suy nghĩ rất ít cho các nhiệm vụ viết mã phức tạp. Giảm thiểu độ trễ cho các ứng dụng trò chuyện hoặc ứng dụng có thông lượng cao. Xin lưu ý rằng `minimal` không đảm bảo rằng tính năng suy nghĩ đã tắt. |
| **`low`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Giảm thiểu độ trễ và chi phí. Phù hợp nhất với các ứng dụng tuân theo hướng dẫn đơn giản, trò chuyện hoặc có thông lượng cao. |
| **`medium`** | Được hỗ trợ | Được hỗ trợ | Được hỗ trợ | Tư duy cân bằng cho hầu hết các nhiệm vụ. |
| **`high`** | Được hỗ trợ (Mặc định, Động) | Được hỗ trợ (Động) | Được hỗ trợ (Mặc định, Động) | Tối đa hoá độ sâu suy luận. Mô hình có thể mất nhiều thời gian hơn đáng kể để đạt được mã thông báo đầu ra đầu tiên (không phải mã thông báo tư duy), nhưng đầu ra sẽ được suy luận cẩn thận hơn. |

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="How does AI work?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="low")
    ),
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "How does AI work?",
    config: {
      thinkingConfig: {
        thinkingLevel: "low",
      }
    },
  });

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "How does AI work?"}]
    }],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "low"
      }
    }
  }'
```

### Độ phân giải của nội dung nghe nhìn

Gemini 3 giới thiệu khả năng kiểm soát chi tiết đối với quy trình xử lý hình ảnh đa phương thức thông qua tham số `media_resolution`. Độ phân giải cao hơn giúp cải thiện khả năng đọc văn bản nhỏ hoặc xác định các chi tiết nhỏ của mô hình, nhưng làm tăng mức sử dụng mã thông báo và độ trễ.
Tham số `media_resolution` xác định **số lượng mã thông báo tối đa được phân bổ cho mỗi khung hình đầu vào của hình ảnh hoặc video.**

Giờ đây, bạn có thể đặt độ phân giải thành `media_resolution_low`, `media_resolution_medium`, `media_resolution_high` hoặc `media_resolution_ultra_high` cho từng phần nội dung đa phương tiện hoặc trên toàn cầu (thông qua `generation_config`, độ phân giải siêu cao không có sẵn trên toàn cầu). Nếu không được chỉ định, mô hình sẽ sử dụng các giá trị mặc định tối ưu dựa trên loại nội dung nghe nhìn.

**Chế độ cài đặt được đề xuất**

| Loại phương tiện | Chế độ cài đặt nên dùng | Số mã thông báo tối đa | Hướng dẫn sử dụng |
| --- | --- | --- | --- |
| **Hình ảnh** | `media_resolution_high` | 1120 | Bạn nên dùng chế độ này cho hầu hết các tác vụ phân tích hình ảnh để đảm bảo chất lượng tối đa. |
| **Tệp PDF** | `media_resolution_medium` | 560 | Tối ưu cho việc hiểu tài liệu; chất lượng thường đạt đến mức tối đa ở `medium`. Việc tăng lên `high` hiếm khi cải thiện kết quả OCR cho các tài liệu tiêu chuẩn. |
| **Video** (Chung) | `media_resolution_low` (hoặc `media_resolution_medium`) | 70 (mỗi khung hình) | **Lưu ý:** Đối với video, chế độ cài đặt `low` và `medium` được xử lý giống nhau (70 token) để tối ưu hoá việc sử dụng ngữ cảnh. Điều này là đủ cho hầu hết các nhiệm vụ nhận dạng và mô tả hành động. |
| **Video** (Nhiều văn bản) | `media_resolution_high` | 280 (mỗi khung hình) | Chỉ bắt buộc khi trường hợp sử dụng liên quan đến việc đọc văn bản dày đặc (OCR) hoặc các chi tiết nhỏ trong khung hình video. |

### Python

```
from google import genai
from google.genai import types
import base64

# The media_resolution parameter is currently only available in the v1alpha API version.
client = genai.Client(http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents=[
        types.Content(
            parts=[
                types.Part(text="What is in this image?"),
                types.Part(
                    inline_data=types.Blob(
                        mime_type="image/jpeg",
                        data=base64.b64decode("..."),
                    ),
                    media_resolution={"level": "media_resolution_high"}
                )
            ]
        )
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// The media_resolution parameter is currently only available in the v1alpha API version.
const ai = new GoogleGenAI({ apiVersion: "v1alpha" });

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: [
      {
        parts: [
          { text: "What is in this image?" },
          {
            inlineData: {
              mimeType: "image/jpeg",
              data: "...",
            },
            mediaResolution: {
              level: "media_resolution_high"
            }
          }
        ]
      }
    ]
  });

  console.log(response.text);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [
        { "text": "What is in this image?" },
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "..."
          },
          "mediaResolution": {
            "level": "media_resolution_high"
          }
        }
      ]
    }]
  }'
```

### Nhiệt độ

Đối với tất cả các mô hình Gemini 3, bạn nên giữ tham số nhiệt độ ở giá trị mặc định là `1.0`.

Mặc dù các mô hình trước đây thường được hưởng lợi từ việc điều chỉnh nhiệt độ để kiểm soát khả năng sáng tạo so với tính xác định, nhưng khả năng suy luận của Gemini 3 được tối ưu hoá cho chế độ cài đặt mặc định. Việc thay đổi nhiệt độ (đặt nhiệt độ dưới 1.0) có thể dẫn đến hành vi không mong muốn, chẳng hạn như lặp lại hoặc giảm hiệu suất, đặc biệt là trong các nhiệm vụ phức tạp về toán học hoặc lý luận.

### Chữ ký của suy nghĩ

Gemini 3 sử dụng [Chữ ký suy luận](https://ai.google.dev/gemini-api/docs/Chữ ký suy luận) để duy trì ngữ cảnh suy luận trên các lệnh gọi API. Đây là các chữ ký được mã hoá thể hiện quy trình suy nghĩ nội bộ của mô hình. Để đảm bảo mô hình duy trì khả năng suy luận, bạn phải trả lại các chữ ký này cho mô hình trong yêu cầu của mình chính xác như khi nhận được:

- **Gọi hàm (Nghiêm ngặt):** API thực thi quy trình xác thực nghiêm ngặt đối với "Lượt hiện tại". Nếu thiếu chữ ký, bạn sẽ gặp lỗi 400.
- **Văn bản/Trò chuyện:** Việc xác thực không được thực thi nghiêm ngặt, nhưng việc bỏ qua chữ ký sẽ làm giảm khả năng suy luận và chất lượng câu trả lời của mô hình.
- **Tạo/chỉnh sửa hình ảnh (Nghiêm ngặt)**: API thực thi quy trình xác thực nghiêm ngặt trên tất cả các phần của Mô hình, bao gồm cả `thoughtSignature`. Nếu thiếu chữ ký, bạn sẽ gặp lỗi 400.

#### Gọi hàm (xác thực nghiêm ngặt)

Khi Gemini tạo một `functionCall`, Gemini sẽ dựa vào `thoughtSignature` để xử lý chính xác đầu ra của công cụ trong lượt tiếp theo. "Lượt tương tác hiện tại" bao gồm tất cả các bước của Mô hình (`functionCall`) và Người dùng (`functionResponse`) đã diễn ra kể từ thông báo `text` **Người dùng** tiêu chuẩn gần đây nhất.

- **Lệnh gọi một hàm:** Phần `functionCall` chứa một chữ ký. Bạn phải trả lại thiết bị.
- **Lệnh gọi hàm song song:** Chỉ phần `functionCall` đầu tiên trong danh sách sẽ chứa chữ ký. Bạn phải trả lại các bộ phận theo đúng thứ tự đã nhận.
- **Nhiều bước (Tuần tự):** Nếu mô hình gọi một công cụ, nhận được kết quả và gọi *một* công cụ khác (trong cùng một lượt), thì **cả hai** lệnh gọi hàm đều có chữ ký. Bạn phải trả về **tất cả** chữ ký tích luỹ trong nhật ký.

#### Văn bản và truyền trực tuyến

Đối với tính năng trò chuyện hoặc tạo văn bản thông thường, chúng tôi không đảm bảo sẽ có chữ ký.

- **Không truyền trực tuyến**: Phần nội dung cuối cùng của phản hồi có thể chứa một `thoughtSignature`, mặc dù không phải lúc nào cũng có. Nếu có một sản phẩm bị trả lại, bạn nên gửi sản phẩm đó trở lại để duy trì hiệu suất tốt nhất.
- **Phát trực tuyến**: Nếu được tạo, chữ ký có thể xuất hiện trong một đoạn cuối cùng chứa phần văn bản trống. Đảm bảo trình phân tích cú pháp luồng của bạn kiểm tra chữ ký ngay cả khi trường văn bản trống.

#### Tạo và chỉnh sửa hình ảnh

Đối với `gemini-3-pro-image-preview` và `gemini-3.1-flash-image-preview`, chữ ký ý tưởng là yếu tố quan trọng đối với tính năng chỉnh sửa bằng ngôn ngữ tự nhiên. Khi bạn yêu cầu mô hình sửa đổi một hình ảnh, mô hình sẽ dựa vào `thoughtSignature` từ lượt tương tác trước để hiểu bố cục và logic của hình ảnh gốc.

- **Chỉnh sửa:** Chữ ký được đảm bảo ở phần đầu tiên sau các ý tưởng của câu trả lời (`text` hoặc `inlineData`) và ở mọi phần `inlineData` tiếp theo. Bạn phải trả về tất cả các chữ ký này để tránh lỗi.

#### Ví dụ về mã

#### Gọi hàm nhiều bước (Tuần tự)

Người dùng đặt một câu hỏi yêu cầu hai bước riêng biệt (Kiểm tra chuyến bay -> Đặt taxi) trong một lượt.   
  
**Bước 1: Mô hình gọi Công cụ chuyến bay.**  
Mô hình trả về một chữ ký `<Sig_A>`

```
// Model Response (Turn 1, Step 1)
  {
    "role": "model",
    "parts": [
      {
        "functionCall": { "name": "check_flight", "args": {...} },
        "thoughtSignature": "<Sig_A>" // SAVE THIS
      }
    ]
  }
```

**Bước 2: Người dùng gửi Kết quả chuyến bay**  
Chúng ta phải gửi lại `<Sig_A>` để duy trì mạch suy nghĩ của mô hình.

```
// User Request (Turn 1, Step 2)
[
  { "role": "user", "parts": [{ "text": "Check flight AA100..." }] },
  { 
    "role": "model", 
    "parts": [
      { 
        "functionCall": { "name": "check_flight", "args": {...} }, 
        "thoughtSignature": "<Sig_A>" // REQUIRED
      } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": { "name": "check_flight", "response": {...} } }] }
]
```

**Bước 3: Mô hình gọi Công cụ taxi**  
Mô hình ghi nhớ thông tin chuyến bay bị trễ thông qua `<Sig_A>` và giờ quyết định đặt taxi. Thao tác này sẽ tạo ra một chữ ký *mới* `<Sig_B>`.

```
// Model Response (Turn 1, Step 3)
{
  "role": "model",
  "parts": [
    {
      "functionCall": { "name": "book_taxi", "args": {...} },
      "thoughtSignature": "<Sig_B>" // SAVE THIS
    }
  ]
}
```

**Bước 4: Người dùng gửi Kết quả về taxi**  
Để hoàn tất lượt này, bạn phải gửi lại toàn bộ chuỗi: `<Sig_A>` VÀ `<Sig_B>`.

```
// User Request (Turn 1, Step 4)
[
  // ... previous history ...
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "check_flight", ... }, "thoughtSignature": "<Sig_A>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] },
  { 
    "role": "model", 
    "parts": [
       { "functionCall": { "name": "book_taxi", ... }, "thoughtSignature": "<Sig_B>" } 
    ]
  },
  { "role": "user", "parts": [{ "functionResponse": {...} }] }
]
```

#### Gọi hàm song song

Người dùng hỏi: "Kiểm tra thời tiết ở Paris và London." Mô hình này trả về 2 lệnh gọi hàm trong một phản hồi.

```
// User Request (Sending Parallel Results)
[
  {
    "role": "user",
    "parts": [
      { "text": "Check the weather in Paris and London." }
    ]
  },
  {
    "role": "model",
    "parts": [
      // 1. First Function Call has the signature
      {
        "functionCall": { "name": "check_weather", "args": { "city": "Paris" } },
        "thoughtSignature": "<Signature_A>" 
      },
      // 2. Subsequent parallel calls DO NOT have signatures
      {
        "functionCall": { "name": "check_weather", "args": { "city": "London" } }
      } 
    ]
  },
  {
    "role": "user",
    "parts": [
      // 3. Function Responses are grouped together in the next block
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "15C" } }
      },
      {
        "functionResponse": { "name": "check_weather", "response": { "temp": "12C" } }
      }
    ]
  }
]
```

#### Văn bản/Lý luận trong ngữ cảnh (Không xác thực)

Người dùng đặt câu hỏi đòi hỏi phải suy luận trong ngữ cảnh mà không cần đến các công cụ bên ngoài. Mặc dù không được xác thực một cách nghiêm ngặt, nhưng việc thêm chữ ký sẽ giúp mô hình duy trì chuỗi suy luận cho các câu hỏi nối tiếp.

```
// User Request (Follow-up question)
[
  {
    "role": "user",
    "parts": [{ "text": "What are the risks of this investment?" }]
  },
  {
    "role": "model",
    "parts": [
      {
        "text": "I need to calculate the risk step-by-step. First, I'll look at volatility...",
        "thoughtSignature": "<Signature_C>" // Recommended to include
      }
    ]
  },
  {
    "role": "user",
    "parts": [{ "text": "Summarize that in one sentence." }]
  }
]
```

#### Tạo và chỉnh sửa hình ảnh

Đối với tính năng tạo hình ảnh, chữ ký sẽ được xác thực nghiêm ngặt. Chúng xuất hiện ở **phần đầu tiên** (văn bản hoặc hình ảnh) và **tất cả các phần hình ảnh tiếp theo**. Tất cả phải được trả lại trong lượt tiếp theo.

```
// Model Response (Turn 1)
{
  "role": "model",
  "parts": [
    // 1. First part ALWAYS has a signature (even if text)
    {
      "text": "I will generate a cyberpunk city...",
      "thoughtSignature": "<Signature_D>"
    },
    // 2. ALL InlineData (Image) parts ALWAYS have signatures
    {
      "inlineData": { ... }, 
      "thoughtSignature": "<Signature_E>"
    },
  ]
}

// User Request (Turn 2 - Requesting an Edit)
{
  "contents": [
    // History must include ALL signatures received
    {
      "role": "user",
      "parts": [{ "text": "Generate a cyberpunk city" }]
    },
    {
      "role": "model",
      "parts": [
         { "text": "...", "thoughtSignature": "<Signature_D>" },
         { "inlineData": "...", "thoughtSignature": "<Signature_E>" },
      ]
    },
    // New User Prompt
    {
      "role": "user",
      "parts": [{ "text": "Make it daytime." }]
    }
  ]
}
```

#### Di chuyển từ các mô hình khác

Nếu đang chuyển dấu vết của cuộc trò chuyện từ một mô hình khác (ví dụ: Gemini 2.5) hoặc chèn một lệnh gọi hàm tuỳ chỉnh không do Gemini 3 tạo, thì bạn sẽ không có chữ ký hợp lệ.

Để bỏ qua quy trình xác thực nghiêm ngặt trong những trường hợp cụ thể này, hãy điền vào trường chuỗi giả cụ thể này: `"thoughtSignature": "context_engineering_is_the_way
to_go"`

### Đầu ra có cấu trúc bằng các công cụ

Các mô hình Gemini 3 cho phép bạn kết hợp [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/Đầu ra có cấu trúc) với các công cụ tích hợp sẵn, bao gồm [Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/Dựa trên kết quả của Google Tìm kiếm), [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/Ngữ cảnh URL), [Thực thi mã](https://ai.google.dev/gemini-api/docs/Thực thi mã) và [Gọi hàm](https://ai.google.dev/gemini-api/docs/Gọi hàm).

### Python

```
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

### Tạo hình ảnh

Gemini 3.1 Flash Image và Gemini 3 Pro Image cho phép bạn tạo và chỉnh sửa hình ảnh từ câu lệnh văn bản. Gemini sử dụng khả năng suy luận để "suy nghĩ" về một câu lệnh và có thể truy xuất dữ liệu theo thời gian thực (chẳng hạn như dự báo thời tiết hoặc biểu đồ chứng khoán) trước khi sử dụng tính năng [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/Google Tìm kiếm) để liên kết thực tế trước khi tạo ra những hình ảnh có độ trung thực cao.

**Các chức năng mới và được cải thiện:**

- **Độ phân giải 4K và kết xuất văn bản:** Tạo văn bản và sơ đồ sắc nét, dễ đọc với độ phân giải lên đến 2K và 4K.
- **Tạo nội dung dựa trên thông tin thực tế:** Sử dụng công cụ `google_search` để xác minh dữ kiện và tạo hình ảnh dựa trên thông tin thực tế. Tính năng liên kết thực tế bằng Google *Tìm kiếm hình ảnh* có trong Gemini 3.1 Flash Image.
- **Chỉnh sửa bằng ngôn ngữ tự nhiên:** Chỉnh sửa ảnh nhiều lần bằng cách chỉ cần yêu cầu thay đổi (ví dụ: "Chỉnh sửa để có nền là cảnh hoàng hôn"). Quy trình này dựa vào **Chữ ký tư duy** để duy trì ngữ cảnh trực quan giữa các lượt tương tác.

Để biết thông tin chi tiết về tỷ lệ khung hình, quy trình chỉnh sửa và các lựa chọn cấu hình, hãy xem [hướng dẫn Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/hướng dẫn Tạo hình ảnh).

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Generate an infographic of the current weather in Tokyo.",
    config=types.GenerateContentConfig(
        tools=[{"google_search": {}}],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="4K"
        )
    )
)

image_parts = [part for part in response.parts if part.inline_data]

if image_parts:
    image = image_parts[0].as_image()
    image.save('weather_tokyo.png')
    image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3-pro-image-preview",
    contents: "Generate a visualization of the current weather in Tokyo.",
    config: {
      tools: [{ googleSearch: {} }],
      imageConfig: {
        aspectRatio: "16:9",
        imageSize: "4K"
      }
    }
  });

  for (const part of response.candidates[0].content.parts) {
    if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("weather_tokyo.png", buffer);
    }
  }
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Generate a visualization of the current weather in Tokyo."}]
    }],
    "tools": [{"googleSearch": {}}],
    "generationConfig": {
        "imageConfig": {
          "aspectRatio": "16:9",
          "imageSize": "4K"
      }
    }
  }'
```

**Ví dụ về phản hồi**

![Thời tiết ở Tokyo](https://ai.google.dev/static/gemini-api/docs/images/weather-tokyo.jpg?hl=vi)

### Thực thi mã bằng hình ảnh

Gemini 3 Flash có thể coi hình ảnh là một đối tượng cần chủ động tìm hiểu, chứ không chỉ là một hình ảnh tĩnh. Bằng cách kết hợp suy luận với [thực thi mã](https://ai.google.dev/gemini-api/docs/thực thi mã), mô hình sẽ xây dựng một kế hoạch, sau đó viết và thực thi mã Python để phóng to, cắt, chú thích hoặc thao tác hình ảnh theo cách khác từng bước để đưa ra câu trả lời trực quan.

**Trường hợp sử dụng:**

- **Thu phóng và kiểm tra:** Mô hình sẽ tự động phát hiện khi các chi tiết quá nhỏ (ví dụ: đọc một đồng hồ đo hoặc số sê-ri ở xa) và viết mã để cắt cũng như kiểm tra lại khu vực ở độ phân giải cao hơn.
- **Phép toán và biểu đồ trực quan:** Mô hình có thể chạy các phép tính nhiều bước bằng mã (ví dụ: tính tổng các mục hàng trên biên nhận hoặc tạo biểu đồ Matplotlib từ dữ liệu đã trích xuất).
- **Chú thích hình ảnh:** Mô hình có thể vẽ mũi tên, khung viền hoặc các chú thích khác trực tiếp lên hình ảnh để trả lời các câu hỏi về không gian như "Mặt hàng này nên đặt ở đâu?".

Để bật tính năng tư duy trực quan, hãy định cấu hình [Thực thi mã](https://ai.google.dev/gemini-api/docs/Thực thi mã) làm công cụ. Mô hình sẽ tự động dùng mã để chỉnh sửa hình ảnh khi cần.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        image,
        "Zoom into the expression pedals and tell me how many pedals are there?"
    ],
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
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString("base64");

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [
      {
        inlineData: {
          mimeType: "image/jpeg",
          data: base64ImageData,
        },
      },
      {
        text: "Zoom into the expression pedals and tell me how many pedals are there?",
      },
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  for (const part of result.candidates[0].content.parts) {
    if (part.text) {
      console.log("Text:", part.text);
    }
    if (part.executableCode) {
      console.log("Code:", part.executableCode.code);
    }
    if (part.codeExecutionResult) {
      console.log("Output:", part.codeExecutionResult.output);
    }
  }
}

main();
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
      "tools": [{"code_execution": {}}]
    }'
```

Để biết thêm thông tin chi tiết về việc thực thi mã bằng hình ảnh, hãy xem phần [Thực thi mã](https://ai.google.dev/gemini-api/docs/Thực thi mã).

### Phản hồi của hàm đa phương thức

[Tính năng gọi hàm đa phương thức](https://ai.google.dev/gemini-api/docs/Tính năng gọi hàm đa phương thức) cho phép người dùng nhận được các phản hồi của hàm có chứa các đối tượng đa phương thức, giúp cải thiện khả năng sử dụng tính năng gọi hàm của mô hình. Tính năng gọi hàm tiêu chuẩn chỉ hỗ trợ các phản hồi hàm dựa trên văn bản:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'tool',
    parts: [
      {
        functionResponse: {
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData],
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

### Kết hợp các công cụ tích hợp và tính năng gọi hàm

Gemini 3 cho phép sử dụng các công cụ tích hợp sẵn (như Google Tìm kiếm, ngữ cảnh URL và [nhiều công cụ khác](https://ai.google.dev/gemini-api/docs/nhiều công cụ khác)) cũng như các công cụ [gọi hàm](https://ai.google.dev/gemini-api/docs/gọi hàm) tuỳ chỉnh trong cùng một lệnh gọi API, cho phép các quy trình công việc phức tạp hơn. Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/các tổ hợp công cụ).

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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

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
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

## Di chuyển từ Gemini 2.5

Gemini 3 là nhóm mô hình mạnh mẽ nhất của chúng tôi cho đến nay và có những bước cải tiến so với Gemini 2.5. Khi di chuyển, hãy cân nhắc những điều sau:

- **Tư duy:** Nếu trước đây bạn đang sử dụng kỹ thuật thiết kế câu lệnh phức tạp (chẳng hạn như chuỗi suy luận) để buộc Gemini 2.5 suy luận, hãy thử Gemini 3 với `thinking_level: "high"` và câu lệnh đơn giản.
- **Chế độ cài đặt nhiệt độ:** Nếu mã hiện tại của bạn đặt nhiệt độ một cách rõ ràng (đặc biệt là ở giá trị thấp cho đầu ra tất định), bạn nên xoá tham số này và sử dụng giá trị mặc định là 1.0 của Gemini 3 để tránh các vấn đề tiềm ẩn về vòng lặp hoặc hiệu suất giảm sút đối với các tác vụ phức tạp.
- **Hiểu PDF và tài liệu:** Nếu bạn dựa vào hành vi cụ thể để phân tích cú pháp tài liệu dày đặc, hãy kiểm thử chế độ cài đặt `media_resolution_high` mới để đảm bảo độ chính xác liên tục.
- **Mức tiêu thụ mã thông báo:** Việc di chuyển sang chế độ mặc định của Gemini 3 có thể **tăng** mức sử dụng mã thông báo cho tệp PDF nhưng **giảm** mức sử dụng mã thông báo cho video. Nếu các yêu cầu hiện vượt quá cửa sổ ngữ cảnh do độ phân giải mặc định cao hơn, bạn nên giảm rõ ràng độ phân giải của nội dung nghe nhìn.
- **Phân đoạn hình ảnh:** Gemini 3 Pro hoặc Gemini 3 Flash không được hỗ trợ các chức năng phân đoạn hình ảnh (trả về mặt nạ ở cấp độ pixel cho các đối tượng). Đối với những khối lượng công việc yêu cầu phân đoạn hình ảnh gốc, bạn nên tiếp tục sử dụng Gemini 2.5 Flash khi tắt chế độ tư duy hoặc [Gemini Robotics-ER 1.6](https://ai.google.dev/gemini-api/docs/Gemini Robotics-ER 1.6).
- **Sử dụng máy tính:** Gemini 3 Pro và Gemini 3 Flash hỗ trợ tính năng [Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/Sử dụng máy tính). Không giống như dòng 2.5, bạn không cần sử dụng một mô hình riêng để truy cập vào công cụ Sử dụng máy tính.
- **Hỗ trợ công cụ**: [Các mô hình Gemini 3 hiện hỗ trợ việc kết hợp các công cụ tích hợp với tính năng gọi hàm](https://ai.google.dev/gemini-api/docs/Các mô hình Gemini 3 hiện hỗ trợ việc kết hợp các công cụ tích hợp với tính năng gọi hàm). [Tính năng liên kết thực tế trên Maps](https://ai.google.dev/gemini-api/docs/Tính năng liên kết thực tế trên Maps) hiện cũng được hỗ trợ cho các mô hình Gemini 3.

## Khả năng tương thích với OpenAI

Đối với những người dùng sử dụng [lớp tương thích OpenAI](https://ai.google.dev/gemini-api/docs/lớp tương thích OpenAI), các tham số tiêu chuẩn (`reasoning_effort` của OpenAI) sẽ tự động được liên kết với các tham số tương đương của Gemini (`thinking_level`).

## Các phương pháp hay nhất để đưa ra câu lệnh

Gemini 3 là một mô hình suy luận, do đó bạn cần thay đổi cách đưa ra câu lệnh.

- **Hướng dẫn chính xác:** Nhập câu lệnh một cách ngắn gọn. Gemini 3 phản hồi tốt nhất khi nhận được chỉ dẫn trực tiếp và rõ ràng. Có thể phân tích quá mức các kỹ thuật thiết kế câu lệnh dài dòng hoặc quá phức tạp được dùng cho các mô hình cũ.
- **Mức độ chi tiết của câu trả lời:** Theo mặc định, Gemini 3 ít chi tiết hơn và ưu tiên cung cấp câu trả lời trực tiếp, hiệu quả. Nếu trường hợp sử dụng của bạn yêu cầu một nhân cách trò chuyện hoặc "hay chuyện" hơn, bạn phải hướng dẫn rõ ràng cho mô hình trong câu lệnh (ví dụ: "Giải thích điều này với tư cách là một trợ lý thân thiện và hay chuyện").
- **Quản lý bối cảnh:** Khi làm việc với các tập dữ liệu lớn (ví dụ: toàn bộ sách, cơ sở mã hoặc video dài), hãy đặt hướng dẫn hoặc câu hỏi cụ thể của bạn ở cuối câu lệnh, sau bối cảnh dữ liệu. Neo lập luận của mô hình vào dữ liệu được cung cấp bằng cách bắt đầu câu hỏi bằng một cụm từ như "Dựa trên thông tin ở trên...".

Tìm hiểu thêm về các chiến lược thiết kế câu lệnh trong [hướng dẫn kỹ thuật tạo câu lệnh](https://ai.google.dev/gemini-api/docs/hướng dẫn kỹ thuật tạo câu lệnh).

## Câu hỏi thường gặp

1. **Điểm cắt kiến thức của Gemini 3 là khi nào?** Các mô hình Gemini 3 có điểm cắt kiến thức là tháng 1 năm 2025. Để biết thông tin mới nhất, hãy sử dụng công cụ [Tìm kiếm thông tin cơ sở](https://ai.google.dev/gemini-api/docs/Tìm kiếm thông tin cơ sở).
2. **Hạn mức cửa sổ ngữ cảnh là bao nhiêu?** Các mô hình Gemini 3 hỗ trợ cửa sổ ngữ cảnh đầu vào 1 triệu token và đầu ra lên đến 64.000 token.
3. **Gemini 3 có phiên bản miễn phí không?** Gemini 3 Flash `gemini-3-flash-preview` và 3.1 Flash-Lite `gemini-3.1-flash-lite-preview` có các cấp miễn phí trong Gemini API. Bạn có thể dùng thử miễn phí Gemini 3.1 Pro và 3 Flash trong Google AI Studio, nhưng không có cấp miễn phí cho `gemini-3.1-pro-preview` trong Gemini API.
4. **Mã `thinking_budget` cũ của tôi có còn hoạt động không?** Có, `thinking_budget` vẫn được hỗ trợ để đảm bảo khả năng tương thích ngược, nhưng bạn nên di chuyển sang `thinking_level` để có hiệu suất dễ dự đoán hơn. Đừng sử dụng cả hai trong cùng một yêu cầu.
5. **Gemini 3 có hỗ trợ Batch API không?** Có, Gemini 3 hỗ trợ [Batch API](https://ai.google.dev/gemini-api/docs/Batch API).
6. **Context Caching có được hỗ trợ không?** Có, Gemini 3 có hỗ trợ tính năng [Lưu vào bộ nhớ đệm theo bối cảnh](https://ai.google.dev/gemini-api/docs/Lưu vào bộ nhớ đệm theo bối cảnh).
7. **Gemini 3 hỗ trợ những công cụ nào?** Gemini 3 hỗ trợ [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/Google Tìm kiếm), [Kết nối với Google Maps](https://ai.google.dev/gemini-api/docs/Kết nối với Google Maps), [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/Tìm kiếm tệp), [Thực thi mã](https://ai.google.dev/gemini-api/docs/Thực thi mã) và [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/Ngữ cảnh URL). Ngoài ra, mô hình này còn hỗ trợ tính năng [Gọi hàm](https://ai.google.dev/gemini-api/docs/Gọi hàm) tiêu chuẩn cho các công cụ tuỳ chỉnh của riêng bạn và [kết hợp với các công cụ tích hợp](https://ai.google.dev/gemini-api/docs/kết hợp với các công cụ tích hợp).
8. **`gemini-3.1-pro-preview-customtools` là gì?** Nếu bạn đang sử dụng `gemini-3.1-pro-preview` và mô hình này bỏ qua các công cụ tuỳ chỉnh của bạn để ưu tiên các lệnh bash, hãy thử mô hình `gemini-3.1-pro-preview-customtools`. Xem thêm thông tin [tại đây](https://ai.google.dev/gemini-api/docs/tại đây).

## Các bước tiếp theo

- Làm quen với [Sổ tay Gemini 3](https://ai.google.dev/gemini-api/docs/Sổ tay Gemini 3)
- Hãy xem hướng dẫn chuyên biệt về [các cấp độ tư duy](https://ai.google.dev/gemini-api/docs/các cấp độ tư duy) trong Sổ tay nấu ăn và cách di chuyển từ ngân sách tư duy sang các cấp độ tư duy.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://ai.google.dev/gemini-api/docs/Giấy phép ghi nhận tác giả 4.0 của Creative Commons) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://ai.google.dev/gemini-api/docs/Giấy phép Apache 2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://ai.google.dev/gemini-api/docs/Chính sách trang web của Google Developers). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?
