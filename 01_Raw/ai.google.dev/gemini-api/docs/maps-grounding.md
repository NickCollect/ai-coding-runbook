---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi
fetched_at: 2026-09-21T05:45:41.085773+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng Bám sát nguồn bằng Google Maps kết nối các khả năng tạo sinh của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng tích hợp chức năng nhận biết vị trí vào các ứng dụng của họ. Khi một cụm từ tìm kiếm của người dùng có bối cảnh liên quan đến dữ liệu trên Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời chính xác về mặt thực tế và mới nhất, đồng thời liên quan đến vị trí cụ thể hoặc khu vực khái quát mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết vị trí:** Tận dụng dữ liệu phong phú và mới nhất của Google Maps cho các cụm từ tìm kiếm theo địa lý cụ thể.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Neo bám vào Google Maps vào ứng dụng của bạn để cung cấp câu trả lời có độ chính xác cao, nhận biết vị trí cho các truy vấn của người dùng. Câu lệnh yêu cầu đề xuất địa điểm ở địa phương kèm theo vị trí người dùng (không bắt buộc), cho phép mô hình Gemini sử dụng dữ liệu của Google Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "What are the best Italian restaurants within a 15-minute walk from here?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the model's text response and annotations
if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What are the best Italian restaurants within a 15-minute walk from here?",
    "tools": [{
      "type": "google_maps",
      "latitude": 34.050481,
      "longitude": -118.248526
    }]
  }'
```

## Cách hoạt động của tính năng Neo bám vào Google Maps

Tính năng neo bám vào Google Maps tích hợp Gemini API với hệ sinh thái Google Geo bằng cách sử dụng Maps API làm nguồn neo bám. Khi cụm từ tìm kiếm của người dùng có ngữ cảnh địa lý, mô hình Gemini có thể gọi công cụ Nền tảng với Google Maps. Sau đó, mô hình có thể tạo ra câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quy trình này thường bao gồm:

1. **Cụm từ tìm kiếm của người dùng:** Người dùng gửi một cụm từ tìm kiếm đến ứng dụng của bạn, có thể bao gồm cả bối cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini, khi nhận ra ý định về địa lý, sẽ gọi công cụ Grounding with Google Maps. Bạn có thể cung cấp cho công cụ này `latitude` và `longitude` của người dùng (không bắt buộc). Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như khi bạn tìm kiếm trên Maps, trong đó các cụm từ tìm kiếm tại địa phương ("gần tôi") sẽ sử dụng toạ độ, trong khi các cụm từ tìm kiếm cụ thể hoặc không phải tại địa phương sẽ khó bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Grounding with Google Maps truy vấn Google Maps để tìm thông tin liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo câu trả lời dựa trên dữ liệu:** Dữ liệu được truy xuất từ Maps được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ phù hợp của thông tin.
5. **Phản hồi và chú thích:** Mô hình này trả về một phản hồi bằng văn bản kèm theo chú thích nội tuyến liên kết đến các nguồn trên Google Maps, cho phép nhà phát triển hiển thị nội dung trích dẫn.

## Lý do và thời điểm nên sử dụng tính năng Neo bám vào Google Maps

Neo bám vào Google Maps là lựa chọn lý tưởng cho những ứng dụng cần thông tin chính xác, mới nhất và theo vị trí cụ thể. Nhờ cơ sở dữ liệu phong phú của Google Maps với hơn 250 triệu địa điểm trên toàn thế giới, tính năng này mang đến nội dung phù hợp và được cá nhân hoá, giúp nâng cao trải nghiệm người dùng.

Bạn nên sử dụng tính năng Neo bám vào Google Maps khi ứng dụng của bạn cần:

- Đưa ra câu trả lời đầy đủ và chính xác cho các câu hỏi theo vị trí địa lý.
- Xây dựng công cụ lập kế hoạch chuyến đi và hướng dẫn viên địa phương dựa trên cuộc trò chuyện.
- Đề xuất các địa điểm yêu thích dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ xã hội, bán lẻ hoặc giao đồ ăn.

Neo bám vào Google Maps vượt trội trong các trường hợp sử dụng mà dữ liệu thực tế hiện tại và khoảng cách là yếu tố quan trọng, chẳng hạn như tìm "quán cà phê ngon nhất gần tôi" hoặc nhận chỉ đường.

## Trường hợp sử dụng

Tính năng liên kết với Google Maps hỗ trợ nhiều trường hợp sử dụng có nhận biết vị trí.

### Xử lý các câu hỏi về địa điểm cụ thể

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên các bài đánh giá của người dùng trên Google và dữ liệu khác trên Maps.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Is there a cafe near the corner of 1st and Main that has outdoor seating?"))
        .tools(
            Arrays.asList(
                GoogleMaps.builder().latitude(34.050481).longitude(-118.248526).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### Cung cấp tính năng cá nhân hoá dựa trên vị trí

Nhận đề xuất phù hợp với lựa chọn ưu tiên của người dùng và một khu vực địa lý cụ thể.

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Annotation;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.PlaceCitation;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Which family-friendly restaurants near here have the best playground reviews?"))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(30.2672).longitude(-97.7431).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.steps().isPresent()) {
  for (Step step : interaction.steps().get()) {
    if (step instanceof ModelOutputStep) {
      ModelOutputStep outputStep = (ModelOutputStep) step;
      if (outputStep.content().isPresent()) {
        for (Content contentBlock : outputStep.content().get()) {
          if (contentBlock instanceof TextContent) {
            TextContent textContent = (TextContent) contentBlock;
            System.out.println(textContent.text().orElse(""));
            if (textContent.annotations().isPresent()
                && !textContent.annotations().get().isEmpty()) {
              System.out.println("\nSources:");
              for (Annotation annotation : textContent.annotations().get()) {
                if (annotation instanceof PlaceCitation) {
                  PlaceCitation citation = (PlaceCitation) annotation;
                  System.out.printf(
                      "  - %s: %s%n", citation.name().orElse(""), citation.url().orElse(""));
                }
              }
            }
          }
        }
      }
    }
  }
}
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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GoogleMaps;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;

Client client = new Client();

String prompt =
    "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .tools(
            Arrays.asList(GoogleMaps.builder().latitude(37.78193).longitude(-122.40476).build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// ... code to process response
System.out.println(interaction.outputText().orElse(""));
```

### REST

```
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.",
    "tools": [{
      "type": "google_maps",
      "latitude": 37.78193,
      "longitude": -122.40476
    }]
  }'
```

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ để sử dụng tính năng Grounding with Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn của Google Maps

Với mỗi kết quả dựa trên dữ liệu thực tế trên Google Maps, bạn sẽ nhận được chú thích nguồn trên các khối nội dung của bước `model_output` hỗ trợ từng câu trả lời. Hệ thống sẽ trả về siêu dữ liệu sau:

- URL nguồn
- tên

Khi trình bày kết quả từ tính năng Grounding with Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng về những điều sau:

- Các nguồn trên Google Maps phải nằm ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả dựa trên vị trí thực tế trên Google Maps.
- Người dùng phải xem được các nguồn dữ liệu của Google Maps trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps bằng đường liên kết đến Google Maps

Đối với mỗi chú thích nguồn, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo [nguyên tắc ghi công](#maps-attribution-guidelines) văn bản của Google Maps.
- Hiển thị tên nguồn có trong phản hồi.
- Liên kết đến nguồn bằng cách sử dụng `url` từ chú giải.

### Nguyên tắc ghi công bằng văn bản của Google Maps

Khi ghi nguồn cho Google Maps bằng văn bản, hãy tuân thủ các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps theo bất kỳ cách nào:
  - Không thay đổi kiểu viết hoa của Google Maps.
  - Đừng xuống dòng Google Maps.
  - Đừng bản địa hoá Google Maps sang một ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và điều khoản cấp phép của họ, hãy xem [Thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để nhận được câu trả lời phù hợp và được cá nhân hoá nhất, hãy luôn thêm `latitude` và `longitude` vào cấu hình công cụ `google_maps` khi bạn biết vị trí của người dùng.
- **Thông báo cho Người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu trên Google Maps đang được dùng để trả lời các câu hỏi của họ, đặc biệt là khi công cụ này được bật.
- **Tắt khi không cần thiết:** Theo mặc định, tính năng tiếp đất bằng Google Maps sẽ ở trạng thái tắt. Chỉ bật (`"tools": [{"type": "google_maps"}]`) khi truy vấn có ngữ cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- Tính năng căn cứ vào Google Maps hiện chỉ hỗ trợ câu lệnh và câu trả lời bằng tiếng Anh.
- Công cụ này có thể không dùng được ở một số khu vực.
- Kết quả có thể khác nhau tuỳ thuộc vào độ chính xác của vị trí và dữ liệu có sẵn trên Maps.
- **Phạm vi địa lý:** Tính năng neo bám vào Google Maps được cung cấp trên toàn cầu.
- **Trạng thái mặc định:** Công cụ Neo bám vào Google Maps sẽ tắt theo mặc định.
  Bạn phải bật tính năng này một cách rõ ràng trong các yêu cầu API.

## Mức giá và hạn mức

Mức giá của tính năng neo bám vào Google Maps sẽ khác nhau tuỳ thuộc vào thế hệ mô hình:

- **Mô hình Gemini 3:** Dự án của bạn sẽ bị tính phí cho mỗi **cụm từ tìm kiếm** mà mô hình quyết định thực hiện. Một **câu lệnh tìm kiếm** (yêu cầu API của bạn đối với mô hình) có thể khiến mô hình thực hiện nhiều truy vấn tìm kiếm để tìm thông tin cần thiết. Mỗi truy vấn này được tính là một lần sử dụng có tính phí của công cụ.
- **Gemini 2.5 và các mô hình cũ:** Dự án của bạn sẽ được tính phí theo **câu lệnh tìm kiếm**.
  Bạn chỉ bị tính phí cho yêu cầu nếu câu lệnh trả về thành công ít nhất một kết quả có căn cứ trên Google Maps, bất kể mô hình đã thực hiện bao nhiêu truy vấn tìm kiếm riêng lẻ ở nội bộ để nhận được kết quả đó.

Để biết thông tin chi tiết về giá, hãy xem [trang định giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Neo bám vào Google Maps:

| Mô hình | Neo bám vào Google Maps |
| --- | --- |
| [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=vi) | ✔️ |
| [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=vi) | ✔️ |
| [Gemini 3.6 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash?hl=vi) | ✔️ |
| [Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?hl=vi) | ✔️ |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |

## Các tổ hợp công cụ được hỗ trợ

Bạn có thể sử dụng tính năng Nền tảng kiến thức dựa trên Google Maps cùng với các công cụ tích hợp khác như [Nền tảng kiến thức dựa trên Google Tìm kiếm](https://ai.google.dev/gemini-api/docs/google-search?hl=vi) (được hỗ trợ trên Gemini 3.5 Flash và các mô hình sau này) để hỗ trợ các trường hợp sử dụng phức tạp hơn. Các mô hình Gemini 3 cũng hỗ trợ kết hợp những công cụ tích hợp này với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Bước tiếp theo

- Tìm hiểu về [các công cụ khác hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi).
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [hướng dẫn về Chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-18 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-18 UTC."],[],[]]
