---
source_url: https://ai.google.dev/gemini-api/docs/long-context?hl=vi
fetched_at: 2026-05-05T13:17:24.969219+00:00
title: "Ng\u1eef c\u1ea3nh d\u00e0i \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/Tính năng Nghiên cứu chuyên sâu của Gemini) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

- [Trang chủ](https://ai.google.dev/gemini-api/docs/Trang chủ)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/Tài liệu)

Gửi ý kiến phản hồi

# Ngữ cảnh dài

Nhiều mô hình Gemini có cửa sổ ngữ cảnh lớn gồm 1 triệu token trở lên.
Trước đây, các mô hình ngôn ngữ lớn (LLM) bị hạn chế đáng kể về lượng văn bản (hoặc token) có thể được truyền đến mô hình cùng một lúc.
Cửa sổ ngữ cảnh dài của Gemini mở ra nhiều trường hợp sử dụng và mô hình nhà phát triển mới.

Mã mà bạn đã sử dụng cho các trường hợp như [văn bản
tạo](https://ai.google.dev/gemini-api/docs/văn bảntạo) hoặc [đa phương thức
đầu vào](https://ai.google.dev/gemini-api/docs/đa phương thứcđầu vào) sẽ hoạt động mà không cần thay đổi gì với ngữ cảnh dài.

Tài liệu này cung cấp cho bạn thông tin tổng quan về những gì bạn có thể đạt được khi sử dụng các mô hình có cửa sổ ngữ cảnh gồm 1 triệu token trở lên. Trang này cung cấp thông tin tổng quan ngắn gọn về cửa sổ ngữ cảnh, đồng thời khám phá cách nhà phát triển nên suy nghĩ về ngữ cảnh dài, các trường hợp sử dụng ngữ cảnh dài trong thế giới thực và cách tối ưu hoá việc sử dụng ngữ cảnh dài.

Để biết kích thước cửa sổ ngữ cảnh của các mô hình cụ thể, hãy xem trang
[Mô hình](https://ai.google.dev/gemini-api/docs/Mô hình).

## Cửa sổ ngữ cảnh là gì?

Cách cơ bản để bạn sử dụng các mô hình Gemini là truyền thông tin (ngữ cảnh) đến mô hình. Sau đó, mô hình sẽ tạo ra phản hồi. Bạn có thể hình dung cửa sổ ngữ cảnh giống như trí nhớ ngắn hạn. Bộ nhớ ngắn hạn của một người chỉ có thể lưu trữ một lượng thông tin có hạn và điều này cũng đúng với các mô hình tạo sinh.

Bạn có thể đọc thêm về cách các mô hình hoạt động ở bên trong trong hướng dẫn về [mô hình tạo sinh](https://ai.google.dev/gemini-api/docs/mô hình tạo sinh).

## Bắt đầu sử dụng ngữ cảnh dài

Các phiên bản trước của mô hình tạo sinh chỉ có thể xử lý 8.000 token cùng một lúc. Các mô hình mới hơn đã đẩy con số này lên cao hơn bằng cách chấp nhận 32.000 hoặc thậm chí 128.000 token. Gemini là mô hình đầu tiên có khả năng chấp nhận 1 triệu token.

Trong thực tế, 1 triệu token sẽ có dạng như sau:

- 50.000 dòng mã (với 80 ký tự tiêu chuẩn mỗi dòng)
- Tất cả tin nhắn văn bản bạn đã gửi trong 5 năm qua
- 8 tiểu thuyết tiếng Anh có độ dài trung bình
- Bản chép lời của hơn 200 tập podcast có độ dài trung bình

Các cửa sổ ngữ cảnh hạn chế hơn thường thấy trong nhiều mô hình khác thường yêu cầu các chiến lược như tự ý loại bỏ tin nhắn cũ, tóm tắt nội dung, sử dụng RAG với cơ sở dữ liệu vectơ hoặc lọc câu lệnh để lưu token.

Mặc dù các kỹ thuật này vẫn có giá trị trong các trường hợp cụ thể, nhưng cửa sổ ngữ cảnh mở rộng của Gemini mời bạn áp dụng một phương pháp trực tiếp hơn: cung cấp trước tất cả thông tin có liên quan. Vì các mô hình Gemini được xây dựng có mục đích với khả năng ngữ cảnh lớn, nên chúng thể hiện khả năng học tập mạnh mẽ trong ngữ cảnh. [Ví dụ: chỉ sử dụng tài liệu hướng dẫn trong ngữ cảnh (một ngữ pháp tham khảo gồm 500 trang, một từ điển và ≈400 câu song song), Gemini đã học cách dịch từ tiếng Anh sang tiếng Kalamang – một ngôn ngữ Papua có ít hơn 200 người nói – với chất lượng tương tự như một người học là con người sử dụng cùng tài liệu.](https://ai.google.dev/gemini-api/docs/Ví dụ: chỉ sử dụng tài liệu hướng dẫn trong ngữ cảnh (một ngữ pháp tham khảo gồm 500 trang, một từ điển và ≈400 câu song song), Gemini đã học cách dịch từ tiếng Anh sang tiếng Kalamang – một ngôn ngữ Papua có ít hơn 200 người nói – với chất lượng tương tự như một người học là con người sử dụng cùng tài liệu.) Điều này minh hoạ sự thay đổi mô hình do ngữ cảnh dài của Gemini mang lại, mở ra những khả năng mới thông qua việc học tập mạnh mẽ trong ngữ cảnh.

## Các trường hợp sử dụng ngữ cảnh dài

Mặc dù trường hợp sử dụng tiêu chuẩn cho hầu hết các mô hình tạo sinh vẫn là dữ liệu đầu vào văn bản, nhưng họ mô hình Gemini cho phép một mô hình mới về các trường hợp sử dụng đa phương thức. Các mô hình này có thể hiểu được văn bản, video, âm thanh và hình ảnh một cách tự nhiên. Chúng đi kèm với [Gemini API, API này nhận các loại tệp đa phương thức để thuận tiện.](https://ai.google.dev/gemini-api/docs/Gemini API, API này nhận các loại tệp đa phương thức để thuận tiện.)

### Văn bản dài

Văn bản đã chứng tỏ là lớp trí tuệ làm nền tảng cho phần lớn động lực xung quanh LLM. Như đã đề cập trước đó, phần lớn hạn chế thực tế của LLM là do không có cửa sổ ngữ cảnh đủ lớn để thực hiện một số tác vụ. Điều này dẫn đến việc nhanh chóng áp dụng thế hệ tăng cường khả năng truy xuất (RAG) và các kỹ thuật khác giúp cung cấp cho mô hình thông tin theo ngữ cảnh có liên quan một cách linh hoạt. Giờ đây, với các cửa sổ ngữ cảnh ngày càng lớn hơn, các kỹ thuật mới đang trở nên khả dụng, mở ra các trường hợp sử dụng mới.

Sau đây là một số trường hợp sử dụng mới nổi và tiêu chuẩn cho ngữ cảnh dài dựa trên văn bản:

- Tóm tắt các tập hợp văn bản lớn
  - Các lựa chọn tóm tắt trước đây với các mô hình ngữ cảnh nhỏ hơn sẽ yêu cầu một cửa sổ trượt hoặc một kỹ thuật khác để duy trì trạng thái của các phần trước đó khi các token mới được truyền đến mô hình
- Hỏi và trả lời
  - Trước đây, điều này chỉ có thể thực hiện được với RAG do lượng ngữ cảnh hạn chế và khả năng nhớ lại thông tin thực tế của mô hình thấp
- Quy trình công việc của trợ lý AI
  - Văn bản là nền tảng của cách các trợ lý AI duy trì trạng thái về những gì họ đã làm và những gì họ cần làm; việc không có đủ thông tin về thế giới và mục tiêu của trợ lý AI là một hạn chế đối với độ tin cậy của trợ lý AI

[Học tập trong ngữ cảnh nhiều ví dụ](https://ai.google.dev/gemini-api/docs/Học tập trong ngữ cảnh nhiều ví dụ) là một trong những
khả năng độc đáo nhất do các mô hình ngữ cảnh dài mở ra. Nghiên cứu đã chỉ ra rằng việc áp dụng mô hình ví dụ "một lần" hoặc "nhiều lần" phổ biến, trong đó mô hình được trình bày một hoặc một vài ví dụ về một tác vụ và mở rộng quy mô đó lên hàng trăm, hàng nghìn hoặc thậm chí hàng trăm nghìn ví dụ, có thể dẫn đến các khả năng mới của mô hình. Phương pháp nhiều ví dụ này cũng cho thấy hiệu quả tương tự như các mô hình được tinh chỉnh cho một tác vụ cụ thể. Đối với các trường hợp sử dụng mà hiệu suất của mô hình Gemini chưa đủ để phát hành công khai, bạn có thể thử phương pháp nhiều ví dụ. Như bạn có thể khám phá sau này trong phần tối ưu hoá ngữ cảnh dài, việc lưu vào bộ nhớ đệm ngữ cảnh giúp loại khối lượng công việc token đầu vào cao này trở nên khả thi hơn về mặt kinh tế và thậm chí giảm độ trễ trong một số trường hợp.

### Video dài

Tiện ích của nội dung video từ lâu đã bị hạn chế do thiếu khả năng tiếp cận của chính phương tiện này. Rất khó để đọc lướt nội dung, bản chép lời thường không nắm bắt được sắc thái của video và hầu hết các công cụ không xử lý hình ảnh, văn bản và âm thanh cùng nhau. Với Gemini, các khả năng văn bản trong ngữ cảnh dài chuyển thành khả năng suy luận và trả lời các câu hỏi về dữ liệu đầu vào đa phương thức với hiệu suất bền vững.

Sau đây là một số trường hợp sử dụng mới nổi và tiêu chuẩn cho ngữ cảnh dài của video:

- Hỏi và trả lời video
- Bộ nhớ video, như minh hoạ với [Project Astra của Google](https://ai.google.dev/gemini-api/docs/Project Astra của Google)
- Phụ đề video
- Hệ thống đề xuất video, bằng cách làm phong phú siêu dữ liệu hiện có bằng khả năng hiểu đa phương thức mới
- Tuỳ chỉnh video, bằng cách xem một tập hợp dữ liệu và siêu dữ liệu video liên quan, sau đó xoá các phần video không liên quan đến người xem
- Kiểm duyệt nội dung video
- Xử lý video theo thời gian thực

Khi làm việc với video, bạn cần cân nhắc cách [video được
xử lý thành token](https://ai.google.dev/gemini-api/docs/video đượcxử lý thành token), điều này ảnh hưởng đến
giới hạn thanh toán và mức sử dụng. [Bạn có thể tìm hiểu thêm về cách đưa ra câu lệnh bằng tệp video trong
hướng dẫn về cách đưa ra câu lệnh](https://ai.google.dev/gemini-api/docs/Bạn có thể tìm hiểu thêm về cách đưa ra câu lệnh bằng tệp video tronghướng dẫn về cách đưa ra câu lệnh).

### Âm thanh dài

Các mô hình Gemini là những mô hình ngôn ngữ lớn đa phương thức đầu tiên có thể hiểu được âm thanh. Trước đây, quy trình làm việc điển hình của nhà phát triển sẽ liên quan đến việc kết hợp nhiều mô hình cụ thể theo miền, chẳng hạn như mô hình chuyển lời nói thành văn bản và mô hình chuyển văn bản thành văn bản, để xử lý âm thanh. Điều này dẫn đến độ trễ bổ sung cần thiết do thực hiện nhiều yêu cầu khứ hồi và giảm hiệu suất thường là do kiến trúc không kết nối của thiết lập nhiều mô hình.

Sau đây là một số trường hợp sử dụng mới nổi và tiêu chuẩn cho ngữ cảnh âm thanh:

- Chép lời và dịch theo thời gian thực
- Hỏi và trả lời podcast / video
- Chép lời và tóm tắt cuộc họp
- Trợ lý giọng nói

Bạn có thể tìm hiểu thêm về cách đưa ra câu lệnh bằng tệp âm thanh trong hướng dẫn về cách đưa ra câu lệnh [Prompting](https://ai.google.dev/gemini-api/docs/Prompting).

## Tối ưu hoá ngữ cảnh dài

Phương pháp tối ưu hoá chính khi làm việc với ngữ cảnh dài và các mô hình Gemini
là sử dụng [tính năng lưu vào bộ nhớ đệm ngữ cảnh](https://ai.google.dev/gemini-api/docs/tính năng lưu vào bộ nhớ đệm ngữ cảnh). Ngoài việc không thể xử lý nhiều token trong một yêu cầu, hạn chế chính khác là chi phí. Nếu bạn có một ứng dụng "trò chuyện với dữ liệu của bạn" trong đó người dùng tải lên 10 tệp PDF, một video và một số tài liệu công việc, thì trước đây bạn sẽ phải làm việc với một công cụ/khung thế hệ tăng cường khả năng truy xuất (RAG) phức tạp hơn để xử lý các yêu cầu này và trả một khoản tiền đáng kể cho các token được chuyển vào cửa sổ ngữ cảnh. Giờ đây, bạn có thể lưu vào bộ nhớ đệm các tệp mà người dùng tải lên và trả tiền để lưu trữ các tệp đó theo giờ. Ví dụ: chi phí đầu vào / đầu ra cho mỗi yêu cầu với Gemini Flash thấp hơn khoảng 4 lần so với chi phí đầu vào / đầu ra tiêu chuẩn. Vì vậy, nếu người dùng trò chuyện đủ với dữ liệu của họ, thì bạn sẽ tiết kiệm được một khoản chi phí lớn với tư cách là nhà phát triển.

## Các hạn chế của ngữ cảnh dài

Trong nhiều phần của hướng dẫn này, chúng tôi đã nói về cách các mô hình Gemini đạt được hiệu suất cao trong nhiều bài kiểm tra đánh giá khả năng truy xuất kim trong đống cỏ khô. Các bài kiểm tra này xem xét thiết lập cơ bản nhất, trong đó bạn có một kim duy nhất mà bạn đang tìm kiếm. Trong trường hợp bạn có thể có nhiều "kim" hoặc thông tin cụ thể mà bạn đang tìm kiếm, mô hình sẽ không hoạt động với độ chính xác tương tự. Hiệu suất có thể thay đổi ở mức độ lớn tuỳ thuộc vào ngữ cảnh. Bạn cần cân nhắc điều này vì có sự đánh đổi vốn có giữa việc truy xuất thông tin chính xác và chi phí. Bạn có thể đạt được khoảng 99% cho một truy vấn duy nhất, nhưng bạn phải trả chi phí token đầu vào mỗi khi gửi truy vấn đó. Vì vậy, để truy xuất 100 thông tin, nếu bạn cần hiệu suất 99%, thì có thể bạn sẽ cần gửi 100 yêu cầu. Đây là một ví dụ điển hình về trường hợp lưu vào bộ nhớ đệm ngữ cảnh có thể giảm đáng kể chi phí liên quan đến việc sử dụng các mô hình Gemini trong khi vẫn duy trì hiệu suất cao.

## Câu hỏi thường gặp

### Đâu là nơi tốt nhất để đặt truy vấn của tôi trong cửa sổ ngữ cảnh?

Trong hầu hết các trường hợp, đặc biệt là nếu tổng ngữ cảnh dài, hiệu suất của mô hình sẽ tốt hơn nếu bạn đặt truy vấn / câu hỏi ở cuối câu lệnh (sau tất cả ngữ cảnh khác).

### Tôi có bị mất hiệu suất mô hình khi thêm nhiều token vào một truy vấn không?

Nói chung, nếu bạn không cần truyền token đến mô hình, thì tốt nhất là bạn nên tránh truyền token. Tuy nhiên, nếu bạn có một khối lượng lớn token chứa một số thông tin và muốn hỏi về thông tin đó, thì mô hình có khả năng cao trong việc trích xuất thông tin đó (độ chính xác lên đến 99% trong nhiều trường hợp).

### Làm cách nào để giảm chi phí cho các truy vấn ngữ cảnh dài?

Nếu bạn có một tập hợp token / ngữ cảnh tương tự mà bạn muốn sử dụng lại nhiều
lần, thì [tính năng lưu vào bộ nhớ đệm ngữ cảnh](https://ai.google.dev/gemini-api/docs/tính năng lưu vào bộ nhớ đệm ngữ cảnh) có thể giúp giảm chi phí
liên quan đến việc hỏi về thông tin đó.

### Độ dài ngữ cảnh có ảnh hưởng đến độ trễ của mô hình không?

Có một lượng độ trễ cố định trong mọi yêu cầu, bất kể kích thước, nhưng nói chung, các truy vấn dài hơn sẽ có độ trễ cao hơn (thời gian đến token đầu tiên).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://ai.google.dev/gemini-api/docs/Giấy phép ghi nhận tác giả 4.0 của Creative Commons) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://ai.google.dev/gemini-api/docs/Giấy phép Apache 2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://ai.google.dev/gemini-api/docs/Chính sách trang web của Google Developers). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?
