---
source_url: https://ai.google.dev/gemini-api/docs/thinking?hl=fa
fetched_at: 2026-10-12T07:04:18.565100+00:00
title: "\u202bGemini \u062f\u0631\u062d\u0627\u0644 \u0641\u06a9\u0631 \u06a9\u0631\u062f\u0646 \u0627\u0633\u062a \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash اکنون در دسترس است. [آن را امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=fa) .

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# ‫Gemini درحال فکر کردن است

[مدل‌های سری Gemini 3 و 2.5](https://ai.google.dev/gemini-api/docs/models?hl=fa) از «فرایند تفکر» استفاده می‌کنند که توانایی‌های استدلال و برنامه‌ریزی چندمرحله‌ای آن‌ها را به‌طور قابل‌توجهی بهبود می‌بخشد و آن‌ها را برای انجام تکالیف پیچیده مانند کدنویسی، ریاضیات پیشرفته، و تجزیه‌وتحلیل داده‌ها بسیار مؤثر می‌کند.

وقتی از مدل تفکر استفاده می‌کنید، Gemini پیش‌از پاسخ دادن، درونی استدلال می‌کند. «میانای برنامه‌سازی کاربردی تعاملات» این استدلال را ازطریق `thought` مرحله، مراحل اختصاصی که به‌ترتیب زمانی در کنار فراخوانی‌های تابع، ورودی‌های کاربر، یا بروندادهای مدل در آرایه `steps` ظاهر می‌شوند، نمایان می‌کند.

هر مرحله فکر شامل دو فیلد است:

| فیلد | الزامی | شرح |
| --- | --- | --- |
| `signature` | ✅ بله | نمایشی رمزگذاری‌شده از وضعیت استدلال داخلی مدل. همیشه ارائه می‌شود، حتی وقتی مدل حداقل استدلال را انجام می‌دهد. |
| `summary` | ❌ نه | مجموعه‌ای از محتوا (نوشتار و/یا تصاویر) که استدلال را خلاصه می‌کند. بسته به پیکربندی [`thinking_summaries`](https://ai.google.dev/api/interactions-api?hl=fa)، اینکه مدل استدلال کافی انجام داده است یا نه، یا نوع محتوا (برای مثال، تصاویر پنهان ممکن است خلاصه نوشتاری نداشته باشند) ممکن است خالی باشد. |

## تعامل با فکر کردن

شروع تعامل با مدل تفکر مشابه با هر درخواست تعامل دیگری است. یکی از [مدل‌های دارای پشتیبانی از تفکر](#thinking-levels) را در فیلد `model` مشخص کنید:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain the concept of Occam's Razor and provide a simple, everyday example."
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain the concept of Occam's Razor and provide a simple, everyday example."
});
console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Explain the concept of Occam's Razor and provide a simple, everyday example."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Explain the concept of Occam's Razor and provide a simple, everyday example."),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain the concept of Occam'\''s Razor and provide a simple example."
  }'
```

## خلاصه‌های فکر

خلاصه‌های فکر بینش‌هایی درباره فرایند استدلال داخلی مدل ارائه می‌دهند.
به‌طور پیش‌فرض، فقط برونداد نهایی برگردانده می‌شود. می‌توانید خلاصه فکر را با `thinking_summaries` فعال کنید:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtStep;
import com.google.genai.gaos.models.interactions.ThoughtSummaryContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the sum of the first 50 prime numbers?"))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ThoughtStep thoughtStep) {
    System.out.println("Thought summary:");
    for (ThoughtSummaryContent contentBlock : thoughtStep.summary().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println(textContent.text().orElse(""));
      }
    }
    System.out.println();
  } else if (step instanceof ModelOutputStep outputStep) {
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent textContent) {
        System.out.println("Answer:");
        System.out.println(textContent.text().orElse(""));
        System.out.println();
      }
    }
  }
}
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Provide a list of 3 famous physicists and their key contributions"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelLow.ToPointer(),
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
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers?",
    "generation_config": {
      "thinking_summaries": "auto"
    }
  }'
```

در این موارد، یک بلوک فکر ممکن است **فقط حاوی امضا بدون خلاصه** باشد:

- درخواست‌های ساده، جایی که مدل برای تولید خلاصه به‌اندازه کافی استدلال نکرده است
- ‫`thinking_summaries: "none"`، جایی که خلاصه به‌طور صریح غیرفعال شده است
- برخی‌از انواع محتوای فکری، مثل تصاویر، ممکن است خلاصه نوشتاری نداشته باشند

کد شما باید همیشه بلوک‌های فکری را در جایی که `summary` خالی یا وجود ندارد مدیریت کند.

## جاری‌سازی با اندیشیدن

از جاری‌سازی برای دریافت خلاصه‌های تدریجی فکر درطول تولید استفاده کنید.
بلوک‌های فکر بااستفاده از «رویدادهای ارسالی سرور» (SSE) با دو نوع
دلتا متمایز ارائه می‌شوند:

| نوع دلتا | شامل می‌شود | زمان ارسال |
| --- | --- | --- |
| `thought_summary` | خلاصه محتوای نوشتار یا تصویر | یک یا چند دلتا با خلاصه افزایشی |
| `thought_signature` | امضای رمزنگارانه | آخرین تغییر قبل‌از `step.stop` |

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
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.InteractionSSEEvent;
import com.google.genai.gaos.models.interactions.InteractionSSEStreamEvent;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.StepDelta;
import com.google.genai.gaos.models.interactions.StepDeltaData;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.TextDelta;
import com.google.genai.gaos.models.interactions.ThinkingSummaries;
import com.google.genai.gaos.models.interactions.ThoughtSummaryDelta;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.gaos.models.operations.CreateInteractionResponse;
import com.google.genai.gaos.utils.EventStream;

Client client = new Client();

String prompt =
    "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.\n"
        + "Alice does not live in the red house.\n"
        + "Bob does not live in the green house.\n"
        + "Carol does not live in the red or green house.\n"
        + "Which house does each person live in?";

StringBuilder thoughts = new StringBuilder();
StringBuilder answer = new StringBuilder();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of(prompt))
        .generationConfig(
            GenerationConfig.builder().thinkingSummaries(ThinkingSummaries.AUTO).build())
        .stream(true)
        .build();

CreateInteractionResponse response =
    client.interactions.create(CreateInteractionRequestBody.of(params));

try (EventStream<InteractionSSEStreamEvent> stream = response.events()) {
  for (InteractionSSEStreamEvent streamEvent : stream) {
    InteractionSSEEvent event = streamEvent.data().orElse(null);
    if (event instanceof StepDelta stepDelta) {
      StepDeltaData delta = stepDelta.delta().orElse(null);
      if (delta instanceof ThoughtSummaryDelta thoughtDelta) {
        Content content = thoughtDelta.content().orElse(null);
        if (content instanceof TextContent textContent) {
          if (thoughts.length() == 0) {
            System.out.println("Thinking...");
          }
          String summaryText = textContent.text().orElse("");
          System.out.print("[Thought] " + summaryText);
          thoughts.append(summaryText);
        }
      } else if (delta instanceof TextDelta textDelta) {
        String text = textDelta.text().orElse("");
        if (!text.isEmpty()) {
          if (answer.length() == 0) {
            System.out.println("\nAnswer:");
          }
          System.out.print(text);
          answer.append(text);
        }
      }
    }
  }
}
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if thought := step.ThoughtStep; thought != nil {
            for _, part := range thought.Summary {
                if part.TextContent != nil {
                    fmt.Printf("Thought summary:\n%s\n\n", part.TextContent.Text)
                }
            }
        }
    }

    if res.Interaction.OutputText != nil {
        fmt.Printf("Answer:\n%s\n", *res.Interaction.OutputText)
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
    "model": "gemini-3.8-flash",
    "input": "Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue. Alice does not live in the red house. Bob does not live in the green house. Carol does not live in the red or green house. Which house does each person live in?",
    "generation_config": {
      "thinking_summaries": "auto"
    },
    "stream": true
  }'
```

پاسخ جاری‌سازی از «رویدادهای ارسالی سرور» (SSE) استفاده می‌کند و از مراحل و رویدادها تشکیل شده است، برای مثال:

```
event: interaction.created
data: {"interaction":{"id":"v1_xxx","status":"in_progress","object":"interaction","model":"gemini-3.8-flash"},"event_type":"interaction.created"}

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

## کنترل کردن اندیشیدن

مدل‌های Gemini به‌طور پیش‌فرض درگیر تفکر پویا می‌شوند و به‌طور خودکار میزان تلاش برای استدلال را براساس پیچیدگی درخواست تنظیم می‌کنند. بااستفاده از پارامتر `thinking_level` می‌توانید این رفتار را کنترل کنید.

| مدل | اندیشیدن پیش‌فرض | سطوح پشتیبانی‌شده |
| --- | --- | --- |
| gemini-3.8-flash | روشن (متوسط) | کم، متوسط، زیاد |
| gemini-3.6-flash | روشن (متوسط) | حداقل، کم، متوسط، زیاد |
| gemini-3.5-flash-lite | روشن (کمینه) | حداقل، کم، متوسط، زیاد |
| gemini-3.1-pro-preview | روشن (زیاد) | کم، متوسط، زیاد |
| gemini-3.1-flash-lite-image | روشن (کمینه) | کمینه، زیاد |
| gemini-3-flash-preview | روشن (زیاد) | حداقل، کم، متوسط، زیاد |
| gemini-3-pro-preview | روشن (زیاد) | کم، زیاد |
| gemini-2.5-pro | روشن | کم، متوسط، زیاد |
| gemini-2.5-flash | روشن | کم، متوسط، زیاد |
| gemini-2.5-flash-lite | خاموش | کم، متوسط، زیاد |
| gemini-robotics-er-2-preview | روشن (زیاد) | حداقل، کم، متوسط، زیاد |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
    model: "gemini-3.8-flash",
    input: "Provide a list of 3 famous physicists and their key contributions",
    generation_config: {
        thinking_level: "low"
    }
});
console.log(interaction.output_text);
```

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.GenerationConfig;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.ThinkingLevel;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(
            InteractionsInput.of(
                "Provide a list of 3 famous physicists and their key contributions"))
        .generationConfig(GenerationConfig.builder().thinkingLevel(ThinkingLevel.LOW).build())
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

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

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("What is the sum of the first 50 prime numbers?"),
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel:     interactions.ThinkingLevelHigh.ToPointer(),
                ThinkingSummaries: interactions.ThinkingSummariesAuto.ToPointer(),
            },
            Stream: genai.Ptr(true),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    stream := res.InteractionSSEStreamEvent
    defer stream.Close()

    for stream.Next() {
        event := stream.Value()
        if stepDelta := event.GetDataStepDelta(); stepDelta != nil {
            if thoughtDelta := stepDelta.GetDeltaThoughtSummary(); thoughtDelta != nil {
                if textContent := thoughtDelta.GetContentText(); textContent != nil {
                    fmt.Printf("[Thought Summary] %s\n", textContent.Text)
                }
            }
            if textDelta := stepDelta.GetDeltaText(); textDelta != nil {
                fmt.Print(textDelta.GetText())
            }
        }
    }
    if err := stream.Err(); err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Provide a list of 3 famous physicists and their key contributions",
    "generation_config": {
      "thinking_level": "low"
    }
  }'
```

### محدودیت‌های کد و `max_output_tokens`

پارامتر تولید [`max_output_tokens`](https://ai.google.dev/api/interactions-api?hl=fa#request-body) حداکثر تعداد نشانه‌هایی را که یک پاسخ می‌تواند تولید کند، ازجمله نشانه‌های فکری، تعیین می‌کند.

وقتی تنظیم شود، این پارامتر به‌عنوان برش سخت‌گیرانه‌ای عمل می‌کند که زیرساخت آن را اعمال می‌کند
بدون اینکه نحوه تخصیص بودجه فکری مدل را تغییر دهد
(`thinking_level`).

اگر مدل درحین استدلال به این حد مجاز برسد، تولید را با وضعیت
`"incomplete"` متوقف می‌کند و برونداد کوتاه یا خالی برمی‌گرداند (درحالی‌که همچنان هزینه
هر نشانه فکری تولیدشده را محاسبه می‌کند). برای کاهش هزینه یا تأخیر بدون کوتاه کردن پاسخ‌ها، به‌جای تنظیم `max_output_tokens` کوچک، `thinking_level` (`low` یا `medium`) را کاهش دهید.

## امضاهای فکری

امضاهای فکری نمایشی رمزگذاری‌شده از استدلال داخلی مدل است. این مدل‌ها باید پیوستگی استدلال را در تعاملات چندنوبتی حفظ کنند.

«میانای برنامه‌سازی کاربردی تعامل‌ها» مدیریت امضاهای فکری را بسیار ساده‌تر از `generateContent` API می‌کند.

### حالت Stateful (توصیه می‌شود)

به‌طور پیش‌فرض، وقتی از «میاناهای برنامه‌سازی کاربردی تعاملات» در حالت با وضعیت (با تنظیم `store: true` و ارسال `previous_interaction_id` در نوبت‌های بعدی) استفاده می‌کنید، سرور به‌طور خودکار وضعیت مکالمه را مدیریت می‌کند، ازجمله همه بلوک‌های فکر و امضاها. در این حالت، نیازی نیست کاری درخصوص امضاها انجام دهید. این‌ها کاملاً در سمت سرور مدیریت می‌شوند.

### حالت بدون وضعیت

اگر خودتان وضعیت مکالمه را مدیریت می‌کنید (حالت بدون وضعیت) و سابقه کامل ورودی‌ها و خروجی‌ها را در هر درخواست ارسال می‌کنید:

- شما **باید** همیشه همه بلوک‌های `thought` را دقیقاً همان‌گونه که از مدل دریافت شده‌اند دوباره ارسال کنید.
- شما باید بلوک‌های فکری را از سابقه **حذف نکنید** یا آن‌ها را تغییر ندهید، زیرا این بلوک‌ها حاوی امضاهای لازم برای ادامه استدلال مدل هستند.
- هنگام تغییر مدل‌ها در یک جلسه، همچنان باید بلوک‌های فکری مدل قبلی را دوباره ارسال کنید. سازگاری را زیرینه مدیریت می‌کند.

## قیمت‌گذاری

وقتی اندیشیدن روشن باشد، قیمت پاسخ مجموع داده‌واحدهای برونداد و داده‌واحدهای اندیشیدن است. می‌توانید تعداد کل نشانه‌های فکری تولیدشده را از فیلد `total_thought_tokens` دریافت کنید.

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

### جاوا

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.Usage;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain the concept of Occam's Razor."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

if (interaction.usage().isPresent()) {
  Usage usage = interaction.usage().get();
  System.out.println("Thoughts tokens: " + usage.totalThoughtTokens().orElse(0));
  System.out.println("Output tokens: " + usage.totalOutputTokens().orElse(0));
}
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

    // Turn 1: Execute a reasoning + tool use interaction
    turn1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-pro"),
            Input: interactions.NewInteractionsInput("Compare the GDP growth of Japan and Germany in 2025."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.GoogleSearch{}),
            },
            GenerationConfig: &interactions.GenerationConfig{
                ThinkingLevel: interactions.ThinkingLevelHigh.ToPointer(),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    // Turn 2: Pass PreviousInteractionID so thought signatures are automatically preserved
    turn2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-pro"),
            PreviousInteractionID: turn1.Interaction.ID,
            Input:                 interactions.NewInteractionsInput("Now summarize that comparison in a 3-row markdown table."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    if turn2.Interaction.OutputText != nil {
        fmt.Println(*turn2.Interaction.OutputText)
    }
}
```

مدل‌های اندیشگر برای بهبود کیفیت پاسخ نهایی، اندیشه‌های کامل تولید می‌کنند و سپس [خلاصه‌هایی](#summaries) را به‌عنوان برونداد ارائه می‌دهند تا بینشی درباره فرایند اندیشیدن ارائه دهند. قیمت‌گذاری براساس تعداد کامل نشانه‌های فکری است که مدل برای تولید نیاز دارد،
حتی اگر فقط خلاصه از API برونداد شود.

در راهنمای [شمارش نشان](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) می‌توانید درباره نشان‌ها بیشتر بدانید.

## روال‌های مطلوب

با دنبال کردن این دستورالعمل‌ها، از مدل‌های فکری به‌طور کارآمد استفاده کنید.

- **مرور استدلال**: خلاصه‌های فکر را تجزیه‌وتحلیل کنید تا دلیل شکست‌ها را بفهمید و پیام‌واره‌ها را بهبود دهید.
- **کنترل بودجه تفکر**: برای صرفه‌جویی در تعداد نشانه‌ها، مدل را ترغیب کنید برای بروندادهای طولانی کمتر فکر کند.
- **وظایف ساده**: برای بازیابی یا طبقه‌بندی حقایق از حداقل یا سطح پایین تفکر استفاده کنید (برای نمونه، «DeepMind در کجا تأسیس شد؟»).
- **تکالیف میانه‌روی**: از اندیشیدن پیش‌فرض برای مقایسه مفاهیم یا استدلال خلاقانه استفاده کنید (برای نمونه، مقایسه خودروهای برقی و هیبریدی).
- **کارهای پیچیده**: از حداکثر توان فکری برای کدنویسی پیشرفته، ریاضیات، یا برنامه‌ریزی چندمرحله‌ای استفاده کنید (برای نمونه، مسائل ریاضی AIME را حل کنید).

## قدم بعدی چیست

- [تولید نوشتار](https://ai.google.dev/gemini-api/docs/text-generation?hl=fa): پاسخ‌های نوشتاری پایه
- [فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa): اتصال به ابزارها
- [راهنمای Gemini 3](https://ai.google.dev/gemini-api/docs/gemini-3?hl=fa): ویژگی‌های مختص مدل

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-09 به‌وقت ساعت هماهنگ جهانی."],[],[]]
