---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=vi
fetched_at: 2026-07-20T04:36:18.674958+00:00
title: "D\u1ecbch tr\u1ef1c ti\u1ebfp b\u1eb1ng Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Dịch trực tiếp bằng Gemini Live API

Gemini Live API hỗ trợ dịch lời nói sang lời nói theo thời gian thực với độ trễ thấp giữa hơn 70 ngôn ngữ bằng mô hình [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=vi). Bằng cách định cấu hình Live API với chế độ cài đặt dịch, bạn có thể phát trực tuyến âm thanh bằng một ngôn ngữ và nhận đầu ra âm thanh đã dịch bằng một ngôn ngữ khác, giúp dịch liền mạch từ giọng nói sang giọng nói theo thời gian thực.

[Hãy thử tính năng Dịch trực tiếp trong Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=vi)
[Clone the example app from GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Use coding agent skillsterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=vi#gemini-live-api-dev)

## Nhân viên hỗ trợ trực tiếp so với tính năng Dịch trực tiếp

Mặc dù cả hai đều sử dụng Live API, nhưng mô hình tư duy cho tính năng Dịch trực tiếp khác với các tương tác theo thời gian thực của nhân viên hỗ trợ.

| Nhân viên hỗ trợ trực tiếp | Dịch trực tiếp |
| --- | --- |
| **Mô hình này đóng vai trò là trợ lý.** Mô hình này lắng nghe, suy luận và thực hiện hành động thay mặt bạn. | **Mô hình này đóng vai trò là phiên dịch viên.** Mô hình này hoạt động như một quy trình dịch theo thời gian thực. |
| **Sử dụng các tương tác theo lượt.** Dựa vào các khoảng dừng, phát hiện ý định và xử lý các trường hợp ngắt lời. | **Sử dụng xử lý theo luồng liên tục.** Dịch khi người nói đang nói mà không cần chờ đến lượt. |
| **Hỗ trợ các công cụ và nhân viên hỗ trợ.** Hỗ trợ gốc cho việc gọi hàm, Google Tìm kiếm và hướng dẫn. | **Chỉ hỗ trợ dịch.** Chỉ dịch với độ trễ thấp; không hỗ trợ các công cụ hoặc hướng dẫn. |
| **Hoàn toàn đa phương thức.** Hỗ trợ văn bản, âm thanh, video và hình ảnh đầu vào. | **Hạn chế về âm thanh.** Chỉ hỗ trợ âm thanh đầu vào để đảm bảo các ngưỡng độ trễ theo thời gian thực nghiêm ngặt. |
| **Cấu hình chi tiết.** Sử dụng hướng dẫn tạo, lời nói, công cụ và hệ thống. | **Cấu hình đơn giản.** Đặt `target_language_code` và các nút bật/tắt như `echo_target_language`. |

## Bắt đầu

Các ví dụ sau đây minh hoạ cách khởi chạy một ứng dụng và kết nối với Live API bằng cấu hình dịch.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()

model = "gemini-3.5-live-translate-preview"
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
    output_audio_transcription=types.AudioTranscriptionConfig(),
    translation_config=types.TranslationConfig(
        target_language_code="pl",
        echo_target_language=True
    )
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started with translation")
        # Start receiving the translated audio stream
        async for response in session.receive():
            if response.server_content:
                if response.server_content.input_transcription:
                    print(f"Input transcript: {response.server_content.input_transcription.text}")
                if response.server_content.output_transcription:
                    print(f"Output transcript: {response.server_content.output_transcription.text}")
                if response.server_content.model_turn:
                    for part in response.server_content.model_turn.parts:
                        if part.inline_data:
                            audio_data = part.inline_data.data
                            # Play or process the translated audio chunk
                            print(f"Received audio chunk ({len(audio_data)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-live-translate-preview';
const config = {
    responseModalities: [Modality.AUDIO],
    inputAudioTranscription: {},
    outputAudioTranscription: {},
    translationConfig: {
        targetLanguageCode: 'pl',
        echoTargetLanguage: true
    }
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.debug('Opened'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Input transcript:', content.inputTranscription.text);
        }
        if (content?.outputTranscription) {
          console.log('Output transcript:', content.outputTranscription.text);
        }
        if (content?.modelTurn?.parts) {
          for (const part of content.modelTurn.parts) {
            if (part.inlineData) {
              const audioData = part.inlineData.data;
              // Play or process the translated audio chunk (base64 encoded)
              console.debug(`Received audio chunk (${audioData.length} bytes)`);
            }
          }
        }
      },
      onerror: (e) => console.debug('Error:', e.message),
      onclose: (e) => console.debug('Close:', e.reason),
    },
  });

  console.debug("Session started with translation");
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-live-translate-preview";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket Connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['AUDIO'],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
        translationConfig: {
          targetLanguageCode: 'pl',
          echoTargetLanguage: true
        }
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  if (response.serverContent) {
    const content = response.serverContent;
    if (content.inputTranscription) {
      console.log('Input transcript:', content.inputTranscription.text, `(${content.inputTranscription.languageCode})`);
    }
    if (content.outputTranscription) {
      console.log('Output transcript:', content.outputTranscription.text, `(${content.outputTranscription.languageCode})`);
    }
    if (content.modelTurn?.parts) {
      for (const part of content.modelTurn.parts) {
        if (part.inlineData) {
          const audioData = part.inlineData.data;
          // Play or process the translated audio chunk (base64 encoded)
          console.debug(`Received audio chunk (${audioData.length} bytes)`);
        }
      }
    }
  }
};
```

## Gửi âm thanh

Để phát trực tuyến dữ liệu đầu vào bằng giọng nói để dịch, bạn sẽ gửi âm thanh PCM 16 bit, little-endian, thô.

- **Định dạng âm thanh đầu vào**: PCM 16 bit thô ở tần số 16kHz (mono, little-endian).
- **Định dạng âm thanh đầu ra**: PCM 16 bit thô ở tần số 24kHz (mono, little-endian).
- **Kích thước đoạn và độ trễ**: Gửi âm thanh theo đoạn 100 mili giây.

Các ví dụ sau đây cho thấy cách gửi các đoạn âm thanh đến phiên.

### Python

```
# Assuming 'chunk' is your raw PCM audio bytes
await session.send_realtime_input(
    audio=types.Blob(
        data=chunk,
        mime_type="audio/pcm;rate=16000"
    )
)
```

### JavaScript

```
// Assuming 'chunk' is a Buffer of raw PCM audio
session.sendRealtimeInput({
  audio: {
    data: chunk.toString('base64'),
    mimeType: 'audio/pcm;rate=16000'
  }
});
```

### WebSockets

```
// Assuming 'chunk' is a Buffer of raw PCM audio
function sendAudioChunk(chunk) {
  if (websocket.readyState === WebSocket.OPEN) {
    const audioMessage = {
      realtimeInput: {
        audio: {
          data: chunk.toString('base64'),
          mimeType: 'audio/pcm;rate=16000'
        }
      }
    };
    websocket.send(JSON.stringify(audioMessage));
  }
}
```

## Cấu hình

Để bật tính năng dịch, bạn phải chỉ định `translationConfig` trong `generationConfig` trong quá trình thiết lập phiên.

### Thiết lập cấu hình thông báo

`generationConfig` hỗ trợ các trường sau để bật bản chép lời:

- **`inputAudioTranscription`**: Một đối tượng mà khi có mặt, sẽ cho phép mô hình gửi bản chép lời bằng văn bản của âm thanh đầu vào.
- **`outputAudioTranscription`**: Một đối tượng mà khi có mặt, sẽ cho phép mô hình gửi bản chép lời bằng văn bản của âm thanh đầu ra (đã dịch).

`translationConfig` hỗ trợ các trường sau:

- **`targetLanguageCode`**: Mã ngôn ngữ [BCP-47](#supported-languages) của ngôn ngữ mà bạn muốn mô hình dịch sang (ví dụ: `"pl"` cho tiếng Ba Lan, `"es"` cho tiếng Tây Ban Nha). Giá trị mặc định là `"en"`.
- **`echoTargetLanguage`**: Một giá trị boolean cho biết cách xử lý âm thanh đầu vào đã ở ngôn ngữ mục tiêu. Nếu được đặt thành `true`, mô hình sẽ lặp lại (nhại) âm thanh đầu vào đã ở ngôn ngữ mục tiêu. Nếu được đặt thành `false`, mô hình sẽ giữ im lặng khi lời nói đầu vào đã ở ngôn ngữ mục tiêu. Giá trị mặc định là `false`.

Dưới đây là ví dụ về cấu trúc thông báo thiết lập:

```
"setup": {
    "model": "models/gemini-3.5-live-translate-preview",
    "generationConfig": {
      "responseModalities": [
        "AUDIO"
      ],
      "inputAudioTranscription": {},
      "outputAudioTranscription": {},
      "translationConfig": {
        "targetLanguageCode": "pl",
        "echoTargetLanguage": true
      }
    }
}
```

## Mã thông báo tạm thời cho các ứng dụng phía máy khách

Đối với các ứng dụng từ máy khách đến máy chủ, bạn có thể sử dụng [mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=vi) (hiện ở `v1alpha`) để tránh tiết lộ khoá API của mình.

Khi sử dụng mã thông báo tạm thời với tính năng Dịch trực tiếp:

1. Bạn phải sử dụng điểm cuối `v1alpha`.
2. **Khoá cấu hình:** Theo mặc định, bạn nên chỉ định `translationConfig` trong các ràng buộc tạo mã thông báo trên máy chủ của mình. Điều này đảm bảo cấu hình dịch được khoá và ứng dụng không thể can thiệp.
3. **Mở khoá cấu hình:** Nếu muốn có thể đặt `translationConfig` ở phía máy khách (ví dụ: để cho phép người dùng chọn ngôn ngữ mục tiêu của riêng họ), bạn phải bỏ qua cấu hình này trong yêu cầu tạo mã thông báo và đặt `"lock_additional_fields": []` thay thế. Thao tác này sẽ mở khoá `translationConfig` để đặt ở phía máy khách.

### Tạo mã thông báo tạm thời bị ràng buộc

Các ví dụ sau đây minh hoạ cách tạo mã thông báo tạm thời có các ràng buộc về bản dịch.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client(
    http_options={'api_version': 'v1alpha'}
)

token = client.auth_tokens.create(
    config = {
        'uses': 1,
        'expire_time': now + datetime.timedelta(minutes=30),
        'live_connect_constraints': {
            'model': 'gemini-3.5-live-translate-preview',
            'config': {
                'translation_config': {
                    'target_language_code': 'pl',
                    'echo_target_language': True
                }
            }
        },
        'http_options': {'api_version': 'v1alpha'},
    }
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
    config: {
        uses: 1,
        expireTime: expireTime,
        liveConnectConstraints: {
            model: 'gemini-3.5-live-translate-preview',
            config: {
                responseModalities: ['AUDIO'],
                inputAudioTranscription: {},
                outputAudioTranscription: {},
                translationConfig: {
                    targetLanguageCode: 'pl',
                    echoTargetLanguage: true
                }
            }
        },
        httpOptions: {
            apiVersion: 'v1alpha'
        }
    },
});
```

## Các điểm hạn chế

- **Phương thức đầu vào**: Chỉ hỗ trợ âm thanh đầu vào để dịch. Không được hỗ trợ văn bản đầu vào.
- **Sao chép giọng nói**: Việc sao chép giọng nói có thể không nhất quán. Giọng nói có thể thay đổi sau các khoảng dừng dài, gán giới tính không chính xác dựa trên cách lời nói bắt đầu hoặc bị kẹt ở một giọng nói trong các cuộc trò chuyện nhanh có nhiều người nói.
- **Phát hiện ngôn ngữ**: Tính năng phát hiện ngôn ngữ gặp khó khăn với giọng nói có âm sắc nặng, các ngôn ngữ tương tự (ví dụ: tiếng Tây Ban Nha so với tiếng Bồ Đào Nha) hoặc các trường hợp chuyển đổi ngôn ngữ nhanh. **Lưu ý:** Điều này chỉ ảnh hưởng đến bản chép lời đầu vào. Mã ngôn ngữ và bản dịch cuối cùng vẫn phải chính xác.
- **Âm thanh nền**: Mô hình này được thiết kế để lọc tiếng ồn và nhạc nhằm tạo ra lời nói rõ ràng, nhưng không phải tất cả âm thanh nền đều có thể bị bỏ qua.
- **Lặp lại ngôn ngữ mục tiêu**: Khi `echoTargetLanguage: true`, tạp âm hoặc nhạc nền có thể tạo ra các thành phần giả trong âm thanh đã dịch khi âm thanh đầu vào đã ở ngôn ngữ mục tiêu.

## Ngôn ngữ được hỗ trợ

Tính năng Dịch trực tiếp hỗ trợ các ngôn ngữ sau.

| Ngôn ngữ | Mã BCP-47 | Ngôn ngữ | Mã BCP-47 |
| --- | --- | --- | --- |
| Tiếng Hà Lan ở Nam Phi | af | Tiếng Kazakh | kk |
| Akan | ak | Tiếng Khmer | km |
| Tiếng Albania | sq | Tiếng Kinyarwanda | rw |
| Tiếng Amhara | am | Tiếng Hàn | ko |
| Tiếng Ả Rập | ar | Tiếng Lào | lo |
| Tiếng Armenia | hy | Tiếng Latvia | lv |
| Tiếng Azerbaijan | az | Tiếng Lithuania | lt |
| Tiếng Basque | eu | Tiếng Macedonia | mk |
| Tiếng Belarus | be | Tiếng Malay | ms |
| Tiếng Bengal | bn | Tiếng Malayalam | ml |
| Tiếng Bungary | bg | Tiếng Marathi | mr |
| Tiếng Miến Điện (Myanmar) | my | Tiếng Mông Cổ | mn |
| Tiếng Catalan | ca | Tiếng Nepal | ne |
| Tiếng Trung (Giản thể) | zh-Hans | Tiếng Na Uy | no, nb |
| Tiếng Trung (Phồn thể) | zh-Hant | Persian | fa |
| Tiếng Croatia | hr | Tiếng Ba Lan | pl |
| Tiếng Séc | cs | Tiếng Bồ Đào Nha (Brazil) | pt-BR |
| Tiếng Đan Mạch | da | Tiếng Bồ Đào Nha (Bồ Đào Nha) | pt-PT |
| Tiếng Hà Lan | nl | Tiếng Punjab | pa |
| Tiếng Anh | en | Tiếng Rumani | ro |
| Tiếng Estonia | et | Tiếng Nga | ru |
| Tiếng Philippines | fil | Tiếng Serbia | sr |
| Tiếng Phần Lan | fi | Tiếng Sindh | sd |
| Tiếng Pháp | fr | Tiếng Sinhala | si |
| Tiếng Galicia | gl | Tiếng Slovak | sk |
| Tiếng Gruzia | ka | Tiếng Slovenia | sl |
| Tiếng Đức | de | Tiếng Tây Ban Nha | es |
| Tiếng Hy Lạp | el | Tiếng Sunda | su |
| Tiếng Gujarat | gu | Tiếng Swahili | sw |
| Tiếng Hausa | ha | Tiếng Thuỵ Điển | sv |
| Tiếng Do Thái | he | Tiếng Tamil | ta |
| Tiếng Hindi | hi | Tiếng Telugu | te |
| Tiếng Hungary | hu | Tiếng Thái | th |
| Tiếng Iceland | is | Tiếng Thổ Nhĩ Kỳ | tr |
| Tiếng Indonesia | id | Tiếng Ukraina | uk |
| Tiếng Ý | it | Tiếng Urdu | ur |
| Tiếng Nhật | ja | Tiếng Uzbek | uz |
| Tiếng Java | jv | Tiếng Việt | vi |
| Tiếng Kannada | kn | Tiếng Zulu | zu |

## Bước tiếp theo

- Đọc hướng dẫn đầy đủ về Các tính năng của Live API [Capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=vi).
- Đọc hướng dẫn [Bắt đầu sử dụng SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=vi).
- Đọc hướng dẫn [Bắt đầu sử dụng WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=vi).
- Đọc hướng dẫn về [Mã thông báo tạm thời](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=vi) để xác thực an toàn trong các ứng dụng từ máy khách đến máy chủ.
- Sao chép các víעים về [Live API](https://github.com/google-gemini/gemini-live-api-examples) trên GitHub.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-09 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-09 UTC."],[],[]]
