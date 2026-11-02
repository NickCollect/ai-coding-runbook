---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=fa
fetched_at: 2026-11-02T07:30:05.919632+00:00
title: "\u0645\u062d\u06cc\u0637\u200c\u0647\u0627 \u062f\u0631 \u0639\u0627\u0645\u0644\u200c\u0647\u0627\u06cc \u0645\u062f\u06cc\u0631\u06cc\u062a\u200c\u0634\u062f\u0647 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# محیط‌ها در عامل‌های مدیریت‌شده

محیط‌ها جعبه‌های ایمنی مدیریت‌شده Linux هستند که به عامل‌ها مکانی مجزا برای
اجرای کد و ماندگار کردن فایل‌ها می‌دهند. این محیط‌ها از بافت تعامل جدا شده‌اند، بنابراین می‌توانید از محیط یکسانی در چندین تعامل استفاده مجدد کنید یا هرزمان بخواهید از ابتدا شروع کنید.

مثال زیر نشان می‌دهد که چگونه می‌توان تعاملی با محیط راه دور جدید ایجاد کرد و شناسه آن را بازیابی کرد:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas and matplotlib, verify the imports, and print the versions.",
    environment="remote",
)

print(f"Environment ID: {interaction.environment_id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
```

### جاوا

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
    .input(InteractionsInput.of("Install pandas and matplotlib, verify the imports, and print the versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println("Environment ID: " + interaction.environmentId().orElse(""));
```

### رفتن

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
            Input:       interactions.NewInteractionsInput("Install pandas and matplotlib, verify the imports, and print the versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.Interaction.EnvironmentID != nil {
        fmt.Printf("Environment ID: %s\n", *res.Interaction.EnvironmentID)
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
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## پارامتر `environment`

پارامتر `environment` سه شکل را می‌پذیرد:

| فرم | مثال | زمان استفاده |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | جعبه شنی جدیدی آماده کنید. |
| شناسه محیط | `environment="env_abc123"` | از جعبه شنی موجود با همه فایل‌ها و بسته‌هایش مجدداً استفاده کنید. |
| شیء پیکربندی | `environment={...}` | سندباکس جدیدی را با منابع، قوانین شبکه، متغیرهای محیطی، یا ترکیبی از آن‌ها آماده کنید. |

نمونه‌های زیر سه روش استفاده از پارامتر `environment`
را نشان می‌دهد.

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files and summarize the project.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            }
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Fresh sandbox
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List all files and summarize the project.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
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

// Fresh sandbox
CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Write a hello world script."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse an existing sandbox
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Modify the script to accept a name argument."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// New sandbox with sources
Environment env3 = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build()
    ))
    .build();

CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files and summarize the project."))
    .environment(CreateAgentInteractionEnvironment.of(env3))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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

    // Fresh sandbox
    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Write a hello world script."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse an existing sandbox
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Modify the script to accept a name argument."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res2

    // New sandbox with sources
    env3 := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
        },
    }

    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files and summarize the project."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env3)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-09-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "List all files and summarize the project."}],
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            }
        ]
    }
}'
```

## پیکربندی محیط

یکی از روش‌های راه‌اندازی محیط این است که به عامل بگویید چه چیزی باید نصب شود.
این ویژگی حل وابستگی و عیب‌یابی را مدیریت می‌کند. وقتی محیط آماده شد، `environment_id` را ذخیره کنید و دوباره از آن استفاده کنید.

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Using the tools in /workspace/tools, list the files.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction_2.id,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateAgentInteraction params1 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();
Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params2 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction.id().orElse(""))
    .build();
Interaction interaction2 = client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

// Reuse the configured environment
CreateAgentInteraction params3 = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Using the tools in /workspace/tools, list the files."))
    .environment(CreateAgentInteractionEnvironment.of(interaction.environmentId().orElse("")))
    .previousInteractionId(interaction2.id().orElse(""))
    .build();
Interaction interaction3 = client.interactions.create(CreateInteractionRequestBody.of(params3)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := res1.Interaction

    // Reuse the configured environment
    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction2 := res2.Interaction

    // Reuse the configured environment
    res3, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:                 interactions.AgentOption("antigravity-preview-09-2026"),
            Input:                 interactions.NewInteractionsInput("Using the tools in /workspace/tools, list the files."),
            Environment:           genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(*interaction.EnvironmentID)),
            PreviousInteractionID: interaction2.ID,
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    _ = res3

    if interaction.OutputText != nil {
        fmt.Println(*interaction.OutputText)
    }
}
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### نصب از منبع

اگر دقیقاً می‌دانید نماینده به چه فایل‌هایی نیاز دارد، آن‌ها را در یک تماس واحد
به‌جای تکرار سوار کنید. شیء پیکربندی `environment` آرایه‌ای از `sources` را با سه نوع می‌پذیرد:

| نوع منبع | به‌ارزش `type` | شرح | حد |
| --- | --- | --- | --- |
| مخزن Git | `repository` | مخزنی را از نشانی وب در جعبه ایمنی در `target` همسانه‌سازی می‌کند. | ‫۵۰۰ مگابایت |
| فضای ذخیره‌سازی ابری | `gcs` | فایل یا دایرکتوری را از Cloud Storage در `target` در محیط امن کپی می‌کند. | ۲ گیگابایت |
| محتوای به‌خط | `inline` | محتوای نوشتاری خام را در فایلی در محیط امن در `target` می‌نویسد. | ۱ مگابایت برای هر فایل، مجموعاً ۲ مگابایت |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List all files under /workspace and describe what you find.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data",
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md",
            },
        ],
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
    input: "List all files under /workspace and describe what you find.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
            {
                type: "gcs",
                source: "gs://cloud-samples-data/bigquery/us-states/",
                target: "/workspace/gcs-data",
            },
            {
                type: "inline",
                content: "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                target: "/workspace/notes/readme.md",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
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
            .type(SourceType.REPOSITORY)
            .source("https://github.com/octocat/Spoon-Knife")
            .target("/workspace/spoon-knife")
            .build(),
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://cloud-samples-data/bigquery/us-states/")
            .target("/workspace/gcs-data")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .content("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n")
            .target("/workspace/notes/readme.md")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List all files under /workspace and describe what you find."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/octocat/Spoon-Knife"),
                Target: genai.Ptr("/workspace/spoon-knife"),
            },
            {
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://cloud-samples-data/bigquery/us-states/"),
                Target: genai.Ptr("/workspace/gcs-data"),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Content: genai.Ptr("# Project Notes\n\n- Analyze state population data\n- Create visualizations\n"),
                Target:  genai.Ptr("/workspace/notes/readme.md"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List all files under /workspace and describe what you find."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "List all files under /workspace and describe what you find.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data"
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md"
            }
        ]
    }
}'
```

می‌توانید هر دو رویکرد را ترکیب کنید: منابع شناخته‌شده را به‌صورت بیانیه نصب کنید، سپس با
تعاملات پیگیری برای نصب بسته‌ها یا اجرای دستورگان‌های راه‌اندازی تکرار کنید. هنگام افزودن منبع سفارشی نمی‌توانید
ریشه (`/`) را به‌عنوان هدف تنظیم کنید، همیشه باید
زیرپوشه را مشخص کنید.

### قلاب‌ها

همچنین می‌توانید یک فایل پیکربندی `.agents/hooks.json` و پلاتفرم‌های رهگیری سفارشی را در محیط امن نصب کنید تا نرده‌های محافظ امنیتی را اعمال کنید یا هر زمان که ابزارها اجرا می‌شوند، اعتبارسنجی‌های خودکار را اجرا کنید. برای تعریف‌های طرحواره و نمونه‌های کد، [قلاب‌ها](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fa) را ببینید.

### منابع خصوصی

همچنین می‌توانید با اصالت‌سنجی دامنه منبع در پیکربندی شبکه، از مخازن خصوصی GitHub یا دسته‌های خصوصی Cloud Storage بارگیری کنید.

یکی از گزینه‌ها [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره‌شده‌ای است که با شناسه ارجاع داده می‌شود، بنابراین رمز را یک‌بار ذخیره می‌کنید و هر محیطی که به آن منبع نیاز دارد می‌تواند به آن ارجاع دهد:

```
"network": {
    "allowlist": [
        { "domain": "github.com", "credential": "github-production" },
        { "domain": "*" }
    ]
}
```

همچنین می‌توانید سرایند را به‌صورت درون‌خطی با `transform` تنظیم کنید، همان‌طور که در مثال‌های زیر
انجام شده است. پراکسی خروجی هر دو شکل را به یک روش اعمال می‌کند و در هیچ‌کدام از این موارد
راز در داخل محیط امن قرار نمی‌گیرد.

برای **مخازن خصوصی Git**، از اصالت‌سنجی `Basic` با
[رمز دسترسی شخصی GitHub
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) استفاده کنید.
رمزگذاری کردن کد بااستفاده از `x-oauth-basic` به‌عنوان نام کاربری:

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the test for my backend app and fix any issue.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the test for my backend app and fix any issue.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app"
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/your-org/backend")
            .target("/backend-app")
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Run the test for my backend app and fix any issue."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/your-org/backend"),
                Target: genai.Ptr("/backend-app"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Run the test for my backend app and fix any issue."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": "Run the test for my backend app and fix any issue.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

برای **انباره‌های خصوصی Cloud Storage**، از یک نماد استاندارد OAuth 2.0 Bearer استفاده کنید:

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the discrepancies across the data in workspace",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "*.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Analyze the discrepancies across the data in workspace",
    environment: {
        type: "remote",
        sources: [
            {
                type: "gcs",
                source: "gs://my-private-bucket/data",
                target: "/workspace",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.GCS)
            .source("gs://my-private-bucket/data")
            .target("/workspace")
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("*.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer YOUR_GCS_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder()
                    .domain("*")
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the discrepancies across the data in workspace"))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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
                Type:   interactions.SourceTypeGcs.ToPointer(),
                Source: genai.Ptr("gs://my-private-bucket/data"),
                Target: genai.Ptr("/workspace"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "*.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer YOUR_GCS_TOKEN",
                    })),
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the discrepancies across the data in workspace"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": "Analyze the discrepancies across the data in workspace",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

## نرم‌افزار ازپیش نصب‌شده

جعبه امن روی Ubuntu اجرا می‌شود و زمان‌های اجرا و بسته‌های رایج ازقبل نصب‌شده دارد. کارگزار می‌تواند بسته‌های اضافی را در زمان اجرا بااستفاده از `pip
install` یا `npm install` نصب کند. بسته‌های نصب‌شده درطول تعامل وقتی که از همان `environment_id` استفاده مجدد می‌کنید ماندگار هستند.

| دسته | بسته‌های ازپیش نصب‌شده |
| --- | --- |
| **ابزارهای UNIX** | `curl`، `wget`، `git`، `rsync`، `unzip`، `ripgrep`، `fd-find`، `gawk`، `bc`، `tree`، `which`، `lsof`، `htop`، `jq`، `iproute2`، `procps`، `gcloud CLI` |
| **Python 3.12** | ‫`numpy`،‏ `pandas`،‏ `requests`،‏ `google-genai`،‏ `beautifulsoup4`،‏ `pyyaml`،‏ `ast-grep-cli` |
| **Node.js 22** | `create-next-app`، `create-vite`، `typescript` |

## متغیرهای محیط

از فیلد `env` برای تنظیم متغیرهای محیطی در محیط آزمایشی استفاده کنید. هر ورودی نام متغیر را به یکی از این موارد نگاشت می‌دهد:
یا رشته‌ای حرفی برای پیکربندی یا
مرجعی به [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره‌شده برای
رمز. کارگزار آن‌ها را همان‌گونه که در هر پوسته دیگری می‌بیند می‌بیند، بنابراین ابزارها و دستورگان‌هایی که از محیط فرایند می‌خوانند آن‌ها را بدون سیم‌کشی اضافی دریافت می‌کنند.

| فیلد | نوع | شرح |
| --- | --- | --- |
| `env` | `object` | نقشه نام متغیر به مقدار. مقدار یا یک مقدار ثابت `string` است یا مرجع اطلاعات اعتباری به‌شکل `{"credential": "credential-id"}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Build the project and run the test suite.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"},
        },
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
    input: "Build the project and run the test suite.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            LOG_LEVEL: "debug",
            API_TOKEN: { credential: "my-api-token" },
        },
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": [{"type": "text", "text": "Build the project and run the test suite."}],
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "LOG_LEVEL": "debug",
            "API_TOKEN": {"credential": "my-api-token"}
        }
    }
}'
```

متغیرها برای هر فرمانی که عامل در آن تعامل اجرا می‌کند اعمال می‌شود، ازجمله
فرمان‌های پوسته، مراحل ساخت، و هر فرایندی که شروع می‌کند.

این دو نوع مقدار رفتار متفاوتی دارند. رشته‌ای تحت‌اللفظی به‌عنوان نوشتار ساده در
ظرف نوشته می‌شود. مرجع اطلاعات اعتباری این‌گونه نیست: متغیر جای‌بان دریافت می‌کند، و پراکسی خروجی رمز واقعی را فقط در درخواست‌های خروجی به دامنه‌های مورداعتماد آن اطلاعات اعتباری جایگزین می‌کند. برای اطلاع از نحوه عملکرد آن،
[استفاده از اعتبارنامه‌ها به‌عنوان متغیرهای محیطی](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa#environment-variables)
را ببینید.

## پیکربندی شبکه

به‌طور پیش‌فرض، محیط‌ها دسترسی نامحدود به شبکه خروجی دارند. از فیلد
`network` برای محدود کردن ترافیک خروجی به دامنه‌های خاص استفاده کنید. هر قانون
`domain` را مشخص می‌کند، به‌علاوه `credential` اختیاری برای تزریق کردن رمز ذخیره‌شده
و `transform` اختیاری برای تزریق کردن سرایندها به درخواست‌های منطبق.
این سرایندها می‌توانند برای هر تعامل منحصربه‌فرد باشند و می‌توانید آن‌ها را برای محیط یکسان به‌روز کنید.

| فیلد | نوع | شرح |
| --- | --- | --- |
| `domain` | `string` | دامنه برای مطابقت. از نام میزبان دقیق یا `*` برای همه دامنه‌ها استفاده کنید. |
| `credential` | `string` | شناسه [اعتبارنامه](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره‌شده. کارگزار خروجی آن را حل می‌کند و سرایند احراز هویت را در زمان درخواست تزریق می‌کند. |
| `transform` | `object` | شیء حاوی جفت‌های مقدار-کلید مسطح که نشان‌دهنده سرایندهایی است که باید در درخواست‌های منطبق تزریق شود، برای نمونه `{"Authorization": "Bearer ..."}`. |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                {"domain": "pypi.org"},
                {"domain": "*"},
            ]
        },
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
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                { domain: "pypi.org" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_your_github_token"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build(),
                AllowlistEntry.builder().domain("*").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Fetch the latest issues from the GitHub API for my-org/my-repo."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_your_github_token",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
                {
                    Domain: "*",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Fetch the latest issues from the GitHub API for my-org/my-repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    }
                },
                {"domain": "pypi.org"},
                {"domain": "*"}
            ]
        }
    }
}'
```

وقتی فهرست مجاز تنظیم می‌شود، فقط درخواست‌های دامنه‌هایی که به‌طور صریح فهرست شده‌اند مجاز است. می‌توانید از نویسه‌های عام برای مطابقت دادن زیردامنه‌ها (مثلاً `{"domain":
"*.example.com"}`) استفاده کنید، اما توجه داشته باشید که این کار با دامنه ریشه
`example.com` مطابقت ندارد و باید جداگانه اضافه شود. برای مجاز کردن همه ترافیک‌های دیگر، مانند مسیریابی دامنه‌های فهرست‌نشده بدون سرایندهای تزریق‌شده، `{"domain": "*"}` را به‌عنوان ورودی
catch-all اضافه کنید.

### اطلاعات کاربری

دو روش برای اصالت‌سنجی ترافیک خروجی وجود دارد: اعتبارنامه ذخیره‌شده
ارجاع‌شده براساس شناسه و `transform` درون‌خطی در قانون فهرست مجازها. کارگزار خروجی هم در سیم اعمال می‌شود، بنابراین در هر دو مورد، رمز هرگز وارد
جعبه ایمنی نمی‌شود و هرگز در محموله‌های تعامل شما ظاهر نمی‌شود.

[اطلاعات اعتباری مدیریت‌شده](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) اطلاعاتی است که وقتی می‌خواهید رمز را یک‌بار ذخیره کنید و دوباره از آن استفاده کنید، باید به آن دسترسی پیدا کنید. هر محیط،
عامل، و راه‌انداز در پروژه شما می‌تواند به همان شناسه ارجاع دهد، و آن را
در یک مکان می‌چرخانید.

### Python

```
from google import genai

client = genai.Client()

# Store the secret once
client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_your_github_token",
)

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Store the secret once
await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_your_github_token",
});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
# Store the secret once
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_your_github_token"
}'

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

گواهینامه `oauth2` نیز به‌تنهایی رمز دسترسی خود را بازآوری می‌کند، بنابراین تعامل طولانی‌مدت با انقضای رمز قطع نمی‌شود. برای فهرست کامل انواع اطلاعات اعتباری و عملیات مدیریت،
[اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) را ببینید.

همچنین می‌توانید سرایندها را به‌صورت درون‌خطی با `transform` تنظیم کنید. این مورد زمانی مناسب است که مقدار
متعلق به یک تماس باشد، برای مثال، نشانه‌ای که درست قبل‌از ایجاد
تعامل تولید می‌کنید. سرایندهایی که به این روش تنظیم می‌شوند توسط همان پراکسی خروجی تزریق می‌شوند،
این سرایندها هرگز در محیط امن به‌عنوان متغیرهای محیطی یا فایل‌ها آشکار نمی‌شوند.

### Python

```
import subprocess
from google import genai

# Fetch a short-lived access token from your local gcloud CLI
gcloud_token = subprocess.check_output(
    ["gcloud", "auth", "print-access-token"], text=True
).strip()

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": f"Bearer {gcloud_token}"
                    },
                }
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import { execSync } from "child_process";

const gcloudToken = execSync("gcloud auth print-access-token").toString().trim();

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": `Bearer ${gcloudToken}`
                    },
                }
            ]
        }
    },
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

// Fetch a short-lived access token from your local gcloud CLI
Process process = new ProcessBuilder("gcloud", "auth", "print-access-token").start();
String gcloudToken = new String(process.getInputStream().readAllBytes(), StandardCharsets.UTF_8).trim();

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer " + gcloudToken
                    )))
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

```
package main

import (
    "context"
    "fmt"
    "log"
    "os/exec"
    "strings"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()

    // Fetch a short-lived access token from your local gcloud CLI
    out, err := exec.Command("gcloud", "auth", "print-access-token").Output()
    if err != nil {
        log.Fatal(err)
    }
    gcloudToken := strings.TrimSpace(string(out))

    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer " + gcloudToken,
                    })),
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer <YOUR_GCLOUD_TOKEN>"
                    }
                }
            ]
        }
    }
}'
```

‫`credential` و `transform` می‌توانند در یک قانون ظاهر شوند. ابتدا اطلاعات اعتباری اعمال می‌شود و `transform` در بالا ادغام می‌شود، بنابراین اگر هر دو کلید یکسانی را تنظیم کنند، سرصفحه `transform` صریح برنده است. الگوی رایج عبارت است از اطلاعات اعتباری برای سرایند اصالت‌سنجی به‌علاوه `transform` برای سرایندهای اضافی که سرویس
همراه با آن انتظار دارد.

### غیرفعال کردن دسترسی به شبکه

برای مسدود کردن همه دسترسی‌های شبکه خروجی، `network` را روی `disabled` تنظیم کنید:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the local files only.",
    environment={
        "type": "remote",
        "network": "disabled",
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
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
    },
});

console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.NetworkEnum;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

Environment env = Environment.builder()
    .network(Network.of(NetworkEnum.DISABLED))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the local files only."))
    .environment(CreateAgentInteractionEnvironment.of(env))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### رفتن

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
        Network: genai.Ptr(interactions.NewNetwork(interactions.NetworkEnumDisabled)),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Analyze the local files only."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### بازآوری اعتبارنامه‌ها

ژتون‌های درون‌خطی مانند ژتون‌های دسترسی و کلیدهای API کوتاه‌مدت منقضی می‌شوند.
با ارسال `environment_id` موجود به‌همراه پیکربندی `network` جدید در تعامل بعدی، می‌توانید آن‌ها را بازآوری کنید. قوانین شبکه جدید به‌طور کامل جایگزین قوانین قبلی می‌شود، درحالی‌که وضعیت سیستم فایل محیط (بسته‌های نصب‌شده، فایل‌ها، مخازن) حفظ می‌شود.

اگر به‌جای آن از [اطلاعات اعتباری](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=fa) ذخیره‌شده استفاده می‌کنید،
به این مورد نیاز ندارید. اعتبارنامه‌های `oauth2` خودشان را بازآوری می‌کنند و چرخش هر اعتبارنامه‌ای `PATCH` در اعتبارنامه است که هر قانون فهرست مجاز ارجاع‌دهنده به آن را دست‌نخورده باقی می‌گذارد.

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        },
    },
)

# Later: refresh the token on the same environment
result = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Now download the file reports/q1.csv from the same bucket.",
    environment={
        "type": "remote",
        "environment_id": first.environment_id,
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First interaction: use an initial token
const first = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        }
    },
});

// Later: refresh the token on the same environment
const result = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Now download the file reports/q1.csv from the same bucket.",
    environment: {
        type: "remote",
        environment_id: first.environment_id,
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        }
    },
});

console.log(result.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Transform;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;
import java.util.Map;

Client client = new Client();

// First interaction: use an initial token
Environment initialEnv = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer INITIAL_TOKEN"
                    )))
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction firstParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("List the files in gs://my-bucket/reports/ using the GCS JSON API."))
    .environment(CreateAgentInteractionEnvironment.of(initialEnv))
    .build();

Interaction first = client.interactions.create(CreateInteractionRequestBody.of(firstParams)).interaction().get();

// Later: refresh the token on the same environment
Environment refreshedEnv = Environment.builder()
    .environmentId(first.environmentId().orElse(""))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("storage.googleapis.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer REFRESHED_TOKEN"
                    )))
                    .build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction secondParams = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Now download the file reports/q1.csv from the same bucket."))
    .environment(CreateAgentInteractionEnvironment.of(refreshedEnv))
    .build();

Interaction result = client.interactions.create(CreateInteractionRequestBody.of(secondParams)).interaction().get();
System.out.println(result.outputText().orElse(""));
```

### رفتن

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

    // First interaction: use an initial token
    initialEnv := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer INITIAL_TOKEN",
                    })),
                },
            })),
        })),
    }

    firstRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("List the files in gs://my-bucket/reports/ using the GCS JSON API."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(initialEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    first := firstRes.Interaction

    // Later: refresh the token on the same environment
    refreshedEnv := interactions.Environment{
        EnvironmentID: first.EnvironmentID,
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "storage.googleapis.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer REFRESHED_TOKEN",
                    })),
                },
            })),
        })),
    }

    secondRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Now download the file reports/q1.csv from the same bucket."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(refreshedEnv)),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if secondRes.Interaction.OutputText != nil {
        fmt.Println(*secondRes.Interaction.OutputText)
    }
}
```

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Now download the file reports/q1.csv from the same bucket.",
    "environment": {
        "type": "remote",
        "environment_id": "<ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION>",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    }
                }
            ]
        }
    }
}'
```

## چرخه حیات محیط

محیط‌ها از این چرخه حیات پیروی می‌کنند:

| ایالت | رفتار |
| --- | --- |
| **ایجادشده** | وقتی تعاملی `environment: "remote"` یا شیء پیکربندی را مشخص می‌کند، آماده می‌شود. |
| **فعال** | درحال اجرا شدن درحالی‌که تعاملی درجریان است. |
| **Idle** | عکس فوری خودکار و پس‌از ۱۵ دقیقه عدم فعالیت متوقف شد. |
| **آفلاین** | از آخرین زمان فعال بودن به‌مدت ۷ روز نگهداری می‌شود. با ارسال شناسه آن می‌توان ازسر گرفت. |
| **حذف‌شده** | پس‌از منقضی شدن دوره نگهداری ۷ روزه «زمان زنده بودن» یا پس‌از حذف دستی، به‌طور خودکار از سیستم برداشته می‌شود. |

## Environments API

می‌توانید از «میانای برنامه‌سازی کاربردی محیط‌ها» برای مدیریت برنامه‌ریزی‌شده جلسات جعبه امن استفاده کنید.
شمردن محیط‌ها به شما امکان می‌دهد شناسه‌های جلسه فعال را پیدا کنید و اگر اتصال کارخواه درطول تکلیف طولانی‌مدت قطع شد، وضعیت را بازیابی کنید. همچنین می‌توانید
فراداده جلسه را بازرسی کنید و محیط‌ها را به‌طور صریح حذف کنید
وقتی گردش‌های کار به‌پایان می‌رسند، به‌جای اینکه منتظر انقضای خودکار TTL بمانید.

### فهرست کردن محیط‌ها

فهرست محیط‌های فعال متعلق به پروژه شما. از پارامترهای صفحه‌بندی
برای کنترل اندازه دسته‌ای پاسخ استفاده کنید.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.list(page_size=10)
for env in response.environments:
    print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ page_size: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
}
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;
import com.google.genai.gaos.models.environments.ListEnvironmentsResponse;
import java.util.List;

Client client = new Client();

ListEnvironmentsResponse response = client.environments.listEnvironments()
    .pageSize(10)
    .call()
    .listEnvironmentsResponse()
    .get();

for (Environment env : response.environments().orElse(List.of())) {
    System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
}
```

### رفتن

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

    res, err := sdk.Environments.ListEnvironments(ctx, operations.ListEnvironmentsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    if res.ListEnvironmentsResponse != nil {
        for _, env := range res.ListEnvironmentsResponse.Environments {
            fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

پاسخ شبیه به این است:

```
{
  "environments": [
    {
      "id": "140128b2a13c12c00a5a0d8cf7af9469",
      "status": "active"
    },
    {
      "id": "362b738275a1d74af6f1c62bc050da73",
      "status": "active"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### دریافت محیط

جزئیات پیکربندی و فراداده‌های محیط خاصی را براساس نام منبع آن بازیابی کنید.

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(id="YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.id}, Status: {env.status}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get("YOUR_ENVIRONMENT_ID");
console.log(`Environment ID: ${env.id}, Status: ${env.status}`);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.environments.Environment;

Client client = new Client();

Environment env = client.environments.getEnvironment("YOUR_ENVIRONMENT_ID").environment().get();
System.out.println("Environment ID: " + env.id().orElse("") + ", Status: " + env.status().orElse(null));
```

### رفتن

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

    res, err := sdk.Environments.GetEnvironment(ctx, operations.GetEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }

    env := res.Environment
    fmt.Printf("Environment ID: %s, Status: %v\n", env.ID, env.Status)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

پاسخ شبیه به این است:

```
{
  "id": "140128b2a13c12c00a5a0d8cf7af9469",
  "status": "active",
  "sources": [
    {
      "type": "repository",
      "source": "https://github.com/octocat/Spoon-Knife",
      "target": "/workspace/spoon-knife"
    }
  ],
  "network": {
    "allowlist": [
      {
        "domain": "api.github.com"
      },
      {
        "domain": "github.com"
      }
    ]
  }
}
```

### حذف محیط

وقتی کارها یا خطوط لوله شما تمام شد، محیط را به‌طور صریح خاتمه دهید و حذف کنید تا منابع جعبه ایمنی پاک‌سازی شود.

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(id="YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete("YOUR_ENVIRONMENT_ID");
```

### جاوا

```
import com.google.genai.Client;

Client client = new Client();

client.environments.deleteEnvironment("YOUR_ENVIRONMENT_ID");
```

### رفتن

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

    _, err := sdk.Environments.DeleteEnvironment(ctx, operations.DeleteEnvironmentRequest{
        ID: "YOUR_ENVIRONMENT_ID",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## مدیریت فایل‌ها در محیط

کارگزار درطول اجرا فایل‌ها را در داخل محیط امن ایجاد و اصلاح می‌کند. می‌توانید محتوای فهرست راهنما را مرور کنید، فراداده فایل را دریافت کنید، فایل‌های جداگانه یا کل فهرست‌های راهنما را به‌عنوان بایگانی‌های tar بارگیری کنید، و فایل‌ها را بارگذاری کنید یا بایگانی‌ها را مستقیماً در محیط استخراج کنید. فضای ذخیره‌سازی در محیط‌های جعبه شنی مشمول
حدود استفاده منصفانه است.

### فهرست کردن فایل‌ها در یک فهرست

محتوای دایرکتوری را در محیط فهرست کنید. به‌طور پیش‌فرض، فهرست
دایرکتوری ریشه را نشان می‌دهد.

#### پارامترهای پُرسمان

| پارامتر | نوع | شرح |
| --- | --- | --- |
| `recursive` | بولی | وقتی `true`، همه فایل‌ها و فهرستگان‌ها را به‌صورت بازگشتی فهرست می‌کند. پیش‌فرض: `false`. |

### Python

```
from google import genai

client = genai.Client()

# List root directory
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="",
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")

# List a subdirectory recursively
response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
    recursive=True,
)
for file in response.files:
    print(f"{file.name} ({file.type}) - {file.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// List root directory
const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "",
});
for (const file of response.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}

// List a subdirectory recursively
const srcResponse = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
    recursive: true,
});
for (const file of srcResponse.files) {
    console.log(`${file.name} (${file.type}) - ${file.path}`);
}
```

### REST

```
# List root directory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List a subdirectory
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src" \
  -H "x-goog-api-key: $GEMINI_API_KEY"

# List all files recursively
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

پاسخ یک آرایه `files` با فراداده برای هر ورودی برمی‌گرداند:

```
{
  "files": [
    {
      "name": "config",
      "path": "config",
      "type": "DIRECTORY",
      "created": "2026-08-12T07:44:18Z",
      "modified": "2026-08-12T07:44:18Z"
    },
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

#### فیلدهای ورودی فایل

| فیلد | نوع | شرح |
| --- | --- | --- |
| `name` | رشته | نام فایل یا دایرکتوری. |
| `path` | رشته | مسیر کامل نسبت به ریشه محیط. |
| `type` | رشته | یا `FILE` یا `DIRECTORY`. |
| `size_bytes` | رشته | اندازه فایل برحسب بایت (فقط فایل‌ها). |
| `mime_type` | رشته | نوع MIME (فقط فایل‌ها). |
| `created` | رشته | مُهر زمان ایجاد ISO 8601. |
| `modified` | رشته | مُهر زمان آخرین تغییر ISO 8601. |

### دریافت فراداده فایل

فراداده‌های فایل خاصی را براساس مسیر دریافت کنید.

### Python

```
from google import genai

client = genai.Client()

response = client.environments.files.list(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)
file = response.files[0]
print(f"Name: {file.name}, Size: {file.size_bytes} bytes, Type: {file.mime_type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.files.list({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});
const file = response.files[0];
console.log(`Name: ${file.name}, Size: ${file.size_bytes} bytes, Type: ${file.mime_type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

پاسخ فراداده فایل را که در آرایه `files` پیچیده شده است برمی‌گرداند:

```
{
  "files": [
    {
      "name": "main.py",
      "path": "src/main.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python; charset=utf-8",
      "created": "2026-08-12T07:44:20Z",
      "modified": "2026-08-12T07:44:20Z"
    }
  ]
}
```

اگر فایل وجود نداشته باشد، API خطای `404` برمی‌گرداند:

```
{
  "error": {
    "message": "Path 'nonexistent.txt' not found in environment 'ENV_ID'.",
    "code": "not_found"
  }
}
```

### بارگیری یک فایل

محتوای فایل خاصی را بارگیری کنید. در کیت‌های توسعه نرم‌افزار، از روش `download()`
استفاده کنید. در درخواست‌های REST، پارامتر پُرسمان `?alt=media` را به مسیر فایل
ضمیمه کنید. سرور با `200 OK` پاسخ می‌دهد و محتوای فایل خام را جاری‌سازی می‌کند.

### Python

```
from google import genai

client = genai.Client()

content = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src/main.py",
)

with open("main.py", "wb") as f:
    f.write(content)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src/main.py",
});

fs.writeFileSync("main.py", Buffer.from(bytes));
```

### REST

```
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src/main.py?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o main.py
```

### بارگیری کردن پوشه به‌عنوان بایگانی tar

با درخواست مسیر دایرکتوری با `?alt=media`، کل دایرکتوری را به‌عنوان بایگانی tar بارگیری کنید. این کار فایل tar ‏POSIX (بدون فشرده‌سازی با gzip) برمی‌گرداند. برای افزودن زیرپوشه‌های تودرتو، از
`recursive=true` استفاده کنید.

### Python

```
import tarfile
from google import genai

client = genai.Client()

# Download a subdirectory archive
archive = client.environments.files.download(
    environment="YOUR_ENVIRONMENT_ID",
    path="src",
)

with open("src.tar", "wb") as f:
    f.write(archive)

with tarfile.open("src.tar") as tar:
    tar.extractall(path="./extracted")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

// Download a subdirectory archive
const bytes = await client.environments.files.download({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "src",
});

fs.writeFileSync("src.tar", Buffer.from(bytes));
execSync("tar -xf src.tar -C ./extracted");
```

### REST

```
# Download a subdirectory (top-level files only)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/src?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o src.tar

# Download a subdirectory recursively (includes nested directories)
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files/config?alt=media&recursive=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o config.tar

# Download root directory
curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -o snapshot.tar

# Extract the archive
tar xf snapshot.tar -C ./extracted
```

#### ماتریس رفتار

ماتریس رفتار زیر رفتار بایگانی و پاسخ موردانتظار را در سراسر نقطه‌های پایانی فایل و دایرکتوری، روش‌های HTTP، و پارامترهای پُرسمان خلاصه می‌کند:

| درخواست | `alt` | `recursive` | `extract` | `overwrite` | پاسخ |
| --- | --- | --- | --- | --- | --- |
| `GET /files` | (هیچ‌کدام) | (هیچ‌کدام) | - | - | فهرست JSON دایرکتوری ریشه |
| ‫`GET /files/{path}` (فایل) | (هیچ‌کدام) | - | - | - | فراداده JSON برای فایل |
| ‫`GET /files/{path}` (dir) | (هیچ‌کدام) | `false` | - | - | فهرست JSON از فرزندان بی‌واسطه |
| ‫`GET /files/{path}` (dir) | (هیچ‌کدام) | `true` | - | - | فهرست JSON همه نوادگان |
| ‫`GET /files/{path}?alt=media` (فایل) | `media` | - | - | - | محتوای فایل Raw |
| ‫`GET /files/{path}?alt=media` (dir) | `media` | `false` | - | - | بایگانی tar از فایل‌های فوری در دایرکتوری |
| ‫`GET /files/{path}?alt=media` (dir) | `media` | `true` | - | - | بایگانی Tar همه فایل‌ها به‌صورت بازگشتی |
| `GET /files?alt=media` | `media` | `false` | - | - | بایگانی tar فقط از فایل‌های سطح ریشه |
| ‫`PUT /files/{path}` (فایل) | - | - | `false` | `false` | فایل را در مسیر می‌نویسد. اگر ازقبل وجود داشته باشد، `409 Conflict` را برمی‌گرداند |
| `PUT /files/{path}?overwrite=true` | - | - | `false` | `true` | فایل را در مسیر می‌نویسد یا رونویسی می‌کند |
| `PUT /files/{path}?extract=true` | - | - | `true` | `false` | بایگانی را در دایرکتوری مقصد ازهم باز می‌کند. اگر فایل هدفی وجود داشته باشد، `409 Conflict` را برمی‌گرداند |
| `PUT /files/{path}?extract=true&overwrite=true` | - | - | `true` | `true` | بایگانی را ازهم باز می‌کند و فایل‌های موجود را جایگزین می‌کند |

### بارگذاری فایل‌ها در محیط

فایل‌های تکی یا بایگانی‌های دایرکتوری را مستقیماً در محیط
جعبه ایمنی موجود بااستفاده از HTTP `PUT` بارگذاری کنید. اگر دایرکتوری‌های والد وجود نداشته باشند، به‌طور خودکار ایجاد می‌شوند. فضای ذخیره‌سازی در محیط‌ها مشمول حدود استفاده منصفانه است.

#### بارگذاری یک فایل

### Python

```
from google import genai

client = genai.Client()

with open("local_file.txt", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/data/file.txt",
        file=f,
        mime_type="text/plain",
        overwrite=True,
    )

file = result.files[0]
print(f"Uploaded: {file.name} ({file.size_bytes} bytes)")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const content = fs.readFileSync("local_file.txt");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/data/file.txt",
    file: content,
    mime_type: "text/plain",
    overwrite: true,
});

const file = result.files[0];
console.log(`Uploaded: ${file.name} (${file.size_bytes} bytes)`);
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/file.txt" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: text/plain" \
  --data-binary @local_file.txt
```

پاسخ فراداده‌های فایل بارگذاری‌شده را برمی‌گرداند که در یک `files` آرایه
برای یکپارچگی با فهرست و دریافت نقطه‌های پایانی پیچیده شده است:

```
{
  "files": [
    {
      "name": "file.txt",
      "path": "workspace/data/file.txt",
      "type": "FILE",
      "size_bytes": "1024",
      "mime_type": "text/plain"
    }
  ]
}
```

#### بارگذاری و استخراج بایگانی دایرکتوری

برای قرار دادن کل پایگاه کد یا ساختار دایرکتوری در یک درخواست، بایگانی
`.tar` یا `.tar.gz` با `extract=true` بارگذاری کنید.

### Python

```
from google import genai

client = genai.Client()

with open("source.tar.gz", "rb") as f:
    result = client.environments.files.upload(
        environment="YOUR_ENVIRONMENT_ID",
        path="workspace/src/",
        file=f,
        extract=True,
    )

for entry in result.files:
    print(f"Extracted: {entry.path}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "fs";

const client = new GoogleGenAI({});

const archive = fs.readFileSync("source.tar.gz");
const result = await client.environments.files.upload({
    environment: "YOUR_ENVIRONMENT_ID",
    path: "workspace/src/",
    file: archive,
    extract: true,
});

for (const entry of result.files) {
    console.log(`Extracted: ${entry.path}`);
}
```

### REST

```
curl -X PUT "https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/src/?extract=true" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/x-tar" \
  --data-binary @source.tar.gz
```

پاسخ فهرستی از همه فایل‌های نوشته‌شده توسط بایگانی را ارائه می‌دهد:

```
{
  "files": [
    {
      "name": "app.py",
      "path": "workspace/src/app.py",
      "type": "FILE",
      "size_bytes": "15",
      "mime_type": "text/x-python"
    },
    {
      "name": "requirements.txt",
      "path": "workspace/src/requirements.txt",
      "type": "FILE",
      "size_bytes": "17",
      "mime_type": "text/plain"
    }
  ]
}
```

#### بارگذاری فایل‌های بزرگ با جلسه ازسرگیری‌پذیر

برای پیام‌واره‌های بزرگ، یا هنگام بارگذاری ازطریق اتصال غیرقابل‌اعتماد، به‌جای ارسال کل بدنه در یک درخواست، از
جلسه ازسرگیری استفاده کنید. بارگذاری
ازسرگیری‌پذیر انتقال را به بخش‌هایی تقسیم می‌کند که می‌توان آن‌ها را به‌صورت جداگانه دوباره امتحان کرد، بنابراین
اگر در حین انتقال مشکلی پیش بیاید، مجبور نیستید از ابتدا شروع کنید.

با شروع جلسه با `uploadType=resumable` شروع کنید. بدنه خالی ارسال کنید
و از سرایندهای `X-Upload-Content-Type` و `X-Upload-Content-Length` برای
اعلام نوع رسانه و اندازه کل داده‌برداری که قصد دارید بارگذاری کنید استفاده کنید:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable HTTP/1.1
Host: generativelanguage.googleapis.com
X-Upload-Content-Type: application/octet-stream
X-Upload-Content-Length: 20971520
Content-Length: 0
x-goog-api-key: $GEMINI_API_KEY
```

پاسخ نشانی وب جلسه را در سرصفحه `Location` حمل می‌کند. این نشانی وب ازقبل
دارای `upload_id` است، بنابراین نیازی به کلید میانای برنامه‌سازی کاربردی دوباره ندارد:

```
HTTP/1.1 200 OK
Location: https://generativelanguage.googleapis.com/upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY
Content-Length: 0
```

بار محموله را به‌صورت تکه‌ای در آن نشانی وب بارگذاری کنید. هر تکه محدوده بایت و اندازه کل را با سرایند `Content-Range` اعلام می‌کند:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 0-10485759/20971520
Content-Length: 10485760

<10 MB binary payload>
```

هر بخش به‌جز بخش آخر `308 Resume Incomplete` را برمی‌گرداند. سرصفحه `Range` به شما می‌گوید که سرور چند بایت را متعهد کرده است، که درصورت ناموفق بودن یک تکه، از همان‌جا ازسر می‌گیرید:

```
HTTP/1.1 308 Resume Incomplete
Range: bytes=0-10485759
Content-Length: 0
```

بخش‌های باقی‌مانده را به همین روش ارسال کنید:

```
PUT /upload/v1beta/environments/$ENV_ID/files/workspace/data/large_dataset.bin?uploadType=resumable&upload_id=AJjja9bfHjiYlGi60pUazCaTuPY HTTP/1.1
Host: generativelanguage.googleapis.com
Content-Type: application/octet-stream
Content-Range: bytes 10485760-20971519/20971520
Content-Length: 10485760

<remaining 10 MB binary payload>
```

تکه نهایی بارگذاری را تکمیل می‌کند و فراداده فایل را در همان
`files` پاکت بارگذاری تک‌ضرب برمی‌گرداند:

```
{
  "files": [
    {
      "name": "large_dataset.bin",
      "path": "workspace/data/large_dataset.bin",
      "type": "FILE",
      "size_bytes": "20971520",
      "mime_type": "application/octet-stream"
    }
  ]
}
```

جلسه‌های ازسرگیری‌پذیر با `extract` و `overwrite` نیز کار می‌کند. آن پارامترهای پُرسمان را در درخواست آغازگر تنظیم کنید، نه در تکه‌های جداگانه.

#### محافظت دربرابر رونویسی

به‌طور پیش‌فرض، `overwrite` روی `false` تنظیم شده است. اگر مسیر مقصد ازقبل وجود داشته باشد،
درخواست با خطای `409 Conflict` مواجه می‌شود و چیزی نوشته نمی‌شود:

```
{
  "error": {
    "message": "Requested entity already exists",
    "code": "aborted"
  }
}
```

برای جایگزین کردن فایل یا دایرکتوری موجود، `overwrite=true` را تنظیم کنید (یا `?overwrite=true` را در REST پیوست کنید). با `extract=true`، بررسی تعارض برای
هر فایل در بایگانی اعمال می‌شود، بنابراین اگر هر فایل هدفی وجود داشته باشد، درخواست ناموفق خواهد بود.

### بارگیری عکس آنی کامل (منسوخ)

برای انتقال کد موجود به «میانای برنامه‌سازی کاربردی فایل‌های محیطی»:

- **Python**: درخواست‌های بارگیری فایل قدیمی را با این جایگزین کنید:

  ```
  archive = client.environments.files.download(
      environment="YOUR_ENVIRONMENT_ID",
      path="workspace",
  )
  with open("snapshot.tar", "wb") as f:
      f.write(archive)
  ```
- **JavaScript**: درخواست‌های بارگیری فایل قدیمی را با این موارد جایگزین کنید:

  ```
  const bytes = await client.environments.files.download({
      environment: "YOUR_ENVIRONMENT_ID",
      path: "workspace",
  });
  fs.writeFileSync("snapshot.tar", Buffer.from(bytes));
  ```
- **REST**: جایگزین کردن `GET /v1beta/files/environment-$ENV_ID:download?alt=media` با:

  ```
  curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/environments/$ENV_ID/files?alt=media" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -o snapshot.tar
  ```

## قیمت‌گذاری و منابع

هر محیط با تخصیص منابع ثابت اجرا می‌شود:

| منبع | مقدار |
| --- | --- |
| **CPU** | ‫۴ هسته |
| **حافظه** | ‫۱۶ گیگابایت |

محاسبه محیط (CPU، حافظه، اجرای sandbox) درطول دوره پیش‌نمایش **صورت‌حساب نمی‌شود**. برای هزینه‌های
رمز عامل،
[قیمت‌گذاری](https://ai.google.dev/gemini-api/docs/pricing?hl=fa#pricing-for-agents) را ببینید.

## محدودیت‌ها

- **وضعیت پیش‌نمایش:** محیط‌ها و عامل‌های مدیریت‌شده در پیش‌نمایش هستند. ویژگی‌ها و طرحواره‌ها ممکن است تغییر کنند.
- **اندازه منبع درون‌خطی:** منابع درون‌خطی به ۱ مگابایت در هر فایل و در مجموع ۲ مگابایت در همه فایل‌ها محدود می‌شوند.
- **اندازه منبع**: مخازن Git به ۵۰۰ مگابایت و مخازن Cloud Storage به ۲ گیگابایت محدود می‌شوند.
- **راه‌اندازی محیط:** آماده‌سازی محیط جدید تا ۵ ثانیه طول می‌کشد. مخازن منبع بزرگ ممکن است این زمان را افزایش دهند.
- **انقضای محیط:** محیط‌های آفلاین غیرفعال به‌مدت ۷ روز نگهداری می‌شوند و سپس بااستفاده از پاک‌سازی خودکار TTL منقضی می‌شوند. ارسال شناسه محیط منقضی یا
  نامعتبر خطای `404 Not Found` را برمی‌گرداند.
- **پشتیبانی از فایل:** درحال‌حاضر، کارگزار به خواندن فایل‌های نوشتاری و تصویری محدود شده است. پشتیبانی از فایل باینری هنوز دردسترس نیست.
- **بدون نصب از ریشه:** هنگام افزودن منبع سفارشی نمی‌توانید ریشه (`/`) را به‌عنوان هدف تنظیم کنید، همیشه باید زیرشاخه را مشخص کنید.

## قدم بعدی چیست

- [نمای کلی عامل‌ها](https://ai.google.dev/gemini-api/docs/agents?hl=fa): با مفاهیم اصلی عامل‌های مدیریت‌شده آشنا شوید.
- [شروع سریع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fa): با مکالمه‌های چند نوبتی و جاری‌سازی شروع به ساختن کنید.
- [عامل ضدجاذبه](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fa): توانمندی‌ها، ابزارها، انتخاب مدل، و قیمت‌گذاری عامل پیش‌فرض را کاوش کنید.
- [ساختن عامل‌های سفارشی](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fa): بااستفاده از `AGENTS.md` و `SKILL.md`، عامل‌های خودتان را تعریف کنید.
- [قلاب‌ها](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fa): نرده‌های محافظ امنیتی را اعمال کنید و اعتبارسنجی‌های اثر جانبی را در محیط امن اجرا کنید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی."],[],[]]
