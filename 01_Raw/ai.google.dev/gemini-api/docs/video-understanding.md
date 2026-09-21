---
source_url: https://ai.google.dev/gemini-api/docs/video-understanding?hl=pl
fetched_at: 2026-09-21T05:55:58.354635+00:00
title: "Rozpoznawanie film\u00f3w \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash jest już dostępny. [Przećwicz to samodzielnie](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=pl).

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# Rozpoznawanie filmów

> Więcej informacji o generowaniu filmów znajdziesz w przewodniku po [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=pl).

Modele Gemini mogą przetwarzać filmy, co umożliwia programistom korzystanie z wielu nowych przypadków użycia, które wcześniej wymagały modeli specyficznych dla danej domeny.
Niektóre funkcje Gemini Vision obejmują możliwość opisywania, segmentowania i wyodrębniania informacji z filmów, odpowiadania na pytania dotyczące treści wideo oraz odwoływania się do konkretnych sygnatur czasowych w filmie.

Filmy możesz przekazywać do Gemini na te sposoby:

| Sposób wprowadzania tekstu | Wielkość maksymalna | Zalecany przypadek użycia |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (płatne) / 2 GB (bezpłatne) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), pliki wielokrotnego użytku. |
| [Rejestracja w Cloud Storage](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl#registration) | 2 GB (na plik, bez limitów miejsca na dane) | Duże pliki (ponad 100 MB), długie filmy (ponad 10 minut), trwałe pliki wielokrotnego użytku. |
| [Dane w treści](#inline-video) | < 100 MB | Małe pliki (poniżej 100 MB), krótkie filmy (poniżej 1 minuty), jednorazowe dane wejściowe. |
| [Adresy URL z YouTube](#youtube) | Nie dotyczy | Publiczne filmy na YouTube. |

> **Uwaga:** w większości przypadków zalecamy korzystanie z [File API](#upload-video), zwłaszcza w przypadku plików większych niż 100 MB lub gdy chcesz użyć tego samego pliku w wielu żądaniach.

Więcej informacji o innych metodach wprowadzania plików, takich jak używanie zewnętrznych adresów URL lub plików
przechowywanych w Google Cloud, znajdziesz w przewodniku
[Metody wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Przesyłanie pliku wideo

Poniższy kod pobiera przykładowy film, przesyła go za pomocą [Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl),
czeka na jego przetworzenie, a następnie używa odniesienia do przesłanego pliku, aby
podsumować film.

### Python

```
from google import genai
import time

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

while not myfile.state or myfile.state.name != "ACTIVE":
    print("Processing video...")
    time.sleep(5)
    myfile = client.files.get(name=myfile.name)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "video", "uri": myfile.uri, "mime_type": myfile.mime_type},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  let getFile = await ai.files.get({ name: myfile.name });
  while (getFile.state === 'PROCESSING') {
      getFile = await ai.files.get({ name: myfile.name });
      console.log(`current file status: ${getFile.state}`);
      console.log('File is still processing, retrying in 5 seconds');

      await new Promise((resolve) => {
          setTimeout(resolve, 5000);
      });
  }
  if (getFile.state === 'FAILED') {
      throw new Error('File processing failed.');
  }

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "video", uri: myfile.uri, mime_type: myfile.mimeType },
      { type: "text", text: "Summarize this video. Then create a quiz with an answer key based on the information in this video." }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.FileState;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File myfile =
    client.files.upload(
        "path/to/sample.mp4", UploadFileConfig.builder().mimeType("video/mp4").build());

while (!myfile.state().isPresent()
    || myfile.state().get().knownEnum() != FileState.Known.ACTIVE) {
  System.out.println("Processing video...");
  Thread.sleep(5000);
  myfile = client.files.get(myfile.name().get(), null);
}

Content videoContent =
    VideoContent.builder()
        .uri(myfile.uri().get())
        .mimeType(VideoContentMimeType.of(myfile.mimeType().get()))
        .build();
Content textContent =
    TextContent.builder()
        .text(
            "Summarize this video. Then create a quiz with an answer key based on the information in this video.")
        .build();

List<Content> contents = Arrays.asList(videoContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
file_name=$(jq -r ".file.name" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# Polling loop
echo "Waiting for file to be processed..."
while true; do
  curl -s "https://generativelanguage.googleapis.com/v1beta/${file_name}" \
    -H "x-goog-api-key: $GEMINI_API_KEY" > file_status.json
  state=$(jq -r ".state" file_status.json)
  echo "Current state: $state"
  if [ "$state" == "ACTIVE" ]; then
    break
  elif [ "$state" == "FAILED" ]; then
    echo "File processing failed."
    exit 1
  fi
  sleep 5
done

echo "Generating content from video..."
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "video", "uri": "'${file_uri}'", "mime_type": "'${MIME_TYPE}'"},
        {"type": "text", "text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}
      ]
    }' 2> /dev/null > response.json

jq ".steps[].content[0].text" response.json
```

Aby zoptymalizować wydajność i wykorzystanie tokenów, rozważ użycie
[przetwarzania wideo przez agenta](#agentic-video-understanding).

Zawsze używaj Files API, gdy łączny rozmiar żądania (w tym pliku, prompta tekstowego, instrukcji systemowych itp.) jest większy niż 20 MB, czas trwania filmu jest znaczący lub gdy zamierzasz użyć tego samego filmu w wielu promptach.
File API bezpośrednio akceptuje formaty plików wideo.

Więcej informacji o pracy z plikami multimedialnymi znajdziesz w artykule
[Files API](https://ai.google.dev/gemini-api/docs/files?hl=pl).

### Przekazywanie danych wideo w treści

Zamiast przesyłać plik wideo za pomocą File API, możesz przekazywać mniejsze filmy bezpośrednio w żądaniu. Jest to odpowiednie rozwiązanie w przypadku krótszych filmów o łącznym rozmiarze żądania poniżej 20 MB.

Oto przykład przekazywania danych wideo w treści:

### Python

```
from google import genai
import base64

video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "data": base64.b64encode(video_bytes).decode('utf-8'),
            "mime_type": "video/mp4"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      data: base64VideoFile,
      mime_type: "video/mp4",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.interactions.VideoContentMimeType;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

String videoFileName = "/path/to/your/video.mp4";
byte[] videoBytes = Files.readAllBytes(Paths.get(videoFileName));
String base64Video = Base64.getEncoder().encodeToString(videoBytes);

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .data(base64Video)
        .mimeType(VideoContentMimeType.VIDEO_MP4)
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'",
          "mime_type": "video/mp4"
        }
      ]
    }' 2> /dev/null
```

### Przekazywanie adresów URL z YouTube

Adresy URL z YouTube możesz przekazywać bezpośrednio do Gemini API w ramach żądania w ten sposób:

### Python

```
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    model='gemini-3.8-flash',
    input=[
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
            "type": "video",
            "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    { type: "text", text: "Please summarize the video in 3 sentences." },
    {
      type: "video",
      uri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    }
  ],
});
console.log(interaction.output_text);
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.interactions.VideoContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent =
    TextContent.builder().text("Please summarize the video in 3 sentences.").build();
Content videoContent =
    VideoContent.builder()
        .uri("https://www.youtube.com/watch?v=9hE5-98ZeCg")
        .build();

List<Content> contents = Arrays.asList(textContent, videoContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Please summarize the video in 3 sentences."},
        {
          "type": "video",
          "uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
        }
      ]
    }' 2> /dev/null
```

**Ograniczenia:**

- W przypadku poziomu bezpłatnego nie możesz przesyłać więcej niż 8 godzin filmów na YouTube dziennie.
- W przypadku płatnego poziomu nie ma limitu opartego na długości wideo.
- W przypadku modeli wcześniejszych niż Gemini 2.5 możesz przesłać tylko 1 film na żądanie. W przypadku modeli Gemini 2.5 i nowszych możesz przesłać maksymalnie 10 filmów na żądanie.
- Możesz przesyłać tylko filmy publiczne (nie prywatne ani niepubliczne).

## Analizowanie filmów przez agenta

Domyślnie dane wejściowe wideo są przetwarzane statycznie (wyodrębnianie klatek z szybkością 1 kl./s).
Modele Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash i 3.5 Flash Lite obsługują też
**analizowanie filmów przez agenta**, w którym model dynamicznie analizuje oś czasu
filmu, selektywnie sprawdza transkrypcje i na bieżąco dostosowuje liczbę klatek na
sekundę oraz rozdzielczość na podstawie prompta.

| **Tryb** | **Opis** | **Obsługiwane modele** |
| --- | --- | --- |
| **Statyczny** (domyślnie) | Wyodrębnia klatki ze stałą szybkością (1 kl./s) i umieszcza je w kontekście w jednym przebiegu. Dobrze sprawdza się w przypadku krótkich klipów. | Wszystkie modele Gemini |
| **Rozwiązania agentowe** | Model dynamicznie porusza się po osi czasu filmu, wczytując tylko te treści, których potrzebuje na podstawie prompta. Do 88% większa wydajność tokenów i o ok. 7% wyższa jakość w przypadku długich treści. | Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite |

### Wybieranie trybu przetwarzania

Ogólnie rzecz biorąc, zacznij od trybu **rozwiązań agentowych**, zwłaszcza gdy optymalizujesz jakość odpowiedzi lub wydajność tokenów.

- **Rozwiązania agentowe:** długie filmy lub zapytania dotyczące konkretnych momentów. Model dynamicznie porusza się po osi czasu, aby znaleźć informacje istotne w kontekście, bez wypełniania okna kontekstu.
- **Statyczny:** zapytania wrażliwe na opóźnienia w przypadku krótkich klipów (poniżej 5 minut) lub przypadki, w których wymagana jest precyzja na poziomie klatek w całym klipie.

> **Uwaga:** w przypadku długich filmów lub złożonych promptów, w których przetwarzanie przez agenta zajmuje więcej czasu, użyj strumieniowania (`stream=True`) lub wykonywania w tle (`background=True`). Dzięki temu połączenie pozostaje aktywne, wyświetlane są pośrednie kroki wnioskowania i unikasz przekroczenia limitu czasu połączenia lub uwierzytelnienia.

### Ustawianie trybu przetwarzania

### Python

```
import time
from google import genai

client = genai.Client()

# Upload a long video
video_file = client.files.upload(file="path/to/lecture.mp4")

while video_file.state.name == "PROCESSING":
    time.sleep(2)
    video_file = client.files.get(name=video_file.name)

# Use agentic processing
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": "agentic"
        },
        {"type": "text", "text": "What are the three main arguments presented?"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

// Upload a long video
let videoFile = await ai.files.upload({
  file: "path/to/lecture.mp4",
  config: { mimeType: "video/mp4" }
});

while (videoFile.state === "PROCESSING") {
  await new Promise((resolve) => setTimeout(resolve, 2000));
  videoFile = await ai.files.get({ name: videoFile.name });
}

// Use agentic processing
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: "agentic"
    },
    { type: "text", text: "What are the three main arguments presented?" }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {"type": "text", "text": "What are the three main arguments presented?"}
    ]
  }' 2> /dev/null
```

> **Uwaga:** aby sprawdzić, czy użyto przetwarzania przez agenta, sprawdź `interaction.steps`. Obecność `processing_call` i `processing_result` oznacza, że model dynamicznie poruszał się po filmie.

### Kroki odpowiedzi

Przetwarzanie przez agenta dodaje do tablicy `steps` 2 nowe typy kroków:

- `processing_call`: model poprosił o segment wideo lub transkrypcję dźwięku, zidentyfikowane przez `id`.
- `processing_result`: wynik tego wczytania, połączony przez `call_id`.

Pojawiają się one przeplatane z krokami `thought` (gdy włączone są podsumowania) i poprzedzają ostatni krok `model_output`. Można ich używać do wyświetlania śladu postępu w interfejsie, ale nie wymagają odpowiedzi.

Ten przykład pokazuje ładunek odpowiedzi z przeplatanymi krokami przetwarzania:

```
{
  "steps": [
    {
      "type": "thought",
      "signature": "sig_thought_1",
      "summary": [
        {
          "type": "text",
          "text": "Inspecting transcript for key discussion topics..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_01",
      "signature": "sig_call_01"
    },
    {
      "type": "processing_result",
      "call_id": "call_01",
      "signature": "sig_result_01"
    },
    {
      "type": "thought",
      "signature": "sig_thought_2",
      "summary": [
        {
          "type": "text",
          "text": "Loading visual frames to verify slide content..."
        }
      ]
    },
    {
      "type": "processing_call",
      "id": "call_02",
      "signature": "sig_call_02"
    },
    {
      "type": "processing_result",
      "call_id": "call_02",
      "signature": "sig_result_02"
    },
    {
      "type": "thought",
      "signature": "sig_thought_3",
      "summary": [
        {
          "type": "text",
          "text": "Synthesizing answer from gathered evidence..."
        }
      ]
    },
    {
      "type": "model_output",
      "content": [
        {
          "type": "text",
          "text": "The three main arguments presented in the lecture are..."
        }
      ]
    }
  ]
}
```

### Łączenie trybów przetwarzania w różnych filmach

W tym samym żądaniu możesz ustawić różne tryby przetwarzania dla każdego filmu:

### Python

```
from google import genai

client = genai.Client()

lecture = client.files.upload(file="path/to/long-lecture.mp4")
experiment = client.files.upload(file="path/to/short-experiment.mp4")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": lecture.uri,
            "mime_type": lecture.mime_type,
            "processing": "agentic"  # Use agentic video understanding
        },
        {
            "type": "video",
            "uri": experiment.uri,
            "mime_type": experiment.mime_type,
            "processing": "static"  # Use static processing
        },
        {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const lecture = await ai.files.upload({
  file: "path/to/long-lecture.mp4",
  config: { mimeType: "video/mp4" }
});
const experiment = await ai.files.upload({
  file: "path/to/short-experiment.mp4",
  config: { mimeType: "video/mp4" }
});

const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: lecture.uri,
      mime_type: lecture.mimeType,
      processing: "agentic" // Use agentic video understanding
    },
    {
      type: "video",
      uri: experiment.uri,
      mime_type: experiment.mimeType,
      processing: "static" // Use static processing
    },
    { type: "text", text: "Compare the lecture content with the experiment results." }
  ]
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${lecture_uri}'",
        "mime_type": "video/mp4",
        "processing": "agentic"
      },
      {
        "type": "video",
        "uri": "'${experiment_uri}'",
        "mime_type": "video/mp4",
        "processing": "static"
      },
      {"type": "text", "text": "Compare the lecture content with the experiment results."}
    ]
  }' 2> /dev/null
```

### Rozmowy wideo wieloetapowe

Kontekst wideo jest zachowywany w kolejnych etapach rozmowy. W przypadku korzystania z przetwarzania przez agenta:

- **Tryb stanowy** (z użyciem `previous_interaction_id`): serwer zachowuje kontekst wideo. Nie jest wymagana żadna dodatkowa obsługa.
- **Tryb bezstanowy** (z użyciem `step_list`): w trybie bezstanowym odpowiedź zawiera kroki `processing_call` i `processing_result`, które kodują kontekst wideo. Aby zachować kontekst wideo, musisz uwzględnić wszystkie kroki z odpowiedzi w `step_list` następnego żądania. Chociaż pominięcie ich nie powoduje obecnie błędu interfejsu API, kontekst wideo zostaje utracony, co znacznie obniża jakość odpowiedzi na pytania uzupełniające. Pamiętaj, że zwrócone kroki wysyłane w kolejnych żądaniach są uwzględniane w liczbie tokenów wejściowych.

## Odwoływanie się do sygnatur czasowych w treści

Możesz zadawać pytania dotyczące konkretnych momentów w filmie, używając sygnatur czasowych w formacie `MM:SS`.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?"
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Java

```
String prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Wyodrębnianie szczegółowych informacji z filmu

Modele Gemini oferują zaawansowane możliwości analizowania treści wideo dzięki przetwarzaniu informacji z **ścieżek audio i wizualnych**. Dzięki temu możesz wyodrębnić bogaty zestaw szczegółów, w tym generować opisy tego, co dzieje się w filmie, i odpowiadać na pytania dotyczące jego treści.

W przypadku opisów wizualnych model próbkuje film z szybkością **1 klatka na sekundę** (kl./s). Ta domyślna szybkość próbkowania sprawdza się w przypadku większości treści, ale pamiętaj, że może pomijać szczegóły w filmach z szybkim ruchem lub szybkimi zmianami scen.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Java

```
String prompt =
    "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Dostosowywanie przetwarzania wideo

Przetwarzanie wideo w Gemini API możesz dostosować, ustawiając interwały przycinania lub podając niestandardowe próbkowanie liczby klatek na sekundę. Te opcje dostosowywania
są obsługiwane tylko podczas przetwarzania filmu w trybie `"static"`.

### Ustawianie interwałów przycinania

Możesz przyciąć film, określając `start_offset` i `end_offset` w obiekcie konfiguracji `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "start_offset": 1200,
                "end_offset": 1500,
            },
        },
        {"type": "text", "text": "Summarize this section of the video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        start_offset: 1200,
        end_offset: 1500,
      },
    },
    { type: "text", text: "Summarize this section of the video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "start_offset": 1200,
          "end_offset": 1500
        }
      },
      {"type": "text", "text": "Summarize this section of the video."}
    ]
  }' 2> /dev/null
```

### Ustawianie niestandardowej liczby klatek na sekundę

Możesz ustawić niestandardowe próbkowanie liczby klatek na sekundę, przekazując argument `fps` w obiekcie konfiguracji `processing`.

### Python

```
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {
            "type": "video",
            "uri": video_file.uri,
            "mime_type": video_file.mime_type,
            "processing": {
                "type": "static",
                "fps": 0.5,  # Sample 1 frame every 2 seconds
            },
        },
        {"type": "text", "text": "Describe the scene changes in this video."},
    ],
)
print(interaction.output_text)
```

### JavaScript

```
const interaction = await ai.interactions.create({
  model: "gemini-3.8-flash",
  input: [
    {
      type: "video",
      uri: videoFile.uri,
      mime_type: videoFile.mimeType,
      processing: {
        type: "static",
        fps: 0.5, // Sample 1 frame every 2 seconds
      },
    },
    { type: "text", text: "Describe the scene changes in this video." },
  ],
});
console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {
        "type": "video",
        "uri": "'${file_uri}'",
        "mime_type": "video/mp4",
        "processing": {
          "type": "static",
          "fps": 0.5
        }
      },
      {"type": "text", "text": "Describe the scene changes in this video."}
    ]
  }' 2> /dev/null
```

## Obsługiwane formaty wideo

Gemini obsługuje te typy MIME formatów wideo:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Szczegóły techniczne dotyczące filmów

- **Obsługiwane modele i kontekst**: wszystkie modele Gemini mogą przetwarzać dane wideo.
  - Modele z oknem kontekstu o rozmiarze 1 mln tokenów mogą domyślnie przetwarzać filmy o długości do 3 godzin (przy niskiej rozdzielczości multimediów) lub do 1 godziny (przy wysokiej rozdzielczości multimediów).
- **Tryby przetwarzania**: modele Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash Lite,
  i nowsze obsługują 2 tryby przetwarzania wideo:
  - **Statyczny**: klatki są wyodrębniane z szybkością 1 kl./s i umieszczane w kontekście (domyślnie
    we wszystkich modelach). Dźwięk jest przetwarzany z szybkością 1 kb/s (jeden kanał).
    Sygnatury czasowe są dodawane co sekundę. Najlepsze rozwiązanie w przypadku krótkich klipów lub gdy liczy się każda klatka (np. podczas sprawdzania klatka po klatce). Pamiętaj, że szybkie sekwencje akcji mogą utracić szczegóły ze względu na szybkość próbkowania wynoszącą 1 kl./s.
  - **Rozwiązania agentowe**: model dynamicznie porusza się po filmie, wczytując na żądanie
    transkrypcję, klatki lub dźwięk. W przypadku długich treści zużywa do 88% mniej tokenów, ale nawigacja może nieznacznie zwiększyć czas do pierwszego tokena (TTFT) w przypadku krótkich klipów (poniżej 5 minut) ze względu na wewnętrzne rozumowanie i wywołania narzędzi przed rozpoczęciem generowania. Najlepsze rozwiązanie w przypadku długich filmów, aby zoptymalizować koszty tokenów i jakość odpowiedzi.
    Obsługiwane w modelach Gemini 3.8 Flash, 3.7 Flash, 3.6 Flash i 3.5 Flash Lite.
    Więcej informacji znajdziesz w sekcji [Analizowanie filmów przez agenta](#agentic-video-understanding).
- **Obliczanie tokenów (tryb statyczny)**: każda sekunda filmu jest tokenizowana w ten sposób:
  w następujący sposób:
  - Pojedyncze klatki (próbkowane z szybkością 1 kl./s):
    - Jeśli `media_resolution` jest ustawiona na niską, klatki są tokenizowane z szybkością 66 tokenów na klatkę.
    - W przeciwnym razie klatki są tokenizowane z szybkością 258 tokenów na klatkę.
  - Dźwięk: 32 tokeny na sekundę.
  - Uwzględniane są też metadane.
  - Łącznie: około 100 tokenów na sekundę filmu przy domyślnej (niskiej) rozdzielczości multimediów lub około 300 tokenów na sekundę filmu przy wysokiej rozdzielczości multimediów.
- **Obliczanie tokenów (tryb rozwiązań agentowych)**: zużycie tokenów różni się w zależności od złożoności treści
  i strategii nawigacji modelu. Tokeny rozumowania nawigacji generowane podczas eksploracji filmu są traktowane jako **tokeny myśli** (`total_thought_tokens`), a klatki, dźwięk i transkrypcja wczytywane na żądanie są traktowane jako tokeny użycia narzędzi (`total_tool_use_tokens`). Przetwarzanie agentowe zwykle zużywa do 88% mniej tokenów niż przetwarzanie statyczne w przypadku długich treści, ponieważ model wczytuje tylko transkrypcję, klatki lub dźwięk potrzebne do odpowiedzi na prompt (patrz [przewodnik po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl#video-token-usage)).
- **Rozdzielczość multimediów**: Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem multimodalnym
  za pomocą parametru `media_resolution`. Parametr `media_resolution` określa **maksymalną liczbę tokenów przydzielonych na obraz wejściowy lub klatkę wideo**. Wyższe rozdzielczości poprawiają zdolność modelu do odczytywania drobnego tekstu lub identyfikowania małych szczegółów, ale zwiększają zużycie tokenów i opóźnienie. Parametry `media_resolution` i `processing` są niezależne: możesz ustawić oba w tym samym wejściu wideo.

Więcej informacji o obliczaniu tokenów znajdziesz w
[przewodniku po tokenach](https://ai.google.dev/gemini-api/docs/tokens?hl=pl).

- **Format sygnatury czasowej**: gdy w prompcie odwołujesz się do konkretnych momentów w filmie, użyj formatu `MM:SS` (np. `01:15` oznacza 1 minutę i 15 sekund).
- **Umieszczanie prompta**: jeśli łączysz tekst i pojedynczy film, umieść prompt tekstowy
  *po* części wideo w tablicy `input`.
- **Limity czasu w przypadku długich żądań**: w przypadku filmów, które wymagają dłuższego
  czasu przetwarzania lub złożonego wnioskowania wieloetapowego, użyj strumieniowania
  (`stream=True`) lub wykonywania w tle (`background=True`).
  Synchroniczne żądania bez strumieniowania, które w przypadku dużego zapotrzebowania powodują ponawianie prób na backendzie, mogą przekroczyć okna ważności tokenów połączenia lub uwierzytelnienia,
  co może powodować nieoczekiwane `401 Unauthorized` lub przekroczenia limitu czasu.
  Strumieniowanie utrzymuje aktywne połączenie i wyświetla pośrednie wnioskowanie oraz postęp wywołań narzędzi.

## Co dalej?

- [Rozdzielczość multimediów](https://ai.google.dev/gemini-api/docs/media-resolution?hl=pl): kontroluj
  rozdzielczość klatek wideo, aby zrównoważyć jakość i zużycie tokenów.
- [Tokeny](https://ai.google.dev/gemini-api/docs/tokens?hl=pl): dowiedz się, jak treści wideo są tokenizowane
  w trybie statycznym i trybie rozwiązań agentowych.
- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować działaniem modelu na podstawie
  konkretnych potrzeb i przypadków użycia.
- [Interfejs API plików](https://ai.google.dev/gemini-api/docs/files?hl=pl): dowiedz się więcej o przesyłaniu plików i zarządzaniu nimi na potrzeby Gemini.
- [Strategie tworzenia promptów dla plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, obrazów, dźwięków i filmów, czyli tworzenie promptów multimodalnych.
- [Wskazówki dotyczące bezpieczeństwa](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=pl): modele generatywnej AI
  czasami generują nieoczekiwane wyniki, np. niedokładne,
  stronnicze lub obraźliwe. Przetwarzanie końcowe i ocena przez człowieka są niezbędne, aby ograniczyć ryzyko szkód wynikających z takich danych wyjściowych.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-09-18 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-09-18 UTC."],[],[]]
