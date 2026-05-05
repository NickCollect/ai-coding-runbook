---
source_url: https://ai.google.dev/gemini-api/docs/code-execution?hl=fr
fetched_at: 2026-05-05T13:09:14.809078+00:00
title: "Ex\u00e9cution de code \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/recherche approfondie Gemini) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

- [Accueil](https://ai.google.dev/gemini-api/docs/Accueil)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Docs](https://ai.google.dev/gemini-api/docs/Docs)

Envoyer des commentaires

# Exécution de code

L'API Gemini fournit un outil d'exécution de code qui permet au modèle de générer et d'exécuter du code Python. Le modèle peut ensuite apprendre de manière itérative à partir des résultats de l'exécution du code jusqu'à ce qu'il parvienne à une sortie finale. Vous pouvez utiliser l'exécution de code pour créer des applications qui bénéficient d'un raisonnement basé sur du code. Par exemple, vous pouvez utiliser l'exécution de code pour résoudre des équations ou traiter du texte. Vous pouvez
également utiliser les [bibliothèques](https://ai.google.dev/gemini-api/docs/bibliothèques) incluses dans l'environnement d'exécution de code
pour effectuer des tâches plus spécialisées.

Gemini ne peut exécuter du code qu'en Python. Vous pouvez toujours demander à Gemini de générer du code dans un autre langage, mais le modèle ne peut pas utiliser l'outil d'exécution de code pour l'exécuter.

## Activer l'exécution de code

Pour activer l'exécution de code, configurez l'outil d'exécution de code sur le modèle. Cela permet au modèle de générer et d'exécuter du code.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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
        "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

La sortie peut ressembler à ce qui suit, qui a été mis en forme pour faciliter la lecture :

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

Cette sortie combine plusieurs parties de contenu renvoyées par le modèle lors de l'utilisation de l'exécution de code :

- `text` : texte intégré généré par le modèle
- `executableCode` : code généré par le modèle et destiné à être exécuté
- `codeExecutionResult` : résultat du code exécutable

Les conventions d'attribution de noms pour ces parties varient selon le langage de programmation.

## Exécution de code avec des images (Gemini 3)

Le modèle Gemini 3 Flash peut désormais écrire et exécuter du code Python pour manipuler et inspecter activement des images.

**Cas d'utilisation**

- **Zoom et inspection** : le modèle détecte implicitement lorsque les détails sont trop petits
  (par exemple, la lecture d'une jauge éloignée) et écrit du code pour recadrer et réexaminer la zone
  à une résolution plus élevée.
- **Mathématiques visuelles** : le modèle peut exécuter des calculs en plusieurs étapes à l'aide de code (par exemple,
  additionner les éléments d'une facture).
- **Annotation d'images** : le modèle peut annoter des images pour répondre à des questions, par exemple
  en dessinant des flèches pour montrer des relations.

### Activer l'exécution de code avec des images

L'exécution de code avec des images est officiellement compatible avec Gemini 3 Flash. Vous pouvez activer ce comportement en activant à la fois l'exécution de code en tant qu'outil et la réflexion.

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
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
        "gemini-3-flash-preview",
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
MODEL="gemini-3-flash-preview"

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

## Utiliser l'exécution de code dans le chat

Vous pouvez également utiliser l'exécution de code dans un chat.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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
        "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## Entrée/Sortie (E/S)

L'exécution de code est compatible avec l'entrée de fichier et la sortie de graphique. Grâce à ces fonctionnalités d'entrée et de
sortie, vous pouvez importer des fichiers CSV et des fichiers texte, poser des questions sur les
fichiers et générer des graphiques [Matplotlib](https://ai.google.dev/gemini-api/docs/Matplotlib) dans la réponse. Les fichiers de sortie sont renvoyés en tant qu'images intégrées dans la réponse.

### Tarifs d'E/S

Lorsque vous utilisez l'E/S d'exécution de code, vous êtes facturé pour les jetons d'entrée et les jetons de sortie :

**Jetons d'entrée** :

- Prompt de l'utilisateur

**Jetons de sortie** :

- Code généré par le modèle
- Sortie d'exécution de code dans l'environnement de code
- Jetons de réflexion
- Résumé généré par le modèle

### Détails d'E/S

Lorsque vous utilisez l'E/S d'exécution de code, tenez compte des détails techniques suivants :

- La durée d'exécution maximale de l'environnement de code est de 30 secondes.
- Si l'environnement de code génère une erreur, le modèle peut décider de régénérer la sortie de code. Cela peut se produire jusqu'à cinq fois.
- La taille maximale de l'entrée de fichier est limitée par la fenêtre de jetons du modèle. Dans AI Studio, la taille maximale du fichier d'entrée est de 1 million de jetons (environ 2 Mo pour les fichiers texte des types d'entrée compatibles). Si vous importez un fichier trop volumineux, AI Studio ne vous permettra pas de l'envoyer.
- L'exécution de code fonctionne mieux avec les fichiers texte et CSV.
- Le fichier d'entrée peut être transmis dans `part.inlineData` ou `part.fileData` (importé
  via l'[API Files](https://ai.google.dev/gemini-api/docs/API Files)), et le fichier de sortie est toujours
  renvoyé en tant que `part.inlineData`.

## Facturation

L'exécution de code à partir de l'API Gemini n'entraîne aucuns frais supplémentaires.
Vous serez facturé au tarif actuel des jetons d'entrée et de sortie en fonction du modèle Gemini que vous utilisez.

Voici quelques autres points à connaître concernant la facturation de l'exécution du code :

- Vous ne serez facturé qu'une seule fois pour les jetons d'entrée que vous transmettez au modèle, et vous serez facturé pour les jetons de sortie finaux qui vous sont renvoyés par le modèle.
- Les jetons représentant le code généré sont comptabilisés comme des jetons de sortie. Le code généré peut inclure du texte et une sortie multimodale comme des images.
- Les résultats de l'exécution du code sont également comptabilisés comme des jetons de sortie.

Le modèle de facturation est présenté dans le schéma suivant :

![Modèle de facturation de l&#39;exécution de code](https://ai.google.dev/static/gemini-api/docs/images/code-execution-diagram.png?hl=fr)

- Vous êtes facturé au tarif actuel des jetons d'entrée et de sortie en fonction du modèle Gemini que vous utilisez.
- Si Gemini utilise l'exécution de code pour générer votre réponse, le prompt d'origine, le code généré et le résultat du code exécuté sont désignés comme des *jetons intermédiaires* et sont facturés en tant que *jetons d'entrée*.
- Gemini génère ensuite un résumé et renvoie le code généré, le résultat du code exécuté et le résumé final. Ils sont facturés en tant que *jetons de sortie*.
- L'API Gemini inclut un nombre de jetons intermédiaires dans la réponse de l'API. Vous savez ainsi pourquoi vous obtenez des jetons d'entrée supplémentaires au-delà de votre prompt initial.

## Limites

- Le modèle ne peut que générer et exécuter du code. Il ne peut pas renvoyer d'autres artefacts tels que des fichiers multimédias.
- Dans certains cas, l'activation de l'exécution du code peut entraîner des régressions dans d'autres domaines de la sortie du modèle (par exemple, l'écriture d'une histoire).
- La capacité des différents modèles à utiliser l'exécution de code varie.

## Combinaisons d'outils compatibles

L'outil d'exécution de code peut être combiné avec
[l'ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/l'ancrage avec la recherche Google) pour
des cas d'utilisation plus complexes.

Les modèles Gemini 3 sont compatibles avec la combinaison d'outils intégrés (comme l'exécution de code) et d'outils personnalisés (appel de fonction). Vous devez renvoyer les champs `id` et `thought_signature` pour que la combinaison d'outils fonctionne. Pour en savoir plus, consultez la
[page sur les combinaisons d'outils](https://ai.google.dev/gemini-api/docs/page sur les combinaisons d'outils).

## Bibliothèques prises en charge

L'environnement d'exécution du code inclut les bibliothèques suivantes :

- attrs
- échecs
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
- packaging
- pandas
- pillow
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

Vous ne pouvez pas installer vos propres bibliothèques.

## Étape suivante

- Essayez l'
  [atelier de programmation sur l'exécution de code](https://ai.google.dev/gemini-api/docs/atelier de programmation sur l'exécution de code).
- Découvrez d'autres outils de l'API Gemini :
  - [Appel de fonction](https://ai.google.dev/gemini-api/docs/Appel de fonction)
  - [Ancrage avec la recherche Google](https://ai.google.dev/gemini-api/docs/Ancrage avec la recherche Google)

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/Creative Commons Attribution 4.0), et les échantillons de code sont régis par une licence [Apache 2.0](https://ai.google.dev/gemini-api/docs/Apache 2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://ai.google.dev/gemini-api/docs/Règles du site Google Developers). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/04/29 (UTC).

Voulez-vous nous donner plus d'informations ?
