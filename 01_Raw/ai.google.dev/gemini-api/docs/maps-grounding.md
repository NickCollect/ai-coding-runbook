---
source_url: https://ai.google.dev/gemini-api/docs/maps-grounding?hl=vi
fetched_at: 2026-05-05T20:08:16.699450+00:00
title: "C\u0103n c\u1ee9 v\u00e0o Google Maps \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Căn cứ vào Google Maps

Tính năng Kết nối với Google Maps kết hợp các khả năng tạo nội dung của Gemini với dữ liệu phong phú, thực tế và mới nhất của Google Maps. Tính năng này giúp nhà phát triển dễ dàng kết hợp chức năng nhận biết vị trí vào ứng dụng của họ. Khi một truy vấn của người dùng có bối cảnh liên quan đến dữ liệu của Maps, mô hình Gemini sẽ tận dụng Google Maps để cung cấp câu trả lời mới và chính xác dựa trên thực tế, đồng thời phù hợp với vị trí cụ thể hoặc khu vực khái quát mà người dùng chỉ định.

- **Câu trả lời chính xác, nhận biết vị trí:** Tận dụng dữ liệu phong phú và mới nhất của Google Maps cho các truy vấn cụ thể về mặt địa lý.
- **Cá nhân hoá nâng cao:** Điều chỉnh đề xuất và thông tin dựa trên vị trí do người dùng cung cấp.
- **Thông tin và tiện ích theo bối cảnh:** Mã thông báo theo bối cảnh để kết xuất các tiện ích tương tác của Google Maps cùng với nội dung được tạo.

## Bắt đầu

Ví dụ này minh hoạ cách tích hợp tính năng Kết nối với Google Maps vào ứng dụng của bạn để cung cấp câu trả lời chính xác, nhận biết vị trí cho các truy vấn của người dùng. Lời nhắc yêu cầu các đề xuất tại địa phương kèm theo vị trí không bắt buộc của người dùng, cho phép mô hình Gemini sử dụng dữ liệu của Google Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "What are the best Italian restaurants within a 15-minute walk from here?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
    model: "gemini-3-flash-preview",
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

Tính năng Kết nối với Google Maps tích hợp Gemini API với hệ sinh thái Google Geo bằng cách sử dụng API Maps làm nguồn liên kết thực tế. Khi truy vấn của người dùng chứa bối cảnh địa lý, mô hình Gemini có thể gọi công cụ Kết nối với Google Maps. Sau đó, mô hình này có thể tạo câu trả lời dựa trên dữ liệu của Google Maps liên quan đến vị trí được cung cấp.

Quá trình này thường bao gồm:

1. **Truy vấn của người dùng:** Người dùng gửi một truy vấn đến ứng dụng của bạn, có thể bao gồm bối cảnh địa lý (ví dụ: "quán cà phê gần tôi", "bảo tàng ở San Francisco").
2. **Gọi công cụ:** Mô hình Gemini, nhận ra ý định địa lý, sẽ gọi công cụ Kết nối với Google Maps. Bạn có thể tuỳ ý cung cấp `latitude` và `longitude` của người dùng cho công cụ này. Công cụ này là một công cụ tìm kiếm bằng văn bản và hoạt động tương tự như tìm kiếm trên Maps, trong đó các truy vấn tại địa phương ("gần tôi") sẽ sử dụng toạ độ, còn các truy vấn cụ thể hoặc không phải tại địa phương sẽ không bị ảnh hưởng bởi vị trí rõ ràng.
3. **Truy xuất dữ liệu:** Dịch vụ Kết nối với Google Maps truy vấn Google Maps để tìm thông tin có liên quan (ví dụ: địa điểm, bài đánh giá, ảnh, địa chỉ, giờ mở cửa).
4. **Tạo nội dung dựa trên dữ liệu thực tế:** Dữ liệu của Maps được truy xuất sẽ được dùng để cung cấp thông tin cho câu trả lời của mô hình Gemini, đảm bảo tính chính xác và mức độ phù hợp.
5. **Mã thông báo câu trả lời và tiện ích:** Mô hình này trả về một câu trả lời bằng văn bản, bao gồm cả trích dẫn các nguồn trên Google Maps. Bạn cũng có thể tuỳ ý để phản hồi API chứa `google_maps_widget_context_token`, cho phép nhà phát triển kết xuất một tiện ích Địa điểm theo bối cảnh trong ứng dụng của họ để tương tác bằng hình ảnh.

## Lý do và thời điểm nên sử dụng tính năng Kết nối với Google Maps

Tính năng Kết nối với Google Maps là lựa chọn lý tưởng cho những ứng dụng yêu cầu thông tin chính xác, mới nhất và dành riêng cho vị trí. Tính năng này giúp nâng cao trải nghiệm người dùng bằng cách cung cấp nội dung phù hợp và được cá nhân hoá dựa trên cơ sở dữ liệu phong phú của Google Maps về hơn 250 triệu địa điểm trên toàn thế giới.

Bạn nên sử dụng tính năng Kết nối với Google Maps khi ứng dụng của bạn cần:

- Cung cấp câu trả lời đầy đủ và chính xác cho các câu hỏi cụ thể về địa lý.
- Xây dựng trình lập kế hoạch chuyến đi và hướng dẫn viên địa phương theo hình thức trò chuyện.
- Đề xuất các địa điểm yêu thích dựa trên vị trí và lựa chọn ưu tiên của người dùng, chẳng hạn như nhà hàng hoặc cửa hàng.
- Tạo trải nghiệm nhận biết vị trí cho các dịch vụ xã hội, bán lẻ hoặc giao đồ ăn.

Tính năng Kết nối với Google Maps vượt trội trong các trường hợp sử dụng mà khoảng cách và dữ liệu thực tế hiện tại là rất quan trọng, chẳng hạn như tìm "quán cà phê ngon nhất gần tôi" hoặc tìm đường đi.

## Phương thức và tham số API

Tính năng Kết nối với Google Maps được cung cấp thông qua Gemini API dưới dạng một công cụ trong
phương thức [`generateContent`](https://ai.google.dev/api/generate-content?hl=vi). Bạn có thể bật và định cấu hình
tính năng Kết nối với Google Maps bằng cách thêm đối tượng
[`googleMaps`](https://ai.google.dev/api/caching?hl=vi#GoogleMaps) vào tham số `tools` trong yêu cầu của mình.

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

Công cụ [`googleMaps`](https://ai.google.dev/api/caching?hl=vi#GoogleMaps) cũng có thể chấp nhận tham số
boolean `enableWidget`. Tham số này được dùng để kiểm soát việc trường
[`googleMapsWidgetContextToken`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata)
có được trả về trong phản hồi hay không. Bạn có thể dùng tham số này để hiển thị một
[tiện ích Địa điểm theo bối cảnh](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=vi).

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

Ngoài ra, công cụ này còn hỗ trợ việc truyền vị trí theo bối cảnh dưới dạng `toolConfig`.

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

### Tìm hiểu về phản hồi kết nối

Khi một phản hồi được kết nối thành công với dữ liệu của Google Maps, phản hồi đó
sẽ bao gồm trường [`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata).
Dữ liệu có cấu trúc này là cần thiết để xác minh các tuyên bố và xây dựng trải nghiệm trích dẫn phong phú trong ứng dụng của bạn, cũng như đáp ứng các yêu cầu về việc sử dụng dịch vụ.

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

Gemini API trả về thông tin sau đây cùng với the
[`groundingMetadata`](https://ai.google.dev/api/generate-content?hl=vi#GroundingMetadata):

- `groundingChunks`: Mảng các đối tượng chứa nguồn `maps` (`uri`, `placeId` và `title`).
- `groundingSupports`: Mảng các đoạn để kết nối văn bản phản hồi của mô hình với các nguồn trong `groundingChunks`. Mỗi đoạn liên kết một khoảng văn bản (được xác định bởi `startIndex` và `endIndex`) với một hoặc nhiều `groundingChunkIndices`. Đây là chìa khoá để xây dựng trích dẫn nội tuyến.
- `googleMapsWidgetContextToken`: Mã thông báo văn bản có thể dùng để hiển thị một
  [tiện ích Địa điểm theo bối cảnh](https://developers.google.com/maps/documentation/javascript/reference/places-widget?hl=vi).

Để xem đoạn mã cho biết cách hiển thị trích dẫn nội tuyến trong văn bản, hãy xem [ví
dụ](https://ai.google.dev/gemini-api/docs/google-search?hl=vi#attributing_sources_with_inline_citations)
trong tài liệu Dựa trên kết quả của Google Tìm kiếm.

### Hiển thị tiện ích theo bối cảnh của Google Maps

Để sử dụng `googleMapsWidgetContextToken` được trả về, bạn cần [tải
Google Maps JavaScript
API](https://developers.google.com/maps/documentation/javascript/load-maps-js-api?hl=vi).

## Trường hợp sử dụng

Tính năng Kết nối với Google Maps hỗ trợ nhiều trường hợp sử dụng nhận biết vị trí. Các ví dụ sau đây minh hoạ cách các lời nhắc và tham số khác nhau có thể tận dụng tính năng Kết nối với Google Maps. Thông tin trong Kết quả dựa trên dữ liệu của Google Maps có thể khác với tình hình thực tế.

### Xử lý các câu hỏi cụ thể về địa điểm

Đặt câu hỏi chi tiết về một địa điểm cụ thể để nhận câu trả lời dựa trên bài đánh giá của người dùng Google và các dữ liệu khác của Maps.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Is there a cafe near the corner of 1st and Main that has outdoor seating?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
    model: 'gemini-3-flash-preview',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

Nhận các đề xuất phù hợp với lựa chọn ưu tiên của người dùng và một khu vực địa lý cụ thể.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Which family-friendly restaurants near here have the best playground reviews?"

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
    model: 'gemini-3-flash-preview',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

Trong ví dụ này, `googleMapsWidgetContextToken` đã được yêu cầu bằng cách bật tiện ích trong công cụ Google Maps. Khi được bật, mã thông báo được trả về
có thể dùng để kết xuất một tiện ích Địa điểm theo bối cảnh bằng cách sử dụng
`<gmp-places-contextual> component`
từ Google Maps JavaScript API.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

prompt = "Plan a day in San Francisco for me. I want to see the Golden Gate Bridge, visit a museum, and have a nice dinner."

response = client.models.generate_content(
    model='gemini-3-flash-preview',
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
    model: 'gemini-3-flash-preview',
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
curl -X POST 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent' \
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

Khi được kết xuất, tiện ích này sẽ trông giống như sau:

![Ví dụ về một tiện ích bản đồ khi được hiển thị](https://ai.google.dev/static/gemini-api/docs/images/maps/maps-widget.png?hl=vi)

## Yêu cầu về việc sử dụng dịch vụ

Phần này mô tả các yêu cầu về việc sử dụng dịch vụ đối với tính năng Kết nối với Google Maps.

### Thông báo cho người dùng về việc sử dụng các nguồn trên Google Maps

Với mỗi kết quả dựa trên dữ liệu của Google Maps, bạn sẽ nhận được các nguồn trong `groundingChunks` hỗ trợ từng câu trả lời. Siêu dữ liệu sau đây cũng được trả về:

- URI nguồn
- Tiêu đề
- ID

Khi trình bày kết quả từ tính năng Kết nối với Google Maps, bạn phải chỉ định các nguồn liên kết trên Google Maps và thông báo cho người dùng của mình về những điều sau:

- Các nguồn trên Google Maps phải xuất hiện ngay sau nội dung được tạo mà các nguồn đó hỗ trợ. Nội dung được tạo này còn được gọi là Kết quả dựa trên dữ liệu của Google Maps.
- Người dùng phải xem được các nguồn trên Google Maps trong một lượt tương tác của người dùng.

### Hiển thị các nguồn trên Google Maps kèm theo đường liên kết đến Google Maps

Đối với mỗi nguồn trong `groundingChunks` và trong `grounding_chunks.maps.placeAnswerSources.reviewSnippets`, bạn phải tạo bản xem trước đường liên kết theo các yêu cầu sau:

- Ghi công từng nguồn cho Google Maps theo nguyên tắc ghi công văn bản của Google Maps
  .
- Hiển thị tiêu đề nguồn được cung cấp trong phản hồi.
- Liên kết đến nguồn bằng cách sử dụng `uri` hoặc `googleMapsUri` từ phản hồi.

Những hình ảnh này cho thấy các yêu cầu tối thiểu để hiển thị các nguồn và đường liên kết đến Google Maps.

![Câu lệnh có câu trả lời cho thấy nguồn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-expanded.jpg?hl=vi)

Bạn có thể thu gọn chế độ xem các nguồn.

![Câu lệnh có phản hồi và nguồn được thu gọn](https://ai.google.dev/static/gemini-api/docs/images/maps/sources-collapsed.jpg?hl=vi)

Không bắt buộc: Nâng cao bản xem trước đường liên kết bằng nội dung bổ sung, chẳng hạn như:

- Biểu tượng trang web của [Google Maps](https://www.google.com/images/branding/product/ico/web_maps_icon_32dp.ico?hl=vi) được chèn trước phần ghi công văn bản của Google Maps.
- Một bức ảnh từ URL nguồn (`og:image`).

Để biết thêm thông tin về một số nhà cung cấp dữ liệu của Google Maps và các
điều khoản cấp phép của họ, hãy xem [thông báo pháp lý của Google Maps và Google Earth](https://www.google.com/help/legalnotices_maps/?hl=vi).

### Nguyên tắc ghi công văn bản của Google Maps

Khi bạn ghi công các nguồn cho Google Maps trong văn bản, hãy tuân theo các nguyên tắc sau:

- Không sửa đổi văn bản Google Maps theo bất kỳ cách nào:
  - Không thay đổi cách viết hoa của Google Maps.
  - Không xuống dòng cho Google Maps.
  - Không bản địa hoá Google Maps sang ngôn ngữ khác.
  - Ngăn trình duyệt dịch Google Maps bằng cách sử dụng thuộc tính HTML translate="no".
- Tạo kiểu cho văn bản Google Maps như mô tả trong bảng sau:

| Thuộc tính | Kiểu |
| --- | --- |
| `Font family` | Roboto. Bạn không bắt buộc phải tải phông chữ. |
| `Fallback font family` | Bất kỳ phông chữ không chân nào đã được dùng trong sản phẩm của bạn hoặc "Sans-Serif" để gọi phông chữ mặc định của hệ thống |
| `Font style` | Bình thường |
| `Font weight` | 400 |
| `Font color` | Trắng, đen (#1F1F1F) hoặc xám (#5E5E5E). Duy trì độ tương phản dễ tiếp cận (4,5:1) so với nền. |
| `Font size` | - Cỡ chữ tối thiểu: 12sp - Cỡ chữ tối đa: 16sp - Để tìm hiểu về sp, hãy xem bài viết Đơn vị cỡ chữ trên trang web [Material Design](https://m3.material.io/styles/typography/type-scale-tokens#3f4488e7-3b74-45b0-a143-9d6afa4d62dc). |
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

### Mã thông báo theo bối cảnh, mã địa điểm và mã bài đánh giá

Dữ liệu của Google Maps bao gồm mã thông báo theo bối cảnh, mã địa điểm và mã bài đánh giá. Bạn có thể lưu vào bộ nhớ đệm, lưu trữ và xuất dữ liệu phản hồi sau đây:

- `googleMapsWidgetContextToken`
- `placeId`
- `reviewId`

Các hạn chế đối với việc lưu vào bộ nhớ đệm trong Điều khoản về tính năng Kết nối với Google Maps không áp dụng.

### Hoạt động và lãnh thổ bị cấm

Tính năng Kết nối với Google Maps có thêm các hạn chế đối với một số nội dung và hoạt động để duy trì một nền tảng an toàn và đáng tin cậy. Ngoài các hạn chế về việc sử dụng
trong [Điều khoản](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-maps):

- Bạn sẽ không sử dụng tính năng Kết nối với Google Maps cho các hoạt động có rủi ro cao, bao gồm cả dịch vụ ứng phó khẩn cấp.
- Bạn sẽ không phân phối hoặc tiếp thị ứng dụng của mình cung cấp tính năng Kết nối với Google Maps ở Lãnh thổ bị cấm. Các Lãnh thổ bị cấm hiện tại là:

  - Trung Quốc
  - Crimea
  - Cuba
  - Cộng hoà Nhân dân Donetsk
  - Iran
  - Cộng hoà Nhân dân Luhansk
  - Triều Tiên
  - Syria
  - Việt Nam

  Danh sách này có thể được cập nhật theo thời gian.

## Các phương pháp hay nhất

- **Cung cấp vị trí của người dùng:** Để có câu trả lời phù hợp và được cá nhân hoá nhất, hãy luôn thêm `user_location` (vĩ độ và kinh độ) vào cấu hình `googleMapsGrounding` khi bạn biết vị trí của người dùng.
- **Kết xuất tiện ích theo bối cảnh của Google Maps:** Tiện ích theo bối cảnh được kết xuất bằng mã thông báo theo bối cảnh, `googleMapsWidgetContextToken`. Mã thông báo này được trả về trong phản hồi của Gemini API và có thể dùng để kết xuất nội dung trực quan từ Google Maps. Để biết thêm thông tin về tiện ích theo bối cảnh, hãy xem
  [Tiện ích Kết nối với Google Maps
  trong Hướng dẫn cho nhà phát triển của Google.](https://developers.google.com/maps/documentation/javascript/maps-grounding-widget?hl=vi)
- **Thông báo cho người dùng cuối:** Thông báo rõ ràng cho người dùng cuối rằng dữ liệu của Google Maps đang được dùng để trả lời các truy vấn của họ, đặc biệt là khi công cụ này được bật.
- **Theo dõi độ trễ:** Đối với các ứng dụng trò chuyện, hãy đảm bảo rằng độ trễ P95 cho các câu trả lời được kết nối vẫn nằm trong ngưỡng chấp nhận được để duy trì trải nghiệm người dùng mượt mà.
- **Tắt khi không cần:** Tính năng Kết nối với Google Maps được tắt theo mặc định. Chỉ bật tính năng này (`"tools": [{"googleMaps": {}}]`) khi một truy vấn có bối cảnh địa lý rõ ràng để tối ưu hoá hiệu suất và chi phí.

## Các điểm hạn chế

- **Phạm vi địa lý:** Tính năng Kết nối với Google Maps có trên toàn cầu
- **Hỗ trợ mô hình:** Xem phần [Mô hình được hỗ trợ](#supported-models).
- **Nội dung đầu vào/đầu ra đa phương thức:** Tính năng Kết nối với Google Maps hiện không hỗ trợ nội dung đầu vào hoặc đầu ra đa phương thức ngoài văn bản và tiện ích bản đồ theo bối cảnh.
- **Trạng thái mặc định:** Công cụ Kết nối với Google Maps được tắt theo mặc định.
  Bạn phải bật công cụ này một cách rõ ràng trong các yêu cầu API.

## Giá và hạn mức về giá

Giá của tính năng Kết nối với Google Maps dựa trên các truy vấn. Mức giá hiện tại là **25 USD / 1.000 câu lệnh được liên kết thực tế**. Cấp miễn phí cũng có tối đa 500 yêu cầu mỗi ngày. Một yêu cầu chỉ được tính vào hạn mức khi một lời nhắc trả về thành công ít nhất một kết quả được kết nối trên Google Maps (tức là kết quả chứa ít nhất một nguồn trên Google Maps). Nếu nhiều truy vấn được gửi đến Google Maps từ một yêu cầu, thì yêu cầu đó sẽ được tính là một yêu cầu theo hạn mức về giá.

Để biết thông tin chi tiết về giá, hãy xem [trang Giá của Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Các mô hình sau đây hỗ trợ tính năng Kết nối với Google Maps:

| Mô hình | Kết nối với Google Maps |
| --- | --- |
| [Bản xem trước Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=vi) | ✔️ |
| [Bản xem trước Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=vi) | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=vi) | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=vi) | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=vi) | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=vi) | ✔️ |

## Các cách kết hợp công cụ được hỗ trợ

Các mô hình Gemini 3 hỗ trợ việc kết hợp các công cụ tích hợp (như Kết nối với Google Maps) với các công cụ tuỳ chỉnh (gọi hàm). Tìm hiểu thêm trên trang về các cách kết hợp công cụ
.

## Bước tiếp theo

- Hãy thử tính năng [Dựa trên kết quả của Google Tìm kiếm trong Gemini API Sổ tay](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=vi).
- Tìm hiểu về các [công cụ khác hiện có](https://ai.google.dev/gemini-api/docs/tools?hl=vi).
- Để tìm hiểu thêm về các phương pháp hay nhất về AI có trách nhiệm và bộ lọc an toàn của Gemini API, hãy xem [Hướng dẫn về chế độ cài đặt an toàn](https://ai.google.dev/gemini-api/docs/safety-settings?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-04-29 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-04-29 UTC."],[],[]]
