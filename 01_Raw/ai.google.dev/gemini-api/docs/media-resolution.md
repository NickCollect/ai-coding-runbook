---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi
fetched_at: 2026-06-29T05:41:30.262015+00:00
title: "\u0110\u1ed9 ph\u00e2n gi\u1ea3i n\u1ed9i dung nghe nh\u00ecn \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Độ phân giải nội dung nghe nhìn

Tham số `media_resolution` kiểm soát cách Gemini API xử lý dữ liệu đầu vào đa phương tiện như hình ảnh, video và tài liệu PDF bằng cách xác định **số lượng mã thông báo tối đa** được phân bổ cho dữ liệu đầu vào đa phương tiện, cho phép bạn cân bằng chất lượng phản hồi với độ trễ và chi phí. Đối với các chế độ cài đặt khác nhau, giá trị mặc định và cách các giá trị này tương ứng với mã thông báo, hãy xem phần [Số lượng mã thông báo](#token-counts).

Bạn có thể định cấu hình độ phân giải đa phương tiện cho từng đối tượng đa phương tiện (mục nội dung) trong yêu cầu của mình (chỉ Gemini 3).

## Độ phân giải đa phương tiện cho từng mục nội dung (chỉ Gemini 3)

Gemini 3 cho phép bạn đặt độ phân giải đa phương tiện cho từng đối tượng đa phương tiện trong yêu cầu của mình, giúp tối ưu hoá chi tiết việc sử dụng mã thông báo. Bạn có thể kết hợp các mức độ phân giải trong một yêu cầu. Ví dụ: sử dụng độ phân giải cao cho một sơ đồ phức tạp và độ phân giải thấp cho một hình ảnh theo ngữ cảnh đơn giản.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
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
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
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
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Các giá trị độ phân giải hiện có

Gemini API xác định các cấp độ sau đây cho độ phân giải đa phương tiện:

- `unspecified`: Chế độ cài đặt mặc định. Số lượng mã thông báo cho cấp độ này khác nhau đáng kể giữa Gemini 3 và các mô hình Gemini trước đó.
- `low`: Số lượng mã thông báo thấp hơn, giúp xử lý nhanh hơn và chi phí thấp hơn, nhưng ít chi tiết hơn.
- `medium`: Cân bằng giữa chi tiết, chi phí và độ trễ.
- `high`: Số lượng mã thông báo cao hơn, cung cấp nhiều chi tiết hơn để mô hình hoạt động, nhưng độ trễ và chi phí sẽ tăng lên.
- `ultra_high` (Chỉ dành cho từng mục nội dung): Số lượng mã thông báo cao nhất, cần thiết cho các trường hợp sử dụng cụ thể như [sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi).

Xin lưu ý rằng `high` mang lại hiệu suất tối ưu cho hầu hết các trường hợp sử dụng.

Số lượng mã thông báo chính xác được tạo cho từng cấp độ này phụ thuộc vào cả **loại phương tiện** (Hình ảnh, Video, PDF) và **phiên bản mô hình**.

## Số lượng mã thông báo

Các bảng dưới đây tóm tắt số lượng mã thông báo gần đúng cho từng giá trị `media_resolution` và loại phương tiện cho mỗi họ mô hình.

**Mô hình Gemini 3**

| MediaResolution | Hình ảnh | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (Mặc định) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + Văn bản gốc |
| `medium` | 560 | 70 | 560 + Văn bản gốc |
| `high` | 1120 | 280 | 1120 + Văn bản gốc |
| `ultra_high` | 2240 | Không áp dụng | Không áp dụng |

## Chọn độ phân giải phù hợp

- **Mặc định (`unspecified`):** Bắt đầu với chế độ mặc định. Chế độ này được điều chỉnh để cân bằng chất lượng, độ trễ và chi phí cho hầu hết các trường hợp sử dụng phổ biến.
- **`low`:** Sử dụng cho các trường hợp mà chi phí và độ trễ là quan trọng nhất, còn chi tiết chi tiết thì ít quan trọng hơn.
- **`medium` / `high`:** Tăng độ phân giải khi tác vụ yêu cầu hiểu các chi tiết phức tạp trong nội dung đa phương tiện. Điều này thường cần thiết cho việc phân tích hình ảnh phức tạp, đọc biểu đồ hoặc hiểu tài liệu dày đặc.
- **`ultra_high`** – Chỉ có cho chế độ cài đặt từng mục nội dung. Nên dùng cho các trường hợp sử dụng cụ thể như sử dụng máy tính hoặc khi thử nghiệm cho thấy có sự cải thiện rõ rệt so với `high`.
- **Kiểm soát từng mục nội dung (Gemini 3):** Tối ưu hoá việc sử dụng mã thông báo. Ví dụ: trong một câu lệnh có nhiều hình ảnh, hãy sử dụng `high` cho một sơ đồ phức tạp và `low` hoặc `medium` cho các hình ảnh theo ngữ cảnh đơn giản hơn.

**Chế độ cài đặt được đề xuất**

Sau đây là danh sách các chế độ cài đặt độ phân giải đa phương tiện được đề xuất cho từng loại phương tiện được hỗ trợ.

| Loại phương tiện | Chế độ cài đặt được đề xuất | Số lượng mã thông báo tối đa | Hướng dẫn sử dụng |
| --- | --- | --- | --- |
| **Hình ảnh** | `high` | 1120 | Nên dùng cho hầu hết các tác vụ phân tích hình ảnh để đảm bảo chất lượng tối đa. |
| **Tệp PDF** | `medium` | 560 | Tối ưu cho việc hiểu tài liệu; chất lượng thường đạt đến mức `medium`. Việc tăng lên `high` hiếm khi cải thiện kết quả OCR cho các tài liệu tiêu chuẩn. |
| **Video** (Chung) | `low` (hoặc `medium`) | 70 (mỗi khung hình) | **Lưu ý:** Đối với video, các chế độ cài đặt `low` và `medium` được xử lý giống nhau (70 mã thông báo) để tối ưu hoá việc sử dụng ngữ cảnh. Điều này là đủ cho hầu hết các tác vụ nhận dạng và mô tả hành động. |
| **Video** (Nhiều văn bản) | `high` | 280 (mỗi khung hình) | Chỉ cần thiết khi trường hợp sử dụng liên quan đến việc đọc văn bản dày đặc (OCR) hoặc các chi tiết nhỏ trong khung hình video. |

Luôn kiểm thử và đánh giá tác động của các chế độ cài đặt độ phân giải khác nhau đối với ứng dụng của bạn để tìm ra sự cân bằng tốt nhất giữa chất lượng, độ trễ và chi phí.

## Tóm tắt về khả năng tương thích với phiên bản

- Việc đặt `resolution` trên từng mục nội dung là **dành riêng cho các mô hình Gemini 3**.

## Các bước tiếp theo

- Tìm hiểu thêm về các tính năng đa phương thức của Gemini API trong hướng dẫn về [hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi), [hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi) và [hiểu tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
