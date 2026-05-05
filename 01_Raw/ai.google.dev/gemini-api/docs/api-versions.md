---
source_url: https://ai.google.dev/gemini-api/docs/api-versions?hl=vi
fetched_at: 2026-05-05T20:47:08.738646+00:00
title: "Gi\u1ea3i th\u00edch v\u1ec1 c\u00e1c phi\u00ean b\u1ea3n API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu tham khảo API](https://ai.google.dev/api?hl=vi)

Gửi ý kiến phản hồi

# Giải thích về các phiên bản API

Tài liệu này cung cấp thông tin tổng quan cấp cao về sự khác biệt giữa phiên bản `v1` và `v1beta` của Gemini API.

- **v1**: Phiên bản ổn định của API. Các tính năng trong phiên bản ổn định được hỗ trợ đầy đủ trong suốt thời gian tồn tại của phiên bản lớn. Nếu có bất kỳ thay đổi có thể gây lỗi nào, thì phiên bản lớn tiếp theo của API sẽ được tạo và phiên bản hiện có sẽ không được dùng nữa sau một khoảng thời gian hợp lý.
  Các thay đổi không làm gián đoạn có thể được giới thiệu cho API mà không làm thay đổi phiên bản chính.
- **v1beta**: Phiên bản này bao gồm các tính năng ban đầu có thể đang trong giai đoạn phát triển và có thể có các thay đổi làm gián đoạn. Ngoài ra, không có gì đảm bảo rằng các tính năng trong phiên bản thử nghiệm sẽ chuyển sang phiên bản ổn định. **Nếu cần sự ổn định trong môi trường phát hành chính thức và không thể chấp nhận các thay đổi có thể gây lỗi, bạn không nên sử dụng phiên bản này trong môi trường phát hành chính thức.**

| Tính năng | v1 | v1beta |
| --- | --- | --- |
| Tạo nội dung – Chỉ nhập văn bản |  |  |
| Tạo nội dung – Đầu vào là văn bản và hình ảnh |  |  |
| Tạo nội dung – Kết quả dạng văn bản |  |  |
| Tạo nội dung – Cuộc trò chuyện nhiều lượt (trò chuyện) |  |  |
| Tạo nội dung – Lệnh gọi hàm |  |  |
| Tạo nội dung – Phát trực tuyến |  |  |
| Nhúng nội dung – Chỉ nhập văn bản |  |  |
| Tạo câu trả lời |  |  |
| Công cụ truy xuất ngữ nghĩa |  |  |
| Interactions API |  |  |

- – Được hỗ trợ
- – Sẽ không bao giờ được hỗ trợ

## Định cấu hình phiên bản API trong SDK

Gemini API SDK mặc định là `v1beta`, nhưng bạn có thể chọn sử dụng các phiên bản khác bằng cách đặt phiên bản API như trong mẫu mã sau:

### Python

```
from google import genai

client = genai.Client(http_options={'api_version': 'v1'})

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents="Explain how AI works",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  httpOptions: { apiVersion: "v1" },
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'
```

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
