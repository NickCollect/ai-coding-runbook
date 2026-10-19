---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=pl
fetched_at: 2026-10-19T05:59:28.242979+00:00
title: "Wykonanie kodu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Model Gemini 4 Argon jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wykonanie kodu

Interfejs Gemini API udostępnia narzędzie do wykonywania kodu, które umożliwia modelowi generowanie i uruchamianie kodu w Pythonie. Model może się wtedy uczyć iteracyjnie na podstawie wyników wykonywania kodu, aż uzyska ostateczne dane wyjściowe. Wykonanie kodu możesz wykorzystać do tworzenia aplikacji, które korzystają z wnioskowania opartego na kodzie. Możesz na przykład użyć wykonania kodu do rozwiązywania równań lub przetwarzania tekstu. Możesz też używać [bibliotek](#supported-libraries) zawartych w środowisku wykonywania kodu do wykonywania bardziej specjalistycznych zadań.

Gemini może wykonywać kod tylko w Pythonie. Nadal możesz poprosić Gemini o wygenerowanie kodu w innym języku, ale model nie może użyć narzędzia do wykonywania kodu, aby go uruchomić.

## Włączanie wykonywania kodu

Aby włączyć wykonywanie kodu, skonfiguruj narzędzie do wykonywania kodu w modelu. Dzięki temu model może generować i uruchamiać kod.

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

Dane wyjściowe mogą wyglądać mniej więcej tak (są sformatowane dla lepszej czytelności):

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

Te dane wyjściowe łączą kilka części treści, które model zwraca podczas wykonywania kodu:

- `text`: tekst wstawiony wygenerowany przez model
- `code_execution_call`: kod wygenerowany przez model, który ma zostać wykonany
- `code_execution_result`: wynik kodu wykonywalnego

## Wykonywanie kodu z obrazami (Gemini 3)

Model Gemini 3 Flash może teraz pisać i wykonywać kod w Pythonie, aby aktywnie manipulować obrazami i je analizować.

**Przypadki użycia**

- **Powiększanie i sprawdzanie**: model niejawnie wykrywa, kiedy szczegóły są zbyt małe
  (np. odczytywanie odległego wskaźnika), i pisze kod, aby przyciąć i ponownie sprawdzić obszar
  w wyższej rozdzielczości.
- **Matematyka wizualna**: model może wykonywać obliczenia wieloetapowe za pomocą kodu (np.
  sumowanie pozycji na paragonie).
- **Adnotacje do obrazów**: model może dodawać adnotacje do obrazów, aby odpowiadać na pytania, np.
  rysować strzałki wskazujące relacje.

## Włączanie wykonywania kodu z obrazami

Wykonywanie kodu z obrazami jest oficjalnie obsługiwane w Gemini 3 Flash. Możesz aktywować to działanie, włączając zarówno wykonywanie kodu jako narzędzie, jak i myślenie.

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

## Używanie wykonywania kodu w interakcjach wieloetapowych

Wykonywanie kodu możesz też używać w ramach rozmowy wieloetapowej za pomocą parametru `previous_interaction_id`.

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

## Wejście/wyjście (I/O)

W obecnych modelach Gemini, takich jak
[Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=pl), wykonywanie kodu
obsługuje wejście pliku i wyjście wykresu. Dzięki tym możliwościom wejścia i wyjścia
możesz przesyłać pliki CSV i tekstowe, zadawać pytania dotyczące tych
plików oraz generować wykresy [Matplotlib](https://matplotlib.org/) w ramach
odpowiedzi. Pliki wyjściowe są zwracane jako obrazy wstawione w odpowiedzi.

### Ceny operacji wejścia/wyjścia

Gdy używasz operacji wejścia/wyjścia wykonywania kodu, opłaty są naliczane za tokeny wejściowe i wyjściowe:

**Tokeny wejściowe:**

- Prompt użytkownika

**Tokeny wyjściowe:**

- Kod wygenerowany przez model
- Dane wyjściowe wykonywania kodu w środowisku kodu
- Tokeny myślenia
- Podsumowanie wygenerowane przez model

### Szczegóły operacji wejścia/wyjścia

Podczas pracy z operacjami wejścia/wyjścia wykonywania kodu pamiętaj o tych szczegółach technicznych:

- Maksymalny czas działania środowiska kodu to 30 sekund.
- Jeśli środowisko kodu wygeneruje błąd, model może zdecydować się na ponowne wygenerowanie danych wyjściowych kodu. Może się to zdarzyć maksymalnie 5 razy.
- Maksymalny rozmiar pliku wejściowego jest ograniczony przez okno tokena modelu. Jeśli prześlesz plik, który przekracza maksymalne okno kontekstu modelu, interfejs API zwróci błąd.
- Wykonywanie kodu najlepiej sprawdza się w przypadku plików tekstowych i CSV.
- Plik wejściowy można przekazać jako dane wstawione lub przesłać za pomocą interfejsu
  [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl),
  a plik wyjściowy jest zawsze zwracany jako dane wstawione.

## Płatności

Włączenie wykonywania kodu w interfejsie Gemini API nie wiąże się z dodatkowymi opłatami.
Opłaty będą naliczane według aktualnej stawki za tokeny wejściowe i wyjściowe na podstawie używanego modelu Gemini.

Oto kilka innych informacji o płatnościach za wykonywanie kodu:

- Opłata jest naliczana tylko raz za tokeny wejściowe przekazywane do modelu oraz za tokeny wyjściowe zwracane przez model.
- Tokeny reprezentujące wygenerowany kod są liczone jako tokeny wyjściowe. Wygenerowany kod może zawierać tekst i dane wyjściowe multimodalne, takie jak obrazy.
- Wyniki wykonywania kodu są też liczone jako tokeny wyjściowe.

Model płatności jest przedstawiony na tym diagramie:

![model rozliczeniowy wykonywania kodu](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=pl)

- Opłaty będą naliczane według aktualnej stawki za tokeny wejściowe i wyjściowe na podstawie używanego modelu Gemini.
- Jeśli Gemini używa wykonywania kodu podczas generowania odpowiedzi, oryginalny prompt, wygenerowany kod i wynik wykonanego kodu są oznaczane jako *tokeny pośrednie* i rozliczane jako *tokeny wejściowe*.
- Gemini generuje następnie podsumowanie i zwraca wygenerowany kod, wynik wykonanego kodu oraz podsumowanie końcowe. Są one rozliczane jako *tokeny wyjściowe*.
- Interfejs Gemini API zawiera w odpowiedzi interfejsu API liczbę tokenów pośrednich, dzięki czemu wiesz, dlaczego otrzymujesz dodatkowe tokeny wejściowe poza początkowym promptem.

## Ograniczenia

- Model może tylko generować i wykonywać kod. Nie może zwracać innych artefaktów, takich jak pliki multimedialne.
- W niektórych przypadkach włączenie wykonywania kodu może prowadzić do regresji w innych obszarach danych wyjściowych modelu (np. pisania opowieści).
- Różne modele mają różną zdolność do skutecznego wykonywania kodu.

## Obsługiwane kombinacje narzędzi

Narzędzie do wykonywania kodu można łączyć z
[powiązaniem ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), aby
obsługiwać bardziej złożone przypadki użycia.

Modele Gemini 4 i Gemini 3 obsługują łączenie narzędzi wbudowanych (takich jak wykonywanie kodu) z narzędziami niestandardowymi (wywoływanie funkcji).

## Obsługiwane biblioteki

Środowisko wykonywania kodu zawiera te biblioteki:

- attrs
- szachy
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
- przygotowywanie pakietów
- pandy
- poduszka
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
- sześć
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

Nie możesz instalować własnych bibliotek.

## Co dalej?

- Wypróbuj przewodnik [Krótkie wprowadzenie do interfejsu Interactions API](https://ai.google.dev/gemini-api/docs/quickstart?hl=pl).
- Więcej informacji o innych narzędziach interfejsu Gemini API:
  - [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
  - [Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-10-13 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-10-13 UTC."],[],[]]
