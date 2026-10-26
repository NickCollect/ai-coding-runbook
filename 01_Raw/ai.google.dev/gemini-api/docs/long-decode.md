---
source_url: https://ai.google.dev/gemini-api/docs/long-decode?hl=de
fetched_at: 2026-10-26T05:40:45.010587+00:00
title: "Lange Decodierung \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Lange Decodierung

Mit der langen Decodierung kann Gemini 4 Argon für Aufgaben mit komplexen Schlussfolgerungen mehr als 64.000 Tokens generieren, bis zum einheitlichen Kontextfenster von 1 Million Tokens (1.048.576 Tokens, die für Eingabe, Überlegungen und Ausgabe verwendet werden). In der Interactions API aktivieren Sie die lange Decodierung mit der Ausführung im Hintergrund, damit unsere Server automatisch jeden 64.000-Token-Schritt generieren und zu einer einzelnen Interaktion kombinieren.

## Funktionsweise der langen Decodierung

Mit einem einzelnen Modellaufruf werden bis zu 64.000 Tokens generiert. Wenn für eine Antwort mehr als 64.000 Tokens erforderlich sind, generiert der Server sie in Schritten von 64.000 Tokens, die dort fortgesetzt werden, wo der vorherige Schritt aufgehört hat. Bei jedem Schritt wird `interaction.steps` unter derselben Interaktions-ID ein `model_output`-Schritt hinzugefügt. Sie müssen diese Schritte also zusammenführen, um die vollständige Antwort zu lesen:

1. Sie erstellen eine Interaktion mit `background: true` und `max_output_tokens` größer als 65.536, bis zu 1 Million.
2. Der Server generiert den ersten Schritt mit bis zu 64.000 Tokens.
3. Der Server startet den nächsten Hop dort, wo der letzte aufgehört hat, und wiederholt den Vorgang, bis das Modell fertig ist oder alle `max_output_tokens` verwendet wurden.
4. Sie rufen die Interaktion ab oder streamen sie, um das Ergebnis zu erhalten.

### Python

```
import time
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-argon",
    input="Write a complete, rigorous proof of the prime number theorem.",
    background=True,
    generation_config={
        "max_output_tokens": 262144,
        "thinking_level": "high",
    },
)

while interaction.status in ("in_progress", "queued"):
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Each hop adds a model_output step, so join the text of all of them.
text = "".join(
    content.text
    for step in interaction.steps
    if step.type == "model_output"
    for content in step.content
    if content.type == "text"
)
print(text)
print("Status:", interaction.status)
print("Usage:", interaction.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

let interaction = await client.interactions.create({
  model: "gemini-4-argon",
  input: "Write a complete, rigorous proof of the prime number theorem.",
  background: true,
  generation_config: {
    max_output_tokens: 262144,
    thinking_level: "high",
  },
});

while (interaction.status === "in_progress" || interaction.status === "queued") {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  interaction = await client.interactions.get(interaction.id);
}

// Each hop adds a model_output step, so join the text of all of them.
const text = interaction.steps
  .filter((step) => step.type === "model_output")
  .flatMap((step) => step.content ?? [])
  .filter((content) => content.type === "text")
  .map((content) => content.text)
  .join("");
console.log(text);
console.log("Status:", interaction.status);
console.log("Usage:", interaction.usage);
```

### REST

```
# 1. Create the background interaction. It returns an ID right away.
ID=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-4-argon",
    "input": "Write a complete, rigorous proof of the prime number theorem.",
    "background": true,
    "generation_config": {"max_output_tokens": 262144, "thinking_level": "high"}
  }' | jq -r '.id')

# 2. Poll until the status is no longer in_progress or queued.
#    The REST response has no output_text field, so join the text of every model_output step.
while true; do
  RESP=$(curl -s "https://generativelanguage.googleapis.com/v1beta/interactions/$ID" \
    -H "x-goog-api-key: $GEMINI_API_KEY")
  STATUS=$(echo "$RESP" | jq -r '.status')
  if [[ "$STATUS" != "in_progress" && "$STATUS" != "queued" ]]; then
    echo "$RESP" | jq -r '[.steps[]? | select(.type == "model_output") | .content[]? | select(.type == "text") | .text] | join("")'
    echo "$RESP" | jq '{status, usage}'
    break
  fi
  sleep 5
done
```

## Ausgabelimits

Für Streaming- und Nicht-Streaming-Interaktionen gilt standardmäßig ein Ausgabetokenlimit von 64.000. Für Antworten mit bis zu 64.000 Tokens sind also keine Codeänderungen erforderlich. Wenn Sie mehr als 64.000 Tokens generieren möchten, aktivieren Sie die Ausführung im Hintergrund und erhöhen Sie `max_output_tokens`.

| So erstellen Sie die Interaktion | Ausgabelimit |
| --- | --- |
| `background: false` (Streaming oder Nicht-Streaming) | 65.536 Tokens Werte über 65.536 geben einen 400-Fehler zurück. Lange Decodierung demnächst verfügbar. |
| `background: true`, `max_output_tokens` nicht festgelegt | 65.536 Tokens |
| `background: true`, `max_output_tokens` größer als 65.536 | Ihr `max_output_tokens`, bis zu 1.048.576 minus Ihre Eingabe |

## Wann sollte die lange Decodierung verwendet werden?

Die meisten Anfragen sind mit 64.000 Tokens abgeschlossen. Verwenden Sie die lange Decodierung nur, wenn für eine Antwort mehr Überlegungen und Ausgaben erforderlich sind.

| Arbeitslast | Lange Decodierung verwenden? | Warum |
| --- | --- | --- |
| Schwierige mathematische, wissenschaftliche und Forschungsaufgaben sowie formale Beweise | Ja | Das Modell kann mehr als 64.000 Tokens verwenden, um seine Überlegungen zu untersuchen und zu prüfen. |
| Die schwierigsten Coding- und Agentenaufgaben | Ja | Für einige Aufgaben sind mehr als 64.000 Tokens für Überlegungen und Code in einer Antwort erforderlich. Die meisten Coding- und Agentenaufgaben sind mit weniger als 64.000 Tokens abgeschlossen. |
| Bewertungstools, die am Ausgabelimit anhalten | Ja | Die lange Decodierung verhindert abgeschnittene Antworten, wenn das Modell die gesamten 64.000 Tokens für Überlegungen verwendet. |
| Chat, Fragen und Antworten, Zusammenfassung, Klassifizierung und Extraktion | Nein | Diese Aufgaben sind mit deutlich weniger als 32.000 Tokens abgeschlossen. |
| Anfragen mit einer festen Länge, z. B. „Schreibe ein Buch mit 700.000 Wörtern“ | Nein | Das Modell berücksichtigt keine Längenziele. |
| Agenten, die Tools in vielen kurzen Schritten aufrufen | Nein | Jeder Schritt ist kurz. Große Ausgaben in jedem Schritt füllen das gemeinsame Kontextfenster schnell. |
| Prompts in der Nähe des Eingabelimits | Nein | Für die Ausgabe können nur 1.048.576 Tokens minus Ihre Eingabe verwendet werden. |
| Latenzsensitive Anfragen | Nein | Die lange Decodierung kann mehrere Minuten dauern. |

Wenn Sie einen hohen Wert für `max_output_tokens` festlegen, hat das Modell mehr Zeit, über schwierige Probleme nachzudenken. Es entscheidet jedoch weiterhin, wie viel es schreibt. Mit [`thinking_level`](https://ai.google.dev/gemini-api/docs/thinking?hl=de) können Sie festlegen, wie viel Aufwand das Modell für die Überlegungen verwendet.

## Auswahl der Ausführungsmethode für die lange Decodierung

Die Ausführung im Hintergrund ist die einfachste Möglichkeit, die lange Decodierung in der Interactions API auszuführen. Die clientseitige Fortsetzung, bei der Ihr Code jeden Schritt startet, ist mit der GenerateContent API verfügbar. Sie wird bald auch in der Interactions API als erweiterte Option zur Verwaltung Ihrer eigenen Resilienz verfügbar sein.

|  | Ausführung im Hintergrund (Interactions API) | Clientseitige Fortsetzung (GenerateContent API) |
| --- | --- | --- |
| **Wer startet jeden Schritt?** | Unsere Server | Das Google GenAI SDK oder Ihr eigener Code |
| **Tokens pro Anfrage** | Ihr `max_output_tokens` in einer Interaktion | 64.000 pro Stream, 32.000 pro Nicht-Streaming-Anfrage |
| **Laufzeit** | Bis zu 24 Stunden | 20 Minuten |
| **Speicher** | `store: true` erforderlich | Nichts auf dem Server gespeichert. |
| **Optimal für** | Die einfachste Möglichkeit, die lange Decodierung auszuführen | Feinere Kontrolle über Wiederholungsversuche, sodass Sie Ihre eigene Backoff-Strategie, Fehlerbehandlung und Resilienz entwickeln können |

Informationen zur Verwendung der clientseitigen Fortsetzung finden Sie unter [Lange Decodierung mit der GenerateContent API](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=de).

## Lange Decodierung streamen

Wenn Sie Ausgaben und Zusammenfassungen der Überlegungen streamen möchten, sobald sie verfügbar sind, fügen Sie `stream: true` und `thinking_summaries: "auto"` hinzu. Lange Streams können unterbrochen werden, daher muss Ihr Client die Verbindung wiederherstellen. Folgen Sie dem Muster für die Wiederherstellung der Verbindung in der [Anleitung zur Ausführung im Hintergrund](https://ai.google.dev/gemini-api/docs/background-execution?hl=de). Bei der langen Decodierung gelten die folgenden Regeln:

- **Interaktions-ID speichern**:Lesen Sie sie aus dem Ereignis `interaction.created`.
- **Jede `event_id` speichern**:Eine `event_id` kann bei `interaction.status_update`-Ereignissen eintreffen, nicht nur bei Textänderungen.
- **Verbindung mit `last_event_id` wiederherstellen**:Rufen Sie `interactions.get` mit `stream: true` und der letzten `event_id` auf. Der Stream wird nach diesem Ereignis fortgesetzt.
- **Bis zum Ende lesen**:Nachdem Sie die Verbindung wiederhergestellt haben, lesen Sie den Stream bis zum Ende, bevor Sie den Status prüfen. Der Server spielt verpasste Ereignisse auch nach Abschluss der Interaktion ab.
- **Lange Zeitüberschreitungen festlegen**:Legen Sie für HTTP-Lesevorgänge eine Zeitüberschreitung von 15 bis 20 Minuten pro Stream fest.
- **Ausgabe in 5.000-Token-Blöcken erwarten**:Nach den ersten 64.000 Tokens (ungefähr die ersten 10 Minuten) sendet der Stream die Ausgabe in Blöcken von etwa 5.000 Tokens. Pausen zwischen den Blöcken sind normal. Die Interaktion ist nicht blockiert. Lassen Sie die Verbindung also geöffnet.

## Hintergrundstatus

Eine Hintergrundinteraktion kann bis zu 24 Stunden dauern. Sobald der Status nicht mehr `in_progress` oder `queued` ist, verarbeiten Sie den Endstatus anhand dieser Tabelle:

| Status | Bedeutung | Was muss ich tun? |
| --- | --- | --- |
| `completed` | Das Modell ist fertig. | Führen Sie die `model_output`-Schritte in `steps` zusammen und lesen Sie `usage`. Wenn Sie die Unterhaltung fortsetzen möchten, übergeben Sie die `id` dieser Interaktion als `previous_interaction_id`. |
| `requires_action` | Das Modell hat einen Toolaufruf angefordert. | Führen Sie das Tool aus. Senden Sie dann das Ergebnis mit der `id` dieser Interaktion. |
| `incomplete` | Das Modell hat alle `max_output_tokens` verwendet. Der Text kann leer sein, wenn das Modell noch überlegt hat. | Senden Sie die Anfrage noch einmal mit einem höheren Wert für `max_output_tokens`. |
| `failed` | Der Server konnte den Vorgang nicht abschließen oder die Interaktion hat länger als 24 Stunden gedauert. | Wiederholen Sie die Anfrage. Wenn der Fehler wieder auftritt, teilen Sie dem Support die `id` der Interaktion mit. |
| `cancelled` | Sie haben die Interaktion abgebrochen. | Lesen Sie `usage`, um die abgerechneten Tokens zu sehen. |

Wenn Sie eine laufende Interaktion beenden möchten, rufen Sie in Python `client.interactions.cancel(id=interaction.id)`, in JavaScript `client.interactions.cancel(interaction.id)` oder in REST `POST /v1beta/interactions/{id}/cancel` auf.

## `max_output_tokens` festlegen

`max_output_tokens` legt das kombinierte Limit für Überlegungen und Ausgaben für die gesamte Interaktion fest. Wenn Sie diesen Wert senken, überlegt das Modell nicht präziser, sondern die Antwort wird früher abgeschnitten.

| Ihre Arbeitslast | Empfohlener Wert für `max_output_tokens` |
| --- | --- |
| Vorhandene Apps mit einem Limit unter 32.000 | Auf 32.768 erhöhen. Die Ausführung im Hintergrund ist nicht erforderlich. |
| Lange Coding- und Agentenaufgaben | Beginnen Sie mit 65.536 (Standard). Die Ausführung im Hintergrund ist nicht erforderlich. |
| Komplexe Schlussfolgerungen, schwierige mathematische und wissenschaftliche Aufgaben sowie Beweise | Legen Sie `background: true` fest und beginnen Sie mit 262.144, bis zu 1.048.576 minus Ihre Eingabetokens. |

Wenn Sie weniger Tokens verwenden möchten, senken Sie `thinking_level`. Verwenden Sie `high` für die schwierigsten Aufgaben mit Schlussfolgerungen. Verwenden Sie `medium` (Standard) für die meisten Coding- und Agentenaufgaben.

## Tokens zählen

`interaction.usage` meldet die Summen für alle Schritte. Lesen Sie die folgenden Felder: `total_input_tokens`, `total_cached_tokens`, `total_output_tokens`, `total_thought_tokens` und `total_tokens`.

`total_input_tokens` summiert die Eingabetokens aller Schritte. Bei jedem Schritt werden Ihr Prompt und alle bisher generierten Inhalte als Eingabe an das Modell zurückgesendet. Die gleichen Tokens werden also in jedem späteren Schritt noch einmal gezählt. Ein Prompt mit 1.000 Tokens, der 200.000 Tokens für Überlegungen und Ausgaben erzeugt, erfordert beispielsweise vier Schritte:

| Schritt | An das Modell gesendete Eingabe | Eingabetokens |
| --- | --- | --- |
| 1 | Prompt | 1.000 |
| 2 | Prompt + Schritt 1 | 66.536 |
| 3 | Prompt + Schritte 1 und 2 | 132.072 |
| 4 | Prompt + Schritte 1 bis 3 | 197.608 |
| **Summe** |  | **397.216** |

`total_input_tokens` meldet etwa 397.000 Tokens (wobei wiederholte Eingaben für Schritte durch implizites Caching automatisch um 95% reduziert werden), obwohl die tatsächliche Kontextgröße nur etwa 201.000 Tokens beträgt: der Prompt mit 1.000 Tokens plus 200.000 Tokens für Überlegungen und Ausgaben.

Während eines Streams enthalten sowohl `step.stop`- als auch `interaction.status_update`-Ereignisse `usage` (kumulativ für die Interaktion). Lesen Sie den neuesten Wert für `usage`, anstatt die Werte zu addieren.

## Informationen zur Abrechnung

Sie zahlen für jedes Token in jedem Schritt, einschließlich der Schritte, die nur Überlegungen enthalten.

- **Cache-Rabatt**:Durch implizites Caching wird die wiederholte Eingabe in jedem Schritt um 95 % reduziert. Für zwischengespeicherte Eingaben fallen während des Einführungszeitraums 0,10 $ pro 1 Million Tokens an, statt 2,00 $.
- **Abgebrochene und fehlgeschlagene Interaktionen**:Sie zahlen für alle Arbeiten, die vor dem Ende der Interaktion abgeschlossen wurden.

## Fehlerbehebung

| Symptom | Ursache und Lösung |
| --- | --- |
| Ausgabe endet bei 64.000 | `background` ist `false` oder `max_output_tokens` ist nicht festgelegt. Legen Sie `background: true` und `max_output_tokens` größer als 65.536 fest. |
| 400: „max\_output\_tokens greater than 65536 is not yet supported with background=false.“ | Die lange Decodierung ohne Ausführung im Hintergrund ist noch nicht verfügbar. Legen Sie `background: true` fest. |
| 400: „store=true is required for background interactions“ | Für die Ausführung im Hintergrund ist `store: true` erforderlich. |
| Status `incomplete` mit leerem Text | Das Modell hat alle Tokens für Überlegungen verwendet. Erhöhen Sie `max_output_tokens` oder senken Sie `thinking_level`. |
| Die Kontextkomprimierung beginnt zu früh | Ihr Agenten-Framework oder Bewertungstool liest `total_input_tokens`. Weitere Informationen finden Sie unter [Tokens zählen](#count-tokens). |

## Beschränkungen

- **Keine lange Decodierung ohne Ausführung im Hintergrund**:Interaktionen mit `background: false` enden bei 65.536 Tokens. Unterstützung ist demnächst verfügbar.
- **Keine Längenziele**:Das Modell berücksichtigt keine Ziele für die Tokenlänge oder die Anzahl der Wörter.

## Nächste Schritte

- [Neuerungen in Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/latest-model?hl=de)
- [Ausführung im Hintergrund](https://ai.google.dev/gemini-api/docs/background-execution?hl=de)
- [Überlegungen](https://ai.google.dev/gemini-api/docs/thinking?hl=de)
- [Lange Decodierung mit der GenerateContent API](https://ai.google.dev/gemini-api/docs/generate-content/long-decode?hl=de)

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-10-13 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-10-13 (UTC)."],[],[]]
