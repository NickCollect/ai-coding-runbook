---
source_url: https://ai.google.dev/gemini-api/docs/voice-design?hl=it
fetched_at: 2026-11-02T07:31:06.596876+00:00
title: "Progettazione vocale \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Progettazione vocale

La progettazione della voce ti consente di creare una nuova persona vocale persistente a partire da una
descrizione in linguaggio naturale utilizzando l'endpoint Voci dell'API Gemini
(`POST /v1beta/voices`). Invece di essere limitato a voci predefinite o
alla registrazione di audio di riferimento, puoi descrivere l'età, il timbro vocale,
l'accento e la dizione di base di un personaggio e ricevere un ID `voice_...` riutilizzabile salvato nel
tuo progetto.

Il modo più rapido per progettare, testare e perfezionare voci personalizzate è utilizzare lo studio interattivo **Voice Design** in [Google AI Studio](https://aistudio.google.com/generate-speech?hl=it). Puoi
generare persona personalizzate da prompt di testo, testarle con script di esempio e
copiare l'ID `voice_...` risultante direttamente nel codice dell'applicazione.

[Prova in Google AI Studio](https://aistudio.google.com/generate-speech?hl=it)

Sia [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=it)
(`gemini-3.8-flash-tts`) sia
[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=it)
(`gemini-3.8-flash-lite-tts`) supportano la progettazione vocale.

## Creare una voce progettata

Utilizza l'SDK Google GenAI (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) o l'API REST
per creare una voce personalizzata da una descrizione testuale. Per le voci `"prompted"`, sia
`voices.create` (`CreateVoice`) che `voices.get` (`GetVoice`) restituiscono un
campo `sample_audio` di solo output (`mime_type: "audio/wav"`, `data` codificato in base64) in modo da poter ascoltare immediatamente la voce generata:

### Python

```
import base64
from google import genai

client = genai.Client()

# 1. Design a custom voice persona from natural language
created_voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Warm British Astronomer",
        "gender": "male",
        "language_code": "en-GB",
        "prompted": {
            "input": (
                "A warm, thoughtful astronomer in his late 60s with a gentle"
                " British accent, speaking with quiet wonder."
            )
        },
    },
)

print(f"Created voice ID: {created_voice.id}")

# Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if created_voice.sample_audio and created_voice.sample_audio.data:
    with open("voice_preview.wav", "wb") as f:
        f.write(base64.b64decode(created_voice.sample_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// 1. Design a custom voice persona from natural language
const createdVoice = await ai.voices.create({
  store: true,
  voice: {
    model: "gemini-3.8-flash-tts",
    type: "prompted",
    display_name: "Warm British Astronomer",
    gender: "male",
    language_code: "en-GB",
    prompted: {
      input:
        "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder.",
    },
  },
});

console.log(`Created voice ID: ${createdVoice.id}`);

// Save the generated sample_audio preview (audio/wav) returned by CreateVoice
if (createdVoice.sample_audio?.data) {
  fs.writeFileSync(
    "voice_preview.wav",
    Buffer.from(createdVoice.sample_audio.data, "base64")
  );
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "store": true,
    "voice": {
      "model": "gemini-3.8-flash-tts",
      "type": "prompted",
      "display_name": "Warm British Astronomer",
      "gender": "male",
      "language_code": "en-GB",
      "prompted": {
        "input": "A warm, thoughtful astronomer in his late 60s with a gentle British accent, speaking with quiet wonder."
      }
    }
  }' | tee created_voice.json | jq -r '.sample_audio.data' | base64 --decode > voice_preview.wav
```

## Come funziona la progettazione vocale

1. **Crea un prompt vocale:** chiama `voices.create` (`POST /v1beta/voices`)
   con `type="prompted"` e `store=True`.
2. **Ricevi un `voice_id` e un'anteprima `sample_audio` permanenti**:l'API genera l'identità vocale, la memorizza nel tuo progetto e restituisce un ID permanente (ad esempio `voice_abc123...`) insieme a `sample_audio` (`mime_type: "audio/wav"`, `data` codificato in base64) contenente l'audio di anteprima generato per la voce.
3. **Sintetizza la voce**:passa `voice_id` ovunque sia accettato un nome di voce
   nelle tue richieste di sintesi.

## Sintetizzare il parlato con la voce che hai progettato

Una volta creata una voce, passa il relativo `id` (`voice_...`) all'API Interactions
per generare la sintesi vocale:

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[{
        "type": "user_input",
        "content": [{
            "type": "text",
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "annotations": [{
                "type": "speech_metadata",
                "style": "reflective and awe-inspired",
            }],
        }],
    }],
    response_format={"type": "audio"},
    generation_config={
        "speech_config": [
            {"voice": created_voice.id},
        ]
    },
)

with open("designed_voice.wav", "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash-tts",
  input: [{
    type: "user_input",
    content: [{
      type: "text",
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      annotations: [{
        type: "speech_metadata",
        style: "reflective and awe-inspired",
      }],
    }],
  }],
  response_format: { type: "audio" },
  generation_config: {
    speech_config: [
      { voice: createdVoice.id },
    ],
  },
});

fs.writeFileSync("designed_voice.wav", Buffer.from(interaction.output_audio.data, "base64"));
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "input": [{
      "type": "user_input",
      "content": [{
        "type": "text",
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "annotations": [{
          "type": "speech_metadata",
          "style": "reflective and awe-inspired"
        }]
      }]
    }],
    "response_format": {"type": "audio"},
    "generation_config": {
      "speech_config": [
        {"voice": "voice_YOUR_DESIGNED_VOICE_ID"}
      ]
    }
  }' | jq -r '[.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio")] | last | .data' | base64 --decode > out.wav
```

## Gestire le voci

Puoi elencare, filtrare, esaminare ed eliminare le voci memorizzate in qualsiasi momento utilizzando
l'API Voices (consulta
[Libreria di voci estesa e filtri](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it#voice-library)
per tutti i parametri di filtro).

- **Limiti di archiviazione e TTL**:le voci con stato (`store=True`, condivise tra le voci richieste e replicate) hanno un limite di **200 voci per progetto** e un **TTL di 1 anno** (durata).
- **Disponibilità di `sample_audio`:** `voices.create()` (`CreateVoice`) e
  `voices.get()` (`GetVoice`) compilano `sample_audio` (`mime_type:
  "audio/wav"`, `data` codificato in base64) per le voci `"prompted"`. Per mantenere
  la scheda leggera, `voices.list()` (`ListVoices`) omette `sample_audio`
  (e `sample_audio` non è impostato per le voci `"replicated"` e `"prebuilt"`).

### Python

```
from google import genai

client = genai.Client()

# List stored prompted voices in your project filtered by language
response = client.voices.list(
    type_=["prompted"],
    language_code=["en-US", "en-GB"],
)
for voice in response.voices or []:
    print(voice.id, voice.display_name, voice.type)

# Retrieve a specific voice by ID
voice_details = client.voices.get(id=created_voice.id)

# Delete a stored custom voice
client.voices.delete(id=created_voice.id)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

// List stored prompted voices in your project filtered by language
const response = await ai.voices.list({
  type: ["prompted"],
  language_code: ["en-US", "en-GB"],
});
for (const voice of response.voices ?? []) {
  console.log(voice.id, voice.display_name, voice.type);
}

// Retrieve a specific voice by ID
const voiceDetails = await ai.voices.get(createdVoice.id);

// Delete a stored custom voice
await ai.voices.delete(createdVoice.id);
```

### REST

```
# List stored prompted voices filtered by language
curl -G "https://generativelanguage.googleapis.com/v1beta/voices" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  --data-urlencode "type=prompted" \
  --data-urlencode "language_code=en-US" \
  --data-urlencode "language_code=en-GB"

# Retrieve a specific voice by ID
curl "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# Delete a stored custom voice
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/voices/voice_YOUR_DESIGNED_VOICE_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Best practice per la creazione di prompt per la progettazione vocale

- **Inserisci le caratteristiche vocali permanenti nella progettazione della voce, non in `style`:** definisci le caratteristiche immutabili, come età, genere, timbro, struttura vocale e accento regionale, quando crei la voce in `voices.create`.
- **Riserva `speech_metadata.style` per l'emozione situazionale**:una volta creata la tua voce personalizzata, utilizza prompt brevi `style` (ad esempio, `"whispered urgently"` o `"cheerful and energetic"`) per guidare la recitazione passo passo senza alterare l'identità principale dell'oratore.
- **Sii specifico e conciso**:una descrizione chiara di 1-2 frasi (ad esempio
  *"Una telecronista sportiva energica e frizzante sui 30 anni con un leggero accento del Midwest"*) produce risultati più puliti e coerenti rispetto a paragrafi contraddittori o troppo lunghi.

## Passaggi successivi

- Scopri come replicare la voce di un oratore esistente nella
  [replica vocale](https://ai.google.dev/gemini-api/docs/voice-replication?hl=it).
- Scopri lo stile a livello di turno, i tag in linea e il dialogo con più relatori nella
  [guida Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-24 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-24 UTC."],[],[]]
