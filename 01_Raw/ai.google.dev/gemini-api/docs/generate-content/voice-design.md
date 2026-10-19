---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/voice-design?hl=de
fetched_at: 2026-10-19T05:38:35.685719+00:00
title: "Sprachdesign \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs/generate-content?hl=de)

Feedback geben

# Sprachdesign

Mit Voice Design können Sie mithilfe des Gemini API-Endpunkts „Voices“ (`POST /v1beta/voices`) eine völlig neue, dauerhafte stimmliche Persona aus einer natürlichsprachlichen Beschreibung erstellen. Anstatt auf vorgefertigte Stimmen beschränkt zu sein oder Referenz-Audio aufzunehmen, können Sie das Alter, das Stimm-Timbre, den Akzent und die grundlegende Sprechweise einer Figur beschreiben und erhalten eine wiederverwendbare `voice_...`-ID, die in Ihrem Projekt gespeichert wird.

Die schnellste Möglichkeit, benutzerdefinierte Stimmen zu entwerfen, zu testen und zu iterieren, ist das interaktive **Voice Design**-Studio in [Google AI Studio](https://aistudio.google.com/generate-speech?hl=de). Sie können benutzerdefinierte Identitäten aus Text-Prompts generieren, sie mit Beispielskripts testen und die resultierende `voice_...`-ID direkt in Ihren Anwendungscode kopieren.

[In Google AI Studio ausprobieren](https://aistudio.google.com/generate-speech?hl=de)

Sowohl [Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=de) (`gemini-3.8-flash-tts`) als auch [Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=de) (`gemini-3.8-flash-lite-tts`) unterstützen Voice Design.

## Design-Stimme erstellen

Mit dem Google GenAI SDK (`google-genai` 2.25.0+ / `@google/genai` 2.24.0+) oder der REST API können Sie eine benutzerdefinierte Stimme aus einer Textbeschreibung erstellen. Bei `"prompted"`-Stimmen geben sowohl `voices.create` (`CreateVoice`) als auch `voices.get` (`GetVoice`) ein reines Ausgabefeld `sample_audio` (`mime_type: "audio/wav"`, base64-codiertes `data`) zurück, sodass Sie die generierte Stimme sofort anhören können:

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

## So funktioniert das Voice-Design

1. **Sprache mit Prompt erstellen**:Rufen Sie `voices.create` (`POST /v1beta/voices`) mit `type="prompted"` und `store=True` auf.
2. **Dauerhafte `voice_id`- und `sample_audio`-Vorschau erhalten**:Die API generiert die stimmliche Identität, speichert sie in Ihrem Projekt und gibt eine dauerhafte ID (z. B. `voice_abc123...`) zusammen mit `sample_audio` (`mime_type: "audio/wav"`, base64-codiertes `data`) zurück, das die generierte Vorschau-Audio für die Stimme enthält.
3. **Sprache synthetisieren**:Übergeben Sie `voice_id` in `speechConfig.voiceConfig.voice`, wenn Sie `generateContent` aufrufen.

## Sprache mit Ihrer benutzerdefinierten Stimme synthetisieren

Übergeben Sie den zurückgegebenen `id` (`voice_...`) in `voiceConfig.voice`, wenn Sie `generateContent` aufrufen:

### Python

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=[{
        "role": "user",
        "parts": [{
            "text": (
                "Look out past the rings of Saturn. Those faint photons left"
                " their source millions of years ago."
            ),
            "speech_metadata": {"style": "reflective and awe-inspired"},
        }],
    }],
    config={
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {"voice": created_voice.id}
        },
    },
)

audio_bytes = response.candidates[0].content.parts[0].inline_data.data
with open("designed_voice.wav", "wb") as f:
    f.write(audio_bytes)
```

### JavaScript

```
import * as fs from "node:fs";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();

const response = await ai.models.generateContent({
  model: "gemini-3.8-flash-tts",
  contents: [{
    role: "user",
    parts: [{
      text: "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
      speechMetadata: { style: "reflective and awe-inspired" },
    }],
  }],
  config: {
    responseModalities: ["AUDIO"],
    speechConfig: {
      voiceConfig: { voice: createdVoice.id },
    },
  },
});

const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
if (data) {
  fs.writeFileSync("designed_voice.wav", Buffer.from(data, "base64"));
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{
        "text": "Look out past the rings of Saturn. Those faint photons left their source millions of years ago.",
        "speech_metadata": {
          "style": "reflective and awe-inspired"
        }
      }]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {
          "voice": "voice_YOUR_DESIGNED_VOICE_ID"
        }
      }
    }
  }'
```

## Stimmen verwalten

Sie können Ihre gespeicherten Stimmen jederzeit mit der Voices API auflisten, filtern, prüfen und löschen (alle Filterparameter finden Sie unter [Erweiterte Stimmenbibliothek und Filterung](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=de#voice-library)).

- **Speicherlimits und TTL**:Für zustandsbehaftete Stimmen (`store=True`, die für angeforderte und replizierte Stimmen freigegeben sind) gilt ein Limit von **200 Stimmen pro Projekt** und eine **Gültigkeitsdauer von 1 Jahr** (Time-to-Live, TTL).
- **Verfügbarkeit von `sample_audio`**:`voices.create()` (`CreateVoice`) und `voices.get()` (`GetVoice`) füllen `sample_audio` (`mime_type:
  "audio/wav"`, base64-codiertes `data`) für `"prompted"`-Stimmen aus. Damit der Eintrag übersichtlich bleibt, wird in `voices.list()` (`ListVoices`) `sample_audio` ausgelassen (und `sample_audio` ist für `"replicated"`- und `"prebuilt"`-Stimmen nicht festgelegt).

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

## Best Practices für Prompts für das Voice-Design

- **Dauerhafte stimmliche Merkmale im Voice-Design festlegen, nicht in `style`**:Lege unveränderliche Merkmale wie Alter, Geschlecht, Klangfarbe, stimmliche Textur und regionalen Akzent beim Erstellen der Stimme in `voices.create` fest.
- **`speech_metadata.style` für situationsbezogene Emotionen reservieren**:Nachdem Sie Ihre benutzerdefinierte Stimme erstellt haben, verwenden Sie kurze `style`-Prompts (z. B. `"whispered urgently"` oder `"cheerful and energetic"`), um die schrittweise Darstellung zu steuern, ohne die grundlegende Identität des Sprechers zu ändern.
- **Spezifisch und prägnant sein**:Eine klare Beschreibung in ein bis zwei Sätzen (z. B. *„Eine dynamische Sportmoderatorin in den Dreißigern mit leichtem Akzent aus dem Mittleren Westen“*) führt zu besseren, konsistenteren Ergebnissen als widersprüchliche oder zu lange Absätze.

## Nächste Schritte

- [Weitere Informationen zur Stimmreplikation](https://ai.google.dev/gemini-api/docs/generate-content/voice-replication?hl=de)
- Weitere Informationen zu Stil auf Turn-Ebene, Inline-Tags und Dialogen mit mehreren Sprechern finden Sie im [Leitfaden zur Sprachsynthese](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation?hl=de).

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-24 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-24 (UTC)."],[],[]]
