---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/files?hl=tr
fetched_at: 2026-10-19T05:53:11.604337+00:00
title: "Dosyalar API'si \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Dosyalar API'si

Gemini; metin, resim ve ses dahil olmak üzere çeşitli giriş verisi türlerini aynı anda işleyebilir.

Bu kılavuzda, Files API'yi kullanarak medya dosyalarıyla nasıl çalışacağınız gösterilmektedir. Ses dosyaları, resimler, videolar, dokümanlar ve desteklenen diğer dosya türleri için temel işlemler aynıdır.

Dosya istemiyle ilgili rehberlik için [Dosya istemi kılavuzu](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide) bölümüne göz atın.

## Dosya yükleyin

Medya dosyası yüklemek için Files API'yi kullanabilirsiniz. Toplam istek boyutu (dosyalar, metin istemi, sistem talimatları vb. dahil) 100 MB'tan büyükse her zaman Files API'yi kullanın. Bu sınır, PDF dosyaları için 50 MB'tır.

Aşağıdaki kod bir dosya yükler ve ardından dosyayı `generateContent` çağrısında kullanır.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-3.8-flash", contents=["Describe this audio clip", myfile]
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
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.Files.Delete(ctx, file.Name)

resp, err := client.Models.GenerateContent(ctx, "gemini-3.8-flash", []*genai.Content{
  {
    Parts: []*genai.Part{
      genai.NewPartFromFile(*file),
      genai.NewPartFromText("Describe this audio clip"),
    },
  },
}, nil)

if err != nil {
    log.Fatal(err)
}

printResponse(resp)
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
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
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

## Dosyanın meta verilerini alma

API'nin, yüklenen dosyayı başarıyla depoladığını doğrulayabilir ve `files.get` yöntemini çağırarak dosyanın meta verilerini alabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await ai.files.get({ name: fileName });
  console.log(fetchedFile);
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.Files.Get(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)
```

### REST

```
# file_info.json was created in the upload example
name=$(jq ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/files/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri
```

## Yüklenen dosyaları listeleme

Aşağıdaki kod, yüklenen tüm dosyaların listesini alır:

### Python

```
from google import genai

client = genai.Client()

print('My files:')
for f in client.files.list():
    print(' ', f.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const listResponse = await ai.files.list({ config: { pageSize: 10 } });
  for await (const file of listResponse) {
    console.log(file.name);
  }
}

await main();
```

### Go

```
for file, err := range client.Files.All(ctx) {
  if err != nil {
    log.Fatal(err)
  }
  fmt.Println(file.Name)
}
```

### REST

```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Yüklenen dosyaları silme

Dosyalar 48 saat sonra otomatik olarak silinir. Yüklenen bir dosyayı manuel olarak da silebilirsiniz:

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)
```

### JavaScript

```
import {
  GoogleGenAI,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await ai.files.delete({ name: fileName });
}

await main();
```

### Go

```
file, err := client.Files.UploadFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.Files.Delete(ctx, file.Name)
```

### REST

```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Kullanım bilgileri

Medya dosyalarını yüklemek ve bunlarla etkileşim kurmak için Files API'yi kullanabilirsiniz. Files API, proje başına 20 GB'a kadar dosya depolamanıza olanak tanır. Dosya başına maksimum boyut 2 GB'tır. Dosyalar 48 saat boyunca saklanır.

Bu süre zarfında, dosyalarla ilgili meta verileri almak için API'yi kullanabilirsiniz. Ancak kullanıcılar tarafından yüklenen dosyaları indiremezsiniz. Modeller tarafından üretilen dosyaları (ör. videolar) `files.download` yöntemini kullanarak indirebilirsiniz. Files API, Gemini API'nin kullanılabildiği tüm bölgelerde ücretsiz olarak kullanılabilir.

## Dosya istemi stratejileri

Bu bölümde, Gemini API istemleriyle medya dosyalarını kullanmaya yönelik yönergeler ve en iyi uygulamalar yer almaktadır.

İstemlerinizde çeşitli veri türlerini kullanabilmek, Gemini API ile gerçekleştirebileceğiniz görevler açısından size daha fazla esneklik sağlar. Örneğin, modele lezzetli bir yemeğin fotoğrafını gönderip yemekle ilgili kısa bir blog yazmasını isteyebilirsiniz.

|  |  |
| --- | --- |
| **İstem** | **Yanıt** |
| Bu resme dayalı olarak kısa ve ilgi çekici bir blog yayını yaz. Fotoğraftaki yemeğin açıklamasını içermeli ve yemek hazırlama yolculuğumdan bahsetmeli.   Çerezler | Öğün hazırlama, zamandan ve paradan tasarruf etmenin harika bir yoludur. Ayrıca daha sağlıklı beslenmenize de yardımcı olabilir. Bu yemek, önceden kolayca hazırlanabilen sağlıklı ve lezzetli bir yemeğe harika bir örnektir.  Bu yemekte kahverengi pirinç, fırınlanmış sebzeler ve teriyaki soslu tavuk bulunur. Kahverengi pirinç, size uzun süreli enerji verecek sağlıklı ve karmaşık bir karbonhidrattır. Kızarmış sebzeler, günlük vitamin ve mineral ihtiyacınızı karşılamanın harika bir yoludur. Teriyaki soslu tavuk ise lezzetli ve protein açısından zengin bir seçenektir.  Bu yemeğin hazırlanması da çok kolaydır. Kahverengi pirinci pişirin, sebzeleri kavurun ve teriyaki soslu tavuğu pişirin. Her şey piştikten sonra yemekleri kaplara bölüp buzdolabında saklayın. Ardından, yoğun sabahlarınızda bir kap alıp çıkabilirsiniz.  Önceden kolayca hazırlanabilecek sağlıklı ve lezzetli bir yemek arıyorsanız bu yemek harika bir seçenektir. Besin değeri yüksek ve lezzetli olan bu yemek, sizi tok tutacak ve tatmin edecek.  Sağlıklı ve lezzetli yemek hazırlama! |

Medya dosyalarını kullanan istemlerden istediğiniz çıkışı almakta sorun yaşıyorsanız istediğiniz sonuçları elde etmenize yardımcı olabilecek bazı stratejiler vardır. Aşağıdaki bölümlerde, çok formatlı giriş kullanan istemleri iyileştirmeye yönelik tasarım yaklaşımları ve sorun giderme ipuçları verilmiştir.

Aşağıdaki en iyi uygulamaları izleyerek çok formatlı istemlerinizi iyileştirebilirsiniz:

- ### [İstem tasarımıyla ilgili temel bilgiler](#specific-instructions)

  - **Talimatlarınızda net olun**: Yanlış yorumlamaya en az yer bırakacak şekilde net ve kısa talimatlar oluşturun.
  - **İsteminize birkaç örnek ekleyin:** Elde etmek istediğiniz sonucu göstermek için gerçekçi few-shot örnekleri kullanın.
  - **Adım adım ilerleyin**: Karmaşık görevleri yönetilebilir alt hedeflere bölerek modele süreç boyunca rehberlik edin.
  - **Çıkış biçimini belirtin**: İsteminizde çıkışın Markdown, JSON, HTML gibi istediğiniz biçimde olmasını talep edin.
  - **Tek resimli istemlerde resminizi ilk sıraya koyun**: Gemini, resim ve metin girişlerini herhangi bir sırayla işleyebilir ancak tek bir resim içeren istemlerde, resim (veya video) metin isteminden önce yerleştirilirse daha iyi performans gösterebilir. Ancak anlamlı olması için resimlerin metinlerle yoğun bir şekilde iç içe geçmesini gerektiren istemlerde en doğal olan sırayı kullanın.
- ### [Çok formatlı istem yazma sorunlarını giderme](#troubleshooting)

  - **Model, resmin ilgili bölümünden bilgi almıyorsa:** İstemden, resmin hangi yönleriyle ilgili bilgi almasını istediğinize dair ipuçları verin.
  - **Model çıkışı çok genel ise (görüntü/video girişine yeterince uygun değilse):** İstemin başında, görev talimatını vermeden önce modelden görüntüleri veya videoyu açıklamasını isteyin ya da modelden görüntüdeki öğelere atıfta bulunmasını isteyin.
  - **Hangi bölümün başarısız olduğunu gidermek için:** Modelden görüntüyü açıklamasını veya akıl yürütmesini açıklamasını isteyerek modelin ilk anlayışını ölçün.
  - **İsteminiz halüsinasyonlu içerik üretiyorsa:** Sıcaklık ayarını düşürmeyi veya modelden daha kısa açıklamalar istemeyi deneyin. Böylece modelin ek ayrıntılar uydurma olasılığı azalır.
  - **Örnekleme parametrelerini ayarlama:** Modelin yaratıcılığını ayarlamak için farklı sıcaklık ayarları ve top-k seçimleriyle denemeler yapın.

### Talimatlarınızda ayrıntılı bilgi verin

İstemler en iyi sonucu net ve ayrıntılı olduğunda verir. Aklınızda belirli bir çıktı varsa istediğiniz çıktıyı elde etmek için bu şartı isteme eklemeniz daha iyi olur.

Havaalanı panosunun bu görüntüsü için modelden yalnızca "bu görüntüyü açıklamasını" istemek genel bir açıklama oluşturabilir. Modelin, resimdeki saati ve şehri ayrıştırmasını istiyorsanız bu isteği doğrudan isteminize ekleyebilirsiniz.

| İstem | Model yanıtı |
| --- | --- |
| Bu resmi tanımla. | Resimde, havaalanındaki gelen ve giden uçuşlar panosu gösteriliyor. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Seyahat zaman çizelgesi Parse the time and city from the airport board shown in this image into a list. | - 10:50 Moskova - 11:05 Edinburgh - 11:05 Londra - 11:10 Bükreş - 11:30 Kiev - 11:35 Dublin - 11:45 East Midlands - 12:15 Sofya - 12:30 Londra - 12:30 Newcastle - 12:40 St Petersburg - 12:40 Londra - 12:45 Manchester |

### Birkaç örnek ekleyin

Gemini modeli, istediğiniz çıktıyı anlamak için örnek olarak kullanabileceği birden fazla girişi kabul edebilir. Bu örnekleri eklemek, modelin kalıpları belirlemesine ve verilen resimler ile yanıtlar arasındaki ilişkiyi yeni örneğe uygulamasına yardımcı olabilir. Buna "few-shot" öğrenme de denir.

Aşağıdaki örnekte, ilk çıkış cümle şeklinde yazılmış ve ülke (Brezilya) bilgisi de yer alıyor. Çıktının farklı bir biçimde veya stilde olmasını ve ülke yerine yalnızca şehir bilgisini içermesini istediğinizi varsayalım. İsteminize few-shot örnekleri eklemek, modelin istediğiniz şekilde yanıt vermesini sağlayabilir.

| **İstem** | **Model yanıtı** |
| --- | --- |
| Seyahat zaman çizelgesi Şehri ve simge yapıyı belirleyin. | Bu önemli yer, Brezilya'nın Rio de Janeiro kentindeki Kurtarıcı İsa heykelidir. |

| **Güncellenen istem** | **Daha iyi yanıt** |
| --- | --- |
| Şehri ve simge yapıyı belirleyin. colosseum | Şehir: Roma, simge yapı: Kolezyum. |
| Yasak Şehir | şehir: Pekin, önemli yer: Yasak Şehir |
| forbidden-city | şehir: Rio de Janeiro, simge yapı: Christ the Redeemer heykeli |

### Adım adım açıklama

Hem görsel anlama hem de muhakeme gerektiren görevler gibi karmaşık görevleri daha küçük ve basit adımlara bölmek yararlı olabilir. Alternatif olarak, isteminizde doğrudan modelden "adım adım düşünmesini" istemek de etkili olabilir.

| İstem | Model yanıtı |
| --- | --- |
| Tuvalet kağıdım ne zaman biter? | Kısa süre sonra yalnızca 3 rulo kalır. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| 1. Öncelikle bu resimde kaç tane tuvalet kağıdı rulosu olduğunu sayın.  2. Ardından, normal bir kişinin günde ne kadar tuvalet kağıdı kullandığını belirleyin.  3. Bu tuvalet kağıdı rulolarının ne kadar süre dayanacağını hesaplayın. | 1. Bu resimde 3 rulo tuvalet kağıdı var.  2. Tipik bir kişi günde yaklaşık 20 yaprak tuvalet kağıdı kullanır.  3. Her ruloda 200 yaprak varsa her rulo yaklaşık 10 gün dayanır. Bu nedenle, 3 rulo yaklaşık bir ay dayanır. |

Matematik problemleri veya diğer sözel problemler, modelin adım adım düşünmesini istemek için idealdir.

| **İstem** | **Yanıt** |
| --- | --- |
| Dizideki 4. terim nedir? | -135 |

Modelin yanıtı yanlış. Bunu iyileştirmenin bazı yolları, modelden isteme yanıt vermeden önce sorunu ayrıştırmasını istemektir.

| **İstem** | **Yanıt** |
| --- | --- |
| Önce resimdeki formülü ayrıştırın.  Ardından, formüle göre "Dizideki 4. terim nedir?" sorusunu yanıtlayın. | *Sonucu genişletmek için tıklayın* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. Formülde n = 4 değerini yerine koyun:  $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. b(3) değerini bilmiyoruz. Bu nedenle, n = 3 değerini formülde yerine koyun:  $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. b(2) değerini bilmiyoruz. Bu nedenle, n = 2 değerini formülde yerine koyun:  $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. b(1) değerinin 15 olduğunu biliyoruz. Bu değeri formülde yerine koyalım:  $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. b(2)'nin değerini bildiğimize göre b(3) formülünde yerine koyalım:  $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. b(3) değerini bildiğimize göre bunu b(4) formülünde yerine koyalım:  $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Bu nedenle, dizideki 4. terim -405'tir. |

Bu model yanıtı doğru. Yanıtı daha da kolaylaştırmak için modele adım adım düşünmesini söyleyebilirsiniz.

| **Güncellenen istem** | **Daha iyi yanıt** |
| --- | --- |
| Dizideki 4. terim nedir? Adım adım düşünün. | İlk terim 15'tir.  İkinci terim b(1) \* (-3) = 15 \* (-3) = -45 olur.  Üçüncü terim b(2) \* (-3) = -45 \* (-3) = 135'tir.  Dördüncü terim b(3) \* (-3) = 135 \* (-3) = -405 olur. |

### Çıkış biçimini belirtme

Sık karşılaşılan sorunlardan biri, model çıktısının belirli bir biçimde (ör.Markdown, JSON, HTML) olması gerektiğidir. Bu durum, özellikle model çıktısının bir alt görev tarafından alınması gerektiğinde geçerlidir. İstemde modeli bu biçimde çıkış üretmeye yönlendirerek bu biçimde çıkış üretmeyi deneyebilirsiniz. Aşağıda iki örnek verilmiştir:

| İstem | Model yanıtı |
| --- | --- |
| Bu resimdeki tabloyu Markdown biçiminde ayrıştır. | | Konu | Durum | Saat | Başlangıç tarihi | Teslim tarihi |  | ------- | ------ | ---- | ---------- | ------ |  | Matematik | Tamamlandı | 1,5 saat | 29.11.2023 | 01.12.2023 |  | Coğrafya | Tamamlandı | 30 dk | 2.12.2023 | 4.12.2023 |  | Fizik | Devam ediyor | 2 saat | 3.12.2023 | 5.12.2023 |  | Biyoloji | Başlatılmadı | 6 saat | 11/2/2016 | 12/6/2023 | |

| **İstem** | **Model yanıtı** |
| --- | --- |
| Aşağıdaki tüm özelliklerin listesini sağlayın:  malzemeler, mutfak türü, vejetaryen olup olmadığı, JSON biçiminde | ```` ```json ````  `{`  `"ingredients": [`  `"rice",`  `"shrimp",`  `"clams",`  `"mussels",`  `"peas",`  `"tomatoes",`  `"onions",`  `"garlic",`  `"olive oil",`  `"paprika",`  `"salt",`  `"pepper"`  `],`  `"type of cuisine": "Spanish",`  `"vegetarian": false`  `}`  ```` ``` ```` |

### Tek resim içeren istemlerde önce resminizi ekleyin

Gemini, bir istemdeki resim ve metni herhangi bir sırayla yorumlayabilir ancak metin isteminden önce tek bir resim yerleştirmek daha iyi sonuçlar verebilir.
Aşağıdaki örneklerde, her istemde önce resmin, sonra metnin geldiğini göreceksiniz.

### Çok formatlı istem yazma sorunlarını giderme

Faydalı bir yanıt alamıyorsanız isteminizle ilgili sorunları gidermeniz gerekebilir. Deneyebileceğiniz birkaç strateji:

#### Model, görüntünün ilgili bölümünden bilgi almıyorsa

Daha spesifik bir yanıt almak için istemin, yanıtını oluştururken görüntünün hangi yönlerinden bilgi almasını istediğinizi belirtebilirsiniz.

| İstem | Model yanıtı |
| --- | --- |
| Bu bezler bir bebeğe kaç gün yeter? | Bezler bitmeden 198 gün boyunca kullanılabilir. |

| **Güncellenen istem** | **Daha iyi yanıt** |
| --- | --- |
| Bu bebek bezleri ne kadar süre yeter?  Çocuğun yaşını belirlemek için kutuda gösterilen ağırlığı, kutudaki toplam bebek bezi sayısını kullanın.  Toplam sayıyı, çocuğun günde kullandığı bez sayısına bölün. | Kutuda 198 adet bez bulunur. Kutuda, bezlerin 10-17 kg ağırlığındaki çocuklar için olduğu belirtiliyor.  Bu ağırlık aralığındaki ortalama bir çocuğun yaşı muhtemelen 1 ile 2 arasındadır.  2 yaşındaki bir çocuk genellikle günde 6 bez kullanır. Bu nedenle bezler yaklaşık 33 gün (198/6) yeterli olur. |

#### Model çıkışı çok genel ve resim girişine yeterince uyarlanmamışsa

Modelin yanıtını resimlere göre uyarlamasına yardımcı olmak için akıl yürütme görevini gerçekleştirmeden önce resimleri açıklamasını isteyin.

| İstem | Model yanıtı |
| --- | --- |
| Bu resimlerin ortak noktası nedir? | Dört resmin tamamı manzara fotoğrafçılığı örnekleridir. |

| **Güncellenen istem** | **Daha iyi yanıt** |
| --- | --- |
| Öncelikle her resimde ne olduğunu ayrıntılı olarak açıklayın. Bu resimlerin ortak noktası nedir? | İlk resimde bavul hazırlayan bir kişi gösteriliyor. İkinci resimde bir alışveriş merkezindeki boş bir koridor gösteriliyor. Üçüncü resimde bir rulo tuvalet kağıdı gösteriliyor. Dördüncü resimde karanlık ve fırtınalı bir deniz gösteriliyor.  Bu resimlerin ortak noktası, hepsinin eşik alan örnekleri olmasıdır. Geçiş alanları, iki yer veya durum arasında kalan yerler ya da durumlardır. Genellikle belirsizlik veya muğlaklık hissiyle karakterize edilirler.  İlk resimde, kişinin evde ve seyahatte olma durumu arasında kaldığı gösteriliyor. İkinci resimde iki mağaza arasındaki koridor gösteriliyor. Üçüncü resimde, banyoyu temsil edebilecek tuvalet kağıdı gösteriliyor. Banyo, özel ve kamusal alanlar arasında geçiş sağlayan bir mekandır. Dış dünyaya girmeye veya dış dünyadan ayrılmaya hazırlandığımız bir yerdir.  Dördüncü resimde, sakin ve fırtınalı bir deniz gösteriliyor.  Eşik alanlar hem heyecan verici hem de rahatsız edici olabilir. Yeni bir başlangıç veya bir sonun yeri olabilirler. Düşünme veya harekete geçme yeri olabilirler. |

Ayrıca, modelden görüntüdeki bilgilere açıkça atıfta bulunmasını da isteyebilirsiniz.

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Bu resimlerin ortak noktası nedir? Yanıtınızda resimlerdeki öğelere atıfta bulunun. | Tüm resimler seyahatle ilgilidir. İlk resimde valiz hazırlayan bir kişi, ikinci resimde alışveriş merkezindeki boş bir koridor, üçüncü resimde bir rulo tuvalet kağıdı, dördüncü resimde ise karanlık ve fırtınalı bir deniz gösteriliyor.  Bu resimlerin tümü seyahatle ilgilidir çünkü hepsi insanların seyahat ederken ihtiyaç duyduğu veya kullandığı şeylerdir. İlk resimde, bir valiz hazırlayan bir kişi gösteriliyor. Bu, insanların seyahate çıkarken yaptığı bir şeydir. İkinci resimde, insanların seyahatleri için eşya satın almak üzere sık sık gittiği bir yer olan alışveriş merkezindeki boş bir koridor gösteriliyor. Üçüncü resimde, insanların seyahat ederken sıkça kullandığı bir ürün olan tuvalet kağıdı rulosu gösteriliyor. Dördüncü resimde, insanların seyahat ederken sıkça karşılaştığı bir durum olan karanlık ve fırtınalı bir deniz gösteriliyor. |

Aynı ipuçları, resimlerden elde edilen reklam öğesi çıkışları için de geçerlidir. Tavşanla ilgili aşağıdaki örnekte, modelden resimdeki unsurları dahil etmesini açıkça istemek çıkışı iyileştirebilir.

| İstem | Model yanıtı |
| --- | --- |
| Bu görsel hakkında bir şiir yazabilir misin? | Küçük tavşan, yumuşak ve kahverengi,  Tarlada zıplıyor, yukarı ve aşağı.  Kulakların uzun, kuyruğun küçük,  En tatlı canlı sensin, minik tavşan.  Yeşil ve tatlı çimleri yersin,  Beni görünce de zıplayarak kaçarsın.  Ama ben her zaman senin arkadaşın olacağım,  Küçük tavşan, en sonuna kadar. |

| **Güncellenen istem** | **Daha iyi yanıt** |
| --- | --- |
| Bu görsel hakkında açıklayıcı ve dramatik bir şiir yazıp konumu da ekleyebilir misin? | Küçük tavşan çimenlerde,  Uzun kulakları dikilmiş.  Ne görüyorsun orada,  Uzaklarda, baktığın yerde?  Güneşin rengiyle parıldayan  Mavi okyanus mu?  Yoksa dalgaların sesi mi,  Seni büyüleyen ritim?  Küçük tavşan, söyle bana,  Nedir seni böyle büyüleyen?  Tuzlu rüzgar mı,  Yoksa martıların çığlıkları mı hoşunuza giden?  Belki de her şeyin büyüklüğünden,  Dünya hem çok büyük hem çok küçük.  Hayallerin dolaşabileceği,  Maceraların yeşerebileceği bir yer.  Küçük tavşan, rüyanda ne görüyorsun acaba?  Çimlerin üzerinde otururken çok huzurlu görünüyorsun.  Derinlikleri keşfetmek mi istersiniz,  Yoksa karada kalıp zıplamak mı?  Ne olursa olsun, küçük tavşan,  Merak kıvılcımını parlak bir şekilde yakmaya devam et.  Hayallerinizde ve isteklerinizde,  Yaratmanızı bekleyen bir dünya var. |

#### İstemin hangi bölümünün başarısız olduğunu belirleme

Bir istemin başarısız olmasının nedeni, modelin **görüntüyü anlamaması** mı yoksa görüntüyü anlamasına rağmen doğru **akıl yürütme adımlarını** uygulamaması mı, bunu anlamak zor olabilir.
Bu nedenleri netleştirmek için modelden resimde ne olduğunu açıklamasını isteyin.

Aşağıdaki örnekte, model çayla birlikte tüketildiğinde şaşırtıcı görünen bir atıştırmalık (ör. patlamış mısır) önerirse öncelikle modelin resimde çay olduğunu doğru şekilde algılayıp algılamadığını belirlemek için sorun giderebilirsiniz.

| İstem | Sorun giderme istemi |
| --- | --- |
| Bununla iyi gidecek, 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? | Bu resimde ne olduğunu açıklayın. |

Diğer bir strateji de modelden akıl yürütme sürecini açıklamasını istemektir. Bu, muhakemenin hangi kısmında sorun olduğunu (varsa) belirlemenize yardımcı olabilir.

| İstem | Sorun giderme istemi |
| --- | --- |
| Bununla iyi gidecek, 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? | Bununla iyi gidecek ve 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? Lütfen nedeniyle birlikte açıklayın. |

## Sırada ne var?

- [Google AI Studio](http://aistudio.google.com?hl=tr)'yu kullanarak kendi çok formatlı istemlerinizi yazmayı deneyin.
- Medya dosyalarını yüklemek ve istemlerinize dahil etmek için Gemini Files API'yi kullanma hakkında bilgi edinmek üzere [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=tr), [Ses](https://ai.google.dev/gemini-api/docs/audio?hl=tr) ve [Belge işleme](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) kılavuzlarını inceleyin.
- Örnekleme parametrelerini ayarlama gibi istem tasarımıyla ilgili daha fazla bilgi için [İstem stratejileri](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) sayfasını inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-14 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-14 UTC."],[],[]]
