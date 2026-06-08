---
source_url: https://ai.google.dev/gemini-api/docs/agents?hl=vi
fetched_at: 2026-06-08T05:27:13.551969+00:00
title: "T\u1ed5ng quan v\u1ec1 nh\u00e2n vi\u00ean h\u1ed7 tr\u1ee3 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tổng quan về nhân viên hỗ trợ

Các tác nhân được quản lý trên Gemini API cung cấp cho bạn một bộ công cụ tác nhân có thể định cấu hình. Một lệnh gọi API duy nhất sẽ cung cấp một hộp cát Linux, nơi tác nhân suy luận, thực thi mã, quản lý tệp và duyệt web một cách tự động.

[rocket\_launch

Bắt đầu nhanh

Thực hiện cuộc gọi đầu tiên cho tác nhân, truyền trực tuyến các câu trả lời và tạo tác nhân tuỳ chỉnh.](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi)
[smart\_toy

Tác nhân Antigravity

Các chức năng, công cụ, chế độ nhập đa phương thức và giá của tác nhân mặc định.](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi)
[experiment

Tác nhân trong AI Studio

Sân chơi trực quan để tạo nguyên mẫu cho các tác nhân mà không cần viết mã.](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=vi)

## Các tác nhân được quản lý có sẵn

- **[Tác nhân Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi)**: Tác nhân được quản lý đa năng dựa trên Gemini 3.5 Flash. Chạy mã, quản lý tệp và tìm kiếm trên web trong một hộp cát Linux an toàn do Google lưu trữ. Bạn có thể mở rộng Gemini bằng các hướng dẫn, kỹ năng và dữ liệu của riêng mình để [xây dựng một tác nhân tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi).
- **[Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi)**: Tác nhân nghiên cứu tự động lập kế hoạch, thực hiện và tổng hợp các nhiệm vụ nghiên cứu nhiều bước cho các trường hợp sử dụng như phân tích thị trường, thẩm định và đánh giá tài liệu.

## Bảo mật và các phương pháp hay nhất

Mọi tác nhân đều chạy trong một môi trường hộp cát được cách ly ở cấp hệ điều hành.
Theo mặc định, hộp cát có quyền truy cập không hạn chế vào mạng bên ngoài. Bạn có thể hạn chế hoặc tắt quyền truy cập vào mạng bằng danh sách cho phép.

### Quyền truy cập mạng

Theo mặc định, các môi trường có quyền truy cập mạng đi không hạn chế. Sử dụng danh sách cho phép `network` để hạn chế lưu lượng truy cập đi đến các miền cụ thể hoặc mẫu ký tự đại diện. Để biết thông tin chi tiết về cấu hình, hãy xem [Danh sách cho phép mạng](https://ai.google.dev/gemini-api/docs/aistudio-agents?hl=vi#network_allow_list) (AI Studio) hoặc [Quy tắc mạng](https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi#with_network_rules) (API).

### Công cụ và API bên ngoài

Bạn có thể kết nối các công cụ và API bên ngoài để mở rộng phạm vi hoạt động của trợ lý. Chỉ sử dụng các công cụ từ các nguồn đáng tin cậy và giới hạn quyền ở mức tối thiểu cần thiết. Thông tin đăng nhập có thể được chèn một cách an toàn thông qua các biến đổi tiêu đề proxy truyền dữ liệu ra và không bao giờ bị lộ trong hộp cát. Tác nhân có thể sử dụng mọi thông tin đăng nhập mà tác nhân có quyền truy cập, vì vậy, bạn chỉ nên cung cấp thông tin đăng nhập mà bạn sẵn sàng cấp toàn bộ phạm vi.

- Sử dụng tài khoản dịch vụ hoặc khoá API có đặc quyền tối thiểu.
- Ưu tiên mã thông báo có thời gian tồn tại ngắn hơn khoá có thời gian tồn tại dài.
- Chỉ cung cấp thông tin đăng nhập mà bạn sẵn sàng cấp toàn bộ phạm vi.
- Thay đổi thông tin xác thực theo lịch trình đều đặn.

Để biết thông tin chi tiết về cách định cấu hình các phép biến đổi tiêu đề, hãy xem phần [Thông tin đăng nhập](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#credentials).

### Sự giám sát của con người

Luôn xác minh kết quả (mã được tạo, các phép biến đổi dữ liệu, thay đổi cấu hình) trước khi triển khai, đặc biệt là đối với những tác vụ sửa đổi dữ liệu hoặc tương tác với các hệ thống bên ngoài.

## Giá

Các tác nhân được quản lý sử dụng [mô hình trả tiền theo mức dùng](https://ai.google.dev/gemini-api/docs/pricing?hl=vi#pricing-for-agents) dựa trên số lượng token của mô hình Gemini và mức sử dụng công cụ. Một lượt tương tác có thể kích hoạt nhiều vòng lặp suy luận, thường tiêu thụ từ 100.000 đến 3.000.000 mã thông báo. Bạn sẽ **không bị tính phí** cho tài nguyên điện toán môi trường trong thời gian dùng thử. Xem [chi phí ước tính](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#availability-and-pricing) cho từng phần công việc.

## Giới hạn

| Hạn mức | Mô tả |
| --- | --- |
| **Vòng đời môi trường** | Các môi trường sẽ bị xoá vĩnh viễn sau 7 ngày không hoạt động. |
| **Tắt máy ảo** | Các VM sẽ tắt sau một khoảng thời gian ngắn không hoạt động để tiết kiệm tài nguyên. Yêu cầu tiếp theo sẽ khôi phục trạng thái (với một lần khởi động nguội). |
| **Phần mềm cài đặt sẵn** | Môi trường dựa trên Ubuntu có Python 3.12 và Node.js 22. Để biết thêm thông tin về hình ảnh cơ sở của môi trường, hãy xem phần [Phần mềm được cài đặt sẵn](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#pre-installed-software). |
| **Số nhân viên tối đa** | Bạn có thể có tối đa 1.000 nhân viên hỗ trợ được quản lý. |

## Khung tác nhân

Bạn cũng có thể tạo tác nhân bằng Gemini thông qua các khung và SDK sau:

- [**LangChain / LangGraph**](https://ai.google.dev/gemini-api/docs/langgraph-example?hl=vi): Xây dựng các luồng ứng dụng phức tạp, có trạng thái và hệ thống đa tác nhân bằng cách sử dụng cấu trúc đồ thị.
- [**LlamaIndex**](https://ai.google.dev/gemini-api/docs/llama-index?hl=vi): Kết nối các tác nhân Gemini với dữ liệu riêng tư của bạn để có quy trình làm việc nâng cao bằng RAG.
- [**CrewAI**](https://ai.google.dev/gemini-api/docs/crewai-example?hl=vi): Điều phối các tác nhân AI tự động, cộng tác và đóng vai.
- [**Vercel AI SDK**](https://ai.google.dev/gemini-api/docs/vercel-ai-sdk-example?hl=vi): Xây dựng giao diện người dùng và tác nhân dựa trên AI bằng JavaScript/TypeScript.
- [**Google ADK**](https://google.github.io/adk-docs/get-started/python/): Một khung mã nguồn mở để xây dựng và điều phối các tác nhân AI có khả năng tương tác.
- [**Antigravity SDK**](https://antigravity.google/product/antigravity-sdk?hl=vi): Xây dựng các tác nhân AI tự động bằng cách sử dụng cùng các công cụ, vòng lặp tác nhân và tính năng quản lý bối cảnh hỗ trợ Google Antigravity, có thể lập trình bằng Python.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-20 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-20 UTC."],[],[]]
