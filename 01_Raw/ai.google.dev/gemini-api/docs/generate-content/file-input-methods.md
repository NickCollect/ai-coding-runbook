---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/file-input-methods?hl=vi
fetched_at: 2026-07-06T05:13:00.359071+00:00
title: "Ph\u01b0\u01a1ng th\u1ee9c nh\u1eadp t\u1ec7p \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Phương thức nhập tệp

Hướng dẫn này giải thích các cách để bạn có thể đưa tệp nội dung nghe nhìn (chẳng hạn như hình ảnh, âm thanh, video và tài liệu) vào khi gửi yêu cầu đến Gemini API.
Các phương thức mới được hỗ trợ trong tất cả các điểm cuối của Gemini API, bao gồm cả
API Hàng loạt, Tương tác và API Trực tiếp.
Việc chọn phương thức phù hợp phụ thuộc vào kích thước tệp, vị trí hiện tại của dữ liệu và tần suất bạn dự định sử dụng tệp.

Cách đơn giản nhất để đưa tệp vào làm dữ liệu đầu vào là đọc tệp cục bộ và đưa tệp đó vào lời nhắc. Ví dụ sau đây cho biết cách đọc tệp PDF cục bộ. Đối với phương thức này, tệp PDF chỉ được có kích thước tối đa là 50 MB. Hãy xem
[bảng so sánh phương thức nhập](#method-comparison) để biết danh sách đầy đủ các loại và giới hạn của tệp
đầu vào.

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

## So sánh phương thức nhập

Bảng sau đây so sánh từng phương thức nhập với giới hạn tệp và các trường hợp sử dụng phù hợp nhất. Xin lưu ý rằng giới hạn kích thước tệp có thể khác nhau tuỳ thuộc vào loại tệp và mô hình/trình mã hoá mã thông báo được dùng để xử lý tệp.

| Phương thức | Phù hợp nhất cho | Kích thước tệp tối đa | Khả năng lưu trữ dài lâu |
| --- | --- | --- | --- |
| **Dữ liệu cùng dòng** | Thử nghiệm nhanh, tệp nhỏ, ứng dụng theo thời gian thực. | 100 MB cho mỗi yêu cầu/tải trọng   (**50 MB đối với tệp PDF**) | Không có (được gửi kèm theo mọi yêu cầu) |
| **Tải tệp lên bằng File API** | Tệp lớn, tệp được dùng nhiều lần. | 2 GB cho mỗi tệp,   tối đa 20 GB cho mỗi dự án | 48 giờ |
| **Đăng ký URI GCS bằng File API** | Tệp lớn đã có trong Google Cloud Storage, tệp được dùng nhiều lần. | 2 GB cho mỗi tệp, không có giới hạn dung lượng lưu trữ tổng thể | Không có (được tìm nạp theo yêu cầu). Bạn có thể đăng ký một lần để có quyền truy cập trong tối đa 30 ngày. |
| **URL bên ngoài** | Dữ liệu công khai hoặc dữ liệu trong các bộ chứa đám mây (AWS, Azure, GCS) mà không cần tải lại. | 100 MB cho mỗi yêu cầu/tải trọng | Không có (được tìm nạp theo yêu cầu) |

## Dữ liệu cùng dòng

Đối với các tệp nhỏ hơn (dưới 100 MB hoặc 50 MB đối với tệp PDF), bạn có thể truyền trực tiếp dữ liệu trong tải trọng yêu cầu. Đây là phương thức đơn giản nhất để thử nghiệm nhanh hoặc các ứng dụng xử lý dữ liệu tạm thời theo thời gian thực. Bạn có thể cung cấp dữ liệu dưới dạng chuỗi được mã hoá base64 hoặc bằng cách đọc trực tiếp các tệp cục bộ.

Để biết ví dụ về cách đọc từ tệp cục bộ, hãy xem ví dụ ở đầu trang này.

### Tìm nạp từ URL

Bạn cũng có thể tìm nạp tệp từ URL, chuyển đổi tệp đó thành byte và đưa tệp đó vào dữ liệu đầu vào.

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

## Gemini File API

File API được thiết kế cho các tệp lớn hơn (tối đa 2 GB) hoặc các tệp mà bạn dự định dùng trong nhiều yêu cầu.

### Tải tệp lên theo cách tiêu chuẩn

Tải tệp cục bộ lên Gemini API. Các tệp được tải lên theo cách này sẽ được lưu trữ tạm thời (48 giờ) và được xử lý để mô hình có thể truy xuất hiệu quả.

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

### Đăng ký tệp Google Cloud Storage

Nếu dữ liệu của bạn đã có trong Google Cloud Storage, thì bạn không cần tải xuống và tải lại. Bạn có thể đăng ký trực tiếp bằng File API.

1. Cấp quyền truy cập **Tác nhân dịch vụ** vào từng bộ chứa

   1. Bật Gemini API trong dự án trên đám mây của bạn.
   2. Tạo Tác nhân dịch vụ:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. **Cấp quyền cho Tác nhân dịch vụ Gemini API** để đọc các bộ chứa lưu trữ của bạn.

      Người dùng cần chỉ định `Storage Object Viewer`
      [vai trò IAM](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=vi#storage.objectViewer)
      cho tác nhân dịch vụ này trên các bộ chứa lưu trữ cụ thể mà họ dự định sử dụng.

   Theo mặc định, quyền truy cập này không hết hạn, nhưng bạn có thể thay đổi bất cứ lúc nào. [Bạn cũng có thể sử dụng các lệnh SDK IAM của Google Cloud Storage để cấp quyền.](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=vi)
2. Xác thực dịch vụ của bạn

   **Điều kiện tiên quyết**

   - Bật API
   - Tạo tài khoản/tác nhân dịch vụ có các quyền thích hợp.

   Trước tiên, bạn cần xác thực với tư cách là dịch vụ có quyền xem đối tượng lưu trữ. Cách thức này phụ thuộc vào môi trường mà mã quản lý tệp của bạn sẽ chạy.

   **Bên ngoài Google Cloud**

   Nếu mã của bạn đang chạy bên ngoài Google Cloud (chẳng hạn như trên máy tính của bạn), hãy tải thông tin đăng nhập tài khoản xuống từ Google Cloud Console theo các bước sau:

   1. Duyệt đến bảng điều khiển [Tài khoản dịch vụ](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=vi)
   2. Chọn tài khoản dịch vụ có liên quan
   3. Chọn thẻ **Khoá** rồi chọn **Thêm khoá, Tạo khoá mới**
   4. Chọn loại khoá **JSON** và lưu ý vị trí tải tệp xuống trên máy của bạn.

   Để biết thêm thông tin chi tiết, hãy xem tài liệu chính thức của Google Cloud về việc [quản lý khoá tài khoản dịch vụ](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=vi).

   Sau đó, hãy sử dụng các lệnh sau để xác thực. Các lệnh này giả định rằng tệp tài khoản dịch vụ của bạn nằm trong thư mục hiện tại, có tên là `service-account.json`.

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

   ### Javascript

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

   **Trên Google Cloud**

   Nếu bạn đang chạy trực tiếp trong Google Cloud (ví dụ: bằng cách sử dụng [Cloud
   Run functions](https://cloud.google.com/functions?hl=vi) hoặc
   [phiên bản Compute Engine](https://cloud.google.com/products/compute?hl=vi)), bạn sẽ
   có thông tin đăng nhập ngầm ẩn nhưng cần xác thực lại để cấp các
   phạm vi thích hợp.

   ### Python

   Mã này giả định rằng dịch vụ đang chạy trong một môi trường mà
   [Thông tin xác thực mặc định của ứng dụng](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=vi)
   có thể được tự động lấy, chẳng hạn như Cloud Run hoặc Compute Engine.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Mã này giả định rằng dịch vụ đang chạy trong một môi trường mà
   [Thông tin xác thực mặc định của ứng dụng](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=vi)
   có thể được tự động lấy, chẳng hạn như Cloud Run hoặc Compute Engine.

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

   Đây là một lệnh tương tác. Đối với các dịch vụ như Compute Engine, bạn có thể đính kèm các phạm vi vào dịch vụ đang chạy ở cấp cấu hình. [Hãy xem tài liệu về dịch vụ do người dùng quản lý để biết ví dụ.](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=vi#using)

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Đăng ký tệp (Files API)

   Sử dụng Files API để đăng ký tệp và tạo đường dẫn Files API có thể được dùng trực tiếp trong Gemini API.

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

## URL HTTP / URL đã ký bên ngoài

Bạn có thể truyền trực tiếp các URL HTTPS có thể truy cập công khai hoặc URL đã ký trước (tương thích với
[URL đã ký trước S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html)
và SAS Azure) trong yêu cầu tạo của mình. Gemini API sẽ tìm nạp nội dung một cách an toàn trong quá trình xử lý. Đây là lựa chọn lý tưởng cho các tệp có kích thước tối đa 100 MB mà bạn không muốn tải lại.

Bạn có thể sử dụng URL công khai hoặc URL đã ký làm dữ liệu đầu vào bằng cách sử dụng các URL trong trường `file_uri`.

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

### Javascript

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

### Hỗ trợ tiếp cận

Xác minh rằng các URL bạn cung cấp không dẫn đến các trang yêu cầu đăng nhập hoặc nằm sau tường phí. Đối với cơ sở dữ liệu riêng tư, hãy đảm bảo bạn tạo URL đã ký có quyền truy cập và thời gian hết hạn chính xác.

### Kiểm tra an toàn

Hệ thống sẽ kiểm tra việc kiểm duyệt nội dung trên URL để xác nhận rằng các URL đó đáp ứng các tiêu chuẩn về an toàn và chính sách (ví dụ: nội dung không chọn không tham gia và nội dung có tường phí). Nếu URL bạn cung cấp không vượt qua bước kiểm tra này, bạn sẽ nhận được `url_retrieval_status` là `URL_RETRIEVAL_STATUS_UNSAFE`.

### Các loại nội dung được hỗ trợ

Danh sách các loại tệp và giới hạn được hỗ trợ này chỉ nhằm mục đích hướng dẫn ban đầu và không đầy đủ. Tập hợp các loại được hỗ trợ có hiệu lực có thể thay đổi và có thể khác nhau tuỳ thuộc vào mô hình và phiên bản trình mã hoá mã thông báo cụ thể đang được sử dụng. Các loại không được hỗ trợ sẽ gây ra lỗi.
Ngoài ra, tính năng truy xuất nội dung cho các loại tệp này hiện chỉ hỗ trợ các URL có thể truy cập công khai.

#### Các loại tệp văn bản

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Các loại tệp ứng dụng

- `application/json`
- `application/pdf`

#### Các loại tệp hình ảnh

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Các loại tệp video

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Các phương pháp hay nhất

- **Chọn phương thức phù hợp:** Sử dụng dữ liệu cùng dòng cho các tệp nhỏ, tạm thời.
  Sử dụng File API cho các tệp lớn hơn hoặc thường dùng. Sử dụng URL bên ngoài cho dữ liệu đã được lưu trữ trực tuyến.
- **Chỉ định loại MIME:** Luôn cung cấp loại MIME chính xác cho dữ liệu tệp để đảm bảo quá trình xử lý diễn ra đúng cách.
- **Xử lý lỗi:** Triển khai tính năng xử lý lỗi trong mã của bạn để quản lý các vấn đề tiềm ẩn như lỗi mạng, vấn đề về quyền truy cập vào tệp hoặc lỗi API.
- **Quản lý quyền GCS:** Khi sử dụng tính năng đăng ký GCS, chỉ cấp cho Tác nhân dịch vụ Gemini API vai trò `Storage Object Viewer` cần thiết trên các bộ chứa cụ thể.
- **Bảo mật URL đã ký:** Đảm bảo URL đã ký có thời gian hết hạn thích hợp và các quyền bị hạn chế.

## Các điểm hạn chế

- Giới hạn kích thước tệp khác nhau tuỳ theo phương thức (xem [bảng so sánh](#method-comparison))
  và loại tệp.
- Dữ liệu cùng dòng làm tăng kích thước tải trọng yêu cầu.
- Các tệp tải lên bằng File API là tạm thời và hết hạn sau 48 giờ.
- Tính năng tìm nạp URL bên ngoài bị giới hạn ở mức 100 MB cho mỗi tải trọng và hỗ trợ các loại nội dung cụ thể.
- Tính năng đăng ký Google Cloud Storage yêu cầu thiết lập IAM đúng cách và quản lý mã thông báo OAuth.

## Bước tiếp theo

- Hãy thử viết lời nhắc đa phương thức của riêng bạn bằng
  [Google AI Studio](http://aistudio.google.com/?hl=vi).
- Để biết thông tin về cách đưa tệp vào lời nhắc, hãy xem hướng dẫn
  [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=vi),
  [âm thanh](https://ai.google.dev/gemini-api/docs/audio?hl=vi) và
  [tài liệu](https://ai.google.dev/gemini-api/docs/document-processing?hl=vi).
- Để biết thêm hướng dẫn về thiết kế lời nhắc, chẳng hạn như điều chỉnh các tham số lấy mẫu, hãy xem hướng dẫn về
  [Chiến lược lời nhắc](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=vi).

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-06-23 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-06-23 UTC."],[],[]]
