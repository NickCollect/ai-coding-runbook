---
source_url: https://ai.google.dev/gemini-api/docs/structured-output?hl=it
fetched_at: 2026-05-05T13:27:13.073366+00:00
title: "Output strutturati \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/Gemini Deep Research) è ora disponibile in anteprima con pianificazione collaborativa, visualizzazione, supporto MCP e altro ancora.

- [Home page](https://ai.google.dev/gemini-api/docs/Home page)
- [Gemini API](https://ai.google.dev/gemini-api/docs/Gemini API)
- [Documenti](https://ai.google.dev/gemini-api/docs/Documenti)

Invia feedback

# Output strutturati

Puoi configurare i modelli Gemini per generare risposte conformi a uno schema JSON fornito. Ciò garantisce risultati prevedibili e sicuri e semplifica l'estrazione
di dati strutturati da testo non strutturato.

L'utilizzo di output strutturati è ideale per:

- **Estrazione dei dati:** estrai informazioni specifiche come nomi e date dal testo.
- **Classificazione strutturata**:consente di classificare il testo in categorie predefinite.
- **Workflow agentici**:genera input strutturati per strumenti o API.

Oltre a supportare JSON Schema nell'API REST, gli SDK Google GenAI
semplificano la definizione degli schemi utilizzando
[Pydantic](https://ai.google.dev/gemini-api/docs/Pydantic) (Python) e
[Zod](https://ai.google.dev/gemini-api/docs/Zod) (JavaScript).

Estrai ricette
Moderazione dei contenuti
Strutture ricorsive

Questo esempio mostra come estrarre dati strutturati dal testo utilizzando tipi di schema JSON di base come `object`, `array`, `string` e `integer`.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity of the ingredient, including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description="Optional time in minutes to prepare the recipe.")
    ingredients: List[Ingredient]
    instructions: List[str]

client = genai.Client()

prompt = """
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Recipe.model_json_schema(),
    },
)

recipe = Recipe.model_validate_json(response.text)
print(recipe)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ingredientSchema = z.object({
  name: z.string().describe("Name of the ingredient."),
  quantity: z.string().describe("Quantity of the ingredient, including units."),
});

const recipeSchema = z.object({
  recipe_name: z.string().describe("The name of the recipe."),
  prep_time_minutes: z.number().optional().describe("Optional time in minutes to prepare the recipe."),
  ingredients: z.array(ingredientSchema),
  instructions: z.array(z.string()),
});

const ai = new GoogleGenAI({});

const prompt = `
Please extract the recipe from the following text.
The user wants to make delicious chocolate chip cookies.
They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
For the best part, they'll need 2 cups of semisweet chocolate chips.
First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
onto ungreased baking sheets and bake for 9 to 11 minutes.
`;

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(recipeSchema),
  },
});

const recipe = recipeSchema.parse(JSON.parse(response.text));
console.log(recipe);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    prompt := `
  Please extract the recipe from the following text.
  The user wants to make delicious chocolate chip cookies.
  They need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,
  1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,
  3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.
  For the best part, they'll need 2 cups of semisweet chocolate chips.
  First, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,
  baking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar
  until light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry
  ingredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons
  onto ungreased baking sheets and bake for 9 to 11 minutes.
  `
    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseJsonSchema: map[string]any{
            "type": "object",
            "properties": map[string]any{
                "recipe_name": map[string]any{
                    "type":        "string",
                    "description": "The name of the recipe.",
                },
                "prep_time_minutes": map[string]any{
                    "type":        "integer",
                    "description": "Optional time in minutes to prepare the recipe.",
                },
                "ingredients": map[string]any{
                    "type": "array",
                    "items": map[string]any{
                        "type": "object",
                        "properties": map[string]any{
                            "name": map[string]any{
                                "type":        "string",
                                "description": "Name of the ingredient.",
                            },
                            "quantity": map[string]any{
                                "type":        "string",
                                "description": "Quantity of the ingredient, including units.",
                            },
                        },
                        "required": []string{"name", "quantity"},
                    },
                },
                "instructions": map[string]any{
                    "type":  "array",
                    "items": map[string]any{"type": "string"},
                },
            },
            "required": []string{"recipe_name", "ingredients", "instructions"},
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text(prompt),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          { "text": "Please extract the recipe from the following text.\nThe user wants to make delicious chocolate chip cookies.\nThey need 2 and 1/4 cups of all-purpose flour, 1 teaspoon of baking soda,\n1 teaspoon of salt, 1 cup of unsalted butter (softened), 3/4 cup of granulated sugar,\n3/4 cup of packed brown sugar, 1 teaspoon of vanilla extract, and 2 large eggs.\nFor the best part, they will need 2 cups of semisweet chocolate chips.\nFirst, preheat the oven to 375°F (190°C). Then, in a small bowl, whisk together the flour,\nbaking soda, and salt. In a large bowl, cream together the butter, granulated sugar, and brown sugar\nuntil light and fluffy. Beat in the vanilla and eggs, one at a time. Gradually beat in the dry\ningredients until just combined. Finally, stir in the chocolate chips. Drop by rounded tablespoons\nonto ungreased baking sheets and bake for 9 to 11 minutes." }
        ]
      }],
      "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
          "type": "object",
          "properties": {
            "recipe_name": {
              "type": "string",
              "description": "The name of the recipe."
            },
            "prep_time_minutes": {
                "type": "integer",
                "description": "Optional time in minutes to prepare the recipe."
            },
            "ingredients": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": { "type": "string", "description": "Name of the ingredient."},
                  "quantity": { "type": "string", "description": "Quantity of the ingredient, including units."}
                },
                "required": ["name", "quantity"]
              }
            },
            "instructions": {
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["recipe_name", "ingredients", "instructions"]
        }
      }
    }'
```

**Esempio di risposta:**

```
{
  "recipe_name": "Delicious Chocolate Chip Cookies",
  "ingredients": [
    {
      "name": "all-purpose flour",
      "quantity": "2 and 1/4 cups"
    },
    {
      "name": "baking soda",
      "quantity": "1 teaspoon"
    },
    {
      "name": "salt",
      "quantity": "1 teaspoon"
    },
    {
      "name": "unsalted butter (softened)",
      "quantity": "1 cup"
    },
    {
      "name": "granulated sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "packed brown sugar",
      "quantity": "3/4 cup"
    },
    {
      "name": "vanilla extract",
      "quantity": "1 teaspoon"
    },
    {
      "name": "large eggs",
      "quantity": "2"
    },
    {
      "name": "semisweet chocolate chips",
      "quantity": "2 cups"
    }
  ],
  "instructions": [
    "Preheat the oven to 375°F (190°C).",
    "In a small bowl, whisk together the flour, baking soda, and salt.",
    "In a large bowl, cream together the butter, granulated sugar, and brown sugar until light and fluffy.",
    "Beat in the vanilla and eggs, one at a time.",
    "Gradually beat in the dry ingredients until just combined.",
    "Stir in the chocolate chips.",
    "Drop by rounded tablespoons onto ungreased baking sheets and bake for 9 to 11 minutes."
  ]
}
```

## Streaming

Puoi trasmettere in streaming gli output strutturati, il che ti consente di iniziare a elaborare la risposta man mano che viene generata, senza dover attendere il completamento dell'intero output. In questo modo, puoi migliorare le prestazioni percepite della tua applicazione.

I chunk trasmessi in streaming saranno stringhe JSON parziali valide, che possono essere
concatenate per formare l'oggetto JSON finale completo.

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
    sentiment: Literal["positive", "neutral", "negative"]
    summary: str

client = genai.Client()
prompt = "The new UI is incredibly intuitive and visually appealing. Great job. Add a very long summary to test streaming!"

response_stream = client.models.generate_content_stream(
    model="gemini-3-flash-preview",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_json_schema": Feedback.model_json_schema(),
    },
)

for chunk in response_stream:
    print(chunk.candidates[0].content.parts[0].text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});
const prompt = "The new UI is incredibly intuitive and visually appealing. Great job! Add a very long summary to test streaming!";

const feedbackSchema = z.object({
  sentiment: z.enum(["positive", "neutral", "negative"]),
  summary: z.string(),
});

const stream = await ai.models.generateContentStream({
  model: "gemini-3-flash-preview",
  contents: prompt,
  config: {
    responseMimeType: "application/json",
    responseJsonSchema: zodToJsonSchema(feedbackSchema),
  },
});

for await (const chunk of stream) {
  console.log(chunk.candidates[0].content.parts[0].text)
}
```

## Output strutturati con strumenti

Gemini 3 ti consente di combinare gli output strutturati con strumenti integrati, tra cui
[Grounding con la Ricerca Google](https://ai.google.dev/gemini-api/docs/Grounding con la Ricerca Google),
[Contesto URL](https://ai.google.dev/gemini-api/docs/Contesto URL),
[Esecuzione di codice](https://ai.google.dev/gemini-api/docs/Esecuzione di codice),
[Ricerca file](https://ai.google.dev/gemini-api/docs/Ricerca file) e
[Chiamata di funzioni](https://ai.google.dev/gemini-api/docs/Chiamata di funzioni).

### Python

```
from google import genai
from pydantic import BaseModel, Field
from typing import List

class MatchResult(BaseModel):
    winner: str = Field(description="The name of the winner.")
    final_match_score: str = Field(description="The final match score.")
    scorers: List[str] = Field(description="The name of the scorer.")

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="Search for all details for the latest Euro.",
    config={
        "tools": [
            {"google_search": {}},
            {"url_context": {}}
        ],
        "response_mime_type": "application/json",
        "response_json_schema": MatchResult.model_json_schema(),
    },  
)

result = MatchResult.model_validate_json(response.text)
print(result)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ai = new GoogleGenAI({});

const matchSchema = z.object({
  winner: z.string().describe("The name of the winner."),
  final_match_score: z.string().describe("The final score."),
  scorers: z.array(z.string()).describe("The name of the scorer.")
});

async function run() {
  const response = await ai.models.generateContent({
    model: "gemini-3.1-pro-preview",
    contents: "Search for all details for the latest Euro.",
    config: {
      tools: [
        { googleSearch: {} },
        { urlContext: {} }
      ],
      responseMimeType: "application/json",
      responseJsonSchema: zodToJsonSchema(matchSchema),
    },
  });

  const match = matchSchema.parse(JSON.parse(response.text));
  console.log(match);
}

run();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-pro-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [{
      "parts": [{"text": "Search for all details for the latest Euro."}]
    }],
    "tools": [
      {"googleSearch": {}},
      {"urlContext": {}}
    ],
    "generationConfig": {
        "responseMimeType": "application/json",
        "responseJsonSchema": {
            "type": "object",
            "properties": {
                "winner": {"type": "string", "description": "The name of the winner."},
                "final_match_score": {"type": "string", "description": "The final score."},
                "scorers": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The name of the scorer."
                }
            },
            "required": ["winner", "final_match_score", "scorers"]
        }
    }
  }'
```

## Supporto dello schema JSON

Per generare un oggetto JSON, imposta `response_mime_type` nella configurazione di generazione su `application/json` e fornisci un `response_json_schema`. Lo schema deve essere uno [schema JSON](https://ai.google.dev/gemini-api/docs/schema JSON) valido che descriva il formato di output desiderato.

Il modello genererà quindi una risposta che è una stringa JSON sintatticamente valida corrispondente allo schema fornito. Quando utilizzi output strutturati, il modello produce output nello stesso ordine delle chiavi nello schema.

La modalità di output strutturato di Gemini supporta un sottoinsieme della specifica [JSON Schema](https://ai.google.dev/gemini-api/docs/JSON Schema).

Sono supportati i seguenti valori di `type`:

- **`string`**: Per il testo.
- **`number`**: per i numeri in virgola mobile.
- **`integer`**: per i numeri interi.
- **`boolean`**: per i valori vero/falso.
- **`object`**: per dati strutturati con coppie chiave-valore.
- **`array`**: per gli elenchi di elementi.
- **`null`**: per consentire a una proprietà di essere null, includi `"null"` nell'array di tipi (ad es. `{"type": ["string", "null"]}`).

Queste proprietà descrittive aiutano a guidare il modello:

- **`title`**: una breve descrizione di una proprietà.
- **`description`**: una descrizione più lunga e dettagliata di una proprietà.

### Proprietà specifiche per tipo

**Per i valori di `object`:**

- **`properties`**: un oggetto in cui ogni chiave è il nome di una proprietà e ogni valore è uno schema per quella proprietà.
- **`required`**: un array di stringhe che elenca le proprietà obbligatorie.
- **`additionalProperties`**: controlla se le proprietà non elencate in `properties` sono consentite. Può essere un valore booleano o uno schema.

**Per i valori di `string`:**

- **`enum`**: elenca un insieme specifico di possibili stringhe per le attività di classificazione.
- **`format`**: specifica una sintassi per la stringa, ad esempio `date-time`, `date`, `time`.

**Per i valori `number` e `integer`:**

- **`enum`**: elenca un insieme specifico di valori numerici possibili.
- **`minimum`**: il valore inclusivo minimo.
- **`maximum`**: il valore inclusivo massimo.

**Per i valori di `array`:**

- **`items`**: definisce lo schema per tutti gli elementi dell'array.
- **`prefixItems`**: definisce un elenco di schemi per i primi N elementi, consentendo strutture simili a tuple.
- **`minItems`**: il numero minimo di elementi nell'array.
- **`maxItems`**: il numero massimo di elementi nell'array.

## Supporto del modello

I seguenti modelli supportano l'output strutturato:

| Modello | Output strutturati |
| --- | --- |
| Gemini 3.1 Pro (anteprima) | ✔️ |
| Gemini 3 Flash (anteprima) | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |
| Gemini 2.0 Flash | ✔️\* |
| Gemini 2.0 Flash-Lite | ✔️\* |

*\* Tieni presente che Gemini 2.0 richiede un elenco `propertyOrdering` esplicito all'interno dell'input JSON per definire la struttura preferita. Puoi trovare un esempio in questo [cookbook](https://ai.google.dev/gemini-api/docs/cookbook).*

## Output strutturati e chiamata di funzione

Sia gli output strutturati che le chiamate di funzione utilizzano schemi JSON, ma hanno scopi diversi:

| Funzionalità | Caso d'uso principale |
| --- | --- |
| **Output strutturati** | **Formattazione della risposta finale all'utente.** Utilizza questo prompt quando vuoi che la *risposta* del modello sia in un formato specifico (ad es. estrazione di dati da un documento da salvare in un database). |
| **Chiamata di funzione** | **Eseguire azioni durante la conversazione.** Utilizza questo intent quando il modello deve *chiederti* di eseguire un'attività (ad es. "ottieni il meteo attuale") prima di poter fornire una risposta finale. |

## Best practice

- **Descrizioni chiare**:utilizza il campo `description` nello schema per fornire istruzioni chiare al modello su cosa rappresenta ogni proprietà. Questo è fondamentale per guidare l'output del modello.
- **Tipizzazione forte**:utilizza tipi specifici (`integer`, `string`, `enum`) quando possibile. Se un parametro ha un insieme limitato di valori validi, utilizza un `enum`.
- **Ingegneria dei prompt:** indica chiaramente nel prompt cosa vuoi che faccia il modello. Ad esempio, "Estrai le seguenti informazioni dal testo…" o "Classifica questo feedback in base allo schema fornito…".
- **Convalida**:sebbene l'output strutturato garantisca un JSON sintatticamente corretto, non garantisce che i valori siano semanticamente corretti. Verifica sempre l'output finale nel codice dell'applicazione prima di utilizzarlo.
- **Gestione degli errori:** implementa una gestione degli errori efficace nella tua applicazione per gestire correttamente i casi in cui l'output del modello, pur essendo conforme allo schema, potrebbe non soddisfare i requisiti della logica di business.

## Limitazioni

- **Sottoinsieme dello schema**:non tutte le funzionalità della specifica JSON Schema sono supportate. Il modello ignora le proprietà non supportate.
- **Complessità dello schema**:l'API potrebbe rifiutare schemi molto grandi o nidificati in profondità. Se si verificano errori, prova a semplificare lo schema riducendo i nomi delle proprietà, diminuendo il livello di nidificazione o limitando il numero di vincoli.

Invia feedback

Salvo quando diversamente specificato, i contenuti di questa pagina sono concessi in base alla [licenza Creative Commons Attribution 4.0](https://ai.google.dev/gemini-api/docs/licenza Creative Commons Attribution 4.0), mentre gli esempi di codice sono concessi in base alla [licenza Apache 2.0](https://ai.google.dev/gemini-api/docs/licenza Apache 2.0). Per ulteriori dettagli, consulta le [norme del sito di Google Developers](https://ai.google.dev/gemini-api/docs/norme del sito di Google Developers). Java è un marchio registrato di Oracle e/o delle sue consociate.

Ultimo aggiornamento 2026-04-29 UTC.

Vuoi dirci altro?
