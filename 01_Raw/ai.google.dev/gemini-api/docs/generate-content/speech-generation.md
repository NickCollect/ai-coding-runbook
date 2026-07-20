---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=vi
fetched_at: 2026-07-20T04:38:36.224046+00:00
title: "T\u1ea1o l\u1eddi n\u00f3i t\u1eeb v\u0103n b\u1ea3n (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo lời nói từ văn bản (TTS)

Gemini API có thể chuyển đổi văn bản đầu vào thành âm thanh của một hoặc nhiều người nói bằng cách sử dụng các chức năng tạo văn bản thành lời nói (TTS) của Gemini.
Bạn có thể *[kiểm soát](#controllable)* quá trình tạo văn bản sang lời nói (TTS). Tức là bạn có thể sử dụng ngôn ngữ tự nhiên để cấu trúc các lượt tương tác và hướng dẫn *phong cách*, *giọng*, *tốc độ* và *giọng điệu* của âm thanh.

[Dùng thử trong Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=vi)

Khả năng TTS khác với khả năng tạo lời nói được cung cấp thông qua [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi). API này được thiết kế cho âm thanh tương tác, không có cấu trúc, cũng như đầu vào và đầu ra đa phương thức. Mặc dù Live API vượt trội trong các ngữ cảnh trò chuyện linh hoạt, nhưng TTS thông qua Gemini API được điều chỉnh cho phù hợp với những trường hợp yêu cầu đọc chính xác văn bản với khả năng kiểm soát chi tiết về phong cách và âm thanh, chẳng hạn như tạo podcast hoặc sách nói.

Hướng dẫn này trình bày cách tạo âm thanh một người nói và nhiều người nói từ văn bản.

## Trước khi bắt đầu

Đảm bảo bạn sử dụng một biến thể mô hình Gemini có các chức năng chuyển văn bản sang lời nói (TTS) của Gemini, như được liệt kê trong phần [Các mô hình được hỗ trợ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#supported-models). Để có kết quả tối ưu, hãy cân nhắc xem mô hình nào phù hợp nhất với trường hợp sử dụng cụ thể của bạn.

Bạn nên [kiểm thử các mô hình TTS của Gemini trong AI Studio](https://aistudio.google.com/generate-speech?hl=vi) trước khi bắt đầu xây dựng.

## TTS một người nói

Để chuyển văn bản thành âm thanh của một người nói, hãy đặt phương thức phản hồi thành "audio" và truyền một đối tượng `SpeechConfig` có `VoiceConfig` được đặt.
Bạn sẽ cần chọn tên giọng nói trong số các [giọng nói đầu ra](#voices) được tạo sẵn.

Ví dụ này lưu âm thanh đầu ra từ mô hình vào một tệp sóng:

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        },
        "model": "gemini-3.1-flash-tts-preview",
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode >out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## TTS nhiều giọng nói

Đối với âm thanh nhiều loa, bạn sẽ cần một đối tượng `MultiSpeakerVoiceConfig` có mỗi loa (tối đa 2) được định cấu hình dưới dạng `SpeakerVoiceConfig`.
Bạn sẽ cần xác định từng `speaker` bằng các tên giống nhau được dùng trong [lệnh](#controllable):

### Python

```
from google import genai
from google.genai import types
import wave

# Set up the wave file to save the output:
def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
   with wave.open(filename, "wb") as wf:
      wf.setnchannels(channels)
      wf.setsampwidth(sample_width)
      wf.setframerate(rate)
      wf.writeframes(pcm)

client = genai.Client()

prompt = """TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?"""

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=prompt,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Joe',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Jane',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name='out.wav'
wave_file(file_name, data) # Saves the file to current directory
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import wav from 'wav';

async function saveWaveFile(
   filename,
   pcmData,
   channels = 1,
   rate = 24000,
   sampleWidth = 2,
) {
   return new Promise((resolve, reject) => {
      const writer = new wav.FileWriter(filename, {
            channels,
            sampleRate: rate,
            bitDepth: sampleWidth * 8,
      });

      writer.on('finish', resolve);
      writer.on('error', reject);

      writer.write(pcmData);
      writer.end();
   });
}

async function main() {
   const ai = new GoogleGenAI({});

   const prompt = `TTS the following conversation between Joe and Jane:
         Joe: How's it going today Jane?
         Jane: Not too bad, how about you?`;

   const response = await ai.models.generateContent({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: prompt }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               multiSpeakerVoiceConfig: {
                  speakerVoiceConfigs: [
                        {
                           speaker: 'Joe',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Kore' }
                           }
                        },
                        {
                           speaker: 'Jane',
                           voiceConfig: {
                              prebuiltVoiceConfig: { voiceName: 'Puck' }
                           }
                        }
                  ]
               }
            }
      }
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   const fileName = 'out.wav';
   await saveWaveFile(fileName, audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
  "contents": [{
    "parts":[{
      "text": "TTS the following conversation between Joe and Jane:
                Joe: Hows it going today Jane?
                Jane: Not too bad, how about you?"
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [{
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }, {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }]
      }
    }
  },
  "model": "gemini-3.1-flash-tts-preview",
}' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
    base64 --decode > out.pcm
# You may need to install ffmpeg.
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

## Kiểm soát kiểu giọng nói bằng câu lệnh

Bạn có thể kiểm soát phong cách, giọng điệu, ngữ điệu và tốc độ bằng cách sử dụng câu lệnh bằng ngôn ngữ tự nhiên hoặc [thẻ âm thanh](#transcript-tags) cho cả TTS một người nói và nhiều người nói.
Ví dụ: trong câu lệnh có một người nói, bạn có thể nói:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

Trong câu lệnh có nhiều người nói, hãy cung cấp cho mô hình tên của từng người nói và bản chép lời tương ứng. Bạn cũng có thể hướng dẫn riêng cho từng người nói:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Hãy thử dùng một [lựa chọn giọng nói](#voices) phù hợp với phong cách hoặc cảm xúc mà bạn muốn truyền tải để nhấn mạnh hơn nữa. Ví dụ: trong câu lệnh trước, hơi thở của *Enceladus* có thể nhấn mạnh trạng thái "mệt mỏi" và "buồn chán", trong khi giọng điệu vui vẻ của *Puck* có thể bổ sung cho trạng thái "hào hứng" và "vui vẻ".

## Tạo câu lệnh để chuyển đổi thành âm thanh

Các mô hình TTS chỉ xuất âm thanh, nhưng bạn có thể dùng [các mô hình khác](https://ai.google.dev/gemini-api/docs/models?hl=vi) để tạo bản chép lời trước, sau đó truyền bản chép lời đó đến mô hình TTS để đọc to.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.5-flash",
   contents="""Generate a short transcript around 100 words that reads
            like it was clipped from a podcast by excited herpetologists.
            The hosts names are Dr. Anya and Liam.""").text

response = client.models.generate_content(
   model="gemini-3.1-flash-tts-preview",
   contents=transcript,
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
            speaker_voice_configs=[
               types.SpeakerVoiceConfig(
                  speaker='Dr. Anya',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Kore',
                     )
                  )
               ),
               types.SpeakerVoiceConfig(
                  speaker='Liam',
                  voice_config=types.VoiceConfig(
                     prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Puck',
                     )
                  )
               ),
            ]
         )
      )
   )
)

# ...Code to handle audio output
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

const transcript = await ai.models.generateContent({
   model: "gemini-3.5-flash",
   contents: "Generate a short transcript around 100 words that reads like it was clipped from a podcast by excited herpetologists. The hosts names are Dr. Anya and Liam.",
   })

const response = await ai.models.generateContent({
   model: "gemini-3.1-flash-tts-preview",
   contents: transcript,
   config: {
      responseModalities: ['AUDIO'],
      speechConfig: {
         multiSpeakerVoiceConfig: {
            speakerVoiceConfigs: [
                   {
                     speaker: "Dr. Anya",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Kore"},
                     }
                  },
                  {
                     speaker: "Liam",
                     voiceConfig: {
                        prebuiltVoiceConfig: {voiceName: "Puck"},
                    }
                  }
                ]
              }
            }
      }
  });
}
// ..JavaScript code for exporting .wav file for output audio

await main();
```

## Lựa chọn giọng nói

Các mô hình TTS hỗ trợ 30 lựa chọn giọng nói sau đây trong trường `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *Tươi sáng* | **Puck** – *Rộn ràng* | **Charon** – *Cung cấp nhiều thông tin* |
| **Kore** – *Firm* | **Fenrir** – *Dễ kích động* | **Leda** – *Trẻ trung* |
| **Orus** – *Firm* | **Aoede** – *Breezy* | **Callirrhoe** – *Dễ chịu* |
| **Autonoe** – *Sáng* | **Enceladus** – *Breathy* | **Iapetus** – *Rõ ràng* |
| **Umbriel** – *Dễ tính* | **Algieba** – *Làm mịn* | **Despina** – *Smooth* |
| **Erinome** – *Clear* | **Algenib** – *Khàn* | **Rasalgethi** – *Cung cấp nhiều thông tin* |
| **Laomedeia** – *Rộn ràng* | **Achernar** – *Dịu êm* | **Alnilam** – *Firm* |
| **Schedar** – *Even* | **Gacrux** – *Người trưởng thành* | **Pulcherrima** – *Chuyển tiếp* |
| **Achird** – *Thân thiện* | **Zubenelgenubi** – *Bình thường* | **Vindemiatrix** – *Dịu dàng* |
| **Sadachbia** – *Lively* | **Sadaltager** – *Hiểu biết* | **Sulafat** – *Ấm* |

Bạn có thể nghe tất cả các lựa chọn về giọng nói trong [AI Studio](https://aistudio.google.com/generate-speech?hl=vi).

## Ngôn ngữ được hỗ trợ

Các mô hình TTS tự động phát hiện ngôn ngữ đầu vào. Các ngôn ngữ sau đây được hỗ trợ:

| Ngôn ngữ | Mã BCP-47 | Ngôn ngữ | Mã BCP-47 |
| --- | --- | --- | --- |
| Tiếng Ả Rập | ar | Tiếng Philippines | fil |
| Tiếng Bangla | bn | Tiếng Phần Lan | fi |
| Tiếng Hà Lan | nl | Tiếng Galicia | gl |
| Tiếng Anh | vi | Tiếng Gruzia | ka |
| Tiếng Pháp | fr | Tiếng Hy Lạp | el |
| Tiếng Đức | de | Tiếng Gujarat | gu |
| Tiếng Hindi | hi | Tiếng Creole ở Haiti | ht |
| Tiếng Indonesia | id | Tiếng Do Thái | hi hi |
| Tiếng Ý | it | Tiếng Hungary | hu |
| Tiếng Nhật | ja | Tiếng Iceland | is |
| Tiếng Hàn | ko | Tiếng Java | jv |
| Tiếng Marathi | mr | Tiếng Kannada | kn |
| Tiếng Ba Lan | pl | Tiếng Konkani | kok |
| Tiếng Bồ Đào Nha | pt | Tiếng Lào | lo |
| Tiếng Rumani | ro | Latinh | la |
| Tiếng Nga | ru | Tiếng Latvia | lv |
| Tiếng Tây Ban Nha | es | Tiếng Lithuania | lt |
| Tiếng Tamil | ta | Tiếng Luxembourg | lb |
| Tiếng Telugu | te | Tiếng Macedonia | mk |
| Tiếng Thái | th | Tiếng Maithili | mai |
| Tiếng Thổ Nhĩ Kỳ | tr | Tiếng Malagasy | mg |
| Tiếng Ukraina | uk | Tiếng Malay | ms |
| Tiếng Việt | vi | Tiếng Malayalam | ml |
| Tiếng Hà Lan ở Nam Phi | af | Tiếng Mông Cổ | mn |
| Tiếng Albania | sq | Tiếng Nepal | ne |
| Tiếng Amhara | sáng | Tiếng Na Uy, Bokmål | nb |
| Tiếng Armenia | hy | Tiếng Na Uy, Nynorsk | nn |
| Tiếng Azerbaijan | az | Tiếng Odia | hoặc |
| Tiếng Basque | eu | Tiếng Pashto | ps |
| Tiếng Belarus | be | Persian | fa |
| Tiếng Bungary | bg | Tiếng Punjab | pa |
| Tiếng Myanmar | my | Tiếng Serbia | sr |
| Tiếng Catalan | ca | Tiếng Sindh | sd |
| Tiếng Cebuano | ceb | Tiếng Sinhala | si |
| Tiếng Trung, tiếng Quan thoại | cmn | Tiếng Slovak | sk |
| Croatian | giờ | Tiếng Slovenia | sl |
| Tiếng Séc | cs | Tiếng Swahili | sw |
| Tiếng Đan Mạch | da | Tiếng Thuỵ Điển | sv |
| Tiếng Estonia | et | Tiếng Urdu | ur |

## Mô hình được hỗ trợ

| Mô hình | Loa đơn | Nhiều người nói |
| --- | --- | --- |
| [Bản xem trước tính năng chuyển văn bản sang lời nói của Gemini 3.1 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=vi) | ✔️ | ✔️ |
| [Bản xem trước Gemini 2.5 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=vi) | ✔️ | ✔️ |
| [TTS của Gemini 2.5 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=vi) | ✔️ | ✔️ |

## Hướng dẫn đặt câu lệnh

Mô hình **Tạo âm thanh gốc cho tính năng Chuyển văn bản sang lời nói (TTS) của Gemini** khác biệt với các mô hình TTS truyền thống bằng cách sử dụng một mô hình ngôn ngữ lớn, ***không chỉ biết nội dung cần nói mà còn biết cách nói***.

Ngay từ đầu, mô hình sẽ diễn giải bản chép lời một cách tự nhiên và xác định cách bạn nên truyền tải lời nói. Bản chép lời đơn giản mà không cần thêm câu lệnh nghe có vẻ tự nhiên. Tuy nhiên, Gemini TTS cũng đi kèm với các công cụ mà bạn có thể dùng để điều hướng.

Mục đích của hướng dẫn này là đưa ra hướng dẫn cơ bản và khơi gợi ý tưởng khi phát triển trải nghiệm âm thanh. Chúng ta sẽ bắt đầu với **Thẻ** để kiểm soát nhanh nội dung, sau đó khám phá **Cấu trúc câu lệnh** nâng cao để có hướng dẫn đầy đủ về hiệu suất.

### Thẻ âm thanh

Thẻ là các đối tượng sửa đổi cùng dòng như `[whispers]` hoặc `[laughs]` giúp bạn kiểm soát thật chi tiết quá trình phân phối. Bạn có thể dùng các điểm đánh dấu này để thay đổi giọng điệu, tốc độ và cảm xúc của một dòng hoặc đoạn trong bản chép lời. Bạn cũng có thể dùng các biểu tượng này để thêm từ cảm thán và một số âm thanh không lời khác vào màn trình diễn, chẳng hạn như `[cough]`, `[sighs]` hoặc `[gasp]`.

Không có danh sách đầy đủ về những thẻ hoạt động và không hoạt động. Bạn nên thử nghiệm với nhiều cảm xúc và biểu cảm để xem kết quả thay đổi như thế nào.

Nếu bản chép lời không phải bằng tiếng Anh, để đạt được kết quả tốt nhất, bạn vẫn nên sử dụng thẻ âm thanh bằng tiếng Anh.

**Sáng tạo với thẻ âm thanh**

Để cho thấy mức độ đa dạng mà bạn có thể đạt được với thẻ âm thanh, sau đây là một bộ ví dụ. Mỗi ví dụ đều nói cùng một điều, nhưng cách truyền tải sẽ thay đổi dựa trên thẻ được sử dụng.

Bạn có thể thay đổi mức độ nhấn mạnh của nội dung bằng cách thêm thẻ vào đầu dòng để khiến người nói cảm thấy hào hứng, buồn chán hoặc miễn cưỡng:

- `[excitedly]` Xin chào, tôi là một mô hình chuyển văn bản sang lời nói mới và có thể nói theo nhiều cách. Hôm nay tôi có thể giúp gì cho bạn?
- `[bored]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…
- `[reluctantly]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…

Bạn cũng có thể dùng thẻ để thay đổi tốc độ truyền tải hoặc kết hợp tốc độ với điểm nhấn:

- `[very fast]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…
- `[very slow]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…
- `[sarcastically, one painfully slow word at a time]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…

Bạn cũng có thể kiểm soát chính xác các phần cụ thể, tức là bạn có thể nói thì thầm một phần và hét lên một phần khác.

- `[whispers]` Xin chào, tôi là một mô hình chuyển văn bản sang lời nói mới, `[shouting]` và tôi có thể nói theo nhiều cách khác nhau. `[whispers]` Hôm nay tôi có thể giúp gì cho bạn

Bạn cũng có thể thử nghiệm mọi ý tưởng sáng tạo mà bạn muốn:

- `[like a cartoon dog]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…
- `[like dracula]` Chào bạn, tôi là một mô hình chuyển văn bản sang lời nói mới…

Các thẻ thường dùng bao gồm:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Thẻ giúp bạn kiểm soát việc phân phối bản chép lời một cách nhanh chóng và dễ dàng. Để có thêm quyền kiểm soát, bạn có thể kết hợp các yếu tố này với một câu lệnh theo bối cảnh để đặt tông giọng và cảm xúc tổng thể của bản nhạc.

### Câu lệnh nâng cao

Bạn có thể coi câu lệnh nâng cao là một chỉ dẫn hệ thống để mô hình tuân theo. Đây là cách để cung cấp cho mô hình nhiều bối cảnh và quyền kiểm soát hơn đối với hiệu suất.

Một câu lệnh hiệu quả lý tưởng sẽ bao gồm các yếu tố sau đây kết hợp với nhau để tạo ra hiệu suất tuyệt vời:

- **Hồ sơ âm thanh** – Thiết lập một nhân vật cho giọng nói, xác định danh tính, nguyên mẫu và mọi đặc điểm khác của nhân vật như độ tuổi, bối cảnh, v.v.
- **Cảnh** – Thiết lập bối cảnh. Mô tả cả môi trường vật chất và "bầu không khí".
- **Ghi chú của đạo diễn** – Hướng dẫn về hiệu suất, nơi bạn có thể phân tích những chỉ dẫn quan trọng mà tài năng ảo cần lưu ý. Ví dụ: phong cách, hơi thở, tốc độ, cách phát âm và giọng điệu.
- **Bối cảnh mẫu** – Cung cấp cho mô hình một điểm xuất phát theo bối cảnh, nhờ đó diễn viên ảo của bạn sẽ xuất hiện một cách tự nhiên trong cảnh mà bạn thiết lập.
- **Bản chép lời** – Văn bản mà mô hình sẽ đọc. Để đạt hiệu suất tốt nhất, hãy nhớ rằng chủ đề và phong cách viết của bản chép lời phải tương quan với chỉ dẫn mà bạn đưa ra.
- **Thẻ âm thanh** – Các đối tượng sửa đổi mà bạn có thể đưa vào bản chép lời để thay đổi cách truyền tải phần văn bản đó, chẳng hạn như `[whispers]` hoặc `[shouting]`.

Ví dụ về câu lệnh đầy đủ:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to wake
up an entire nation.

### DIRECTOR'S NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
* Dynamics: High projection without shouting. Punchy consonants and elongated
vowels on excitement words (e.g., "Beauuutiful morning").

Pace: Speaks at an energetic pace, keeping up with the fast music.  Speaks
with A "bouncing" cadence. High-speed delivery with fluid transitions — no dead
air, no gaps.

Accent: Jaz is from Brixton, London

### SAMPLE CONTEXT
Jaz is the industry standard for Top 40 radio, high-octane event promos, or any
script that requires a charismatic Estuary accent and 11/10 infectious energy.

#### TRANSCRIPT
[excitedly] Yes, massive vibes in the studio! You are locked in and it is
absolutely popping off in London right now. If you're stuck on the tube, or
just sat there pretending to work... stop it. Seriously, I see you.
[shouting] Turn this up! We've got the project roadmap landing in three,
two... let's go!
```

### Chiến lược đưa ra câu lệnh chi tiết

Hãy cùng phân tích từng thành phần của câu lệnh.

#### Cấu hình âm thanh

Mô tả ngắn gọn về hình tượng của nhân vật.

- **Tên**  Đặt tên cho nhân vật sẽ giúp mô hình và hiệu suất chặt chẽ hơn, Hãy gọi nhân vật bằng tên khi thiết lập cảnh và bối cảnh
- **Vai trò.** Bản sắc và nguyên mẫu cốt lõi của nhân vật đang xuất hiện trong cảnh. Ví dụ: DJ đài phát thanh, người làm podcast, phóng viên tin tức, v.v.

Ví dụ:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scene

Thiết lập bối cảnh cho cảnh, bao gồm cả vị trí, tâm trạng và các chi tiết về môi trường để tạo ra tông giọng và cảm xúc. Mô tả những gì đang xảy ra xung quanh nhân vật và cách những sự kiện đó ảnh hưởng đến nhân vật. Khung cảnh cung cấp bối cảnh môi trường cho toàn bộ hoạt động tương tác và hướng dẫn diễn xuất một cách tinh tế và tự nhiên.

Ví dụ:

```
## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline,
but inside, it is blindingly bright. The red "ON AIR" tally light is blazing.
Jaz is standing up, not sitting, bouncing on the balls of their heels to the
rhythm of a thumping backing track. Their hands fly across the faders on a
massive mixing desk. It is a chaotic, caffeine-fueled cockpit designed to
wake up an entire nation.
```

```
## THE SCENE: Homegrown Studio
A meticulously sound-treated bedroom in a suburban home. The space is
deadened by plush velvet curtains and a heavy rug, but there is a
distinct "proximity effect."
```

#### Ghi chú của đạo diễn

Phần quan trọng này bao gồm hướng dẫn cụ thể về hiệu suất. Bạn có thể bỏ qua tất cả các phần tử khác, nhưng bạn nên đưa phần tử này vào.

Chỉ xác định những gì quan trọng đối với hiệu suất, cẩn thận để không chỉ định quá mức. Quá nhiều quy tắc nghiêm ngặt sẽ hạn chế khả năng sáng tạo của các mô hình và có thể dẫn đến hiệu suất kém hơn. Cân bằng vai trò và nội dung mô tả cảnh với các quy tắc diễn xuất cụ thể.

Các hướng dẫn phổ biến nhất là **Phong cách, tốc độ và giọng điệu**, nhưng mô hình không giới hạn ở những hướng dẫn này và cũng không yêu cầu phải có những hướng dẫn này. Bạn có thể thoải mái thêm hướng dẫn tuỳ chỉnh để trình bày mọi thông tin bổ sung quan trọng đối với hiệu suất của bạn, đồng thời cung cấp nhiều hoặc ít thông tin chi tiết tuỳ theo nhu cầu.

Ví dụ:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Kiểu:**

Đặt âm điệu và phong cách cho lời nói được tạo. Hãy thêm những thông tin như sôi động, tràn đầy năng lượng, thư giãn, buồn chán, v.v. để hướng dẫn hiệu suất. Hãy mô tả và cung cấp nhiều thông tin chi tiết nhất có thể: *"Nhiệt tình truyền cảm hứng. Người nghe nên cảm thấy như họ là một phần của một sự kiện cộng đồng lớn và thú vị."* sẽ hiệu quả hơn so với việc chỉ nói *"đầy năng lượng và nhiệt huyết".*

Bạn thậm chí có thể thử các thuật ngữ phổ biến trong ngành lồng tiếng, chẳng hạn như "nụ cười trong giọng nói". Bạn có thể xếp lớp bao nhiêu đặc điểm về kiểu dáng tuỳ thích.

Ví dụ:

Cảm xúc đơn giản

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Độ sâu lớn hơn

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Phức tạp

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Giọng:**

Mô tả giọng nói bạn muốn. Bạn càng trình bày cụ thể thì kết quả càng tốt. Ví dụ: sử dụng "*Giọng tiếng Anh Anh như nghe thấy ở Croydon, Anh*" thay vì "*Giọng Anh*".

Ví dụ:

```
### DIRECTORS NOTES
...
Accent: Southern california valley girl from Laguna Beach
...
```

```
### DIRECTORS NOTES
...
Accent: Jaz is a DJ from Brixton, London
...
```

**Nhịp độ:**

Nhịp độ tổng thể và sự thay đổi nhịp độ trong suốt bản nhạc.

Ví dụ:

Đơn giản

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Độ sâu lớn hơn

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Phức tạp

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Bản chép lời và thẻ âm thanh

Bản chép lời là những từ chính xác mà mô hình sẽ nói. Thẻ âm thanh là một từ trong dấu ngoặc vuông cho biết cách nói một nội dung nào đó, sự thay đổi về giọng điệu hoặc một câu cảm thán.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Hãy thử**

Hãy tự mình thử một số ví dụ này trên [AI Studio](https://aistudio.google.com/generate-speech?hl=vi), dùng thử [Ứng dụng TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=vi) của chúng tôi và để Gemini giúp bạn trở thành đạo diễn. Hãy ghi nhớ những mẹo sau để có màn trình diễn thanh nhạc tuyệt vời:

- Hãy nhớ giữ cho toàn bộ câu lệnh nhất quán – kịch bản và chỉ đạo phải đi đôi với nhau để tạo ra một màn trình diễn tuyệt vời.
- Bạn không cần phải mô tả mọi thứ, đôi khi việc cho phép mô hình tự điền vào chỗ trống sẽ giúp tạo ra hình ảnh tự nhiên hơn. (Giống như một diễn viên tài năng)
- Nếu bạn cảm thấy bế tắc, hãy nhờ Gemini giúp bạn soạn kịch bản hoặc dàn dựng màn trình diễn.

## Tạo lời nói trực tuyến

Bạn có thể phát trực tuyến âm thanh được tạo trong khi mô hình đang tạo âm thanh đó. Điều này hữu ích trong việc giảm độ trễ cảm nhận được.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response_stream = client.models.generate_content_stream(
   model="gemini-3.1-flash-tts-preview",
   contents="Say cheerfully: Have a wonderful day!",
   config=types.GenerateContentConfig(
      response_modalities=["AUDIO"],
      speech_config=types.SpeechConfig(
         voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
               voice_name='Kore',
            )
         )
      ),
   )
)

for chunk in response_stream:
   try:
      data = chunk.candidates[0].content.parts[0].inline_data.data
      # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
      # Process the audio chunk (e.g., play it or write to a file)
   except (IndexError, AttributeError):
      pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: "gemini-3.1-flash-tts-preview",
      contents: [{ parts: [{ text: 'Say cheerfully: Have a wonderful day!' }] }],
      config: {
            responseModalities: ['AUDIO'],
            speechConfig: {
               voiceConfig: {
                  prebuiltVoiceConfig: { voiceName: 'Kore' },
               },
            },
      },
   });

   for await (const chunk of responseStream) {
      const data = chunk.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
      if (data) {
         const audioBuffer = Buffer.from(data, 'base64');
         // Process the audio buffer
      }
   }
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "parts":[{
            "text": "Say cheerfully: Have a wonderful day!"
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Kore"
              }
            }
          }
        }
    }'
```

## Các điểm hạn chế

- Các mô hình TTS chỉ có thể nhận dữ liệu đầu vào là văn bản và tạo dữ liệu đầu ra là âm thanh.
- Một phiên TTS có giới hạn [cửa sổ ngữ cảnh](https://ai.google.dev/gemini-api/docs/long-context?hl=vi) là 32.000 token.
- Xem phần [Ngôn ngữ](https://ai.google.dev/gemini-api/docs/speech-generation?hl=vi#languages) để biết thông tin về ngôn ngữ được hỗ trợ.
- TTS không hỗ trợ truyền trực tuyến cho các mô hình cũ hơn phiên bản 3.1 (TTS hỗ trợ truyền trực tuyến cho `gemini-3.1-flash-tts-preview` trở lên).

Các ràng buộc sau đây chỉ áp dụng khi bạn dùng mô hình Gemini 3.1 Flash TTS Preview để tạo lời nói:

- **Giọng nói không nhất quán với hướng dẫn trong câu lệnh:** Đầu ra của mô hình không phải lúc nào cũng hoàn toàn khớp với người nói đã chọn, khiến âm thanh khác với dự kiến. Để tránh giọng điệu không phù hợp (chẳng hạn như giọng nam trầm cố gắng nói như một cô gái trẻ), hãy đảm bảo giọng điệu và ngữ cảnh bằng văn bản của câu lệnh phù hợp một cách tự nhiên với hồ sơ của người nói được chọn.
- **Chất lượng của đầu ra dài hơn:** Chất lượng và tính nhất quán của lời nói có thể bắt đầu giảm sút đối với đầu ra được tạo có thời lượng dài hơn vài phút. Bạn nên chia bản chép lời thành các phần nhỏ hơn.
- **Thỉnh thoảng trả về mã thông báo văn bản:** Đôi khi, mô hình trả về mã thông báo văn bản thay vì mã thông báo âm thanh, khiến máy chủ không thực hiện được yêu cầu và trả về lỗi `500`. Vì điều này xảy ra ngẫu nhiên trong một tỷ lệ rất nhỏ các yêu cầu, bạn nên triển khai logic thử lại tự động trong ứng dụng của mình để xử lý những yêu cầu này.
- **Trường hợp trình phân loại câu lệnh từ chối nhầm:** Các câu lệnh mơ hồ có thể không kích hoạt được trình phân loại tổng hợp lời nói, dẫn đến yêu cầu bị từ chối (`PROHIBITED_CONTENT`) hoặc khiến mô hình đọc to hướng dẫn về phong cách và ghi chú của đạo diễn. Xác thực câu lệnh của bạn bằng cách thêm một phần mở đầu rõ ràng hướng dẫn mô hình tổng hợp lời nói và gắn nhãn rõ ràng nơi bắt đầu bản chép lời thực tế.

## Bước tiếp theo

- Hãy thử [sách hướng dẫn tạo âm thanh](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=vi).
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=vi) của Gemini cung cấp các lựa chọn tạo âm thanh tương tác mà bạn có thể xen kẽ với các phương thức khác.
- Để tìm hiểu cách xử lý *đầu vào* âm thanh, hãy xem hướng dẫn [Hiểu âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-28 UTC."],[],[]]
