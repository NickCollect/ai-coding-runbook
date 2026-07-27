---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=de
fetched_at: 2026-07-27T04:42:47.883677+00:00
title: "Gemini-Denken \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Die [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de) ist jetzt allgemein verfügbar. Wir empfehlen, diese API zu verwenden, um auf alle aktuellen Funktionen und Modelle zuzugreifen.

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Gemini-Denken

Die [Modelle der Gemini 3- und 2.5-Serie](https://ai.google.dev/gemini-api/docs/models?hl=de) nutzen einen „Denkprozess“, der ihre Fähigkeiten zum logischen Denken und zur mehrstufigen Planung erheblich verbessert. Dadurch eignen sie sich hervorragend für komplexe Aufgaben wie Programmieren, fortgeschrittene Mathematik und Datenanalyse.

Wenn Sie ein Denkmodell verwenden, überlegt Gemini intern, bevor es antwortet. Die Interactions API stellt diese Begründung über `thought`-Schritte bereit. Das sind spezielle Schritte, die chronologisch neben Funktionsaufrufen, Nutzereingaben oder Modellausgaben im `steps`-Array angezeigt werden.

Jeder Denkprozessschritt enthält zwei Felder:

| Feld | Erforderlich? | Beschreibung |
| --- | --- | --- |
| `signature` | ✅ Ja | Eine verschlüsselte Darstellung des internen Entscheidungsstatus des Modells. Immer vorhanden, auch wenn das Modell nur minimalen Reasoning-Prozess durchführt. |
| `summary` | ❌ Nein | Eine Reihe von Inhalten (Text und/oder Bilder), die die Begründung zusammenfassen. Kann je nach [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=de)-Konfiguration, der Menge der vom Modell durchgeführten Schlussfolgerungen oder dem Inhaltstyp leer sein (z. B. haben Bild-Latents möglicherweise keine Textzusammenfassungen). |

## Interaktionen mit dem Denkprozess

Eine Interaktion mit einem Denkmodell zu starten, ähnelt jeder anderen Interaktionsanfrage. Geben Sie im Feld `model` eines der [Modelle mit Unterstützung für das Denken](#thinking-levels) an:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## Zusammenfassungen der Gedanken

Zusammenfassungen der Überlegungen geben Einblick in den internen Prozess der Problemlösung des Modells.
Standardmäßig wird nur die endgültige Ausgabe zurückgegeben. Sie können Gedankenzusammenfassungen mit `thinking_summaries` aktivieren:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="What is the sum of the first 50 prime numbers?",
    generation_config={
        "thinking_summaries": "auto"
    }
)

for step in interaction.steps:
    if step.type == "thought":
        print("Thought summary:")
        if step.summary:
            for content_block in step.summary:
                if content_block.type == "text":
                    print(content_block.text)
        print()
    elif step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print("Answer:")
                print(content_block.text)
                print()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "What is the sum of the first 50 prime numbers?",
    generation_config: {
        thinking_summaries: "auto"
    }
});

for (const step of interaction.steps) {
    if (step.type === "thought") {
        console.log("Thought summary:");
        if (step.summary) {
            for (const contentBlock of step.summary) {
                if (contentBlock.type === "text") console.log(contentBlock.text);
            }
        }
    } else if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log("Answer:");
                console.log(contentBlock.text);
            }
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

Ein Denkblock darf in diesen Fällen **nur eine Signatur ohne Zusammenfassung** enthalten:

- Einfache Anfragen, bei denen das Modell nicht genügend Informationen berücksichtigt hat, um eine Zusammenfassung zu erstellen
- `thinking_summaries: "none"`, in denen Zusammenfassungen explizit deaktiviert sind
- Für bestimmte Arten von Gedankeninhalten, z. B. Bilder, sind möglicherweise keine Textzusammenfassungen verfügbar.

Ihr Code sollte immer Thought-Blöcke verarbeiten, in denen `summary` leer ist oder fehlt.

## Streaming mit Denken

Streaming verwenden, um während der Generierung inkrementelle Zusammenfassungen zu erhalten.
Gedankenblöcke werden über Server-Sent Events (SSE) mit zwei unterschiedlichen Deltatyps bereitgestellt:

| Deltatyp | Enthält | Wann werden die Daten gesendet? |
| --- | --- | --- |
| `thought_summary` | Zusammenfassungen in Text- oder Bildform | Ein oder mehrere Deltas mit inkrementeller Zusammenfassung |
| `thought_signature` | Die kryptografische Signatur | das letzte Delta vor dem `step.stop` |

### Python

```
from google import genai

client = genai.Client()

prompt = """
Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?
"""

thoughts = ""
answer = ""

stream = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt,
    generation_config={
        "thinking_summaries": "auto"
    },
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "thought_summary":
            if not thoughts:
                print("Thinking...")
            summary_text = event.delta.content.text
            print(f"[Thought] {summary_text}", end="")
            thoughts += summary_text
        elif event.delta.type == "text" and event.delta.text:
            if not answer:
                print("\nAnswer:")
            print(event.delta.text, end="")
            answer += event.delta.text
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const prompt = `Alice, Bob, and Carol each live in a different house on the same
street: red, green, and blue. Alice does not live in the red house.
Bob does not live in the green house.
Carol does not live in the red or green house.
Which house does each person live in?`;

let thoughts = "";
let answer = "";

const stream = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: prompt,
    generation_config: {
        thinking_summaries: "auto"
    },
    stream: true
});

for await (const event of stream) {
    if (event.event_type === "step.delta") {
        if (event.delta.type === "thought_summary") {
            if (!thoughts) console.log("Thinking...");
            const text = event.delta.content?.text || "";
            process.stdout.write(`[Thought] ${text}`);
            thoughts += text;
        } else if (event.delta.type === "text" && event.delta.text) {
            if (!answer) console.log("\nAnswer:");
            process.stdout.write(event.delta.text);
            answer += event.delta.text;
        }
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  --no-buffer \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

Die Streaming-Antwort verwendet vom Server gesendete Ereignisse (SSE, Server-Sent Events) und besteht aus Schritten und Ereignissen, z. B.:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.5-flash"},"event_type":"interaction.created"}

event: step.start
data: {"index":0,"step":{"signature":"","summary":[{"text":"**Evaluating the clues**\n\nI'm considering...","type":"text"}],"type":"thought"},"event_type":"step.start"}

event: step.delta
data: {"index":0,"delta":{"signature":"EpoGCpcGAXLI2nx/...","type":"thought_signature"},"event_type":"step.delta"}

event: step.stop
data: {"index":0,"event_type":"step.stop"}

event: step.start
data: {"index":1,"step":{"content":[{"text":"Based on the clues provided, here","type":"text"}],"type":"model_output"},"event_type":"step.start"}

event: step.delta
data: {"index":1,"delta":{"text":" is the answer to your question...","type":"text"},"event_type":"step.delta"}

event: step.stop
data: {"index":1,"event_type":"step.stop"}

event: interaction.completed
data: {"interaction":{"id":"v1_xxx","status":"completed","usage":{"total_tokens":530,"total_input_tokens":62,"total_output_tokens":171,"total_thought_tokens":297}},"event_type":"interaction.completed"}

event: done
data: [DONE]
```

## Kontrolliertes Denken

Gemini-Modelle verwenden standardmäßig dynamisches Denken und passen den Aufwand für das Reasoning automatisch an die Komplexität der Anfrage an. Sie können dieses Verhalten mit dem Parameter `thinking_level` steuern.

| Modell | Standardüberlegung | Unterstützte Ebenen |
| --- | --- | --- |
| gemini-3.1-pro-preview | Ein (hoch) | niedrig, mittel, hoch |
| gemini-3.1-flash-lite-image | An (minimal) | minimal, hoch |
| gemini-3-flash-preview | Ein (hoch) | minimal, niedrig, mittel, hoch |
| gemini-3-pro-preview | Ein (hoch) | niedrig, hoch |
| gemini-3.5-flash | An (mittel) | minimal, niedrig, mittel, hoch |
| gemini-2.5-pro | An | niedrig, mittel, hoch |
| gemini-2.5-flash | An | niedrig, mittel, hoch |
| gemini-2.5-flash-lite | Aus | niedrig, mittel, hoch |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Provide a list of 3 famous physicists and their key contributions",
    generation_config={
        "thinking_level": "low"
    }
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.5-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

## Gedankensignaturen

Gedankensignaturen sind verschlüsselte Darstellungen der internen Argumentation des Modells. Sie müssen die Kontinuität der Argumentation über mehrere Interaktionen hinweg aufrechterhalten.

Mit der Interactions API ist die Verarbeitung von Gedanken-Signaturen viel einfacher als mit der `generateContent` API.

### Statusbehafteter Modus (empfohlen)

Wenn Sie die Interactions API standardmäßig im statusbehafteten Modus verwenden (indem Sie `store: true` festlegen und `previous_interaction_id` in nachfolgenden Zügen übergeben), verwaltet der Server automatisch den Unterhaltungsstatus, einschließlich aller Denkblöcke und Signaturen. In diesem Modus müssen Sie nichts in Bezug auf Signaturen unternehmen. Sie werden vollständig serverseitig verarbeitet.

### Zustandsloser Modus

Wenn Sie den Unterhaltungsstatus selbst verwalten (zustandsloser Modus) und bei jeder Anfrage den vollständigen Verlauf der Ein- und Ausgaben übergeben:

- Sie **MÜSSEN** immer alle `thought`-Blöcke genau so noch einmal senden, wie sie vom Modell empfangen wurden.
- Sie sollten **KEINE** Denkblöcke aus dem Verlauf entfernen oder ändern, da sie die Signaturen enthalten, die das Modell für die weitere Argumentation benötigt.
- Wenn Sie das Modell innerhalb einer Sitzung wechseln, sollten Sie die Denkblöcke des vorherigen Modells noch einmal senden. Das Backend verwaltet die Kompatibilität.

## Preise

Wenn der Thinking-Modus aktiviert ist, setzt sich der Preis für die Antwort aus der Summe der Ausgabe-Tokens und der Thinking-Tokens zusammen. Die Gesamtzahl der generierten Denk-Tokens finden Sie im Feld `total_thought_tokens`.

### Python

```
print("Thoughts tokens:", interaction.usage.total_thought_tokens)
print("Output tokens:", interaction.usage.total_output_tokens)
```

### JavaScript

```
console.log(`Thoughts tokens: ${interaction.usage.total_thought_tokens}`);
console.log(`Output tokens: ${interaction.usage.total_output_tokens}`);
```

Denkmodelle generieren vollständige Gedanken, um die Qualität der endgültigen Antwort zu verbessern, und geben dann [Zusammenfassungen](#summaries) aus, um Einblicke in den Denkprozess zu geben. Die Preise basieren auf den vollständigen Thought-Tokens, die das Modell generieren muss, obwohl nur die Zusammenfassung von der API ausgegeben wird.

Weitere Informationen zu Tokens finden Sie im Leitfaden [Tokens zählen](https://ai.google.dev/gemini-api/docs/tokens?hl=de).

## Best Practices

Wenn Sie diese Richtlinien beachten, können Sie Denkmodelle effizient einsetzen.

- **Begründung überprüfen**: Analysieren Sie Zusammenfassungen der Gedankengänge, um Fehler zu verstehen und Prompts zu verbessern.
- **Thinking-Budget steuern**: Weisen Sie das Modell an, bei langen Ausgaben weniger zu überlegen, um Tokens zu sparen.
- **Einfache Aufgaben**: Verwenden Sie minimales oder geringes Denken für den Faktenabruf oder die Klassifizierung (z.B. „Wo wurde DeepMind gegründet?“).
- **Aufgaben moderieren**: Verwenden Sie die Standardlogik, um Konzepte zu vergleichen oder kreative Argumentation zu nutzen (z.B. „Vergleiche Elektro- und Hybridautos“).
- **Komplexe Aufgaben**: Verwenden Sie „Maximales Denken“ für anspruchsvolle Programmier-, Mathematik- oder mehrstufige Planungsaufgaben (z.B. AIME-Mathematikaufgaben lösen).

## Nächste Schritte

- [Textgenerierung](https://ai.google.dev/gemini-api/docs/text-generation?hl=de): Einfache Textantworten
- [Funktionsaufrufe](https://ai.google.dev/gemini-api/docs/function-calling?hl=de): Verbindung zu Tools herstellen
- [Leitfaden zu Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=de): Modellspezifische Funktionen

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-07-06 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-07-06 (UTC)."],[],[]]
