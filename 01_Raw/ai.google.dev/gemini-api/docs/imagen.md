---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=vi
fetched_at: 2026-10-05T06:28:09.084648+00:00
title: "T\u1ea1o h\u00ecnh \u1ea3nh b\u1eb1ng Imagen \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)

Gửi ý kiến phản hồi

# Tạo hình ảnh bằng Imagen

Imagen là mô hình tạo hình ảnh cũ của Google. Công cụ này hiện đã ngừng hoạt động và không còn trong Gemini API nữa.

## Di chuyển sang Nano Banana

Chuyển sang dùng Nano Banana để tạo hình ảnh:

- **Tên mô hình**: Sử dụng `gemini-2.5-flash-image` (hoặc các mô hình Nano Banana 2 như `gemini-3.1-flash-image`) thay vì tên mô hình Imagen.
- **Phương thức**: Sử dụng `client.models.generate_content` thay vì `client.models.generate_images`.
- **Xử lý phản hồi**: Nano Banana trả về các phần nội dung chứa dữ liệu hình ảnh thay vì một đối tượng phản hồi hình ảnh cụ thể.

Hãy xem [Hướng dẫn tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) để biết thông tin chi tiết và ví dụ.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-18 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-18 UTC."],[],[]]
