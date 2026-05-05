---
source_url: https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr
fetched_at: 2026-05-05T20:06:22.164832+00:00
title: "Dosya giri\u015f y\u00f6ntemleri \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Dosya giriş yöntemleri

Bu kılavuzda, Gemini API'ye istek gönderirken resim, ses, video ve doküman gibi medya dosyalarını eklemenin farklı yolları açıklanmaktadır.
Yeni yöntemler, Batch, Interactions ve Live API dahil olmak üzere tüm Gemini API uç noktalarında desteklenir.
Doğru yöntemi seçmek; dosyanızın boyutuna, verilerinizin şu anda nerede depolandığına ve dosyayı ne sıklıkta kullanmayı planladığınıza bağlıdır.

Giriş olarak dosya eklemenin en basit yolu, yerel bir dosyayı okuyup isteme dahil etmektir. Aşağıdaki örnekte, yerel bir PDF dosyasının nasıl okunacağı gösterilmektedir. Bu yöntemde PDF'ler 50 MB ile sınırlıdır. Dosya giriş türlerinin ve sınırlarının tam listesi için [Giriş yöntemi karşılaştırma tablosu](#method-comparison)'na bakın.

### Python

```
from google import genai
from google.genai import types
import pathlib

client = genai.Client()

filepath = pathlib.Path('my_local_file.pdf')

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-3-flash-preview",
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
        model: "gemini-3-flash-preview",
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

curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

## Giriş yöntemi karşılaştırması

Aşağıdaki tabloda, her giriş yöntemi dosya sınırları ve en iyi kullanım alanlarıyla karşılaştırılmaktadır. Dosya boyutu sınırının, dosya türüne ve dosyayı işlemek için kullanılan modele/tokenleştiriciye bağlı olarak değişebileceğini unutmayın.

| Yöntem | En uygun olduğu durumlar | Maksimum dosya boyutu | Kalıcılık |
| --- | --- | --- | --- |
| **Satır içi veriler** | Hızlı test, küçük dosyalar, gerçek zamanlı uygulamalar. | İstek/yük başına 100 MB   (**PDF'ler için 50 MB**) | Yok (her istekle birlikte gönderilir) |
| **Dosya API'si yükleme** | Büyük dosyalar, birden fazla kez kullanılan dosyalar | Dosya başına 2 GB,   proje başına en fazla 20 GB | 48 Saat |
| **File API GCS URI kaydı** | Google Cloud Storage'da bulunan büyük dosyalar, birden çok kez kullanılan dosyalar. | Dosya başına 2 GB, genel depolama alanı sınırı yoktur. | Yok (istek başına getirilir). Tek seferlik kayıt, 30 güne kadar erişim sağlayabilir. |
| **Harici URL'ler** | Herkese açık veriler veya bulut paketlerindeki (AWS, Azure, GCS) veriler yeniden yüklenmeden. | İstek/yük başına 100 MB | Yok (istek başına getirilir) |

## Satır içi veriler

Daha küçük dosyalar (100 MB'tan küçük veya PDF'ler için 50 MB'tan küçük) için verileri doğrudan istek yükünde iletebilirsiniz. Bu, hızlı testler veya gerçek zamanlı, geçici verileri işleyen uygulamalar için en basit yöntemdir. Verileri base64 olarak kodlanmış dizeler şeklinde veya doğrudan yerel dosyaları okuyarak sağlayabilirsiniz.

Yerel bir dosyadan okuma örneği için bu sayfanın başındaki örneğe bakın.

### URL'den getirme

Ayrıca bir URL'den dosya getirebilir, bunu baytlara dönüştürebilir ve girişe ekleyebilirsiniz.

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
  model="gemini-3-flash-preview",
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
        model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

File API, daha büyük dosyalar (2 GB'a kadar) veya birden fazla istekte kullanmayı planladığınız dosyalar için tasarlanmıştır.

### Standart dosya yükleme

Gemini API'ye yerel bir dosya yükleyin. Bu şekilde yüklenen dosyalar geçici olarak (48 saat) depolanır ve model tarafından verimli bir şekilde alınabilmesi için işlenir.

### Python

```
from google import genai
client = genai.Client()

# Upload the file
audio_file = client.files.upload(file="path/to/your/sample.mp3")
prompt = "Describe this audio clip"

# Use the uploaded file in a prompt
response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: "gemini-3-flash-preview",
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
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

### Google Cloud Storage dosyalarını kaydetme

Verileriniz zaten Google Cloud Storage'da ise indirip yeniden yüklemeniz gerekmez. Bunu doğrudan File API ile kaydedebilirsiniz.

1. Her bir pakete **hizmet aracısı** erişimi verin.

   1. Google Cloud projenizde Gemini API'yi etkinleştirin.
   2. Hizmet aracısını oluşturun:

      `gcloud beta services identity create --service=generativelanguage.googleapis.com --project=<your_project>`
   3. Depolama paketlerinizi okumak için **Gemini API hizmet aracısına izin verin**.

      Kullanıcının, kullanmayı planladığı belirli depolama paketlerinde bu hizmet aracısına `Storage Object Viewer`
      [IAM rolü](https://docs.cloud.google.com/storage/docs/access-control/iam-roles?hl=tr#storage.objectViewer)
      atması gerekir.

   Bu erişim varsayılan olarak sona ermez ancak istediğiniz zaman değiştirilebilir. İzin vermek için [Google Cloud Storage IAM SDK](https://cloud.google.com/iam/docs/write-policy-client-libraries?hl=tr) komutlarını da kullanabilirsiniz.
2. Hizmetinizin kimliğini doğrulama

   **Ön koşullar**

   - API'yi Etkinleştir
   - Uygun izinlere sahip bir hizmet hesabı/aracı oluşturun.

   Öncelikle, depolama nesnesi görüntüleyici izinlerine sahip hizmet olarak kimliğinizi doğrulamanız gerekir. Bu işlemin nasıl gerçekleşeceği, dosya yönetimi kodunuzun çalışacağı ortama bağlıdır.

   **Google Cloud dışında**

   Kodunuz Google Cloud'un dışından (ör. masaüstünüzden) çalışıyorsa aşağıdaki adımları uygulayarak Google Cloud Console'dan hesap kimlik bilgilerini indirin:

   1. [Hizmet hesabı konsoluna](https://console.cloud.google.com/iam-admin/serviceaccounts?hl=tr) gidin.
   2. İlgili hizmet hesabını seçin.
   3. **Anahtarlar** sekmesini seçin ve **Anahtar ekle, Yeni anahtar oluştur**'u seçin.
   4. **JSON** anahtar türünü seçin ve dosyanın makinenizde nereye indirildiğini not edin.

   Daha fazla bilgi için [hizmet hesabı anahtarı yönetimi](https://docs.cloud.google.com/iam/docs/keys-create-delete?hl=tr) ile ilgili resmi Google Cloud belgelerine bakın.

   Ardından, kimlik doğrulaması yapmak için aşağıdaki komutları kullanın. Bu komutlar, hizmet hesabı dosyanızın geçerli dizinde olduğunu ve `service-account.json` olarak adlandırıldığını varsayar.

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

   ### KSA

   ```
   gcloud auth application-default login \
     --client-id-file=service-account.json \
     --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only'
   ```

   **Google Cloud'da**

   Doğrudan Google Cloud'da çalışıyorsanız (ör. [Cloud Run işlevlerini](https://cloud.google.com/functions?hl=tr) veya [Compute Engine örneğini](https://cloud.google.com/products/compute?hl=tr) kullanarak) örtülü kimlik bilgileriniz olur ancak uygun kapsamları vermek için yeniden kimlik doğrulamanız gerekir.

   ### Python

   Bu kod, hizmetin Cloud Run veya Compute Engine gibi [Uygulama Varsayılan Kimlik Bilgileri](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=tr)'nın otomatik olarak alınabileceği bir ortamda çalışmasını bekler.

   ```
   import google.auth

   GCS_READ_SCOPES = [       
     'https://www.googleapis.com/auth/devstorage.read_only',
     'https://www.googleapis.com/auth/cloud-platform'
   ]

   credentials, project = google.auth.default(scopes=GCS_READ_SCOPES)
   ```

   ### JavaScript

   Bu kod, hizmetin Cloud Run veya Compute Engine gibi [Uygulama Varsayılan Kimlik Bilgileri](https://docs.cloud.google.com/docs/authentication/application-default-credentials?hl=tr)'nın otomatik olarak alınabileceği bir ortamda çalışmasını bekler.

   ```
   const { GoogleAuth } = require('google-auth-library');

   const auth = new GoogleAuth({
     scopes: [
       'https://www.googleapis.com/auth/devstorage.read_only',
       'https://www.googleapis.com/auth/cloud-platform'
     ]
   });
   ```

   ### KSA

   Bu, etkileşimli bir komuttur. Compute Engine gibi hizmetlerde, yapılandırma düzeyinde çalışan hizmete kapsamlar ekleyebilirsiniz. Örnek için [user-managed service
   docs](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances?hl=tr#using)
   başlıklı makaleye göz atın.

   ```
   gcloud auth application-default login \
   --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/devstorage.read_only"
   ```
3. Dosya kaydı (Files API)

   Dosyaları kaydetmek ve doğrudan Gemini API'de kullanılabilecek bir Files API yolu oluşturmak için Files API'yi kullanın.

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
       model="gemini-3-flash-preview",
       contents=[Part.from_uri(
         file_uri=f.uri,
         mime_type=f.mime_type,
       ),
       prompt],
     )
     print(response.text)
   ```

   ### KSA

   ```
   access_token=$(gcloud auth application-default print-access-token)
   project_id=$(gcloud config get-value project)
   curl -X POST https://generativelanguage.googleapis.com/v1beta/files:register \
       -H 'Content-Type: application/json' \
       -H "Authorization: Bearer ${access_token}" \
       -H "x-goog-user-project: ${project_id}" \
       -d '{"uris": ["gs://bucket/object1", "gs://bucket/object2"]}'
   ```

## Harici HTTP / İmzalı URL'ler

Herkese açık HTTPS URL'lerini veya önceden imzalanmış URL'leri ([S3 Presigned URL'leri](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) ve Azure SAS ile uyumlu) doğrudan oluşturma isteğinize iletebilirsiniz. Gemini API, işleme sırasında içeriği güvenli bir şekilde getirir. Bu yöntem, yeniden yüklemek istemediğiniz 100 MB'a kadar olan dosyalar için idealdir.

`file_uri` alanındaki URL'leri kullanarak giriş olarak herkese açık veya imzalı URL'leri kullanabilirsiniz.

### Python

```
from google import genai
from google.genai.types import Part

uri = "https://ontheline.trincoll.edu/images/bookdown/sample-local-pdf.pdf"
prompt = "Summarize this file"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
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
    model: 'gemini-3-flash-preview',
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent \
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

### Erişilebilirlik

Sağladığınız URL'lerin giriş gerektiren veya ödeme duvarının arkasında olan sayfalara yönlendirmediğini doğrulayın. Özel veritabanları için doğru erişim izinleri ve geçerlilik süresiyle imzalı bir URL oluşturduğunuzdan emin olun.

### Güvenlik kontrolleri

Sistem, URL'de içerik denetimi yaparak güvenlik ve politika standartlarını (ör. kapsam dışında bırakılmamış ve ödeme duvarı olan içerik) karşıladığını onaylar. Belirttiğiniz URL bu kontrolü geçemezse `url_retrieval_status` `URL_RETRIEVAL_STATUS_UNSAFE` hatası alırsınız.

### Desteklenen içerik türleri

Desteklenen dosya türleri ve sınırlamalarla ilgili bu liste, başlangıçta yol göstermek amacıyla hazırlanmıştır ve kapsamlı değildir. Desteklenen türlerin etkili kümesi değişebilir ve kullanılan modele ve belirteç ayrıştırıcı sürümüne göre farklılık gösterebilir. Desteklenmeyen türler hataya neden olur.
Ayrıca, bu dosya türleri için içerik alma işlemi şu anda yalnızca herkese açık URL'leri desteklemektedir.

#### Metin dosyası türleri

- `text/html`
- `text/css`
- `text/plain`
- `text/xml`
- `text/csv`
- `text/rtf`
- `text/javascript`

#### Uygulama dosyası türleri

- `application/json`
- `application/pdf`

#### Resim dosyası türleri

- `image/bmp`
- `image/jpeg`
- `image/png`
- `image/webp`

#### Video dosyası türleri

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## En iyi uygulamalar

- **Doğru yöntemi seçin:** Küçük ve geçici dosyalar için satır içi verileri kullanın.
  Daha büyük veya sık kullanılan dosyalar için File API'yi kullanın. Halihazırda internette barındırılan veriler için harici URL'leri kullanın.
- **MIME türlerini belirtin:** Doğru işleme için dosya verilerinin her zaman doğru MIME türünü sağlayın.
- **Hataları Yönetin:** Ağ hataları, dosya erişimi sorunları veya API hataları gibi olası sorunları yönetmek için kodunuzda hata yönetimini uygulayın.
- **GCS İzinlerini Yönetme:** GCS kaydı kullanılırken Gemini API Hizmet Aracısı'na yalnızca belirli paketlerde gerekli `Storage Object Viewer` rolünü verin.
- **İmzalı URL Güvenliği:** İmzalı URL'lerin uygun bir geçerlilik süresine ve sınırlı izinlere sahip olduğundan emin olun.

## Sınırlamalar

- Dosya boyutu sınırları yönteme ([karşılaştırma tablosuna](#method-comparison) bakın) ve dosya türüne göre değişir.
- Satır içi veriler, istek yükü boyutunu artırır.
- File API yüklemeleri geçicidir ve 48 saat sonra sona erer.
- Harici URL getirme, yük başına 100 MB ile sınırlıdır ve belirli içerik türlerini destekler.
- Google Cloud Storage kaydı için uygun IAM kurulumu ve OAuth jetonu yönetimi gerekir.

## Sırada ne var?

- [Google AI Studio](http://aistudio.google.com/?hl=tr)'yu kullanarak kendi çok formatlı istemlerinizi yazmayı deneyin.
- İstemlerinize dosya ekleme hakkında bilgi edinmek için [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=tr), [Ses](https://ai.google.dev/gemini-api/docs/audio?hl=tr) ve [Belge işleme](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) kılavuzlarına bakın.
- İstem tasarımıyla ilgili daha fazla bilgi (ör. örnekleme parametrelerini ayarlama) için [İstem stratejileri](https://ai.google.dev/gemini-api/docs/prompt-strategies?hl=tr) kılavuzuna bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
