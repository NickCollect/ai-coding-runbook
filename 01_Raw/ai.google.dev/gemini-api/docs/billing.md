---
source_url: https://ai.google.dev/gemini-api/docs/billing?hl=vi
fetched_at: 2026-05-18T05:06:26.572403+00:00
title: "L\u1eadp h\u00f3a \u0111\u01a1n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Lập hóa đơn

Hướng dẫn này cung cấp thông tin tổng quan về các lựa chọn tính phí khi dùng Gemini API, giải thích cách bật tính năng thanh toán và theo dõi mức sử dụng, đồng thời giải đáp các câu hỏi thường gặp (FAQ) về việc thanh toán.

## Giới thiệu về việc thanh toán và các cấp

Việc tính phí cho Gemini API dựa trên nhật ký thanh toán của bạn.

| Cấp sử dụng | Vòng loại | [Hạn mức cấp thanh toán](#spend-caps) |
| --- | --- | --- |
| **Free** | [Dự án đang hoạt động](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) hoặc dùng thử miễn phí | Không áp dụng |
| **Cấp 1** | [Thiết lập và liên kết một tài khoản thanh toán đang hoạt động](#setup-billing) | đô la Hong Kong |
| **Cấp 2** | Đã thanh toán 100 USD + 3 ngày kể từ lần thanh toán thành công đầu tiên | $2.000 |
| **Cấp 3** | Thanh toán 1.000 USD + 30 ngày kể từ lần thanh toán thành công đầu tiên | 20.000 – 100.000 đô la Mỹ trở lên |

Các tài khoản mới sẽ bắt đầu ở Cấp miễn phí, cho phép truy cập vào [một số mô hình](https://ai.google.dev/gemini-api/docs/pricing?hl=vi) trong Gemini API và AI Studio, tối đa theo [hạn mức tốc độ](https://aistudio.google.com/rate-limit?hl=vi) của cấp miễn phí của các mô hình.

Để triển khai các ứng dụng ngay từ Chế độ tạo, bạn có thể sử dụng **Bậc khởi đầu của Google Cloud**.
Cấp này cho phép bạn xuất bản tối đa 2 ứng dụng full stack mà không cần thiết lập dự án trên đám mây của Google hoặc tài khoản thanh toán.
Hãy xem phần [Triển khai từ Google AI Studio](https://ai.google.dev/gemini-api/docs/deploying?hl=vi) để biết thông tin chi tiết và tham khảo [tài liệu về Bậc khởi đầu của Google Cloud](https://docs.cloud.google.com/docs/starter-tier?hl=vi) để biết thêm thông tin.

Để truy cập vào hạn mức tốc độ cao hơn, sử dụng các mô hình nâng cao và đảm bảo rằng câu lệnh và câu trả lời của bạn **không** được dùng để cải thiện các sản phẩm của Google\*, bạn có thể [liên kết tài khoản thanh toán](#setup-billing) và [trả trước](#prepay) để chuyển sang Cấp có tính phí.
Sau đó, bạn sẽ chuyển sang các cấp cao hơn dựa trên tổng mức chi tiêu và tuổi tài khoản. Ở Cấp 3, bạn có thể chuyển sang phương thức thanh toán [trả sau](#postpay).

Các cấp, hạn mức và hạn mức tài khoản thanh toán đều được xác định ở cấp [tài khoản thanh toán](#cloud-billing).

\* *Quyền riêng tư đối với dữ liệu cấp doanh nghiệp: Để biết thêm thông tin về việc sử dụng dữ liệu cho các dịch vụ có tính phí, hãy xem [Điều khoản dịch vụ](https://ai.google.dev/gemini-api/terms?hl=vi#data-use-paid).*

## Thiết lập thông tin thanh toán để sử dụng Gói trả phí

Bạn có thể tạo một dự án và thiết lập thông tin thanh toán hoặc nhập một dự án hiện có để nâng cấp lên Cấp có tính phí trong [Google AI Studio](https://aistudio.google.com/projects?hl=vi).
Việc nâng cấp từ Bậc miễn phí lên Bậc trả phí có nghĩa là bạn phải liên kết một tài khoản thanh toán và [trả trước](#prepay) để thêm ít nhất 10 USD (hoặc số tiền tương đương bằng các đơn vị tiền tệ khác) vào tài khoản của mình.

1. Chuyển đến trang [Khoá API](https://aistudio.google.com/api-keys?hl=vi), trang [Dự án](https://aistudio.google.com/projects?hl=vi) hoặc bất kỳ nơi nào bạn thấy nút **Thiết lập thông tin thanh toán** trong AI Studio.
   - Theo mặc định, người dùng mới sẽ có một [dự án và khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) được tạo cho họ.
   - Nếu bạn cần một khoá mới, hãy nhấp vào [**Tạo khoá API**](https://aistudio.google.com/api-keys?hl=vi) rồi làm theo hộp thoại để thêm một cặp khoá-dự án vào bảng.
2. Tìm dự án thuộc Bậc miễn phí mà bạn muốn nâng cấp lên Bậc có tính phí, rồi nhấp vào **Thiết lập thông tin thanh toán** trong cột *Bậc thanh toán*.
3. Nếu bạn chưa từng thiết lập tài khoản thanh toán trên Google:
   - Bạn sẽ được yêu cầu chọn quốc gia của mình để đồng ý với Điều khoản dịch vụ.
   - Sau đó, hãy điền hoặc xác nhận thông tin liên hệ và phương thức thanh toán để tiếp tục.
4. Nếu trước đây bạn đã thiết lập tài khoản thanh toán của Google:
   - Bạn sẽ được yêu cầu chọn trong số các tài khoản thanh toán hiện có.
   - Nếu bạn không muốn sử dụng bất kỳ tài khoản hiện có nào, hãy nhấp vào **Thêm tài khoản thanh toán mới** rồi điền hoặc xác nhận thông tin liên hệ và phương thức thanh toán để tiếp tục.
5. Tiếp theo, bạn sẽ:
   - Được yêu cầu trả trước tối thiểu 100.000 VND để hoàn tất quy trình thiết lập thông tin thanh toán (tức là tài khoản của bạn được tự động chỉ định cho gói thanh toán [Trả trước](#prepay)),
   - Bạn có thể chọn giữa gói thanh toán [Trả trước](#prepay) và [Trả sau](#postpay) cho tài khoản của mình.
   - Được chỉ định cho gói thanh toán [Trả sau](#postpay) trong một khoảng thời gian trung gian cho đến khi hệ thống Trả trước mới được áp dụng cho tất cả người dùng (kể từ ngày 23 tháng 3 năm 2026).
6. Sau khi thanh toán trước hoặc chọn thanh toán sau, bạn đã hoàn tất việc thiết lập tài khoản.

### Nâng cấp lên gói trả phí tiếp theo

Nếu đang sử dụng một gói có tính phí và đáp ứng [các tiêu chí](#about-billing) để thay đổi gói, bạn sẽ được tự động nâng cấp lên gói tiếp theo (tuỳ thuộc vào [thời gian xử lý](#processing-times)).

## Xác minh trạng thái thanh toán

Sau khi [liên kết một tài khoản thanh toán](#setup-billing) với dự án của mình, bạn có thể theo dõi trạng thái của tài khoản đó trên [trang Thanh toán của AI Studio](https://aistudio.google.com/billing?hl=vi). Không giống như bậc miễn phí, trạng thái bậc có tính phí là trạng thái động; mặc dù bậc sử dụng của bạn được xác định dựa trên nhật ký tài khoản, nhưng Gemini API sẽ chỉ xử lý các yêu cầu nếu bạn có số dư tín dụng [Trả trước](#prepay) dương.

Trên trang [Dự án](https://aistudio.google.com/projects?hl=vi), bạn sẽ có thể xem cấp và gói thanh toán của dự án trong cột *Cấp thanh toán*. Mọi thao tác liên quan đến trạng thái thanh toán mà bạn có thể cần thực hiện cho một dự án đều xuất hiện trong cột *Bậc thanh toán* hoặc *Trạng thái*:

- "***Thiết lập thông tin thanh toán***" nếu dự án chưa có tài khoản thanh toán được đính kèm.
- "***Thiết lập phương thức thanh toán trả trước***" nếu dự án có tài khoản thanh toán được đính kèm, nhưng bạn phải sử dụng gói thanh toán [Trả trước](#prepay) cần được thiết lập.
- "***Không có tín dụng***" nếu tài khoản thanh toán cần mua tín dụng nhưng tài khoản thanh toán trả trước chưa được thiết lập hoặc số dư tín dụng hiện có đã hết.

Nhấp vào một trong các thông báo để tiến hành các hành động cần thiết.

## Giám sát mức sử dụng

Bạn có thể theo dõi mức sử dụng Gemini API trong [Google AI Studio](https://aistudio.google.com/usage?hl=vi) trên **Trang tổng quan** > **Mức sử dụng**.

## Gói thanh toán

Các gói thanh toán cho Gemini API và AI Studio được chia thành 2 danh mục để xác định thời điểm bạn thanh toán cho mức sử dụng: Trả trước và Trả sau. Bạn có thể kiểm tra gói thanh toán được chỉ định và quản lý phương thức thanh toán trên trang [Thanh toán cho AI Studio](https://aistudio.google.com/billing?hl=vi).

### Trả trước

Trong gói thanh toán Trả trước, bạn mua tín dụng để nạp vào số dư trả trước trước khi sử dụng Gemini API và chi phí sử dụng API sẽ được trừ vào số dư tín dụng trả trước của bạn [gần như theo thời gian thực](#processing-times).
Bạn có thể trả trước bằng cách [thêm tín dụng](#buy-credits) vào tài khoản hoặc thiết lập tính năng [tự động nạp tiền](#auto-reload). Sau khi bạn mua tín dụng, tín dụng chưa dùng sẽ hết hạn sau 12 tháng và [không hoàn lại được](#refunds), trừ trường hợp sau khi [chuyển sang tài khoản Trả sau](#postpay).

Khi số dư tín dụng trả trước trong tài khoản thanh toán đạt đến 0 USD, tất cả khoá API trong tất cả dự án được liên kết với tài khoản thanh toán đó sẽ ngừng hoạt động cùng một lúc.
Khoản tín dụng trả trước chỉ áp dụng cho chi phí sử dụng Gemini API; bạn không thể dùng khoản tín dụng này để thanh toán cho các dịch vụ khác của Google Cloud.

Người dùng mới sẽ mặc định sử dụng gói thanh toán Trả trước. Những dự án có trước thời điểm ra mắt gói thanh toán trả trước và trả sau có thể cần phải [cập nhật thông tin thanh toán của dự án](#verify-billing) trước khi tiếp tục sử dụng Gemini API.

*Xin lưu ý rằng phương thức Trả trước không dùng được cho tài khoản [Có hoá đơn (hoặc Ngoại tuyến)](https://docs.cloud.google.com/billing/docs/concepts?hl=vi#billing_account_types).*

#### Mua tín dụng

Bạn có thể mua tín dụng theo cách thủ công trước khi sử dụng Gemini API để nạp tín dụng vào số dư tín dụng trong tài khoản Trả trước.

Để mua tín dụng, hãy chuyển đến trang [Thanh toán của AI Studio](https://aistudio.google.com/billing?hl=vi) rồi chọn **Mua tín dụng**.
Số tiền mua hàng tối thiểu là 10 đô la Mỹ. Số tiền tín dụng tối đa mà bạn có thể trả trước là 50.000.000 VND.

#### Tự động nạp tiền

Tự động nạp tiền là một tính năng không bắt buộc, giúp tự động nạp tiền vào số dư tín dụng trả trước của bạn khi số dư này sắp hết. Điều này giúp tránh bị gián đoạn dịch vụ.

Bạn có thể thiết lập tính năng tự động nạp tiền và xem trạng thái tự động nạp tiền trong thẻ *Số tiền tín dụng hiện có* trên trang [Thanh toán trong AI Studio](https://aistudio.google.com/billing?hl=vi). Nhấp vào **Thiết lập tính năng tự động nạp tiền** hoặc **Quản lý tính năng tự động nạp tiền** để thiết lập phương thức thanh toán, số tiền nạp và số dư tối thiểu kích hoạt khoản thanh toán nạp tiền.

### Trả sau

Trong gói thanh toán trả sau, tài khoản thanh toán trên đám mây của bạn sẽ tích luỹ chi phí và bạn sẽ tự động bị tính phí vào cuối tháng hoặc khi chi phí đạt đến [hạn mức chi tiêu được chỉ định tự động](#tier-spend-caps) dựa trên cấp tài khoản của bạn.
Khoản thanh toán sẽ được tính vào phương thức thanh toán được liên kết với tài khoản thanh toán Trả sau của bạn. Bạn có thể quản lý phương thức thanh toán này trên trang [Thanh toán của AI Studio](https://aistudio.google.com/billing?hl=vi).

Khi đáp ứng [các tiêu chí của Cấp 3](#about-billing), bạn có thể chuyển từ gói Trả trước sang gói Trả sau theo cách thủ công. Để thay đổi gói, bạn cần nhấp vào nút **Chuyển sang trả sau** xuất hiện ở trên cùng bên phải của trang [Thanh toán trong AI Studio](https://aistudio.google.com/billing?hl=vi) khi tài khoản của bạn đủ điều kiện.

Sau đó, trên trang **Thanh toán**, bạn có thể xem số dư, ngày đến hạn và các khoản thanh toán trước đây, cũng như thực hiện thanh toán và quản lý phương thức thanh toán.

Khi [thiết lập thông tin thanh toán](#setup-billing) cho một dự án mới, nếu đủ điều kiện sử dụng phương thức thanh toán trả sau, bạn sẽ có thể chọn giữa phương thức thanh toán trả trước và trả sau trong hộp thoại [thiết lập thông tin thanh toán](#setup-billing).

Sau khi bạn chuyển một tài khoản thanh toán trên Cloud sang sử dụng gói thanh toán Trả sau, tất cả các dự án được liên kết với tài khoản thanh toán đó sẽ được chuyển sang gói Trả sau. Bạn không thể chuyển tài khoản thanh toán đó về lại gói thanh toán trả trước. Bạn có thể di chuyển một dự án sang tài khoản thanh toán có gói thanh toán khác để thay đổi chu kỳ tính phí cho dự án đó; hãy truy cập vào tài liệu trên Cloud về [cách quản lý hoạt động thanh toán cho dự án](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi).

Bạn có thể tìm hiểu thêm về chu kỳ tính phí Postpay trong [hướng dẫn về Thanh toán trên đám mây](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=vi).

## Mức chi tiêu

Gemini API hỗ trợ hạn mức chi tiêu hằng tháng ở cả cấp tài khoản thanh toán và cấp dự án. Các chế độ kiểm soát này được thiết kế để bảo vệ tài khoản của bạn khỏi tình trạng sử dụng quá mức ngoài dự kiến và bảo vệ hệ sinh thái để đảm bảo dịch vụ luôn hoạt động.

*Xin lưu ý rằng hạn mức chi tiêu không dùng được cho tài khoản [Có hoá đơn (hoặc Ngoại tuyến)](https://docs.cloud.google.com/billing/docs/concepts?hl=vi#billing_account_types).*

### Giới hạn chi tiêu dự kiến

Bạn có thể đặt hạn mức chi tiêu [ở cấp dự án](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) trong AI Studio.
Điều này sẽ hữu ích nếu bạn có nhiều dự án trong cùng một tài khoản thanh toán và muốn đảm bảo mỗi dự án đều có đủ hạn mức chi tiêu tích luỹ.

Những tài khoản có [vai trò](https://docs.cloud.google.com/iam/docs/roles-overview?hl=vi) người chỉnh sửa, chủ sở hữu hoặc quản trị viên dự án có thể đặt hạn mức chi tiêu cho mỗi dự án trong AI Studio trên trang [Chi tiêu](https://aistudio.google.com/spend?hl=vi) trong phần **Hạn mức chi tiêu hằng tháng** > **Chỉnh sửa hạn mức chi tiêu**.

Nếu bạn [chuyển một dự án sang một tài khoản thanh toán khác](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi#change_the_billing_account_for_a_project), thì mọi hạn mức chi tiêu mà bạn đã đặt cho dự án đó sẽ vẫn giữ nguyên, nhưng mọi khoản chi tiêu tích luỹ sẽ được đặt lại thành 0 USD cho chu kỳ thanh toán mới.

Việc hoàn tất ở [chế độ hàng loạt](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi) vẫn có thể phát sinh phí vượt mức.

Thời gian xử lý dữ liệu thanh toán trong AI Studio có thể bị chậm trễ một chút, tối đa khoảng 10 phút. Bạn có thể phát sinh thêm chi phí ngoài hạn mức dự án nếu dữ liệu thanh toán chưa được xử lý trước khi phát sinh thêm các khoản phí.

### Hạn mức chi tiêu theo cấp của tài khoản thanh toán

Mỗi [bậc](#about-billing) đều có hạn mức chi tiêu tối đa hằng tháng:

| Cấp sử dụng | Giới hạn chi tiêu |
| --- | --- |
| **Free** | Không áp dụng |
| **Cấp 1** | đô la Hong Kong |
| **Cấp 2** | $2.000 |
| **Cấp 3** | 20.000 – 100.000 đô la Mỹ |

Hạn mức sử dụng hằng tháng được áp dụng cho Gemini API ở cấp [tài khoản thanh toán](#cloud-billing). Mặc dù hạn mức mặc định được đặt sẵn, nhưng bạn có thể [yêu cầu tăng hạn mức](https://docs.google.com/forms/d/e/1FAIpQLSdiP6BWJyNNN65lnwnlOr-5Kv0MOFp0jLQyqi_ixVCfddqWBw/viewform?hl=vi) để đáp ứng nhu cầu sử dụng cao hơn. Tổng mức chi tiêu được tổng hợp trên tất cả các dự án được liên kết có bật dịch vụ Gemini API. Sau khi tổng tài khoản tích luỹ đạt đến hạn mức bậc, dịch vụ sẽ bị tạm dừng cho tất cả các dự án được liên kết với tài khoản thanh toán đó cho đến khi bắt đầu chu kỳ thanh toán tiếp theo (ngày 1 của mỗi tháng).

#### Đánh giá mức chi tiêu của tài khoản thanh toán

Để đánh giá mức chi tiêu hằng tháng trước đây nhằm xác định xem [hạn mức chi tiêu theo cấp độ Tài khoản thanh toán](#tier-spend-caps) mới có ảnh hưởng đến các dự án đang diễn ra của bạn hay không, hãy làm theo các bước sau:

1. Trong bảng điều khiển Google Cloud, hãy xem trang [Báo cáo tài khoản thanh toán Cloud](https://console.cloud.google.com/billing/reports?hl=vi).
   - Nếu bạn có nhiều tài khoản thanh toán, hãy chọn tài khoản thanh toán Cloud mà bạn muốn xem báo cáo chi phí khi được nhắc.
2. Theo mặc định, báo cáo sẽ là "Nhóm theo dịch vụ" trong "Tháng hiện tại". Bạn sẽ thấy **Gemini API** trong cột **Dịch vụ** và tổng mức chi tiêu trong cột **Chi phí sử dụng** của bảng.
3. Để xem chi phí chi tiết chỉ giới hạn ở mức sử dụng Gemini API, hãy đặt bộ lọc **Nhóm theo** để nhóm theo **SKU** và bộ lọc **Dịch vụ** thành **Gemini API**.
4. Điều chỉnh bộ lọc **Phạm vi thời gian theo ngày sử dụng** thành phạm vi bạn muốn để đánh giá mức chi tiêu trước đây trong một khoảng thời gian.

## Thời gian xử lý

Các tín hiệu và thông tin cập nhật về việc thanh toán không phải lúc nào cũng diễn ra theo thời gian thực.

- **Mức sử dụng tín dụng**: Chi phí sử dụng thường được trừ vào số dư của bạn trong vòng vài phút.
- **Xác nhận thanh toán**: Mặc dù hầu hết các khoản thanh toán bằng thẻ đều được xử lý ngay lập tức, nhưng một số phương thức thanh toán (như chuyển khoản ngân hàng) có thể mất vài ngày để xử lý. Các dịch vụ chỉ tiếp tục hoặc nâng cấp sau khi giao dịch mua tín dụng được xác nhận chính thức.
- **Nâng cấp cấp độ**: Sau khi bạn thanh toán thành công hoặc khi bạn đáp ứng [các tiêu chí nâng cấp](#about-billing), hệ thống thường sẽ nâng cấp cấp độ trong vòng 10 phút.
- **Biểu đồ phân tích tổng chi phí**: Biểu đồ cho thấy thông tin phân tích tổng chi phí của bạn trên cả trang [Thanh toán](https://aistudio.google.com/billing?hl=vi) và trang [Chi tiêu](https://aistudio.google.com/spend?hl=vi) có thể mất đến 24 giờ để cập nhật.

Hãy đọc hướng dẫn về Cloud Billing liên quan đến [chu kỳ tính phí](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=vi#delayed-billing) và độ trễ [giao dịch](https://docs.cloud.google.com/billing/docs/how-to/view-history?hl=vi#missing-transactions) để tìm hiểu thêm về các trường hợp có thể bị chậm trễ trong việc lập hoá đơn.

## Hoàn tiền

Bạn không được hoàn tiền cho tài khoản thanh toán **Trả trước**, trừ trường hợp chuyển đổi loại tài khoản.

**Khi tài khoản Trả trước chuyển sang loại tài khoản Trả sau** (sau khi bạn đáp ứng [các tiêu chí](#about-billing) và [nâng cấp tài khoản theo cách thủ công](#postpay)), tài khoản Trả trước sẽ bị đóng và mọi khoản tín dụng trả trước còn lại sẽ tự động được hoàn lại vào phương thức thanh toán trong hồ sơ.

Nếu bạn [đóng](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=vi#close-a-billing-account) tài khoản Trả trước vì bất kỳ lý do nào khác ngoài việc nâng cấp lên tài khoản Trả sau, mọi khoản tín dụng trả trước còn lại sẽ bị mất.

Khoản tín dụng đã mua sẽ hết hạn sau 1 năm. Sau khi hết hạn, các khoản tín dụng sẽ bị mất và không thể lấy lại.

Tài khoản **trả sau** tuân theo [chính sách hoàn tiền của Google Cloud](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=vi#request_a_refund).

## Tài khoản thanh toán trên Cloud

Gemini API sử dụng [tài khoản Cloud Billing](https://cloud.google.com/billing/docs/concepts?hl=vi) cho các dịch vụ thanh toán. Bạn có thể [thiết lập tài khoản này ngay trong AI Studio](#setup-billing).
Bạn có thể sử dụng AI Studio để theo dõi mức chi tiêu, tìm hiểu chi phí và thanh toán.

Các cấp, hạn mức tốc độ và hạn mức tài khoản thanh toán đều được xác định ở cấp tài khoản thanh toán.

### Dự án và khoá API

Tất cả [dự án](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#google-cloud-projects) được liên kết với một tài khoản Thanh toán trên đám mây đều kế thừa cấp sử dụng của tài khoản thanh toán và các giới hạn về tỷ lệ cũng như hạn mức tài khoản được liên kết. Nếu bạn [thay đổi dự án](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi#change_the_billing_account_for_a_project) từ tài khoản thanh toán này sang tài khoản thanh toán khác, thì cấp của dự án đó, cũng như hạn mức tốc độ và hạn mức tài khoản, sẽ chuyển sang cấp của tài khoản thanh toán mới.

Tổng mức chi tiêu (cho tất cả các sản phẩm của Google Cloud) và tuổi tài khoản trên tất cả các dự án được liên kết với một tài khoản thanh toán sẽ được tính vào [điều kiện để đạt được cấp](#about-billing) của tài khoản thanh toán đó.

Bạn có thể [huỷ liên kết một dự án](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi#disable_billing_for_a_project) khỏi tài khoản thanh toán của dự án đó để quay lại bậc miễn phí.

[Khoá API](https://ai.google.dev/gemini-api/docs/api-key?hl=vi) là thông tin xác thực được tạo trong một dự án.
Chúng không có chế độ cài đặt thanh toán độc lập; chúng kế thừa hạn mức theo cấp và trạng thái thanh toán của dự án. Mức sử dụng tích luỹ của tất cả các khoá trong một dự án sẽ được tính vào hạn mức chi tiêu của dự án đó và tổng mức chi tiêu của tài khoản thanh toán.

## Câu hỏi thường gặp

Các phần sau đây cung cấp câu trả lời cho các câu hỏi thường gặp.

### Tôi bị tính phí cho những khoản nào?

Giá của Gemini API dựa trên những yếu tố sau:

- Số lượng mã thông báo đầu vào
- Số lượng mã thông báo đầu ra
- Số lượng mã thông báo được lưu vào bộ nhớ đệm
- Khoảng thời gian lưu trữ mã thông báo được lưu vào bộ nhớ đệm

Để biết thông tin về giá, hãy xem [trang Giá](https://ai.google.dev/pricing?hl=vi).

### Tôi có thể xem hạn mức của mình ở đâu?

Bạn có thể xem hạn mức và giới hạn hệ thống trong [AI Studio](https://aistudio.google.com/usage?hl=vi).

### Làm cách nào để chuyển sang cấp hạn mức tốc độ cao hơn hoặc yêu cầu thêm hạn mức?

Bạn sẽ tự động được cấp thêm hạn mức khi tài khoản của bạn đạt đến [yêu cầu về cấp độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi#usage-tiers) tiếp theo.

### Tôi có thể sử dụng Gemini API miễn phí ở Khu vực kinh tế Châu Âu (bao gồm cả Liên minh Châu Âu), Vương quốc Anh và Thuỵ Sĩ không?

Có. Chúng tôi cung cấp gói miễn phí và gói có tính phí ở [nhiều khu vực](https://ai.google.dev/gemini-api/docs/available-regions?hl=vi).

### Nếu thiết lập thông tin thanh toán cho Gemini API, tôi có bị tính phí khi sử dụng Google AI Studio không?

Người dùng vẫn có thể sử dụng AI Studio miễn phí, trừ phi họ liên kết một khoá API có tính phí để truy cập vào các tính năng có tính phí.
Sau khi liên kết một khoá API có tính phí trong một dự án có tính phí trong AI Studio, bạn sẽ bị tính phí sử dụng AI Studio cho khoá đó. Bạn có thể chuyển đổi giữa các dự án thuộc Cấp có tính phí và các dự án thuộc Cấp miễn phí khi cần bằng cách sử dụng các khoá API tương ứng được liên kết với từng loại.

### Nếu đang sử dụng Bậc miễn phí, làm cách nào để nâng cấp lên các bậc cao hơn?

Để sử dụng các cấp cao hơn, bạn phải thiết lập thông tin thanh toán cho dự án của mình. Nhấp vào [**Thiết lập thông tin thanh toán**](#setup-billing) trong Google AI Studio. Thao tác này sẽ hướng dẫn bạn chọn hoặc tạo một tài khoản thanh toán trên Cloud. Nếu bạn bắt buộc phải sử dụng mô hình thanh toán trả trước, thì quy trình **Thiết lập thông tin thanh toán** sẽ hướng dẫn bạn thực hiện quy trình tạo tài khoản Trả trước được liên kết với tài khoản thanh toán Cloud của bạn.

### Tôi có thể sử dụng 1 triệu mã thông báo trong gói miễn phí không?

Cấp miễn phí cho Gemini API sẽ khác nhau tuỳ thuộc vào mô hình được chọn. Hiện tại, bạn có thể dùng cửa sổ ngữ cảnh 1 triệu token theo những cách sau:

- Trong Google AI Studio
- Với các gói miễn phí cho một số mẫu xe
- Với gói trả sau

### Tôi có thể quay lại Gói miễn phí sau khi nâng cấp lên các gói cao hơn (trả phí) không?

Để hạ cấp xuống Bậc miễn phí, bạn có thể [tắt tính năng thanh toán](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi#disable_billing_for_a_project) trên từng dự án mà bạn muốn hạ cấp.

### Làm cách nào để tính số lượng mã thông báo mà tôi đang sử dụng?

Sử dụng phương thức [`GenerativeModel.count_tokens`](https://ai.google.dev/api/python/google/generativeai/GenerativeModel?hl=vi#count_tokens) để đếm số lượng mã thông báo. Hãy tham khảo [Hướng dẫn về mã thông báo](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) để tìm hiểu thêm về mã thông báo.

### Nếu đăng ký Tài khoản thanh toán trên đám mây đầu tiên thông qua AI Studio, tôi có được dùng thử miễn phí Google Cloud không?

Khi bạn đăng ký Tài khoản thanh toán trên Cloud lần đầu tiên, [Bản dùng thử miễn phí của Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=vi#free-trial) sẽ bắt đầu và bạn sẽ được cấp [Khoản tín dụng chào mừng](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=vi#welcome-credits) trị giá 300 đô la.
Tuy nhiên, bạn không thể dùng những khoản tín dụng đó để thanh toán cho việc sử dụng AI Studio. Bạn có thể sử dụng khoản tín dụng Chào mừng để thanh toán cho các dịch vụ đủ điều kiện khác trong Google Cloud (xin lưu ý rằng sau khi bạn sử dụng hết hoặc khoản tín dụng hết hạn (trong vòng 90 ngày), mọi chi phí sử dụng bổ sung sẽ tự động được tính vào phương thức thanh toán mà bạn đã thiết lập).

### Tôi có thể sử dụng tín dụng chào mừng của Google Cloud với Gemini API không?

Không, bạn không thể dùng [Khoản tín dụng chào mừng](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=vi#welcome-credits) hoặc khoản tín dụng dùng thử miễn phí của Google Cloud cho Gemini API hoặc AI Studio.

Nếu được cấp tín dụng chào mừng của Google Cloud trước khi không đủ điều kiện, bạn vẫn có thể chi tiêu số tín dụng còn lại cho Gemini API và AI Studio cho đến khi tín dụng hết hạn (sau 90 ngày).

### Chương trình Dùng thử miễn phí của Google Cloud có áp dụng cho việc sử dụng Gemini API không?

Không. Kể từ tháng 3 năm 2026, chi phí sử dụng Gemini API sẽ không được tính vào chương trình [Dùng thử miễn phí Google Cloud trị giá 300 USD](https://docs.cloud.google.com/free/docs/free-cloud-features?hl=vi#free-trial).

### Việc thanh toán được xử lý như thế nào?

Hệ thống [Thanh toán trên Google Cloud](https://cloud.google.com/billing/docs/concepts?hl=vi) sẽ xử lý việc thanh toán cho Gemini API. Tìm hiểu về chế độ thiết lập Thanh toán trên đám mây trong sản phẩm trong [tài liệu về Thanh toán trên đám mây](https://docs.cloud.google.com/billing/docs/in-product-billing-setup?hl=vi).

### Tôi có bị tính phí cho các yêu cầu không thực hiện được không?

Nếu yêu cầu của bạn không thành công và gặp lỗi 400 hoặc 500, bạn sẽ không bị tính phí cho các mã thông báo đã dùng. Tuy nhiên, yêu cầu này vẫn được tính vào hạn mức của bạn.

### `GetTokens` có bị tính phí không?

Các yêu cầu gửi đến API `GetTokens` không bị tính phí và không được tính vào hạn mức suy luận.

### Dữ liệu của tôi trên Google AI Studio được xử lý như thế nào nếu tôi có tài khoản API trả phí?

Tham khảo [Điều khoản dịch vụ](https://ai.google.dev/gemini-api/terms?hl=vi#paid-services) để biết thông tin chi tiết về cách dữ liệu được xử lý khi bạn bật tính năng thanh toán qua Cloud (xem phần "Cách Google sử dụng dữ liệu của bạn" trong mục "Dịch vụ có tính phí"). Xin lưu ý rằng các câu lệnh của bạn trên Google AI Studio sẽ được xử lý theo các điều khoản tương tự như "Dịch vụ có tính phí" miễn là có ít nhất 1 dự án API đã bật tính năng thanh toán. Bạn có thể xác thực điều này trên [trang khoá Gemini API](https://aistudio.google.com/api-keys?hl=vi) nếu thấy bất kỳ dự án nào được đánh dấu là "Có tính phí" trong mục "Gói".

### Thanh toán trả trước là gì và những ai phải sử dụng mô hình thanh toán trả trước?

Tính năng thanh toán trả trước cho phép người dùng Gemini API trong AI Studio mua trước tín dụng.
Kể từ ngày 23 tháng 3 năm 2026, người dùng mới của AI Studio có thể phải sử dụng gói thanh toán trả trước. Trong quá trình [Thiết lập thông tin thanh toán](#setup-billing) trên AI Studio, giao diện người dùng sẽ hướng dẫn bạn thực hiện quy trình thiết lập thông tin thanh toán và cho biết liệu bạn có phải trả trước hay không.

### Làm cách nào để mua tín dụng trả trước và có hạn mức tối thiểu hoặc tối đa không?

Bạn có thể [mua tín dụng](#buy-credits) trên trang Thanh toán của AI Studio. Trong quá trình mua, giao diện người dùng sẽ cung cấp số tiền tối thiểu cần có trước khi mua theo khu vực và cấp độ của bạn, cũng như số tiền tối đa có thể có trong tài khoản của bạn tại một thời điểm.

### Tôi có thể định cấu hình tài khoản trả trước để tự động mua thêm tín dụng khi cần không?

Có, bạn nên thiết lập chế độ [tự động nạp tiền](#auto-reload) trong phần Cài đặt thanh toán của AI Studio. Bạn chỉ định số dư tín dụng "kích hoạt" (ví dụ: "khi số dư của tôi thấp hơn 30 USD") và "giá trị nạp lại" (ví dụ: "thêm 100 USD").

### Tôi có thể yêu cầu hoàn tiền cho phần tín dụng chưa sử dụng không?

Tất cả các khoản tín dụng API trả trước đều hết hạn sau 1 năm và không được hoàn tiền. Đọc [chính sách hoàn tiền cho tài khoản trả trước](#refunds).

### Các khoản tín dụng trả trước của tôi có hết hạn không?

Có, tín dụng sẽ hết hạn sau 12 tháng kể từ ngày mua.

### Điều gì sẽ xảy ra khi số dư tín dụng trả trước của tôi đạt mức 0?

Tất cả các dịch vụ Gemini API trong mọi dự án được thanh toán bằng tài khoản Thanh toán trước trên Google Cloud đó sẽ ngừng hoạt động ngay lập tức để tránh phát sinh thêm phí. Các dự án của bạn sẽ không tự động hạ cấp xuống Hạng miễn phí.

Để khôi phục dịch vụ ở Cấp có tính phí hiện tại, bạn phải [mua thêm tín dụng](#buy-credits). Sau khi mua tín dụng, bạn có thể sử dụng Gemini API. Xin lưu ý rằng có thể có [độ trễ](#processing-times) trong khi hệ thống của chúng tôi cập nhật để phản ánh số dư tín dụng của bạn.

Nếu muốn hạ cấp xuống Bậc miễn phí, bạn có thể [tắt tính năng thanh toán](https://docs.cloud.google.com/billing/docs/how-to/modify-project?hl=vi#disable_billing_for_a_project) cho các dự án mà bạn muốn hạ cấp.

### Tại sao mức sử dụng của tôi dừng lại mặc dù số dư tín dụng trả trước của tôi lớn hơn 0?

Bạn có thể đã đạt đến [hạn mức sử dụng](#tier-spend-caps) cho cấp hiện tại.
Hạn mức sử dụng sẽ tự động tăng lên khi bạn chuyển sang các cấp cao hơn. Mức sử dụng Gemini API trong AI Studio cũng có thể bị ảnh hưởng do [trạng thái của tài khoản thanh toán trên Cloud](#missed-payment).

### Tại sao số dư tín dụng trong tài khoản trả trước của tôi lại là số âm?

Do hệ thống thanh toán và xử lý phức tạp của chúng tôi, có thể xảy ra [tình trạng chậm trễ](#processing-times) trong việc chúng tôi ngừng tính phí mức sử dụng sau khi bạn sử dụng hết tất cả các khoản tín dụng. Mức sử dụng vượt quá này có thể xuất hiện dưới dạng số dư tín dụng âm trong trang tổng quan thanh toán của AI Studio. Nếu điều này xảy ra, dịch vụ của bạn sẽ bị tạm dừng và số dư âm sẽ được trừ vào lần mua tín dụng tiếp theo của bạn.

Để tránh bị tạm dừng dịch vụ Gemini API, bạn nên thiết lập tính năng [tự động nạp tiền](#auto-reload) để tự động mua thêm tín dụng khi số dư tín dụng của bạn thấp hơn một giá trị mà bạn chỉ định.

### Tôi có thể sử dụng khoản tín dụng trả trước cho các dịch vụ khác của Google Cloud, chẳng hạn như Nền tảng tác nhân Gemini Enterprise không?

Không. Khoản tín dụng trả trước chỉ được dùng cho việc sử dụng Gemini API. Mọi dịch vụ khác của Google Cloud mà bạn sử dụng (Điện toán, Lưu trữ, Nền tảng tác nhân Gemini Enterprise) đều được tính phí theo [chu kỳ tính phí tiêu chuẩn của Cloud](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=vi).

### Tôi có thể chuyển sang gói thanh toán trả sau không?

Khi đã có nhật ký thanh toán và [đạt đến bậc đủ điều kiện](#about-billing) để sử dụng gói thanh toán Trả sau, bạn có thể chọn chuyển tất cả các khoản phí sử dụng Gemini API trong tương lai sang [chu kỳ tính phí Trả sau](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=vi#view-your-charging-cycle) tiêu chuẩn, hợp nhất của Google Cloud.

### Điều gì sẽ xảy ra với các khoản tín dụng trả trước của tôi nếu tôi chuyển sang gói trả sau?

Khi bạn nâng cấp lên gói [Trả sau](#postpay), Cloud Billing sẽ đóng tài khoản thanh toán Trả trước của bạn, tắt tính năng [tự động nạp tiền](#auto-reload) và tự động hoàn tiền cho mọi khoản tín dụng Trả trước chưa sử dụng (tuỳ thuộc vào thời gian xử lý hoàn tiền tiêu chuẩn).

### Tôi có thể xem số dư tín dụng trả trước hiện tại và nhật ký giao dịch ở đâu?

Bạn phải quản lý số dư và xem nhật ký giao dịch của Gemini API ngay trong thẻ Thanh toán của Google AI Studio.

### Tại sao tôi thấy thông báo "Loại tài khoản thanh toán không hoạt động hoặc không được hỗ trợ"?

Các hoạt động thanh toán trên [trang Thanh toán của AI Studio](https://aistudio.google.com/billing?hl=vi) có thể bị chặn và thay thế bằng thông báo "Loại tài khoản thanh toán không hoạt động hoặc không được hỗ trợ" nếu loại tài khoản thanh toán hoặc trạng thái tài khoản thanh toán mà bạn chọn không đủ điều kiện sử dụng Cấp có tính phí trong AI Studio.

Kiểm tra [Cloud Console](https://console.cloud.google.com/billing/?hl=vi) để xem trạng thái của tài khoản thanh toán. Một loại tài khoản không đủ điều kiện có thể là *Tài khoản dùng thử miễn phí*. Trong trường hợp này, bạn có thể [kích hoạt tính năng thanh toán](#setup-billing) trong AI Studio để đủ điều kiện. Một trạng thái không hoạt động có thể là *Đã đóng*. Trong trường hợp này, bạn có thể [mở lại tài khoản](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account?hl=vi).

### Chi phí sử dụng Gemini API của tôi có xuất hiện trong bảng điều khiển Cloud không?

Có, bạn có thể xem chi phí của Gemini API cùng với chi phí liên quan đến mọi dịch vụ khác của Google Cloud mà tài khoản thanh toán Cloud của bạn thanh toán trên [các trang Quản lý chi phí](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle?hl=vi#cost-reports) trong [bảng điều khiển Thanh toán Cloud](https://console.cloud.google.com/billing?hl=vi). Xin lưu ý rằng bạn chỉ có thể quản lý số dư tín dụng trả trước trong AI Studio.

### Tại sao mức sử dụng Gemini API của tôi không xuất hiện trong Cloud Billing Console, mặc dù tôi có thể thấy mức sử dụng này trong phần Thanh toán của AI Studio, cùng với mức sử dụng tín dụng của tôi?

Google Cloud và AI Studio báo cáo dữ liệu sử dụng cho Cloud Billing theo các khoảng thời gian khác nhau. Do hệ thống thanh toán và xử lý của chúng tôi khá phức tạp, nên có thể bạn sẽ thấy độ trễ giữa thời điểm bạn sử dụng dịch vụ và thời điểm bạn có thể xem mức sử dụng cũng như chi phí trong phần Thanh toán trên Cloud. Thông thường, thông tin chi tiết về chi phí sẽ có trong vòng một ngày, nhưng đôi khi có thể mất hơn 24 giờ.
Tìm hiểu thêm về tính năng thanh toán chậm trong [tài liệu về Thanh toán trên đám mây](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle?hl=vi#delayed-billing).

### Nếu tôi sử dụng các dịch vụ khác của Google Cloud có chi phí phải chịu chu kỳ tính phí trả sau, thì điều gì sẽ xảy ra nếu tôi không thanh toán đúng hạn?

Nếu không thanh toán cho các dịch vụ khác của Google Cloud, bạn có thể bị tạm ngưng quyền truy cập vào Gemini API trong AI Studio, **bất kể bạn có bao nhiêu tín dụng trả trước**. Việc sử dụng AI Studio được hỗ trợ bởi một tài khoản thanh toán Google Cloud. Tài khoản này có thể dùng cả phương thức thanh toán trả trước cho AI Studio và thanh toán trả sau cho các dịch vụ khác trên Cloud. Vấn đề về số dư trả sau sẽ tạm dừng tất cả dịch vụ liên kết với tài khoản đó. Việc sử dụng Gemini API của bạn sẽ bị tạm ngưng nếu Tài khoản thanh toán trên Cloud của bạn bị gắn cờ vì các vấn đề như:

- Số dư quá hạn hoặc chưa thanh toán
- Khoản thanh toán bị từ chối
- Phương thức thanh toán không hợp lệ hoặc đã hết hạn

Để khôi phục dịch vụ, bạn phải [giải quyết vấn đề về tài khoản trả sau](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues?hl=vi#resolving-declined-payments) trong bảng điều khiển Thanh toán của Google Cloud. Sau khi giải quyết vấn đề, bạn sẽ lấy lại được quyền truy cập vào các khoản tín dụng và dịch vụ Gemini API trả trước.

### Tôi có thể yêu cầu trợ giúp về việc thanh toán ở đâu?

Để được trợ giúp về việc thanh toán, hãy xem phần [Yêu cầu hỗ trợ về việc thanh toán trên Cloud](https://cloud.google.com/support/billing?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-16 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-16 UTC."],[],[]]
