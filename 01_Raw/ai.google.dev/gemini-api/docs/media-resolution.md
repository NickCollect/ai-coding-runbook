---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi
fetched_at: 2026-05-11T05:03:53.816426+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Độ phân giải của nội dung nghe nhìn

Tham số `media_resolution` kiểm soát cách Gemini API xử lý thông tin đầu vào đa phương tiện như hình ảnh, video và tài liệu PDF bằng cách xác định **số lượng token tối đa** được phân bổ cho thông tin đầu vào đa phương tiện, cho phép bạn cân bằng chất lượng phản hồi với độ trễ và chi phí. Để biết các chế độ cài đặt, giá trị mặc định và cách các giá trị này tương ứng với mã thông báo, hãy xem phần [Số lượng mã thông báo](#token-counts).

Bạn có thể định cấu hình độ phân giải của nội dung nghe nhìn theo 2 cách:

- [Theo phần](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi#per-part-media-resolution) (chỉ Gemini 3)
- [Trên toàn cầu](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi#global-media-resolution) cho toàn bộ yêu cầu `generateContent` (tất cả các mô hình đa phương thức)

## Độ phân giải của từng phần nội dung nghe nhìn (chỉ Gemini 3)

Gemini 3 cho phép bạn đặt độ phân giải của nội dung nghe nhìn cho từng đối tượng nội dung nghe nhìn trong yêu cầu của mình, giúp tối ưu hoá mức sử dụng mã thông báo một cách chi tiết. Bạn có thể kết hợp các cấp độ phân giải trong một yêu cầu duy nhất. Ví dụ: sử dụng độ phân giải cao cho một sơ đồ phức tạp và độ phân giải thấp cho một hình ảnh theo ngữ cảnh đơn giản. Chế độ cài đặt này sẽ ghi đè mọi cấu hình chung cho một phần cụ thể. Để biết chế độ cài đặt mặc định, hãy xem phần [Số lượng mã thông báo](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi#token-counts).

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is currently only available in the v1alpha API version. (experimental)
client = genai.Client(
  http_options={
      'api_version': 'v1alpha',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1alpha' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1alpha/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Độ phân giải nội dung nghe nhìn trên toàn cầu

Bạn có thể đặt độ phân giải mặc định cho tất cả các phần nội dung nghe nhìn trong một yêu cầu bằng cách sử dụng `GenerationConfig`. Tính năng này được tất cả các mô hình đa phương thức hỗ trợ. Nếu một yêu cầu bao gồm cả chế độ cài đặt chung và [chế độ cài đặt theo từng phần](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi#per-part-media-resolution), thì chế độ cài đặt theo từng phần sẽ được ưu tiên cho mặt hàng cụ thể đó.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3-flash-preview',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Các giá trị độ phân giải có thể sử dụng

Gemini API xác định các cấp độ sau đây cho độ phân giải của nội dung nghe nhìn:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Chế độ cài đặt mặc định. Số lượng mã thông báo cho cấp độ này có sự khác biệt đáng kể giữa Gemini 3 và các mô hình Gemini trước đó.
- `MEDIA_RESOLUTION_LOW`: Số lượng mã thông báo thấp hơn, giúp xử lý nhanh hơn và giảm chi phí, nhưng ít chi tiết hơn.
- `MEDIA_RESOLUTION_MEDIUM`: Cân bằng giữa mức độ chi tiết, chi phí và độ trễ.
- `MEDIA_RESOLUTION_HIGH`: Số lượng mã thông báo cao hơn, cung cấp nhiều thông tin chi tiết hơn để mô hình hoạt động, nhưng phải trả giá bằng độ trễ và chi phí tăng lên.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (Chỉ theo phần): Số lượng mã thông báo cao nhất, bắt buộc đối với các trường hợp sử dụng cụ thể, chẳng hạn như [sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi).

Xin lưu ý rằng `MEDIA_RESOLUTION_HIGH` mang lại hiệu suất tối ưu cho hầu hết các trường hợp sử dụng.

Số lượng mã thông báo chính xác được tạo cho mỗi cấp độ này phụ thuộc vào cả **loại nội dung nghe nhìn** (Hình ảnh, Video, PDF) và **phiên bản mô hình**.

## Số lượng mã thông báo

Các bảng dưới đây tóm tắt số lượng mã thông báo gần đúng cho từng giá trị `media_resolution` và loại nội dung nghe nhìn cho mỗi họ mô hình.

**Các mô hình Gemini 3**

|  |  |  |  |
| --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Video** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Mặc định) | 1120 | 70 | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 280 + Văn bản gốc |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 560 + Văn bản gốc |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 1120 + Văn bản gốc |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | Không áp dụng | Không áp dụng |

**Các mô hình Gemini 2.5**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Image** | **Video** | **PDF (Bản quét)** | **PDF (Gốc)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Mặc định) | 256 + Pan & Scan (~2048) | 256 | 256 + OCR | 256 + Văn bản gốc |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 64 + OCR | 64 + Văn bản gốc |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 256 + OCR | 256 + Văn bản gốc |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 256 + OCR | 256 + Văn bản gốc |

## Chọn độ phân giải phù hợp

- **Mặc định (`UNSPECIFIED`):** Bắt đầu bằng chế độ mặc định. Được điều chỉnh để có sự cân bằng tốt về chất lượng, độ trễ và chi phí cho hầu hết các trường hợp sử dụng phổ biến.
- **`LOW`:** Sử dụng cho các trường hợp mà chi phí và độ trễ là yếu tố quan trọng nhất, còn chi tiết ở mức độ chi tiết không quan trọng bằng.
- **`MEDIUM` / `HIGH`:** Tăng độ phân giải khi tác vụ yêu cầu bạn hiểu rõ các chi tiết phức tạp trong nội dung nghe nhìn. Điều này thường cần thiết cho việc phân tích hình ảnh phức tạp, đọc biểu đồ hoặc hiểu tài liệu dày đặc.
- **`ULTRA HIGH`** – Chỉ áp dụng cho chế độ cài đặt theo phần. Nên dùng cho một số trường hợp sử dụng cụ thể, chẳng hạn như khi dùng máy tính hoặc khi kết quả kiểm thử cho thấy có sự cải tiến rõ rệt so với `HIGH`.
- **Kiểm soát theo phần (Gemini 3):** Tối ưu hoá mức sử dụng mã thông báo. Ví dụ: trong một câu lệnh có nhiều hình ảnh, hãy dùng `HIGH` cho một sơ đồ phức tạp và `LOW` hoặc `MEDIUM` cho các hình ảnh theo bối cảnh đơn giản hơn.

**Chế độ cài đặt được đề xuất**

Sau đây là danh sách các chế độ cài đặt độ phân giải nội dung nghe nhìn được đề xuất cho từng loại nội dung nghe nhìn được hỗ trợ.

|  |  |  |  |
| --- | --- | --- | --- |
| **Loại nội dung nghe nhìn** | **Chế độ cài đặt đề xuất** | **Số mã thông báo tối đa** | **Hướng dẫn sử dụng** |
| **Hình ảnh** | `MEDIA_RESOLUTION_HIGH` | 1120 | Bạn nên dùng chế độ này cho hầu hết các tác vụ phân tích hình ảnh để đảm bảo chất lượng tối đa. |
| **Tệp PDF** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Tối ưu cho việc hiểu tài liệu; chất lượng thường đạt đến mức tối đa ở `medium`. Việc tăng lên `high` hiếm khi cải thiện kết quả OCR cho các tài liệu tiêu chuẩn. |
| **Video** (Chung) | `MEDIA_RESOLUTION_LOW` (hoặc `MEDIA_RESOLUTION_MEDIUM`) | 70 (mỗi khung hình) | **Lưu ý:** Đối với video, chế độ cài đặt `low` và `medium` được xử lý giống nhau (70 token) để tối ưu hoá việc sử dụng ngữ cảnh. Điều này là đủ cho hầu hết các nhiệm vụ nhận dạng và mô tả hành động. |
| **Video** (Nhiều văn bản) | `MEDIA_RESOLUTION_HIGH` | 280 (mỗi khung hình) | Chỉ bắt buộc khi trường hợp sử dụng liên quan đến việc đọc văn bản dày đặc (OCR) hoặc các chi tiết nhỏ trong khung hình video. |

Luôn kiểm thử và đánh giá mức tác động của các chế độ cài đặt độ phân giải khác nhau đối với ứng dụng cụ thể của bạn để tìm ra sự cân bằng tốt nhất giữa chất lượng, độ trễ và chi phí.

## Bản tóm tắt về khả năng tương thích giữa các phiên bản

- Enum `MediaResolution` có sẵn cho tất cả các mô hình hỗ trợ đầu vào đa phương tiện.
- Số lượng mã thông báo liên kết với mỗi cấp enum **khác nhau** giữa các mô hình Gemini 3 và các phiên bản Gemini trước đó.
- Việc đặt `media_resolution` trên từng đối tượng `Part` **chỉ dành cho các mô hình Gemini 3**.

## Các bước tiếp theo

- Tìm hiểu thêm về các khả năng đa phương thức của Gemini API trong các hướng dẫn về [hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi), [hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi) và [hiểu tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-07 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-07 UTC."],[],[]]
