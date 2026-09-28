---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he
fetched_at: 2026-09-28T06:16:51.821729+00:00
title: "\u05de\u05d3\u05e8\u05d9\u05da \u05dc\u05de\u05ea\u05d7\u05d9\u05dc\u05d9\u05dd \u05d1\u05e0\u05d5\u05e9\u05d0 \u05e0\u05d9\u05d4\u05d5\u05dc \u05e1\u05d5\u05db\u05e0\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# מדריך למתחילים בנושא ניהול סוכנים

במדריך הזה נסביר איך ליצור סוכנים מנוהלים ב-Gemini API ולהשתמש בהם באמצעות [סוכן Antigravity](https://ai.google.dev/gemini-api/docs/agents/antigravity-agent?hl=he). תבצעו את השיחה הראשונה עם סוכן, תמשיכו שיחה מרובת שלבים, תצפו בתשובה בזמן אמת, תורידו קבצים מהארגז חול ותעבדו עם הסוכן המנוהל Antigravity.

## הפעלת אינטראקציה ראשונה עם נציג

קריאה יחידה ל-[Interactions API](https://ai.google.dev/gemini-api/docs?hl=he) מספקת ארגז חול של Linux, מריצה את לולאת הסוכן ומחזירה את התוצאה. תגדירו שלושה פרמטרים:

- מעבירים את `agent` בתור `"antigravity-preview-09-2026"`, שהיא הגרסה הנוכחית של הסוכן המנוהל שלנו שמוגדר מראש ומתאים לשימוש כללי.
- מגדירים את `environment="remote"` כדי להקצות סביבת ארגז חול חדשה ורעננה.
- יוצרים קלט ומגדירים מה רוצים שהסוכן יעשה.

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Write a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt. Then read the file and print its contents."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    // Print the agent's final output
    fmt.Printf("Interaction ID: %s\n", *interaction.ID)
    fmt.Printf("Environment ID: %s\n", *interaction.EnvironmentID)
    fmt.Printf("Output: %s\n", *interaction.OutputText)
}
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

התגובה מחזירה אובייקט `Interaction`. אחסון של `interaction.id` ו-`interaction.environment_id` כדי להמשיך את השיחה באותו ארגז חול. משתמשים ב-`interaction.output_text` כדי לגשת לתשובה הסופית של הסוכן. ‫`interaction.steps` מפרט כל שלב שהסוכן ביצע (חשיבה רציונלית, קריאות לכלים, הרצת קוד).

## המשך השיחה (רב-שלבית)

ה-API עוקב אחרי שני ממדי מצב בלתי תלויים:

- **הקשר השיחה:** היסטוריית הצ'אט, מעקב אחר נימוקים, שימוש בכלי, שימוש ב-`previous_interaction_id`.
- [**מצב הסביבה:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he) קבצים, חבילות מותקנות ומצב ארגז החול, באמצעות `environment`.

כדי להמשיך, צריך להזין את שניהם במקום המתאים:

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    interactionID := "INTERACTION_ID"
    environmentID := "ENVIRONMENT_ID"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            PreviousInteractionID: genai.Ptr(interactionID),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(environmentID)),
            Input:                 interactions.NewInteractionsInput("Now plot the Fibonacci sequence as a line chart and save it as chart.png."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

קבצים מתור 1 (`fibonacci.txt`) נשארים בתור 2. הסוכן גם שומר את ההקשר של השיחה.

אפשר לשלב בין האפשרויות הבאות באופן עצמאי:

- **ניקוי השיחה, שמירת הקבצים:** לא כוללים את `previous_interaction_id`, מעבירים רק את מזהה הסביבה באמצעות `environment` כדי ליצור שיחה חדשה באותו מרחב.
- **שמירת השיחה, סביבת עבודה חדשה:** מעבירים את `previous_interaction_id`, מגדירים את `environment="remote"` לארגז חול חדש.

### דחיסה אוטומטית של ההקשר

בשיחות ארוכות ורב-שלביות, ההיסטוריה הגולמית של שלבי החשיבה הרציונלית, קריאות הכלים ותוכן הקבצים הגדולים יכולה לגדול במהירות ולתפוס נפח משמעותי של הקשר. כדי למנוע שגיאות שקשורות למגבלת הטוקנים ולשמור על המיקוד של הסוכן (ולמנוע 'הידרדרות ההקשר'), ב-API של ניהול סוכנים יש שלב דחיסה של ההקשר בסביבות 135,000 טוקנים. פעולה זו מתבצעת באופן אוטומטי.

## הצגת התשובה באופן שוטף

במשימות ארוכות, אפשר להזרים את התשובה כדי לראות את הסוכן פועל בזמן אמת:

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Read Hacker News, summarize the top 5 stories, and save the results as a PDF."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Stream:      genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        fmt.Printf("%+v\n", event)
        if stepStop := event.GetDataStepStop(); stepStop != nil && stepStop.Usage != nil {
            fmt.Printf("%+v\n", stepStop.Usage)
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
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

הסטרימינג מחזיר דלתאות של שלבים עם עדכונים מצטברים. כששלב מסתיים,
האירוע `step.stop` כולל נתונים סטטיסטיים מצטברים של השימוש. מידע נוסף מפורט [במדריך לסטרימינג](https://ai.google.dev/gemini-api/docs/streaming?hl=he).

## הורדת קבצים מהסביבה

כשהסוכן יוצר קבצים בארגז החול. אפשר להוריד אותם באמצעות Files API עם בקשת HTTP ישירה (עדיין אין שיטה ב-SDK):

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

### Go

```
package main

import (
    "context"
    "fmt"
    "io"
    "log"
    "net/http"
    "os"
)

func main() {
    ctx := context.Background()
    envID := "ENVIRONMENT_ID"
    apiKey := os.Getenv("GEMINI_API_KEY")

    url := fmt.Sprintf("https://generativelanguage.googleapis.com/v1beta/files/environment-%s:download?alt=media", envID)
    req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
    if err != nil {
        log.Fatal(err)
    }
    req.Header.Set("x-goog-api-key", apiKey)

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()

    data, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    if err := os.WriteFile("snapshot.tar", data, 0644); err != nil {
        log.Fatal(err)
    }
    fmt.Println("Saved snapshot to snapshot.tar")
}
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

## שמירת סוכן מנוהל

בשלבים הקודמים השתמשנו בסוכן Antigravity שמוגדר כברירת מחדל והתאמנו אותו ישירות. אחרי שמשפרים את ההגדרה (הוראות, יכולות, בחירת מודל וסביבה), אפשר לשמור אותה כסוכן מנוהל לשימוש חוזר. כך אפשר להפעיל אותו באמצעות מזהה בלי לחזור על ההגדרה.

כששומרים סוכן, אפשר לראות את הסימטריה הארכיטקטונית עם אינטראקציות מוטבעות: מציינים `base_agent: "antigravity-preview-09-2026"` ויכולים להעביר `agent_config` עם `model` שבחרתם בדיוק כמו ב-`interactions.create`. אתם גם מגדירים `base_environment` (ממקורות או על ידי יצירת עותק של סביבה קיימת). הסוכן ישתמש בסביבה הזו ובהגדרות המודל האלה בכל אינטראקציה חדשה.

**ממקורות:** הגדרת מקורות בשורה או ממקורות אחרים כמו GitHub או Cloud Storage.

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/agents"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always include a chart and a summary table in your reports."),
            },
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/your-org/skills"),
                Target: genai.Ptr(".agents/skills"),
            },
        },
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:        genai.Ptr("fibonacci-analyst"),
            BaseAgent: genai.Ptr("antigravity-preview-09-2026"),
            AgentConfig: genai.Ptr(agents.NewAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-3.8-flash"),
            })),
            SystemInstruction: genai.Ptr("You are a math analysis agent. Generate sequences, visualize them, and export results as PDF reports."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Saved agent: %s\n", *res.Agent.ID)
}
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

## הפעלת הסוכן המנוהל

אחרי ששומרים סוכן מנוהל, אפשר להפעיל אותו באמצעות המזהה שלו. כל הפעלה יוצרת עותק של סביבת הבסיס, כך שכל הרצה מתחילה בצורה נקייה:

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

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("fibonacci-analyst"),
            Input:       interactions.NewInteractionsInput("Generate the first 50 prime numbers, plot their distribution, and save a PDF report."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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

## המאמרים הבאים

- [סוכן Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he): יכולות, כלים נתמכים, קלט מולטימודאלי, תמחור ומגבלות.
- [יצירת סוכנים מנוהלים](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he): הרחבת Antigravity באמצעות הוראות, מיומנויות ונתונים משלכם.
- [סביבות](https://ai.google.dev/gemini-api/docs/agent-environment?hl=he): מקורות, רשת, מחזור חיים, מגבלות משאבים.
- ‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he): ממשק ה-API הבסיסי למודלים ולאגנטים.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-09-25 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-09-25 (שעון UTC)."],[],[]]
