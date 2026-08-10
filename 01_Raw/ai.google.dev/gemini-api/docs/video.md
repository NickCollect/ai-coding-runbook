---
source_url: https://ai.google.dev/gemini-api/docs/video?hl=vi
fetched_at: 2026-08-10T03:13:12.514231+00:00
title: "T\u1ea1o video trong Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo video trong Gemini API

Gemini API cung cấp 2 mô hình để tạo video, đó là [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=vi) và [Veo](https://ai.google.dev/gemini-api/docs/veo?hl=vi).
Mỗi loại được thiết kế cho một quy trình làm việc riêng.

Sử dụng Gemini Omni Flash làm mô hình mặc định để tạo video. Mô hình này mang đến độ nhất quán vượt trội cho video, khả năng suy luận đa đầu vào (hỗ trợ đồng thời văn bản, hình ảnh, âm thanh và video), tính nhất quán của nhân vật, độ chính xác về thông tin thực tế và khả năng chỉnh sửa bằng ngôn ngữ tự nhiên nhiều lượt (ví dụ: thay thế phần tử hoặc thay đổi góc nhìn). Bạn cần sử dụng Veo 3.1 cho các chức năng cụ thể như mở rộng cảnh, kiểm soát khung hình cuối cùng hoặc tích hợp với các quy trình cũ.

## Gemini Omni Flash

Gemini Omni Flash là một mô hình đa phương thức, có tốc độ cao để tạo video và chỉnh sửa video theo cách đàm thoại. Mô hình này có khả năng chuyển đổi nhanh chóng các câu lệnh dạng văn bản và hình ảnh thành video ngắn, đồng thời cho phép bạn tinh chỉnh kết quả qua nhiều lượt bằng cách sử dụng Interactions API.

[Làm quen với Gemini Omni Flash →](https://ai.google.dev/gemini-api/docs/omni?hl=vi)

## Veo 3.1

Veo 3.1 là một mô hình tạo video có âm thanh gốc. Công cụ này hỗ trợ các tính năng như tiện ích video, tạo nội dung theo khung hình cụ thể và chỉ dẫn dựa trên hình ảnh thông qua API `generateContent`.

[Bắt đầu dùng Veo 3.1 →](https://ai.google.dev/gemini-api/docs/veo?hl=vi)

## Hiểu video

Nếu bạn cần nhập và phân tích nội dung video hiện có thay vì tạo video mới, hãy xem [Hướng dẫn về tính năng hiểu video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-30 UTC."],[],[]]
