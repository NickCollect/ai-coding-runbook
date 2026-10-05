---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=hi
fetched_at: 2026-10-05T06:43:23.113887+00:00
title: "\u0926\u0938\u094d\u0924\u093e\u0935\u0947\u091c\u093c \u0915\u094b \u0938\u092e\u091d\u0928\u093e \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=hi) अब सामान्य तौर पर उपलब्ध है. हमारा सुझाव है कि सभी नई सुविधाओं और मॉडल का ऐक्सेस पाने के लिए, इस एपीआई का इस्तेमाल करें.

![](https://ai.google.dev/_static/images/translated.svg?hl=hi)

Google आपकी पसंदीदा भाषा में कॉन्टेंट का अनुवाद करने के लिए, एआई टेक्नोलॉजी का इस्तेमाल करता है. एआई से मिले अनुवादों में गलतियां हो सकती हैं.

- [होम पेज](https://ai.google.dev/?hl=hi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=hi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=hi)
- [Docs](https://ai.google.dev/gemini-api/docs/generate-content?hl=hi)

सुझाव भेजें

# दस्तावेज़ को समझना

Gemini मॉडल, PDF फ़ॉर्मैट में मौजूद दस्तावेज़ों को प्रोसेस कर सकते हैं. इसके लिए, वे दस्तावेज़ के पूरे कॉन्टेक्स्ट को समझने के लिए, नेटिव विज़न का इस्तेमाल करते हैं. यह सिर्फ़ टेक्स्ट निकालने से कहीं ज़्यादा है. इससे Gemini ये काम कर सकता है:

- कॉन्टेंट का विश्लेषण और व्याख्या करना. इसमें टेक्स्ट, इमेज, डायग्राम, चार्ट, और टेबल शामिल हैं. यह काम, 1, 000 पेजों तक के बड़े दस्तावेज़ों के लिए भी किया जा सकता है.
- जानकारी को [स्ट्रक्चर्ड आउटपुट](https://ai.google.dev/gemini-api/docs/structured-output?hl=hi) फ़ॉर्मैट में निकालना.
- किसी दस्तावेज़ में मौजूद विज़ुअल और टेक्स्ट वाले, दोनों तरह के एलिमेंट के आधार पर, खास जानकारी देना और सवालों के जवाब देना.
- दस्तावेज़ के कॉन्टेंट को ट्रांसक्राइब करना.जैसे, एचटीएमएल में बदलना. साथ ही, लेआउट और फ़ॉर्मैटिंग को बनाए रखना, ताकि इसका इस्तेमाल डाउनस्ट्रीम ऐप्लिकेशन में किया जा सके.

आपके पास, PDF के अलावा दूसरे फ़ॉर्मैट वाले दस्तावेज़ों को भी उसी तरीके से पास करने का विकल्प होता है. हालांकि, Gemini इन्हें सामान्य टेक्स्ट के तौर पर देखेगा. इससे चार्ट या फ़ॉर्मैटिंग जैसे कॉन्टेक्स्ट खत्म हो जाएंगे.

## PDF डेटा को इनलाइन पास करना

`generateContent` के अनुरोध में, PDF डेटा को इनलाइन पास किया जा सकता है. यह छोटे दस्तावेज़ों या अस्थायी प्रोसेसिंग के लिए सबसे सही है. इसमें आपको बाद के अनुरोधों में फ़ाइल का रेफ़रंस देने की ज़रूरत नहीं होती. हमारा सुझाव है कि बड़े दस्तावेज़ों के लिए, [Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=hi#large-pdfs) का इस्तेमाल करें. इससे अनुरोध का इंतज़ार का समय कम होता है और बैंडविथ का इस्तेमाल कम होता है. साथ ही, सिलसिलेवार बातचीत में इन दस्तावेज़ों का रेफ़रंस दिया जा सकता है.

यहां दिए गए उदाहरण में, किसी यूआरएल से PDF फ़ेच करने और उसे प्रोसेस करने के लिए बाइट में बदलने का तरीका बताया गया है:

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
        model: "gemini-3.6-flash",
        contents: contents
    });
    console.log(response.text);
}

main();
```

### ऐप पर जाएं

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

# Check for FreeBSD base64 and set flags accordingly
if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
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

प्रोसेसिंग के लिए, स्थानीय फ़ाइल से PDF को पढ़ा भी जा सकता है:

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

### ऐप पर जाएं

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
        "gemini-3.6-flash",
        contents,
        nil,
    )

    fmt.Println(result.Text())
}
```

## Files API का इस्तेमाल करके PDF अपलोड करना

हमारा सुझाव है कि बड़ी फ़ाइलों के लिए या एक से ज़्यादा अनुरोधों में किसी दस्तावेज़ का फिर से इस्तेमाल करने के लिए, Files API का इस्तेमाल करें. इससे अनुरोध की लेटेन्सी कम होती है और बैंडविड्थ का इस्तेमाल कम होता है. ऐसा इसलिए, क्योंकि फ़ाइल अपलोड करने की प्रोसेस, मॉडल के अनुरोधों से अलग होती है.

### यूआरएल से बड़ी PDF फ़ाइलें

यूआरएल से बड़ी PDF फ़ाइलें अपलोड करने और उन्हें प्रोसेस करने के लिए, File API का इस्तेमाल करें:

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
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);

}

main();
```

### ऐप पर जाएं

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
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

### स्थानीय तौर पर सेव की गई बड़ी PDF फ़ाइलें

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
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);

}

main();
```

### ऐप पर जाएं

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
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

`[`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=hi)` को कॉल करके, यह पुष्टि की जा सकती है कि एपीआई ने अपलोड की गई फ़ाइल को सेव कर लिया है. साथ ही, इसका
मेटाडेटा भी पाया जा सकता है. सिर्फ़ `name` (और इसके साथ ही, `uri`) यूनीक होते हैं.

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

## एक से ज़्यादा PDF पास करना

Gemini API, एक ही अनुरोध में एक से ज़्यादा PDF दस्तावेज़ों (ज़्यादा से ज़्यादा 1,000 पेज) को प्रोसेस कर सकता है. हालांकि, इसके लिए ज़रूरी है कि दस्तावेज़ों और टेक्स्ट प्रॉम्प्ट का कुल साइज़, मॉडल की कॉन्टेक्स्ट विंडो के अंदर हो.

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
        model: 'gemini-3.6-flash',
        contents: content,
    });

    console.log(response.text);
}

main();
```

### ऐप पर जाएं

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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key=$GOOGLE_API_KEY" \
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

## तकनीकी जानकारी

Gemini, 50 एमबी या 1,000 पेजों तक की PDF फ़ाइलों के साथ काम करता है. यह सीमा, इनलाइन डेटा और Files API से अपलोड किए गए डेटा, दोनों पर लागू होती है. दस्तावेज़ का हर पेज, 258 टोकन के बराबर होता है.

[मॉडल की कॉन्टेक्स्ट विंडो के अलावा, किसी दस्तावेज़ में पिक्सल की संख्या पर कोई खास सीमा नहीं है. हालांकि, बड़े पेजों को ज़्यादा से ज़्यादा 3072 x 3072 रिज़ॉल्यूशन तक स्केल डाउन किया जाता है. इस दौरान, उनके ओरिजनल आसपेक्ट रेशियो को बनाए रखा जाता है. वहीं, छोटे पेजों को 768 x 768 पिक्सल तक स्केल अप किया जाता है.](https://ai.google.dev/gemini-api/docs/long-context?hl=hi) कम साइज़ वाले पेजों के लिए, बैंडविड्थ के अलावा कोई लागत कम नहीं होती. वहीं, ज़्यादा रिज़ॉल्यूशन वाले पेजों के लिए, परफ़ॉर्मेंस में कोई सुधार नहीं होता.

### Gemini 3 के मॉडल

Gemini 3 में, `media_resolution` पैरामीटर की मदद से, मल्टीमॉडल विज़न प्रोसेसिंग पर ज़्यादा कंट्रोल मिलता है. अब हर मीडिया पार्ट के लिए, रिज़ॉल्यूशन को कम, सामान्य या ज़्यादा पर सेट किया जा सकता है. इस सुविधा के जुड़ने के बाद, PDF दस्तावेज़ों की प्रोसेसिंग को अपडेट कर दिया गया है:

1. **नेटिव टेक्स्ट शामिल करना:** PDF में नेटिव तौर पर एम्बेड किए गए टेक्स्ट को निकालकर, मॉडल को उपलब्ध कराया जाता है.
2. **बिलिंग और टोकन की रिपोर्टिंग:**
   - PDF में निकाले गए **नेटिव टेक्स्ट** से जनरेट हुए टोकन के लिए, **कोई शुल्क नहीं लिया जाता**.
   - एपीआई के जवाब के `usage_metadata` सेक्शन में, PDF पेजों को (इमेज के तौर पर) प्रोसेस करके जनरेट हुए टोकन को अब `IMAGE` मोडैलिटी में गिना जाता है. पहले के कुछ वर्शन में, इन्हें अलग `DOCUMENT` मोडैलिटी में गिना जाता था.

मीडिया रिज़ॉल्यूशन पैरामीटर के बारे में ज़्यादा जानने के लिए, [मीडिया रिज़ॉल्यूशन](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=hi) से जुड़ी गाइड देखें.

### दस्तावेज़ के टाइप

तकनीकी तौर पर, दस्तावेज़ को समझने के लिए, TXT, Markdown, HTML, XML वगैरह जैसे अन्य MIME टाइप पास किए जा सकते हैं. हालांकि, दस्तावेज़ का विज़न ***सिर्फ़ PDF को समझ पाता है***. अन्य टाइप को सिर्फ़ टेक्स्ट के तौर पर निकाला जाएगा. साथ ही, मॉडल यह नहीं समझ पाएगा कि उन फ़ाइलों की रेंडरिंग में हमें क्या दिखता है. चार्ट, डायग्राम, एचटीएमएल टैग, Markdown फ़ॉर्मैटिंग वगैरह जैसे किसी भी फ़ाइल टाइप की खास जानकारी नहीं मिलेगी.

फ़ाइल इनपुट के अन्य तरीकों के बारे में जानने के लिए, [फ़ाइल इनपुट के तरीकों](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=hi) से जुड़ी गाइड देखें.

### सबसे सही तरीके

सर्वोत्तम परिणामों के लिएः

- अपलोड करने से पहले, पेजों को सही ओरिएंटेशन में घुमाएं.
- धुंधले पेजों का इस्तेमाल न करें.
- अगर किसी एक पेज का इस्तेमाल किया जा रहा है, तो पेज के बाद टेक्स्ट प्रॉम्प्ट डालें.

## आगे क्या करना है

ज़्यादा जानने के लिए, ये लेख देखें:

- [फ़ाइल प्रॉम्प्ट करने की रणनीतियां](https://ai.google.dev/gemini-api/docs/files?hl=hi#prompt-guide): Gemini API, टेक्स्ट, इमेज, ऑडियो, और वीडियो डेटा के साथ प्रॉम्प्ट करने की सुविधा देता है. इसे मल्टीमॉडल प्रॉम्प्टिंग भी कहा जाता है.
- [सिस्टम के निर्देश](https://ai.google.dev/gemini-api/docs/text-generation?hl=hi#system-instructions):
  सिस्टम के निर्देशों की मदद से, अपनी खास ज़रूरतों और इस्तेमाल के उदाहरणों के हिसाब से, मॉडल के व्यवहार को कंट्रोल किया जा सकता है.

सुझाव भेजें

जब तक कुछ अलग से न बताया जाए, तब तक इस पेज की सामग्री को [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) के तहत और कोड के नमूनों को [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) के तहत लाइसेंस मिला है. ज़्यादा जानकारी के लिए, [Google Developers साइट नीतियां](https://developers.google.com/site-policies?hl=hi) देखें. Oracle और/या इससे जुड़ी हुई कंपनियों का, Java एक रजिस्टर किया हुआ ट्रेडमार्क है.

आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया.

क्या आपको हमें और कुछ बताना है?

[[["समझने में आसान है","easyToUnderstand","thumb-up"],["मेरी समस्या हल हो गई","solvedMyProblem","thumb-up"],["अन्य","otherUp","thumb-up"]],[["वह जानकारी मौजूद नहीं है जो मुझे चाहिए","missingTheInformationINeed","thumb-down"],["बहुत मुश्किल है / बहुत सारे चरण हैं","tooComplicatedTooManySteps","thumb-down"],["पुराना","outOfDate","thumb-down"],["अनुवाद से जुड़ी समस्या","translationIssue","thumb-down"],["सैंपल / कोड से जुड़ी समस्या","samplesCodeIssue","thumb-down"],["अन्य","otherDown","thumb-down"]],["आखिरी बार 2026-09-12 (UTC) को अपडेट किया गया."],[],[]]
