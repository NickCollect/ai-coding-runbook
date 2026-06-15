---
source_url: https://ai.google.dev/gemini-api/docs/interactions/maps-grounding?hl=vi
fetched_at: 2026-06-15T06:24:33.820060+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/interactions-overview?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng Kết nối với Google Maps kết hợp các khả năng tạo sinh của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng kết hợp chức năng nhận biết vị trí vào ứng dụng của họ. Khi một truy vấn của người dùng có ngữ cảnh liên quan đến dữ liệu Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời chính xác và mới nhất, phù hợp với vị trí cụ thể hoặc khu vực khái quát mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết vị trí:** Tận dụng dữ liệu phong phú và mới nhất của Google Maps cho các truy vấn cụ thể về mặt địa lý.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Kết nối với Google Maps vào ứng dụng của bạn để cung cấp câu trả lời chính xác, nhận biết vị trí cho các truy vấn của người dùng. Lời nhắc yêu cầu các đề xuất tại địa phương kèm theo vị trí không bắt buộc của người dùng, cho phép mô hình Gemini sử dụng dữ liệu của Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What are the best Italian restaurants within a 15-minute walk from here?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

# Print the model's text response and annotations
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "What are the best Italian restaurants within a 15-minute walk from here?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  // Print the model's text response and annotations
  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - {annotation.name}: {annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Cách hoạt động của tính năng Kết nối với Google Maps

Tính năng Kết nối với Google Maps tích hợp Gemini API với hệ sinh thái Địa lý của Google bằng cách sử dụng Maps API làm nguồn kết nối. Khi truy vấn của người dùng chứa ngữ cảnh địa lý, mô hình Gemini có thể gọi công cụ Kết nối với Google Maps. Sau đó, mô hình này có thể tạo câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quá trình này thường bao gồm:

1. **Truy vấn của người dùng:** Người dùng gửi một truy vấn đến ứng dụng của bạn, có thể bao gồm ngữ cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini, nhận ra ý định địa lý, sẽ gọi công cụ Kết nối với Google Maps. Bạn có thể cung cấp `latitude` và `longitude` của người dùng cho công cụ này. Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như tìm kiếm trên Maps, trong đó các truy vấn tại địa phương ("gần tôi") sẽ sử dụng toạ độ, trong khi các truy vấn cụ thể hoặc không phải tại địa phương sẽ không bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Kết nối với Google Maps truy vấn Google Maps để tìm thông tin liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo dựa trên dữ liệu:** Dữ liệu Maps đã truy xuất được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ liên quan.
5. **Câu trả lời và chú thích:** Mô hình này trả về một câu trả lời bằng văn bản kèm theo chú thích nội tuyến liên kết đến các nguồn trên Google Maps, cho phép nhà phát triển hiển thị trích dẫn.

## Lý do và thời điểm nên sử dụng tính năng Kết nối với Google Maps

Tính năng Kết nối với Google Maps là lựa chọn lý tưởng cho những ứng dụng yêu cầu thông tin chính xác, mới nhất và cụ thể theo vị trí. Tính năng này giúp nâng cao trải nghiệm người dùng bằng cách cung cấp nội dung phù hợp và được cá nhân hoá dựa trên cơ sở dữ liệu phong phú của Google Maps về hơn 250 triệu địa điểm trên toàn thế giới.

Bạn nên sử dụng tính năng Kết nối với Google Maps khi ứng dụng của bạn cần:

- Cung cấp câu trả lời đầy đủ và chính xác cho các câu hỏi cụ thể về địa lý.
- Xây dựng trình lập kế hoạch chuyến đi và hướng dẫn viên địa phương theo dạng trò chuyện.
- Đề xuất các điểm tham quan dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ giao đồ ăn, bán lẻ hoặc mạng xã hội.

Tính năng Kết nối với Google Maps hoạt động hiệu quả trong các trường hợp sử dụng mà khoảng cách và dữ liệu thực tế hiện tại là rất quan trọng, chẳng hạn như tìm "quán cà phê ngon nhất gần tôi" hoặc nhận chỉ đường.

## Trường hợp sử dụng

Tính năng Kết nối với Google Maps hỗ trợ nhiều trường hợp sử dụng nhận biết vị trí.

### Xử lý các câu hỏi cụ thể về địa điểm

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên bài đánh giá của người dùng Google và các dữ liệu khác trên Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools=[{
        "type": "google_maps",
        "latitude": 34.050481,
        "longitude": -118.248526
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Is there a cafe near the corner of 1st and Main that has outdoor seating?",
    tools: [{
      type: "google_maps",
      latitude: 34.050481,
      longitude: -118.248526
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Cung cấp tính năng cá nhân hoá dựa trên vị trí

Nhận các đề xuất phù hợp với lựa chọn ưu tiên của người dùng và một khu vực địa lý cụ thể.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Which family-friendly restaurants near here have the best playground reviews?",
    tools=[{
        "type": "google_maps",
        "latitude": 30.2672,
        "longitude": -97.7431
    }]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
                if content_block.annotations:
                    print("\nSources:")
                    for annotation in content_block.annotations:
                        if annotation.type == "place_citation":
                            print(f"  - {annotation.name}: {annotation.url}")
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Which family-friendly restaurants near here have the best playground reviews?",
    tools: [{
      type: "google_maps",
      latitude: 30.2672,
      longitude: -97.7431
    }]
  });

  for (const step of interaction.steps) {
    if (step.type === 'model_output') {
      for (const contentBlock of step.content) {
        if (contentBlock.type === 'text') {
          console.log(contentBlock.text);
          if (contentBlock.annotations) {
            console.log("\nSources:");
            for (const annotation of contentBlock.annotations) {
              if (annotation.type === 'place_citation') {
                console.log(`  - ${annotation.name}: ${annotation.url}`);
              }
            }
          }
        }
      }
    }
  }
}

main();
```

### Hỗ trợ lập kế hoạch cho hành trình

Tạo kế hoạch nhiều ngày kèm theo chỉ đường và thông tin về nhiều địa điểm, phù hợp với các ứng dụng du lịch.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    tools=[{
        "type": "google_maps",
        "latitude": 37.78193,
        "longitude": -122.40476
    }]
)
# ... code to process response
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.5-flash",
    input: "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    tools: [{
      type: "google_maps",
      latitude: 37.78193,
      longitude: -122.40476
    }]
  });
}

main();
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Api-Revision: 2026-05-20" \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ cho tính năng Kết nối với Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn trên Google Maps

Với mỗi kết quả dựa trên dữ liệu của Google Maps, bạn sẽ nhận được chú thích nguồn trên các khối nội dung của bước `model_output` hỗ trợ từng câu trả lời. Siêu dữ liệu sau đây sẽ được trả về:

- URL nguồn
- tên

Khi trình bày kết quả từ tính năng Kết nối với Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng của bạn về những điều sau:

- Các nguồn trên Google Maps phải xuất hiện ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả dựa trên dữ liệu của Google Maps.
- Người dùng phải xem được các nguồn trên Google Maps trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps kèm theo đường liên kết đến Google Maps

Đối với mỗi chú thích nguồn, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo nguyên tắc ghi công văn bản của Google Maps
  .
- Hiển thị tên nguồn được cung cấp trong câu trả lời.
- Liên kết đến nguồn bằng `url` trong chú thích.

### Nguyên tắc ghi công văn bản của Google Maps

Khi bạn ghi công các nguồn cho Google Maps bằng văn bản, hãy tuân theo các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps theo bất kỳ cách nào:
  - Không thay đổi cách viết hoa của Google Maps.
  - Không chuyển Google Maps sang nhiều dòng.
  - Không bản địa hoá Google Maps sang ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và các
điều khoản cấp phép của họ, hãy xem [thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để có câu trả lời phù hợp và được cá nhân hoá nhất, hãy luôn thêm `latitude` và `longitude` vào cấu hình công cụ `google_maps` khi bạn biết vị trí của người dùng.
- **Thông báo cho người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu của Google Maps đang được sử dụng để trả lời các truy vấn của họ, đặc biệt là khi công cụ này được bật.
- **Tắt khi không cần:** Tính năng Kết nối với Google Maps sẽ tắt theo mặc định. Chỉ bật tính năng này (`"tools": [{"type": "google_maps"}]`) khi một truy vấn có a
  ngữ cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- Tính năng Kết nối với Google Maps hiện chỉ hỗ trợ lời nhắc và câu trả lời bằng tiếng Anh.
- Công cụ này có thể không dùng được ở một số khu vực.
- Kết quả có thể khác nhau dựa trên độ chính xác của vị trí và dữ liệu Maps hiện có.
- **Phạm vi địa lý:** Tính năng Kết nối với Google Maps có trên toàn cầu.
- **Trạng thái mặc định:** Công cụ Kết nối với Google Maps sẽ tắt theo mặc định.
  Bạn phải bật công cụ này một cách rõ ràng trong các yêu cầu API.

## Giá và hạn mức về giá

Giá của tính năng Kết nối với Google Maps dựa trên các truy vấn. Mức giá hiện tại là **25 USD / 1.000 lời nhắc bám sát nguồn**. Cấp miễn phí cũng có tối đa 500 yêu cầu mỗi ngày. Một yêu cầu chỉ được tính vào hạn mức khi một lời nhắc trả về thành công ít nhất một kết quả dựa trên dữ liệu của Google Maps (tức là kết quả chứa ít nhất một nguồn trên Google Maps). Nếu nhiều truy vấn được gửi đến Google Maps từ một yêu cầu, thì yêu cầu đó sẽ được tính là một yêu cầu theo hạn mức về giá.

Để biết thông tin chi tiết về giá, hãy xem [trang giá của Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Kết nối với Google Maps:

| Mô hình | Kết nối với Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Các cách kết hợp công cụ được hỗ trợ

Các mô hình Gemini 3 hỗ trợ kết hợp các công cụ tích hợp (như Kết nối với Google Maps) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang về các cách kết hợp công cụ
.

## Bước tiếp theo

- Tìm hiểu về các [công cụ khác hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi).
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [hướng dẫn về chế độ cài đặt An toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-01 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-01 UTC."],[],[]]
