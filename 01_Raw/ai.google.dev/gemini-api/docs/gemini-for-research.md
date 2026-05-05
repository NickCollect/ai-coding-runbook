---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=vi
fetched_at: 2026-05-05T20:42:58.306510+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)

# Tăng tốc độ khám phá bằng Gemini cho Nghiên cứu

[Nhận Gemini API](https://aistudio.google.com/apikey?hl=vi)

Bạn có thể sử dụng các mô hình Gemini để thúc đẩy nghiên cứu cơ bản trên nhiều lĩnh vực.
Dưới đây là những cách bạn có thể khám phá Gemini cho nghiên cứu của mình:

- **Phân tích và kiểm soát kết quả đầu ra của mô hình**: Để phân tích thêm, bạn có thể kiểm tra một
  ứng viên phản hồi do mô hình tạo bằng các công cụ như
  `CitationMetadata`. Bạn cũng có thể định cấu hình các lựa chọn cho quá trình tạo và kết quả đầu ra của mô hình, chẳng hạn như `responseSchema`, `topP` và `topK`. [Tìm hiểu thêm](https://ai.google.dev/api/generate-content?hl=vi).
- **Đầu vào đa phương thức**: Gemini có thể xử lý hình ảnh, âm thanh và video, mở ra nhiều hướng nghiên cứu thú vị. [Tìm hiểu thêm](https://ai.google.dev/gemini-api/docs/vision?hl=vi).
- **Khả năng ngữ cảnh dài**: Gemini 3.0 Flash và Pro có cửa sổ ngữ cảnh 1 triệu token. [Tìm hiểu thêm](https://ai.google.dev/gemini-api/docs/long-context?hl=vi).
- **Grow with Google**: Truy cập nhanh vào các mô hình Gemini thông qua API và Google AI
  Studio cho các trường hợp sử dụng trong quá trình sản xuất. Nếu bạn đang tìm kiếm một nền tảng dựa trên Google Cloud, thì Nền tảng tác nhân Gemini Enterprise có thể cung cấp thêm cơ sở hạ tầng hỗ trợ.

Để hỗ trợ nghiên cứu học thuật và thúc đẩy nghiên cứu tiên tiến, Google cung cấp
quyền truy cập vào hạn mức tín dụng Gemini API cho các nhà khoa học và nhà nghiên cứu học thuật thông qua
[Chương trình học thuật Gemini](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=vi#gemini-academic-program).

## Làm quen với Gemini

Gemini API và Google AI Studio giúp bạn bắt đầu làm việc với các mô hình mới nhất của Google và biến ý tưởng của bạn thành các ứng dụng có thể mở rộng.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Các nhà nghiên cứu học thuật nổi bật

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=vi)

"Nghiên cứu của chúng tôi điều tra Gemini dưới dạng một mô hình ngôn ngữ trực quan (VLM) và hành vi của tác nhân trong nhiều môi trường từ góc độ tính ổn định và an toàn. Cho đến nay, chúng tôi đã đánh giá tính ổn định của Gemini trước các yếu tố gây xao nhãng như cửa sổ bật lên khi các tác nhân VLM thực hiện các tác vụ trên máy tính và đã tận dụng Gemini để phân tích tương tác xã hội, các sự kiện tạm thời cũng như các yếu tố rủi ro dựa trên đầu vào video."

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=vi)

"Gemini Pro và Flash, với cửa sổ ngữ cảnh dài, đã giúp chúng tôi trong OK-Robot, dự án thao tác trên thiết bị di động có từ vựng mở của chúng tôi. Gemini cho phép các truy vấn và lệnh bằng ngôn ngữ tự nhiên phức tạp trên "bộ nhớ" của robot: trong trường hợp này, các quan sát trước đây do robot thực hiện trong thời gian hoạt động dài. Tôi và Mahi Shafiullah cũng đang sử dụng Gemini để phân tách các tác vụ thành mã mà robot có thể thực thi trong thế giới thực."

## Chương trình học thuật Gemini

Các nhà nghiên cứu học thuật đủ điều kiện (chẳng hạn như giảng viên, nhân viên và sinh viên tiến sĩ) ở các quốc gia [được hỗ trợ](https://ai.google.dev/gemini-api/docs/available-regions?hl=vi) có thể đăng ký để nhận hạn mức tín dụng Gemini API
và hạn mức cao hơn cho các dự án nghiên cứu. Sự hỗ trợ này cho phép thông lượng cao hơn cho các thí nghiệm khoa học và thúc đẩy nghiên cứu.

Chúng tôi đặc biệt quan tâm đến các lĩnh vực nghiên cứu trong phần sau, nhưng chúng tôi hoan nghênh các đơn đăng ký từ nhiều lĩnh vực khoa học:

- **Đánh giá và điểm chuẩn**: Các phương pháp đánh giá được cộng đồng xác nhận có thể cung cấp tín hiệu hiệu quả mạnh mẽ trong các lĩnh vực như tính xác thực, mức độ an toàn, tuân theo hướng dẫn, suy luận và lập kế hoạch.
- **Thúc đẩy khám phá khoa học để mang lại lợi ích cho nhân loại**: Các ứng dụng tiềm năng
  của AI trong nghiên cứu khoa học liên ngành, bao gồm các lĩnh vực
  như bệnh hiếm gặp và bị bỏ quên, sinh học thực nghiệm, khoa học vật liệu,
  và tính bền vững.
- **Hiện thân và tương tác**: Sử dụng các mô hình ngôn ngữ lớn để
  điều tra các tương tác mới trong các lĩnh vực AI hiện thân, tương tác xung quanh,
  robot học và tương tác giữa người và máy tính.
- **Khả năng mới nổi**: Khám phá các khả năng của tác nhân AI mới cần thiết để nâng cao khả năng suy luận và lập kế hoạch, cũng như cách mở rộng các khả năng trong quá trình suy luận (ví dụ: bằng cách sử dụng Gemini Flash).
- **Tương tác và hiểu biết đa phương thức**: Xác định các khoảng trống và cơ hội cho các mô hình nền tảng đa phương thức để phân tích, suy luận và lập kế hoạch trên nhiều tác vụ.

Điều kiện: Chỉ những cá nhân (giảng viên, nhà nghiên cứu hoặc tương đương) liên kết với một tổ chức học thuật hợp lệ hoặc tổ chức nghiên cứu học thuật mới có thể đăng ký. Xin lưu ý rằng quyền truy cập API và hạn mức tín dụng sẽ được cấp và xoá theo quyết định của Google. Chúng tôi xem xét các đơn đăng ký hằng tháng.

### Bắt đầu nghiên cứu bằng Gemini API

[Đăng ký ngay](https://forms.gle/HMviQstU8PxC5iCt5)

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
