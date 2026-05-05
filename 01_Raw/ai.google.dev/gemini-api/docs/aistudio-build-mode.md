---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi
fetched_at: 2026-05-05T20:06:31.635199+00:00
title: "T\u1ea1o \u1ee9ng d\u1ee5ng trong Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo ứng dụng trong Google AI Studio

Trang này mô tả cách sử dụng Google AI Studio để nhanh chóng tạo (hoặc "lập trình theo cảm hứng") và triển khai các ứng dụng kiểm thử các tính năng mới nhất của Gemini như
[Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) và [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=vi). Google AI Studio hiện hỗ trợ **thời gian chạy
toàn ngăn xếp**, cho phép bạn tạo các ứng dụng mạnh mẽ với logic phía máy chủ,
quản lý bí mật an toàn và hỗ trợ gói npm, tất cả thông qua câu lệnh bằng ngôn ngữ tự nhiên.

## Bắt đầu

Bắt đầu lập trình theo cảm hứng trong [Chế độ tạo](https://aistudio.google.com/apps?hl=vi) của Google AI Studio. Bạn có thể bắt đầu tạo theo một số cách:

- **Bắt đầu bằng một câu lệnh**: Trong Chế độ tạo, hãy sử dụng ô nhập dữ liệu để nhập
  nội dung mô tả những gì bạn muốn tạo. Chọn AI Chips để thêm các tính năng cụ thể như tạo hình ảnh hoặc dữ liệu Google Maps vào câu lệnh. Bạn thậm chí có thể nói những gì bạn muốn bằng nút chuyển giọng nói thành văn bản.
- **Nút "Xem trang đầu tiên tìm được"**: Nếu bạn cần một ý tưởng sáng tạo, hãy sử dụng nút "Xem
  trang đầu tiên tìm được" và Gemini sẽ tạo một câu lệnh với ý tưởng dự án
  để giúp bạn bắt đầu.
- **Phối lại một dự án từ thư viện**: Mở một dự án từ [Thư viện
  ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi) rồi chọn **Sao chép ứng dụng**.

Sau khi chạy câu lệnh, bạn sẽ thấy mã và tệp cần thiết được tạo, cùng với bản xem trước trực tiếp của ứng dụng xuất hiện ở bên phải.

## Những gì được tạo?

Khi bạn chạy câu lệnh, AI Studio sẽ tạo một ứng dụng hoàn chỉnh. Theo mặc định, ứng dụng này sẽ tạo một môi trường toàn ngăn xếp có thể bao gồm:

- **Phía máy khách**: giao diện người dùng web (React là mặc định).
- **Phía máy chủ**: thời gian chạy Node.js cho phép thực hiện các lệnh gọi API an toàn,
  kết nối cơ sở dữ liệu và sử dụng gói npm.

Bạn có thể xem mã được tạo bằng cách chọn thẻ **Mã** trong ngăn xem trước ở bên phải. **Tác nhân Antigravity** quản lý thông minh nhiều tệp trên ngăn xếp của bạn, đảm bảo rằng các thay đổi được truyền đúng cách.

### Tác nhân Antigravity

**Tác nhân Antigravity** là chức năng AI chính trong [Google
Antigravity](https://antigravity.google?hl=vi) và hiện là các thành phần cốt lõi của bộ khai thác tác nhân đang hỗ trợ trải nghiệm Chế độ tạo trong Google AI Studio. Tác nhân này không chỉ đơn giản là tạo mã mà còn duy trì bối cảnh của toàn bộ dự án, quản lý nhiều tệp và hiểu các hướng dẫn phức tạp để tạo các ứng dụng full stack mạnh mẽ.

Các chức năng chính bao gồm:

- **Nhận biết bối cảnh**: duy trì bối cảnh của các câu lệnh và trạng thái tệp trước đó.
- **Quản lý nhiều tệp**: xử lý các phần phụ thuộc trên nhiều tệp.
- **Thực thi đã xác minh**: xác minh các bản cập nhật mã để giảm ảo giác.

## Các chức năng toàn ngăn xếp

Google AI Studio khai thác sức mạnh của hệ sinh thái web hiện đại, cho phép bạn tạo nhiều thứ hơn là chỉ nguyên mẫu phía máy khách.

- **Thời gian chạy phía máy chủ và npm**: sử dụng thư viện gói npm rộng lớn. Tác nhân sẽ tự động xác định và cài đặt các gói khi cần cho ứng dụng của bạn (ví dụ: các thư viện cụ thể cho việc trực quan hoá dữ liệu hoặc ứng dụng API). Bạn cũng có thể yêu cầu các gói cụ thể nếu muốn.
- **Quản lý bí mật**: lưu trữ an toàn các khoá API và bí mật trong trình đơn
  **Cài đặt**. Bạn có thể truy cập vào các khoá này trong mã phía máy chủ, giúp bảo vệ chúng khỏi bị lộ ở phía máy khách.
- **Nhiều người chơi**: tạo trải nghiệm cộng tác theo thời gian thực ngay trong
  AI Studio. Thời gian chạy phía máy chủ quản lý trạng thái và các kết nối cần thiết để người dùng tương tác với nhau.
- **Tích hợp Firebase**: tự động cung cấp và thiết lập Firebase,
  bao gồm cơ sở dữ liệu Firestore (lưu trữ dữ liệu liên tục) và
  Xác thực Firebase (quy trình đăng nhập, cụ thể là "Đăng nhập bằng Google").
  Tác nhân xử lý toàn bộ quy trình thiết lập và thậm chí viết mã trong ứng dụng của bạn cho các dịch vụ này.

[Tìm hiểu thêm về cách phát triển ứng dụng toàn ngăn xếp](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi)

## Tiếp tục tạo

Sau khi Google AI Studio tạo mã ban đầu cho ứng dụng, bạn có thể tiếp tục tinh chỉnh mã đó:

### Tạo trong Google AI Studio

- **Lặp lại với Gemini**: Sử dụng bảng điều khiển trò chuyện trong **Chế độ tạo** để hỏi Gemini sửa đổi, thêm tính năng mới hoặc thay đổi kiểu.
- **Chỉnh sửa mã trực tiếp**: Mở **thẻ Mã** trong bảng xem trước để
  chỉnh sửa trực tiếp.

### Phát triển bên ngoài

Đối với các quy trình làm việc nâng cao hơn, bạn có thể xuất mã và làm việc trong môi trường ưa thích:

- **Tải xuống và phát triển cục bộ**: Xuất mã đã tạo dưới dạng **Tệp ZIP** và nhập mã đó vào trình soạn thảo mã.
- **Đẩy lên GitHub**: Tích hợp mã với các quy trình phát triển và triển khai hiện có bằng cách đẩy mã đó lên **kho lưu trữ GitHub**.

## Các tính năng chính

Google AI Studio có một số tính năng giúp quá trình tạo trực quan và dễ hiểu:

- **Tạo và lặp lại trên các ứng dụng toàn ngăn xếp**: Tạo các ứng dụng toàn ngăn xếp chỉ bằng
  một câu lệnh và lặp lại thông qua trò chuyện hoặc **chế độ chú thích**. Chế độ chú thích cho phép bạn đánh dấu bất kỳ phần nào trên giao diện người dùng của ứng dụng và mô tả thay đổi bạn muốn.
- **Chia sẻ và triển khai ứng dụng**: Bạn có thể chia sẻ các tác phẩm của mình với người khác để
  cộng tác hoặc giới thiệu tác phẩm. Sau đó, khi ứng dụng của bạn đã sẵn sàng, hãy triển khai lên Cloud Run.
- **Thư viện ứng dụng**: Thư viện ứng dụng cung cấp một thư viện trực quan về các ý tưởng dự án.
  Bạn có thể duyệt xem những gì có thể thực hiện được với Gemini, xem trước ứng dụng ngay lập tức và phối lại các ứng dụng đó để tạo thành ứng dụng của riêng mình.

## Triển khai hoặc lưu trữ ứng dụng

Sau khi ứng dụng của bạn đã sẵn sàng, bạn có thể triển khai ứng dụng đó:

- **Google Cloud Run**: triển khai ứng dụng của bạn dưới dạng một dịch vụ có thể mở rộng.
  Bạn có thể phải trả phí cho [Google Cloud Run](https://cloud.google.com/run?hl=vi) dựa trên mức sử dụng.
- **GitHub**: xuất dự án của bạn sang kho lưu trữ GitHub.

## Các điểm hạn chế

Phần này liệt kê các điểm hạn chế hiện tại của chế độ tạo trong Google AI Studio.

### Bảo mật khoá API

- **Phía máy khách**: không bao giờ sử dụng trực tiếp khoá API thực trong mã phía máy khách.
- **Phía máy chủ**: sử dụng tính năng Quản lý bí mật để xử lý các khoá nhạy cảm
  một cách an toàn trong thời gian chạy phía máy chủ.

### Triển khai bên ngoài Google AI Studio

- Mặc dù bạn có thể triển khai ứng dụng của mình lên Cloud Run cho một URL công khai, nhưng chế độ thiết lập này sẽ sử dụng khoá API của bạn cho tất cả các lệnh gọi Gemini API của người dùng.
  - Các ứng dụng JavaScript được chạy ở phía máy khách, vì vậy, hãy đảm bảo khoá API chỉ có quyền truy cập tối thiểu để ngăn chặn rò rỉ hoặc sử dụng sai dữ liệu. Ví dụ: người dùng có thể truy cập vào các Cửa hàng tìm kiếm tệp khác từ cùng một dự án thông qua cơ chế này.
- Triển khai bên ngoài an toàn: Để chạy một ứng dụng một cách an toàn bên ngoài AI Studio (ví dụ: sau khi tải tệp zip xuống), bạn phải di chuyển logic sử dụng khoá API sang một thành phần phía máy chủ để ngăn chặn việc lộ khoá cho người dùng cuối. Bạn không cần thực hiện việc này nếu triển khai bằng Cloud Run.
- Cảnh báo về việc lộ khoá: Bạn không nên chỉ thay thế trình giữ chỗ bằng khoá API thực trong môi trường phía máy khách, vì khoá này sẽ hiển thị cho bất kỳ người dùng nào.

### Lỗi khi chia sẻ ứng dụng

Nếu bạn chia sẻ ứng dụng và người dùng cuối gặp lỗi **403 Truy cập bị hạn chế** khi sử dụng URL được chia sẻ, thì có thể là do một trong những nguyên nhân sau:

- **Tiện ích trình duyệt**: các tiện ích bảo mật như Privacy Badger có thể đang chặn ứng dụng. Hãy tắt tiện ích này để tránh gặp lỗi.
- **Vấn đề về bản dựng**: có thể có vấn đề với mã hiện tại. Yêu cầu tác nhân "khắc phục mọi vấn đề về bản dựng với mã hiện tại" rồi chia sẻ lại URL.

## Câu hỏi thường gặp

### Chế độ tạo trong AI Studio là gì?

AI Studio Build là một nền tảng được thiết kế để đưa bạn từ một câu lệnh đơn giản đến một ứng dụng được hỗ trợ bởi AI, sẵn sàng cho hoạt động sản xuất bằng Gemini. Mô tả những gì bạn muốn tạo bằng một câu lệnh và Gemini sẽ tạo một ứng dụng cho bạn. Bạn cũng có thể khám phá thư viện của chúng tôi để xem những gì có thể thực hiện được với Gemini API và phối lại các ứng dụng để tạo thành ứng dụng của riêng mình.

### Tại sao Bản dựng gọi Gemini API từ mã phía máy khách?

Thông thường, bạn nên gọi Gemini API từ phía máy chủ để không lộ khoá API. Tuy nhiên, AI Studio có một proxy Gemini API cho các lệnh gọi phía máy khách, proxy này sẽ đính kèm khoá API mà không lộ khoá đó trong mã. Hiện tại, chúng tôi tạo các lệnh gọi phía máy khách để sử dụng proxy này, vì proxy này giúp đơn giản hoá mã và cho phép bạn chia sẻ ứng dụng của mình với người khác mà không cần cung cấp khoá API.

### Khoá API của tôi có bị lộ khi chia sẻ ứng dụng không?

Không sử dụng khoá API thực trong ứng dụng của bạn. Thay vào đó, hãy sử dụng giá trị trình giữ chỗ.
`process.env.GEMINI_API_KEY` được đặt thành giá trị trình giữ chỗ mà bạn có thể sử dụng.
Khi một người dùng khác sử dụng ứng dụng của bạn, AI Studio sẽ uỷ quyền các lệnh gọi đến Gemini
API, thay thế giá trị trình giữ chỗ bằng *khoá API của người dùng* (không phải của bạn).
Không sử dụng khoá API thực trong ứng dụng của bạn, vì mã này hiển thị cho bất kỳ ai có thể xem ứng dụng của bạn.

### Ai có thể xem ứng dụng của tôi?

Theo mặc định, ứng dụng của bạn là riêng tư. Bạn có thể chia sẻ ứng dụng của mình với những người dùng khác để cho phép họ sử dụng ứng dụng đó. Những người dùng mà bạn chia sẻ ứng dụng có thể xem mã của ứng dụng và phát triển nhánh mã đó cho mục đích riêng của họ. Nếu bạn chia sẻ ứng dụng của mình với quyền chỉnh sửa, thì những người dùng khác có thể chỉnh sửa mã của ứng dụng.

### Tôi có thể chạy ứng dụng bên ngoài AI Studio không?

Bạn có thể triển khai ứng dụng của mình lên [Cloud Run](https://cloud.google.com/run?hl=vi)
từ AI Studio. Việc này sẽ cung cấp cho ứng dụng của bạn một URL công khai. Ứng dụng được triển khai cùng với một máy chủ proxy sẽ giữ khoá API của bạn ở chế độ riêng tư. Tuy nhiên, ứng dụng được triển khai sẽ sử dụng khoá API của bạn cho tất cả các lệnh gọi Gemini API của người dùng. Bạn cũng có thể tải ứng dụng xuống dưới dạng tệp zip. Nếu bạn thay thế giá trị trình giữ chỗ bằng khoá API thực, thì ứng dụng vẫn hoạt động. Tuy nhiên, bạn *không nên* triển khai ứng dụng như thế này, vì bất kỳ người dùng nào cũng có thể xem khoá API. Để
chạy một ứng dụng một cách an toàn bên ngoài AI Studio, bạn cần
[di chuyển một số logic phía máy chủ](https://ai.google.dev/gemini-api/tutorials/web-app?lang=python&hl=vi),
để khoá API không còn bị lộ.

### Tôi có thể phát triển ứng dụng cục bộ bằng các công cụ của riêng mình rồi chia sẻ ứng dụng đó tại đây không?

Chức năng này hiện chưa có. Chúng tôi rất vui khi hỗ trợ thêm các trường hợp sử dụng cho ứng dụng trong tương lai. Vui lòng cân nhắc gửi cho chúng tôi ý kiến phản hồi nếu bạn có điều gì cụ thể trong đầu.

### Làm cách nào để sử dụng cơ sở dữ liệu hoặc bộ nhớ khác với ứng dụng của tôi?

Các ứng dụng AI Studio là các ứng dụng tiêu chuẩn chạy trong vùng chứa Cloud Run. Bạn có thể sử dụng bất kỳ giải pháp lưu trữ nào mà bạn có thể kết nối qua mạng, miễn là không có tường lửa ngăn chặn quyền truy cập từ dải IP động.

Chúng tôi đang nỗ lực bổ sung tính năng hỗ trợ trực tiếp cho bộ nhớ trong tương lai. Bạn sẽ có thể định cấu hình trực tiếp trong AI Studio.

### Làm cách nào để truy cập vào micrô, webcam và các API Navigator khác?

Để đảm bảo người xem biết về việc ứng dụng sử dụng webcam hoặc các thiết bị khác
của họ, chúng tôi yêu cầu xác nhận bổ sung trước khi ứng dụng có thể truy cập
vào các [API Navigator](https://developer.mozilla.org/en-US/docs/Web/API/Navigator) này.
Người tạo ứng dụng có thể thêm các yêu cầu cấp quyền này vào tệp `metadata.json` của ứng dụng. Ví dụ:

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

Các giá trị được hỗ trợ cho `requestFramePermissions` là một tập hợp con của các
tính năng [tiêu chuẩn do chính sách kiểm soát](https://github.com/w3c/webappsec-permissions-policy/blob/main/features.md).

### Làm cách nào để sử dụng GitHub với ứng dụng của tôi?

Tính năng tích hợp GitHub của AI Studio cho phép bạn tạo kho lưu trữ cho công việc và cam kết các thay đổi mới nhất. Chúng tôi hiện không hỗ trợ việc kéo các thay đổi từ xa.

### Tôi có thể cấp quyền chỉnh sửa cho người dùng khác đối với ứng dụng của mình không?

Tính năng này hiện chưa được hỗ trợ nhưng sẽ sớm ra mắt.

### Tại sao ứng dụng của tôi bị gắn cờ do vi phạm chính sách?

Chúng tôi có các hệ thống tự động xem xét ứng dụng để đảm bảo ứng dụng tuân thủ chính sách của chúng tôi. Nếu phát hiện một ứng dụng vi phạm chính sách của chúng tôi, thì ứng dụng đó sẽ bị xoá khỏi AI Studio. Các lỗi vi phạm chính sách có thể bao gồm nhưng không giới hạn ở những lỗi sau:

- Ứng dụng chứa phần mềm độc hại, nội dung lừa đảo hoặc mạo danh
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về hình ảnh xâm hại tình dục trẻ em
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về hành vi quấy rối
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm Chính sách về lời nói hận thù
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về buôn người
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về nội dung khiêu dâm
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về bạo lực và máu me
- Ứng dụng hiển thị hoặc phát tán nội dung vi phạm chính sách về nội dung gây hại hoặc nguy hiểm

Nếu ứng dụng của bạn bị gắn cờ do vi phạm chính sách và bạn cho rằng đó là do nhầm lẫn, thì bạn có thể gửi đơn kháng nghị. Việc vi phạm chính sách của chúng tôi nhiều lần có thể dẫn đến việc bạn bị chấm dứt quyền truy cập vào AI Studio.

### Tôi có trách nhiệm gì với tư cách là nhà phát triển ứng dụng?

Xin nhắc lại rằng với tư cách là chủ sở hữu ứng dụng, bạn chịu trách nhiệm về hành vi và tất cả dữ liệu mà ứng dụng xử lý. Nội dung như vậy bao gồm:

- **Tuân thủ pháp luật và quyền của bên thứ ba:** Đảm bảo ứng dụng của bạn tuân thủ mọi luật và quy định hiện hành, đồng thời không vi phạm quyền của người khác, bao gồm cả quyền sở hữu trí tuệ và quyền riêng tư.
- **Giám sát nội dung:** Bạn có thể phải tuân thủ các điều khoản bổ sung đối với
  các dịch vụ khác mà ứng dụng của bạn sử dụng. Ví dụ:
  [Điều khoản dịch vụ của Google Cloud](https://cloud.google.com/terms?hl=vi),
  áp dụng cho Firestore yêu cầu khách hàng lưu trữ nội dung của bên thứ ba phải
  công bố các chính sách xác định nội dung bị cấm (ví dụ: nội dung bất hợp pháp)
  và giám sát sự hiện diện của nội dung bất hợp pháp đó.
- **Triển khai an toàn:** Triển khai các biện pháp bảo vệ và công cụ kiểm duyệt cần thiết để ngăn chặn việc sử dụng sai ứng dụng của bạn.

Lưu ý về các quy định hạn chế [sử dụng](https://ai.google.dev/gemini-api/terms?hl=vi#use-restrictions)
trong Điều khoản dịch vụ.

### Những điều khoản nào áp dụng cho các ứng dụng trong thư viện ứng dụng trong AI Studio?

Điều khoản dịch vụ bổ sung của [Gemini API](https://ai.google.dev/gemini-api/terms?hl=vi)
áp dụng cho việc sử dụng các ứng dụng có trong thư viện ứng dụng trong AI Studio, trừ phi
có quy định khác.

## Bước tiếp theo

- [Phát triển ứng dụng toàn ngăn xếp](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi)
- Xem các ví dụ trong [Thư viện ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
