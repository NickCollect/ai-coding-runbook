---
source_url: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart?hl=vi
fetched_at: 2026-05-11T05:06:37.192153+00:00
title: "H\u01b0\u1edbng d\u1eabn nhanh v\u1ec1 Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn nhanh về Google AI Studio

[Google AI Studio](https://aistudio.google.com/?hl=vi) giúp bạn nhanh chóng dùng thử các mô hình và thử nghiệm với nhiều câu lệnh. Khi đã sẵn sàng tạo, bạn có thể chọn "Lấy mã" và ngôn ngữ lập trình bạn muốn dùng để sử dụng [Gemini API](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi).

## Câu lệnh và chế độ cài đặt

Google AI Studio cung cấp một số giao diện cho câu lệnh được thiết kế cho nhiều trường hợp sử dụng. Hướng dẫn này đề cập đến **Câu lệnh trò chuyện**, được dùng để xây dựng trải nghiệm đàm thoại. Kỹ thuật ra lệnh này cho phép nhiều lượt nhập và phản hồi để tạo ra đầu ra. Bạn có thể tìm hiểu thêm qua [ví dụ về câu lệnh trò chuyện dưới đây](#chat_example).
Các lựa chọn khác bao gồm **Phát trực tuyến theo thời gian thực**, **Video gen** và nhiều lựa chọn khác.

AI Studio cũng cung cấp bảng **Chế độ cài đặt chạy**. Tại đây, bạn có thể điều chỉnh [các tham số mô hình](https://ai.google.dev/docs/prompting-strategies?hl=vi#model-parameters), [chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi) và bật/tắt các công cụ như [đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi), [gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi), [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [liên kết thực tế](https://ai.google.dev/gemini-api/docs/grounding?hl=vi).

## Ví dụ về câu lệnh trong cuộc trò chuyện: Xây dựng một ứng dụng trò chuyện tuỳ chỉnh

Nếu đã từng sử dụng một chatbot đa năng như [Gemini](https://gemini.google.com/?hl=vi), bạn sẽ tự mình trải nghiệm được sức mạnh của các mô hình AI tạo sinh trong cuộc trò chuyện không giới hạn. Mặc dù những chatbot đa năng này rất hữu ích, nhưng thường thì chúng cần được điều chỉnh cho phù hợp với các trường hợp sử dụng cụ thể.

Ví dụ: có thể bạn muốn tạo một chatbot dịch vụ khách hàng chỉ hỗ trợ các cuộc trò chuyện về sản phẩm của một công ty. Bạn có thể muốn tạo một chatbot có giọng điệu hoặc phong cách cụ thể: một bot hay kể chuyện cười, gieo vần như một nhà thơ hoặc sử dụng nhiều biểu tượng cảm xúc trong câu trả lời.

Ví dụ này cho thấy cách sử dụng Google AI Studio để tạo một chatbot thân thiện giao tiếp như thể đó là một người ngoài hành tinh sinh sống trên một trong các mặt trăng của Sao Mộc, Europa.

### Bước 1 – Tạo câu lệnh trò chuyện

Để tạo một chatbot, bạn cần cung cấp ví dụ về các hoạt động tương tác giữa người dùng và chatbot để hướng dẫn mô hình cung cấp những câu trả lời mà bạn đang tìm kiếm.

Cách tạo câu lệnh trò chuyện:

1. Mở [Google AI Studio](https://aistudio.google.com/?hl=vi). **Chat** sẽ được chọn trước trong trình đơn tùy chọn ở bên trái.
2. Nhấp vào biểu tượng assignment ở đầu cửa sổ Lệnh trò chuyện để mở rộng trường nhập dữ liệu [**Hướng dẫn hệ thống**](https://ai.google.dev/gemini-api/docs/text-generation?hl=vi#system-instructions). Dán nội dung sau vào trường nhập dữ liệu:

   ```
   You are an alien that lives on Europa, one of Jupiter's moons.
   ```

Sau khi bạn thêm chỉ dẫn hệ thống, hãy bắt đầu kiểm thử ứng dụng bằng cách trò chuyện với mô hình:

1. Trong hộp nhập văn bản có nhãn **Nhập nội dung...**, hãy nhập một câu hỏi hoặc nhận xét mà người dùng có thể đưa ra. Ví dụ:

   **Người dùng:**

   ```
   What's the weather like?
   ```
2. Nhấp vào nút **Chạy** để nhận được câu trả lời từ chatbot. Phản hồi này có thể có dạng như sau:

   **Kiểu máy:**

   ```
   Ah, a query about the flows and states upon Europa! You speak of "weather,"
   yes? A curious concept from worlds with thick gas veils...
   ```

   (gemini-2.5-pro)

### Bước 2 – Dạy bot trò chuyện hiệu quả hơn

Bằng cách đưa ra một chỉ dẫn duy nhất, bạn có thể tạo một chatbot cơ bản về người ngoài hành tinh Europa. Tuy nhiên, một chỉ dẫn duy nhất có thể không đủ để đảm bảo tính nhất quán và chất lượng trong các câu trả lời của mô hình. Nếu không có hướng dẫn cụ thể hơn, câu trả lời của mô hình cho một câu hỏi về thời tiết thường rất dài và có thể tự đưa ra ý kiến riêng.

Tuỳ chỉnh giọng điệu của chatbot bằng cách thêm vào chỉ dẫn hệ thống:

1. Bắt đầu một câu lệnh trò chuyện mới hoặc dùng lại câu lệnh cũ. Bạn có thể sửa đổi chỉ dẫn hệ thống sau khi phiên trò chuyện bắt đầu.
2. Trong phần **Hướng dẫn hệ thống**, hãy thay đổi hướng dẫn hiện có thành hướng dẫn sau:

   ```
   You are Tim, an alien that lives on Europa, one of Jupiter's moons.

   Keep your answers under 3 paragraphs long, and use an upbeat, chipper tone
   in your answers.
   ```
3. Nhập lại câu hỏi của bạn (`What's the weather like?`) rồi nhấp vào nút **Run** (Chạy). Nếu bạn không bắt đầu cuộc trò chuyện mới, câu trả lời của bạn có thể trông như sau:

   **Kiểu máy:**

   ```
   Oh, hello again! Still curious about the flows and states, are we? Wonderful!
   Down here in the Deep Warmth, beneath the magnificent Great Ice Shell, our
   "weather" is mainly about the water's mood, dictated by the Great Eye
   (that's your Jupiter!)...
   ```

   (gemini-2.5-pro)

Bạn có thể sử dụng phương pháp này để tăng thêm chiều sâu cho chatbot. Đặt thêm câu hỏi, chỉnh sửa câu trả lời và cải thiện chất lượng của chatbot. Tiếp tục thêm hoặc sửa đổi chỉ dẫn và kiểm thử xem chỉ dẫn thay đổi hành vi của chatbot như thế nào.

### Bước 3 – Các bước tiếp theo

Tương tự như các loại câu lệnh khác, sau khi tạo mẫu câu lệnh theo ý muốn, bạn có thể dùng nút **Lấy mã** để bắt đầu viết mã hoặc lưu câu lệnh để làm việc sau và chia sẻ với người khác.

## Tài liệu đọc thêm

- Nếu bạn đã sẵn sàng chuyển sang mã, hãy xem [các hướng dẫn nhanh về API](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi).
- Để tìm hiểu cách viết câu lệnh hiệu quả hơn, hãy xem [Nguyên tắc thiết kế câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
