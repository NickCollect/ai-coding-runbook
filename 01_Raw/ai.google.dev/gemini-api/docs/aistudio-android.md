---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=vi
fetched_at: 2026-06-22T06:30:43.420681+00:00
title: "T\u1ea1o \u1ee9ng d\u1ee5ng Android trong Google AI Studio \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo ứng dụng Android trong Google AI Studio

Google AI Studio cho phép bạn tạo các ứng dụng Android gốc từ một câu lệnh bằng ngôn ngữ tự nhiên. Mô tả ứng dụng bạn muốn, và [Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi#antigravity-agent) sẽ tạo một dự án hoàn chỉnh bằng Kotlin và [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=vi). Trên trình duyệt, bạn có thể xem trước ứng dụng trong trình mô phỏng Android dựa trên trình duyệt, cài đặt ứng dụng trên một thiết bị thực và xuất bản ứng dụng để kiểm thử.

## Bắt đầu

Cách bắt đầu tạo một ứng dụng Android:

1. Chuyển đến [Chế độ xây dựng](https://aistudio.google.com/apps?hl=vi) trong Google AI Studio bằng bảng điều hướng bên trái.
2. Chọn **Android** trong bộ chọn nền tảng.
3. Nhập một câu lệnh mô tả ứng dụng bạn muốn tạo (ví dụ: *"Tạo một bảng theo dõi nhiệm vụ hằng ngày có bộ nhớ cục bộ"* hoặc *"Tạo một Máy tính đơn giản"*).
4. Tác nhân sẽ tạo dự án và chạy dự án đó trong trình mô phỏng Android dựa trên trình duyệt.

Sau đó, bạn có thể lặp lại quy trình này trên ứng dụng bằng cách sử dụng bảng trò chuyện, giống như trải nghiệm trên web. Tác nhân này quản lý tất cả các tệp trong dự án Android của bạn và truyền các thay đổi trên toàn bộ cơ sở mã.

## Trình mô phỏng Android dựa trên trình duyệt

Trình mô phỏng Android chạy hoàn toàn trên đám mây và truyền trực tuyến đến trình duyệt của bạn.
Bạn không cần cài đặt Android SDK, Android Studio hoặc trình mô phỏng cục bộ.

Trình mô phỏng này cung cấp:

- **Mô phỏng thiết bị giống Pixel**: nhấn, cuộn và tương tác với ứng dụng của bạn giống như trên một thiết bị thực.
- **Hỗ trợ xoay**: chuyển đổi giữa hướng dọc và hướng ngang.
- **Xem trước trực tiếp**: khi tác nhân thực hiện các thay đổi về mã, ứng dụng sẽ tạo lại và trình mô phỏng sẽ tự động làm mới.

### Giới hạn của trình mô phỏng

Trình mô phỏng dựa trên trình duyệt không hỗ trợ tất cả các tính năng phần cứng. Trình mô phỏng không có các tính năng sau:

- Chụp ảnh và quay video bằng camera
- NFC và Bluetooth
- GPS (vị trí được mô phỏng)
- Dịch vụ Google Play (Đăng nhập bằng Google, Maps và các tính năng khác của Dịch vụ Play hoạt động trên thiết bị thực nhưng không hoạt động trong trình mô phỏng)

## Cài đặt trên thiết bị có ADB

Bạn có thể cài đặt trực tiếp APK đã tạo trên một thiết bị Android thực được kết nối với máy tính bằng USB. Tính năng này sử dụng [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=vi) để giao tiếp với thiết bị của bạn thông qua trình duyệt. Không cần cài đặt ADB cục bộ.

### Điều kiện tiên quyết

- Trình duyệt Chrome hoặc Edge hỗ trợ WebUSB.
- Một thiết bị Android đã bật [Tuỳ chọn cho nhà phát triển và Gỡ lỗi qua USB](https://developer.android.com/studio/debug/dev-options?hl=vi).
- Cáp USB kết nối thiết bị với máy tính.

### Cài đặt ứng dụng trên thiết bị

1. Nhấp vào **Cài đặt trên thiết bị** trong bảng điều khiển xem trước.
2. Chọn thiết bị Android của bạn trong trình chọn thiết bị USB của trình duyệt.
3. Tệp APK sẽ được chuyển và cài đặt trên thiết bị của bạn.
4. Ứng dụng sẽ tự động chạy.

## Phát hành lên Cửa hàng Play

Bạn có thể xuất bản ứng dụng Android của mình lên kênh kiểm thử nội bộ của [Google Play Console](https://play.google.com/console?hl=vi). Kênh này cho phép bạn phân phối ứng dụng cho tối đa 100 người kiểm thử.

### Điều kiện tiên quyết

- [Tài khoản nhà phát triển trên Google Play](https://play.google.com/console/signup?hl=vi) (bạn phải trả phí đăng ký một lần là 25 USD).
- Hồ sơ nhà phát triển đã hoàn tất trong Play Console.

### Phát hành ứng dụng

1. Mở **Settings > Publish** (Cài đặt > Xuất bản) trong Google AI Studio.
2. Nhấp vào **Xuất bản lên Cửa hàng Play**.
3. Xác thực bằng tài khoản nhà phát triển trên Google Play của bạn.
4. AI Studio ký APK, tạo trang thông tin trên Cửa hàng Play (hoặc tải phiên bản mới lên) và xuất bản lên kênh kiểm thử nội bộ.
5. Bạn sẽ nhận được một đường liên kết để chia sẻ với người kiểm thử.

AI Studio tự động quản lý việc ký APK bằng kho khoá được quản lý. Bạn có thể tuỳ chỉnh trang thông tin ứng dụng (biểu tượng, ảnh chụp màn hình, nội dung mô tả) sau này trong Play Console.

## Nội dung được tạo

Khi bạn tạo một ứng dụng Android, tác nhân sẽ tạo một dự án tiêu chuẩn dựa trên Gradle có cấu trúc như sau:

- **Cấu hình bản dựng**: Các tệp `build.gradle.kts` (cấp dự án và cấp ứng dụng) bằng Kotlin DSL.
- **Lớp giao diện người dùng**: Các thành phần [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=vi) có giao diện [Material 3](https://m3.material.io/).
- **Cấu trúc**: cấu trúc một hoạt động với ViewModel và các lớp dữ liệu.
- **Tài nguyên**: `AndroidManifest.xml`, các đối tượng có thể vẽ, chuỗi và các tài nguyên khác của Android.

Tác nhân này tự động quản lý các phần phụ thuộc Gradle, thêm các gói từ kho lưu trữ Maven và Google khi cần.

Bạn có thể xem và chỉnh sửa mã được tạo bằng thẻ **Code** (Mã) trong bảng xem trước. Để tiếp tục phát triển trong Android Studio, hãy tải dự án xuống dưới dạng **tệp ZIP**.

## Các điểm hạn chế

Hoạt động tạo ứng dụng Android trong AI Studio có những hạn chế sau:

### Các hạn chế về nền tảng

- **Chỉ phía máy khách**: Các ứng dụng Android không có thành phần phía máy chủ.
  Các tính năng yêu cầu thời gian chạy máy chủ (quản lý bí mật, nhiều người chơi, Firebase, API Google Workspace) không dùng được.
- **Cấu trúc một hoạt động**: chỉ hỗ trợ các dự án một hoạt động, một mô-đun.
- **Chỉ Jetpack Compose**: ứng dụng sử dụng Kotlin và Jetpack Compose. Không hỗ trợ bố cục Java và XML.
- **Không có NDK hoặc mã gốc**: Mã C và C++ không được hỗ trợ.
- **Không có Wear OS hoặc Android TV**: chỉ hỗ trợ hệ số hình dạng điện thoại và máy tính bảng.

### Hạn chế khi xuất

- **Chỉ tải tệp ZIP xuống**: bạn có thể tải dự án xuống dưới dạng tệp ZIP. Tính năng xuất sang GitHub hiện chưa được cung cấp cho các dự án Android.

## Bước tiếp theo

- [Tạo ứng dụng trong Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=vi)
- [Phát triển ứng dụng Full-Stack](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=vi) (web)
- Xem các ví dụ trong [Thư viện ứng dụng](https://aistudio.google.com/apps?source=showcase&hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
