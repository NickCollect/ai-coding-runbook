---
source_url: https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=tr
fetched_at: 2026-06-29T05:39:11.288707+00:00
title: "Google GenAI SDK'y\u0131 kullanarak Gemini Live API'yi kullanmaya ba\u015flama \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google GenAI SDK'yı kullanarak Gemini Live API'yi kullanmaya başlama

Gemini Live API, Gemini modelleriyle gerçek zamanlı ve çift yönlü etkileşime olanak tanır. Ses, video ve metin girişlerinin yanı sıra doğal ses çıkışlarını destekler. Bu kılavuzda, sunucunuzda Google GenAI SDK'sını kullanarak API ile nasıl entegrasyon yapacağınız açıklanmaktadır.

[Google AI Studio'da Live API'yi deneyinmic](https://aistudio.google.com/live?hl=tr)
[Örnek uygulamayı GitHub'dan klonlayıncode](https://github.com/google-gemini/gemini-live-api-examples/tree/main/gemini-live-genai-python-sdk)
[Kodlama aracısı becerilerini kullanınterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)

## Genel Bakış

Gemini Live API, anlık iletişim için WebSocket'leri kullanır. `google-genai` SDK, bu bağlantıları yönetmek için üst düzey bir eşzamansız arayüz sağlar.

Temel kavramlar:

- **Oturum**: Modele kalıcı bağlantı.
- **Yapılandırma**: Formatları (ses/metin), sesi ve sistem talimatlarını ayarlama.
- **Anlık Giriş**: Ses ve video karelerini blob olarak gönderme.

## Live API'ye bağlanma

API anahtarıyla Live API oturumu başlatma:

### Python

```
import asyncio
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

model = "gemini-3.1-flash-live-preview"
config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session started")
        # Send content...

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY"});
const model = 'gemini-3.1-flash-live-preview';
const config = { responseModalities: [Modality.AUDIO] };

async function main() {

  const session = await ai.live.connect({
    model: model,
    callbacks: {
      onopen: function () {
        console.debug('Opened');
      },
      onmessage: function (message) {
        console.debug(message);
      },
      onerror: function (e) {
        console.debug('Error:', e.message);
      },
      onclose: function (e) {
        console.debug('Close:', e.reason);
      },
    },
    config: config,
  });

  console.debug("Session started");
  // Send content...

  session.close();
}

main();
```

## Kısa mesaj gönderiliyor

Metin, `send_realtime_input` (Python) veya `sendRealtimeInput` (JavaScript) kullanılarak gönderilebilir.

### Python

```
await session.send_realtime_input(text="Hello, how are you?")
```

### JavaScript

```
session.sendRealtimeInput({
  text: 'Hello, how are you?'
});
```

## Ses gönderme

Ses, ham PCM verileri (ham 16 bit PCM ses, 16 kHz, little-endian) olarak gönderilmelidir.

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

İstemci cihazdan (ör. tarayıcı) ses alma örneği için [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L31-L70)'daki uçtan uca örneğe bakın.

## Video gönderiliyor

Video kareleri, belirli bir kare hızında (saniyede en fazla 1 kare) ayrı resimler (ör. JPEG veya PNG) olarak gönderilir.

### Python

```
# Assuming 'frame' is your JPEG-encoded image bytes
await session.send_realtime_input(
    video=types.Blob(
        data=frame,
        mime_type="image/jpeg"
    )
)
```

### JavaScript

```
// Assuming 'frame' is a Buffer of JPEG-encoded image data
session.sendRealtimeInput({
  video: {
    data: frame.toString('base64'),
    mimeType: 'image/jpeg'
  }
});
```

Videoyu istemci cihazdan (ör. tarayıcı) alma örneği için [GitHub](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L84-L120)'daki uçtan uca örneğe bakın.

## Ses alma

Modelin sesli yanıtları veri parçaları olarak alınır.

### Python

```
async for response in session.receive():
    if response.server_content and response.server_content.model_turn:
        for part in response.server_content.model_turn.parts:
            if part.inline_data:
                audio_data = part.inline_data.data
                # Process or play the audio data
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data;
      // Process or play audioData (base64 encoded string)
    }
  }
}
```

[Sunucunuzda sesi nasıl alacağınızı](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/gemini_live.py#L86-L98) ve [tarayıcıda nasıl çalacağınızı](https://github.com/google-gemini/gemini-live-api-examples/blob/main/gemini-live-genai-python-sdk/frontend/media-handler.js#L145-L174) öğrenmek için GitHub'daki örnek uygulamaya bakın.

## Kısa mesaj alınıyor

Hem kullanıcı girişi hem de model çıkışı için transkriptler sunucu içeriğinde mevcuttur.

### Python

```
async for response in session.receive():
    content = response.server_content
    if content:
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
```

### JavaScript

```
// Inside the onmessage callback
const content = response.serverContent;
if (content?.inputTranscription) {
  console.log('User:', content.inputTranscription.text);
}
if (content?.outputTranscription) {
  console.log('Gemini:', content.outputTranscription.text);
}
```

## Araç çağrılarını işleme

API, araç çağrısını (işlev çağrısı) destekler. Model bir araç çağrısı istediğinde işlevi yürütmeniz ve yanıtı geri göndermeniz gerekir.

### Python

```
async for response in session.receive():
    if response.tool_call:
        function_responses = []
        for fc in response.tool_call.function_calls:
            # 1. Execute the function locally
            result = my_tool_function(**fc.args)

            # 2. Prepare the response
            function_responses.append(types.FunctionResponse(
                name=fc.name,
                id=fc.id,
                response={"result": result}
            ))

        # 3. Send the tool response back to the session
        await session.send_tool_response(function_responses=function_responses)
```

### JavaScript

```
// Inside the onmessage callback
if (response.toolCall) {
  const functionResponses = [];
  for (const fc of response.toolCall.functionCalls) {
    const result = myToolFunction(fc.args);
    functionResponses.push({
      name: fc.name,
      id: fc.id,
      response: { result }
    });
  }
  session.sendToolResponse({ functionResponses });
}
```

## Sırada ne var?

- Konuşma Etkinliği Algılama ve yerel ses özellikleri de dahil olmak üzere temel özellikler ve yapılandırmalar için Live API [Özellikleri](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) kılavuzunun tamamını okuyun.
- Live API'yi araçlarla ve işlev çağırmayla nasıl entegre edeceğinizi öğrenmek için [Araç kullanımı](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr) kılavuzunu okuyun.
- Uzun süren görüşmeleri yönetmek için [Oturum yönetimi](https://ai.google.dev/gemini-api/docs/live-session?hl=tr) kılavuzunu okuyun.
- [İstemciden sunucuya](#implementation-approach) uygulamalarda güvenli kimlik doğrulama için [Geçici jetonlar](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=tr) kılavuzunu okuyun.
- Temel alınan WebSockets API hakkında daha fazla bilgi için [WebSockets API referansı](https://ai.google.dev/api/live?hl=tr) başlıklı makaleyi inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-01 UTC."],[],[]]
