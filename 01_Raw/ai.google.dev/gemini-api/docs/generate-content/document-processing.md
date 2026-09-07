---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=pl
fetched_at: 2026-09-07T05:42:28.923288+00:00
title: "rozumienie dokument\u00f3w; \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# rozumienie dokumentów;

Modele Gemini mogą przetwarzać dokumenty w formacie PDF, korzystając z natywnego rozpoznawania obrazu, aby zrozumieć kontekst całego dokumentu. To coś więcej niż tylko wyodrębnianie tekstu. Gemini może:

- analizować i interpretować treści, w tym tekst, obrazy, diagramy, wykresy i tabele, nawet w długich dokumentach do 1000 stron;
- wyodrębniać informacje do [ustrukturyzowanych formatów wyjściowych](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl);
- podsumowywać dokumenty i odpowiadać na pytania na podstawie elementów wizualnych i tekstowych;
- transkrybować zawartość dokumentu (np. do HTML), zachowując układ i formatowanie, do wykorzystania w aplikacjach podrzędnych.

W ten sam sposób możesz też przekazywać dokumenty w innych formatach niż PDF, ale Gemini będzie je traktować jako zwykły tekst, co spowoduje utratę kontekstu, np. wykresów czy formatowania.

## Przekazywanie danych PDF w tekście

Dane PDF możesz przekazywać w tekście w żądaniu do `generateContent`. Najlepiej sprawdza się to w przypadku mniejszych dokumentów lub przetwarzania tymczasowego, gdy nie musisz odwoływać się do pliku w kolejnych żądaniach. W przypadku większych dokumentów, do których musisz się odwoływać w interakcjach wieloetapowych, zalecamy korzystanie z interfejsu [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs)
aby skrócić czas oczekiwania na odpowiedź i zmniejszyć zużycie przepustowości.

Poniższy przykład pokazuje, jak pobrać plik PDF z adresu URL i przekonwertować go na bajty do przetworzenia:

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"

# Retrieve and encode the PDF byte
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[
        types.Part.from_bytes(
            data=doc_data,
            mime_type='application/pdf',
        ),
        prompt
    ]
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const pdfResp = await fetch('https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf'>)
        .then((response) = response.arrayBuffer());

    const contents = [
        { text: "Summarize this document" },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
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
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx :=& context.Background()
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfResp, _ := http.Get("https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019&&_3_art_0_py4t4l_convrt.pdf")
    var pdfBytes []byte
    if pdfResp != nil  pdfResp.Body != nil {
        pdfBytes, _ = io.ReadAll(pdfRes&p.Body)
        pdfResp.Body.Close()&
    }

    parts := []*genai.Part{
        genai.Part{
            InlineData: genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
    }

    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and>& set flags accordingly
if [[ "$(base64 --version 21)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
      >    {">inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

Możesz też odczytać plik PDF z pliku lokalnego do przetworzenia:

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'fs';

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const contents = [
        { text: "Summarize this document" },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(fs.readFileSync("content/343019_3_art_0_py4t4l_convrt.pdf")).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
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

    ctx := context.Background(&)
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfBytes, _ := os.ReadFile("path/t&o/your/file.pdf")

    parts :=& []*genai.Part{
        genai.Part{
            InlineData: genai.Blob{
                MIMEType: "application/pdf",
                Data:     pdfBytes,
            },
        },
        genai.NewPartFromText("Summarize this document"),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(parts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

## Przesyłanie plików PDF za pomocą interfejsu Files API

W przypadku większych plików lub gdy chcesz ponownie użyć dokumentu w wielu żądaniach, zalecamy korzystanie z interfejsu Files API. Poprawia to czas oczekiwania na odpowiedź i zmniejsza zużycie przepustowości, ponieważ przesyłanie plików jest oddzielone od żądań do modelu.

### Duże pliki PDF z adresów URL

Użyj interfejsu File API, aby uprościć przesyłanie i przetwarzanie dużych plików PDF z adresów URL:

### Python

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.6-flash",
  contents=[sample_doc, prompt])
print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {

    const pdfBuffer = await fetch("https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf&quo>t;)
        .then((response) = response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retry>ing in 5 seconds');

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    &&const content = [
        'Summarize this document',
    ];

    if (file.uri  file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);

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
  "net/http"
  "os"
  "google.golang.org/genai"
)

func main() {

  ctx &:= context.Background()
  client, _ := genai.NewClient(ctx, genai.ClientConfig{
    APIKey:  os.Getenv("GEMINI_API_KEY"),
    Backend: genai.BackendGeminiAPI,
  })

  pdfURL := "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
  localPdfPath := "A17_FlightPlan_downloaded.pdf"

  respHttp, _ := http.Get(pdfURL)
  defer respHttp.Body.Close()

  outFile, _ := os.Create(localPdfP&ath)
  defer outFile.Close()

  _, _ = io.Copy(outFile, respHttp.Body)

  uploadConfig := genai.UploadFileConfig{MIMEType: "application/pdf"}
  uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

  promptParts := []*genai.Part{
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
    genai.NewPartFromText("Summarize this document"),
  }
  contents := []*genai.Content{
    genai.NewContentFromParts(promptParts, genai.RoleUser), // Specify role
  }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

  fmt.Println(result.Text())
}
```

### REST

```
PDF_PATH="https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
DISPLAY_NAME="A17_FlightPlan"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --m<ime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c  "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upl>oad-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2 /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${>tmp_header_>file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2 /dev/null  file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1b>eta/models/>gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      ";contents": [{
        "parts":[
          {"text": "'$PROMPT'"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

### Duże pliki PDF przechowywane lokalnie

### Python

```
from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

# Retrieve and encode the PDF byte
file_path = pathlib.Path('large_file.pdf')

# Upload the PDF using the File API
sample_file = client.files.upload(
    file=file_path,
)

prompt="Summarize this document"

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[sample_file, "Summarize this document"])
print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const file = await ai.files.upload({
        file: 'path-to-localfile.pdf'
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 s>econds');

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const cont&&ent = [
        'Summarize this document',
    ];

    if (file.uri  file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash9;,
        contents: content,
    });

    console.log(response.text);

}

main();
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

    ctx := context.Background(&)
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })
    localPd&fPath := "/path/to/file.pdf"

    uploadConfig := genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile, _ := client.Files.UploadFromPath(ctx, localPdfPath, uploadConfig)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
        genai.NewPartFromText("Give me a summary of this pdf file."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: applicati>on/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2 /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_u>rl}" \>
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2 /dev/null  file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
 >   -X POST >\
    -d '{
      "contents": [{
        "parts":[
          {"text": "Can you add a few more lines to this poem?"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

Możesz sprawdzić, czy interfejs API prawidłowo zapisał przesłany plik, i pobrać jego
metadane, wywołując [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=pl). Unikalne są tylko `name` (a co za tym idzie, `uri`).

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload(file='example.txt')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### REST

```
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/fi>les/$name  file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Przekazywanie wielu plików PDF

Interfejs Gemini API może przetwarzać wiele dokumentów PDF (do 1000 stron) w jednym żądaniu, o ile łączny rozmiar dokumentów i prompta tekstowego mieści się w oknie kontekstu modelu.

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805"
doc_url_2 = "https://arxiv.org/pdf/2403.05530"

# Retrieve and upload both PDFs using the File API
doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=[sample_pdf_1, sample_pdf_2, prompt]
)

print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
      >  .then((response) = response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    // Wait for the file to be processed.
    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds&#>39;);

        await new Promise((resolve) = {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const content = [
        'What is the difference between each of the main benchmarks between these two papers? Output these in a table.',
    ];

    let file1 = await uploadRemot&&ePDF("https://arxiv.org/pdf/2312.11805", "PDF 1")
    if (file1.uri  file1.mimeType) {
        const fileContent = createPartFromUri(file1.uri, file1.mimeType);
        content.push(fileContent);
    }
    let file2&& = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2")
    if (file2.uri  file2.mimeType) {
        const fileContent = createPartFromUri(file2.uri, file2.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);
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
    "net/http"
    "os"
    "google.golang.org/genai"
)

func main() {

    ctx :=& context.Background()
    client, _ := genai.NewClient(ctx, genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    docUrl1 := "https://arxiv.org/pdf/2312.11805"
    docUrl2 := "https://arxiv.org/pdf/2403.05530"
    localPath1 := "doc1_downloaded.pdf"
    localPath2 := "doc2_downloaded.pdf"

    respHttp1, _ := http.Get(docUrl1)
    defer respHttp1.Body.Close()

    outFile1, _ := os.Create(localPath1)
    _, _ = io.Copy(outFile1, respHttp1.Body)
    outFile1.Close()

    respHttp2, _ := http.Get(docUrl2)
    defer respHttp2.Body.Close()

    outFile2, _ := &os.Create(localPath2)
    _, _ = io.Copy(outFile2, respHttp2.Body)
    outFile2.Close()

    uploadConfig1 := genai.UploadFileConfig{MIMEType: "applicati&on/pdf"}
    uploadedFile1, _ := client.Files.UploadFromPath(ctx, localPath1, uploadConfig1)

    uploadConfig2 := genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile2, _ := client.Files.UploadFromPath(ctx, localPath2, uploadConfig2)

    promptParts := []*genai.Part{
        genai.NewPartFromURI(uploadedFile1.URI, uploadedFile1.MIMEType),
        genai.NewPartFromURI(uploadedFile2.URI, uploadedFile2.MIMEType),
        genai.NewPartFromText("What is the difference between each of the " +
                              "main benchmarks between these two papers? " +
                              "Output these in a table."),
    }
    contents := []*genai.Content{
        genai.NewContentFromParts(promptParts, genai.RoleUser),
    }

    modelName := "gemini-3.6-flash"
    result, _ := client.Models.GenerateContent(
        ctx,
        modelName,
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

### REST

```
DOC_URL_1="https://arxiv.org/pdf/2312.11805"
DOC_URL_2="https://arxiv.org/pdf/2403.05530"
DISPLAY_NAME_1="Gemini_paper"
DISPLAY_NAME_2="Gemini_1.5_paper"
PROMPT="What is the difference between each of the main benchmarks between these two papers? Output these in a table."

# Function to download and upload a PDF
upload_pdf() {
  local doc_url="$1"
  local display_name="$2"

  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}"
<
  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c  "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}"
  echo "NUM_BYTES: ${NUM_BYTES}"

  local tmp_header_file=upload-header.tmp

  # Initial resumable request
  curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length>: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2 /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" >" -f2 >| tr -d "\r")
  rm "${tmp_header_file}"

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2 /dev/null  "file_info_${display_name}.json"

  local file_uri=$(jq ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}"

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Now generate content using both files
curl "https://g>enerativela>nguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_1'}},
          {"file_data": {"mime_type": "application/pdf", "file_uri": '$file_uri_2'}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2 /dev/null  response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Szczegóły techniczne

Gemini obsługuje pliki PDF o rozmiarze do 50 MB lub 1000 stron. Ten limit dotyczy zarówno danych w tekście, jak i przesyłania za pomocą interfejsu Files API. Każda strona dokumentu odpowiada 258 tokenom.

Oprócz
okna [kontekstu](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) modelu nie ma konkretnych limitów liczby pikseli w dokumencie. Większe strony są
zmniejszane do maksymalnej rozdzielczości 3072 x 3072 pikseli przy zachowaniu oryginalnych
proporcji, a mniejsze strony są powiększane do 768 x 768 pikseli. Nie ma obniżki kosztów w przypadku stron o mniejszym rozmiarze (oprócz przepustowości) ani poprawy wydajności w przypadku stron o wyższej rozdzielczości.

### Modele Gemini 3

Gemini 3 wprowadza szczegółową kontrolę nad przetwarzaniem obrazu multimodalnego za pomocą parametru `media_resolution`. Teraz możesz ustawić rozdzielczość na niską, średnią lub wysoką dla każdej części multimedialnej. Wraz z tym dodatkiem zaktualizowano przetwarzanie dokumentów PDF:

1. **Natywne uwzględnianie tekstu:** tekst natywnie osadzony w pliku PDF jest wyodrębniany i przekazywany do modelu.
2. **Rozliczenia i raportowanie tokenów:**
   - **Nie naliczamy opłat** za tokeny pochodzące z wyodrębnionego **tekstu natywnego** w plikach PDF.
   - W sekcji `usage_metadata` odpowiedzi interfejsu API tokeny wygenerowane na podstawie przetwarzania stron PDF (jako obrazów) są teraz zliczane w ramach modalności `IMAGE`, a nie w osobnej modalności `DOCUMENT`, jak w niektórych wcześniejszych wersjach.

Więcej informacji o parametrze rozdzielczości multimediów znajdziesz w
[przewodniku po rozdzielczości multimediów](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=pl).

### Typy dokumentów

Technicznie możesz przekazywać inne typy MIME do rozpoznawania dokumentów, takie jak TXT, Markdown, HTML, XML itp. Jednak rozpoznawanie dokumentów ***rozumie tylko pliki PDF***. Inne typy będą wyodrębniane jako czysty tekst, a model nie będzie w stanie zinterpretować tego, co widzimy w renderowaniu tych plików. Utracone zostaną wszelkie szczegóły dotyczące typu pliku, takie jak wykresy, diagramy, tagi HTML, formatowanie Markdown itp.

Więcej informacji o innych metodach wprowadzania plików znajdziesz w
[przewodniku po metodach wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Sprawdzone metody

Aby uzyskać najlepsze wyniki:

- Przed przesłaniem obróć strony do prawidłowej orientacji.
- Unikaj rozmazanych stron.
- Jeśli używasz jednej strony, umieść prompta tekstowego po stronie.

## Co dalej?

Więcej informacji znajdziesz w tych materiałach:

- [Strategie tworzenia promptów z plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): interfejs Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, graficznych, dźwiękowych i wideo, czyli tworzenie promptów multimodalnych.
- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować działaniem modelu na podstawie
  konkretnych potrzeb i przypadków użycia.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
