---
source_url: https://ai.google.dev/gemini-api/docs/files?hl=tr
fetched_at: 2026-07-27T04:46:27.000906+00:00
title: "Dosyalar API'si \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Dosyalar API'si

Gemini, metin, resim ve ses gibi çeşitli giriş verilerini aynı anda işleyebilir.

Bu kılavuzda, Files API'yi kullanarak medya dosyalarıyla nasıl çalışacağınız gösterilmektedir. Ses dosyaları, resimler, videolar, dokümanlar ve desteklenen diğer dosya türleri için temel işlemler aynıdır.

Dosya istemiyle ilgili rehberlik için [Dosya istemi kılavuzu](https://ai.google.dev/gemini-api/docs/files?hl=tr#prompt-guide) bölümüne göz atın.

## Dosya yükleyin

Medya dosyası yüklemek için Files API'yi kullanabilirsiniz. Toplam istek boyutu (dosyalar, metin istemi, sistem talimatları vb. dahil) 100 MB'tan büyük olduğunda her zaman Files API'yi kullanın. Bu sınır, PDF dosyaları için 50 MB'tır.

Aşağıdaki kod, bir dosyayı yükler ve ardından `interactions.create` çağrısında dosyayı kullanır.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp3")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=[
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": myfile.uri, "mime_type": myfile.mime_type}
    ]
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const interaction = await client.interactions.create({
    model: "gemini-3.5-flash",
    input: [
      { type: "text", text: "Describe this audio clip" },
      { type: "audio", uri: myfile.uri, mime_type: myfile.mimeType }
    ]
  });
  console.log(interaction.output_text);
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

interaction, err := client.Interactions.Create(ctx, "gemini-3.5-flash", &genai.InteractionRequest{
    Input: []interface{}{
        genai.NewPartFromFile(*file),
        genai.NewPartFromText("Describe this audio clip"),
    },
}, nil)

if err != nil {
    log.Fatal(err)
}

// Print the model's text response
for _, step := range interaction.Steps {
    if step.Type == "model_output" {
        for _, part := range step.Content {
            if part.Type == "text" {
                fmt.Println(part.Text)
            }
        }
    }
}
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

# Now create an interaction using the Interactions API
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
      "model": "gemini-3.5-flash",
      "input": [
        {"type": "text", "text": "Describe this audio clip"},
        {"type": "audio", "uri": '$file_uri', "mime_type": "'${MIME_TYPE}'"}
      ]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".outputs[] | select(.type == \"text\") | .text" response.json
```

## Dosyanın meta verilerini alma

`files.get` işlevini çağırarak API'nin yüklenen dosyayı başarıyla depoladığını doğrulayabilir ve dosyanın meta verilerini alabilirsiniz.

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

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  const fetchedFile = await client.files.get({ name: fileName });
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
name=$(jq -r ".file.name" file_info.json)
# Get the file of interest to check state
curl https://generativelanguage.googleapis.com/v1beta/$name \
-H "x-goog-api-key: $GEMINI_API_KEY" > file_info.json
# Print some information about the file you got
name=$(jq -r ".name" file_info.json)
echo name=$name
file_uri=$(jq -r ".uri" file_info.json)
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

const client = new GoogleGenAI({});

async function main() {
  const listResponse = await client.files.list({ config: { pageSize: 10 } });
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

const client = new GoogleGenAI({});

async function main() {
  const myfile = await client.files.upload({
    file: "path/to/sample.mp3",
    config: { mime_type: "audio/mpeg" },
  });

  const fileName = myfile.name;
  await client.files.delete({ name: fileName });
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
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/$name \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Kullanım bilgileri

Medya dosyalarını yüklemek ve bu dosyalarla etkileşim kurmak için Files API'yi kullanabilirsiniz. Files API, proje başına 20 GB'a kadar dosya depolamanıza olanak tanır. Dosya başına maksimum boyut 2 GB'tır. Dosyalar 48 saat boyunca saklanır. Bu süre zarfında, dosyalarla ilgili meta verileri almak için API'yi kullanabilirsiniz ancak dosyaları indiremezsiniz.
Files API, Gemini API'nin kullanılabildiği tüm bölgelerde ücretsiz olarak kullanılabilir.

## Dosya istemi stratejileri

Bu bölümde, Gemini API için istemlerle medya dosyalarını kullanmayla ilgili rehberlik ve en iyi uygulamalar yer almaktadır.

İstemlerinizde çeşitli veri türlerini kullanabilmek, Gemini API ile hangi görevleri yapabileceğiniz konusunda daha fazla esneklik sağlar. Örneğin, modele lezzetli bir yemeğin fotoğrafını gönderip yemekle ilgili kısa bir blog yazısı yazmasını isteyebilirsiniz.

|  |  |
| --- | --- |
| **İstem** | **Yanıt** |
| Bu resme dayalı olarak kısa ve ilgi çekici bir blog yayını yaz. Fotoğraftaki yemeğin açıklamasını içermeli ve yemek hazırlama yolculuğumdan bahsetmelidir.   Çerezler | Yemek hazırlığı, zamandan ve paradan tasarruf etmenin yanı sıra daha sağlıklı beslenmenize de yardımcı olur. Bu yemek, önceden hazırlanabilen sağlıklı ve lezzetli bir yemeğe harika bir örnektir.  Bu öğünde kahverengi pirinç, fırında sebzeler ve teriyaki soslu tavuk bulunur. Esmer pirinç, size uzun süreli enerji verecek sağlıklı ve kompleks bir karbonhidrattır. Kızartılmış sebzeler, günlük vitamin ve mineral ihtiyacınızı karşılamak için harika bir seçenektir. Teriyaki soslu tavuk ise lezzetli ve protein açısından zengin bir seçenektir.  Bu yemeği hazırlamak da kolaydır. Kahverengi pirinci pişirin, sebzeleri fırında kızartın ve teriyaki soslu tavuğu pişirin. Her şey piştikten sonra yemek hazırlama kaplarına bölüp buzdolabında saklayın. Ardından, yoğun sabahlarınızda bir kap alıp çıkabilirsiniz.  Önceden hazırlanabilen sağlıklı ve lezzetli bir yemek arıyorsanız bu yemek harika bir seçenek. Besinler ve lezzetlerle dolu bu yemek, sizi tok ve memnun hissettirecek.  Sağlıklı ve lezzetli yemek hazırlama! |

Medya dosyalarının kullanıldığı istemlerden istediğiniz çıkışı almakta zorlanıyorsanız istediğiniz sonuçları elde etmenize yardımcı olabilecek bazı stratejiler vardır. Aşağıdaki bölümlerde, çok formatlı giriş kullanan istemleri iyileştirmeye yönelik tasarım yaklaşımları ve sorun giderme ipuçları verilmektedir.

Aşağıdaki en iyi uygulamaları izleyerek çok formatlı istemlerinizi iyileştirebilirsiniz:

- ### [İstem tasarımıyla ilgili temel bilgiler](#specific-instructions)

  - **Talimatlarınızda net olun**: Yanlış yorumlamaya en az yer bırakacak şekilde net ve kısa talimatlar oluşturun.
  - **İsteminize birkaç örnek ekleyin:** Ne elde etmek istediğinizi göstermek için gerçekçi birkaç görev örneği kullanın.
  - **Adım adım ilerleyin**: Karmaşık görevleri yönetilebilir alt hedeflere ayırarak modele süreç boyunca rehberlik edin.
  - **Çıkış biçimini belirtin**: İsteminizde, çıkışın istediğiniz biçimde (ör. Markdown, JSON, HTML vb.) olmasını isteyin.
  - **Tek resimli istemlerde resminizi önce girin**: Gemini, resim ve metin girişlerini herhangi bir sırada işleyebilse de tek resim içeren istemlerde, resim (veya video) metin isteminden önce yerleştirilirse daha iyi performans gösterebilir. Ancak, anlamlı olması için resimlerin metinlerle yoğun bir şekilde iç içe geçmesini gerektiren istemlerde en doğal olan sırayı kullanın.
- ### [Çok formatlı isteminizle ilgili sorunları giderme](#troubleshooting)

  - **Model, resmin ilgili bölümünden bilgi almıyorsa:** İstemden, resmin hangi yönleriyle ilgili bilgi almasını istediğinize dair ipuçları verin.
  - **Model çıktısı çok genel ise (resim/video girişine yeterince uyarlanmamışsa):** İstemin başında, görev talimatını vermeden önce modelden resimleri veya videoyu açıklamasını ya da modelden resimdeki içeriğe atıfta bulunmasını isteyin.
  - **Hangi bölümün başarısız olduğunu belirlemek için:** Modelin ilk anlayışını ölçmek üzere modelden resmi açıklamasını veya gerekçesini açıklamasını isteyin.
  - **İsteminiz halüsinasyon içeren içeriklerle sonuçlanıyorsa:** Sıcaklık ayarını düşürmeyi veya modelden daha kısa açıklamalar istemeyi deneyin. Böylece modelin ek ayrıntılar üretme olasılığı azalır.
  - **Örnekleme parametrelerini ayarlama:** Modelin yaratıcılığını ayarlamak için farklı sıcaklık ayarları ve top-k seçimleriyle denemeler yapın.

### Talimatlarınızda net olun

İstemler en iyi sonucu net ve ayrıntılı olduğunda verir. Aklınızda belirli bir çıkış varsa istediğiniz çıkışı elde etmek için bu şartı isteme eklemeniz daha iyi olur.

Havaalanı panosunun yer aldığı bu resim için modele yalnızca "bu resmi açıkla" komutunu verdiğinizde genel bir açıklama oluşturulabilir. Modelin resimdeki saati ve şehri ayrıştırması gerekiyorsa bu isteği doğrudan isteminize ekleyebilirsiniz.

| İstem | Model yanıtı |
| --- | --- |
| Bu resmi tanımla. | Resimde, havalimanındaki gelen ve giden uçuşlar tabelası gösteriliyor. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Seyahat zaman çizelgesi Bu resimde gösterilen havaalanı panosundaki saati ve şehri ayrıştırarak listeleyin. | - 10:50 Moskova - 11:05 Edinburgh - 11:05 Londra - 11:10 Bükreş - 11:30 Kiev - 11:35 Dublin - 11:45 East Midlands - 12:15 Sofya - 12:30 Londra - 12:30 Newcastle - 12:40 St Petersburg - 12:40 Londra - 12:45 Manchester |

### Birkaç örnek ekleyin

Gemini modeli, istediğiniz çıktıyı anlamak için örnek olarak kullanabileceği birden fazla giriş kabul edebilir. Bu örnekleri eklemek, modelin kalıpları belirlemesine ve verilen resimler ile yanıtlar arasındaki ilişkiyi yeni örneğe uygulamasına yardımcı olabilir. Bu, "az görevli" öğrenme olarak da adlandırılır.

Aşağıdaki örnekte, ilk çıkış cümle şeklinde yazılmış ve ülkeyi (Brezilya) de içeriyor. Çıktının farklı bir biçimde veya tarzda olmasını ve yalnızca şehri (ülkeyi değil) istiyorsunuz. İsteminize birkaç görevli örnek eklemek, modelin istediğiniz şekilde yanıt vermesini sağlayabilir.

| **İstem** | **Model yanıtı** |
| --- | --- |
| Seyahat zaman çizelgesi Simge yapıyla birlikte şehri belirleyin. | Bu simge yapı, Brezilya'nın Rio de Janeiro şehrindeki Kurtarıcı İsa heykelidir. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Simge yapıyla birlikte şehri belirleyin. colosseum | city: Rome, landmark: the Colosseum. |
| Yasak Şehir | city: Beijing, landmark: Forbidden City |
| forbidden-city | city: Rio de Janeiro, landmark: Christ the Redeemer statue |

### Adım adım inceleme

Hem görsel anlayış hem de akıl yürütme gerektiren görevler gibi karmaşık görevleri daha küçük ve basit adımlara bölmek faydalı olabilir. Alternatif olarak, isteminizde doğrudan modelden "adım adım düşünmesini" istemek de etkili olabilir.

| İstem | Model yanıtı |
| --- | --- |
| Tuvalet kağıdım ne zaman bitecek? | Çok yakında yalnızca 3 rulo hakkınız kalacak. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| 1. Öncelikle bu resimde kaç rulo tuvalet kağıdı olduğunu sayın. 2. Ardından, bir kişinin günde ne kadar tuvalet kağıdı kullandığını belirleyin. 3. Bu tuvalet kağıdı rulolarının ne kadar süre dayanacağını hesaplayın. | 1. Bu resimde 3 rulo tuvalet kağıdı var. 2. Tipik bir kişi günde yaklaşık 20 yaprak tuvalet kağıdı kullanır. 3. Her ruloda 200 yaprak varsa her rulo yaklaşık 10 gün dayanır. Bu nedenle, 3 rulo yaklaşık bir ay dayanır. |

Matematik problemleri veya diğer sözel problemler, modelden adım adım düşünmesini istemek için idealdir.

| **İstem** | **Yanıt** |
| --- | --- |
| Dizideki 4. terim nedir? | -135 |

Modelin yanıtı yanlış. Bunu iyileştirmenin bazı yolları, modelden isteme yanıt vermeden önce sorunu ayrıştırmasını istemektir.

| **İstem** | **Yanıt** |
| --- | --- |
| Önce resimdeki formülü ayrıştırın.  Ardından, formüle göre "Dizideki 4. terim nedir?" sorusunu yanıtlayın. | *Sonucu genişletmek için tıklayın* $$ b(n) = b(n-1) \* (-3) $$  $$ b(1) = 15 $$   1. n = 4 değerini formülde yerine koyun: $$ b(4) = b(4-1) \* (-3) $$  $$ b(4) = b(3) \* (-3) $$ 2. b(3) değerini bilmiyoruz. Bu nedenle, n = 3 değerini formülde yerine koyun: $$ b(3) = b(3-1) \* (-3) $$  $$ b(3) = b(2) \* (-3) $$ 3. b(2) değerini bilmiyoruz. Bu nedenle, n = 2 değerini formülde yerine koyun: $$ b(2) = b(2-1) \* (-3) $$  $$ b(2) = b(1) \* (-3) $$ 4. b(1) değerinin 15 olduğunu biliyoruz. Bu nedenle, formülde yerine koyalım: $$ b(2) = 15 \* (-3) $$  $$ b(2) = -45 $$ 5. b(2) değerini bildiğimize göre bunu b(3) formülünde yerine koyalım: $$ b(3) = b(2) \* (-3) $$  $$ b(3) = -45 \* (-3) $$  $$ b(3) = 135 $$ 6. Artık b(3) değerini bildiğimize göre bu değeri b(4) formülünde yerine koyabiliriz: $$ b(4) = b(3) \* (-3) $$  $$ b(4) = 135 \* (-3) $$  $$ b(4) = -405 $$   Bu nedenle, dizideki 4. terim -405'tir. |

Bu model yanıtı doğru. Yanıtı daha da kolaylaştırmak için modele adım adım düşünmesini söyleyebilirsiniz.

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Dizideki 4. terim nedir? Adım adım düşünün. | İlk terim 15'tir.  İkinci terim b(1) \* (-3) = 15 \* (-3) = -45 olur.  Üçüncü terim b(2) \* (-3) = -45 \* (-3) = 135'tir.  Dördüncü terim b(3) \* (-3) = 135 \* (-3) = -405 olur. |

### Çıkış biçimini belirtin

Model çıkışının belirli bir biçimde (ör.Markdown, JSON, HTML) olması gerektiğinde yaygın bir sorun yaşanır. Bu durum, özellikle model çıkışının sonraki bir görev tarafından alınması gerektiğinde ortaya çıkar. İstemde modeli bu biçimde çıkış üretmeye yönlendirerek bu biçimde çıkış üretmeyi deneyebilirsiniz. Aşağıda iki örnek verilmiştir:

| İstem | Model yanıtı |
| --- | --- |
| Bu resimdeki tabloyu Markdown biçiminde ayrıştır | ```none | Konu | Durum | Süre | Başlangıç tarihi | Son tarih | | ------- | ------ | ---- | ---------- | ------ | | Matematik | Tamamlandı | 1,5 saat | 29.11.2023 | 01.12.2023 | | Coğrafya | Tamamlandı | 30 dakika | 02.12.2023 | 04.12.2023 | | Fizik | Devam ediyor | 2 saat | 03.12.2023 | 05.12.2023 | | Biyoloji | Başlatılmadı | 6 saat | 02.11.2016 | 06.12.2023 | ``` |

| **İstem** | **Model yanıtı** |
| --- | --- |
| Aşağıdaki tüm özelliklerin listesini sağlayın:  Malzemeler, mutfak türü, vejetaryen olup olmadığı (JSON biçiminde) | ```json { "ingredients": [ "rice", "shrimp", "clams", "mussels", "peas", "tomatoes", "onions", "garlic", "olive oil", "paprika", "salt", "pepper" ], "type of cuisine": "Spanish", "vegetarian": false } ``` |

### Tek resim istemlerinde resminizi ön plana çıkarma

Gemini, istemdeki görüntü ve metni herhangi bir sırada yorumlayabilir ancak metin isteminden önce tek bir görüntü yerleştirmek daha iyi sonuçlar verebilir.
Aşağıdaki örneklerde, her istemde önce resmin, ardından metnin geldiğini göreceksiniz.

### Çok formatlı isteminizle ilgili sorunları giderme

Faydalı bir yanıt alamıyorsanız isteminizle ilgili sorunları gidermeniz gerekebilir. Deneyebileceğiniz birkaç strateji:

#### Model, resmin ilgili bölümünden bilgi almıyorsa

Daha ayrıntılı bir yanıt almak için istemin, yanıtını oluştururken hangi resim öğelerinden bilgi almasını istediğinizi belirtebilirsiniz.

| İstem | Model yanıtı |
| --- | --- |
| Bu bezler bir bebeğe kaç gün yeter? | Bezler bitmeden 198 gün boyunca kullanılabilir. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Bu bezler bitmeden ne kadar süre dayanır?  Çocuğun yaşını belirlemek için kutunun üzerinde gösterilen ağırlığı ve kutudaki toplam bebek bezi sayısını kullanın.  Toplam sayıyı, çocuğun günde kullandığı bez sayısına bölün. | Kutuda 198 adet bez bulunur. Kutuda, bezlerin 10-17 kg ağırlığındaki çocuklar için olduğu belirtiliyor.  Bu ağırlık aralığındaki ortalama bir çocuk muhtemelen 1-2 yaşlarındadır.  2 yaşındaki bir çocuk genellikle günde 6 bez kullanır. Bu nedenle, bezler yaklaşık 33 gün (198/6) dayanır. |

#### Model çıkışı çok genel ve resim girişine yeterince uyarlanmamışsa

Modelin yanıtını resimlere göre uyarlamasına yardımcı olmak için akıl yürütme görevini gerçekleştirmeden önce resimleri açıklamasını isteyin.

| İstem | Model yanıtı |
| --- | --- |
| Bu resimlerin ortak noktası nedir? | Dört resmin tamamı manzara fotoğrafı örnekleridir. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Öncelikle her resimde ne olduğunu ayrıntılı olarak açıklayın. Bu resimlerin ortak noktası nedir? | İlk resimde, bir kişinin bavul hazırladığı gösteriliyor. İkinci resimde, bir alışveriş merkezindeki boş koridor gösteriliyor. Üçüncü resimde bir rulo tuvalet kağıdı gösteriliyor. Dördüncü resimde karanlık ve fırtınalı bir deniz gösteriliyor.  Bu resimlerin ortak özelliği, hepsinin geçiş alanlarına örnek olmasıdır. Geçiş alanları, iki yer veya durum arasında kalan yerler ya da durumlardır. Genellikle belirsizlik veya muğlaklık hissiyle karakterize edilirler.  İlk resimde, kişinin evde ve seyahatte olduğu gösteriliyor. İkinci resimde, iki mağaza arasındaki koridor gösteriliyor. Üçüncü resimde, banyoyu temsil edebilecek tuvalet kağıdı gösteriliyor. Banyo, özel ve kamusal alanlar arasında geçiş yapılan bir yerdir. Dış dünyaya girerken veya dış dünyadan çıkarken kendimizi hazırladığımız bir yerdir.  Dördüncü resimde, sakin ve fırtınalı deniz arasında bir geçiş gösteriliyor.  Geçiş alanları hem heyecan verici hem de rahatsız edici olabilir. Yeni başlangıçların veya sonların yeri olabilirler. Bunlar, düşünme veya harekete geçme yeri olabilir. |

Ayrıca modelden, resimdeki içeriğe açıkça atıfta bulunmasını da isteyebilirsiniz.

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Bu resimlerin ortak noktası nedir? Yanıtınızda resimlerdeki içeriklere atıfta bulunun. | Resimlerin tamamı seyahatle ilgili. İlk resimde valiz hazırlayan bir kişi, ikinci resimde alışveriş merkezindeki boş bir koridor, üçüncü resimde bir rulo tuvalet kağıdı, dördüncü resimde ise karanlık ve fırtınalı bir deniz gösteriliyor.  Bu resimlerin hepsi seyahatle ilgili çünkü seyahat edenlerin ihtiyaç duyduğu veya kullandığı şeyler. İlk resimde, bir valizi hazırlayan bir kişi gösteriliyor. Bu, insanların seyahate çıkarken yaptığı bir şeydir. İkinci resimde, insanların seyahatleri için eşya satın almak üzere sık sık gittiği bir yer olan alışveriş merkezindeki boş bir koridor gösteriliyor. Üçüncü resimde, insanların seyahat ederken sıkça kullandığı bir ürün olan tuvalet kağıdı rulosu gösteriliyor. Dördüncü resimde, insanların seyahat ederken sıkça karşılaştığı bir durum olan karanlık ve fırtınalı bir deniz gösteriliyor. |

Aynı ipuçları, resimlerden elde edilen reklam öğesi çıkışları için de geçerlidir. Tavşanın yer aldığı aşağıdaki örnekte, modelden resimdeki unsurları dahil etmesini açıkça istemek çıkışı iyileştirebilir.

| İstem | Model yanıtı |
| --- | --- |
| Bu resim hakkında bir şiir yazabilir misin? | Küçük tavşan, yumuşacık ve kahverengi,  Tarlada zıplıyor, yukarı ve aşağı.  Kulakların uzun, kuyruğun küçük,  Sen hepsinin en tatlısısın.  Yeşil ve tatlı çimleri yersin,  Beni görünce de zıplayarak uzaklaşırsın.  Ama her zaman arkadaşın olacağım,  Küçük tavşan, sonuna kadar. |

| **Güncellenen istem** | **İyileştirilmiş yanıt** |
| --- | --- |
| Bu resim hakkında, yeri de belirterek betimleyici ve etkileyici bir şiir yazabilir misin? | Çayırda küçük bir tavşan,  Kulakları çok uzun, çok keskin.  Uzakta, baktığın yerde ne görüyorsun?  Is it the ocean blue,  Sparkling in the sun's hue?  Ya da dalgaların çarpıp kükremesi,  Bayıldığınız bir ritim?  Küçük tavşan, doğruyu söyle bana,  İlginizi bu kadar çok çeken şey ne?  Tuzlu esinti mi,  Yoksa martıların çığlıkları mı hoşunuza gidiyor?  Belki de her şeyin büyüklüğüdür,  Dünya hem çok büyük hem de çok küçük.  Hayallerin dolaşabileceği,  Maceraların ekilebileceği bir yer.  Küçük tavşan, ne hayal ettiğini merak ediyorum,  Çimlerin üzerinde otururken, çok sakinsin.  Derinlikleri keşfetmek mi istersin,  Yoksa karada kalıp zıplamayı mı?  Ne olursa olsun, küçük tavşan,  Merak kıvılcımını parlak bir şekilde yakmaya devam et.  Çünkü hayallerinizde ve arzularınızda,  Yaratılmayı bekleyen bir dünya var. |

#### İstemin hangi bölümünün başarısız olduğunu belirleme

Bir istemin başarısız olmasının nedeni, modelin **görüntüyü anlamaması** mı yoksa görüntüyü anlamasına rağmen doğru **akıl yürütme adımlarını** uygulamaması mı, bunu anlamak zor olabilir.
Bu nedenleri netleştirmek için modele resimde ne olduğunu sorun.

Aşağıdaki örnekte, model çayla birlikte şaşırtıcı görünen bir atıştırmalıkla (ör. patlamış mısır) yanıt verirse önce modelin resimde çay olduğunu doğru tanıyıp tanımadığını belirlemek için sorun giderme işlemi yapabilirsiniz.

| İstem | Sorun giderme istemi |
| --- | --- |
| Bununla iyi gidecek, 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? | Bu resimde ne olduğunu açıklayın. |

Diğer bir strateji ise modelden gerekçesini açıklamasını istemektir. Bu, muhakemenin hangi kısmının (varsa) bozulduğunu daraltmanıza yardımcı olabilir.

| İstem | Sorun giderme istemi |
| --- | --- |
| Bununla iyi gidecek, 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? | Bununla iyi gidecek, 1 dakikada hazırlayabileceğim bir atıştırmalık önerir misin? Lütfen nedeniyle birlikte açıklayın. |

## Sırada ne var?

- [Google AI Studio](http://aistudio.google.com?hl=tr)'yu kullanarak kendi çok formatlı istemlerinizi yazmayı deneyin.
- Medya dosyalarını yüklemek ve istemlerinize dahil etmek için Gemini Files API'yi kullanma hakkında bilgi edinmek üzere [Vision](https://ai.google.dev/gemini-api/docs/vision?hl=tr), [Audio](https://ai.google.dev/gemini-api/docs/audio?hl=tr) ve [Document processing](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) kılavuzlarına bakın.
- İstem tasarımıyla ilgili daha fazla bilgi (ör. örnekleme parametrelerini ayarlama) için [İstem stratejileri](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=tr) sayfasına bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-06 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-06 UTC."],[],[]]
