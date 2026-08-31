---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/code-execution?hl=es-419
fetched_at: 2026-08-31T06:41:51.446084+00:00
title: "Ejecuci\u00f3n de c\u00f3digo \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

La [API de Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=es-419) ya está disponible de forma general. Te recomendamos que uses esta API para acceder a todos los modelos y funciones más recientes.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Ejecución de código

La API de Gemini proporciona una herramienta de ejecución de código que permite que el modelo genere y ejecute código de Python. Luego, el modelo puede aprender de forma iterativa a partir de los resultados de la ejecución de código hasta llegar a un resultado final. Puedes usar la ejecución de código para crear aplicaciones que se beneficien del razonamiento basado en código. Por ejemplo, puedes usar la ejecución de código para resolver ecuaciones o procesar texto. También puedes
usar las [bibliotecas](#supported-libraries) incluidas en el entorno de ejecución de código
para realizar tareas más especializadas.

Gemini solo puede ejecutar código en Python. Aun así, puedes pedirle a Gemini que genere código en otro lenguaje, pero el modelo no puede usar la herramienta de ejecución de código para ejecutarlo.

## Habilita la ejecución de código

Para habilitar la ejecución de código, configura la herramienta de ejecución de código en el modelo. Esto permite que el modelo genere y ejecute código.

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

El resultado podría ser similar al siguiente, que se formateó para mejorar la legibilidad:

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

Este resultado combina varias partes de contenido que el modelo muestra cuando se usa la ejecución de código:

- `text`: Texto intercalado generado por el modelo
- `executableCode`: Código generado por el modelo que se debe ejecutar
- `codeExecutionResult`: Resultado del código ejecutable

Las convenciones de nomenclatura para estas partes varían según el lenguaje de programación.

## Ejecución de código con imágenes (Gemini 3)

El modelo Gemini 3 Flash ahora puede escribir y ejecutar código de Python para manipular y examinar imágenes de forma activa.

**Casos de uso**

- **Acercar y examinar**: El modelo detecta de forma implícita cuando los detalles son demasiado pequeños
  (p.ej., leer un indicador distante) y escribe código para recortar y volver a examinar el área
  con una resolución más alta.
- **Matemáticas visuales**: El modelo puede ejecutar cálculos de varios pasos con código (p.ej.,
  sumar los artículos de una factura).
- **Anotación de imágenes**: El modelo puede anotar imágenes para responder preguntas, como
  dibujar flechas para mostrar relaciones.

### Habilita la ejecución de código con imágenes

La ejecución de código con imágenes se admite oficialmente en Gemini 3 Flash. Puedes activar este comportamiento habilitando la ejecución de código como herramienta y el razonamiento.

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

## Usa la ejecución de código en el chat

También puedes usar la ejecución de código como parte de un chat.

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

## Entrada y salida (E/S)

La ejecución de código admite la entrada de archivos y la salida de gráficos. Con estas capacidades de entrada y
salida, puedes subir archivos CSV y de texto, hacer preguntas sobre los
archivos y generar gráficos de [Matplotlib](https://matplotlib.org/) como parte
de la respuesta. Los archivos de salida se muestran como imágenes intercaladas en la respuesta.

### Precios de E/S

Cuando usas la E/S de ejecución de código, se te cobra por los tokens de entrada y salida:

**Tokens de entrada:**

- Instrucción del usuario

**Tokens de salida:**

- Código generado por el modelo
- Resultado de la ejecución de código en el entorno de código
- Tokens de razonamiento
- Resumen generado por el modelo

### Detalles de E/S

Cuando trabajes con la E/S de ejecución de código, ten en cuenta los siguientes detalles técnicos:

- El tiempo de ejecución máximo del entorno de código es de 30 segundos.
- Si el entorno de código genera un error, es posible que el modelo decida volver a generar el resultado del código. Esto puede suceder hasta 5 veces.
- El tamaño máximo de entrada de archivos está limitado por la ventana de tokens del modelo. En AI Studio, el tamaño máximo del archivo de entrada es de 1 millón de tokens (aproximadamente 2 MB para archivos de texto de los tipos de entrada admitidos). Si subes un archivo demasiado grande, AI Studio no te permitirá enviarlo.
- La ejecución de código funciona mejor con archivos de texto y CSV.
- El archivo de entrada se puede pasar en `part.inlineData` o `part.fileData` (subido
  a través de la [API de Files](https://ai.google.dev/gemini-api/docs/files?hl=es-419)), y el archivo de salida siempre
  se muestra como `part.inlineData`.

## Facturación

No hay cargos adicionales por habilitar la ejecución de código desde la API de Gemini.
Se te facturará según la tarifa actual de los tokens de entrada y salida en función del modelo de Gemini que uses.

Estos son algunos aspectos que debes tener en cuenta sobre la facturación de la ejecución de código:

- Solo se te factura una vez por los tokens de entrada que pasas al modelo, y se te factura por los tokens de salida finales que te muestra el modelo.
- Los tokens que representan el código generado se cuentan como tokens de salida. El código generado puede incluir texto y salida multimodal, como imágenes.
- Los resultados de la ejecución de código también se cuentan como tokens de salida.

El modelo de facturación se muestra en el siguiente diagrama:

![Modelo de facturación de ejecución de código](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=es-419)

- Se te facturará según la tarifa actual de los tokens de entrada y salida en función del modelo de Gemini que uses.
- Si Gemini usa la ejecución de código cuando genera tu respuesta, la instrucción original, el código generado y el resultado del código ejecutado se etiquetan como *tokens intermedios* y se facturan como *tokens de entrada*.
- Luego, Gemini genera un resumen y muestra el código generado, el resultado del código ejecutado y el resumen final. Estos se facturan como *tokens de salida*.
- La API de Gemini incluye un recuento de tokens intermedios en la respuesta de la API, por lo que sabes por qué obtienes tokens de entrada adicionales más allá de tu instrucción inicial.

## Limitaciones

- El modelo solo puede generar y ejecutar código. No puede mostrar otros artefactos, como archivos multimedia.
- En algunos casos, habilitar la ejecución de código puede provocar regresiones en otras áreas del resultado del modelo (por ejemplo, escribir una historia).
- Existe cierta variación en la capacidad de los diferentes modelos para usar la ejecución de código de forma correcta.

## Combinaciones de herramientas compatibles

La herramienta de ejecución de código se puede combinar con
[Fundamentación con la Búsqueda de Google](https://ai.google.dev/gemini-api/docs/google-search?hl=es-419) para
potenciar casos de uso más complejos.

Los modelos de Gemini 3 admiten la combinación de herramientas integradas (como la ejecución de código) con herramientas personalizadas (llamadas a funciones). Debes volver a pasar los campos `id` y `thought_signature` para que funcione la combinación de herramientas. Obtén más información en la
[página de combinaciones de herramientas](https://ai.google.dev/gemini-api/docs/tool-combination?hl=es-419).

## Bibliotecas compatibles

El entorno de ejecución de código incluye las siguientes bibliotecas:

- attrs
- ajedrez
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
- empaquetado
- pandas
- almohada
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
- six
- striprtf
- sympy
- tabulate
- tensorflow
- toolz
- xlrd

No puedes instalar tus propias bibliotecas.

## ¿Qué sigue?

- Prueba el
  [Colab de ejecución de código](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb?hl=es-419).
- Obtén información sobre otras herramientas de la API de Gemini:
  - [Llamada a función](https://ai.google.dev/gemini-api/docs/function-calling?hl=es-419)
  - [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding?hl=es-419)

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-07-30 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-07-30 (UTC)"],[],[]]
