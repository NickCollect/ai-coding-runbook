---
source_url: https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi
fetched_at: 2026-06-15T06:27:53.381467+00:00
title: "Nh\u1eadt k\u00fd v\u00e0 t\u1eadp d\u1eef li\u1ec7u \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Nhật ký và tập dữ liệu

Hướng dẫn này chứa mọi thông tin bạn cần để bắt đầu bật tính năng ghi nhật ký cho các ứng dụng Gemini API hiện có. Trong hướng dẫn này, bạn sẽ tìm hiểu cách xem nhật ký của một ứng dụng hiện có hoặc ứng dụng mới trong trang tổng quan Google AI Studio để hiểu rõ hơn về hành vi của mô hình và cách người dùng có thể tương tác với các ứng dụng của bạn. Sử dụng tính năng ghi nhật ký để quan sát, gỡ lỗi và *tuỳ ý chia sẻ ý kiến phản hồi về việc sử dụng với Google nhằm giúp cải thiện Gemini trong các trường hợp sử dụng của nhà phát triển*.[\*](https://ai.google.dev/gemini-api/docs/logs-policy?hl=vi)

Tất cả lệnh gọi API `GenerateContent` và `StreamGenerateContent` đều được hỗ trợ, kể cả những lệnh gọi được thực hiện thông qua các điểm cuối [khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi).

## 1. Bật tính năng ghi nhật ký trong Google AI Studio

Trước khi bắt đầu, hãy đảm bảo bạn có một dự án có bật tính năng thanh toán mà bạn sở hữu.

1. Mở trang nhật ký trong [AI Studio](https://aistudio.google.com/logs?hl=vi) của Google.
2. Chọn dự án của bạn trong trình đơn thả xuống rồi nhấn nút bật để bật tính năng ghi nhật ký cho tất cả các yêu cầu theo mặc định.

![](https://ai.google.dev/static/gemini-api/docs/images/logs-state.png?hl=vi)

Bạn có thể bật hoặc tắt tính năng ghi nhật ký cho tất cả dự án hoặc cho các dự án cụ thể, đồng thời thay đổi các lựa chọn ưu tiên này bất cứ lúc nào thông qua Google AI Studio.

## 2. Xem nhật ký trong AI Studio

1. Chuyển đến [AI Studio](https://aistudio.google.com/logs?hl=vi).
2. Chọn dự án mà bạn đã bật tính năng ghi nhật ký.
3. Bạn sẽ thấy nhật ký xuất hiện trong bảng theo thứ tự thời gian đảo ngược.

![](https://storage.googleapis.com/generativeai-downloads/images/nano-banana-logs.gif)

Nhấp vào một mục để xem toàn bộ lượt xem trang của cặp yêu cầu và phản hồi. Bạn có thể kiểm tra toàn bộ câu lệnh, phản hồi hoàn chỉnh từ Gemini và ngữ cảnh từ lượt trò chuyện trước đó. Xin lưu ý rằng mỗi dự án có hạn mức lưu trữ mặc định là tối đa 1.000 nhật ký và nhật ký không được lưu trong tập dữ liệu sẽ hết hạn sau 55 ngày. Nếu dự án của bạn đạt đến hạn mức bộ nhớ, bạn sẽ được nhắc xoá nhật ký.

## 3. Tuyển chọn và chia sẻ tập dữ liệu

- Trong bảng nhật ký, hãy tìm thanh bộ lọc ở trên cùng để chọn một thuộc tính cần lọc.
- Trong chế độ xem nhật ký đã lọc, hãy dùng hộp đánh dấu để chọn tất cả hoặc một số nhật ký.
- Nhấp vào nút "Tạo tập dữ liệu" xuất hiện ở đầu danh sách.
- Đặt tên mang tính mô tả và nội dung mô tả (không bắt buộc) cho tập dữ liệu mới.
- Bạn sẽ thấy tập dữ liệu mà bạn vừa tạo cùng với tập hợp nhật ký được tuyển chọn.
- Xuất tập dữ liệu để phân tích thêm dưới dạng tệp CSV, JSONL hoặc sang Google Trang tính.

![](https://storage.googleapis.com/generativeai-downloads/images/sales-dataset.gif)

Tập dữ liệu có thể hữu ích cho nhiều trường hợp sử dụng.

- **Tuyển chọn các bộ thử thách:** Thúc đẩy những điểm cải tiến trong tương lai nhắm đến những lĩnh vực mà bạn muốn AI cải thiện.
- **Tuyển chọn các bộ dữ liệu mẫu:** Ví dụ: một mẫu từ việc sử dụng thực tế để tạo phản hồi từ một mô hình khác hoặc một tập hợp các trường hợp đặc biệt để kiểm tra thường xuyên trước khi triển khai.
- **Tập hợp đánh giá:** Tập hợp đại diện cho mức sử dụng thực tế trên các chức năng quan trọng, để so sánh giữa các mô hình hoặc các lần lặp lại hướng dẫn hệ thống khác.

Bạn có thể giúp thúc đẩy tiến trình nghiên cứu AI, Gemini API và Google AI Studio bằng cách chọn chia sẻ các tập dữ liệu của mình dưới dạng ví dụ minh hoạ. Điều này cho phép chúng tôi tinh chỉnh các mô hình của mình trong nhiều bối cảnh và tạo ra các hệ thống AI vẫn hữu ích cho nhà phát triển trong nhiều lĩnh vực và ứng dụng

## Các bước tiếp theo và những điều cần kiểm thử

Giờ đây, khi đã bật tính năng ghi nhật ký, bạn có thể thử một số thao tác sau:

- **Tạo mẫu bằng nhật ký phiên:** Tận dụng [AI Studio Build](https://aistudio.google.com/apps?hl=vi) để tạo ứng dụng mã rung và thêm khoá API để bật nhật ký nhật ký người dùng.
- **Chạy lại nhật ký bằng Gemini Batch API:** Sử dụng các tập dữ liệu để lấy mẫu phản hồi và đánh giá các mô hình hoặc logic ứng dụng bằng cách chạy lại nhật ký thông qua [Gemini Batch API](https://github.com/google-gemini/cookbook/blob/main/examples/Datasets.ipynb).

## Khả năng tương thích

Tính năng ghi nhật ký hiện không được hỗ trợ cho những trường hợp sau:

- Mô hình Imagen và Veo
- Mô hình nhúng Gemini
- Đầu vào chứa video, ảnh GIF hoặc tệp PDF

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-01 UTC."],[],[]]
