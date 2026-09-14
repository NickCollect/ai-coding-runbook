---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=vi
fetched_at: 2026-09-14T05:52:20.374119+00:00
title: "Ghi nh\u1eadt k\u00fd v\u00e0 chia s\u1ebb d\u1eef li\u1ec7u \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ghi nhật ký và chia sẻ dữ liệu

Trang này trình bày cách lưu trữ và quản lý [nhật ký Gemini API](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi). Đây là dữ liệu API do nhà phát triển sở hữu từ các lệnh gọi Gemini API được hỗ trợ cho những dự án có bật tính năng thanh toán. Nhật ký bao gồm toàn bộ quy trình từ yêu cầu của người dùng đến phản hồi của mô hình.
Những nhật ký này (chỉ dành riêng cho dự án trên đám mây của Google Cloud) tách biệt với mọi nhật ký chỉ được lưu giữ cho mục đích [giám sát hành vi sai trái](https://ai.google.dev/gemini-api/docs/usage-policies?hl=vi).

## Dữ liệu có thể chia sẻ

Là chủ sở hữu dự án, bạn có thể chọn ghi lại các lệnh gọi Gemini API để sử dụng cho riêng mình hoặc để gửi ý kiến phản hồi và chia sẻ với Google nhằm giúp chúng tôi không ngừng cải thiện các mô hình của mình.

Khi bật tính năng ghi nhật ký, bạn có thể giúp chúng tôi xây dựng các hệ thống AI tiếp tục mang lại giá trị cho các nhà phát triển trong nhiều lĩnh vực và trường hợp sử dụng bằng cách chọn đóng góp dữ liệu sau đây để cải thiện sản phẩm và huấn luyện mô hình:

- **Tập dữ liệu:** Sử dụng giao diện Nhật ký và Tập dữ liệu của Google AI Studio để chọn nhật ký (yêu cầu, phản hồi, siêu dữ liệu, v.v.) mà bạn quan tâm trong các lệnh gọi Gemini API được hỗ trợ; được đóng góp thông qua việc đưa vào tập dữ liệu, với lựa chọn không tham gia trong quá trình tạo tập dữ liệu.
- **Ý kiến phản hồi:** Khi xem xét nhật ký, bạn có thể đưa ra ý kiến phản hồi, bao gồm cả điểm xếp hạng thích và không thích cũng như mọi bình luận bằng văn bản mà bạn cung cấp.

Khi bạn chia sẻ một tập dữ liệu với Google, nhật ký của bạn trong tập dữ liệu đó (bao gồm cả yêu cầu và phản hồi) sẽ được xử lý theo [Điều khoản](https://developers.google.com/terms?hl=vi) của chúng tôi đối với "[Dịch vụ không tính phí](https://ai.google.dev/gemini-api/terms?hl=vi#data-use-unpaid)", nghĩa là tập dữ liệu đó có thể được dùng để phát triển và cải thiện các sản phẩm, dịch vụ và công nghệ học máy của Google, bao gồm cả việc cải thiện và huấn luyện các mô hình của chúng tôi. **Đừng thêm thông tin cá nhân, thông tin nhạy cảm hoặc thông tin mật.**

## Cách chúng tôi sử dụng dữ liệu của bạn

Nhật ký được giữ lại trong khoảng thời gian tối đa mặc định là 55 ngày. Sau khoảng thời gian này, nhật ký sẽ tự động được đánh dấu là cần xoá. Bạn có thể cập nhật khoảng thời gian lưu giữ bộ nhớ cho một dự án trong AI Studio để tự động đánh dấu nhật ký cần xoá sau 7, 14, 28 hoặc 55 ngày.

Bạn có thể tạo [tập dữ liệu](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi) để giữ lại nhật ký về mối quan tâm ngoài khoảng thời gian lưu giữ đã đặt cho các trường hợp sử dụng hạ nguồn và đóng góp không bắt buộc cho việc cải thiện mô hình. Nhật ký được lưu trữ trong tập dữ liệu không có khoảng thời gian lưu giữ cố định.

Theo mặc định, vì tính năng ghi nhật ký chỉ có trong các dự án có bật tính năng thanh toán, nên các câu lệnh và câu trả lời trong nhật ký không được dùng để cải thiện hoặc phát triển sản phẩm, theo [Điều khoản](https://developers.google.com/terms?hl=vi) của chúng tôi về việc sử dụng dữ liệu.

Nếu bạn chọn chia sẻ các tập dữ liệu nhật ký với Google, thì những tập dữ liệu đó sẽ được dùng làm dữ liệu minh hoạ thực tế để hiểu rõ hơn về sự đa dạng của các miền và bối cảnh mà hệ thống cũng như ứng dụng AI được dùng. Dữ liệu này có thể được dùng để cải thiện chất lượng mô hình, cũng như cung cấp thông tin cho việc huấn luyện và đánh giá các mô hình và dịch vụ trong tương lai. Dữ liệu này được xử lý theo các điều khoản sử dụng dữ liệu của chúng tôi đối với [Dịch vụ không tính phí](https://ai.google.dev/gemini-api/terms?hl=vi#data-use-unpaid).

Theo đó, nhân viên đánh giá có thể đọc, chú thích và xử lý dữ liệu đầu vào và đầu ra của API mà bạn chia sẻ. Trước khi sử dụng dữ liệu để cải thiện mô hình, Google sẽ thực hiện các bước để bảo vệ quyền riêng tư của người dùng trong quá trình này. Chẳng hạn như huỷ mối liên kết giữa dữ liệu này với Tài khoản Google, khoá API và dự án trên đám mây của bạn trước khi nhân viên đánh giá xem hoặc chú thích dữ liệu đó.

## Quyền đối với dữ liệu

Khi chọn đóng góp dữ liệu API, bạn xác nhận rằng bạn có các quyền cần thiết để Google xử lý và sử dụng dữ liệu như mô tả trong tài liệu này. **Vui lòng không đóng góp nhật ký chứa thông tin nhạy cảm, bí mật hoặc độc quyền thu được thông qua dịch vụ có tính phí**.
Giấy phép mà bạn cấp cho Google theo phần "[Gửi nội dung](https://developers.google.com/terms?hl=vi#b_submission_of_content)" trong Điều khoản API cũng mở rộng (trong phạm vi cần thiết theo luật hiện hành cho việc sử dụng của chúng tôi) đối với mọi nội dung (ví dụ: câu lệnh, bao gồm cả hướng dẫn hệ thống liên quan, nội dung được lưu vào bộ nhớ đệm và các tệp như hình ảnh, video hoặc tài liệu) mà bạn gửi cho Dịch vụ và mọi câu trả lời được tạo.

## Chia sẻ dữ liệu và ý kiến phản hồi

Bạn có thể giúp chúng tôi thúc đẩy nghiên cứu AI, Gemini API và Google AI Studio bằng cách chọn chia sẻ dữ liệu của bạn dưới dạng ví dụ. Nhờ đó, chúng tôi có thể liên tục cải thiện các mô hình của mình trong nhiều bối cảnh và xây dựng các hệ thống AI tiếp tục mang lại giá trị cho các nhà phát triển trong nhiều lĩnh vực và trường hợp sử dụng.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-08 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-08 UTC."],[],[]]
