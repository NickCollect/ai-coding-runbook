---
source_url: https://ai.google.dev/gemini-api/docs/tokens?hl=pl
fetched_at: 2026-05-05T20:01:08.641442+00:00
title: "Zrozumienie i liczenie token\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=pl) jest teraz dostępna w wersji testowej z funkcjami planowania współpracy, wizualizacji, obsługi MCP i nie tylko.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Zrozumienie i liczenie tokenów

Gemini i inne modele generatywnej AI przetwarzają dane wejściowe i wyjściowe z dokładnością do *tokena*.

**W przypadku modeli Gemini token odpowiada około 4 znakom.
100 tokenów to około 60–80 słów w języku angielskim.**

## Informacje o tokenach

Tokeny mogą być pojedynczymi znakami, np. `z`, lub całymi słowami, np. `cat`. Długie słowa są dzielone na kilka tokenów. Zbiór wszystkich tokenów używanych przez model nazywa się słownikiem, a proces dzielenia tekstu na tokeny – *tokenizacją*.

Gdy płatności są włączone, [koszt wywołania interfejsu Gemini API](https://ai.google.dev/pricing?hl=pl) jest
częściowo określany przez liczbę tokenów wejściowych i wyjściowych, dlatego warto wiedzieć, jak je
zliczać.

Możesz wypróbować zliczanie tokenów w Colab.

|  |  |  |
| --- | --- | --- |
| [Wyświetl w ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens?hl=pl) | [Wypróbuj notatnik Colab](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=pl) | [Wyświetl notatnik w GitHub](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb?hl=pl) |

## Zliczanie tokenów

Wszystkie dane wejściowe i wyjściowe interfejsu Gemini API są tokenizowane, w tym tekst, pliki graficzne i inne formaty nietekstowe.

Tokeny możesz zliczać na te sposoby:

- **Wywołaj funkcję [`count_tokens`](https://ai.google.dev/api/rest/v1/models/countTokens?hl=pl) z danymi wejściowymi
  żądania.**  
   Zwraca ona łączną liczbę tokenów *tylko w danych wejściowych*. Możesz wywołać tę funkcję przed wysłaniem danych wejściowych do modelu, aby sprawdzić rozmiar żądań.
- **Po wywołaniu funkcji `generate_content` użyj atrybutu `usage_metadata` w obiekcie `response`**  
   Zwraca on łączną liczbę
  tokenów *zarówno w danych wejściowych, jak i wyjściowych*: `total_token_count`.  
   Zwraca też oddzielnie liczbę tokenów w danych wejściowych i wyjściowych: `prompt_token_count` (tokeny wejściowe) i `candidates_token_count` (tokeny wyjściowe).

  Jeśli używasz modelu [myślącego, tokeny użyte podczas procesu myślenia
  są zwracane w `thoughts_token_count`.](https://ai.google.dev/gemini-api/docs/thinking?hl=pl) A jeśli używasz
  [buforowania kontekstu](https://ai.google.dev/gemini-api/docs/caching?hl=pl), liczba tokenów w pamięci podręcznej będzie w `cached_content_token_count`.

### Zliczanie tokenów tekstowych

Jeśli wywołasz funkcję `count_tokens` z danymi wejściowymi zawierającymi tylko tekst, zwróci ona liczbę tokenów tekstu *tylko w danych wejściowych* (`total_tokens`). Możesz wywołać tę funkcję przed wywołaniem funkcji `generate_content`, aby sprawdzić rozmiar żądań.

Inną opcją jest wywołanie funkcji `generate_content`, a następnie użycie atrybutu `usage_metadata` w obiekcie `response`, aby uzyskać te informacje:

- oddzielne liczby tokenów w danych wejściowych (`prompt_token_count`), treści w pamięci podręcznej (`cached_content_token_count`) i danych wyjściowych (`candidates_token_count`);
- liczba tokenów w procesie myślenia (`thoughts_token_count`);
- łączna liczba tokenów *zarówno w danych wejściowych, jak i wyjściowych* (`total_token_count`).

### Python

```
from google import genai

client = genai.Client()
prompt = "The quick brown fox jumps over the lazy dog."

total_tokens = client.models.count_tokens(
    model="gemini-3-flash-preview", contents=prompt
)
print("total_tokens: ", total_tokens)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=prompt
)

print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "The quick brown fox jumps over the lazy dog.";

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: prompt,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

// Convert prompt to a slice of *genai.Content using the helper.
contents := []*genai.Content{
  genai.NewContentFromText(prompt, genai.RoleUser),
}
countResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  return err
}
fmt.Println("total_tokens:", countResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
    ```
```

### Zliczanie tokenów w czacie wieloetapowym

Jeśli wywołasz funkcję `count_tokens` z historią czatu, zwróci ona łączną liczbę tokenów tekstu z każdej roli w czacie (`total_tokens`).

Inną opcją jest wywołanie funkcji `send_message`, a następnie użycie atrybutu `usage_metadata` w obiekcie `response`, aby uzyskać te informacje:

- oddzielne liczby tokenów w danych wejściowych (`prompt_token_count`), treści w pamięci podręcznej (`cached_content_token_count`) i danych wyjściowych (`candidates_token_count`);
- liczba tokenów w procesie myślenia (`thoughts_token_count`);
- łączna liczba tokenów *zarówno w danych wejściowych, jak i wyjściowych* (`total_token_count`).

Aby dowiedzieć się, jak duży będzie następny etap rozmowy, musisz dołączyć go do historii, gdy wywołujesz funkcję `count_tokens`.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

chat = client.chats.create(
    model="gemini-3-flash-preview",
    history=[
        types.Content(
            role="user", parts=[types.Part(text="Hi my name is Bob")]
        ),
        types.Content(role="model", parts=[types.Part(text="Hi Bob!")]),
    ],
)

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=chat.get_history()
    )
)

response = chat.send_message(
    message="In one sentence, explain how a computer works to a young child."
)
print(response.usage_metadata)

extra = types.UserContent(
    parts=[
        types.Part(
            text="What is the meaning of life?",
        )
    ]
)
history = [*chat.get_history(), extra]
print(client.models.count_tokens(model="gemini-3-flash-preview", contents=history))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const history = [
    { role: "user", parts: [{ text: "Hi my name is Bob" }] },
    { role: "model", parts: [{ text: "Hi Bob!" }] },
  ];
  const chat = ai.chats.create({
    model: "gemini-3-flash-preview",
    history: history,
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: chat.getHistory(),
  });
  console.log(countTokensResponse.totalTokens);

  const chatResponse = await chat.sendMessage({
    message: "In one sentence, explain how a computer works to a young child.",
  });
  console.log(chatResponse.usageMetadata);

  const extraMessage = {
    role: "user",
    parts: [{ text: "What is the meaning of life?" }],
  };
  const combinedHistory = [...chat.getHistory(), extraMessage];
  const combinedCountTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: combinedHistory,
  });
  console.log(
    "Combined history token count:",
    combinedCountTokensResponse.totalTokens,
  );
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

history := []*genai.Content{
  {Role: genai.RoleUser, Parts: []*genai.Part({Text: "Hi my name is Bob"})},
  {Role: genai.RoleModel, Parts: []*genai.Part({Text: "Hi Bob!"})},
}
chat, err := client.Chats.Create(ctx, "gemini-3-flash-preview", nil, history)
if err != nil {
  log.Fatal(err)
}

firstTokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", chat.History(false), nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(firstTokenResp.TotalTokens)

resp, err := chat.SendMessage(ctx, genai.NewPartFromText("In one sentence, explain how a computer works to a young child."))
if err != nil {
  log.Fatal(err)
}
fmt.Printf("%#v\n", resp.UsageMetadata)

extra := genai.NewContentFromText("What is the meaning of life?", genai.RoleUser)
hist := chat.History(false)
hist = append(hist, extra)

secondTokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", hist, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println(secondTokenResp.TotalTokens)
```

### Zliczanie tokenów multimodalnych

Wszystkie dane wejściowe interfejsu Gemini API są tokenizowane, w tym tekst, pliki graficzne i inne formaty nietekstowe. Podczas przetwarzania przez interfejs Gemini API pamiętaj o tych najważniejszych kwestiach dotyczących tokenizacji danych wejściowych multimodalnych:

- Dane wejściowe obrazu o obu wymiarach <= 384 piksele są liczone jako 258 tokenów. Obrazy większe w jednym lub obu wymiarach są w razie potrzeby przycinane i skalowane do kafelków o wymiarach 768 x 768 pikseli, z których każdy jest liczony jako 258 tokenów.
- Pliki wideo i audio są konwertowane na tokeny według tych stałych stawek: wideo – 263 tokeny na sekundę, audio – 32 tokeny na sekundę.

#### Rozdzielczości multimediów

[Modele Gemini 3](https://ai.google.dev/gemini-api/docs/models?hl=pl#gemini-3) wprowadzają szczegółową kontrolę nad
przetwarzaniem obrazu multimodalnego za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**.
Wyższe rozdzielczości zwiększają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają zużycie tokenów i opóźnienie.

Więcej informacji o parametrze i jego wpływie na obliczenia tokenów,
znajdziesz w przewodniku po [rozdzielczości multimediów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl).

#### Pliki graficzne

Jeśli wywołasz funkcję `count_tokens` z danymi wejściowymi zawierającymi tekst i obraz, zwróci ona łączną liczbę tokenów tekstu i obrazu *tylko w danych wejściowych* (`total_tokens`). Możesz wywołać tę funkcję przed wywołaniem funkcji `generate_content`, aby sprawdzić rozmiar żądań. Opcjonalnie możesz też wywołać funkcję `count_tokens` oddzielnie dla tekstu i pliku.

Inną opcją jest wywołanie funkcji `generate_content`, a następnie użycie atrybutu `usage_metadata` w obiekcie `response`, aby uzyskać te informacje:

- oddzielne liczby tokenów w danych wejściowych (`prompt_token_count`), treści w pamięci podręcznej (`cached_content_token_count`) i danych wyjściowych (`candidates_token_count`);
- liczba tokenów w procesie myślenia (`thoughts_token_count`);
- łączna liczba tokenów *zarówno w danych wejściowych, jak i wyjściowych* (`total_token_count`).

Przykład, który używa przesłanego obrazu z interfejsu File API:

### Python

```
from google import genai

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = client.files.upload(file=media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";

async function main() {
  const organ = await ai.files.upload({
    file: path.join(media, "organ.jpg"),
    config: { mimeType: "image/jpeg" },
  });

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(organ.uri, organ.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx, 
  filepath.Join(getMedia(), "organ.jpg"), 
  &genai.UploadFileConfig{
    MIMEType : "image/jpeg",
  },
)
if err != nil {
  log.Fatal(err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

Przykład, który udostępnia obraz jako dane wbudowane:

### Python

```
from google import genai
import PIL.Image

client = genai.Client()
prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=[prompt, your_image_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_image_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this image";
const imageBuffer = fs.readFileSync(path.join(media, "organ.jpg"));

const imageBase64 = imageBuffer.toString("base64");

const contents = createUserContent([
  prompt,
  createPartFromBase64(imageBase64, "image/jpeg"),
]);

async function main() {
  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: contents,
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: contents,
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

imageBytes, err := os.ReadFile("organ.jpg")
if err != nil {
    log.Fatalf("Failed to read image file: %v", err)
}
parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this image"),
  {
        InlineData: &genai.Blob{
              MIMEType: "image/jpeg",
              Data:     imageBytes,
        },
  },
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal image token count:", tokenResp.TotalTokens)

response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

#### Pliki wideo lub audio

Audio i wideo są konwertowane na tokeny według tych stałych stawek:

- Wideo: 263 tokeny na sekundę
- Audio: 32 tokeny na sekundę

Jeśli wywołasz funkcję `count_tokens` z danymi wejściowymi zawierającymi tekst i wideo/audio, zwróci ona łączną liczbę tokenów tekstu i pliku wideo/audio *tylko w danych wejściowych* (`total_tokens`). Możesz wywołać tę funkcję przed wywołaniem funkcji `generate_content`, aby sprawdzić rozmiar żądań. Opcjonalnie możesz też wywołać funkcję `count_tokens` oddzielnie dla tekstu i pliku.

Inną opcją jest wywołanie funkcji `generate_content`, a następnie użycie atrybutu `usage_metadata` w obiekcie `response`, aby uzyskać te informacje:

- oddzielne liczby tokenów w danych wejściowych (`prompt_token_count`), treści w pamięci podręcznej (`cached_content_token_count`) i danych wyjściowych (`candidates_token_count`);
- liczba tokenów w procesie myślenia (`thoughts_token_count`);
- łączna liczba tokenów *zarówno w danych wejściowych, jak i wyjściowych* (`total_token_count`).

### Python

```
from google import genai
import time

client = genai.Client()
prompt = "Tell me about this video"
your_file = client.files.upload(file=media / "Big_Buck_Bunny.mp4")

while not your_file.state or your_file.state.name != "ACTIVE":
    print("Processing video...")
    print("File state:", your_file.state)
    time.sleep(5)
    your_file = client.files.get(name=your_file.name)

print(
    client.models.count_tokens(
        model="gemini-3-flash-preview", contents=[prompt, your_file]
    )
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents=[prompt, your_file]
)
print(response.usage_metadata)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});
const prompt = "Tell me about this video";

async function main() {
  let videoFile = await ai.files.upload({
    file: path.join(media, "Big_Buck_Bunny.mp4"),
    config: { mimeType: "video/mp4" },
  });

  while (!videoFile.state || videoFile.state.toString() !== "ACTIVE") {
    console.log("Processing video...");
    console.log("File state: ", videoFile.state);
    await sleep(5000);
    videoFile = await ai.files.get({ name: videoFile.name });
  }

  const countTokensResponse = await ai.models.countTokens({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(countTokensResponse.totalTokens);

  const generateResponse = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([
      prompt,
      createPartFromUri(videoFile.uri, videoFile.mimeType),
    ]),
  });
  console.log(generateResponse.usageMetadata);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)

file, err := client.Files.UploadFromPath(
  ctx,
  filepath.Join(getMedia(), "Big_Buck_Bunny.mp4"),
  &genai.UploadFileConfig{
    MIMEType : "video/mp4",
  },
)
if err != nil {
  log.Fatal(err)
}

for file.State == genai.FileStateUnspecified || file.State != genai.FileStateActive {
  fmt.Println("Processing video...")
  fmt.Println("File state:", file.State)
  time.Sleep(5 * time.Second)

  file, err = client.Files.Get(ctx, file.Name, nil)
  if err != nil {
    log.Fatal(err)
  }
}

parts := []*genai.Part{
  genai.NewPartFromText("Tell me about this video"),
  genai.NewPartFromURI(file.URI, file.MIMEType),
}
contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

tokenResp, err := client.Models.CountTokens(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
fmt.Println("Multimodal video/audio token count:", tokenResp.TotalTokens)
response, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", contents, nil)
if err != nil {
  log.Fatal(err)
}
usageMetadata, err := json.MarshalIndent(response.UsageMetadata, "", "  ")
if err != nil {
  log.Fatal(err)
}
fmt.Println(string(usageMetadata))
```

## Okna kontekstu

Modele dostępne za pomocą interfejsu Gemini API mają okna kontekstu, które są mierzone w tokenach. Okno kontekstu określa, ile danych wejściowych możesz podać i ile danych wyjściowych może wygenerować model. Rozmiar okna kontekstu możesz określić, wywołując punkt końcowy [`models.get` lub sprawdzając [dokumentację modeli](https://ai.google.dev/gemini-api/docs/models?hl=pl).](https://ai.google.dev/api/rest/v1/models/get?hl=pl)

### Python

```
from google import genai

client = genai.Client()
model_info = client.models.get(model="gemini-3-flash-preview")
print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({});

async function main() {
  const modelInfo = await ai.models.get({model: 'gemini-3-flash-preview'});
  console.log(modelInfo.inputTokenLimit);
  console.log(modelInfo.outputTokenLimit);
}

await main();
```

### Go

```
ctx := context.Background()
client, err := genai.NewClient(ctx, nil)
if err != nil {
  log.Fatal(err)
}
modelInfo, err := client.ModelInfo(ctx, "models/gemini-3-flash-preview")
if err != nil {
  log.Fatal(err)
}
fmt.Println("input token limit:", modelInfo.InputTokenLimit)
fmt.Println("output token limit:", modelInfo.OutputTokenLimit)
```

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-04-29 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-04-29 UTC."],[],[]]
