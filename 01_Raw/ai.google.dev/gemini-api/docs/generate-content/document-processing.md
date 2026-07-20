---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=tr
fetched_at: 2026-07-20T04:38:00.475350+00:00
title: "Belge anlama \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Belge anlama

Gemini modelleri, doküman bağlamlarının tamamını anlamak için yerel görsel işleme özelliğini kullanarak PDF biçimindeki dokümanları işleyebilir. Bu, yalnızca metin ayıklamanın ötesine geçerek Gemini'ın aşağıdaki işlemleri yapmasına olanak tanır:

- Metin, resim, diyagram, grafik ve tablo gibi içerikleri 1.000 sayfaya kadar olan uzun dokümanlarda bile analiz edip yorumlayın.
- Bilgileri [yapılandırılmış çıkış](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) biçimlerinde ayıklayın.
- Bir belgedeki hem görsel hem de metin öğelerini temel alarak özetleme ve soru yanıtlama
- Aşağı akış uygulamalarında kullanılmak üzere düzenleri ve biçimlendirmeyi koruyarak doküman içeriğini (ör. HTML'ye) transkribe edin.

PDF olmayan dokümanları da aynı şekilde iletebilirsiniz ancak Gemini bunları normal metin olarak görür. Bu durumda grafikler veya biçimlendirme gibi bağlamlar ortadan kalkar.

## PDF verilerini satır içi olarak iletme

PDF verilerini `generateContent` isteğinde satır içi olarak iletebilirsiniz. Bu yöntem, daha küçük belgeler veya dosyaya sonraki isteklerde başvurmanız gerekmeyen geçici işlemler için en uygun yöntemdir. İstek gecikmesini iyileştirmek ve bant genişliği kullanımını azaltmak için çok aşamalı etkileşimlerde başvurmanız gereken daha büyük belgeler için [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr#large-pdfs)'yi kullanmanızı öneririz.

Aşağıdaki örnekte, bir URL'den PDF'nin nasıl getirileceği ve işlenmek üzere baytlara nasıl dönüştürüleceği gösterilmektedir:

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

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {
    const pdfResp = await fetch('https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf')
        .then((response) => response.arrayBuffer());

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
        model: "gemini-3.5-flash",
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

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfResp, _ := http.Get("https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf")
    var pdfBytes []byte
    if pdfResp != nil && pdfResp.Body != nil {
        pdfBytes, _ = io.ReadAll(pdfResp.Body)
        pdfResp.Body.Close()
    }

    parts := []*genai.Part{
        &genai.Part{
            InlineData: &genai.Blob{
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
        "gemini-3.5-flash",
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

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Base64 encode the PDF
ENCODED_PDF=$(base64 $B64FLAGS "${DISPLAY_NAME}.pdf")

# Generate content using the base64 encoded PDF
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GOOGLE_API_KEY" \
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

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

İşleme için yerel bir dosyadan PDF de okuyabilirsiniz:

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
  model="gemini-3.5-flash",
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
        model: "gemini-3.5-flash",
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

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })

    pdfBytes, _ := os.ReadFile("path/to/your/file.pdf")

    parts := []*genai.Part{
        &genai.Part{
            InlineData: &genai.Blob{
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
        "gemini-3.5-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

## Files API'yi kullanarak PDF yükleme

Daha büyük dosyalar için veya bir dokümanı birden fazla istekte yeniden kullanmak istediğinizde Files API'yi kullanmanızı öneririz. Bu sayede, dosya yükleme işlemi model isteklerinden ayrılır ve istek gecikmesi iyileşirken bant genişliği kullanımı azalır.

### URL'lerden alınan büyük PDF'ler

URL'lerden büyük PDF dosyalarını yükleme ve işleme sürecini basitleştirmek için File API'yi kullanın:

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
  model="gemini-3.5-flash",
  contents=[sample_doc, prompt])
print(response.text)
```

### JavaScript

```
import { createPartFromUri, GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

async function main() {

    const pdfBuffer = await fetch("https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf")
        .then((response) => response.arrayBuffer());

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
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const content = [
        'Summarize this document',
    ];

    if (file.uri && file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.5-flash',
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

  ctx := context.Background()
  client, _ := genai.NewClient(ctx, &genai.ClientConfig{
    APIKey:  os.Getenv("GEMINI_API_KEY"),
    Backend: genai.BackendGeminiAPI,
  })

  pdfURL := "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"
  localPdfPath := "A17_FlightPlan_downloaded.pdf"

  respHttp, _ := http.Get(pdfURL)
  defer respHttp.Body.Close()

  outFile, _ := os.Create(localPdfPath)
  defer outFile.Close()

  _, _ = io.Copy(outFile, respHttp.Body)

  uploadConfig := &genai.UploadFileConfig{MIMEType: "application/pdf"}
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
        "gemini-3.5-flash",
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

MIME_TYPE=$(file -b --mime-type "${DISPLAY_NAME}.pdf")
NUM_BYTES=$(wc -c < "${DISPLAY_NAME}.pdf")

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

file_uri=$(jq ".file.uri" file_info.json)
echo "file_uri: ${file_uri}"

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "'$PROMPT'"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

# Clean up the downloaded PDF
rm "${DISPLAY_NAME}.pdf"
```

### Yerel olarak depolanan büyük PDF'ler

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
    model="gemini-3.5-flash",
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
        console.log('File is still processing, retrying in 5 seconds');

        await new Promise((resolve) => {
            setTimeout(resolve, 5000);
        });
    }
    if (file.state === 'FAILED') {
        throw new Error('File processing failed.');
    }

    // Add the file to the contents.
    const content = [
        'Summarize this document',
    ];

    if (file.uri && file.mimeType) {
        const fileContent = createPartFromUri(file.uri, file.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.5-flash',
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

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  os.Getenv("GEMINI_API_KEY"),
        Backend: genai.BackendGeminiAPI,
    })
    localPdfPath := "/path/to/file.pdf"

    uploadConfig := &genai.UploadFileConfig{MIMEType: "application/pdf"}
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
        "gemini-3.5-flash",
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

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Can you add a few more lines to this poem?"},
          {"file_data":{"mime_type": "application/pdf", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

[`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=tr) işlevini çağırarak API'nin yüklenen dosyayı başarıyla sakladığını doğrulayabilir ve dosyanın meta verilerini alabilirsiniz. Yalnızca `name`
(ve dolayısıyla `uri`) benzersizdir.

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
curl https://generativelanguage.googleapis.com/v1beta/files/$name > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Birden fazla PDF'yi iletme

Gemini API, belgelerin ve metin isteminin toplam boyutu modelin bağlam penceresi içinde kaldığı sürece tek bir istekte birden fazla PDF belgesini (1.000 sayfaya kadar) işleyebilir.

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
    model="gemini-3.5-flash",
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
        .then((response) => response.arrayBuffer());

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
    const content = [
        'What is the difference between each of the main benchmarks between these two papers? Output these in a table.',
    ];

    let file1 = await uploadRemotePDF("https://arxiv.org/pdf/2312.11805", "PDF 1")
    if (file1.uri && file1.mimeType) {
        const fileContent = createPartFromUri(file1.uri, file1.mimeType);
        content.push(fileContent);
    }
    let file2 = await uploadRemotePDF("https://arxiv.org/pdf/2403.05530", "PDF 2")
    if (file2.uri && file2.mimeType) {
        const fileContent = createPartFromUri(file2.uri, file2.mimeType);
        content.push(fileContent);
    }

    const response = await ai.models.generateContent({
        model: 'gemini-3.5-flash',
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

    ctx := context.Background()
    client, _ := genai.NewClient(ctx, &genai.ClientConfig{
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

    outFile2, _ := os.Create(localPath2)
    _, _ = io.Copy(outFile2, respHttp2.Body)
    outFile2.Close()

    uploadConfig1 := &genai.UploadFileConfig{MIMEType: "application/pdf"}
    uploadedFile1, _ := client.Files.UploadFromPath(ctx, localPath1, uploadConfig1)

    uploadConfig2 := &genai.UploadFileConfig{MIMEType: "application/pdf"}
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

    modelName := "gemini-3.5-flash"
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

  local MIME_TYPE=$(file -b --mime-type "${display_name}.pdf")
  local NUM_BYTES=$(wc -c < "${display_name}.pdf")

  echo "MIME_TYPE: ${MIME_TYPE}"
  echo "NUM_BYTES: ${NUM_BYTES}"

  local tmp_header_file=upload-header.tmp

  # Initial resumable request
  curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
    -D "${tmp_header_file}" \
    -H "X-Goog-Upload-Protocol: resumable" \
    -H "X-Goog-Upload-Command: start" \
    -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
    -H "Content-Type: application/json" \
    -d "{'file': {'display_name': '${display_name}'}}" 2> /dev/null

  local upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
  rm "${tmp_header_file}"

  # Upload the PDF
  curl "${upload_url}" \
    -H "Content-Length: ${NUM_BYTES}" \
    -H "X-Goog-Upload-Offset: 0" \
    -H "X-Goog-Upload-Command: upload, finalize" \
    --data-binary "@${display_name}.pdf" 2> /dev/null > "file_info_${display_name}.json"

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GOOGLE_API_KEY" \
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
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Teknik ayrıntılar

Gemini, 50 MB veya 1.000 sayfaya kadar olan PDF dosyalarını destekler. Bu sınır hem satır içi veriler hem de Files API yüklemeleri için geçerlidir. Her belge sayfası 258 jetona karşılık gelir.

Modelin [bağlam penceresi](https://ai.google.dev/gemini-api/docs/long-context?hl=tr) dışında bir dokümandaki piksel sayısıyla ilgili belirli bir sınır olmasa da daha büyük sayfalar, orijinal en boy oranları korunarak maksimum 3072 x 3072 çözünürlüğe ölçeklendirilirken daha küçük sayfalar 768 x 768 piksele ölçeklendirilir. Daha küçük boyutlardaki sayfalar için bant genişliği dışında maliyet düşüşü veya daha yüksek çözünürlükteki sayfalar için performans artışı olmaz.

### Gemini 3 modelleri

Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol sunar. Artık çözünürlüğü her bir medya parçası için ayrı ayrı düşük, orta veya yüksek olarak ayarlayabilirsiniz. Bu eklemeyle birlikte PDF belgelerinin işlenmesi güncellendi:

1. **Doğal metin ekleme:** PDF'ye doğal olarak yerleştirilmiş metin çıkarılır ve modele sağlanır.
2. **Faturalandırma ve jeton raporlama:**
   - PDF'lerdeki çıkarılan **yerel metinden** kaynaklanan jetonlar için **ücretlendirilmezsiniz**.
   - API yanıtının `usage_metadata` bölümünde, PDF sayfalarının (resim olarak) işlenmesiyle oluşturulan jetonlar artık `IMAGE` biçimi altında sayılıyor. Bazı önceki sürümlerde olduğu gibi ayrı bir `DOCUMENT` biçimi altında sayılmıyor.

Medya çözünürlüğü parametresi hakkında daha fazla bilgi için [Medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=tr) kılavuzuna bakın.

### Belge türleri

Teknik olarak, doküman anlama için TXT, Markdown, HTML, XML gibi diğer MIME türlerini iletebilirsiniz. Ancak dokümanla ilgili görsel algılama ***yalnızca PDF'leri anlamlı bir şekilde anlar***. Diğer türler düz metin olarak ayıklanır ve model, bu dosyaların oluşturulmasında gördüklerimizi yorumlayamaz. Grafikler, diyagramlar, HTML etiketleri, Markdown biçimlendirmesi vb. gibi dosya türüne özgü tüm özellikler kaybolur.

Diğer dosya giriş yöntemleri hakkında bilgi edinmek için [Dosya giriş yöntemleri](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr) kılavuzuna bakın.

### En iyi uygulamalar

En iyi sonuçlar için:

- Yüklemeden önce sayfaları doğru yöne döndürün.
- Bulanık sayfalardan kaçının.
- Tek sayfa kullanıyorsanız metin istemini sayfanın sonuna yerleştirin.

## Sırada ne var?

Daha fazla bilgi edinmek için aşağıdaki kaynakları inceleyin:

- [Dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide): Gemini API, çok formatlı istem olarak da bilinen metin, resim, ses ve video verileriyle istemi destekler.
- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions):
  Sistem talimatları, modelin davranışını özel ihtiyaçlarınıza ve kullanım alanlarınıza göre yönlendirmenizi sağlar.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-24 UTC."],[],[]]
