---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=de
fetched_at: 2026-09-21T05:48:58.478253+00:00
title: "Kurzanleitung f\u00fcr verwaltete Agents \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ist jetzt verfügbar. [Jetzt ausprobieren](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=de).

![](https://ai.google.dev/_static/images/translated.svg?hl=de)

Google verwendet KI-Technologie, um Inhalte in Ihre bevorzugte Sprache zu übersetzen. KI-Übersetzungen können Fehler enthalten.

- [Startseite](https://ai.google.dev/?hl=de)
- [Gemini API](https://ai.google.dev/gemini-api?hl=de)
- [Dokumentation](https://ai.google.dev/gemini-api/docs?hl=de)

Feedback geben

# Kurzanleitung für verwaltete Agents

In diesem Leitfaden wird beschrieben, wie Sie verwaltete KI-Agenten in der Gemini API erstellen und verwenden. Dazu wird der [Antigravity-Agent](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=de) verwendet. Sie führen Ihren ersten Agent-Aufruf aus, setzen eine Unterhaltung mit mehreren Schritten fort, streamen die Antwort, laden Dateien aus der Sandbox herunter und arbeiten mit dem verwalteten Antigravity-Agent.

## Erste Interaktion mit einem KI-Agenten ausführen

Bei einem einzelnen Aufruf der [Interactions API](https://ai.google.dev/gemini-api/docs?hl=de) wird eine Linux-Sandbox bereitgestellt, die Agentenschleife ausgeführt und das Ergebnis zurückgegeben. Sie definieren drei Parameter:

- Übergeben Sie `agent` als `"antigravity-preview-09-2026",`. Das ist die aktuelle Version unseres vordefinierten und universellen verwalteten Agents.
- Definieren Sie `environment="remote"`, um eine neue, frische Sandbox-Umgebung bereitzustellen.
- Erstellen Sie eine Eingabe, in der Sie definieren, was der KI-Agent tun soll.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment="remote",
)

# Print the agent's final output
print(f"Interaction ID: {interaction.id}")
print(f"Environment ID: {interaction.environment_id}")
print(f"Output: {interaction.output_text}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents.",
    environment: "remote",
});

console.log(`Interaction ID: ${interaction.id}`);
console.log(`Environment ID: ${interaction.environment_id}`);

console.log(`Output: ${interaction.output_text}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Print the agent's final output
System.out.println("Interaction ID: " + interaction.id().orElse(""));
System.out.println("Environment ID: " + interaction.environmentId().orElse(""));
System.out.println("Output: " + interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."}],
    "environment": {"type": "remote"}
}'
```

Die Antwort gibt ein `Interaction`-Objekt zurück. Speichern Sie `interaction.id` und `interaction.environment_id`, um die Unterhaltung in derselben Sandbox fortzusetzen. Verwenden Sie `interaction.output_text`, um auf die endgültige Antwort des Agenten zuzugreifen. `interaction.steps` listet jeden Schritt auf, den der Agent ausgeführt hat (Begründung, Tool-Aufrufe, Code-Ausführung).

## Unterhaltung fortsetzen (Mehrfachdialog)

Die API erfasst zwei unabhängige Zustandsdimensionen:

- **Kontext der Unterhaltung**:Chatverlauf, Begründungsablauf, Tool-Nutzung, Verwendung von `previous_interaction_id`.
- [**Umgebungsstatus**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de):Dateien, installierte Pakete und Sandbox-Status mit `environment`.

Geben Sie beide an der entsprechenden Stelle ein, um fortzufahren:

### Python

```
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    input="Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
)

print(interaction_2.output_text)
```

### JavaScript

```
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    input: "Now plot the Fibonacci sequence as a line chart and save it as chart.png.",
}, { timeout: 300_000 });

console.log(interaction2.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
String interactionId = "INTERACTION_ID";
String environmentId = "ENVIRONMENT_ID";

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .previousInteractionId(interactionId)
    .environment(CreateAgentInteractionEnvironment.of(environmentId))
    .input(InteractionsInput.of("Now plot the Fibonacci sequence as a line chart and save it as chart.png."))
    .build();

Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction2.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "previous_interaction_id": "interaction_id_from_step_1",
    "environment": "environment_id_from_step_1",
    "input": [{"type": "text", "text": "Now plot the Fibonacci sequence as a line chart and save it as chart.png."}]
}'
```

Dateien aus Runde 1 (`fibonacci.txt`) sind auch in Runde 2 verfügbar. Der KI-Agent behält auch den Kontext der Unterhaltung bei.

Sie können diese unabhängig voneinander kombinieren:

- **Unterhaltung löschen, Dateien behalten**:Lassen Sie `previous_interaction_id` weg und übergeben Sie nur die Umgebungs-ID mit `environment`, um eine neue Unterhaltung im selben Arbeitsbereich zu starten.
- **Unterhaltung beibehalten, neuer Arbeitsbereich**:Übergeben Sie `previous_interaction_id` und legen Sie `environment="remote"` für eine neue Sandbox fest.

### Automatische Kontextverdichtung

Bei langen Mehrfachdialogen kann der Rohverlauf von Begründungsschritten, Tool-Aufrufen und großen Dateiinhalten schnell anwachsen und viel Kontextspeicherplatz belegen. Um Fehler aufgrund von Tokenlimits zu vermeiden und den Fokus des Agents aufrechtzuerhalten (um „Context Rot“ zu verhindern), enthält die Managed Agents API einen nativen Schritt zur Kontextkomprimierung bei etwa 135.000 Tokens. Dies geschieht automatisch.

## Antwort streamen

Bei zeitaufwendigen Aufgaben können Sie die Antwort streamen, um zu sehen, wie der KI-Agent in Echtzeit arbeitet:

### Python

```
from google import genai

client = genai.Client()

stream = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment="remote",
    stream=True,
)

for event in stream:
    print(event)
    if event.event_type == "step.stop" and event.usage:
        print(event.usage)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    environment: "remote",
    stream: true,
});

for await (const event of stream) {
    console.log(event);
    if (event.event_type === "step.stop" && event.usage) {
        console.log(event.usage);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.StepStop;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Read Hacker News, summarize the top 5 stories, and save the results as a PDF."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .stream(true)
    .build();

try (EventStream<InteractionSSEStreamEvent> stream =
    client.interactions.create(CreateInteractionRequestBody.of(params)).events()) {
  for (InteractionSSEStreamEvent event : stream) {
    System.out.println(event);
    if (event.data().isPresent() && event.data().get() instanceof StepStop stepStop) {
      stepStop.usage().ifPresent(System.out::println);
    }
  }
}
```

### REST

```
curl -N -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Read Hacker News, summarize the top 5 stories, and save the results as a PDF.",
    "environment": "remote",
    "stream": true
}'
```

Beim Streaming werden Schrittdeltas mit inkrementellen Updates zurückgegeben. Wenn ein Schritt abgeschlossen ist, enthält das `step.stop`-Ereignis die zusammengefassten Nutzungsstatistiken. Weitere Informationen finden Sie im [Streaming-Leitfaden](https://ai.google.dev/gemini-api/docs/streaming?hl=de).

## Dateien aus der Umgebung herunterladen

Wenn der Agent Dateien in der Sandbox erstellt. Laden Sie sie mit der Files API über eine direkte HTTP-Anfrage herunter (noch keine SDK-Methode):

### Python

```
import os
import requests
import tarfile

env_id = interaction.environment_id
api_key = os.environ["GEMINI_API_KEY"]

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot.tar", "wb") as f:
    f.write(response.content)

with tarfile.open("snapshot.tar") as tar:
    tar.extractall(path="extracted_snapshot")
```

### JavaScript

```
import fs from "fs";
import { execSync } from "child_process";

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot.tar", buffer);

if (!fs.existsSync("extracted_snapshot")) {
    fs.mkdirSync("extracted_snapshot");
}
execSync("tar -xf snapshot.tar -C extracted_snapshot");

console.log(fs.readdirSync("extracted_snapshot"));
```

### Java

```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.file.Files;
import java.nio.file.Paths;

String envId = "ENVIRONMENT_ID";
String apiKey = System.getenv("GEMINI_API_KEY");

HttpClient httpClient = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://generativelanguage.googleapis.com/v1beta/files/environment-" + envId + ":download?alt=media"))
    .header("x-goog-api-key", apiKey)
    .GET()
    .build();

HttpResponse<byte[]> response = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray());
Files.write(Paths.get("snapshot.tar"), response.body());
System.out.println("Saved snapshot to snapshot.tar");
```

### REST

```
ENV_ID="your_environment_id_here"

curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-o snapshot.tar

mkdir -p extracted_snapshot
tar -xf snapshot.tar -C extracted_snapshot
```

## Verwalteten Agent speichern

In den vorherigen Schritten haben wir den Standard-Antigravity-Agent verwendet und ihn inline angepasst. Wenn Sie Ihre Konfiguration (Anweisungen, Skills, Modellauswahl und Umgebung) optimiert haben, können Sie sie als wiederverwendbaren verwalteten Agent speichern. So können Sie sie anhand der ID aufrufen, ohne die Konfiguration zu wiederholen.

Wenn Sie einen Agent speichern, sehen Sie die architektonische Symmetrie mit Inline-Interaktionen: Sie geben `base_agent: "antigravity-preview-09-2026"` an und können ein `agent_config` mit dem von Ihnen ausgewählten `model` übergeben, genau wie bei `interactions.create`. Sie definieren auch eine `base_environment` (entweder aus Quellen oder durch Forking einer vorhandenen Umgebung). Der Agent verwendet diese Umgebung und Modellkonfiguration für jede neue Interaktion.

**Aus Quellen**:Definieren Sie Quellen inline oder aus anderen Quellen wie GitHub oder Cloud Storage.

### Python

```
agent = client.agents.create(
    id="fibonacci-analyst",
    base_agent="antigravity-preview-09-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.8-flash",
    },
    system_instruction="You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports.",
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ],
    },
)

print(f"Saved agent: {agent.id}")
```

### JavaScript

```
const agent = await client.agents.create({
    id: "fibonacci-analyst",
    base_agent: "antigravity-preview-09-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.8-flash",
    },
    system_instruction: "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always include a chart and a summary table in your reports.",
            },
            {
                type: "repository",
                source: "https://github.com/your-org/skills",
                target: ".agents/skills"
            }
        ],
    },
});

console.log(`Saved agent: ${agent.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.AgentConfig;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always include a chart and a summary table in your reports.")
            .build(),
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/your-org/skills")
            .target(".agents/skills")
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("fibonacci-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .agentConfig(AgentConfig.of(
        AntigravityAgentConfig.builder()
            .model("gemini-3.8-flash")
            .build()
    ))
    .systemInstruction("You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Saved agent: " + agent.id().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "fibonacci-analyst",
    "base_agent": "antigravity-preview-09-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.8-flash"
    },
    "system_instruction": "You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always include a chart and a summary table in your reports."
            },
            {
                "type": "repository",
                "source": "https://github.com/your-org/skills",
                "target": ".agents/skills"
            }
        ]
    }
}'
```

## Verwalteten Agent aufrufen

Nachdem Sie einen verwalteten Agent gespeichert haben, können Sie ihn über die ID aufrufen. Bei jedem Aufruf wird die Basisumgebung verzweigt, sodass jeder Lauf sauber beginnt:

### Python

```
result = client.interactions.create(
    agent="fibonacci-analyst",
    input="Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "fibonacci-analyst",
    input: "Generate the first 50 prime numbers, plot their distribution, and save a PDF report.",
    environment: "remote",
}, {
    timeout: 300_000,
});

console.log(result.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("fibonacci-analyst"))
    .input(InteractionsInput.of("Generate the first 50 prime numbers, plot their distribution, and save a PDF report."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "fibonacci-analyst",
    "environment": "remote",
    "input": "Generate the first 50 prime numbers, plot their distribution, and save a PDF report."
}'
```

## Nächste Schritte

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=de): Funktionen, unterstützte Tools, multimodale Eingabe, Preise und Einschränkungen.
- [Verwaltete KI-Agenten erstellen](https://ai.google.dev/gemini-api/docs/custom-agents?hl=de): Erweitern Sie Antigravity mit Ihren eigenen Anweisungen, Skills und Daten.
- [Umgebungen](https://ai.google.dev/gemini-api/docs/agent-environment?hl=de): Quellen, Netzwerk, Lebenszyklus, Ressourcenlimits.
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=de): Die zugrunde liegende API für Modelle und Agents.

Feedback geben

Sofern nicht anders angegeben, sind die Inhalte dieser Seite unter der [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) und Codebeispiele unter der [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) lizenziert. Weitere Informationen finden Sie in den [Websiterichtlinien von Google Developers](https://developers.google.com/site-policies?hl=de). Java ist eine eingetragene Marke von Oracle und/oder seinen Partnern.

Zuletzt aktualisiert: 2026-09-18 (UTC).

Haben Sie Feedback für uns?

[[["Leicht verständlich","easyToUnderstand","thumb-up"],["Mein Problem wurde gelöst","solvedMyProblem","thumb-up"],["Sonstiges","otherUp","thumb-up"]],[["Benötigte Informationen nicht gefunden","missingTheInformationINeed","thumb-down"],["Zu umständlich/zu viele Schritte","tooComplicatedTooManySteps","thumb-down"],["Nicht mehr aktuell","outOfDate","thumb-down"],["Problem mit der Übersetzung","translationIssue","thumb-down"],["Problem mit Beispielen/Code","samplesCodeIssue","thumb-down"],["Sonstiges","otherDown","thumb-down"]],["Zuletzt aktualisiert: 2026-09-18 (UTC)."],[],[]]
