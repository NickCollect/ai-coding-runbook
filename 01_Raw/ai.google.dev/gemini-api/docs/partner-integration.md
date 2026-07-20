---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=vi
fetched_at: 2026-07-20T04:45:23.043463+00:00
title: "T\u00edch h\u1ee3p v\u1edbi \u0111\u1ed1i t\u00e1c v\u00e0 th\u01b0 vi\u1ec7n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tích hợp với đối tác và thư viện

Hướng dẫn này trình bày các chiến lược kiến trúc để xây dựng thư viện, nền tảng và cổng trên Gemini API. Nội dung này trình bày chi tiết các điểm đánh đổi về kỹ thuật giữa việc sử dụng SDK AI tạo sinh chính thức, Direct API (REST/gRPC) và lớp tương thích OpenAI.

Hãy sử dụng hướng dẫn này nếu bạn đang tạo các công cụ cho nhà phát triển khác, chẳng hạn như khung mã nguồn mở, cổng doanh nghiệp hoặc trình tổng hợp SaaS và cần tối ưu hoá để có sự sạch sẽ về phần phụ thuộc, kích thước gói hoặc tính tương đương về tính năng.

## Tích hợp đối tác là gì?

Đối tác là bất kỳ ai xây dựng mối tích hợp giữa Gemini API và nhà phát triển người dùng cuối. Chúng tôi phân loại các đối tác thành 4 kiểu mẫu. Việc xác định loại nào phù hợp nhất với bạn sẽ giúp bạn chọn đúng đường dẫn tích hợp.

#### Khung hệ sinh thái

- **Bạn là ai:** Người duy trì một khung mã nguồn mở (ví dụ: LangChain, LlamaIndex, Spring AI) hoặc các ứng dụng dành riêng cho ngôn ngữ.
- **Mục tiêu của bạn:** Khả năng tương thích rộng. Bạn muốn thư viện của mình hoạt động trong mọi môi trường mà người dùng chọn mà không gây ra xung đột.

#### Thời gian chạy và nền tảng biên

- **Bạn là ai:** Nền tảng SaaS, Cổng AI hoặc nhà cung cấp cơ sở hạ tầng đám mây (ví dụ: Vercel, Cloudflare, Zapier) nơi quá trình thực thi mã diễn ra trong môi trường bị hạn chế.
- **Mục tiêu của bạn:** Hiệu suất. Bạn cần độ trễ thấp, kích thước gói tối thiểu và khởi động nguội nhanh.

#### Trang web tổng hợp

- **Bạn là ai:** Nền tảng, proxy hoặc "Model Gardens" nội bộ giúp chuẩn hoá quyền truy cập của nhiều nhà cung cấp LLM khác nhau (ví dụ: OpenAI, Anthropic, Google) thành một giao diện duy nhất.
- **Mục tiêu của bạn:** Tính di động và tính đồng nhất.

#### Cổng doanh nghiệp

- **Đối tượng:** Nhóm Kỹ thuật nền tảng nội bộ tại các công ty lớn đang xây dựng "Lộ trình vàng" cho hàng trăm nhà phát triển nội bộ.
- **Mục tiêu của bạn:** Tiêu chuẩn hoá, quản trị và xác thực hợp nhất.

## So sánh nhanh

**Phương pháp hay nhất trên toàn cầu:** Tất cả đối tác phải gửi tiêu đề [`x-goog-api-client` bất kể đường dẫn đã chọn.](#client-id)

| Nếu bạn là... | Đường dẫn được đề xuất | Lợi ích chính | Điểm đánh đổi chính | Phương pháp hay nhất |
| --- | --- | --- | --- | --- |
| **Cổng doanh nghiệp, khung hệ sinh thái** | **[SDK AI tạo sinh của Google](#genai-sdk)** | **Tính tương đồng và tốc độ của Nền tảng tác nhân Gemini Enterprise.** Xử lý sẵn các loại, hoạt động xác thực và tính năng phức tạp (ví dụ: tải tệp lên). Di chuyển liền mạch sang Google Cloud. | **Trọng số phần phụ thuộc.** Các phần phụ thuộc bắc cầu có thể phức tạp và nằm ngoài tầm kiểm soát của bạn. Chỉ hỗ trợ các ngôn ngữ được hỗ trợ (Python/Node/Go/Java). | **Khoá phiên bản.** Ghim các phiên bản SDK trong hình ảnh cơ sở nội bộ để đảm bảo tính ổn định cho các nhóm. |
| **Khung hệ sinh thái, nền tảng biên và đơn vị tổng hợp** | **[Direct API](#rest)**  *(REST / gRPC)* | **Không có phần phụ thuộc.** Bạn kiểm soát ứng dụng HTTP và kích thước gói chính xác. Có toàn quyền sử dụng tất cả các tính năng của API và mô hình. | **Chi phí phát triển cao.** Cấu trúc JSON có thể được lồng sâu và yêu cầu xác thực thủ công cũng như kiểm tra loại nghiêm ngặt. | **Sử dụng thông số kỹ thuật OpenAPI.** Tự động hoá việc tạo kiểu bằng cách sử dụng các thông số kỹ thuật chính thức của chúng tôi thay vì viết chúng theo cách thủ công. |
| **Trình tổng hợp sử dụng các SDK của OpenAI chỉ yêu cầu quy trình làm việc dựa trên văn bản**  *(Tối ưu hoá khả năng tương thích với các phiên bản cũ)* | **[Khả năng tương thích với OpenAI](#openai)** | **Tính di động tức thì.** Sử dụng lại mã hoặc thư viện hiện có tương thích với OpenAI. | **Giới hạn tính năng.** Các tính năng dành riêng cho từng mẫu xe (Video gốc, Lưu vào bộ nhớ đệm) có thể không dùng được. | **Kế hoạch di chuyển.** Hãy sử dụng tính năng này để xác thực nhanh, nhưng hãy lên kế hoạch nâng cấp lên Direct API để sử dụng đầy đủ tính năng API. |

## Tích hợp SDK Google GenAI

Đối với các khung, việc triển khai [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) thường là cách đơn giản nhất, vì có ít dòng mã nhất trong các ngôn ngữ được hỗ trợ.

Đối với các nhóm nền tảng nội bộ, sản phẩm chính mà bạn cung cấp thường là một "lộ trình lý tưởng" cho phép các kỹ sư sản phẩm làm việc nhanh chóng trong khi vẫn tuân thủ các chính sách bảo mật.

**Lợi ích:**

- **Giao diện hợp nhất để di chuyển Nền tảng tác nhân Gemini Enterprise:** Các nhà phát triển nội bộ thường tạo mẫu bằng Khoá API (Gemini API) và triển khai cho Nền tảng tác nhân Gemini Enterprise (IAM) để tuân thủ quy trình sản xuất. SDK này trừu tượng hoá những điểm khác biệt về quy trình xác thực này.
  Tương tự đối với các khung, bạn có thể triển khai một đường dẫn mã và hỗ trợ 2 nhóm người dùng.
- **Các tiện ích phía máy khách:** SDK này bao gồm các tiện ích thành ngữ giúp giảm mã lặp lại cho các tác vụ phức tạp.
  - *Ví dụ:* Hỗ trợ trực tiếp các đối tượng hình ảnh `PIL` trong câu lệnh, gọi hàm tự động và các loại toàn diện.
- **Quyền truy cập vào tính năng từ ngày đầu tiên:** Các tính năng API mới có sẵn tại thời điểm ra mắt thông qua các SDK.
- **Cải thiện khả năng hỗ trợ tạo mã:** Việc cài đặt SDK cục bộ sẽ hiển thị các định nghĩa về loại và chuỗi tài liệu cho các trợ lý lập trình (ví dụ: Cursor, Copilot).
  Bối cảnh này giúp cải thiện độ chính xác của quá trình tạo mã so với việc tạo các yêu cầu REST thô.

**Sự đánh đổi:**

- **Trọng số và độ phức tạp của phần phụ thuộc:** Các SDK có phần phụ thuộc riêng, có thể làm tăng kích thước gói và có khả năng gây ra rủi ro cho chuỗi cung ứng.
- **Phiên bản:** Các tính năng API mới thường được ghim vào các phiên bản SDK tối thiểu.
  Bạn có thể cần gửi bản cập nhật cho người dùng để truy cập vào các tính năng hoặc mô hình mới. Trong một số trường hợp, việc này có thể yêu cầu thay đổi các phần phụ thuộc bắc cầu ảnh hưởng đến người dùng.
- **Giới hạn về giao thức:** Các SDK chỉ hỗ trợ HTTPS cho API chính và WebSocket (WSS) cho Live API. gRPC không được hỗ trợ khi sử dụng các ứng dụng SDK cấp cao.
- **Hỗ trợ ngôn ngữ:** Các SDK hỗ trợ các phiên bản ngôn ngữ *hiện tại*. Nếu cần hỗ trợ các phiên bản EOL (ví dụ: Python 3.9), bạn sẽ cần duy trì một nhánh.

**Phương pháp hay nhất:**

- **Khoá phiên bản:** Ghim phiên bản SDK trong hình ảnh cơ sở nội bộ để đảm bảo tính ổn định cho các nhóm.

## Tích hợp API trực tiếp

Nếu đang phân phối một thư viện cho hàng nghìn nhà phát triển, chạy trong một môi trường bị hạn chế hoặc xây dựng một trình tổng hợp yêu cầu các tính năng mới nhất của Gemini, thì bạn có thể cần tích hợp trực tiếp với API bằng cách sử dụng REST hoặc gRPC.

**Lợi ích:**

- **Toàn quyền truy cập vào tính năng:** Không giống như lớp tương thích của OpenAI, việc sử dụng trực tiếp API này sẽ cho phép các tính năng dành riêng cho Gemini, chẳng hạn như tải lên File API, tạo bộ nhớ đệm nội dung và sử dụng Live API hai chiều.
- **Phụ thuộc tối thiểu:** Trong môi trường mà các phần phụ thuộc nhạy cảm do kích thước hoặc chi phí kiểm tra. Việc sử dụng API trực tiếp thông qua một thư viện chuẩn như `fetch` hoặc thông qua một trình bao bọc như `httpx` sẽ đảm bảo thư viện của bạn vẫn có dung lượng nhỏ.
- **Không phụ thuộc vào ngôn ngữ:** Đây là đường dẫn duy nhất cho những ngôn ngữ không được SDK hỗ trợ, chẳng hạn như Rust, PHP và Ruby, vì không có hạn chế về ngôn ngữ.
- **Hiệu suất:** Direct API không có chi phí khởi động, giúp giảm thiểu các lần khởi động nguội trong các hàm không máy chủ.

**Sự đánh đổi:**

- **Triển khai Nền tảng tác nhân Gemini Enterprise theo cách thủ công:** Không giống như SDK, việc sử dụng trực tiếp API sẽ không tự động xử lý các khác biệt về hoạt động xác thực giữa AI Studio (Khoá API) và Nền tảng tác nhân Gemini Enterprise (IAM). Bạn phải triển khai các trình xử lý uỷ quyền riêng biệt nếu muốn hỗ trợ cả hai môi trường.
- **Không có các loại hoặc trợ giúp gốc:** Bạn sẽ không nhận được các thao tác hoàn thành mã hoặc kiểm tra thời gian biên dịch cho các đối tượng yêu cầu, trừ phi bạn tự triển khai chúng. Không có "trợ lý" nào cho ứng dụng (ví dụ: trình chuyển đổi hàm sang giản đồ), vì vậy, bạn phải tự viết logic này theo cách thủ công.

**Phương pháp hay nhất**

Chúng tôi cung cấp một quy cách có thể đọc được bằng máy mà bạn có thể dùng để tạo các định nghĩa kiểu cho thư viện của mình, giúp bạn không phải viết các định nghĩa này theo cách thủ công. Tải thông số kỹ thuật xuống trong quy trình xây dựng, tạo các loại và gửi mã đã biên dịch.

- **Điểm cuối:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Tích hợp OpenAI SDK

Nếu bạn là một nền tảng ưu tiên giản đồ hợp nhất (OpenAI Chat Completions) hơn các tính năng dành riêng cho mô hình, thì đây là tuyến đường nhanh nhất.

**Lợi ích:**

- **Ít phức tạp:** Bạn thường có thể thêm tính năng hỗ trợ của Gemini bằng cách thay đổi `baseURL` và `apiKey`. Đây là một cách nhanh chóng để tích hợp các hoạt động triển khai "Tự quản lý khoá", thêm tính năng hỗ trợ Gemini mà không cần viết mã mới.
- **Các ràng buộc:** Bạn chỉ nên sử dụng đường dẫn này nếu bị hạn chế sử dụng OpenAI SDK và không cần các tính năng nâng cao của Gemini như File API hoặc thêm hỗ trợ cho các công cụ như Bám sát nguồn bằng Google Tìm kiếm theo cách thủ công.

**Sự đánh đổi:**

- **Giới hạn về tính năng:** Lớp tương thích có những giới hạn đối với các chức năng cốt lõi của Gemini. Các công cụ phía máy chủ hiện có khác nhau giữa các nền tảng và có thể yêu cầu xử lý thủ công để hoạt động với các công cụ Gemini API.
- **Chi phí dịch thuật:** Vì giản đồ OpenAI không ánh xạ 1:1 với cấu trúc của Gemini, nên việc dựa vào lớp tương thích sẽ gây ra một số điểm phức tạp đòi hỏi thêm công việc triển khai để giải quyết, chẳng hạn như ánh xạ công cụ "tìm kiếm" của người dùng với công cụ phù hợp trên nền tảng.
  Nếu bạn cần một lượng lớn trường hợp đặc biệt, thì việc sử dụng một SDK hoặc API chuyên dụng cho mỗi nền tảng có thể mang lại nhiều giá trị hơn.

**Phương pháp hay nhất**

Khi có thể, hãy tích hợp trực tiếp với Gemini API. Tuy nhiên, để có khả năng tương thích tối đa, hãy cân nhắc sử dụng một thư viện nhận biết các nhà cung cấp khác nhau và có thể xử lý việc ánh xạ công cụ và thông báo cho bạn.

## Phương pháp hay nhất cho tất cả các đối tác: nhận dạng khách hàng

Khi gọi Gemini API dưới dạng một nền tảng hoặc thư viện, bạn phải xác định ứng dụng của mình bằng tiêu đề `x-goog-api-client`.

Điều này cho phép Google xác định các phân khúc lưu lượng truy cập cụ thể của bạn và nếu thư viện của bạn đang tạo ra một mẫu lỗi cụ thể, chúng tôi có thể liên hệ để giúp bạn gỡ lỗi.

Sử dụng định dạng `company-product/version` (ví dụ: `acme-framework/1.2.0`).

### Ví dụ về cấu hình triển khai

### SDK AI tạo sinh

Bằng cách cung cấp ứng dụng API, SDK sẽ tự động thêm tiêu đề tuỳ chỉnh của bạn vào các tiêu đề nội bộ.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### SDK OpenAI

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Các bước tiếp theo

- Truy cập vào [phần tổng quan về thư viện](https://ai.google.dev/gemini-api/docs/libraries?hl=vi) để tìm hiểu về các SDK GenAI
- Xem [tài liệu tham khảo API](https://ai.google.dev/api?hl=vi)
- Đọc [hướng dẫn về khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-22 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-22 UTC."],[],[]]
