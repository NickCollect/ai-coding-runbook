---
source_url: https://ai.google.dev/gemini-api/docs/migrate?hl=fr
fetched_at: 2026-05-18T05:16:44.587597+00:00
title: "Migrer vers le SDK Google GenAI \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

La [recherche approfondie Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=fr) est désormais disponible en preview avec la planification collaborative, la visualisation, la compatibilité MCP et plus encore.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Migrer vers le SDK Google GenAI

Avec la version Gemini 2.0, sortie fin 2024, nous avons lancé un nouvel ensemble de bibliothèques appelé [SDK Google GenAI](https://ai.google.dev/gemini-api/docs/libraries?hl=fr). Elle offre une meilleure expérience aux développeurs grâce à une [architecture client mise à jour](https://ai.google.dev/gemini-api/docs/migrate?hl=fr#client) et [simplifie la transition](https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=fr) entre les workflows pour les développeurs et les entreprises.

Le SDK Google GenAI est désormais en [disponibilité générale](https://ai.google.dev/gemini-api/docs/libraries?hl=fr#new-libraries) sur toutes les plates-formes compatibles. Si vous utilisez l'une de nos [anciennes bibliothèques](https://ai.google.dev/gemini-api/docs/libraries?hl=fr#previous-sdks), nous vous recommandons vivement de migrer.

Ce guide fournit des exemples de code avant et après la migration pour vous aider à vous lancer.

## Installation

**Avant**

### Python

```
pip install -U -q "google-generativeai"
```

### JavaScript

```
npm install @google/generative-ai
```

### Go

```
go get github.com/google/generative-ai-go
```

**Après**

### Python

```
pip install -U -q "google-genai"
```

### JavaScript

```
npm install @google/genai
```

### Go

```
go get google.golang.org/genai
```

## Accès API

L'ancien SDK gérait implicitement le client API en arrière-plan à l'aide de diverses méthodes ad hoc. Il était donc difficile de gérer le client et les identifiants.
Vous interagissez désormais via un objet `Client` central. Cet objet `Client` sert de point d'entrée unique pour divers services d'API (par exemple, `models`, `chats`, `files`, `tunings`), ce qui favorise la cohérence et simplifie la gestion des identifiants et de la configuration pour différents appels d'API.

**Avant (accès aux API moins centralisé)**

### Python

L'ancien SDK n'utilisait pas explicitement d'objet client de premier niveau pour la plupart des appels d'API. Vous instancierez directement les objets `GenerativeModel` et interagirez avec eux.

```
import google.generativeai as genai

# Directly create and use model objects
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(...)
chat = model.start_chat(...)
```

### JavaScript

Alors que `GoogleGenerativeAI` était un point central pour les modèles et le chat, d'autres fonctionnalités telles que la gestion des fichiers et du cache nécessitaient souvent d'importer et d'instancier des classes clientes entièrement distinctes.

```
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager, GoogleAICacheManager } from "@google/generative-ai/server"; // For files/caching

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");
const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");

// Get a model instance, then call methods on it
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent(...);
const chat = model.startChat(...);

// Call methods on separate client objects for other services
const uploadedFile = await fileManager.uploadFile(...);
const cache = await cacheManager.create(...);
```

### Go

La fonction `genai.NewClient` a créé un client, mais les opérations de modèle génératif étaient généralement appelées sur une instance `GenerativeModel` distincte obtenue à partir de ce client. Il est possible que d'autres services aient été consultés à l'aide de packages ou de schémas distincts.

```
import (
      "github.com/google/generative-ai-go/genai"
      "github.com/google/generative-ai-go/genai/fileman" // For files
      "google.golang.org/api/option"
)

client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
fileClient, err := fileman.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))

// Get a model instance, then call methods on it
model := client.GenerativeModel("gemini-2.0-flash")
resp, err := model.GenerateContent(...)
cs := model.StartChat()

// Call methods on separate client objects for other services
uploadedFile, err := fileClient.UploadFile(...)
```

**Après (objet client centralisé)**

### Python

```
from google import genai

# Create a single client object
client = genai.Client()

# Access API methods through services on the client object
response = client.models.generate_content(...)
chat = client.chats.create(...)
my_file = client.files.upload(...)
tuning_job = client.tunings.tune(...)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

// Create a single client object
const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});

// Access API methods through services on the client object
const response = await ai.models.generateContent(...);
const chat = ai.chats.create(...);
const uploadedFile = await ai.files.upload(...);
const cache = await ai.caches.create(...);
```

### Go

```
import "google.golang.org/genai"

// Create a single client object
client, err := genai.NewClient(ctx, nil)

// Access API methods through services on the client object
result, err := client.Models.GenerateContent(...)
chat, err := client.Chats.Create(...)
uploadedFile, err := client.Files.Upload(...)
tuningJob, err := client.Tunings.Tune(...)
```

## Authentification

Les anciennes et les nouvelles bibliothèques s'authentifient à l'aide de clés API. Vous pouvez [créer](https://aistudio.google.com/app/apikey?hl=fr) votre clé API dans Google AI Studio.

**Avant**

### Python

L'ancien SDK gérait l'objet client API de manière implicite.

```
import google.generativeai as genai

genai.configure(api_key=...)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
```

### Go

Importez les bibliothèques Google :

```
import (
      "github.com/google/generative-ai-go/genai"
      "google.golang.org/api/option"
)
```

Créez le client :

```
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
```

**Après**

### Python

Avec le SDK Google GenAI, vous créez d'abord un client d'API, qui est utilisé pour appeler l'API.
Le nouveau SDK récupérera votre clé API à partir des variables d'environnement `GEMINI_API_KEY` si vous n'en transmettez pas au client.

```
export GEMINI_API_KEY="YOUR_API_KEY"
```

```
from google import genai

client = genai.Client() # Set the API key using the GEMINI_API_KEY env var.
                        # Alternatively, you could set the API key explicitly:
                        # client = genai.Client(api_key="YOUR_API_KEY")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({apiKey: "GEMINI_API_KEY"});
```

### Go

Importez la bibliothèque GenAI :

```
import "google.golang.org/genai"
```

Créez le client :

```
client, err := genai.NewClient(ctx, &genai.ClientConfig{
        Backend:  genai.BackendGeminiAPI,
})
```

## Génération de contenus

### Texte

**Avant**

### Python

Auparavant, il n'y avait pas d'objets client. Vous accédiez directement aux API via des objets `GenerativeModel`.

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });
const prompt = "Tell me a story in 300 words";

const result = await model.generateContent(prompt);
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
resp, err := model.GenerateContent(ctx, genai.Text("Tell me a story in 300 words."))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response parts
```

**Après**

### Python

Le nouveau SDK Google GenAI permet d'accéder à toutes les méthodes d'API via l'objet `Client`. À l'exception de quelques cas particuliers avec état (`chat` et `session` de l'API Live), il s'agit de fonctions sans état. Pour plus d'utilité et d'uniformité, les objets renvoyés sont des classes `pydantic`.

```
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "Tell me a story in 300 words.",
});
console.log(response.text);
```

### Go

```
ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx, "gemini-2.0-flash", genai.Text("Tell me a story in 300 words."), nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### Image

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content([
    'Tell me a story based on this image',
    Image.open(image_path)
])
print(response.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

function fileToGenerativePart(path, mimeType) {
  return {
    inlineData: {
      data: Buffer.from(fs.readFileSync(path)).toString("base64"),
      mimeType,
    },
  };
}

const prompt = "Tell me a story based on this image";

const imagePart = fileToGenerativePart(
  `path/to/organ.jpg`,
  "image/jpeg",
);

const result = await model.generateContent([prompt, imagePart]);
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

resp, err := model.GenerateContent(ctx,
    genai.Text("Tell me about this instrument"),
    genai.ImageData("jpeg", imgData))
if err != nil {
    log.Fatal(err)
}

printResponse(resp) // utility for printing response
```

**Après**

### Python

De nombreuses fonctionnalités pratiques sont disponibles dans le nouveau SDK. Par exemple, les objets `PIL.Image` sont automatiquement convertis.

```
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open(image_path)
    ]
)
print(response.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const organ = await ai.files.upload({
  file: "path/to/organ.jpg",
});

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: [
    createUserContent([
      "Tell me a story based on this image",
      createPartFromUri(organ.uri, organ.mimeType)
    ]),
  ],
});
console.log(response.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

imgData, err := os.ReadFile("path/to/organ.jpg")
if err != nil {
    log.Fatal(err)
}

parts := []*genai.Part{
    {Text: "Tell me a story based on this image"},
    {InlineData: &genai.Blob{Data: imgData, MIMEType: "image/jpeg"}},
}
contents := []*genai.Content{
    {Parts: parts},
}

result, err := client.Models.GenerateContent(ctx, "gemini-2.0-flash", contents, nil)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

### Streaming

**Avant**

### Python

```
import google.generativeai as genai

response = model.generate_content(
    "Write a cute story about cats.",
    stream=True)
for chunk in response:
    print(chunk.text)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

const prompt = "Write a story about a magic backpack.";

const result = await model.generateContentStream(prompt);

// Print text as it comes in.
for await (const chunk of result.stream) {
  const chunkText = chunk.text();
  process.stdout.write(chunkText);
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
iter := model.GenerateContentStream(ctx, genai.Text("Write a story about a magic backpack."))
for {
    resp, err := iter.Next()
    if err == iterator.Done {
        break
    }
    if err != nil {
        log.Fatal(err)
    }
    printResponse(resp) // utility for printing the response
}
```

**Après**

### Python

```
from google import genai

client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-2.0-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContentStream({
  model: "gemini-2.0-flash",
  contents: "Write a story about a magic backpack.",
});
let text = "";
for await (const chunk of response) {
  console.log(chunk.text);
  text += chunk.text;
}
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

for result, err := range client.Models.GenerateContentStream(
    ctx,
    "gemini-2.0-flash",
    genai.Text("Write a story about a magic backpack."),
    nil,
) {
    if err != nil {
        log.Fatal(err)
    }
    fmt.Print(result.Candidates[0].Content.Parts[0].Text)
}
```

## Configuration

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
  'gemini-2.0-flash',
    system_instruction='you are a story teller for kids under 5 years old',
    generation_config=genai.GenerationConfig(
      max_output_tokens=400,
      top_k=2,
      top_p=0.5,
      temperature=0.5,
      response_mime_type='application/json',
      stop_sequences=['\n'],
    )
)
response = model.generate_content('tell me a story in 100 words')
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  generationConfig: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

const result = await model.generateContent(
  "Tell me a story about a magic backpack.",
);
console.log(result.response.text())
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
model.SetTemperature(0.5)
model.SetTopP(0.5)
model.SetTopK(2.0)
model.SetMaxOutputTokens(100)
model.ResponseMIMEType = "application/json"
resp, err := model.GenerateContent(ctx, genai.Text("Tell me about New York"))
if err != nil {
    log.Fatal(err)
}
printResponse(resp) // utility for printing response
```

**Après**

### Python

Pour toutes les méthodes du nouveau SDK, les arguments requis sont fournis sous forme d'arguments de mot clé. Toutes les entrées facultatives sont fournies dans l'argument `config`. Les arguments de configuration peuvent être spécifiés sous forme de dictionnaires Python ou de classes `Config` dans l'espace de noms `google.genai.types`. Pour des raisons d'utilité et d'uniformité, toutes les définitions du module `types` sont des classes `pydantic`.

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='Tell me a story in 100 words.',
  config=types.GenerateContentConfig(
      system_instruction='you are a story teller for kids under 5 years old',
      max_output_tokens= 400,
      top_k= 2,
      top_p= 0.5,
      temperature= 0.5,
      response_mime_type= 'application/json',
      stop_sequences= ['\n'],
      seed=42,
  ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "Tell me a story about a magic backpack.",
  config: {
    candidateCount: 1,
    stopSequences: ["x"],
    maxOutputTokens: 20,
    temperature: 1.0,
  },
});

console.log(response.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

result, err := client.Models.GenerateContent(ctx,
    "gemini-2.0-flash",
    genai.Text("Tell me about New York"),
    &genai.GenerateContentConfig{
        Temperature:      genai.Ptr[float32](0.5),
        TopP:             genai.Ptr[float32](0.5),
        TopK:             genai.Ptr[float32](2.0),
        ResponseMIMEType: "application/json",
        StopSequences:    []string{"Yankees"},
        CandidateCount:   2,
        Seed:             genai.Ptr[int32](42),
        MaxOutputTokens:  128,
        PresencePenalty:  genai.Ptr[float32](0.5),
        FrequencyPenalty: genai.Ptr[float32](0.5),
    },
)
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing response
```

## Paramètres de sécurité

Générer une réponse avec des paramètres de sécurité :

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    'say something bad',
    safety_settings={
        'HATE': 'BLOCK_ONLY_HIGH',
        'HARASSMENT': 'BLOCK_ONLY_HIGH',
  }
)
```

### JavaScript

```
import { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  safetySettings: [
    {
      category: HarmCategory.HARM_CATEGORY_HARASSMENT,
      threshold: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    },
  ],
});

const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const result = await model.generateContent(unsafePrompt);

try {
  result.response.text();
} catch (e) {
  console.error(e);
  console.log(result.response.candidates[0].safetyRatings);
}
```

**Après**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='say something bad',
  config=types.GenerateContentConfig(
      safety_settings= [
          types.SafetySetting(
              category='HARM_CATEGORY_HATE_SPEECH',
              threshold='BLOCK_ONLY_HIGH'
          ),
      ]
  ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const unsafePrompt =
  "I support Martians Soccer Club and I think " +
  "Jupiterians Football Club sucks! Write an ironic phrase telling " +
  "them how I feel about them.";

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: unsafePrompt,
  config: {
    safetySettings: [
      {
        category: "HARM_CATEGORY_HARASSMENT",
        threshold: "BLOCK_ONLY_HIGH",
      },
    ],
  },
});

console.log("Finish reason:", response.candidates[0].finishReason);
console.log("Safety ratings:", response.candidates[0].safetyRatings);
```

## Asynchrone

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**Après**

### Python

Pour utiliser le nouveau SDK avec `asyncio`, il existe une implémentation `async` distincte de chaque méthode sous `client.aio`.

```
from google import genai

client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-2.0-flash',
    contents='Tell me a story in 300 words.'
)
```

## Chat

Démarrez une discussion et envoyez un message au modèle :

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat()

response = chat.send_message(
    "Tell me a story in 100 words")
response = chat.send_message(
    "What happened after that?")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });
const chat = model.startChat({
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});
let result = await chat.sendMessage("I have 2 dogs in my house.");
console.log(result.response.text());
result = await chat.sendMessage("How many paws are in my house?");
console.log(result.response.text());
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, option.WithAPIKey("GEMINI_API_KEY"))
if err != nil {
    log.Fatal(err)
}
defer client.Close()

model := client.GenerativeModel("gemini-2.0-flash")
cs := model.StartChat()

cs.History = []*genai.Content{
    {
        Parts: []genai.Part{
            genai.Text("Hello, I have 2 dogs in my house."),
        },
        Role: "user",
    },
    {
        Parts: []genai.Part{
            genai.Text("Great to meet you. What would you like to know?"),
        },
        Role: "model",
    },
}

res, err := cs.SendMessage(ctx, genai.Text("How many paws are in my house?"))
if err != nil {
    log.Fatal(err)
}
printResponse(res) // utility for printing the response
```

**Après**

### Python

```
from google import genai

client = genai.Client()

chat = client.chats.create(model='gemini-2.0-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const chat = ai.chats.create({
  model: "gemini-2.0-flash",
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});

const response1 = await chat.sendMessage({
  message: "I have 2 dogs in my house.",
});
console.log("Chat response 1:", response1.text);

const response2 = await chat.sendMessage({
  message: "How many paws are in my house?",
});
console.log("Chat response 2:", response2.text);
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
    log.Fatal(err)
}

chat, err := client.Chats.Create(ctx, "gemini-2.0-flash", nil, nil)
if err != nil {
    log.Fatal(err)
}

result, err := chat.SendMessage(ctx, genai.Part{Text: "Hello, I have 2 dogs in my house."})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result

result, err = chat.SendMessage(ctx, genai.Part{Text: "How many paws are in my house?"})
if err != nil {
    log.Fatal(err)
}
debugPrint(result) // utility for printing result
```

## Appel de fonction

**Avant**

### Python

```
import google.generativeai as genai
from enum import Enum

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**Après**

### Python

Dans le nouveau SDK, l'appel de fonction automatique est défini par défaut. Ici, vous le désactivez.

```
from google import genai
from google.genai import types

client = genai.Client()

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather],
      automatic_function_calling={'disable': True},
  ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### Appel de fonction automatique

**Avant**

### Python

L'ancien SDK n'est compatible qu'avec l'appel de fonction automatique dans le chat. Dans le nouveau SDK, il s'agit du comportement par défaut dans `generate_content`.

```
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**Après**

### Python

```
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents="What is the weather like in Boston?",
  config=types.GenerateContentConfig(
      tools=[get_current_weather]
  ),
)
```

## Exécution du code

L'exécution de code est un outil qui permet au modèle de générer du code Python, de l'exécuter et de renvoyer le résultat.

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    tools="code_execution"
)

result = model.generate_content(
  "What is the sum of the first 50 prime numbers? Generate and run code for "
  "the calculation, and make sure you get all 50.")
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  tools: [{ codeExecution: {} }],
});

const result = await model.generateContent(
  "What is the sum of the first 50 prime numbers? " +
    "Generate and run code for the calculation, and make sure you get " +
    "all 50.",
);

console.log(result.response.text());
```

**Après**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the sum of the first 50 prime numbers? Generate and run '
            'code for the calculation, and make sure you get all 50.',
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)],
    ),
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: `Write and execute code that calculates the sum of the first 50 prime numbers.
            Ensure that only the executable code and its resulting output are generated.`,
});

// Each part may contain text, executable code, or an execution result.
for (const part of response.candidates[0].content.parts) {
  console.log(part);
  console.log("\n");
}

console.log("-".repeat(80));
// The `.text` accessor concatenates the parts into a markdown-formatted text.
console.log("\n", response.text);
```

## Ancrage de recherche

`GoogleSearch` (Gemini>=2.0) et `GoogleSearchRetrieval` (Gemini < 2.0) sont des outils qui permettent au modèle de récupérer des données Web publiques pour l'ancrage, fournis par Google.

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**Après**

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the Google stock price?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ]
    )
)
```

## Réponse JSON

Générez des réponses au format JSON.

**Avant**

### Python

En spécifiant un `response_schema` et en définissant `response_mime_type="application/json"`, les utilisateurs peuvent contraindre le modèle à produire une réponse `JSON` suivant une structure donnée.

```
import google.generativeai as genai
import typing_extensions as typing

class CountryInfo(typing.TypedDict):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

model = genai.GenerativeModel(model_name="gemini-2.0-flash")
result = model.generate_content(
    "Give me information of the United States",
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema = CountryInfo
    ),
)
```

### JavaScript

```
import { GoogleGenerativeAI, SchemaType } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");

const schema = {
  description: "List of recipes",
  type: SchemaType.ARRAY,
  items: {
    type: SchemaType.OBJECT,
    properties: {
      recipeName: {
        type: SchemaType.STRING,
        description: "Name of the recipe",
        nullable: false,
      },
    },
    required: ["recipeName"],
  },
};

const model = genAI.getGenerativeModel({
  model: "gemini-2.0-flash",
  generationConfig: {
    responseMimeType: "application/json",
    responseSchema: schema,
  },
});

const result = await model.generateContent(
  "List a few popular cookie recipes.",
);
console.log(result.response.text());
```

**Après**

### Python

Le nouveau SDK utilise des classes `pydantic` pour fournir le schéma (bien que vous puissiez transmettre un `genai.types.Schema` ou un `dict` équivalent). Lorsque cela est possible, le SDK analyse le JSON renvoyé et renvoie le résultat dans `response.parsed`. Si vous avez fourni une classe `pydantic` comme schéma, le SDK convertira cette `JSON` en instance de la classe.

```
from google import genai
from pydantic import BaseModel

client = genai.Client()

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='Give me information of the United States.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo,
    },
)

response.parsed
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: "List a few popular cookie recipes.",
  config: {
    responseMimeType: "application/json",
    responseSchema: {
      type: "array",
      items: {
        type: "object",
        properties: {
          recipeName: { type: "string" },
          ingredients: { type: "array", items: { type: "string" } },
        },
        required: ["recipeName", "ingredients"],
      },
    },
  },
});
console.log(response.text);
```

## Fichiers

### Importer

Importer un fichier :

**Avant**

### Python

```
import requests
import pathlib
import google.generativeai as genai

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

file = genai.upload_file(path='a11.txt')

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content([
    'Can you summarize this file:',
    my_file
])
print(response.text)
```

**Après**

### Python

```
import requests
import pathlib
from google import genai

client = genai.Client()

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

my_file = client.files.upload(file='a11.txt')

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Can you summarize this file:',
        my_file
    ]
)
print(response.text)
```

### Lister et obtenir

Répertoriez les fichiers importés et récupérez un fichier importé avec un nom de fichier :

**Avant**

### Python

```
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**Après**

### Python

```
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```

### Supprimer

Supprimez un fichier :

**Avant**

### Python

```
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**Après**

### Python

```
import pathlib
from google import genai

client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```

## mise en cache du contexte

La mise en cache du contexte permet à l'utilisateur de transmettre le contenu au modèle une seule fois, de mettre en cache les jetons d'entrée, puis de faire référence aux jetons mis en cache dans les appels suivants pour réduire les coûts.

**Avant**

### Python

```
import requests
import pathlib
import google.generativeai as genai
from google.generativeai import caching

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = genai.upload_file(path="a11.txt")

# Create cache
apollo_cache = caching.CachedContent.create(
    model="gemini-2.0-flash-001",
    system_instruction="You are an expert at analyzing transcripts.",
    contents=[document],
)

# Generate response
apollo_model = genai.GenerativeModel.from_cached_content(
    cached_content=apollo_cache
)
response = apollo_model.generate_content("Find a lighthearted moment from this transcript")
```

### JavaScript

```
import { GoogleAICacheManager, GoogleAIFileManager } from "@google/generative-ai/server";
import { GoogleGenerativeAI } from "@google/generative-ai";

const cacheManager = new GoogleAICacheManager("GEMINI_API_KEY");
const fileManager = new GoogleAIFileManager("GEMINI_API_KEY");

const uploadResult = await fileManager.uploadFile("path/to/a11.txt", {
  mimeType: "text/plain",
});

const cacheResult = await cacheManager.create({
  model: "models/gemini-2.0-flash",
  contents: [
    {
      role: "user",
      parts: [
        {
          fileData: {
            fileUri: uploadResult.file.uri,
            mimeType: uploadResult.file.mimeType,
          },
        },
      ],
    },
  ],
});

console.log(cacheResult);

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModelFromCachedContent(cacheResult);
const result = await model.generateContent(
  "Please summarize this transcript.",
);
console.log(result.response.text());
```

**Après**

### Python

```
import requests
import pathlib
from google import genai
from google.genai import types

client = genai.Client()

# Check which models support caching.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createCachedContent":
      print(m.name)
      break

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

# Upload file
document = client.files.upload(file='a11.txt')

# Create cache
model='gemini-2.0-flash-001'
apollo_cache = client.caches.create(
      model=model,
      config={
          'contents': [document],
          'system_instruction': 'You are an expert at analyzing transcripts.',
      },
  )

# Generate response
response = client.models.generate_content(
    model=model,
    contents='Find a lighthearted moment from this transcript',
    config=types.GenerateContentConfig(
        cached_content=apollo_cache.name,
    )
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const filePath = path.join(media, "a11.txt");
const document = await ai.files.upload({
  file: filePath,
  config: { mimeType: "text/plain" },
});
console.log("Uploaded file name:", document.name);
const modelName = "gemini-2.0-flash";

const contents = [
  createUserContent(createPartFromUri(document.uri, document.mimeType)),
];

const cache = await ai.caches.create({
  model: modelName,
  config: {
    contents: contents,
    systemInstruction: "You are an expert analyzing transcripts.",
  },
});
console.log("Cache created:", cache);

const response = await ai.models.generateContent({
  model: modelName,
  contents: "Please summarize this transcript",
  config: { cachedContent: cache.name },
});
console.log("Response text:", response.text);
```

## Compter les jetons

Compter le nombre de jetons dans une requête.

**Avant**

### Python

```
import google.generativeai as genai

model = genai.GenerativeModel('gemini-2.0-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')
```

### JavaScript

```
 import { GoogleGenerativeAI } from "@google/generative-ai";

 const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
 const model = genAI.getGenerativeModel({
   model: "gemini-2.0-flash",
 });

 // Count tokens in a prompt without calling text generation.
 const countResult = await model.countTokens(
   "The quick brown fox jumps over the lazy dog.",
 );

 console.log(countResult.totalTokens); // 11

 const generateResult = await model.generateContent(
   "The quick brown fox jumps over the lazy dog.",
 );

 // On the response for `generateContent`, use `usageMetadata`
 // to get separate input and output token counts
 // (`promptTokenCount` and `candidatesTokenCount`, respectively),
 // as well as the combined token count (`totalTokenCount`).
 console.log(generateResult.response.usageMetadata);
 // candidatesTokenCount and totalTokenCount depend on response, may vary
 // { promptTokenCount: 11, candidatesTokenCount: 124, totalTokenCount: 135 }
```

**Après**

### Python

```
from google import genai

client = genai.Client()

response = client.models.count_tokens(
    model='gemini-2.0-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const prompt = "The quick brown fox jumps over the lazy dog.";
const countTokensResponse = await ai.models.countTokens({
  model: "gemini-2.0-flash",
  contents: prompt,
});
console.log(countTokensResponse.totalTokens);

const generateResponse = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: prompt,
});
console.log(generateResponse.usageMetadata);
```

## Générer des images

Générer des images :

**Avant**

### Python

```
#pip install https://github.com/google-gemini/generative-ai-python@imagen
import google.generativeai as genai

imagen = genai.ImageGenerationModel(
    "imagen-3.0-generate-001")
gen_images = imagen.generate_images(
    prompt="Robot holding a red skateboard",
    number_of_images=1,
    safety_filter_level="block_low_and_above",
    person_generation="allow_adult",
    aspect_ratio="3:4",
)
```

**Après**

### Python

```
from google import genai

client = genai.Client()

gen_images = client.models.generate_images(
    model='gemini-2.5-flash-image',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 1,
        safety_filter_level= "BLOCK_LOW_AND_ABOVE",
        person_generation= "ALLOW_ADULT",
        aspect_ratio= "3:4",
    )
)

for n, image in enumerate(gen_images.generated_images):
    pathlib.Path(f'{n}.png').write_bytes(
        image.image.image_bytes)
```

## Intégrer du contenu

Générez des embeddings de contenu.

**Avant**

### Python

```
import google.generativeai as genai

response = genai.embed_content(
  model='models/gemini-embedding-001',
  content='Hello world'
)
```

### JavaScript

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("GEMINI_API_KEY");
const model = genAI.getGenerativeModel({
  model: "gemini-embedding-001",
});

const result = await model.embedContent("Hello world!");

console.log(result.embedding);
```

**Après**

### Python

```
from google import genai

client = genai.Client()

response = client.models.embed_content(
  model='gemini-embedding-001',
  contents='Hello world',
)
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });
const text = "Hello World!";
const result = await ai.models.embedContent({
  model: "gemini-embedding-001",
  contents: text,
  config: { outputDimensionality: 10 },
});
console.log(result.embeddings);
```

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/05/13 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/05/13 (UTC)."],[],[]]
