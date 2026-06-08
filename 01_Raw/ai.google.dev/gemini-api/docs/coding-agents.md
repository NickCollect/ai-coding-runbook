---
source_url: https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi
fetched_at: 2026-06-08T05:35:25.891790+00:00
title: "Thi\u1ebft l\u1eadp tr\u1ee3 l\u00fd l\u1eadp tr\u00ecnh b\u1eb1ng Gemini MCP v\u00e0 Skills \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Thiết lập trợ lý lập trình bằng Gemini MCP và Skills

Trợ lý lập trình AI rất mạnh mẽ nhưng có những hạn chế – dữ liệu huấn luyện bị cắt ở một ngày cụ thể, thiếu các tính năng và thay đổi mới của API. Nếu không có quyền truy cập vào tài liệu dành riêng cho Gemini, các đặc vụ có thể đề xuất các mẫu chung thay vì các phương pháp được tối ưu hoá.

Để trợ lý lập trình của bạn luôn được cập nhật theo Gemini API đang phát triển và cách sử dụng được đề xuất, bạn nên thiết lập **MCP của Gemini Docs** và nâng cao môi trường của bạn bằng **Các kỹ năng của Gemini API**. Mặc dù có thể sử dụng độc lập, nhưng những công cụ này được thiết kế để hoạt động cùng nhau nhằm cung cấp phạm vi bao phủ hoàn chỉnh.

## Kết nối Gemini Docs MCP

Gemini lưu trữ một máy chủ Giao thức ngữ cảnh mô hình (MCP) công khai tại `https://gemini-api-docs-mcp.dev`. Việc kết nối tác nhân lập trình với máy chủ này đảm bảo rằng tất cả các truy vấn đều có quyền truy cập vào các API mới nhất, bản cập nhật mã và ví dụ về cấu hình tối ưu.

Chạy lệnh sau trong thiết bị đầu cuối hoặc thư mục gốc của dự án để cài đặt máy chủ:

```
npx add-mcp "https://gemini-api-docs-mcp.dev"
```

Máy chủ này thêm một hàm `search_documentation` mà tác nhân của bạn có thể dùng để truy xuất các định nghĩa API và mẫu tích hợp theo thời gian thực từ các tệp tài liệu chính thức của Gemini.

## Thêm kỹ năng phát triển API

Các kỹ năng này cung cấp **các quy tắc và phương pháp hay nhất được tích hợp sẵn** (chẳng hạn như thực thi đúng SDK và phiên bản mô hình hiện tại) ngay trong ngữ cảnh của trợ lý. Kỹ năng này hoạt động cùng với dịch vụ MCP của Gemini Docs: Nếu bạn đã cài đặt cả hai, thì kỹ năng này sẽ sử dụng dịch vụ MCP cho tài liệu. Tuy nhiên, ngay cả khi chưa cài đặt MCP, kỹ năng này vẫn sẽ tìm nạp `llms.txt` từ `ai.google.dev` làm phương án dự phòng.

Để cài đặt các kỹ năng này, bạn có thể sử dụng một trong các công cụ được hỗ trợ sau đây. Hướng dẫn cài đặt cho cả hai được cung cấp bên dưới mỗi mô-đun kỹ năng:

- **[skills.sh](https://skills.sh)**: Nên dùng. Tiêu chuẩn mở cho các hành vi của tác nhân di động.
- **[Context7](https://context7.com)**: Được hỗ trợ cho những người dùng đã sử dụng hệ sinh thái Context7.

### gemini-api-dev

Kỹ năng cơ bản để phát triển Gemini cho mục đích chung. Kỹ năng này cung cấp tài liệu và các phương pháp hay nhất cho:

- Định tuyến câu lệnh đến các mô hình hiện tại (ví dụ: Gemini 3.1 Pro/Flash) và tránh các mô hình không dùng nữa
- Câu lệnh đa phương thức, gọi hàm, đầu ra có cấu trúc và các mẫu tích hợp phổ biến

#### Cài đặt bằng skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

#### Cài đặt bằng Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-api-dev
```

### gemini-live-api-dev

Kỹ năng xây dựng các ứng dụng AI đàm thoại theo thời gian thực bằng Gemini Live API. Kỹ năng này cung cấp tài liệu và các phương pháp hay nhất cho:

- Kết nối WebSocket để truyền phát trực tuyến có độ trễ thấp
- Truyền trực tuyến âm thanh, video và văn bản
- Hỗ trợ phát hiện hoạt động bằng giọng nói và tính năng nói chồng lên

#### Cài đặt bằng skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
```

#### Cài đặt bằng Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-live-api-dev
```

### gemini-interactions-api

Kỹ năng xây dựng ứng dụng bằng [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi). Interactions API là một giao diện hợp nhất để tương tác với các mô hình và tác nhân Gemini, được thiết kế cho các ứng dụng dựa trên tác nhân. Kỹ năng này bao gồm:

- Tạo văn bản, trò chuyện nhiều lượt và phát trực tuyến
- Gọi hàm, đầu ra có cấu trúc và tạo hình ảnh
- Chạy ở chế độ nền và các tác nhân Deep Research
- Quản lý trạng thái cuộc trò chuyện phía máy chủ
- Các mẫu SDK Python và TypeScript

#### Cài đặt bằng skills.sh

```
npx skills add google-gemini/gemini-skills --skill gemini-interactions-api --global
```

#### Cài đặt bằng Context7

```
npx ctx7 skills install /google-gemini/gemini-skills gemini-interactions-api
```

## Xác minh cài đặt

Sau khi cài đặt, hãy xác nhận rằng trợ lý lập trình của bạn có thể kết nối với máy chủ MCP của Gemini Docs và sử dụng các kỹ năng đã cài đặt.

### 1. Xác minh hành vi của nhân viên hỗ trợ

Cách đáng tin cậy nhất để xác minh là đặt cho nhân viên hỗ trợ một câu hỏi kỹ thuật về Gemini API.

**Câu lệnh:** "Làm cách nào để sử dụng tính năng lưu vào bộ nhớ đệm theo bối cảnh bằng Gemini API?"

Quá trình thiết lập thành công sẽ:

- **Cung cấp mã chính xác**: Tham chiếu các phương thức cụ thể của Gemini như `cacheContent` hoặc `cachedContents.create` từ các điểm cuối mới nhất.
- **Sử dụng công cụ MCP**: Cho biết công cụ này được kết nối với **Máy chủ MCP của Gemini Docs** hoặc sử dụng công cụ `search_documentation` để tìm nạp dữ liệu.
- **Gọi các kỹ năng đã tải**: Hiện một chỉ báo cho biết "Đang sử dụng kỹ năng: gemini-api-dev" (nếu dựa vào một trình bao bọc phụ).

### 2. Xác minh biểu hiện và công cụ

Nếu tác nhân đưa ra câu trả lời chung chung, hãy sử dụng các lệnh Discovery hoặc Status cụ thể cho môi trường của bạn để xác minh rằng Docs MCP hoặc kỹ năng đã được tải vào bộ nhớ.

| Môi trường | Xác minh MCP | Xác minh kỹ năng |
| --- | --- | --- |
| **Claude Code** | Nhập `/mcp` vào thiết bị đầu cuối để xem các máy chủ đang hoạt động và các công cụ `search_documentation`. | Nhập `/skills` vào thiết bị đầu cuối để liệt kê tất cả các tệp kê khai đang hoạt động. |
| **Cursor** | Chuyển đến phần **Cài đặt > Tính năng > MCP**. Đảm bảo máy chủ ở trạng thái "Đã kết nối". | Mở phần **Cài đặt > Quy tắc**. Xác minh kỹ năng xuất hiện trong phần "Agent Decides" (Nhân viên quyết định). |
| **Antigravity** | Kiểm tra thanh bên **Tuỳ chỉnh > Kết nối** để biết trạng thái MCP. | Nhập `/skills list` hoặc kiểm tra thanh bên **Tuỳ chỉnh > Quy tắc**. |
| **Gemini CLI** | Chạy `gemini mcp list` hoặc sử dụng `/mcp list`. | Chạy lệnh `gemini skills list` hoặc sử dụng lệnh dấu gạch chéo `/skills` trong phiên. |
| **Copilot** | Nhập `@gemini /mcp` để liệt kê các trình kết nối dữ liệu đang hoạt động. | Nhập `@gemini /skills` (hoặc `/skills`) để xem các tiện ích đang hoạt động. |

## Khắc phục sự cố

Nếu chỉ cung cấp thông tin chung hoặc không nhận ra các phương thức dành riêng cho Gemini, hãy kiểm tra những điều sau:

### Nhân viên hỗ trợ không phát hiện thấy kỹ năng

Hầu hết các tác nhân chỉ lập chỉ mục các kỹ năng khi khởi động.

**Khắc phục:** Khởi động lại hoàn toàn IDE (Cursor/VS Code) hoặc thoát rồi mở lại tác nhân dựa trên thiết bị đầu cuối (Claude Code).

### Xung đột toàn cầu so với xung đột cục bộ

Nếu bạn cài đặt bằng cờ `--global`, thì tác nhân có thể bỏ qua cờ này để ưu tiên các quy tắc dành riêng cho dự án.

**Khắc phục:** Thử cài đặt kỹ năng trực tiếp vào thư mục gốc của dự án mà không cần cờ chung:

```
npx skills add google-gemini/gemini-skills --skill gemini-api-dev
```

## Tài nguyên

- [Các kỹ năng của Gemini API trên GitHub](https://github.com/google-gemini/gemini-skills)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi)
- [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/quickstart?hl=vi)
- [Thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
