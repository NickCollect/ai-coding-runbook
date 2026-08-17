---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=pl
fetched_at: 2026-08-17T02:30:59.384426+00:00
title: "Wykonanie kodu \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Wykonanie kodu

Interfejs Gemini API udostępnia narzędzie do wykonywania kodu, które umożliwia modelowi generowanie i uruchamianie kodu Pythona. Model może się uczyć iteracyjnie na podstawie wyników wykonywania kodu, aż uzyska ostateczne dane wyjściowe. Możesz używać wykonywania kodu do tworzenia aplikacji, które korzystają z wnioskowania opartego na kodzie. Możesz na przykład używać wykonywania kodu do rozwiązywania równań lub przetwarzania tekstu. Możesz też używać [bibliotek](#supported-libraries) zawartych w środowisku wykonywania kodu do wykonywania bardziej specjalistycznych zadań.

Gemini może wykonywać tylko kod w Pythonie. Nadal możesz poprosić Gemini o wygenerowanie kodu w innym języku, ale model nie może użyć narzędzia do wykonywania kodu, aby go uruchomić.

## Włączanie wykonywania kodu

Aby włączyć wykonywanie kodu, skonfiguruj narzędzie do wykonywania kodu w modelu. Dzięki temu model może generować i uruchamiać kod.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

let response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: [
    "What is the sum of the first 50 prime numbers? " +
      "Generate and run code for the calculation, and make sure you get all 50.",
  ],
  config: {
    tools: [{ codeExecution: {} }],
  },
});

const parts = response?.candidates?.[0]?.content?.parts || [];
parts.forEach((part) => {
  if (part.text) {
    console.log(part.text);
  }

  if (part.executableCode && part.executableCode.code) {
    console.log(part.executableCode.code);
  }

  if (part.codeExecutionResult && part.codeExecutionResult.output) {
    console.log(part.codeExecutionResult.output);
  }
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        genai.Text("What is the sum of the first 50 prime numbers? " +
                  "Generate and run code for the calculation, and make sure you get all 50."),
        config,
    )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d ' {"tools": [{"code_execution": {}}],
    "contents": {
      "parts":
        {
            "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
        }
    },
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

- `text`: tekst wbudowany wygenerowany przez model,
- `executableCode`: kod wygenerowany przez model, który ma zostać wykonany,
- `codeExecutionResult`: wynik wykonania kodu,

Konwencje nazewnictwa tych części różnią się w zależności od języka programowania.

## Wykonywanie kodu z obrazami (Gemini 3)

Model Gemini 3 Flash może teraz pisać i wykonywać kod Pythona, aby aktywnie manipulować obrazami i je sprawdzać.

**Przypadki użycia**

- **Powiększanie i sprawdzanie**: model automatycznie wykrywa, kiedy szczegóły są zbyt małe
  (np. odczytanie odległego wskaźnika), i pisze kod, aby przyciąć i ponownie sprawdzić obszar
  w wyższej rozdzielczości.
- **Matematyka wizualna**: model może wykonywać obliczenia wieloetapowe za pomocą kodu (np.
  sumowanie pozycji na paragonie).
- **Adnotacje do obrazów**: model może dodawać adnotacje do obrazów, aby odpowiadać na pytania, takie
  jak rysować strzałki wskazujące relacje.

### Włączanie wykonywania kodu z obrazami

Wykonywanie kodu z obrazami jest oficjalnie obsługiwane w Gemini 3 Flash. Możesz aktywować to działanie, włączając zarówno wykonywanie kodu jako narzędzie, jak i myślenie.

### Python

```
from google import genai
from google.genai import types
import requests
from PIL import Image
import io

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

# Ensure you have your API key set
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[image, "Zoom into the expression pedals and tell me how many pedals are there?"],
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
    if part.as_image() is not None:
        # display() is a standard function in Jupyter/Colab notebooks
        display(Image.open(io.BytesIO(part.as_image().image_bytes)))
```

### JavaScript

```
async function main() {
  const ai = new GoogleGenAI({ });

  // 1. Prepare Image Data
  const imageUrl = "https://goo.gle/instrument-img";
  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  // 2. Call the API with Code Execution enabled
  const result = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: [
      {
        inlineData: {
          mimeType: 'image/jpeg',
          data: base64ImageData,
        },
      },
      { text: "Zoom into the expression pedals and tell me how many pedals are there?" }
    ],
    config: {
      tools: [{ codeExecution: {} }],
    },
  });

  // 3. Process the response (Text, Code, and Execution Results)
  const candidates = result.candidates;
  if (candidates && candidates[0].content.parts) {
    for (const part of candidates[0].content.parts) {
      if (part.text) {
        console.log("Text:", part.text);
      }
      if (part.executableCode) {
        console.log(`\nGenerated Code (${part.executableCode.language}):\n`, part.executableCode.code);
      }
      if (part.codeExecutionResult) {
        console.log(`\nExecution Output (${part.codeExecutionResult.outcome}):\n`, part.codeExecutionResult.output);
      }
    }
  }
}

main();
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

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    // Initialize Client (Reads GEMINI_API_KEY from env)
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    // 1. Download the image
    imageResp, err := http.Get("https://goo.gle/instrument-img")
    if err != nil {
        log.Fatal(err)
    }
    defer imageResp.Body.Close()

    imageBytes, err := io.ReadAll(imageResp.Body)
    if err != nil {
        log.Fatal(err)
    }

    // 2. Configure Code Execution Tool
    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    // 3. Generate Content
    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        []*genai.Content{
            {
                Parts: []*genai.Part{
                    {InlineData: &genai.Blob{MIMEType: "image/jpeg", Data: imageBytes}},
                    {Text: "Zoom into the expression pedals and tell me how many pedals are there?"},
                },
                Role: "user",
            },
        },
        config,
    )
    if err != nil {
        log.Fatal(err)
    }

    // 4. Parse Response (Text, Code, Output)
    for _, cand := range result.Candidates {
        for _, part := range cand.Content.Parts {
            if part.Text != "" {
                fmt.Println("Text:", part.Text)
            }
            if part.ExecutableCode != nil {
                fmt.Printf("\nGenerated Code (%s):\n%s\n", 
                    part.ExecutableCode.Language, 
                    part.ExecutableCode.Code)
            }
            if part.CodeExecutionResult != nil {
                fmt.Printf("\nExecution Output (%s):\n%s\n", 
                    part.CodeExecutionResult.Outcome, 
                    part.CodeExecutionResult.Output)
            }
        }
    }
}
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"
MODEL="gemini-3.6-flash"

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

curl "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"'"$MIME_TYPE"'",
                "data": "'"$IMAGE_B64"'"
              }
            },
            {"text": "Zoom into the expression pedals and tell me how many pedals are there?"}
        ]
      }],
      "tools": [
        {
          "code_execution": {}
        }
      ]
    }'
```

## Używanie wykonywania kodu w czacie

Możesz też używać wykonywania kodu w ramach czatu.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.6-flash",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

response = chat.send_message("I have a math question for you.")
print(response.text)

response = chat.send_message(
    "What is the sum of the first 50 prime numbers? "
    "Generate and run code for the calculation, and make sure you get all 50."
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
```

### JavaScript

```
import {GoogleGenAI} from "@google/genai";

const ai = new GoogleGenAI({});

const chat = ai.chats.create({
  model: "gemini-3.6-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "I have a math question for you:" }],
    },
    {
      role: "model",
      parts: [{ text: "Great! I'm ready for your math question. Please ask away." }],
    },
  ],
  config: {
    tools: [{codeExecution:{}}],
  }
});

const response = await chat.sendMessage({
  message: "What is the sum of the first 50 prime numbers? " +
            "Generate and run code for the calculation, and make sure you get all 50."
});
console.log("Chat response:", response.text);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        Tools: []*genai.Tool{
            {CodeExecution: &genai.ToolCodeExecution{}},
        },
    }

    chat, _ := client.Chats.Create(
        ctx,
        "gemini-3.6-flash",
        config,
        nil,
    )

    result, _ := chat.SendMessage(
                    ctx,
                    genai.Part{Text: "What is the sum of the first 50 prime numbers? " +
                                          "Generate and run code for the calculation, and " +
                                          "make sure you get all 50.",
                              },
                )

    fmt.Println(result.Text())
    fmt.Println(result.ExecutableCode())
    fmt.Println(result.CodeExecutionResult())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{"tools": [{"code_execution": {}}],
    "contents": [
        {
            "role": "user",
            "parts": [{
                "text": "Write code to print \"Hello world!\" and execute it"
            }]
        },{
            "role": "model",
            "parts": [
              {
                "executable_code": {
                  "id": "a1b2c3d4",
                  "language": "PYTHON",
                  "code": "\nprint(\"hello world!\")\n"
                }
                "thought_signature": "..."
              },
              {
                "code_execution_result": {
                  "id": "a1b2c3d4",
                  "outcome": "OUTCOME_OK",
                  "output": "hello world!\n"
                }
              },
              {
                "text": "I have printed \"hello world!\" using the provided python code block. \n",
                "thought_signature": "..."
              }
            ],
        },{
            "role": "user",
            "parts": [{
                "text": "What is the sum of the first 50 prime numbers? Generate and run code for the calculation, and make sure you get all 50."
            }]
        }
    ]
}'
```

## Wejście/wyjście (I/O)

Wykonywanie kodu obsługuje dane wejściowe z plików i dane wyjściowe w postaci wykresów. Dzięki tym możliwościom wejścia i
wyjścia możesz przesyłać pliki CSV i tekstowe, zadawać pytania dotyczące
plików oraz generować [wykresy Matplotlib](https://matplotlib.org/) w ramach
odpowiedzi. Pliki wyjściowe są zwracane jako obrazy wbudowane w odpowiedź.

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
- Maksymalny rozmiar pliku wejściowego jest ograniczony przez okno tokenów modelu. W AI Studio maksymalny rozmiar pliku wejściowego to 1 milion tokenów (około 2 MB w przypadku plików tekstowych obsługiwanych typów danych wejściowych). Jeśli prześlesz zbyt duży plik, AI Studio nie pozwoli Ci go wysłać.
- Wykonywanie kodu najlepiej sprawdza się w przypadku plików tekstowych i CSV.
- Plik wejściowy można przekazać w `part.inlineData` lub `part.fileData` (przesłany
  za pomocą [interfejsu Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl)), a plik wyjściowy jest zawsze
  zwracany jako `part.inlineData`.

## Płatności

Włączenie wykonywania kodu z interfejsu Gemini API nie wiąże się z żadnymi dodatkowymi opłatami.
Opłaty będą naliczane według aktualnej stawki za tokeny wejściowe i wyjściowe na podstawie używanego modelu Gemini.

Oto kilka dodatkowych informacji o płatnościach za wykonywanie kodu:

- Opłata za tokeny wejściowe przekazywane do modelu jest naliczana tylko raz. Opłata jest naliczana za tokeny wyjściowe zwracane przez model.
- Tokeny reprezentujące wygenerowany kod są liczone jako tokeny wyjściowe. Wygenerowany kod może zawierać tekst i dane wyjściowe multimodalne, takie jak obrazy.
- Wyniki wykonywania kodu są również liczone jako tokeny wyjściowe.

Model płatności jest przedstawiony na tym diagramie:

![model rozliczeniowy wykonania kodu,](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=pl)

- Opłaty będą naliczane według aktualnej stawki za tokeny wejściowe i wyjściowe na podstawie używanego modelu Gemini.
- Jeśli Gemini używa wykonywania kodu podczas generowania odpowiedzi, oryginalny prompt, wygenerowany kod i wynik wykonania kodu są oznaczane jako *tokeny pośrednie* i rozliczane jako *tokeny wejściowe*.
- Następnie Gemini generuje podsumowanie i zwraca wygenerowany kod, wynik wykonania kodu oraz podsumowanie końcowe. Są one rozliczane jako *tokeny wyjściowe*.
- Interfejs Gemini API zawiera w odpowiedzi API liczbę tokenów pośrednich, dzięki czemu wiesz, dlaczego otrzymujesz dodatkowe tokeny wejściowe poza początkowym promptem.

## Ograniczenia

- Model może tylko generować i wykonywać kod. Nie może zwracać innych artefaktów, takich jak pliki multimedialne.
- W niektórych przypadkach włączenie wykonywania kodu może prowadzić do regresji w innych obszarach danych wyjściowych modelu (np. pisania opowieści).
- Różne modele mają różną zdolność do skutecznego wykonywania kodu.

## Obsługiwane kombinacje narzędzi

Narzędzie do wykonywania kodu można łączyć z
[powiązaniem ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/google-search?hl=pl), aby
obsługiwać bardziej złożone przypadki użycia.

Modele Gemini 3 obsługują łączenie wbudowanych narzędzi (takich jak wykonywanie kodu) z narzędziami niestandardowymi (wywoływanie funkcji). Aby kombinacja narzędzi działała, musisz przekazać pola `id` i `thought_signature`. Więcej informacji znajdziesz na
[stronie dotyczącej kombinacji narzędzi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=pl).

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

- Wypróbuj Colab z wykonywaniem kodu
  [.](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=pl)
- Dowiedz się więcej o innych narzędziach interfejsu Gemini API:
  - [Wywoływanie funkcji](https://ai.google.dev/gemini-api/docs/function-calling?hl=pl)
  - [Powiązanie ze źródłami informacji przy użyciu wyszukiwarki Google](https://ai.google.dev/gemini-api/docs/grounding?hl=pl)

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
