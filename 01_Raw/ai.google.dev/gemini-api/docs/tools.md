---
source_url: https://ai.google.dev/gemini-api/docs/tools?hl=vi
fetched_at: 2026-05-05T20:46:11.898540+00:00
title: "S\u1eed d\u1ee5ng c\u00f4ng c\u1ee5 v\u1edbi Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Sử dụng công cụ với Gemini API

Các công cụ mở rộng khả năng của mô hình Gemini, cho phép mô hình thực hiện hành động trong thế giới thực, truy cập thông tin theo thời gian thực và thực hiện các tác vụ tính toán phức tạp. Mô hình có thể sử dụng các công cụ trong cả hoạt động tương tác yêu cầu-phản hồi tiêu chuẩn và
phiên phát trực tuyến theo thời gian thực bằng [Live API](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi).

Các công cụ là những khả năng cụ thể (như Google Tìm kiếm hoặc Thực thi mã) mà mô hình có thể sử dụng để trả lời truy vấn. Gemini API cung cấp một bộ công cụ tích hợp sẵn và được quản lý đầy đủ
, hoặc bạn có thể xác định các công cụ tuỳ chỉnh bằng cách sử dụng tính năng [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

Để xây dựng hệ thống nhiều bước và hướng đến mục tiêu, hãy xem bài viết [Tổng quan về tác nhân](https://ai.google.dev/gemini-api/docs/agents?hl=vi).

## Các công cụ tích hợp sẵn có

| Công cụ | Mô tả | Trường hợp sử dụng |
| --- | --- | --- |
| [Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) | Dựa vào các sự kiện và thông tin thực tế hiện tại trên web để giảm thiểu tình trạng ảo giác. | \- Trả lời câu hỏi về các sự kiện gần đây   \- Xác minh thông tin thực tế bằng nhiều nguồn |
| [Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi) | Xây dựng trợ lý nhận biết vị trí có thể tìm địa điểm, chỉ đường và cung cấp bối cảnh địa phương phong phú. | \- Lên kế hoạch cho hành trình du lịch có nhiều điểm dừng   \- Tìm doanh nghiệp địa phương dựa trên tiêu chí của người dùng |
| [Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) | Cho phép mô hình viết và chạy mã Python để giải các bài toán hoặc xử lý dữ liệu một cách chính xác. | \- Giải các phương trình toán học phức tạp   \- Xử lý và phân tích dữ liệu văn bản một cách chính xác |
| [Ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) | Hướng dẫn mô hình đọc và phân tích nội dung từ các trang web hoặc tài liệu cụ thể. | \- Trả lời câu hỏi dựa trên các URL hoặc tài liệu cụ thể   \- Truy xuất thông tin trên nhiều trang web |
| [Sử dụng máy tính (Bản dùng thử)](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi) | Cho phép Gemini xem màn hình và tạo hành động để tương tác với giao diện người dùng của trình duyệt web (Thực thi phía máy khách). | \- Tự động hoá các quy trình làm việc lặp đi lặp lại trên web   \- Kiểm thử giao diện người dùng của ứng dụng web |
| [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) | Lập chỉ mục và tìm kiếm tài liệu của riêng bạn để bật tính năng Tạo sinh tăng cường truy xuất (RAG). | - Tìm kiếm hướng dẫn kỹ thuật   - Trả lời câu hỏi dựa trên dữ liệu độc quyền |

Hãy xem [trang Giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#pricing_for_tools) để biết thông tin chi tiết
về chi phí liên quan đến các công cụ cụ thể.

## Cách thực thi công cụ

Các công cụ cho phép mô hình yêu cầu hành động trong cuộc trò chuyện. Quy trình này khác nhau tuỳ thuộc vào việc công cụ đó là công cụ tích hợp sẵn (do Google quản lý) hay công cụ tuỳ chỉnh (do bạn quản lý).

### Quy trình công cụ tích hợp sẵn

Đối với các công cụ tích hợp sẵn (Google Tìm kiếm, Google Maps, Ngữ cảnh URL, Tìm kiếm tệp, Thực thi mã), toàn bộ quy trình diễn ra trong một lệnh gọi API:

1. **Bạn** gửi một câu lệnh: "Căn bậc hai của giá cổ phiếu mới nhất của GOOG là bao nhiêu?"
2. **Gemini** quyết định cần các công cụ và thực thi các công cụ đó trên máy chủ của Google (ví dụ: tìm kiếm giá cổ phiếu, sau đó chạy mã Python để tính căn bậc hai).
3. **Gemini** gửi lại câu trả lời cuối cùng dựa trên kết quả của công cụ.

### Quy trình công cụ tuỳ chỉnh (Gọi hàm)

Đối với các công cụ tuỳ chỉnh và tính năng Sử dụng máy tính, ứng dụng của bạn sẽ xử lý quá trình thực thi:

1. **Bạn** gửi một câu lệnh cùng với các khai báo hàm (công cụ).
2. **Gemini** có thể gửi lại JSON có cấu trúc để gọi một hàm cụ thể
   (ví dụ: `{"name": "get_order_status", "args": {"order_id": "123"}}`),
   luôn có một `id` duy nhất.
3. **Bạn** thực thi hàm trong ứng dụng hoặc môi trường của mình.
4. **Bạn** gửi kết quả của hàm (có cùng `id` với lệnh gọi hàm) trở lại Gemini.
5. **Gemini** sử dụng kết quả này để tạo câu trả lời cuối cùng hoặc một lệnh gọi công cụ khác.

Tìm hiểu thêm trong [hướng dẫn Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).

### Kết hợp quy trình công cụ tích hợp sẵn và công cụ tuỳ chỉnh

[Đối với các yêu cầu kết hợp công cụ tích hợp sẵn và công cụ tuỳ chỉnh (lệnh gọi hàm), mô hình sẽ sử dụng tính năng lưu thông ngữ cảnh công cụ để điều phối quá trình thực thi trên nhiều môi trường:](https://ai.google.dev/gemini-api/docs/toold-combination?hl=vi)

1. **Bạn** gửi một câu lệnh và khai báo các công cụ tích hợp sẵn cũng như các hàm tuỳ chỉnh mà bạn muốn bật, đồng thời đặt một cờ để bật tính năng hỗ trợ kết hợp.
2. **Gemini** thực thi các công cụ tích hợp sẵn và nhường quyền cho người dùng nếu có bất kỳ lệnh gọi hàm phía máy khách nào được tạo (lệnh gọi nào thực thi trước sẽ phụ thuộc vào câu lệnh và những gì mô hình quyết định). Mô hình sẽ gửi lại một phản hồi có:
   - Xác nhận lệnh gọi công cụ
   - Kết quả của phản hồi công cụ (kết quả này có thể xuất hiện sau JSON nếu mô hình tạo ra 2 lệnh gọi hàm song song)
   - JSON có cấu trúc để gọi hàm
   - Chữ ký ý tưởng được mã hoá để giữ nguyên ngữ cảnh
3. **Bạn** thực thi hàm trong ứng dụng hoặc môi trường của mình.
4. **Bạn** trả về tất cả các phần của phản hồi của Gemini, cộng với kết quả lệnh gọi hàm.
5. **Gemini** tạo phản hồi cuối cùng bằng cách sử dụng tất cả ngữ cảnh kết hợp.

Hãy đọc [hướng dẫn Kết hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi) để tìm hiểu cách bật tính năng hỗ trợ kết hợp công cụ tích hợp sẵn và công cụ tuỳ chỉnh, cũng như các ví dụ về lưu thông ngữ cảnh.

## Đầu ra có cấu trúc so với gọi hàm

Gemini cung cấp 2 phương thức để tạo đầu ra có cấu trúc. Hãy sử dụng tính năng [Gọi
hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi) khi mô hình cần thực hiện một
bước trung gian bằng cách kết nối với các công cụ hoặc hệ thống dữ liệu của riêng bạn. Hãy sử dụng
[Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) khi bạn cần mô hình tuân thủ một giản đồ cụ thể trong phản hồi cuối cùng, chẳng hạn như để kết xuất
giao diện người dùng tuỳ chỉnh.

## Đầu ra có cấu trúc với các công cụ

Bạn có thể kết hợp [Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi) với
các công cụ tích hợp sẵn để đảm bảo rằng các phản hồi của mô hình dựa trên dữ liệu hoặc
tính toán bên ngoài vẫn tuân thủ một giản đồ nghiêm ngặt.

Hãy xem bài viết [Đầu ra có cấu trúc với các công cụ](https://ai.google.dev/gemini-api/docs/structured-output?example=recipe&hl=vi#structured_outputs_with_tools)
để xem các đoạn mã ví dụ.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
