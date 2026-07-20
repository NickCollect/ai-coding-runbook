---
source_url: https://ai.google.dev/gemini-api/docs/troubleshooting?hl=vi
fetched_at: 2026-07-20T04:47:15.873335+00:00
title: "H\u01b0\u1edbng d\u1eabn kh\u1eafc ph\u1ee5c s\u1ef1 c\u1ed1 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn khắc phục sự cố

Hãy dùng hướng dẫn này để chẩn đoán và giải quyết các vấn đề thường gặp khi bạn gọi Gemini API. Bạn có thể gặp phải vấn đề từ dịch vụ phụ trợ Gemini API hoặc SDK ứng dụng. Các SDK ứng dụng của chúng tôi được cung cấp dưới dạng nguồn mở trong các kho lưu trữ sau:

- [python-genai](https://github.com/googleapis/python-genai)
- [js-genai](https://github.com/googleapis/js-genai)
- [go-genai](https://github.com/googleapis/go-genai)

Nếu bạn gặp vấn đề về khoá API, hãy kiểm tra để đảm bảo rằng bạn đã thiết lập khoá API đúng cách theo [hướng dẫn thiết lập khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi).

## Mã lỗi dịch vụ phụ trợ của Gemini API

Bảng sau đây liệt kê các mã lỗi thường gặp ở phần phụ trợ mà bạn có thể gặp phải, cùng với nội dung giải thích về nguyên nhân và các bước khắc phục:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mã HTTP** | **Trạng thái** | **Nội dung mô tả** | **Ví dụ** | **Giải pháp** |
| 400 | INVALID\_ARGUMENT | Nội dung yêu cầu có định dạng không chính xác. | Có lỗi chính tả hoặc thiếu trường bắt buộc trong yêu cầu của bạn. | Hãy tham khảo [tài liệu tham khảo API](https://ai.google.dev/api?hl=vi) để biết định dạng yêu cầu, ví dụ và các phiên bản được hỗ trợ. Việc sử dụng các tính năng của phiên bản API mới hơn với một điểm cuối cũ hơn có thể gây ra lỗi. |
| 400 | FAILED\_PRECONDITION | Bậc miễn phí của Gemini API chưa được cung cấp ở quốc gia của bạn. Vui lòng bật tính năng thanh toán cho dự án của bạn trong Google AI Studio. | Bạn đang đưa ra yêu cầu ở một khu vực không hỗ trợ cấp miễn phí và bạn chưa bật tính năng thanh toán cho dự án của mình trong Google AI Studio. | Để sử dụng Gemini API, bạn cần thiết lập một gói có tính phí bằng [Google AI Studio](https://aistudio.google.com/apikey?hl=vi). |
| 403 | PERMISSION\_DENIED | Khoá API của bạn không có các quyền cần thiết. | Bạn đang sử dụng sai khoá API; bạn đang cố gắng sử dụng một mô hình đã điều chỉnh mà không trải qua [quy trình xác thực thích hợp](https://ai.google.dev/gemini-api/docs/model-tuning?hl=vi). | Kiểm tra để đảm bảo bạn đã đặt khoá API và có quyền truy cập phù hợp. Đồng thời, hãy nhớ thực hiện quy trình xác thực thích hợp để sử dụng các mô hình được điều chỉnh. |
| 404 | NOT\_FOUND | Không tìm thấy tài nguyên được yêu cầu. | Không tìm thấy tệp hình ảnh, âm thanh hoặc video được đề cập trong yêu cầu của bạn. | Kiểm tra xem tất cả [các tham số trong yêu cầu của bạn có hợp lệ](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=vi#check-api) đối với phiên bản API của bạn hay không. |
| 429 | RESOURCE\_EXHAUSTED | Bạn đã vượt quá một trong các giới hạn tần suất của API (RPM, TPM, RPD, mức chi tiêu, v.v.). | Bạn đang gửi quá nhiều yêu cầu, sử dụng quá nhiều mã thông báo hoặc vượt quá hạn mức dựa trên mức chi tiêu cho nhật ký thanh toán và cấp của tài khoản. | Xác minh rằng bạn đang nằm trong [giới hạn về tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi) của mô hình. Đợi một lát rồi thử lại. Giảm tốc độ hoặc kích thước của các yêu cầu. [Yêu cầu tăng giới hạn tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi#request-rate-limit-increase) nếu cần. |
| 499 | ĐÃ HUỶ | Thao tác đã bị huỷ, thường là do người gọi. | Ứng dụng đã đóng kết nối trước khi API có thể hoàn tất việc phản hồi. | Kiểm tra xem máy khách hoặc cơ sở hạ tầng mạng của bạn có đóng kết nối quá sớm hay không (ví dụ: do hết thời gian chờ ở phía máy khách). |
| 500 | NỘI BỘ | Đã xảy ra lỗi không mong muốn với Google. | Bối cảnh đầu vào của bạn quá dài. | Kiểm tra [trang trạng thái của Gemini API](https://aistudio.google.com/status?hl=vi) để biết mọi sự cố đang diễn ra. Giảm ngữ cảnh đầu vào hoặc tạm thời chuyển sang một mô hình khác (ví dụ: từ Gemini 2.5 Pro sang Gemini 2.5 Flash) để xem có hiệu quả không. Hoặc đợi một lát rồi thử lại yêu cầu. Nếu vấn đề vẫn tiếp diễn sau khi bạn thử lại, vui lòng báo cáo vấn đề đó bằng nút **Gửi ý kiến phản hồi** trong Google AI Studio. |
| 503 | KHÔNG CÓ | Dịch vụ có thể tạm thời bị quá tải hoặc không hoạt động. | Dịch vụ này tạm thời hết dung lượng. | Kiểm tra [trang trạng thái của Gemini API](https://aistudio.google.com/status?hl=vi) để biết mọi sự cố đang diễn ra. Tạm thời chuyển sang một mô hình khác (ví dụ: từ Gemini 2.5 Pro sang Gemini 2.5 Flash) để xem vấn đề có được giải quyết hay không. Hoặc đợi một lát rồi thử lại yêu cầu. Nếu vấn đề vẫn tiếp diễn sau khi bạn thử lại, vui lòng báo cáo vấn đề đó bằng nút **Gửi ý kiến phản hồi** trong Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | Dịch vụ không thể hoàn tất quá trình xử lý trong thời hạn. | Câu lệnh (hoặc bối cảnh) của bạn quá lớn nên không xử lý kịp. | Đặt "thời gian chờ" dài hơn trong yêu cầu của ứng dụng để tránh lỗi này. |

## Chiến lược thử lại

Nếu nhận được lỗi cho biết bạn nên thử lại yêu cầu (chẳng hạn như `429 RESOURCE_EXHAUSTED` hoặc `503 UNAVAILABLE`), bạn nên triển khai chiến lược thời gian đợi luỹ thừa. Điều này có nghĩa là bạn đợi một khoảng thời gian ngắn trước lần thử lại đầu tiên, sau đó tăng dần thời gian chờ giữa các lần thử lại tiếp theo.

Các SDK ứng dụng chính thức cho Gemini API (chẳng hạn như [Python SDK](https://github.com/googleapis/python-genai)) theo mặc định có logic tự động thử lại với độ trễ luỹ thừa để xử lý các lỗi tạm thời như hết thời gian chờ, sự cố về mạng và giới hạn về tốc độ (mã trạng thái `429` và `5xx`). Ví dụ: Python SDK tự động thử lại các lỗi tạm thời tối đa 4 lần với độ trễ ban đầu khoảng 1 giây và độ trễ tối đa là 60 giây.

Nếu bạn đang thực hiện các yêu cầu trực tiếp đến REST API hoặc tuỳ chỉnh logic thử lại, hãy làm theo các phương pháp hay nhất sau đây để tăng khả năng yêu cầu thành công và ngăn dịch vụ bị quá tải:

- **Sử dụng cơ chế giảm thời gian chờ theo cấp số nhân:** Chờ một khoảng thời gian ngắn trước lần thử lại đầu tiên (ví dụ: 1 giây), sau đó tăng độ trễ theo cấp số nhân (ví dụ: 2 giây, 4 giây, 8 giây).
- **Thêm biên độ:** Thêm "biên độ" ngẫu nhiên vào độ trễ để giúp ngăn tất cả ứng dụng khách thử lại cùng một lúc.
- **Thử lại khi gặp lỗi cụ thể:** Chỉ thử lại khi gặp lỗi tạm thời (chẳng hạn như `429`, `408` hoặc `5xx`). Không thử lại khi gặp lỗi phía máy khách (chẳng hạn như `400` hoặc `403`) vì những lỗi này cho biết các vấn đề như khoá API không hợp lệ hoặc cú pháp không chính xác.
- **Đặt số lần thử lại tối đa:** Xác định số lần thử lại tối đa để ngăn chặn vòng lặp vô hạn.

## Kiểm tra các lệnh gọi API để tìm lỗi tham số mô hình

Xác minh rằng các thông số mô hình của bạn nằm trong các giá trị sau:

|  |  |
| --- | --- |
| **Tham số mô hình** | **Giá trị (phạm vi)** |
| Số lượng đề xuất | 1-8 (số nguyên) |
| Nhiệt độ | 0.0 – 1.0 |
| Số mã thông báo đầu ra tối đa | Sử dụng [trang mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi) để xác định số lượng mã thông báo tối đa cho mô hình mà bạn đang sử dụng. |
| TopP | 0.0 – 1.0 |

Ngoài việc kiểm tra các giá trị tham số, hãy đảm bảo rằng bạn đang sử dụng [phiên bản API](https://ai.google.dev/gemini-api/docs/api-versions?hl=vi) chính xác (ví dụ: `/v1` hoặc `/v1beta`) và mô hình hỗ trợ các tính năng bạn cần. Ví dụ: nếu một tính năng đang ở giai đoạn phát hành Beta, thì tính năng đó sẽ chỉ có trong phiên bản API `/v1beta`.

## Kiểm tra xem bạn có đúng mẫu không

Xác minh rằng bạn đang sử dụng một mô hình được hỗ trợ có trong [trang mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi) của chúng tôi.

## Độ trễ cao hơn hoặc mức sử dụng mã thông báo cao hơn với các mô hình 2.5

Nếu bạn nhận thấy độ trễ hoặc mức sử dụng mã thông báo cao hơn với các mô hình 2.5 Flash và Pro, thì có thể là do các mô hình này **được bật tính năng suy nghĩ theo mặc định** để nâng cao chất lượng. Nếu đang ưu tiên tốc độ hoặc cần giảm thiểu chi phí, bạn có thể điều chỉnh hoặc tắt tính năng suy nghĩ.

Hãy tham khảo [trang suy nghĩ](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#set-budget) để biết hướng dẫn và mã mẫu.

## Vấn đề về an toàn

Nếu bạn thấy một câu lệnh bị chặn do chế độ cài đặt an toàn trong lệnh gọi API, hãy xem xét câu lệnh đó theo các bộ lọc mà bạn đã đặt trong lệnh gọi API.

Nếu bạn thấy `BlockedReason.OTHER`, thì có thể truy vấn hoặc câu trả lời đó vi phạm [điều khoản dịch vụ](https://ai.google.dev/terms?hl=vi) hoặc không được hỗ trợ.

## Vấn đề về việc đọc thuộc lòng

Nếu bạn thấy mô hình ngừng tạo kết quả do lý do TRÍCH DẪN, thì điều này có nghĩa là kết quả của mô hình có thể giống với một số dữ liệu nhất định. Để khắc phục vấn đề này, hãy cố gắng tạo câu lệnh / bối cảnh độc đáo nhất có thể và sử dụng nhiệt độ cao hơn.

## Vấn đề về mã thông báo lặp lại

Nếu bạn thấy các mã thông báo đầu ra lặp lại, hãy thử các đề xuất sau để giúp giảm hoặc loại bỏ các mã thông báo đó.

| Mô tả | Nguyên nhân | Giải pháp thay thế được đề xuất |
| --- | --- | --- |
| Dấu gạch ngang lặp lại trong bảng Markdown | Điều này có thể xảy ra khi nội dung của bảng quá dài vì mô hình cố gắng tạo một bảng Markdown được căn chỉnh trực quan. Tuy nhiên, việc căn chỉnh trong Markdown là không cần thiết để hiển thị chính xác. | Thêm hướng dẫn vào câu lệnh để cung cấp cho mô hình các nguyên tắc cụ thể về cách tạo bảng Markdown. Cung cấp ví dụ tuân thủ các nguyên tắc đó. Bạn cũng có thể thử điều chỉnh nhiệt độ. Để tạo mã hoặc đầu ra có cấu trúc cao như bảng Markdown, nhiệt độ cao đã cho thấy hiệu quả hơn (>= 0,8).  Sau đây là một ví dụ về bộ nguyên tắc mà bạn có thể thêm vào câu lệnh để ngăn chặn vấn đề này:     ```           # Markdown Table Format                      * Separator line: Markdown tables must include a separator line below             the header row. The separator line must use only 3 hyphens per             column, for example: |---|---|---|. Using more hypens like             ----, -----, ------ can result in errors. Always             use |:---|, |---:|, or |---| in these separator strings.              For example:              | Date | Description | Attendees |             |---|---|---|             | 2024-10-26 | Annual Conference | 500 |             | 2025-01-15 | Q1 Planning Session | 25 |            * Alignment: Do not align columns. Always use |---|.             For three columns, use |---|---|---| as the separator line.             For four columns use |---|---|---|---| and so on.            * Conciseness: Keep cell content brief and to the point.            * Never pad column headers or other cells with lots of spaces to             match with width of other content. Only a single space on each side             is needed. For example, always do "| column name |" instead of             "| column name                |". Extra spaces are wasteful.             A markdown renderer will automatically take care displaying             the content in a visually appealing form. ``` |
| Mã thông báo lặp lại trong bảng Markdown | Tương tự như dấu gạch ngang lặp lại, điều này xảy ra khi mô hình cố gắng căn chỉnh nội dung của bảng một cách trực quan. Bạn không cần phải căn chỉnh trong Markdown để hiển thị chính xác. | - Hãy thử thêm các chỉ dẫn như sau vào câu lệnh hệ thống:      ```               FOR TABLE HEADINGS, IMMEDIATELY ADD ' |' AFTER THE TABLE HEADING.   ``` - Hãy thử điều chỉnh nhiệt độ. Nhiệt độ cao hơn (>= 0,8) thường giúp loại bỏ các đoạn văn lặp lại hoặc trùng lặp trong đầu ra. |
| Ký tự xuống dòng lặp lại (`\n`) trong đầu ra có cấu trúc | Khi đầu vào của mô hình chứa các chuỗi unicode hoặc chuỗi thoát như `\u` hoặc `\t`, thì điều này có thể dẫn đến việc lặp lại các dòng mới. | - Kiểm tra và thay thế các chuỗi thoát bị cấm bằng ký tự UTF-8 trong câu lệnh. Ví dụ: chuỗi thoát `\u` trong các ví dụ JSON có thể khiến mô hình sử dụng các chuỗi đó trong đầu ra của mô hình. - Hướng dẫn mô hình về các ký tự thoát được phép. Thêm một chỉ dẫn hệ thống như sau:      ```               In quoted strings, the only allowed escape sequences are \\, \n, and \". Instead of \u escapes, use UTF-8.   ``` |
| Văn bản lặp lại khi sử dụng đầu ra có cấu trúc | Khi đầu ra của mô hình có thứ tự khác cho các trường so với giản đồ có cấu trúc đã xác định, điều này có thể dẫn đến việc lặp lại văn bản. | - Đừng chỉ định thứ tự của các trường trong câu lệnh. - Đặt tất cả các trường đầu ra là bắt buộc. |
| Gọi công cụ lặp lại | Điều này có thể xảy ra nếu mô hình mất ngữ cảnh của các suy nghĩ trước đó và/hoặc gọi một điểm cuối không có sẵn mà mô hình buộc phải gọi. | Hướng dẫn mô hình duy trì trạng thái trong quá trình suy nghĩ. Thêm nội dung này vào cuối hướng dẫn hệ thống:    ```         When thinking silently: ALWAYS start the thought with a brief         (one sentence) recap of the current progress on the task. In         particular, consider whether the task is already done. ``` |
| Văn bản lặp lại không thuộc đầu ra có cấu trúc | Điều này có thể xảy ra nếu mô hình bị kẹt ở một yêu cầu mà mô hình không thể giải quyết. | - Nếu bạn bật tính năng tư duy, hãy tránh đưa ra các chỉ dẫn rõ ràng về cách suy nghĩ để giải quyết một vấn đề trong hướng dẫn. Chỉ cần yêu cầu kết quả cuối cùng. - Hãy thử nhiệt độ cao hơn >= 0,8. - Thêm hướng dẫn như "Hãy súc tích", "Đừng lặp lại" hoặc "Chỉ đưa ra câu trả lời một lần". |

## Khoá API bị chặn hoặc không hoạt động

Phần này mô tả cách kiểm tra xem khoá Gemini API của bạn có bị chặn hay không và cách xử lý vấn đề này.

### Tìm hiểu lý do khoá bị chặn

Chúng tôi đã xác định được một lỗ hổng bảo mật có thể khiến một số khoá API bị lộ công khai. Để bảo vệ dữ liệu của bạn và ngăn chặn hành vi truy cập trái phép, chúng tôi đã chủ động chặn những khoá bị rò rỉ đã biết này truy cập vào Gemini API.

### Xác nhận xem các khoá của bạn có bị ảnh hưởng hay không

Nếu biết khoá của mình đã bị lộ, bạn sẽ không thể sử dụng khoá đó với Gemini API nữa. Bạn có thể sử dụng [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=vi) để xem có khoá API nào của bạn bị chặn gọi Gemini API hay không và tạo khoá mới. Bạn cũng có thể thấy lỗi sau đây được trả về khi cố gắng sử dụng các khoá này:

```
Your API key was reported as leaked. Please use another API key.
```

### Hành động đối với khoá API bị chặn

Bạn nên tạo khoá API mới cho các mối liên kết tích hợp Gemini API bằng [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=vi). Bạn nên xem xét kỹ các phương pháp quản lý khoá API để đảm bảo khoá mới của bạn được bảo mật và không bị lộ công khai.

### Các khoản phí ngoài dự kiến do lỗ hổng

[Gửi yêu cầu hỗ trợ về việc thanh toán](https://console.cloud.google.com/support/chat?hl=vi).
Nhóm thanh toán của chúng tôi đang xử lý vấn đề này và chúng tôi sẽ thông báo cho bạn ngay khi có thông tin cập nhật.

### Các biện pháp bảo mật của Google đối với khoá bị rò rỉ

**Nếu khoá API của tôi bị lộ, Google sẽ giúp bảo vệ tài khoản của tôi khỏi tình trạng vượt quá chi phí và hành vi sai trái như thế nào?**

- Chúng tôi đang tiến tới việc phát hành khoá API khi bạn yêu cầu một khoá mới bằng [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=vi). Theo mặc định, khoá này sẽ chỉ giới hạn ở Google AI Studio và không chấp nhận khoá từ các dịch vụ khác.
  Điều này sẽ giúp ngăn chặn mọi trường hợp sử dụng khoá chéo ngoài ý muốn.
- Chúng tôi sẽ chặn các khoá API bị rò rỉ và được dùng với Gemini API theo mặc định, giúp ngăn chặn hành vi sai trái về chi phí và dữ liệu ứng dụng của bạn.
- Bạn có thể xem trạng thái của khoá API trong [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-keys?hl=vi) và chúng tôi sẽ chủ động liên hệ với bạn khi phát hiện khoá API của bạn bị lộ để bạn có thể hành động ngay lập tức.

## Cải thiện đầu ra của mô hình

Để có kết quả đầu ra chất lượng cao hơn từ mô hình, hãy thử viết các câu lệnh có cấu trúc hơn. Trang [hướng dẫn về kỹ thuật tạo câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=vi) giới thiệu một số khái niệm, chiến lược và phương pháp hay nhất cơ bản để giúp bạn bắt đầu.

## Tìm hiểu về giới hạn mã thông báo

Hãy đọc [Hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) của chúng tôi để hiểu rõ hơn về cách tính mã thông báo và hạn mức của mã thông báo.

## Vấn đề đã biết

- API này chỉ hỗ trợ một số ngôn ngữ. Việc gửi câu lệnh bằng các ngôn ngữ không được hỗ trợ có thể tạo ra những câu trả lời không mong muốn hoặc thậm chí bị chặn. Xem [các ngôn ngữ được hỗ trợ](https://ai.google.dev/gemini-api/docs/models?hl=vi#supported-languages) để biết thông tin cập nhật.

## Báo cáo lỗi

Tham gia thảo luận trên [diễn đàn nhà phát triển AI của Google](https://discuss.ai.google.dev?hl=vi) nếu bạn có thắc mắc.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-08 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-08 UTC."],[],[]]
