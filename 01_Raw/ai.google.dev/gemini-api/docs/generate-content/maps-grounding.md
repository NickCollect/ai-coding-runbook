---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/maps-grounding?hl=vi
fetched_at: 2026-09-14T05:45:45.856531+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng Bám sát nguồn bằng Google Maps kết nối các khả năng tạo sinh của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng tích hợp chức năng nhận biết vị trí vào các ứng dụng của họ. Khi một cụm từ tìm kiếm của người dùng có bối cảnh liên quan đến dữ liệu trên Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời chính xác về mặt thực tế và mới nhất, đồng thời liên quan đến vị trí cụ thể hoặc khu vực khái quát mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết vị trí:** Tận dụng dữ liệu phong phú và mới nhất của Google Maps cho các cụm từ tìm kiếm theo địa lý cụ thể.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Nền tảng với Google Maps vào ứng dụng của bạn để cung cấp câu trả lời chính xác, nhận biết vị trí cho các truy vấn của người dùng. Câu lệnh yêu cầu đề xuất địa điểm ở địa phương kèm theo vị trí người dùng (không bắt buộc), cho phép mô hình Gemini sử dụng dữ liệu của Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on grounding with Google Maps
        tools=[types.Tool(google_maps=types.GoogleMaps())],
        # Optionally provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function generateContentWithMapsGrounding() {
  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: "What are the best Italian restaurants within a 15-minute walk from here?",
    config: {
      // Turn on grounding with Google Maps
      tools: [{ googleMaps: {} }],
      toolConfig: {
        retrievalConfig: {
          // Optionally provide the relevant location context (this is in Los Angeles)
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526,
          },
        },
      },
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const grounding = response.candidates[0]?.groundingMetadata;
  if (grounding?.groundingChunks) {
    console.log("-".repeat(40));
    console.log("Sources:");
    for (const chunk of grounding.groundingChunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

generateContentWithMapsGrounding();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What are the best Italian restaurants within a 15-minute walk from here?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

## Cách hoạt động của tính năng Neo bám vào Google Maps

Tính năng neo bám vào Google Maps tích hợp Gemini API với hệ sinh thái Google Geo bằng cách sử dụng Maps API làm nguồn neo bám. Khi cụm từ tìm kiếm của người dùng có ngữ cảnh địa lý, mô hình Gemini có thể gọi công cụ Nền tảng với Google Maps. Sau đó, mô hình có thể tạo ra câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quy trình này thường bao gồm:

1. **Cụm từ tìm kiếm của người dùng:** Người dùng gửi một cụm từ tìm kiếm đến ứng dụng của bạn, có thể bao gồm cả bối cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini, khi nhận ra ý định về địa lý, sẽ gọi công cụ Grounding with Google Maps. Bạn có thể cung cấp cho công cụ này `latitude` và `longitude` của người dùng (không bắt buộc). Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như khi bạn tìm kiếm trên Maps, tức là các cụm từ tìm kiếm địa phương ("gần tôi") sẽ sử dụng toạ độ, trong khi các cụm từ tìm kiếm cụ thể hoặc không phải địa phương sẽ khó bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Grounding with Google Maps truy vấn Google Maps để tìm thông tin liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo câu trả lời dựa trên dữ liệu:** Dữ liệu được truy xuất từ Maps được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ phù hợp của thông tin.
5. **Phản hồi:** Mô hình trả về một câu trả lời bằng văn bản, trong đó có nội dung trích dẫn đến các nguồn trên Google Maps.

## Lý do và thời điểm nên sử dụng tính năng Neo bám vào Google Maps

Neo bám vào Google Maps là lựa chọn lý tưởng cho những ứng dụng cần thông tin chính xác, mới nhất và theo vị trí cụ thể. Nhờ cơ sở dữ liệu phong phú của Google Maps với hơn 250 triệu địa điểm trên toàn thế giới, tính năng này mang đến nội dung phù hợp và được cá nhân hoá, giúp nâng cao trải nghiệm người dùng.

Bạn nên sử dụng tính năng Grounding with Google Maps khi ứng dụng của bạn cần:

- Đưa ra câu trả lời đầy đủ và chính xác cho các câu hỏi theo vị trí địa lý.
- Xây dựng công cụ lập kế hoạch chuyến đi và hướng dẫn viên địa phương dựa trên cuộc trò chuyện.
- Đề xuất các địa điểm yêu thích dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ xã hội, bán lẻ hoặc giao đồ ăn.

Neo bám vào Google Maps vượt trội trong các trường hợp sử dụng mà dữ liệu thực tế hiện tại và khoảng cách là yếu tố quan trọng, chẳng hạn như tìm "quán cà phê ngon nhất gần tôi" hoặc nhận chỉ đường.

## Phương thức và tham số API

Tính năng Neo bám vào Google Maps được cung cấp thông qua Gemini API dưới dạng một công cụ trong phương thức [`generateContent`](https://ai.google.dev/api/generate-content?hl=vi). Bạn bật và định cấu hình tính năng Neo bám vào Google Maps bằng cách thêm một đối tượng [`googleMaps`](https://ai.google.dev/api/caching?hl=vi#GoogleMaps) vào tham số `tools` trong yêu cầu của bạn.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": {} }
}
```

Ngoài ra, công cụ này hỗ trợ truyền vị trí theo bối cảnh dưới dạng `toolConfig`.

### JSON

```
{
  "contents": [{
    "parts": [
      {"text": "Restaurants near here."}
    ]
  }],
  "tools":  { "googleMaps": {} },
  "toolConfig":  {
    "retrievalConfig": {
      "latLng": {
        "latitude": 40.758896,
        "longitude": -73.985130
      }
    }
  }
}
```

### Tìm hiểu về câu trả lời dựa trên thông tin thực tế

Khi một câu trả lời được căn cứ thành công vào dữ liệu của Google Maps, câu trả lời đó sẽ bao gồm trường [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata).
Dữ liệu có cấu trúc này rất cần thiết để xác minh các câu trích dẫn và tạo trải nghiệm trích dẫn phong phú trong ứng dụng của bạn, cũng như đáp ứng các yêu cầu về việc sử dụng dịch vụ.

### JSON

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "CanteenM is an American restaurant with..."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "groundingChunks": [
          {
            "maps": {
              "uri": "https://maps.google.com/?cid=13100894621228039586",
              "title": "Heaven on 7th Marketplace",
              "placeId": "places/ChIJ0-zA1vBZwokRon0fGj-6z7U"
            },
            // repeated ...
          }
        ],
        "groundingSupports": [
          {
            "segment": {
              "startIndex": 0,
              "endIndex": 79,
              "text": "CanteenM is an American restaurant with a 4.6-star rating and is open 24 hours."
            },
            "groundingChunkIndices": [0]
          },
          // repeated ...
        ],
        "webSearchQueries": [
          "restaurants near me"
        ]
      }
    }
  ]
}
```

Gemini API trả về thông tin sau bằng [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata):

- `groundingChunks`: Mảng đối tượng chứa các nguồn `maps` (`uri`, `placeId` và `title`).
- `groundingSupports`: Mảng các đoạn văn bản để kết nối văn bản phản hồi của mô hình với các nguồn trong `groundingChunks`. Mỗi đoạn liên kết một khoảng văn bản (do `startIndex` và `endIndex` xác định) với một hoặc nhiều `groundingChunkIndices`. Đây là chìa khoá để tạo trích dẫn trong dòng.

Để xem đoạn mã cho biết cách hiển thị trích dẫn nội dòng trong văn bản, hãy xem [ví dụ](https://ai.google.dev/gemini-api/docs/google-search?hl=vi#attributing_sources_with_inline_citations) trong tài liệu Neo bám vào Google Tìm kiếm.

## Trường hợp sử dụng

Tính năng liên kết với Google Maps hỗ trợ nhiều trường hợp sử dụng có nhận biết vị trí. Các ví dụ sau đây minh hoạ cách các câu lệnh và tham số khác nhau có thể tận dụng tính năng Nền tảng với Google Maps. Thông tin trong Kết quả thực tế trên Google Maps có thể khác với điều kiện thực tế.

### Xử lý các câu hỏi về địa điểm cụ thể

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên các bài đánh giá của người dùng trên Google và dữ liệu khác trên Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        # Turn on the Maps tool
        tools=[types.Tool(google_maps=types.GoogleMaps())],

        # Provide the relevant location context (this is in Los Angeles)
        tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
            lat_lng=types.LatLng(
                latitude=34.050481, longitude=-118.248526))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
  ```
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      // Turn on the Maps tool
      tools: [{googleMaps: {}}],
      // Provide the relevant location context (this is in Los Angeles)
      toolConfig: {
        retrievalConfig: {
          latLng: {
            latitude: 34.050481,
            longitude: -118.248526
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Is there a cafe near the corner of 1st and Main that has outdoor seating?"
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 34.050481, "longitude": -118.248526}
    }
  }
}'
```

### Cung cấp tính năng cá nhân hoá dựa trên vị trí

Nhận đề xuất phù hợp với lựa chọn ưu tiên của người dùng và một khu vực địa lý cụ thể.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context; this is Austin, TX.
          lat_lng=types.LatLng(
              latitude=30.2672, longitude=-97.7431))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if chunks := grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Which family-friendly restaurants near here have the best playground reviews?";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context; this is Austin, TX.
          latLng: {
            latitude: 30.2672,
            longitude: -97.7431
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const chunks = response.candidates[0].groundingMetadata?.groundingChunks;
  if (chunks) {
    console.log('-'.repeat(40));
    console.log("Sources:");
    for (const chunk of chunks) {
      if (chunk.maps) {
        console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Which family-friendly restaurants near here have the best playground reviews?"
    }],
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
      "latLng": {"latitude": 30.2672, "longitude": -97.7431}
    }
  }
}'
```

### Hỗ trợ lập kế hoạch cho hành trình

Tạo kế hoạch nhiều ngày kèm theo chỉ đường và thông tin về nhiều địa điểm, phù hợp với các ứng dụng du lịch.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps())],
      tool_config=types.ToolConfig(retrieval_config=types.RetrievalConfig(
          # Provide the location as context, this is in San Francisco.
          lat_lng=types.LatLng(
              latitude=37.78193, longitude=-122.40476))),
    ),
)

print("Generated Response:")
print(response.text)

if grounding := response.candidates[0].grounding_metadata:
  if grounding.grounding_chunks:
    print('-' * 40)
    print("Sources:")
    for chunk in grounding.grounding_chunks:
      print(f'- [{chunk.maps.title}]({chunk.maps.uri})')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.6-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {}}],
      toolConfig: {
        retrievalConfig: {
          // Provide the location as context, this is in San Francisco.
          latLng: {
            latitude: 37.78193,
            longitude: -122.40476
          }
        }
      }
    },
  });

  console.log("Generated Response:");
  console.log(response.text);

  const groundingMetadata = response.candidates[0]?.groundingMetadata;
  if (groundingMetadata) {
    if (groundingMetadata.groundingChunks) {
      console.log('-'.repeat(40));
      console.log("Sources:");
      for (const chunk of groundingMetadata.groundingChunks) {
        if (chunk.maps) {
          console.log(`- [${chunk.maps.title}](${chunk.maps.uri})`);
        }
      }
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ để sử dụng tính năng Grounding with Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn của Google Maps

Với mỗi kết quả dựa trên dữ liệu thực tế trên Google Maps, bạn sẽ nhận được các nguồn trong `groundingChunks` hỗ trợ cho từng câu trả lời. Siêu dữ liệu sau đây cũng được trả về:

- uri nguồn
- tiêu đề
- ID

Khi trình bày kết quả từ tính năng Grounding with Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng về những điều sau:

- Các nguồn trên Google Maps phải nằm ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả dựa trên vị trí thực tế trên Google Maps.
- Người dùng phải xem được các nguồn dữ liệu của Google Maps trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps bằng đường liên kết đến Google Maps

Đối với mỗi nguồn trong `groundingChunks` và trong `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo [nguyên tắc ghi công](#maps-attribution-guidelines) văn bản của Google Maps.
- Hiển thị tiêu đề nguồn có trong câu trả lời.
- Liên kết đến nguồn bằng cách sử dụng biểu tượng `uri` hoặc `googleMapsUri` trong câu trả lời.

Những hình ảnh này cho thấy các yêu cầu tối thiểu để hiển thị nguồn và đường liên kết đến Google Maps.

![Câu lệnh có câu trả lời cho thấy các nguồn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=vi)

Bạn có thể thu gọn chế độ xem nguồn.

![Câu lệnh có phản hồi và nguồn được thu gọn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=vi)

Không bắt buộc: Cải thiện bản xem trước đường liên kết bằng nội dung bổ sung, chẳng hạn như:

- Một [biểu tượng trang web của Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=vi) được chèn trước thông tin ghi công của Google Maps.
- Ảnh từ URL nguồn (`og:image`).

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và điều khoản cấp phép của họ, hãy xem [Thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

### Nguyên tắc ghi công bằng văn bản của Google Maps

Khi ghi nguồn cho Google Maps bằng văn bản, hãy tuân thủ các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps theo bất kỳ cách nào:
  - Không thay đổi kiểu viết hoa của Google Maps.
  - Đừng xuống dòng Google Maps.
  - Đừng bản địa hoá Google Maps sang một ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".
- Tạo kiểu cho văn bản trên Google Maps như mô tả trong bảng sau:

| Thuộc tính | Kiểu |
| --- | --- |
| `Font family` | Roboto. Bạn không bắt buộc phải tải phông chữ. |
| `Fallback font family` | Mọi phông chữ không chân đã được dùng trong sản phẩm của bạn hoặc "Sans-Serif" để gọi phông chữ hệ thống mặc định |
| `Font style` | Bình thường |
| `Font weight` | 400 |
| `Font color` | Trắng, đen (#1F1F1F) hoặc xám (#5E5E5E). Duy trì độ tương phản dễ tiếp cận (4,5:1) so với nền. |
| `Font size` | - Cỡ chữ tối thiểu: 12sp - Cỡ chữ tối đa: 16sp - Để tìm hiểu về sp, hãy xem phần Đơn vị kích thước phông chữ trên [trang web Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
| `Spacing` | Bình thường |

#### Ví dụ về CSS

CSS sau đây kết xuất Google Maps với kiểu chữ và màu sắc phù hợp trên nền trắng hoặc nền sáng.

### CSS

```
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

.GMP-attribution {

font-family: Roboto, Sans-Serif;
font-style: normal;
font-weight: 400;
font-size: 1rem;
letter-spacing: normal;
white-space: nowrap;
color: #5e5e5e;
}
```

### Mã địa điểm và mã bài đánh giá

Dữ liệu của Google Maps bao gồm mã địa điểm và mã bài đánh giá. Bạn có thể lưu vào bộ nhớ đệm, lưu trữ và xuất dữ liệu phản hồi sau:

- `placeId`
- `reviewId`

Các quy định hạn chế đối với việc lưu vào bộ nhớ đệm trong Điều khoản về việc neo bám vào Google Maps sẽ không áp dụng.

### Hoạt động và lãnh thổ bị cấm

Tính năng tiếp đất bằng Google Maps có thêm các quy định hạn chế đối với một số nội dung và hoạt động nhất định để duy trì một nền tảng an toàn và đáng tin cậy. Ngoài các quy định hạn chế về việc sử dụng trong [Điều khoản](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-maps):

- Bạn sẽ không sử dụng tính năng Grounding với Google Maps cho các hoạt động có rủi ro cao, bao gồm cả dịch vụ ứng phó khẩn cấp.
- Bạn sẽ không phân phối hoặc tiếp thị ứng dụng cung cấp tính năng Định hướng bằng Google Maps ở một Lãnh thổ bị cấm. Để biết thêm thông tin, hãy xem [Các lãnh thổ bị cấm của Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=vi).
  Danh sách Các lãnh thổ bị cấm có thể được cập nhật theo thời gian.

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để nhận được những câu trả lời phù hợp và mang tính cá nhân hoá nhất, hãy luôn thêm `user_location` (vĩ độ và kinh độ) vào cấu hình `googleMapsGrounding` khi bạn biết vị trí của người dùng.
- **Thông báo cho Người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu trên Google Maps đang được dùng để trả lời các câu hỏi của họ, đặc biệt là khi công cụ này được bật.
- **Theo dõi độ trễ:** Đối với các ứng dụng đàm thoại, hãy đảm bảo rằng độ trễ P95 cho các câu trả lời có căn cứ vẫn nằm trong ngưỡng chấp nhận được để duy trì trải nghiệm mượt mà cho người dùng.
- **Tắt khi không cần thiết:** Theo mặc định, tính năng tiếp đất bằng Google Maps sẽ ở trạng thái tắt. Chỉ bật (`"tools": [{"googleMaps": {}}]`) khi truy vấn có ngữ cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- **Phạm vi địa lý:** Tính năng neo bám vào Google Maps được cung cấp trên toàn cầu
- **Hỗ trợ mô hình:** Xem phần [Các mô hình được hỗ trợ](#supported-models).
- **Đầu vào/Đầu ra đa phương thức:** Tính năng liên kết với Google Maps hiện không hỗ trợ đầu vào hoặc đầu ra đa phương thức ngoài văn bản.
- **Trạng thái mặc định:** Công cụ Neo bám vào Google Maps sẽ tắt theo mặc định.
  Bạn phải bật tính năng này một cách rõ ràng trong các yêu cầu API.

## Mức giá và hạn mức

Giá của tính năng neo bám vào Google Maps được tính dựa trên số lượng câu hỏi. Mức giá hiện tại là **25 USD / 1.000 câu lệnh có căn cứ**. Cấp miễn phí cũng có tối đa 500 yêu cầu mỗi ngày. Yêu cầu chỉ được tính vào hạn mức khi một câu lệnh trả về thành công ít nhất một kết quả có căn cứ của Google Maps (tức là kết quả chứa ít nhất một nguồn của Google Maps). Nếu nhiều truy vấn được gửi đến Google Maps từ một yêu cầu duy nhất, thì yêu cầu đó sẽ được tính là một yêu cầu trong giới hạn về tốc độ.

Để biết thông tin chi tiết về giá, hãy xem [trang định giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Neo bám vào Google Maps:

| Mô hình | Neo bám vào Google Maps |
| --- | --- |
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

Các mô hình Gemini 3 hỗ trợ kết hợp các công cụ tích hợp sẵn (như Bám sát nguồn bằng Google Maps) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Bước tiếp theo

- Hãy thử [Hướng dẫn về việc tiếp cận thông tin thực tế bằng Google Tìm kiếm trong sổ tay về Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=vi).
- Tìm hiểu về [các công cụ khác hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi).
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [hướng dẫn về Chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-12 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-12 UTC."],[],[]]
