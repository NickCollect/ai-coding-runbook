---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi
fetched_at: 2026-11-02T07:28:13.234521+00:00
title: "T\u1ea1o t\u00e1c nh\u00e2n \u0111\u01b0\u1ee3c qu\u1ea3n l\u00fd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hiện đã ra mắt. [Hãy dùng thử](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=vi).

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo tác nhân được quản lý

Tác nhân được quản lý trên Gemini API cho phép bạn mở rộng tác nhân Antigravity bằng các chỉ dẫn, kỹ năng và dữ liệu của riêng bạn. Bạn có thể [tuỳ chỉnh tác nhân cùng dòng](#customize-inline) tại thời điểm tương tác hoặc [lưu cấu hình](#save-agent) dưới dạng tác nhân được quản lý mà bạn gọi theo mã nhận dạng.

## Tuỳ chỉnh tác nhân Antigravity

Cách nhanh nhất để tạo một tác nhân tuỳ chỉnh là truyền cấu hình của bạn cùng dòng trong khi tạo một lượt tương tác mới mà không cần bước đăng ký. Bạn có thể mở rộng tác nhân theo một số cách chính:

- **[Lựa chọn mô hình](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#model-selection)**: Chọn mô hình Gemini cơ bản thông qua `agent_config` (mặc định là **Gemini 3.8 Flash**).
- **Chỉ dẫn hệ thống**: Truyền văn bản cùng dòng qua `system_instruction` để định hình hành vi.
- **Công cụ**: Ghi đè các công cụ mặc định (Thực thi mã, Tìm kiếm, Bối cảnh từ URL), đăng ký máy chủ MCP từ xa hoặc xác định các hàm tuỳ chỉnh (Gọi hàm).
- **Tệp và kỹ năng**: Gắn các tệp như `AGENTS.md` và `SKILL.md` vào môi trường.

Dưới đây là ví dụ về cách truyền cả ba tham số cùng dòng:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
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
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

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
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a slide deck."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Analyze the Q1 revenue data and create a slide deck."),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

Mọi thứ đều được xác định tại thời điểm tương tác. Bạn không cần phải đăng ký trước. Khung vận hành tác nhân Antigravity cung cấp môi trường thời gian chạy (thực thi mã, quản lý tệp, truy cập web) và các lớp cấu hình của bạn ở trên cùng.

### Công cụ và chỉ dẫn hệ thống

Bạn có thể tuỳ chỉnh hành vi và chức năng của tác nhân cho một lượt tương tác cụ thể bằng cách sử dụng các tham số `system_instruction` và `tools`.

- **Chỉ dẫn hệ thống**: Sử dụng tham số `system_instruction` để truyền văn bản cùng dòng định hình hành vi của tác nhân. Tính năng này phù hợp cho những điều chỉnh nhanh mà bạn muốn thực hiện cho mỗi cuộc gọi. `system_instruction` và `AGENTS.md` có tính chất bổ sung; cả hai đều áp dụng khi có mặt.
- **Công cụ**: Theo mặc định, tác nhân Antigravity có quyền truy cập vào `code_execution`, `google_search` và `url_context`. Bạn có thể ghi đè danh sách này bằng cách truyền tham số `tools` tại thời điểm tương tác. Bạn cũng có thể đăng ký [máy chủ MCP từ xa](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#mcp-servers) hoặc xác định [hàm tuỳ chỉnh (gọi hàm)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#function-calling) để kết nối tác nhân với API và cơ sở dữ liệu của riêng bạn. Để biết thông tin chi tiết đầy đủ về các công cụ hiện có, hãy xem bài viết [Tác nhân Antigravity: Các công cụ được hỗ trợ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#supported-tools).

### Tuỳ chỉnh dựa trên tệp

#### Cấu trúc thư mục của tác nhân

Mặc dù bạn có thể truyền cấu hình cùng dòng, nhưng bạn nên sắp xếp các tệp của tác nhân trong một thư mục có cấu trúc. Điều này giúp bạn dễ dàng quản lý, quản lý phiên bản và gắn vào môi trường của tác nhân.

Thư mục dự án tác nhân thông thường sẽ có dạng như sau:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Môi trường thời gian chạy Antigravity quét `.agents/` (và thư mục gốc của môi trường) để tìm các tệp này.

#### AGENTS.md

Tác nhân tự động tải `.agents/AGENTS.md` (hoặc `/.agents/AGENTS.md`) từ môi trường dưới dạng chỉ dẫn hệ thống khi khởi động. Sử dụng `AGENTS.md` cho các định nghĩa dài về vai trò, nguyên tắc chi tiết và hướng dẫn mà bạn muốn quản lý phiên bản cùng với mã của mình.

Gắn `AGENTS.md` bằng nguồn cùng dòng:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
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
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

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
            .type(SourceType.INLINE)
            .target(".agents/AGENTS.md")
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Analyze the Q1 revenue data and create a report."))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .environment(CreateAgentInteractionEnvironment.of(env))
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/AGENTS.md"),
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Analyze the Q1 revenue data and create a report."),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### Kỹ năng: SKILL.md

Kỹ năng là các tệp giúp mở rộng khả năng của tác nhân. Hãy đặt các tệp này trong `.agents/skills/<skill-name>/SKILL.md` và bộ kiểm thử sẽ tự động khám phá và đăng ký các tệp này.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Gắn kỹ năng bằng nguồn cùng dòng:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
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
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### Java

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
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html")
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Create a presentation about our Q1 results."))
    .systemInstruction("You create presentations from data.")
    .environment(CreateAgentInteractionEnvironment.of(env))
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

    env := interactions.Environment{
        Sources: []interactions.Source{
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"),
            },
        },
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:             interactions.AgentOption("antigravity-preview-09-2026"),
            Input:             interactions.NewInteractionsInput("Create a presentation about our Q1 results."),
            SystemInstruction: genai.Ptr("You create presentations from data."),
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(env)),
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
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

Các kỹ năng được tải từ `.agents/skills/` và `/.agents/skills/` đều được tự động phát hiện.

## Tạo tác nhân được quản lý

Sau khi lặp lại cấu hình, bạn có thể tạo cấu hình đó dưới dạng tác nhân được quản lý bằng `agents.create`. Nhờ đó, bạn có thể gọi tác nhân theo mã nhận dạng mà không cần lặp lại cấu hình mỗi lần.

`id` mà bạn chỉ định khi tạo tác nhân được quản lý phải là duy nhất cho dự án của bạn và không được bắt đầu bằng các tiền tố dành riêng (ví dụ: `google-`, `gemini-`). Hãy xem phần [Các quy định hạn chế về mã tác nhân](#agent-id-restrictions) để biết danh sách đầy đủ các tiền tố bị hạn chế.

### Từ các nguồn

Chỉ định `base_agent`, `id`, `agent_config`, `system_instruction` và `base_environment` bằng nguồn. Nền tảng này cung cấp một hộp cát mới có các tệp của bạn trong mỗi lần gọi. Hãy xem phần [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi) để biết các loại nguồn có sẵn (Git, GCS, cùng dòng).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-09-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.8-flash",
    },
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-09-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.8-flash",
    },
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
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
            .content("Always use matplotlib for charts. Include a summary table in every report.")
            .build(),
        Source.builder()
            .type(SourceType.INLINE)
            .target(".agents/skills/slide-maker/SKILL.md")
            .content("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.")
            .build(),
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/analysis-templates")
            .target("/workspace/templates")
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .agentConfig(AgentConfig.of(
        AntigravityAgentConfig.builder()
            .model("gemini-3.8-flash")
            .build()
    ))
    .systemInstruction("You are a data analyst. Always include visualizations and export results as PDF.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created agent: " + agent.id().orElse(""));
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
                Content: genai.Ptr("Always use matplotlib for charts. Include a summary table in every report."),
            },
            {
                Type:    interactions.SourceTypeInline.ToPointer(),
                Target:  genai.Ptr(".agents/skills/slide-maker/SKILL.md"),
                Content: genai.Ptr("---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."),
            },
            {
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/my-org/analysis-templates"),
                Target: genai.Ptr("/workspace/templates"),
            },
        },
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:        genai.Ptr("data-analyst"),
            BaseAgent: genai.Ptr("antigravity-preview-09-2026"),
            AgentConfig: genai.Ptr(agents.NewAgentConfig(interactions.AntigravityAgentConfig{
                Model: genai.Ptr("gemini-3.8-flash"),
            })),
            SystemInstruction: genai.Ptr("You are a data analyst. Always include visualizations and export results as PDF."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created agent: %s\n", *res.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-09-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.8-flash"
    },
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### Từ một môi trường hiện có (phân nhánh)

Lặp lại với tác nhân Antigravity cơ sở cho đến khi môi trường phù hợp (các gói đã được cài đặt, tệp đã được đặt đúng chỗ), sau đó phân nhánh thành một tác nhân được quản lý.

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-09-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-09-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

// Step 1: set up the environment interactively
CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("antigravity-preview-09-2026"))
    .input(InteractionsInput.of("Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py."))
    .environment(CreateAgentInteractionEnvironment.of("remote"))
    .build();

Interaction interaction = client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

// Step 2: fork that environment into a managed agent
Agent agentParams = Agent.builder()
    .id("my-data-analyst")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You are a data analyst. Use the template at /workspace/template.py for all reports.")
    .baseEnvironment(BaseEnvironment.of(interaction.environmentId().orElse("")))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Forked agent successfully: " + agent.id().orElse(""));
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

    // Step 1: set up the environment interactively
    intRes, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("antigravity-preview-09-2026"),
            Input:       interactions.NewInteractionsInput("Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    interaction := intRes.Interaction

    // Step 2: fork that environment into a managed agent
    agentRes, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:                genai.Ptr("my-data-analyst"),
            BaseAgent:         genai.Ptr("antigravity-preview-09-2026"),
            SystemInstruction: genai.Ptr("You are a data analyst. Use the template at /workspace/template.py for all reports."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(*interaction.EnvironmentID)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Forked agent successfully: %s\n", *agentRes.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-09-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### Có quy tắc mạng

Bạn có thể khoá quyền truy cập ra bên ngoài hoặc chèn thông tin đăng nhập khi lưu một tác nhân được quản lý. Để biết giản đồ danh sách cho phép, mẫu thông tin xác thực và ký tự đại diện đầy đủ, hãy xem bài viết [Môi trường: Cấu hình mạng](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#network-configuration).

Tham chiếu đến một [thông tin xác thực](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) được lưu trữ theo mã nhận dạng trong quy tắc danh sách cho phép (`"credential": "github-production"`) và proxy đầu ra sẽ chèn thông tin bí mật tại thời điểm yêu cầu, vì vậy, thông tin này sẽ không bao giờ xuất hiện trong định nghĩa tác nhân của bạn. Ví dụ này đặt tiêu đề cùng dòng với `transform`. Proxy áp dụng cả hai biểu mẫu theo cùng một cách, thông tin xác thực còn cho phép bạn sử dụng lại khoá bí mật trên các tác nhân và xoay vòng khoá bí mật ở một nơi.

Ví dụ sau đây tạo một tác nhân `issue-resolver` chỉ có thể truy cập vào GitHub và PyPI, với thông tin xác thực được chèn cho GitHub:

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-09-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-09-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import com.google.genai.gaos.models.agents.BaseEnvironment;
import com.google.genai.gaos.models.interactions.Allowlist;
import com.google.genai.gaos.models.interactions.AllowlistEntry;
import com.google.genai.gaos.models.interactions.Environment;
import com.google.genai.gaos.models.interactions.EnvironmentNetworkEgressAllowlist;
import com.google.genai.gaos.models.interactions.Network;
import com.google.genai.gaos.models.interactions.Source;
import com.google.genai.gaos.models.interactions.SourceType;
import com.google.genai.gaos.models.interactions.Transform;
import java.util.List;
import java.util.Map;

Client client = new Client();

Environment env = Environment.builder()
    .sources(List.of(
        Source.builder()
            .type(SourceType.REPOSITORY)
            .source("https://github.com/my-org/backend")
            .target("/workspace/repo")
            .build()
    ))
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Basic YOUR_BASE64_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            )))
            .build()
    ))
    .build();

Agent agentParams = Agent.builder()
    .id("issue-resolver")
    .baseAgent("antigravity-preview-09-2026")
    .systemInstruction("You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.")
    .baseEnvironment(BaseEnvironment.of(env))
    .build();

Agent agent = client.agents.create(agentParams).agent().get();
System.out.println("Created issue-resolver agent successfully: " + agent.id().orElse(""));
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
                Type:   interactions.SourceTypeRepository.ToPointer(),
                Source: genai.Ptr("https://github.com/my-org/backend"),
                Target: genai.Ptr("/workspace/repo"),
            },
        },
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Basic YOUR_BASE64_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            })),
        })),
    }

    res, err := client.Agents.Create(ctx, operations.CreateAgentRequest{
        Body: agents.Agent{
            ID:                genai.Ptr("issue-resolver"),
            BaseAgent:         genai.Ptr("antigravity-preview-09-2026"),
            SystemInstruction: genai.Ptr("You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR."),
            BaseEnvironment:   genai.Ptr(agents.NewBaseEnvironment(env)),
        },
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created issue-resolver agent successfully: %s\n", *res.Agent.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-09-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Gọi tác nhân

Gọi cho nhân viên hỗ trợ được quản lý bằng mã nhân viên hỗ trợ của bạn bằng cách tạo một lượt tương tác mới. Mỗi lệnh gọi sẽ phân nhánh môi trường cơ sở, vì vậy, mỗi lần chạy đều bắt đầu từ đầu.

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

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
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck."))
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
            Agent:       interactions.AgentOption("data-analyst"),
            Input:       interactions.NewInteractionsInput("Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck."),
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
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

Để biết thông tin về cuộc trò chuyện nhiều lượt và truyền trực tuyến, hãy xem phần [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi). Các mẫu `previous_interaction_id` và `environment` tương tự cũng áp dụng cho các tác nhân được quản lý.

Tác nhân được quản lý cũng hỗ trợ việc thực thi và huỷ trong nền. Để biết thông tin chi tiết và ví dụ về mã, hãy xem bài viết [Tác nhân Antigravity: Thực thi trong nền](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#background-execution).

## Ghi đè cấu hình khi gọi

Bạn có thể ghi đè cấu hình mạng `system_instruction`, `tools` và `environment` mặc định của nhân viên hỗ trợ khi tạo một lượt tương tác. Điều này cho phép bạn sửa đổi hành vi, chức năng hoặc thông tin xác thực của tác nhân cho một lần chạy cụ thể mà không cần thay đổi định nghĩa tác nhân được lưu trữ.

### Ghi đè chỉ dẫn và công cụ hệ thống

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.AgentOption;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CreateAgentInteraction;
import com.google.genai.gaos.models.interactions.CreateAgentInteractionEnvironment;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.List;

Client client = new Client();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("data-analyst"))
    .input(InteractionsInput.of("Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table."))
    .systemInstruction("You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.")
    .tools(List.of(CodeExecution.builder().build())) // Override to only use code execution
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
            Agent:             interactions.AgentOption("data-analyst"),
            Input:             interactions.NewInteractionsInput("Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table."),
            SystemInstruction: genai.Ptr("You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides."),
            Tools:             []interactions.Tool{interactions.NewTool(interactions.CodeExecution{})}, // Override to only use code execution
            Environment:       genai.Ptr(interactions.NewCreateAgentInteractionEnvironment("remote")),
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
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

### Ghi đè cấu hình mạng (làm mới thông tin xác thực)

Nếu tác nhân được quản lý của bạn có thông tin xác thực mạng được tích hợp vào `base_environment`,
bạn có thể ghi đè thông tin xác thực đó tại thời điểm gọi để làm mới mã thông báo đã hết hạn hoặc xoay vòng khoá
API. Truyền một đối tượng `environment` có cấu hình `network` mới. Các quy tắc mạng mới sẽ thay thế hoàn toàn các quy tắc trước đó cho lượt tương tác đó. Các nguồn (tệp, kho lưu trữ) của môi trường cơ sở được giữ nguyên.

Nếu `base_environment` tham chiếu đến một [thông tin xác thực](https://ai.google.dev/gemini-api/docs/agent-credentials?hl=vi) được lưu trữ thay vì mã thông báo cùng dòng, thì bạn không cần ghi đè bất cứ thông tin nào. Xoay vòng thông tin xác thực bằng `PATCH` và mọi tác nhân tham chiếu đến thông tin xác thực đó sẽ nhận được khoá bí mật mới trong lần chạy tiếp theo.

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### Java

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

// Invoke the agent with a fresh token, overriding the base_environment credentials
Environment env = Environment.builder()
    .network(Network.of(
        EnvironmentNetworkEgressAllowlist.builder()
            .allowlist(Allowlist.of(List.of(
                AllowlistEntry.builder()
                    .domain("api.github.com")
                    .transform(Transform.of(Map.of(
                        "Authorization", "Bearer ghp_REFRESHED_TOKEN"
                    )))
                    .build(),
                AllowlistEntry.builder().domain("pypi.org").build()
            )))
            .build()
    ))
    .build();

CreateAgentInteraction params = CreateAgentInteraction.builder()
    .agent(AgentOption.of("issue-resolver"))
    .input(InteractionsInput.of("Fix issue #42 and open a PR."))
    .environment(CreateAgentInteractionEnvironment.of(env))
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

    // Invoke the agent with a fresh token, overriding the base_environment credentials
    env := interactions.Environment{
        Network: genai.Ptr(interactions.NewNetwork(interactions.EnvironmentNetworkEgressAllowlist{
            Allowlist: genai.Ptr(interactions.NewAllowlist([]interactions.AllowlistEntry{
                {
                    Domain: "api.github.com",
                    Transform: genai.Ptr(interactions.NewTransform(map[string]string{
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN",
                    })),
                },
                {
                    Domain: "pypi.org",
                },
            })),
        })),
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent:       interactions.AgentOption("issue-resolver"),
            Input:       interactions.NewInteractionsInput("Fix issue #42 and open a PR."),
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
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Quản lý nhân viên hỗ trợ

Bạn có thể liệt kê, lấy và xoá tác nhân.

### Liệt kê tác nhân

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;
import java.util.List;

Client client = new Client();

List<Agent> agents = client.agents.listDirect().agentListResponse().get().agents().orElse(List.of());
for (Agent a : agents) {
    System.out.println(a.id().orElse("") + ": " + a.description().orElse(""));
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
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Agents.List(ctx, operations.ListAgentsRequest{})
    if err != nil {
        log.Fatal(err)
    }

    if res.AgentListResponse != nil {
        for _, a := range res.AgentListResponse.Agents {
            fmt.Printf("%s: %v\n", *a.ID, a.Description)
        }
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Nhận một tác nhân

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.agents.Agent;

Client client = new Client();

Agent agent = client.agents.get("data-analyst").agent().get();
System.out.println(agent);
```

### Go

```
package main

import (
    "context"
    "fmt"
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

    res, err := client.Agents.Get(ctx, operations.GetAgentRequest{
        ID: "data-analyst",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("%+v\n", res.Agent)
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Xoá nhân viên hỗ trợ

Thao tác xoá sẽ xoá cấu hình. Môi trường và hoạt động tương tác hiện có do nhân viên hỗ trợ tạo sẽ không bị ảnh hưởng.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### Java

```
import com.google.genai.Client;

Client client = new Client();

client.agents.delete("data-analyst");
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

    _, err = client.Agents.Delete(ctx, operations.DeleteAgentRequest{
        ID: "data-analyst",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Tài liệu tham khảo về định nghĩa tác nhân

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `id` | chuỗi | Có | Giá trị nhận dạng riêng biệt của tác nhân trong dự án trên đám mây của Google. Dùng để gọi tác nhân. Không được sử dụng tiền tố dành riêng. Xem [Các quy định hạn chế về mã nhận dạng nhân viên hỗ trợ](#agent-id-restrictions). |
| `description` | chuỗi | Không | Nội dung mô tả về tác nhân mà con người có thể đọc được. |
| `base_agent` | chuỗi | Có | Mã tác nhân cơ sở (ví dụ: `antigravity-preview-09-2026`). |
| `agent_config` | đối tượng | Không | Cấu hình cho tác nhân cơ sở, bao gồm cả lựa chọn mô hình (`{"type": "antigravity", "model": "gemini-3.8-flash"}`). Giá trị mặc định là `gemini-3.8-flash` nếu bạn bỏ qua. Không thể ghi đè tại thời điểm tương tác đối với các nhân viên hỗ trợ có tên. |
| `system_instruction` | chuỗi | Không | Câu lệnh hệ thống xác định hành vi và tính cách. |
| `tools` | mảng | Không | Các công cụ mà tác nhân có thể sử dụng. Nếu bạn bỏ qua, giá trị mặc định sẽ là `code_execution`, `google_search` và `url_context`. Các công cụ được hỗ trợ bao gồm `code_execution`, `google_search`, `url_context`, `mcp_server` và các định nghĩa `function` tuỳ chỉnh. |
| `base_environment` | chuỗi hoặc đối tượng | Không | `"remote"`, `environment_id` hoặc đối tượng cấu hình có `sources` và `network`. Xem phần Môi trường. |

### Các hạn chế về mã nhân viên hỗ trợ

Khi tạo một tác nhân được quản lý, `id` mà bạn chỉ định phải tuân theo các quy tắc sau:

- Giá trị này phải là duy nhất cho dự án trên đám mây của bạn trên Google Cloud.
- Tên này **không** được bắt đầu bằng bất kỳ tiền tố dành riêng nào sau đây (không phân biệt chữ hoa chữ thường), nếu không thì quá trình tạo sẽ không thành công:
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## Quy trình lặp lại

1. **Tạo nguyên mẫu** bằng tác nhân Antigravity cơ bản. Truyền chỉ dẫn hệ thống và nguồn môi trường cùng dòng. Kiểm tra hướng dẫn, kỹ năng và cách thiết lập môi trường một cách tương tác.
2. **Ổn định** môi trường. Cài đặt gói, gắn nguồn, xác minh mọi thứ đều hoạt động.
3. **Tiếp tục** làm tác nhân được quản lý bằng cách tạo một tác nhân mới, từ các nguồn hoặc bằng cách phân nhánh môi trường.
4. **Cập nhật** định nghĩa về tác nhân. Thay đổi chỉ dẫn hệ thống, hoán đổi kỹ năng hoặc thêm nguồn. Lần gọi tiếp theo sẽ áp dụng cấu hình mới.

## Các điểm hạn chế

- **Trạng thái xem trước**: Tác nhân được quản lý đang ở giai đoạn xem trước. Các tính năng và giản đồ có thể thay đổi.
- **Tác nhân và mô hình cơ sở**: Chỉ hỗ trợ `antigravity-preview-09-2026` dưới dạng
  `base_agent`. Các lựa chọn mô hình được hỗ trợ trong `agent_config` là
  `gemini-3.8-flash` (mặc định), `gemini-3.6-flash` và
  `gemini-3.5-flash-lite`. Đối với các tác nhân có tên, bạn không thể ghi đè mô hình tại thời điểm tương tác.
- **Không có tính năng tạo phiên bản**: Tính năng tạo phiên bản và khôi phục phiên bản của tác nhân hiện chưa được hỗ trợ.
- **Không lồng ghép tác nhân phụ**: Tính năng uỷ quyền cho tác nhân phụ chưa được hỗ trợ.
- Bạn có thể có tối đa 1.000 nhân viên hỗ trợ được quản lý.

## Bước tiếp theo

- [Tổng quan về tác nhân](https://ai.google.dev/gemini-api/docs/agents?hl=vi): Tìm hiểu về các khái niệm cốt lõi của tác nhân được quản lý.
- [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi): Bắt đầu xây dựng bằng các cuộc trò chuyện nhiều lượt và truyền trực tuyến.
- [Tác nhân Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi): Khám phá các chức năng, công cụ và giá của tác nhân mặc định.
- [Môi trường tác nhân](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi): Định cấu hình hộp cát, nguồn và kết nối mạng.
- [API Tác nhân được quản lý trên Nền tảng tác nhân](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=vi): Để tạo tác nhân có tích hợp sẵn tính năng quản trị của tổ chức.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-10-28 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-10-28 UTC."],[],[]]
