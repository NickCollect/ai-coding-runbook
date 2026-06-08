---
source_url: https://ai.google.dev/gemini-api/docs/google-search?hl=vi
fetched_at: 2026-06-08T05:28:34.238354+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Tính năng Nghiên cứu chuyên sâu của Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=vi) hiện đang ở giai đoạn xem trước, với các tính năng lập kế hoạch cộng tác, hình ảnh hoá, hỗ trợ MCP và nhiều tính năng khác.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Bám sát nguồn bằng Google Tìm kiếm

Tính năng Bám sát nguồn bằng Google Tìm kiếm kết nối mô hình Gemini với nội dung trên web theo thời gian thực và hoạt động với tất cả các ngôn ngữ hiện có. Điều này cho phép Gemini đưa ra câu trả lời chính xác hơn và trích dẫn các nguồn có thể xác minh ngoài điểm cắt kiến thức.

Cơ sở kiến thức giúp bạn xây dựng các ứng dụng có thể:

- **Tăng độ chính xác về thông tin thực tế:** Giảm tình trạng ảo tưởng của mô hình bằng cách dựa vào thông tin thực tế để đưa ra câu trả lời.
- **Truy cập thông tin theo thời gian thực:** Trả lời các câu hỏi về các sự kiện và chủ đề gần đây.
- **Cung cấp thông tin trích dẫn:** Xây dựng niềm tin của người dùng bằng cách cho thấy nguồn của các tuyên bố của mô hình.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

grounding_tool = types.Tool(
    google_search=types.GoogleSearch()
)

config = types.GenerateContentConfig(
    tools=[grounding_tool]
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Who won the euro 2024?",
    config=config,
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const groundingTool = {
  googleSearch: {},
};

const config = {
  tools: [groundingTool],
};

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents: "Who won the euro 2024?",
  config,
});

console.log(response.text);
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Who won the euro 2024?"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

Bạn có thể tìm hiểu thêm bằng cách dùng [sổ tay công cụ Tìm kiếm](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=vi).

## Cách hoạt động của tính năng bám sát nguồn bằng Google Tìm kiếm

Khi bạn bật công cụ `google_search`, mô hình sẽ tự động xử lý toàn bộ quy trình tìm kiếm, xử lý và trích dẫn thông tin.

![grounding-overview](https://ai.google.dev/static/gemini-api/docs/images/google-search-tool-overview.png?hl=vi)

1. **Câu lệnh của người dùng:** Ứng dụng của bạn gửi câu lệnh của người dùng đến Gemini API khi bật công cụ `google_search`.
2. **Phân tích câu lệnh:** Mô hình sẽ phân tích câu lệnh và xác định xem Google Tìm kiếm có thể cải thiện câu trả lời hay không.
3. **Google Tìm kiếm:** Nếu cần, mô hình sẽ tự động tạo một hoặc nhiều cụm từ tìm kiếm và thực hiện các cụm từ đó.
4. **Xử lý kết quả tìm kiếm:** Mô hình xử lý kết quả tìm kiếm, tổng hợp thông tin và đưa ra câu trả lời.
5. **Câu trả lời bám sát nguồn:** API trả về một câu trả lời cuối cùng, thân thiện với người dùng và bám sát nguồn là các kết quả tìm kiếm. Phản hồi này bao gồm câu trả lời bằng văn bản của mô hình và `groundingMetadata` cùng với các cụm từ tìm kiếm, kết quả trên web và trích dẫn.

## Tìm hiểu về câu trả lời dựa trên thông tin thực tế

Khi một câu trả lời được căn cứ thành công, câu trả lời đó sẽ có trường `groundingMetadata`. Dữ liệu có cấu trúc này là yếu tố cần thiết để xác minh các tuyên bố và tạo trải nghiệm trích dẫn phong phú trong ứng dụng của bạn.

```
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "Spain won Euro 2024, defeating England 2-1 in the final. This victory marks Spain's record fourth European Championship title."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "UEFA Euro 2024 winner",
          "who won euro 2024"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML and CSS for the search widget -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "aljazeera.com"}},
          {"web": {"uri": "https://vertexaisearch.cloud.google.com.....", "title": "uefa.com"}}
        ],
        "groundingSupports": [
          {
            "segment": {"startIndex": 0, "endIndex": 85, "text": "Spain won Euro 2024, defeatin..."},
            "groundingChunkIndices": [0]
          },
          {
            "segment": {"startIndex": 86, "endIndex": 210, "text": "This victory marks Spain's..."},
            "groundingChunkIndices": [0, 1]
          }
        ]
      }
    }
  ]
}
```

Gemini API trả về thông tin sau bằng `groundingMetadata`:

- `webSearchQueries` : Mảng gồm các cụm từ tìm kiếm đã dùng. Điều này hữu ích cho việc gỡ lỗi và tìm hiểu quy trình suy luận của mô hình.
- `searchEntryPoint` : Chứa HTML và CSS để kết xuất các Đề xuất tìm kiếm bắt buộc. Bạn có thể xem toàn bộ yêu cầu sử dụng trong [Điều khoản dịch vụ](https://ai.google.dev/gemini-api/terms?hl=vi#grounding-with-google-search).
- `groundingChunks` : Mảng các đối tượng chứa nguồn trên web (`uri` và `title`).
- `groundingSupports` : Mảng các đoạn để kết nối phản hồi của mô hình `text` với các nguồn trong `groundingChunks`. Mỗi đoạn liên kết một văn bản `segment` (do `startIndex` và `endIndex` xác định) với một hoặc nhiều `groundingChunkIndices`. Đây là chìa khoá để tạo chú thích trong dòng.

Bạn cũng có thể sử dụng tính năng Bám sát nguồn bằng Google Tìm kiếm kết hợp với [công cụ ngữ cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) để bám sát nguồn câu trả lời bằng cả dữ liệu trên web công khai và các URL cụ thể mà bạn cung cấp.

## Ghi nguồn bằng trích dẫn cùng dòng

API này trả về dữ liệu trích dẫn có cấu trúc, giúp bạn kiểm soát hoàn toàn cách hiển thị nguồn trong giao diện người dùng. Bạn có thể sử dụng các trường `groundingSupports` và `groundingChunks` để liên kết trực tiếp các câu của mô hình với nguồn của chúng. Sau đây là một mẫu phổ biến để xử lý siêu dữ liệu nhằm tạo một phản hồi có các trích dẫn có thể nhấp vào trong dòng.

### Python

```
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # Sort supports by end_index in descending order to avoid shifting issues when inserting.
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # Create citation string like [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text

# Assuming response with grounding metadata
text_with_citations = add_citations(response)
print(text_with_citations)
```

### JavaScript

```
function addCitations(response) {
    let text = response.text;
    const supports = response.candidates[0]?.groundingMetadata?.groundingSupports;
    const chunks = response.candidates[0]?.groundingMetadata?.groundingChunks;

    // Sort supports by end_index in descending order to avoid shifting issues when inserting.
    const sortedSupports = [...supports].sort(
        (a, b) => (b.segment?.endIndex ?? 0) - (a.segment?.endIndex ?? 0),
    );

    for (const support of sortedSupports) {
        const endIndex = support.segment?.endIndex;
        if (endIndex === undefined || !support.groundingChunkIndices?.length) {
        continue;
        }

        const citationLinks = support.groundingChunkIndices
        .map(i => {
            const uri = chunks[i]?.web?.uri;
            if (uri) {
            return `[${i + 1}](${uri})`;
            }
            return null;
        })
        .filter(Boolean);

        if (citationLinks.length > 0) {
        const citationString = citationLinks.join(", ");
        text = text.slice(0, endIndex) + citationString + text.slice(endIndex);
        }
    }

    return text;
}

const textWithCitations = addCitations(response);
console.log(textWithCitations);
```

Câu trả lời mới có trích dẫn nội dòng sẽ có dạng như sau:

```
Spain won Euro 2024, defeating England 2-1 in the final.[1](https:/...), [2](https:/...), [4](https:/...), [5](https:/...) This victory marks Spain's record-breaking fourth European Championship title.[5]((https:/...), [2](https:/...), [3](https:/...), [4](https:/...)
```

## Giá

Khi bạn sử dụng tính năng Bám sát nguồn bằng Google Tìm kiếm với Gemini 3, dự án của bạn sẽ bị tính phí cho mỗi cụm từ tìm kiếm mà mô hình quyết định thực hiện. Nếu mô hình quyết định thực hiện nhiều cụm từ tìm kiếm để trả lời một câu lệnh duy nhất (ví dụ: tìm kiếm `"UEFA Euro 2024 winner"` và `"Spain vs England Euro 2024 final
score"` trong cùng một lệnh gọi API), thì điều này được tính là hai lần sử dụng công cụ có tính phí cho yêu cầu đó. Để tính phí, chúng tôi bỏ qua các cụm từ tìm kiếm trống trên web khi tính số lượng cụm từ tìm kiếm riêng biệt. Mô hình tính phí này chỉ áp dụng cho các mô hình Gemini 3; khi bạn sử dụng tính năng căn cứ vào kết quả tìm kiếm với Gemini 2.5 hoặc các mô hình cũ hơn, dự án của bạn sẽ được tính phí theo từng câu lệnh.

Để biết thông tin chi tiết về giá, hãy xem [trang định giá Gemini API](https://ai.google.dev/gemini-api/docs/pricing?hl=vi).

## Mô hình được hỗ trợ

Bạn có thể xem toàn bộ các chức năng trên trang [tổng quan về mẫu](https://ai.google.dev/gemini-api/docs/models?hl=vi).

| Mô hình | Bám sát nguồn bằng Google Tìm kiếm |
| --- | --- |
| Gemini 3.5 Flash | ✔️ |
| Gemini 3.1 Flash-Lite | ✔️ |
| Bản xem trước hình ảnh Gemini 3.1 Flash | ✔️ |
| Bản xem trước Gemini 3.1 Pro | ✔️ |
| Bản xem trước hình ảnh của Gemini 3 Pro | ✔️ |
| Bản xem trước Gemini 3 Flash | ✔️ |
| Bản xem trước Gemini 3.1 Flash-Lite | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️ |

## Các tổ hợp công cụ được hỗ trợ

Bạn có thể sử dụng tính năng Bám sát nguồn bằng Google Tìm kiếm với các công cụ khác như [thực thi mã](https://ai.google.dev/gemini-api/docs/code-execution?hl=vi) và [bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi) để hỗ trợ các trường hợp sử dụng phức tạp hơn.

Các mô hình Gemini 3 hỗ trợ việc kết hợp các công cụ tích hợp sẵn (chẳng hạn như tính năng Nền tảng kiến thức với Google Tìm kiếm) với các công cụ tuỳ chỉnh (lệnh gọi hàm). Tìm hiểu thêm trên trang [các tổ hợp công cụ](https://ai.google.dev/gemini-api/docs/tool-combination?hl=vi).

## Bước tiếp theo

- Hãy thử [Bám sát nguồn bằng Google Tìm kiếm trong sổ tay về Gemini API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Search_Grounding.ipynb?hl=vi).
- Tìm hiểu về các công cụ khác hiện có, chẳng hạn như [Gọi hàm](https://ai.google.dev/gemini-api/docs/function-calling?hl=vi).
- Tìm hiểu cách tăng cường câu lệnh bằng các URL cụ thể bằng [công cụ bối cảnh URL](https://ai.google.dev/gemini-api/docs/url-context?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-05-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-05-19 UTC."],[],[]]
