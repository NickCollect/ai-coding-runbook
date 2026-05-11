---
source_url: https://ai.google.dev/gemini-api/docs/interactions/file-input-methods?hl=pt-BR
fetched_at: 2026-05-11T05:02:28.796347+00:00
title: "Gemini Interactions API \u00a0|\u00a0 Google AI for Developers"
---

O [Deep Research do Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=pt-br) já está disponível em pré-lançamento com planejamento colaborativo, visualização, suporte a MCP e muito mais.

![](https://ai.google.dev/_static/images/translated.svg?hl=pt-br)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Página inicial](https://ai.google.dev/?hl=pt-br)
- [Gemini API](https://ai.google.dev/gemini-api?hl=pt-br)
- [Interactions API](https://ai.google.dev/gemini-api/docs/interactions/overview?hl=pt-br)
- [Documentos](https://ai.google.dev/gemini-api/docs?hl=pt-br)

Envie comentários

# Métodos de entrada de arquivo

Este guia explica as diferentes maneiras de incluir arquivos de mídia, como imagens, áudio, vídeo e documentos, ao fazer solicitações para a API Gemini.
Os novos métodos são compatíveis com todos os endpoints da API Gemini, incluindo
API Batch, Interactions e Live.
A escolha do método certo depende do tamanho do arquivo, de onde os dados estão armazenados e da frequência com que você planeja usar o arquivo.

A maneira mais simples de incluir um arquivo como entrada é ler um arquivo local e
incluí-lo em um comando. O exemplo a seguir mostra como ler um arquivo PDF local. Os PDFs são limitados a 50 MB para esse método. Consulte a [tabela de comparação de métodos de entrada](#method-comparison) para ver uma lista completa de tipos e limites de entrada de arquivos.

### Python

```
from google import genai
import pathlib
import base64

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "data": base64.b64encode(filepath.read_bytes()).decode('utf-8'), "mime_type": "application/pdf"}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
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
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: fs.readFileSync(filePath).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
}

main();
```

### REST

```
# Encode the local file to base64
B64_CONTENT=$(base64 -w 0 my_local_file.pdf)

curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3-flash-preview",
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

## Comparação de métodos de entrada

A tabela a seguir compara cada método de entrada com limites de arquivos e casos de uso recomendados. Observe que o limite de tamanho do arquivo pode variar dependendo do tipo de arquivo e do modelo ou tokenizador usado para processar o arquivo.

| Método | Ideal para | Tamanho máximo do arquivo | Persistência |
| --- | --- | --- | --- |
| **Dados inline** | Testes rápidos, arquivos pequenos, aplicativos em tempo real. | 100 MB por solicitação ou payload   (**50 MB para PDFs**) | Nenhum (enviado com todas as solicitações) |
| **Upload de arquivos da API** | Arquivos grandes, arquivos usados várias vezes. | 2 GB por arquivo,   até 20 GB por projeto | 48 horas |
| **Registro de URI do GCS da API File** | Arquivos grandes já no Google Cloud Storage, arquivos usados várias vezes. | 2 GB por arquivo, sem limites gerais de armazenamento | Nenhum (buscado por solicitação). Um registro único pode dar acesso por até 30 dias. |
| **URLs externos** | Dados públicos ou em buckets da nuvem (AWS, Azure, GCS) sem fazer upload novamente. | 100 MB por solicitação/payload | Nenhum (buscado por solicitação) |

## Dados inline

Para arquivos menores (menos de 100 MB ou 50 MB para PDFs), é possível transmitir os dados diretamente no payload da solicitação. Esse é o método mais simples para testes rápidos ou
aplicativos que processam dados transitórios em tempo real. Você pode fornecer dados como strings codificadas em base64 ou lendo arquivos locais diretamente.

Para ver um exemplo de leitura de um arquivo local, consulte o exemplo no início
desta página.

### Buscar de um URL

Também é possível buscar um arquivo de um URL, convertê-lo em bytes e incluí-lo na entrada.

### Python

```
from google import genai
import httpx
import base64

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "data": base64.b64encode(doc_data).decode('utf-8'), "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
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
        model: "gemini-3-flash-preview",
        input: [
            { type: "text", text: prompt },
            {
                type: "document",
                data: Buffer.from(pdfResp).toString("base64"),
                mime_type: "application/pdf"
            }
        ]
    });
    const modelStep = interaction.steps.find(s => s.type === 'model_output');
    if (modelStep) {
      for (const contentBlock of modelStep.content) {
        if (contentBlock.type === 'text') console.log(contentBlock.text);
      }
    }
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

# Create JSON payload file
cat <<EOF > payload.json
{
"model": "gemini-3-flash-preview",
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

## API Gemini File

A API File foi projetada para arquivos maiores (até 2 GB) ou arquivos que você pretende usar em várias solicitações.

### Upload de arquivo padrão

Faça upload de um arquivo local para a API Gemini. Os arquivos enviados dessa forma são armazenados temporariamente (48 horas) e processados para recuperação eficiente pelo modelo.

### Python

```
from google import genai

client = genai.Client()

# Upload the file
doc_file = client.files.upload(file="path/to/your/sample.pdf")
prompt = "Summarize this document"

# Use the uploaded file in an interaction
interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "text", "text": prompt},
        {"type": "document", "uri": doc_file.uri, "mime_type": doc_file.mime_type}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
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
    model: "gemini-3-flash-preview",
    input: [
        { type: "text", text: prompt },
        { type: "document", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

await main();
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
      "model": "gemini-3-flash-preview",
      "input": [
        {"type": "text", "text": "Summarize this document"},
        {"type": "document", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }'
```

### Registrar arquivos do Google Cloud Storage

Se os dados já estiverem no Google Cloud Storage, não será necessário fazer o download e o reenvio. É possível registrar diretamente com a API File.

1. Conceda ao **agente de serviço** acesso a cada bucket.

   1. Ative a API Gemini no seu projeto do Google Cloud.
   2. Crie o agente de serviço:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Conceda ao agente de serviço da API Gemini permissões** para ler seus buckets de armazenamento.

      O usuário precisa atribuir o [papel do IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=pt-br#storage.objectViewer) `Storage Object Viewer` a esse agente de serviço nos buckets de armazenamento específicos que pretende usar.

   Esse acesso não expira por padrão, mas pode ser alterado a qualquer momento. Também é possível usar os comandos do [SDK do IAM do Google Cloud Storage](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=pt-br) para conceder permissões.
2. Autenticar seu serviço

   **Pré-requisitos**

   - Ativar API
   - Crie uma conta de serviço ou um agente com as permissões adequadas.

   Primeiro, faça a autenticação como o serviço que tem permissões de leitor de objetos do Storage. Isso depende do ambiente em que o código de gerenciamento de arquivos
   será executado.

   **Fora do Google Cloud**

   Se o código estiver sendo executado fora do Google Cloud, como no seu computador,
   faça o download das credenciais da conta no console do Google Cloud seguindo estas etapas:

   1. Acesse o [console da conta de serviço](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=pt-br).
   2. Selecione a conta de serviço relevante
   3. Selecione a guia **Chaves** e escolha **Adicionar chave, Criar nova chave**.
   4. Escolha o tipo de chave **JSON** e observe onde o arquivo foi baixado na sua máquina.

   Para mais detalhes, consulte a documentação oficial do Google Cloud sobre
   [gerenciamento de chaves de conta de serviço](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=pt-br).

   Em seguida, use os comandos a seguir para autenticar. Esses comandos pressupõem que o arquivo da conta de serviço esteja no diretório atual, chamado `service-account.json`.

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

   **No Google Cloud**

   Se você estiver executando diretamente no Google Cloud, por exemplo, usando [funções do Cloud Run](https://cloud.google.com/functions?hl=pt-br) ou uma [instância do Compute Engine](https://cloud.google.com/products/compute?hl=pt-br), terá credenciais implícitas, mas precisará fazer a autenticação novamente para conceder os escopos adequados.

   ### Python

   Esse código espera que o serviço esteja sendo executado em um ambiente em que as [Credenciais padrão de aplicativo](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pt-br) podem ser obtidas automaticamente, como o Cloud Run ou o Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Esse código espera que o serviço esteja sendo executado em um ambiente em que as [Credenciais padrão de aplicativo](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=pt-br) podem ser obtidas automaticamente, como o Cloud Run ou o Compute Engine.

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

   Este é um comando interativo. Para serviços como o Compute Engine, é possível anexar escopos ao
   serviço em execução no nível da configuração. Consulte a [documentação do serviço gerenciado pelo usuário](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=pt-br#using) para ver um exemplo.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Registro de arquivos (API Files)

   Use a API Files para registrar arquivos e produzir um caminho da API Files que pode
   ser usado diretamente na API Gemini.

   ### Python

   ```
   from google import genai

   # Note that you must provide an API key in the GEMINI_API_KEY
   # environment variable, but it is unused for the registration endpoint.
   client = genai.Client(credentials=credentials)

   registered_gcs_files = client.files.register_files(
       uris=["gs://my_bucket/some_object.pdf", "gs://bucket2/object2.txt"]
   )
   prompt = "Summarize this file."

   # call interactions.create for each file
   for f in registered_gcs_files.files:
     print(f.name)
     interaction = client.interactions.create(
       model="gemini-3-flash-preview",
       input=[
         {"type": "text", "text": prompt},
         {"type": "document", "uri": f.uri, "mime_type": f.mime_type}
       ],
     )
     # Print the model's text response
     for step in interaction.steps:
         if step.type == "model_output":
             for content_block in step.content:
                 if content_block.type == "text":
                     print(content_block.text)
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
               model: "gemini-3-flash-preview",
               input: [
                   { type: "text", text: prompt },
                   { type: "document", uri: file.uri, mime_type: file.mimeType }
               ]
           });

           const modelStep = interaction.steps.find(s => s.type === 'model_output');
           if (modelStep) {
               for (const contentBlock of modelStep.content) {
                   if (contentBlock.type === 'text') console.log(contentBlock.text);
               }
           }
       }
   }

   main();
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

## HTTP externo / URLs assinados

É possível transmitir URLs HTTPS acessíveis publicamente ou pré-assinados diretamente na sua
solicitação. A API Gemini vai buscar o conteúdo com segurança durante o processamento.
É ideal para arquivos de até 100 MB que você não quer reenviar.

### Python

```
from google import genai

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input=[
        {"type": "document", "uri": uri, "mime_type": "application/pdf"},
        {"type": "text", "text": prompt}
    ]
)
# Print the model's text response
for step in interaction.steps:
    if step.type == "model_output":
        for content_block in step.content:
            if content_block.type == "text":
                print(content_block.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf";

async function main() {
  const interaction = await client.interactions.create({
    model: 'gemini-3-flash-preview',
    input: [
      { type: "document", uri: uri, mime_type: "application/pdf" },
      { type: "text", text: "summarize this file" }
    ]
  });

  const modelStep = interaction.steps.find(s => s.type === 'model_output');
  if (modelStep) {
    for (const contentBlock of modelStep.content) {
      if (contentBlock.type === 'text') console.log(contentBlock.text);
    }
  }
}

main();
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
      -H 'x-goog-api-key: $GEMINI_API_KEY' \
      -H 'Content-Type: application/json' \
      -d '{
          "model": "gemini-3-flash-preview",
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

### Acessibilidade

Verifique se os URLs fornecidos não levam a páginas que exigem login ou estão atrás de um paywall. Para bancos de dados particulares, crie um URL assinado
com as permissões de acesso e o vencimento corretos.

### Confirmações de segurança

O sistema faz uma verificação de moderação de conteúdo no URL para confirmar se ele atende aos padrões de segurança e política. Se o URL não passar nessa verificação, você vai receber um
`url_retrieval_status` de `URL_RETRIEVAL_STATUS_UNSAFE`.

### Tipos de conteúdo compatíveis

Essa lista de tipos de arquivo e limitações aceitos é apenas uma orientação inicial e não é abrangente. O conjunto efetivo de tipos compatíveis está sujeito a mudanças e pode variar de acordo com o modelo específico e a versão do tokenizador em uso. Tipos incompatíveis vão resultar em um erro.
Além disso, a recuperação de conteúdo para esses tipos de arquivo só é compatível com URLs de acesso público.

#### Tipos de arquivos de texto

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Tipos de arquivo de aplicativo

- `application/json`
- `application/pdf`

#### Tipos de arquivo de imagem

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

## Práticas recomendadas

- **Escolha o método certo**:use dados inline para arquivos pequenos e temporários.
  Use a API File para arquivos maiores ou usados com frequência. Use URLs externos
  para dados já hospedados on-line.
- **Especifique tipos MIME**:sempre forneça o tipo MIME correto para os dados do arquivo para garantir o processamento adequado.
- **Tratar erros**:implemente o tratamento de erros no seu código para gerenciar
  possíveis problemas, como falhas de rede, problemas de acesso a arquivos ou erros
  de API.

## Limitações

- Os limites de tamanho de arquivo variam de acordo com o método (consulte a [tabela de comparação](#method-comparison)) e o tipo de arquivo.
- Os dados inline aumentam o tamanho do payload da solicitação.
- Os uploads da API File são temporários e expiram após 48 horas.
- A busca de URL externo é limitada a 100 MB por payload e é compatível com tipos de conteúdo específicos.

## A seguir

- Escreva seus próprios comandos multimodais usando o [Google AI Studio](http://aistudio.google.com/?hl=pt-br).
- Para informações sobre como incluir arquivos nos comandos, consulte os guias de
  [Vision](https://ai.google.dev/gemini-api/docs/interactions/vision?hl=pt-br),
  [Áudio](https://ai.google.dev/gemini-api/docs/interactions/audio?hl=pt-br) e
  [Processamento de documentos](https://ai.google.dev/gemini-api/docs/interactions/document-processing?hl=pt-br).

Envie comentários

Exceto em caso de indicação contrária, o conteúdo desta página é licenciado de acordo com a [Licença de atribuição 4.0 do Creative Commons](https://creativecommons.org/licenses/by/4.0/), e as amostras de código são licenciadas de acordo com a [Licença Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Para mais detalhes, consulte as [políticas do site do Google Developers](https://developers.google.com/site-policies?hl=pt-br). Java é uma marca registrada da Oracle e/ou afiliadas.

Última atualização 2026-05-09 UTC.

Quer enviar seu feedback?

[[["Fácil de entender","easyToUnderstand","thumb-up"],["Meu problema foi resolvido","solvedMyProblem","thumb-up"],["Outro","otherUp","thumb-up"]],[["Não contém as informações de que eu preciso","missingTheInformationINeed","thumb-down"],["Muito complicado / etapas demais","tooComplicatedTooManySteps","thumb-down"],["Desatualizado","outOfDate","thumb-down"],["Problema na tradução","translationIssue","thumb-down"],["Problema com as amostras / o código","samplesCodeIssue","thumb-down"],["Outro","otherDown","thumb-down"]],["Última atualização 2026-05-09 UTC."],[],[]]
