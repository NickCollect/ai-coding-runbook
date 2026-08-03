---
source_url: https://ai.google.dev/gemini-api/docs/robotics-overview?hl=vi
fetched_at: 2026-08-03T04:41:25.062504+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Gemini Robotics ER

Các mô hình Gemini Robotics ER (lý luận dựa trên dữ liệu thực tế) là các mô hình ngôn ngữ thị giác (VLM) cho phép robot nhận thức và tương tác với thế giới thực. Các mô hình này diễn giải dữ liệu trực quan, thực hiện suy luận về không gian và thời gian, lập kế hoạch cho các tác vụ nhiều bước, đồng thời điều phối các robot và công cụ.

## Mô hình

Mô hình Gemini Robotics ER 2 là mô hình mới nhất của Gemini Robotics.
Đây là mô hình suy luận mới nhất của chúng tôi, giúp robot hiểu chính xác môi trường xung quanh. Mô hình này chuyên về các khả năng suy luận dựa trên cơ thể, chẳng hạn như điều phối các tác nhân của robot (ví dụ: sử dụng VLA), khả năng hiểu video về robot, bao gồm cả khả năng hiểu tiến trình và phát hiện thành công, khả năng đọc thiết bị, chỉ và suy luận không gian.

Mô hình Gemini Robotics ER 2 giới thiệu 2 điểm cuối mô hình:

- **`gemini-robotics-er-2-preview`**: Mô hình ER 2 tiêu chuẩn. Dựa trên Gemini 3.5 Flash với khả năng suy luận không gian, tìm khoảnh khắc trong video, phân loại tiến trình video, điều phối nhiều robot và sử dụng công cụ nhiều bước được cải thiện.
- **`gemini-robotics-er-2-streaming-preview`**: Được tối ưu hoá để phát trực tiếp theo thời gian thực thông qua [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi). Sử dụng mô hình này cho các tác nhân robot có độ trễ thấp, xử lý liên tục tín hiệu âm thanh và video đầu vào.

Nếu đang sử dụng Gemini Robotics ER 1.6, hãy nâng cấp lên Gemini Robotics ER 2 bằng cách thay thế `model="gemini-robotics-er-1.6-preview"` bằng `model="gemini-robotics-er-2-preview"` hoặc `model="gemini-robotics-er-2-streaming-preview"` trong các lệnh gọi API. Xin lưu ý rằng mô hình Gemini Robotics ER 1.6 sẽ ngừng hoạt động vào [cuối tháng 8](https://ai.google.dev/gemini-api/docs/deprecations?hl=vi#robotics-models).

[Dùng thử Gemini Robotics ER 2 trong Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=vi)

## Các chức năng của robot

Gemini Robotics ER hỗ trợ nhiều khả năng suy luận dựa trên dữ liệu thực tế.
Chọn một khả năng để tìm hiểu thêm:

| Chức năng | Mô tả | Hướng dẫn |
| --- | --- | --- |
| Suy luận không gian | Chỉ vào các đối tượng, theo dõi chúng trong video, phát hiện bằng khung hình chữ nhật, lập kế hoạch cho quỹ đạo. | [Suy luận không gian](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=vi) |
| Tầm nhìn dựa trên tác nhân | Sử dụng tính năng thực thi mã để nâng cao các khả năng khác bằng cách tận dụng các công cụ chỉnh sửa hình ảnh. | [Thị giác dựa trên trợ lý AI](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=vi) |
| Điều phối tác vụ | Kết hợp khả năng suy luận không gian với các API robot tuỳ chỉnh để hoàn thành các tác vụ trong thời gian dài. | [Điều phối công việc](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=vi) |
| Truyền trực tuyến (chỉ dành cho điểm cuối Truyền trực tuyến Gemini Robotics ER 2) | Truyền trực tuyến hai chiều cho các tác nhân robot theo thời gian thực với chức năng gọi có độ trễ thấp. | [Truyền trực tuyến cho robot](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi) |
| Tiến trình video (chỉ Gemini Robotics ER 2) | Tính năng tìm khoảnh khắc và phân loại tiến trình từ nguồn cấp dữ liệu video liên tục. | [Hiểu video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=vi) |

## Bắt đầu

Ví dụ sau đây tìm các đối tượng trong một hình ảnh và trả về nhãn cũng như toạ độ 2D được chuẩn hoá của các đối tượng đó. Bạn có thể chuyển trực tiếp đầu ra này đến một API về robot học hoặc một mô hình VLA để tạo các hành động của robot.

### Python

```
from google import genai

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

image_response = client.interactions.create(
    model="gemini-robotics-er-2-preview",
    input=[
        {
            "type": "image",
            "uri": uploaded_file.uri,
            "mime_type": uploaded_file.mime_type
        },
        {"type": "text", "text": PROMPT}
    ],
    generation_config={"thinking_level": "high"},
)

print(image_response.output_text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-robotics-er-2-preview",
    "input": {
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/png",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
        }
      ]
    },
    "generation_config": {
      "thinking_config": {
        "thinking_level": "high"
      }
    }
  }'
```

Đầu ra sẽ là một mảng JSON chứa các đối tượng, mỗi đối tượng có một `point` (toạ độ `[y, x]` được chuẩn hoá) và một `label` xác định đối tượng.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Hình ảnh sau đây là ví dụ về cách hiển thị các điểm này:

![Ví dụ minh hoạ các điểm của đối tượng trong hình ảnh](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=vi)

## Cách hoạt động

Gemini Robotics ER nhận đầu vào là hình ảnh, video hoặc âm thanh bằng câu lệnh ngôn ngữ tự nhiên. Công cụ này xác định các đối tượng, lý do về bối cảnh cảnh và mối quan hệ không gian, đồng thời trả về đầu ra có cấu trúc như toạ độ hoặc khung hình chữ nhật.

Gemini Robotics ER cũng có khả năng dựa trên tác nhân: mô hình này chia các tác vụ phức tạp thành các tác vụ phụ và thực thi các tác vụ đó bằng cách gọi các hàm robot của bạn hoặc chạy mã được tạo. Ví dụ: "đặt quả táo vào bát" sẽ trở thành một chuỗi các bước tìm, nắm và đặt.

Hãy xem phần [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=vi#how-it-works) để biết thông tin chi tiết về cách Gemini thực hiện lệnh gọi công cụ.

## An toàn

Mặc dù Gemini Robotics ER được xây dựng với mục tiêu đảm bảo an toàn, nhưng bạn vẫn phải chịu trách nhiệm duy trì một môi trường an toàn xung quanh robot. Các mô hình AI tạo sinh có thể mắc lỗi và robot thực có thể gây hư hỏng. Để tìm hiểu thêm, hãy truy cập vào [trang an toàn về robot của Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=vi).

## Các phương pháp hay nhất

1. Sử dụng ngôn ngữ tự nhiên, đơn giản. Mô tả những việc bạn muốn robot làm giống như cách bạn mô tả cho một người. Nếu một cụm từ không hoạt động, hãy thử một từ đồng nghĩa phổ biến.
2. Tối ưu hoá dữ liệu đầu vào trực quan. Cắt hoặc phóng to các đối tượng nhỏ hoặc không rõ ràng trước khi gửi hình ảnh. Ánh sáng và độ tương phản màu thấp có thể ảnh hưởng đến khả năng phát hiện.
3. Chia nhỏ các việc phức tạp thành nhiều bước. Gửi từng bước dưới dạng một câu lệnh riêng biệt để giữ cho mô hình tập trung và cải thiện độ chính xác.
4. Truy vấn nhiều lần và tính trung bình kết quả cho các tác vụ có độ chính xác cao. Phương pháp đồng thuận này giúp giảm sự khác biệt về đầu ra không gian.

## Các điểm hạn chế

Hãy cân nhắc những hạn chế sau đây khi phát triển bằng Gemini Robotics ER:

- **Các quy tắc hạn chế đối với khoá API:** Gemini API không chấp nhận các yêu cầu từ khoá API không bị hạn chế và trả về lỗi `403 Forbidden`. Bảo mật khoá API bằng cách thêm các quy tắc hạn chế trong [AI Studio](https://aistudio.google.com/api-keys?hl=vi).
  Hãy xem bài viết [Bảo mật khoá API không bị hạn chế](https://ai.google.dev/gemini-api/docs/api-key?hl=vi#secure-unrestricted-keys) để biết thông tin chi tiết.
- **Độ trễ so với hiệu suất:** Các truy vấn phức tạp, dữ liệu đầu vào có độ phân giải cao hoặc mức độ tư duy cao có thể dẫn đến thời gian xử lý tăng lên. Đối với cấp độ tư duy, hãy sử dụng mức trung bình để cân bằng giữa độ trễ và hiệu suất.
- **Ảo tưởng:** Giống như mọi mô hình ngôn ngữ lớn, các mô hình ER của Gemini Robotics đôi khi có thể "ảo tưởng" hoặc cung cấp thông tin không chính xác, đặc biệt là đối với những câu lệnh mơ hồ hoặc đầu vào nằm ngoài phân phối.
- **Phụ thuộc vào chất lượng câu lệnh:** Chất lượng đầu ra phụ thuộc vào độ rõ ràng của câu lệnh đầu vào. Sử dụng câu lệnh cụ thể và có cấu trúc rõ ràng.
- **Chi phí điện toán:** Việc chạy mô hình, đặc biệt là với dữ liệu đầu vào là video hoặc `thinking_budget` cao, sẽ tiêu tốn tài nguyên điện toán và phát sinh chi phí.
  Hãy xem trang [Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi) để biết thêm thông tin chi tiết.
- **Loại dữ liệu đầu vào:** Xem các chủ đề sau để biết thông tin chi tiết về hạn chế đối với từng chế độ.
  - [Đầu vào hình ảnh](https://ai.google.dev/gemini-api/docs/image-understanding?hl=vi#technical-details-image)
  - [Đầu vào video](https://ai.google.dev/gemini-api/docs/video-understanding?hl=vi#supported-formats)
  - [Thiết bị đầu vào âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi#supported-formats)

## Thông báo về quyền riêng tư

Bạn xác nhận rằng các mô hình được đề cập trong tài liệu này ("Mô hình robot") tận dụng dữ liệu video và âm thanh để hoạt động và di chuyển phần cứng theo hướng dẫn của bạn. Do đó, bạn có thể vận hành Các mô hình robot sao cho Các mô hình robot sẽ thu thập dữ liệu của những người có thể nhận dạng, chẳng hạn như dữ liệu giọng nói, hình ảnh và dữ liệu về hình ảnh khuôn mặt ("Dữ liệu cá nhân"). Nếu chọn vận hành Các mô hình robot theo cách thu thập Dữ liệu cá nhân, bạn đồng ý rằng bạn sẽ không cho phép bất kỳ cá nhân nào có thể nhận dạng tương tác hoặc xuất hiện trong khu vực xung quanh Các mô hình robot, trừ phi và cho đến khi những cá nhân có thể nhận dạng đó được thông báo đầy đủ và đồng ý với việc Dữ liệu cá nhân của họ có thể được Google cung cấp và sử dụng như được nêu trong Điều khoản dịch vụ bổ sung về Gemini API tại [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=vi) ("Điều khoản"), kể cả theo phần "Cách Google sử dụng dữ liệu của bạn". Bạn sẽ đảm bảo rằng thông báo đó cho phép thu thập và sử dụng dữ liệu cá nhân như quy định trong Điều khoản, đồng thời bạn sẽ nỗ lực hợp lý về phương diện thương mại để giảm thiểu việc thu thập và phân phối dữ liệu cá nhân bằng cách sử dụng các kỹ thuật như làm mờ khuôn mặt và vận hành Mô hình robot ở những khu vực không có người có thể nhận dạng được trong phạm vi có thể thực hiện được.

## Giá

Để biết thông tin chi tiết về giá và các khu vực có cung cấp dịch vụ, hãy tham khảo trang [định giá](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Điểm cuối của mô hình

### Bản xem trước Gemini Robotics ER 2

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | `gemini-robotics-er-2-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Thông tin đầu vào**  Văn bản, hình ảnh, video, âm thanh  **Đầu ra**  Văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  131.072  **Giới hạn mã thông báo đầu ra**  65.536 |
| handymanChức năng | **[Tạo âm thanh](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi)**  Không được hỗ trợ  **[Lưu vào bộ nhớ đệm](https://ai.google.dev/gemini-api/docs/caching?hl=vi)**  Được hỗ trợ  **[Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)**  Được hỗ trợ  **[Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)**  Được hỗ trợ  **[Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)**  Được hỗ trợ  **[Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)**  Được hỗ trợ  **[Neo bám vào Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)**  Được hỗ trợ  **[Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)**  Không được hỗ trợ  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=vi)**  Không được hỗ trợ  **[Tìm trong phần liên kết thực tế](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)**  Được hỗ trợ  **[Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi)**  Được hỗ trợ  **[Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)**  Được hỗ trợ  **[Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)**  Được hỗ trợ |
| speedCác lựa chọn thưởng thức nội dung | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi)**  Được hỗ trợ  **[Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi)**  Không được hỗ trợ  **[Suy luận mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi)**  Không được hỗ trợ |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Xem trước: `gemini-robotics-er-2-preview` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 7 năm 2026 |
| id\_cardThẻ mô hình | [Thẻ mô hình](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=vi) |

### Bản xem trước Gemini Robotics ER 2 Streaming

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | `gemini-robotics-er-2-streaming-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Thông tin đầu vào**  Văn bản, hình ảnh, video, âm thanh  **Đầu ra**  Văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  131.072  **Giới hạn mã thông báo đầu ra**  65.536 |
| handymanChức năng | **[Tạo âm thanh](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi)**  Không được hỗ trợ  **[Lưu vào bộ nhớ đệm](https://ai.google.dev/gemini-api/docs/caching?hl=vi)**  Không được hỗ trợ  **[Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)**  Không được hỗ trợ  **[Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)**  Không được hỗ trợ  **[Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)**  Không được hỗ trợ  **[Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)**  Được hỗ trợ  **[Neo bám vào Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)**  Không được hỗ trợ  **[Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)**  Không được hỗ trợ  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=vi)**  Được hỗ trợ  **[Tìm trong phần liên kết thực tế](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)**  Được hỗ trợ  **[Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi)**  Không được hỗ trợ  **[Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)**  Được hỗ trợ  **[Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)**  Không được hỗ trợ |
| speedCác lựa chọn thưởng thức nội dung | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi)**  Không được hỗ trợ  **[Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi)**  Không được hỗ trợ  **[Suy luận mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi)**  Không được hỗ trợ |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Xem trước: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 7 năm 2026 |
| id\_cardThẻ mô hình | [Thẻ mô hình](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=vi) |

### Bản xem trước Gemini Robotics ER 1.6

| Thuộc tính | Mô tả |
| --- | --- |
| id\_cardMã kiểu máy | `gemini-robotics-er-1.6-preview` |
| saveCác loại dữ liệu được hỗ trợ | **Thông tin đầu vào**  Văn bản, hình ảnh, video, âm thanh  **Đầu ra**  Văn bản |
| token\_autoGiới hạn mã thông báo[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=vi) | **Giới hạn mã thông báo đầu vào**  131.072  **Giới hạn mã thông báo đầu ra**  65.536 |
| handymanChức năng | **[Tạo âm thanh](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi)**  Không được hỗ trợ  **[Lưu vào bộ nhớ đệm](https://ai.google.dev/gemini-api/docs/caching?hl=vi)**  Được hỗ trợ  **[Thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi)**  Được hỗ trợ  **[Sử dụng máy tính](https://ai.google.dev/gemini-api/docs/computer-use?hl=vi)**  Được hỗ trợ  **[Tìm kiếm tệp](https://ai.google.dev/gemini-api/docs/file-search?hl=vi)**  Được hỗ trợ  **[Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi)**  Được hỗ trợ  **[Neo bám vào Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi)**  Được hỗ trợ  **[Tạo hình ảnh](https://ai.google.dev/gemini-api/docs/image-generation?hl=vi)**  Không được hỗ trợ  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=vi)**  Không được hỗ trợ  **[Tìm trong phần liên kết thực tế](https://ai.google.dev/gemini-api/docs/google-search?hl=vi)**  Được hỗ trợ  **[Đầu ra có cấu trúc](https://ai.google.dev/gemini-api/docs/structured-output?hl=vi)**  Được hỗ trợ  **[Tư duy](https://ai.google.dev/gemini-api/docs/thinking?hl=vi)**  Được hỗ trợ  **[Bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi)**  Được hỗ trợ |
| speedCác lựa chọn thưởng thức nội dung | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=vi)**  Được hỗ trợ  **[Suy luận linh hoạt](https://ai.google.dev/gemini-api/docs/flex-inference?hl=vi)**  Không được hỗ trợ  **[Suy luận mức độ ưu tiên](https://ai.google.dev/gemini-api/docs/priority-inference?hl=vi)**  Không được hỗ trợ |
| 123Phiên bản | Đọc [các mẫu phiên bản mô hình](https://ai.google.dev/gemini-api/docs/models/gemini?hl=vi#model-versions) để biết thêm thông tin chi tiết.  - Xem trước: `gemini-robotics-er-1.6-preview` |
| calendar\_monthThông tin cập nhật mới nhất | Tháng 12 năm 2025 |
| cognition\_2Điểm cắt kiến thức | Tháng 1 năm 2025 |

## Bước tiếp theo

- [Lý luận không gian](https://ai.google.dev/gemini-api/docs/robotics-spatial?hl=vi) – trỏ, theo dõi, hộp bao quanh, quỹ đạo.
- [Khả năng của tác nhân AI](https://ai.google.dev/gemini-api/docs/robotics-agentic?hl=vi) – thực thi mã, đọc công cụ, chú thích hình ảnh.
- [Điều phối tác vụ](https://ai.google.dev/gemini-api/docs/robotics-orchestration?hl=vi) – các tác vụ dài hạn bằng API robot tuỳ chỉnh.
- [Robot học có tính năng truyền trực tuyến](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=vi) – truyền trực tuyến hai chiều theo thời gian thực (chỉ Gemini Robotics ER 2).
- [Hiểu video](https://ai.google.dev/gemini-api/docs/robotics-video-progress?hl=vi) – tìm khoảnh khắc và phân loại tiến trình (chỉ Gemini Robotics ER 2).
- [An toàn trong lĩnh vực robot của Google DeepMind](https://deepmind.google/models/gemini-robotics/safety?hl=vi) – nghiên cứu về độ an toàn đằng sau nhóm mô hình này.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-07-30 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-07-30 UTC."],[],[]]
