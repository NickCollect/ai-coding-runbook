---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=es-419
fetched_at: 2026-06-15T06:22:34.669638+00:00
title: "Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=es-419) ya está disponible en versión preliminar con planificación colaborativa, visualización, compatibilidad con MCP y mucho más.

![](https://ai.google.dev/_static/images/translated.svg?hl=es-419)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página principal](https://ai.google.dev/?hl=es-419)
- [Gemini API](https://ai.google.dev/gemini-api?hl=es-419)
- [generateContent API](https://ai.google.dev/gemini-api/docs/generate-content?hl=es-419)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=es-419)

Enviar comentarios

# Métodos de entrada de archivos

En esta guía, se explican las diferentes formas en que puedes incluir archivos multimedia, como imágenes, audio, video y documentos, cuando realizas solicitudes a la API de Gemini.
Los nuevos métodos son compatibles con todos los extremos de la API de Gemini, incluidas las APIs de Batch, Interactions y Live.
Elegir el método correcto depende del tamaño del archivo, dónde se almacenan tus datos actualmente y con qué frecuencia planeas usar el archivo.

La forma más sencilla de incluir un archivo como entrada es leer un archivo local e incluirlo en una instrucción. En el siguiente ejemplo, se muestra cómo leer un archivo PDF local. Los archivos PDF están limitados a 50 MB para este método. Consulta la [tabla de comparación de métodos de entrada](#method-comparison) para obtener una lista completa de los tipos y límites de entrada de archivos.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
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
import * as fs from 'node:fs';

const ai = new GoogleGenAI({});
const prompt = "Summarize this document";

async function main() {
    const filePath = path.join('content', 'my_local_file.pdf'); // Adjust path as needed

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: fs.readFileSync(filePath).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "Summarize this document"}
        ]
      },
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "application/pdf",
              "data": "'"${B64_CONTENT}"'"
            }
          }
        ]
      }
    ]
  }'
```

## Comparación de métodos de entrada

En la siguiente tabla, se compara cada método de entrada con los límites de archivos y los mejores casos de uso. Ten en cuenta que el límite de tamaño del archivo puede variar según el tipo de archivo y el modelo o el tokenizador que se usen para procesarlo.

| Método | Ideal para | Tamaño máximo de los archivos | Persistencia |
| --- | --- | --- | --- |
| **Datos intercalados** | Pruebas rápidas, archivos pequeños y aplicaciones en tiempo real | 100 MB por solicitud o carga útil   (**50 MB para PDFs**) | Ninguna (se envía con cada solicitud) |
| **Subida de archivos a la API** | Archivos grandes y archivos que se usan varias veces | 2 GB por archivo,   hasta 20 GB por proyecto | 48 horas |
| **Registro del URI de GCS de la API de File** | Archivos grandes que ya están en Google Cloud Storage y archivos que se usan varias veces | 2 GB por archivo, sin límites de almacenamiento generales | Ninguno (se recupera por solicitud). El registro único puede brindar acceso por hasta 30 días. |
| **URLs externas** | Datos públicos o datos en buckets de la nube (AWS, Azure, GCS) sin volver a subirlos | 100 MB por solicitud o carga útil | Ninguno (se recupera por solicitud) |

## Datos intercalados

En el caso de archivos más pequeños (menos de 100 MB o 50 MB para archivos PDF), puedes pasar los datos directamente en la carga útil de la solicitud. Este es el método más simple para pruebas rápidas o aplicaciones que manejan datos transitorios en tiempo real. Puedes proporcionar datos como cadenas codificadas en base64 o leer archivos locales directamente.

Para ver un ejemplo de lectura desde un archivo local, consulta el ejemplo al comienzo de esta página.

### Recuperar desde una URL

También puedes recuperar un archivo de una URL, convertirlo en bytes y agregarlo a la entrada.

### Python

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-3.5-flash",
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

const ai = new GoogleGenAI({});
const docUrl = 'https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf';
const prompt = "Summarize this document";

async function main() {
    const pdfResp = await fetch(docUrl);
      .then((response) => response.arrayBuffer());

    const contents = [
        { text: prompt },
        {
            inlineData: {
                mimeType: 'application/pdf',
                data: Buffer.from(pdfResp).toString("base64")
            }
        }
    ];

    const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
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

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"inline_data": {"mime_type": "application/pdf", "data": "'"$ENCODED_PDF"'"}},
          {"text": "'$PROMPT'"}
        ]
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## API de Gemini File

La API de File está diseñada para archivos más grandes (hasta 2 GB) o archivos que planeas usar en varias solicitudes.

### Carga de archivos estándar

Sube un archivo local a la API de Gemini. Los archivos que se suben de esta manera se almacenan temporalmente (48 horas) y se procesan para que el modelo los recupere de manera eficiente.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[prompt, audio_file]
)
print(response.text)
```

### JavaScript

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});
const prompt = "Describe this audio clip";

async function main() {
  const filePath = "path/to/your/sample.mp3"; // Adjust path as needed

  const myfile = await ai.files.upload({
    file: filePath,
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: createUserContent([
      prompt,
      createPartFromUri(myfile.uri, myfile.mimeType),
    ]),
  });
  console.log(response.text);

}
await main();
```

### REST

```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "${BASE_URL}/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D "${tmp_header_file}" \
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
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

### Registra archivos de Google Cloud Storage

Si tus datos ya están en Google Cloud Storage, no es necesario que los descargues y vuelvas a subirlos. Puedes registrarlo directamente con la API de File.

1. Otorga acceso de **agente de servicio** a cada bucket

   1. Habilita la API de Gemini en tu proyecto de Google Cloud.
   2. Crea el agente de servicio:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Otorga permisos al agente de servicio de la API de Gemini** para leer tus buckets de almacenamiento.

      El usuario debe asignar el [rol de IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=es-419#storage.objectViewer) `Storage Object Viewer` a este agente de servicio en los buckets de almacenamiento específicos que pretende usar.

   Este acceso no vence de forma predeterminada, pero se puede cambiar en cualquier momento. También puedes usar los comandos del [SDK de IAM de Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=es-419) para otorgar permisos.
2. Autentica tu servicio

   **Requisitos previos**

   - Habilitar API
   - Crea una cuenta o un agente de servicio con los permisos adecuados.

   Primero, debes autenticarte como el servicio que tiene permisos de visualizador de objetos de almacenamiento. La forma en que esto sucede depende del entorno en el que se ejecutará tu código de administración de archivos.

   **Fuera de Google Cloud**

   Si tu código se ejecuta fuera de Google Cloud, por ejemplo, desde tu computadora de escritorio, descarga las credenciales de la cuenta desde la consola de Google Cloud siguiendo estos pasos:

   1. Navega a la [consola de cuentas de servicio](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=es-419).
   2. Selecciona la cuenta de servicio pertinente.
   3. Selecciona la pestaña **Claves** y elige **Agregar clave, Crear clave nueva**.
   4. Elige el tipo de clave **JSON** y anota dónde se descargó el archivo en tu máquina.

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

   ### CLI

   Este es un comando interactivo. En el caso de servicios como Compute Engine, puedes adjuntar alcances al servicio en ejecución a nivel de la configuración. Consulta la [documentación del servicio administrado por el usuario](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=es-419#using) para ver un ejemplo.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Registro de archivos (API de Files)

   Usa la API de Files para registrar archivos y generar una ruta de acceso a la API de Files que se pueda usar directamente en la API de Gemini.

   ### Python

   ```
   from google import genai
   from google.genai.types import Part

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client()

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"],
       # Use the credentials obtained in the previous step.
       auth=credentials
   )
   prompt = "Summarize this file."

   # call generateContent for each file
   for f in registered_gcs_files.files:
     print(f.name)
     response = client.models.generate_content(
       model="gemini-3.5-flash",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
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

## URLs externas de HTTP o firmadas

Puedes pasar URLs HTTPS de acceso público o URLs previamente firmadas (compatibles con las [URLs previamente firmadas de S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) y las SAS de Azure) directamente en tu solicitud de generación. La API de Gemini recuperará el contenido de forma segura durante el procesamiento. Esta opción es ideal para archivos de hasta 100 MB que no quieres volver a subir.

Puedes usar URLs públicas o firmadas como entrada con las URLs en el campo `file_uri`.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[
        Part.from_uri(
            file_uri=uri,
            mime_type="application/pdf",
        ),
        prompt
    ],
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, createPartFromUri } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const response = await client.models.generateContent({
    model: 'gemini-3.5-flash',
    contents: [
      // equivalent to Part.from_uri(file_uri=uri, mime_type="...")
      createPartFromUri(uri, "application/pdf"),
      "summarize this file",
    ],
  });

  console.log(response.text);
}

main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "contents":[
            {
              "parts":[
                {"text": "Summarize this pdf"},
                {
                  "file_data": {
                    "mime_type":"application/pdf",
                    "file_uri": "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
                  }
                }
              ]
            }
          ]
        }'
```

### Accesibilidad

Verifica que las URLs que proporciones no dirijan a páginas que requieran acceso o estén detrás de un muro de pago. En el caso de las bases de datos privadas, asegúrate de crear una URL firmada con los permisos de acceso y la fecha de vencimiento correctos.

### Verificaciones de seguridad

El sistema realiza una verificación de moderación de contenido en la URL para confirmar que cumple con los estándares de seguridad y políticas (p.ej., contenido no excluido y con muro de pago). Si la URL que proporcionaste no pasa esta verificación, recibirás un `url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipos de contenido admitidos

Esta lista de tipos de archivos admitidos y limitaciones se proporciona como guía inicial y no es exhaustiva. El conjunto efectivo de tipos admitidos está sujeto a cambios y puede variar según el modelo específico y la versión del tokenizador que se usen. Los tipos no admitidos generarán un error.
Además, actualmente, la recuperación de contenido para estos tipos de archivos solo admite URLs de acceso público.

#### Tipos de archivos de texto

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipos de archivos de aplicación

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
- **Especifica tipos de MIME:** Siempre proporciona el tipo de MIME correcto para los datos del archivo para garantizar el procesamiento adecuado.
- **Manejo de errores:** Implementa el manejo de errores en tu código para administrar posibles problemas, como fallas de red, problemas de acceso a archivos o errores de API.
- **Administra los permisos de GCS:** Cuando uses el registro de GCS, otorga al agente de servicio de la API de Gemini solo el rol `Storage Object Viewer` necesario en los buckets específicos.
- **Seguridad de las URLs firmadas:** Asegúrate de que las URLs firmadas tengan un tiempo de vencimiento adecuado y permisos limitados.

## Limitaciones

- Los límites de tamaño de los archivos varían según el método (consulta la [tabla de comparación](#method-comparison)) y el tipo de archivo.
- Los datos intercalados aumentan el tamaño de la carga útil de la solicitud.
- Las cargas de la API de File son temporales y vencen después de 48 horas.
- La recuperación de URLs externas se limita a 100 MB por carga útil y admite tipos de contenido específicos.
- El registro de Google Cloud Storage requiere una configuración adecuada de IAM y la administración de tokens de OAuth.

## ¿Qué sigue?

- Intenta escribir tus propias instrucciones multimodales con [Google AI Studio](http://aistudio.google.com/?hl=es-419).
- Para obtener información sobre cómo incluir archivos en tus instrucciones, consulta las guías de [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=es-419), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=es-419) y [Procesamiento de documentos](https://ai.google.dev/gemini-api/docs/document-processing?hl=es-419).
- Para obtener más orientación sobre el diseño de instrucciones, como el ajuste de los parámetros de muestreo, consulta la guía de [Estrategias de instrucciones](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=es-419).

Enviar comentarios

Salvo que se indique lo contrario, el contenido de esta página está sujeto a la [licencia Atribución 4.0 de Creative Commons](https://creativecommons.org/licenses/by/4.0/), y los ejemplos de código están sujetos a la [licencia Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para obtener más información, consulta las [políticas del sitio de Google Developers](https://developers.google.com/site-policies?hl=es-419). Java es una marca registrada de Oracle o sus afiliados.

Última actualización: 2026-06-01 (UTC)

¿Quieres brindar más información?

[[["Fácil de comprender","easyToUnderstand","thumb-up"],["Resolvió mi problema","solvedMyProblem","thumb-up"],["Otro","otherUp","thumb-up"]],[["Falta la información que necesito","missingTheInformationINeed","thumb-down"],["Muy complicado o demasiados pasos","tooComplicatedTooManySteps","thumb-down"],["Desactualizado","outOfDate","thumb-down"],["Problema de traducción","translationIssue","thumb-down"],["Problema con las muestras o los códigos","samplesCodeIssue","thumb-down"],["Otro","otherDown","thumb-down"]],["Última actualización: 2026-06-01 (UTC)"],[],[]]
