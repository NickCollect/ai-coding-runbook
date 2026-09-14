---
source_url: https://ai.google.dev/gemini-api/docs/live-api/live-translate?hl=de
fetched_at: 2026-09-14T05:39:57.037296+00:00
title: "Live-\u00dcbersetzung mit der Gemini Live API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Live-Übersetzung mit der Gemini Live API

Die Gemini Live API unterstützt die Echtzeit-Sprache-zu-Sprache-Übersetzung mit geringer Latenz zwischen mehr als 70 Sprachen mit dem Modell [`gemini-3.5-live-translate-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview?hl=de). Wenn Sie die Live API mit Übersetzungseinstellungen konfigurieren, können Sie Audio in einer Sprache streamen und übersetzte Audioausgabe in einer anderen Sprache empfangen. So ist eine nahtlose Sprachübersetzung in Echtzeit möglich.

[Live Translate in Google AI Studio ausprobierenmic](https://aistudio.google.com/live?model=gemini-3.5-live-translate-preview&hl=de)
[Beispiel-App von GitHub klonencode](https://github.com/google-gemini/gemini-live-api-examples)
[Coding-Agent-Skills verwendenterminal](https://ai.google.dev/gemini-api/docs/coding-agents?hl=de#gemini-live-api-dev)

## Live-Kundenservicemitarbeiter im Vergleich zur Live-Übersetzung

Beide verwenden die Live API, aber das mentale Modell für die Live-Übersetzung unterscheidet sich von Echtzeit-Interaktionen mit einem Agenten.

| Frag den Kundenservice | Live-Übersetzung |
| --- | --- |
| **Das Modell fungiert als Assistent.** Er hört zu, zieht Schlüsse und führt Aktionen in Ihrem Namen aus. | **Das Modell fungiert als Dolmetscher.** Sie verhält sich wie eine Echtzeit-Übersetzungspipeline. |
| **Verwendet rundenbasierte Interaktionen.** Sie basiert auf Pausen und der Erkennung von Intentionen und kann Unterbrechungen verarbeiten. | **Verwendet die kontinuierliche Streamverarbeitung.** Übersetzt, während der Sprecher spricht, ohne auf die Reihe zu warten. |
| **Unterstützt Tools und Agenten.** Native Unterstützung für Funktionsaufrufe, Google Suche und Anweisungen. | **Unterstützt nur die Übersetzung.** Reine Übersetzung mit niedriger Latenz; keine Unterstützung für Tools oder Anleitungen. |
| **Vollständig multimodal**: Unterstützt Text-, Audio-, Video- und Bildeingaben. | **Audio eingeschränkt.** Die Eingabe ist auf Audio beschränkt, um strenge Echtzeit-Latenzschwellenwerte einzuhalten. |
| **Detaillierte Konfiguration**: Verwendet Generierung, Sprache, Tools und Systemanweisungen. | **Vereinfachte Konfiguration**: Legen Sie `target_language_code` und Schalter wie `echo_target_language` fest. |

## Jetzt starten

Die folgenden Beispiele zeigen, wie Sie einen Client initialisieren und mit einer Übersetzungskonfiguration eine Verbindung zur Live API herstellen.

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

## Audio senden

Wenn Sie Spracheingaben für die Übersetzung streamen möchten, senden Sie rohes 16‑Bit-PCM-Audio im Little-Endian-Format.

- **Eingabeaudioformat**: Rohes 16‑Bit-PCM mit 16 kHz (Mono, Little Endian).
- **Audioausgabeformat**: Rohes 16‑Bit-PCM mit 24 kHz (Mono, Little Endian).
- **Chunk-Größe und Latenz**: Senden Sie Audio in Chunks von 100 ms.

Die folgenden Beispiele zeigen, wie Sie Audio-Chunks an die Sitzung senden.

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

## Konfiguration

Wenn Sie die Übersetzung aktivieren möchten, müssen Sie `translationConfig` in `generationConfig` während der Sitzungseinrichtung angeben.

### Einrichtungsnachrichten konfigurieren

Das `generationConfig` unterstützt die folgenden Felder, um Transkripte zu aktivieren:

- **`inputAudioTranscription`**: Ein Objekt, das, sofern vorhanden, dem Modell ermöglicht, Texttranskripte der Audioeingabe zu senden.
- **`outputAudioTranscription`**: Ein Objekt, das, sofern vorhanden, dem Modell ermöglicht, Texttranskripte der (übersetzten) Audioausgabe zu senden.

`translationConfig` unterstützt die folgenden Felder:

- **`targetLanguageCode`**: Der [BCP-47-Sprachcode](#supported-languages) der Sprache, in die das Modell übersetzen soll (z.B. `"pl"` für Polnisch, `"es"` für Spanisch). Die Standardeinstellung ist `"en"`.
- **`echoTargetLanguage`**: Ein boolescher Wert, der angibt, wie mit Audioeingaben umgegangen werden soll, die bereits in der Zielsprache vorliegen. Wenn der Wert auf `true` gesetzt ist, gibt das Modell Audioeingaben, die bereits in der Zielsprache vorliegen, unverändert wieder. Wenn der Wert auf `false` gesetzt ist, gibt das Modell keine Antwort aus, wenn die Eingabesprache bereits die Zielsprache ist. Die Standardeinstellung ist `false`.

Hier sehen Sie ein Beispiel für die Struktur der Einrichtungsnachricht:

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

## Einmal-Tokens in clientseitigen Anwendungen verwenden

Bei Client-Server-Anwendungen können Sie [kurzlebige Tokens](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=de) (derzeit in `v1beta`) verwenden, um zu verhindern, dass Ihr API-Schlüssel offengelegt wird.

Bei der Verwendung von temporären Tokens mit der Live-Übersetzung gilt Folgendes:

1. Sie müssen den Endpunkt `v1beta` verwenden.
2. **Konfiguration für das Sperren**:Standardmäßig sollten Sie die `translationConfig` in den Einschränkungen für die Token-Erstellung auf Ihrem Server angeben. So wird sichergestellt, dass die Übersetzungskonfiguration gesperrt ist und nicht vom Client manipuliert werden kann.
3. **Konfiguration zum Entsperren**:Wenn Sie `translationConfig` auf der Clientseite festlegen möchten, z. B. damit ein Nutzer seine eigene Zielsprache auswählen kann, müssen Sie sie aus der Anfrage zum Erstellen des Tokens weglassen und stattdessen `"lock_additional_fields": []` festlegen. Dadurch wird die Möglichkeit freigeschaltet, `translationConfig` clientseitig festzulegen.

### Eingeschränktes sitzungsspezifisches Token erstellen

Die folgenden Beispiele zeigen, wie Sie ein temporäres Token mit Übersetzungsbeschränkungen erstellen.

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

## Beschränkungen

- **Eingabemodalitäten**: Für die Übersetzung wird nur Audioeingabe unterstützt. Texteingabe wird nicht unterstützt.
- **Stimmreplikation**: Die Stimmreplikation kann uneinheitlich sein. Stimmen können sich nach längeren Pausen ändern, basierend auf dem Beginn der Sprache das falsche Geschlecht zuweisen oder bei schnellen Unterhaltungen mit mehreren Sprechern bei einer Stimme bleiben.
- **Spracherkennung**: Die Spracherkennung hat Probleme mit starken Akzenten, ähnlichen Sprachen (z. B. Spanisch und Portugiesisch) oder schnellen Sprachwechseln. **Hinweis**:Dies sollte sich nur auf das Eingabetranskript auswirken. Sprachcodes und die endgültige Übersetzung sollten weiterhin korrekt sein.
- **Hintergrundaudio**: Das Modell ist so konzipiert, dass Rauschen und Musik herausgefiltert werden, um eine saubere Sprachausgabe zu erzeugen. Es kann jedoch sein, dass nicht alle Hintergrundgeräusche ignoriert werden.
- **Echo-Zielsprache**: Wenn `echoTargetLanguage: true`, können Hintergrundgeräusche oder Musik Artefakte im übersetzten Audio verursachen, wenn das Eingabe-Audio bereits in der Zielsprache ist.

## Unterstützte Sprachen

Die folgenden Sprachen werden für die Live-Übersetzung unterstützt.

| Sprache | BCP-47-Code | Sprache | BCP-47-Code |
| --- | --- | --- | --- |
| Afrikaans | af | Kasachisch | kk |
| Akan | ak | Khmer | km |
| Albanisch | sq | Kinyarwanda | rw |
| Amharisch | am | Koreanisch | ko |
| Arabisch | ar | Lao | lo |
| Armenisch | hy | Lettisch | lv |
| Aserbaidschanisch | az | Litauisch | lt |
| Baskisch | eu | Mazedonisch | mk |
| Belarussisch | be | Malaiisch | ms |
| Bengalisch | bn | Malayalam | ml |
| Bulgarisch | bg | Marathi | mr |
| Burmesisch (Myanmar) | my | Mongolisch | mn |
| Katalanisch | ca | Nepalesisch | ne |
| Chinesisch (vereinfacht) | zh-Hans | Norwegisch | no, nb |
| Chinesisch (traditionell) | zh-Hant | Persisch | fa |
| Kroatisch | Std. | Polnisch | pl |
| Tschechisch | cs | Portugiesisch (Brasilien) | pt-BR |
| Dänisch | da | Portugiesisch (Portugal) | pt-PT |
| Niederländisch | nl | Punjabi | pa |
| Englisch | de | Rumänisch | ro |
| Estnisch | et | Russisch | ru |
| Filipino | fil | Serbisch | sr |
| Finnisch | fi | Sindhi | sd |
| Französisch | fr | Singhalesisch | si |
| Galizisch | gl | Slowakisch | sk |
| Georgisch | ka | Slowenisch | sl |
| Deutsch | de | Spanisch | es |
| Griechisch | el | Sundanesisch | su |
| Gujarati | gu | Swahili | sw |
| Hausa | ha | Schwedisch | sv |
| Hebräisch | er | Tamil | ta |
| Hindi | hi | Telugu | te |
| Ungarisch | hu | Thailändisch | th |
| Isländisch | ist | Türkisch | tr |
| Indonesisch | id | Ukrainisch | uk |
| Italienisch | it | Urdu | ur |
| Japanisch | ja | Usbekisch | uz |
| Javanisch | jv | Vietnamesisch | vi |
| Kannada | kn | Zulu | zu |

## Nächste Schritte

- [Vollständigen Leitfaden zu den Funktionen der Live API](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=de) lesen
- [Lesen Sie die Anleitung „Erste Schritte mit dem SDK“](https://ai.google.dev/gemini-api/docs/live-api/get-started-sdk?hl=de).
- [Anleitung für die ersten Schritte mit WebSockets](https://ai.google.dev/gemini-api/docs/live-api/get-started-websocket?hl=de)
- Lesen Sie den Leitfaden zu [Einmal-Tokens](https://ai.google.dev/gemini-api/docs/live-api/ephemeral-tokens?hl=de) für die sichere Authentifizierung in Client-Server-Anwendungen.
- Klonen Sie die [Live API-Beispiele](https://github.com/google-gemini/gemini-live-api-examples) aus GitHub.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-23 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-23 (UTC)."],[],[]]
