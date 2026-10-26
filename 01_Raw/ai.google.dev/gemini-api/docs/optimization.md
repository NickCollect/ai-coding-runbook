---
source_url: https://ai.google.dev/gemini-api/docs/optimization?hl=vi
fetched_at: 2026-10-26T05:42:33.855206+00:00
title: "T\u1ed1i \u01b0u ho\u00e1 v\u00e0 suy lu\u1eadn Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tối ưu hoá và suy luận Gemini API

Gemini API cung cấp nhiều cơ chế tối ưu hoá để giúp bạn cân bằng tốc độ, chi phí và độ tin cậy dựa trên nhu cầu cụ thể về khối lượng công việc.
Cho dù bạn đang xây dựng bot trò chuyện theo thời gian thực hay chạy các quy trình xử lý dữ liệu ngoại tuyến nặng, việc chọn đúng mô hình có thể giúp giảm đáng kể chi phí hoặc tăng hiệu suất.

| Tính năng | Chuẩn | Gập | Mức độ ưu tiên | Theo nhóm | Đang lưu vào bộ nhớ đệm |
| --- | --- | --- | --- | --- | --- |
| **Định giá** | Giá ban đầu | Giảm giá 50% | Cao hơn từ 75% đến 100% so với mức tiêu chuẩn | Giảm giá 50% | Chiết khấu 90% + Bộ nhớ mã thông báo được tính theo tỷ lệ |
| **Độ trễ** | Vài giây đến vài phút | Phút (mục tiêu 1 – 15 phút) | Giây | Tối đa 24 giờ | Thời gian nhận token đầu tiên nhanh hơn |
| **Độ tin cậy** | Cao / Trung bình cao | Nỗ lực tối đa (Có thể loại bỏ) | Cao (Không rụng lông) | Cao (cho thông lượng) | Không áp dụng |
| **Giao diện** | Đồng bộ | Đồng bộ | Đồng bộ | Không đồng bộ | Trạng thái đã lưu |
| **Trường hợp sử dụng phù hợp nhất** | Quy trình công việc chung của ứng dụng | Chuỗi không khẩn cấp theo trình tự | Ứng dụng phát hành công khai dành cho người dùng | Tập dữ liệu khổng lồ, đánh giá ngoại tuyến | Truy vấn định kỳ trên cùng một tệp |

## Cấp dịch vụ suy luận (Đồng bộ)

Bạn có thể chuyển đổi giữa lưu lượng truy cập đồng bộ được tối ưu hoá về độ tin cậy và lưu lượng truy cập đồng bộ được tối ưu hoá về chi phí bằng cách truyền tham số `service_tier` trong các lệnh gọi tạo tiêu chuẩn.

### Suy luận tiêu chuẩn (Mặc định)

Cấp tiêu chuẩn là lựa chọn mặc định để tạo nội dung tuần tự.
Dịch vụ này cung cấp thời gian phản hồi bình thường mà không cần trả thêm phí hoặc xếp hàng quá lâu.

- **Độ tin cậy:** Mức độ nghiêm trọng tiêu chuẩn
- **Giá:** Giá thông thường.
- **Phù hợp nhất cho:** Hầu hết các ứng dụng tương tác hằng ngày.

### Suy luận ưu tiên (Tối ưu hoá độ trễ)

[Mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi) sẽ định tuyến các yêu cầu của bạn đến các hàng đợi tính toán có mức độ quan trọng cao.
Lưu lượng truy cập này hoàn toàn không thể bị loại bỏ (không bao giờ bị các cấp khác chiếm quyền ưu tiên) và có độ tin cậy cao nhất. Nếu bạn vượt quá giới hạn Ưu tiên linh động, hệ thống sẽ hạ cấp yêu cầu xuống mức Xử lý tiêu chuẩn một cách linh hoạt thay vì báo lỗi.

- **Độ tin cậy:** Mức độ quan trọng cao nhất
- **Giá:** Cao hơn từ 75% đến 100% so với giá chuẩn.
- **Phù hợp nhất với:** Bot trò chuyện với khách hàng, phát hiện gian lận theo thời gian thực và trợ lý AI quan trọng cho doanh nghiệp.

### Suy luận Flex (Tối ưu hoá chi phí)

[Suy luận Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) giảm giá 50% so với mức giá tiêu chuẩn bằng cách tận dụng năng lực điện toán ngoài giờ cao điểm. Các yêu cầu được xử lý đồng bộ, nghĩa là bạn không cần viết lại mã để quản lý các đối tượng theo lô.
Vì đây là lưu lượng truy cập "có thể loại bỏ", nên các yêu cầu có thể bị ưu tiên nếu hệ thống gặp phải tình trạng lưu lượng truy cập tăng đột biến.

- **Độ tin cậy:** Không được đảm bảo, có thể loại bỏ mức độ nghiêm trọng
- **Giá:** 50% Giá tiêu chuẩn (tính phí theo mã thông báo).
- **Phù hợp nhất cho:** Quy trình làm việc nhiều bước của tác nhân, trong đó lệnh gọi N+1 phụ thuộc vào đầu ra của lệnh gọi N, các bản cập nhật CRM ở chế độ nền và các hoạt động đánh giá ngoại tuyến.

## Batch API (Hàng loạt, không đồng bộ)

[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) được thiết kế để xử lý số lượng lớn yêu cầu một cách không đồng bộ với 50% chi phí tiêu chuẩn. Bạn có thể gửi yêu cầu dưới dạng từ điển cùng dòng
hoặc sử dụng tệp đầu vào JSONL (tối đa 2 GB). Hệ thống này xử lý các yêu cầu bằng hàng đợi thông lượng trong nền với thời gian xử lý mục tiêu là 24 giờ.

- **Độ tin cậy:** Có thể bỏ qua nhưng có hệ thống xếp hàng và thử lại tự động trong 24 giờ
- **Giá:** 50% giá của gói Standard.
- **Phù hợp nhất cho:** Tiền xử lý các tập dữ liệu lớn, chạy bộ kiểm thử hồi quy định kỳ và tạo hình ảnh hoặc nhúng khối lượng lớn.

## Lưu bộ nhớ đệm ngữ cảnh (Tiết kiệm dữ liệu đầu vào)

[Bộ nhớ đệm ngữ cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi) được dùng khi một ngữ cảnh ban đầu đáng kể được các yêu cầu ngắn hơn tham chiếu nhiều lần.

- **Lưu vào bộ nhớ đệm ngầm:** Tự động bật trên Gemini 2.5 và các mô hình mới hơn.
  Hệ thống sẽ giúp bạn tiết kiệm chi phí nếu yêu cầu của bạn sử dụng bộ nhớ đệm hiện có dựa trên
  các tiền tố câu lệnh phổ biến.
- **Lưu vào bộ nhớ đệm tường minh:** Bạn có thể tạo đối tượng bộ nhớ đệm theo cách thủ công với một Thời gian tồn tại (TTL) cụ thể. Sau khi tạo, bạn sẽ tham chiếu đến các mã thông báo được lưu vào bộ nhớ đệm cho các yêu cầu tiếp theo để tránh việc truyền tải cùng một tải trọng văn bản nhiều lần. Gemini 4 Argon trở lên không hỗ trợ tính năng lưu vào bộ nhớ đệm tường minh.
- **Giá:** Tính phí dựa trên số lượng mã thông báo bộ nhớ đệm và thời gian lưu trữ (TTL).
- **Phù hợp nhất với:** Chatbot có nhiều chỉ dẫn hệ thống, phân tích lặp đi lặp lại các tệp video dài hoặc truy vấn đối với các tập tài liệu lớn.

## Giảm chi phí đầu vào video bằng quy trình xử lý dựa trên tác nhân

Đối với nội dung video dài (hơn 5 – 10 phút) hoặc các truy vấn có mục tiêu, quy trình xử lý dựa trên tác nhân có thể giảm chi phí mã thông báo đầu vào lên đến 88% trong khi vẫn cải thiện chất lượng phản hồi. Theo mặc định, tất cả mô hình (bao gồm cả Gemini 4) đều sử dụng [quy trình xử lý tĩnh](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#agentic-video-understanding) để trích xuất khung hình ở tốc độ 1 khung hình/giây. Với khả năng hiểu video dựa trên tác nhân, mô hình này sẽ kiểm tra bản chép lời video trước, sau đó tải các phân đoạn hình ảnh một cách linh động ở tốc độ khung hình và độ phân giải cao hơn chỉ khi cần thiết. Đối với các đoạn video ngắn (dưới 5 phút) hoặc bản tóm tắt video đầy đủ trên diện rộng, hãy giữ chế độ xử lý tĩnh mặc định để có Thời gian hiển thị mã thông báo đầu tiên (TTFT) nhanh hơn và chi phí mã thông báo thấp hơn. Chế độ có tác nhân sẽ phát sinh suy luận nội bộ (`total_thought_tokens`) và các chuyến đi khứ hồi bằng công cụ (`total_tool_use_tokens`) trong quá trình điều hướng trên dòng thời gian.

Để sử dụng tính năng xử lý tác nhân với Gemini 4 Argon, 3.8 Flash, 3.6 Flash hoặc 3.5 Flash Lite,
hãy đặt `processing: "agentic"` (Interactions API) hoặc
`media_processing: "AGENTIC"` (GenerateContent API) trên video đầu vào. Nếu không hỗ trợ xử lý theo hướng tác nhân, mô hình sẽ trả về lỗi.

Để biết thêm thông tin, hãy xem bài viết [Tính năng hiểu video dựa trên tác nhân](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#agentic-video-understanding).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
