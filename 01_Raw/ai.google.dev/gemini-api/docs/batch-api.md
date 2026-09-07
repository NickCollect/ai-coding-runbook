---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=fr
fetched_at: 2026-09-07T05:33:01.876962+00:00
title: "API Batch \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# API Batch

L'API Gemini Batch est conçue pour traiter de grands volumes de requêtes de manière asynchrone à [50% du coût standard](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).
Le délai de traitement cible est de 24 heures, mais il est généralement beaucoup plus rapide.

Utilisez l'API Batch pour les tâches à grande échelle et non urgentes, telles que le prétraitement des données ou l'exécution d'évaluations pour lesquelles une réponse immédiate n'est pas requise.

## Créer un job par lot

Vous pouvez envoyer vos requêtes dans l'API Batch de deux manières :

- **[Requêtes intégrées](#inline-requests)** : liste d'objets [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=fr#GenerateContentRequest) directement inclus dans votre demande de création par lot. Cette méthode convient aux petits lots dont la taille totale de la requête est inférieure à 20 Mo. La **sortie** renvoyée par le modèle est une liste d'objets `inlineResponse`.
- **[Fichier d'entrée](#input-file)** : fichier [JSON Lines (JSONL)](https://jsonlines.org/) dans lequel chaque ligne contient un objet [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=fr#GenerateContentRequest) complet.
  Cette méthode est recommandée pour les requêtes plus volumineuses. La **sortie** renvoyée par le modèle est un fichier JSONL dans lequel chaque ligne est un objet `GenerateContentResponse` ou un objet d'état.

### Requêtes intégrées

Pour un petit nombre de requêtes, vous pouvez intégrer directement les objets [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=fr#GenerateContentRequest) dans votre [`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=fr#request-body). L'exemple suivant appelle la méthode [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=fr#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent) avec des requêtes intégrées :

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### Fichier en entrée

Pour les ensembles de requêtes plus volumineux, préparez un fichier JSON Lines (JSONL). Chaque ligne de ce fichier doit être un objet JSON contenant une clé définie par l'utilisateur et un objet de requête, où la requête est un objet [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=fr#GenerateContentRequest) valide. La clé définie par l'utilisateur est utilisée dans la réponse pour indiquer quel résultat correspond à quelle requête. Par exemple, la réponse à une requête dont la clé est définie sur `request-1` sera annotée avec le même nom de clé.

Ce fichier est importé à l'aide de l'[API File](https://ai.google.dev/gemini-api/docs/files?hl=fr). La taille maximale autorisée pour un fichier d'entrée est de 2 Go.

Voici un exemple de fichier JSONL. Vous pouvez l'enregistrer dans un fichier nommé `my-batch-requests.json` :

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

Comme pour les requêtes intégrées, vous pouvez spécifier d'autres paramètres tels que des instructions système, des outils ou d'autres configurations dans chaque requête JSON.

Vous pouvez importer ce fichier à l'aide de l'[API File](https://ai.google.dev/gemini-api/docs/files?hl=fr), comme illustré dans l'exemple suivant. Si vous utilisez une entrée multimodale, vous pouvez faire référence à d'autres fichiers importés dans votre fichier JSONL.

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

L'exemple suivant appelle la méthode [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=fr#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent) avec le fichier d'entrée importé à l'aide de l'API File :

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

Lorsque vous créez un job par lot, un nom de job vous est renvoyé. Utilisez ce nom pour [surveiller](#batch-job-status) l'état du job et [récupérer les résultats](#retrieve-batch-results) une fois le job terminé.

Voici un exemple de résultat contenant un nom de job :

```
Created batch job from file: batches/123456789
```

### Compatibilité avec l'embedding par lot

Vous pouvez utiliser l'API Batch pour interagir avec le [modèle Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=fr) et obtenir un débit plus élevé.
Pour créer un job par lot d'embeddings avec des [requêtes intégrées](#inline-requests) ou des [fichiers d'entrée](#input-file), utilisez l'API `batches.create_embeddings` et spécifiez le modèle d'embeddings.

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

Pour obtenir d'autres exemples, consultez la section "Embeddings" du [cookbook de l'API Batch](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb).

### Configurer la requête

Vous pouvez inclure toutes les configurations de requête que vous utiliseriez dans une requête standard non par lot. Par exemple, vous pouvez spécifier la température, les instructions système ou même transmettre d'autres modalités. L'exemple suivant montre une requête intégrée contenant une instruction système pour l'une des requêtes :

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

De même, vous pouvez spécifier les outils à utiliser pour une requête. L'exemple suivant montre une requête qui active l'[outil de recherche Google](https://ai.google.dev/gemini-api/docs/google-search?hl=fr) :

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

Vous pouvez également spécifier une [sortie structurée](https://ai.google.dev/gemini-api/docs/structured-output?hl=fr).
L'exemple suivant montre comment spécifier vos requêtes par lot.

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

Voici un exemple de résultat de ce job :

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## Surveiller l'état d'un job

Utilisez le nom de l'opération obtenu lors de la création du job par lot pour interroger son état.
Le champ "state" du job par lot indique son état actuel. Un job par lot peut avoir l'un des états suivants :

- `JOB_STATE_PENDING` : la tâche a été créée et attend d'être traitée par le service.
- `JOB_STATE_RUNNING` : la tâche est en cours d'exécution.
- `JOB_STATE_SUCCEEDED` : la tâche a été effectuée avec succès. Vous pouvez maintenant récupérer les résultats.
- `JOB_STATE_FAILED` : la tâche a échoué. Pour en savoir plus, consultez les détails de l'erreur.
- `JOB_STATE_CANCELLED` : la tâche a été annulée par l'utilisateur.
- `JOB_STATE_EXPIRED` : la tâche a expiré, car elle était en cours d'exécution ou en attente depuis plus de 48 heures. La tâche ne générera aucun résultat à récupérer.
  Vous pouvez essayer d'envoyer de nouveau le job ou de diviser les requêtes en plus petits lots.

Vous pouvez interroger régulièrement l'état du job pour vérifier s'il est terminé.

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### Interrogation et webhooks

**Vous en avez assez des sondages ?** Gemini prend désormais en charge les [Webhooks](https://ai.google.dev/gemini-api/docs/webhooks?hl=fr) pour traiter les complétions de manière asynchrone.
Au lieu d'appeler `GET / operations` en continu, abonnez-vous à `batch.succeeded` directement pour permettre à l'API Gemini d'envoyer des notifications en temps réel à votre serveur lorsque des opérations asynchrones ou de longue durée sont terminées.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## Récupération des résultats

Une fois que l'état du job par lot indique qu'il a réussi, les résultats sont disponibles dans le champ `response`.
Par défaut, les résultats des jobs par lot sont stockés et disponibles au téléchargement pendant six semaines avant d'être définitivement supprimés.

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## Lister les jobs par lot

Vous pouvez lister vos jobs par lot récents.

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Annuler un job par lot

Vous pouvez annuler un job par lot en cours à l'aide de son nom. Lorsqu'un job est annulé, il cesse de traiter les nouvelles requêtes.

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## Supprimer un job par lot

Vous pouvez supprimer un job par lot existant à l'aide de son nom. Lorsqu'un job est supprimé, il cesse de traiter les nouvelles requêtes et est supprimé de la liste des jobs par lot.

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Générer des images par lot

Si vous utilisez [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=fr) et que vous devez générer de nombreuses images, vous pouvez utiliser l'API Batch pour obtenir des [limites de fréquence](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr) plus élevées en échange d'un délai de traitement pouvant aller jusqu'à 24 heures.

Vous pouvez utiliser des [requêtes intégrées](#inline-requests-images) pour les petits lots de requêtes (moins de 20 Mo) ou un [fichier d'entrée JSONL](#input-file-images) pour les grands lots (recommandé pour la génération d'images) :

### Demandes d'images intégrées

### Python

```
import time
import base64
import json
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create batch job with inline requests
inline_requests = [
    {
        'contents': [{'parts': [{'text': 'A big letter A surrounded by animals starting with the A letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    },
    {
        'contents': [{'parts': [{'text': 'A big letter B surrounded by animals starting with the B letter'}]}],
        'config': {'response_modalities': ['TEXT', 'IMAGE']}
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=inline_requests,
    config={
        'display_name': "inlined-image-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")

# 2. Monitor job status
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 3. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    print("Results are inline:")
    for i, inline_response in enumerate(batch_job.dest.inlined_responses):
        print(f"Response {i+1}:")
        if inline_response.response:
            for part in inline_response.response.candidates[0].content.parts:
                if part.text:
                    print(part.text)
                elif part.inline_data:
                    print(f"Image mime type: {part.inline_data.mime_type}")
                    image = part.as_image()
                    image.save(f"image_{i+1}.png")
        elif inline_response.error:
            print(f"Error: {inline_response.error}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create batch job with inline requests
    const inlinedRequests = [
        {
            contents: [{parts: [{text: 'A big letter A surrounded by animals starting with the A letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        },
        {
            contents: [{parts: [{text: 'A big letter B surrounded by animals starting with the B letter'}]}],
            config: {responseModalities: ['TEXT', 'IMAGE']}
        }
    ]

    const inlineBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: inlinedRequests,
        config: {
            displayName: 'inlined-image-requests-job-1',
        }
    });

    console.log(inlineBatchJob);

    // 2. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: inlineBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${inlineBatchJob.name}:`, error);
        return;
    }

    // 3. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    for (const part of inlineResponse.response.candidates[0].content.parts) {
                        if (part.text) {
                            console.log(part.text);
                        } else if (part.inlineData) {
                            console.log(`Image mime type: ${part.inlineData.mimeType}`);
                        }
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No inline results found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### REST

```
# 1. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-image-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-1" }
                    },
                    {
                        "request": {
                            "contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}],
                            "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}
                        },
                        "metadata": { "key": "request-2" }
                    }
                ]
            }
        }
    }
}'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -X POST \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 2. Poll job status until completion by repeating the following command
# Replace $BATCH_NAME with the name returned above.
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 3. If state is JOB_STATE_SUCCEEDED, retrieve results from batch_status.json
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    echo "Job succeeded. Results:"
    jq -r '.dest.inlinedResponses' batch_status.json
fi
```

### Fichier d'entrée pour les images

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## Détails techniques

- **Modèles compatibles** : l'API Batch est compatible avec différents modèles Gemini.
  Consultez la page [Modèles](https://ai.google.dev/gemini-api/docs/models?hl=fr) pour connaître la compatibilité de chaque modèle avec l'API Batch. Les modalités acceptées pour l'API Batch sont les mêmes que celles acceptées pour l'API interactive (ou non par lot).
- **Tarifs** : l'utilisation de l'API Batch est facturée à 50% du coût standard de l'API interactive pour le modèle équivalent. Pour en savoir plus, consultez la [page des tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr). Pour en savoir plus sur les limites de débit de cette fonctionnalité, consultez la page [Limites de débit](https://ai.google.dev/gemini-api/docs/rate-limits?hl=fr#batch-mode).
- **Objectif de niveau de service (SLO)** : les jobs par lot sont conçus pour être traités dans un délai de 24 heures. De nombreux jobs peuvent se terminer beaucoup plus rapidement en fonction de leur taille et de la charge système actuelle.
- **Mise en cache** : la [mise en cache du contexte](https://ai.google.dev/gemini-api/docs/caching?hl=fr) est compatible avec les requêtes par lot. Réutilisez le contenu mis en cache en spécifiant le nom de ressource `cached_content` dans la configuration des requêtes individuelles de votre lot.
  Si une requête de votre lot génère un appel de cache, vous payez les [tarifs standard de mise en cache du contexte](https://ai.google.dev/gemini-api/docs/pricing?hl=fr).

## Bonnes pratiques

- **Utilisez des fichiers d'entrée pour les requêtes volumineuses** : pour un grand nombre de requêtes, utilisez toujours la méthode d'entrée de fichier pour une meilleure gestion et pour éviter d'atteindre les limites de taille des requêtes pour l'appel [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=fr#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent) lui-même. Notez que la taille de chaque fichier d'entrée est limitée à 2 Go.
- **Gestion des erreurs** : vérifiez le `batchStats` pour `failedRequestCount` une fois le job terminé. Si vous utilisez la sortie de fichier, analysez chaque ligne pour vérifier s'il s'agit d'un `GenerateContentResponse` ou d'un objet d'état indiquant une erreur pour cette requête spécifique. Consultez le [guide de dépannage](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=fr#error-codes) pour obtenir la liste complète des codes d'erreur.
- **N'envoyez les jobs qu'une seule fois** : la création d'un job par lot n'est pas idempotente.
  Si vous envoyez la même demande de création deux fois, deux jobs par lot distincts seront créés.
- **Fractionnez les très grands lots** : bien que le délai de traitement cible soit de 24 heures, le temps de traitement réel peut varier en fonction de la charge du système et de la taille du job.
  Pour les jobs volumineux, envisagez de les diviser en plus petits lots si vous avez besoin de résultats intermédiaires plus rapidement.

## Étape suivante

- Pour obtenir d'autres exemples, consultez le [notebook de l'API Batch](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=fr).
- La couche de compatibilité OpenAI est compatible avec l'API Batch. Consultez les exemples sur la page [Compatibilité avec OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=fr#batch).

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/07/02 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/07/02 (UTC)."],[],[]]
