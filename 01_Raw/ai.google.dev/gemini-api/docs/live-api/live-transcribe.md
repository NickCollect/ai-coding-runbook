---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=de
fetched_at: 2026-09-14T05:39:39.250494+00:00
title: "Live-Transkription mit der Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)

Feedback geben

# Live-Transkription mit der Gemini Live API

Die Gemini Live API unterstützt die Echtzeit-Sprach-zu-Text-Transkription mit geringer Latenz mithilfe des Modells [`gemini-3.5-transcribe-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=de). Wenn Sie über WebSockets eine Verbindung zur Live API herstellen oder das Google Gen AI SDK verwenden, können Sie kontinuierliche Audioeingaben streamen und inkrementelle Texttranskriptionen in Echtzeit erhalten, während gesprochen wird.

[Live-Transkription in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live&hl=de)
[Colab-Cookbook öffnencode](https://github.com/google-gemini/cookbook)
[Coding-Agent-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de#gemini-live-api-dev)

Durch die Nutzung der Gemini Live API können Entwicklerplattformen wie [Agora](https://docs.agora.io/en/ai/models/asr/gemini), [Fishjam](https://docs.fishjam.io/tutorials/gemini-live-integration), [LiveKit](https://docs.livekit.io/agents/models/stt/gemini/), [Pipecat](https://docs.pipecat.ai/api-reference/server/services/stt/google), [Vercel](https://vercel.com/docs/ai-gateway/modalities/speech-to-text) und [Vision Agents](https://visionagents.ai/integrations/stt/gemini) ganz einfach leistungsstarke sprachgesteuerte Benutzeroberflächen erstellen und bereitstellen. Diese Plattformen verwalten im Hintergrund eine komplexe Infrastruktur für das Media-Streaming in Echtzeit, sodass sich Entwickler ganz auf die Gestaltung der Nutzererfahrung konzentrieren können.

## Kundenservicemitarbeiter im Vergleich zur Live-Transkription

Beide nutzen die bidirektionale Streamingverbindung der Live API, aber die automatische Transkription ist eine spezielle Spracherkennungspipeline mit niedriger Latenz und kein Konversations-Agent.

| Funktion | Frag den Kundenservice | Live-Transkription |
| --- | --- | --- |
| **Primäre Rolle** | Ein konversationeller Assistent, der zuhört, nachdenkt und antwortet. | Echtzeit-Spracherkennungspipeline, die eingehende Audioinhalte transkribiert. |
| **Antwortmodalität** | Gesprochene Audioinhalte und Text (`response_modalities=["AUDIO"]`). | Transkriptionen von Streamingtext (`response_modalities=["TEXT"]`) |
| **Interaktionsstil** | Turn-basierter Dialog mit Pausenerkennung und Unterbrechungen. | Kontinuierliche Streamverarbeitung während des Sprechens. |
| **Unterstützte Funktionen** | Funktionsaufrufe, Google Suche, Systemanweisungen. | Sprachbias (`custom_vocabulary`), Spracherkennung, manuelle und hybride VAD, Smart Transcription. |
| **Eingabestream** | Multimodal: Audio, Video, Bilder, Text. | Audioeingabe (rohes 16‑Bit-PCM). |

## Jetzt starten

Die folgenden Beispiele zeigen, wie Sie mit `gemini-3.5-transcribe-live` eine bidirektionale Streaming-Sitzung öffnen und Echtzeit-Transkriptionen empfangen.

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

## Vorläufige und endgültige Transkriptionen

Wenn Audio in die Live API gestreamt wird, gibt der Server zwei sich ergänzende Transkriptionsfelder in `server_content` aus:

- **`interim_input_transcription`**: Spekulative Teilhypothesen mit geringer Latenz, die aktualisiert werden, während der Sprecher aktiv spricht. Diese Teilaktualisierungen erfolgen schnell und mit minimaler Verzögerung. Verwenden Sie `interim_input_transcription`, um responsive Live-Untertitel für die Benutzeroberfläche oder Vorschauuntertitel zu rendern.
- **`input_transcription`**: Das endgültige Transkript, das ausgegeben wird, wenn der Sprecher pausiert, der Turn abgeschlossen ist oder die Sprache fertiggestellt ist. Sobald dieser Text ausgegeben wird, stellt er die maßgebliche Transkription des Modells für dieses Sprachsegment dar. Im Modus „Intelligente Transkription“ ist die bereinigte, formatierte Antwort enthalten.

Im folgenden Beispiel wird gezeigt, wie Sie Streaming-Zwischenergebnisse anzeigen und endgültige Transkripte übertragen:

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

## Audio senden

Audio-Chunks als rohes 16‑Bit-PCM-Audio über die aktive Verbindung streamen.

- **Audioformat**:Rohes 16‑Bit-PCM mit 16 kHz (Mono, Little Endian).
- **Blockgröße**:Senden Sie Audio in Blöcken von 100 ms (1.024 bis 2.048 Frames).
- **MIME-Typ**:`audio/pcm;rate=16000` (oder die entsprechende Samplingrate).

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

## Transkriptionsfunktionen

### Automatische Spracherkennung

Wenn Sie `language_codes` weglassen oder `language_codes=[]` festlegen, wird die Sprache standardmäßig automatisch erkannt. Das Modell erkennt die gesprochene Sprache in Äußerungen dynamisch, auch bei mehrsprachigen Unterhaltungen und Sprachwechseln.

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

### Spezifischer Sprachhinweis

Geben Sie explizite BCP-47-Sprachcodes an (z. B. `["es-ES"]` für Spanisch oder `["fr-FR"]` für Französisch), um die Spracherkennung auf bestimmte Sprachen auszurichten (siehe [Unterstützte Sprachen](#supported-languages)).

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

### Benutzerdefiniertes Vokabular

Geben Sie in `custom_vocabulary` eine Liste mit bis zu 1.000 Begriffen, Eigennamen, Markennamen oder Fachbegriffen an, um die Spracherkennung auf bestimmte Begriffe auszurichten. Die besten Ergebnisse werden in der Regel mit bis zu 100 Begriffen erzielt.

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

### Intelligente Transkription

Konfigurieren Sie die Formatierung der Transkriptionsausgabe mit dem Parameter `mode` in `input_audio_transcription`:

- **`VERBATIM` (Standard)**: Erstellt ein exaktes wörtliches Transkript von allem Gesprochenen, wobei Füllwörter („ähm“, „äh“, „wie“), Wiederholungen und Falschstarts beibehalten werden.
- **`SMART` (Smart Transcribe)**: Das Transkript wird bereinigt und strukturiert, um die Lesbarkeit zu verbessern:

  - **Entfernung von Unflüssigkeiten**: Füllwörter, Stottern und Fehlstarts werden entfernt.
  - **Inline-Selbstkorrekturen**: Gesprochene Korrekturen werden auf natürliche Weise berücksichtigt.
  - **Strukturierte Formatierung**: Listen, Aufzählungszeichen, Zahlen, Datumsangaben und Absatzumbrüche werden automatisch formatiert.
  - **Grammatik und Groß-/Kleinschreibung**: Wendet natürliche Groß-/Kleinschreibung und Interpunktion an.

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

## Strategien zur Erkennung von Sprachaktivitäten (Voice Activity Detection, VAD)

### Automatische VAD (Standard)

Standardmäßig wird serverseitig automatisch erkannt, wann ein Sprecher zu sprechen beginnt und aufhört.

### Hybrid-VAD

[Hybrid-VAD](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de#hybrid-vad) kombiniert die serverseitige automatische Erkennung des Sprechbeginns mit der clientseitigen Erkennung des Sprechendes für die latenzfreie Finalisierung von Zügen:

1. **Die serverseitige automatische VAD bleibt aktiviert**, um den Beginn der Sprache mit Prefix-Audio-Padding genau zu erkennen und so das Abschneiden von Wörtern am Anfang zu verhindern.
2. **Clientseitige VAD erkennt Stille**: Wenn eine lokale VAD auf dem Gerät erkennt, dass der Sprecher aufgehört hat zu sprechen, sendet der Client sofort ein `audio_stream_end`-Signal.
3. **Schnelle Finalisierung**: Der Server behandelt `audio_stream_end` als Aufforderung zur sofortigen Finalisierung des Turns. Die standardmäßige serverseitige Wartezeit für die Stille wird umgangen und das finalisierte Transkript wird mit minimaler Latenz zurückgegeben.
4. **Fallback**: Wenn die clientseitige VAD nicht ausgelöst wird, dient die serverseitige VAD als automatischer Fallback.

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

### Manuelle VAD (Push-to-Talk)

Bei Walkie-Talkie-Schnittstellen oder Push-to-Talk-Schaltflächen sollten Sie die automatische VAD vollständig deaktivieren und die Sprechpausen explizit mit `activity_start` und `activity_end` steuern:

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

## Sitzungsspezifische Tokens in Clientanwendungen

Verwenden Sie für Client-Server-Anwendungen (z. B. mobile Apps oder Web-Apps, die direkt von einem Mikrofon streamen) [ephemere Tokens](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=de), um zu vermeiden, dass Ihr API-Schlüssel im Clientcode offengelegt wird.

Erstellen Sie auf Ihrem Server ein eingeschränktes temporäres Token, bevor Sie die Clientverbindung initiieren:

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

## Unterstützte Sprachen

Die folgenden Sprachen und BCP-47-Sprachcodes werden für Gemini 3.5 Transcribe Live unterstützt:

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Afrikaans | `af-ZA` | Japanisch | `ja-JP` |
| Amharisch | `am-ET` | Javanisch | `jv-ID` |
| Arabisch (Ägypten) | `ar-EG` | Kabuverdianu | `kea-CV` |
| Armenisch | `hy-AM` | Kannada | `kn-IN` |
| Assamesisch | `as-IN` | Kasachisch | `kk-KZ` |
| Aserbaidschanisch | `az-AZ` | Koreanisch | `ko-KR` |
| Belarussisch | `be-BY` | Kirgisisch | `ky-KG` |
| Bengalisch (Bangladesch) | `bn-BD` | Lettisch | `lv-LV` |
| Bengalisch (Indien) | `bn-IN` | Lingala | `ln-CD` |
| Bosnisch | `bs-BA` | Litauisch | `lt-LT` |
| Bulgarisch | `bg-BG` | Mazedonisch | `mk-MK` |
| Bulgarisch (Aromanisch) | `rup-BG` | Malaiisch | `ms-MY` |
| Burmesisch | `my-MM` | Malayalam | `ml-IN` |
| Kantonesisch (traditionell) | `yue-Hant-HK` | Maltesisch | `mt-MT` |
| Katalanisch | `ca-ES` | Chinesisch (Mandarin, vereinfacht) | `cmn-Hans-CN` |
| Cebuano | `ceb` | Marathi | `mr-IN` |
| Standard-Khmer | `km-KH` | Mongolisch | `mn-MN` |
| Kroatisch | `hr-HR` | Nepalesisch | `ne-NP` |
| Tschechien | `cs-CZ` | Norwegisch | `nb-NO` |
| Dänisch | `da-DK` | Oriya | `or-IN` |
| Niederländisch | `nl-NL` | Polnisch | `pl-PL` |
| Englisch (Vereinigtes Königreich) | `en-GB` | Portugiesisch (Brasilien) | `pt-BR` |
| Englisch (Indien) | `en-IN` | Portugiesisch (Portugal) | `pt-PT` |
| Englisch (USA) | `en-US` | Punjabi | `pa-IN` |
| Estnisch | `et-EE` | Panjabi (Gurmukhi-Schrift) | `pa-Guru-IN` |
| Farsi | `fa-IR` | Rumänisch | `ro-RO` |
| Filipino | `fil-PH` | Russisch | `ru-RU` |
| Finnisch | `fi-FI` | Serbisch | `sr-RS` |
| Französisch | `fr-FR` | Sindhi (arabische Schrift) | `sd-Arab-IN` |
| Galizisch | `gl-ES` | Slowakisch | `sk-SK` |
| Georgisch | `ka-GE` | Slowenisch | `sl-SI` |
| Deutsch | `de-DE` | Spanisch (Lateinamerika) | `es-419` |
| Griechisch | `el-GR` | Spanisch (USA) | `es-US` |
| Gujarati | `gu-IN` | Swahili (Kenia) | `sw-KE` |
| Hausa | `ha-NG` | Schwedisch | `sv-SE` |
| Hebräisch | `he-IL` | Tadschikisch | `tg-TJ` |
| Hindi | `hi-IN` | Telugu | `te-IN` |
| Ungarisch | `hu-HU` | Thailändisch | `th-TH` |
| Isländisch | `is-IS` | Türkisch | `tr-TR` |
| Indisches Englisch | `en-IN` | Ukrainisch | `uk-UA` |
| Indonesisch | `id-ID` | Usbekisch | `uz-UZ` |
| Italienisch | `it-IT` | Vietnamesisch | `vi-VN` |

## Parameterverweis

Konfigurieren Sie die Live-Transkription mithilfe von Feldern in `input_audio_transcription` und `realtime_input_config`:

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| `language_codes` | String-Array | BCP-47-Sprachcodes (z.B. `["en-US"]`). Wenn dieser Parameter weggelassen oder leer ist (`[]`), erkennt das Modell die Sprache automatisch und verarbeitet mehrsprachige Sprache. |
| `custom_vocabulary` | String-Array | Bis zu 1.000 benutzerdefinierte Begriffe, Akronyme, Markennamen oder Eigennamen, um die Spracherkennung zu optimieren. |
| `mode` | String | Transkriptionsmodus: `"VERBATIM"` (Standard) oder `"SMART"` (Smart-Transkription). Wenn diese Option auf `"SMART"` gesetzt ist, entfernt das Modell Füllwörter, formatiert Listen und korrigiert Unflüssigkeiten. |
| `automatic_activity_detection.disabled` | Boolesch | Wenn Sie `true` festlegen, wird die automatische Erkennung von Sprachaktivitäten deaktiviert und Sie müssen die Signale `activityStart` und `activityEnd` manuell senden. |

### Felder für Serverantworten

| Feld | Beschreibung |
| --- | --- |
| `server_content.interim_input_transcription` | Hypothese für die vorläufige Teiltranskription mit geringer Latenz, die kontinuierlich ausgegeben wird, während der Nutzer aktiv spricht. |
| `server_content.input_transcription` | Finalisiertes, autoritatives Eingabetranskript, das ausgegeben wird, wenn ein Sprachabschnitt beendet ist. |

## Beschränkungen

- **Sitzungsdauer**:Livetranskriptionssitzungen unterstützen kontinuierliches Streaming für bis zu 10 Minuten.
- **Sprecherbestimmung**:Die Sprecherbestimmung wird in Livestreaming-Sitzungen nicht unterstützt. Verwenden Sie für die Sprecherzuordnung den Nicht-Streaming-Endpunkt [Audio-Transkription](https://ai.google.dev/gemini-api/docs/transcribe?hl=de#speaker-diarization).
- **Zeitstempel auf Wortebene**:Zeitstempel auf Wortebene werden über die Live API nicht unterstützt. Die Live API gibt Zeitstempel auf Äußerungsebene aus (`interim_input_transcription` und `input_transcription`).
- **Benutzerdefiniertes Vokabular**:Sie können bis zu 1.000 Begriffe in `custom_vocabulary` angeben. Die besten Ergebnisse werden jedoch in der Regel mit bis zu 100 Begriffen erzielt.
- **Kompatibilität mit Modi**:Bei der intelligenten Transkription (`"mode": "SMART"`) werden Füllwörter entfernt und der Text wird entsprechend der Intention formatiert. Sie kann jedoch nicht mit Wortanmerkungen kombiniert werden.

## Nächste Schritte

- [Dokumentation zu Gemini Transcribe](https://ai.google.dev/gemini-api/docs/transcribe?hl=de) für nicht gestreamte Audiodateien
- Lesen Sie die [Übersicht über die Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=de) für Konversations-Sprach-Agents.
- Weitere Informationen zur Echtzeit-Übersetzung von Sprache zu Sprache finden Sie im [Leitfaden zur Live-Übersetzung](https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=de).
- Die Preise für das Streaming über die Live API [findest du auf der Preisseite](https://ai.google.dev/gemini-api/docs/pricing?hl=de#gemini-3.5-transcribe-live).
- [Leitfaden zu den Funktionen der Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-10 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-10 (UTC)."],[],[]]
