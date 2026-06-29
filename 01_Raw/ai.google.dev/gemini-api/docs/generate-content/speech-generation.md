---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=tr
fetched_at: 2026-06-29T05:33:53.714349+00:00
title: "Metin okuma \u00fcretimi (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Metin okuma üretimi (TTS)

Gemini API, Gemini metin okuma (TTS) oluşturma özelliklerini kullanarak metin girişini tek veya çok hoparlörlü sese dönüştürebilir.
Metin okuma (TTS) üretimi *[kontrol edilebilir](#controllable)*. Bu sayede, etkileşimleri yapılandırmak ve sesin *stilini*, *aksanını*, *hızını* ve *tonunu* yönlendirmek için doğal dil kullanabilirsiniz.

[Google AI Studio'da deneme](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=tr)

TTS özelliği, etkileşimli, yapılandırılmamış ses ve çok formatlı girişler ve çıkışlar için tasarlanan [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) aracılığıyla sağlanan konuşma oluşturma özelliğinden farklıdır. Live API, dinamik sohbet bağlamlarında mükemmel performans gösterirken Gemini API aracılığıyla TTS, stil ve ses üzerinde ayrıntılı kontrolle metnin tam olarak okunmasını gerektiren senaryolar (ör. podcast veya sesli kitap oluşturma) için özel olarak tasarlanmıştır.

Bu kılavuzda, metinden tek konuşmacılı ve çok konuşmacılı seslerin nasıl oluşturulacağı gösterilmektedir.

## Başlamadan önce

[Desteklenen modeller](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#supported-models) bölümünde listelendiği gibi, Gemini metin okuma (TTS) özelliklerine sahip bir Gemini modeli varyantı kullandığınızdan emin olun. En iyi sonuçları elde etmek için hangi modelin kullanım alanınıza en uygun olduğunu belirleyin.

Geliştirmeye başlamadan önce [Gemini TTS modellerini AI Studio'da test etmeniz](https://aistudio.google.com/generate-speech?hl=tr) faydalı olabilir.

## Tek konuşmacılı TTS

Metni tek konuşmacılı sese dönüştürmek için yanıt biçimini "ses" olarak ayarlayın ve `VoiceConfig` ayarlanmış bir `SpeechConfig` nesnesi iletin.
Önceden oluşturulmuş [çıkış sesleri](#voices) arasından bir ses adı seçmeniz gerekir.

Bu örnekte, modelden gelen çıkış sesi bir wave dosyasına kaydedilir:

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

## Birden fazla konuşmacı için TTS

Çok konuşmacılı ses için her konuşmacı (en fazla 2) `SpeakerVoiceConfig` olarak yapılandırılmış bir `MultiSpeakerVoiceConfig` nesnesi gerekir.
Her `speaker` öğesini, [istemde](#controllable) kullanılan adlarla tanımlamanız gerekir:

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

## İstemlerle konuşma stilini kontrol etme

Hem tek hem de çok konuşmacılı TTS için doğal dil istemlerini veya [ses etiketlerini](#transcript-tags) kullanarak stil, ton, vurgu ve hızı kontrol edebilirsiniz.
Örneğin, tek konuşmacılı bir istemde şunları söyleyebilirsiniz:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

Birden fazla konuşmacının yer aldığı istemlerde, her konuşmacının adını ve ilgili transkripti modele sağlayın. Ayrıca her hoparlör için ayrı ayrı rehberlik de sağlayabilirsiniz:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Daha da vurgulamak için, iletmek istediğiniz stile veya duyguya karşılık gelen bir [ses seçeneği](#voices) kullanmayı deneyin. Örneğin, önceki istemde *Enceladus*'un fısıltılı sesi "yorgun" ve "sıkılmış" kelimelerini vurgulayabilirken *Puck*'ın neşeli tonu "heyecanlı" ve "mutlu" kelimelerini tamamlayabilir.

## Sese dönüştürme istemi oluşturma

TTS modelleri yalnızca ses çıkışı verir ancak önce transkript oluşturmak için [diğer modelleri](https://ai.google.dev/gemini-api/docs/models?hl=tr) kullanabilir, ardından bu transkripti TTS modeline aktararak yüksek sesle okutabilirsiniz.

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

## Ses seçenekleri

TTS modelleri, `voice_name` alanında aşağıdaki 30 ses seçeneğini destekler:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Parlak* | **Puck** -- *Upbeat* | **Charon** -- *Bilgilendirici* |
| **Kore** -- *Firm* | **Fenrir** -- *Heyecanlı* | **Leda** -- *Genç* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *Sakin* |
| **Autonoe** -- *Parlak* | **Enceladus** -- *Nefesli* | **Iapetus** -- *Temizle* |
| **Umbriel** -- *Rahat* | **Algieba** -- *Akış sorunsuz* | **Despina** -- *Akıcı* |
| **Erinome** -- *Temizle* | **Algenib** -- *Gravelly* | **Rasalgethi** -- *Bilgilendirici* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Eşit* | **Gacrux** -- *Yetişkin* | **Pulcherrima** -- *Yönlendir* |
| **Achird** -- *Dostu* | **Zubenelgenubi** -- *Basit* | **Vindemiatrix** -- *Nazik* |
| **Sadachbia** -- *Canlı* | **Sadaltager** -- *Bilgili* | **Sulafat** -- *Warm* |

Tüm ses seçeneklerini [AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'da dinleyebilirsiniz.

## Desteklenen diller

TTS modelleri, giriş dilini otomatik olarak algılar. Desteklenen diller:

| Dil | BCP-47 Kodu | Dil | BCP-47 Kodu |
| --- | --- | --- | --- |
| Arapça | ar | Filipince | fil |
| Bengalce | bn | Fince | fi |
| Felemenkçe | nl | Galiçyaca | gl |
| İngilizce | en | Gürcüce | ka |
| Fransızca | fr | Yunanca | el |
| Almanca | de | Güceratça | gu |
| Hintçe | hi | Haiti Creole Dili | ht |
| Endonezce | id | İbranice | o |
| İtalyanca | it | Macarca | hu |
| Japonca | ja | İzlandaca | : |
| Korece | ko | Cava dili | jv |
| Marathi | mr | Kannada | kn |
| Lehçe | pl | Konkani | kok |
| Portekizce | pt | Laoca | lo |
| Rumence | ro | Latince | la |
| Rusça | ru | Letonca | lv |
| İspanyolca | es | Litvanca | lt |
| Tamilce | ta | Lüksemburgca | lb |
| Telugu dili | te | Makedonca | mk |
| Tayca | th | Maithili dili | mai |
| Türkçe | tr | Malgaşça | mg |
| Ukraynaca | uk | Malayca | ms |
| Vietnamca | vi | Malayalam | ml |
| Afrikaanca | af | Moğolca | mn |
| Arnavutça | sq | Nepalce | ne |
| Amharca | öö | Norveççe, Bokmål | nb |
| Ermenice | hy | Norveççe, Yeni Norveççe | nn |
| Azerice | az | Oriya | veya |
| Baskça | eu | Peştuca | ps |
| Belarusça | be | Farsça | fa |
| Bulgarca | bg | Pencapça | pa |
| Burmaca | my | Sırpça | sr |
| Katalanca | ca | Sindice | sd |
| Sabuanca | ceb | Seylanca | si |
| Çince, Mandarin | cmn | Slovakça | sk |
| Hırvatça | s | Slovence | sl |
| Çekya | cs | Swahili | sw |
| Danca | da | İsveççe | sv |
| Estonca | et | Urduca | UR |

## Desteklenen modeller

| Model | Tek konuşmacı | Çok hoparlörlü |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=tr) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=tr) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Önizleme TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=tr) | ✔️ | ✔️ |

## İstem yazma kılavuzu

**Gemini tümleşik ses üretimi Text-to-Speech (TTS)** modeli, ***ne söyleyeceğini değil, nasıl söyleyeceğini de*** bilen bir büyük dil modeli kullanarak geleneksel TTS modellerinden ayrılır.

Model, hazır olarak transkripti doğal bir şekilde yorumlar ve kelimelerinizin nasıl iletilmesi gerektiğini belirler. Ek istem içermeyen basit transkriptler doğal bir şekilde okunur. Ancak Gemini TTS, yönlendirmek için kullanabileceğiniz araçlarla da birlikte gelir.

Bu kılavuzun amacı, ses deneyimleri geliştirirken temel yönlendirme sunmak ve fikirler üretmektir. Hızlı satır içi kontrol için **Etiketler** ile başlayacağız. Ardından, tam performans yönlendirmesi için gelişmiş **İstem yapılarını** inceleyeceğiz.

### Ses etiketleri

Etiketler, yayını ayrıntılı bir şekilde kontrol etmenizi sağlayan `[whispers]` veya `[laughs]` gibi satır içi değiştiricilerdir. Bunları, transkriptin bir satırının veya bölümünün tonunu, hızını ve duygusal atmosferini değiştirmek için kullanabilirsiniz. Ayrıca bu sesleri kullanarak performansa ünlem ve birkaç başka sözel olmayan ses de ekleyebilirsiniz. Örneğin, `[cough]`, `[sighs]` veya `[gasp]`.

Hangi etiketlerin işe yaradığına ve yaramadığına dair kapsamlı bir liste yoktur. Çıkışın nasıl değiştiğini görmek için farklı duygular ve ifadelerle denemeler yapmanızı öneririz.

Transkriptiniz İngilizce değilse en iyi sonuçları elde etmek için yine de İngilizce ses etiketleri kullanmanızı öneririz.

**Ses etiketlerini yaratıcı bir şekilde kullanın**

Ses etiketleriyle elde edebileceğiniz değişkenliği göstermek için, her biri aynı şeyi söyleyen ancak kullanılan etiketlere göre farklı şekilde sunulan bir dizi örnek aşağıda verilmiştir.

Bir satırın başına etiket ekleyerek konuşmacının heyecanlı, sıkılmış veya isteksiz olmasını sağlayıp konuşmanın vurgusunu değiştirebilirsiniz:

- `[excitedly]` Merhaba, ben yeni bir metin okuma modeliyim ve birçok farklı şekilde konuşabilirim. Bugün size nasıl yardımcı olabilirim?
- `[bored]` Merhaba, ben yeni bir metin okuma modeliyim…
- `[reluctantly]` Merhaba, ben yeni bir metin okuma modeliyim…

Etiketler, yayın hızını değiştirmek veya hızı vurguyla birleştirmek için de kullanılabilir:

- `[very fast]` Merhaba, ben yeni bir metin okuma modeliyim…
- `[very slow]` Merhaba, ben yeni bir metin okuma modeliyim…
- `[sarcastically, one painfully slow word at a time]` Merhaba, ben yeni bir metin okuma modeliyim…

Ayrıca belirli bölümler üzerinde hassas kontrol sahibi olursunuz. Yani bir bölümü fısıldayabilir, diğerini bağırabilirsiniz.

- `[whispers]` Merhaba, ben yeni bir metin okuma modeliyim `[shouting]` ve birçok farklı şekilde konuşabilirim. `[whispers]` Bugün size nasıl yardımcı olabilirim?

Dilediğiniz reklam öğesi fikrini de deneyebilirsiniz:

- `[like a cartoon dog]` Merhaba, ben yeni bir metin okuma modeliyim…
- `[like dracula]` Merhaba, ben yeni bir metin okuma modeliyim…

En çok tercih edilen etiketler şunlardır:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Etiketler, transkriptinizin yayınlanması üzerinde hızlı ve kolay kontrol sağlar. Daha da fazla kontrol için bunları bir bağlam istemiyle birleştirerek performansın genel tonunu ve atmosferini ayarlayabilirsiniz.

### Gelişmiş istemler

Gelişmiş istemleri, modelin uyması gereken bir sistem talimatı olarak düşünebilirsiniz. Bu, modele daha fazla bağlam sunmanın ve performansı kontrol etmenin bir yoludur.

Güçlü bir istem, ideal olarak mükemmel bir performans oluşturmak için bir araya gelen aşağıdaki öğeleri içerir:

- **Ses Profili**: Ses için bir karakter oluşturur. Karakter kimliğini, arketipini ve yaş, geçmiş vb. diğer özellikleri tanımlar.
- **Sahne**: Ortamı hazırlar. Hem fiziksel ortamı hem de "atmosferi" açıklar.
- **Yönetmen Notları**: Sanal karakterinizin dikkate alması gereken talimatları ayrıntılı olarak inceleyebileceğiniz performans rehberliği. Örnekler arasında stil, nefes, tempo, telaffuz ve vurgu yer alır.
- **Örnek bağlam**: Modele bağlamsal bir başlangıç noktası sağlar. Böylece sanal aktörünüz, oluşturduğunuz sahneye doğal bir şekilde girer.
- **Transkript**: Modelin seslendireceği metin. En iyi performans için transkript konusunun ve yazım stilinin verdiğiniz talimatlarla ilişkili olması gerektiğini unutmayın.
- **Ses etiketleri**: Metnin ilgili bölümünün nasıl okunacağını değiştirmek için transkripte ekleyebileceğiniz değiştiricilerdir (ör. `[whispers]` veya `[shouting]`).

Tam istem örneği:

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

### Ayrıntılı istem stratejileri

İstemin her bir öğesini inceleyelim.

#### Ses Profili

Karakterin kişiliğini kısaca açıklayın.

- **Ad.** Karakterinize ad vermek, modeli ve performansını bir araya getirmenize yardımcı olur. Sahneyi ve bağlamı ayarlarken karakterden adıyla bahsedin.
- **Rol** Sahnedeki karakterin temel kimliği ve arketipi. Örneğin, radyo DJ'i, podcast yayıncısı, haber muhabiri vb.

Örnekler:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Sahne

Konum, ruh hali ve ortamla ilgili ayrıntılar da dahil olmak üzere sahnenin bağlamını belirleyin. Bu ayrıntılar, tonu ve atmosferi oluşturur. Karakterin etrafında neler olduğunu ve bunun karakteri nasıl etkilediğini açıklayın. Sahne, etkileşimin tamamı için çevresel bağlamı sağlar ve oyunculuk performansını ince ve doğal bir şekilde yönlendirir.

Örnekler:

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

#### Yönetmen notları

Bu önemli bölümde, performansla ilgili özel yönergeler yer alır. Diğer tüm öğeleri atlayabilirsiniz ancak bu öğeyi eklemenizi öneririz.

Yalnızca performans için önemli olanı tanımlayın ve aşırı belirtmemeye dikkat edin. Çok fazla katı kural, modellerin yaratıcılığını sınırlar ve daha kötü bir performansa yol açabilir. Rol ve sahne açıklamasını, belirli performans kurallarıyla dengeleyin.

En yaygın talimatlar **Stil, Tempo ve Vurgu**'dur ancak model bunlarla sınırlı değildir ve bunları gerektirmez. Performansınız için önemli olan ek ayrıntıları kapsayacak özel talimatlar ekleyebilir ve gerektiği kadar ayrıntılı veya az bilgi verebilirsiniz.

Örneğin:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Stil:**

Oluşturulan konuşmanın üslubunu ve stilini belirler. Performansa yön vermek için neşeli, enerjik, rahat, sıkılmış gibi ifadeler ekleyin. Açıklayıcı olun ve gerektiği kadar ayrıntı verin: *"Bulaşıcı bir coşku. Dinleyici, büyük ve heyecan verici bir topluluk etkinliğinin parçası olduğunu hissetmeli."* ifadesi, *"Enerjik ve coşkulu"* ifadesinden daha iyi sonuç veriyor.

Hatta seslendirme sektöründe popüler olan "vokal gülümsemesi" gibi terimleri de deneyebilirsiniz. İstediğiniz sayıda stil özelliği ekleyebilirsiniz.

Örnekler:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Daha fazla derinlik

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Karmaşık

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Aksan:**

İstediğiniz aksanı açıklayın. Ne kadar ayrıntılı olursanız sonuçlar o kadar iyi olur. Örneğin, "*British English accent as heard in Croydon,
England*" (İngiltere, Croydon'da duyulan İngiliz İngilizcesi aksanı) yerine "*British Accent*" (İngiliz aksanı) kullanın.

Örnekler:

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

**İlerleme hızı:**

Parça boyunca genel tempo ve tempo değişimi.

Örnekler:

Basit

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Daha fazla derinlik

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Karmaşık

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Transkript ve ses etiketleri

Transkript, modelin konuşacağı kelimelerin bire bir aynısıdır. Ses etiketi, bir şeyin nasıl söylenmesi gerektiğini, ton değişikliğini veya ünlemi belirten, köşeli parantez içindeki bir kelimedir.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Deneyin**

[AI Studio](https://aistudio.google.com/generate-speech?hl=tr)'da bu örneklerden bazılarını kendiniz deneyin, [TTS uygulamamızla](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=tr) oynayın ve Gemini'ın sizi yönetmen koltuğuna oturtmasına izin verin. Harika vokal performansları için şu ipuçlarını aklınızda bulundurun:

- Tüm istemin tutarlı olmasına dikkat edin. Senaryo ve yönlendirme, harika bir performans oluşturmak için birlikte çalışır.
- Her şeyi açıklamanız gerekmez. Bazen boşlukları doldurması için modele alan bırakmak doğallığa yardımcı olur. (Tıpkı yetenekli bir oyuncu gibi)
- Takıldığınız noktalarda Gemini'dan yardım alarak senaryonuzu veya performansınızı şekillendirebilirsiniz.

## Gerçek zamanlı konuşma üretme

Oluşturulan sesi, model tarafından oluşturulurken yayınlayabilirsiniz. Bu özellik, algılanan gecikmeyi azaltmak için kullanışlıdır.

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

## Sınırlamalar

- TTS modelleri yalnızca metin girişleri alabilir ve ses çıkışları oluşturabilir.
- TTS oturumunun [bağlam penceresi](https://ai.google.dev/gemini-api/docs/long-context?hl=tr) sınırı 32 bin jetondur.
- Dil desteği için [Diller](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#languages) bölümünü inceleyin.
- TTS, 3.1 sürümünden eski modellerde akışı desteklemez (`gemini-3.1-flash-tts-preview` ve daha yeni sürümlerde akış desteklenir).

Konuşma üretimi için Gemini 3.1 Flash TTS Önizleme modeli kullanılırken özellikle aşağıdaki kısıtlamalar geçerlidir:

- **İstem talimatlarıyla tutarsız ses:** Modelin çıktısı her zaman seçilen konuşmacıyla tam olarak eşleşmeyebilir. Bu durumda ses, beklenenden farklı duyulur. Uyumsuz tonları (ör. genç bir kız gibi konuşmaya çalışan derin bir erkek sesi) önlemek için isteminizin yazılı tonunun ve bağlamının, seçilen konuşmacının profiliyle doğal olarak uyumlu olduğundan emin olun.
- **Daha uzun çıkışların kalitesi:** Konuşma kalitesi ve tutarlılığı, birkaç dakikadan uzun olan oluşturulmuş çıkışlarda değişmeye başlayabilir. Transkriptlerinizi daha küçük parçalara bölmenizi öneririz.
- **Bazen metin belirteçleri döndürülüyor:** Model, bazen ses belirteçleri yerine metin belirteçleri döndürdüğü için sunucu, isteği `500` hatasıyla reddediyor. Bu durum, isteklerin çok küçük bir yüzdesinde rastgele gerçekleştiğinden, bu durumları işlemek için uygulamanızda otomatik yeniden deneme mantığı uygulamanız gerekir.
- **İstem sınıflandırıcısının yanlış reddetmeleri:** Belirsiz istemler, konuşma sentezi sınıflandırıcısını tetikleyemeyebilir. Bu durumda istek reddedilir (`PROHIBITED_CONTENT`) veya model, stil talimatlarınızı ve yönetmen notlarınızı yüksek sesle okur. Modele konuşma sentezleme talimatı veren net bir giriş ekleyerek ve gerçek konuşulan transkriptin başladığı yeri açıkça etiketleyerek istemlerinizi doğrulayın.

## Sırada ne var?

- [Ses üreten model çözüm kitabını](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=tr) deneyin.
- Gemini'ın [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr)'si, diğer yöntemlerle birlikte kullanabileceğiniz etkileşimli ses üretme seçenekleri sunar.
- Ses *girişleriyle* çalışma hakkında bilgi edinmek için [Ses yorumlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr) rehberini inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-28 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-28 UTC."],[],[]]
