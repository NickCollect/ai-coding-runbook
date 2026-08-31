---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=pl
fetched_at: 2026-08-31T06:42:10.323537+00:00
title: "Generowanie tekstu na mow\u0119 (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Generowanie tekstu na mowę (TTS)

Interfejs Gemini API może przekształcać tekst wejściowy w dźwięk z jednym lub wieloma mówcami za pomocą funkcji generowania tekstu na mowę (TTS) Gemini.
Generowanie tekstu na mowę (TTS) jest *[kontrolowane](#controllable)*, co oznacza, że możesz używać języka naturalnego do strukturyzowania interakcji i określania *stylu*, *akcentu*, *tempa* i *tonu* dźwięku.

[Wypróbuj w Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=pl)

Funkcja TTS różni się od generowania mowy za pomocą [interfejsu Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl), który jest przeznaczony do interaktywnych, nieustrukturyzowanych danych audio oraz multimodalnych danych wejściowych i wyjściowych. Interfejs Live API sprawdza się w dynamicznych kontekstach konwersacyjnych, a TTS za pomocą interfejsu Gemini API jest dostosowany do scenariuszy, które wymagają dokładnego odczytania tekstu z precyzyjną kontrolą stylu i dźwięku, takich jak generowanie podcastów lub audiobooków.

Z tego przewodnika dowiesz się, jak generować dźwięk z tekstu dla jednego lub wielu mówców.

## Zanim zaczniesz

Używaj wariantu modelu Gemini z funkcjami zamiany tekstu na mowę (TTS) Gemini, jak podano w sekcji [Obsługiwane modele](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#supported-models). Aby uzyskać optymalne wyniki, zastanów się, który model najlepiej pasuje do Twojego konkretnego przypadku użycia.

Zanim zaczniesz tworzyć, możesz [przetestować modele TTS Gemini w AI Studio](https://aistudio.google.com/generate-speech?hl=pl).

## TTS z jednym głosem

Aby przekonwertować tekst na dźwięk z jednym mówcą, ustaw tryb odpowiedzi na „audio” i przekaż obiekt `SpeechConfig` z ustawionym parametrem `VoiceConfig`.
Musisz wybrać nazwę głosu z gotowych [głosów wyjściowych](#voices).

W tym przykładzie zapisujemy wyjściowy dźwięk z modelu w pliku wave:

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

## TTS z wieloma rozmówcami

W przypadku dźwięku z wielu głośników potrzebny jest obiekt `MultiSpeakerVoiceConfig`, w którym każdy głośnik (maksymalnie 2) jest skonfigurowany jako `SpeakerVoiceConfig`.
Każdy parametr `speaker` musisz zdefiniować za pomocą tych samych nazw, które zostały użyte w [prompcie](#controllable):

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

## Sterowanie stylem mowy za pomocą promptów

Możesz kontrolować styl, ton, akcent i tempo za pomocą promptów w języku naturalnym lub [tagów audio](#transcript-tags) w przypadku zamiany tekstu na mowę z jednym lub wieloma mówcami.
Na przykład w prompcie z jednym mówcą możesz powiedzieć:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

W prompcie z wieloma osobami mówiącymi podaj modelowi imię każdej z nich i odpowiednią transkrypcję. Możesz też podać wskazówki dla każdego głośnika z osobna:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Aby jeszcze bardziej podkreślić styl lub emocje, które chcesz przekazać, użyj [opcji głosu](#voices), która do nich pasuje. Na przykład w poprzednim prompcie *Enceladus* może podkreślać słowa „zmęczony” i „znudzony”, a *Puck* może uzupełniać słowa „podekscytowany” i „szczęśliwy”.

## Generowanie prompta do przekształcenia w dźwięk

Modele TTS generują tylko dźwięk, ale możesz użyć [innych modeli](https://ai.google.dev/gemini-api/docs/models?hl=pl), aby najpierw wygenerować transkrypcję, a potem przekazać ją do modelu TTS, który ją odczyta.

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

## Opcje głosowe

Modele TTS obsługują te 30 opcji głosowych w polu `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** – *jasny* | **Puck** – *Upbeat* | **Charon** – *Zawiera przydatne informacje* |
| **Kore** – *firma* | **Fenrir** – *pobudliwy* | **Leda** -- *Youthful* |
| **Orus** – *firma* | **Aoede** – *Breezy* | **Callirrhoe** – *spokojny* |
| **Autonoe** – *jasny* | **Enceladus** – *Breathy* | **Iapetus** – *Clear* |
| **Umbriel** – *spokojny* | **Algieba** – *Smooth* | **Despina** – *Smooth* |
| **Erinome** – *przezroczysty* | **Algenib** – *żwirowy* | **Rasalgethi** – *zawiera przydatne informacje* |
| **Laomedeia** – *Upbeat* | **Achernar** – *miękka* | **Alnilam** – *Firm* |
| **Schedar** – *Równomierna* | **Gacrux** – *treści dla dorosłych* | **Pulcherrima** – *Przekaż dalej* |
| **Achird** – *przyjazny* | **Zubenelgenubi** – *zwykłe* | **Vindemiatrix** – *łagodna* |
| **Sadachbia** – *Lively* | **Sadaltager** – *wiedza* | **Sulafat** – *ciepły* |

Wszystkie opcje głosowe możesz usłyszeć w [AI Studio](https://aistudio.google.com/generate-speech?hl=pl).

## Obsługiwane języki

Modele TTS automatycznie wykrywają język wejściowy. Obsługiwane języki:

| Język | Kod BCP-47 | Język | Kod BCP-47 |
| --- | --- | --- | --- |
| arabski | ar | filipiński | fil |
| bengalski | bn | fiński | fi |
| niderlandzki | nl | galicyjski | gl |
| angielski | en | gruziński | ka |
| francuski | fr | grecki | el |
| niemiecki | de | gudżarati | gu |
| hindi | hi | kreolski haitański | ht |
| indonezyjski | id | hebrajski | on |
| włoski | it | węgierski | hu |
| japoński | ja | islandzki | jest |
| koreański | ko | jawajski | jv |
| marathi | mr | kannada | kn |
| polski | pl | konkani | kok |
| portugalski | pt | laotański | lo |
| rumuński | ro | łaciński | la |
| rosyjski | ru | łotewski | lv |
| hiszpański | es | litewski | lt |
| tamilski | ta | luksemburski | lb |
| telugu | te | macedoński | mk |
| tajski | th | maithili | mai |
| turecki | tr | malgaski | mg |
| ukraiński | uk | malajski | ms |
| wietnamski | vi | malajalam | ml |
| afrikaans | af | mongolski | mn |
| albański | sq | nepalski | ne |
| amharski | am | norweski (bokmål), | nb |
| ormiański | hy | norweski (nynorsk), | nn |
| azerski | az | orija | lub |
| baskijski | eu | paszto | ps |
| białoruski | be | perski | fa |
| bułgarski | bg | pendżabski | pa |
| birmański | my | serbski | sr |
| kataloński | ca | sindhi | sd |
| cebuański | ceb | syngaleski | si |
| chiński (mandaryński), | cmn | słowacki | sk |
| chorwacki | h | słoweński | sl |
| czeski | cs | suahili | sw |
| duński | da | szwedzki | sv |
| estoński | et | urdu | ur |

## Obsługiwane modele

| Model | Pojedynczy rozmówca | Wielogłośnikowy |
| --- | --- | --- |
| [Gemini 3.1 Flash TTS (wersja testowa)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=pl) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=pl) | ✔️ | ✔️ |
| [Wersja testowa Gemini 2.5 Pro TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=pl) | ✔️ | ✔️ |

## Przewodnik po promptach

Model **Gemini Native Audio Generation Text-to-Speech (TTS)** różni się od tradycyjnych modeli TTS tym, że korzysta z dużego modelu językowego, który wie ***nie tylko co powiedzieć, ale też jak to zrobić***.

Model od razu zinterpretuje transkrypcję i określi, jak powinny być wypowiadane słowa. Proste transkrypcje bez dodatkowych promptów brzmią naturalnie. Ale Gemini TTS ma też narzędzia, których możesz używać do sterowania nim.

Celem tego przewodnika jest dostarczenie podstawowych wskazówek i inspiracji podczas tworzenia treści audio. Zaczniemy od **tagów**, które umożliwiają szybkie sterowanie w tekście, a potem przejdziemy do zaawansowanych **struktur promptów**, które pozwalają w pełni kontrolować wydajność.

### Tagi audio

Tagi to modyfikatory wstawiane w tekście, np. `[whispers]` lub `[laughs]`, które zapewniają precyzyjną kontrolę nad wyświetlaniem. Możesz ich używać do zmiany tonu, tempa i emocjonalnego wydźwięku wiersza lub fragmentu transkrypcji. Możesz też używać ich do dodawania do występu wykrzykników i innych dźwięków niewerbalnych, takich jak `[cough]`, `[sighs]` czy `[gasp]`.

Nie ma wyczerpującej listy tagów, które działają, a które nie. Zalecamy eksperymentowanie z różnymi emocjami i wyrażeniami, aby sprawdzić, jak zmienia się wynik.

Jeśli transkrypcja nie jest w języku angielskim, zalecamy używanie tagów audio w języku angielskim, aby uzyskać najlepsze wyniki.

**Kreatywne wykorzystanie tagów audio**

Aby pokazać, jak bardzo mogą się różnić tagi audio, przygotowaliśmy zestaw przykładów, w których każdy mówi to samo, ale sposób przekazu zmienia się w zależności od użytych tagów.

Możesz zmienić sposób przekazu, dodając na początku wiersza tagi, które sprawią, że lektor będzie podekscytowany, znudzony lub niechętny:

- `[excitedly]` Cześć, jestem nowym modelem zamiany tekstu na mowę i mogę mówić na wiele różnych sposobów. W czym mogę Ci pomóc?
- `[bored]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[reluctantly]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Tagi mogą też służyć do zmiany tempa odczytu lub łączenia tempa z podkreśleniem:

- `[very fast]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[very slow]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[sarcastically, one painfully slow word at a time]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Masz też precyzyjną kontrolę nad poszczególnymi sekcjami, co oznacza, że możesz szeptać jedną część, a krzyczeć inną.

- `[whispers]` Cześć, jestem nowym modelem zamiany tekstu na mowę `[shouting]` i mogę mówić na wiele różnych sposobów. `[whispers]` W czym mogę Ci dziś pomóc?

Możesz też eksperymentować z dowolnym pomysłem na kreację:

- `[like a cartoon dog]` Cześć, jestem nowym modelem zamiany tekstu na mowę…
- `[like dracula]` Cześć, jestem nowym modelem zamiany tekstu na mowę…

Często używane tagi:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

Tagi umożliwiają szybkie i łatwe kontrolowanie dostarczania transkrypcji. Aby mieć jeszcze większą kontrolę, możesz połączyć je z promptem kontekstowym, aby ustawić ogólny ton i klimat występu.

### Zaawansowane prompty

Zaawansowany prompt to instrukcja systemowa dla modelu. Dzięki temu model ma więcej kontekstu i większą kontrolę nad skutecznością.

Dobry prompt powinien zawierać te elementy, które razem tworzą świetny wynik:

- **Profil audio** – określa charakter głosu, definiując tożsamość postaci, archetyp i inne cechy, takie jak wiek, pochodzenie itp.
- **Scena** – przygotowuje scenę. Opisuje zarówno środowisko fizyczne, jak i „klimat”.
- **Notatki reżysera** – wskazówki dotyczące skuteczności, w których możesz określić, które instrukcje są ważne dla Twojego wirtualnego talentu. Przykłady to styl, oddech, tempo, artykulacja i akcent.
- **Przykładowy kontekst** – zapewnia modelowi kontekstowy punkt wyjścia, dzięki czemu wirtualny aktor wchodzi na scenę w sposób naturalny.
- **Transkrypcja** – tekst, który model będzie odczytywać. Aby uzyskać najlepsze wyniki, pamiętaj, że temat transkrypcji i styl pisania powinny być powiązane z podawanymi przez Ciebie wskazówkami.
- **Tagi audio** – modyfikatory, które możesz umieścić w transkrypcji, aby zmienić sposób odczytywania danej części tekstu, np. `[whispers]` lub `[shouting]`.

Przykładowy pełny prompt:

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

### Szczegółowe strategie tworzenia promptów

Rozbijmy każdy element prompta na części.

#### Profil audio

Krótko opisz osobowość postaci.

- **Nazwa** Nadanie postaci imienia pomoże modelowi i zwiększy spójność działania. Odwołuj się do postaci po imieniu podczas tworzenia sceny i kontekstu.
- **Rola** Główna tożsamość i archetyp postaci, która występuje w scenie, np. DJ radiowy, podcaster, reporter itp.

Przykłady:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Sceneria

Określ kontekst sceny, w tym lokalizację, nastrój i szczegóły środowiskowe, które nadają ton i klimat. Opisz, co dzieje się wokół postaci i jak to na nią wpływa. Scena zapewnia kontekst środowiskowy dla całej interakcji i w subtelny, naturalny sposób kieruje działaniami aktora.

Przykłady:

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

#### Notatki reżysera

Ta kluczowa sekcja zawiera szczegółowe wskazówki dotyczące skuteczności. Możesz pominąć wszystkie inne elementy, ale zalecamy uwzględnienie tego elementu.

Określ tylko to, co jest ważne dla wydajności, uważając, aby nie przesadzić. Zbyt wiele ścisłych reguł ograniczy kreatywność modeli i może pogorszyć ich skuteczność. Zrównoważ opis roli i sceny ze szczegółowymi zasadami dotyczącymi występu.

Najczęstsze wskazówki to **Styl, tempo i akcent**, ale model nie jest ograniczony do tych wskazówek ani ich nie wymaga. Możesz dodać niestandardowe instrukcje, aby uwzględnić dodatkowe szczegóły ważne dla skuteczności, i podać tyle szczegółów, ile uznasz za konieczne.

Na przykład:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Styl:**

Ustawia ton i styl wygenerowanej mowy. Wpisz np. „radosny”, „energiczny”, „zrelaksowany”, „znudzony” itp., aby określić charakter występu. Opisz je i podaj jak najwięcej szczegółów: *„Zaraźliwy entuzjazm. Słuchacz powinien mieć wrażenie, że uczestniczy w wielkim, ekscytującym wydarzeniu społecznościowym”.* To zdanie jest lepsze niż po prostu *„energetyczny i entuzjastyczny”*.

Możesz nawet wypróbować terminy popularne w branży voiceover, takie jak „uśmiech w głosie”. Możesz nałożyć na siebie dowolną liczbę cech stylu.

Przykłady:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Większa głębia

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Złożona

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Akcent:**

Opisz pożądany akcent. Im bardziej szczegółowe informacje podasz, tym lepsze będą wyniki. Na przykład użyj „*akcentu brytyjskiego angielskiego, jakiego używa się w Croydon w Anglii*” zamiast „*akcentu brytyjskiego*”.

Przykłady:

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

**Tempo:**

ogólne tempo i jego zmiany w całym utworze;

Przykłady:

Prosty

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Większa głębia

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Złożona

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Tagi transkrypcji i audio

Transkrypcja zawiera dokładne słowa, które wypowie model. Tag audio to słowo w nawiasach kwadratowych, które wskazuje, jak coś powinno być powiedziane, zmianę tonu lub wykrzyknik.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Wypróbuj**

Wypróbuj te przykłady w [AI Studio](https://aistudio.google.com/generate-speech?hl=pl), skorzystaj z naszej [aplikacji TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=pl) i pozwól, aby Gemini wcielił się w rolę reżysera. Aby uzyskać świetne wykonanie wokalne, pamiętaj o tych wskazówkach:

- Pamiętaj, aby cały prompt był spójny – scenariusz i instrukcje są ze sobą ściśle powiązane i wspólnie tworzą świetne wykonanie.
- Nie musisz opisywać wszystkiego. Czasami pozostawienie modelu przestrzeni do wypełnienia luk pomaga zachować naturalność. (Podobnie jak utalentowany aktor)
- Jeśli utkniesz w martwym punkcie, poproś Gemini o pomoc w przygotowaniu scenariusza lub występu.

## Generowanie mowy strumieniowej

Wygenerowany dźwięk możesz przesyłać strumieniowo w miarę jego generowania przez model. Pomaga to zmniejszyć odczuwalne opóźnienie.

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

## Ograniczenia

- Modele TTS mogą otrzymywać tylko dane wejściowe w postaci tekstu i generować dane wyjściowe w postaci dźwięku.
- Sesja TTS ma limit [okna kontekstu](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) wynoszący 32 tys. tokenów.
- Więcej informacji o obsługiwanych językach znajdziesz w sekcji [Języki](https://ai.google.dev/gemini-api/docs/speech-generation?hl=pl#languages).
- Usługa TTS nie obsługuje strumieniowania w przypadku modeli starszych niż wersja 3.1 (strumieniowanie jest obsługiwane w przypadku wersji `gemini-3.1-flash-tts-preview` i nowszych).

Poniższe ograniczenia obowiązują w przypadku korzystania z modelu Gemini 3.1 Flash TTS Preview do generowania mowy:

- **Niespójność głosu z instrukcjami w prompcie:** wygenerowane przez model dane wyjściowe nie zawsze ściśle pasują do wybranego głosu, przez co dźwięk może brzmieć inaczej niż oczekiwano. Aby uniknąć niedopasowania tonów (np. gdy głęboki męski głos próbuje mówić jak mała dziewczynka), upewnij się, że ton i kontekst tekstu w promcie są naturalnie zgodne z profilem wybranego lektora.
- **Jakość dłuższych wyjść:** jakość i spójność mowy mogą zacząć się pogarszać w przypadku wygenerowanych wyjść, które trwają dłużej niż kilka minut. Zalecamy podzielenie transkrypcji na mniejsze części.
- **Sporadyczne zwracanie tokenów tekstowych:** model sporadycznie zwraca tokeny tekstowe zamiast tokenów audio, co powoduje, że serwer odrzuca żądanie z błędem `500`. Dzieje się tak losowo w bardzo małym odsetku żądań, dlatego w aplikacji należy zaimplementować automatyczną logikę ponawiania, aby sobie z tym radzić.
- **Fałszywe odrzucenia klasyfikatora promptów:** niejasne prompty mogą nie wywołać klasyfikatora syntezy mowy, co spowoduje odrzucenie żądania (`PROHIBITED_CONTENT`) lub odczytanie na głos instrukcji dotyczących stylu i uwag reżysera. Sprawdzaj prośby, dodając jasny wstęp, który instruuje model, aby syntetyzował mowę, i wyraźnie oznaczaj miejsce, w którym zaczyna się rzeczywisty zapis wypowiedzi.

## Co dalej?

- Wypróbuj [przepis na generowanie dźwięku](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=pl).
- [Interfejs Live API](https://ai.google.dev/gemini-api/docs/live?hl=pl) Gemini oferuje interaktywne opcje generowania dźwięku, które możesz przeplatać z innymi trybami.
- Informacje o pracy z *wejściowymi danymi audio* znajdziesz w przewodniku [Rozumienie dźwięku](https://ai.google.dev/gemini-api/docs/audio?hl=pl).

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
