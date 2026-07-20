---
source_url: https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=tr
fetched_at: 2026-07-20T04:48:29.798596+00:00
title: "Lyria RealTime ile an\u0131nda m\u00fczik \u00fcretme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Lyria RealTime ile anında müzik üretme

[deneysel modeldir](https://ai.google.dev/gemini-api/docs/models?hl=tr#experimental).

[Lyria RealTime](https://deepmind.google/technologies/lyria/realtime/?hl=tr)'ı kullanan Gemini API, son teknoloji ürünü, gerçek zamanlı ve akışlı bir müzik üretme modeline erişim sağlar. Bu API, geliştiricilerin kullanıcıların etkileşimli olarak oluşturabileceği, sürekli yönlendirebileceği ve enstrümantal müzik yapabileceği uygulamalar geliştirmesine olanak tanır.

Lyria RealTime müzik üretimi, [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) kullanılarak kalıcı, çift yönlü ve düşük gecikmeli bir akış bağlantısı kullanır.

Lyria RealTime ile neler yapılabileceğini deneyimlemek için [Prompt DJ](https://aistudio.google.com/apps/bundled/promptdj?hl=tr) veya [MIDI DJ](https://aistudio.google.com/apps/bundled/promptdj-midi?hl=tr) uygulamalarını kullanarak AI Studio'da deneyin.

## Müzik üretme ve müziği kontrol etme

Lyria RealTime, modelle anlık iletişimi sürdürmek için Websocket'leri kullanması bakımından [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)'ye benzer şekilde çalışır.

Aşağıdaki kodda nasıl müzik oluşturulacağı gösterilmektedir:

### Python

Bu örnekte, `client.aio.live.music.connect()` kullanılarak Lyria RealTime oturumu başlatılıyor, ardından `session.set_weighted_prompts()` ile ilk istem ve `session.set_music_generation_config` kullanılarak ilk yapılandırma gönderiliyor, `session.play()` kullanılarak müzik üretimi başlatılıyor ve `receive_audio()`, aldığı ses parçalarını işleyecek şekilde ayarlanıyor.

```
  import asyncio
  from google import genai
  from google.genai import types

  client = genai.Client(http_options={'api_version': 'v1alpha'})

  async def main():
      async def receive_audio(session):
        """Example background task to process incoming audio."""
        while True:
          async for message in session.receive():
            audio_data = message.server_content.audio_chunks[0].data
            # Process audio...
            await asyncio.sleep(10**-12)

      async with (
        client.aio.live.music.connect(model='models/lyria-realtime-exp') as session,
        asyncio.TaskGroup() as tg,
      ):
        # Set up task to receive server messages.
        tg.create_task(receive_audio(session))

        # Send initial prompts and config
        await session.set_weighted_prompts(
          prompts=[
            types.WeightedPrompt(text='minimal techno', weight=1.0),
          ]
        )
        await session.set_music_generation_config(
          config=types.LiveMusicGenerationConfig(bpm=90, temperature=1.0)
        )

        # Start streaming music
        await session.play()
  if __name__ == "__main__":
      asyncio.run(main())
```

### JavaScript

Bu örnekte, `client.live.music.connect()` kullanılarak Lyria RealTime oturumu başlatılıyor, ardından `session.setWeightedPrompts()` ile ilk istem ve `session.setMusicGenerationConfig` kullanılarak ilk yapılandırma gönderiliyor, `session.play()` kullanılarak müzik oluşturma işlemi başlatılıyor ve alınan ses parçalarını işlemek için `onMessage` geri çağırma işlevi ayarlanıyor.

```
import { GoogleGenAI } from "@google/genai";
import Speaker from "speaker";
import { Buffer } from "buffer";

const client = new GoogleGenAI({
  apiKey: GEMINI_API_KEY,
    apiVersion: "v1alpha" ,
});

async function main() {
  const speaker = new Speaker({
    channels: 2,       // stereo
    bitDepth: 16,      // 16-bit PCM
    sampleRate: 44100, // 44.1 kHz
  });

  const session = await client.live.music.connect({
    model: "models/lyria-realtime-exp",
    callbacks: {
      onmessage: (message) => {
        if (message.serverContent?.audioChunks) {
          for (const chunk of message.serverContent.audioChunks) {
            const audioBuffer = Buffer.from(chunk.data, "base64");
            speaker.write(audioBuffer);
          }
        }
      },
      onerror: (error) => console.error("music session error:", error),
      onclose: () => console.log("Lyria RealTime stream closed."),
    },
  });

  await session.setWeightedPrompts({
    weightedPrompts: [
      { text: "Minimal techno with deep bass, sparse percussion, and atmospheric synths", weight: 1.0 },
    ],
  });

  await session.setMusicGenerationConfig({
    musicGenerationConfig: {
      bpm: 90,
      temperature: 1.0,
      audioFormat: "pcm16",  // important so we know format
      sampleRateHz: 44100,
    },
  });

  await session.play();
}

main().catch(console.error);
```

Ardından oturumu başlatmak, duraklatmak, durdurmak veya sıfırlamak için `session.play()`, `session.pause()`, `session.stop()` ve `session.reset_context()` simgelerini kullanabilirsiniz.

## Müziği anlık olarak yönlendirme

İstemler göndererek ve üretim parametrelerini anlık olarak güncelleyerek müzik üretimini anlık olarak yönlendirebilirsiniz.

### Lyria RealTime'a istem girme

Yayın etkin durumdayken, oluşturulan müziği değiştirmek için istediğiniz zaman yeni `WeightedPrompt` mesajları gönderebilirsiniz. Model, yeni girişe göre sorunsuz bir şekilde geçiş yapar.

İstemler, `text` (asıl istem) ve `weight` ile doğru biçimde olmalıdır. `weight`, `0` hariç herhangi bir değeri alabilir. `1.0`
genellikle iyi bir başlangıç noktasıdır.

### Python

```
  from google.genai import types

  await session.set_weighted_prompts(
    prompts=[
      {"text": "Piano", "weight": 2.0},
      types.WeightedPrompt(text="Meditation", weight=0.5),
      types.WeightedPrompt(text="Live Performance", weight=1.0),
    ]
  )
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    weightedPrompts: [
      { text: 'Harmonica', weight: 0.3 },
      { text: 'Afrobeat', weight: 0.7 }
    ],
  });
```

İstemler önemli ölçüde değiştirildiğinde model geçişlerinin biraz ani olabileceğini unutmayın. Bu nedenle, modele ara ağırlık değerleri göndererek bir tür çapraz geçiş uygulamanız önerilir.

### Yapılandırmayı güncelleme

Müzik üretimi parametrelerini gerçek zamanlı olarak güncelleyerek müzik üretimini yönlendirebilirsiniz. Yalnızca bir parametreyi güncelleyemezsiniz. Diğer alanların varsayılan değerlerine sıfırlanmaması için tüm yapılandırmayı ayarlamanız gerekir.

BPM'yi veya ölçeği güncellemek model için önemli bir değişiklik olduğundan, yeni yapılandırmayı dikkate alması için `reset_context()` kullanarak bağlamını sıfırlamasını da söylemeniz gerekir. Bu işlem yayını durdurmaz ancak geçiş zor olur. Diğer parametreler için bu işlemi yapmanız gerekmez.

### Python

```
  from google.genai import types

  await session.set_music_generation_config(
    config=types.LiveMusicGenerationConfig(
      bpm=128,
      scale=types.Scale.D_MAJOR_B_MINOR,
      music_generation_mode=types.MusicGenerationMode.QUALITY
    )
  )
  await session.reset_context();
```

### JavaScript

```
  await session.setMusicGenerationConfig({
    musicGenerationConfig: { 
      bpm: 120,
      density: 0.75,
      musicGenerationMode: MusicGenerationMode.QUALITY
    },
  });
  await session.reset_context();
```

## Lyria RealTime için istem rehberi

Lyria RealTime'a istem göndermek için kullanabileceğiniz istemlerin kapsamlı olmayan bir listesini aşağıda bulabilirsiniz:

- Ödeme araçları: `303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone,
  Bagpipes, Balalaika Ensemble, Banjo, Bass Clarinet, Bongos, Boomy Bass,
  Bouzouki, Buchla Synths, Cello, Charango, Clavichord, Conga Drums,
  Didgeridoo, Dirty Synths, Djembe, Drumline, Dulcimer, Fiddle, Flamenco
  Guitar, Funk Drums, Glockenspiel, Guitar, Hang Drum, Harmonica, Harp,
  Harpsichord, Hurdy-gurdy, Kalimba, Koto, Lyre, Mandolin, Maracas, Marimba,
  Mbira, Mellotron, Metallic Twang, Moog Oscillations, Ocarina, Persian Tar,
  Pipa, Precision Bass, Ragtime Piano, Rhodes Piano, Shamisen, Shredding
  Guitar, Sitar, Slide Guitar, Smooth Pianos, Spacey Synths, Steel Drum, Synth
  Pads, Tabla, TR-909 Drum Machine, Trumpet, Tuba, Vibraphone, Viola Ensemble,
  Warm Acoustic Guitar, Woodwinds, ...`
- Müzik Türü: `Acid Jazz, Afrobeat, Alternative Country, Baroque, Bengal Baul,
  Bhangra, Bluegrass, Blues Rock, Bossa Nova, Breakbeat, Celtic Folk, Chillout,
  Chiptune, Classic Rock, Contemporary R&B, Cumbia, Deep House, Disco Funk,
  Drum & Bass, Dubstep, EDM, Electro Swing, Funk Metal, G-funk, Garage Rock,
  Glitch Hop, Grime, Hyperpop, Indian Classical, Indie Electronic, Indie Folk,
  Indie Pop, Irish Folk, Jam Band, Jamaican Dub, Jazz Fusion, Latin Jazz, Lo-Fi
  Hip Hop, Marching Band, Merengue, New Jack Swing, Minimal Techno, Moombahton,
  Neo-Soul, Orchestral Score, Piano Ballad, Polka, Post-Punk, 60s Psychedelic
  Rock, Psytrance, R&B, Reggae, Reggaeton, Renaissance Music, Salsa, Shoegaze,
  Ska, Surf Rock, Synthpop, Techno, Trance, Trap Beat, Trip Hop, Vaporwave,
  Witch house, ...`
- Ruh hali/Açıklama: `Acoustic Instruments, Ambient, Bright Tones, Chill,
  Crunchy Distortion, Danceable, Dreamy, Echo, Emotional, Ethereal Ambience,
  Experimental, Fat Beats, Funky, Glitchy Effects, Huge Drop, Live Performance,
  Lo-fi, Ominous Drone, Psychedelic, Rich Orchestration, Saturated Tones,
  Subdued Melody, Sustained Chords, Swirling Phasers, Tight Groove,
  Unsettling, Upbeat, Virtuoso, Weird Noises, ...`

Bunlar yalnızca birkaç örnektir. Lyria RealTime çok daha fazlasını yapabilir. Kendi istemlerinizle
denemeler yapın.

## En iyi uygulamalar

- İstemci uygulamaları, sorunsuz oynatma sağlamak için güçlü ses arabelleği oluşturma işlevini uygulamalıdır. Bu, ağ titremesini ve oluşturma gecikmesindeki küçük farklılıkları hesaba katmaya yardımcı olur.
- Etkili istemler:
  - Açıklayıcı olun. Atmosferi, türü ve enstrümanları açıklayan sıfatlar kullanın.
  - İterasyon yapın ve yavaş yavaş yönlendirin. İstemi tamamen değiştirmek yerine, müziği daha sorunsuz bir şekilde dönüştürmek için öğeler eklemeyi veya değiştirmeyi deneyin.
  - Yeni bir istemin devam eden üretimi ne kadar etkileyeceğini belirlemek için `WeightedPrompt` ağırlığıyla denemeler yapın.

## Teknik ayrıntılar

Bu bölümde, Lyria RealTime müzik üretme özelliğinin nasıl kullanılacağıyla ilgili ayrıntılar açıklanmaktadır.

### Teknik Özellikler

- Çıkış biçimi: Raw 16 bit PCM Ses
- Örnek hızı: 48 kHz
- Kanallar: 2 (stereo)

### Denetimler

Müzik üretimi, aşağıdakileri içeren mesajlar gönderilerek anlık olarak etkilenebilir:

- `WeightedPrompt`: Müzikal bir fikri, türü, enstrümanı, ruh halini veya özelliği açıklayan bir metin dizesi. Etkileri karıştırmak için birden fazla istem sağlanabilir. Lyria RealTime'ı en iyi şekilde isteme hakkında daha fazla bilgi için [yukarıdaki](#steer-music) bölüme bakın.
- `MusicGenerationConfig`: Müzik üretme sürecinin yapılandırması (çıkış sesinin özelliklerini etkiler). Parametreler
  şunları içerir:
  - `guidance`: (kayan nokta) Aralık: `[0.0, 6.0]`. Varsayılan: `4.0`.
    Modelin istemlere ne kadar sıkı uyacağını kontrol eder. Daha yüksek yönlendirme, isteme uyumu artırır ancak geçişleri daha ani hale getirir.
  - `bpm`: (int) Aralık: `[60, 200]`.
    Oluşturulan müzik için istediğiniz dakikadaki vuruş sayısını ayarlar. Yeni BPM'yi dikkate alması için modeli durdurmanız/oynatmanız veya bağlamı sıfırlamanız gerekir.
  - `density`: (kayan nokta) Aralık: `[0.0, 1.0]`.
    Müzik notalarının/seslerin yoğunluğunu kontrol eder. Düşük değerler daha seyrek müzikler üretir. Yüksek değerler ise daha "yoğun" müzikler üretir.
  - `brightness`: (kayan nokta) Aralık: `[0.0, 1.0]`.
    Ton kalitesini ayarlar. Daha yüksek değerler, genellikle daha yüksek frekansları vurgulayan "daha parlak" sesler üretir.
  - `scale`: (Enum)
    Oluşturma için müzik ölçeğini (anahtar ve mod) ayarlar. SDK tarafından sağlanan [`Scale` enum değerlerini](#scale-enum) kullanın. Modelin yeni ölçeği dikkate alması için bağlamı durdurmanız/oynatmanız veya sıfırlamanız gerekir.
  - `mute_bass`: (bool) Varsayılan: `False`.
    Modelin çıkışlardaki bası azaltıp azaltmayacağını kontrol eder.
  - `mute_drums`: (bool) Varsayılan: `False`.
    Model çıktılarının, davul sesini azaltıp azaltmadığını kontrol eder.
  - `only_bass_and_drums`: (bool) Varsayılan: `False`.
    Modeli yalnızca bas ve davul sesleri üretmeye yönlendirin.
  - `music_generation_mode`: (Enum)
    Modele, müziğin `QUALITY` (varsayılan değer) veya `DIVERSITY` kısmına odaklanıp odaklanmaması gerektiğini belirtir. Ayrıca, modelin başka bir enstrüman olarak seslendirme oluşturmasına (yeni istemler olarak ekleme) izin vermek için `VOCALIZATION` olarak da ayarlanabilir.
- `PlaybackControl`: Oynatma, duraklatma, durdurma veya bağlamı sıfırlama gibi oynatma özelliklerini kontrol etme komutları.

`bpm`, `density`, `brightness` ve `scale` için değer sağlanmazsa model, ilk istemlerinize göre en iyi seçeneğe karar verir.

`temperature` (0,0-3,0, varsayılan 1,1), `top_k` (1-1000, varsayılan 40) ve `seed` (0-2.147.483.647, varsayılan olarak rastgele seçilir) gibi daha klasik parametreler de `MusicGenerationConfig` içinde özelleştirilebilir.

#### Enum Değerlerini Ölçeklendirme

Modelin kabul edebileceği tüm ölçek değerleri şunlardır:

| Enum Değeri | Ölçek / Anahtar |
| --- | --- |
| `C_MAJOR_A_MINOR` | Do majör / La minör |
| `D_FLAT_MAJOR_B_FLAT_MINOR` | Re bemol majör / Si bemol minör |
| `D_MAJOR_B_MINOR` | D major / B minor |
| `E_FLAT_MAJOR_C_MINOR` | Mi bemol majör / Do minör |
| `E_MAJOR_D_FLAT_MINOR` | Mi majör / Do diyez/Re bemol minör |
| `F_MAJOR_D_MINOR` | Fa majör / Re minör |
| `G_FLAT_MAJOR_E_FLAT_MINOR` | Sol bemol majör / Mi bemol minör |
| `G_MAJOR_E_MINOR` | Sol majör / Mi minör |
| `A_FLAT_MAJOR_F_MINOR` | La bemol majör / Fa minör |
| `A_MAJOR_G_FLAT_MINOR` | La majör / Fa diyez/Sol bemol minör |
| `B_FLAT_MAJOR_G_MINOR` | Si bemol majör / Sol minör |
| `B_MAJOR_A_FLAT_MINOR` | Si majör / Sol diyez/La bemol minör |
| `SCALE_UNSPECIFIED` | Varsayılan / Model karar verir |

Model, çalınan notlara rehberlik edebilir ancak göreceli tuşlar arasında ayrım yapmaz. Bu nedenle her enum hem göreli büyük hem de göreli küçüğe karşılık gelir. Örneğin, `C_MAJOR_A_MINOR`, piyanodaki tüm beyaz tuşlara, `F_MAJOR_D_MINOR` ise si bemol dışındaki tüm beyaz tuşlara karşılık gelir.

### Sınırlamalar

- Yalnızca enstrümantal: Model yalnızca enstrümantal müzik üretir.
- Güvenlik: İstemler, güvenlik filtreleriyle kontrol edilir. Filtreleri tetikleyen istemler yoksayılır. Bu durumda, çıkışın `filtered_prompt` alanına bir açıklama yazılır.
- Filigran: Çıkış sesi, [Sorumlu Yapay Zeka](https://ai.google/responsibility/principles/?hl=tr) ilkelerimize uygun olarak tanımlama için her zaman filigranlıdır.

## Sırada ne var?

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) ile eksiksiz şarkılar ve vokal parçaları üretin.
- Müzik yerine, [TTS modellerini](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) kullanarak birden fazla konuşmacının yer aldığı sohbetler oluşturmayı öğrenin.
- [Resim](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) veya [video](https://ai.google.dev/gemini-api/docs/video?hl=tr) oluşturmayı öğrenin.
- Müzik veya ses üretmek yerine Gemini'ın [ses dosyalarını nasıl anlayabileceğini](https://ai.google.dev/gemini-api/docs/audio?hl=tr) öğrenin.
- [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)'yi kullanarak Gemini ile gerçek zamanlı sohbet edin.

Daha fazla kod örneği ve eğitim için [Çözüm Kitabı](https://github.com/google-gemini/cookbook)'nı inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-16 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-16 UTC."],[],[]]
