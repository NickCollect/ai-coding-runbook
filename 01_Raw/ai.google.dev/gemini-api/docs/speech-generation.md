---
source_url: https://ai.google.dev/gemini-api/docs/speech-generation?hl=it
fetched_at: 2026-06-15T06:26:53.508044+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=it) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Generazione di sintesi vocale (TTS)

L'API Gemini può trasformare l'input di testo in audio con una o più voci
utilizzando le funzionalità di generazione di sintesi vocale (TTS) di Gemini.
La generazione di sintesi vocale (TTS) è *[controllabile](#controllable)*, il che significa che puoi utilizzare il linguaggio naturale per strutturare le interazioni e guidare lo *stile*, l'*accento*, il *ritmo* e il *tono* dell'audio.

[Prova in Google AI Studio](https://aistudio.google.com/apps/bundled/voice-library?showPreview=truew&hl=it)

La funzionalità TTS è diversa dalla generazione vocale fornita tramite l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it), progettata per audio interattivi e non strutturati, nonché per input e output multimodali. Mentre l'API Live eccelle
in contesti conversazionali dinamici, la sintesi vocale tramite l'API Gemini
è pensata per scenari che richiedono una recitazione esatta del testo con un controllo
preciso su stile e suono, come la generazione di podcast o audiolibri.

Questa guida mostra come generare audio con un solo relatore e con più relatori dal testo.

## Prima di iniziare

Assicurati di utilizzare una variante del modello Gemini con funzionalità di sintesi vocale (TTS) di Gemini, come indicato nella sezione [Modelli supportati](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#supported-models). Per risultati ottimali, valuta quale modello si adatta meglio al tuo caso d'uso specifico.

Prima di iniziare a creare, ti consigliamo di [testare i modelli Gemini TTS in AI Studio](https://aistudio.google.com/generate-speech?hl=it).

## TTS con un solo speaker

Per convertire il testo in audio con un solo oratore, imposta la modalità di risposta su "audio" e passa un oggetto `SpeechConfig` con `VoiceConfig` impostato.
Dovrai scegliere un nome per la voce tra le [voci di output](#voices) predefinite.

Questo esempio salva l'audio di output del modello in un file wave:

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

## TTS multilingue

Per l'audio multi-speaker, avrai bisogno di un oggetto `MultiSpeakerVoiceConfig` con
ogni oratore (fino a 2) configurato come `SpeakerVoiceConfig`.
Devi definire ogni `speaker` con gli stessi nomi utilizzati nel
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

## Controllare lo stile del discorso con i prompt

Puoi controllare stile, tono, accento e ritmo utilizzando prompt in linguaggio naturale
o [tag audio](#transcript-tags) per la sintesi vocale di una o più persone.
Ad esempio, in un prompt con un solo oratore, puoi dire:

```
Say in an spooky voice:
"By the pricking of my thumbs... [short pause]
[whisper] Something wicked this way comes"
```

In un prompt con più speaker, fornisci al modello il nome di ciascuno e
la trascrizione corrispondente. Puoi anche fornire indicazioni per ogni oratore
singolarmente:

```
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... [yawn] what's on the agenda today?
Speaker2: You're never going to guess!
```

Prova a utilizzare un'[opzione vocale](#voices) che corrisponda allo stile o all'emozione che vuoi trasmettere, per enfatizzarla ancora di più. Nel prompt precedente, ad esempio,
il tono affannoso di *Encelado* potrebbe enfatizzare "stanco" e "annoiato", mentre
il tono allegro di *Puck* potrebbe completare "entusiasta" e "felice".

## Generazione di un prompt per la conversione in audio in corso…

I modelli TTS generano solo audio, ma puoi utilizzare
[altri modelli](https://ai.google.dev/gemini-api/docs/models?hl=it) per generare prima una trascrizione,
quindi trasmetterla al modello TTS per la lettura ad alta voce.

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

## Opzioni vocali

I modelli TTS supportano le seguenti 30 opzioni vocali nel campo `voice_name`:

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *Luminoso* | **Puck** - *Upbeat* | **Caronte**: *informativa* |
| **Kore** -- *Firm* | **Fenrir**: *eccitabile* | **Leda** - *Giovane* |
| **Orus** -- *Azienda* | **Aoede** - *Breezy* | **Callirrhoe**: *informale* |
| **Autonoe** -- *Luminoso* | **Enceladus** - *Breathy* | **Iapetus** -- *Cancella* |
| **Umbriel**: *tranquillo* | **Algieba** - *Smooth* | **Despina** -- *Smooth* |
| **Erinome** -- *Cancella* | **Algenib** - *Gravelly* | **Rasalgethi** -- *Priorità informativa* |
| **Laomedeia** - *Upbeat* | **Achernar** - *Soft* | **Alnilam** -- *Firm* |
| **Schedar** -- *Even* | **Gacrux** - *Per adulti* | **Pulcherrima** -- *Inoltra* |
| **Achird** -- *Amichevole* | **Zubenelgenubi** - *Casual* | **Vindemiatrix** - *Delicato* |
| **Sadachbia** - *Vivace* | **Sadaltager** -- *Knowledgeable* | **Sulafat** - *Calda* |

Puoi ascoltare tutte le opzioni vocali in
[AI Studio](https://aistudio.google.com/generate-speech?hl=it).

## Lingue supportate

I modelli di sintesi vocale rilevano automaticamente la lingua di input. Sono supportate le seguenti lingue:

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Arabo | ar | Filippino | fil |
| Bengalese | bn | Finlandese | fi |
| Olandese | nl | Galiziano | gl |
| Inglese | it | Georgiano | ka |
| Francese | fr | Greco | el |
| Tedesco | de | Gujarati | gu |
| Hindi | hi | Creolo haitiano | ht |
| Indonesiano | id | Ebraico | lui |
| Italiano | it | Ungherese | hu |
| Giapponese | ja | Islandese | è |
| Coreano | ko | Giavanese | jv |
| Marathi | mr | Kannada | kn |
| Polacco | pl | Konkani | kok |
| Portoghese | pt | Lao | lo |
| Rumeno | ro | Latino | la |
| Russo | ru | Lettone | lv |
| Spagnolo | es | Lituano | lt |
| Tamil | ta | Lussemburghese | lb |
| Telugu | te | Macedone | mk |
| Thailandese | th | Maithili | mai |
| Turco | tr | Malgascio | mg |
| Ucraino | uk | Malese | ms |
| Vietnamita | vi | Malayalam | ml |
| Afrikaans | af | Mongolo | mn |
| Albanese | sq | Nepalese | ne |
| Amarico | am | Norvegese, bokmål | nb |
| Armeno | hy | Norvegese, nynorsk | nn |
| Azero | az | Odia | o |
| Basco | eu | Pashto | ps |
| Bielorusso | be | Persiano | fa |
| Bulgaro | bg | Punjabi | pa |
| Birmano | my | Serbo | sr |
| Catalano | ca | Sindhi | sd |
| Cebuano | ceb | Singalese | si |
| Cinese, mandarino | cmn | Slovacco | sk |
| Croato | h | Sloveno | sl |
| Ceco | cs | Swahili | sw |
| Danese | da | Svedese | sv |
| Estone | et | Urdu | UK |

## Modelli supportati

| Modello | Unico relatore | Multispeaker |
| --- | --- | --- |
| [Anteprima di Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=it) | ✔️ | ✔️ |
| [Gemini 2.5 Flash Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-preview-tts?hl=it) | ✔️ | ✔️ |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=it) | ✔️ | ✔️ |

## Guida ai prompt

Il modello **Gemini Native Audio Generation Text-to-Speech (TTS)** si differenzia dai modelli TTS tradizionali perché utilizza un modello linguistico di grandi dimensioni che sa ***non solo cosa dire, ma anche come dirlo***.

Il modello interpreterà in modo nativo una trascrizione e determinerà come
devono essere pronunciate le parole. Trascrizioni semplici senza ulteriori
richieste che suonino naturali. Tuttavia, Gemini TTS è dotato anche di strumenti che puoi utilizzare per
guidarlo.

Lo scopo di questa guida è fornire indicazioni fondamentali e stimolare idee per lo sviluppo di esperienze audio. Inizieremo con i **tag** per un controllo rapido in linea, per poi esplorare le **strutture di prompt** avanzate per una direzione completa delle prestazioni.

### Tag audio

I tag sono modificatori incorporati come `[whispers]` o `[laughs]` che ti offrono un controllo granulare sulla pubblicazione. Puoi utilizzarli per modificare il tono, il ritmo e
l'atmosfera emotiva di una riga o di una sezione della trascrizione. Puoi anche usarli per
aggiungere interiezioni e altri suoni non verbali alla performance, come
`[cough]`, `[sighs]` o `[gasp]`.

Non esiste un elenco esaustivo dei tag che funzionano e di quelli che non funzionano. Ti consigliamo di
sperimentare con diverse emozioni ed espressioni per vedere come cambia l'output.

Se la trascrizione non è in inglese, per ottenere risultati ottimali ti consigliamo di
utilizzare comunque i tag audio in inglese.

**Utilizzare i tag audio in modo creativo**

Per mostrare il tipo di variabilità che puoi ottenere con i tag audio, ecco una serie di esempi che dicono la stessa cosa, ma la pronuncia cambia in base ai tag utilizzati.

Puoi modificare l'enfasi della recitazione aggiungendo tag all'inizio di una
riga per rendere l'oratore entusiasta, annoiato o riluttante:

- `[excitedly]` Ciao, sono un nuovo modello di sintesi vocale e posso dire le cose
  in molti modi diversi. Come posso aiutarti?
- `[bored]` Ciao, sono un nuovo modello di sintesi vocale…
- `[reluctantly]` Ciao, sono un nuovo modello di sintesi vocale…

I tag possono essere utilizzati anche per modificare il ritmo della pronuncia o per combinare il ritmo
con l'enfasi:

- `[very fast]` Ciao, sono un nuovo modello di sintesi vocale…
- `[very slow]` Ciao, sono un nuovo modello di sintesi vocale…
- `[sarcastically, one painfully slow word at a time]` Ciao, sono un nuovo modello di sintesi vocale…

Hai anche il controllo preciso su sezioni specifiche, il che significa che puoi sussurrare
una parte e urlarne un'altra.

- `[whispers]` Ciao, sono un nuovo modello di sintesi vocale `[shouting]` e posso
  dire le cose in molti modi diversi. `[whispers]` Come posso aiutarti oggi?

Puoi anche sperimentare qualsiasi idea creativa tu voglia:

- `[like a cartoon dog]` Ciao, sono un nuovo modello di sintesi vocale…
- `[like dracula]` Ciao, sono un nuovo modello di sintesi vocale…

I tag di uso comune includono:

|  |  |  |  |
| --- | --- | --- | --- |
| `[amazed]` | `[crying]` | `[curious]` | `[excited]` |
| `[sighs]` | `[gasp]` | `[giggles]` | `[laughs]` |
| `[mischievously]` | `[panicked]` | `[sarcastic]` | `[serious]` |
| `[shouting]` | `[tired]` | `[trembling]` | `[whispers]` |

I tag consentono di controllare in modo rapido e semplice la pubblicazione della trascrizione. Per un controllo
ancora maggiore, puoi combinarli con un prompt di contesto per impostare il tono
e l'atmosfera generale della performance.

### Prompt avanzati

Puoi considerare un prompt avanzato come un'istruzione di sistema che il modello deve
seguire. È un modo per fornire al modello più contesto e controllo sulle
prestazioni.

Un prompt efficace include idealmente i seguenti elementi che si combinano per
creare una performance eccezionale:

- **Profilo audio**: definisce una persona per la voce, definendo un'identità, un archetipo e qualsiasi altra caratteristica come età, background e così via.
- **Scena**: prepara il terreno. Descrive sia l'ambiente fisico sia l'"atmosfera".
- **Note del regista**: indicazioni sul rendimento in cui puoi specificare quali
  istruzioni sono importanti da tenere a mente per il tuo talento virtuale. Alcuni esempi sono
  lo stile, la respirazione, il ritmo, l'articolazione e l'accento.
- **Contesto di esempio**: fornisce al modello un punto di partenza contestuale, in modo che l'attore virtuale entri in scena in modo naturale.
- **Trascrizione**: il testo che il modello pronuncerà. Per ottenere il massimo rendimento,
  ricorda che l'argomento e lo stile di scrittura della trascrizione devono essere correlati alle
  indicazioni che stai dando.
- **Tag audio**: modificatori che puoi inserire in una trascrizione per cambiare la modalità di riproduzione di una parte del testo, ad esempio `[whispers]` o `[shouting]`.

Prompt completo di esempio:

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

### Strategie di prompting dettagliate

Analizziamo ogni elemento del prompt.

#### Profilo audio

Descrivi brevemente la personalità del personaggio.

- **Nome.** Assegnare un nome al personaggio aiuta a dare un contesto al modello e a migliorare la qualità della performance. Fai riferimento al personaggio per nome quando imposti la scena e il contesto.
- **Ruolo.** Identità e archetipo principali del personaggio che si manifestano
  nella scena. Ad es. DJ radiofonico, podcaster, giornalista, ecc.

Esempi:

```
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"
```

```
# AUDIO PROFILE: Monica A.
## "The Beauty Influencer"
```

#### Scena

Imposta il contesto della scena, inclusi posizione, stato d'animo e dettagli ambientali
che stabiliscono il tono e l'atmosfera. Descrivi cosa sta succedendo intorno al
personaggio e come lo influenza. La scena fornisce il contesto ambientale
per l'intera interazione e guida la recitazione in modo sottile
e organico.

Esempi:

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

#### Note del regista

Questa sezione fondamentale include indicazioni specifiche sul rendimento. Puoi saltare tutti gli altri elementi, ma ti consigliamo di includere questo elemento.

Definisci solo ciò che è importante per il rendimento, facendo attenzione a non
specificare eccessivamente. Troppe regole rigide limiteranno la creatività dei modelli e potrebbero
comportare un rendimento peggiore. Bilancia la descrizione del ruolo e della scena con le
regole di performance specifiche.

Le indicazioni più comuni sono **Stile, Ritmo e Accento**, ma il modello non è limitato a queste e non le richiede. Puoi includere istruzioni personalizzate per coprire eventuali dettagli aggiuntivi importanti per il tuo rendimento e fornire tutti i dettagli necessari.

Ad esempio:

```
### DIRECTOR'S NOTES

Style: Enthusiastic and Sassy GenZ beauty YouTuber

Pacing: Speaks at an energetic pace, keeping up with the extremely fast, rapid
delivery influencers use in short form videos.

Accent: Southern california valley girl from Laguna Beach |
```

**Stile:**

Imposta il tono e lo stile del discorso generato. Includi elementi come allegro,
energetico, rilassato, annoiato e così via per guidare la performance. Fornisci una descrizione
e tutti i dettagli necessari: *"Entusiasmo contagioso. L'ascoltatore
deve sentirsi parte di un evento comunitario enorme ed entusiasmante".* funziona
meglio di dire semplicemente *"energetico ed entusiasta".*

Puoi anche provare termini popolari nel settore del voiceover, come "sorriso
vocale". Puoi sovrapporre tutte le caratteristiche di stile che vuoi.

Esempi:

Simple Emotion

```
DIRECTORS NOTES
...
Style: Frustrated and angry developer who can't get the build to run.
...
```

Maggiore profondità

```
DIRECTORS NOTES
...
Style: Sassy GenZ beauty YouTuber, who mostly creates content for YouTube Shorts.
...
```

Complesso

```
DIRECTORS NOTES
Style:
* The "Vocal Smile": You must hear the grin in the audio. The soft palate is
always raised to keep the tone bright, sunny, and explicitly inviting.
*Dynamics: High projection without shouting. Punchy consonants and
elongated vowels on excitement words (e.g., "Beauuutiful morning").
```

**Accento:**

Descrivi l'accento che preferisci. Più specifico è il prompt, migliori sono i risultati. Ad esempio, utilizza "*Accento inglese britannico come si sente a Croydon, Inghilterra*" anziché "*Accento britannico*".

Esempi:

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

**Pacing:**

Il ritmo generale e la sua variazione nel corso del brano.

Esempi:

Semplice

```
### DIRECTORS NOTES
...
Pacing: Speak as fast as possible
...
```

Più profondità

```
### DIRECTORS NOTES
...
Pacing: Speaks at a faster, energetic pace, keeping up with fast paced music.
...
```

Complesso

```
### DIRECTORS NOTES
...
Pacing: The "Drift": The tempo is incredibly slow and liquid. Words bleed into each other. There is zero urgency.
...
```

#### Tag di trascrizione e audio

La trascrizione è costituita dalle parole esatte che il modello pronuncerà. Un tag audio è una parola
tra parentesi quadre che indica come deve essere pronunciata una frase, un cambio
di tono o un'interiezione.

```
### TRANSCRIPT

I know right, [sarcastically] I couldn't believe it. [whispers] She should have totally left
at that point.

[cough] Well, [sighs] I guess it doesn't matter now.
```

**Prova**

Prova alcuni di questi esempi su
[AI Studio](https://aistudio.google.com/generate-speech?hl=it), gioca con la nostra
[app TTS](http://aistudio.google.com/app/apps/bundled/synergy_intro?hl=it) e lascia che
Gemini ti metta nei panni del regista. Tieni a mente questi suggerimenti per ottenere ottime
performance vocali:

- Ricorda di mantenere la coerenza dell'intera richiesta: il copione e la regia vanno di pari passo per creare una performance eccezionale.
- Non sentirti in dovere di descrivere tutto. A volte, lasciare al modello lo spazio per colmare le lacune aiuta a rendere il testo più naturale. (proprio come un attore di talento)
- Se ti senti bloccato, chiedi a Gemini di aiutarti a creare il copione o la performance.

## Limitazioni

- I modelli TTS possono ricevere solo input di testo e generare output audio.
- Una sessione TTS ha un limite di [finestra contestuale](https://ai.google.dev/gemini-api/docs/long-context?hl=it) di
  32.000 token.
- Consulta la sezione [Lingue](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#languages) per informazioni sulle lingue supportate.
- La sintesi vocale non supporta lo streaming.

I seguenti vincoli si applicano in modo specifico quando si utilizza il modello di anteprima Gemini 3.1 Flash
TTS per la generazione di voce:

- **Incoerenza della voce con le istruzioni del prompt:** l'output del modello potrebbe non
  corrispondere sempre rigorosamente al relatore selezionato, facendo sì che l'audio suoni
  in modo diverso dal previsto. Per evitare toni non corrispondenti (ad esempio una voce maschile profonda che tenta di parlare come una bambina), assicurati che il tono e il contesto del prompt siano in linea con il profilo del relatore selezionato.
- **Qualità degli output più lunghi:** la qualità e la coerenza della voce potrebbero iniziare a
  diminuire con gli output generati più lunghi di qualche minuto. Ti
  consigliamo di dividere le trascrizioni in parti più piccole.
- **Restituzione occasionale di token di testo**:il modello a volte restituisce token di testo anziché token audio, causando l'esito negativo della richiesta del server con un errore `500`. Poiché questo si verifica in modo casuale in una percentuale molto piccola di richieste,
  devi implementare una logica di ripetizione automatica nella tua applicazione per gestirle.
- **Rifiuti errati del classificatore di prompt**:i prompt vaghi potrebbero non attivare il classificatore di sintesi vocale, con conseguente rifiuto della richiesta (`PROHIBITED_CONTENT`) o indurre il modello a leggere ad alta voce le istruzioni di stile e le note del regista. Convalida i prompt aggiungendo un preambolo chiaro
  che istruisca il modello a sintetizzare il discorso e indica esplicitamente dove inizia
  la trascrizione effettiva.

## Passaggi successivi

- Prova il [cookbook per la generazione audio](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb?hl=it).
- L'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it) di Gemini offre opzioni di generazione audio interattive che puoi alternare ad altre modalità.
- Per lavorare con gli *input* audio, consulta la guida [Comprensione dell'audio](https://ai.google.dev/gemini-api/docs/audio?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-05-19 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-05-19 UTC."],[],[]]
