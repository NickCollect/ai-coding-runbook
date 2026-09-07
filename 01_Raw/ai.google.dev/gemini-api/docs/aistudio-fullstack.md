---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi
fetched_at: 2026-09-07T05:36:09.724206+00:00
title: "Ph\u00e1t tri\u1ec3n c\u00e1c \u1ee9ng d\u1ee5ng to\u00e0n ng\u0103n x\u1ebfp trong Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Phát triển các ứng dụng toàn ngăn xếp trong Google AI Studio

Giờ đây, Google AI Studio hỗ trợ hoạt động phát triển full stack, cho phép bạn tạo các ứng dụng vượt xa nguyên mẫu phía máy khách. Với thời gian chạy phía máy chủ, bạn có thể quản lý các khoá bí mật, kết nối với các API bên ngoài và tạo trải nghiệm nhiều người chơi theo thời gian thực.

## Thời gian chạy phía máy chủ

Giờ đây, các ứng dụng Google AI Studio có thể bao gồm một thành phần phía máy chủ (Node.js).
Điều này cho phép bạn:

- **Thực thi logic phía máy chủ**: Chạy mã không được hiển thị cho máy khách.
- **Truy cập vào các gói npm**: [Antigravity Agent](https://antigravity.google/docs/agent?hl=vi) có thể cài đặt và sử dụng các gói từ hệ sinh thái npm rộng lớn.
- **Xử lý thông tin bí mật**: Sử dụng khoá API và thông tin đăng nhập một cách an toàn.

### Sử dụng các gói npm

Bạn không cần chạy `npm install` theo cách thủ công. Bạn chỉ cần yêu cầu Agent thêm chức năng yêu cầu một gói, và Agent sẽ xử lý việc cài đặt và nhập gói đó.

**Ví dụ**: > "Sử dụng `axios` để tìm nạp dữ liệu từ API bên ngoài."

## Quản lý bí mật một cách an toàn

Với tính năng quản lý mã và khoá bí mật phía máy chủ, giờ đây, bạn có thể tạo các ứng dụng tương tác với thế giới.

### Khoá Gemini API

Khi bạn tạo một ứng dụng mới sử dụng Gemini API, AI Studio sẽ tự động định cấu hình `GEMINI_API_KEY` của bạn dưới dạng một khoá bí mật phía máy chủ mà không cần thiết lập thủ công. Bạn có thể xem khoá này trong bảng điều khiển **Khoá bí mật** trong phần Cài đặt. Các lệnh gọi Gemini API của ứng dụng được thực hiện từ mã phía máy chủ bằng khoá này, vì vậy, khoá này sẽ không bao giờ xuất hiện trong trình duyệt.

### Khoá API của bên thứ ba

Đối với các dịch vụ khác, bạn có thể thêm khoá API theo cách thủ công:

- **API của bên thứ ba**: Kết nối với các dịch vụ như Stripe, SendGrid hoặc API REST tuỳ chỉnh.
- **Cơ sở dữ liệu**: Kết nối với cơ sở dữ liệu bên ngoài (ví dụ: thông qua Supabase, Firebase hoặc MongoDB Atlas) để duy trì dữ liệu ngoài phiên.

Khi tạo các ứng dụng trong thế giới thực, bạn thường cần kết nối với các dịch vụ bên thứ ba (chẳng hạn như Twilio, Slack hoặc cơ sở dữ liệu) yêu cầu khoá API. Bạn có thể thêm khoá theo cách thủ công bằng cách làm theo các bước sau:

1. **Thêm một khoá bí mật**: Chuyển đến trình đơn **Cài đặt** trong Google AI Studio rồi tìm phần Khoá bí mật.
2. **Lưu trữ khoá**: Thêm khoá API hoặc mã thông báo bí mật của bạn vào đây.
3. **Truy cập trong mã**: Agent có thể viết mã phía máy chủ để truy cập vào các bí mật này một cách an toàn (thường là thông qua các biến môi trường), đảm bảo rằng chúng không bao giờ bị lộ cho trình duyệt phía máy khách.

Khi cần, tác nhân cũng sẽ hiển thị một thẻ trong cuộc trò chuyện, nhắc bạn thêm khoá bất cứ khi nào cần một bí mật mới hoặc khi phát hiện thấy một khoá mới trong các biến môi trường của dự án.

### Tích hợp Firebase cho cơ sở dữ liệu và xác thực

Giờ đây, Google AI Studio giúp bạn dễ dàng thêm cơ sở dữ liệu hoặc tính năng xác thực vào ứng dụng thông qua tính năng [tích hợp Firebase](https://firebase.google.com/docs/ai-assistance/ai-studio-integration?hl=vi).
Antigravity Agent có thể tự động cung cấp và thiết lập các dịch vụ sau cho bạn:

- **Cơ sở dữ liệu Firestore**: một cơ sở dữ liệu đám mây NoSQL linh hoạt, có thể mở rộng để lưu trữ và đồng bộ hoá dữ liệu cho quá trình phát triển phía máy khách và phía máy chủ.
- **Xác thực Firebase**: cho phép người dùng đăng nhập an toàn vào ứng dụng của bạn bằng quy trình "Đăng nhập bằng Google".

Bạn chỉ cần yêu cầu tác nhân "thêm cơ sở dữ liệu vào ứng dụng của tôi" hoặc "thiết lập tính năng Đăng nhập bằng Google", tác nhân sẽ xử lý cấu hình cần thiết và tạo mã cho bạn.

Firebase cho phép bạn bắt đầu miễn phí và tuỳ ý mở rộng quy mô bằng tài khoản trả phí bất cứ khi nào bạn cần thêm hạn mức hoặc sử dụng các tính năng trả phí.

## API Google Workspace

Google AI Studio cho phép bạn tạo các ứng dụng kết nối với API Google Workspace, nhờ đó người dùng có thể làm việc với dữ liệu thực của họ: email, bảng tính, tài liệu, sự kiện trên lịch và nhiều dữ liệu khác, tất cả đều nằm trong ứng dụng của bạn. Bạn không cần thiết lập dự án trên đám mây của Google, định cấu hình OAuth hoặc quản lý API theo cách thủ công nữa.

### Cách hoạt động

Bạn có thể thêm một chế độ tích hợp Workspace theo hai cách:

- **Mô tả yêu cầu trong bảng điều khiển trò chuyện**: Bạn chỉ cần cho tác nhân biết những gì bạn muốn trong bảng điều khiển trò chuyện ở dưới cùng. Ví dụ: *"Tạo một trình theo dõi chi phí ghi lại biên nhận vào Google Trang tính của tôi"* hoặc *"Tạo một trang tổng quan tóm tắt các thư chưa đọc của tôi trong Gmail"*.
- **Chọn trong bảng điều khiển tích hợp**: Mở bảng điều khiển **Tích hợp** trong thanh bên bên phải của Chế độ tạo và bật ứng dụng trong Workspace mà bạn muốn kết nối.

Khi bạn thêm một ứng dụng trong Workspace, AI Studio sẽ tự động:

1. Kết nối API Google cần thiết cho ứng dụng của bạn.
2. Tạo mã phía máy chủ để gọi API.
3. Thêm một quy trình "Đăng nhập bằng Google" an toàn để người dùng cuối của ứng dụng có thể uỷ quyền truy cập vào dữ liệu của riêng họ.

### Ứng dụng được hỗ trợ

Các ứng dụng Google Workspace sau đây hiện có:

| Ứng dụng | Những gì bạn có thể tạo |
| --- | --- |
| Lịch Google | Đọc, tạo và quản lý sự kiện cũng như lịch |
| Google Chat | Đọc và tương tác với các cuộc trò chuyện và không gian nhóm |
| Google Tài liệu | Tạo, đọc, cập nhật và định dạng tài liệu |
| Google Drive | Sắp xếp, tìm kiếm và quản lý tệp cũng như thư mục |
| Google Biểu mẫu | Tạo khảo sát, cập nhật câu hỏi và truy xuất câu trả lời |
| Gmail | Đọc, gửi và quản lý nội dung email |
| Google Keep | Quản lý ghi chú, danh sách và tệp đính kèm |
| Google Meet | Lên lịch và quản lý cuộc gọi video |
| Danh bạ | Đồng bộ hoá và quản lý danh bạ |
| Google Trang tính | Đọc, ghi và định dạng dữ liệu bảng tính |
| Google Trang trình bày | Tạo và chỉnh sửa bản trình bày |
| Google Tasks | Tạo, quản lý và sắp xếp việc cần làm |

### Xác thực và quyền

Là nhà phát triển, bạn không cần định cấu hình ứng dụng OAuth, quản lý thông tin đăng nhập hoặc thiết lập dự án trên đám mây của Google. AI Studio sẽ xử lý mọi vấn đề này cho bạn.

Các ứng dụng có tích hợp API Workspace sử dụng tính năng "Đăng nhập bằng Google" để xác thực người dùng cuối. Khi người dùng mở ứng dụng của bạn, họ sẽ được nhắc đăng nhập và cấp các quyền cụ thể mà ứng dụng của bạn cần (ví dụ: quyền chỉ đọc đối với lịch của họ hoặc khả năng chỉnh sửa bảng tính). Ứng dụng của bạn chỉ truy cập vào dữ liệu của người đang sử dụng ứng dụng. Mỗi người dùng sẽ uỷ quyền truy cập vào tài khoản của riêng mình.

### Câu lệnh mẫu

Sau đây là một số ý tưởng để bắt đầu sử dụng các tính năng tích hợp của Workspace:

- *"Xây dựng một ứng dụng đọc Lịch Google của tôi và soạn thảo email chuẩn bị trong Gmail cho mỗi cuộc họp."*
- *"Tạo một công cụ lấy một tài liệu trên Google Tài liệu và tạo một bản trình bày tóm tắt gồm 5 trang trên Google Trang trình bày."*
- *"Tạo một công cụ theo dõi chi phí, trong đó tôi tải biên nhận lên, Gemini trích xuất thông tin chi tiết và ghi lại một hàng mới trong Google Trang tính của tôi."*

### Thiết lập OAuth

Một trường hợp sử dụng chính cho việc quản lý bí mật là thiết lập OAuth để kết nối với các trang web hoặc ứng dụng khác. Khi câu lệnh của bạn có hướng dẫn về cách kết nối với một ứng dụng bên thứ ba yêu cầu xác thực OAuth, thì trợ lý sẽ cung cấp hướng dẫn về cách thiết lập OAuth cho ứng dụng đó. Các hướng dẫn này sẽ bao gồm những URL gọi lại cần thiết để định cấu hình Ứng dụng OAuth.
Bạn cũng có thể tìm thấy các URL gọi lại trong mục **Tích hợp** trong bảng Cài đặt.

## Tạo trải nghiệm nhiều người chơi

Thời gian chạy toàn ngăn xếp cho phép các tính năng cộng tác theo thời gian thực.

- **Trạng thái theo thời gian thực**: Bạn có thể yêu cầu Trợ lý tạo các tính năng như "một cuộc trò chuyện trực tiếp", "một bảng trắng cộng tác" hoặc "một trò chơi nhiều người chơi".
- **Phiên được đồng bộ hoá**: Máy chủ quản lý trạng thái, cho phép nhiều người dùng tương tác với cùng một phiên bản ứng dụng theo thời gian thực.

**Ví dụ về câu lệnh**: > "Hãy biến đây thành một trò chơi nhiều người chơi, trong đó người chơi có thể nhìn thấy con trỏ của nhau."

### Mẹo kiểm thử ứng dụng nhiều người chơi

Bạn có thể kiểm thử chế độ nhiều người chơi theo 2 cách trước khi triển khai ứng dụng.

1. Mở ứng dụng của bạn ở chế độ Tạo của Google AI Studio trong nhiều thẻ. Khi phát triển ở chế độ Build, ứng dụng của bạn sẽ nằm trong một vùng chứa dành cho nhà phát triển. Việc mở ứng dụng ở nhiều thẻ sẽ cho phép bạn mô phỏng nhiều người chơi sử dụng ứng dụng của mình.
2. Chia sẻ ứng dụng với người khác bằng trình đơn **Chia sẻ** ở trên cùng bên phải, sau đó sử dụng **URL được chia sẻ** trong thẻ **Tích hợp** của trình đơn **Chia sẻ** để sử dụng ứng dụng với những người chơi mà bạn đã chia sẻ ứng dụng.

## Các phương pháp hay nhất

- **Lệnh gọi Gemini API**: `GEMINI_API_KEY` của bạn sẽ tự động được định cấu hình làm khoá bí mật phía máy chủ. Gọi Gemini API từ mã phía máy chủ bằng khoá này. Bạn có thể xem khoá này trong bảng điều khiển **Secrets** (Khoá bí mật).
- **Bảo mật bí mật**: Luôn sử dụng Trình quản lý bí mật cho các khoá nhạy cảm.
  Đừng bao giờ mã hoá cứng các giá trị này trong tệp.
- **Phân tách các mối lo ngại**: Giữ logic giao diện người dùng trong khung phía máy khách (React/Angular) và logic nghiệp vụ/xử lý dữ liệu ở phía máy chủ.
- **Xử lý lỗi**: Đảm bảo mã phía máy chủ của bạn xử lý lỗi một cách mạnh mẽ từ các lệnh gọi API bên ngoài để ngăn ứng dụng gặp sự cố.

## Tiếp theo là gì?

- [Tạo ứng dụng trong Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi)
- [Triển khai từ Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=vi)
- [App Gallery](https://aistudio.google.com/apps?source=showcase&hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-08-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-08-19 UTC."],[],[]]
