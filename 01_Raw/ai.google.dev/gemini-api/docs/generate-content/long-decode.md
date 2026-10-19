---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=vi
fetched_at: 2026-10-19T05:45:18.309607+00:00
title: "Gi\u1ea3i m\u00e3 d\u00e0i \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Giải mã dài

Tính năng giải mã dài cho phép Gemini 4 Argon tạo ra kết quả vượt quá giới hạn đầu ra của một yêu cầu cho các nhiệm vụ suy luận sâu, lên đến cửa sổ ngữ cảnh hợp nhất 1 triệu token (1.048.576 token được chia sẻ cho đầu vào, suy nghĩ và đầu ra).

Chỉ thay đổi mã mô hình sẽ không bật tính năng giải mã dài. Nếu không thiết lập thêm, đầu ra sẽ dừng ở 64.000 mã thông báo cho các lệnh gọi truyền trực tuyến và 32.000 mã thông báo cho các lệnh gọi không truyền trực tuyến. Cách nhanh nhất để bật tính năng giải mã dài là nâng cấp Google GenAI SDK và đặt `max_output_tokens` lớn hơn 65.536. Hướng dẫn này giải thích cách hoạt động của tính năng giải mã dài, thời điểm sử dụng và cách bật tính năng này bằng `generateContent`.

## Thời gian giải mã

Một yêu cầu truyền trực tuyến hoặc yêu cầu SDK duy nhất tạo ra tối đa 64.000 mã thông báo, còn yêu cầu REST không truyền trực tuyến tạo ra tối đa 32.000 mã thông báo. Khi một phản hồi cần thêm mã thông báo, mô hình sẽ tạo phản hồi đó qua nhiều bước yêu cầu và phản hồi, mỗi bước tiếp tục từ nơi bước trước dừng lại.

- **Giới hạn về số lượng mã thông báo đầu vào và đầu ra hợp nhất:** Đầu vào, quá trình suy nghĩ, lệnh gọi hàm và câu trả lời cuối cùng dùng chung một cửa sổ 1 triệu mã thông báo. Kết quả đầu ra có thể sử dụng tối đa 1.048.576 trừ đi số token đầu vào của bạn.
- **Giới hạn cho mỗi bước nhảy:** Một bước nhảy trả về tối đa 65.536 mã thông báo đầu ra. Yêu cầu REST không truyền trực tuyến trả về tối đa 32.768.
- **Tín hiệu tiếp tục:** Nếu mô hình đạt đến giới hạn và vẫn còn mã thông báo, thì phản hồi sẽ kết thúc bằng `finish_reason: CONTINUATION` và `continuation_token`.
- **Bước tiếp theo:** Máy khách gửi lại cùng một yêu cầu kèm theo mã thông báo. Mô hình sẽ tiếp tục từ nơi đã dừng lại.
- **Một tổng số cho tất cả các bước:** `max_output_tokens` đặt tổng số mã thông báo tư duy và đầu ra cho tất cả các bước cùng nhau.
- **Tín hiệu dừng:** Khi mô hình sử dụng hết `max_output_tokens`, câu trả lời sẽ kết thúc bằng `finish_reason: MAX_TOKENS`.

Đối với các vấn đề khó, một bước nhảy có thể sử dụng tất cả mã thông báo cho quá trình suy nghĩ nội bộ và trả về văn bản trống kèm theo `continuation_token`. Điều này là bình thường và câu trả lời cuối cùng sẽ xuất hiện ở các bước tiếp theo.

## Hạn mức đầu ra mặc định

Nếu không có tính năng giải mã dài, một yêu cầu sẽ dừng lại ở các giới hạn sau cho mỗi yêu cầu:

- **Yêu cầu truyền trực tuyến và yêu cầu không truyền trực tuyến thông qua SDK GenAI của Google (`generate_content`):** Mặc định là 64.000 mã thông báo đầu ra.
- **Lệnh gọi REST trực tiếp không truyền trực tuyến (`generateContent`):** Mặc định là 32.000 mã thông báo đầu ra. Nếu bạn đặt `max_output_tokens` lớn hơn 32.768 cho một lệnh gọi REST không truyền trực tuyến mà không có `continuation_token`,thì hệ thống sẽ trả về lỗi `400`.

| Cách bạn gọi mô hình | Giới hạn đầu ra mà không có quá trình giải mã dài | Giải mã lâu khi khởi chạy | Việc nên làm |
| --- | --- | --- | --- |
| Google GenAI SDK, phiên bản mới nhất | 64K | Có, SDK tiếp tục cho bạn | Đặt `max_output_tokens`. |
| Google GenAI SDK, phiên bản cũ, không truyền trực tuyến | 64K | Không | Nâng cấp SDK. |
| REST `streamGenerateContent` | 64K | Có, với vòng lặp của riêng bạn | Viết một vòng lặp. Xem [Cách 2](#option-2-loop). |
| REST `generateContent` | 32 nghìn | Có, bằng vòng lặp của riêng bạn | Viết một vòng lặp. Xem [Cách 2](#option-2-loop). |

## Trường hợp sử dụng tính năng giải mã dài

Hầu hết các yêu cầu đều nằm trong giới hạn yêu cầu duy nhất (64.000 mã thông báo cho các lệnh gọi phát trực tuyến và SDK hoặc 32.000 mã thông báo cho các lệnh gọi REST không phát trực tuyến). Hãy sử dụng tính năng giải mã dài khi một câu trả lời cần nhiều mã thông báo tư duy và mã thông báo đầu ra kết hợp hơn mức cho phép của một yêu cầu. Việc tăng `max_output_tokens` sẽ giúp mô hình có giới hạn cao hơn để suy luận về các vấn đề khó, thay vì làm cho các câu trả lời tiêu chuẩn dài hơn.

| Tải công việc | Sử dụng phương thức giải mã dài? | Lý do |
| --- | --- | --- |
| Toán học, khoa học, nghiên cứu và chứng minh chính thức ở mức độ khó | Có | Mô hình có thể sử dụng hơn 64.000 token để khám phá và kiểm tra lập luận của mình. |
| Những nhiệm vụ khó nhất về lập trình và tác nhân | Có | Một số nhiệm vụ cần hơn 64.000 token suy nghĩ và mã trong một câu trả lời. Hầu hết các nhiệm vụ lập trình và nhiệm vụ dạng tác nhân đều hoàn thành trong phạm vi 64 nghìn mã thông báo. |
| Hệ thống đánh giá dừng lại ở giới hạn đầu ra | Có | Việc giải mã dài ngăn câu trả lời bị cắt khi mô hình dành toàn bộ yêu cầu 64K hoặc 32K để suy nghĩ. |
| Trò chuyện, hỏi đáp, tóm tắt, phân loại và trích xuất | Không | Những nhiệm vụ này hoàn thành tốt dưới 32.000 mã thông báo. |
| Yêu cầu về độ dài cố định, chẳng hạn như "viết một cuốn sách dài 700.000 từ" | Không | Mô hình không tuân theo mục tiêu về độ dài. |
| Các tác nhân gọi công cụ trong nhiều lượt ngắn | Không | Mỗi lượt chơi đều ngắn. Kết quả đầu ra lớn ở mỗi lượt sẽ nhanh chóng lấp đầy cửa sổ đầu vào và đầu ra hợp nhất 1 triệu token. |
| Câu lệnh gần đạt đến giới hạn đầu vào là 1 triệu | Không | Kết quả đầu ra chỉ có thể sử dụng 1 triệu trừ đi dữ liệu đầu vào của bạn. |
| Yêu cầu có độ trễ thấp | Không | Quá trình giải mã dài có thể mất vài phút. |

Việc đặt `max_output_tokens` cao giúp mô hình có thêm thời gian suy nghĩ về các vấn đề khó, nhưng mô hình vẫn quyết định lượng nội dung cần viết. Để kiểm soát mức độ nỗ lực suy luận mà mô hình sử dụng, hãy đặt [`thinking_level`](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=vi).

## Bật tính năng giải mã dài

Bạn có thể tự động chạy giải mã dài bằng SDK Google GenAI (Lựa chọn 1, nên dùng cho hầu hết ứng dụng) hoặc viết vòng lặp tiếp tục của riêng bạn (Lựa chọn 2). Cả hai lựa chọn này đều hỗ trợ cửa sổ ngữ cảnh 1 triệu token.

|  | Cách 1: SDK Google GenAI (nên dùng) | Cách 2: Vòng lặp phát trực tuyến của riêng bạn | Cách 2: Vòng lặp không phát trực tuyến của riêng bạn |
| --- | --- | --- | --- |
| **Ai bắt đầu mỗi lượt chuyển tiếp** | SDK. Bạn đã đặt `max_output_tokens`. | Mã của bạn, tại mỗi điểm kiểm tra hoặc sau khi luồng bị rớt | Mã của bạn, mỗi 32.000 token |
| **Số mã thông báo trên mỗi yêu cầu** | 64K mỗi bước nhảy | 64.000 mã thông báo cho mỗi luồng, với một điểm kiểm tra sau mỗi 5.000 mã thông báo sau 32.000 | 32 nghìn mỗi yêu cầu |
| **Giới hạn thời gian cho mỗi yêu cầu** | 20 phút | 20 phút | 20 phút |
| **Bộ nhớ** | Không có bộ nhớ máy chủ | Không có bộ nhớ máy chủ | Không có bộ nhớ máy chủ |
| **Phù hợp nhất cho** | Hầu hết các ứng dụng | Người gọi REST và các thiết bị tuỳ chỉnh truyền phát trực tiếp | Các công cụ đánh giá đơn giản |

`continuation_token` được mã hoá sẽ mang trạng thái của mô hình giữa các yêu cầu, vì vậy không có dữ liệu nào được lưu trữ trên máy chủ.

### Cách 1: Sử dụng SDK Google GenAI (nên dùng)

Trong Google GenAI SDK mới nhất, `automatic_continuation` được bật theo mặc định cho cả lệnh gọi truyền trực tuyến và không truyền trực tuyến, vì vậy bạn không cần đặt tham số này. Khi bạn đặt `max_output_tokens` cao hơn giới hạn cho mỗi yêu cầu, SDK sẽ tự động chạy các bước tiếp theo và trả về một phản hồi kết hợp.

1. Nâng cấp SDK.

   ### Python

   ```
   pip install -U "google-genai>=2.30.1"
   ```

   ### JavaScript

   ```
   npm install "@google/genai@>=2.29.1"
   ```
2. Đặt `max_output_tokens` lớn hơn 65.536.

   ### Python

   ```
   from google import genai
   from google.genai import types

   client = genai.Client()  # Reads GEMINI_API_KEY

   response = client.models.generate_content(
       model="gemini-4-argon",
       contents="Write a complete, rigorous proof of the prime number theorem.",
       config=types.GenerateContentConfig(
           max_output_tokens=262_144,  # Total thinking and output for all hops
           thinking_config=types.ThinkingConfig(thinking_level="high"),
           automatic_continuation=True,  # Default. Shown for clarity.
       ),
   )

   print(response.text)
   print("Finish reason:", response.candidates[0].finish_reason)
   print("Prompt size:", response.usage_metadata.initial_prompt_token_count)
   print("Billed tokens:", response.usage_metadata.total_token_count)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI, ThinkingLevel } from "@google/genai";

   const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY

   const response = await ai.models.generateContent({
     model: "gemini-4-argon",
     contents: "Write a complete, rigorous proof of the prime number theorem.",
     config: {
       maxOutputTokens: 262144, // Total thinking and output for all hops
       thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
       automaticContinuation: true, // Default. Shown for clarity.
     },
   });

   console.log(response.text);
   console.log("Finish reason:", response.candidates?.[0]?.finishReason);
   console.log("Prompt size:", response.usageMetadata?.initialPromptTokenCount);
   console.log("Billed tokens:", response.usageMetadata?.totalTokenCount);
   ```

Xin lưu ý những điều sau đây:

- **Phát trực tuyến:** `generate_content_stream` (Python) và `generateContentStream` (JavaScript) cũng tiếp tục cho bạn. Nếu một luồng bị rớt sau một điểm kiểm tra, thì SDK sẽ tiếp tục từ điểm kiểm tra đó.
- **Thời gian chờ:** Thời gian chờ và số lần thử lại áp dụng cho từng bước, chứ không phải cho toàn bộ quá trình chạy.
- **Kiểm soát thủ công:** Để tự chạy vòng lặp, hãy đặt `automatic_continuation=False` (Python) hoặc `automaticContinuation: false` (JavaScript). Sau đó, hãy làm theo Cách 2.
- **Mức sử dụng:** Các trường mức sử dụng cho biết tổng số tất cả các chặng. Để biết kích thước của câu lệnh, hãy đọc `initial_prompt_token_count`. Xem phần [Đếm mã thông báo](#count-tokens).

### Cách 2: Tự viết vòng lặp

Viết vòng lặp của riêng bạn nếu bạn gọi REST trực tiếp, sử dụng ngôn ngữ không có SDK mới nhất hoặc cần toàn quyền kiểm soát. Bạn cũng có thể tham khảo các cách triển khai SDK AI tạo sinh của Google trong [Python](https://github.com/googleapis/python-genai/blob/v2.30.1/google/genai/models.py#L6111) và [JavaScript/TypeScript](https://github.com/googleapis/js-genai/blob/v2.29.1/src/models.ts#L88).

Hãy tuân thủ các quy tắc sau:

1. **Gửi cùng một yêu cầu trên mọi bước nhảy.** Gửi `contents`, `system_instruction`, `tools` và `generation_config` ban đầu. Giữ nguyên `max_output_tokens`.
2. **Đừng thêm kết quả một phần vào `contents`.** `continuation_token` mang trạng thái của mô hình, bao gồm cả suy nghĩ của mô hình.
3. **Chỉ gửi mã thông báo mới nhất.** Mỗi mã thông báo đều chứa tất cả tiến trình trước đó.
4. **Tiếp tục trong khi `finish_reason` là `CONTINUATION`.** Dừng khi có bất kỳ lý do kết thúc nào khác.
5. **Nối các phần sau bước nhảy cuối cùng.** Kết hợp các phần của tất cả các bước nhảy thành một lượt của mô hình cho nhật ký trò chuyện.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()  # Reads GEMINI_API_KEY
PROMPT = "Write a complete, rigorous proof of the prime number theorem."
parts = []
token = None

while True:
    response = client.models.generate_content(
        model="gemini-4-argon",
        contents=PROMPT,  # The original contents on every request
        config=types.GenerateContentConfig(
            max_output_tokens=262_144,  # The same total on every request
            thinking_config=types.ThinkingConfig(thinking_level="high"),
            automatic_continuation=False,  # You run the loop
            continuation_token=token,
        ),
    )
    candidate = response.candidates[0]
    if candidate.content and candidate.content.parts:
        parts.extend(candidate.content.parts)
    token = candidate.continuation_token
    if candidate.finish_reason != types.FinishReason.CONTINUATION or not token:
        break

print("".join(p.text for p in parts if p.text and not p.thought))
print("Finish reason:", candidate.finish_reason)
```

### JavaScript

```
import { GoogleGenAI, ThinkingLevel } from "@google/genai";

const ai = new GoogleGenAI({}); // Reads GEMINI_API_KEY
const PROMPT = "Write a complete, rigorous proof of the prime number theorem.";
const parts = [];
let token = undefined;
let candidate = undefined;

while (true) {
  const response = await ai.models.generateContent({
    model: "gemini-4-argon",
    contents: PROMPT, // The original contents on every request
    config: {
      maxOutputTokens: 262144, // The same total on every request
      thinkingConfig: { thinkingLevel: ThinkingLevel.HIGH },
      automaticContinuation: false, // You run the loop
      continuationToken: token,
    },
  });
  candidate = response.candidates?.[0];
  if (candidate?.content?.parts) {
    parts.push(...candidate.content.parts);
  }
  token = candidate?.continuationToken;
  if (candidate?.finishReason !== "CONTINUATION" || !token) {
    break;
  }
}

console.log(parts.filter((p) => p.text && !p.thought).map((p) => p.text).join(""));
console.log("Finish reason:", candidate?.finishReason);
```

### REST

```
# Hop 1: send the request with max_output_tokens.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    }
  }'

# Hop 2: if finishReason is CONTINUATION, send the same request plus the token.
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-4-argon:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "Write a complete, rigorous proof of the prime number theorem."}]}],
    "generationConfig": {
      "maxOutputTokens": 262144,
      "thinkingConfig": {"thinkingLevel": "high"}
    },
    "continuationToken": "TOKEN_FROM_HOP_1"
  }'
```

Một hop chỉ dành cho việc suy nghĩ sẽ trả về `text` trống với `finishReason: "CONTINUATION"`. Hãy coi đây là tiến trình bình thường và yêu cầu hop tiếp theo:

```
{
  "candidates": [{
    "content": {"role": "model", "parts": [{"text": ""}]},
    "finishReason": "CONTINUATION",
    "continuationToken": "CiQ4ZmQ3..."
  }],
  "usageMetadata": {
    "promptTokenCount": 142,
    "candidatesTokenCount": 0,
    "thoughtsTokenCount": 32768,
    "totalTokenCount": 32910
  }
}
```

**Vòng lặp phát trực tuyến** cần thêm một quy tắc nữa. Sau 32.768 mã thông báo đầu tiên, luồng sẽ gửi một mã thông báo điểm kiểm tra sau mỗi 5.000 mã thông báo. Giữ các đoạn mới trong danh sách đang chờ xử lý. Khi một đoạn có `continuation_token`, hãy di chuyển các đoạn đang chờ xử lý sang kết quả đã cam kết và lưu mã thông báo. Nếu luồng bị gián đoạn, hãy loại bỏ các đoạn đang chờ xử lý và tiếp tục từ mã thông báo gần đây nhất. Nếu luồng bị gián đoạn trước điểm kiểm tra đầu tiên, hãy gửi lại yêu cầu ban đầu.

## Đặt `max_output_tokens`

`max_output_tokens` đặt giới hạn kết hợp cho việc suy nghĩ và kết quả đầu ra trên tất cả các bước. Việc giảm giá trị này không khiến mô hình suy nghĩ ngắn gọn hơn mà thay vào đó sẽ cắt bớt câu trả lời sớm hơn.

| Khối lượng công việc của bạn | `max_output_tokens` đề xuất |
| --- | --- |
| Ứng dụng hiện có có giới hạn thấp hơn 32K | Tăng lên 32.768. |
| Các nhiệm vụ lập trình và nhiệm vụ dựa trên tác nhân dài | Bắt đầu từ 65.536. |
| Toán học, khoa học, nghiên cứu và chứng minh khó | Giá trị thử nghiệm từ 262.144 đến 1.048.576 trừ đi số mã thông báo đầu vào. |

Để sử dụng ít mã thông báo hơn, hãy giảm `thinking_level`. Sử dụng `high` cho những nhiệm vụ suy luận khó nhất. Sử dụng `medium` (mặc định) cho hầu hết các công việc lập trình và tác nhân. Sử dụng `low` cho các tác vụ ít phức tạp hơn.

## Xử lý các yêu cầu chạy trong thời gian dài

Vì Gemini 4 Argon suy nghĩ lâu hơn các mô hình Gemini 3.x đối với các vấn đề khó, nên bạn cần tăng thời gian chờ của ứng dụng để các yêu cầu dài không bị ngắt kết nối sớm.

- **Cuộc gọi không truyền trực tuyến:** Máy chủ sẽ đóng kết nối sau 10 phút.
- **Cuộc gọi trực tuyến:** Máy chủ sẽ đóng luồng sau 20 phút.
- **Thời gian chờ của ứng dụng:** Đặt thời gian chờ đọc HTTP thành 20 phút. Thời gian chờ 3 phút hoặc 5 phút sẽ dừng yêu cầu sớm.

Trong Python, hãy đặt thời gian chờ trên ứng dụng khách tính bằng mili giây:

```
client = genai.Client(http_options=types.HttpOptions(timeout=1_200_000))  # 20 minutes
```

Đối với những công việc mà ứng dụng của bạn thăm dò ý kiến, Interactions API sẽ chạy quá trình giải mã dài trên máy chủ. Xem phần [thực thi trong nền](https://ai.google.dev/gemini-api/docs/background-execution?hl=vi).

## Tiếp tục khi mô hình sử dụng tất cả mã thông báo đầu ra

Khi một phản hồi kết thúc bằng `MAX_TOKENS`, phản hồi đó vẫn chứa `continuation_token`. Bạn có hai lựa chọn:

- **Tiếp tục:** Gửi cùng một yêu cầu kèm theo mã thông báo và `max_output_tokens` cao hơn. Giá trị phải cao hơn số lượng mã thông báo đã sử dụng cho đến nay. Nếu không, API sẽ trả về lỗi 400.
- **Bắt đầu lại:** Gửi yêu cầu ban đầu với `max_output_tokens` cao hơn và không có mã thông báo. Bạn sẽ phải trả tiền cho cả hai lần chạy.

## Đếm số token

Với tính năng tiếp tục tự động, `usage_metadata` sẽ báo cáo tổng số lượt truy cập trên tất cả các chặng. SDK sẽ cộng mọi trường số lượng: `prompt_token_count`, `cached_content_token_count`, `candidates_token_count`, `thoughts_token_count` và `total_token_count`.

`prompt_token_count` cộng dồn mã thông báo đầu vào của mỗi bước nhảy. Mỗi bước sẽ gửi câu lệnh của bạn cùng với mọi nội dung đã tạo cho đến thời điểm đó trở lại mô hình dưới dạng dữ liệu đầu vào, vì vậy, các mã thông báo giống nhau sẽ được tính lại ở mỗi bước sau đó. Ví dụ: với SDK Google GenAI, một câu lệnh 1.000 mã thông báo tạo ra 200.000 mã thông báo suy nghĩ và đầu ra sẽ mất 4 bước:

| Hop | Dữ liệu đầu vào được gửi đến mô hình | Mã thông báo nhập |
| --- | --- | --- |
| 1 | Câu lệnh | 1.000 |
| 2 | Lời nhắc + hop 1 | 66.536 |
| 3 | Lời nhắc + bước nhảy 1 và 2 | 132.072 |
| 4 | Câu lệnh + 1 đến 3 bước | 197.608 |
| **Tổng cộng** |  | **397.216** |

`prompt_token_count` báo cáo khoảng 397.000 mã thông báo (với các đầu vào lặp lại được giảm tự động 95% nhờ bộ nhớ đệm ngầm) và `total_token_count` báo cáo khoảng 597.000 mã thông báo, mặc dù kích thước ngữ cảnh thực tế chỉ khoảng 201.000 mã thông báo: câu lệnh 1.000 mã thông báo cộng với 200.000 mã thông báo của quá trình suy nghĩ và đầu ra. Vòng lặp REST không truyền trực tuyến sử dụng 32K bước nhảy, vì vậy,cần 7 bước nhảy cho cùng một đầu ra và báo cáo 695.128 mã thông báo đầu vào.

| Cách bạn gọi mô hình | Nội dung `usage_metadata` cho thấy | Chi phí | Đối với kích thước câu lệnh |
| --- | --- | --- | --- |
| Google GenAI SDK, tự động tiếp tục (mặc định) | Tổng số trên tất cả các chặng | Đọc các trường sử dụng như hiện tại. | Đọc `usage_metadata.initial_prompt_token_count` (Python) hoặc `usageMetadata.initialPromptTokenCount` (JavaScript). |
| SDK có `automatic_continuation=False` hoặc REST | Một bước nhảy cho mỗi phản hồi | Thêm từng trường trên các chặng. | Đọc `prompt_token_count` từ bước nhảy đầu tiên. |

`prompt_token_count` và `total_token_count` là tổng của mọi bước nhảy, chứ không phải kích thước của bối cảnh. Đừng sử dụng các mã thông báo này để quyết định thời điểm tóm tắt hoặc cắt bớt nhật ký trò chuyện (thu gọn ngữ cảnh) hoặc để thực thi giới hạn ngữ cảnh. Để ước tính kích thước ngữ cảnh, hãy cộng kích thước câu lệnh trong bảng vào `candidates_token_count` và `thoughts_token_count`.

Cập nhật khung tác nhân, công cụ đánh giá hoặc proxy trước khi bạn chạy quy trình giải mã dài:

- **Các tác nhân và công cụ đánh giá:** Nếu mã của bạn nén ngữ cảnh hoặc dừng một lần chạy ở giới hạn mã thông báo, hãy sử dụng `initial_prompt_token_count` (hoặc `prompt_token_count` của bước nhảy đầu tiên trong REST) thay vì `prompt_token_count` được cộng. Các phản hồi hoàn tất trong một bước nhảy sẽ báo cáo cùng một giá trị trong cả hai trường, vì vậy, các thử nghiệm ngắn không cho thấy vấn đề.
- **Các proxy và cổng gọi REST:** Mỗi phản hồi REST chỉ báo cáo bước nhảy của riêng mình. Cộng từng trường trong các bước nhảy để tính chi phí và giữ `promptTokenCount` của bước nhảy đầu tiên làm kích thước câu lệnh. Nếu không, người dùng của bạn sẽ thấy các số khác với số mà người dùng SDK thấy cho cùng một yêu cầu.
- **Nhật ký và phản hồi được chuyển đổi tuần tự:** SDK tính toán `initial_prompt_token_count` trên ứng dụng khách. Thông tin này không có trong phản hồi REST hoặc trong kết quả JSON của SDK, chẳng hạn như `model_dump()`. Hãy lưu giá trị này dưới dạng một giá trị riêng biệt nếu bạn cần dùng sau này.

Nếu bạn phát trực tuyến trong vòng lặp của riêng mình, thì `usage_metadata` sẽ được tích luỹ trong mỗi sự kiện phát trực tiếp. Chỉ giữ lại giá trị cuối cùng của mỗi luồng, sau đó cộng các giá trị qua các bước nhảy.

## Tìm hiểu về việc tính phí

Bạn phải trả phí cho mọi mã thông báo trong mọi bước, kể cả những bước chỉ chứa suy nghĩ.

- **Chiết khấu cho bộ nhớ đệm:** Bộ nhớ đệm ngầm định giúp giảm 95% chi phí cho dữ liệu đầu vào lặp lại trong mỗi bước. Trong giai đoạn ra mắt, chi phí cho dữ liệu đầu vào được lưu vào bộ nhớ đệm là 0,1 USD/1 triệu token thay vì 2 USD.
- **Hết hạn bộ nhớ đệm:** Bộ nhớ đệm sẽ hết hạn sau 15 đến 20 phút nếu không được sử dụng. Nếu bạn tạm dừng lâu giữa các lần nhảy, thì tốc độ đầu vào sẽ được tính lại từ đầu.
- **Lượt gọi không trực tuyến không thành công:** Bạn chỉ trả phí khi một phản hồi hoàn tất. Yêu cầu không thành công hoặc bị huỷ sẽ không mất phí.
- **Luồng bị rớt:** Luồng bị rớt trước khi đạt 32.000 mã thông báo sẽ có giá 0 USD. Sau đó, bạn thanh toán cho đến mã thông báo điểm kiểm tra cuối cùng, vì bạn có thể tiếp tục từ đó.

## Khắc phục sự cố

| Dấu hiệu | Nguyên nhân và cách khắc phục |
| --- | --- |
| Đầu ra dừng ở 64K hoặc 32K với `CONTINUATION` | Mô hình vẫn còn mã thông báo, nhưng không có gì tiếp tục yêu cầu. Nâng cấp SDK hoặc thêm vòng lặp. |
| Đầu ra dừng ở 64K hoặc 32K với `MAX_TOKENS` | `max_output_tokens` chưa được đặt hoặc quá thấp. Đặt giá trị này lớn hơn 65.536. |
| Văn bản trống có `MAX_TOKENS` | Mô hình đã sử dụng tất cả mã thông báo để suy nghĩ. Tăng `max_output_tokens` hoặc giảm `thinking_level`. |
| 400: "Mã thông báo tiếp tục đã sử dụng mã thông báo đầu ra..." | `max_output_tokens` không vượt quá số lượng mã thông báo đã sử dụng cho đến nay. Nâng nó lên. |
| Lỗi đối với `thinking_level: "minimal"` hoặc đối với `thinking_budget` có `thinking_level` | Gemini 4 Argon không hỗ trợ `minimal`. Sử dụng `low`, `medium` hoặc `high`. Đặt `thinking_level` hoặc `thinking_budget`, không đặt cả hai. |
| Cảnh báo cho `thinking_budget`, `temperature`, `top_p` hoặc `top_k` | Gemini 4 Argon bỏ qua hoặc liên kết các trường này. Sử dụng `thinking_level` và xoá các tham số lấy mẫu. |
| Yêu cầu sẽ kết thúc sau 3 hoặc 5 phút | Thời gian chờ của ứng dụng quá ngắn. Đặt thành 20 phút. |
| Quá trình thu gọn bối cảnh bắt đầu quá sớm | Bộ khung đọc tổng đầu vào. Thay vào đó, hãy đọc `initial_prompt_token_count`. |

## Các điểm hạn chế

- **Điểm cuối khả năng tương thích với OpenAI:** Không có tính năng giải mã dài. Kết quả đầu ra sẽ dừng ở giới hạn cho mỗi yêu cầu.
- **SDK cũ:** Các phiên bản thấp hơn mức tối thiểu trong ghi chú sẽ không tự động tiếp tục.
- **Độ dài:** Mô hình không tuân theo mục tiêu về độ dài mã thông báo hoặc số từ.

## Danh sách kiểm tra

- Nâng cấp Google GenAI SDK lên phiên bản tối thiểu.
- Đặt `max_output_tokens` lớn hơn 65.536.
- Sử dụng `thinking_level` (`low`, `medium` hoặc `high`), không sử dụng `thinking_budget`.
- Đặt thời gian chờ đọc HTTP thành 20 phút.
- Sử dụng `initial_prompt_token_count` cho kích thước và độ nén của bối cảnh.
- Chạy một câu lệnh để thử nghiệm trước khi đánh giá trên quy mô lớn.

## Các bước tiếp theo

- [Tính năng mới trong Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/generate-content/latest-model?hl=vi)
- [Đang suy nghĩ](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=vi)
- [Đếm số lượng mã thông báo](https://ai.google.dev/gemini-api/docs/generate-content/tokens?hl=vi)

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-13 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-13 UTC."],[],[]]
