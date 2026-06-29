---
source_url: https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi
fetched_at: 2026-06-29T05:33:39.832116+00:00
title: "Suy lu\u1eadn m\u1ee9c \u0111\u1ed9 \u01b0u ti\u00ean \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Suy luận mức độ ưu tiên

Mô tả: Tìm hiểu cách tối ưu hoá độ trễ bằng cấp suy luận Ưu tiên trong API Tương tác

Gemini Priority API là một cấp suy luận cao cấp được thiết kế cho các khối lượng công việc quan trọng đối với doanh nghiệp, đòi hỏi độ trễ thấp hơn và độ tin cậy cao nhất với mức giá cao cấp. Lưu lượng truy cập ở cấp Ưu tiên được ưu tiên hơn lưu lượng truy cập ở API chuẩn và cấp Linh hoạt.

Bạn có thể suy luận ở cấp Ưu tiên trên các điểm cuối của API Tương tác.

## Cách sử dụng Mức độ ưu tiên

Để sử dụng cấp Ưu tiên, hãy đặt trường `service_tier` trong yêu cầu thành `priority`. Cấp mặc định là chuẩn nếu bạn bỏ qua trường này.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Triage this critical customer support ticket immediately.",
    service_tier='priority'
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
    const interaction = await ai.interactions.create({
        model: "gemini-3.5-flash",
        input: "Triage this critical customer support ticket immediately.",
        service_tier: "priority"
    });
    console.log(interaction.output_text);
}

await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Triage this critical customer support ticket immediately.",
    "service_tier": "priority"
  }'
```

## Cách hoạt động của tính năng suy luận ở cấp Ưu tiên

Tính năng suy luận ở cấp Ưu tiên định tuyến các yêu cầu đến hàng đợi tính toán có mức độ quan trọng cao, mang lại hiệu suất nhanh chóng và có thể dự đoán được cho các ứng dụng hướng đến người dùng. Cơ chế chính của tính năng này là hạ cấp nhẹ phía máy chủ xuống quy trình xử lý chuẩn đối với lưu lượng truy cập vượt quá giới hạn linh động, đảm bảo tính ổn định của ứng dụng thay vì không thực hiện được yêu cầu.

| Tính năng | Mức độ ưu tiên | Chuẩn | Linh hoạt | Theo nhóm |
| --- | --- | --- | --- | --- |
| **Định giá** | Cao hơn 75 – 100% so với cấp Chuẩn | Giá đầy đủ | Chiết khấu 50% | Chiết khấu 50% |
| **Độ trễ** | Giây | Giây đến phút | Phút (mục tiêu 1 – 15 phút) | Tối đa 24 giờ |
| **Độ tin cậy** | Cao (Không thể loại bỏ) | Cao / Trung bình cao | Trong khả năng tốt nhất có thể (Có thể loại bỏ) | Cao (đối với thông lượng) |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ |

### Lợi ích chính

- **Độ trễ thấp**: Được thiết kế để có thời gian phản hồi trong vài giây đối với các công cụ AI tương tác,
  hướng đến người dùng.
- **Độ tin cậy cao**: Lưu lượng truy cập được xử lý với mức độ quan trọng cao nhất và
  hoàn toàn không thể loại bỏ.
- **Hạ cấp nhẹ**: Các đợt tăng đột biến lưu lượng truy cập vượt quá giới hạn linh động sẽ
  tự động được hạ cấp xuống cấp Chuẩn để xử lý thay vì không thực hiện được,
  ngăn ngừa tình trạng ngừng dịch vụ.
- **Ít trở ngại**: Sử dụng cùng một phương thức `create` đồng bộ như các cấp
  Chuẩn và Linh hoạt.

### Trường hợp sử dụng

Quy trình xử lý ở cấp Ưu tiên là lý tưởng cho các quy trình công việc quan trọng đối với doanh nghiệp, trong đó hiệu suất và độ tin cậy là tối quan trọng.

- **Ứng dụng AI tương tác**: Chatbot và trợ lý ảo dịch vụ khách hàng, trong đó
  người dùng trả phí cao cấp và mong đợi các câu trả lời nhanh chóng và nhất quán.
- **Công cụ đưa ra quyết định theo thời gian thực**: Các hệ thống đòi hỏi kết quả có độ tin cậy cao và độ trễ thấp,
  chẳng hạn như phân loại phiếu hỗ trợ trực tiếp hoặc phát hiện gian lận.
- **Các tính năng cao cấp dành cho khách hàng**: Nhà phát triển cần đảm bảo các mục tiêu về cấp dịch vụ (SLO) cao hơn cho khách hàng trả phí.

### Giới hạn số lượng yêu cầu

[Mức tiêu thụ ở cấp Ưu tiên có giới hạn số lượng yêu cầu riêng, mặc dù mức tiêu thụ được tính vào giới hạn số lượng yêu cầu chung đối với lưu lượng truy cập tương tác.](https://aistudio.google.com/rate-limit?hl=vi) Giới hạn số lượng yêu cầu mặc định đối với tính năng suy luận ở cấp Ưu tiên là **0,3 lần giới hạn số lượng yêu cầu chuẩn đối với Mô hình / Cấp**

### Logic hạ cấp nhẹ

Nếu vượt quá giới hạn ở cấp Ưu tiên do tắc nghẽn, các yêu cầu vượt quá sẽ được **tự động và nhẹ nhàng** hạ cấp xuống quy trình xử lý Chuẩn thay vì không thực hiện được với lỗi 503 hoặc 429. Các yêu cầu được hạ cấp sẽ được tính phí theo mức giá chuẩn, chứ không phải mức giá cao cấp ở cấp Ưu tiên.

### Trách nhiệm của ứng dụng khách

- **Theo dõi phản hồi**: Nhà phát triển nên theo dõi `x-gemini-service-tier`
  tiêu đề trong phản hồi API để phát hiện xem các yêu cầu có thường xuyên bị hạ cấp xuống
  `standard`.
- **Thử lại**: Ứng dụng khách phải triển khai logic thử lại/thuật toán thời gian đợi luỹ thừa đối với
  các lỗi chuẩn, chẳng hạn như `DEADLINE_EXCEEDED`.

## Định giá

Tính năng suy luận ở cấp Ưu tiên có giá cao hơn 75 – 100% so với [API chuẩn](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) và được tính phí theo mỗi mã thông báo.

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng suy luận ở cấp Ưu tiên:

| Mô hình | Tính năng suy luận ở cấp Ưu tiên |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Gemini 3.1 Pro (Bản xem trước)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3 Flash (Bản xem trước)](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Bước tiếp theo

- [Tính năng suy luận ở cấp Linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) để giảm chi phí.
- [Mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi): Tìm hiểu về mã thông báo.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
