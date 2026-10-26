---
source_url: https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja
fetched_at: 2026-10-26T05:52:47.322184+00:00
title: "Antigravity \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon が今すぐチェックできるようになりました。[試してみる](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=ja)

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google は AI 技術を使用して、コンテンツをご希望の言語に翻訳しています。AI 翻訳には誤りが含まれる場合があります。

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# Antigravity エージェント

Antigravity エージェントは、Gemini API の汎用マネージド エージェントです。1 回の API 呼び出しで、Google がホストする独自の安全な Linux サンドボックス内で推論、コードの実行、ファイルの管理、ウェブの閲覧を行うエージェントを取得できます。

Gemini 3.8 Flash で構築されており、Antigravity IDE と同じハーネスを使用しています。基盤となる Gemini モデルは `agent_config` を使用して構成できます。[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) と [Google AI Studio](https://aistudio.google.com?hl=ja) で利用できます。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment="remote",
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    environment: "remote",
}, { timeout: 300000 });

console.log(interaction.output_text);
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
    .input(InteractionsInput.of("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
            Input:       interactions.NewInteractionsInput("Read Hacker News, summarize the top 10 stories, and save the results as a PDF."),
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
    "agent": "antigravity-preview-09-2026",
    "input": "Read Hacker News, summarize the top 10 stories, and save the results as a PDF.",
    "environment": "remote"
}'
```

## 機能

各呼び出しは Linux サンドボックスをプロビジョニングし、ツール使用ループを開始できます。エージェントは、計画、実行、結果の観察を行い、タスクが完了するまで繰り返します。

- **コード実行:** Bash、Python、Node.js のコマンドを実行します。パッケージのインストール、テストの実行、アプリのビルド。
- **ファイル管理:** サンドボックス内のファイルの読み取り、書き込み、編集、検索、一覧表示を行います。ファイルはインタラクション間で保持されます。
- **ウェブアクセス:** Google 検索とデータ用の URL の取得。
- **コンテキストの圧縮:** 自動コンテキスト圧縮（約 135, 000 トークンでトリガー）により、コンテキストを失うことなく、トークン上限に達することなく、長時間実行されるマルチターン セッションをサポートします。

マルチターンの使用方法とストリーミングについては、[クイックスタート](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja)をご覧ください。

## サポートされているツール

デフォルトでは、エージェントは `code_execution`、`google_search`、`url_context` にアクセスできます。`environment` パラメータを指定すると、ファイルシステム ツールが自動的に有効になります。**カスタム関数**を定義して、エージェントを独自の API やツールに接続することもできます。`tools` パラメータを指定する必要があるのは、デフォルト セットをカスタマイズまたは制限する場合、またはカスタム関数を追加する場合のみです。

| ツール | Type 値 | 説明 |
| --- | --- | --- |
| コード実行 | `code_execution` | stdout/stderr キャプチャを使用してシェル コマンド（bash、Python、Node）を実行します。 |
| Google 検索 | `google_search` | 公開ウェブを検索する。 |
| URL コンテキスト | `url_context` | ウェブページを取得して読み取ります。 |
| ファイルシステム | *（`environment` で有効）* | サンドボックス内のファイルの読み取り、書き込み、編集、検索、一覧表示。`environment` を設定すると、これらのツールが自動的に有効になります。 |
| カスタム関数 | `function` | エージェントが実行をリクエストできるカスタム関数を定義します。[関数呼び出し](#function-calling)をご覧ください。 |
| リモート MCP サーバー | `mcp_server` | 外部の Model Context Protocol（MCP）サーバーをツールとして登録します。[MCP サーバー](#mcp-servers)をご覧ください。 |

同期[フック](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=ja)を使用して、リモート サンドボックス内で `code_execution` ツールと `filesystem` ツールの実行をインターセプトして検証できます。

エージェントを特定のツールに制限するには、必要なツールのみを渡します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Search for the latest AI research papers on reasoning and summarize them.",
    environment="remote",
    tools=[
        {"type": "google_search"},
        {"type": "url_context"},
    ],
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Search for the latest AI research papers on reasoning and summarize them.",
    environment: "remote",
    tools: [
        { type: "google_search" },
        { type: "url_context" },
    ],
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.URLContext;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Search for the latest AI research papers on reasoning and summarize them."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        GoogleSearch.builder().build(),
        URLContext.builder().build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
            Input:       interactions.NewInteractionsInput("Search for the latest AI research papers on reasoning and summarize them."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
                interactions.NewTool(interactions.URLContext{}),
            },
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
    "input": "Search for the latest AI research papers on reasoning and summarize them.",
    "environment": "remote",
    "tools": [
        {"type": "google_search"},
        {"type": "url_context"}
    ]
}'
```

## マルチモーダル入力

Antigravity エージェントは、マルチモーダル入力をサポートしています。現時点では、`text` と `image` の入力のみがサポートされています。画像はインラインの Base64 エンコード文字列（`data`）として指定する必要があります。

### Python

```
import base64
from google import genai

client = genai.Client()

with open("path/to/chart.png", "rb") as f:
    image_bytes = f.read()

interaction_inline = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input=[
        {"type": "text", "text": "Analyze this chart and summarize the trends."},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
    environment="remote",
)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import * as fs from "node:fs";

const client = new GoogleGenAI({});
const base64Image = fs.readFileSync("path/to/chart.png", { encoding: "base64" });

const interactionInline = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: [
        { type: "text", text: "Analyze this chart and summarize the trends." },
        {
            type: "image",
            data: base64Image,
            mime_type: "image/png",
        },
    ],
    environment: "remote",
}, { timeout: 300000 });
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] imageBytes = Files.readAllBytes(Paths.get("path/to/chart.png"));
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.ofContent(List.of(
        TextContent.builder().text("Analyze this chart and summarize the trends.").build(),
        ImageContent.builder()
            .data(base64Image)
            .mimeType(ImageContentMimeType.IMAGE_PNG)
            .build()
    )))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interactionInline = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interactionInline.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

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

    imageBytes, err := os.ReadFile("path/to/chart.png")
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Analyze this chart and summarize the trends.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeTypeImagePng.ToPointer(),
                }),
            }),
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
BASE64_IMAGE=$(base64 -w0 /path/to/chart.png)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
    \"input\": [
        {\"type\": \"text\", \"text\": \"Analyze this chart and summarize the trends.\"},
        {
            \"type\": \"image\",
            \"mime_type\": \"image/png\",
            \"data\": \"$BASE64_IMAGE\"
        }
    ],
    \"environment\": \"remote\"
}"
```

## 関数呼び出し

関数呼び出しを使用すると、エージェントが呼び出すことができるカスタムツールを定義して、Antigravity エージェントを外部 API やデータベースに接続できます。一般的なコンセプトについては、[Gemini API を使用した関数呼び出し](https://ai.google.dev/gemini-api/docs/function-calling?hl=ja)をご覧ください。

次の例は、2 ターンのインタラクションを示しています。エージェントが最初にカスタム `get_weather` 関数呼び出しをリクエストし、クライアントがそれを実行して、2 番目のターンで結果を返します。

### Python

```
from google import genai

client = genai.Client()

# 1. Define the custom function
get_weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g. San Francisco, USA",
            }
        },
        "required": ["location"],
    },
}

# 2. Call the agent with the custom tool (Turn 1)
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[
        {"type": "code_execution"},  # Enable default code execution
        get_weather_tool,            # Add custom function
    ],
)

# Check if the agent requested a function call
if interaction.status == "requires_action":
    # Find function calls that do not have a matching function result.
    # Filesystem tools (like write_to_file) are also represented as function calls
    # but are executed automatically by the environment.
    executed_calls = {step.call_id for step in interaction.steps if step.type == "function_result"}
    pending_calls = [step for step in interaction.steps if step.type == "function_call" and step.id not in executed_calls]

    if pending_calls:
        fc_step = pending_calls[0]
        print(f"Function to call: {fc_step.name} (ID: {fc_step.id})")
        print(f"Arguments: {fc_step.arguments}")

        # 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        function_result = {
            "temperature": 23,
            "unit": "celsius"
        }

        final_interaction = client.interactions.create(
            agent="antigravity-preview-09-2026",
            previous_interaction_id=interaction.id,  # Reference the interaction ID
            environment=interaction.environment_id,
            input=[
                {
                    "type": "function_result",
                    "name": fc_step.name,
                    "call_id": fc_step.id,
                    "result": function_result,
                }
            ],
        )

        print(final_interaction.output_text)
        # Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    else:
        print("No pending function calls.")
else:
    print(f"Interaction completed with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// 1. Call the agent with the custom tool (Turn 1)
const interaction = await client.interactions.create({
  agent: "antigravity-preview-09-2026",
  input: "What is the weather in Tokyo?",
  environment: "remote",
  tools: [
    { type: "code_execution" },
    {
      type: "function",
      name: "get_weather",
      description: "Gets the current weather for a given location.",
      parameters: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and country, e.g. San Francisco, USA",
          },
        },
        required: ["location"],
      },
    },
  ],
}, { timeout: 300000 });

if (interaction.status === "requires_action") {
  // Find function calls that do not have a matching function result.
  // Filesystem tools (like write_to_file) are also represented as function calls
  // but are executed automatically by the environment.
  const executedCalls = new Set(
    (interaction.steps || [])
      .filter(s => s.type === "function_result")
      .map(s => s.call_id)
  );
  const pendingCalls = (interaction.steps || []).filter(
    s => s.type === "function_call" && !executedCalls.has(s.id)
  );

  if (pendingCalls.length > 0) {
    const fcStep = pendingCalls[0];
    if (fcStep.type === "function_call") {
      console.log(`Function to call: ${fcStep.name} (ID: ${fcStep.id})`);

      // Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
      const functionResult = {
        temperature: 23,
        unit: "celsius"
      };

      const finalInteraction = await client.interactions.create({
        agent: "antigravity-preview-09-2026",
        previous_interaction_id: interaction.id, // Reference the interaction ID
        environment: interaction.environment_id,
        input: [
          {
            type: "function_result",
            name: fcStep.name,
            call_id: fcStep.id,
            result: functionResult,
          }
        ],
      }, { timeout: 300000 });

      console.log(finalInteraction.output_text);
    }
  } else {
    console.log("No pending function calls.");
  }
} else {
  console.log(`Interaction completed with status: ${interaction.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.FunctionCallStep;
import com.google.genai.gaos.models.interactions.FunctionResultStep;
import com.google.genai.gaos.models.interactions.FunctionResultStepResultUnion;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

Client client = new Client();

// 1. Define the custom function
Function getWeatherTool = Function.builder()
    .name("get_weather")
    .description("Gets the current weather for a given location.")
    .parameters(Map.of(
        "type", "object",
        "properties", Map.of(
            "location", Map.of(
                "type", "string",
                "description", "The city and country, e.g. San Francisco, USA"
            )
        ),
        "required", List.of("location")
    ))
    .build();

// 2. Call the agent with the custom tool (Turn 1)
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        CodeExecution.builder().build(), // Enable default code execution
        getWeatherTool                   // Add custom function
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Check if the agent requested a function call
if (interaction.status().orElse(null) == InteractionStatus.REQUIRES_ACTION) {
    // Find function calls that do not have a matching function result.
    List<Step> steps = interaction.steps().orElse(List.of());
    Set<String> executedCalls = steps.stream()
        .filter(step -> step instanceof FunctionResultStep)
        .map(step -> ((FunctionResultStep) step).callId().orElse(""))
        .collect(Collectors.toSet());

    List<FunctionCallStep> pendingCalls = steps.stream()
        .filter(step -> step instanceof FunctionCallStep)
        .map(step -> (FunctionCallStep) step)
        .filter(fc -> !executedCalls.contains(fc.id().orElse("")))
        .collect(Collectors.toList());

    if (!pendingCalls.isEmpty()) {
        FunctionCallStep fcStep = pendingCalls.get(0);
        System.out.println("Function to call: " + fcStep.name().orElse("") + " (ID: " + fcStep.id().orElse("") + ")");
        System.out.println("Arguments: " + fcStep.arguments().orElse(Map.of()));

        // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
        FunctionResultStep resultStep = FunctionResultStep.builder()
            .name(fcStep.name().orElse(""))
            .callId(fcStep.id().orElse(""))
            .result(FunctionResultStepResultUnion.of("{\"temperature\": 23, \"unit\": \"celsius\"}"))
            .build();

        CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
            .agent(AgentOption.of("antigravity-preview-09-2026"))
            .previousInteractionId(interaction.id().orElse(""))
            .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
            .input(InteractionsInput.ofStep(List.of(resultStep)))
            .build();

        Interaction finalInteraction = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();
        System.out.println(finalInteraction.outputText().orElse(""));
        // Output: The current weather in Tokyo, Japan is 23°C (Celsius).
    } else {
        System.out.println("No pending function calls.");
    }
} else {
    System.out.println("Interaction completed with status: " + interaction.status().orElse(null));
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

    // 1. Define the custom function
    getWeatherTool := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_weather"),
        Description: genai.Ptr("Gets the current weather for a given location."),
        Parameters: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "location": map[string]any{
                    "type":        "string",
                    "description": "The city and country, e.g. San Francisco, USA",
                },
            },
            "required": []string{"location"},
        },
    })

    // 2. Call the agent with the custom tool (Turn 1)
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}), // Enable default code execution
                getWeatherTool, // Add custom function
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction

    // Check if the agent requested a function call
    if interaction.Status == interactions.InteractionStatusRequiresAction {
        executedCalls := make(map[string]bool)
        for _, step := range interaction.Steps {
            if fr := step.FunctionResultStep; fr != nil {
                executedCalls[fr.CallID] = true
            }
        }

        var pendingCalls []*interactions.FunctionCallStep
        for _, step := range interaction.Steps {
            if fc := step.FunctionCallStep; fc != nil && !executedCalls[fc.ID] {
                pendingCalls = append(pendingCalls, fc)
            }
        }

        if len(pendingCalls) > 0 {
            fcStep := pendingCalls[0]
            fmt.Printf("Function to call: %s (ID: %s)\n", fcStep.Name, fcStep.ID)
            fmt.Printf("Arguments: %v\n", fcStep.Arguments)

            // 3. Execute the function locally (simulated get_weather()) and send the result back (Turn 2)
            resultStep := interactions.FunctionResultStep{
                Name:   genai.Ptr(fcStep.Name),
                CallID: fcStep.ID,
                Result: interactions.NewFunctionResultStepResultUnion(`{"temperature": 23, "unit": "celsius"}`),
            }

            followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
                Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
                    Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
                    PreviousInteractionID: interaction.ID,
                    Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
                    Input: interactions.NewInteractionsInput([]interactions.Step{
                        interactions.NewStep(resultStep),
                    }),
                }),
            })
            if err != nil {
                log.Fatal(err)
            }
            if followupRes.Interaction.OutputText != nil {
                fmt.Println(*followupRes.Interaction.OutputText)
            }
        } else {
            fmt.Println("No pending function calls.")
        }
    } else {
        fmt.Printf("Interaction completed with status: %s\n", interaction.Status)
    }
}
```

### REST

```
# 1. Turn 1: Request function call
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [
          {"type": "code_execution"},
          {
              "type": "function",
              "name": "get_weather",
              "description": "Gets the current weather for a given location.",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {"type": "string"}
                  },
                  "required": ["location"]
              }
          }
      ]
  }')

# Extract interaction ID, environment ID, and call ID (requires jq)
INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')
ENVIRONMENT_ID=$(echo $RESPONSE | jq -r '.environment_id')
CALL_ID=$(echo $RESPONSE | jq -r '.steps[] | select(.type=="function_call") | .id')

# 2. Turn 2: Send function result back using variables
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d "{
      \"agent\": \"antigravity-preview-09-2026\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"input\": [
          {
              \"type\": \"function_result\",
              \"name\": \"get_weather\",
              \"call_id\": \"$CALL_ID\",
              \"result\": {
                  \"temperature\": 23,
                  \"unit\": \"celsius\"
              }
          }
      ]
  }"
```

## MCP サーバー

リモート Model Context Protocol（MCP）サーバーを登録することで、Antigravity エージェントを外部ツールに接続できます。エージェントは、ストリーミング可能な HTTP 経由のリモート MCP サーバーをサポートしています。

MCP サーバーを登録する際は、`tools` 配列に次のフィールドを指定する必要があります。

| フィールド | 型 | 必須 / 省略可 | 説明 |
| --- | --- | --- | --- |
| `type` | 文字列 | ○ | `"mcp_server"` を指定します。 |
| `name` | 文字列 | ○ | サーバーの固有識別子。小文字の英数字（`^[a-z0-9_-]+$` に一致）にする必要があります。 |
| `url` | 文字列 | ○ | リモート MCP サーバーのエンドポイント URL。 |
| `headers` | オブジェクト | いいえ | リクエストとともに送信されるカスタム ヘッダー（認証など）。 |
| `allowed_tools` | 配列 | いいえ | 実行を許可するツール名のリスト。省略すると、すべてのツールが許可されます。 |

### Python

```
from google import genai

client = genai.Client()

# Register a remote HTTP MCP server
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="What is the weather in Tokyo?",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "weather", # Must be lowercase
        "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "What is the weather in Tokyo?",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "weather", // Must be lowercase
        url: "https://gemini-api-demos.uc.r.appspot.com/mcp"
    }]
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.MCPServer;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

// Register a remote HTTP MCP server
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("What is the weather in Tokyo?"))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .tools(List.of(
        MCPServer.builder()
            .name("weather") // Must be lowercase
            .url("https://gemini-api-demos.uc.r.appspot.com/mcp")
            .build()
    ))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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

    // Register a remote HTTP MCP server
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("What is the weather in Tokyo?"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("weather"), // Must be lowercase
                    URL:  genai.Ptr("https://gemini-api-demos.uc.r.appspot.com/mcp"),
                }),
            },
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
      "input": "What is the weather in Tokyo?",
      "environment": "remote",
      "tools": [{
          "type": "mcp_server",
          "name": "weather",
          "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
      }]
  }'
```

## モデルの選択

`antigravity-preview-09-2026` の場合、デフォルトのモデルは **Gemini 3.8 Flash**（`gemini-3.8-flash`）です。`agent_config` を省略すると、エージェントはデフォルトで `gemini-3.8-flash` になります。

`agent_config` を使用して、速度、費用、推論能力を最適化するように、基盤となる Gemini モデルを構成できます。たとえば、複雑なソフトウェア エンジニアリングと推論タスクの場合は、`model` を **Gemini 4 Argon**（`gemini-4-argon`）に設定します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Summarize the key differences between functional and object-oriented programming.",
    environment="remote",
    agent_config={
        "type": "antigravity",
        "model": "gemini-4-argon",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Summarize the key differences between functional and object-oriented programming.",
    environment: "remote",
    agent_config: {
        type: "antigravity",
        model: "gemini-4-argon",
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Summarize the key differences between functional and object-oriented programming."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .model("gemini-4-argon")
            .build()
    )
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
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
            Input:       interactions.NewInteractionsInput("Summarize the key differences between functional and object-oriented programming."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-4-argon"),
            })),
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
      "input": "Summarize the key differences between functional and object-oriented programming.",
      "environment": "remote",
      "agent_config": {
          "type": "antigravity",
          "model": "gemini-4-argon"
      }
  }'
```

`agent_config.model` でサポートされている値は次のとおりです。

| モデル | `agent_config.model` の値 | 説明 |
| --- | --- | --- |
| **Gemini 3.8 Flash**（デフォルト） | `gemini-3.8-flash` | 推論、コーディング、ツール使用のデフォルトのバランス モデル。 |
| **Gemini 4 Argon** | `gemini-4-argon` | 複雑なソフトウェア エンジニアリング、高度な問題解決、長期的なエージェント タスク向けのフロンティア推論モデル。 |
| **Gemini 3.6 Flash** | `gemini-3.6-flash` | 一般的な Agentic Workflows 向けのバランスの取れた Flash モデル。 |
| **Gemini 3.5 Flash-Lite** | `gemini-3.5-flash-lite` | 低レイテンシとコスト重視のタスクに最適化された軽量モデル。 |

`agents.create` を使用してマネージド エージェントを作成する場合は、`base_agent` と `agent_config` を渡すことで、モデルをまったく同じ方法で構成します。`agents.create` で作成されたマネージド エージェントの場合、インタラクション時にモデルをオーバーライドすることはできません。モデルは、エージェントの作成時に設定されたものにロックされます。これにより、予測可能なツール呼び出し動作、一貫したデバッグ、セキュリティ境界の遵守が保証されます。

## エージェントのカスタマイズ

Antigravity エージェントは、命令、ツール、環境をカスタマイズすることで拡張できます。エージェントは、カスタマイズに対するファイル システム ネイティブなアプローチをサポートしています。指示やスキル用の `AGENTS.md` などのファイルを `.agents/skills/` の下に直接サンドボックスにマウントしたり、やり取り時に構成をインラインで渡したりできます。構成をインラインで反復処理し、準備ができたらマネージド エージェントとして保存できます。

カスタム エージェントの構築方法の詳細については、[マネージド エージェントの構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja)をご覧ください。

## バックグラウンド実行

複数ステップの推論、コード実行、ファイル オペレーションを伴うエージェント タスクは、完了までに数分かかることがあります。`background=True` を使用して、インタラクションを非同期で実行します。API はすぐにインタラクション ID を返します。この ID は、ステータスが `completed` または `failed` になるまでポーリングします。

### Python

```
import time
from google import genai

client = genai.Client()

# 1. Start the interaction in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run a complex analysis on the repository.",
    environment="remote",
    background=True,
)

print(f"Interaction started in background: {interaction.id}")

# 2. Poll for completion
while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

if interaction.status == "completed":
    print(interaction.output_text)
else:
    print(f"Finished with status: {interaction.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run a complex analysis on the repository.",
    environment: "remote",
    background: true,
});

console.log(`Interaction started in background: ${interaction.id}`);

let result = interaction;
while (result.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    result = await client.interactions.get(interaction.id);
}

if (result.status === "completed") {
    console.log(result.output_text);
} else {
    console.log(`Finished with status: ${result.status}`);
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// 1. Start the interaction in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run a complex analysis on the repository."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Interaction started in background: " + interaction.id().orElse(""));

// 2. Poll for completion
while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

if (interaction.status().orElse(null) == InteractionStatus.COMPLETED) {
    System.out.println(interaction.outputText().orElse(""));
} else {
    System.out.println("Finished with status: " + interaction.status().orElse(null));
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    // 1. Start the interaction in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run a complex analysis on the repository."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Interaction started in background: %s\n", *interaction.ID)

    // 2. Poll for completion
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    if interaction.Status == interactions.InteractionStatusCompleted {
        if interaction.OutputText != nil {
            fmt.Println(*interaction.OutputText)
        }
    } else {
        fmt.Printf("Finished with status: %s\n", interaction.Status)
    }
}
```

### REST

```
# 1. Start the interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Run a complex analysis on the repository.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll for results (repeat until status is "completed")
curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

バックグラウンド実行には `store=True` が必要です。これはデフォルトです。バックグラウンド実行中の進行状況のリアルタイム更新については、[バックグラウンド操作のストリーミング](https://ai.google.dev/gemini-api/docs/background-execution?hl=ja#streaming-pattern)をご覧ください。

実行中のバックグラウンド インタラクションをキャンセルするには、`cancel` メソッドを使用します。

### Python

```
client.interactions.cancel(id="INTERACTION_ID")
```

### JavaScript

```
await client.interactions.cancel("INTERACTION_ID");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();
client.interactions.cancel("INTERACTION_ID");
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Interactions.Cancel(ctx, operations.CancelInteractionByIDRequest{
        ID: "INTERACTION_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions/INTERACTION_ID:cancel" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

**バックグラウンド実行による複数ターンの会話**

バックグラウンド インタラクションにステートフル ツール（サンドボックスでのコード実行など）が含まれている場合は、完了したインタラクションの `environment_id` を使用して、同じ環境で続行します。これにより、エージェントはすべてのファイルと状態をそのままにして、中断したところから再開できます。

### Python

```
import time
from google import genai

client = genai.Client()

# First turn: run a task in the background
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/google/generative-ai-python and run its tests.",
    environment="remote",
    background=True,
)

while interaction.status == "in_progress":
    time.sleep(5)
    interaction = client.interactions.get(id=interaction.id)

# Second turn: continue in the same environment
followup = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fix any failing tests and re-run them.",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    background=True,
)

while followup.status == "in_progress":
    time.sleep(5)
    followup = client.interactions.get(id=followup.id)

print(followup.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn: run a task in the background
let interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Clone https://github.com/google/generative-ai-python and run its tests.",
    environment: "remote",
    background: true,
});

while (interaction.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    interaction = await client.interactions.get(interaction.id);
}

// Second turn: continue in the same environment
let followup = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fix any failing tests and re-run them.",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    background: true,
});

while (followup.status === "in_progress") {
    await new Promise(resolve => setTimeout(resolve, 5000));
    followup = await client.interactions.get(followup.id);
}

console.log(followup.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionStatus;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;

Client client = new Client();

// First turn: run a task in the background
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/google/generative-ai-python and run its tests."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .background(true)
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

while (interaction.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    interaction = client.interactions.get(new GetInteractionByIdRequest(interaction.id().orElse(""))).interaction().get();
}

// Second turn: continue in the same environment
CreateAgentInteraction followupParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fix any failing tests and re-run them."))
    .previousInteractionId(interaction.id().orElse(""))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .background(true)
    .build();

Interaction followup = client.interactions.create(CreateInteractionRequestBody.of(followupParams)).interaction().get();

while (followup.status().orElse(null) == InteractionStatus.IN_PROGRESS) {
    Thread.sleep(5000);
    followup = client.interactions.get(new GetInteractionByIdRequest(followup.id().orElse(""))).interaction().get();
}

System.out.println(followup.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "time"

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

    // First turn: run a task in the background
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Clone https://github.com/google/generative-ai-python and run its tests."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
            Background:  genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    for interaction.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *interaction.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        interaction = getRes.Interaction
    }

    // Second turn: continue in the same environment
    followupRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Fix any failing tests and re-run them."),
            PreviousInteractionID: interaction.ID,
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            Background:            genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    followup := followupRes.Interaction
    for followup.Status == interactions.InteractionStatusInProgress {
        time.Sleep(5 * time.Second)
        getRes, err := client.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
            ID: *followup.ID,
        })
        if err != nil {
            log.Fatal(err)
        }
        followup = getRes.Interaction
    }

    if followup.OutputText != nil {
        fmt.Println(*followup.OutputText)
    }
}
```

### REST

```
# 1. Start first interaction in the background
RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Clone https://github.com/google/generative-ai-python and run its tests.",
      "environment": "remote",
      "background": true
  }')

INTERACTION_ID=$(echo $RESPONSE | jq -r '.id')

# 2. Poll until completed (repeat until status is "completed")
RESULT=$(curl -s -X GET "https://generativelanguage.googleapis.com/v1beta/interactions/$INTERACTION_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY")

ENVIRONMENT_ID=$(echo $RESULT | jq -r '.environment_id')

# 3. Continue in the same environment
curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Api-Revision: 2026-05-20" \
  -d "{
      \"agent\": \"antigravity-preview-09-2026\",
      \"input\": \"Fix any failing tests and re-run them.\",
      \"previous_interaction_id\": \"$INTERACTION_ID\",
      \"environment\": \"$ENVIRONMENT_ID\",
      \"background\": true
  }"
```

## 環境

呼び出しごとに、Linux サンドボックスが作成されるか、再利用されます。`environment` パラメータには次の 3 つの形式があります。

| フォーム | 説明 |
| --- | --- |
| `"remote"` | デフォルト設定で新しいサンドボックスをプロビジョニングします。 |
| `"env_abc123"` | ID で既存の環境を再利用し、すべてのファイルと状態を保持します。 |
| `{...}` | カスタムソースとネットワーク ルールを使用した完全な `EnvironmentConfig`。 |

ソース（Git、GCS、インライン）、ネットワーキング、ライフサイクル、リソースの上限の詳細については、[環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja)をご覧ください。

## トリガー

トリガーを使用すると、Cron スケジュールでエージェントが自動的に実行されるようにスケジュールを設定できます。トリガーは、エージェント、環境、プロンプト、スケジュールを永続的なリソースにバインドし、手動介入なしで実行します。各実行では同じ環境が再利用されるため、1 回の実行で作成されたファイルは保持され、次の実行でも参照できます。

### トリガーを作成する

cron スケジュール、タイムゾーン、インタラクション構成を指定してトリガーを作成します。トリガーは `active` ステータスで開始され、次に一致する cron 時間に起動します。返された `id` を保存して、後続の呼び出しでトリガーを管理します。

トリガーはスケジュールに従って無人で実行されるため、インライン トークンではなく、保存された[認証情報](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ja)を参照します。下り（外向き）プロキシは実行のたびにシークレットを解決し、トリガーに触れることなくシークレットをローテーションします。インライン `transform` ルールはここでも機能します。値が変更されるたびにトリガーを更新する必要があります。

### Python

```
from google import genai

client = genai.Client()

trigger = client.triggers.create(
    schedule="0 9 * * *",
    time_zone="America/Argentina/Buenos_Aires",
    display_name="issue-solver",
    interaction={
        "agent": "antigravity-preview-09-2026",
        "input": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        "environment": {
            "type": "remote",
            "network": {
                "allowlist": [
                    {
                        "domain": "api.github.com",
                        "credential": "github-production",
                    },
                    {"domain": "github.com"},
                ]
            },
        },
    },
)

print(f"Trigger created: {trigger.id}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const trigger = await client.triggers.create({
    schedule: "0 9 * * *",
    time_zone: "America/Argentina/Buenos_Aires",
    display_name: "issue-solver",
    interaction: {
        agent: "antigravity-preview-09-2026",
        input: [{
            type: "text",
            text: "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/.",
        }],
        environment: {
            type: "remote",
            network: {
                allowlist: [
                    {
                        domain: "api.github.com",
                        credential: "github-production",
                    },
                    { domain: "github.com" },
                ],
            },
        },
    },
});

console.log(`Trigger created: ${trigger.id}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import com.google.genai.gaos.models.triggers.TriggerCreateParams;
import java.util.List;
import java.util.Map;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("github.com")
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction interactionTemplate = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

TriggerCreateParams params = TriggerCreateParams.builder()
    .schedule("0 9 * * *")
    .timeZone("America/Argentina/Buenos_Aires")
    .displayName("issue-solver")
    .interaction(interactionTemplate)
    .build();

Trigger trigger = client.triggers().create(params).trigger().get();
System.out.println("Trigger created: " + trigger.id().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    })),
                },
                {
                    Domain: "github.com",
                },
            })),
        })),
    }

    interactionTemplate := interactions.CreateAgentInteraction{
        Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
        Input:       interactions.NewInteractionsInput("Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled 'accepted', skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."),
        Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
    }

    res, err := sdk.Triggers.Create(ctx, operations.CreateTriggerRequest{
        Body: triggers.TriggerCreateParams{
            Schedule:    "0 9 * * *",
            TimeZone:    "America/Argentina/Buenos_Aires",
            DisplayName: genai.Ptr("issue-solver"),
            Interaction: interactionTemplate,
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    trigger := res.Trigger
    fmt.Printf("Trigger created: %s\n", trigger.ID)
    fmt.Printf("Next run: %v\n", trigger.NextRunTime)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "schedule": "0 9 * * *",
      "time_zone": "America/Argentina/Buenos_Aires",
      "display_name": "issue-solver",
      "interaction": {
          "agent": "antigravity-preview-09-2026",
          "input": [{"type": "text", "text": "Review open PRs in my-org/my-app for new comments and address feedback. Close issues whose PRs were merged. Then check for new issues labeled accepted, skip any already tracked in /workspace/solved-issues/, fix the rest, and open a PR for each. Save reports to /workspace/solved-issues/."}],
          "environment": {
              "type": "remote",
              "network": {
                  "allowlist": [
                      {
                          "domain": "api.github.com",
                          "credential": "github-production"
                      },
                      {"domain": "github.com"}
                  ]
              }
          }
      }
  }'
```

`CreateTrigger` リクエストでは、次のフィールドを指定できます。

| フィールド | 型 | 必須 / 省略可 | 説明 |
| --- | --- | --- | --- |
| `schedule` | 文字列 | ○ | cron 式（例: `0 * * * *` は毎時、`0 9 * * 1-5` は平日の午前）。 |
| `time_zone` | 文字列 | ○ | IANA タイムゾーン（例: `UTC`、`America/Argentina/Buenos_Aires`）。 |
| `display_name` | 文字列 | いいえ | 人が読める形式のトリガー名。 |
| `max_consecutive_failures` | integer | いいえ | トリガーが自動的に一時停止するまでの最大失敗回数。デフォルト: 5。 |
| `execution_timeout_seconds` | integer | いいえ | 実行あたりのタイムアウト（秒単位）。デフォルト: 600。 |
| `interaction` | オブジェクト | ○ | エージェント、入力、ツール、環境を定義する `CreateInteractionRequest`。 |

レスポンスには次のキーフィールドが含まれます。

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `id` | 文字列 | トリガーの固有識別子。以降のすべてのオペレーションでこれを使用します。 |
| `status` | 文字列 | 現在の状態: `active`、`paused`、`disabled`。 |
| `next_run_time` | 文字列 | 次回の実行スケジュールの ISO 8601 タイムスタンプ。 |
| `consecutive_failure_count` | integer | 最後の成功以降の連続した失敗実行回数。 |

### トリガーの一覧表示

プロジェクトに関連付けられているすべてのトリガーを取得します。

### Python

```
triggers = client.triggers.list()
for trigger in triggers.triggers:
    print(f"{trigger.id}: {trigger.display_name} ({trigger.status})")
```

### JavaScript

```
const triggers = await client.triggers.list();
for (const trigger of triggers.triggers) {
    console.log(`${trigger.id}: ${trigger.display_name} (${trigger.status})`);
}
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<Trigger> triggers = client.triggers().listDirect().listTriggersResponse().get().triggers().orElse(List.of());
for (Trigger trigger : triggers) {
    System.out.println(trigger.id().orElse("") + ": " + trigger.displayName().orElse("") + " (" + trigger.status().orElse(null) + ")");
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.List(ctx, operations.ListTriggersRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggersResponse != nil {
        for _, trigger := range res.ListTriggersResponse.Triggers {
            fmt.Printf("%s: %s (%v)\n", trigger.ID, *trigger.GetDisplayName(), trigger.Status)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### トリガーを取得する

1 つのトリガーの完全な構成と現在の状態を取得します。

### Python

```
trigger = client.triggers.get(id="TRIGGER_ID")
print(f"Schedule: {trigger.schedule}")
print(f"Next run: {trigger.next_run_time}")
```

### JavaScript

```
const trigger = await client.triggers.get("TRIGGER_ID");
console.log(`Schedule: ${trigger.schedule}`);
console.log(`Next run: ${trigger.next_run_time}`);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.Trigger;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

Trigger trigger = client.triggers().get("TRIGGER_ID").trigger().get();
System.out.println("Schedule: " + trigger.schedule().orElse(""));
System.out.println("Next run: " + trigger.nextRunTime().orElse(null));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.Get(ctx, operations.GetTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Schedule: %s\n", res.Trigger.Schedule)
    fmt.Printf("Next run: %v\n", res.Trigger.NextRunTime)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 一時停止と再開

トリガーを一時停止すると、スケジュールされた実行を停止できます。再開すると、スケジュールが再び有効になります。一時停止は手動実行には影響しません。

### Python

```
# Pause
client.triggers.update(id="TRIGGER_ID", status="paused")

# Resume
client.triggers.update(id="TRIGGER_ID", status="active")
```

### JavaScript

```
// Pause
await client.triggers.update("TRIGGER_ID", { status: "paused" });

// Resume
await client.triggers.update("TRIGGER_ID", { status: "active" });
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerUpdate;
import com.google.genai.gaos.models.triggers.TriggerUpdateStatus;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

// Pause
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.PAUSED).build());

// Resume
client.triggers().update("TRIGGER_ID", TriggerUpdate.builder().status(TriggerUpdateStatus.ACTIVE).build());
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
    "google.golang.org/genai/interactions/models/triggers"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    // Pause
    _, err := sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusPaused.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    // Resume
    _, err = sdk.Triggers.Update(ctx, operations.UpdateTriggerRequest{
        ID: "TRIGGER_ID",
        Body: triggers.TriggerUpdate{
            Status: triggers.TriggerUpdateStatusActive.ToPointer(),
        },
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
# Pause
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "paused"}'

# Resume
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{"status": "active"}'
```

### トリガーの削除

トリガーを完全に削除します。過去の実行履歴は削除されません。

### Python

```
client.triggers.delete(id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.delete("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().delete("TRIGGER_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Delete(ctx, operations.DeleteTriggerRequest{
        ID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### トリガーをすぐに実行する

次のスケジュールされた時刻を待たずに、オンデマンドでトリガーを起動します。これは、トリガーが一時停止されている場合でも機能します。

### Python

```
client.triggers.run(trigger_id="TRIGGER_ID")
```

### JavaScript

```
await client.triggers.run("TRIGGER_ID");
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.shared.Security;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

client.triggers().run("TRIGGER_ID");
```

### Go

```
package main

import (
    "context"
    "log"
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    _, err := sdk.Triggers.Run(ctx, operations.RunTriggerRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### 実行の一覧表示

トリガーの実行履歴を表示します。各実行には、`status`、タイムスタンプ、完全なインタラクション出力を取得するために使用できる `interaction_id`、すべての実行が同じサンドボックスを共有していることを確認する `environment_id` が含まれます。

### Python

```
executions = client.triggers.list_executions(trigger_id="TRIGGER_ID")
for ex in executions.trigger_executions:
    print(f"{ex.id}: {ex.status} ({ex.start_time} - {ex.end_time})")

# Fetch the full interaction for an execution
interaction = client.interactions.get(id=ex.interaction_id)
print(interaction.output_text)
```

### JavaScript

```
const executions = await client.triggers.listExecutions("TRIGGER_ID");
for (const ex of executions.trigger_executions) {
    console.log(`${ex.id}: ${ex.status} (${ex.start_time} - ${ex.end_time})`);
}

// Fetch the full interaction for an execution
const interaction = await client.interactions.get(ex.interaction_id);
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.gaos.GenAI;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.operations.GetInteractionByIdRequest;
import com.google.genai.gaos.models.shared.Security;
import com.google.genai.gaos.models.triggers.TriggerExecution;
import java.util.List;

GenAI client = GenAI.builder()
    .security(Security.builder().apiKey(System.getenv("GEMINI_API_KEY")).build())
    .build();

List<TriggerExecution> executions = client.triggers().listExecutions("TRIGGER_ID")
    .listTriggerExecutionsResponse().get()
    .triggerExecutions().orElse(List.of());

for (TriggerExecution ex : executions) {
    System.out.println(ex.id().orElse("") + ": " + ex.status().orElse(null)
        + " (" + ex.startTime().orElse(null) + " - " + ex.endTime().orElse(null) + ")");

    // Fetch the full interaction for an execution
    if (ex.interactionId().isPresent()) {
        Interaction interaction = client.interactions().get(new GetInteractionByIdRequest(ex.interactionId().get())).interaction().get();
        System.out.println(interaction.outputText().orElse(""));
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
    "os"

    "google.golang.org/genai"
    interactionssdk "google.golang.org/genai/interactions"
    "google.golang.org/genai/interactions/models/components"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    sdk := interactionssdk.New(interactionssdk.WithSecurity(components.Security{
        APIKey: genai.Ptr(os.Getenv("GEMINI_API_KEY")),
    }))

    res, err := sdk.Triggers.ListExecutions(ctx, operations.ListTriggerExecutionsRequest{
        TriggerID: "TRIGGER_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListTriggerExecutionsResponse != nil {
        for _, ex := range res.ListTriggerExecutionsResponse.TriggerExecutions {
            fmt.Printf("%s: %v (%v - %v)\n", ex.ID, ex.Status, ex.StartTime, ex.EndTime)

            // Fetch the full interaction for an execution
            if ex.InteractionID != nil {
                intRes, err := sdk.Interactions.Get(ctx, operations.GetInteractionByIDRequest{
                    ID: *ex.InteractionID,
                })
                if err != nil {
                    log.Fatal(err)
                }
                if intRes.Interaction.OutputText != nil {
                    fmt.Println(*intRes.Interaction.OutputText)
                }
            }
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/triggers/TRIGGER_ID/executions" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## 提供状況と価格

Antigravity エージェントは、Google AI Studio の [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) と Gemini API を通じて、無料枠と有料枠の両方のプロジェクトでプレビュー版として利用できます。

料金は、基盤となる Gemini モデルのトークンとエージェントが使用するツールに基づく[従量課金制モデル](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#pricing-for-agents)に従います。単一の出力を生成する標準的なチャット リクエストとは異なり、Antigravity インタラクションはエージェント ワークフローです。1 つのリクエストで、推論、ツールの実行、コードの実行、ファイル管理の自律的なループがトリガーされます。無料枠プロジェクトには、無料のレート制限と使用量割り当てが含まれます。

Antigravity のインタラクションは、マルチターンの自律ループを実行し、大量のトークンを消費する可能性があります。リクエストに[予算管理](#budget-controls)を設定して、トークンの使用量を制限します。[SSE ストリーミング](https://ai.google.dev/gemini-api/docs/streaming?hl=ja)を使用して進行状況をリアルタイムでモニタリングしたり、実行中のリクエストをキャンセルしたりすることもできます。

### 予算管理

[モデルの選択](#model-selection)に加えて、`agent_config`（`"type": "antigravity"` を使用）内で `max_total_tokens` を設定して、インタラクションで使用できるトークンの合計数（入力 + 出力 + 思考）を制限します。キャッシュに保存されたトークンは、この上限にはカウントされません。エージェントが上限に達すると、インタラクションが停止し、`status: "incomplete"` が返されます。この上限はベスト エフォートです。エージェントがステップ間で予算を確認するタイミングによっては、実際の使用量が上限をわずかに超える可能性があります。

`agent_config` のインタラクション リクエストで、`agent` と `input` とともに予算を設定します。

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    },
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": "/workspace/data.csv",
                "content": "id,name,value\n1,alpha,100\n2,beta,200\n",
            }
        ],
    }
)
print(f"Status: {interaction.status}")  # "incomplete" if budget was hit
print(f"Tokens used: {interaction.usage.total_tokens}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    },
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: "/workspace/data.csv",
                content: "id,name,value\n1,alpha,100\n2,beta,200\n",
            },
        ],
    },
});
console.log(`Status: ${interaction.status}`);
console.log(`Tokens used: ${interaction.usage?.total_tokens}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.INLINE)
            .target("/workspace/data.csv")
            .content("id,name,value\n1,alpha,100\n2,beta,200\n")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the dataset in /workspace/data.csv and generate a summary report."))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + interaction.status().orElse(null)); // "incomplete" if budget was hit
interaction.usage().ifPresent(usage -> System.out.println("Tokens used: " + usage.totalTokens().orElse(0)));
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr("/workspace/data.csv"),
                Content: genai.Ptr("id,name,value\n1,alpha,100\n2,beta,200\n"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Analyze the dataset in /workspace/data.csv and generate a summary report."),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    interaction := res.Interaction
    fmt.Printf("Status: %s\n", interaction.Status) // "incomplete" if budget was hit
    if interaction.Usage != nil && interaction.Usage.TotalTokens != nil {
        fmt.Printf("Tokens used: %d\n", *interaction.Usage.TotalTokens)
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
    "input": "Analyze the dataset in /workspace/data.csv and generate a summary report.",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    },
    "environment": {
      "type": "remote",
      "sources": [
        {
          "type": "inline",
          "target": "/workspace/data.csv",
          "content": "id,name,value\n1,alpha,100\n2,beta,200\n"
        }
      ]
    }
  }'
```

#### 未完了のやり取りを継続する

インタラクションが `status: "incomplete"` を返すと、エージェントの作業とコンテキストが保持されます。元のインタラクション `id` と `environment_id` を参照する新しいインタラクションを送信して、中断したところから再開します。新しいインタラクションには、独自の `max_total_tokens` 予算が割り当てられます。

### Python

```
# Continue from where the agent stopped
continuation = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="continue",
    previous_interaction_id=interaction.id,
    environment=interaction.environment_id,
    agent_config={
        "type": "antigravity",
        "max_total_tokens": 50000
    }
)
print(f"Status: {continuation.status}")
```

### JavaScript

```
const continuation = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "continue",
    previous_interaction_id: interaction.id,
    environment: interaction.environment_id,
    agent_config: {
        type: "antigravity",
        max_total_tokens: "50000"
    }
});
console.log(`Status: ${continuation.status}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.AntigravityAgentConfig;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();
String interactionId = "INTERACTION_ID";
String environmentId = "ENVIRONMENT_ID";

// Continue from where the agent stopped
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("continue"))
    .previousInteractionId(interactionId)
    .environment(CreateAgentInteractionEnvironment.of(environmentId))
    .agentConfig(
        AntigravityAgentConfig.builder()
            .maxTotalTokens("50000")
            .build()
    )
    .build();

Interaction continuation = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Status: " + continuation.status().orElse(null));
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

    // Continue from where the agent stopped
    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("continue"),
            PreviousInteractionID: genai.Ptr(interactionID),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(environmentID)),
            AgentConfig: genai.Ptr(interactions.NewCreateAgentInteractionAgentConfig(interactions.AntigravityAgentConfig{
                MaxTotalTokens: genai.Ptr(int64(50000)),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Status: %s\n", res.Interaction.Status)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
    "agent": "antigravity-preview-09-2026",
    "input": "continue",
    "previous_interaction_id": "INTERACTION_ID",
    "environment": "ENVIRONMENT_ID",
    "agent_config": {
      "type": "antigravity",
      "max_total_tokens": 50000
    }
  }'
```

### 推定費用

費用はタスクの複雑さによって異なります。エージェントは、必要なツール呼び出し、コード実行、ファイル操作の数を自律的に判断します。以下の見積もりは実行に基づいています。

| タスクのカテゴリ | 入力トークン | 出力トークン | 一般的な費用 |
| --- | --- | --- | --- |
| **リサーチと情報の統合** | 10 万～ 50 万 | 10,000 ～ 40,000 | $0.30 ～$1.00 |
| **ドキュメントとコンテンツの生成** | 10 万～ 50 万 | 15,000 ～ 50,000 | $0.30 ～$1.30 |
| **プロセスとシステムの設計** | 10 万～ 40 万 | 10,000 ～ 30,000 | $0.25 ～$0.80 |
| **データ処理と分析** | 30 万～ 300 万 | 3 万～ 15 万 | $0.70 ～$3.25 |

通常、入力トークンの 50 ～ 70% がキャッシュされます。多くのツール呼び出しを伴う複雑な Agentic Workflows では、1 回のインタラクションで 300 万～ 500 万トークンが蓄積され、費用は最大 5 ドルに達することがあります。

プレビュー期間中は、**環境コンピューティング**（CPU、メモリ、サンドボックス実行）は**課金されません**。

## 制限事項

- **プレビュー ステータス:** Antigravity エージェントと Interactions API。機能とスキーマは変更される可能性があります。
- **サポートされていない生成構成:** 次のパラメータはサポートされておらず、400 エラーが返されます。`temperature`、`top_p`、`top_k`、`stop_sequences`、`max_output_tokens`。
- **構造化出力:** Antigravity エージェントは構造化出力をサポートしていません。
- **利用できないツール:** `file_search`、`computer_use`、`google_maps` はまだサポートされていません。
- **リモート MCP の制限事項:** サーバー送信イベント（SSE）トランスポートはサポートされていません（ストリーミング可能な HTTP を使用してください）。また、サーバー `name` は厳密に小文字の英数字である必要があります（大文字を使用すると、一般的な `400 Bad Request` エラーがトリガーされます）。
- **ファイルシステム ツール:** 現在、ファイルシステム ツールはありません。これは `environment` の一部です。
- **ストアの要件:** `background=True` を使用したエージェントの実行には `store=True` が必要です。
- **ステートフルのみの関数呼び出し:** 関数呼び出しはステートフル モードでのみサポートされています。ターンを続行するには `previous_interaction_id` を使用する必要があります。履歴を手動で再構築する（ステートレス モード）ことはサポートされていません。
- **サポートされていないマルチモーダル タイプ。**現時点では、音声、動画、ドキュメントの入力はサポートされていません。テキストと画像のみが許可されます。

## 次のステップ

- [クイックスタート](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja): マルチターン会話とストリーミング。
- [カスタム エージェントの構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja): カスタム指示、スキル、エージェントの保存。
- [環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja): サンドボックス構成、ソース、ネットワーキング。
- [フック](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=ja): サンドボックス内でセキュリティ ゲートと副作用の検証を適用します。
- [Deep Research エージェント](https://ai.google.dev/gemini-api/docs/deep-research?hl=ja): 長文の調査タスク。
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja): 基盤となる API。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-10-16 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-10-16 UTC。"],[],[]]
