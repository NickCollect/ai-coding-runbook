---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=fa
fetched_at: 2026-10-19T05:38:46.268890+00:00
title: "\u0631\u0648\u0634\u200c\u0647\u0627\u06cc \u0648\u0631\u0648\u062f\u06cc \u0641\u0627\u06cc\u0644 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# روش‌های ورودی فایل

این راهنما روش‌های مختلفی را که می‌توانید هنگام درخواست از Gemini API فایل‌های رسانه‌ای مثل
تصاویر، صدا، ویدیو، و اسناد را اضافه کنید توضیح می‌دهد.
روش‌های جدید در همه نقاط پایانی «میانای برنامه‌سازی کاربردی Gemini»، ازجمله
میانای برنامه‌سازی کاربردی «دسته‌ای»، «تعامل‌ها»، و «زنده» پشتیبانی می‌شوند.
انتخاب روش صحیح به اندازه فایل، محل ذخیره داده‌ها، و تعداد دفعاتی که قصد دارید از فایل استفاده کنید بستگی دارد.

ساده‌ترین راه برای افزودن فایل به‌عنوان ورودی این است که فایل محلی را بخوانید و آن را در پیام‌واره بگنجانید. مثال زیر نحوه خواندن فایل PDF محلی را نشان می‌دهد. فایل‌های PDF برای این روش محدود به ۵۰ مگابایت است. برای فهرست کامل انواع ورودی فایل و محدودیت‌ها،
[جدول مقایسه روش ورودی](#method-comparison) را ببینید.

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

### جاوا

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

### رفتن

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

## مقایسه روش ورودی

جدول زیر هر روش ورودی را با محدودیت‌های فایل و موارد استفاده بهینه مقایسه می‌کند. توجه داشته باشید که محدودیت اندازه فایل ممکن است بسته به نوع فایل و مدل یا نشانه‌گذاری استفاده‌شده برای پردازش فایل متفاوت باشد.

| روش | بهترین برای | حداکثر اندازه فایل | ماندگاری |
| --- | --- | --- | --- |
| **داده‌های درون‌خطی** | آزمایش سریع، فایل‌های کوچک، برنامه‌های بلادرنگ. | ‫۱۰۰ مگابایت در هر درخواست یا داده‌بار   (**۵۰ مگابایت برای فایل‌های PDF**) | هیچ‌کدام (با هر درخواست ارسال می‌شود) |
| **بارگذاری File API** | فایل‌های بزرگ، فایل‌هایی که چندین بار استفاده شده‌اند. | ۲ گیگابایت برای هر فایل،   تا ۲۰ گیگابایت برای هر پروژه | ‫۴۸ ساعت |
| **ثبت نشانی وب یکنواخت GCS میانای برنامه‌سازی کاربردی فایل** | فایل‌های بزرگی که ازقبل در Google Cloud Storage هستند، فایل‌هایی که چندین بار استفاده شده‌اند. | ۲ گیگابایت برای هر فایل، بدون محدودیت کلی فضای ذخیره‌سازی | هیچ‌کدام (براساس درخواست واکشی می‌شود). ثبت‌نام یک‌باره می‌تواند تا ۳۰ روز دسترسی بدهد. |
| **نشانی‌های وب خارجی** | داده‌های عمومی یا داده‌های موجود در دسته‌های ابری (AWS،‏ Azure،‏ GCS) بدون بارگذاری مجدد. | ‫۱۵ مگابایت برای هر فایل | هیچ‌کدام (براساس درخواست واکشی شد) |

## داده‌های به‌خط

برای فایل‌های کوچک‌تر (کمتر از ۱۰۰ مگابایت، یا ۵۰ مگابایت برای فایل‌های PDF)، می‌توانید داده‌ها را
مستقیماً در محتوای درخواست بگذرانید. این ساده‌ترین روش برای آزمون‌های سریع یا
برنامه‌هایی است که داده‌های گذرا و هم‌زمان را مدیریت می‌کنند. می‌توانید داده‌ها را به‌صورت
رشته‌های کدبندی‌شده base64 ارائه دهید یا فایل‌های محلی را مستقیماً بخوانید.

برای نمونه‌ای از خواندن از فایل محلی، نمونه ابتدای
این صفحه را ببینید.

### واکشی از نشانی وب

همچنین می‌توانید فایلی را از نشانی وب واکشی کنید، آن را به بایت تبدیل کنید، و در
ورودی بگنجانید.

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

### جاوا

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

### رفتن

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

## Gemini File API

«میانای برنامه‌سازی کاربردی فایل» برای فایل‌های بزرگ‌تر (تا ۲ گیگابایت) یا فایل‌هایی که قصد دارید در چندین درخواست استفاده کنید طراحی شده است.

### بارگذاری فایل استاندارد

فایل محلی را در «میانای برنامه‌سازی کاربردی Gemini» بارگذاری کنید. فایل‌هایی که به این روش بارگذاری می‌شوند به‌طور موقت (۴۸ ساعت) ذخیره می‌شوند و برای بازیابی کارآمد توسط مدل پردازش می‌شوند.

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

### جاوا

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

### رفتن

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

### ثبت فایل‌های Google Cloud Storage

اگر داده‌هایتان ازقبل در Google Cloud Storage است، نیازی نیست آن را
بارگیری و دوباره بارگذاری کنید. می‌توانید آن را مستقیماً در «میانای برنامه‌سازی کاربردی فایل» ثبت کنید.

1. دسترسی **عامل سرویس** را به هر مخزن اعطا کنید

   1. «میانای برنامه‌سازی کاربردی Gemini» را در پروژه Google Cloud خود فعال کنید.
   2. ایجاد «عامل خدمات»:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **اجازه‌های «عامل سرویس API Gemini» را** برای خواندن
      فضای ذخیره‌سازی اعطا کنید.

      کاربر باید `Storage Object Viewer`
      [نقش IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=fa#storage.objectViewer)
      را به این عامل سرویس در باکت‌های ذخیره‌سازی خاصی که قصد دارد استفاده کند اختصاص دهد.

   این دسترسی به‌طور پیش‌فرض منقضی نمی‌شود، اما در هر زمانی قابل تغییر است. همچنین می‌توانید از دستورات
   [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=fa)
   برای اعطای اجازه‌ها استفاده کنید.
2. اصالت‌سنجی سرویس

   **پیش‌نیازها**

   - فعال کردن API
   - حساب خدمات یا کارگزاری با مجوزهای مناسب ایجاد کنید.

   ابتدا باید به‌عنوان سرویسی که مجوزهای
   بیننده شیء فضای ذخیره‌سازی دارد اصالت‌سنجی کنید. نحوه انجام این کار به محیطی که کد مدیریت فایل شما در آن اجرا می‌شود بستگی دارد.

   **خارج از Google Cloud**

   اگر کدتان از خارج Google Cloud اجرا می‌شود، مثلاً از رایانه،
   اطلاعات اعتباری حساب را با مراحل زیر از «کنسول Google Cloud» بارگیری کنید:

   1. به [کنسول حساب سرویس](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=fa) مرور کنید
   2. حساب سرویس مربوطه را انتخاب کنید
   3. برگه **کلیدها** را انتخاب کنید و **افزودن کلید، ایجاد کلید جدید** را انتخاب کنید
   4. نوع کلید **JSON** را انتخاب کنید و توجه داشته باشید که فایل در کجا در دستگاهتان بارگیری شده است.

   برای جزئیات بیشتر، به اسناد رسمی Google Cloud درباره
   [مدیریت کلید حساب سرویس](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=fa) مراجعه کنید.

   سپس از فرمان‌های زیر برای اصالت‌سنجی استفاده کنید. این فرمان‌ها فرض می‌کنند فایل حساب خدمات شما در
   دایرکتوری کنونی قرار دارد و نام آن `service-account.json` است.

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

   ### جاوا اسکریپت

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

   **در Google Cloud**

   اگر مستقیماً در Google Cloud اجرا می‌کنید، برای مثال بااستفاده از [توابع Cloud Run](https://cloud.google.com/functions?hl=fa) یا
   [نمونه Compute Engine](https://cloud.google.com/products/compute?hl=fa)، اطلاعات اعتباری ضمنی خواهید داشت اما برای اعطای دامنه‌های مناسب باید دوباره اصالت‌سنجی کنید.

   ### Python

   این کد انتظار دارد که سرویس در محیطی اجرا شود که در آن
   [اطلاعات اعتباری پیش‌فرض برنامه](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=fa)
   را بتوان به‌طور خودکار دریافت کرد، مثل Cloud Run یا Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   این کد انتظار دارد که سرویس در محیطی اجرا شود که در آن
   [اطلاعات اعتباری پیش‌فرض برنامه](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=fa)
   را بتوان به‌طور خودکار دریافت کرد، مثل Cloud Run یا Compute Engine.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

### جاوا

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

### رفتن

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

این یک فرمان تعاملی است. برای سرویس‌هایی مثل Compute Engine می‌توانید محدوده‌ها را در سطح پیکربندی به سرویس درحال اجرا پیوست کنید. برای مثال، [اسناد سرویس مدیریت‌شده توسط کاربر](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=fa#using)
را ببینید.

```
gcloud auth application-default login \
--scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
```

1. ثبت فایل (میانای برنامه‌سازی کاربردی Files)
   از میانای برنامه‌سازی کاربردی Files برای ثبت فایل‌ها و تولید مسیر میانای برنامه‌سازی کاربردی Files استفاده کنید که می‌تواند
   مستقیماً در «میانای برنامه‌سازی کاربردی Gemini» استفاده شود.

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

### جاوا

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

### رفتن

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

## HTTP خارجی / نشانی‌های وب امضاشده

می‌توانید نشانی‌های وب HTTPS دردسترس عموم یا نشانی‌های وب پیش‌امضاشده را مستقیماً در
درخواستتان بگذرانید. ‫Gemini API محتوا را درطول پردازش به‌طور ایمن واکشی می‌کند.
این برای فایل‌هایی که نمی‌خواهید دوباره بارگذاری کنید ایده‌آل است. هر فایل می‌تواند تا ۱۵ مگابایت باشد. برای فایل‌های بزرگ‌تر، از [File API](#file-api) استفاده کنید.

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

### جاوا اسکریپت

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

### دسترس‌پذیری

تأیید کنید که نشانی‌های وبی که ارائه می‌کنید به صفحه‌هایی که نیاز به ورود به سیستم دارند یا
پشت دیوار پرداخت هستند منتهی نمی‌شوند. برای پایگاه‌های داده خصوصی، مطمئن شوید نشانی وب امضاشده‌ای با اجازه‌های دسترسی و انقضای صحیح ایجاد کنید.

### بررسی‌های ایمنی

سیستم بررسی محتوای نشانی وب را انجام می‌دهد تا تأیید کند که با استانداردهای ایمنی و خط‌مشی مطابقت دارد. اگر نشانی وب در این بررسی ناموفق باشد،
`url_retrieval_status` از `URL_RETRIEVAL_STATUS_UNSAFE` دریافت خواهید کرد.

### انواع محتوای پشتیبانی‌شده

این فهرست از انواع فایل پشتیبانی‌شده و محدودیت‌ها به‌عنوان راهنمایی اولیه درنظر گرفته شده است و جامع نیست. مجموعه مؤثر انواع پشتیبانی‌شده ممکن است تغییر کند و براساس مدل خاص و نسخه نشانه‌گذار درحال استفاده متفاوت باشد. انواع پشتیبانی‌نشده منجر به خطا می‌شود.
علاوه‌براین، واکشی محتوا برای این نوع فایل‌ها فقط از نشانی‌های وب دردسترس عمومی پشتیبانی می‌کند.

#### انواع فایل نوشتاری

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### انواع فایل برنامه

- `application/json`
- `application/pdf`

#### انواع فایل تصویری

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### انواع فایل ویدیو

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## روال‌های مطلوب

- **روش صحیح را انتخاب کنید:** برای فایل‌های کوچک و موقت از داده‌های درون‌خطی استفاده کنید.
  برای فایل‌های بزرگ‌تر یا فایل‌هایی که اغلب استفاده می‌شوند، از «میانای برنامه‌سازی کاربردی فایل» استفاده کنید. از نشانی‌های وب خارجی
  برای داده‌هایی که قبلاً به‌صورت آنلاین میزبانی شده‌اند استفاده کنید.
- **مشخص کردن انواع MIME:** همیشه نوع MIME صحیح را برای داده‌های فایل ارائه دهید تا پردازش به‌درستی انجام شود.
- **مدیریت خطاها:** مدیریت خطا را در کد خود پیاده‌سازی کنید تا مشکلات احتمالی مانند خرابی شبکه، مشکلات دسترسی به فایل، یا خطاهای API را مدیریت کنید.

## محدودیت‌ها

- محدودیت‌های اندازه فایل براساس روش (به [جدول مقایسه](#method-comparison) مراجعه کنید)
  و نوع فایل متفاوت است.
- داده‌های درون‌خطی اندازه پایه‌بار درخواست را افزایش می‌دهد.
- بارگذاری‌های «میانای برنامه‌سازی کاربردی فایل» موقتی هستند و پس‌از ۴۸ ساعت منقضی می‌شوند.
- واکشی نشانی وب خارجی به ۱۵ مگابایت در هر فایل محدود است و از انواع محتوای خاصی پشتیبانی می‌کند.

## قدم بعدی چیست

- بااستفاده از [Google AI Studio](http://aistudio.google.com/?hl=fa)، پیام‌واره‌های چندوجهی خودتان را بنویسید.
- برای کسب اطلاعات درباره افزودن فایل به پیام‌واره‌هایتان، راهنمای
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=fa)،
  [صوت](https://ai.google.dev/gemini-api/docs/audio?hl=fa)، و
  [پردازش سند](https://ai.google.dev/gemini-api/docs/document-processing?hl=fa)
  را ببینید.

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-07 به‌وقت ساعت هماهنگ جهانی."],[],[]]
