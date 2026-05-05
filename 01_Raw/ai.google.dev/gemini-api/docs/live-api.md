---
source_url: https://ai.google.dev/gemini-api/docs/live-api?hl=tr
fetched_at: 2026-05-05T20:09:57.057406+00:00
title: "Gemini Live API overview \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Live API overview

Live API, Gemini ile düşük gecikmeli ve gerçek zamanlı sesli ve görsel etkileşimler sağlar. Kullanıcılarınıza doğal bir sohbet deneyimi sunmak için anında, insan benzeri sözlü yanıtlar vermek üzere sürekli ses, resim ve metin akışlarını işler.

![Live API&#39;ye Genel Bakış](https://ai.google.dev/static/gemini-api/docs/images/live-api-overview.png?hl=tr)

[Google AI Studio'da Live API'yi deneyinmic](https://aistudio.google.com/live?hl=tr)
[GitHub'dan örnek uygulamaları klonlayıncode](https://github.com/google-gemini/gemini-live-api-examples)
[Kodlama aracısı becerilerini kullanınterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=tr)

## Kullanım alanları

Live API, aşağıdakiler de dahil olmak üzere çeşitli sektörlerde gerçek zamanlı sesli temsilciler oluşturmak için kullanılabilir:

- **E-ticaret ve perakende:** Kişiselleştirilmiş öneriler sunan alışveriş asistanları ve müşteri sorunlarını çözen destek temsilcileri.
- **Oyun:** Etkileşimli oynanamayan karakterler (NPC'ler), oyun içi yardım asistanları ve oyun içi içeriğin anlık çevirisi.
- **Yeni nesil arayüzler:** Robotik, akıllı gözlükler ve araçlarda ses ve video özellikli deneyimler.
- **Sağlık hizmetleri:** Hasta desteği ve eğitimi için sağlık yardımcıları.
- **Finansal hizmetler:** Servet yönetimi ve yatırım rehberliği için yapay zeka danışmanları.
- **Eğitim:** Kişiselleştirilmiş talimatlar ve geri bildirimler sağlayan yapay zeka eğitmenleri ve öğrenci yardımcıları.

## Temel özellikler

Live API, güçlü sesli temsilciler oluşturmak için kapsamlı bir özellik seti sunar:

- [**Çok dilli destek**](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#supported-languages):
  Desteklenen 70 dilde sohbet edin.
- [**Araya girme**](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#interruptions):
  Kullanıcılar, yanıt veren etkileşimler için modeli istedikleri zaman kesebilir.
- [**Araç kullanımı**](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr):
  Dinamik etkileşimler için işlev çağırma ve Google Arama gibi araçları entegre eder.
- [**Ses transkriptleri**](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#audio-transcription):
  Hem kullanıcı girişinin hem de model çıkışının metin transkriptlerini sağlar.
- [**Proaktif ses**](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#proactive-audio):
  Modelin ne zaman ve hangi bağlamlarda yanıt vereceğini kontrol etmenizi sağlar.
- [**Duygusal diyalog**](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#affective-dialog):
  Yanıt stilini ve üslubunu, kullanıcının giriş ifadesine uyacak şekilde uyarlar.

## Teknik özellikler

Aşağıdaki tabloda, Live API'nin teknik özellikleri özetlenmiştir:

| Kategori | Ayrıntılar |
| --- | --- |
| Giriş biçimleri | Ses (ham 16 bit PCM ses, 16 kHz, little-endian), resimler (JPEG <= 1 FPS), metin |
| Çıkış biçimleri | Ses (ham 16 bit PCM ses, 24 kHz, little-endian) |
| Protokol | Durum bilgili WebSocket bağlantısı (WSS) |

## Bir uygulama yaklaşımı seçin

Live API ile entegrasyon yaparken aşağıdaki uygulama yaklaşımlarından birini seçmeniz gerekir:

- **Sunucudan sunucuya**: Arka ucunuz, [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) kullanarak Live API'ye bağlanır. Genellikle istemciniz, akış verilerini (ses, video, metin) sunucunuza gönderir. Sunucunuz da bu verileri Live API'ye iletir.
- **İstemciden sunucuya**: Ön uç kodunuz, verileri yayınlamak için [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) kullanarak doğrudan Live API'ye bağlanır ve arka ucunuzu atlar.

## Başlayın

Geliştirme ortamınıza uygun kılavuzu seçin:

Sunucudan sunucuya

### [GenAI SDK eğitimi](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=tr)

Python arka ucuyla gerçek zamanlı çok formatlı bir uygulama oluşturmak için GenAI SDK'yı kullanarak Gemini Live API'ye bağlanın.

İstemciden sunucuya

### [WebSocket eğitimi](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=tr)

JavaScript ön ucu ve kısa ömürlü jetonlarla gerçek zamanlı çok formatlı bir uygulama oluşturmak için WebSockets kullanarak Gemini Live API'ye bağlanın.

Temsilci geliştirme kiti

### [ADK eğitimi](https://google.github.io/adk-docs/streaming/)

Temsilci oluşturun ve sesli ve görüntülü iletişimi etkinleştirmek için Agent Development Kit (ADK) Streaming'i kullanın.

## İş ortağı entegrasyonları

Anlık ses ve video uygulamalarının geliştirilmesini kolaylaştırmak için WebRTC veya WebSockets üzerinden Gemini Live API'yi destekleyen bir üçüncü taraf entegrasyonu kullanabilirsiniz.

[LiveKit

Gemini Live API'yi LiveKit Agents ile kullanma](https://docs.livekit.io/agents/models/realtime/plugins/gemini/)
[Pipecat by Daily

Gemini Live ve Pipecat'i kullanarak gerçek zamanlı yapay zeka destekli chatbot oluşturun.](https://docs.pipecat.ai/guides/features/gemini-live)
[Software Mansion tarafından geliştirilen Fishjam

Fishjam ile canlı video ve ses akışı uygulamaları oluşturun.](https://docs.fishjam.io/tutorials/gemini-live-integration)
[Akışa göre Vision Agents

Vision Agents ile gerçek zamanlı ses ve video yapay zeka uygulamaları oluşturun.](https://visionagents.ai/integrations/gemini)
[Voximplant

Gelen ve giden aramaları Voximplant ile Live API'ye bağlayın.](https://voximplant.com/products/gemini-client)
[Agora

Agora ile anlık etkileşimli yapay zeka uygulamaları oluşturun.](https://docs.agora.io/en/conversational-ai/models/mllm/gemini)
[Firebase AI SDK

Firebase AI Logic'i kullanarak Gemini Live API'yi kullanmaya başlayın.](https://firebase.google.com/docs/ai-logic/live-api?api=dev&hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
