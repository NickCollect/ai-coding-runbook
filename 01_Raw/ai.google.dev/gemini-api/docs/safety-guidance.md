---
source_url: https://ai.google.dev/gemini-api/docs/safety-guidance?hl=vi
fetched_at: 2026-09-07T05:42:19.517390+00:00
title: "H\u01b0\u1edbng d\u1eabn v\u1ec1 \u0111\u1ed9 an to\u00e0n v\u00e0 t\u00ednh x\u00e1c th\u1ef1c \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Hướng dẫn về độ an toàn và tính xác thực

Các mô hình trí tuệ nhân tạo tạo sinh là những công cụ mạnh mẽ, nhưng vẫn tồn tại một số hạn chế. Tính linh hoạt và khả năng áp dụng của các mô hình này đôi khi có thể dẫn đến kết quả không mong muốn, chẳng hạn như kết quả không chính xác, thiên vị hoặc phản cảm. Việc xử lý hậu kỳ và đánh giá thủ công nghiêm ngặt là điều cần thiết để hạn chế nguy cơ gây hại từ những kết quả như vậy.

Bạn có thể sử dụng các mô hình do Gemini API cung cấp cho nhiều ứng dụng AI tạo sinh và xử lý ngôn ngữ tự nhiên (NLP). Bạn chỉ có thể sử dụng các
hàm này thông qua Gemini API hoặc ứng dụng web Google AI Studio. Việc bạn sử dụng Gemini API cũng phải tuân thủ [Chính sách về các hành vi bị cấm khi sử dụng AI tạo sinh
Policy](https://policies.google.com/terms/generative-ai/use-policy?hl=vi) và các
[điều khoản dịch vụ của Gemini API](https://ai.google.dev/terms?hl=vi).

Một trong những yếu tố khiến các mô hình ngôn ngữ lớn (LLM) trở nên hữu ích là vì đây là những công cụ sáng tạo có thể giải quyết nhiều tác vụ ngôn ngữ khác nhau. Rất tiếc, điều này cũng có nghĩa là các mô hình ngôn ngữ lớn có thể tạo ra kết quả mà bạn không mong muốn, bao gồm cả văn bản phản cảm, vô tâm hoặc không chính xác về mặt thực tế.
Hơn nữa, tính linh hoạt đáng kinh ngạc của các mô hình này cũng là yếu tố khiến bạn khó dự đoán chính xác loại kết quả không mong muốn mà các mô hình này có thể tạo ra. Mặc dù
Gemini API được thiết kế dựa trên [các nguyên tắc AI
của Google](https://ai.google/principles/?hl=vi), nhưng nhà phát triển phải có trách nhiệm
áp dụng các mô hình này. Để hỗ trợ nhà phát triển tạo các ứng dụng an toàn và có trách nhiệm, Gemini API có một số tính năng lọc nội dung tích hợp cũng như các chế độ cài đặt an toàn có thể điều chỉnh trên 4 phương diện gây hại. Hãy tham khảo hướng dẫn về
[chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi) để tìm hiểu thêm. API này cũng cung cấp tính năng Bám sát nguồn bằng Google Tìm kiếm để cải thiện tính chính xác về mặt thực tế, mặc dù tính năng này có thể bị tắt đối với những nhà phát triển có trường hợp sử dụng sáng tạo hơn và không tìm kiếm thông tin.

Tài liệu này nhằm giới thiệu cho bạn một số rủi ro về an toàn có thể phát sinh khi sử dụng LLM và đề xuất các phương pháp thiết kế và phát triển an toàn mới. (Xin lưu ý rằng luật và quy định cũng có thể áp đặt các hạn chế, nhưng những vấn đề này nằm ngoài phạm vi của hướng dẫn này.)

Bạn nên làm theo các bước sau khi xây dựng ứng dụng bằng LLM:

- Tìm hiểu các rủi ro về an toàn của ứng dụng
- Cân nhắc điều chỉnh để giảm thiểu rủi ro về an toàn
- Thực hiện kiểm thử an toàn phù hợp với trường hợp sử dụng của bạn
- Yêu cầu người dùng gửi ý kiến phản hồi và theo dõi mức sử dụng

Bạn nên lặp lại các giai đoạn điều chỉnh và kiểm thử cho đến khi đạt được hiệu suất phù hợp với ứng dụng của mình.

![Chu kỳ triển khai mô hình](https://ai.google.dev/static/gemini-api/docs/images/safety_diagram.png?hl=vi)

## Tìm hiểu các rủi ro về an toàn của ứng dụng

Trong bối cảnh này, an toàn được định nghĩa là khả năng của LLM trong việc tránh gây hại cho người dùng, chẳng hạn như bằng cách tạo ngôn ngữ độc hại hoặc nội dung thúc đẩy các khuôn mẫu. Các mô hình có sẵn thông qua Gemini API đã được thiết kế dựa trên [Nguyên tắc về trí tuệ nhân tạo của Google](https://ai.google/principles/?hl=vi) và việc bạn sử dụng các mô hình này phải tuân thủ [Chính sách về các hành vi bị cấm khi sử dụng AI tạo sinh](https://policies.google.com/terms/generative-ai/use-policy?hl=vi). API này cung cấp các bộ lọc an toàn tích hợp để giúp giải quyết một số vấn đề thường gặp về mô hình ngôn ngữ, chẳng hạn như ngôn ngữ độc hại và lời nói hận thù, đồng thời nỗ lực hướng đến sự đa dạng và tránh các khuôn mẫu. Tuy nhiên, mỗi ứng dụng có thể gây ra một tập hợp rủi ro khác nhau cho người dùng. Vì vậy, với tư cách là chủ sở hữu ứng dụng, bạn có trách nhiệm biết rõ người dùng và những tác hại tiềm ẩn mà ứng dụng của bạn có thể gây ra, đồng thời đảm bảo rằng ứng dụng của bạn sử dụng LLM một cách an toàn và có trách nhiệm.

Trong quá trình đánh giá này, bạn nên cân nhắc khả năng gây hại và xác định mức độ nghiêm trọng cũng như các bước giảm thiểu. Ví dụ: một ứng dụng tạo bài luận dựa trên các sự kiện thực tế sẽ cần phải cẩn thận hơn trong việc tránh thông tin sai lệch so với một ứng dụng tạo câu chuyện hư cấu để giải trí. Một cách hay để bắt đầu khám phá các rủi ro tiềm ẩn về an toàn là nghiên cứu người dùng cuối và những người khác có thể bị ảnh hưởng bởi kết quả của ứng dụng. Bạn có thể thực hiện việc này theo nhiều cách, bao gồm nghiên cứu các nghiên cứu hiện đại trong miền ứng dụng của bạn, quan sát cách mọi người sử dụng các ứng dụng tương tự hoặc chạy một nghiên cứu về người dùng, khảo sát hoặc tiến hành phỏng vấn không chính thức với người dùng tiềm năng.

### Mẹo nâng cao

- Trao đổi với nhiều người dùng tiềm năng trong nhóm đối tượng mục tiêu về ứng dụng và mục đích dự kiến của ứng dụng để có cái nhìn rộng hơn về các rủi ro tiềm ẩn và điều chỉnh tiêu chí đa dạng khi cần.
- Khung quản lý rủi ro về [AI](https://www.nist.gov/itl/ai-risk-management-framework)
  do Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST) của chính phủ Hoa Kỳ phát hành cung cấp hướng dẫn chi tiết hơn và các tài nguyên học tập bổ sung về quản lý rủi ro về AI.
- Ấn phẩm của DeepMind về các
  [rủi ro đạo đức và xã hội về tác hại từ các mô hình ngôn ngữ](https://arxiv.org/abs/2112.04359)
  mô tả chi tiết những cách mà các ứng dụng mô hình ngôn ngữ
  có thể gây hại.

## Cân nhắc điều chỉnh để giảm thiểu rủi ro về an toàn và tính chính xác về mặt thực tế

Giờ đây, khi đã hiểu rõ các rủi ro, bạn có thể quyết định cách giảm thiểu các rủi ro đó. Việc xác định những rủi ro cần ưu tiên và mức độ cần thiết để cố gắng ngăn chặn các rủi ro đó là một quyết định quan trọng, tương tự như việc phân loại lỗi trong một dự án phần mềm. Sau khi xác định các ưu tiên, bạn có thể bắt đầu suy nghĩ về các loại biện pháp giảm thiểu phù hợp nhất. Thông thường, những thay đổi đơn giản có thể tạo ra sự khác biệt và giảm thiểu rủi ro.

Ví dụ: khi thiết kế một ứng dụng, hãy cân nhắc:

- **Tinh chỉnh đầu ra của mô hình** để phản ánh rõ hơn những gì có thể chấp nhận được trong bối cảnh ứng dụng của bạn. Việc tinh chỉnh có thể giúp kết quả của mô hình trở nên dễ dự đoán và nhất quán hơn, từ đó có thể giúp giảm thiểu một số rủi ro.
- **Cung cấp phương thức nhập giúp tạo ra kết quả an toàn hơn.** Chính xác nội dung bạn nhập vào LLM có thể tạo ra sự khác biệt về chất lượng của kết quả.
  Việc thử nghiệm các câu lệnh nhập để tìm ra câu lệnh hoạt động an toàn nhất trong trường hợp sử dụng của bạn là điều đáng làm, vì sau đó bạn có thể cung cấp trải nghiệm người dùng giúp tạo điều kiện cho việc này. Ví dụ: bạn có thể hạn chế người dùng chỉ chọn từ danh sách thả xuống các câu lệnh nhập hoặc đưa ra các đề xuất bật lên bằng các cụm từ mô tả mà bạn nhận thấy hoạt động an toàn trong bối cảnh ứng dụng của bạn.
- **Chặn các nội dung nhập không an toàn và lọc kết quả trước khi hiển thị cho người dùng.** Trong các tình huống đơn giản, bạn có thể sử dụng danh sách chặn để xác định và chặn các từ hoặc cụm từ không an toàn trong câu lệnh hoặc câu trả lời, hoặc yêu cầu nhân viên đánh giá thủ công sửa đổi hoặc chặn nội dung đó.
- **Sử dụng các bộ phân loại đã được huấn luyện để gắn nhãn cho từng câu lệnh bằng các tác hại tiềm ẩn hoặc tín hiệu đối nghịch.** Sau đó, bạn có thể áp dụng các chiến lược khác nhau về cách xử lý yêu cầu dựa trên loại tác hại được phát hiện. Ví dụ: Nếu nội dung nhập có bản chất đối nghịch hoặc lạm dụng một cách rõ ràng, thì nội dung đó có thể bị chặn và thay vào đó là đưa ra câu trả lời được viết sẵn.
  **Mẹo nâng cao:** Nếu tín hiệu xác định kết quả là gây hại, thì ứng dụng có thể sử dụng các lựa chọn sau:

  - Đưa ra thông báo lỗi hoặc kết quả được viết sẵn.
  - Thử lại câu lệnh, trong trường hợp kết quả an toàn thay thế được tạo, vì đôi khi cùng một câu lệnh sẽ tạo ra các kết quả khác nhau.
- **Áp dụng các biện pháp bảo vệ chống lại hành vi cố ý sử dụng sai** chẳng hạn như chỉ định cho mỗi người dùng một mã nhận dạng duy nhất và áp đặt giới hạn về số lượng truy vấn của người dùng có thể gửi trong một khoảng thời gian nhất định. Một biện pháp bảo vệ khác là cố gắng bảo vệ chống lại việc tiêm câu lệnh (prompt injection) có thể xảy ra. Việc tiêm câu lệnh (prompt injection), giống như việc chèn SQL, là cách để người dùng độc hại thiết kế một câu lệnh nhập giúp thao túng kết quả của mô hình, chẳng hạn như bằng cách gửi một câu lệnh nhập hướng dẫn mô hình bỏ qua mọi ví dụ trước đó. Hãy xem
  [Chính sách về các hành vi bị cấm khi sử dụng AI tạo sinh](https://policies.google.com/terms/generative-ai/use-policy?hl=vi)
  để biết thông tin chi tiết về hành vi cố ý sử dụng sai.
- **Điều chỉnh chức năng thành chức năng vốn có rủi ro thấp hơn.**
  Các tác vụ có phạm vi hẹp hơn (ví dụ: trích xuất từ khoá từ các đoạn văn bản) hoặc có sự giám sát chặt chẽ hơn của con người (ví dụ: tạo nội dung dạng ngắn sẽ được con người xem xét) thường có rủi ro thấp hơn. Vì vậy, chẳng hạn, thay vì tạo một ứng dụng để viết câu trả lời email từ đầu, bạn có thể giới hạn ứng dụng này chỉ mở rộng trên một dàn ý hoặc đề xuất các cách diễn đạt thay thế.
- **Điều chỉnh chế độ cài đặt an toàn cho nội dung gây hại để giảm khả năng bạn thấy các câu trả lời có thể gây hại.** Gemini API cung cấp các chế độ cài đặt an toàn mà bạn có thể điều chỉnh trong giai đoạn tạo mẫu để xác định xem ứng dụng của bạn có yêu cầu cấu hình an toàn hạn chế hơn hay ít hạn chế hơn. Bạn có thể điều chỉnh các chế độ cài đặt này trên 5 danh mục bộ lọc để hạn chế hoặc cho phép một số loại nội dung. Hãy tham khảo [hướng dẫn về chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi) để tìm hiểu về
  các chế độ cài đặt an toàn có thể điều chỉnh thông qua Gemini API.
- **Giảm các điểm không chính xác về mặt thực tế hoặc ảo giác tiềm ẩn bằng cách bật tính năng Bám sát nguồn bằng Google Tìm kiếm**. Hãy nhớ rằng nhiều mô hình AI đang ở giai đoạn thử nghiệm và có thể đưa ra thông tin không chính xác về mặt thực tế, ảo giác hoặc tạo ra các kết quả có vấn đề khác. Tính năng Bám sát nguồn bằng Google Tìm kiếm kết nối mô hình Gemini với nội dung trên web theo thời gian thực và hỗ trợ tất cả các ngôn ngữ hiện có. Nhờ đó, Gemini có thể đưa ra câu trả lời chính xác hơn và trích dẫn các nguồn có thể xác minh ngoài điểm cắt kiến thức của mô hình.

## Thực hiện kiểm thử an toàn phù hợp với trường hợp sử dụng của bạn

Kiểm thử là một phần quan trọng trong việc xây dựng các ứng dụng mạnh mẽ và an toàn, nhưng mức độ, phạm vi và chiến lược kiểm thử sẽ khác nhau. Ví dụ: một trình tạo thơ haiku chỉ để giải trí có khả năng gây ra rủi ro ít nghiêm trọng hơn so với, chẳng hạn như một ứng dụng được thiết kế để các công ty luật sử dụng nhằm tóm tắt các tài liệu pháp lý và giúp soạn thảo hợp đồng. Tuy nhiên, trình tạo thơ haiku có thể được nhiều người dùng sử dụng hơn, điều này có nghĩa là khả năng xảy ra các nỗ lực đối nghịch hoặc thậm chí các nội dung nhập gây hại không chủ ý có thể cao hơn. Bối cảnh triển khai cũng quan trọng. Ví dụ: một ứng dụng có kết quả được các chuyên gia xem xét trước khi thực hiện bất kỳ hành động nào có thể được coi là ít có khả năng tạo ra kết quả gây hại hơn so với ứng dụng giống hệt nhưng không có sự giám sát như vậy.

Bạn thường phải trải qua nhiều lần thay đổi và kiểm thử trước khi cảm thấy tự tin rằng mình đã sẵn sàng ra mắt, ngay cả đối với những ứng dụng có rủi ro tương đối thấp. Hai loại kiểm thử đặc biệt hữu ích cho các ứng dụng AI:

- **Điểm chuẩn an toàn** bao gồm việc thiết kế các chỉ số an toàn phản ánh những cách mà ứng dụng của bạn có thể không an toàn trong bối cảnh có khả năng được sử dụng, sau đó kiểm thử hiệu suất của ứng dụng dựa trên các chỉ số bằng cách sử dụng tập dữ liệu đánh giá. Bạn nên cân nhắc các mức tối thiểu có thể chấp nhận được của các chỉ số an toàn trước khi kiểm thử để 1) bạn có thể đánh giá kết quả kiểm thử dựa trên những kỳ vọng đó và 2) bạn có thể thu thập tập dữ liệu đánh giá dựa trên các kiểm thử đánh giá các chỉ số mà bạn quan tâm nhất.

  **Mẹo nâng cao:**

  - Hãy cẩn thận khi quá dựa vào các phương pháp "có sẵn" vì có khả năng bạn sẽ cần xây dựng tập dữ liệu kiểm thử của riêng mình bằng cách sử dụng người đánh giá để phù hợp hoàn toàn với bối cảnh của ứng dụng.
  - Nếu có nhiều hơn một chỉ số, bạn sẽ cần quyết định cách đánh đổi nếu một thay đổi dẫn đến việc cải thiện một chỉ số nhưng lại gây hại cho chỉ số khác. Giống như các kỹ thuật hiệu suất khác, bạn có thể muốn tập trung vào hiệu suất trong trường hợp xấu nhất trên tập dữ liệu đánh giá thay vì hiệu suất trung bình.
- **Kiểm thử đối nghịch** bao gồm việc chủ động cố gắng phá vỡ ứng dụng của bạn. Mục tiêu là xác định các điểm yếu để bạn có thể thực hiện các bước khắc phục phù hợp. Việc kiểm thử đối nghịch có thể tốn nhiều thời gian/công sức của người đánh giá có chuyên môn về ứng dụng của bạn – nhưng bạn càng làm nhiều thì càng có nhiều cơ hội phát hiện vấn đề, đặc biệt là những vấn đề hiếm khi xảy ra hoặc chỉ xảy ra sau khi chạy ứng dụng nhiều lần.

  - Kiểm thử đối nghịch là một phương pháp để đánh giá một cách có hệ thống mô hình học máy với mục đích tìm hiểu cách mô hình này hoạt động khi được cung cấp nội dung nhập độc hại hoặc vô tình gây hại:
    - Nội dung nhập có thể độc hại khi nội dung nhập được thiết kế rõ ràng để tạo ra kết quả không an toàn hoặc gây hại – ví dụ: yêu cầu mô hình tạo văn bản tạo ra một bài phát biểu hận thù về một tôn giáo cụ thể.
    - Nội dung nhập vô tình gây hại khi bản thân nội dung nhập có thể vô hại, nhưng lại tạo ra kết quả gây hại – ví dụ: yêu cầu mô hình tạo văn bản mô tả một người thuộc một dân tộc cụ thể và nhận được kết quả phân biệt chủng tộc.
  - Điểm khác biệt giữa kiểm thử đối nghịch và đánh giá tiêu chuẩn là thành phần của dữ liệu được sử dụng để kiểm thử. Đối với các kiểm thử đối nghịch, hãy chọn
    dữ liệu kiểm thử có nhiều khả năng tạo ra kết quả có vấn đề từ
    mô hình nhất. Điều này có nghĩa là thăm dò hành vi của mô hình đối với tất cả các loại tác hại có thể xảy ra, bao gồm cả các ví dụ hiếm gặp hoặc bất thường và các trường hợp đặc biệt có liên quan đến chính sách an toàn. Nội dung này cũng phải bao gồm sự đa dạng trong các phương diện khác nhau của một câu, chẳng hạn như cấu trúc, ý nghĩa và độ dài. Bạn có thể tham khảo các phương pháp AI có trách nhiệm của [Google
    về tính
    công bằng](https://ai.google/responsibilities/responsible-ai-practices/?category=fairness&hl=vi)
    để biết thêm thông tin chi tiết về những điều cần cân nhắc khi xây dựng tập dữ liệu kiểm thử.
    **Mẹo nâng cao:**
  - Sử dụng [kiểm thử tự động](https://www.deepmind.com/blog/red-teaming-language-models-with-language-models?hl=vi)
    thay vì phương pháp truyền thống là tuyển dụng người vào 'nhóm
    đỏ' để cố gắng phá vỡ ứng dụng của bạn. Trong kiểm thử tự động, 'đội đỏ' là một mô hình ngôn ngữ khác tìm thấy văn bản nhập tạo ra kết quả gây hại từ mô hình đang được kiểm thử.

## Theo dõi các vấn đề

Dù bạn kiểm thử và giảm thiểu bao nhiêu, bạn cũng không bao giờ có thể đảm bảo sự hoàn hảo. Vì vậy, hãy lên kế hoạch trước về cách phát hiện và xử lý các vấn đề phát sinh. Các phương pháp phổ biến bao gồm thiết lập một kênh được giám sát để người dùng chia sẻ ý kiến phản hồi (ví dụ: xếp hạng thích/không thích) và chạy một nghiên cứu về người dùng để chủ động yêu cầu ý kiến phản hồi từ nhiều người dùng – đặc biệt có giá trị nếu các mẫu sử dụng khác với kỳ vọng.

### Mẹo nâng cao

- Khi người dùng đưa ra ý kiến phản hồi cho các sản phẩm AI, ý kiến phản hồi đó có thể cải thiện đáng kể hiệu suất của AI và trải nghiệm người dùng theo thời gian, chẳng hạn như giúp bạn chọn các ví dụ hay hơn để tinh chỉnh câu lệnh. Chương
  [Phản hồi và Kiểm soát](https://pair.withgoogle.com/chapter/feedback-controls/)
  trong [Sổ tay về con người và AI của Google](https://pair.withgoogle.com/guidebook/chapters)
  nêu bật những điểm cần cân nhắc khi thiết kế
  cơ chế phản hồi.

## Các bước tiếp theo

- Hãy tham khảo hướng dẫn về
  [chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi) để tìm hiểu về các chế độ cài đặt an toàn có thể điều chỉnh thông qua Gemini API.
- Hãy xem phần [giới thiệu về câu lệnh](https://ai.google.dev/gemini-api/docs/prompting-intro?hl=vi) để bắt đầu
  viết câu lệnh đầu tiên.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-05 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-05 UTC."],[],[]]
