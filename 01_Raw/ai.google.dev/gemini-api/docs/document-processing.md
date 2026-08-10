---
source_url: https://ai.google.dev/gemini-api/docs/document-processing?hl=pl
fetched_at: 2026-08-10T03:25:26.139460+00:00
title: "rozumienie dokument\u00f3w; \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interfejs Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=pl) jest już ogólnie dostępny. Zalecamy korzystanie z tego interfejsu API, aby mieć dostęp do wszystkich najnowszych funkcji i modeli.

![](https://ai.google.dev/_static/images/translated.svg?hl=pl)

Google używa technologii AI do tłumaczenia treści na Twój preferowany język. Tłumaczenia wygenerowane przez AI mogą zawierać błędy.

- [Strona główna](https://ai.google.dev/?hl=pl)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pl)
- [Dokumenty](https://ai.google.dev/gemini-api/docs?hl=pl)

Prześlij opinię

# rozumienie dokumentów;

Modele Gemini mogą przetwarzać dokumenty w formacie PDF, korzystając z natywnego rozpoznawania obrazu, aby zrozumieć cały kontekst dokumentu. To coś więcej niż tylko wyodrębnianie tekstu. Gemini może:

- analizować i interpretować treści, w tym tekst, obrazy, diagramy, wykresy i tabele, nawet w długich dokumentach do 1000 stron;
- wyodrębniać informacje do [ustrukturyzowanych formatów wyjściowych](https://ai.google.dev/gemini-api/docs/structured-output?hl=pl);
- podsumowywać dokumenty i odpowiadać na pytania na podstawie elementów wizualnych i tekstowych w dokumencie;
- transkrybować zawartość dokumentu (np. do formatu HTML), zachowując układ i formatowanie, do wykorzystania w aplikacjach podrzędnych.

W ten sam sposób możesz też przekazywać dokumenty w innych formatach niż PDF, ale Gemini będzie je traktować jako zwykły tekst, co spowoduje utratę kontekstu, np. wykresów czy formatowania.

## Przekazywanie danych PDF w tekście

Dane PDF możesz przekazywać w tekście żądania. Jest to najlepsze rozwiązanie w przypadku mniejszych dokumentów lub przetwarzania tymczasowego, gdy nie musisz odwoływać się do pliku w kolejnych żądaniach. W przypadku większych dokumentów, do których musisz się odwoływać w interakcjach wieloetapowych, zalecamy korzystanie z
[interfejsu Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=pl#large-pdfs)
, aby
skrócić czas oczekiwania na odpowiedź i zmniejszyć zużycie przepustowości.

Z tego przykładu dowiesz się, jak przekazywać dane PDF w tekście:

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/document.pdf', 'rb') as f:
    pdf_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {
            "type": "document",
            "data": base64.b64encode(pdf_bytes).decode('utf-8'),
            "mime_type": "application/pdf"
        },
        {"type": "text", "text": "Summarize this document"}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    const pdfData = fs.readFileSync("path/to/document.pdf", {
        encoding: "base64"
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                data: pdfData,
                mime_type: "application/pdf"
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
PDF_PATH="path/to/document.pdf"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": [
      {
        "type": "document",
        "data": "'$(base64 $B64FLAGS $PDF_PATH)'",
        "mime_type": "application/pdf"
      },
      {"type": "text", "text": "Summarize this document"}
    ]
  }'
```

Możesz też przesłać lokalny plik PDF do przetworzenia:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="file.pdf")

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": uploaded_file.uri, "mime_type": uploaded_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const uploadedFile = await ai.files.upload({
        file: "file.pdf",
        config: { mime_type: "application/pdf" }
    });

    const interaction = await ai.interactions.create({
        model: "gemini-3.6-flash",
        input: [
            { type: "text", text: "Summarize this document" },
            {
                type: "document",
                uri: uploadedFile.uri,
                mime_type: uploadedFile.mime_type
            }
        ]
    });
    console.log(interaction.output_text);
}

main();
```

### REST

```
PDF_PATH="file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME="file.pdf"
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Summarize this document"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

## Przesyłanie plików PDF za pomocą interfejsu Files API

W przypadku większych plików lub gdy chcesz użyć dokumentu w wielu żądaniach, zalecamy korzystanie z interfejsu Files API. Pozwala to skrócić czas oczekiwania na odpowiedź i zmniejszyć zużycie przepustowości, ponieważ przesyłanie plików jest oddzielone od żądań do modelu.

### Duże pliki PDF z adresów URL

Użyj interfejsu File API, aby uprościć przesyłanie i przetwarzanie dużych plików PDF z adresów URL:

### Python

```
from google import genai
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://arxiv.org/pdf/2312.11805"

doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": sample_doc.uri, "mime_type": sample_doc.mime_type},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {

    const pdfBuffer = await fetch("https://arxiv.org/pdf/2312.11805")
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.6-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### REST

```
PDF_PATH="https://arxiv.org/pdf/2312.11805"
DISPLAY_NAME="Gemini_paper"
PROMPT="Summarize this document"

# Download the PDF from the provided URL
wget -O "${DISPLAY_NAME}.pdf" "${PDF_PATH}"

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

echo "MIME_TYPE: ${MIME_TYPE}"
echo "NUM_BYTES: ${NUM_BYTES}"

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${DISPLAY_NAME}.pdf" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Create payload JSON file for safety
cat << EOF > payload.json
{
  "model": "gemini-3.6-flash",
  "input": [
    {"type": "text", "text": "${PROMPT}"},
    {"type": "document", "uri": "${file_uri}", "mime_type": "application/pdf"}
  ]
}
EOF

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm "${DISPLAY_NAME}.pdf"
rm payload.json
```

### Duże pliki PDF przechowywane lokalnie

### Python

```
from google import genai
import pathlib

client = genai.Client()

file_path = pathlib.Path('large_file.pdf')
sample_file = client.files.upload(
    file=file_path,
)

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": sample_file.uri, "mime_type": sample_file.mime_type},
        {"type": "text", "text": "Summarize this document"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
    const file = await ai.files.upload({
        file: 'large_file.pdf',
        config: {
            displayName: 'A17_FlightPlan.pdf',
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    const interaction = await ai.interactions.create({
        model: 'gemini-3.6-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### REST

```
PDF_PATH="large_file.pdf"
NUM_BYTES=$(wc -c < "${PDF_PATH}")
DISPLAY_NAME=TEXT
tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: application/pdf" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${PDF_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now create an interaction using that file
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "model": "gemini-3.6-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Can you add a few more lines to this poem?"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

Możesz sprawdzić, czy interfejs API prawidłowo zapisał przesłany plik, i pobrać jego
metadane, wywołując [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=pl). Unikalne są tylko `name` (a co za tym idzie, `uri`).

### Python

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.pdf')
fpath.write_text('hello')

file = client.files.upload(file='example.pdf')

file_info = client.files.get(name=file.name)
print(file_info.model_dump_json(indent=4))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
    fs.writeFileSync("example.pdf", "hello");

    const file = await ai.files.upload({
        file: "example.pdf",
        config: { mime_type: "application/pdf" }
    });

    const fileInfo = await ai.files.get({ name: file.name });
    console.log(fileInfo);
}

main();
```

### REST

```
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl "https://generativelanguage.googleapis.com/v1beta/$name?key=$GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
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

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {"type": "document", "uri": sample_pdf_1.uri, "mime_type": sample_pdf_1.mime_type},
        {"type": "document", "uri": sample_pdf_2.uri, "mime_type": sample_pdf_2.mime_type},
        {"type": "text", "text": prompt}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function uploadRemotePDF(url, displayName) {
    const pdfBuffer = await fetch(url)
        .then((response) => response.arrayBuffer());

    const fileBlob = new Blob([pdfBuffer], { type: 'application/pdf' });

    const file = await ai.files.upload({
        file: fileBlob,
        config: {
            displayName: displayName,
        },
    });

    let getFile = await ai.files.get({ name: file.name });
    while (getFile.state === 'PROCESSING') {
        getFile = await ai.files.get({ name: file.name });
        console.log(`current file status: ${getFile.state}`);
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    return file;
}

async function main() {
    const file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1");
    const file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2");

    const interaction = await ai.interactions.create({
        model: 'gemini-3.6-flash',
        input: [
            { type: "document", uri: file1.uri, mime_type: file1.mime_type },
            { type: "document", uri: file2.uri, mime_type: file2.mime_type },
            { type: "text", text: "What is the difference between each of the main benchmarks between these two papers? Output these in a table." }
        ],
    });

    console.log(interaction.output_text);
}

main();
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

  echo "Downloading ${display_name} from ${doc_url}..." >&2
  # Download the PDF
  wget -O "${display_name}.pdf" "${doc_url}" 2> /dev/null

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}" >&2
  echo "NUM_BYTES: ${NUM_BYTES}" >&2

  local tmp_header_file="upload-header-${display_name}.tmp"

  # Initial resumable request
  # Using GEMINI_API_KEY instead of GOOGLE_API_KEY
  curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GEMINI_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  echo "Upload URL for ${display_name}: ${upload_url}" >&2

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

  local file_uri=$(jq -r ".file.uri" "file_info_${display_name}.json")
  echo "file_uri for ${display_name}: ${file_uri}" >&2

  # Clean up the downloaded PDF
  rm "${display_name}.pdf"

  echo "${file_uri}"
}

# Upload the first PDF
file_uri_1=$(upload_pdf "${DOC_URL_1}" "${DISPLAY_NAME_1}")

# Upload the second PDF
file_uri_2=$(upload_pdf "${DOC_URL_2}" "${DISPLAY_NAME_2}")

# Create payload JSON file for safety
cat << EOF > payload_multi.json
{
  "model": "gemini-3.6-flash",
  "input": [
    {"type": "document", "uri": "${file_uri_1}", "mime_type": "application/pdf"},
    {"type": "document", "uri": "${file_uri_2}", "mime_type": "application/pdf"},
    {"type": "text", "text": "${PROMPT}"}
  ]
}
EOF

# Now create an interaction using both files
# Using GEMINI_API_KEY instead of GOOGLE_API_KEY
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @payload_multi.json 2> /dev/null > response.json

cat response.json
echo

jq ".steps[-1].content[0].text" response.json

# Clean up
rm payload_multi.json
rm "file_info_${DISPLAY_NAME_1}.json"
rm "file_info_${DISPLAY_NAME_2}.json"
```

## Szczegóły techniczne

Gemini obsługuje pliki PDF o rozmiarze do 50 MB lub 1000 stron. Ten limit dotyczy zarówno danych w tekście, jak i przesyłania za pomocą interfejsu Files API. Każda strona dokumentu odpowiada 258 tokenom.

Oprócz
okna [kontekstu](https://ai.google.dev/gemini-api/docs/long-context?hl=pl) modelu nie ma konkretnych limitów liczby pikseli w dokumencie. Większe strony są
zmniejszane do maksymalnej rozdzielczości 3072 x 3072 pikseli przy zachowaniu oryginalnych
proporcji, a mniejsze strony są powiększane do 768 x 768 pikseli. Nie ma obniżki kosztów w przypadku stron o mniejszym rozmiarze (oprócz przepustowości) ani wzrostu wydajności w przypadku stron o wyższej rozdzielczości.

### Modele Gemini 3

W Gemini 3 wprowadzono szczegółową kontrolę nad przetwarzaniem multimodalnym za pomocą parametru `media_resolution`. Teraz możesz ustawić rozdzielczość na niską, średnią lub wysoką dla każdej części multimedialnej. W związku z tym zaktualizowano przetwarzanie dokumentów PDF:

1. **Natywne uwzględnianie tekstu:** tekst natywnie osadzony w pliku PDF jest wyodrębniany i przekazywany do modelu.
2. **Rozliczenia i raportowanie tokenów:**
   - **Nie naliczamy opłat** za tokeny pochodzące z wyodrębnionego **tekstu natywnego** w plikach PDF.
   - W sekcji `usage_metadata` odpowiedzi interfejsu API tokeny wygenerowane na podstawie przetwarzania stron PDF (jako obrazów) są teraz zliczane w ramach modalności `IMAGE`, a nie w osobnej modalności `DOCUMENT`, jak w niektórych wcześniejszych wersjach.

Więcej informacji o parametrze rozdzielczości multimediów znajdziesz w
[przewodniku po rozdzielczości multimediów](https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=pl).

### Typy dokumentów

Technicznie możesz przekazywać inne typy MIME do rozpoznawania dokumentów, takie jak TXT, Markdown, HTML, XML itp. Jednak rozpoznawanie dokumentów ***rozumie tylko pliki PDF***. Inne typy będą wyodrębniane jako czysty tekst, a model nie będzie w stanie zinterpretować tego, co widzimy w renderowaniu tych plików. Utracone zostaną wszelkie szczegóły dotyczące typu pliku, takie jak wykresy, diagramy, tagi HTML, formatowanie Markdown itp.

Więcej informacji o innych metodach wprowadzania plików znajdziesz w
[przewodniku po metodach wprowadzania plików](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=pl).

### Sprawdzone metody

Aby uzyskać najlepsze wyniki:

- Przed przesłaniem obróć strony do prawidłowej orientacji.
- Unikaj rozmazanych stron.
- Jeśli używasz jednej strony, umieść prompta tekstowego za stroną.

## Co dalej?

Więcej informacji znajdziesz w tych materiałach:

- [Strategie tworzenia promptów z plików](https://ai.google.dev/gemini-api/docs/files?hl=pl#prompt-guide): interfejs Gemini API obsługuje tworzenie promptów za pomocą danych tekstowych, graficznych, dźwiękowych i wideo, czyli tworzenie promptów multimodalnych.
- [Instrukcje systemowe](https://ai.google.dev/gemini-api/docs/text-generation?hl=pl#system-instructions):
  Instrukcje systemowe pozwalają sterować zachowaniem modelu na podstawie konkretnych potrzeb i przypadków użycia.

Prześlij opinię

O ile nie stwierdzono inaczej, treść tej strony jest objęta [licencją Creative Commons – uznanie autorstwa 4.0](https://creativecommons.org/licenses/by/4.0/), a fragmenty kodu są dostępne na [licencji Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Szczegółowe informacje na ten temat zawierają [zasady dotyczące witryny Google Developers](https://developers.google.com/site-policies?hl=pl). Java jest zastrzeżonym znakiem towarowym firmy Oracle i jej podmiotów stowarzyszonych.

Ostatnia aktualizacja: 2026-07-30 UTC.

Chcesz przekazać coś jeszcze?

[[["Łatwo zrozumieć","easyToUnderstand","thumb-up"],["Rozwiązało to mój problem","solvedMyProblem","thumb-up"],["Inne","otherUp","thumb-up"]],[["Brak potrzebnych mi informacji","missingTheInformationINeed","thumb-down"],["Zbyt skomplikowane / zbyt wiele czynności do wykonania","tooComplicatedTooManySteps","thumb-down"],["Nieaktualne treści","outOfDate","thumb-down"],["Problem z tłumaczeniem","translationIssue","thumb-down"],["Problem z przykładami/kodem","samplesCodeIssue","thumb-down"],["Inne","otherDown","thumb-down"]],["Ostatnia aktualizacja: 2026-07-30 UTC."],[],[]]
