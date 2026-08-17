---
source_url: https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi
fetched_at: 2026-08-17T02:20:41.257936+00:00
title: "Gi\u1edbi h\u1ea1n s\u1ed1 l\u01b0\u1ee3ng y\u00eau c\u1ea7u \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Giới hạn số lượng yêu cầu

Hạn mức tỷ lệ điều chỉnh số lượng yêu cầu mà bạn có thể gửi đến Gemini API trong một khoảng thời gian nhất định. Những giới hạn này giúp duy trì mức sử dụng hợp lý, bảo vệ khỏi hành vi sai trái và giúp duy trì hiệu suất hệ thống cho tất cả người dùng.

[Xem hạn mức sử dụng đang hoạt động trong AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=vi)

## Cách hoạt động của hạn mức yêu cầu

Hạn mức tỷ lệ thường được đo lường theo 3 phương diện:

- Số yêu cầu mỗi phút (**RPM**)
- Số mã thông báo mỗi phút (đầu vào) (**TPM**)
- Số yêu cầu mỗi ngày (**RPD**)

Mức sử dụng của bạn được đánh giá dựa trên từng hạn mức và việc vượt quá bất kỳ hạn mức nào trong số đó sẽ kích hoạt lỗi giới hạn tốc độ. Ví dụ: nếu giới hạn RPM của bạn là 20, thì việc đưa ra 21 yêu cầu trong vòng một phút sẽ dẫn đến lỗi, ngay cả khi bạn chưa vượt quá giới hạn TPM hoặc các giới hạn khác.

Hạn mức sử dụng được áp dụng cho mỗi dự án, chứ không phải cho mỗi khoá API. Hạn mức số yêu cầu mỗi ngày (**RPD**) sẽ được đặt lại vào lúc nửa đêm theo giờ Thái Bình Dương.

Hạn mức sẽ khác nhau tuỳ thuộc vào mô hình cụ thể đang được sử dụng và một số hạn mức chỉ áp dụng cho một số mô hình cụ thể. Ví dụ: Số hình ảnh mỗi phút (IPM) chỉ được tính cho các mô hình có khả năng tạo hình ảnh (Nano Banana), nhưng về mặt khái niệm thì tương tự như số mã thông báo mỗi phút (TPM). Các mô hình khác có thể có giới hạn về số lượng mã thông báo mỗi ngày (TPD).

Hạn mức sử dụng của các mô hình thử nghiệm và mô hình xem trước sẽ bị hạn chế hơn.

### Giới hạn số lượng yêu cầu dựa trên mức chi tiêu

Ngoài hạn mức yêu cầu mỗi phút (RPM) và hạn mức mã thông báo mỗi phút (TPM), Gemini API còn áp dụng hạn mức dựa trên mức chi tiêu để ngăn chặn các khoản phí không mong muốn. Việc các hạn mức này có áp dụng cho tài khoản của bạn hay không phụ thuộc vào nhật ký thanh toán và [bậc sử dụng](#usage-tiers) của bạn.

Bảng sau đây cho biết hạn mức dựa trên mức chi tiêu cho từng [bậc sử dụng](#usage-tiers). Các hạn mức này được đánh giá trong khoảng thời gian 10 phút liên tục. Việc tài khoản của bạn có phải tuân thủ những hạn mức này hay không phụ thuộc vào nhật ký thanh toán và trạng thái tài khoản của bạn.

| Cấp sử dụng | Giới hạn tốc độ chi tiêu (mỗi 10 phút) |
| --- | --- |
| **Free** | Không áp dụng |
| **Cấp 1** | đô la Hong Kong |
| **Cấp 2** | đô la Hong Kong |
| **Cấp 3** | đô la Hong Kong |

Nếu bạn đạt đến giới hạn tốc độ dựa trên mức chi tiêu, API sẽ trả về lỗi `429 RESOURCE_EXHAUSTED`. Cách giải quyết:

- **Đợi rồi thử lại** sau một khoảng thời gian ngắn.
- **Giảm tốc độ của các yêu cầu tốn kém**, chẳng hạn như bằng cách sử dụng các cửa sổ ngữ cảnh nhỏ hơn hoặc đầu ra ngắn hơn.
- Nếu bạn thường xuyên đạt đến giới hạn này trong quá trình sử dụng bình thường, hãy [yêu cầu tăng giới hạn tốc độ](#request-rate-limit-increase).

## Cấp sử dụng

Giới hạn về tốc độ được gắn với cấp sử dụng của dự án. Khi mức sử dụng và mức chi tiêu API tăng lên, bạn sẽ tự động được nâng cấp lên một cấp cao hơn với hạn mức tốc độ cao hơn.

Điều kiện để đạt được Cấp 2 và Cấp 3 dựa trên tổng mức chi tiêu tích luỹ cho các dịch vụ của Google Cloud (bao gồm nhưng không giới hạn ở Gemini API) đối với tài khoản thanh toán được liên kết với dự án của bạn.

| Cấp sử dụng | Vòng loại | [Hạn mức cấp thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi#tier-spend-caps) |
| --- | --- | --- |
| **Free** | [Dự án đang hoạt động](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) hoặc dùng thử miễn phí | Không áp dụng |
| **Cấp 1** | [Thiết lập và liên kết một tài khoản thanh toán đang hoạt động](https://ai.google.dev/gemini-api/docs/billing?hl=vi#setup-billing) | 250 USD |
| **Cấp 2** | Thanh toán 100 USD + 3 ngày kể từ lần thanh toán thành công đầu tiên | $2.000 |
| **Cấp 3** | Thanh toán 1.000 USD + 30 ngày kể từ lần thanh toán thành công đầu tiên | 20.000 – 100.000 đô la Mỹ trở lên |

Mặc dù việc đáp ứng các tiêu chí đủ điều kiện đã nêu thường là đủ để được phê duyệt, nhưng trong một số trường hợp hiếm gặp, yêu cầu nâng cấp có thể bị từ chối dựa trên các yếu tố khác được xác định trong quá trình xem xét.

Hệ thống này giúp duy trì tính bảo mật và tính toàn vẹn của nền tảng Gemini API cho tất cả người dùng.

## Hạn mức yêu cầu Gemini API

Hạn mức sử dụng phụ thuộc vào nhiều yếu tố (chẳng hạn như cấp sử dụng của bạn) và bạn có thể xem hạn mức này trong Google AI Studio. Khi cấp và trạng thái tài khoản của bạn thay đổi theo thời gian, giới hạn tốc độ sẽ tự động cập nhật.

[Xem hạn mức sử dụng đang hoạt động trong AI Studio](https://aistudio.google.com/rate-limit?timeRange=last-28-days&hl=vi)

Hạn mức tốc độ được chỉ định không được đảm bảo và dung lượng thực tế có thể thay đổi.

## Giới hạn số lượng yêu cầu suy luận mức độ ưu tiên

[Mức tiêu thụ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi) có giới hạn tốc độ riêng, mặc dù mức tiêu thụ được tính vào giới hạn tốc độ lưu lượng truy cập tương tác tổng thể. **Giới hạn tốc độ mặc định là: 0,3 lần [giới hạn tốc độ tiêu chuẩn](https://aistudio.google.com/rate-limit?hl=vi) cho mỗi mô hình và cấp**

## Hạn mức về tốc độ của Batch API

Các yêu cầu [Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) phải tuân theo giới hạn tốc độ riêng, tách biệt với các lệnh gọi API không theo lô.

- **Số yêu cầu theo lô đồng thời:** 100
- **Giới hạn kích thước tệp đầu vào:** 2 GB
- **Hạn mức lưu trữ tệp:** 20 GB
- **Số lượng mã thông báo được đưa vào hàng đợi cho mỗi mô hình:** Bảng **Số lượng mã thông báo được đưa vào hàng đợi theo lô** liệt kê số lượng mã thông báo tối đa có thể được đưa vào hàng đợi để xử lý theo lô trên tất cả các công việc xử lý theo lô đang hoạt động của bạn cho một mô hình nhất định.

### Cấp 1

| Mô hình | Mã thông báo được xếp hàng đợi theo lô |
| --- | --- |
| Mô hình xoá văn bản | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Bản xem trước) | 5.000.000 |
| Gemini 3.1 Flash Lite | 10.000.000 |
| Bản xem trước Gemini 3.1 Flash Lite | 10.000.000 |
| Gemini 3.5 Flash | 3.000.000 |
| Gemini 2.5 Pro | 5.000.000 |
| Gemini 2.5 Pro TTS | 25.000 |
| Gemini 2.5 Flash | 3.000.000 |
| Bản xem trước Gemini 2.5 Flash | 3.000.000 |
| Bản xem trước hình ảnh Gemini 2.5 Flash | 3.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 10.000.000 |
| Bản xem trước Gemini 2.5 Flash Lite | 10.000.000 |
| Gemini 2.0 Flash | 10.000.000 |
| Hình ảnh Gemini 2.0 Flash | 3.000.000 |
| Gemini 2.0 Flash Lite | 10.000.000 |
| Mô hình tạo nội dung đa phương thức | | | | |
| Bản xem trước hình ảnh Gemini 3.1 Flash 🍌 | 1.000.000 |
| Hình ảnh Gemini 3.1 Flash Lite 🍌 | 2.000.000 |
| Bản xem trước hình ảnh của Gemini 3 Pro 🍌 | 2.000.000 |
| Mô hình nhúng | | | | |
| Gemini Embedding | 500.000 |

### Cấp 2

| Mô hình | Mã thông báo được xếp hàng đợi theo lô |
| --- | --- |
| Mô hình xoá văn bản | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Bản xem trước) | 500.000.000 |
| Gemini 3.1 Flash Lite | 500.000.000 |
| Bản xem trước Gemini 3.1 Flash Lite | 500.000.000 |
| Gemini 3.5 Flash | 400.000.000 |
| Gemini 2.5 Pro | 500.000.000 |
| Gemini 2.5 Pro TTS | 100.000 |
| Gemini 2.5 Flash | 400.000.000 |
| Bản xem trước Gemini 2.5 Flash | 400.000.000 |
| Bản xem trước hình ảnh Gemini 2.5 Flash | 400.000.000 |
| Gemini 2.5 Flash TTS | 100.000 |
| Gemini 2.5 Flash Lite | 500.000.000 |
| Bản xem trước Gemini 2.5 Flash Lite | 500.000.000 |
| Gemini 2.0 Flash | 1.000.000.000 |
| Hình ảnh Gemini 2.0 Flash | 400.000.000 |
| Gemini 2.0 Flash Lite | 1.000.000.000 |
| Mô hình tạo nội dung đa phương thức | | | | |
| Bản xem trước hình ảnh Gemini 3.1 Flash 🍌 | 250.000.000 |
| Hình ảnh Gemini 3.1 Flash Lite 🍌 | 270.000.000 |
| Bản xem trước hình ảnh của Gemini 3 Pro 🍌 | 270.000.000 |
| Mô hình nhúng | | | | |
| Gemini Embedding | 5.000.000 |

### Cấp 3

| Mô hình | Mã thông báo được xếp hàng đợi theo lô |
| --- | --- |
| Mô hình xoá văn bản | | | | |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Pro (Bản xem trước) | 1.000.000.000 |
| Gemini 3.1 Flash Lite | 1.000.000.000 |
| Bản xem trước Gemini 3.1 Flash Lite | 1.000.000.000 |
| Gemini 3.5 Flash | 1.000.000.000 |
| Gemini 2.5 Pro | 1.000.000.000 |
| Gemini 2.5 Pro TTS | 1.000.000 |
| Gemini 2.5 Flash | 1.000.000.000 |
| Bản xem trước Gemini 2.5 Flash | 1.000.000.000 |
| Bản xem trước hình ảnh Gemini 2.5 Flash | 1.000.000.000 |
| Gemini 2.5 Flash TTS | 4.000.000 |
| Gemini 2.5 Flash Lite | 1.000.000.000 |
| Bản xem trước Gemini 2.5 Flash Lite | 1.000.000.000 |
| Gemini 2.0 Flash | 5.000.000.000 |
| Hình ảnh Gemini 2.0 Flash | 1.000.000.000 |
| Gemini 2.0 Flash Lite | 5.000.000.000 |
| Mô hình tạo nội dung đa phương thức | | | | |
| Bản xem trước hình ảnh Gemini 3.1 Flash 🍌 | 750.000.000 |
| Hình ảnh Gemini 3.1 Flash Lite 🍌 | 1.000.000.000 |
| Bản xem trước hình ảnh của Gemini 3 Pro 🍌 | 1.000.000.000 |
| Mô hình nhúng | | | | |
| Gemini Embedding | 10.000.000 |

## Cách nâng cấp lên cấp độ tiếp theo

Để chuyển từ gói Miễn phí sang gói có tính phí, trước tiên, bạn phải [thiết lập thông tin thanh toán trong AI Studio](https://ai.google.dev/gemini-api/docs/billing?hl=vi).

Sau khi dự án của bạn đáp ứng [các tiêu chí được chỉ định](#usage-tiers), dự án đó sẽ tự động được nâng cấp lên cấp tiếp theo. Việc nâng cấp từ gói Miễn phí lên Cấp 1 thường có hiệu lực ngay lập tức, còn các lần nâng cấp cấp độ tiếp theo sẽ có hiệu lực trong vòng 10 phút. Chuyển đến [trang Dự án](https://aistudio.google.com/projects?hl=vi) trong AI Studio để kiểm tra các cấp.

## Yêu cầu tăng giới hạn tốc độ

Mỗi biến thể mô hình đều có một hạn mức liên kết (số yêu cầu mỗi phút, RPM).
Để biết thông tin chi tiết về các giới hạn tốc độ đó, hãy xem trang [Giới hạn tốc độ của AI Studio](https://aistudio.google.com/rate-limit?hl=vi).

[Yêu cầu tăng giới hạn tốc độ cho cấp có tính phí](https://forms.gle/ETzX94k8jf7iSotH9)

Chúng tôi không đảm bảo sẽ tăng hạn mức sử dụng cho bạn, nhưng chúng tôi sẽ cố gắng hết sức để xem xét yêu cầu của bạn.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-03 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-03 UTC."],[],[]]
