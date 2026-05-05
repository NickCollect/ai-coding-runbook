---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=vi
fetched_at: 2026-05-05T19:52:22.312413+00:00
title: "Ghi ch\u00fa ph\u00e1t h\u00e0nh \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Ghi chú phát hành

Trang này ghi lại nội dung cập nhật của Gemini API.

## Ngày 5 tháng 5 năm 2026

- Cập nhật tính năng **Tìm kiếm tệp** để hỗ trợ tìm kiếm đa phương thức. Giờ đây, bạn có thể nhúng và tìm kiếm hình ảnh một cách tự nhiên bằng mô hình `gemini-embedding-2`.
  Siêu dữ liệu liên kết thực tế hiện bao gồm `media_id` cho trích dẫn trực quan và `page_numbers` cho biết nơi tìm thấy thông tin. Để tìm hiểu thêm, hãy xem hướng dẫn về [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi).

## Ngày 4 tháng 5 năm 2026

- Ra mắt tính năng hỗ trợ [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=vi) dựa trên sự kiện trong Gemini API để thay thế quy trình thăm dò ý kiến cho Batch API và các thao tác kéo dài.

## Ngày 30 tháng 4 năm 2026

- Mô hình `gemini-robotics-er-1.5-preview` đã [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi). Thay vào đó, hãy sử dụng [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=vi).

## Ngày 22 tháng 4 năm 2026

- Phát hành `gemini-embedding-2` dưới dạng bản phát hành công khai (GA). Để tìm hiểu thêm, hãy xem trang [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi) (Nhúng).

## Ngày 21 tháng 4 năm 2026

- Phát hành các phiên bản mới của tác nhân [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) (Nghiên cứu chuyên sâu) với tính năng lập kế hoạch cộng tác, hỗ trợ trực quan hoá, tích hợp máy chủ MCP và tính năng Tìm kiếm tệp:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=vi): Được thiết kế để đạt tốc độ và hiệu quả cao, lý tưởng để truyền trực tuyến trở lại giao diện người dùng của ứng dụng.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=vi): Mức độ toàn diện tối đa để tự động thu thập và tổng hợp bối cảnh.

## Ngày 15 tháng 4 năm 2026

- Ra mắt [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=vi), mô hình chuyển văn bản sang lời nói tiết kiệm chi phí, giàu biểu cảm và có thể điều hướng. Hãy đọc tài liệu về [Chuyển văn bản sang lời nói](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi) để tìm hiểu thêm.

## Ngày 14 tháng 4 năm 2026

- Phát hành `gemini-robotics-er-1.6-preview`, mô hình robot mới của chúng tôi.
  Giờ đây, mô hình này có các chức năng mới như đọc nhạc cụ, cải thiện khả năng suy luận không gian và vật lý. Để tìm hiểu thêm, hãy xem trang [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi) và [blog](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=vi).
- Thông báo ngừng cung cấp: Mô hình `gemini-robotics-er-1.5-preview` sẽ [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) vào lúc 9 giờ sáng ngày 30 tháng 4 năm 2026 (giờ Thái Bình Dương).

## Ngày 2 tháng 4 năm 2026

- Phát hành `gemma-4-26b-a4b-it` và `gemma-4-31b-it`, có trên [AI Studio](https://aistudio.google.com?hl=vi) và thông qua Gemini API, trong đợt ra mắt [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=vi).

## Ngày 1 tháng 4 năm 2026

- Giới thiệu các cấp suy luận [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi) và [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi) mới, cung cấp nhiều lựa chọn hơn để tối ưu hoá chi phí hoặc độ trễ.

## Ngày 31 tháng 3 năm 2026

- Ra mắt bản xem trước Veo 3.1 Lite, [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=vi), mô hình [tạo video](https://ai.google.dev/gemini-api/docs/video?hl=vi) tiết kiệm chi phí nhất của chúng tôi, được thiết kế để lặp lại nhanh chóng và xây dựng các ứng dụng có khối lượng lớn.
- Mô hình `gemini-2.5-flash-lite-preview-09-2025` đã ngừng hoạt động. Thay vào đó, hãy sử dụng [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=vi).

## Ngày 26 tháng 3 năm 2026

- Được phát hành vào ngày [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=vi), mô hình âm thanh sang âm thanh (A2A) mới nhất được thiết kế cho các ứng dụng AI ưu tiên giọng nói và lời thoại theo thời gian thực. Hãy đọc tài liệu về [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=vi) để bắt đầu.

## Ngày 25 tháng 3 năm 2026

- Ra mắt các mô hình tạo nhạc [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi): [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=vi) (đoạn nhạc dài 30 giây) và [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=vi) (bài hát trọn vẹn). Cả hai mô hình này đều chấp nhận văn bản và hình ảnh đầu vào, đồng thời tạo ra âm thanh nổi 48 kHz chất lượng cao. Hãy xem hướng dẫn về [Tạo nhạc](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi) để biết thông tin chi tiết và các mẫu mã.

## Ngày 23 tháng 3 năm 2026

- Ra mắt [Gói thanh toán trả trước và trả sau](https://ai.google.dev/gemini-api/docs/billing?hl=vi) trong AI Studio. Các tài khoản hiện có có thể bị ảnh hưởng; hãy đọc tài liệu về [Thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi) để biết thêm thông tin.

## Ngày 18 tháng 3 năm 2026

- Phát hành tính năng mới [Kết hợp công cụ tích hợp và tính năng Gọi hàm](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi), cho phép sử dụng các công cụ tích hợp của Gemini cùng với các công cụ gọi hàm tuỳ chỉnh trong một lệnh gọi API duy nhất.
- [Tính năng căn cứ vào Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi#supported_models) hiện được hỗ trợ cho các mô hình Gemini 3 trong tương lai.

## Ngày 16 tháng 3 năm 2026

- Ra mắt [Bậc sử dụng](https://ai.google.dev/gemini-api/docs/billing?hl=vi#about-billing) được cải tiến và [hạn mức chi tiêu của Tài khoản thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi#tier-spend-caps) để cải thiện trải nghiệm thanh toán của người dùng.

## Ngày 12 tháng 3 năm 2026

- Giới thiệu [hạn mức chi tiêu ở cấp dự án](https://ai.google.dev/gemini-api/docs/billing?hl=vi#project-spend-caps) cho việc thanh toán trong AI Studio.

## Ngày 10 tháng 3 năm 2026

- Phát hành `gemini-embedding-2-preview`, mô hình nhúng đa phương thức đầu tiên của chúng tôi.
  Mô hình này hỗ trợ văn bản, hình ảnh, video, âm thanh và tệp PDF đầu vào, ánh xạ tất cả các phương thức vào một không gian nhúng hợp nhất. Để tìm hiểu thêm, hãy xem phần [Nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi).
- Thông báo ngừng hoạt động: Mô hình `gemini-2.5-flash-lite-preview-09-2025` sẽ [ngừng hoạt động](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) vào ngày 31 tháng 3 năm 2026.

## Ngày 9 tháng 3 năm 2026

- Mô hình Gemini 3 Pro Preview đã [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi). `gemini-3-pro-preview` hiện trỏ đến [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi).

## Ngày 3 tháng 3 năm 2026

- Ra mắt Gemini 3.1 Flash-Lite Preview, mô hình Flash-Lite đầu tiên trong dòng Gemini 3. Đọc [trang mô hình](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=vi) để biết thông số kỹ thuật, các bản cập nhật cụ thể và hướng dẫn dành cho nhà phát triển.

## Ngày 26 tháng 2 năm 2026

- Ra mắt Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=vi), một mô hình có hiệu suất cao được tối ưu hoá cho tốc độ và các trường hợp sử dụng với khối lượng lớn.
- Thông báo ngừng cung cấp: Gemini 3 Pro Preview (`gemini-3-pro-preview`) sẽ [ngừng hoạt động](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) từ ngày 9 tháng 3 năm 2026.

## Ngày 19 tháng 2 năm 2026

- Phát hành [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi), phiên bản mới nhất trong dòng Gemini 3 mới.
- Ra mắt một điểm cuối riêng biệt `gemini-3.1-pro-preview-customtools`, có khả năng ưu tiên các công cụ tuỳ chỉnh tốt hơn cho những người dùng tạo bằng cách kết hợp bash và các công cụ.

## Ngày 18 tháng 2 năm 2026

- Thông báo về việc ngừng cung cấp: Các mẫu sau đây sẽ [ngừng hoạt động](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) từ ngày 1 tháng 6 năm 2026:

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## Ngày 17 tháng 2 năm 2026

- Các mô hình sau đây sẽ [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## Ngày 29 tháng 1 năm 2026

- Ra mắt dịch vụ hỗ trợ cho công cụ Sử dụng máy tính ở `gemini-3-pro-preview` và `gemini-3-flash-preview`.

## Ngày 21 tháng 1 năm 2026

- Đã thay đổi các bí danh `latest`:

  - `gemini-pro-latest` chuyển sang `gemini-3-pro-preview`
  - `gemini-flash-latest` chuyển sang `gemini-3-flash-preview`

## Ngày 15 tháng 1 năm 2026

- Thông báo về việc ngừng hoạt động: Các mô hình sau đây sẽ [ngừng hoạt động](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) từ ngày 17 tháng 2 năm 2026:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- Mô hình `gemini-2.5-flash-image-preview` đã ngừng hoạt động.

## Ngày 14 tháng 1 năm 2026

- Mô hình `text-embedding-004` đã [tắt](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi).

## Ngày 13 tháng 1 năm 2026

- Thêm độ phân giải đầu ra 4K cho [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi) và hỗ trợ thêm cho video dọc ở mọi độ phân giải.

## Ngày 12 tháng 1 năm 2026

- Ra mắt tính năng vòng đời của mô hình. Giờ đây, một số mô hình sẽ chỉ định giai đoạn vòng đời và tiến trình ngừng sử dụng. Hãy xem tài liệu sau để biết thêm thông tin:

  - [Các giai đoạn của mô hình](https://ai.google.dev/api/generate-content?hl=vi#ModelStatus)

## Ngày 8 tháng 1 năm 2026

- Ra mắt tính năng hỗ trợ các bộ chứa Cloud Storage và mọi URL công khai và riêng tư đã ký trước DB làm nguồn dữ liệu đầu vào cho Gemini API. Giới hạn kích thước tệp cũng tăng từ 20 MB lên 100 MB. Để biết thông tin chi tiết, hãy xem [Hướng dẫn về phương thức nhập tệp](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=vi).

## Ngày 19 tháng 12 năm 2025

- Giới thiệu một thay đổi có thể gây lỗi cho bản dùng thử công khai Interactions API trong phiên bản v1beta. Trường `total_reasoning_tokens` đã được đổi tên thành `total_thought_tokens` để phù hợp hơn với khái niệm "suy nghĩ" trong các mô hình tư duy.

## Ngày 17 tháng 12 năm 2025

- Ra mắt bản dùng thử Gemini 3 Flash, `gemini-3-flash-preview`, mang đến hiệu suất nhanh chóng ở đẳng cấp tiên tiến, ngang bằng với các mô hình lớn hơn nhưng chỉ với một phần nhỏ chi phí. Với khả năng lập trình dựa trên tác nhân, cũng như khả năng suy luận về không gian và hình ảnh được nâng cấp. Đọc tài liệu về một số tính năng mới, bao gồm:

  - [Phản hồi đa phương thức của hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#multimodal)
  - [Thực thi mã bằng hình ảnh](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi#images)

## Ngày 12 tháng 12 năm 2025

- Phát hành `gemini-2.5-flash-native-audio-preview-12-2025`, một mô hình âm thanh gốc mới cho Live API. Bản cập nhật này cải thiện khả năng xử lý các quy trình làm việc phức tạp của mô hình. Để tìm hiểu thêm, hãy xem [hướng dẫn về Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi) và [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=vi).

## Ngày 11 tháng 12 năm 2025

- Phát hành Interactions API ở giai đoạn thử nghiệm. API này cung cấp một giao diện hợp nhất để tương tác với các mô hình và tác nhân Gemini. Để tìm hiểu thêm, hãy xem hướng dẫn về [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=vi).
- Ra mắt Tác nhân Deep Research của Gemini ở chế độ xem trước. Tính năng này có thể tự động lên kế hoạch, thực thi và tổng hợp kết quả cho các tác vụ nghiên cứu nhiều bước. Xem hướng dẫn về tính năng [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) để biết thông tin chi tiết.

## Ngày 10 tháng 12 năm 2025

- Ra mắt các điểm cải tiến cho [mô hình chuyển văn bản sang lời nói](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi), bản dùng thử Gemini 2.5 Flash TTS (được tối ưu hoá để có độ trễ thấp) và bản dùng thử Gemini 2.5 Pro TTS (được tối ưu hoá về chất lượng), bao gồm khả năng diễn đạt nâng cao, tốc độ chính xác và đối thoại liền mạch.

## Ngày 9 tháng 12 năm 2025

- Các mô hình Gemini Live API sau đây hiện đã ngừng hoạt động:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## Ngày 5 tháng 12 năm 2025

- Gemini 3 sẽ bắt đầu tính phí cho tính năng [Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) từ ngày 5 tháng 1 năm 2026.

## Ngày 4 tháng 12 năm 2025

- Thông báo ngừng sử dụng: Mô hình `gemini-2.5-flash-image-preview` sẽ ngừng hoạt động từ ngày 15 tháng 1 năm 2026.

## Ngày 3 tháng 12 năm 2025

- Thông báo ngừng cung cấp: Mô hình `text-embedding-004` sẽ ngừng hoạt động vào ngày 14 tháng 1 năm 2026.

## Ngày 20 tháng 11 năm 2025

- Phát hành bản xem trước hình ảnh của Gemini 3 Pro, `gemini-3-pro-image-preview`, phiên bản tiếp theo của mô hình Nano Banana. Hãy đọc trang [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) để biết thêm thông tin chi tiết.

## Ngày 18 tháng 11 năm 2025

- Ra mắt mô hình đầu tiên thuộc dòng Gemini 3, `gemini-3-pro-preview`, mô hình suy luận và hiểu biết đa phương thức tiên tiến của chúng tôi với khả năng lập trình và tác nhân mạnh mẽ.

  Ngoài những điểm cải tiến về trí thông minh và hiệu suất, Gemini 3 Pro Preview còn có hành vi mới liên quan đến:

  - [Độ phân giải của nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/media-resolution?hl=vi)
  - [Chữ ký tư duy](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=vi)
  - [Cấp độ tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi#thinking-levels)

  Đọc [Hướng dẫn dành cho nhà phát triển Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=vi) để biết thông tin về việc di chuyển, các tính năng mới và thông số kỹ thuật.

## Ngày 11 tháng 11 năm 2025

- Thông báo ngừng sử dụng: Các mô hình sau đây sẽ ngừng hoạt động:

  - Ngày 12 tháng 11:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - Ngày 14 tháng 11:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## Ngày 10 tháng 11 năm 2025

- Mô hình sau đây sẽ ngừng hoạt động:

  - `imagen-3.0-generate-002`

  Thay vào đó, hãy sử dụng [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=vi#imagen-4). Hãy tham khảo [bảng Ngừng cung cấp Gemini](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi) để biết thêm thông tin chi tiết.

## Ngày 6 tháng 11 năm 2025

- Ra mắt API Tìm kiếm tệp ở bản dùng thử công khai, cho phép nhà phát triển đưa ra các câu trả lời dựa trên dữ liệu của riêng họ. Hãy đọc trang [Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi) mới để biết thêm thông tin.

## Ngày 4 tháng 11 năm 2025

- Đối với [Hình ảnh Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi), số lượng mã thông báo đầu vào cho hình ảnh đã giảm từ 1290 xuống 258, giúp giảm chi phí chỉnh sửa hình ảnh.
- Thông báo ngừng sử dụng: Các mô hình sau đây sẽ ngừng hoạt động:

  - Ngày 18 tháng 11:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - Ngày 2 tháng 12:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - Ngày 9 tháng 12:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## Ngày 29 tháng 10 năm 2025

- Ra mắt công cụ [ghi nhật ký và tập dữ liệu](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=vi) mới cho Gemini API.

## Ngày 20 tháng 10 năm 2025

- Các mô hình Gemini Live API sau đây hiện đã ngừng hoạt động:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Bạn có thể sử dụng `gemini-2.5-flash-native-audio-preview-09-2025` thay thế.
- Thông báo ngừng hoạt động: `gemini-2.0-flash-live-001` và `gemini-live-2.5-flash-preview` sẽ ngừng hoạt động từ ngày 9 tháng 12 năm 2025.

## Ngày 17 tháng 10 năm 2025

- Tính năng **Kết nối với Google Maps** hiện đã được cung cấp rộng rãi. Để biết thêm thông tin, hãy xem tài liệu [Kết nối với Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi).

## Ngày 15 tháng 10 năm 2025

- Phát hành các mô hình [Veo 3.1 và 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=vi#veo-3.1) trong bản dùng thử công khai, với các tính năng mới như:

  - Kéo dài thời lượng video do Veo tạo.
  - Tham khảo tối đa 3 hình ảnh để tạo video.
  - Cung cấp hình ảnh khung hình đầu tiên và cuối cùng để tạo video.

  Trong lần ra mắt này, chúng tôi cũng bổ sung thêm các lựa chọn về thời lượng video đầu ra của Veo 3: 4, 6 và 8 giây.
- Thông báo ngừng hoạt động: `veo-3.0-generate-preview` và `veo-3.0-fast-generate-preview` sẽ ngừng hoạt động từ ngày 12 tháng 11 năm 2025.

## Ngày 7 tháng 10 năm 2025

- Ra mắt [Gemini 2.5 Computer Use Preview](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)

## Ngày 2 tháng 10 năm 2025

- Ra mắt phiên bản GA của Gemini 2.5 Flash Image: [Tạo hình ảnh bằng Gemini](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)

## Ngày 29 tháng 9 năm 2025

- Các mô hình Gemini 1.5 sau đây hiện đã ngừng hoạt động:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## Ngày 25 tháng 9 năm 2025

- Phát hành mô hình Gemini Robotics-ER 1.5 ở chế độ xem trước. Hãy xem [Tổng quan về robot](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi) để tìm hiểu cách sử dụng mô hình này cho ứng dụng robot của bạn.
- Ra mắt các mô hình xem trước sau đây:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Hãy xem trang [Mô hình](https://ai.google.dev/gemini-api/docs/models?hl=vi) để biết thông tin chi tiết.

## Ngày 23 tháng 9 năm 2025

- Phát hành `gemini-2.5-flash-native-audio-preview-09-2025`, một mô hình âm thanh gốc mới cho Live API với chức năng gọi được cải thiện và khả năng xử lý việc cắt lời. Để tìm hiểu thêm, hãy xem [hướng dẫn về Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi) và [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-native-audio).

## Ngày 16 tháng 9 năm 2025

- Thông báo ngừng sử dụng: Các mô hình sau đây sẽ ngừng hoạt động từ tháng 10 năm 2025:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  Hãy xem trang [Nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi) để biết thông tin chi tiết về mô hình nhúng mới nhất.

## Ngày 10 tháng 9 năm 2025

- Phát hành tính năng hỗ trợ cho [mô hình Nhúng trong Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi#batch-embedding) và thêm Batch API vào [thư viện tương thích với OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi#batch) để dễ dàng bắt đầu với các truy vấn theo lô.

## Ngày 9 tháng 9 năm 2025

- Ra mắt phiên bản GA của Veo 3 và Veo 3 Fast, với mức giá thấp hơn và các lựa chọn mới về tỷ lệ khung hình, độ phân giải và tính năng gieo mầm. Hãy đọc [tài liệu về Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi#model-features) để biết thêm thông tin.

## Ngày 26 tháng 8 năm 2025

- Ra mắt [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-image-preview) (Xem trước hình ảnh do Gemini 2.5 tạo), mô hình tạo hình ảnh gốc mới nhất của chúng tôi.

## Ngày 18 tháng 8 năm 2025

- Phát hành [công cụ bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) cho phiên bản cung cấp công khai (GA), đây là một công cụ cung cấp URL làm bối cảnh bổ sung cho câu lệnh. Chúng tôi sẽ ngừng hỗ trợ việc sử dụng ngữ cảnh URL với mô hình `gemini-2.0-flash` (có trong bản phát hành thử nghiệm) sau một tuần nữa.

## Ngày 14 tháng 8 năm 2025

- Phát hành các mô hình Imagen 4 Ultra, Standard và Fast ở giai đoạn phát hành rộng rãi (GA). Để tìm hiểu thêm, hãy xem trang [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=vi).

## Ngày 7 tháng 8 năm 2025

- Hiện tại, chế độ cài đặt `allow_adult` trong tính năng tạo Video từ hình ảnh đã có ở những khu vực bị hạn chế. Hãy xem trang [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=vi#veo-model-parameters) để biết thông tin chi tiết.

## Ngày 31 tháng 7 năm 2025

- Ra mắt tính năng tạo video từ hình ảnh cho mô hình Veo 3 (bản dùng thử).
- Phát hành mô hình Veo 3 Fast Preview.
- Để tìm hiểu thêm về Veo 3, hãy truy cập vào trang [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi).

## Ngày 22 tháng 7 năm 2025

- Phát hành `gemini-2.5-flash-lite`, mô hình Gemini 2.5 hiệu suất cao, nhanh chóng và chi phí thấp. Để tìm hiểu thêm, hãy xem [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-lite).

## Ngày 17 tháng 7 năm 2025

- Ra mắt `veo-3.0-generate-preview`, bản cập nhật mới nhất cho Veo, bổ sung tính năng tạo video có âm thanh. Để tìm hiểu thêm về Veo 3, hãy truy cập vào trang [Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi).
- Tăng hạn mức tốc độ cho Imagen 4 Standard và Ultra. Hãy truy cập vào trang [Giới hạn về tốc độ](https://ai.google.dev/gemini-api/docs/rate-limits?hl=vi) để biết thêm thông tin chi tiết.

## Ngày 14 tháng 7 năm 2025

- Phát hành `gemini-embedding-001`, phiên bản ổn định của mô hình nhúng văn bản. Để tìm hiểu thêm, hãy xem bài viết về [các vectơ nhúng](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi). Mô hình `gemini-embedding-exp-03-07`
  sẽ ngừng hoạt động từ ngày 14 tháng 8 năm 2025.

## Ngày 7 tháng 7 năm 2025

- Ra mắt Chế độ xử lý theo lô của Gemini API. Gộp các yêu cầu và gửi chúng để xử lý không đồng bộ. Để tìm hiểu thêm, hãy xem phần [Chế độ hàng loạt](https://ai.google.dev/gemini-api/docs/batch-mode?hl=vi).

## Ngày 26 tháng 6 năm 2025

- Các mô hình xem trước `gemini-2.5-pro-preview-05-06` và `gemini-2.5-pro-preview-03-25` hiện đang chuyển hướng đến phiên bản ổn định mới nhất `gemini-2.5-pro`.
- `gemini-2.5-pro-exp-03-25` đã tắt.

## Ngày 24 tháng 6 năm 2025

- Phát hành các mô hình Xem trước tiêu chuẩn và Ultra của Imagen 4. Để tìm hiểu thêm, hãy xem trang [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi).

## Ngày 17 tháng 6 năm 2025

- Phát hành `gemini-2.5-pro`, phiên bản ổn định của mô hình mạnh mẽ nhất của chúng tôi, hiện có khả năng tư duy thích ứng. Để tìm hiểu thêm, hãy xem [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-pro) và [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi). `gemini-2.5-pro-preview-05-06` sẽ được chuyển hướng đến `gemini-2.5-pro` vào ngày 26 tháng 6 năm 2025.
- Phát hành `gemini-2.5-flash`, mô hình 2.5 Flash ổn định đầu tiên của chúng tôi. Để tìm hiểu thêm, hãy xem [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash).
  `gemini-2.5-flash-preview-04-17` sẽ ngừng hoạt động kể từ ngày 15 tháng 7 năm 2025.
- Phát hành mô hình Gemini 2.5 `gemini-2.5-flash-lite-preview-06-17` có hiệu suất cao và chi phí thấp. Để tìm hiểu thêm, hãy xem phần [Bản xem trước Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-lite).

## Ngày 5 tháng 6 năm 2025

- Phát hành `gemini-2.5-pro-preview-06-05`, một phiên bản mới của mô hình mạnh mẽ nhất của chúng tôi, hiện có khả năng tư duy thích ứng. Để tìm hiểu thêm, hãy xem phần [Bản dùng thử Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-pro-preview-06-05) và [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).
  `gemini-2.5-pro-preview-05-06` sẽ được chuyển hướng đến `gemini-2.5-pro` vào ngày 26 tháng 6 năm 2025.

## Ngày 27 tháng 5 năm 2025

- Mô hình điều chỉnh cuối cùng hiện có là Gemini 1.5 Flash 001 đã ngừng hoạt động.
  Tính năng điều chỉnh không còn được hỗ trợ trên bất kỳ mô hình nào.
  Xem phần [Tinh chỉnh bằng Gemini API](https://ai.google.dev/gemini-api/docs/model-tuning?hl=vi).

## Ngày 20 tháng 5 năm 2025

**Các bản cập nhật API:**

- Ra mắt tính năng hỗ trợ [xử lý trước video tuỳ chỉnh](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#customize-video-processing) bằng cách sử dụng các khoảng thời gian cắt và lấy mẫu tốc độ khung hình có thể định cấu hình.
- Ra mắt tính năng sử dụng nhiều công cụ, hỗ trợ việc định cấu hình [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi) trên cùng một yêu cầu `generateContent`.
- Ra mắt tính năng hỗ trợ [các lệnh gọi hàm không đồng bộ](https://ai.google.dev/gemini-api/docs/live-tools?hl=vi#async-function-calling) trong Live API.
- Ra mắt [công cụ bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) thử nghiệm để cung cấp URL làm bối cảnh bổ sung cho câu lệnh.

**Bản cập nhật mô hình:**

- Phát hành `gemini-2.5-flash-preview-05-20`, một mô hình [xem trước](https://ai.google.dev/gemini-api/docs/models?hl=vi#model-versions) Gemini được tối ưu hoá về hiệu suất và khả năng tư duy thích ứng. Để tìm hiểu thêm, hãy xem phần [Bản xem trước Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-preview) và [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).
- Phát hành các mô hình [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-pro-preview-tts) và [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-preview-tts) có khả năng [tạo lời nói](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi) với một hoặc hai người nói.
- Phát hành mô hình `lyria-realtime-exp`, có khả năng [tạo nhạc](https://ai.google.dev/gemini-api/docs/music-generation?hl=vi) theo thời gian thực.
- Phát hành `gemini-2.5-flash-preview-native-audio-dialog` và `gemini-2.5-flash-exp-native-audio-thinking-dialog`, các mô hình Gemini mới cho Live API có khả năng đầu ra âm thanh gốc. Để tìm hiểu thêm, hãy xem [hướng dẫn về Live API](https://ai.google.dev/gemini-api/docs/live-guide?hl=vi#native-audio-output) và [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-native-audio).
- Bản xem trước `gemma-3n-e4b-it` đã phát hành, có trên [AI Studio](https://aistudio.google.com?hl=vi) và thông qua Gemini API, trong khuôn khổ việc ra mắt [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=vi).

## Ngày 7 tháng 5 năm 2025

- Phát hành `gemini-2.0-flash-preview-image-generation`, một mô hình xem trước để tạo và chỉnh sửa hình ảnh. Để tìm hiểu thêm, hãy xem phần [Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi) và [Tính năng tạo hình ảnh của Gemini 2.0 Flash (bản dùng thử)](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.0-flash-preview-image-generation).

## Ngày 6 tháng 5 năm 2025

- Phát hành `gemini-2.5-pro-preview-05-06`, một phiên bản mới của mô hình mạnh mẽ nhất của chúng tôi, với những điểm cải tiến về mã và lệnh gọi hàm. `gemini-2.5-pro-preview-03-25`sẽ tự động trỏ đến phiên bản mới của mô hình.

## Ngày 17 tháng 4 năm 2025

- Phát hành `gemini-2.5-flash-preview-04-17`, một mô hình [xem trước](https://ai.google.dev/gemini-api/docs/models?hl=vi#model-versions) Gemini được tối ưu hoá về hiệu suất và khả năng tư duy thích ứng. Để tìm hiểu thêm, hãy xem phần [Bản xem trước Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-flash-preview) và [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).

## Ngày 16 tháng 4 năm 2025

- Ra mắt tính năng lưu vào bộ nhớ đệm bối cảnh cho [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.0-flash).

## Ngày 9 tháng 4 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `veo-2.0-generate-001`, một mô hình chuyển văn bản và hình ảnh sang video ở giai đoạn phát hành rộng rãi (GA), có khả năng tạo ra những video chi tiết và giàu sắc thái nghệ thuật. Để tìm hiểu thêm, hãy xem [tài liệu về Veo](https://ai.google.dev/gemini-api/docs/video?hl=vi).
- Phát hành `gemini-2.0-flash-live-001`, một phiên bản xem trước công khai của mô hình [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) có bật tính năng thanh toán.

  - **Quản lý phiên và độ tin cậy nâng cao**

    - **Tiếp tục phiên:** Duy trì phiên hoạt động trong thời gian mạng bị gián đoạn tạm thời. API này hiện hỗ trợ tính năng lưu trữ trạng thái phiên ở phía máy chủ (tối đa 24 giờ) và cung cấp các hàm (session\_resumption) để kết nối lại và tiếp tục từ nơi bạn đã dừng.
    - **Các phiên dài hơn thông qua tính năng nén ngữ cảnh:** Cho phép các lượt tương tác kéo dài hơn giới hạn thời gian trước đó. Định cấu hình tính năng nén cửa sổ ngữ cảnh bằng cơ chế cửa sổ trượt để tự động quản lý độ dài ngữ cảnh, ngăn chặn tình trạng kết thúc đột ngột do giới hạn ngữ cảnh.
    - **Thông báo ngắt kết nối một cách êm ái:** Nhận thông báo từ máy chủ `GoAway` cho biết thời điểm một kết nối sắp đóng, cho phép xử lý một cách êm ái trước khi kết thúc.
  - **Kiểm soát nhiều hơn đối với động lực tương tác**
  - **Tính năng phát hiện hoạt động bằng giọng nói (VAD) có thể định cấu hình:** Chọn mức độ nhạy hoặc tắt hoàn toàn tính năng VAD tự động và sử dụng các sự kiện mới của ứng dụng (`activityStart`, `activityEnd`) để điều khiển lượt theo cách thủ công.
  - **Xử lý gián đoạn có thể định cấu hình:** Quyết định xem hoạt động đầu vào của người dùng có nên làm gián đoạn phản hồi của mô hình hay không.
  - **Phạm vi phủ sóng có thể định cấu hình:** Chọn xem API xử lý liên tục tất cả dữ liệu đầu vào âm thanh và video hay chỉ ghi lại dữ liệu đầu vào khi phát hiện thấy người dùng cuối đang nói.
  - **Độ phân giải nội dung nghe nhìn có thể định cấu hình:** Tối ưu hoá chất lượng hoặc mức sử dụng mã thông báo bằng cách chọn độ phân giải cho nội dung nghe nhìn đầu vào.
  - **Đầu ra và tính năng phong phú hơn**
  - **Mở rộng các lựa chọn về giọng nói và ngôn ngữ:** Chọn trong số 2 giọng nói mới và 30 ngôn ngữ mới cho đầu ra âm thanh. Giờ đây, bạn có thể định cấu hình ngôn ngữ đầu ra trong `speechConfig`.
  - **Truyền trực tuyến văn bản:** Nhận phản hồi bằng văn bản theo từng phần khi văn bản được tạo, giúp hiển thị nhanh hơn cho người dùng.
  - **Báo cáo mức sử dụng mã thông báo:** Nắm được thông tin chi tiết về mức sử dụng thông qua số lượng mã thông báo chi tiết được cung cấp trong trường `usageMetadata` của thông báo máy chủ, được phân tích theo phương thức và giai đoạn của câu lệnh hoặc câu trả lời.

## Ngày4 tháng 4 năm 2025

- Phát hành `gemini-2.5-pro-preview-03-25`, phiên bản Gemini 2.5 Pro dùng thử công khai có tính năng thanh toán. Bạn có thể tiếp tục sử dụng `gemini-2.5-pro-exp-03-25` ở cấp miễn phí.

## Ngày 25 tháng 3 năm 2025

- Phát hành `gemini-2.5-pro-exp-03-25`, một mô hình Gemini thử nghiệm công khai, luôn bật chế độ tư duy theo mặc định.
  Để tìm hiểu thêm, hãy xem phần [Gemini 2.5 Pro (thử nghiệm)](https://ai.google.dev/gemini-api/docs/models?hl=vi#gemini-2.5-pro-preview-03-25).

## Ngày 12 tháng 3 năm 2025

**Bản cập nhật mô hình:**

- Ra mắt mô hình thử nghiệm [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi#gemini) có khả năng tạo và chỉnh sửa hình ảnh.
- Được phát hành `gemma-3-27b-it`, có trên [AI Studio](https://aistudio.google.com?hl=vi) và thông qua Gemini API, trong khuôn khổ việc ra mắt [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=vi).

**Các bản cập nhật API:**

- Thêm tính năng hỗ trợ cho [URL YouTube](https://ai.google.dev/gemini-api/docs/vision?hl=vi#youtube) làm nguồn nội dung nghe nhìn.
- Đã thêm tính năng hỗ trợ để đưa [video cùng dòng](https://ai.google.dev/gemini-api/docs/vision?hl=vi#inline-video) có kích thước dưới 20 MB vào.

## Ngày 11 tháng 3 năm 2025

**Nội dung cập nhật đối với SDK:**

- Phát hành [Google Gen AI SDK cho TypeScript và JavaScript](https://googleapis.github.io/js-genai) ở chế độ xem trước công khai.

## Ngày 7 tháng 3 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `gemini-embedding-exp-03-07`, một mô hình nhúng dựa trên Gemini [thử nghiệm](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=vi) trong bản dùng thử công khai.

## Ngày 28 tháng 2 năm 2025

**Các bản cập nhật API:**

- Hỗ trợ tính năng [Tìm kiếm dưới dạng công cụ](https://ai.google.dev/gemini-api/docs/grounding?hl=vi) được thêm vào `gemini-2.0-pro-exp-02-05`, một mô hình thử nghiệm dựa trên Gemini 2.0 Pro.

## Ngày 25 tháng 2 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `gemini-2.0-flash-lite`, phiên bản phát hành rộng rãi (GA) của [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-2.0-flash-lite), được tối ưu hoá về tốc độ, quy mô và hiệu quả chi phí.

## Ngày 19 tháng 2 năm 2025

**Tin cập nhật về AI Studio:**

- Hỗ trợ [các khu vực khác](https://ai.google.dev/gemini-api/docs/available-regions?hl=vi) (Kosovo, Greenland và Quần đảo Faroe).

**Các bản cập nhật API:**

- Hỗ trợ [các khu vực khác](https://ai.google.dev/gemini-api/docs/available-regions?hl=vi) (Kosovo, Greenland và Quần đảo Faroe).

## Ngày 18 tháng 2 năm 2025

**Bản cập nhật mô hình:**

- Gemini 1.0 Pro không còn được hỗ trợ nữa. Để biết danh sách các mô hình được hỗ trợ, hãy xem phần [Các mô hình Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi).

## Ngày 11 tháng 2 năm 2025

**Các bản cập nhật API:**

- Thông tin cập nhật về [khả năng tương thích của các thư viện OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=vi).

## Ngày 6 tháng 2 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `imagen-3.0-generate-002`, một phiên bản được cung cấp rộng rãi (GA) của [Imagen 3 trong Gemini API](https://ai.google.dev/gemini-api/docs/imagen?hl=vi).

**Nội dung cập nhật đối với SDK:**

- Phát hành [Google Gen AI SDK cho Java](https://github.com/googleapis/java-genai) để dùng thử công khai.

## Ngày 5 tháng 2 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `gemini-2.0-flash-001`, phiên bản phát hành rộng rãi (GA) của [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-2.0-flash) hỗ trợ đầu ra chỉ bằng văn bản.
- Phát hành `gemini-2.0-pro-exp-02-05`, một phiên bản xem trước công khai [thử nghiệm](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=vi) của Gemini 2.0 Pro.
- Phát hành `gemini-2.0-flash-lite-preview-02-05`, một [mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-2.0-flash-lite) thử nghiệm xem trước công khai được tối ưu hoá để mang lại hiệu quả chi phí.

**Các bản cập nhật API:**

- Thêm tính năng hỗ trợ [đầu vào tệp và đầu ra đồ thị](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi#input-output) vào quá trình thực thi mã.

**Nội dung cập nhật đối với SDK:**

- Phát hành [Google Gen AI SDK cho Python](https://googleapis.github.io/python-genai/) cho giai đoạn phát hành rộng rãi (GA).

## Ngày 21 tháng 1 năm 2025

**Bản cập nhật mô hình:**

- Phát hành `gemini-2.0-flash-thinking-exp-01-21`, phiên bản dùng thử mới nhất của mô hình đằng sau [Mô hình Gemini 2.0 Flash Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=vi).

## Ngày 19 tháng 12 năm 2024

**Bản cập nhật mô hình:**

- Phát hành Chế độ tư duy Gemini 2.0 Flash cho bản dùng thử công khai. Chế độ Tư duy là một mô hình tính toán trong thời gian thử nghiệm, cho phép bạn xem quy trình tư duy của mô hình trong khi mô hình tạo phản hồi và tạo ra các phản hồi có khả năng suy luận mạnh mẽ hơn.

  Đọc thêm về Chế độ tư duy 2.0 Flash của Gemini trên [trang tổng quan](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=vi) của chúng tôi.

## Ngày 11 tháng 12 năm 2024

**Bản cập nhật mô hình:**

- Phát hành [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-2.0-flash) để dùng thử công khai. Danh sách một phần các tính năng của Gemini 2.0 Flash Experimental bao gồm:
  - Nhanh gấp đôi so với Gemini 1.5 Pro
  - Phát trực tiếp hai chiều bằng Live API
  - Tạo câu trả lời đa phương thức dưới dạng văn bản, hình ảnh và lời nói
  - Sử dụng công cụ tích hợp với khả năng suy luận nhiều lượt để dùng các tính năng như thực thi mã, Tìm kiếm, gọi hàm, v.v.

Đọc thêm về Gemini 2.0 Flash trên [trang tổng quan](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=vi) của chúng tôi.

## Ngày 21 tháng 11 năm 2024

**Bản cập nhật mô hình:**

- Phát hành `gemini-exp-1121`, một mô hình Gemini API thử nghiệm mạnh mẽ hơn nữa.

**Bản cập nhật mô hình:**

- Cập nhật các bí danh mô hình `gemini-1.5-flash-latest` và `gemini-1.5-flash` để sử dụng `gemini-1.5-flash-002`.
  - Thay đổi thành tham số `top_k`: Mô hình `gemini-1.5-flash-002` hỗ trợ các giá trị `top_k` từ 1 đến 41 (không bao gồm).
    Các giá trị lớn hơn 40 sẽ được thay đổi thành 40.

## Ngày 14 tháng 11 năm 2024

**Bản cập nhật mô hình:**

- Phát hành `gemini-exp-1114`, một mô hình Gemini API thử nghiệm mạnh mẽ.

## Ngày 8 tháng 11 năm 2024

**Các bản cập nhật API:**

- Đã thêm [hỗ trợ cho Gemini](https://ai.google.dev/gemini-api/docs/openai?hl=vi) trong các thư viện OpenAI / REST API.

## Ngày 31 tháng 10 năm 2024

**Các bản cập nhật API:**

- Thêm [khả năng hỗ trợ cho tính năng Dựa trên kết quả của Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/grounding?hl=vi).

## Ngày 3 tháng 10 năm 2024

**Bản cập nhật mô hình:**

- Phát hành `gemini-1.5-flash-8b-001`, một phiên bản ổn định của mô hình API Gemini nhỏ nhất của chúng tôi.

## Ngày 24 tháng 9 năm 2024

**Bản cập nhật mô hình:**

- Phát hành `gemini-1.5-pro-002` và `gemini-1.5-flash-002`, hai phiên bản ổn định mới của Gemini 1.5 Pro và 1.5 Flash, ở giai đoạn phát hành rộng rãi.
- Cập nhật mã mô hình `gemini-1.5-pro-latest` để sử dụng `gemini-1.5-pro-002` và mã mô hình `gemini-1.5-flash-latest` để sử dụng `gemini-1.5-flash-002`.
- Phát hành `gemini-1.5-flash-8b-exp-0924` để thay thế `gemini-1.5-flash-8b-exp-0827`.
- Phát hành [bộ lọc an toàn về tính toàn vẹn của công dân](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi#safety-filters) cho Gemini API và AI Studio.
- Phát hành tính năng hỗ trợ 2 tham số mới cho Gemini 1.5 Pro và 1.5 Flash trong Python và NodeJS: [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=vi#FIELDS.frequency_penalty) và [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=vi#FIELDS.presence_penalty).

## Ngày 19 tháng 9 năm 2024

**Tin cập nhật về AI Studio:**

- Thêm nút thích và không thích vào các câu trả lời của mô hình để cho phép người dùng đưa ra ý kiến phản hồi về chất lượng của câu trả lời.

**Các bản cập nhật API:**

- Thêm chế độ hỗ trợ cho các khoản tín dụng của Google Cloud. Giờ đây, bạn có thể dùng các khoản tín dụng này cho việc sử dụng Gemini API.

## Ngày 17 tháng 9 năm 2024

**Tin cập nhật về AI Studio:**

- Thêm nút **Mở trong Colab** để xuất một câu lệnh và mã để kích hoạt câu lệnh đó sang một sổ tay Colab. Tính năng này hiện chưa hỗ trợ việc đưa ra lời nhắc bằng các công cụ (chế độ JSON, gọi hàm hoặc thực thi mã).

## Ngày 13 tháng 9 năm 2024

**Tin cập nhật về AI Studio:**

- Thêm chế độ so sánh để bạn có thể so sánh các câu trả lời trên nhiều mô hình và câu lệnh nhằm tìm ra câu trả lời phù hợp nhất cho trường hợp sử dụng của bạn.

## Ngày 30 tháng 8 năm 2024

**Bản cập nhật mô hình:**

- Gemini 1.5 Flash hỗ trợ [cung cấp giản đồ JSON thông qua cấu hình mô hình](https://ai.google.dev/gemini-api/docs/json-mode?hl=vi#supply-schema-in-config).

## Ngày 27 tháng 8 năm 2024

**Bản cập nhật mô hình:**

- Phát hành [các mô hình thử nghiệm](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=vi) sau đây:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## Ngày 9 tháng 8 năm 2024

**Các bản cập nhật API:**

- Thêm tính năng hỗ trợ [xử lý tệp PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).

## Ngày 5 tháng 8 năm 2024

**Bản cập nhật mô hình:**

- Đã phát hành tính năng tinh chỉnh cho Gemini 1.5 Flash.

## Ngày 1 tháng 8 năm 2024

**Bản cập nhật mô hình:**

- Phát hành `gemini-1.5-pro-exp-0801`, một phiên bản thử nghiệm mới của [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-1.5-pro).

## Ngày 12 tháng 7 năm 2024

**Bản cập nhật mô hình:**

- Xoá tính năng hỗ trợ Gemini 1.0 Pro Vision khỏi các dịch vụ và công cụ AI của Google.

## Ngày 27 tháng 6 năm 2024

**Bản cập nhật mô hình:**

- Giai đoạn phát hành rộng rãi cho cửa sổ ngữ cảnh 2 triệu token của Gemini 1.5 Pro.

**Các bản cập nhật API:**

- Thêm tính năng hỗ trợ cho [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi).

## Ngày 18 tháng 6 năm 2024

**Các bản cập nhật API:**

- Thêm tính năng hỗ trợ cho [hoạt động lưu vào bộ nhớ đệm theo bối cảnh](https://ai.google.dev/gemini-api/docs/caching?hl=vi).

## Ngày 12 tháng 6 năm 2024

**Bản cập nhật mô hình:**

- Gemini 1.0 Pro Vision không còn được dùng nữa.

## Ngày 23 tháng 5 năm 2024

**Bản cập nhật mô hình:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-1.5-pro) (`gemini-1.5-pro-001`) hiện đã được cung cấp rộng rãi (GA).
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-1.5-flash) (`gemini-1.5-flash-001`) đã được phát hành rộng rãi (GA).

## Ngày 14 tháng 5 năm 2024

**Các bản cập nhật API:**

- Ra mắt cửa sổ ngữ cảnh 2 triệu token cho Gemini 1.5 Pro (danh sách chờ).
- Ra mắt chế độ [thanh toán](https://ai.google.dev/gemini-api/docs/billing?hl=vi) trả tiền theo mức dùng cho Gemini 1.0 Pro, trong đó chế độ thanh toán cho Gemini 1.5 Pro và Gemini 1.5 Flash sẽ ra mắt trong thời gian tới.
- Giới thiệu hạn mức tăng lên cho cấp có tính phí sắp tới của Gemini 1.5 Pro.
- Thêm tính năng hỗ trợ video tích hợp vào [File API](https://ai.google.dev/api/rest/v1beta/files?hl=vi).
- Thêm tính năng hỗ trợ văn bản thuần tuý vào [File API](https://ai.google.dev/api/rest/v1beta/files?hl=vi).
- Thêm tính năng hỗ trợ gọi hàm song song, trả về nhiều lệnh gọi cùng một lúc.

## Ngày 10 tháng 5 năm 2024

**Bản cập nhật mô hình:**

- Phát hành [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-1.5-flash) (`gemini-1.5-flash-latest`) ở chế độ xem trước.

## Ngày 9 tháng 4 năm 2024

**Bản cập nhật mô hình:**

- Phát hành [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#gemini-1.5-pro) (`gemini-1.5-pro-latest`) ở chế độ xem trước.
- Phát hành một mô hình nhúng văn bản mới, `text-embeddings-004`, hỗ trợ các kích thước [nhúng linh hoạt](https://ai.google.dev/gemini-api/docs/embeddings?hl=vi#elastic-embedding) dưới 768.

**Các bản cập nhật API:**

- Phát hành [File API](https://ai.google.dev/api/rest/v1beta/files?hl=vi) để tạm thời lưu trữ các tệp đa phương tiện để dùng trong quá trình tạo câu lệnh.
- Thêm tính năng hỗ trợ đặt câu lệnh bằng dữ liệu văn bản, hình ảnh và âm thanh, còn được gọi là đặt câu lệnh *đa phương thức*. Để tìm hiểu thêm, hãy xem bài viết [Đưa ra câu lệnh bằng nội dung nghe nhìn](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=vi).
- Phát hành [Hướng dẫn hệ thống](https://ai.google.dev/gemini-api/docs/system-instructions?hl=vi) ở giai đoạn thử nghiệm beta.
- Thêm [Chế độ gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi#function_calling_mode), xác định hành vi thực thi cho việc gọi hàm.
- Đã thêm chế độ hỗ trợ cho lựa chọn cấu hình `response_mime_type`, cho phép bạn yêu cầu phản hồi ở [định dạng JSON](https://ai.google.dev/gemini-api/docs/api-overview?hl=vi#json).

## Ngày 19 tháng 3 năm 2024

**Bản cập nhật mô hình:**

- Đã thêm chức năng hỗ trợ [điều chỉnh Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) trong Google AI Studio hoặc bằng Gemini API.

## Ngày 13 tháng 12 năm 2023

**Bản cập nhật mô hình:**

- gemini-pro: Mô hình văn bản mới cho nhiều loại nhiệm vụ. Cân bằng khả năng và hiệu quả.
- gemini-pro-vision: Mô hình đa phương thức mới cho nhiều loại nhiệm vụ.
  Cân bằng khả năng và hiệu quả.
- embedding-001: Mô hình nhúng mới.
- aqa: Một mô hình mới được điều chỉnh đặc biệt để trả lời các câu hỏi bằng cách sử dụng các đoạn văn bản để làm cơ sở cho câu trả lời được tạo.

Hãy xem bài viết [Các mô hình Gemini](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi) để biết thêm thông tin.

**Các bản cập nhật phiên bản API:**

- v1: Kênh API ổn định.
- v1beta: Kênh thử nghiệm Beta. Kênh này có các tính năng có thể đang trong quá trình phát triển.

Hãy xem [chủ đề về các phiên bản API](https://ai.google.dev/gemini-api/docs/api-versions?hl=vi) để biết thêm thông tin chi tiết.

**Các bản cập nhật API:**

- `GenerateContent` là một điểm cuối hợp nhất duy nhất cho cuộc trò chuyện và tin nhắn văn bản.
- Phát trực tuyến bằng phương thức `StreamGenerateContent`.
- Chức năng đa phương thức: Hình ảnh là một phương thức mới được hỗ trợ
- Các tính năng thử nghiệm mới:
  - [Lệnh gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=vi)
  - Tính năng Trả lời câu hỏi có trích dẫn (AQA)
- Số lượng đề xuất được cập nhật: Các mô hình Gemini chỉ trả về 1 đề xuất.
- Các danh mục Chế độ cài đặt về an toàn và SafetyRating. Hãy xem [chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi) để biết thêm thông tin.
- Các mô hình Gemini hiện chưa hỗ trợ tính năng điều chỉnh mô hình (Đang tiến hành).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-05 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-05 UTC."],[],[]]
