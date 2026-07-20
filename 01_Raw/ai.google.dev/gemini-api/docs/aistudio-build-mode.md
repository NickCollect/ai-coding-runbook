---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi
fetched_at: 2026-07-20T04:35:25.175035+00:00
title: "T\u1ea1o \u1ee9ng d\u1ee5ng trong Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo ứng dụng trong Google AI Studio

Trang này mô tả cách sử dụng Google AI Studio để nhanh chóng tạo (hoặc "vibe code") và triển khai các ứng dụng thử nghiệm những tính năng mới nhất của Gemini như [Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) và [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi). Google AI Studio hỗ trợ việc tạo **ứng dụng web** bằng thời gian chạy toàn ngăn xếp và **ứng dụng Android gốc** bằng Kotlin và Jetpack Compose – tất cả đều thông qua câu lệnh bằng ngôn ngữ tự nhiên.

## Bắt đầu

Bắt đầu lập trình theo cảm hứng trong [Chế độ tạo](https://aistudio.google.com/apps?hl=vi) của Google AI Studio. Bạn có thể bắt đầu xây dựng theo một số cách:

- **Bắt đầu bằng một câu lệnh**: Ở chế độ Tạo, hãy dùng hộp nhập để nhập nội dung mô tả về những gì bạn muốn tạo. Chọn AI Chips để thêm các tính năng cụ thể như tạo hình ảnh hoặc dữ liệu của Google Maps vào câu lệnh. Bạn thậm chí có thể nói nội dung mình muốn bằng nút chuyển lời nói thành văn bản.
- **Nút "Xem trang đầu tiên tìm được"**: Nếu cần khơi nguồn sáng tạo, hãy dùng nút "Xem trang đầu tiên tìm được" và Gemini sẽ tạo một câu lệnh kèm theo ý tưởng dự án để giúp bạn bắt đầu.
- **Phối lại một dự án trong thư viện**: Mở một dự án trong [Thư viện ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi) rồi chọn **Sao chép ứng dụng**.
- **Nhập một dự án từ GitHub**: Ở chế độ Build (Xây dựng), hãy chọn **Import from GitHub** (Nhập từ GitHub) trong trình đơn **Add files** (Thêm tệp) (+ biểu tượng) trong hộp nhập lời nhắc để nhập mã hiện có.

Sau khi chạy câu lệnh, bạn sẽ thấy mã và các tệp cần thiết được tạo, đồng thời bản xem trước trực tiếp của ứng dụng sẽ xuất hiện ở bên phải.

## Nội dung nào được tạo?

Khi bạn chạy câu lệnh, AI Studio sẽ tạo một ứng dụng hoàn chỉnh. Bạn có thể chọn tạo **ứng dụng web** hoặc **ứng dụng Android gốc** bằng cách sử dụng bộ chọn nền tảng.

Đối với **ứng dụng web** (mặc định), AI Studio sẽ tạo một môi trường toàn ngăn xếp bao gồm:

- **Phía máy khách**: giao diện người dùng web (React là giao diện mặc định).
- **Phía máy chủ**: một thời gian chạy Node.js cho phép thực hiện các lệnh gọi API bảo mật, kết nối cơ sở dữ liệu và sử dụng gói npm.

Đối với **các ứng dụng Android**, AI Studio tạo một dự án Kotlin và Jetpack Compose mà bạn có thể xem trước trong trình mô phỏng dựa trên trình duyệt, cài đặt trên thiết bị thực và xuất bản lên Cửa hàng Play để kiểm thử. [Tìm hiểu thêm về cách tạo ứng dụng Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=vi).

Bạn có thể xem mã được tạo bằng cách chọn thẻ **Mã** trong ngăn xem trước bên phải. **Antigravity Agent** quản lý một cách thông minh nhiều tệp trên ngăn xếp của bạn, đảm bảo các thay đổi được truyền tải chính xác.

### Tác nhân Antigravity

**Antigravity Agent** là chức năng AI chính trong [Google Antigravity](https://antigravity.google?hl=vi) và hiện là các thành phần cốt lõi của bộ công cụ tác nhân, hỗ trợ trải nghiệm Chế độ tạo trong Google AI Studio. Gemini Advanced không chỉ tạo mã đơn giản mà còn duy trì ngữ cảnh của toàn bộ dự án, quản lý nhiều tệp và hiểu các chỉ dẫn phức tạp để tạo các ứng dụng toàn diện, mạnh mẽ.

Các chức năng chính bao gồm:

- **Nhận biết bối cảnh**: duy trì bối cảnh của các câu lệnh trước đó và trạng thái tệp.
- **Quản lý nhiều tệp**: xử lý các phần phụ thuộc trên nhiều tệp.
- **Thực thi đã xác minh**: xác minh nội dung cập nhật mã để giảm hiện tượng ảo giác.

## Khả năng full-stack

Google AI Studio khai thác sức mạnh của hệ sinh thái web hiện đại, cho phép bạn tạo nhiều nguyên mẫu hơn là chỉ nguyên mẫu phía máy khách.

- **Thời gian chạy phía máy chủ và npm**: sử dụng thư viện rộng lớn gồm các gói npm. Tác nhân sẽ tự động xác định và cài đặt các gói khi cần cho ứng dụng của bạn (ví dụ: các thư viện cụ thể để trực quan hoá dữ liệu hoặc ứng dụng API). Bạn cũng có thể yêu cầu các gói cụ thể nếu muốn.
- **Quản lý bí mật**: lưu trữ an toàn các khoá API và bí mật trong trình đơn **Settings** (Cài đặt). Bạn có thể truy cập vào các khoá này trong mã phía máy chủ, giúp bảo vệ chúng khỏi bị lộ ở phía máy khách.
- **Nhiều người chơi**: xây dựng trải nghiệm cộng tác theo thời gian thực ngay trong AI Studio. Thời gian chạy phía máy chủ quản lý trạng thái và các kết nối cần thiết để người dùng tương tác với nhau.
- **Firebase Firestore và Xác thực**: tự động cung cấp và thiết lập Firebase, bao gồm cả cơ sở dữ liệu Firestore (lưu trữ dữ liệu liên tục) và Xác thực Firebase (quy trình đăng nhập, cụ thể là "Đăng nhập bằng Google").
  Tác nhân này xử lý toàn bộ quy trình thiết lập và thậm chí viết mã trong ứng dụng của bạn cho các dịch vụ này.
- **Tích hợp Google Workspace**: Kết nối ứng dụng của bạn với các API của Google Workspace như Gmail, Trang tính, Tài liệu, Drive, Lịch và nhiều API khác. AI Studio sẽ tự động xử lý mọi cấu hình OAuth.

[Tìm hiểu thêm về cách phát triển ứng dụng full-stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi)

### Ứng dụng Android

Bạn cũng có thể tạo ứng dụng Android gốc bằng Kotlin và Jetpack Compose.
Xem trước ứng dụng của bạn trong trình mô phỏng Android dựa trên trình duyệt, cài đặt ứng dụng trên một thiết bị thực bằng ADB trong trình duyệt và xuất bản lên Cửa hàng Play để kiểm thử nội bộ.

[Tìm hiểu thêm về cách tạo ứng dụng Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=vi)

## Tiếp tục xây dựng

Sau khi Google AI Studio tạo mã ban đầu cho ứng dụng của bạn, bạn có thể tiếp tục tinh chỉnh mã đó:

### Tạo trong Google AI Studio

- **Lặp lại với Gemini**: Sử dụng bảng trò chuyện ở **Chế độ tạo** để yêu cầu Gemini sửa đổi, thêm tính năng mới hoặc thay đổi kiểu.
- **Chỉnh sửa mã trực tiếp**: Mở **thẻ Mã** trong bảng xem trước để chỉnh sửa trực tiếp.

### Phát triển bên ngoài

Đối với các quy trình làm việc nâng cao hơn, bạn có thể xuất mã và làm việc trong môi trường mà bạn muốn:

- **Tải xuống và phát triển cục bộ**: Xuất mã đã tạo dưới dạng **tệp ZIP** rồi nhập mã đó vào trình chỉnh sửa mã của bạn.
- **Đẩy lên GitHub**: Tích hợp mã với các quy trình phát triển và triển khai hiện có bằng cách đẩy mã đó lên một **kho lưu trữ GitHub**.

## Các tính năng chính

Google AI Studio có một số tính năng giúp quá trình xây dựng trở nên trực quan và dễ hiểu:

- **Tạo và lặp lại các ứng dụng toàn diện**: Tạo các ứng dụng toàn diện chỉ bằng một câu lệnh và lặp lại thông qua chế độ trò chuyện hoặc **chú thích**. Chế độ chú thích cho phép bạn làm nổi bật mọi phần trên giao diện người dùng của ứng dụng và mô tả thay đổi bạn muốn.
- **Chia sẻ và triển khai ứng dụng**: Bạn có thể chia sẻ các tác phẩm của mình với người khác để cộng tác hoặc giới thiệu tác phẩm. Khi chia sẻ, các lệnh gọi API sẽ được tính vào hạn mức sử dụng của bạn. Nếu bạn sử dụng các mô hình có tính phí, bạn có thể phải trả phí. Sau đó, khi ứng dụng của bạn đã sẵn sàng, hãy triển khai lên Cloud Run.
- **Thư viện ứng dụng**: Thư viện ứng dụng cung cấp một thư viện trực quan về các ý tưởng dự án.
  Bạn có thể khám phá những tính năng của Gemini, xem trước các ứng dụng ngay lập tức và kết hợp chúng để tạo ra ứng dụng của riêng mình.

## Triển khai hoặc lưu trữ ứng dụng

Sau khi ứng dụng đã sẵn sàng, bạn có thể triển khai ứng dụng đó:

- **Cloud Run**: triển khai ứng dụng của bạn dưới dạng một dịch vụ có khả năng mở rộng.
  Bạn có thể phải trả phí cho [Google Cloud Run](https://cloud.google.com/run?hl=vi) dựa trên mức sử dụng. Để tìm hiểu thêm về quy trình triển khai, hãy xem bài viết [Triển khai từ Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=vi).
- **GitHub**: xuất dự án của bạn sang kho lưu trữ GitHub.

## Các điểm hạn chế

Phần này liệt kê các hạn chế hiện tại của chế độ tạo trong Google AI Studio.

### Quản lý khoá API

Khi bạn tạo một ứng dụng mới sử dụng Gemini API, AI Studio sẽ tự động định cấu hình khoá Gemini API của bạn dưới dạng một bí mật trong môi trường phía máy chủ của ứng dụng.
Bạn có thể xem và quản lý khoá này trong bảng điều khiển **Bí mật**.

- **Thiết lập tự động**: `GEMINI_API_KEY` được thiết lập cho bạn – bạn không cần định cấu hình theo cách thủ công để bắt đầu tạo.
- **Chỉ phía máy chủ**: Khoá API được chèn vào thời gian chạy phía máy chủ và không bao giờ được đưa vào mã phía máy khách.
- **Các ứng dụng hiện có**: Đối với những ứng dụng được tạo trước ngày 14 tháng 5 năm 2026, tác nhân sẽ tự động nâng cấp quy trình tích hợp Gemini API của bạn lên phương pháp phía máy chủ được đề xuất vào lần tiếp theo bạn sửa đổi các tính năng Gemini của ứng dụng.

### Triển khai bên ngoài Google AI Studio

- **Cloud Run**: Khi bạn triển khai lên Cloud Run từ AI Studio, khoá API của bạn sẽ được đưa vào một cách an toàn trong môi trường phía máy chủ. Ứng dụng đã triển khai sẽ dùng khoá API của bạn cho tất cả các lệnh gọi Gemini API của người dùng.
- **Tải tệp ZIP xuống**: Nếu tải ứng dụng xuống dưới dạng tệp ZIP để chạy ở nơi khác, bạn sẽ cần thiết lập biến môi trường `GEMINI_API_KEY` trong môi trường lưu trữ. Vì các lệnh gọi Gemini API của ứng dụng được thực hiện từ mã phía máy chủ, nên khoá này không được hiển thị cho người dùng cuối.

### Lỗi khi chia sẻ ứng dụng

Nếu bạn chia sẻ ứng dụng của mình và người dùng cuối gặp phải lỗi **403 Access Restricted** (Truy cập bị hạn chế) khi sử dụng URL được chia sẻ, thì có thể là do một trong những nguyên nhân sau:

- **Tiện ích trên trình duyệt**: các tiện ích bảo vệ quyền riêng tư như Privacy Badger có thể đang chặn ứng dụng. Hãy tắt tiện ích này để tránh gặp lỗi.
- **Vấn đề về bản dựng**: có thể có vấn đề với mã hiện tại. Yêu cầu tác nhân "khắc phục mọi vấn đề về bản dựng bằng mã hiện tại", sau đó chia sẻ lại URL.

## Câu hỏi thường gặp

### Build trong AI Studio là gì?

AI Studio Build là một nền tảng được thiết kế để đưa bạn từ một câu lệnh đơn giản đến một ứng dụng dựa trên AI, sẵn sàng phát hành bằng Gemini. Mô tả nội dung bạn muốn tạo bằng một câu lệnh và Gemini sẽ tạo một ứng dụng cho bạn. Bạn cũng có thể khám phá thư viện của chúng tôi để xem những việc có thể làm với Gemini API và phối lại các ứng dụng để tạo ra ứng dụng của riêng mình.

### Build xử lý khoá Gemini API của tôi như thế nào?

Khi bạn tạo một ứng dụng sử dụng Gemini API, AI Studio sẽ tự động thiết lập khoá Gemini API của bạn dưới dạng một bí mật phía máy chủ. Các lệnh gọi Gemini API của ứng dụng được thực hiện từ mã phía máy chủ bằng khoá này, vì vậy, khoá này sẽ không bao giờ xuất hiện trong trình duyệt. Bạn có thể xem khoá API trong bảng **Bí mật** trong phần Cài đặt.

### Khoá API của tôi có bị lộ khi chia sẻ ứng dụng không?

Không. Khoá API của bạn được lưu trữ dưới dạng một bí mật phía máy chủ và không bao giờ được đưa vào mã phía máy khách. Khi bạn chia sẻ ứng dụng, những người dùng khác có thể sử dụng ứng dụng đó nhưng không thể xem khoá API của bạn.

Khi bạn chia sẻ ứng dụng của mình với người khác, các lệnh gọi API sẽ được tính vào hạn mức sử dụng của bạn.
Nếu bạn sử dụng các mô hình có tính phí, bạn có thể phải trả phí. AI Studio sẽ thông báo cho bạn trong quá trình thiết lập và trước khi bạn chia sẻ nếu ứng dụng của bạn có thể phát sinh chi phí.

### Những người có thể thấy ứng dụng của tôi

Theo mặc định, ứng dụng của bạn sẽ ở chế độ riêng tư. Bạn có thể chia sẻ ứng dụng của mình với những người dùng khác để cho phép họ sử dụng ứng dụng đó. Những người dùng mà bạn chia sẻ ứng dụng có thể xem mã của ứng dụng và phân nhánh mã đó cho mục đích riêng của họ. Nếu bạn chia sẻ ứng dụng của mình với quyền chỉnh sửa, thì những người dùng khác có thể chỉnh sửa mã của ứng dụng.

### Tôi có thể chạy các ứng dụng bên ngoài AI Studio không?

Có. Bạn có thể triển khai ứng dụng của mình lên [Cloud Run](https://cloud.google.com/run?hl=vi) từ AI Studio. Việc này sẽ cung cấp cho ứng dụng của bạn một URL công khai với khoá API được định cấu hình an toàn trong môi trường phía máy chủ. Bạn cũng có thể tải ứng dụng xuống dưới dạng tệp ZIP và lưu trữ ở nơi khác. Bạn sẽ cần đặt biến môi trường `GEMINI_API_KEY` trong môi trường lưu trữ của mình. Vì các lệnh gọi Gemini API được thực hiện từ mã phía máy chủ, nên khoá của bạn vẫn an toàn.

Để tìm hiểu thêm về các lựa chọn triển khai, hãy xem phần [Triển khai từ Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying?hl=vi).

### Tôi có thể phát triển ứng dụng trên thiết bị của mình bằng các công cụ riêng rồi chia sẻ chúng tại đây không?

Chức năng này hiện chưa hoạt động. Chúng tôi rất vui khi có thể hỗ trợ nhiều trường hợp sử dụng hơn cho các ứng dụng trong tương lai. Vui lòng cân nhắc gửi ý kiến phản hồi cho chúng tôi nếu bạn có ý tưởng cụ thể.

### Làm cách nào để sử dụng cơ sở dữ liệu hoặc bộ nhớ khác với các ứng dụng của tôi?

Các ứng dụng AI Studio là những ứng dụng tiêu chuẩn chạy trong một vùng chứa Cloud Run. Bạn có thể sử dụng bất kỳ giải pháp lưu trữ nào mà bạn có thể kết nối qua mạng, miễn là không có tường lửa ngăn chặn quyền truy cập từ dải IP động.

Chúng tôi đang nỗ lực bổ sung tính năng hỗ trợ trực tiếp cho bộ nhớ trong tương lai. Bạn sẽ có thể định cấu hình bộ nhớ trực tiếp trong AI Studio.

### Làm cách nào để truy cập vào micrô, webcam và các API Navigator khác?

Để đảm bảo người xem biết về việc một ứng dụng sử dụng webcam hoặc các thiết bị khác của họ, chúng tôi yêu cầu họ xác nhận thêm trước khi ứng dụng có thể truy cập vào [các API Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) này.
Nhà sáng tạo ứng dụng có thể thêm các yêu cầu cấp quyền này vào tệp `metadata.json` của ứng dụng. Ví dụ:

```
{
  "name": "My app",
  "requestFramePermissions": [
    "microphone",
    "camera",
    "display-capture",
    "geolocation",
    "bluetooth",
    "clipboard-read",
    "serial",
    "usb"
  ]
}
```

Các giá trị được hỗ trợ cho `requestFramePermissions` là một phần trong số các [tính năng tiêu chuẩn chịu sự kiểm soát của chính sách](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Làm cách nào để sử dụng GitHub với các ứng dụng của tôi?

Tính năng tích hợp GitHub của AI Studio cho phép bạn nhập một dự án hiện có từ GitHub để bắt đầu tạo hoặc xuất dự án sang một kho lưu trữ GitHub và xác nhận các thay đổi mới nhất.

### Tôi có thể cấp cho người dùng khác quyền chỉnh sửa ứng dụng của tôi không?

Tính năng này hiện chưa được hỗ trợ nhưng sẽ sớm ra mắt.

### Tại sao ứng dụng của tôi bị gắn cờ do vi phạm chính sách?

Chúng tôi có các hệ thống tự động xem xét ứng dụng để đảm bảo ứng dụng tuân thủ chính sách của chúng tôi. Nếu chúng tôi phát hiện thấy một ứng dụng vi phạm chính sách của chúng tôi, thì ứng dụng đó sẽ bị xoá khỏi AI Studio. Các lỗi vi phạm chính sách có thể bao gồm nhưng không giới hạn ở những lỗi sau:

- Ứng dụng chứa phần mềm độc hại, nội dung lừa đảo hoặc mạo danh
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về hình ảnh xâm hại tình dục trẻ em
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về hành vi quấy rối
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về lời nói hận thù
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về buôn người
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về nội dung khiêu dâm
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về bạo lực và cảnh đẫm máu
- Ứng dụng hiển thị hoặc phân phối nội dung vi phạm chính sách về nội dung gây hại hoặc nguy hiểm

Nếu ứng dụng của bạn bị gắn cờ do vi phạm chính sách và bạn cho rằng đó là do nhầm lẫn, thì bạn có thể gửi đơn kháng nghị. Việc nhiều lần vi phạm chính sách của chúng tôi có thể khiến bạn bị chấm dứt quyền truy cập vào AI Studio.

### Tôi có trách nhiệm gì với tư cách là nhà phát triển ứng dụng?

Xin lưu ý rằng, với tư cách là chủ sở hữu ứng dụng, bạn chịu trách nhiệm về hành vi của ứng dụng và mọi dữ liệu mà ứng dụng xử lý. Nội dung như vậy bao gồm:

- **Tuân thủ pháp luật và tôn trọng quyền của bên thứ ba:** Đảm bảo ứng dụng của bạn tuân thủ tất cả luật và quy định hiện hành, đồng thời không vi phạm quyền của người khác, bao gồm cả quyền sở hữu trí tuệ và quyền riêng tư.
- **Giám sát nội dung:** Việc tuân thủ các điều khoản bổ sung có thể áp dụng cho các dịch vụ khác mà ứng dụng của bạn sử dụng. Ví dụ: [Điều khoản dịch vụ của Google Cloud](https://cloud.google.com/terms?hl=vi) (áp dụng cho Firestore) yêu cầu những khách hàng lưu trữ nội dung của bên thứ ba phải xuất bản các chính sách xác định nội dung bị cấm (ví dụ: nội dung bất hợp pháp) và giám sát sự xuất hiện của nội dung bất hợp pháp đó.
- **Triển khai an toàn:** Triển khai các biện pháp bảo vệ và công cụ kiểm duyệt cần thiết để ngăn chặn việc sử dụng sai mục đích ứng dụng của bạn.

Lưu ý [các hạn chế về việc sử dụng](https://ai.google.dev/gemini-api/terms?hl=vi#use-restrictions) trong Điều khoản dịch vụ.

### Những điều khoản nào áp dụng cho các ứng dụng trong thư viện ứng dụng của AI Studio?

[Điều khoản dịch vụ bổ sung của Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi) áp dụng cho việc sử dụng các ứng dụng xuất hiện trong thư viện ứng dụng của AI Studio, trừ phi có quy định khác.

## Bước tiếp theo

- [Phát triển ứng dụng Full-Stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi) (web)
- [Tạo ứng dụng Android](https://ai.google.dev/gemini-api/docs/aistudio-android?hl=vi)
- Xem các ví dụ trong [Thư viện ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-14 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-14 UTC."],[],[]]
