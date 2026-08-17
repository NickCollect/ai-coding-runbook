---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=id
fetched_at: 2026-08-17T02:30:52.145811+00:00
title: "Pembuatan text-to-speech (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Pembuatan text-to-speech (TTS)

Gemini API dapat mengubah input teks menjadi audio satu penutur atau multi-penutur menggunakan kemampuan pembuatan text-to-speech (TTS) Gemini.
Pembuatan text-to-speech (TTS) dapat *[dikontrol](#controllable)*,
artinya Anda dapat menggunakan bahasa alami untuk menyusun interaksi dan memandu *gaya*, *aksen*, *kecepatan*, dan *nada* audio.

[Coba di Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=id)

Kemampuan TTS berbeda dengan pembuatan ucapan yang disediakan melalui
[Live API](https://ai.google.dev/gemini-api/docs/live?hl=id), yang dirancang untuk input dan output multimodal, serta audio interaktif dan tidak terstruktur. Meskipun Live API unggul dalam konteks percakapan dinamis, TTS melalui Gemini API disesuaikan untuk skenario yang memerlukan pembacaan teks yang tepat dengan kontrol gaya dan suara yang cermat, seperti pembuatan podcast atau buku audio.

Panduan ini menunjukkan cara membuat audio satu pembicara dan beberapa pembicara dari
teks.

## Sebelum memulai

Pastikan Anda menggunakan varian model Gemini dengan kemampuan text-to-speech (TTS) Gemini, seperti yang tercantum di bagian [Model yang didukung](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id#supported-models). Untuk hasil yang optimal, pertimbangkan model mana yang paling sesuai dengan kasus penggunaan spesifik Anda.

Anda mungkin merasa perlu [menguji model TTS Gemini di AI Studio](https://aistudio.google.com/generate-speech?hl=id) sebelum mulai membangun.

## TTS satu penutur

Untuk mengonversi teks menjadi audio satu penutur, tetapkan modalitas respons ke "audio",
dan teruskan objek `SpeechConfig` dengan `VoiceConfig` yang ditetapkan.
Anda harus memilih nama suara dari [suara output](#voices) bawaan.

Contoh ini menyimpan audio output dari model dalam file wave:

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

## TTS multi-penutur

Untuk audio multi-pembicara, Anda memerlukan objek `MultiSpeakerVoiceConfig` dengan
setiap pembicara (hingga 2) yang dikonfigurasi sebagai `SpeakerVoiceConfig`.
Anda harus menentukan setiap `speaker` dengan nama yang sama yang digunakan dalam
[prompt](#controllable):

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

## Mengontrol gaya ucapan dengan perintah

Anda dapat mengontrol gaya, intonasi, aksen, dan kecepatan menggunakan perintah bahasa alami atau [tag audio](#transcript-tags) untuk TTS satu penutur dan multi-penutur.
Misalnya, dalam perintah satu penutur, Anda dapat mengucapkan:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

Dalam perintah multi-pembicara, berikan nama setiap pembicara dan transkrip yang sesuai kepada model. Anda juga dapat memberikan panduan untuk setiap pembicara secara terpisah:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Coba gunakan [opsi suara](#voices) yang sesuai dengan gaya atau emosi yang ingin Anda sampaikan, untuk lebih menekankannya. Misalnya, dalam perintah sebelumnya,
keberingasan *Enceladus* dapat menekankan "lelah" dan "bosan", sementara
nada riang *Puck* dapat melengkapi "bersemangat" dan "bahagia".

## Membuat perintah untuk mengonversi ke audio

Model TTS hanya menghasilkan output audio, tetapi Anda dapat menggunakan
[model lain](https://ai.google.dev/gemini-api/docs/models?hl=id) untuk membuat transkrip terlebih dahulu,
lalu meneruskan transkrip tersebut ke model TTS untuk dibacakan.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

transcript = client.models.generate_content(
   model="gemini-3.6-flash",
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
   model: "gemini-3.6-flash",
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

## Pilihan suara

Model TTS mendukung 30 opsi suara berikut di kolom `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** -- *Bright* | **Puck** -- *Ceria* | **Charon** -- *Informatif* |
| **Kore** -- *Firm* | **Fenrir** -- *Mudah Terangsang (Excitable)* | **Leda** -- *Muda* |
| **Orus** -- *Firm* | **Aoede** -- *Breezy* | **Callirrhoe** -- *Santai* |
| **Autonoe** -- *Bright* | **Enceladus** -- *Breathy* | **Iapetus** -- *Jelas* |
| **Umbriel** -- *Santai* | **Algieba** -- *Halus (Smooth)* | **Despina** -- *Halus (Smooth)* |
| **Erinome** -- *Clear* | **Algenib** -- *Berbatu* | **Rasalgethi** -- *Informatif* |
| **Laomedeia** -- *Upbeat* | **Achernar** -- *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** -- *Dewasa* | **Pulcherrima** -- *Meneruskan* |
| **Achird** -- *Ramah* | **Zubenelgenubi** -- *Kasual* | **Vindemiatrix** -- *Lembut (Gentle)* |
| **Sadachbia** -- *Lively* | **Sadaltager** -- *Berpengetahuan* | **Sulafat** -- *Hangat* |

Anda dapat mendengar semua opsi suara di
[AI Studio](https://aistudio.google.com/generate-speech?hl=id).

## Bahasa yang didukung

Model TTS mendeteksi bahasa input secara otomatis. Bahasa berikut didukung:

| Language | Kode BCP-47 | Language | Kode BCP-47 |
| --- | --- | --- | --- |
| Arab | ar | Filipino | fil |
| Bangla | bn | Finlandia | fi |
| Belanda | nl | Galisia | gl |
| Inggris | en | Georgia | ka |
| Prancis | fr | Yunani | el |
| Jerman | de | Gujarat | gu |
| Hindi | hi | Kreol Haiti | ht |
| Indonesia | id | Ibrani | dia |
| Italia | it | Hungaria | hu |
| Jepang | ja | Islandia | is |
| Korea | ko | Jawa | jv |
| Marathi | mr | Kannada | kn |
| Polandia | pl | Konkani | kok |
| Portugis | pt | Laos | lo |
| Rumania | ro | Latin | la |
| Rusia | ru | Latvia | lv |
| Spanyol | es | Lituania | lt |
| Tamil | ta | Luksemburg | lb |
| Telugu | te | Makedonia | mk |
| Thai | th | Maithili | mai |
| Turkiye | tr | Malagasi | mg |
| Ukraina | uk | Melayu | md |
| Vietnam | vi | Malayalam | ml |
| Afrika | af | Mongolia | mn |
| Albania | sq | Nepal | ne |
| Amharik | am | Norwegia, Bokmål | nb |
| Armenia | hy | Norwegia, Nynorsk | nn |
| Azerbaijan | az | Odia | atau |
| Basque | eu | Pashto | ps |
| Belarusia | be | Persia | fa |
| Bulgaria | bg | Punjabi | pa |
| Burma | my | Serbia | sr |
| Katalan | ca | Sindhi | sd |
| Cebuano | ceb | Sinhala | si |
| China, Mandarin | cmn | Slovakia | sk |
| Kroasia | jam | Slovenia | sl |
| Ceko | cs | Swahili | sw |
| Denmark | da | Swedia | sv |
| Estonia | et | Urdu | ur |

## Model yang didukung

| Model | Satu penutur | Multi-penutur |
| --- | --- | --- |
| [Pratinjau Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=id) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=id) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=id) | ✔️ | ✔️ |

## Panduan penulisan perintah

Model **Gemini Native Audio Generation Text-to-Speech (TTS)** berbeda
dengan model TTS tradisional karena menggunakan model bahasa besar yang
mengetahui ***tidak hanya apa yang harus diucapkan, tetapi juga cara mengucapkannya***.

Secara langsung, model akan menafsirkan transkrip dan menentukan cara
kata-kata Anda harus disampaikan. Transkrip sederhana tanpa perintah tambahan
terdengar alami. Namun, Gemini TTS juga dilengkapi dengan alat yang dapat Anda gunakan untuk
mengarahkan outputnya.

Tujuan panduan ini adalah untuk memberikan arahan mendasar dan memicu ide saat mengembangkan pengalaman audio. Kita akan mulai dengan **Tag** untuk kontrol inline cepat, lalu mempelajari **Struktur perintah** lanjutan untuk arahan performa penuh.

### Tag audio

Tag adalah pengubah inline seperti `[whispers]` atau `[laughs]` yang memberi Anda kontrol terperinci atas penayangan. Anda dapat menggunakannya untuk mengubah nada, kecepatan, dan
nuansa emosional baris atau bagian transkrip. Anda juga dapat menggunakannya untuk
menambahkan interjeksi dan beberapa suara non-verbal lainnya ke dalam performa, seperti
`[cough]`, `[sighs]`, atau `[gasp]`.

Tidak ada daftar lengkap tentang tag yang berfungsi dan tidak berfungsi. Sebaiknya lakukan eksperimen dengan berbagai emosi dan ekspresi untuk melihat perubahan outputnya.

Jika transkrip Anda tidak dalam bahasa Inggris, untuk hasil terbaik, sebaiknya Anda tetap menggunakan tag audio dalam bahasa Inggris.

**Berkreasilah dengan tag audio**

Untuk menunjukkan jenis variabilitas yang bisa Anda dapatkan dengan tag audio, berikut adalah serangkaian contoh yang masing-masing mengatakan hal yang sama, tetapi penyampaiannya berubah berdasarkan tag yang digunakan.

Anda dapat mengubah penekanan penyampaian dengan menambahkan tag di awal baris untuk membuat pembicara bersemangat, bosan, atau enggan:

- `[excitedly]` Halo, saya adalah model text-to-speech baru, dan saya dapat mengucapkan kata-kata dengan berbagai cara. Ada yang bisa saya bantu?
- `[bored]` Halo, saya adalah model text-to-speech baru…
- `[reluctantly]` Halo, saya adalah model text-to-speech baru…

Tag juga dapat digunakan untuk mengubah kecepatan penayangan, atau untuk menggabungkan kecepatan dengan penekanan:

- `[very fast]` Halo, saya adalah model text-to-speech baru…
- `[very slow]` Halo, saya adalah model text-to-speech baru…
- `[sarcastically, one painfully slow word at a time]` Halo, saya adalah model text-to-speech baru…

Anda juga memiliki kontrol yang akurat atas bagian tertentu, yang berarti Anda dapat membisikkan
satu bagian dan meneriakkan bagian lainnya.

- `[whispers]` Halo, saya adalah model text to speech baru, `[shouting]` dan saya dapat
  mengucapkan berbagai hal dengan banyak cara yang berbeda. `[whispers]` Ada yang bisa saya bantu?

Anda juga dapat bereksperimen dengan ide kreatif apa pun yang Anda inginkan:

- `[like a cartoon dog]` Halo, saya adalah model text-to-speech baru…
- `[like dracula]` Halo, saya adalah model text-to-speech baru…

Tag yang umum digunakan meliputi:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Tag memberikan kontrol yang cepat dan mudah atas pengiriman transkrip Anda. Untuk kontrol yang lebih besar, Anda dapat menggabungkannya dengan perintah konteks untuk menetapkan keseluruhan nada dan nuansa performa.

### Penulisan perintah lanjutan

Anda dapat menganggap perintah lanjutan sebagai petunjuk sistem yang harus diikuti model. Ini adalah cara untuk memberikan lebih banyak konteks dan kontrol atas performa model.

Perintah yang efektif idealnya mencakup elemen berikut yang digabungkan untuk menghasilkan performa yang luar biasa:

- **Profil Audio** - Menetapkan persona untuk suara, menentukan identitas karakter, arketipe, dan karakteristik lainnya seperti usia, latar belakang, dll.
- **Adegan** - Menyiapkan latar. Mendeskripsikan lingkungan fisik dan "suasana".
- **Catatan Sutradara** - Panduan performa tempat Anda dapat menguraikan petunjuk mana yang penting untuk diperhatikan oleh talenta virtual Anda. Contohnya adalah
  gaya, pernapasan, kecepatan, artikulasi, dan aksen.
- **Contoh konteks** - Memberi model titik awal kontekstual, sehingga aktor virtual Anda memasuki adegan yang Anda siapkan secara alami.
- **Transkrip** - Teks yang akan diucapkan oleh model. Untuk performa terbaik,
  ingatlah bahwa topik transkrip dan gaya penulisan harus berkorelasi dengan
  petunjuk yang Anda berikan.
- **Tag audio** - Pengubah yang dapat Anda masukkan ke dalam transkrip untuk mengubah cara penyampaian bagian teks tersebut, seperti `[whispers]` atau `[shouting]`.

Contoh perintah lengkap:

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

### Strategi penulisan perintah yang mendetail

Mari kita uraikan setiap elemen perintah.

#### Profil Audio

Jelaskan secara singkat persona karakter.

- **Nama.** Memberi nama karakter membantu menyatukan model dan performa yang ketat. Sebutkan karakter dengan namanya saat mengatur adegan dan konteks
- **Peran.** Identitas inti dan arketipe karakter yang ditampilkan dalam adegan. Misalnya, DJ Radio, Podcaster, Reporter berita, dll.

Contoh:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scene

Tetapkan konteks untuk adegan, termasuk lokasi, suasana, dan detail lingkungan yang menentukan nuansa dan suasana. Jelaskan apa yang terjadi di sekitar karakter
dan dampaknya. Adegan memberikan konteks lingkungan
untuk seluruh interaksi dan memandu performa akting dengan cara yang halus
dan alami.

Contoh:

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

#### Catatan sutradara

Bagian penting ini mencakup panduan performa tertentu. Anda dapat melewati semua
elemen lainnya, tetapi sebaiknya sertakan elemen ini.

Tentukan hanya hal yang penting untuk performa, dengan berhati-hati agar tidak
menspesifikasikan secara berlebihan. Terlalu banyak aturan ketat akan membatasi kreativitas model dan dapat menghasilkan performa yang lebih buruk. Seimbangkan deskripsi peran dan adegan dengan
aturan performa tertentu.

Arahannya yang paling umum adalah **Gaya, Kecepatan, dan Aksen**, tetapi model tidak terbatas pada hal ini, dan tidak memerlukannya. Jangan ragu untuk menyertakan petunjuk kustom untuk mencakup detail tambahan yang penting bagi performa Anda, dan berikan detail sebanyak atau sesedikit yang diperlukan.

Contoh:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Gaya:**

Menetapkan nada dan Gaya ucapan yang dihasilkan. Sertakan hal-hal seperti bersemangat,
penuh energi, santai, bosan, dll. untuk memandu performa. Berikan deskripsi dan
berikan detail sebanyak yang diperlukan: *"Antusiasme yang menular. Pendengar
harus merasa seperti mereka adalah bagian dari acara komunitas yang besar dan menarik."* lebih baik
daripada hanya mengatakan *"bersemangat dan antusias".*

Anda bahkan dapat mencoba istilah yang populer di industri voiceover, seperti "senyum vokal". Anda dapat menyusun karakteristik gaya sebanyak yang Anda inginkan.

Contoh:

Emosi Sederhana

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Lebih dalam

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Kompleks

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Aksen:**

Jelaskan aksen yang diinginkan. Makin spesifik perintah Anda, makin baik hasilnya. Misalnya, gunakan "*Aksen Inggris Britania seperti yang terdengar di Croydon, Inggris*" vs. "*Aksen Inggris Britania*".

Contoh:

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

**Kecepatan:**

Kecepatan keseluruhan dan variasi kecepatan di seluruh bagian.

Contoh:

Sederhana

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Lebih Dalam

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Kompleks

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Transkrip dan tag audio

Transkrip adalah kata-kata persis yang akan diucapkan model. Tag audio adalah kata
dalam tanda kurung siku yang menunjukkan cara mengucapkan sesuatu, perubahan
nada, atau kata seru.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Coba deh**

Coba sendiri beberapa contoh ini di [AI Studio](https://aistudio.google.com/generate-speech?hl=id), gunakan [Aplikasi TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=id) kami, dan biarkan Gemini memandu Anda. Ingatlah tips berikut untuk menghasilkan performa vokal yang luar biasa:

- Ingatlah untuk menjaga seluruh perintah tetap koheren – skrip dan arahan saling terkait dalam menciptakan performa yang hebat.
- Anda tidak perlu menjelaskan semuanya. Terkadang, memberikan ruang bagi model untuk mengisi kekosongan akan membantu kealamian. (Sama seperti aktor berbakat)
- Jika Anda merasa kesulitan, minta bantuan Gemini untuk menyusun naskah atau penampilan Anda.

## Pembuatan ucapan saat streaming

Anda dapat melakukan streaming audio yang dihasilkan saat audio tersebut dibuat oleh model. Hal ini berguna untuk mengurangi latensi yang dirasakan.

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

## Batasan

- Model TTS hanya dapat menerima input teks dan menghasilkan output audio.
- Sesi TTS memiliki batas [jendela konteks](https://ai.google.dev/gemini-api/docs/long-context?hl=id) sebesar
  32 ribu token.
- Tinjau bagian [Bahasa](https://ai.google.dev/gemini-api/docs/speech-generation?hl=id#languages) untuk mengetahui dukungan bahasa.
- TTS tidak mendukung streaming untuk model yang lebih lama dari versi 3.1 (streaming didukung untuk `gemini-3.1-flash-tts-preview` dan yang lebih baru).

Batasan berikut berlaku secara khusus saat menggunakan model Gemini 3.1 Flash TTS Preview untuk pembuatan ucapan:

- **Suara tidak konsisten dengan petunjuk perintah:** Output model mungkin tidak selalu cocok dengan speaker yang dipilih, sehingga audio terdengar berbeda dari yang diharapkan. Untuk menghindari nada yang tidak cocok (seperti suara pria dewasa yang mencoba berbicara seperti gadis kecil), pastikan nada dan konteks tertulis perintah Anda selaras secara alami dengan profil penutur yang dipilih.
- **Kualitas output yang lebih panjang:** Kualitas dan konsistensi ucapan dapat mulai
  berubah dengan output yang dihasilkan yang lebih panjang dari beberapa menit. Sebaiknya bagi transkrip Anda menjadi beberapa bagian yang lebih kecil.
- **Token teks yang terkadang ditampilkan:** Model terkadang menampilkan token teks, bukan token audio, sehingga menyebabkan server gagal memenuhi permintaan dengan error `500`. Karena hal ini terjadi secara acak dalam persentase permintaan yang sangat kecil, Anda harus menerapkan logika coba lagi otomatis di aplikasi Anda untuk menanganinya.
- **Penolakan palsu pengklasifikasi perintah:** Perintah yang tidak jelas dapat gagal memicu pengklasifikasi sintesis ucapan, sehingga permintaan ditolak (`PROHIBITED_CONTENT`) atau menyebabkan model membaca petunjuk gaya dan catatan sutradara Anda dengan keras. Validasi perintah Anda dengan menambahkan pengantar yang jelas yang menginstruksikan model untuk menyintesis ucapan, dan secara eksplisit memberi label di mana transkrip ucapan sebenarnya dimulai.

## Langkah berikutnya

- Coba [cookbook pembuatan audio](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=id).
- [Live API](https://ai.google.dev/gemini-api/docs/live?hl=id) Gemini menawarkan opsi pembuatan audio interaktif yang dapat Anda selingi dengan modalitas lain.
- Untuk bekerja dengan *input* audio, buka panduan [Audio understanding](https://ai.google.dev/gemini-api/docs/audio?hl=id).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-07-30 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-07-30 UTC."],[],[]]
