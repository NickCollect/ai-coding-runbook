---
source_url: https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th
fetched_at: 2026-11-02T07:15:44.525949+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e34\u0e48\u0e21\u0e15\u0e49\u0e19\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e2d\u0e22\u0e48\u0e32\u0e07\u0e23\u0e27\u0e14\u0e40\u0e23\u0e47\u0e27 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon พร้อมให้บริการแล้ว [ลองใช้เลย](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเริ่มต้นใช้งาน Agent ที่มีการจัดการอย่างรวดเร็ว

คู่มือนี้จะแนะนำวิธีสร้างและใช้ Agent ที่ได้รับการจัดการ ใน Gemini
API โดยใช้ [Agent ของ Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th) คุณจะ โทรหาเอเจนต์เป็นครั้งแรก สนทนาแบบการสนทนาไปมา สตรีม คำตอบ ดาวน์โหลดไฟล์จากแซนด์บ็อกซ์ และทำงานกับเอเจนต์ที่มีการจัดการของ Antigravity

## เรียกใช้การโต้ตอบกับ Agent ครั้งแรก

การเรียกใช้ [Interactions API](https://ai.google.dev/gemini-api/docs?hl=th) เพียงครั้งเดียวจะจัดสรรแซนด์บ็อกซ์ Linux เรียกใช้ลูปของเอเจนต์ และแสดงผลลัพธ์ คุณจะกำหนดพารามิเตอร์ 3 รายการ ได้แก่

- ส่ง `agent` เป็น `"antigravity-preview-09-2026"` ซึ่งเป็นเวอร์ชันปัจจุบันของเอเจนต์ที่มีการจัดการแบบกำหนดไว้ล่วงหน้าและแบบอเนกประสงค์
- กำหนด `environment="remote"` เพื่อจัดสรรสภาพแวดล้อมแซนด์บ็อกซ์ใหม่ที่สะอาด
- สร้างอินพุตโดยกำหนดสิ่งที่คุณต้องการให้ Agent ทำ

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

การตอบกลับจะแสดงผลออบเจ็กต์ `Interaction` จัดเก็บ `interaction.id` และ `interaction.environment_id` เพื่อสนทนาต่อในแซนด์บ็อกซ์เดียวกัน ใช้ `interaction.output_text` เพื่อเข้าถึงคำตอบสุดท้ายของเอเจนต์ `interaction.steps` แสดงรายการแต่ละขั้นตอนที่เอเจนต์ดำเนินการ (การให้เหตุผล การเรียกใช้เครื่องมือ การเรียกใช้โค้ด)

## สนทนาต่อ (การสนทนาไปมา)

API จะติดตามมิติข้อมูลสถานะ 2 รายการที่แยกกัน ดังนี้

- **บริบทการสนทนา:** ประวัติการแชท ร่องรอยการให้เหตุผล การใช้เครื่องมือ การใช้ `previous_interaction_id`
- [**สถานะสภาพแวดล้อม:**](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th) ไฟล์ แพ็กเกจที่ติดตั้ง และสถานะแซนด์บ็อกซ์โดยใช้ `environment`

ส่งทั้ง 2 อย่างในตำแหน่งที่เกี่ยวข้องเพื่อดำเนินการต่อ

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

ไฟล์จากเทิร์นที่ 1 (`fibonacci.txt`) จะยังคงอยู่ในเทิร์นที่ 2 นอกจากนี้ Agent ยังคงบริบทการสนทนาไว้ด้วย

คุณสามารถผสมและจับคู่สิ่งต่อไปนี้ได้อย่างอิสระ

- **ล้างการสนทนา เก็บไฟล์:** ละเว้น `previous_interaction_id` ส่งเฉพาะรหัสสภาพแวดล้อมโดยใช้ `environment` เพื่อการสนทนาใหม่ในพื้นที่ทำงานเดียวกัน
- **เก็บการสนทนา พื้นที่ทำงานใหม่:** ส่ง `previous_interaction_id` ตั้งค่า `environment="remote"` สำหรับแซนด์บ็อกซ์ใหม่

### การย่อบริบทอัตโนมัติ

ในการสนทนาแบบหลายรอบที่ใช้เวลานาน ประวัติแบบดิบของขั้นตอนการให้เหตุผล การเรียกใช้เครื่องมือ และเนื้อหาไฟล์ขนาดใหญ่อาจเพิ่มขึ้นอย่างรวดเร็วและใช้พื้นที่บริบทจำนวนมาก เพื่อป้องกันข้อผิดพลาดเกี่ยวกับขีดจำกัดของโทเค็นและรักษาโฟกัสของเอเจนต์ (ป้องกัน "บริบทที่ล้าสมัย") Managed Agents API มีขั้นตอนการบีบอัดบริบทดั้งเดิมที่ประมาณ 135,000 โทเค็น ซึ่งจะเป็นการทำงานโดยอัตโนมัติ

## สตรีมคำตอบ

สำหรับงานที่ใช้เวลานาน คุณสามารถสตรีมคำตอบเพื่อดูการทำงานของ Agent แบบเรียลไทม์ได้โดยทำดังนี้

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

การสตรีมจะแสดงเดลต้าของขั้นตอนการคืนสินค้าพร้อมการอัปเดตที่เพิ่มขึ้น เมื่อขั้นตอนเสร็จสมบูรณ์ เหตุการณ์ `step.stop` จะมีสถิติการใช้งานสะสม ดูข้อมูลเพิ่มเติมได้ใน[คู่มือการสตรีม](https://ai.google.dev/gemini-api/docs/streaming?hl=th)

## ดาวน์โหลดไฟล์จากสภาพแวดล้อม

เมื่อเอเจนต์สร้างไฟล์ภายในแซนด์บ็อกซ์ ดาวน์โหลดโดยใช้ Files API ด้วยคำขอ HTTP โดยตรง (ยังไม่มีเมธอด SDK)

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

## บันทึก Agent ที่มีการจัดการ

ในขั้นตอนก่อนหน้า เราใช้ Agent ของ Antigravity เริ่มต้นและปรับแต่งในบรรทัด เมื่อปรับปรุงการกำหนดค่า (คำสั่ง ทักษะ การเลือกโมเดล และสภาพแวดล้อม) แล้ว คุณจะบันทึกการกำหนดค่าเป็นเอเจนต์ที่มีการจัดการที่นำกลับมาใช้ใหม่ได้ ซึ่งจะช่วยให้คุณเรียกใช้ได้ด้วยรหัสโดยไม่ต้องกำหนดค่าซ้ำ

เมื่อบันทึกเอเจนต์ ให้สังเกตความสมมาตรของสถาปัตยกรรมกับการโต้ตอบในบรรทัด: คุณระบุ `base_agent: "antigravity-preview-09-2026"` และส่ง `agent_config` พร้อม `model` ที่เลือกได้เช่นเดียวกับใน `interactions.create` นอกจากนี้ คุณยังกำหนด `base_environment` (จากแหล่งที่มาหรือโดยการแยกสภาพแวดล้อมที่มีอยู่) ได้ด้วย Agent จะใช้การกำหนดค่าสภาพแวดล้อมและโมเดลนี้สำหรับการโต้ตอบใหม่ทุกครั้ง

**จากแหล่งที่มา:** กำหนดแหล่งที่มาในบรรทัด หรือจากแหล่งที่มาอื่นๆ เช่น GitHub หรือ Cloud Storage

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

## เรียกใช้ Agent ที่มีการจัดการ

เมื่อบันทึกเอเจนต์ที่มีการจัดการแล้ว คุณจะเรียกใช้เอเจนต์ดังกล่าวได้โดยใช้รหัส การเรียกใช้แต่ละครั้งจะแยกสภาพแวดล้อมฐานออกเป็น 2 ส่วน ดังนั้นการเรียกใช้ทุกครั้งจึงเริ่มต้นอย่างสะอาด

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

## ขั้นตอนถัดไป

- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): ความสามารถ เครื่องมือที่รองรับ อินพุตแบบหลายรูปแบบ ราคา และข้อจำกัด
- [การสร้าง Agent ที่ได้รับการจัดการ](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th): ขยาย Antigravity ด้วยวิธีการ ทักษะ และข้อมูลของคุณเอง
- [สภาพแวดล้อม](https://ai.google.dev/gemini-api/docs/agent-environment?hl=th): แหล่งข้อมูล เครือข่าย วงจรการใช้งาน ขีดจำกัดของทรัพยากร
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th): API พื้นฐานสำหรับโมเดลและเอเจนต์

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-10-01 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-10-01 UTC"],[],[]]
