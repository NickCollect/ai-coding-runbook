---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=th
fetched_at: 2026-10-05T06:36:25.365284+00:00
title: "\u0e01\u0e32\u0e23\u0e40\u0e23\u0e35\u0e22\u0e01\u0e43\u0e0a\u0e49\u0e42\u0e04\u0e49\u0e14 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash พร้อมให้บริการแล้ว [ลองเลย](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=th)

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# การเรียกใช้โค้ด

Gemini API มีเครื่องมือการเรียกใช้โค้ดที่ช่วยให้โมเดลสามารถ
สร้างและรันโค้ด Python ได้ จากนั้นโมเดลจะเรียนรู้ซ้ำๆ จาก
ผลการเรียกใช้โค้ดจนกว่าจะได้เอาต์พุตสุดท้าย คุณสามารถใช้การดำเนินการโค้ด
เพื่อสร้างแอปพลิเคชันที่ได้รับประโยชน์จากการให้เหตุผลตามโค้ด เช่น คุณสามารถใช้การเรียกใช้โค้ดเพื่อแก้สมการหรือประมวลผลข้อความ นอกจากนี้ คุณยังใช้[ไลบรารี](#supported-libraries)ที่รวมอยู่ในการเรียกใช้โค้ด
เพื่อทำงานที่เฉพาะเจาะจงมากขึ้นได้ด้วย

Gemini รันโค้ดได้ใน Python เท่านั้น คุณยังคงขอให้ Gemini สร้างโค้ดในภาษาอื่นได้ แต่โมเดลจะใช้เครื่องมือการดำเนินการโค้ดเพื่อรันโค้ดนั้นไม่ได้

## เปิดใช้การเรียกใช้โค้ด

หากต้องการเปิดใช้การเรียกใช้โค้ด ให้กำหนดค่าเครื่องมือเรียกใช้โค้ดในโมเดล ซึ่งจะ
ช่วยให้โมเดลสร้างและเรียกใช้โค้ดได้

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.of(
                "What is the sum of the first 50 prime numbers? "
                    + "Generate and run code for the calculation, and make sure you get all 50."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep outputStep = (ModelOutputStep) step;
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println(((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().ifPresent(args -> System.out.println(args.code().orElse("")));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println(resultStep.result().orElse(""));
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
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput(
                "What is the sum of the first 50 prime numbers? " +
                    "Generate and run code for the calculation, and make sure you get all 50.",
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if outStep := step.ModelOutputStep; outStep != nil {
            for _, contentBlock := range outStep.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println(textContent.GetText())
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if code := callStep.Arguments.GetCode(); code != nil {
                fmt.Println(*code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println(resultStep.GetResult())
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
    "model": "gemini-3.8-flash",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

เอาต์พุตอาจมีลักษณะดังต่อไปนี้ ซึ่งได้รับการจัดรูปแบบเพื่อให้อ่านง่าย

```
Okay, I need to calculate the sum of the first 50 prime numbers. Here's how I'll
approach this:

1.  **Generate Prime Numbers:** I'll use an iterative method to find prime
    numbers. I'll start with 2 and check if each subsequent number is divisible
    by any number between 2 and its square root. If not, it's a prime.
2.  **Store Primes:** I'll store the prime numbers in a list until I have 50 of
    them.
3.  **Calculate the Sum:**  Finally, I'll sum the prime numbers in the list.

Here's the Python code to do this:

def is_prime(n):
  """Efficiently checks if a number is prime."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

primes = []
num = 2
while len(primes) < 50:
  if is_prime(num):
    primes.append(num)
  num += 1

sum_of_primes = sum(primes)
print(f'{primes=}')
print(f'{sum_of_primes=}')

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
sum_of_primes=5117

The sum of the first 50 prime numbers is 5117.
```

เอาต์พุตนี้รวมส่วนเนื้อหาหลายส่วนที่โมเดลแสดงเมื่อใช้
การเรียกใช้โค้ด

- `text`: ข้อความในบรรทัดที่โมเดลสร้างขึ้น
- `code_execution_call`: โค้ดที่โมเดลสร้างขึ้นซึ่งมีไว้เพื่อดำเนินการ
- `code_execution_result`: ผลลัพธ์ของโค้ดที่เรียกใช้งานได้

## การดำเนินการโค้ดด้วยรูปภาพ (Gemini 3)

ตอนนี้โมเดล Gemini 3 Flash สามารถเขียนและรันโค้ด Python เพื่อ
จัดการและตรวจสอบรูปภาพได้อย่างมีประสิทธิภาพ

**กรณีการใช้งาน**

- **ซูมและตรวจสอบ**: โมเดลจะตรวจหาโดยนัยเมื่อรายละเอียดมีขนาดเล็กเกินไป (เช่น การอ่านมาตรวัดที่อยู่ไกล) และเขียนโค้ดเพื่อครอบตัดและตรวจสอบพื้นที่อีกครั้งที่ความละเอียดสูงขึ้น
- **คณิตศาสตร์ภาพ**: โมเดลสามารถทำการคำนวณหลายขั้นตอนโดยใช้โค้ด (เช่น
  การบวกรายการในใบเสร็จ)
- **การอธิบายประกอบรูปภาพ**: โมเดลสามารถอธิบายประกอบรูปภาพเพื่อตอบคำถามได้ เช่น การวาดลูกศรเพื่อแสดงความสัมพันธ์

## เปิดใช้การเรียกใช้โค้ดด้วยรูปภาพ

Gemini 3 Flash รองรับการดำเนินการโค้ดที่มีรูปภาพอย่างเป็นทางการ คุณ
เปิดใช้งานลักษณะการทำงานนี้ได้โดยเปิดใช้ทั้งเครื่องมือเรียกใช้โค้ดและการคิด

### Python

```
from google import genai
import requests
import base64
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "image", "data": base64.b64encode(image_bytes).decode('utf-8'), "mime_type": "image/jpeg"},
        {"type": "text", "text": "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools=[{"type": "code_execution"}]
)

for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
            elif content_block.type == "image":
                img = Image.open(io.BytesIO(base64.b64decode(content_block.data)))
                img.show()  # or: img.save("output_image.jpg")
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const client = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      {
        type: "image",
        data: base64ImageData,
        mime_type: "image/jpeg"
      },
      { type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    tools: [{ type: "code_execution" }]
  });

  for (const step of interaction.steps) {
    if (step.type === "model_output") {
      for (const contentBlock of step.content) {
        if (contentBlock.type === "text") {
          console.log("Text:", contentBlock.text);
        }
      }
    } else if (step.type === "code_execution_call") {
      console.log(`\nGenerated Code:\n`, step.arguments.code);
    } else if (step.type === "code_execution_result") {
      console.log(`\nExecution Output:\n`, step.result);
    }
  }
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.io.InputStream;
import java.net.URI;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collections;

String imageUrl = "https://goo.gle/instrument-img";
byte[] imageBytes;
try (InputStream in = URI.create(imageUrl).toURL().openStream()) {
  imageBytes = in.readAllBytes();
}
String base64Image = Base64.getEncoder().encodeToString(imageBytes);

Client client = new Client();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(
            InteractionsInput.ofContent(
                Arrays.asList(
                    ImageContent.builder()
                        .data(base64Image)
                        .mimeType(ImageContentMimeType.IMAGE_JPEG)
                        .build(),
                    TextContent.builder()
                        .text(
                            "Zoom into the expression pedals and tell me how many pedals are there?")
                        .build())))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

for (Step step : interaction.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep outputStep = (ModelOutputStep) step;
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println(((TextContent) contentBlock).text().orElse(""));
      } else if (contentBlock instanceof ImageContent) {
        ImageContent imgContent = (ImageContent) contentBlock;
        if (imgContent.data().isPresent()) {
          byte[] decoded = Base64.getDecoder().decode(imgContent.data().get());
          Files.write(Paths.get("output_image.jpg"), decoded);
        }
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().ifPresent(args -> System.out.println(args.code().orElse("")));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println(resultStep.result().orElse(""));
  }
}
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "io"
    "log"
    "net/http"
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

    imageURL := "https://goo.gle/instrument-img"
    httpResp, err := http.Get(imageURL)
    if err != nil {
        log.Fatal(err)
    }
    defer httpResp.Body.Close()
    imageBytes, err := io.ReadAll(httpResp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Image := base64.StdEncoding.EncodeToString(imageBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.ImageContent{
                    Data:     genai.Ptr(base64Image),
                    MimeType: interactions.ImageContentMimeType("image/jpeg").ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Zoom into the expression pedals and tell me how many pedals are there?",
                }),
            }),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res.Interaction.Steps {
        if outStep := step.ModelOutputStep; outStep != nil {
            for _, contentBlock := range outStep.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println(textContent.GetText())
                } else if imgContent := contentBlock.ImageContent; imgContent != nil && imgContent.Data != nil {
                    decoded, err := base64.StdEncoding.DecodeString(*imgContent.Data)
                    if err == nil {
                        _ = os.WriteFile("output_image.jpg", decoded, 0644)
                    }
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if code := callStep.Arguments.GetCode(); code != nil {
                fmt.Println(*code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println(resultStep.GetResult())
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.8-flash"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

# Use jq to create the JSON payload to avoid "Argument list too long" error with large base64 strings
echo -n "$IMAGE_B64" > image_b64.txt
jq -n \
  --rawfile b64 image_b64.txt \
  --arg mime "$MIME_TYPE" \
  '{
    model: "gemini-3.8-flash",
    input: [
      {type: "image", data: $b64, mime_type: $mime},
      {type: "text", text: "Zoom into the expression pedals and tell me how many pedals are there?"}
    ],
    tools: [{type: "code_execution"}]
  }' > payload.json

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json
```

## ใช้การเรียกใช้โค้ดในการสนทนาไปมาหลายรอบ

นอกจากนี้ คุณยังใช้การเรียกใช้โค้ดเป็นส่วนหนึ่งของการสนทนาไปมาได้ด้วยการใช้
`previous_interaction_id`

### Python

```
from google import genai

client = genai.Client()

interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have a math question for you.",
    tools=[{"type": "code_execution"}]
)
print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    previous_interaction_id=interaction1.id,
    input="What is the sum of the first 50 prime numbers? "
          "Generate and run code for the calculation, and make sure you get all 50.",
    tools=[{"type": "code_execution"}]
)

for step in interaction2.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
    elif step.type == "code_execution_call":
        print(step.arguments.code)
    elif step.type == "code_execution_result":
        print(step.result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction1 = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "I have a math question for you.",
    tools: [{ type: "code_execution" }]
});
console.log(interaction1.output_text);

const interaction2 = await client.interactions.create({
    model: "gemini-3.8-flash",
    previous_interaction_id: interaction1.id,
    input: "What is the sum of the first 50 prime numbers? " +
           "Generate and run code for the calculation, and make sure you get all 50.",
    tools: [{ type: "code_execution" }]
});

for (const step of interaction2.steps) {
    if (step.type === "model_output") {
        for (const contentBlock of step.content) {
            if (contentBlock.type === "text") {
                console.log(contentBlock.text);
            }
        }
    } else if (step.type === "code_execution_call") {
        console.log(step.arguments.code);
    } else if (step.type === "code_execution_result") {
        console.log(step.result);
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CodeExecution;
import com.google.genai.gaos.models.interactions.CodeExecutionCallStep;
import com.google.genai.gaos.models.interactions.CodeExecutionResultStep;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.ModelOutputStep;
import com.google.genai.gaos.models.interactions.Step;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.Collections;

Client client = new Client();

CreateModelInteraction params1 =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .input(InteractionsInput.of("I have a math question for you."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction1 =
    client.interactions.create(CreateInteractionRequestBody.of(params1)).interaction().get();
System.out.println(interaction1.outputText().orElse(""));

CreateModelInteraction params2 =
    CreateModelInteraction.builder()
        .model("gemini-3.8-flash")
        .previousInteractionId(interaction1.id().get())
        .input(
            InteractionsInput.of(
                "What is the sum of the first 50 prime numbers? "
                    + "Generate and run code for the calculation, and make sure you get all 50."))
        .tools(Arrays.asList(CodeExecution.builder().build()))
        .build();

Interaction interaction2 =
    client.interactions.create(CreateInteractionRequestBody.of(params2)).interaction().get();

for (Step step : interaction2.steps().orElse(Collections.emptyList())) {
  if (step instanceof ModelOutputStep) {
    ModelOutputStep outputStep = (ModelOutputStep) step;
    for (Content contentBlock : outputStep.content().orElse(Collections.emptyList())) {
      if (contentBlock instanceof TextContent) {
        System.out.println(((TextContent) contentBlock).text().orElse(""));
      }
    }
  } else if (step instanceof CodeExecutionCallStep) {
    CodeExecutionCallStep callStep = (CodeExecutionCallStep) step;
    callStep.arguments().ifPresent(args -> System.out.println(args.code().orElse("")));
  } else if (step instanceof CodeExecutionResultStep) {
    CodeExecutionResultStep resultStep = (CodeExecutionResultStep) step;
    System.out.println(resultStep.result().orElse(""));
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

    res1, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("I have a math question for you."),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res1.Interaction.OutputText != nil {
        fmt.Println(*res1.Interaction.OutputText)
    }

    res2, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model:                 interactions.Model("gemini-3.8-flash"),
            PreviousInteractionID: res1.Interaction.ID,
            Input: interactions.NewInteractionsInput(
                "What is the sum of the first 50 prime numbers? " +
                    "Generate and run code for the calculation, and make sure you get all 50.",
            ),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.CodeExecution{}),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, step := range res2.Interaction.Steps {
        if outStep := step.ModelOutputStep; outStep != nil {
            for _, contentBlock := range outStep.Content {
                if textContent := contentBlock.TextContent; textContent != nil {
                    fmt.Println(textContent.GetText())
                }
            }
        } else if callStep := step.CodeExecutionCallStep; callStep != nil {
            if code := callStep.Arguments.GetCode(); code != nil {
                fmt.Println(*code)
            }
        } else if resultStep := step.CodeExecutionResultStep; resultStep != nil {
            fmt.Println(resultStep.GetResult())
        }
    }
}
```

### REST

```
# First turn
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.8-flash",
    "input": "I have a math question for you.",
    "tools": [{"type": "code_execution"}]
}')

INTERACTION_ID=$(echo $RESPONSE1 | jq -r '.id')

# Second turn with previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
    "model": "gemini-3.8-flash",
    "previous_interaction_id": "'"$INTERACTION_ID"'",
    "input": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50.",
    "tools": [{"type": "code_execution"}]
}'
```

## อินพุต/เอาต์พุต (I/O)

ในโมเดล Gemini ปัจจุบัน เช่น [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=th#gemini-3.5-flash) การ
เรียกใช้โค้ดรองรับการป้อนไฟล์และเอาต์พุตกราฟ ความสามารถในการป้อนข้อมูลและเอาต์พุตเหล่านี้ช่วยให้คุณอัปโหลดไฟล์ CSV และไฟล์ข้อความ ถามคำถามเกี่ยวกับไฟล์ และให้ระบบสร้างกราฟ [Matplotlib](https://matplotlib.org/) เป็นส่วนหนึ่งของคำตอบได้ ระบบจะแสดงไฟล์เอาต์พุตเป็นรูปภาพในบรรทัดในคำตอบ

### ราคา I/O

เมื่อใช้ I/O การเรียกใช้โค้ด ระบบจะเรียกเก็บเงินจากโทเค็นอินพุตและโทเค็นเอาต์พุต

**โทเค็นอินพุต:**

- พรอมต์ของผู้ใช้

**โทเค็นเอาต์พุต:**

- โค้ดที่โมเดลสร้างขึ้น
- เอาต์พุตการเรียกใช้โค้ดในสภาพแวดล้อมของโค้ด
- โทเค็นการคิด
- ข้อมูลสรุปที่โมเดลสร้างขึ้น

### รายละเอียด I/O

เมื่อทำงานกับ I/O การดำเนินการโค้ด โปรดทราบรายละเอียดทางเทคนิคต่อไปนี้

- ระยะเวลาการทำงานสูงสุดของสภาพแวดล้อมโค้ดคือ 30 วินาที
- หากสภาพแวดล้อมของโค้ดสร้างข้อผิดพลาด โมเดลอาจตัดสินใจสร้างเอาต์พุตโค้ดใหม่ ซึ่งอาจเกิดขึ้นได้สูงสุด 5 ครั้ง
- ขนาดไฟล์อินพุตสูงสุดจะจำกัดตามหน้าต่างโทเค็นของโมเดล หากคุณอัปโหลดไฟล์ที่มีขนาดเกินหน้าต่างบริบทสูงสุดของโมเดล API จะแสดงข้อผิดพลาด
- การเรียกใช้โค้ดจะทำงานได้ดีที่สุดกับไฟล์ข้อความและ CSV
- คุณส่งไฟล์อินพุตเป็นข้อมูลแบบอินไลน์หรืออัปโหลดโดยใช้
  [Files API](https://ai.google.dev/gemini-api/docs/files?hl=th)
  และระบบจะส่งคืนไฟล์เอาต์พุตเป็นข้อมูลแบบอินไลน์เสมอ

## การเรียกเก็บเงิน

การเปิดใช้การเรียกใช้โค้ดจาก Gemini API จะไม่มีค่าใช้จ่ายเพิ่มเติม
ระบบจะเรียกเก็บเงินจากคุณตามอัตราปัจจุบันของโทเค็นอินพุตและเอาต์พุตโดยอิงตาม
โมเดล Gemini ที่คุณใช้

สิ่งอื่นๆ ที่ควรทราบเกี่ยวกับการเรียกเก็บเงินสำหรับการเรียกใช้โค้ดมีดังนี้

- ระบบจะเรียกเก็บเงินจากคุณเพียงครั้งเดียวสำหรับโทเค็นอินพุตที่คุณส่งไปยังโมเดล และจะเรียกเก็บเงินสำหรับโทเค็นเอาต์พุตสุดท้ายที่โมเดลส่งกลับมาให้คุณ
- ระบบจะนับโทเค็นที่แสดงโค้ดที่สร้างขึ้นเป็นโทเค็นเอาต์พุต โค้ดที่สร้างขึ้น
  อาจมีข้อความและเอาต์พุตแบบหลายรูปแบบ เช่น รูปภาพ
- ผลการเรียกใช้โค้ดจะนับเป็นโทเค็นเอาต์พุตด้วย

รูปแบบการเรียกเก็บเงินแสดงอยู่ในแผนภาพต่อไปนี้

![รูปแบบการเรียกเก็บเงินสำหรับการเรียกใช้โค้ด](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=th)

- ระบบจะเรียกเก็บเงินจากคุณตามอัตราปัจจุบันของโทเค็นอินพุตและเอาต์พุตโดยอิงตามโมเดล Gemini ที่คุณใช้
- หาก Gemini ใช้การเรียกใช้โค้ดเมื่อสร้างคำตอบ ระบบจะติดป้ายกำกับพรอมต์ต้นฉบับ โค้ดที่สร้างขึ้น และผลลัพธ์ของโค้ดที่เรียกใช้เป็น*โทเค็นกลาง* และจะเรียกเก็บเงินเป็น*โทเค็นอินพุต*
- จากนั้น Gemini จะสร้างข้อมูลสรุปและส่งคืนโค้ดที่สร้างขึ้น ผลลัพธ์ของ
  โค้ดที่เรียกใช้ และข้อมูลสรุปสุดท้าย ระบบจะเรียกเก็บเงินสำหรับโทเค็นเหล่านี้เป็น*โทเค็นเอาต์พุต*
- Gemini API จะรวมจำนวนโทเค็นระหว่างการประมวลผลไว้ในการตอบกลับจาก API เพื่อให้คุณทราบสาเหตุที่ได้รับโทเค็นอินพุตเพิ่มเติมจากพรอมต์เริ่มต้น

## ข้อจำกัด

- โมเดลจะสร้างและเรียกใช้โค้ดได้เท่านั้น แต่จะแสดงอาร์ติแฟกต์อื่นๆ เช่น ไฟล์สื่อ ไม่ได้
- ในบางกรณี การเรียกใช้โค้ดอาจทำให้เกิดการถดถอยในด้านอื่นๆ ของเอาต์พุตโมเดล (เช่น การเขียนเรื่องราว)
- ความสามารถของโมเดลต่างๆ ในการใช้การดำเนินการโค้ดให้สำเร็จนั้นแตกต่างกันไป

## ชุดเครื่องมือที่รองรับ

คุณสามารถใช้เครื่องมือการเรียกใช้โค้ดร่วมกับ[การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th) เพื่อรองรับกรณีการใช้งานที่ซับซ้อนมากขึ้น

โมเดล Gemini 3 รองรับการรวมเครื่องมือในตัว (เช่น การดำเนินการโค้ด) กับ
เครื่องมือที่กำหนดเอง (การเรียกใช้ฟังก์ชัน)

## ไลบรารีที่รองรับ

สภาพแวดล้อมการเรียกใช้โค้ดมีไลบรารีต่อไปนี้

- attrs
- หมากรุก
- contourpy
- fpdf
- geopandas
- imageio
- jinja2
- joblib
- jsonschema
- jsonschema-specifications
- lxml
- matplotlib
- mpmath
- numpy
- opencv-python
- openpyxl
- การสร้างแพ็กเกจ
- แพนด้า
- หมอน
- protobuf
- pylatex
- pyparsing
- PyPDF2
- python-dateutil
- python-docx
- python-pptx
- reportlab
- scikit-learn
- scipy
- Seaborn
- หก
- striprtf
- sympy
- จัดตาราง
- tensorflow
- toolz
- xlrd

คุณจะติดตั้งไลบรารีของคุณเองไม่ได้

## ขั้นตอนถัดไป

- ลองใช้ [Quickstart ของ Interactions API](https://ai.google.dev/gemini-api/docs/quickstart?hl=th)
- ดูข้อมูลเกี่ยวกับเครื่องมืออื่นๆ ของ Gemini API
  - [การเรียกใช้ฟังก์ชัน](https://ai.google.dev/gemini-api/docs/function-calling?hl=th)
  - [การเชื่อมต่อแหล่งข้อมูลกับ Google Search](https://ai.google.dev/gemini-api/docs/google-search?hl=th)

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-09-24 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-09-24 UTC"],[],[]]
