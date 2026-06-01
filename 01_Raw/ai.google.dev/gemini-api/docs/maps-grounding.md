---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi
fetched_at: 2026-06-01T05:57:34.589275+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng căn cứ vào thông tin trên Google Maps kết nối các khả năng tạo sinh của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng tích hợp chức năng nhận biết vị trí vào các ứng dụng của họ. Khi một cụm từ tìm kiếm của người dùng có bối cảnh liên quan đến dữ liệu trên Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời chính xác về mặt thực tế và mới nhất, đồng thời phù hợp với vị trí cụ thể hoặc khu vực khái quát mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết được vị trí:** Tận dụng dữ liệu phong phú và mới nhất của Google Maps cho các cụm từ tìm kiếm theo địa lý cụ thể.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.
- **Thông tin theo bối cảnh và tiện ích:** Mã thông báo theo bối cảnh để hiển thị các tiện ích tương tác của Google Maps cùng với nội dung được tạo.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Kết nối với Google Maps vào ứng dụng của bạn để cung cấp câu trả lời chính xác, nhận biết vị trí cho các truy vấn của người dùng. Câu lệnh yêu cầu đề xuất địa điểm ở địa phương (có thể có vị trí của người dùng), cho phép mô hình Gemini sử dụng dữ liệu trên Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: "gemini-3.5-flash",
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

## Cách hoạt động của tính năng Kết nối với Google Maps

Tính năng kết nối với Google Maps tích hợp Gemini API với hệ sinh thái Google Geo bằng cách sử dụng Maps API làm nguồn thông tin cơ bản. Khi cụm từ tìm kiếm của người dùng chứa ngữ cảnh địa lý, mô hình Gemini có thể gọi công cụ Grounding with Google Maps. Sau đó, mô hình có thể tạo ra câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quy trình này thường bao gồm:

1. **Câu hỏi của người dùng:** Người dùng gửi một câu hỏi đến ứng dụng của bạn, có thể bao gồm cả bối cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini, khi nhận ra ý định về địa lý, sẽ gọi công cụ Grounding with Google Maps. Bạn có thể cung cấp `latitude` và `longitude` của người dùng cho công cụ này (không bắt buộc). Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như khi bạn tìm kiếm trên Maps, tức là các cụm từ tìm kiếm địa phương ("gần tôi") sẽ sử dụng toạ độ, trong khi các cụm từ tìm kiếm cụ thể hoặc không phải địa phương sẽ ít bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Kết nối với Google Maps truy vấn Google Maps để tìm thông tin liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo thông tin bám sát nguồn:** Dữ liệu được truy xuất từ Maps được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ phù hợp của thông tin.
5. **Phản hồi và mã thông báo tiện ích:** Mô hình này trả về một phản hồi bằng văn bản, bao gồm cả các trích dẫn đến các nguồn trên Google Maps. Ngoài ra, phản hồi API cũng có thể chứa một `google_maps_widget_context_token`, cho phép nhà phát triển hiển thị một tiện ích Google Maps theo bối cảnh trong ứng dụng của họ để tương tác trực quan.

## Lý do và thời điểm nên sử dụng tính năng Kết nối với Google Maps

Kết nối với Google Maps rất phù hợp cho những ứng dụng yêu cầu thông tin chính xác, mới nhất và theo vị trí cụ thể. Nhờ cơ sở dữ liệu rộng lớn của Google Maps với hơn 250 triệu địa điểm trên toàn thế giới, tính năng này mang đến nội dung phù hợp và được cá nhân hoá, giúp nâng cao trải nghiệm người dùng.

Bạn nên sử dụng tính năng Kết nối với Google Maps khi ứng dụng của bạn cần:

- Đưa ra câu trả lời đầy đủ và chính xác cho các câu hỏi theo vị trí địa lý.
- Xây dựng công cụ lập kế hoạch chuyến đi và hướng dẫn viên địa phương đàm thoại.
- Đề xuất các địa điểm yêu thích dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ xã hội, bán lẻ hoặc giao đồ ăn.

Kết nối với Google Maps rất phù hợp trong những trường hợp sử dụng cần có dữ liệu thực tế hiện tại và thông tin về tương cận, chẳng hạn như khi tìm "quán cà phê ngon nhất gần tôi" hoặc xem chỉ đường.

## Phương thức và thông số API

Tính năng Kết nối với Google Maps được cung cấp thông qua Gemini API dưới dạng một công cụ trong phương thức [`generateContent`](https://ai.google.dev/api/generate-content?hl=vi). Bạn có thể bật và định cấu hình tính năng Kết nối với Google Maps bằng cách thêm một đối tượng [`googleMaps`](https://ai.google.dev/api/caching?hl=vi#GoogleMaps) vào tham số `tools` trong yêu cầu của bạn.

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

Công cụ [`googleMaps`](https://ai.google.dev/api/caching?hl=vi#GoogleMaps) cũng có thể chấp nhận một tham số boolean `enableWidget`. Tham số này được dùng để kiểm soát xem trường [`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata) có được trả về trong phản hồi hay không. Bạn có thể dùng tham số này để hiển thị [tiện ích Places theo bối cảnh](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=vi).

### JSON

```
{
"contents": [{
    "parts": [
      {"text": "Restaurants near Times Square."}
    ]
  }],
  "tools":  { "googleMaps": { "enableWidget": true } }
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
Dữ liệu có cấu trúc này rất cần thiết để xác minh các tuyên bố và tạo trải nghiệm trích dẫn phong phú trong ứng dụng của bạn, cũng như đáp ứng các yêu cầu về việc sử dụng dịch vụ.

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
        ],
        "googleMapsWidgetContextToken": "widgetcontent/..."
      }
    }
  ]
}
```

Gemini API trả về thông tin sau bằng [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata):

- `groundingChunks`: Mảng đối tượng chứa các nguồn `maps` (`uri`, `placeId` và `title`).
- `groundingSupports`: Mảng các đoạn văn bản để kết nối văn bản phản hồi của mô hình với các nguồn trong `groundingChunks`. Mỗi đoạn liên kết một khoảng văn bản (được xác định bằng `startIndex` và `endIndex`) với một hoặc nhiều `groundingChunkIndices`. Đây là chìa khoá để tạo trích dẫn trong dòng.
- `googleMapsWidgetContextToken`: Một mã thông báo văn bản có thể dùng để hiển thị một [tiện ích Places theo bối cảnh](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=vi).

Để xem đoạn mã minh hoạ cách hiển thị trích dẫn nội dòng trong văn bản, hãy xem [ví dụ](https://ai.google.dev/gemini-api/docs/google-search?hl=vi#attributing_sources_with_inline_citations) trong tài liệu Bám sát nguồn bằng Google Tìm kiếm.

### Hiển thị tiện ích theo bối cảnh của Google Maps

Để sử dụng `googleMapsWidgetContextToken` được trả về, bạn cần [tải API JavaScript của Google Maps](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=vi).

## Trường hợp sử dụng

Tính năng kết nối với Google Maps hỗ trợ nhiều trường hợp sử dụng dựa trên thông tin vị trí. Các ví dụ sau đây minh hoạ cách các câu lệnh và tham số khác nhau có thể tận dụng tính năng Nền tảng với Google Maps. Thông tin trong Kết quả có căn cứ trên Google Maps có thể khác với điều kiện thực tế.

### Xử lý các câu hỏi dành riêng cho địa điểm

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên các bài đánh giá của người dùng trên Google và dữ liệu khác trên Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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
    model='gemini-3.5-flash',
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
    model: 'gemini-3.5-flash',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
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

### Hỗ trợ lập kế hoạch hành trình

Tạo kế hoạch nhiều ngày kèm theo chỉ đường và thông tin về nhiều địa điểm, phù hợp với các ứng dụng du lịch.

Trong ví dụ này, `googleMapsWidgetContextToken` đã được yêu cầu bằng cách bật tiện ích trong công cụ Google Maps. Khi được bật, bạn có thể dùng mã thông báo được trả về để hiển thị một tiện ích Places theo bối cảnh bằng cách sử dụng `<gmp-places-contextual> component` từ API JavaScript của Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
      tools=[types.Tool(google_maps=types.GoogleMaps(enable_widget=True))],
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

  if widget_token := grounding.google_maps_widget_context_token:
    print('-' * 40)
    print(f'<gmp-place-contextual context-token="{widget_token}"></gmp-place-contextual>')
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
  const prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner.";

  const response = await ai.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: prompt,
    config: {
      tools: [{googleMaps: {enableWidget: true}}],
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

    if (groundingMetadata.googleMapsWidgetContextToken) {
      console.log('-'.repeat(40));
      document.body.insertAdjacentHTML('beforeend', `<gmp-place-contextual context-token="${groundingMetadata.googleMapsWidgetContextToken}`"></gmp-place-contextual>`);
    }
  }
}

run();
```

### REST

```
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."
    }]
  }],
  "tools": [{"googleMaps": {"enableWidget":"true"}}],
  "toolConfig": {
    "retrievalConfig": {
    "latLng": {"latitude": 37.78193, "longitude": -122.40476}
  }
  }
}'
```

Khi được kết xuất, tiện ích này sẽ có dạng như sau:

![Ví dụ về một tiện ích bản đồ khi được hiển thị](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=vi)

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ để sử dụng tính năng Grounding with Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn dữ liệu của Google Maps

Với mỗi kết quả dựa trên dữ liệu thực tế trên Google Maps, bạn sẽ nhận được các nguồn `groundingChunks` hỗ trợ cho từng câu trả lời. Siêu dữ liệu sau đây cũng được trả về:

- uri nguồn
- tiêu đề
- ID

Khi trình bày kết quả từ tính năng Kết nối với Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng về những điều sau:

- Các nguồn trên Google Maps phải nằm ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả có căn cứ trên Google Maps.
- Người dùng phải xem được các nguồn của Google Maps trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps bằng đường liên kết đến Google Maps

Đối với mỗi nguồn trong `groundingChunks` và trong `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo [nguyên tắc ghi công](#maps-attribution-guidelines) văn bản của Google Maps.
- Hiển thị tiêu đề nguồn có trong câu trả lời.
- Liên kết đến nguồn bằng cách sử dụng biểu tượng `uri` hoặc `googleMapsUri` trong câu trả lời.

Những hình ảnh này cho thấy các yêu cầu tối thiểu để hiển thị nguồn và đường liên kết đến Google Maps.

![Câu lệnh có câu trả lời cho thấy nguồn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=vi)

Bạn có thể thu gọn chế độ xem nguồn.

![Câu lệnh có câu trả lời và nguồn được thu gọn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=vi)

Không bắt buộc: Nâng cao bản xem trước đường liên kết bằng nội dung bổ sung, chẳng hạn như:

- Một [biểu tượng Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=vi) được chèn trước thông tin ghi nhận quyền tác giả của Google Maps.
- Ảnh từ URL nguồn (`og:image`).

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và điều khoản cấp phép của họ, hãy xem [Thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

### Nguyên tắc ghi công bằng văn bản của Google Maps

Khi ghi nguồn cho Google Maps bằng văn bản, hãy tuân thủ các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps dưới bất kỳ hình thức nào:
  - Đừng thay đổi kiểu viết hoa của Google Maps.
  - Đừng xuống dòng Google Maps.
  - Đừng bản địa hoá Google Maps sang một ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".
- Tạo kiểu cho văn bản trên Google Maps như mô tả trong bảng sau:

| Thuộc tính | Kiểu |
| --- | --- |
| `Font family` | Roboto. Bạn không bắt buộc phải tải phông chữ. |
| `Fallback font family` | Mọi phông chữ không chân được dùng trong sản phẩm của bạn hoặc "Sans-Serif" để gọi phông chữ hệ thống mặc định |
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

### Mã thông báo ngữ cảnh, mã địa điểm và mã bài đánh giá

Dữ liệu trên Google Maps bao gồm mã thông báo bối cảnh, mã địa điểm và mã bài đánh giá. Bạn có thể lưu vào bộ nhớ đệm, lưu trữ và xuất dữ liệu phản hồi sau:

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Các quy định hạn chế về việc lưu vào bộ nhớ đệm trong Điều khoản về việc kết nối với Google Maps sẽ không áp dụng.

### Hoạt động và lãnh thổ bị cấm

Tính năng Kết nối với Google Maps có thêm các quy định hạn chế đối với một số nội dung và hoạt động nhất định để duy trì một nền tảng an toàn và đáng tin cậy. Ngoài các quy định hạn chế về việc sử dụng trong [Điều khoản](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-maps):

- Bạn sẽ không sử dụng tính năng Grounding với Google Maps cho các hoạt động có rủi ro cao, bao gồm cả dịch vụ ứng phó khẩn cấp.
- Bạn sẽ không phân phối hoặc tiếp thị ứng dụng cung cấp tính năng Định hướng bằng Google Maps ở một Lãnh thổ bị cấm. Để biết thêm thông tin, hãy xem [Các lãnh thổ bị cấm của Google Maps Platform](https://cloud.google.com/maps-platform/terms/maps-prohibited-territories?hl=vi).
  Danh sách Các lãnh thổ bị cấm có thể được cập nhật tuỳ từng thời điểm.

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để có được những câu trả lời phù hợp và phù hợp với từng cá nhân nhất, hãy luôn thêm `user_location` (vĩ độ và kinh độ) vào cấu hình `googleMapsGrounding` khi bạn biết vị trí của người dùng.
- **Kết xuất tiện ích theo bối cảnh của Google Maps:** Tiện ích theo bối cảnh được kết xuất bằng mã thông báo bối cảnh, `googleMapsWidgetContextToken`. Mã thông báo này được trả về trong phản hồi của Gemini API và có thể dùng để kết xuất nội dung trực quan từ Google Maps. Để biết thêm thông tin về tiện ích theo ngữ cảnh, hãy xem phần [Kết nối với Google Maps](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=vi) trong Hướng dẫn cho nhà phát triển của Google.
- **Thông báo cho Người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu trên Google Maps đang được dùng để trả lời các câu hỏi của họ, đặc biệt là khi công cụ này được bật.
- **Theo dõi độ trễ:** Đối với các ứng dụng đàm thoại, hãy đảm bảo độ trễ P95 cho các câu trả lời có căn cứ vẫn nằm trong ngưỡng chấp nhận được để duy trì trải nghiệm mượt mà cho người dùng.
- **Tắt khi không cần thiết:** Theo mặc định, tính năng tiếp đất bằng Google Maps sẽ ở trạng thái tắt. Chỉ bật (`"tools": [{"googleMaps": {}}]`) khi truy vấn có ngữ cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- **Phạm vi địa lý:** Tính năng kết nối với Google Maps có trên toàn cầu
- **Hỗ trợ mô hình:** Xem phần [Các mô hình được hỗ trợ](#supported-models).
- **Đầu vào/đầu ra đa phương thức:** Tính năng Kết nối với Google Maps hiện không hỗ trợ đầu vào hoặc đầu ra đa phương thức ngoài văn bản và các tiện ích bản đồ theo bối cảnh.
- **Trạng thái mặc định:** Công cụ Kết nối với Google Maps sẽ tắt theo mặc định.
  Bạn phải bật tính năng này một cách rõ ràng trong các yêu cầu API.

## Mức giá và hạn mức

Giá của tính năng kết nối với Google Maps được tính dựa trên số lượng câu hỏi. Mức giá hiện tại là **25 USD / 1.000 câu lệnh có căn cứ**. Cấp miễn phí cũng có tối đa 500 yêu cầu mỗi ngày. Yêu cầu chỉ được tính vào hạn mức khi một câu lệnh trả về thành công ít nhất một kết quả có nguồn gốc từ Google Maps (tức là kết quả chứa ít nhất một nguồn từ Google Maps). Nếu nhiều truy vấn được gửi đến Google Maps từ một yêu cầu duy nhất, thì yêu cầu đó sẽ được tính là một yêu cầu trong giới hạn về tốc độ.

Để biết thông tin chi tiết về giá, hãy xem [trang định giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Kết nối với Google Maps:

| Mô hình | Kết nối với Google Maps |
| --- | --- |
| [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=vi) | ✔️ |
| [Bản dùng thử Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=vi) | ✔️ |

## Các tổ hợp công cụ được hỗ trợ

Các mô hình Gemini 3 hỗ trợ việc kết hợp các công cụ tích hợp sẵn (chẳng hạn như tính năng Căn cứ thông tin bằng Google Maps) với các công cụ tuỳ chỉnh (lệnh gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Bước tiếp theo

- Hãy thử [Bám sát nguồn bằng Google Tìm kiếm trong sổ tay về Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=vi).
- Tìm hiểu về [các công cụ hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi) khác.
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [hướng dẫn về Chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-28 UTC."],[],[]]
