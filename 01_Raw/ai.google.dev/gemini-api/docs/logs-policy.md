---
source_url: https://ai.google.dev/gemini-api/docs/logs-policy?hl=vi
fetched_at: 2026-10-26T06:01:04.082562+00:00
title: "Ghi nh\u1eadt k\u00fd v\u00e0 chia s\u1ebb d\u1eef li\u1ec7u \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ghi nhật ký và chia sẻ dữ liệu

Trang này trình bày cách lưu trữ và quản lý [nhật ký Gemini API](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi). Đây là dữ liệu API do nhà phát triển sở hữu từ các lệnh gọi Gemini API được hỗ trợ cho những dự án có bật tính năng thanh toán. Nhật ký bao gồm toàn bộ quá trình từ yêu cầu của người dùng đến phản hồi của mô hình.
Các nhật ký này chỉ dành riêng cho dự án trên đám mây của bạn trên Google Cloud và tách biệt với mọi nhật ký chỉ được lưu giữ cho mục đích [giám sát hành vi sai trái](https://ai.google.dev/gemini-api/docs/usage-policies?hl=vi).

## Dữ liệu có thể được chia sẻ

Là chủ sở hữu dự án, bạn có thể chọn ghi nhật ký các lệnh gọi Gemini API để sử dụng cho riêng mình hoặc để gửi ý kiến phản hồi và chia sẻ với Google nhằm giúp chúng tôi liên tục cải thiện các mô hình của mình.

Khi bật tính năng ghi nhật ký, bạn có thể giúp chúng tôi xây dựng các hệ thống AI tiếp tục mang lại giá trị cho các nhà phát triển trong nhiều lĩnh vực và trường hợp sử dụng bằng cách chọn đóng góp dữ liệu sau đây để cải thiện sản phẩm và huấn luyện mô hình:

- **Tập dữ liệu:** Sử dụng giao diện Nhật ký và Tập dữ liệu của Google AI Studio để chọn nhật ký (yêu cầu, phản hồi, siêu dữ liệu, v.v.) mà bạn quan tâm từ các lệnh gọi Gemini API được hỗ trợ; đóng góp thông qua việc đưa vào tập dữ liệu, với lựa chọn không tham gia trong quá trình tạo tập dữ liệu.
- **Ý kiến phản hồi:** Khi xem xét nhật ký, bạn có thể đưa ra ý kiến phản hồi, bao gồm cả điểm xếp hạng thích và không thích cũng như mọi nhận xét bằng văn bản mà bạn cung cấp.

Khi bạn chia sẻ một tập dữ liệu với Google, nhật ký của bạn trong tập dữ liệu đó (bao gồm cả yêu cầu và phản hồi) sẽ được xử lý theo [Điều khoản](https://developers.google.com/terms?hl=vi) của chúng tôi đối với "[Dịch vụ không tính phí](https://ai.google.dev/gemini-api/terms?hl=vi#data-use-unpaid)", nghĩa là tập dữ liệu đó có thể được dùng để phát triển và cải thiện các sản phẩm, dịch vụ và công nghệ học máy của Google, bao gồm cả việc cải thiện và huấn luyện các mô hình của chúng tôi. **Đừng thêm thông tin cá nhân, thông tin nhạy cảm hoặc thông tin mật.**

## Cách chúng tôi sử dụng dữ liệu của bạn

Nhật ký được giữ lại trong khoảng thời gian tối đa mặc định là 55 ngày. Sau khoảng thời gian này, nhật ký sẽ tự động được đánh dấu là cần xoá. Bạn có thể cập nhật khoảng thời gian lưu giữ bộ nhớ cho một dự án trong AI Studio để tự động đánh dấu nhật ký cần xoá sau 7, 14, 28 hoặc 55 ngày.

Bạn có thể tạo [tập dữ liệu](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi) để giữ lại nhật ký về mối quan tâm ngoài khoảng thời gian lưu giữ đã đặt cho các trường hợp sử dụng hạ nguồn và đóng góp không bắt buộc cho việc cải thiện mô hình. Nhật ký được lưu trữ trong tập dữ liệu không có khoảng thời gian lưu giữ cố định.

Theo mặc định, vì tính năng ghi nhật ký chỉ dành cho các dự án đã bật thông tin thanh toán,
nên các câu lệnh và câu trả lời trong nhật ký sẽ không được dùng để cải thiện hoặc
phát triển sản phẩm, theo [Điều khoản](https://developers.google.com/terms?hl=vi) của chúng tôi
về việc sử dụng dữ liệu.

Nếu bạn chọn chia sẻ các tập dữ liệu nhật ký của mình với Google, thì những tập dữ liệu đó sẽ được dùng làm dữ liệu minh hoạ thực tế để hiểu rõ hơn về sự đa dạng của các miền và bối cảnh mà hệ thống cũng như ứng dụng AI được sử dụng. Dữ liệu này có thể được dùng để cải thiện chất lượng mô hình, đồng thời cung cấp thông tin cho quá trình huấn luyện và đánh giá các mô hình cũng như dịch vụ trong tương lai. Dữ liệu này được xử lý theo các điều khoản sử dụng dữ liệu của chúng tôi đối với [Dịch vụ không tính phí](https://ai.google.dev/gemini-api/terms?hl=vi#data-use-unpaid).

Theo đó, nhân viên đánh giá có thể đọc, chú thích và xử lý dữ liệu đầu vào và đầu ra của API mà bạn chia sẻ. Trước khi dữ liệu được dùng để cải thiện mô hình, Google sẽ thực hiện các bước để bảo vệ quyền riêng tư của người dùng trong quá trình này. Điều này bao gồm việc huỷ mối liên kết giữa dữ liệu này với Tài khoản Google, khoá API và dự án trên đám mây của bạn trước khi người đánh giá xem hoặc chú thích.

## Quyền đối với dữ liệu

Khi chọn tham gia đóng góp dữ liệu API, bạn xác nhận rằng bạn có các quyền cần thiết để Google xử lý và sử dụng dữ liệu như mô tả trong tài liệu này. **Vui lòng không đóng góp nhật ký chứa thông tin nhạy cảm,
bí mật hoặc độc quyền mà bạn có được thông qua dịch vụ có tính phí**.
Giấy phép mà bạn cấp cho Google theo mục "[Gửi nội dung](https://developers.google.com/terms?hl=vi#b_submission_of_content)" trong Điều khoản API cũng áp dụng cho mọi nội dung (ví dụ: câu lệnh, bao gồm cả hướng dẫn hệ thống liên quan, nội dung được lưu vào bộ nhớ đệm và các tệp như hình ảnh, video hoặc tài liệu) mà bạn gửi đến Dịch vụ và mọi câu trả lời được tạo, trong phạm vi cần thiết theo luật hiện hành để chúng tôi sử dụng.

## Chia sẻ dữ liệu và ý kiến phản hồi

Bạn có thể giúp chúng tôi thúc đẩy ranh giới của nghiên cứu AI, Gemini API và Google AI Studio bằng cách chọn chia sẻ dữ liệu của bạn làm ví dụ, giúp chúng tôi liên tục cải thiện các mô hình của mình trong nhiều bối cảnh và xây dựng các hệ thống AI tiếp tục có giá trị cho nhà phát triển trong nhiều lĩnh vực và trường hợp sử dụng.

### Cấp Người đóng góp cho Gemini API

Cấp Người đóng góp cho Gemini cho phép nhà phát triển được giảm chi phí mã thông báo trên một số mô hình nhất định, đổi lại, Google được phép sử dụng dữ liệu từ các mô hình đó để cung cấp, cải thiện và phát triển các sản phẩm, dịch vụ cũng như công nghệ học máy của Google.

Nhà phát triển được giảm giá đến 50% chi phí mã thông báo cho một số mô hình, trong khi vẫn được hưởng hiệu suất theo thời gian thực tương đương với [API tiêu chuẩn](https://ai.google.dev/gemini-api/docs/optimization?hl=vi). Các mô hình sau đây được hỗ trợ:

| Mô hình | Cấp Người đóng góp |
| --- | --- |
| [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#gemini-4-argon) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#gemini-3.1-pro-preview) | ✔️ |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#gemini-3.8-flash) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#gemini-3.5-flash-lite) | ✔️ |

**Sử dụng dữ liệu:**

- Khi bạn bật Cấp độ Cộng tác viên cho một dự án, dữ liệu của bạn từ việc sử dụng mô hình tham gia trong dự án sẽ được sử dụng theo các điều khoản của chúng tôi về "[Dịch vụ không tính phí](https://ai.google.dev/gemini-api/terms?hl=vi#unpaid-services)".
  Vì dữ liệu của bạn sẽ được dùng để cải thiện các sản phẩm và công nghệ học máy của Google, nên vui lòng không gửi thông tin nhạy cảm hoặc thông tin cá nhân.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-14 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-14 UTC."],[],[]]
