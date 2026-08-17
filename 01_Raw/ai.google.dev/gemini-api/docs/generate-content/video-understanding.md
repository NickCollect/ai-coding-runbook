---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=tr
fetched_at: 2026-08-17T02:36:28.038357+00:00
title: "Video anlama \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Video anlama

> Video üretimi hakkında bilgi edinmek için [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) kılavuzuna bakın.

Gemini modelleri, videoları işleyebilir. Bu sayede, geçmişte alana özel modeller gerektiren birçok yeni geliştirici kullanım alanı mümkün olur.
Gemini'ın bazı görme özellikleri arasında videoları açıklama, segmentlere ayırma ve videolardan bilgi ayıklama, video içeriğiyle ilgili soruları yanıtlama ve videodaki belirli zaman damgalarına başvurma yer alır.

Gemini'a giriş olarak aşağıdaki yöntemlerle video sağlayabilirsiniz:

| Giriş yöntemi | Maks. boyut | Önerilen kullanım alanı |
| --- | --- | --- |
| [File API](#upload-video) | 20 GB (ücretli) / 2 GB (ücretsiz) | Büyük dosyalar (100 MB'tan büyük), uzun videolar (10 dakikadan uzun), yeniden kullanılabilir dosyalar. |
| [Cloud Storage Kaydı](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr#registration) | 2 GB (dosya başına, depolama alanı sınırı yoktur) | Büyük dosyalar (100 MB'tan büyük), uzun videolar (10 dakikadan uzun), kalıcı ve yeniden kullanılabilir dosyalar. |
| [Satır İçi Veriler](#inline-video) | < 100MB | Küçük dosyalar (<100 MB), kısa süre (<1 dakika), tek seferlik girişler. |
| [YouTube URL'leri](#youtube) | Yok | Herkese açık YouTube videoları. |

> **Not:** [File API](#upload-video), özellikle 100 MB'tan büyük dosyalar için veya dosyayı birden fazla istekte yeniden kullanmak istediğinizde çoğu kullanım alanı için önerilir.

Harici URL'leri veya Google Cloud'da depolanan dosyaları kullanma gibi diğer dosya giriş yöntemleri hakkında bilgi edinmek için [Dosya giriş yöntemleri](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr) kılavuzuna bakın.

### Video dosyası yükleme

Aşağıdaki kod, örnek bir videoyu indirir, [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr)'yi kullanarak yükler, işlenmesini bekler ve ardından yüklenen dosya referansını kullanarak videoyu özetler.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-3.6-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
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

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.6-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
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
```

### REST

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

Toplam istek boyutu (dosya, metin istemi, sistem talimatları vb. dahil) 20 MB'tan büyükse, video süresi uzunsa veya aynı videoyu birden fazla istemde kullanmayı planlıyorsanız her zaman Files API'yi kullanın.
File API, video dosyası biçimlerini doğrudan kabul eder.

Medya dosyalarıyla çalışma hakkında daha fazla bilgi edinmek için [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr)'yi inceleyin.

### Video verilerini satır içi olarak iletme

Dosya API'sini kullanarak video dosyası yüklemek yerine, daha küçük videoları doğrudan `generateContent` isteğinde iletebilirsiniz. Bu, toplam istek boyutu 20 MB'tan küçük olan kısa videolar için uygundur.

Satır içi video verileri sağlama örneğini burada bulabilirsiniz:

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [
  {
    inlineData: {
      mimeType: "video/mp4",
      data: base64VideoFile,
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
```

### REST

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {
              "inline_data": {
                "mime_type":"video/mp4",
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"
              }
            },
            {"text": "Please summarize the video in 3 sentences."}
        ]
      }]
    }' 2> /dev/null
```

### YouTube URL'lerini iletme

YouTube URL'lerini, isteğinizin bir parçası olarak doğrudan Gemini API'ye aşağıdaki şekilde iletebilirsiniz:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

const contents = [
  {
    fileData: {
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",
    },
  },
  { text: "Please summarize the video in 3 sentences." }
];

const response = await ai.models.generateContent({
  model: "gemini-3.6-flash",
  contents: contents,
});
console.log(response.text);
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
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
            {"text": "Please summarize the video in 3 sentences."},
            {
              "file_data": {
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"
              }
            }
        ]
      }]
    }' 2> /dev/null
```

**Sınırlamalar:**

- Ücretsiz katmanda, günde 8 saatten fazla YouTube videosu yükleyemezsiniz.
- Ücretli katmanda video uzunluğuna göre bir sınırlama yoktur.
- Gemini 2.5'ten önceki modellerde, istek başına yalnızca 1 video yükleyebilirsiniz. Gemini 2.5 ve sonraki modellerde, istek başına en fazla 10 video yükleyebilirsiniz.
- Yalnızca herkese açık videoları (gizli veya liste dışı videoları değil) yükleyebilirsiniz.

## Uzun videolarda bağlamı önbelleğe alma özelliğini kullanma

10 dakikadan uzun videolar veya aynı video dosyasına birden fazla istek göndermeyi planladığınız durumlarda, maliyetleri düşürmek ve gecikmeyi azaltmak için [bağlam önbelleğe almayı](https://ai.google.dev/gemini-api/docs/caching?hl=tr) kullanın. Bağlamı önbelleğe alma özelliği, videoyu bir kez işlemenize ve sonraki sorgularda parçaları yeniden kullanmanıza olanak tanır. Bu nedenle, sohbet oturumları veya uzun içeriklerin tekrar tekrar analiz edilmesi için idealdir.

## İçerikteki zaman damgalarına bakın

`MM:SS` biçimindeki zaman damgalarını kullanarak videodaki belirli zaman noktaları hakkında soru sorabilirsiniz.

### Python

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

### JavaScript

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

### REST

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Videodan ayrıntılı analizler çıkarma

Gemini modelleri, hem **ses hem de görsel** akışlardaki bilgileri işleyerek video içeriklerini anlamak için güçlü özellikler sunar. Bu sayede, videoda olan bitenin açıklamalarını oluşturma ve içeriğiyle ilgili soruları yanıtlama da dahil olmak üzere zengin bir ayrıntı kümesi çıkarabilirsiniz.

Görsel açıklamalar için model, videoyu **saniyede 1 kare** (FPS) hızında örnekler. Bu varsayılan örnekleme hızı çoğu içerik için uygundur ancak hızlı hareketlerin veya hızlı sahne değişikliklerinin olduğu videolarda ayrıntılar atlanabilir.
Bu tür yüksek hareketli içerikler için [özel bir kare hızı ayarlamayı](#custom-frame-rate) düşünebilirsiniz.

### Python

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

### JavaScript

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

### Go

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

### REST

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Video işlemeyi özelleştirme

Kırpma aralıkları ayarlayarak veya özel kare hızı örnekleme sağlayarak Gemini API'de video işlemeyi özelleştirebilirsiniz.

### Kırpma aralıklarını ayarlama

Başlangıç ve bitiş zamanlarını belirterek `videoMetadata` ile video klip oluşturabilirsiniz.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),
                video_metadata=types.VideoMetadata(
                    start_offset='1250s',
                    end_offset='1570s'
                )
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-3.6-flash';

async function main() {
const contents = [
  {
    role: 'user',
    parts: [
      {
        fileData: {
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',
          mimeType: 'video/*',
        },
        videoMetadata: {
          startOffset: '40s',
          endOffset: '80s',
        }
      },
      {
        text: 'Please summarize the video in 3 sentences.',
      },
    ],
  },
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Özel kare hızı ayarlama

`fps` işlevine `videoMetadata` bağımsız değişkenini ileterek özel kare hızı örneklemesi ayarlayabilirsiniz.

### Python

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-3.6-flash',
    contents=types.Content(
        parts=[
            types.Part(
                inline_data=types.Blob(
                    data=video_bytes,
                    mime_type='video/mp4'),
                video_metadata=types.VideoMetadata(fps=5)
            ),
            types.Part(text='Please summarize the video in 3 sentences.')
        ]
    )
)
```

Varsayılan olarak videodan saniyede 1 kare (FPS) örneklenir. Uzun videolar için düşük FPS (< 1) ayarlamak isteyebilirsiniz. Bu özellik, özellikle çoğunlukla statik olan videolar (ör. dersler) için kullanışlıdır. Hızlı aksiyonu anlama veya yüksek hızlı hareket izleme gibi ayrıntılı zamansal analiz gerektiren videolar için daha yüksek bir FPS kullanın.

## Desteklenen video biçimleri

Gemini aşağıdaki video biçimi MIME türlerini destekler:

- `video/mp4`
- `video/mpeg`
- `video/quicktime`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Videolarla ilgili teknik ayrıntılar

- **Desteklenen modeller ve bağlam**: Tüm Gemini modelleri video verilerini işleyebilir.
  - 1 milyon parçalık bağlam penceresine sahip modeller, 1 saate kadar uzunluktaki videoları varsayılan medya çözünürlüğünde veya 3 saate kadar uzunluktaki videoları düşük medya çözünürlüğünde işleyebilir.
- **File API işleme**: File API kullanılırken videolar saniyede 1 kare (FPS) hızında depolanır ve ses 1 Kbps (tek kanal) hızında işlenir.
  Zaman damgaları her saniye eklenir.
  - Bu oranlar, çıkarım iyileştirmeleri için gelecekte değişebilir.
  - [Özel bir kare hızı ayarlayarak](#custom-frame-rate) 1 FPS örnekleme hızını geçersiz kılabilirsiniz.
- **Jeton hesaplama**: Videonun her saniyesi aşağıdaki şekilde jetonlaştırılır:
  - Tek tek kareler (1 FPS'de örneklenir):
    - [`mediaResolution`](https://ai.google.dev/api/generate-content?hl=tr#MediaResolution) düşük olarak ayarlanırsa kareler, kare başına 66 jeton olacak şekilde jetonlaştırılır.
    - Aksi takdirde, kareler kare başına 258 jeton olacak şekilde jetonlaştırılır.
  - Ses: Saniyede 32 jeton.
  - Meta veriler de dahildir.
  - Toplam: Varsayılan medya çözünürlüğünde saniyede yaklaşık 300 jeton veya düşük medya çözünürlüğünde saniyede 100 jeton.
- **Medya çözünürlüğü**: Gemini 3, `media_resolution` parametresiyle çok formatlı görüntü işleme üzerinde ayrıntılı kontrol imkanı sunar. `media_resolution` parametresi, **giriş resim veya video karesi başına ayrılan maksimum jeton sayısını** belirler.
  Daha yüksek çözünürlükler, modelin küçük metinleri okuma veya küçük ayrıntıları tanımlama becerisini artırır ancak jeton kullanımını ve gecikmeyi de artırır.

  Parametre ve jeton hesaplamalarını nasıl etkileyebileceği hakkında daha fazla bilgi için [medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=tr) rehberine bakın.
- **Zaman damgası biçimi**: İsteminizde bir videodaki belirli anlardan bahsederken `MM:SS` biçimini kullanın (ör. 1 dakika 15 saniye için `01:15`).
- **En iyi uygulamalar**:

  - En iyi sonuçları elde etmek için istem isteği başına yalnızca bir video kullanın.
  - Metin ve tek bir videoyu birleştiriyorsanız metin istemini `contents` dizisinde video bölümünden *sonra* yerleştirin.
  - Hızlı hareket dizilerinin, 1 FPS örnekleme hızı nedeniyle ayrıntı kaybedebileceğini unutmayın. Gerekirse bu tür klipleri yavaşlatabilirsiniz.

## Sırada ne var?

Bu kılavuzda, video dosyalarının nasıl yükleneceği ve video girişlerinden nasıl metin çıkışları oluşturulacağı gösterilmektedir. Daha fazla bilgi edinmek için aşağıdaki kaynakları inceleyin:

- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/text-generation?hl=tr#system-instructions):
  Sistem talimatları, modelin davranışını özel ihtiyaçlarınıza ve kullanım alanlarınıza göre yönlendirmenizi sağlar.
- [Files API](https://ai.google.dev/gemini-api/docs/files?hl=tr): Gemini ile kullanılacak dosyaları yükleme ve yönetme hakkında daha fazla bilgi edinin.
- [Dosya istemi stratejileri](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide): Gemini API, çok formatlı istem olarak da bilinen metin, resim, ses ve video verileriyle istem oluşturmayı destekler.
- [Güvenlik yönergeleri](https://ai.google.dev/gemini-api/docs/safety-guidance?hl=tr): Üretken yapay zeka modelleri bazen yanlış, önyargılı veya rahatsız edici gibi beklenmedik çıkışlar üretebilir. Bu tür çıkışlardan kaynaklanan zarar riskini sınırlamak için son işlem ve uzman değerlendirmesi şarttır.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
