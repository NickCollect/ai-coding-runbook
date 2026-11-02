---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=vi
fetched_at: 2026-11-02T07:24:33.465691+00:00
title: "Thi\u1ebft k\u1ebf gi\u1ecdng n\u00f3i \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs/generate-content?hl=vi)

Gửi ý kiến phản hồi

# Thiết kế giọng nói

Thiết kế giọng nói cho phép bạn tạo một cá tính giọng nói hoàn toàn mới và bền vững từ nội dung mô tả bằng ngôn ngữ tự nhiên bằng cách sử dụng điểm cuối Giọng nói của Gemini API (`POST /v1beta/voices`). Thay vì bị giới hạn ở giọng nói được tạo sẵn hoặc bản ghi âm tham chiếu, bạn có thể mô tả độ tuổi, âm sắc, giọng điệu và cách truyền đạt cơ bản của nhân vật, đồng thời nhận được mã nhận dạng `voice_...` có thể dùng lại được lưu vào dự án của bạn.

Cách nhanh nhất để thiết kế, thử giọng và lặp lại các giọng nói tuỳ chỉnh là sử dụng phòng thu **Thiết kế giọng nói** tương tác trong [Google AI Studio](https://aistudio.google.com/generate-speech?hl=vi). Bạn có thể tạo các vai trò tuỳ chỉnh từ câu lệnh văn bản, kiểm thử các vai trò đó bằng tập lệnh mẫu và sao chép mã nhận dạng `voice_...` thu được trực tiếp vào mã xử lý ứng dụng của bạn.

[Dùng thử trong Google AI Studio](https://aistudio.google.com/generate-speech?hl=vi)

Cả [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi) (`gemini-3.8-flash-tts`) và [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi) (`gemini-3.8-flash-lite-tts`) đều hỗ trợ Thiết kế giọng nói.

## Tạo giọng nói được thiết kế

Sử dụng Google GenAI SDK (`google-genai` 2.25.0 trở lên / `@google/genai` 2.24.0 trở lên) hoặc API REST để tạo giọng nói tuỳ chỉnh từ nội dung mô tả bằng văn bản. Đối với giọng nói `"prompted"`, cả `voices.create` (`CreateVoice`) và `voices.get` (`GetVoice`) đều trả về trường `sample_audio` chỉ có đầu ra (`mime_type: "audio/wav"`, `data` được mã hoá base64) để bạn có thể nghe thử giọng nói được tạo ngay lập tức:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Cách hoạt động của thiết kế giọng nói

1. **Tạo giọng nói được nhắc:** Gọi `voices.create` (`POST /v1beta/voices`) bằng `type="prompted"` và `store=True`.
2. **Nhận bản xem trước `voice_id` và `sample_audio` liên tục:** API này tạo danh tính giọng nói, lưu trữ danh tính đó trong dự án của bạn và trả về một mã nhận dạng vĩnh viễn (ví dụ: `voice_abc123...`) cùng với `sample_audio` (`mime_type: "audio/wav"`, `data` được mã hoá base64) chứa âm thanh xem trước đã tạo cho giọng nói.
3. **Tổng hợp lời nói:** Truyền `voice_id` trong `speechConfig.voiceConfig.voice` khi gọi `generateContent`.

## Tổng hợp lời nói bằng giọng nói do bạn thiết kế

Truyền `id` (`voice_...`) đã trả về trong `voiceConfig.voice` khi gọi `generateContent`:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Quản lý giọng nói

Bạn có thể liệt kê, lọc, kiểm tra và xoá giọng nói đã lưu trữ bất cứ lúc nào bằng Voices API (xem phần [Thư viện giọng nói mở rộng và tính năng lọc](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=vi#voice-library) để biết tất cả các tham số lọc).

- **Giới hạn bộ nhớ và TTL:** Giọng nói có trạng thái (`store=True`, được chia sẻ giữa giọng nói được nhắc và giọng nói được sao chép) có giới hạn là **200 giọng nói cho mỗi dự án** và **TTL (thời gian tồn tại) là 1 năm**.
- **`sample_audio` phạm vi cung cấp:** `voices.create()` (`CreateVoice`) và `voices.get()` (`GetVoice`) điền sẵn `sample_audio` (`mime_type:
  "audio/wav"`, `data` được mã hoá bằng base64) cho các giọng nói `"prompted"`. Để giữ cho danh sách gọn nhẹ, `voices.list()` (`ListVoices`) sẽ bỏ qua `sample_audio` (và `sample_audio` sẽ không được đặt cho giọng nói `"replicated"` và `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Các phương pháp hay nhất để viết câu lệnh cho thiết kế giọng nói

- **Đưa các đặc điểm giọng nói cố định vào phần Thiết kế giọng nói, không phải `style`:** Xác định các đặc điểm không thay đổi (chẳng hạn như độ tuổi, giới tính, âm sắc, chất giọng và giọng vùng miền) khi tạo giọng nói trong `voices.create`.
- **Dành `speech_metadata.style` cho cảm xúc theo tình huống:** Sau khi tạo giọng nói tuỳ chỉnh, hãy dùng các câu lệnh ngắn `style` (ví dụ: `"whispered urgently"` hoặc `"cheerful and energetic"`) để hướng dẫn diễn xuất từng bước mà không làm thay đổi danh tính cốt lõi của người nói.
- **Nêu cụ thể và ngắn gọn:** Nội dung mô tả rõ ràng từ 1 đến 2 câu (chẳng hạn như *"Một người dẫn chương trình thể thao sắc sảo, tràn đầy năng lượng ở độ tuổi 30, có giọng nói hơi pha tạp của vùng Trung Tây"*) sẽ tạo ra kết quả rõ ràng và nhất quán hơn so với các đoạn văn mâu thuẫn hoặc quá dài.

## Bước tiếp theo

- Tìm hiểu cách nhân bản giọng nói của một người nói hiện có trong tính năng [Nhân bản giọng nói](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=vi).
- Khám phá kiểu theo lượt, thẻ nội tuyến và đoạn hội thoại nhiều người nói trong [Hướng dẫn về tính năng chuyển văn bản sang lời nói](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-24 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-24 UTC."],[],[]]
