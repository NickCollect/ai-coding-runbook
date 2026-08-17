---
source_url: https://ai.google.dev/gemini-api/docs/music-generation?hl=de
fetched_at: 2026-08-17T02:33:27.262776+00:00
title: "Musik mit Lyria\u00a03 generieren \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Musik mit Lyria 3 generieren

Lyria 3 ist die Familie der Musikgenerierungsmodelle von Google, die über die Gemini API verfügbar sind. Mit Lyria 3 können Sie aus Textprompts oder Bildern hochwertiges Stereo-Audio mit 44,1 kHz generieren. Diese Modelle liefern strukturelle Kohärenz, einschließlich Gesang, zeitgesteuerter Songtexte und vollständiger Instrumentalarrangements.

Die Lyria 3-Familie umfasst zwei Modelle:

| Modell | Modell-ID | Optimal für | Dauer | Ausgabe |
| --- | --- | --- | --- | --- |
| **Lyria 3 Clip** | `lyria-3-clip-preview` | Kurze Clips, Loops, Vorschauen | 30 Sekunden | MP3 |
| **Lyria 3 Pro** | `lyria-3-pro-preview` | Songs in voller Länge mit Strophen, Refrains und Bridges | Ein paar Minuten (über Prompt steuerbar) | MP3 |

Beide Modelle können mit der neuen
[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) verwendet werden, die multimodale
Eingaben (Text und Bilder) unterstützt und **Stereo-Audio mit 44,1 kHz**
erzeugt.

## Musikclip generieren

Das Modell Lyria 3 Clip generiert immer einen **30-sekündigen** Clip. Rufen Sie zum Generieren eines Clips die Methode `interactions.create` mit einem Text-Prompt auf. Die Antwort enthält immer den generierten Songtext und die Songstruktur sowie das Audio im `steps`-Schema.

### Python

```
import base64
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A short instrumental acoustic guitar piece.",
)

generated_audio = interaction.output_audio
if generated_audio:
    with open("music.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
import * as fs from 'fs';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A short instrumental acoustic guitar piece.',
});

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
  fs.writeFileSync('music.mp3', Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
  console.log(`Lyrics:\n${lyrics}`);
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-clip-preview",
    "input": "A short instrumental acoustic guitar piece."
}'
```

Sie können generierte Musikdaten mit der Eigenschaft `interaction.output_audio` abrufen, die den letzten generierten Audioblock zurückgibt. Sie können auch den Songtext und die Struktur des Songs mit der Eigenschaft `interaction.output_text` abrufen. Weitere Informationen zu Convenience-Eigenschaften finden Sie in der
[Übersicht zu Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de#convenience-properties).

## Song in voller Länge generieren

Mit dem Modell `lyria-3-pro-preview` können Sie Songs in voller Länge generieren, die ein paar Minuten dauern. Das Pro-Modell versteht die musikalische Struktur und kann Kompositionen mit unterschiedlichen Strophen, Refrains und Bridges erstellen. Sie können die
Dauer beeinflussen, indem Sie sie in Ihrem Prompt angeben (z.B. „Erstelle einen 2-Minuten-Song“) oder
[Zeitstempel](#timing) verwenden, um die Struktur zu definieren.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="An epic cinematic orchestral piece about a journey home. Starts with a solo piano intro, builds through sweeping strings, and climaxes with a massive wall of sound.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody."
}'
```

## Ausgabeformat auswählen

Standardmäßig generieren die Lyria 3-Modelle Audio im **MP3** -Format. Für Lyria 3 Pro können Sie die Ausgabe auch im **WAV** -Format anfordern, indem Sie `response_format` festlegen.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="A beautiful piano melody.",
    response_format={"type": "audio"},
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'A beautiful piano melody.',
    response_format: {
        type: 'audio',
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "A beautiful piano melody.",
    "response_format": {
        "type": "audio"
    }
  }'
```

## Antwort analysieren

Die Antwort von Lyria 3 enthält mehrere Inhaltsblöcke im `steps`-Schema.
Interactions geben eine Abfolge von Schritten zurück, wobei `model_output`-Schritte den generierten Inhalt enthalten.
Textinhaltsblöcke enthalten den generierten Songtext oder eine JSON-Beschreibung der Songstruktur.
Inhaltsblöcke mit dem Typ `audio` enthalten die base64-codierten Audiodaten.

### Python

```
lyrics = []
audio_data = None

generated_audio = interaction.output_audio
if generated_audio:
    with open("output.mp3", "wb") as f:
        f.write(base64.b64decode(generated_audio.data))

lyrics = interaction.output_text
if lyrics:
    print(f"Lyrics:\n{lyrics}")
```

### JavaScript

```
const lyrics = [];
let audioData = null;

const generatedAudio = interaction.output_audio;
if (generatedAudio) {
    fs.writeFileSync("output.mp3", Buffer.from(generatedAudio.data, 'base64'));
}

const lyrics = interaction.output_text;
if (lyrics) {
    console.log("Lyrics:\n" + lyrics);
}
```

### REST

```
# The output from the REST API is a JSON object containing base64 encoded data.
# You can extract the text or the audio data using a tool like jq.
# To extract the audio and save it to a file:
curl ... | jq -r '.steps[] | select(.type=="model_output") | .content[] | select(.type=="audio") | .data' | base64 -d > output.mp3
```

#### Verschachtelte Songtexte und Musik

Da die Ausgabe von Lyria 3 komplex ist und separate Schritte und Blöcke für generierte Songtexte (Text) und den Song selbst (Audio) enthält, bieten Convenience-Eigenschaften eine schnelle und empfohlene Abkürzung.

Wenn Sie jedoch die vollständige programmatische Kontrolle über die Rohzeitachse der vom Server zurückgegebenen Schritte haben möchten (z. B. einzelne Inhaltsblöcke protokollieren, sobald sie empfangen werden), können Sie stattdessen manuell über `steps` iterieren:

### Python

```
lyrics = []
audio_data = None

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "audio":
                audio_data = base64.b64decode(content_block.data)
            elif content_block.type == "text":
                lyrics.append(content_block.text)

if lyrics:
    print("Lyrics:\n" + "\n".join(lyrics))

if audio_data:
    with open("output.mp3", "wb") as f:
        f.write(audio_data)
```

### JavaScript

```
const lyrics = [];
let audioData = null;

for (const step of interaction.steps) {
    if (step.type === 'model_output') {
        for (const contentBlock of step.content) {
            if (contentBlock.type === 'audio') {
                audioData = Buffer.from(contentBlock.data, 'base64');
            } else if (contentBlock.type === 'text') {
                lyrics.push(contentBlock.text);
            }
        }
    }
}

if (lyrics.length) {
    console.log("Lyrics:\n" + lyrics.join("\n"));
}

if (audioData) {
    fs.writeFileSync("output.mp3", audioData);
}
```

## Musik aus Bildern generieren

Lyria 3 unterstützt multimodale Eingaben. Sie können in der Liste `input` neben Ihrem Textprompt bis zu **10 Bilder** angeben. Das Modell komponiert dann Musik, die von den visuellen Inhalten inspiriert ist.

### Python

```
import base64

with open("desert_sunset.jpg", "rb") as f:
    image_bytes = f.read()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

response = client.interactions.create(
    model="lyria-3-pro-preview",
    input=[
        {
            "type": "text",
            "text": "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": image_b64,
        },
    ],
)
```

### JavaScript

```
import * as fs from "fs";

const imageBytes = fs.readFileSync("desert_sunset.jpg").toString("base64");

const interaction = await client.interactions.create({
    model: "lyria-3-pro-preview",
    input: [
        {
            type: "text",
            text: "An atmospheric ambient track inspired by the mood and colors in this image.",
        },
        {
            type: "image",
            mime_type: "image/jpeg",
            data: imageBytes,
        },
    ],
});
```

### REST

```
# Pass base64 encoded image data directly:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": [
      {"type": "text", "text": "An atmospheric ambient track inspired by the mood and colors in this image."},
      {"type": "image", "mime_type": "image/jpeg", "data": "/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPxA="}
    ]
  }'
```

## Benutzerdefinierte Songtexte angeben

Sie können Ihre eigenen Songtexte schreiben und in den Prompt einfügen. Verwenden Sie Abschnitts-Tags wie `[Verse]`, `[Chorus]` und `[Bridge]`, damit das Modell die Songstruktur versteht:

### Python

```
prompt = """
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
Create a dreamy indie pop song with the following lyrics:

[Verse 1]
Walking through the neon glow,
city lights reflect below,
every shadow tells a story,
every corner, fading glory.

[Chorus]
We are the echoes in the night,
burning brighter than the light,
hold on tight, don't let me go,
we are the echoes down below.

[Verse 2]
Footsteps lost on empty streets,
rhythms sync to heartbeats,
whispers carried by the breeze,
dancing through the autumn leaves.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Create a dreamy indie pop song with the following lyrics: ..."
  }'
```

## Timing und Struktur steuern

Mit Zeitstempeln können Sie genau angeben, was in bestimmten Momenten im Song passiert. Das ist nützlich, um zu steuern, wann Instrumente einsetzen, wann Songtexte gesungen werden und wie der Song weitergeht:

### Python

```
prompt = """
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
"""

interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input=prompt,
)
```

### JavaScript

```
const prompt = `
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled
              vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody
              and gentle vocals singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring
              synth leads. The lyrics are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
`;

const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: prompt,
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "[0:00 - 0:10] Intro: ..."
  }'
```

## Instrumentaltracks generieren

Für Hintergrundmusik, Game-Soundtracks oder jeden Anwendungsfall, bei dem kein Gesang erforderlich ist, können Sie das Modell auffordern, reine Instrumentaltracks zu erstellen:

### Python

```
interaction = client.interactions.create(
    model="lyria-3-clip-preview",
    input="A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-clip-preview',
    input: 'A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-clip-preview",
    "input": "A bright chiptune melody in C Major, retro 8-bit video game style. Instrumental only, no vocals."
  }'
```

## Musik in verschiedenen Sprachen generieren

Lyria 3 generiert Songtexte in der Sprache Ihres Prompts. Wenn Sie einen Song mit französischen Songtexten generieren möchten, schreiben Sie Ihren Prompt auf Französisch. Das Modell passt seinen Gesangsstil und seine Aussprache an die Sprache an.

### Python

```
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.",
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    model: 'lyria-3-pro-preview',
    input: 'Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique.',
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "lyria-3-pro-preview",
    "input": "Crée une chanson pop romantique en français sur un coucher de soleil à Paris. Utilise du piano et de la guitare acoustique."
  }'
```

## Modellintelligenz

Lyria 3 analysiert Ihren Prompt-Prozess, wobei das Modell die musikalische Struktur (Intro, Strophe, Refrain, Bridge usw.) anhand Ihres Prompts ableitet.
Das geschieht, bevor das Audio generiert wird, und sorgt für strukturelle Kohärenz und Musikalität.

## Anleitung zu Prompts

Je genauer Ihr Prompt ist, desto besser sind die Ergebnisse. Hier sind einige Beispiele für Informationen, die Sie angeben können, um die Generierung zu steuern:

- **Genre**: Geben Sie ein Genre oder eine Mischung aus Genres an (z.B. „Lo-Fi-Hip-Hop“,
  „Jazz-Fusion“, „Orchestral-Soundtrack“).
- **Instrumente**: Nennen Sie bestimmte Instrumente (z.B. „Fender Rhodes-Piano“,
  „Slide-Gitarre“, „TR-808-Drum-Machine“).
- **BPM**: Legen Sie das Tempo fest (z.B. „120 BPM“, „langsames Tempo um 70 BPM“).
- **Tonart/Tonleiter**: Geben Sie eine Tonart an (z.B. „in G-Dur“, „D-Moll“).
- **Stimmung und Atmosphäre**: Verwenden Sie beschreibende Adjektive (z.B. „nostalgisch“,
  „aggressiv“, „ätherisch“, „vertäumt“).
- **Struktur**: Verwenden Sie Tags wie `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]`,
  `[Outro]` oder Zeitstempel, um den Ablauf des Songs zu steuern.
- **Dauer**: Das Modell „Clip“ erzeugt immer 30-sekündige Clips. Geben Sie für das Modell „Pro“ die gewünschte Länge in Ihrem Prompt an (z.B. „Erstelle einen 2-Minuten-Song“) oder verwenden Sie Zeitstempel, um die Dauer zu steuern.

### Beispiele für Prompts

Beispiele für effektive Prompts:

- `"A 30-second lofi hip hop beat with dusty vinyl crackle, mellow Rhodes
  piano chords, a slow boom-bap drum pattern at 85 BPM, and a jazzy upright
  bass line. Instrumental only."`
- `"An upbeat, feel-good pop song in G major at 120 BPM with bright acoustic
  guitar strumming, claps, and warm vocal harmonies about a summer road
  trip."`
- `"A dark, atmospheric trap beat at 140 BPM with heavy 808 bass, eerie synth
  pads, sharp hi-hats, and a haunting vocal sample. In D minor."`

## Best Practices

- **Zuerst mit Clip iterieren** Verwenden Sie das schnellere Modell `lyria-3-clip-preview`, um mit Prompts zu experimentieren, bevor Sie eine Generierung in voller Länge mit `lyria-3-pro-preview` starten.
- **Machen Sie genaue Angaben** Vage Prompts führen zu allgemeinen Ergebnissen. Geben Sie Instrumente, BPM, Tonart, Stimmung und Struktur an, um die besten Ergebnisse zu erzielen.
- **Passen Sie die Sprache an** Geben Sie den Prompt in der Sprache an, in der Sie den Songtext haben möchten.
- **Abschnitts-Tags verwenden** Die Tags `[Verse]`, `[Chorus]` und `[Bridge]` geben dem Modell eine klare Struktur, an die es sich halten kann.
- **Songtexte von Anweisungen trennen** Wenn Sie benutzerdefinierte Songtexte angeben, trennen Sie sie deutlich von Ihren Anweisungen zur musikalischen Ausrichtung.

## Beschränkungen

- **Sicherheit**: Alle Prompts werden von Sicherheitsfiltern geprüft. Prompts, die die Filter auslösen, werden blockiert. Dazu gehören Prompts, in denen bestimmte Stimmen von Künstlern angefordert werden oder urheberrechtlich geschützte Songtexte generiert werden sollen.
- **Wasserzeichen**: Alle generierten Audioinhalte enthalten ein
  [SynthID-Audio-Wasserzeichen](https://ai.google.dev/responsible/docs/safeguards/synthid?hl=de) zur
  Identifizierung. Dieses Wasserzeichen ist für das menschliche Ohr nicht wahrnehmbar und beeinträchtigt das Hörerlebnis nicht.
- **Bearbeitung in mehreren Schritten**: Die Musikgenerierung ist ein Prozess in einem Schritt.
  Die iterative Bearbeitung oder Verfeinerung eines generierten Clips durch mehrere Prompts wird in der aktuellen Version von Lyria 3 nicht unterstützt.
- **Länge**: Das Modell „Clip“ erzeugt immer 30-sekündige Clips. Das Modell „Pro“ generiert Songs, die ein paar Minuten dauern. Die genaue Dauer kann über Ihren Prompt beeinflusst werden.
- **Determinismus**: Die Ergebnisse können zwischen den Aufrufen variieren, auch bei demselben Prompt.

## Nächste Schritte

- Preise für [Lyria 3-Modelle](https://ai.google.dev/gemini-api/docs/pricing?hl=de) ansehen
- [Musikgenerierung in Echtzeit](https://ai.google.dev/gemini-api/docs/realtime-music-generation?hl=de)
  mit Lyria RealTime ausprobieren.
- Unterhaltungen mit mehreren Sprechern mit den
  [TTS-Modellen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=de) generieren
- Informationen zum Generieren von [Bildern](https://ai.google.dev/gemini-api/docs/image-generation?hl=de) oder [Videos](https://ai.google.dev/gemini-api/docs/video?hl=de)
- Informationen dazu, wie Gemini [Audiodateien verstehen](https://ai.google.dev/gemini-api/docs/audio?hl=de) kann.
- Unterhaltungen mit Gemini in Echtzeit über die
  [Live API](https://ai.google.dev/gemini-api/docs/live?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-30 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-30 (UTC)."],[],[]]
