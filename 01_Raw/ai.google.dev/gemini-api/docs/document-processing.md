---
source_url: https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419
fetched_at: 2026-10-05T06:40:56.385671+00:00
title: "Comprensi\u00f3n de documentos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 3.8 Flash ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Comprensión de documentos

Los modelos de Gemini pueden procesar documentos en formato PDF y usar la visión nativa para comprender el contexto de documentos completos. Esto va más allá de la extracción de texto, ya que le permite a Gemini hacer lo siguiente:

- Analiza e interpreta contenido, como texto, imágenes, diagramas, gráficos y tablas, incluso en documentos largos de hasta 1, 000 páginas.
- Extrae información en formatos de [salida estructurada](https://ai.google.dev/gemini-api/docs/structured-output?hl=es-419).
- Resumir y responder preguntas basadas en los elementos visuales y textuales de un documento
- Transcribir el contenido de documentos (p. ej., a HTML), conservando los diseños y el formato, para su uso en aplicaciones posteriores

También puedes pasar documentos que no sean PDF de la misma manera, pero Gemini los verá como texto normal, lo que eliminará el contexto, como gráficos o formato.

## Cómo pasar datos de PDF intercalados

Puedes pasar los datos del PDF de forma intercalada en la solicitud. Este método es más adecuado para documentos más pequeños o para el procesamiento temporal en el que no necesitas hacer referencia al archivo en solicitudes posteriores. Te recomendamos que uses la [API de Files](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419#large-pdfs) para los documentos más grandes a los que debas hacer referencia en interacciones de varios turnos para mejorar la latencia de las solicitudes y reducir el uso de ancho de banda.

En el siguiente ejemplo, se muestra cómo pasar datos de PDF de forma intercalada:

### Python

```
from google import genai
import base64

client = genai.Client()

with open('path/to/document.pdf', 'rb') as f:
    pdf_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

byte[] pdfBytes = Files.readAllBytes(Paths.get("path/to/document.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "encoding/base64"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    pdfBytes, err := os.ReadFile("path/to/document.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
    "model": "gemini-3.8-flash",
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

También puedes subir un archivo PDF local para su procesamiento:

### Python

```
from google import genai

client = genai.Client()

uploaded_file = client.files.upload(file="file.pdf")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
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
        model: "gemini-3.8-flash",
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File uploadedFile =
    client.files.upload(
        new java.io.File("file.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

Content docContent =
    DocumentContent.builder()
        .uri(uploadedFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(uploadedFile.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    uploadedFile, err := client.Files.UploadFromPath(ctx, "file.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(uploadedFile.URI),
                    MimeType: interactions.DocumentContentMimeType(uploadedFile.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Summarize this document"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

## Cómo subir archivos PDF con la API de Files

Te recomendamos que uses la API de Files para archivos más grandes o cuando quieras reutilizar un documento en varias solicitudes. Esto mejora la latencia de las solicitudes y reduce el uso de ancho de banda, ya que desacopla la carga de archivos de las solicitudes del modelo.

### Archivos PDF grandes desde URLs

Usa la API de File para simplificar la carga y el procesamiento de archivos PDF grandes desde URLs:

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
    model="gemini-3.8-flash",
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
        model: 'gemini-3.8-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

String longContextPdfPath = "https://arxiv.org/pdf/2312.11805";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(longContextPdfPath)).build();
byte[] pdfBytes = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();

File sampleDoc =
    client.files.upload(
        pdfBytes, UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .uri(sampleDoc.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(sampleDoc.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "bytes"
    "context"
    "fmt"
    "io"
    "log"
    "net/http"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    longContextPdfPath := "https://arxiv.org/pdf/2312.11805"
    resp, err := http.Get(longContextPdfPath)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    pdfBytes, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }

    sampleDoc, err := client.Files.Upload(ctx, bytes.NewReader(pdfBytes), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(sampleDoc.URI),
                    MimeType: interactions.DocumentContentMimeType(sampleDoc.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
  "model": "gemini-3.8-flash",
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

### PDFs grandes almacenados de forma local

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
    model="gemini-3.8-flash",
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
        model: 'gemini-3.8-flash',
        input: [
            { type: "document", uri: file.uri, mime_type: file.mime_type },
            { type: "text", text: "Summarize this document" }
        ],
    });

    console.log(interaction.output_text);

}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

File sampleFile =
    client.files.upload(
        new java.io.File("large_file.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

Content docContent =
    DocumentContent.builder()
        .uri(sampleFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(sampleFile.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text("Summarize this document").build();

List<Content> contents = Arrays.asList(docContent, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    sampleFile, err := client.Files.UploadFromPath(ctx, "large_file.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(sampleFile.URI),
                    MimeType: interactions.DocumentContentMimeType(sampleFile.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: "Summarize this document",
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
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
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "document", "uri": "'$file_uri'", "mime_type": "application/pdf"},
        {"type": "text", "text": "Can you add a few more lines to this poem?"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq -r ".steps[-1].content[0].text" response.json
```

Puedes verificar que la API haya almacenado correctamente el archivo subido y obtener sus metadatos llamando a [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=es-419). Solo el `name` (y, por extensión, el `uri`) son únicos.

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

### Java

```
import com.google.genai.Client;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

Client client = new Client();

Path fpath = Paths.get("example.pdf");
Files.write(fpath, "hello".getBytes(StandardCharsets.UTF_8));

File file =
    client.files.upload(
        fpath.toFile(), UploadFileConfig.builder().mimeType("application/pdf").build());

File fileInfo = client.files.get(file.name().orElse(""), null);
System.out.println(fileInfo.toJson());
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    if err := os.WriteFile("example.pdf", []byte("hello"), 0644); err != nil {
        log.Fatal(err)
    }

    file, err := client.Files.UploadFromPath(ctx, "example.pdf", &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    fileInfo, err := client.Files.Get(ctx, file.Name, nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(fileInfo)
}
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

## Cómo pasar varios PDFs

La API de Gemini puede procesar varios documentos PDF (hasta 1,000 páginas) en una sola solicitud, siempre que el tamaño combinado de los documentos y la instrucción de texto permanezcan dentro de la ventana de contexto del modelo.

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
    model="gemini-3.8-flash",
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
        model: 'gemini-3.8-flash',
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

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.DocumentContent;
import com.google.genai.gaos.models.interactions.DocumentContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import com.google.genai.types.File;
import com.google.genai.types.UploadFileConfig;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

String docUrl1 = "https://arxiv.org/pdf/2312.11805";
String docUrl2 = "https://arxiv.org/pdf/2403.05530";

HttpClient httpClient = HttpClient.newHttpClient();
byte[] docData1 =
    httpClient
        .send(HttpRequest.newBuilder().uri(URI.create(docUrl1)).build(), HttpResponse.BodyHandlers.ofByteArray())
        .body();
byte[] docData2 =
    httpClient
        .send(HttpRequest.newBuilder().uri(URI.create(docUrl2)).build(), HttpResponse.BodyHandlers.ofByteArray())
        .body();

File samplePdf1 =
    client.files.upload(
        docData1, UploadFileConfig.builder().mimeType("application/pdf").build());
File samplePdf2 =
    client.files.upload(
        docData2, UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt =
    "What is the difference between each of the main benchmarks between these two papers? Output these in a table.";

Content doc1Content =
    DocumentContent.builder()
        .uri(samplePdf1.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(samplePdf1.mimeType().orElse("application/pdf")))
        .build();
Content doc2Content =
    DocumentContent.builder()
        .uri(samplePdf2.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(samplePdf2.mimeType().orElse("application/pdf")))
        .build();
Content textContent = TextContent.builder().text(prompt).build();

List<Content> contents = Arrays.asList(doc1Content, doc2Content, textContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "bytes"
    "context"
    "fmt"
    "io"
    "log"
    "net/http"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    docURL1 := "https://arxiv.org/pdf/2312.11805"
    docURL2 := "https://arxiv.org/pdf/2403.05530"

    resp1, err := http.Get(docURL1)
    if err != nil {
        log.Fatal(err)
    }
    defer resp1.Body.Close()
    docData1, err := io.ReadAll(resp1.Body)
    if err != nil {
        log.Fatal(err)
    }

    resp2, err := http.Get(docURL2)
    if err != nil {
        log.Fatal(err)
    }
    defer resp2.Body.Close()
    docData2, err := io.ReadAll(resp2.Body)
    if err != nil {
        log.Fatal(err)
    }

    samplePdf1, err := client.Files.Upload(ctx, bytes.NewReader(docData1), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }
    samplePdf2, err := client.Files.Upload(ctx, bytes.NewReader(docData2), &genai.UploadFileConfig{
        MIMEType: "application/pdf",
    })
    if err != nil {
        log.Fatal(err)
    }

    prompt := "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(samplePdf1.URI),
                    MimeType: interactions.DocumentContentMimeType(samplePdf1.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(samplePdf2.URI),
                    MimeType: interactions.DocumentContentMimeType(samplePdf2.MIMEType).ToPointer(),
                }),
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
            }),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
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
  "model": "gemini-3.8-flash",
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

## Detalles técnicos

Gemini admite archivos PDF de hasta 50 MB o 1,000 páginas. Este límite se aplica tanto a los datos intercalados como a las cargas de la API de Files. Cada página del documento equivale a 258 tokens.

Si bien no hay límites específicos para la cantidad de píxeles en un documento, además de la [ventana de contexto](https://ai.google.dev/gemini-api/docs/long-context?hl=es-419) del modelo, las páginas más grandes se reducen a una resolución máxima de 3,072 x 3,072, a la vez que conservan su relación de aspecto original, mientras que las páginas más pequeñas se amplían a 768 x 768 píxeles. No hay reducción de costos para las páginas de tamaños más pequeños, aparte del ancho de banda, ni mejora del rendimiento para las páginas de mayor resolución.

### Modelos de Gemini 3

Gemini 3 introduce un control detallado sobre el procesamiento de la visión multimodal con el parámetro `media_resolution`. Ahora puedes establecer la resolución en baja, media o alta para cada parte de contenido multimedia individual. Con esta incorporación, se actualizó el procesamiento de documentos PDF de la siguiente manera:

1. **Inclusión de texto nativo:** Se extrae el texto incorporado de forma nativa en el PDF y se proporciona al modelo.
2. **Informes de facturación y tokens:**
   - **No se te cobra** por los tokens que se originan en el **texto nativo** extraído de los PDFs.
   - En la sección `usage_metadata` de la respuesta de la API, los tokens generados a partir del procesamiento de páginas en formato PDF (como imágenes) ahora se contabilizan en la modalidad `IMAGE`, no en una modalidad `DOCUMENT` separada como en algunas versiones anteriores.

Para obtener más detalles sobre el parámetro de resolución de medios, consulta la guía de [resolución de medios](https://ai.google.dev/gemini-api/docs/interactions/media-resolution?hl=es-419).

### Tipos de documentos

Técnicamente, puedes pasar otros tipos de MIME para la comprensión de documentos, como TXT, Markdown, HTML, XML, etcétera. Sin embargo, la visión de documentos ***solo comprende los PDFs de manera significativa***. Otros tipos se extraerán como texto puro, y el modelo no podrá interpretar lo que vemos en la renderización de esos archivos. Se perderán las especificaciones de tipo de archivo, como gráficos, diagramas, etiquetas HTML, formato Markdown, etcétera.

Para obtener información sobre otros métodos de entrada de archivos, consulta la guía [Métodos de entrada de archivos](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419).

### Prácticas recomendadas

Para lograr resultados óptimos, haz lo siguiente:

- Rota las páginas a la orientación correcta antes de subirlas.
- Evita las páginas borrosas.
- Si usas una sola página, coloca la instrucción de texto después de la página.

## ¿Qué sigue?

Para obtener más información, consulta los siguientes recursos:

- [Estrategias de instrucciones con archivos](https://ai.google.dev/gemini-api/docs/files?hl=es-419#prompt-guide): La API de Gemini admite instrucciones con datos de texto, imagen, audio y video, lo que también se conoce como instrucciones multimodales.
- [Instrucciones del sistema](https://ai.google.dev/gemini-api/docs/text-generation?hl=es-419#system-instructions):
  Las instrucciones del sistema te permiten dirigir el comportamiento del modelo según tus necesidades y casos de uso específicos.

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-09-24 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-09-24 (UTC)"],[],[]]
