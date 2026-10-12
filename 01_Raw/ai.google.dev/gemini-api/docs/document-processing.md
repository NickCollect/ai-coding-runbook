---
source_url: https://ai.google.dev/gemini-api/docs/document-processing?hl=bn
fetched_at: 2026-10-12T07:06:54.630158+00:00
title: "\u09a1\u0995\u09c1\u09ae\u09c7\u09a8\u09cd\u099f \u09ac\u09cb\u099d\u09be \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

জেমিনি ৩.৮ ফ্ল্যাশ এখন পাওয়া যাচ্ছে। [ব্যবহার করে দেখুন](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=bn) ।

![](https://ai.google.dev/_static/images/translated.svg?hl=bn)

আপনার পছন্দের ভাষায় কন্টেন্ট অনুবাদ করতে Google তার AI প্রযুক্তি ব্যবহার করে। AI-এর মাধ্যমে করা অনুবাদে ভুল থাকতে পারে।

- [হোম](https://ai.google.dev/?hl=bn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=bn)
- [দস্তাবেজ](https://ai.google.dev/gemini-api/docs?hl=bn)

মতামত জানান

# ডকুমেন্ট বোঝা

Gemini মডেল, সম্পূর্ণ ডকুমেন্টের প্রসঙ্গ বোঝার জন্য নেটিভ
ভিশন ব্যবহার করে, PDF ফর্ম্যাটে ডকুমেন্ট প্রসেস করতে পারে। এটি শুধু টেক্সট এক্সট্র্যাক্ট করার
চেয়ে অনেক বেশি কিছু করে, এর ফলে Gemini এগুলি করতে পারে:

- ১০০০ পৃষ্ঠা পর্যন্ত দীর্ঘ ডকুমেন্টের টেক্সট, ছবি, ডায়াগ্রাম,
  চার্ট ও টেবিল সহ কন্টেন্ট বিশ্লেষণ ও ব্যাখ্যা করো।
- [স্ট্রাকচার্ড আউটপুট](https://ai.google.dev/gemini-api/docs/structured-output?hl=bn) ফর্ম্যাটে তথ্য এক্সট্র্যাক্ট করা।
- ডকুমেন্টে থাকা ভিজ্যুয়াল ও টেক্সচুয়াল এলিমেন্ট, দু'টির ভিত্তিতেই সারসংক্ষেপ তৈরি করা ও প্রশ্নের উত্তর দেওয়া
  ।
- ডকুমেন্টের কন্টেন্ট (যেমন, HTML-এ) ট্রান্সক্রাইব করা, লেআউট ও
  ফর্ম্যাটিং বজায় রাখা, যাতে ডাউনস্ট্রিম অ্যাপ্লিকেশনে ব্যবহার করা যায়।

আপনি একই পদ্ধতিতে PDF নয় এমন ডকুমেন্টও পাস করতে পারবেন, তবে Gemini সেগুলি
সাধারণ টেক্সট হিসেবে দেখবে, যার ফলে চার্ট বা ফর্ম্যাটিংয়ের মতো প্রসঙ্গ বাদ পড়ে যাবে।

## ইনলাইন PDF ডেটা পাস করা

আপনি অনুরোধে ইনলাইন হিসেবে PDF ডেটা পাস করতে পারবেন। ছোট ডকুমেন্ট বা অস্থায়ী প্রসেসিংয়ের জন্য এটি সবচেয়ে
উপযুক্ত, যেখানে পরবর্তী অনুরোধে আপনাকে ফাইলটি
রেফার করার প্রয়োজন নেই। আমরা সাজেস্ট করি যে, একাধিক ইন্ট্যার‍্যাকশনের ক্ষেত্রে আপনাকে উল্লেখ করতে হবে এমন বড় ডকুমেন্ট
[Files API](https://ai.google.dev/gemini-api/docs/document-processing?hl=bn#large-pdfs)
ব্যবহার করে আপলোড করুন। এর ফলে অনুরোধের লেটেন্সি কমে যাবে এবং ব্যান্ডউইথের ব্যবহারও কম হবে।

কীভাবে ইনলাইন PDF ডেটা পাস করতে হয় তা নিম্নলিখিত উদাহরণ থেকে দেখুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

এছাড়াও, প্রসেস করার জন্য আপনি কোনও লোকাল পিডিএফ ফাইল আপলোড করতে পারেন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## Files API ব্যবহার করে PDF আপলোড করা

আমরা সাজেস্ট করি যে আপনি বড় ফাইল বা একাধিক অনুরোধ জুড়ে কোনও
ডকুমেন্ট আবার ব্যবহার করতে চাইলে Files API ব্যবহার করুন। এটি মডেল অনুরোধ থেকে ফাইল আপলোডকে আলাদা করে অনুরোধ লেটেন্সি উন্নত করে এবং
ব্যান্ডউইথ ব্যবহার কমায়।

### URL থেকে বড় পিডিএফ

URL থেকে বড় PDF ফাইল আপলোড ও প্রসেস করার প্রক্রিয়া সহজ করতে File API ব্যবহার করুন:

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

### স্থানীয়ভাবে সেভ করা বড় সাইজের পিডিএফ

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

আপনি যাচাই করতে পারবেন যে API আপলোড করা ফাইলটি সঠিকভাবে সেভ করেছে এবং [`files.get`](https://ai.google.dev/api/rest/v1beta/files/get?hl=bn) কল করে এর
মেটাডেটা পেতে পারবেন। শুধুমাত্র `name`
(এবং এর সাথে সাথে `uri`) অনন্য।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## একাধিক পিডিএফ পাস করা

Gemini API একটি অনুরোধে একাধিক PDF ডকুমেন্ট (সর্বাধিক ১০০০ পৃষ্ঠা) প্রসেস করতে পারে, তবে ডকুমেন্ট ও টেক্সট
প্রম্পটের সম্মিলিত সাইজ মডেলের কন্টেক্সট উইন্ডোর মধ্যে থাকতে হবে।

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

### জাভাস্ক্রিপ্ট

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

### খুলুন

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

## প্রযুক্তিগত বিবরণ

Gemini-তে সর্বাধিক ৫০ এমবি বা ১০০০ পৃষ্ঠা পর্যন্ত পিডিএফ ফাইল কাজ করে। ইনলাইন ডেটা ও Files API আপলোড, দু'টির ক্ষেত্রেই এই সীমা প্রযোজ্য। প্রতিটি ডকুমেন্ট পৃষ্ঠা ২৫৮টি
টোকেনের সমান।

মডেলের [কনটেক্সট উইন্ডো](https://ai.google.dev/gemini-api/docs/long-context?hl=bn) ছাড়া ডকুমেন্টের পিক্সেলের সংখ্যার কোনও নির্দিষ্ট সীমা না থাকলেও, বড় পৃষ্ঠাগুলি তাদের আসল
অ্যাস্পেক্ট রেশিও বজায় রেখে সর্বাধিক ৩০৭২ x ৩০৭২ রেজোলিউশনে স্কেল ডাউন করা হয়, যেখানে ছোট পৃষ্ঠাগুলি ৭৬৮ x ৭৬৮ পিক্সেল পর্যন্ত স্কেল আপ করা হয়। কম সাইজের পৃষ্ঠার জন্য ব্যান্ডউইথ ছাড়া অন্য কোনও খরচ কমানো হয় না অথবা বেশি রেজোলিউশনের পৃষ্ঠার জন্য পারফর্ম্যান্স
উন্নত করা হয় না।

### Gemini 3 মডেল

Gemini 3,
`media_resolution` প্যারামিটারের মাধ্যমে মাল্টিমোডাল ভিশন প্রসেসিংয়ের উপর গ্র্যানুলার কন্ট্রোল প্রদান করে। আপনি এখন প্রতিটি মিডিয়া পার্টের জন্য রেজোলিউশন কম, মাঝারি বা
বেশি হিসেবে সেট করতে পারবেন। এটি যোগ করার ফলে, PDF
ডকুমেন্ট প্রসেস করার পদ্ধতি আপডেট করা হয়েছে:

1. **নেটিভ টেক্সট অন্তর্ভুক্ত করা:** পিডিএফের মধ্যে নেটিভ হিসেবে এম্বেড করা টেক্সট এক্সট্র্যাক্ট করা হয়
   এবং মডেলকে প্রদান করা হয়।
2. **বিলিং ও টোকেন সংক্রান্ত রিপোর্ট:**
   - পিডিএফ থেকে এক্সট্র্যাক্ট করা
     **নেটিভ টেক্সট** থেকে তৈরি টোকেনের জন্য আপনাকে **চার্জ করা হয় না**।
   - API উত্তরের `usage_metadata` বিভাগে, PDF পৃষ্ঠা (ছবি হিসেবে) প্রসেস করে জেনারেট করা টোকেন
     এখন `IMAGE`
     মডালিটির অধীনে গণনা করা হয়, কিছু আগের ভার্সনের মতো আলাদা `DOCUMENT` মডালিটি হিসেবে
     নয়।

মিডিয়া রেজোলিউশন প্যারামিটার সম্পর্কে আরও জানতে, [মিডিয়া রেজোলিউশন](https://ai.google.dev/gemini-api/docs/media-resolution?hl=bn) নির্দেশিকা দেখুন।

### ডকুমেন্টের ধরন

টেকনিক্যালি, আপনি ডকুমেন্ট বোঝার জন্য অন্যান্য MIME টাইপ পাস করতে পারেন, যেমন
TXT, Markdown, HTML, XML ইত্যাদি। তবে, ডকুমেন্ট ভিশন ***শুধুমাত্র অর্থপূর্ণভাবে
PDF বোঝে***। অন্যান্য ধরনের ফাইল থেকে শুধু টেক্সট এক্সট্র্যাক্ট করা হবে এবং মডেল
সেইসব ফাইলের রেন্ডারিংয়ে যা দেখা যায় তা বুঝতে পারবে না। চার্ট, ডায়াগ্রাম, HTML ট্যাগ, মার্কডাউন ফর্ম্যাটিং ইত্যাদি
ফাইল-টাইপ নির্দিষ্ট তথ্য
মুছে যাবে।

অন্যান্য ফাইল ইনপুট পদ্ধতি সম্পর্কে জানতে, [ফাইল ইনপুট পদ্ধতি](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=bn) নির্দেশিকা দেখুন।

### পেশাদার পদ্ধতি

সেরা ফলাফলের জন্য:

- আপলোড করার আগে পৃষ্ঠাগুলি সঠিক ওরিয়েন্টেশনে ঘোরান।
- অস্পষ্ট পৃষ্ঠা এড়িয়ে চলুন।
- একটি পৃষ্ঠা ব্যবহার করলে, পৃষ্ঠার পরে টেক্সট প্রম্পটটি রাখুন।

## এর পরে কী করতে হবে

আরও জানতে, নিম্নলিখিত রিসোর্স দেখুন:

- [ফাইল প্রম্পটিং স্ট্র্যাটেজি](https://ai.google.dev/gemini-api/docs/files?hl=bn#prompt-guide): Gemini API
  টেক্সট, ছবি, অডিও ও ভিডিও ডেটা সহ প্রম্পটিং কাজ করে। এটি
  মাল্টিমোডাল প্রম্পটিং নামেও পরিচিত।
- [সিস্টেম নির্দেশাবলী](https://ai.google.dev/gemini-api/docs/text-generation?hl=bn#system-instructions):
  সিস্টেম নির্দেশাবলী আপনাকে নিজের
  নির্দিষ্ট প্রয়োজন ও ব্যবহারের ক্ষেত্রে মডেলের আচরণ নিয়ন্ত্রণ করতে দেয়।

মতামত জানান

অন্য কিছু উল্লেখ না করা থাকলে, এই পৃষ্ঠার কন্টেন্ট [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)-এর অধীনে এবং কোডের নমুনাগুলি [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)-এর অধীনে লাইসেন্স প্রাপ্ত। আরও জানতে, [Google Developers সাইট নীতি](https://developers.google.com/site-policies?hl=bn) দেখুন। Java হল Oracle এবং/অথবা তার অ্যাফিলিয়েট সংস্থার রেজিস্টার্ড ট্রেডমার্ক।

2026-10-08 UTC-তে শেষবার আপডেট করা হয়েছে।

আমাদের আরও কিছু জানাতে চান?

[[["সহজে বোঝা যায়","easyToUnderstand","thumb-up"],["আমার সমস্যার সমাধান হয়েছে","solvedMyProblem","thumb-up"],["অন্যান্য","otherUp","thumb-up"]],[["এতে আমার প্রয়োজনীয় তথ্য নেই","missingTheInformationINeed","thumb-down"],["খুব জটিল / অনেক ধাপ","tooComplicatedTooManySteps","thumb-down"],["পুরনো","outOfDate","thumb-down"],["অনুবাদ সংক্রান্ত সমস্যা","translationIssue","thumb-down"],["নমুনা / কোড সংক্রান্ত সমস্যা","samplesCodeIssue","thumb-down"],["অন্যান্য","otherDown","thumb-down"]],["2026-10-08 UTC-তে শেষবার আপডেট করা হয়েছে।"],[],[]]
