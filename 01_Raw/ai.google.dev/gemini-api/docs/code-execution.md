---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=id
fetched_at: 2026-10-12T06:56:54.049840+00:00
title: "Eksekusi kode \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=id) kini tersedia secara umum. Sebaiknya gunakan API ini untuk mengakses semua fitur dan model terbaru.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google menggunakan teknologi AI untuk menerjemahkan konten ke dalam bahasa pilihan Anda. Terjemahan AI mungkin mengandung kesalahan.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Eksekusi kode

Gemini API menyediakan alat eksekusi kode yang memungkinkan model untuk membuat dan menjalankan kode Python. Kemudian, model dapat belajar secara iteratif dari hasil eksekusi kode hingga mencapai output akhir. Anda dapat menggunakan eksekusi
kode untuk membangun aplikasi yang memanfaatkan penalaran berbasis kode. Misalnya, Anda dapat menggunakan eksekusi kode untuk menyelesaikan persamaan atau memproses teks. Anda juga dapat menggunakan [library](#supported-libraries) yang disertakan dalam lingkungan eksekusi kode untuk melakukan tugas yang lebih khusus.

Gemini hanya dapat mengeksekusi kode di Python. Anda tetap dapat meminta Gemini untuk membuat kode dalam bahasa lain, tetapi model tidak dapat menggunakan alat eksekusi kode untuk menjalankannya.

## Mengaktifkan eksekusi kode

Untuk mengaktifkan eksekusi kode, konfigurasi alat eksekusi kode pada model. Hal ini memungkinkan model membuat dan menjalankan kode.

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

Outputnya mungkin akan terlihat seperti berikut, yang telah diformat agar mudah dibaca:

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

Output ini menggabungkan beberapa bagian konten yang ditampilkan model saat menggunakan
eksekusi kode:

- `text`: Teks inline yang dihasilkan oleh model
- `code_execution_call`: Kode yang dibuat oleh model yang dimaksudkan untuk dieksekusi
- `code_execution_result`: Hasil kode yang dapat dieksekusi

## Eksekusi Kode dengan gambar (Gemini 3)

Model Gemini 3 Flash kini dapat menulis dan mengeksekusi kode Python untuk memanipulasi dan memeriksa gambar secara aktif.

**Kasus penggunaan**

- **Memperbesar dan memeriksa**: Model secara implisit mendeteksi saat detail terlalu kecil
  (misalnya, membaca pengukur dari jarak jauh) dan menulis kode untuk memangkas dan memeriksa ulang area tersebut
  pada resolusi yang lebih tinggi.
- **Matematika visual**: Model dapat menjalankan penghitungan multi-langkah menggunakan kode (misalnya, menjumlahkan item baris pada tanda terima).
- **Anotasi gambar**: Model dapat menganotasi gambar untuk menjawab pertanyaan, seperti menggambar panah untuk menunjukkan hubungan.

## Mengaktifkan Eksekusi Kode dengan gambar

Eksekusi Kode dengan gambar secara resmi didukung di Gemini 3 Flash. Anda dapat mengaktifkan perilaku ini dengan mengaktifkan Eksekusi Kode sebagai alat dan Penalaran.

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

## Menggunakan eksekusi kode dalam interaksi multi-turn

Anda juga dapat menggunakan eksekusi kode sebagai bagian dari percakapan multi-turn menggunakan
`previous_interaction_id`.

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

## Input/output (I/O)

Pada model Gemini saat ini seperti
[Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=id), eksekusi
kode mendukung input file dan output grafik. Dengan kemampuan input dan output ini, Anda dapat mengupload file CSV dan teks, mengajukan pertanyaan tentang file, dan membuat grafik [Matplotlib](https://matplotlib.org/) sebagai bagian dari respons. File output ditampilkan sebagai gambar inline dalam respons.

### Harga I/O

Saat menggunakan I/O eksekusi kode, Anda akan ditagih untuk token input dan token output:

**Token input:**

- Perintah pengguna

**Token output:**

- Kode yang dihasilkan oleh model
- Output eksekusi kode di lingkungan kode
- Token penalaran
- Ringkasan yang dibuat oleh model

### Detail I/O

Saat Anda menangani I/O eksekusi kode, perhatikan detail teknis berikut:

- Waktu proses maksimum lingkungan kode adalah 30 detik.
- Jika lingkungan kode menghasilkan error, model dapat memutuskan untuk
  membuat ulang output kode. Hal ini dapat terjadi hingga 5 kali.
- Ukuran input file maksimum dibatasi oleh jendela token model. Jika Anda mengupload file yang melebihi jendela konteks maksimum model, API akan menampilkan error.
- Eksekusi kode berfungsi paling baik dengan file teks dan CSV.
- File input dapat diteruskan sebagai data inline atau diupload menggunakan
  [Files API](https://ai.google.dev/gemini-api/docs/files?hl=id),
  dan file output selalu ditampilkan sebagai data inline.

## Penagihan

Tidak ada biaya tambahan untuk mengaktifkan eksekusi kode dari Gemini API.
Anda akan ditagih dengan tarif token input dan output saat ini berdasarkan model Gemini yang Anda gunakan.

Berikut beberapa hal lain yang perlu diketahui tentang penagihan untuk eksekusi kode:

- Anda hanya ditagih satu kali untuk token input yang Anda teruskan ke model, dan Anda ditagih untuk token output akhir yang dikembalikan kepada Anda oleh model.
- Token yang merepresentasikan kode yang dihasilkan dihitung sebagai token output. Kode yang dihasilkan dapat mencakup teks dan output multimodal seperti gambar.
- Hasil eksekusi kode juga dihitung sebagai token output.

Model penagihan ditampilkan dalam diagram berikut:

![model penagihan eksekusi kode](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=id)

- Anda akan ditagih dengan tarif token input dan output saat ini berdasarkan
  model Gemini yang Anda gunakan.
- Jika Gemini menggunakan eksekusi kode saat membuat respons Anda, perintah asli, kode yang dihasilkan, dan hasil kode yang dieksekusi akan diberi label *token perantara* dan ditagih sebagai *token input*.
- Kemudian, Gemini membuat ringkasan dan menampilkan kode yang dihasilkan, hasil dari
  kode yang dieksekusi, dan ringkasan akhir. Token ini ditagih sebagai *token output*.
- Gemini API menyertakan jumlah token perantara dalam respons API, sehingga Anda tahu alasan Anda mendapatkan token input tambahan di luar perintah awal Anda.

## Batasan

- Model hanya dapat membuat dan menjalankan kode. API ini tidak dapat menampilkan artefak lain seperti file media.
- Dalam beberapa kasus, mengaktifkan eksekusi kode dapat menyebabkan regresi di area output model lainnya (misalnya, menulis cerita).
- Ada beberapa variasi dalam kemampuan berbagai model untuk menggunakan eksekusi kode dengan berhasil.

## Kombinasi alat yang didukung

Alat eksekusi kode dapat digabungkan dengan
[Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id) untuk
mendukung kasus penggunaan yang lebih kompleks.

Model Gemini 3 mendukung penggabungan alat bawaan (seperti Eksekusi Kode) dengan alat kustom (panggilan fungsi).

## Library yang didukung

Lingkungan eksekusi kode mencakup library berikut:

- attrs
- catur
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
- paket
- pandas
- bantal
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
- seaborn
- enam
- striprtf
- sympy
- tabulasi
- tensorflow
- toolz
- xlrd

Anda tidak dapat menginstal library Anda sendiri.

## Langkah berikutnya

- Coba [Panduan Memulai Interactions API](https://ai.google.dev/gemini-api/docs/quickstart?hl=id).
- Pelajari alat Gemini API lainnya:
  - [Pemanggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id)
  - [Grounding dengan Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id)

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-10-09 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-10-09 UTC."],[],[]]
