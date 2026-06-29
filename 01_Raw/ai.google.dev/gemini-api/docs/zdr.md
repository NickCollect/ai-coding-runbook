---
source_url: https://ai.google.dev/gemini-api/docs/zdr?hl=vi
fetched_at: 2026-06-29T05:35:35.086720+00:00
title: "Kh\u00f4ng gi\u1eef l\u1ea1i d\u1eef li\u1ec7u trong Gemini Developer API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Không giữ lại dữ liệu trong Gemini Developer API

Trang này trình bày chi tiết về điều thường được gọi là "không lưu giữ dữ liệu" trong Gemini Developer API.

## Quy định hạn chế về hoạt động huấn luyện

Như đã nêu trong [Điều khoản dịch vụ của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi), khi bạn sử dụng Dịch vụ có tính phí, Google sẽ không sử dụng câu lệnh của bạn (bao gồm cả hướng dẫn hệ thống liên quan, nội dung được lưu vào bộ nhớ đệm và các tệp như hình ảnh, video hoặc tài liệu) hoặc câu trả lời để cải thiện sản phẩm của chúng tôi. Dịch vụ trả phí được định nghĩa [tại đây](https://ai.google.dev/gemini-api/terms?hl=vi#paid-services).

## Việc giữ lại dữ liệu khách hàng và đạt được mục tiêu không giữ lại dữ liệu

Dữ liệu khách hàng thường được lưu giữ trong một khoảng thời gian giới hạn trong các trường hợp và điều kiện sau. Để đạt được mục tiêu không lưu giữ dữ liệu, khách hàng phải thực hiện các hành động cụ thể hoặc tránh sử dụng các tính năng cụ thể trong từng lĩnh vực sau:

- **Ghi nhật ký câu lệnh để giám sát hành vi sai trái**: Như đã nêu trong [Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi), đối với Dịch vụ có trả phí, Google chỉ ghi nhật ký câu lệnh và câu trả lời trong một khoảng thời gian giới hạn để phát hiện các hành vi vi phạm [Chính sách về các hành vi bị cấm khi sử dụng](https://policies.google.com/terms/generative-ai/use-policy?hl=vi). Khi yêu cầu của bạn về ZDR cho một dự án cụ thể được phê duyệt, tất cả nội dung của người dùng (câu lệnh và câu trả lời) và siêu dữ liệu nhận dạng (chẳng hạn như địa chỉ IP và mã nhận dạng Tài khoản Google) sẽ bị xoá trước khi ghi nhật ký. Bản ghi kết quả được đánh dấu là đã được dọn dẹp và không chứa dữ liệu người dùng có thể nhận dạng được, đảm bảo tính tương đồng với chính sách Giữ lại dữ liệu bằng 0 của Nền tảng tác nhân Gemini Enterprise.
- **Dựa trên kết quả của Google Tìm kiếm**: Như đã nêu trong [Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-search), Google lưu trữ câu lệnh, thông tin theo ngữ cảnh và kết quả được tạo trong vòng 30 ngày cho mục đích tạo kết quả dựa trên thông tin thực tế và đề xuất tìm kiếm.
  Thông tin được lưu trữ này có thể được dùng để gỡ lỗi và kiểm thử các hệ thống hỗ trợ việc tiếp đất. **Bạn không thể tắt tính năng lưu trữ thông tin này nếu sử dụng tính năng Dựa trên kết quả của Google Tìm kiếm.**
- **Kết nối với Google Maps**: Như đã nêu trong [Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi), Google lưu trữ câu lệnh, thông tin theo ngữ cảnh và đầu ra được tạo trong vòng 30 ngày cho mục đích tạo kết quả dựa trên thông tin thực tế. Thông tin được lưu trữ này chỉ có thể được dùng cho hoạt động kỹ thuật về độ tin cậy, chẳng hạn như gỡ lỗi trong trường hợp có vấn đề về dịch vụ.
  **Bạn không thể tắt tính năng lưu trữ thông tin này nếu sử dụng tính năng Kết nối với Google Maps.**
- **Interactions API**: Interactions API quản lý trạng thái hoạt động của một cuộc trò chuyện để cho phép nhiều lượt tương tác. **Theo mặc định, Interactions API cho phép lưu trữ trạng thái**. Để đảm bảo không có dấu vết dữ liệu, bạn phải đặt rõ ràng tham số `store` thành `false` trong các yêu cầu API để chọn không tham gia giữ lại trạng thái mặc định.
- **Live API**: API có trạng thái này cho phép kết nối lại theo thời gian thực bằng cách lưu trữ trạng thái cuộc trò chuyện. Để đạt được mục tiêu không lưu giữ dữ liệu, hãy **không định cấu hình SessionResumptionConfig**. Nếu một phiên được tạo, trạng thái trò chuyện (bao gồm văn bản, âm thanh và video) sẽ được giữ lại trong tối đa 24 giờ.
- **Bộ nhớ File API**: File API cho phép người dùng tải các tài sản lớn lên.
  Các tệp được lưu trữ ở trạng thái không hoạt động cho đến khi người dùng xoá hoặc cho đến khi hết hạn.
  Việc sử dụng File API không phụ thuộc vào nhật ký ZDR; người dùng phải xoá tệp theo cách thủ công để đảm bảo không có dấu vết dữ liệu.
- **Lưu vào bộ nhớ đệm ngữ cảnh rõ ràng**: Người dùng có thể lưu thủ công các tập dữ liệu lớn (ví dụ: video dài hoặc thư viện tài liệu) vào bộ nhớ đệm bằng trường `cached_content`. Mặc dù nhật ký của các yêu cầu này tuân theo chính sách loại bỏ ZDR, nhưng bản thân ngữ cảnh được lưu vào bộ nhớ đệm sẽ được lưu trữ bằng `ttl` hoặc `expire_time` do người dùng xác định. Để đạt được mức sử dụng dữ liệu bằng 0 tuyệt đối, đừng sử dụng tính năng cached\_content.
- **Lưu vào bộ nhớ đệm ngầm trong bộ nhớ**: Theo mặc định, các mô hình Gemini lưu dữ liệu vào bộ nhớ đệm trong bộ nhớ để giảm độ trễ và chi phí cho nhà phát triển. Dữ liệu này hoàn toàn nằm trong RAM (không ở trạng thái tĩnh), được tách biệt ở cấp dự án và có TTL là 24 giờ.
  **Điều này không vi phạm chính sách Không lưu giữ dữ liệu.**

## Bước tiếp theo

- Tìm hiểu về [Chính sách về các hành vi bị cấm khi sử dụng AI tạo sinh](https://policies.google.com/terms/generative-ai/use-policy?hl=vi).
- Xem [Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi).
- Nếu bạn cần các chế độ kiểm soát ZDR tự phục vụ ở cấp doanh nghiệp, hãy xem [hướng dẫn về Nền tảng tác nhân Gemini Enterprise
  Giữ lại dữ liệu bằng không](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-28 UTC."],[],[]]
