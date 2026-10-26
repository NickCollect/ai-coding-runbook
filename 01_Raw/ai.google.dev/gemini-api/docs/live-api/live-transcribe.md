---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=it
fetched_at: 2026-10-26T05:53:48.287804+00:00
title: "Trascrizione in tempo reale con l'API Gemini Live \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon è ora disponibile. [Provalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=it).

![](https://ai.google.dev/_static/images/translated.svg?hl=it)

Google utilizza la tecnologia AI per tradurre i contenuti nella tua lingua preferita. Le traduzioni generate dall'AI potrebbero contenere errori.

- [Home page](https://ai.google.dev/?hl=it)
- [Gemini API](https://ai.google.dev/gemini-api?hl=it)
- [Documenti](https://ai.google.dev/gemini-api/docs?hl=it)

Invia feedback

# Trascrizione in tempo reale con l'API Gemini Live

L'API Gemini Live supporta la trascrizione della conversione della voce in testo in tempo reale e a bassa latenza utilizzando il modello [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=it). Se ti connetti all'API Live tramite WebSocket o utilizzi l'SDK Google Gen AI, puoi trasmettere in streaming l'input audio continuo e ricevere trascrizioni di testo incrementali in tempo reale man mano che viene pronunciato il discorso.

[Prova la Trascrizione in tempo reale in Google AI Studiomic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=it)
[Apri il cookbook di Colabcode](https://github.com/google-gemini/cookbook)
[Utilizza le competenze dell'agente di codificaterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=it#gemini-live-api-dev)

Sfruttando l'API Gemini Live, piattaforme per sviluppatori come
[Agora](https://docs.agora.io/en/ai/models/asr/gemini),
[Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration),
[LiveKit](https://docs.livekit.io/agents/models/stt/gemini/),
[Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google),
[Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) e
[Vision Agents](https://visionagents.ai/integrations/stt/gemini)
consentono agli sviluppatori di creare e implementare interfacce vocali ad alte prestazioni
con facilità. Queste piattaforme gestiscono un'infrastruttura complessa di streaming multimediale in tempo reale
dietro le quinte, consentendo agli sviluppatori di concentrarsi interamente sulla
creazione dell'esperienza utente.

## Operatore e trascrizione in tempo reale

Sebbene entrambi utilizzino la connessione di streaming bidirezionale dell'API Live, la trascrizione in tempo reale funziona come una pipeline di riconoscimento vocale dedicata a bassa latenza anziché come un agente conversazionale.

| Funzionalità | Agente | Trascrizione Istantanea |
| --- | --- | --- |
| **Ruolo principale** | Assistente conversazionale che ascolta, ragiona e risponde. | Pipeline di conversione della voce in testo in tempo reale che trascrive l'audio in entrata. |
| **Modalità di risposta** | Audio e testo parlati (`response_modalities=["AUDIO"]`). | Trascrizioni di testo dello streaming (`response_modalities=["TEXT"]`). |
| **Stile di interazione** | Dialogo a turni con rilevamento di pause e interruzioni. | Elaborazione continua del flusso mentre l'oratore parla. |
| **Funzionalità supportate** | Chiamata di funzione, Ricerca Google, istruzioni di sistema. | Bias del parlato (`custom_vocabulary`), rilevamento della lingua, VAD manuale e ibrido, trascrizione intelligente. |
| **Stream di input** | Multimodale: audio, video, immagini, testo. | Input audio (PCM a 16 bit non elaborato). |

## Inizia

I seguenti esempi mostrano come aprire una sessione di streaming bidirezionale con `gemini-3.5-transcribe-live` e ricevere trascrizioni in tempo reale.

### Python

```
import asyncio
from google import genai
from google.genai import types

client = genai.Client()
model = "gemini-3.5-transcribe-live"

config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],  # Automatic language detection
    ),
)

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        print("Session established with Live Transcription")

        # Receive transcription events
        async for response in session.receive():
            server_content = response.server_content
            if server_content and server_content.input_transcription:
                print("Transcript:", server_content.input_transcription.text)

if __name__ == "__main__":
    asyncio.run(main())
```

### JavaScript

```
import { GoogleGenAI, Modality } from '@google/genai';

const ai = new GoogleGenAI({});
const model = 'gemini-3.5-transcribe-live';

const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [], // Automatic language detection
  },
};

async function main() {
  const session = await ai.live.connect({
    model: model,
    config: config,
    callbacks: {
      onopen: () => console.log('Connected to Live Transcription'),
      onmessage: (message) => {
        const content = message.serverContent;
        if (content?.inputTranscription) {
          console.log('Transcript:', content.inputTranscription.text);
        }
      },
      onerror: (e) => console.error('Error:', e.message),
      onclose: (e) => console.log('Connection closed:', e.reason),
    },
  });
}

main();
```

### WebSockets

```
const API_KEY = "YOUR_API_KEY";
const MODEL_NAME = "gemini-3.5-transcribe-live";
const WS_URL = `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${API_KEY}`;

const websocket = new WebSocket(WS_URL);

websocket.onopen = () => {
  console.log('WebSocket connected');

  const setupMessage = {
    setup: {
      model: `models/${MODEL_NAME}`,
      generationConfig: {
        responseModalities: ['TEXT'],
      },
      inputAudioTranscription: {
        languageCodes: []
      }
    }
  };
  websocket.send(JSON.stringify(setupMessage));
};

websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.inputTranscription) {
    console.log('Transcript:', content.inputTranscription.text);
  }
};
```

## Trascrizioni provvisorie e definitive

Man mano che gli stream audio vengono inseriti nell'API Live, il server emette due campi di trascrizione complementari all'interno di `server_content`:

- **`interim_input_transcription`**: ipotesi parziali speculative a bassa latenza aggiornate mentre l'oratore parla attivamente. Questi aggiornamenti parziali vengono eseguiti rapidamente con un ritardo minimo. Utilizza `interim_input_transcription` per visualizzare in anteprima i sottotitoli codificati o i sottotitoli codificati in tempo reale reattivi dell'interfaccia utente.
- **`input_transcription`**: la trascrizione finalizzata emessa quando l'oratore si ferma, il turno termina o il discorso viene finalizzato. Una volta emesso, questo testo rappresenta la trascrizione autorevole del modello del segmento vocale. In modalità di trascrizione intelligente, verrà inclusa la risposta pulita e formattata.

L'esempio seguente mostra come visualizzare i risultati parziali intermedi dello streaming e inviare le trascrizioni finali:

### Python

```
async def receive_transcripts(session):
    async for response in session.receive():
        server_content = response.server_content
        if not server_content:
            continue

        # Real-time interim hypothesis (updates dynamically as user speaks)
        if server_content.interim_input_transcription:
            interim_text = server_content.interim_input_transcription.text
            print(f"\r[Interim] {interim_text}", end="", flush=True)

        # Finalized transcript (emitted on speech completion)
        if server_content.input_transcription:
            final_text = server_content.input_transcription.text
            print(f"\n[Final] {final_text}")
```

### JavaScript

```
onmessage: (message) => {
  const content = message.serverContent;
  if (!content) return;

  if (content.interimInputTranscription) {
    // Update live subtitle preview on screen
    renderInterimPreview(content.interimInputTranscription.text);
  }

  if (content.inputTranscription) {
    // Append final committed transcript to chat history
    commitFinalTranscript(content.inputTranscription.text);
  }
};
```

### WebSockets

```
websocket.onmessage = (event) => {
  const response = JSON.parse(event.data);
  const content = response.serverContent;
  if (content?.interimInputTranscription) {
    console.log('[Interim]:', content.interimInputTranscription.text);
  }
  if (content?.inputTranscription) {
    console.log('[Final]:', content.inputTranscription.text);
  }
};
```

## Invio di audio

Trasmetti in streaming blocchi audio tramite la connessione attiva come audio PCM a 16 bit non elaborato.

- **Formato audio**:PCM a 16 bit non elaborato a 16 kHz (mono, little-endian).
- **Dimensioni chunk**:invia l'audio in chunk di 100 ms (da 1024 a 2048 frame).
- **Tipo MIME:** `audio/pcm;rate=16000` (o la frequenza di campionamento corrispondente).

### Python

```
# Stream a raw PCM audio chunk
await session.send_realtime_input(
    audio=types.Blob(
        data=audio_chunk_bytes,
        mime_type="audio/pcm;rate=16000"
    )
)

# Signal the end of the audio stream when finished
await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
// Send base64-encoded PCM audio chunk
session.sendRealtimeInput({
  audio: {
    data: audioChunkBase64,
    mimeType: 'audio/pcm;rate=16000'
  }
});

// Signal stream end
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
// Send base64-encoded PCM audio chunk
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: {
      data: audioChunkBase64,
      mimeType: 'audio/pcm;rate=16000'
    }
  }
}));

// Signal stream end
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

## Funzionalità di trascrizione

### Rilevamento automatico della lingua

Per impostazione predefinita, l'omissione di `language_codes` o l'impostazione di `language_codes=[]` attiva l'identificazione automatica della lingua. Il modello rileva dinamicamente la lingua parlata in tutte le espressioni, incluse le conversazioni multilingue e il cambio di codice.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Suggerimento per una lingua specifica

Fornisci codici lingua BCP-47 espliciti (ad esempio, `["es-ES"]` per lo spagnolo o `["fr-FR"]` per il francese) per orientare il riconoscimento verso lingue specifiche (vedi [Lingue supportate](#supported-languages)).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=["es-ES"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: ['es-ES'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: ['es-ES'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Bias del vocabolario personalizzato

Fornisci un elenco di massimo 1000 frasi, nomi propri, nomi di brand o termini tecnici in `custom_vocabulary` per orientare il riconoscimento vocale verso una terminologia specifica (i risultati migliori si ottengono in genere con un massimo di 100 termini).

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        language_codes=[],
        custom_vocabulary=["Gemini", "Kubernetes", "BigQuery"],
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    languageCodes: [],
    customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      languageCodes: [],
      customVocabulary: ['Gemini', 'Kubernetes', 'BigQuery'],
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

### Trascrizione intelligente

Configura la formattazione dell'output della trascrizione utilizzando il parametro `mode` in `input_audio_transcription`:

- **`VERBATIM` (impostazione predefinita)**: produce una trascrizione letterale esatta di tutto ciò che viene detto, conservando le parole di riempimento grezze ("um", "uh", "tipo"), le ripetizioni e le false partenze.
- **`SMART` (Trascrizione intelligente)**: pulisce e struttura la trascrizione per renderla più leggibile:

  - **Rimozione delle disfluenze**: rimuove gli intercalari, le balbuzie e gli avvii errati.
  - **Correzioni automatiche in linea**: risolve le correzioni vocali in modo naturale.
  - **Formattazione strutturata**: formatta automaticamente elenchi, punti elenco, numeri, date e interruzioni di paragrafo.
  - **Grammatica e maiuscole**: applica la punteggiatura e le maiuscole naturali.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(
        mode="SMART",
    ),
)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {
    mode: 'SMART',
  },
};
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {
      mode: 'SMART',
    },
  },
};
websocket.send(JSON.stringify(setupMessage));
```

## Strategie di rilevamento di attività vocale (VAD)

### Rilevamento automatico dell'attività vocale (impostazione predefinita)

Per impostazione predefinita, il rilevamento automatico dell'attività vocale lato server rileva quando un oratore inizia e smette di parlare.

### VAD ibrido

[VAD ibrido](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=it#hybrid-vad) combina il rilevamento automatico dell'inizio del discorso lato server con il rilevamento della fine del discorso lato client per la finalizzazione del turno a latenza zero:

1. **Il rilevamento automatico dell'attività vocale lato server rimane attivo** per rilevare con precisione l'inizio del parlato con il padding audio del prefisso, evitando il troncamento delle parole iniziali.
2. **Rilevamento dell'attività vocale lato client rileva il silenzio**: quando il rilevamento dell'attività vocale locale sul dispositivo rileva che l'oratore ha smesso di parlare, il client invia immediatamente un segnale `audio_stream_end`.
3. **Finalizzazione rapida**: il server considera `audio_stream_end` come un prompt di finalizzazione immediata, ignorando il tempo di attesa predefinito del silenzio lato server e restituendo la trascrizione finalizzata con una latenza minima.
4. **Fallback**: se la VAD lato client non viene attivata, la VAD lato server funge da fallback automatico.

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Stream audio chunks...
    await session.send_realtime_input(
        audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
    )

    # When client-side VAD detects end of speech, send audio_stream_end:
    await session.send_realtime_input(audio_stream_end=True)
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  inputAudioTranscription: {},
};

// Stream audio...
session.sendRealtimeInput({
  audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
});

// When client VAD detects end of speech, send audioStreamEnd:
session.sendRealtimeInput({
  audioStreamEnd: true
});
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' }
  }
}));

// When client VAD detects end of speech, send audioStreamEnd:
websocket.send(JSON.stringify({
  realtimeInput: {
    audioStreamEnd: true
  }
}));
```

### VAD manuale (premi per parlare)

Per le interfacce walkie-talkie o i pulsanti push-to-talk, disattiva completamente il VAD automatico e controlla i limiti di turno in modo esplicito utilizzando `activity_start` e `activity_end`:

### Python

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    realtime_input_config=types.RealtimeInputConfig(
        automatic_activity_detection=types.AutomaticActivityDetection(
            disabled=True
        )
    ),
    input_audio_transcription=types.AudioTranscriptionConfig(),
)

async with client.aio.live.connect(model=model, config=config) as session:
    # Button pressed: signal speech start
    await session.send_realtime_input(activity_start=types.ActivityStart())

    # Stream audio chunks...
    await session.send_realtime_input(audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000"))

    # Button released: signal speech end
    await session.send_realtime_input(activity_end=types.ActivityEnd())
```

### JavaScript

```
const config = {
  responseModalities: [Modality.TEXT],
  realtimeInputConfig: {
    automaticActivityDetection: {
      disabled: true,
    },
  },
  inputAudioTranscription: {},
};

// Signal speech start
session.sendRealtimeInput({ activityStart: {} });

// Stream audio...

// Signal speech end
session.sendRealtimeInput({ activityEnd: {} });
```

### WebSockets

```
const setupMessage = {
  setup: {
    model: 'models/gemini-3.5-transcribe-live',
    generationConfig: {
      responseModalities: ['TEXT'],
    },
    realtimeInputConfig: {
      automaticActivityDetection: {
        disabled: true,
      },
    },
    inputAudioTranscription: {},
  },
};
websocket.send(JSON.stringify(setupMessage));

// Button pressed: signal speech start
websocket.send(JSON.stringify({
  realtimeInput: {
    activityStart: {},
  },
}));

// Stream audio...
websocket.send(JSON.stringify({
  realtimeInput: {
    audio: { data: chunkBase64, mimeType: 'audio/pcm;rate=16000' },
  },
}));

// Button released: signal speech end
websocket.send(JSON.stringify({
  realtimeInput: {
    activityEnd: {},
  },
}));
```

## Token effimeri nelle applicazioni client

Per le applicazioni client-server (come le app web o mobile che trasmettono in streaming direttamente da un microfono), utilizza i [token effimeri](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=it) per evitare di esporre la chiave API nel codice client.

Crea un token effimero vincolato sul server prima di avviare la connessione client:

### Python

```
import datetime
from google import genai

client = genai.Client()
expire_time = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=30)

token = client.auth_tokens.create(
    config={
        "uses": 1,
        "expire_time": expire_time,
        "live_connect_constraints": {
            "model": "gemini-3.5-transcribe-live",
            "config": {
                "response_modalities": ["TEXT"],
                "input_audio_transcription": {
                    "language_codes": [],
                },
            },
        },
    }
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});
const expireTime = new Date(Date.now() + 30 * 60 * 1000).toISOString();

const token = await client.authTokens.create({
  config: {
    uses: 1,
    expireTime: expireTime,
    liveConnectConstraints: {
      model: 'gemini-3.5-transcribe-live',
      config: {
        responseModalities: ['TEXT'],
        inputAudioTranscription: {
          languageCodes: [],
        },
      },
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
      "model": "models/gemini-3.5-transcribe-live",
      "config": {
        "responseModalities": ["TEXT"],
        "inputAudioTranscription": {
          "languageCodes": []
        }
      }
    }
  }'
```

## Lingue supportate

Le seguenti lingue e i seguenti codici lingua BCP-47 sono supportati per Gemini 3.5 Transcribe Live:

| Lingua | Codice BCP-47 | Lingua | Codice BCP-47 |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Giapponese | `ja-JP` |
| Amarico | `am-ET` | Giavanese | `jv-ID` |
| Arabo (Egitto) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armeno | `hy-AM` | Kannada | `kn-IN` |
| Assamese | `as-IN` | Kazako | `kk-KZ` |
| Azero | `az-AZ` | Coreano | `ko-KR` |
| Bielorusso | `be-BY` | Kirgizo | `ky-KG` |
| Bengalese (Bangladesh) | `bn-BD` | Lettone | `lv-LV` |
| Bengalese (India) | `bn-IN` | Lingala | `ln-CD` |
| Bosniaco | `bs-BA` | Lituano | `lt-LT` |
| Bulgaro | `bg-BG` | Macedone | `mk-MK` |
| Bulgaro (aromeno) | `rup-BG` | Malese | `ms-MY` |
| Birmano | `my-MM` | Malayalam | `ml-IN` |
| Cantonese (tradizionale) | `yue-Hant-HK` | Maltese | `mt-MT` |
| Catalano | `ca-ES` | Cinese mandarino (semplificato) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Khmer centrale | `km-KH` | Mongolo | `mn-MN` |
| Croato | `hr-HR` | Nepalese | `ne-NP` |
| Ceco | `cs-CZ` | Norvegese | `nb-NO` |
| Danese | `da-DK` | Oriya | `or-IN` |
| Olandese | `nl-NL` | Polacco | `pl-PL` |
| Inglese (Gran Bretagna) | `en-GB` | Portoghese (Brasile) | `pt-BR` |
| Inglese (India) | `en-IN` | Portoghese (Portogallo) | `pt-PT` |
| Inglese (Stati Uniti) | `en-US` | Punjabi | `pa-IN` |
| Estone | `et-EE` | Punjabi (Gurmukhi script) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Rumeno | `ro-RO` |
| Filippino | `fil-PH` | Russo | `ru-RU` |
| Finlandese | `fi-FI` | Serbo | `sr-RS` |
| Francese | `fr-FR` | Sindhi (alfabeto arabo) | `sd-Arab-IN` |
| Galiziano | `gl-ES` | Slovacco | `sk-SK` |
| Georgiano | `ka-GE` | Sloveno | `sl-SI` |
| Tedesco | `de-DE` | Spagnolo (America Latina) | `es-419` |
| Greek | `el-GR` | Spagnolo (Stati Uniti) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenya) | `sw-KE` |
| Hausa | `ha-NG` | Svedese | `sv-SE` |
| Ebraico | `he-IL` | Tagico | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Ungherese | `hu-HU` | Thailandese | `th-TH` |
| Islandese | `is-IS` | Turco | `tr-TR` |
| Inglese indiano | `en-IN` | Ucraino | `uk-UA` |
| Indonesiano | `id-ID` | Uzbeco | `uz-UZ` |
| Italiano | `it-IT` | Vietnamita | `vi-VN` |

## Riferimento ai parametri

Configura la trascrizione in tempo reale utilizzando i campi in `input_audio_transcription` e `realtime_input_config`:

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| `language_codes` | Array di stringhe | Codici lingua BCP-47 (ad es. `["en-US"]`). Se omesso o vuoto (`[]`), il modello rileva automaticamente la lingua e gestisce la voce multilingue. |
| `custom_vocabulary` | Array di stringhe | Fino a 1000 termini personalizzati, acronimi, nomi di brand o nomi propri per orientare il riconoscimento vocale. |
| `mode` | Stringa | Modalità di trascrizione: `"VERBATIM"` (predefinita) o `"SMART"` (Trascrizione intelligente). Se impostato su `"SMART"`, il modello rimuove gli intercalari, formatta gli elenchi e corregge le disfluenze. |
| `automatic_activity_detection.disabled` | Booleano | Imposta su `true` per disattivare il rilevamento di attività vocale automatico e inviare manualmente i segnali `activityStart` e `activityEnd`. |

### Campi di risposta del server

| Campo | Descrizione |
| --- | --- |
| `server_content.interim_input_transcription` | Ipotesi di trascrizione parziale provvisoria a bassa latenza emessa continuamente mentre l'utente parla. |
| `server_content.input_transcription` | Trascrizione autorevole e finalizzata emessa al termine di un turno di parola. |

## Limitazioni

- **Durata della sessione**:le sessioni di trascrizione in tempo reale supportano lo streaming continuo fino a 10 minuti.
- **Diarizzazione degli oratori**:la diarizzazione degli oratori non è supportata nelle sessioni di live streaming. Per la diarizzazione degli oratori, utilizza l'endpoint [Trascrizione audio](https://ai.google.dev/gemini-api/docs/transcribe?hl=it#speaker-diarization) non in streaming.
- **Timestamp a livello di parola**:i timestamp a livello di parola non sono supportati tramite l'API Live. L'API Live emette timestamp a livello di enunciato (`interim_input_transcription` e `input_transcription`).
- **Vocabolario personalizzato**:puoi fornire fino a 1000 termini in `custom_vocabulary`, ma in genere i risultati migliori si ottengono con un massimo di 100 termini.
- **Compatibilità delle modalità**:la trascrizione intelligente (`"mode": "SMART"`) rimuove le parole di riempimento e formatta il testo in base all'intent, ma non può essere combinata con le annotazioni delle parole.

## Passaggi successivi

- Leggi la [documentazione di Gemini Transcribe](https://ai.google.dev/gemini-api/docs/transcribe?hl=it) per i file audio non in streaming.
- Leggi la [panoramica dell'API Live](https://ai.google.dev/gemini-api/docs/live-api?hl=it) per gli agenti vocali conversazionali.
- Leggi la [guida alla traduzione live](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=it) per la traduzione vocale in tempo reale.
- Consulta la [pagina dei prezzi](https://ai.google.dev/gemini-api/docs/pricing?hl=it#gemini-3.5-transcribe-live) per i prezzi dello streaming dell'API Live.
- Esplora la [guida alle funzionalità dell'API Live](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=it).

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://developers.google.com/site-policies?hl=it). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-09-10 UTC.

Vuoi dirci altro?

[[["Facile da capire","easyToUnderstand","thumb-up"],["Il problema è stato risolto","solvedMyProblem","thumb-up"],["Altra","otherUp","thumb-up"]],[["Mancano le informazioni di cui ho bisogno","missingTheInformationINeed","thumb-down"],["Troppo complicato/troppi passaggi","tooComplicatedTooManySteps","thumb-down"],["Obsoleti","outOfDate","thumb-down"],["Problema di traduzione","translationIssue","thumb-down"],["Problema relativo a esempi/codice","samplesCodeIssue","thumb-down"],["Altra","otherDown","thumb-down"]],["Ultimo aggiornamento 2026-09-10 UTC."],[],[]]
