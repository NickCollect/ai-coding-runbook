---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it
fetched_at: 2026-10-12T07:07:15.943100+00:00
title: "Generazione di sintesi vocale (TTS) \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs/generate-content?hl=it)

Invia feedback

# Generazione di sintesi vocale (TTS)

L'API Gemini può trasformare l'input di testo in audio con una o più voci utilizzando le funzionalità di sintesi vocale (TTS) di Gemini.
La generazione di sintesi vocale è
*[controllabile](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#controllable)*,
il che significa che puoi combinare i metadati strutturati del turno (`speech_metadata`) e i tag vocali incorporati per guidare lo *stile*, l'*accento*, il *ritmo* e il *tono* dell'audio.

[Prova in Google AI Studio](https://aistudio.google.com/generate-speech?hl=it)

La funzionalità TTS è diversa dalla generazione vocale fornita tramite l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it), progettata per input e output multimodali e audio interattivi e non strutturati. Mentre l'API Live eccelle
in contesti conversazionali dinamici, la sintesi vocale tramite l'API Gemini
è pensata per scenari che richiedono una recitazione esatta del testo con un controllo
preciso su stile e suono, come la generazione di podcast o audiolibri.

Questa guida mostra come generare audio con una o più voci a partire da un testo utilizzando [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it) (`gemini-3.8-flash-tts`) e [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it) (`gemini-3.8-flash-lite-tts`).

## Prima di iniziare

Assicurati di utilizzare un modello Gemini TTS elencato nella sezione
[Modelli supportati](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#supported-models). Per risultati ottimali, consulta la sezione
[Quando utilizzare un modello](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#when-to-use-which-model)
per selezionare il modello migliore per il tuo carico di lavoro.

Prima di iniziare a creare, ti consigliamo di
[testare i modelli Gemini TTS in AI Studio](https://aistudio.google.com/generate-speech?hl=it).

## TTS con un solo speaker

Per convertire il testo in audio con una sola voce utilizzando i modelli Gemini 3.8 TTS, passa la trascrizione letterale in `parts[].text`, allega lo stile a livello di turno in `parts[].speech_metadata` e configura la voce in `speechConfig.voiceConfig`. Puoi trasmettere un nome di voce predefinito, un ID Extended
Voice Library, un ID [progettazione
vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it) personalizzato (`voice_...`)
o un ID [replica vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it)
(`voice_...` o `voicekey_...` senza stato facoltativo).

Questo esempio salva l'audio di output del modello in un file WAV:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.wav
```

## TTS multilocutore

Per i dialoghi con più interlocutori, configura due interlocutori in
`multiSpeakerVoiceConfig.speakerVoiceConfigs` utilizzando `prebuiltVoiceConfig` e
passa ogni turno di dialogo come un `part` separato con `speech_metadata` che specifica
sia `speaker` sia `style` facoltativo a livello di turno:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [
            {
                "text": "How's it going today Jane?",
                "speech_metadata": {
                    "speaker": "Joe",
                    "style": "cheerful and friendly",
                },
            },
            {
                "text": "Not too bad, how about you? Ready to test these new voices?",
                "speech_metadata": {
                    "speaker": "Jane",
                    "style": "calm and relaxed",
                },
            },
        ],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "multi_speaker_voice_config": {
                "speaker_voice_configs": [
                    {
                        "speaker": "Joe",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Puck"}
                        },
                    },
                    {
                        "speaker": "Jane",
                        "voice_config": {
                            "prebuilt_voice_config": {"voice_name": "Kore"}
                        },
                    },
                ]
            }
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.wav", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [
            {
               text: "How's it going today Jane?",
               speechMetadata: {
                  speaker: 'Joe',
                  style: 'cheerful and friendly',
               },
            },
            {
               text: 'Not too bad, how about you? Ready to test these new voices?',
               speechMetadata: {
                  speaker: 'Jane',
                  style: 'calm and relaxed',
               },
            },
         ],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            multiSpeakerVoiceConfig: {
               speakerVoiceConfigs: [
                  {
                     speaker: 'Joe',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Puck' },
                     },
                  },
                  {
                     speaker: 'Jane',
                     voiceConfig: {
                        prebuiltVoiceConfig: { voiceName: 'Kore' },
                     },
                  },
               ],
            },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.wav', audioBuffer);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {
          "text": "How'\''s it going today Jane?",
          "speech_metadata": {
            "speaker": "Joe",
            "style": "cheerful and friendly"
          }
        },
        {
          "text": "Not too bad, how about you? Ready to test these new voices?",
          "speech_metadata": {
            "speaker": "Jane",
            "style": "calm and relaxed"
          }
        }
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {
              "speaker": "Joe",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Puck" }
              }
            },
            {
              "speaker": "Jane",
              "voiceConfig": {
                "prebuiltVoiceConfig": { "voiceName": "Kore" }
              }
            }
          ]
        }
      }
    }
  }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
      base64 --decode > out.wav
```

## Controllare lo stile del parlato con metadati e tag

Gemini 3.8 TTS considera il campo `text` esclusivamente come una trascrizione letterale. Per
controllare la recitazione senza che le indicazioni di regia vengano lette ad alta voce, dividi le
istruzioni per ambito:

- **Pronuncia sostenuta a livello di turno (`speech_metadata.style`)**: inserisci emozioni,
  stile di pronuncia, prosodia, ritmo e volume che si applicano a un intero turno
  in `speech_metadata.style` (ad esempio, `"style": "whispered urgently"`,
  `"style": "out of breath"` o `"style": "warm and enthusiastic"`).
- **Eventi puntuali (tag in linea)**: inserisci brevi interruzioni o pause vocali non verbali direttamente all'interno della trascrizione utilizzando le parentesi angolari (ad esempio, `"Wait... <short pause> did you hear that? <sigh>"` o `"Excuse me <cough> as I was saying..."`).

Consulta la
[Guida ai prompt](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#prompting-guide)
per best practice complete.

## Opzioni vocali

Gemini 3.8 TTS supporta quattro modi per selezionare o creare voci:

1. **Voci di studio predefinite**:30 voci selezionate elencate nella tabella seguente.
2. **Libreria di voci estesa**:centinaia di voci aggiuntive in diverse lingue,
   accenti e archetipi di personaggi accessibili tramite `client.voices.list()`
   (`GET /v1beta/voices`).
3. **[Progettazione della voce](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it):** genera
   una voce personalizzata da una descrizione in linguaggio naturale in
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=it) o utilizzando
   `POST /v1beta/voices` (`type="prompted"`, che restituisce un ID
   `voice_...` persistente e un'anteprima `sample_audio` WAV in `CreateVoice` e
   `GetVoice`).
4. **[Replica vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it):**
   replica la voce di un oratore dall'audio di riferimento e di consenso in
   [Google AI Studio](https://aistudio.google.com/generate-speech?hl=it) o utilizzando
   `POST /v1beta/voices` (`type="replicated"`, `store=True` persistente per
   impostazione predefinita o `store=False` stateless facoltativo).

### Limiti e TTL della voce personalizzata

| Tipo di voce | Modalità di archiviazione | Quota / limite | Conservazione (TTL) |
| --- | --- | --- | --- |
| **Voci stateful** (`voice_...`, richieste o replicate) | `store=True` | **200 voci per progetto** (condivise tra le voci richieste e replicate) | **1 anno dall'ultimo utilizzo\*** |
| **Chiavi vocali stateless** (`voicekey_...`, replicate) | `store=False` | Gestito dal cliente | **7 giorni** |

\* **Estensione TTL**:il periodo di conservazione di un anno viene reimpostato ogni volta che la voce viene utilizzata attivamente (per la sintesi vocale o come voce di base per il remix). Le voci senza attività per 1 anno vengono eliminate automaticamente.

### Voci predefinite

|  |  |  |
| --- | --- | --- |
| **Zephyr** - *Luminoso* | **Puck** - *Upbeat* | **Caronte** -- *Istruttiva* |
| **Kore** -- *Firm* | **Fenrir**: *eccitabile* | **Leda** -- *Giovane* |
| **Orus** -- *Azienda* | **Aoede** - *Breezy* | **Callirrhoe**: *informale* |
| **Autonoe** -- *Luminoso* | **Enceladus** - *Breathy* | **Iapetus** -- *Cancella* |
| **Umbriel**: *tranquillo* | **Algieba** -- *Fluido* | **Despina** -- *Smooth* |
| **Erinome** -- *Cancella* | **Algenib** - *Gravelly* | **Rasalgethi** - *Informativa* |
| **Laomedeia** - *Upbeat* | **Achernar** - *Soft* | **Alnilam** -- *Firm* |
| **Schedar** - *Even* | **Gacrux** -- *Per adulti* | **Pulcherrima** -- *Forward* |
| **Achird**: *amichevole* | **Zubenelgenubi** - *Informale* | **Vindemiatrix** - *Gentle* |
| **Sadachbia** - *Vivace* | **Sadaltager** -- *Knowledgeable* | **Sulafat** -- *Calda* |

### Libreria di voci estesa e filtri

Oltre alle 30 voci di studio in primo piano nella tabella precedente, la **Extended
Voice Library** offre centinaia di voci aggiuntive in varie lingue,
accenti regionali, personaggi e domini. Puoi sfogliare, filtrare e
provare l'intera libreria di voci in modo interattivo in
[Google AI Studio](https://aistudio.google.com/generate-speech?hl=it) oppure interrogarla
in modo programmatico utilizzando `client.voices.list()` (`GET /v1beta/voices`, utilizzando
`google-genai` 2.25.0+ / `@google/genai` 2.24.0+).

`ListVoices` restituisce le voci personalizzate memorizzate (ordinate dalla più recente) seguite
dalle voci del catalogo predefinite che corrispondono ai criteri di filtro. Quando vengono passati più valori
per un filtro elenco, vengono restituite le voci corrispondenti a **qualsiasi** valore del filtro (`OR`), mentre i parametri di filtro distinti si combinano con `AND`:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| `language_code` | `list[str]` | Tag lingua BCP-47 (ad esempio, `["en-US", "en-GB"]`). Corrispondenza esatta senza distinzione tra maiuscole e minuscole. |
| `region_code` | `list[str]` | Codice o codici regione ISO 3166-1 alpha-2 o UN M.49 (ad esempio, `["US", "GB"]`). |
| `accent` | `list[str]` | Descrittore o descrittori dell'accento regionale (ad esempio, `["American", "British"]`). |
| `gender` | `list[str]` | Presentazione del genere percepito (`"female"`, `"male"` o `"neutral"`). |
| `pitch` | `list[str]` | Classificazione del tono vocale (`"low"`, `"medium"` o `"high"`). |
| `persona` | `list[str]` | Personaggio vocale o archetipo del personaggio (ad esempio, `["Warm, Friendly"]`, `["Narrator"]`). |
| `contexts` (`context` in REST) | `list[str]` | Dominio di utilizzo ottimale (ad esempio, `["Audiobook", "Conversational", "News"]`). |
| `type` (`type_` in Python) | `list[str]` | Filtra per fonte della voce: `"prebuilt"`, `"prompted"` ([Progettazione vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it)) o `"replicated"` ([Replica vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it)). |
| `search` | `str` | La ricerca di sottostringhe di testo libero è stata eseguita senza distinzione tra maiuscole e minuscole sia per `display_name` che per `description`. |
| `page_size` | `int` | Numero massimo di voci restituite per pagina (valore predefinito `50`, massimo `1000`). |
| `page_token` | `str` | Token di `response.next_page_token` per recuperare la pagina successiva dei risultati. |

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

## Lingue supportate

I modelli di sintesi vocale rilevano automaticamente la lingua di input.
[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it)
(`gemini-3.8-flash-tts`) supporta **oltre 130 lingue** e
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it)
(`gemini-3.8-flash-lite-tts`) supporta **oltre 100 lingue**:

| Lingua | Gemini 3.8 Flash TTS | Gemini 3.8 Flash-Lite TTS |
| --- | --- | --- |
| Accinese (alfabeto arabo) | ✔️ | ✔️ |
| Afrikaans | ✔️ | ✔️ |
| Akan | ✔️ | ✔️ |
| Amarico | ✔️ | ✔️ |
| Armeno | ✔️ | ✔️ |
| Assamese | ✔️ | ✔️ |
| Awadhi | ✔️ | ✔️ |
| Balinese | ✔️ | ✔️ |
| Bengalese | ✔️ | ✔️ |
| Banjar (caratteri arabi) | ✔️ | — |
| Banjar (alfabeto latino) | ✔️ | ✔️ |
| Bashkir | ✔️ | — |
| Basco | ✔️ | ✔️ |
| Bielorusso | ✔️ | ✔️ |
| Bemba | ✔️ | — |
| Bhojpuri | ✔️ | ✔️ |
| Bosniaco | ✔️ | ✔️ |
| Buginese | ✔️ | ✔️ |
| Bulgaro | ✔️ | ✔️ |
| Birmano | ✔️ | — |
| Cantonese | ✔️ | ✔️ |
| Catalano | ✔️ | ✔️ |
| Cebuano | ✔️ | ✔️ |
| Curdo centrale | ✔️ | ✔️ |
| Chhattisgarhi | ✔️ | ✔️ |
| Cinese (caratteri Hans) | ✔️ | ✔️ |
| Cinese (caratteri Hant) | ✔️ | ✔️ |
| Tataro di Crimea | ✔️ | — |
| Croato | ✔️ | ✔️ |
| Ceco | ✔️ | ✔️ |
| Danese | ✔️ | ✔️ |
| Olandese | ✔️ | ✔️ |
| Diula | ✔️ | — |
| Dzongkha | ✔️ | — |
| Arabo (Egitto) | ✔️ | ✔️ |
| Inglese | ✔️ | ✔️ |
| Estone | ✔️ | ✔️ |
| Filippino | ✔️ | ✔️ |
| Finlandese | ✔️ | — |
| Francese | ✔️ | ✔️ |
| Galiziano | ✔️ | ✔️ |
| ganda | ✔️ | ✔️ |
| Georgiano | ✔️ | ✔️ |
| Tedesco | ✔️ | ✔️ |
| Greek | ✔️ | ✔️ |
| Guarani | ✔️ | — |
| Gujarati | ✔️ | ✔️ |
| Creolo haitiano | ✔️ | ✔️ |
| Halh mongolo | ✔️ | ✔️ |
| Hausa | ✔️ | ✔️ |
| Ebraico | ✔️ | ✔️ |
| Hindi | ✔️ | ✔️ |
| Ungherese | ✔️ | ✔️ |
| Islandese | ✔️ | ✔️ |
| Igbo | ✔️ | — |
| Ilocano | ✔️ | ✔️ |
| Indonesiano | ✔️ | ✔️ |
| Persiano iraniano | ✔️ | ✔️ |
| Italiano | ✔️ | ✔️ |
| Giapponese | ✔️ | ✔️ |
| Giavanese | ✔️ | ✔️ |
| Kabyle | ✔️ | — |
| Kamba | ✔️ | ✔️ |
| Kannada | ✔️ | ✔️ |
| Kashmiri (scrittura araba) | ✔️ | ✔️ |
| Kashmiri (Deva script) | ✔️ | ✔️ |
| Kazako | ✔️ | ✔️ |
| Khmer | ✔️ | ✔️ |
| Kikuyu | ✔️ | ✔️ |
| Kinyarwanda | ✔️ | ✔️ |
| Kongo | ✔️ | ✔️ |
| Coreano | ✔️ | ✔️ |
| Kirgizo | ✔️ | ✔️ |
| Lao | ✔️ | ✔️ |
| Letgallo | ✔️ | — |
| Lingala | ✔️ | ✔️ |
| Lituano | ✔️ | — |
| Lussemburghese | ✔️ | — |
| Macedone | ✔️ | ✔️ |
| Magahi | ✔️ | ✔️ |
| Maithili | ✔️ | ✔️ |
| Malayalam | ✔️ | ✔️ |
| Maltese | ✔️ | ✔️ |
| Manipuri | ✔️ | ✔️ |
| Marathi | ✔️ | ✔️ |
| Minangkabau (scrittura araba) | ✔️ | ✔️ |
| Minangkabau (latino) | ✔️ | — |
| Mizo | ✔️ | ✔️ |
| Nepalese (lingua individuale) | ✔️ | ✔️ |
| Fulfulde nigeriano | ✔️ | ✔️ |
| Azerbaigian settentrionale | ✔️ | ✔️ |
| Sotho del nord | ✔️ | ✔️ |
| Uzbeko settentrionale | ✔️ | ✔️ |
| Norvegese bokmål | ✔️ | ✔️ |
| Norvegese (Nynorsk) | ✔️ | ✔️ |
| Nyanja | ✔️ | ✔️ |
| Occitano | ✔️ | — |
| Odia (lingua individuale) | ✔️ | ✔️ |
| Pangasinan | ✔️ | — |
| Persiano (Afghanistan) | ✔️ | ✔️ |
| Polacco | ✔️ | ✔️ |
| Portoghese | ✔️ | ✔️ |
| Punjabi | ✔️ | ✔️ |
| Rumeno | ✔️ | ✔️ |
| Russo | ✔️ | ✔️ |
| Santali | ✔️ | ✔️ |
| Serbo | ✔️ | ✔️ |
| Sindhi | ✔️ | — |
| Singalese | ✔️ | ✔️ |
| Slovacco | ✔️ | ✔️ |
| Sloveno | ✔️ | — |
| Somalo | ✔️ | — |
| Azerbaigiano meridionale | ✔️ | ✔️ |
| Pashto meridionale | ✔️ | ✔️ |
| Sotho del sud | ✔️ | — |
| Spagnolo | ✔️ | ✔️ |
| Arabo standard (caratteri arabi) | ✔️ | ✔️ |
| Arabo standard (alfabeto latino) | ✔️ | ✔️ |
| Lettone standard | ✔️ | ✔️ |
| Malese standard | ✔️ | ✔️ |
| Swahili (singola lingua) | ✔️ | — |
| Swati | ✔️ | — |
| Svedese | ✔️ | — |
| Tagico | ✔️ | — |
| Tamil | ✔️ | ✔️ |
| Telugu | ✔️ | ✔️ |
| Thailandese | ✔️ | — |
| Tigrinya | ✔️ | — |
| Albanese tosk | ✔️ | — |
| Turco | ✔️ | ✔️ |
| Uiguro | ✔️ | — |
| Vietnamita | ✔️ | ✔️ |

## Modelli supportati

| Modello | Unico relatore | Più relatori | Progettazione vocale | Replica vocale |
| --- | --- | --- | --- | --- |
| [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it) (`gemini-3.8-flash-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it) (`gemini-3.8-flash-lite-tts`) | ✔️ | ✔️ | ✔️ | ✔️ |
| [Anteprima di Gemini 3.1 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=it) | ✔️ | ✔️ | — | — |
| [Gemini 2.5 Pro Preview TTS](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro-preview-tts?hl=it) | ✔️ | ✔️ | — | — |

### Quando utilizzare un modello o l'altro

Entrambi i modelli Gemini 3.8 TTS condividono lo stesso schema dell'API e formato di prompt,
consentendoti di passare da uno all'altro con una sola modifica del parametro:

- **Utilizza [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it)
  (`gemini-3.8-flash-tts`)** quando la massima fedeltà acustica, l'interpretazione ricca di sfumature
  e il controllo espressivo sono la priorità assoluta. È ideale per lavori creativi di qualità professionale, dialoghi complessi tra più persone, tag di burst vocali pesanti, pronunce difficili, dialetti regionali o di minoranze e narrazioni di lunga durata che richiedono una stabilità assoluta della voce e del tono della stanza.
- **Utilizza [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it)
  (`gemini-3.8-flash-lite-tts`)** come sostituto rapido ed economico
  di `gemini-3.1-flash-tts-preview`. È ottimizzato per
  la produzione di grandi volumi, le cascate di agenti vocali conversazionali, le funzionalità di lettura
  ad alta voce, la replica vocale affidabile e la sintesi vocale quotidiana con un solo oratore
  nelle principali lingue.

### Guida alla migrazione

Quando esegui l'upgrade dai modelli di anteprima precedenti (`gemini-3.1-flash-tts-preview` o
`gemini-2.5-pro-preview-tts`) a Gemini 3.8 TTS (`gemini-3.8-flash-tts` o
`gemini-3.8-flash-lite-tts`), esamina queste cinque modifiche chiave:

1. **Separa lo stile dalla trascrizione**:sposta le istruzioni relative a recitazione, tono, prosodia e ritmo (ad esempio `"whispering"`, `"out of breath"` o `"speaking slowly"`) dal testo normale a `speech_metadata.style`.
   Mantieni `text` esattamente come la trascrizione letterale più i tag vocali incorporati.
2. **Progetta le buyer persona in anticipo con la progettazione vocale**:sostituisci i blocchi di più paragrafi
   `"Audio Profile"` o `"Director's Notes"` con una voce personalizzata creata
   in [Progettazione vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it), quindi
   trasporta l'ID `voice_...` nelle richieste TTS con stringhe `style` minime o vuote.
3. **Utilizza turni di dialogo strutturati**:per i dialoghi con più interlocutori, passa un
   `part` per turno di interlocutore con `speech_metadata.speaker` anziché incorporare
   i prefissi `Speaker: ...` all'interno di un singolo blocco di testo.
4. **Utilizza le parentesi angolari per i tag vocali incorporati:** utilizza le parentesi angolari (`<laugh>`,
   `<sigh>`, `<cough>`, `<breath>`, `<short pause>`) per le vocalizzazioni e le pause umane
   in un determinato momento. Evita tag di effetti sonori non vocali (come
   applausi o tonfi).
5. **Tieni conto dell'output WAV (`AUDIO_WAV`) predefinito nelle richieste unarie:** a differenza di
   `gemini-3.1-flash-tts-preview` (che restituiva PCM non elaborato senza intestazione
   `AUDIO_L16` per impostazione predefinita), i modelli Gemini 3.8 TTS restituiscono audio **WAV
   (`AUDIO_WAV`)** completo con un'intestazione RIFF (24 kHz, mono, PCM a 16 bit) nelle
   richieste unarie:
   - Se in precedenza il tuo codice racchiudeva i byte PCM non elaborati in un'intestazione WAV (ad esempio utilizzando il modulo `wave` di Python o il pacchetto `wav` di Node), rimuovi il wrapper dell'intestazione manuale e scrivi i byte audio decodificati direttamente in un file `.wav`.
   - Se la pipeline esistente richiede audio PCM non elaborato, mu-law o A-law senza intestazione, imposta esplicitamente `response_format.audio.mime_type` su `"AUDIO_L16"`, `"AUDIO_MULAW"` o `"AUDIO_ALAW"` (ad esempio, `{"response_format": {"audio": {"mime_type": "AUDIO_L16"}}}` in `generateContent` o `{"response_format": {"type": "audio", "mime_type": "audio/l16"}}` nell'API Interactions). Consulta
     [Formati di uscita audio](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#audio-output-formats).

## Guida ai prompt

I modelli Gemini 3.8 TTS trattano il testo di input rigorosamente come una **trascrizione letterale**.
A differenza dei modelli di anteprima precedenti in cui le indicazioni sceniche erano incorporate nel testo normale,
la sintesi vocale di Gemini 3.8 separa le indicazioni di turno sostenute (`speech_metadata`)
dai tag vocali incorporati puntuali.

### Campo Stile e tag in linea

Dividi le istruzioni sul rendimento per ambito:

- **Turn-level delivery (`speech_metadata.style`)**: inserisci gli attributi di delivery sostenuta, come emozione, prosodia, ritmo generale o stile di delivery (ad esempio `"whispering"`, `"out of breath"`, `"muttering"` o `"sarcastic"`), nel campo `style` di `speech_metadata`. Per creare un personaggio e
  una performance stabili nel tempo, progetta la persona in anticipo in
  [Progettazione della voce](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it) e utilizza
  `style` solo per modifiche facoltative a livello di turno.
- **Eventi puntuali (tag in linea):** inserisci brevi interruzioni vocali non verbali,
  respiri o pause in linea all'interno della trascrizione utilizzando le parentesi angolari
  (`<cough>`, `<breath>`, `<sigh>`, `<short pause>`). Utilizza le parentesi angolari
  (`<...>`) per ottenere la massima qualità audio e concentrati sulle vocalizzazioni umane
  anziché sugli effetti sonori non vocali.

| Ambito | Dove posizionare | Esempi |
| --- | --- | --- |
| **Svolta per svolta** (mantenuta durante la svolta) | `speech_metadata.style` | `"angry tone"`, `"speaking rapidly"`, `"out of breath"`, `"whispers"`, `"sarcastic"` |
| **Point-in-time** (si verifica in una parola specifica) | Inline in `text` (`<...>`) | `"<cough> Thank you all for coming tonight! <throat-clearing> As I was saying..."` |

### Pacing e pause

Puoi controllare il ritmo e il silenzio a tre livelli di granularità:

- **Punteggiatura e puntini di sospensione**:utilizza virgole, trattini (`--`) e puntini di sospensione (`...`)
  per simulare le esitazioni naturali di una conversazione.
- **Tag di pausa in linea**:inserisci `<short pause>` o `<long pause>` nei punti esatti
  del copione in cui un oratore deve fare una pausa:
  `text
  Hold on, let me think... <short pause> Alright, I've got it.`
- **Ritmo a livello di turno**:imposta `"style": "speaking rapidly"` o
  `"style": "speaking slowly"` in `speech_metadata` per controllare la velocità
  di pronuncia durante l'intero turno.

### Prosodia e intonazione

Utilizza **`speech_metadata.style`** per controllare la prosodia, il tono e l'inflessione in un turno (ad esempio, `"style": "high pitch, cheerful and excited inflection"` o `"style": "monotone and flat"`). Se l'emozione o la prosodia cambia a metà del dialogo, dividi il copione in turni separati con valori `style` distinti per ogni turno.

### Enfasi

Metti in maiuscolo parole specifiche nella trascrizione, combinate con punteggiatura e tag vocali
in linea, per enfatizzare naturalmente le parole chiave:

```
This is a VERY important point!
It was a VERY long day <sigh> ... nobody listens anymore.
```

### Esplosioni vocali e suoni non vocali

Inserisci le vocalizzazioni umane non verbali in linea utilizzando le parentesi angolari (`<...>`) nel punto esatto in cui deve verificarsi il suono. I tag vocali consigliati includono:

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

### Canali secondari e voci sovrapposte

Nel dialogo tra più oratori, racchiudi le reazioni degli ascoltatori tra caratteri pipe
(`|reaction|`) all'interno del turno di un oratore per creare backchannel naturali o
sovrapposizioni di parlato senza interrompere un turno separato per reazione.

- **Scambi brevi nel backchannel**:inserisci brevi reazioni degli ascoltatori (`|oh hmm|`,
  `|oh really?|`, `|absolutely|`) all'interno del turno dell'oratore attivo:
  - **Turno 1 (Speaker A):** `"So the launch is Thursday |oh hmm| Are we actually ready?"`
  - **Turno 2 (Speaker B):** `"Ready enough |oh really?| The last blocker cleared this morning."`
  - **Turno 3 (Speaker A):** `"Then let's ship it |absolutely| and watch the dashboards."`
- **Discorso sovrapposto e alternato:** utilizza più segmenti di pipe per
  simulare un discorso simultaneo o alternato tra due oratori (funziona meglio
  con `gemini-3.8-flash-tts`):
  - **Simultaneous countdown/chorus:** `"Let's surprise him on three |ok| ready?"` followed by `"one. two. three. |happy| happy |birthday| birthday!"`
  - **Sovrapposizione completa degli speaker:** `"Hello |oh| there |my| it |goodness| must |gracious| be |would| almost |you| time |look| for |at that| dinner"`

### Coerenza tra le generazioni e cosa evitare

Segui queste linee guida per mantenere stabile l'identità vocale durante i turni:

- **Progetta le buyer persona in anticipo nella progettazione vocale anziché in lunghi blocchi di stile:**
  i paragrafi `"Audio Profile"` in formato lungo e gli elenchi puntati multipli `"Director's Notes"`
  riportati dai modelli precedenti sono la causa più comune di deriva della voce.
  Utilizza la stessa intuizione creativa in anticipo nella
  [progettazione della voce](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it) per generare una
  persona `voice_...` personalizzata persistente, quindi riporta l'ID voce nelle tue
  chiamate TTS.
- **Affidati al riferimento vocale per la stabilità (ometti le metainstruzioni):**
  I modelli TTS Gemini 3.8 sono addestrati ad ancorarsi prima al riferimento audio.
  Non includere istruzioni che indicano al modello di mantenere la voce costante (ad esempio `"do not switch speaker identity"` o `"maintain identical timbre"`). Il testo del prompt aggiuntivo aumenta la deriva. Elimina le istruzioni di stile non necessarie e lascia che il modello vari naturalmente intorno al punto stabile fornito dal riferimento vocale.
- **Non tentare di modificare le caratteristiche immutabili del relatore in `style`:** evita di inserire
  cambiamenti di età, genere, nomi o accento permanenti in `speech_metadata.style`.
  Scegli invece una voce regionale dalla raccolta di voci estese o creane una
  con [Progettazione vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it).

### Workflow consigliato

1. **Crea il personaggio una sola volta:** crea il tuo personaggio in
   [Progettazione della voce](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it) o seleziona una
   voce regionale dalla raccolta di voci estese che corrisponda alla lingua e alla personalità di destinazione.
2. **Scrivi trascrizioni naturali con disfluenze**:per ottenere la massima naturalezza, scrivi il `text` come una vera trascrizione del parlato, includendo disfluenze e esitazioni naturali (ad esempio, `"Oh uh yeah I think... hm, so that's interesting"`).
3. **Per prima cosa, prova la sintesi vocale standard:** sintetizza la trascrizione con un campo `style` vuoto. La maggior parte delle richieste non richiede alcuna istruzione `style`.
4. **Aggiungi prompt brevi `style` solo per modifiche:** aggiungi una stringa `style` concisa
   (ad esempio `"casual, friendly"` o `"muttering, then reassuring"`) solo per
   i turni che richiedono una modifica specifica della pubblicazione e riutilizza la stessa stringa
   breve nei vari turni quando vuoi una base di riferimento coerente.

### Agenti vocali e di dialogo multi-turno

Quando crei agenti vocali conversazionali in tempo reale o applicazioni multi-turno:

- Effettua **una chiamata TTS per turno** all'arrivo dei blocchi di testo LLM.
- Consenti al `voice` configurato (predefinito, progettato `voice_...` o replicato
  `voice_...` / `voicekey_...`) di mantenere l'identità dell'oratore durante i turni, senza
  inviare di nuovo una persona con un lungo carattere a ogni turno.
- Lascia vuoto il campo `style` per turno o invia una breve stringa costante
  (ad esempio `"casual, friendly"`) per l'intera conversazione.
- Dividi le risposte lunghe dell'agente in turni più brevi anziché ricorrere a prompt di stile più efficaci.

## Generazione di sintesi vocale in streaming

Puoi riprodurre in streaming l'audio generato mentre viene sintetizzato dal modello. A differenza
delle richieste unarie (che restituiscono un file WAV completo con un'intestazione RIFF),
**le richieste di streaming restituiscono blocchi PCM lineari little-endian con segno a 16 bit non elaborati senza intestazione (`AUDIO_L16` / `audio/L16;codec=pcm;rate=24000`, 24 kHz, mono) per impostazione
predefinita**, in modo che i blocchi audio possano essere riprodotti o concatenati continuamente senza
intestazioni del contenitore:

### Python

```
from google import genai

client = genai.Client()

response_stream = client.models.generate_content_stream(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

for chunk in response_stream:
    try:
        data = chunk.candidates[0].content.parts[0].inline_data.data
        # data contains raw PCM bytes (24kHz, 1-channel, 16-bit)
    except (IndexError, AttributeError):
        pass
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

async function main() {
   const ai = new GoogleGenAI({});

   const responseStream = await ai.models.generateContentStream({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:streamGenerateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }'
```

## Formati di uscita audio

I modelli Gemini 3.8 TTS utilizzano formati audio predefiniti diversi a seconda che
la richiesta sia unaria o di streaming:

- **Richieste unarie (`models.generate_content`)**: restituiscono audio **WAV
  (`AUDIO_WAV`)** completo con un'intestazione RIFF (24 kHz, mono, PCM little-endian firmato a 16 bit). Puoi scrivere i byte audio decodificati direttamente in un file `.wav` senza aggiungere manualmente un contenitore WAV.
- **Richieste di streaming (`models.generate_content_stream` / `streamGenerateContent`):**
  restituisci blocchi **PCM lineare non elaborato senza intestazione (`AUDIO_L16`)** (24 kHz, mono,
  PCM little-endian con segno a 16 bit) per impostazione predefinita, in modo che i blocchi possano essere trasmessi in streaming o
  concatenati continuamente senza intestazioni del contenitore su ogni blocco.

Puoi sostituire la codifica audio di output e la frequenza di campionamento utilizzando
`generationConfig.responseFormat.audio`:

| Valore `mimeType` | Formato | Descrizione |
| --- | --- | --- |
| `"AUDIO_WAV"` *(predefinito unario)* | WAV (`audio/wav`) | File WAV completo con un'intestazione RIFF (24 kHz, mono, PCM a 16 bit). |
| `"AUDIO_L16"` *(predefinito per lo streaming)* | PCM lineare (`audio/l16`) | PCM lineare little-endian signed a 16 bit non elaborato senza intestazione. Ideale per lo streaming, le pipeline audio personalizzate o la concatenazione di clip multi-turn. |
| `"AUDIO_MULAW"` | μ-law (`audio/basic` / `audio/mulaw`) | Audio compresso G.711 μ-law. Comunemente utilizzato nella telefonia nordamericana e giapponese (8 kHz). |
| `"AUDIO_ALAW"` | A-law (`audio/alaw`) | Audio compresso G.711 A-law. Comunemente utilizzato nella telefonia europea e internazionale (8 kHz). |

Puoi anche specificare facoltativamente `sampleRate` (ad esempio, `24000`, `16000` o
`8000` Hz; il valore predefinito è `24000` Hz).

L'esempio seguente richiede PCM a 16 bit non elaborato senza intestazione (`AUDIO_L16`) a
24 kHz:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {"style": "cheerful and friendly"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "response_format": {
            "audio": {
                "mime_type": "AUDIO_L16",
                "sample_rate": 24000,
            }
        },
        "speech_config": {
            "voice_config": {"voice": "Kore"}
        },
    },
)

data = response.candidates[0].content.parts[0].inline_data.data
with open("out.pcm", "wb") as f:
    f.write(data)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from 'node:fs';

async function main() {
   const ai = new GoogleGenAI({});

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash-tts',
      contents: [{
         role: 'user',
         parts: [{
            text: 'Have a wonderful day!',
            speechMetadata: { style: 'cheerful and friendly' },
         }],
      }],
      config: {
         responseModalities: ['AUDIO'],
         responseFormat: {
            audio: {
               mimeType: 'AUDIO_L16',
               sampleRate: 24000,
            },
         },
         speechConfig: {
            voiceConfig: { voice: 'Kore' },
         },
      },
   });

   const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
   const audioBuffer = Buffer.from(data, 'base64');

   fs.writeFileSync('out.pcm', audioBuffer);
}
await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
        "contents": [{
          "role": "user",
          "parts": [{
            "text": "Have a wonderful day!",
            "speech_metadata": {
              "style": "cheerful and friendly"
            }
          }]
        }],
        "generationConfig": {
          "responseModalities": ["AUDIO"],
          "responseFormat": {
            "audio": {
              "mimeType": "AUDIO_L16",
              "sampleRate": 24000
            }
          },
          "speechConfig": {
            "voiceConfig": {
              "voice": "Kore"
            }
          }
        }
    }' | jq -r '.candidates[0].content.parts[0].inlineData.data' | \
          base64 --decode > out.pcm
```

## Limitazioni

- I modelli TTS accettano input solo di testo e generano output solo audio.
- La generazione multirelatore con una sola richiesta (`multiSpeakerVoiceConfig`) supporta
  fino a 2 relatori che utilizzano voci predefinite. Per combinare voci progettate su misura
  (`voice_...`) o replicate (`voice_...` / `voicekey_...`) in
  un dialogo con più personaggi, sintetizza il turno di ogni oratore singolarmente.
  Poiché le richieste unarie restituiscono `audio/wav` con un'intestazione RIFF di 44 byte per impostazione predefinita, richiedi PCM non elaborato (`AUDIO_L16`) o rimuovi l'intestazione WAV da ogni turno prima di concatenare i frame audio PCM a 24 kHz.
- **Limiti di archiviazione e TTL della voce personalizzata:**
  - **Voci con stato (`store=True`, richieste o replicate)**: massimo **200 voci per progetto** con un **TTL di 1 anno** (durata).
  - **Chiavi vocali stateless (`store=False`, `voicekey_...`):** **TTL di 7 giorni**
    (durata).
- Consulta la sezione
  [Lingue supportate](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=it#languages)
  per informazioni sulla copertura linguistica.

## Passaggi successivi

- Crea personaggi vocali personalizzati a partire dal linguaggio naturale con
  [Voice Design](https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=it).
- Replica la voce di un oratore esistente in
  [Replica vocale](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=it).
- Confronta le specifiche dei modelli nelle pagine dei modelli [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it) e [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it).
- Esplora l'audio bidirezionale interattivo con l'[API Live](https://ai.google.dev/gemini-api/docs/live?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-10-02 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-10-02 UTC."],[],[]]
