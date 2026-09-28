---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi
fetched_at: 2026-09-28T06:20:51.608328+00:00
title: "T\u1ea1o l\u1eddi n\u00f3i t\u1eeb v\u0103n b\u1ea3n (TTS) \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo lời nói từ văn bản (TTS)

Gemini API có thể chuyển đổi văn bản đầu vào thành âm thanh một người nói hoặc nhiều người nói bằng cách sử dụng các chức năng tạo lời nói từ văn bản (TTS) của Gemini.
Tính năng tạo văn bản thành lời nói có thể *[kiểm soát](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#controllable)*, tức là bạn có thể kết hợp siêu dữ liệu lượt có cấu trúc (`speech_metadata`) và thẻ thoại nội dòng để hướng dẫn *phong cách*, *giọng*, *tốc độ* và *giọng điệu* của âm thanh.

Khả năng TTS khác với khả năng tạo lời nói được cung cấp thông qua [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi). API này được thiết kế cho âm thanh tương tác, không có cấu trúc, cũng như đầu vào và đầu ra đa phương thức. Mặc dù Live API vượt trội trong các ngữ cảnh trò chuyện linh hoạt, nhưng TTS thông qua Gemini API được điều chỉnh cho phù hợp với những trường hợp yêu cầu đọc văn bản chính xác với khả năng kiểm soát chi tiết về phong cách và âm thanh, chẳng hạn như tạo podcast hoặc sách nói.

Hướng dẫn này cho bạn biết cách tạo âm thanh một người nói và nhiều người nói từ văn bản bằng [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi) (`gemini-3.8-flash-tts`) và [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi) (`gemini-3.8-flash-lite-tts`).

## Trước khi bắt đầu

Đảm bảo bạn sử dụng một mô hình TTS của Gemini có trong phần [Các mô hình được hỗ trợ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#supported-models).
Để có kết quả tối ưu, hãy xem phần [Thời điểm sử dụng mô hình nào](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#when-to-use-which-model) để chọn mô hình phù hợp nhất cho khối lượng công việc của bạn.

Bạn có thể thấy việc [kiểm thử các mô hình TTS của Gemini trong AI Studio](https://aistudio.google.com/generate-speech?hl=vi) là hữu ích trước khi bắt đầu xây dựng.

## TTS một người nói

Để chuyển văn bản thành âm thanh của một người nói bằng các mô hình TTS Gemini 3.8, hãy truyền bản chép lời nguyên văn trong `input`, đính kèm kiểu theo lượt bằng chú thích `speech_metadata` và định cấu hình giọng nói của bạn trong `generation_config.speech_config`. Bạn có thể chọn một giọng nói trong [Các lựa chọn về giọng nói](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#voices) được tạo sẵn, Thư viện giọng nói mở rộng (`GET /v1beta/voices`), [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi) tuỳ chỉnh (`voice_...`) hoặc [Nhân bản giọng nói](https://ai.google.dev/gemini-api/docs/voice-replication?hl=vi) (`voice_...` hoặc `voicekey_...` không trạng thái không bắt buộc).

Ví dụ này lưu âm thanh đầu ra WAV mặc định (`audio/wav`) từ mô hình trực tiếp vào một tệp:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-flash-tts-preview"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

Trong SDK Python và JavaScript, bạn có thể truy xuất dữ liệu âm thanh đã tạo bằng cách sử dụng thuộc tính tiện lợi `interaction.output_audio`. Thuộc tính này trả về khối âm thanh được tạo gần đây nhất (trong các phản hồi JSON REST thô, âm thanh được mã hoá base64 sẽ được lưu trữ trong `steps[].content[].data`). Để biết thông tin chi tiết về các thuộc tính tiện lợi, hãy xem phần [Tổng quan về các hoạt động tương tác](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi#convenience-properties).

## TTS nhiều người nói

Đối với đoạn hội thoại có nhiều người nói, hãy định cấu hình 2 người nói trong `speech_config.speakers` và truyền từng lượt nói dưới dạng một mục văn bản riêng biệt có chú thích `speech_metadata` chỉ định `speaker` và `style` ở cấp lượt nói (không bắt buộc). Sử dụng `"mode": "conversational"` để có nhịp độ trò chuyện tự nhiên:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [
            {
                "type": "text",
                "text": "How's it going today Jane?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                }],
            },
            {
                "type": "text",
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                }],
            },
        ],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": {
            "mode": "conversational",
            "speakers": [
                {"speaker": "Joe", "voice": "Puck"},
                {"speaker": "Jane", "voice": "Kore"},
            ],
        }
    },
)

with open("out.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [
            {
               type: 'text',
               text: "How's it going today Jane?",
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               }],
            },
            {
               type: 'text',
               text: 'Not too bad, how about you? Ready to test these new voices?',
               annotations: [{
                  type: 'speech_metadata',
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               }],
            },
         ],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: {
            mode: 'conversational',
            speakers: [
               { speaker: 'Joe', voice: 'Puck' },
               { speaker: 'Jane', voice: 'Kore' },
            ],
         },
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "encoding/binary"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func saveWaveFile(filename string, pcmData []byte) error {
    f, err := os.Create(filename)
    if err != nil {
        return err
    }
    defer f.Close()

    sampleRate := uint32(24000)
    numChannels := uint16(1)
    bitsPerSample := uint16(16)
    byteRate := sampleRate * uint32(numChannels) * uint32(bitsPerSample/8)
    blockAlign := numChannels * (bitsPerSample / 8)
    dataSize := uint32(len(pcmData))

    f.WriteString("RIFF")
    binary.Write(f, binary.LittleEndian, uint32(36+dataSize))
    f.WriteString("WAVEfmt ")
    binary.Write(f, binary.LittleEndian, uint32(16))
    binary.Write(f, binary.LittleEndian, uint16(1))
    binary.Write(f, binary.LittleEndian, numChannels)
    binary.Write(f, binary.LittleEndian, sampleRate)
    binary.Write(f, binary.LittleEndian, byteRate)
    binary.Write(f, binary.LittleEndian, blockAlign)
    binary.Write(f, binary.LittleEndian, bitsPerSample)
    f.WriteString("data")
    binary.Write(f, binary.LittleEndian, dataSize)
    _, err = f.Write(pcmData)
    return err
}

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := "TTS the following conversation between Joe and Jane:\n" +
        "Joe: How's it going today Jane?\n" +
        "Jane: Not too bad, how about you?"

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Joe"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Jane"), Voice: genai.Ptr("Puck")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-flash-tts-preview"),
            Input: interactions.NewInteractionsInput(prompt),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.OutputAudio != nil && res.Interaction.OutputAudio.Data != nil {
        pcmBytes, err := base64.StdEncoding.DecodeString(*res.Interaction.OutputAudio.Data)
        if err != nil {
            log.Fatal(err)
        }
        if err := saveWaveFile("out.wav", pcmBytes); err != nil {
            log.Fatal(err)
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [
        {
          "type": "text",
          "text": "How'\''s it going today Jane?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }]
        },
        {
          "type": "text",
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "annotations": [{
            "type": "speech_metadata",
            "speaker": "Jane",
            "style": "calm and relaxed"
          }]
        }
      ]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": {
        "mode": "conversational",
        "speakers": [
          { "speaker": "Joe", "voice": "Puck" },
          { "speaker": "Jane", "voice": "Kore" }
        ]
      }
    }
  }'
```

## Kiểm soát kiểu giọng nói bằng siêu dữ liệu và thẻ

Công nghệ chuyển văn bản sang lời nói (TTS) Gemini 3.8 coi trường `text` hoàn toàn là bản chép lời nguyên văn. Để kiểm soát việc truyền tải mà không cần đọc to chỉ dẫn sân khấu, hãy chia chỉ dẫn theo phạm vi:

- **Phân phối liên tục theo lượt (`speech_metadata.style`):** Đặt cảm xúc, kiểu phân phối, ngữ điệu, nhịp độ và âm lượng áp dụng cho toàn bộ lượt trong trường `style` (ví dụ: `"style": "whispered urgently"`, `"style": "out of breath"` hoặc `"style": "warm and enthusiastic"`).
- **Sự kiện tại một thời điểm (thẻ nội tuyến):** Đặt các đoạn giọng nói không phải lời nói hoặc khoảng dừng ngắn ngay trong bản chép lời bằng dấu ngoặc nhọn (ví dụ: `"Wait... <short pause> did you hear that? <sigh>"` hoặc `"Excuse me <cough> as I was saying..."`).

Hãy xem [Hướng dẫn tạo câu lệnh](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#prompting-guide) để biết các phương pháp hay nhất toàn diện.

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    transcriptRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "Generate a short transcript around 100 words that reads " +
                    "like it was clipped from a podcast by excited herpetologists. " +
                    "The hosts names are Dr. Anya and Liam.",
            ),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    var transcript string
    if transcriptRes.Interaction.OutputText != nil {
        transcript = *transcriptRes.Interaction.OutputText
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Speaker: genai.Ptr("Dr. Anya"), Voice: genai.Ptr("Kore")},
            {Speaker: genai.Ptr("Liam"), Voice: genai.Ptr("Puck")},
        })),
    }

    ttsRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-flash-tts-preview"),
            Input: interactions.NewInteractionsInput(transcript),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = ttsRes
}
```

## Tạo lời nói phát trực tuyến

Bạn có thể phát trực tuyến âm thanh được tạo khi âm thanh đó đang được tổng hợp bằng cách đặt `stream: true`. Không giống như các yêu cầu đơn phương (trả về một tệp WAV hoàn chỉnh có tiêu đề RIFF), **các yêu cầu truyền trực tuyến sẽ trả về các đoạn PCM tuyến tính 16 bit không có tiêu đề (`audio/l16`, 24 kHz, đơn âm) theo mặc định** để các đoạn âm thanh có thể được phát hoặc nối liên tục mà không cần tiêu đề vùng chứa.

### Python

```
import base64
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
    stream=True,
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "audio":
            audio_data = base64.b64decode(event.delta.data)
            # Process the audio chunk (e.g. play it or write to a file)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const stream = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: { type: 'audio' },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
      stream: true,
   });

   for await (const event of stream) {
      if (event.event_type === 'step.delta') {
         if (event.delta.type === 'audio') {
            const audioBuffer = Buffer.from(event.delta.data, 'base64');
            // Process the audio buffer
         }
      }
   }
}
await main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio"
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    },
    "stream": true
  }'
```

## Định dạng đầu ra âm thanh

Các mô hình TTS Gemini 3.8 sử dụng các định dạng âm thanh mặc định khác nhau, tuỳ thuộc vào việc yêu cầu là đơn phương hay truyền trực tuyến:

- **Yêu cầu một ngôi sao (`stream=False`):** Trả về âm thanh **WAV (`audio/wav`)** hoàn chỉnh có tiêu đề RIFF tiêu chuẩn (24 kHz, đơn âm, PCM có dấu 16 bit little-endian). Bạn có thể lưu trực tiếp các byte âm thanh đã giải mã vào tệp `.wav` mà không cần thêm tiêu đề WAV theo cách thủ công.
- **Yêu cầu phát trực tuyến (`stream=True`):** Trả về các đoạn **PCM tuyến tính thô không có tiêu đề (`audio/l16`)** (24 kHz, đơn âm, PCM little-endian có dấu 16 bit) theo mặc định để các đoạn có thể được phát trực tuyến hoặc nối liên tục mà không có tiêu đề vùng chứa trên mỗi đoạn.

Để yêu cầu tốc độ lấy mẫu hoặc phương thức mã hoá âm thanh khác, hãy định cấu hình `mime_type` và `sample_rate` (không bắt buộc) trong `response_format`:

| Định dạng | Giá trị `mime_type` | Mô tả |
| --- | --- | --- |
| **WAV** *(mặc định đơn nguyên)* | `"audio/wav"` | Tệp WAV chưa nén có tiêu đề RIFF (PCM 16 bit có dấu little-endian, đơn âm, mặc định là 24 kHz). Mặc định cho các yêu cầu đơn phương. |
| **PCM thô (L16)** *(mặc định khi phát trực tuyến)* | `"audio/l16"` | Âm thanh PCM tuyến tính 16 bit đã ký, không nén, không có tiêu đề, little-endian (24 kHz, đơn âm). Mặc định cho các yêu cầu phát trực tuyến. |
| **Mu-law** | `"audio/mulaw"` | Âm thanh được mã hoá theo chuẩn mu-law G.711 8 bit (thường được dùng trong hệ thống điện thoại/IVR ở Bắc Mỹ và Nhật Bản). |
| **A-law** | `"audio/alaw"` | Âm thanh được mã hoá theo luật A G.711 8 bit (thường dùng trong các hệ thống điện thoại quốc tế và của Châu Âu). |

Bạn cũng có thể chỉ định `sample_rate` theo đơn vị Hertz (ví dụ: `24000`, `16000` hoặc `8000`).

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": "Have a wonderful day!",
            "annotations": [{
                "type": "speech_metadata",
                "style": "cheerful and friendly",
            }],
        }],
    }],
    response_format={
        "type": "audio",
        "mime_type": "audio/l16",  # "audio/wav" (default), "audio/l16", "audio/mulaw", or "audio/alaw"
        "sample_rate": 24000,
    },
    generation_config={
        "speech_config": [
            {"voice": "Kore"},
        ]
    },
)

with open("out.pcm", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from 'node:fs';
import {GoogleGenAI} from '@google/genai';

async function main() {
   const client = new GoogleGenAI({});

   const interaction = await client.interactions.create({
      model: 'gemini-3.8-flash-tts',
      input: [{
         type: 'user_input',
         content: [{
            type: 'text',
            text: 'Have a wonderful day!',
            annotations: [{
               type: 'speech_metadata',
               style: 'cheerful and friendly',
            }],
         }],
      }],
      response_format: {
         type: 'audio',
         mime_type: 'audio/l16', // 'audio/wav' (default), 'audio/l16', 'audio/mulaw', or 'audio/alaw'
         sample_rate: 24000,
      },
      generation_config: {
         speech_config: [
            { voice: 'Kore' },
         ],
      },
   });

   const audioBuffer = Buffer.from(interaction.output_audio.data, 'base64');
   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    generationConfig := &interactions.GenerationConfig{
        SpeechConfig: genai.Ptr(interactions.NewSpeechConfigUnion([]interactions.SpeechConfig{
            {Voice: genai.Ptr("Kore")},
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.1-flash-tts-preview"),
            Input: interactions.NewInteractionsInput("Say cheerfully: Have a wonderful day!"),
            ResponseFormat: genai.Ptr(interactions.NewCreateModelInteractionResponseFormat(
                interactions.NewResponseFormat(interactions.AudioResponseFormat{}),
            )),
            GenerationConfig: generationConfig,
            Stream:           genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if audioDelta := stepDelta.GetDeltaAudio(); audioDelta != nil && audioDelta.Data != nil {
                audioData, err := base64.StdEncoding.DecodeString(*audioDelta.Data)
                if err != nil {
                    log.Fatal(err)
                }
                // Process the audio chunk (e.g. play it or write to a file)
                _ = audioData
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Have a wonderful day!",
        "annotations": [{
          "type": "speech_metadata",
          "style": "cheerful and friendly"
        }]
      }]
    }],
    "response_format": {
      "type": "audio",
      "mime_type": "audio/l16",
      "sample_rate": 24000
    },
    "generation_config": {
      "speech_config": [
        { "voice": "Kore" }
      ]
    }
  }'
```

## Lựa chọn giọng nói

Công nghệ TTS Gemini 3.8 hỗ trợ 4 cách chọn hoặc tạo giọng nói:

1. **Giọng nói được tạo sẵn trong Studio:** 30 giọng nói được tuyển chọn có trong bảng sau.
2. **Thư viện giọng nói mở rộng:** Hàng trăm giọng nói bổ sung thuộc nhiều ngôn ngữ, giọng điệu và nguyên mẫu nhân vật có thể truy cập bằng `client.voices.list()` (`GET /v1beta/voices`).
3. **[Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi):** Tạo một nhân vật giọng nói tuỳ chỉnh từ nội dung mô tả bằng ngôn ngữ tự nhiên trong [Google AI Studio](https://aistudio.google.com/generate-speech?hl=vi) hoặc sử dụng `POST /v1beta/voices` (`type="prompted"`, trả về một mã nhận dạng `voice_...` liên tục và bản xem trước `sample_audio` WAV trong `CreateVoice` và `GetVoice`).
4. **[Nhân bản giọng nói](https://ai.google.dev/gemini-api/docs/voice-replication?hl=vi):** Nhân bản giọng nói của người nói từ âm thanh tham chiếu và âm thanh có sự đồng ý trong [Google AI Studio](https://aistudio.google.com/generate-speech?hl=vi) hoặc bằng cách sử dụng `POST /v1beta/voices` (`type="replicated"`, `store=True` liên tục theo mặc định hoặc `store=False` không trạng thái tuỳ chọn).

### Hạn mức và TTL cho giọng nói tuỳ chỉnh

| Loại giọng nói | Chế độ lưu trữ | Hạn mức / giới hạn | Thời gian lưu giữ (TTL) |
| --- | --- | --- | --- |
| **Giọng nói có trạng thái** (`voice_...`, được nhắc hoặc sao chép) | `store=True` | **200 giọng nói cho mỗi dự án** (được chia sẻ giữa giọng nói được nhắc và giọng nói được sao chép) | **1 năm** |
| **Khoá thoại không trạng thái** (`voicekey_...`, được sao chép) | `store=False` | Do ứng dụng quản lý | **7 ngày** |

### Giọng nói tạo sẵn

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *Tươi sáng* | **Puck** – *Rộn ràng* | **Charon** – *Cung cấp nhiều thông tin* |
| **Kore** – *Firm* | **Fenrir** – *Dễ kích động* | **Leda** – *Trẻ trung* |
| **Orus** – *Firm* | **Aoede** – *Breezy* | **Callirrhoe** – *Dễ chịu* |
| **Autonoe** – *Sáng* | **Enceladus** – *Breathy* | **Iapetus** – *Clear* (Rõ ràng) |
| **Umbriel** – *Dễ tính* | **Algieba** – *Làm mịn* | **Despina** – *Smooth* |
| **Erinome** – *Clear* | **Algenib** – *Gravelly* | **Rasalgethi** – *Cung cấp nhiều thông tin* |
| **Laomedeia** – *Rộn ràng* | **Achernar** – *Dịu êm* | **Alnilam** – *Firm* |
| **Schedar** – *Even* | **Gacrux** – *Trưởng thành* | **Pulcherrima** – *Chuyển tiếp* |
| **Achird** – *Thân thiện* | **Zubenelgenubi** – *Thông thường* | **Vindemiatrix** – *Êm dịu* |
| **Sadachbia** – *Lively* | **Sadaltager** – *Hiểu biết* | **Sulafat** – *Ấm* |

### Thư viện giọng nói mở rộng và tính năng lọc

Ngoài 30 giọng nói nổi bật của phòng thu trong bảng trước đó, **Thư viện giọng nói mở rộng** còn cung cấp hàng trăm giọng nói khác theo ngôn ngữ, giọng địa phương, tính cách nhân vật và lĩnh vực. Bạn có thể duyệt xem, lọc và nghe thử toàn bộ Thư viện giọng nói một cách tương tác trong [Google AI Studio](https://aistudio.google.com/generate-speech?hl=vi) hoặc truy vấn theo phương thức lập trình bằng `client.voices.list()` (`GET /v1beta/voices`, sử dụng `google-genai` 2.25.0 trở lên / `@google/genai` 2.24.0 trở lên).

`ListVoices` sẽ trả về các giọng nói tuỳ chỉnh đã lưu (sắp xếp theo thứ tự mới nhất trước) rồi đến các giọng nói có sẵn trong danh mục khớp với tiêu chí lọc của bạn. Khi nhiều giá trị được truyền cho một bộ lọc danh sách, những giọng nói khớp với **bất kỳ** giá trị nào trong bộ lọc đó sẽ được trả về (`OR`), trong khi các tham số bộ lọc riêng biệt kết hợp với `AND`:

| Tham số | Loại | Mô tả |
| --- | --- | --- |
| `language_code` | `list[str]` | (Các) thẻ ngôn ngữ BCP-47 (ví dụ: `["en-US", "en-GB"]`). So khớp chính xác không phân biệt chữ hoa chữ thường. |
| `region_code` | `list[str]` | (Các) mã khu vực theo tiêu chuẩn ISO 3166-1 alpha-2 hoặc UN M.49 (ví dụ: `["US", "GB"]`). |
| `accent` | `list[str]` | (Các) phần mô tả giọng địa phương (ví dụ: `["American", "British"]`). |
| `gender` | `list[str]` | Giới tính thể hiện được cảm nhận (`"female"`, `"male"` hoặc `"neutral"`). |
| `pitch` | `list[str]` | Phân loại cao độ giọng nói (`"low"`, `"medium"` hoặc `"high"`). |
| `persona` | `list[str]` | Nhân vật hoặc nguyên mẫu giọng nói (ví dụ: `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` trong REST) | `list[str]` | Miền sử dụng tối ưu (ví dụ: `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` trong Python) | `list[str]` | Lọc theo nguồn giọng nói: `"prebuilt"`, `"prompted"` ([Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi)) hoặc `"replicated"` ([Nhân bản giọng nói](https://ai.google.dev/gemini-api/docs/voice-replication?hl=vi)). |
| `search` | `str` | Cụm từ tìm kiếm con bằng văn bản tự do được so khớp không phân biệt chữ hoa chữ thường với cả `display_name` và `description`. |
| `page_size` | `int` | Số lượng giọng nói tối đa được trả về trên mỗi trang (mặc định là `50`, tối đa là `1000`). |
| `page_token` | `str` | Mã thông báo từ `response.next_page_token` để tìm nạp trang kết quả tiếp theo. |

### Python

```
from google import genai

client = genai.Client()

# Filter the Voice Library by language, gender, pitch, domain context, and keyword
response = client.voices.list(
    language_code=["en-US", "en-GB"],
    gender=["female"],
    pitch=["medium", "low"],
    contexts=["Audiobook", "Conversational"],
    type_=["prebuilt"],
    search="warm",
    page_size=50,
)

for voice in response.voices or []:
    print(
        f"{voice.id} | {voice.display_name} ({voice.language_code},"
        f" {voice.accent}, {voice.gender}, pitch={voice.pitch}):"
        f" {voice.description}"
    )
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// Filter the Voice Library by language, gender, pitch, domain context, and keyword
const response = await ai.voices.list({
  language_code: ["en-US", "en-GB"],
  gender: ["female"],
  pitch: ["medium", "low"],
  contexts: ["Audiobook", "Conversational"],
  type: ["prebuilt"],
  search: "warm",
  page_size: 50,
});

for (const voice of response.voices ?? []) {
  console.log(
    `${voice.id} | ${voice.display_name} (${voice.language_code}, ${voice.accent}, ${voice.gender}, pitch=${voice.pitch}): ${voice.description}`
  );
}
```

### REST

```
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB" \
  --data-urlencode "gender=female" \
  --data-urlencode "pitch=medium" \
  --data-urlencode "context=Audiobook" \
  --data-urlencode "type=prebuilt" \
  --data-urlencode "search=warm" \
  --data-urlencode "page_size=50"
```

## Ngôn ngữ được hỗ trợ

Các mô hình TTS tự động phát hiện ngôn ngữ đầu vào.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi) (`gemini-3.8-flash-tts`) hỗ trợ **hơn 130 ngôn ngữ** và [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi) (`gemini-3.8-flash-lite-tts`) hỗ trợ **hơn 100 ngôn ngữ**:

| Ngôn ngữ | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Tiếng Aceh (Chữ Ả Rập) | ✔️ | ✔️ |
| Tiếng Hà Lan ở Nam Phi | ✔️ | ✔️ |
| Tiếng Akan | ✔️ | ✔️ |
| Tiếng Amhara | ✔️ | ✔️ |
| Tiếng Armenia | ✔️ | ✔️ |
| Tiếng Assam | ✔️ | ✔️ |
| Tiếng Awadhi | ✔️ | ✔️ |
| Chữ Bali | ✔️ | ✔️ |
| Tiếng Bangla | ✔️ | ✔️ |
| Banjar (chữ Ả Rập) | ✔️ | — |
| Banjar (chữ Latinh) | ✔️ | ✔️ |
| Tiếng Bashkir | ✔️ | — |
| Tiếng Basque | ✔️ | ✔️ |
| Tiếng Belarus | ✔️ | ✔️ |
| Tiếng Bemba | ✔️ | — |
| Tiếng Bhojpuri | ✔️ | ✔️ |
| Tiếng Bosnia | ✔️ | ✔️ |
| Chữ Bugin | ✔️ | ✔️ |
| Tiếng Bungary | ✔️ | ✔️ |
| Tiếng Miến Điện | ✔️ | — |
| Tiếng Quảng Đông | ✔️ | ✔️ |
| Tiếng Catalan | ✔️ | ✔️ |
| Tiếng Cebuano | ✔️ | ✔️ |
| Tiếng Trung Kurd | ✔️ | ✔️ |
| Tiếng Chhattisgarhi | ✔️ | ✔️ |
| Tiếng Trung (chữ Hán) | ✔️ | ✔️ |
| Tiếng Trung (chữ Hán phồn thể) | ✔️ | ✔️ |
| Tiếng Tatar Krym | ✔️ | — |
| Tiếng Croatia | ✔️ | ✔️ |
| Tiếng Séc | ✔️ | ✔️ |
| Tiếng Đan Mạch | ✔️ | ✔️ |
| Tiếng Hà Lan | ✔️ | ✔️ |
| Dyula | ✔️ | — |
| Tiếng Dzongkha | ✔️ | — |
| Tiếng Ả Rập | ✔️ | ✔️ |
| Tiếng Anh | ✔️ | ✔️ |
| Tiếng Estonia | ✔️ | ✔️ |
| Tiếng Philippines | ✔️ | ✔️ |
| Tiếng Phần Lan | ✔️ | — |
| Tiếng Pháp | ✔️ | ✔️ |
| Tiếng Galicia | ✔️ | ✔️ |
| Tiếng Ganda | ✔️ | ✔️ |
| Tiếng Gruzia | ✔️ | ✔️ |
| Tiếng Đức | ✔️ | ✔️ |
| Tiếng Hy Lạp | ✔️ | ✔️ |
| Tiếng Guarani | ✔️ | — |
| Tiếng Gujarat | ✔️ | ✔️ |
| Tiếng Creole ở Haiti | ✔️ | ✔️ |
| Tiếng Mông Cổ Khalkha | ✔️ | ✔️ |
| Tiếng Hausa | ✔️ | ✔️ |
| Tiếng Do Thái | ✔️ | ✔️ |
| Tiếng Hindi | ✔️ | ✔️ |
| Tiếng Hungary | ✔️ | ✔️ |
| Tiếng Iceland | ✔️ | ✔️ |
| Tiếng Igbo | ✔️ | — |
| Tiếng Iloko | ✔️ | ✔️ |
| Tiếng Indonesia | ✔️ | ✔️ |
| Tiếng Ba Tư của người Iran | ✔️ | ✔️ |
| Tiếng Ý | ✔️ | ✔️ |
| Tiếng Nhật | ✔️ | ✔️ |
| Tiếng Java | ✔️ | ✔️ |
| Tiếng Kabyle | ✔️ | — |
| Tiếng Kamba | ✔️ | ✔️ |
| Tiếng Kannada | ✔️ | ✔️ |
| Tiếng Kashmiri (Chữ Ả Rập) | ✔️ | ✔️ |
| Kashmiri (chữ Deva) | ✔️ | ✔️ |
| Tiếng Kazakh | ✔️ | ✔️ |
| Tiếng Khmer | ✔️ | ✔️ |
| Tiếng Kikuyu | ✔️ | ✔️ |
| Tiếng Kinyarwanda | ✔️ | ✔️ |
| Tiếng Kongo | ✔️ | ✔️ |
| Tiếng Hàn | ✔️ | ✔️ |
| Tiếng Kyrgyz | ✔️ | ✔️ |
| Tiếng Lào | ✔️ | ✔️ |
| Tiếng Latgale | ✔️ | — |
| Tiếng Lingala | ✔️ | ✔️ |
| Tiếng Lithuania | ✔️ | — |
| Tiếng Luxembourg | ✔️ | — |
| Tiếng Macedonia | ✔️ | ✔️ |
| Tiếng Magahi | ✔️ | ✔️ |
| Tiếng Maithili | ✔️ | ✔️ |
| Tiếng Malayalam | ✔️ | ✔️ |
| Tiếng Malta | ✔️ | ✔️ |
| Tiếng Manipur | ✔️ | ✔️ |
| Tiếng Marathi | ✔️ | ✔️ |
| Tiếng Minangkabau (chữ Ả Rập) | ✔️ | ✔️ |
| Tiếng Minangkabau (chữ Latinh) | ✔️ | — |
| Tiếng Mizo | ✔️ | ✔️ |
| Tiếng Nepal (ngôn ngữ riêng lẻ) | ✔️ | ✔️ |
| Tiếng Fulfulde ở Nigeria | ✔️ | ✔️ |
| Tiếng Azerbaijan miền Bắc | ✔️ | ✔️ |
| Tiếng Bắc Sotho | ✔️ | ✔️ |
| Tiếng Uzbek ở miền Bắc | ✔️ | ✔️ |
| Tiếng Bokmål ở Na Uy | ✔️ | ✔️ |
| Tiếng Na Uy Nynorsk | ✔️ | ✔️ |
| Tiếng Nyanja | ✔️ | ✔️ |
| Tiếng Occitan | ✔️ | — |
| Tiếng Odia (ngôn ngữ riêng lẻ) | ✔️ | ✔️ |
| Tiếng Pangasinan | ✔️ | — |
| Tiếng Ba Tư (Afghanistan) | ✔️ | ✔️ |
| Tiếng Ba Lan | ✔️ | ✔️ |
| Tiếng Bồ Đào Nha | ✔️ | ✔️ |
| Tiếng Punjab | ✔️ | ✔️ |
| Tiếng Rumani | ✔️ | ✔️ |
| Tiếng Nga | ✔️ | ✔️ |
| Tiếng Santali | ✔️ | ✔️ |
| Tiếng Serbia | ✔️ | ✔️ |
| Tiếng Sindh | ✔️ | — |
| Tiếng Sinhala | ✔️ | ✔️ |
| Tiếng Slovak | ✔️ | ✔️ |
| Tiếng Slovenia | ✔️ | — |
| Tiếng Somali | ✔️ | — |
| Tiếng Azerbaijan miền Nam | ✔️ | ✔️ |
| Tiếng Pashto miền Nam | ✔️ | ✔️ |
| Tiếng Nam Sotho | ✔️ | — |
| Tiếng Tây Ban Nha | ✔️ | ✔️ |
| Tiếng Ả Rập chuẩn (chữ Ả Rập) | ✔️ | ✔️ |
| Tiếng Ả Rập chuẩn (chữ Latinh) | ✔️ | ✔️ |
| Tiếng Latvia tiêu chuẩn | ✔️ | ✔️ |
| Tiếng Mã Lai chuẩn | ✔️ | ✔️ |
| Tiếng Swahili (ngôn ngữ riêng lẻ) | ✔️ | — |
| Tiếng Swati | ✔️ | — |
| Tiếng Thuỵ Điển | ✔️ | — |
| Tiếng Tajik | ✔️ | — |
| Tiếng Tamil | ✔️ | ✔️ |
| Tiếng Telugu | ✔️ | ✔️ |
| Tiếng Thái | ✔️ | — |
| Tiếng Tigrinya | ✔️ | — |
| Tiếng Albania ở vùng Tosk | ✔️ | — |
| Tiếng Thổ Nhĩ Kỳ | ✔️ | ✔️ |
| Tiếng Duy Ngô Nhĩ | ✔️ | — |
| Tiếng Việt | ✔️ | ✔️ |

## Mô hình được hỗ trợ

| Mô hình | Loa đơn | Nhiều loa | Thiết kế giọng nói | Nhân bản giọng nói |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Bản xem trước tính năng chuyển văn bản sang lời nói của Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=vi) | ✔️ | ✔️ | — | — |
| [TTS xem trước Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=vi) | ✔️ | ✔️ | — | — |

### Trường hợp sử dụng mô hình nào

Cả hai mô hình TTS Gemini 3.8 đều có cùng một lược đồ API và định dạng câu lệnh, cho phép bạn chuyển đổi giữa chúng chỉ bằng một thay đổi về thông số:

- **Sử dụng [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi)
  (`gemini-3.8-flash-tts`)** khi độ trung thực âm thanh tối đa, diễn xuất tinh tế và khả năng kiểm soát biểu cảm là ưu tiên hàng đầu. Đây là lựa chọn lý tưởng cho công việc sáng tạo ở cấp độ chuyên nghiệp, đoạn hội thoại phức tạp của nhiều người nói, các thẻ có nhiều đoạn lời thoại, cách phát âm khó, phương ngữ của khu vực hoặc nhóm thiểu số và những đoạn tường thuật dài đòi hỏi giọng nói và âm thanh môi trường ổn định.
- **Sử dụng [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi)
  (`gemini-3.8-flash-lite-tts`)** làm công cụ thay thế nhanh chóng, tiết kiệm chi phí cho `gemini-3.1-flash-tts-preview`. Nền tảng này được tối ưu hoá cho hoạt động sản xuất hàng loạt với số lượng lớn, các tầng tác nhân giọng nói đàm thoại, các tính năng đọc to, khả năng nhân bản giọng nói đáng tin cậy và lời nói hằng ngày của một người nói bằng các ngôn ngữ chính.

### Hướng dẫn di chuyển

Nếu bạn đang di chuyển từ `gemini-3.1-flash-tts-preview` hoặc các mô hình TTS Gemini cũ hơn sang TTS Gemini 3.8:

1. **Di chuyển chỉ dẫn theo từng lượt vào `speech_metadata`:** TTS Gemini 3.8 coi văn bản đầu vào hoàn toàn là bản chép lời nguyên văn. Di chuyển hướng dẫn phân phối liên tục (`style`, chẳng hạn như `"whispering"`, `"out of breath"` hoặc `"speaking slowly"`) và nhãn người nói (`speaker`) vào chú thích có cấu trúc `speech_metadata` thay vì nhúng chỉ dẫn sân khấu vào văn bản bản chép lời.
2. **Chỉ sử dụng thẻ nội tuyến dấu ngoặc nhọn cho các sự kiện âm thanh tại một thời điểm:** Giữ các đoạn âm thanh không phải lời nói và khoảng dừng ngắn trong bản chép lời bằng dấu ngoặc nhọn (chẳng hạn như `<laugh>`, `<sigh>`, `<cough>`, `<breath>` hoặc `<short pause>`). Tránh thẻ hiệu ứng âm thanh (chẳng hạn như tiếng vỗ tay hoặc tiếng động mạnh) và đặt kiểu truyền tải trong `speech_metadata.style`.
3. **Chỉ định `speaker` ở mỗi lượt trong yêu cầu có nhiều người nói:** Mỗi lượt trong yêu cầu có nhiều người nói phải bao gồm rõ ràng `speaker` bên trong `speech_metadata` khớp với một trong những người nói đã định cấu hình.
4. **Thiết kế các nhân vật giả định trước bằng tính năng Thiết kế giọng nói:** Thay thế các khối `"Audio Profile"` hoặc `"Director's Notes"` có nhiều đoạn bằng giọng nói tuỳ chỉnh được tạo trong [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi), sau đó truyền mã nhận dạng `voice_...` đó qua các yêu cầu TTS của bạn với chuỗi `style` tối thiểu hoặc trống.
5. **Tài khoản cho đầu ra WAV mặc định (`audio/wav`) trên các yêu cầu đơn phương:** Không giống như `gemini-3.1-flash-tts-preview` và các mô hình TTS trước đó (trả về PCM thô không có tiêu đề `audio/l16` theo mặc định), Gemini 3.8 TTS trả về âm thanh WAV (`audio/wav`) có tiêu đề RIFF tiêu chuẩn theo mặc định cho các yêu cầu đơn phương.
   - Nếu trước đây mã của bạn đã bao bọc các byte PCM thô trong một tiêu đề WAV (ví dụ: sử dụng mô-đun `wave` của Python hoặc `ffmpeg`), hãy xoá trình bao bọc tiêu đề theo cách thủ công và ghi trực tiếp các byte được trả về vào tệp `.wav`.
   - Nếu quy trình của bạn yêu cầu âm thanh PCM thô không có tiêu đề, mu-law hoặc A-law, hãy đặt `response_format` một cách rõ ràng thành `"audio/l16"`, `"audio/mulaw"` hoặc `"audio/alaw"`. Xem [Định dạng đầu ra âm thanh](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#audio-output-formats).

## Hướng dẫn đặt câu lệnh

Các mô hình TTS Gemini 3.8 coi văn bản đầu vào hoàn toàn là **bản chép lời nguyên văn**.
Không giống như các mô hình xem trước trước đây, trong đó chỉ dẫn sân khấu được nhúng trong văn bản thuần tuý, TTS Gemini 3.8 tách biệt chỉ dẫn duy trì ở cấp lượt (`speech_metadata`) với thẻ thoại nội dòng tại một thời điểm.

### Trường kiểu so với thẻ nội tuyến

Chia chỉ dẫn về hiệu suất theo phạm vi:

- **Mức độ chuyển lời (`speech_metadata.style`):** Đặt các thuộc tính chuyển lời bền vững (chẳng hạn như cảm xúc, ngữ điệu, tốc độ tổng thể hoặc phong cách chuyển lời (như `"whispering"`, `"out of breath"`, `"muttering"` hoặc `"sarcastic"`)) vào trường `style` của `speech_metadata`. Để tạo một nhân vật và hiệu suất ổn định qua các lượt, hãy thiết kế nhân vật trước trong [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi) và chỉ sử dụng `style` cho các tinh chỉnh không bắt buộc ở cấp lượt.
- **Sự kiện tại một thời điểm (thẻ nội tuyến):** Đặt các đoạn âm thanh không phải lời nói, tiếng thở hoặc khoảng dừng ngắn vào nội tuyến bên trong bản chép lời bằng dấu ngoặc nhọn (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Sử dụng dấu ngoặc nhọn (`<...>`) để có chất lượng âm thanh cao nhất và chỉ sử dụng giọng nói của con người thay vì hiệu ứng âm thanh không phải giọng nói.

| Phạm vi | Vị trí đặt | Ví dụ |
| --- | --- | --- |
| **Cấp lượt** (duy trì trong suốt lượt) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Tại một thời điểm cụ thể** (xảy ra tại một từ cụ thể) | Nội tuyến trong `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Nhịp độ và khoảng dừng

Bạn có thể kiểm soát nhịp điệu và khoảng lặng ở 3 mức độ chi tiết:

- **Dấu chấm câu và dấu ba chấm:** Sử dụng dấu phẩy, dấu gạch ngang (`--`) và dấu ba chấm (`...`) để tạo cảm giác do dự tự nhiên trong cuộc trò chuyện.
- **Thẻ tạm dừng cùng dòng:** Chèn `<short pause>` hoặc `<long pause>` vào đúng vị trí trong kịch bản mà người nói cần tạm dừng:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Tốc độ theo lượt:** Đặt `"style": "speaking rapidly"` hoặc `"style": "speaking slowly"` trong `speech_metadata` để kiểm soát tốc độ nói trong toàn bộ lượt.

### Ngữ điệu và cao độ

Sử dụng **`speech_metadata.style`** để kiểm soát ngữ điệu, cao độ và biến tố trong một lượt lời (ví dụ: `"style": "high pitch, cheerful and excited inflection"` hoặc `"style": "monotone and flat"`). Nếu cảm xúc hoặc ngữ điệu thay đổi giữa cuộc trò chuyện, hãy chia kịch bản thành các lượt lời riêng biệt với các giá trị `style` riêng biệt cho mỗi lượt lời.

### Điểm nhấn

Viết hoa một số từ trong bản chép lời, kết hợp với dấu câu và thẻ thanh nhạc nội dòng để nhấn giọng tự nhiên vào các từ khoá:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Tiếng bật âm và âm thanh không phải lời nói

Đặt các âm thanh không phải lời nói của con người vào dòng bằng dấu ngoặc nhọn (`<...>`) tại đúng thời điểm mà âm thanh đó xuất hiện. Các thẻ giọng nói nên dùng bao gồm:

|  |  |  |  |
| --- | --- | --- | --- |
| `<argh>` | `<breath>` | `<heavy breath>` | `<exhales>` |
| `<cackle>` | `<cheer>` | `<chuckle>`/`<chuckles>` | `<cough>` |
| `<cry>` | `<gasp>` | `<giggle>` | `<groan>` |
| `<growl>` | `<grunt>` | `<grr>` | `<hiss>` |
| `<laugh>`/`<laughter>` | `<moan>` | `<pant>` | `<pff>`/`<phew>` |
| `<scream>` | `<shout>` | `<shriek>` | `<sigh>`/`<sighs>` |
| `<sneeze>` | `<snicker>` | `<snort>` | `<sob>` |
| `<throat-clearing>` | `<tsk>` | `<whimper>` | `<whispers>`/`<whispering>` |
| `<yawn>` | `<short pause>` | `<long pause>` |  |

### Kênh phụ và lời nói chồng chéo

Trong đoạn hội thoại có nhiều người nói, hãy đặt các phản ứng của người nghe trong dấu gạch dọc (`|reaction|`) trong lượt lời của người nói để tạo kênh liên lạc bí mật tự nhiên hoặc lời nói chồng chéo mà không bị ngắt thành một lượt lời riêng cho mỗi phản ứng.

- **Trao đổi qua kênh phụ trong thời gian ngắn:** Lồng ghép phản ứng ngắn của người nghe (`|oh hmm|`, `|oh really?|`, `|absolutely|`) trong lượt nói của người đang nói:
  - **Lượt 1 (Người nói A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Lượt 2 (Người nói B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Lượt 3 (Người nói A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Lời nói chồng chéo và xen kẽ:** Sử dụng nhiều đoạn dấu gạch đứng để mô phỏng lời nói đồng thời hoặc xen kẽ giữa hai người nói (phù hợp nhất với `gemini-3.8-flash-tts`):
  - **Đếm ngược/hát đồng thanh cùng lúc:** `"Let's surprise him on three |ok| ready?"` rồi đến `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Full speaker overlap** (Chồng chéo hoàn toàn giữa các diễn giả): `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Tính nhất quán giữa các thế hệ và những điều cần tránh

Hãy làm theo các nguyên tắc sau để duy trì giọng nói ổn định trong suốt cuộc trò chuyện:

- **Thiết kế nhân vật đại diện ngay từ đầu trong Thiết kế giọng nói thay vì các khối kiểu dài:**
  Các đoạn văn `"Audio Profile"` dạng dài và nhiều dấu đầu dòng `"Director's Notes"` được chuyển từ các mô hình trước đó là nguyên nhân phổ biến nhất gây ra sự thay đổi về giọng nói.
  Hãy sử dụng trực giác sáng tạo đó ngay từ đầu trong [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi) để tạo ra một `voice_...` nhân vật tuỳ chỉnh lâu dài, sau đó truyền mã nhận dạng giọng nói đó qua các lệnh gọi TTS.
- **Dựa vào giọng nói tham chiếu để đảm bảo tính ổn định (bỏ qua các chỉ dẫn meta):**
  Các mô hình TTS 3.8 của Gemini được huấn luyện để ưu tiên giọng nói tham chiếu.
  Không được đưa ra hướng dẫn yêu cầu mô hình giữ giọng nói ổn định (chẳng hạn như `"do not switch speaker identity"` hoặc `"maintain identical timbre"`) – văn bản câu lệnh bổ sung sẽ làm tăng độ lệch. Loại bỏ những hướng dẫn không cần thiết về phong cách và để mô hình thay đổi một cách tự nhiên xung quanh điểm ổn định do giọng nói tham khảo cung cấp.
- **Đừng cố gắng thay đổi các đặc điểm không thay đổi của người nói trong `style`:** Tránh đưa tuổi, giới tính, tên hoặc các thay đổi về giọng điệu vĩnh viễn vào `speech_metadata.style`.
  Thay vào đó, hãy chọn một giọng nói theo khu vực trong Thư viện giọng nói mở rộng hoặc tạo một giọng nói bằng tính năng [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi).

### Quy trình làm việc được đề xuất

1. **Tạo nhân vật một lần:** Tạo nhân vật trong phần [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi) hoặc chọn một giọng nói theo khu vực trong Thư viện giọng nói mở rộng phù hợp với ngôn ngữ đích và tính cách của bạn.
2. **Viết bản chép lời tự nhiên như lời nói, có cả những đoạn ngắt lời:** Để đạt được mức độ tự nhiên cao nhất, hãy viết `text` dưới dạng bản chép lời thực tế như lời nói, bao gồm cả những đoạn ngắt lời và do dự tự nhiên trong cuộc trò chuyện (ví dụ: `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Trước tiên, hãy kiểm thử TTS thông thường:** Trước tiên, hãy tổng hợp bản chép lời của bạn bằng một trường `style` trống – hầu hết các yêu cầu đều không cần hướng dẫn `style`.
4. **Chỉ thêm câu lệnh ngắn `style` để tinh chỉnh:** Chỉ thêm một chuỗi `style` ngắn gọn (chẳng hạn như `"casual, friendly"` hoặc `"muttering, then reassuring"`) cho những lượt cần điều chỉnh cụ thể về cách phân phối và sử dụng lại chính xác chuỗi ngắn đó trong các lượt khi bạn muốn có một đường cơ sở nhất quán.

### Hội thoại nhiều lượt và tác nhân thoại

Khi xây dựng các tác nhân giọng nói đàm thoại theo thời gian thực hoặc các ứng dụng nhiều lượt tương tác:

- Thực hiện **một lệnh gọi TTS cho mỗi lượt** khi các đoạn văn bản LLM đến.
- Cho phép `voice` đã định cấu hình (được tạo sẵn, được thiết kế `voice_...` hoặc được sao chép `voice_...` / `voicekey_...`) mang danh tính của người nói qua các lượt trò chuyện – không bao giờ gửi lại một nhân vật dài ở mỗi lượt.
- Để trống trường `style` cho mỗi lượt hoặc gửi một chuỗi hằng số ngắn (chẳng hạn như `"casual, friendly"`) cho toàn bộ cuộc trò chuyện.
- Chia câu trả lời dài của trợ lý thành các lượt ngắn hơn thay vì sử dụng các câu lệnh có phong cách mạnh mẽ hơn.

## Các điểm hạn chế

- Các mô hình TTS chấp nhận đầu vào chỉ có văn bản và tạo ra đầu ra chỉ có âm thanh.
- Tính năng tạo nhiều người nói bằng một yêu cầu (`speech_config.speakers`) hỗ trợ tối đa 2 người nói bằng giọng nói được tạo sẵn. Để kết hợp giọng nói được thiết kế riêng (`voice_...`) hoặc giọng nói được sao chép (`voice_...` / `voicekey_...`) trong đoạn hội thoại có nhiều nhân vật, hãy tổng hợp từng lượt lời của người nói một cách riêng lẻ.
  Vì các yêu cầu đơn phương trả về `audio/wav` với tiêu đề RIFF 44 byte theo mặc định, hãy yêu cầu PCM thô (`{"type": "audio", "mime_type": "audio/l16"}`) hoặc loại bỏ tiêu đề WAV khỏi mỗi lượt trước khi nối các khung âm thanh PCM 24 kHz.
- **Hạn mức bộ nhớ và TTL cho giọng nói tuỳ chỉnh:**
  - **Giọng nói có trạng thái (`store=True`, được nhắc hoặc sao chép):** Tối đa **200 giọng nói cho mỗi dự án** với **TTL (thời gian tồn tại) là 1 năm**.
  - **Khoá thoại không trạng thái (`store=False`, `voicekey_...`):** **TTL 7 ngày** (thời gian tồn tại).
- Xem phần [Ngôn ngữ được hỗ trợ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#languages) để biết phạm vi hỗ trợ ngôn ngữ.

## Bước tiếp theo

- Tạo nhân vật ảo có giọng nói tuỳ chỉnh bằng ngôn ngữ tự nhiên thông qua tính năng [Thiết kế giọng nói](https://ai.google.dev/gemini-api/docs/voice-design?hl=vi).
- Nhân bản giọng nói của một người nói hiện có trong tính năng [Nhân bản giọng nói](https://ai.google.dev/gemini-api/docs/voice-replication?hl=vi).
- So sánh thông số kỹ thuật của mô hình trên các trang mô hình [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=vi) và [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=vi).
- Khám phá âm thanh tương tác hai chiều bằng [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-09-24 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-09-24 UTC."],[],[]]
