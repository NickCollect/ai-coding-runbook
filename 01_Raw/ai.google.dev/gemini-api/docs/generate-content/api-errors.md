---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=vi
fetched_at: 2026-08-03T04:32:52.586683+00:00
title: "L\u1ed7i API \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Lỗi API

Trang này cung cấp thông tin tham khảo về các mã lỗi phụ trợ do API `GenerateContent` trả về, mô tả định dạng phản hồi lỗi gRPC và cung cấp các bước khắc phục sự cố.

## Mã lỗi HTTP

Bảng sau đây liệt kê các mã lỗi phổ biến ở phần phụ trợ, giải thích nguyên nhân gây ra các lỗi đó và các giải pháp được đề xuất:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mã HTTP** | **Trạng thái** | **Nội dung mô tả** | **Ví dụ** | **Giải pháp** |
| 400 | INVALID\_ARGUMENT | Nội dung yêu cầu có định dạng không chính xác. | Có lỗi chính tả hoặc thiếu trường bắt buộc trong yêu cầu của bạn. | Hãy tham khảo [tài liệu tham khảo API](https://ai.google.dev/api?hl=vi) để biết định dạng yêu cầu, ví dụ và các phiên bản được hỗ trợ. Việc sử dụng các tính năng của phiên bản API mới hơn với một điểm cuối cũ hơn có thể gây ra lỗi. |
| 400 | FAILED\_PRECONDITION | Bậc miễn phí của Gemini API chưa được cung cấp ở quốc gia của bạn. Vui lòng bật tính năng thanh toán cho dự án của bạn trong Google AI Studio. | Bạn đang đưa ra yêu cầu ở một khu vực không được hỗ trợ cấp miễn phí và bạn chưa bật tính năng thanh toán cho dự án của mình trong Google AI Studio. | Để sử dụng Gemini API, bạn cần thiết lập một gói có tính phí bằng [Google AI Studio](https://aistudio.google.com/apikey?hl=vi). |
| 403 | PERMISSION\_DENIED | Khoá API của bạn không có các quyền cần thiết. | Bạn đang sử dụng sai khoá API; bạn đang cố gắng sử dụng một mô hình đã điều chỉnh mà không trải qua quy trình [xác thực thích hợp](https://ai.google.dev/gemini-api/docs/model-tuning?hl=vi). | Kiểm tra để đảm bảo bạn đã đặt khoá API và có quyền truy cập phù hợp. Đồng thời, hãy nhớ thực hiện quy trình xác thực thích hợp để sử dụng các mô hình được điều chỉnh. |
| 404 | NOT\_FOUND | Không tìm thấy tài nguyên được yêu cầu. | Không tìm thấy tệp hình ảnh, âm thanh hoặc video được đề cập trong yêu cầu của bạn. | Kiểm tra xem tất cả các tham số trong yêu cầu của bạn có hợp lệ cho phiên bản API của bạn hay không. |
| 429 | RESOURCE\_EXHAUSTED | Bạn đã vượt quá một trong các giới hạn tần suất yêu cầu của API (RPM, TPM, RPD, mức chi tiêu, v.v.). | Bạn đang gửi quá nhiều yêu cầu, sử dụng quá nhiều mã thông báo hoặc vượt quá hạn mức dựa trên mức chi tiêu cho lịch sử thanh toán và cấp của tài khoản. | Xác minh rằng bạn đang nằm trong [giới hạn về tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi) của mô hình. Đợi một lát rồi thử lại. Giảm tốc độ hoặc kích thước của các yêu cầu. [Yêu cầu tăng giới hạn tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi#request-rate-limit-increase) nếu cần. |
| 499 | ĐÃ HỦY | Thao tác đã bị huỷ, thường là do người gọi. | Ứng dụng đã đóng kết nối trước khi API có thể hoàn tất việc phản hồi. | Kiểm tra xem máy khách hoặc cơ sở hạ tầng mạng của bạn có đóng kết nối quá sớm hay không (ví dụ: do hết thời gian chờ ở phía máy khách). |
| 500 | NỘI BỘ | Đã xảy ra lỗi không mong muốn với Google. | Bối cảnh đầu vào của bạn quá dài. | Kiểm tra [trang trạng thái của Gemini API](https://aistudio.google.com/status?hl=vi) để biết mọi sự cố đang diễn ra. Giảm ngữ cảnh đầu vào hoặc tạm thời chuyển sang một mô hình khác (ví dụ: từ Gemini 2.5 Pro sang Gemini 2.5 Flash) để xem có hiệu quả không. Hoặc đợi một lát rồi thử lại yêu cầu. Nếu vấn đề vẫn tiếp diễn sau khi bạn thử lại, vui lòng báo cáo vấn đề đó bằng nút **Gửi ý kiến phản hồi** trong Google AI Studio. |
| 503 | KHÔNG CÓ | Dịch vụ có thể tạm thời bị quá tải hoặc không hoạt động. | Dịch vụ này tạm thời hết dung lượng. | Kiểm tra [trang trạng thái của Gemini API](https://aistudio.google.com/status?hl=vi) để biết mọi sự cố đang diễn ra. Tạm thời chuyển sang một mô hình khác (ví dụ: từ Gemini 2.5 Pro sang Gemini 2.5 Flash) để xem vấn đề có được giải quyết hay không. Hoặc đợi một lát rồi thử lại yêu cầu. Nếu vấn đề vẫn tiếp diễn sau khi bạn thử lại, vui lòng báo cáo vấn đề đó bằng nút **Gửi ý kiến phản hồi** trong Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Dịch vụ không thể hoàn tất quá trình xử lý trong thời hạn. | Câu lệnh (hoặc bối cảnh) của bạn quá lớn nên không thể xử lý kịp thời. | Đặt "thời gian chờ" dài hơn trong yêu cầu của ứng dụng để tránh lỗi này. |

## Định dạng phản hồi lỗi

Khi yêu cầu `GenerateContent` không thành công, API sẽ đặt mã trạng thái HTTP (chẳng hạn như `400 Bad Request`, `403 Forbidden` hoặc `429 Too Many Requests`) và trả về một phần nội dung phản hồi JSON chứa thông tin chi tiết về trạng thái gRPC:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Trường | Loại | Mô tả |
| --- | --- | --- |
| `code` | số nguyên | Mã trạng thái HTTP. |
| `message` | chuỗi | Nội dung mô tả lỗi mà con người có thể đọc được. |
| `status` | chuỗi | Mã trạng thái gRPC trong `SCREAMING_CASE`. |
| `details` | mảng | Ngữ cảnh bổ sung về lỗi, chẳng hạn như `ErrorInfo` hoặc `LocalizedMessage`. |

## Bước tiếp theo

- [Khắc phục sự cố về API](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=vi): Giải quyết các vấn đề thường gặp và các trường hợp lỗi.
- [Hạn mức về tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi): Tìm hiểu về hạn mức yêu cầu và cách xử lý hạn mức.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
