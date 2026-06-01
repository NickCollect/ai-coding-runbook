---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=vi
fetched_at: 2026-06-01T06:00:02.590435+00:00
title: "T\u1ed5ng quan v\u1ec1 Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tổng quan về Gemini Live API

Live API cho phép tương tác bằng giọng nói và hình ảnh theo thời gian thực với độ trễ thấp với Gemini. API này xử lý các luồng âm thanh, hình ảnh và văn bản liên tục để đưa ra các câu trả lời bằng giọng nói tức thì, giống như con người, tạo ra trải nghiệm trò chuyện tự nhiên cho người dùng.

![Tổng quan về Live API](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=vi)

[Dùng thử Live API trong Google AI Studiomic](https://aistudio.google.com/live?hl=vi)
[Dùng thử các ứng dụng ví dụ từ GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Sử dụng các kỹ năng của tác nhân mã hoáterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi)

## Trường hợp sử dụng

Bạn có thể sử dụng Live API để xây dựng các tác nhân giọng nói theo thời gian thực cho nhiều ngành, bao gồm:

- **Thương mại điện tử và bán lẻ:** Trợ lý mua sắm đưa ra các đề xuất được cá nhân hoá và các tác nhân hỗ trợ giải quyết vấn đề cho khách hàng.
- **Trò chơi:** Các nhân vật không phải người chơi (NPC) tương tác, trợ lý trợ giúp trong trò chơi và bản dịch theo thời gian thực của nội dung trong trò chơi.
- **Giao diện thế hệ tiếp theo:** Trải nghiệm hỗ trợ giọng nói và video trong lĩnh vực robot, kính thông minh và xe.
- **Chăm sóc sức khoẻ:** Trợ lý sức khoẻ hỗ trợ và giáo dục bệnh nhân.
- **Dịch vụ tài chính:** Cố vấn AI để quản lý tài sản và hướng dẫn đầu tư.
- **Giáo dục:** Người hướng dẫn AI và trợ lý học tập cung cấp hướng dẫn và ý kiến phản hồi được cá nhân hoá.

## Các tính năng chính

Live API cung cấp một bộ tính năng toàn diện để xây dựng các tác nhân giọng nói mạnh mẽ:

- [**Hỗ trợ đa ngôn ngữ**](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#supported-languages):
  Trò chuyện bằng 70 ngôn ngữ được hỗ trợ.
- [**Barge-in**](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#interruptions):
  Người dùng có thể ngắt lời mô hình bất cứ lúc nào để tương tác phản hồi.
- [**Sử dụng công cụ**](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi):
  Tích hợp các công cụ như gọi hàm và Google Tìm kiếm để tương tác linh hoạt.
- [**Bản chép lời âm thanh**](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#audio-transcription):
  Cung cấp bản chép lời dạng văn bản của cả hoạt động đầu vào của người dùng và đầu ra của mô hình.
- [**Âm thanh chủ động**](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#proactive-audio):
  Cho phép bạn kiểm soát thời điểm mô hình phản hồi và trong những ngữ cảnh nào.
- [**Đối thoại cảm xúc**](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#affective-dialog):
  Điều chỉnh kiểu phản hồi và giọng điệu cho phù hợp với biểu cảm đầu vào của người dùng.

## Quy cách kỹ thuật

Bảng sau đây trình bày quy cách kỹ thuật của Live API:

| Danh mục | Thông tin chi tiết |
| --- | --- |
| Phương thức đầu vào | Âm thanh (âm thanh PCM 16 bit thô, 16 kHz, little-endian), hình ảnh (JPEG <= 1 FPS), văn bản |
| Phương thức đầu ra | Âm thanh (âm thanh PCM 16 bit thô, 24 kHz, little-endian) |
| Giao thức | Kết nối WebSocket có trạng thái (WSS) |

## Chọn phương pháp triển khai

Khi tích hợp với Live API, bạn cần chọn một trong các phương pháp triển khai sau:

- **Máy chủ đến máy chủ**: Phần phụ trợ của bạn kết nối với Live API bằng
  [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API). Thông thường, ứng dụng gửi dữ liệu luồng (âm thanh, video, văn bản) đến máy chủ của bạn, sau đó chuyển tiếp dữ liệu đó đến Live API.
- **Ứng dụng đến máy chủ**: Mã giao diện người dùng kết nối trực tiếp với Live API
  sử dụng [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) để truyền trực tuyến dữ liệu, bỏ qua phần phụ trợ.

## Bắt đầu

Chọn hướng dẫn phù hợp với môi trường phát triển của bạn:

Máy chủ đến máy chủ

### [Hướng dẫn về GenAI SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=vi)

Kết nối với Gemini Live API bằng GenAI SDK để xây dựng một ứng dụng đa phương thức theo thời gian thực với phần phụ trợ Python.

Ứng dụng đến máy chủ

### [Hướng dẫn về WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=vi)

Kết nối với Gemini Live API bằng WebSocket để xây dựng một ứng dụng đa phương thức theo thời gian thực với giao diện người dùng JavaScript và mã thông báo tạm thời.

Bộ công cụ phát triển tác nhân

### [Hướng dẫn về ADK](https://google.github.io/adk-docs/streaming/)

Tạo một tác nhân và sử dụng tính năng Truyền trực tuyến của Bộ công cụ phát triển tác nhân (ADK) để bật tính năng giao tiếp bằng giọng nói và video.

## Nền tảng tích hợp của đối tác

Để đơn giản hoá quá trình phát triển các ứng dụng âm thanh và video theo thời gian thực, bạn có thể sử dụng
một nền tảng tích hợp của bên thứ ba hỗ trợ Gemini Live
API qua WebRTC hoặc WebSocket.

[LiveKit

Sử dụng Gemini Live API với các tác nhân LiveKit.](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat của Daily

Tạo một chatbot AI theo thời gian thực bằng Gemini Live và Pipecat.](https://docs.pipecat.ai/guides/features/gemini-live)
[Fishjam của Software Mansion

Tạo các ứng dụng truyền trực tuyến video trực tiếp và âm thanh bằng Fishjam.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Tác nhân Vision của Stream

Xây dựng các ứng dụng AI bằng giọng nói và video theo thời gian thực bằng Tác nhân Vision.](https://visionagents.ai/integrations/gemini)
[Voximplant

Kết nối các cuộc gọi đến và đi với Live API bằng Voximplant.](https://voximplant.com/products/gemini-client)
[Agora

Xây dựng các ứng dụng AI đàm thoại theo thời gian thực bằng Agora.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Bắt đầu sử dụng Gemini Live API bằng Firebase AI Logic.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-29 UTC."],[],[]]
