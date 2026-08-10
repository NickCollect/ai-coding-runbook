---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi
fetched_at: 2026-08-10T03:24:41.464155+00:00
title: "\u0110\u1ed9 ph\u00e2n gi\u1ea3i n\u1ed9i dung nghe nh\u00ecn \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Độ phân giải nội dung nghe nhìn

Tham số `media_resolution` kiểm soát cách Gemini API xử lý dữ liệu đầu vào đa phương tiện như hình ảnh, video và tài liệu PDF bằng cách xác định **số lượng mã thông báo tối đa** được phân bổ cho dữ liệu đầu vào đa phương tiện, cho phép bạn cân bằng chất lượng phản hồi với độ trễ và chi phí. Để biết các chế độ cài đặt, giá trị mặc định và cách các giá trị này tương ứng với mã thông báo, hãy xem phần [Số lượng mã thông báo](#token-counts).

Bạn có thể định cấu hình độ phân giải của nội dung nghe nhìn cho từng đối tượng nội dung nghe nhìn (mục nội dung) trong yêu cầu của mình (chỉ Gemini 3).

## Độ phân giải nội dung đa phương tiện theo từng mục nội dung (chỉ Gemini 3)

Gemini 3 cho phép bạn đặt độ phân giải của nội dung nghe nhìn cho từng đối tượng nội dung nghe nhìn trong yêu cầu của mình, giúp tối ưu hoá mức sử dụng mã thông báo một cách chi tiết. Bạn có thể kết hợp các cấp độ phân giải trong một yêu cầu duy nhất. Ví dụ: sử dụng độ phân giải cao cho một sơ đồ phức tạp và độ phân giải thấp cho một hình ảnh theo ngữ cảnh đơn giản.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
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
    model: "gemini-3.6-flash",
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
    "model": "gemini-3.6-flash",
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

## Các giá trị độ phân giải có thể sử dụng

Gemini API xác định các cấp độ sau đây cho độ phân giải của nội dung nghe nhìn:

- `unspecified`: Chế độ cài đặt mặc định. Số token cho cấp độ này có sự khác biệt đáng kể giữa Gemini 3 và các mô hình Gemini trước đó.
- `low`: Số token thấp hơn, giúp xử lý nhanh hơn và giảm chi phí, nhưng ít chi tiết hơn.
- `medium`: Cân bằng giữa mức độ chi tiết, chi phí và độ trễ.
- `high`: Số token cao hơn, cung cấp nhiều thông tin chi tiết hơn để mô hình hoạt động, nhưng phải trả giá bằng độ trễ và chi phí tăng lên.
- `ultra_high` (Chỉ tính trên mỗi mục nội dung): Số lượng mã thông báo cao nhất, bắt buộc đối với một số trường hợp sử dụng cụ thể, chẳng hạn như [sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi).

Xin lưu ý rằng `high` mang lại hiệu suất tối ưu cho hầu hết các trường hợp sử dụng.

Số lượng mã thông báo chính xác được tạo cho mỗi cấp độ này phụ thuộc vào cả **loại nội dung nghe nhìn** (Hình ảnh, Video, PDF) và **phiên bản mô hình**.

## Số lượng mã thông báo

Các bảng dưới đây tóm tắt số lượng mã thông báo gần đúng cho từng giá trị `media_resolution` và loại nội dung nghe nhìn cho mỗi họ mô hình.

**Các mô hình Gemini 3**

| MediaResolution | Hình ảnh | Video | PDF |
| --- | --- | --- | --- |
| `unspecified` (Mặc định) | 1120 | 70 | 560 |
| `low` | 280 | 70 | 280 + Văn bản gốc |
| `medium` | 560 | 70 | 560 + Văn bản gốc |
| `high` | 1120 | 280 | 1120 + Văn bản gốc |
| `ultra_high` | 2240 | Không áp dụng | Không áp dụng |

## Chọn độ phân giải phù hợp

- **Mặc định (`unspecified`):** Bắt đầu bằng chế độ mặc định. Nó được điều chỉnh để cân bằng chất lượng, độ trễ và chi phí cho hầu hết các trường hợp sử dụng phổ biến.
- **`low`:** Sử dụng cho những trường hợp mà chi phí và độ trễ là yếu tố quan trọng nhất, còn chi tiết chính xác thì ít quan trọng hơn.
- **`medium` / `high`:** Tăng độ phân giải khi nhiệm vụ yêu cầu bạn hiểu rõ các chi tiết phức tạp trong nội dung nghe nhìn. Điều này thường cần thiết cho việc phân tích hình ảnh phức tạp, đọc biểu đồ hoặc hiểu tài liệu dày đặc.
- **`ultra_high`** – Chỉ có trong chế độ cài đặt theo từng mục nội dung. Nên dùng cho các trường hợp sử dụng cụ thể, chẳng hạn như khi dùng máy tính hoặc khi thử nghiệm cho thấy có sự cải tiến rõ rệt so với `high`.
- **Kiểm soát theo từng mục nội dung (Gemini 3):** Tối ưu hoá mức sử dụng mã thông báo. Ví dụ: trong một câu lệnh có nhiều hình ảnh, hãy dùng `high` cho một sơ đồ phức tạp và `low` hoặc `medium` cho các hình ảnh theo ngữ cảnh đơn giản hơn.

**Chế độ cài đặt được đề xuất**

Sau đây là danh sách các chế độ cài đặt độ phân giải phương tiện được đề xuất cho từng loại phương tiện được hỗ trợ.

| Loại phương tiện | Chế độ cài đặt nên dùng | Số mã thông báo tối đa | Hướng dẫn sử dụng |
| --- | --- | --- | --- |
| **Hình ảnh** | `high` | 1120 | Bạn nên dùng chế độ này cho hầu hết các tác vụ phân tích hình ảnh để đảm bảo chất lượng tối đa. |
| **Tệp PDF** | `medium` | 560 | Tối ưu cho việc hiểu tài liệu; chất lượng thường đạt đến mức tối đa ở `medium`. Việc tăng lên `high` hiếm khi cải thiện kết quả OCR cho các tài liệu tiêu chuẩn. |
| **Video** (Chung) | `low` (hoặc `medium`) | 70 (mỗi khung hình) | **Lưu ý:** Đối với video, chế độ cài đặt `low` và `medium` được xử lý giống nhau (70 mã thông báo) để tối ưu hoá việc sử dụng ngữ cảnh. Điều này là đủ cho hầu hết các nhiệm vụ nhận dạng và mô tả hành động. |
| **Video** (Nhiều văn bản) | `high` | 280 (mỗi khung hình) | Chỉ bắt buộc khi trường hợp sử dụng liên quan đến việc đọc văn bản dày đặc (OCR) hoặc các chi tiết nhỏ trong khung hình video. |

Luôn kiểm thử và đánh giá tác động của các chế độ cài đặt độ phân giải khác nhau đối với ứng dụng của bạn để tìm ra sự cân bằng tốt nhất giữa chất lượng, độ trễ và chi phí.

## Bản tóm tắt về khả năng tương thích với phiên bản

- Việc đặt `resolution` cho từng mục nội dung là **đặc quyền của các mô hình Gemini 3**.

## Các bước tiếp theo

- Tìm hiểu thêm về các khả năng đa phương thức của Gemini API trong các hướng dẫn về [hiểu hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi), [hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi) và [hiểu tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
