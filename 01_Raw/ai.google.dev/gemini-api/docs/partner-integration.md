---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=vi
fetched_at: 2026-05-05T13:27:48.944690+00:00
title: "T\u00edch h\u1ee3p v\u1edbi \u0111\u1ed1i t\u00e1c v\u00e0 th\u01b0 vi\u1ec7n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/Tính năng Nghiên cứu chuyên sâu của Gemini) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

- [Trang chủ](https://ai.google.dev/gemini-api/docs/Trang chủ)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/Tài liệu)

Gửi ý kiến phản hồi

# Tích hợp với đối tác và thư viện

Hướng dẫn này trình bày các chiến lược về kiến trúc để xây dựng thư viện, nền tảng và cổng trên Gemini API. Hướng dẫn này trình bày chi tiết các điểm đánh đổi về kỹ thuật giữa việc sử dụng SDK GenAI chính thức, API Trực tiếp (REST/gRPC) và lớp tương thích OpenAI.

Hãy sử dụng hướng dẫn này nếu bạn đang xây dựng các công cụ cho nhà phát triển khác, chẳng hạn như khung nguồn mở, cổng doanh nghiệp hoặc trang web tổng hợp SaaS và cần tối ưu hoá để đảm bảo tính hợp vệ sinh của phần phụ thuộc, kích thước gói hoặc tính tương đương của tính năng.

## Tích hợp đối tác là gì?

Đối tác là bất kỳ ai xây dựng mối quan hệ tích hợp giữa Gemini API và nhà phát triển người dùng cuối. Chúng tôi phân loại đối tác thành 4 nguyên mẫu. Việc xác định nguyên mẫu nào phù hợp nhất với bạn sẽ giúp bạn chọn đúng đường dẫn tích hợp.

#### Khung hệ sinh thái

- **Bạn là ai:** Người duy trì khung nguồn mở (ví dụ: LangChain, LlamaIndex, Spring AI) hoặc ứng dụng cụ thể theo ngôn ngữ.
- **Mục tiêu của bạn:** Khả năng tương thích rộng. Bạn muốn thư viện của mình hoạt động trong mọi môi trường mà người dùng chọn mà không gây ra xung đột.

#### Nền tảng thời gian chạy và nền tảng biên

- **Bạn là ai:** Nền tảng SaaS, Cổng AI hoặc nhà cung cấp cơ sở hạ tầng đám mây (ví dụ: Vercel, Cloudflare, Zapier) nơi quá trình thực thi mã diễn ra trong các môi trường bị hạn chế.
- **Mục tiêu của bạn:** Hiệu suất. Bạn cần độ trễ thấp, kích thước gói tối thiểu và thời gian khởi động nguội nhanh.

#### Trang web tổng hợp

- **Bạn là ai:** Nền tảng, proxy hoặc "Model Gardens" nội bộ giúp chuẩn hoá quyền truy cập trên nhiều nhà cung cấp LLM (ví dụ: OpenAI, Anthropic, Google) vào một giao diện duy nhất.
- **Mục tiêu của bạn:** Tính di động và tính đồng nhất.

#### Cổng doanh nghiệp

- **Bạn là ai:** Nhóm Kỹ thuật nền tảng nội bộ tại các công ty lớn xây dựng "Golden Paths" cho hàng trăm nhà phát triển nội bộ.
- **Mục tiêu của bạn:** Tiêu chuẩn hoá, quản trị và xác thực hợp nhất.

## So sánh nhanh

**Phương pháp hay nhất trên toàn cầu:** Tất cả đối tác phải gửi [`x-goog-api-client`
tiêu đề](https://ai.google.dev/gemini-api/docs/`x-goog-api-client`tiêu đề) bất kể đường dẫn đã chọn.

| Nếu bạn là... | Đường dẫn đề xuất | Lợi ích chính | Điểm đánh đổi chính | Phương pháp hay nhất |
| --- | --- | --- | --- | --- |
| **Cổng doanh nghiệp, khung hệ sinh thái** | **[SDK GenAI của Google](https://ai.google.dev/gemini-api/docs/SDK GenAI của Google)** | **Tính tương đương và tốc độ của Nền tảng tác nhân Gemini Enterprise.** Xử lý tích hợp cho các loại, quá trình xác thực và tính năng phức tạp (ví dụ: tải tệp lên). Di chuyển liền mạch sang Google Cloud. | **Trọng số phần phụ thuộc.** Các phần phụ thuộc bắc cầu có thể phức tạp và nằm ngoài tầm kiểm soát của bạn. Chỉ hỗ trợ các ngôn ngữ được hỗ trợ (Python/Node/Go/Java). | **Khoá phiên bản.** Ghim các phiên bản SDK trong hình ảnh cơ sở nội bộ để đảm bảo tính ổn định trên các nhóm. |
| **Khung hệ sinh thái, nền tảng biên và trang web tổng hợp** | **[API Trực tiếp](https://ai.google.dev/gemini-api/docs/API Trực tiếp)**  *(REST / gRPC)* | **Không có phần phụ thuộc.** Bạn kiểm soát ứng dụng HTTP và kích thước gói chính xác. Toàn quyền truy cập vào tất cả các tính năng của API và mô hình. | **Chi phí phát triển cao.** Cấu trúc JSON có thể được lồng sâu và yêu cầu xác thực thủ công nghiêm ngặt cũng như kiểm tra loại. | **Sử dụng thông số kỹ thuật OpenAPI.** Tự động hoá quá trình tạo loại bằng cách sử dụng thông số kỹ thuật chính thức của chúng tôi thay vì viết chúng theo cách thủ công. |
| **Trang web tổng hợp sử dụng SDK OpenAI chỉ yêu cầu quy trình làm việc dựa trên văn bản**  *(Tối ưu hoá tính di động cũ)* | **[Khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/Khả năng tương thích với OpenAI)** | **Tính di động tức thì.** Sử dụng lại mã hoặc thư viện hiện có tương thích với OpenAI. | **Giới hạn tính năng.** Các tính năng dành riêng cho mô hình (Video gốc, Bộ nhớ đệm) có thể không dùng được. | **Kế hoạch di chuyển.** Sử dụng tính năng này để xác thực nhanh, nhưng hãy lên kế hoạch nâng cấp lên API Trực tiếp để có tính năng API hoàn chỉnh. |

## Tích hợp SDK GenAI của Google

Đối với các khung, việc triển khai [SDK GenAI của Google](https://ai.google.dev/gemini-api/docs/SDK GenAI của Google)
thường là đường dẫn đơn giản nhất, vì có ít dòng mã nhất bằng các ngôn ngữ được hỗ trợ.

Đối với các nhóm nền tảng nội bộ, sản phẩm chính mà bạn cung cấp thường là "đường dẫn vàng" cho phép kỹ sư sản phẩm di chuyển nhanh chóng trong khi tuân thủ các chính sách bảo mật.

**Lợi ích:**

- **Giao diện hợp nhất để di chuyển Nền tảng tác nhân Gemini Enterprise:** Nhà phát triển nội bộ thường tạo nguyên mẫu bằng Khoá API (Gemini API) và triển khai lên Nền tảng tác nhân Gemini Enterprise (IAM) để tuân thủ quy trình sản xuất. SDK này tóm tắt những điểm khác biệt về quá trình xác thực này.
  Tương tự đối với các khung, bạn có thể triển khai một đường dẫn mã và hỗ trợ 2 nhóm người dùng.
- **Trình trợ giúp phía máy khách:** SDK này bao gồm các tiện ích thành ngữ giúp giảm mã nguyên mẫu cho các tác vụ phức tạp.
  - *Ví dụ:* Hỗ trợ trực tiếp các đối tượng hình ảnh `PIL` trong lời nhắc, gọi hàm tự động và các loại toàn diện.
- **Quyền truy cập vào tính năng từ ngày đầu tiên:** Các tính năng API mới có sẵn tại thời điểm ra mắt thông qua SDK.
- **Cải thiện khả năng hỗ trợ tạo mã:** Quá trình cài đặt SDK cục bộ sẽ hiển thị các định nghĩa loại và chuỗi tài liệu cho trợ lý lập trình (ví dụ: Cursor, Copilot).
  Ngữ cảnh này cải thiện độ chính xác khi tạo mã so với việc tạo các yêu cầu REST thô.

**Điểm đánh đổi:**

- **Trọng số và độ phức tạp của phần phụ thuộc:** SDK có các phần phụ thuộc riêng, có thể làm tăng kích thước gói và có khả năng gây ra rủi ro cho chuỗi cung ứng.
- **Phiên bản:** Các tính năng API mới thường được ghim vào các phiên bản SDK tối thiểu.
  Bạn có thể cần gửi bản cập nhật cho người dùng để truy cập vào các tính năng hoặc mô hình mới. Trong một số trường hợp, việc này có thể yêu cầu thay đổi các phần phụ thuộc bắc cầu ảnh hưởng đến người dùng của bạn.
- **Giới hạn giao thức:** SDK chỉ hỗ trợ HTTPS cho API chính và WebSocket (WSS) cho Live API. gRPC không được hỗ trợ khi sử dụng ứng dụng SDK cấp cao.
- **Hỗ trợ ngôn ngữ:** SDK hỗ trợ các phiên bản ngôn ngữ *hiện tại*. Nếu cần hỗ trợ các phiên bản EOL (ví dụ: Python 3.9), bạn cần duy trì một nhánh.

**Phương pháp hay nhất:**

- **Khoá phiên bản:** Ghim phiên bản SDK trong hình ảnh cơ sở nội bộ để đảm bảo tính ổn định trên các nhóm.

## Tích hợp API Trực tiếp

Nếu bạn đang phân phối một thư viện cho hàng nghìn nhà phát triển, chạy trong một môi trường bị hạn chế hoặc xây dựng một trang web tổng hợp yêu cầu các tính năng tiên tiến của Gemini, bạn có thể cần tích hợp trực tiếp với API bằng REST hoặc gRPC.

**Lợi ích:**

- **Toàn quyền truy cập vào tính năng:** Không giống như lớp tương thích OpenAI, việc sử dụng trực tiếp API sẽ bật các tính năng dành riêng cho Gemini, chẳng hạn như tải lên File API, tạo bộ nhớ đệm nội dung và sử dụng Live API hai chiều.
- **Phần phụ thuộc tối thiểu:** Trong môi trường mà các phần phụ thuộc nhạy cảm do kích thước hoặc chi phí kiểm tra. Việc sử dụng trực tiếp API thông qua một thư viện tiêu chuẩn như `fetch` hoặc thông qua một trình bao bọc như `httpx` sẽ đảm bảo thư viện của bạn vẫn gọn nhẹ.
- **Không phụ thuộc vào ngôn ngữ:** Đây là đường dẫn duy nhất cho các ngôn ngữ không được SDK hỗ trợ, chẳng hạn như Rust, PHP và Ruby, vì không có giới hạn về ngôn ngữ.
- **Hiệu suất:** API Trực tiếp không có chi phí khởi tạo, giúp giảm thiểu thời gian khởi động nguội trong các hàm phi máy chủ.

**Điểm đánh đổi:**

- **Triển khai Nền tảng tác nhân Gemini Enterprise theo cách thủ công:** Không giống như SDK, việc sử dụng trực tiếp API sẽ không tự động xử lý các điểm khác biệt về quá trình xác thực giữa AI Studio (Khoá API) và Nền tảng tác nhân Gemini Enterprise (IAM). Bạn phải triển khai các trình xử lý xác thực riêng nếu muốn hỗ trợ cả hai môi trường.
- **Không có loại hoặc trình trợ giúp gốc:** Bạn không nhận được tính năng hoàn thành mã hoặc kiểm tra thời gian biên dịch cho các đối tượng yêu cầu, trừ phi bạn tự triển khai. Không có "trình trợ giúp" ứng dụng (ví dụ: trình chuyển đổi hàm sang lược đồ), vì vậy, bạn phải tự viết logic này theo cách thủ công.

**Phương pháp hay nhất**

Chúng tôi cung cấp một thông số kỹ thuật có thể đọc bằng máy mà bạn có thể dùng để tạo định nghĩa loại cho thư viện của mình, giúp bạn không phải viết chúng theo cách thủ công. Tải thông số kỹ thuật xuống trong quá trình xây dựng, tạo các loại và gửi mã đã biên dịch.

- **Điểm cuối:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## Tích hợp SDK OpenAI

Nếu bạn là một nền tảng ưu tiên lược đồ hợp nhất (Hoàn thành cuộc trò chuyện OpenAI) hơn các tính năng dành riêng cho mô hình, thì đây là tuyến đường nhanh nhất.

**Lợi ích:**

- **Ít trở ngại:** Bạn thường có thể thêm tính năng hỗ trợ Gemini bằng cách thay đổi `baseURL` và `apiKey`. Đây là cách nhanh chóng để tích hợp các cách triển khai "Mang theo khoá của riêng bạn", thêm tính năng hỗ trợ Gemini mà không cần viết mã mới.
- **Các ràng buộc:** Bạn chỉ nên sử dụng đường dẫn này nếu bị giới hạn ở SDK OpenAI và không yêu cầu các tính năng nâng cao của Gemini như File API hoặc thêm tính năng hỗ trợ theo cách thủ công cho các công cụ như Dựa trên kết quả của Google Tìm kiếm.

**Điểm đánh đổi:**

- **Giới hạn tính năng:** Lớp tương thích cung cấp các giới hạn cho các tính năng cốt lõi của Gemini. Các công cụ phía máy chủ có sẵn khác nhau giữa các nền tảng và có thể yêu cầu xử lý thủ công để hoạt động với các công cụ Gemini API.
- **Chi phí dịch:** Vì giản đồ OpenAI không ánh xạ 1:1 với kiến trúc của Gemini, nên việc dựa vào lớp tương thích sẽ gây ra một số phức tạp đòi hỏi phải triển khai thêm để giải quyết, chẳng hạn như ánh xạ công cụ "tìm kiếm" của người dùng với công cụ nền tảng phù hợp.
  Nếu bạn cần một lượng lớn trường hợp đặc biệt, thì việc sử dụng SDK hoặc API riêng cho từng nền tảng có thể mang lại nhiều giá trị hơn.

**Phương pháp hay nhất**

Khi có thể, hãy tích hợp trực tiếp với Gemini API. Tuy nhiên, để có khả năng tương thích tối đa, hãy cân nhắc sử dụng một thư viện nhận biết các nhà cung cấp khác nhau và có thể xử lý việc ánh xạ công cụ và thông báo cho bạn.

## Phương pháp hay nhất cho tất cả đối tác: xác định ứng dụng

Khi gọi Gemini API dưới dạng nền tảng hoặc thư viện, bạn phải xác định ứng dụng của mình bằng tiêu đề `x-goog-api-client`.

Điều này cho phép Google xác định các phân khúc lưu lượng truy cập cụ thể của bạn. Nếu thư viện của bạn đang tạo ra một mẫu lỗi cụ thể, chúng tôi có thể liên hệ để giúp gỡ lỗi.

Sử dụng định dạng `company-product/version` (ví dụ: `acme-framework/1.2.0`).

### Ví dụ về cấu hình triển khai

### SDK GenAI

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

### API Trực tiếp (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key=$GEMINI_API_KEY" \
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

- Truy cập vào phần tổng quan về thư viện [library overview](https://ai.google.dev/gemini-api/docs/library overview) để tìm hiểu về
  the GenAI SDKs
- Duyệt tài liệu tham khảo [API](https://ai.google.dev/gemini-api/docs/API)
- Đọc [hướng dẫn về khả năng tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/hướng dẫn về khả năng tương thích với OpenAI)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://ai.google.dev/gemini-api/docs/Giấy phép ghi nhận tác giả 4.0 của Creative Commons) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://ai.google.dev/gemini-api/docs/Giấy phép Apache 2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://ai.google.dev/gemini-api/docs/Chính sách trang web của Google Developers). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?
