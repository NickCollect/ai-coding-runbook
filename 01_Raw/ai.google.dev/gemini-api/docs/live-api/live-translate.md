---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=it
fetched_at: 2026-09-28T06:11:44.955362+00:00
title: "Traduzione in tempo reale con l'API Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash è ora disponibile. [Mettiti alla prova](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Traduzione in tempo reale con l'API Gemini Live

L'API Gemini Live supporta la traduzione vocale in tempo reale a bassa latenza tra oltre 70 lingue utilizzando il [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=it) modello. Configurando l'API Live con le impostazioni di traduzione, puoi eseguire lo streaming dell'audio in una lingua e ricevere l'output audio tradotto in un'altra lingua, consentendo una traduzione vocale in tempo reale senza interruzioni.

[Prova Traduzione dal Vivo in Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=it)
[Clona l'app di esempio da GitHubcode](https://github.com/google-gemini/gemini-live-api-examples)
[Usa le competenze dell'agente di codificaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#gemini-live-api-dev)

## Operatore vs. Traduzione dal Vivo

Sebbene entrambi utilizzino l'API Live, il modello mentale per Traduzione dal Vivo è diverso dalle interazioni in tempo reale con gli operatori.

| Operatore | Traduzione dal Vivo |
| --- | --- |
| **Il modello funge da assistente.** Ascolta, ragiona e intraprende azioni per tuo conto. | **Il modello funge da interprete.** Si comporta come una pipeline di traduzione in tempo reale. |
| **Utilizza interazioni basate sui turni.** Si basa su pause, rilevamento dell'intent e gestione delle interruzioni. | **Utilizza l'elaborazione continua dei flussi.** Traduce mentre l'oratore parla senza attendere i turni. |
| **Supporta strumenti e operatori.** Supporto nativo per la chiamata di funzioni, la Ricerca Google e le istruzioni. | **Supporta solo la traduzione.** Traduzione pura a bassa latenza; nessun supporto per strumenti o istruzioni. |
| **Completamente multimodale.** Supporta input di testo, audio, video e immagini. | **Audio limitato.** L'input è limitato all'audio per garantire soglie di latenza in tempo reale rigorose. |
| **Configurazione granulare.** Utilizza istruzioni di generazione, vocali, di strumenti e di sistema. | **Configurazione semplificata.** Imposta `target_language_code` e attiva/disattiva opzioni come `echo_target_language`. |

## Inizia

Gli esempi riportati di seguito mostrano come inizializzare un client e connettersi all'API Live con una configurazione di traduzione.

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

## Invio di audio

Per eseguire lo streaming degli input vocali per la traduzione, invia audio PCM a 16 bit, little endian, non elaborato.

- **Formato audio di input**: PCM a 16 bit non elaborato a 16 kHz (mono, little endian).
- **Formato audio di output**: PCM a 16 bit non elaborato a 24 kHz (mono, little endian).
- **Dimensione dei blocchi e latenza**: invia l'audio in blocchi di 100 ms.

Gli esempi riportati di seguito mostrano come inviare blocchi audio alla sessione.

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

## Configurazione

Per abilitare la traduzione, devi specificare `translationConfig` all'interno di `generationConfig` durante la configurazione della sessione.

### Configurazione dei messaggi di configurazione

`generationConfig` supporta i seguenti campi per abilitare le trascrizioni:

- **`inputAudioTranscription`**: un oggetto che, se presente, consente al modello di inviare trascrizioni di testo dell'audio di input.
- **`outputAudioTranscription`**: un oggetto che, se presente, consente al modello di inviare trascrizioni di testo dell'audio di output (tradotto).

`translationConfig` supporta i seguenti campi:

- **`targetLanguageCode`**: il [codice lingua BCP-47](#supported-languages) della lingua in cui vuoi che il modello traduca (ad es. `"pl"` per il polacco, `"es"` per lo spagnolo). Il valore predefinito è `"en"`.
- **`echoTargetLanguage`**: un valore booleano che indica come deve essere gestito l'audio di input già nella lingua di destinazione. Se impostato su `true`, il modello ripeterà l'audio di input già nella lingua di destinazione. Se impostato su `false`, il modello rimarrà in silenzio quando il parlato di input è già nella lingua di destinazione. Il valore predefinito è `false`.

Di seguito è riportato un esempio della struttura del messaggio di configurazione:

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

## Utilizzare token effimeri nelle applicazioni lato client

Per le applicazioni client-server, puoi utilizzare i [token effimeri](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=it) (attualmente in `v1beta`) per evitare di esporre la chiave API.

Quando utilizzi i token effimeri con Traduzione dal Vivo:

1. Devi utilizzare l'endpoint `v1beta`.
2. **Blocco della configurazione**:per impostazione predefinita, devi specificare `translationConfig` nei vincoli di creazione dei token sul server. In questo modo, la configurazione della traduzione viene bloccata e non può essere manomessa dal client.
3. **Sblocco della configurazione**:se vuoi poter impostare `translationConfig` lato client (ad esempio, per consentire a un utente di scegliere la propria lingua di destinazione), devi ometterlo dalla richiesta di creazione del token e impostare `"lock_additional_fields": []` invece. In questo modo, `translationConfig` verrà sbloccato per essere impostato lato client.

### Creare un token effimero vincolato

Gli esempi riportati di seguito mostrano come creare un token effimero con vincoli di traduzione.

### Python

```
import datetime
from google import genai

now = datetime.datetime.now(tz=datetime.timezone.utc)

client = genai.Client()

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
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/auth_tokens" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "uses": 1,
    "expireTime": "YYYY-MM-DDTHH:MM:SSZ",
    "liveConnectConstraints": {
      "model": "models/gemini-3.5-live-translate-preview",
      "config": {
        "responseModalities": ["AUDIO"],
        "inputAudioTranscription": {},
        "outputAudioTranscription": {},
        "translationConfig": {
          "targetLanguageCode": "pl",
          "echoTargetLanguage": true
        }
      }
    }
  }'
```

## Limitazioni

- **Modalità di input**: per la traduzione è supportato solo l'input audio. L'input di testo non è supportato.
- **Replica vocale**: la replica vocale può essere incoerente. Le voci potrebbero cambiare dopo lunghe pause, assegnare il genere sbagliato in base all'inizio del parlato o bloccarsi su una voce durante conversazioni rapide con più oratori.
- **Rilevamento della lingua**: il rilevamento della lingua ha difficoltà con accenti marcati, lingue simili (ad es. spagnolo e portoghese) o cambi di lingua rapidi. **Nota**:questo dovrebbe influire solo sulla trascrizione di input. I codici lingua e la traduzione finale dovrebbero comunque essere accurati.
- **Audio di sottofondo**: il modello è progettato per filtrare il rumore e la musica per produrre un parlato pulito, ma non tutti gli audio di sottofondo potrebbero essere ignorati.
- **Ripeti lingua di destinazione**: quando `echoTargetLanguage: true`, il rumore di fondo o la musica potrebbero introdurre artefatti nell'audio tradotto quando l'audio di input è già nella lingua di destinazione.

## Lingue supportate

Le seguenti lingue sono supportate per Traduzione dal Vivo.

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | af | Kazako | kk |
| Akan | ak | Khmer | km |
| Albanese | sq | Kinyarwanda | rw |
| Amarico | am | Coreano | ko |
| Arabo | ar | Lao | lo |
| Armeno | hy | Lettone | lv |
| Azero | az | Lituano | lt |
| Basco | eu | Macedone | mk |
| Bielorusso | be | Malese | ms |
| Bengalese | bn | Malayalam | ml |
| Bulgaro | bg | Marathi | mr |
| Birmano (Myanmar) | my | Mongolo | mn |
| Catalano | ca | Nepalese | ne |
| Cinese (semplificato) | zh-Hans | Norvegese | no, nb |
| Cinese (tradizionale) | zh-Hant | Persiano | fa |
| Croato | hr | Polacco | pl |
| Ceco | cs | Portoghese (Brasile) | pt-BR |
| Danese | da | Portoghese (Portogallo) | pt-PT |
| Olandese | nl | Punjabi | pa |
| Inglese | en | Rumeno | ro |
| Estone | et | Russo | ru |
| Filippino | fil | Serbo | sr |
| Finlandese | fi | Sindhi | sd |
| Francese | fr | Singalese | si |
| Galiziano | gl | Slovacco | sk |
| Georgiano | ka | Sloveno | sl |
| Tedesco | de | Spagnolo | es |
| Greco | el | Sundanese | su |
| Gujarati | gu | Swahili | sw |
| Hausa | ha | Svedese | sv |
| Ebraico | he | Tamil | ta |
| Hindi | hi | Telugu | te |
| Ungherese | hu | Thailandese | th |
| Islandese | is | Turco | tr |
| Indonesiano | id | Ucraino | uk |
| Italiano | it | Urdu | ur |
| Giapponese | ja | Uzbeco | uz |
| Giavanese | jv | Vietnamita | vi |
| Kannada | kn | Zulu | zu |

## Passaggi successivi

- Leggi la guida completa alle [funzionalità](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=it) dell'API Live.
- Leggi la guida [Inizia a utilizzare l'SDK](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=it).
- Leggi la guida [Inizia a utilizzare WebSocket](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=it).
- Leggi la guida [Token effimeri](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=it) per l'autenticazione sicura nelle applicazioni client-server.
- Clona gli esempi dell'API [Live](https://github.com/google-gemini/gemini-live-api-examples) da GitHub.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-07-23 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-07-23 UTC."],[],[]]
