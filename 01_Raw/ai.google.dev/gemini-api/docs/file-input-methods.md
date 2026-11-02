---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419
fetched_at: 2026-11-02T07:31:36.410584+00:00
title: "M\u00e9todos de entrada de archivos \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon ya está disponible. [Pruébalo](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=es-419).

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google utiliza tecnología de IA para traducir contenido a tu idioma preferido. Las traducciones realizadas con IA pueden contener errores.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Métodos de entrada de archivos

En esta guía, se explican las diferentes formas en que puedes incluir archivos multimedia, como imágenes, audio, video y documentos, cuando realizas solicitudes a la API de Gemini.
Los nuevos métodos son compatibles con todos los extremos de la API de Gemini, incluidas las APIs de Batch, Interactions y Live.
Elegir el método adecuado depende del tamaño del archivo, dónde se almacenan tus datos y con qué frecuencia planeas usar el archivo.

La forma más sencilla de incluir un archivo como entrada es leer un archivo local e incluirlo en una instrucción. En el siguiente ejemplo, se muestra cómo leer un archivo PDF local. Los archivos PDF tienen un límite de 50 MB para este método. Consulta la [tabla de comparación de métodos de entrada](#method-comparison) para obtener una lista completa de los tipos y límites de entrada de archivos.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from 'node:fs';

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = 'my_local_file.pdf';

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
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

byte[] pdfBytes = Files.readAllBytes(Paths.get("my_local_file.pdf"));
String base64Pdf = Base64.getEncoder().encodeToString(pdfBytes);

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

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

    pdfBytes, err := os.ReadFile("my_local_file.pdf")
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(pdfBytes)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
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
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Summarize this document"},
      {
        "type": "document",
        "data": "'${B64_CONTENT}'",
        "mime_type": "application/pdf"
      }
    ]
  }'
```

## Comparación de métodos de entrada

En la siguiente tabla, se compara cada método de entrada con los límites de archivos y los casos de uso más adecuados. Ten en cuenta que el límite de tamaño del archivo puede variar según el tipo de archivo y el modelo o el tokenizador que se usen para procesarlo.

| Método | Ideal para | Tamaño máximo de los archivos | Persistencia |
| --- | --- | --- | --- |
| **Datos intercalados** | Pruebas rápidas, archivos pequeños y aplicaciones en tiempo real | 100 MB por solicitud o carga útil   (**50 MB para archivos PDF**) | Ninguna (se envía con cada solicitud) |
| **Subida de archivos a la API** | Archivos grandes y archivos que se usan varias veces | 2 GB por archivo,   hasta 20 GB por proyecto | 48 horas |
| **Registro del URI de GCS de la API de File** | Archivos grandes que ya están en Google Cloud Storage y archivos que se usan varias veces | 2 GB por archivo, sin límites de almacenamiento generales | Ninguno (se recupera por solicitud). El registro único puede brindar acceso por hasta 30 días. |
| **URLs externas** | Datos públicos o datos en buckets de la nube (AWS, Azure, GCS) sin volver a subirlos | 15 MB por archivo | Ninguno (se recupera por solicitud) |

## Datos intercalados

En el caso de archivos más pequeños (menos de 100 MB o 50 MB para archivos PDF), puedes pasar los datos directamente en la carga útil de la solicitud. Este es el método más simple para pruebas rápidas o aplicaciones que manejan datos transitorios en tiempo real. Puedes proporcionar datos como cadenas codificadas en base64 o leyendo archivos locales directamente.

Para ver un ejemplo de lectura desde un archivo local, consulta el ejemplo que se encuentra al principio de esta página.

### Recuperar desde una URL

También puedes recuperar un archivo desde una URL, convertirlo en bytes y agregarlo a la entrada.

### Python

```
from google import genai
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl)
      .then((response) => response.arrayBuffer());

    const interaction = await client.interactions.create({
        model: "gemini-3.8-flash",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
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
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.Base64;
import java.util.List;

Client client = new Client();

String docUrl = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf";
HttpClient httpClient = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(docUrl)).build();
byte[] docData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
String base64Pdf = Base64.getEncoder().encodeToString(docData);

String prompt = "Summarize this document";

Content docContent =
    DocumentContent.builder()
        .data(base64Pdf)
        .mimeType(DocumentContentMimeType.APPLICATION_PDF)
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
    "context"
    "encoding/base64"
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

    docURL := "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
    resp, err := http.Get(docURL)
    if err != nil {
        log.Fatal(err)
    }
    defer resp.Body.Close()
    docData, err := io.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
    base64Pdf := base64.StdEncoding.EncodeToString(docData)

    prompt := "Summarize this document"

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.DocumentContent{
                    Data:     genai.Ptr(base64Pdf),
                    MimeType: interactions.DocumentContentMimeTypeApplicationPdf.ToPointer(),
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
DOC_URL="https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
PROMPT="Summarize this document"
DISPLAY_NAME="base64_pdf"

# Download the PDF
wget -O "${DISPLAY_NAME}.pdf" "${DOC_URL}"

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3.8-flash",
"input": [
{"type": "document", "data": "${ENCODED_PDF}", "mime_type": "application/pdf"},
{"type": "text", "text": "${PROMPT}"}
]
}
EOF

# Generate content using interactions
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d @payload.json 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## API de Gemini File

La API de File está diseñada para archivos más grandes (hasta 2 GB) o archivos que planeas usar en varias solicitudes.

### Carga de archivos estándar

Sube un archivo local a la API de Gemini. Los archivos que se suben de esta manera se almacenan temporalmente (48 horas) y se procesan para que el modelo los recupere de manera eficiente.

### Python

```
from google import genai

client = genai.Client()

doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
  const filePath = "path/to/your/sample.pdf";

  const myfile = await client.files.upload({
    file: filePath,
    config: { mime_type: "application/pdf" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
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

File docFile =
    client.files.upload(
        new java.io.File("path/to/your/sample.pdf"),
        UploadFileConfig.builder().mimeType("application/pdf").build());

String prompt = "Summarize this document";

Content textContent = TextContent.builder().text(prompt).build();
Content docContent =
    DocumentContent.builder()
        .uri(docFile.uri().orElse(""))
        .mimeType(DocumentContentMimeType.of(docFile.mimeType().orElse("application/pdf")))
        .build();

List<Content> contents = Arrays.asList(textContent, docContent);

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

    docFile, err := client.Files.UploadFromPath(ctx, "path/to/your/sample.pdf", &genai.UploadFileConfig{
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
                interactions.NewContent(interactions.TextContent{
                    Text: prompt,
                }),
                interactions.NewContent(interactions.DocumentContent{
                    URI:      genai.Ptr(docFile.URI),
                    MimeType: interactions.DocumentContentMimeType(docFile.MIMEType).ToPointer(),
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
FILE_PATH="path/to/sample.pdf"
MIME_TYPE=$(file -b --mime-type "${FILE_PATH}")
NUM_BYTES=$(wc -c < "${FILE_PATH}")
DISPLAY_NAME=DOCUMENT

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -D "${tmp_header_file}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
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
  --data-binary "@${FILE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)

# Now use in an interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.8-flash",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Registra archivos de Google Cloud Storage

Si tus datos ya están en Google Cloud Storage, no es necesario que los descargues y vuelvas a subirlos. Puedes registrarlo directamente con la API de File.

1. Otorga acceso de **agente de servicio** a cada bucket.

   1. Habilita la API de Gemini en tu proyecto de Google Cloud.
   2. Crea el agente de servicio:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Otorga permisos al agente de servicio de la API de Gemini** para leer tus buckets de almacenamiento.

      El usuario debe asignar el [rol de IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=es-419#storage.objectViewer) `Storage Object Viewer` a este agente de servicio en los buckets de almacenamiento específicos que pretende usar.

   Este acceso no vence de forma predeterminada, pero se puede cambiar en cualquier momento. También puedes usar los comandos del [SDK de IAM de Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=es-419) para otorgar permisos.
2. Autentica tu servicio

   **Requisitos previos**

   - Habilitar la API
   - Crea una cuenta de servicio o un agente con los permisos adecuados.

   Primero, debes autenticarte como el servicio que tiene permisos de visualizador de objetos de almacenamiento. La forma en que esto sucede depende del entorno en el que se ejecutará tu código de administración de archivos.

   **Fuera de Google Cloud**

   Si tu código se ejecuta fuera de Google Cloud, por ejemplo, desde tu computadora de escritorio, descarga las credenciales de la cuenta desde la consola de Google Cloud siguiendo estos pasos:

   1. Navega a la [consola de cuentas de servicio](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=es-419).
   2. Selecciona la cuenta de servicio pertinente.
   3. Selecciona la pestaña **Claves** y elige **Agregar clave, Crear clave nueva**.
   4. Elige el tipo de clave **JSON** y observa dónde se descargó el archivo en tu máquina.

   Para obtener más detalles, consulta la documentación oficial de Google Cloud sobre la [administración de claves de cuentas de servicio](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=es-419).

   Luego, usa los siguientes comandos para autenticarte. En estos comandos, se supone que el archivo de tu cuenta de servicio se encuentra en el directorio actual y se llama `service-account.json`.

   ### Python

   ```
   from google.oauth2.service_account import Credentials

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   SERVICE_ACCOUNT_FILE = 'service-account.json'

   credentials = Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE,
       scopes=GCS_READ_SCOPES
   )
   ```

   ### JavaScript

   ```
   const { GoogleAuth } = require('google-auth-library');

   const GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ];

   const SERVICE_ACCOUNT_FILE = 'service-account.json';

   const auth = new GoogleAuth({
     keyFile: SERVICE_ACCOUNT_FILE,
     scopes: GCS_READ_SCOPES
   });
   ```

   ### CLI

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **En Google Cloud**

   Si ejecutas directamente en Google Cloud, por ejemplo, con [Cloud Run functions](https://cloud.google.com/functions?hl=es-419) o una [instancia de Compute Engine](https://cloud.google.com/products/compute?hl=es-419), tendrás credenciales implícitas, pero deberás volver a autenticarte para otorgar los permisos adecuados.

   ### Python

   Este código espera que el servicio se ejecute en un entorno en el que se puedan obtener automáticamente las [credenciales predeterminadas de la aplicación](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=es-419), como Cloud Run o Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Este código espera que el servicio se ejecute en un entorno en el que se puedan obtener automáticamente las [credenciales predeterminadas de la aplicación](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=es-419), como Cloud Run o Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.List;

List<String> gcsReadScopes =
    Arrays.asList(
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/cloud-platform");

String serviceAccountFile = "service-account.json";

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream(serviceAccountFile))
        .createScoped(gcsReadScopes);
```

### Go

```
package main

import (
    "log"

    "google.golang.org/genai"
)

func main() {
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    _ = cc.Credentials
}
```

### CLI

Este es un comando interactivo. En el caso de servicios como Compute Engine, puedes adjuntar alcances al servicio en ejecución a nivel de la configuración. Consulta la [documentación del servicio administrado por el usuario](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=es-419#using) para ver un ejemplo.

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. Registro de archivos (API de Files)
   Usa la API de Files para registrar archivos y generar una ruta de acceso a la API de Files que se pueda usar directamente en la API de Gemini.

   ### Python

   ```
   from google import genai

   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3.8-flash",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     print(interaction.output_text)
   ```

   ### JavaScript

   ```
   import { GoogleGenAI } from "@google/genai";

   const ai = new GoogleGenAI({ auth: auth });

   async function main() {
       const registeredGcsFiles = await ai.files.registerFiles({
           uris: ["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
       });

       const prompt = "Summarize this file.";

       for (const file of registeredGcsFiles.files) {
           console.log(file.name);
           const interaction = await ai.interactions.create({
               model: "gemini-3.8-flash",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           console.log(interaction.output_text);
       }
   }

   main();
   ```

### Java

```
import com.google.auth.oauth2.GoogleCredentials;
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
import com.google.genai.types.RegisterFilesResponse;
import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

GoogleCredentials credentials =
    GoogleCredentials.fromStream(new FileInputStream("service-account.json"))
        .createScoped(
            Arrays.asList(
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/cloud-platform"));

Client client = Client.builder().credentials(credentials).build();

RegisterFilesResponse registeredGcsFiles =
    client.files.registerFiles(
        credentials,
        Arrays.asList("gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"),
        null);

String prompt = "Summarize this file.";

for (File f : registeredGcsFiles.files().orElse(Collections.emptyList())) {
  System.out.println(f.name().orElse(""));

  Content textContent = TextContent.builder().text(prompt).build();
  Content docContent =
      DocumentContent.builder()
          .uri(f.uri().orElse(""))
          .mimeType(DocumentContentMimeType.of(f.mimeType().orElse("application/pdf")))
          .build();

  CreateModelInteraction params =
      CreateModelInteraction.builder()
          .model(Model.of("gemini-3.8-flash"))
          .input(InteractionsInput.ofContent(Arrays.asList(textContent, docContent)))
          .build();

  Interaction interaction =
      client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();
  System.out.println(interaction.outputText().orElse(""));
}
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
    cc := &genai.ClientConfig{}
    if err := cc.UseDefaultCredentials(); err != nil {
        log.Fatal(err)
    }
    client, err := genai.NewClient(ctx, cc)
    if err != nil {
        log.Fatal(err)
    }

    registeredGcsFiles, err := client.Files.RegisterFiles(
        ctx,
        []string{"gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"},
        cc.Credentials,
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }

    prompt := "Summarize this file."

    for _, f := range registeredGcsFiles.Files {
        fmt.Println(f.Name)
        res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
            Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
                Model: interactions.Model("gemini-3.8-flash"),
                Input: interactions.NewInteractionsInput([]interactions.Content{
                    interactions.NewContent(interactions.TextContent{
                        Text: prompt,
                    }),
                    interactions.NewContent(interactions.DocumentContent{
                        URI:      genai.Ptr(f.URI),
                        MimeType: interactions.DocumentContentMimeType(f.MIMEType).ToPointer(),
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
}
```

### CLI

```
access_token=$(gcloud auth application-default print-access-token)
project_id=$(gcloud config get-value project)
curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" \
    -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
```

## URLs externas HTTP o firmadas

Puedes pasar URLs HTTPS de acceso público o URLs previamente firmadas directamente en tu solicitud. La API de Gemini recuperará el contenido de forma segura durante el procesamiento.
Esto es ideal para los archivos que no quieres volver a subir. Cada archivo puede tener hasta 15 MB. Para archivos más grandes, usa la [API de File](#file-api).

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3.8-flash',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  console.log(interaction.output_text);
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3.8-flash",
          "input": [
            {"type": "text", "text": "Summarize this pdf"},
            {
              "type": "document",
              "uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf",
              "mime_type": "application/pdf"
            }
          ]
        }'
```

### Accesibilidad

Verifica que las URLs que proporciones no dirijan a páginas que requieran acceso o estén detrás de un muro de pago. En el caso de las bases de datos privadas, asegúrate de crear una URL firmada con los permisos de acceso y la fecha de vencimiento correctos.

### Controles de seguridad

El sistema realiza una verificación de moderación de contenido en la URL para confirmar que cumple con los estándares de seguridad y políticas. Si la URL no pasa esta verificación, recibirás un `url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipos de contenido admitidos

Esta lista de tipos de archivos admitidos y limitaciones se proporciona como guía inicial y no es exhaustiva. El conjunto efectivo de tipos admitidos está sujeto a cambios y puede variar según el modelo específico y la versión del tokenizador en uso. Los tipos no admitidos generarán un error.
Además, la recuperación de contenido para estos tipos de archivos solo admite URLs de acceso público.

#### Tipos de archivos de texto

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipos de archivos de la aplicación

- `application/json`
- `application/pdf`

#### Tipos de archivo de imagen

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Tipos de archivo de video

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Prácticas recomendadas

- **Elige el método adecuado:** Usa datos intercalados para archivos pequeños y transitorios.
  Usa la API de File para los archivos más grandes o que se usan con frecuencia. Usa URLs externas para los datos que ya están alojados en línea.
- **Especifica los tipos de MIME:** Siempre proporciona el tipo de MIME correcto para los datos del archivo para garantizar el procesamiento adecuado.
- **Maneja los errores:** Implementa el manejo de errores en tu código para administrar posibles problemas, como fallas de red, problemas de acceso a archivos o errores de API.

## Limitaciones

- Los límites de tamaño de los archivos varían según el método (consulta la [tabla de comparación](#method-comparison)) y el tipo de archivo.
- Los datos intercalados aumentan el tamaño de la carga útil de la solicitud.
- Las cargas de la API de File son temporales y vencen después de 48 horas.
- La recuperación de URLs externas se limita a 15 MB por archivo y admite tipos de contenido específicos.

## ¿Qué sigue?

- Intenta escribir tus propias instrucciones multimodales con [Google AI Studio](http://aistudio.google.com/?hl=es-419).
- Para obtener información sobre cómo incluir archivos en tus instrucciones, consulta las guías de [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=es-419), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419) y [Procesamiento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-10-07 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-10-07 (UTC)"],[],[]]
