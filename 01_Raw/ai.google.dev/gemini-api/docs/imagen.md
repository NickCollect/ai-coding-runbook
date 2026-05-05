---
source_url: https://ai.google.dev/gemini-api/docs/imagen?hl=tr
fetched_at: 2026-05-05T20:10:05.155307+00:00
title: "Imagen'i kullanarak resim olu\u015fturma \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Imagen'i kullanarak resim oluşturma

Imagen, Google'ın yüksek kaliteli görüntü üretme modelidir. Metin istemlerinden gerçekçi ve yüksek kaliteli görüntüler üretebilir. Üretilen tüm görüntülerde SynthID filigranı bulunur. Kullanılabilen Imagen modeli varyantları hakkında daha fazla bilgi edinmek için [Model sürümleri](#model-versions) bölümüne bakın.

## Imagen modellerini kullanarak resim üretme

Bu örnekte, [Imagen modeliyle](https://deepmind.google/technologies/imagen/?hl=tr) görüntü oluşturma gösterilmektedir:

### Python

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

response = client.models.generate_images(
    model='imagen-4.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  generated_image.image.show()
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({});

  const response = await ai.models.generateImages({
    model: 'imagen-4.0-generate-001',
    prompt: 'Robot holding a red skateboard',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
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
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  config := &genai.GenerateImagesConfig{
      NumberOfImages: 4,
  }

  response, _ := client.Models.GenerateImages(
      ctx,
      "imagen-4.0-generate-001",
      "Robot holding a red skateboard",
      config,
  )

  for n, image := range response.GeneratedImages {
      fname := fmt.Sprintf("imagen-%d.png", n)
          _ = os.WriteFile(fname, image.Image.ImageBytes, 0644)
  }
}
```

### REST

```
curl -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "instances": [
          {
            "prompt": "Robot holding a red skateboard"
          }
        ],
        "parameters": {
          "sampleCount": 4
        }
      }'
```

![Kırmızı kaykay tutan bir robotun yapay zekayla üretilmiş görüntüsü](https://ai.google.dev/static/gemini-api/docs/images/robot-skateboard.png?hl=tr)

Kırmızı kaykay tutan bir robotun yapay zekayla üretilmiş görüntüsü

### Imagen yapılandırması

Imagen şu anda yalnızca İngilizce istemleri ve aşağıdaki parametreleri desteklemektedir:

- `numberOfImages`: Oluşturulacak resim sayısı (1-4 arası).
  Varsayılan değer 4'tür.
- `imageSize`: Üretilen resmin boyutu. Bu özellik yalnızca Standart ve Ultra modellerinde desteklenir. Desteklenen değerler `1K` ve `2K`'dir.
  Varsayılan değer `1K`'dır.
- `aspectRatio`: Oluşturulan resmin en boy oranını değiştirir. Desteklenen değerler: `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"` ve `"16:9"`. Varsayılan değer: `"1:1"`.
- `personGeneration`: Modelin insan resimleri oluşturmasına izin verin. Aşağıdaki değerler desteklenir:

  - `"dont_allow"`: İnsanların yer aldığı görüntülerin üretilmesini engelleme
  - `"allow_adult"`: Çocukların değil, yetişkinlerin resimlerini üretin. Bu, varsayılan seçenektir.
  - `"allow_all"`: Yetişkinlerin ve çocukların yer aldığı görüntüler üretme

## Imagen istem rehberi

Imagen kılavuzunun bu bölümünde, metinden görüntü oluşturma istemini değiştirmenin nasıl farklı sonuçlar verebileceği ve oluşturabileceğiniz resim örnekleri gösterilmektedir.

### İstem yazmayla ilgili temel bilgiler

İyi bir istem açıklayıcı ve net olmalı, anlamlı anahtar kelimeler ve değiştiriciler kullanmalıdır. **Özne**, **bağlam** ve **stil** hakkında düşünerek başlayın.

![Konu, bağlam ve stilin vurgulandığı istem](https://ai.google.dev/static/gemini-api/docs/images/imagen/style-subject-context.png?hl=tr)

Resim metni: *Gökdelenlerle* (**bağlam ve arka plan**) çevrili bir *modern apartman binasının* (**konu**) *eskizi* (**stil**).

1. **Özne**: Her istemde ilk olarak *özneyi* düşünmeniz gerekir. Bu, resmini istediğiniz nesne, kişi, hayvan veya manzaradır.
2. **Bağlam ve arka plan:** Konunun yerleştirileceği *arka plan veya bağlam* da aynı derecede önemlidir. Öznenizi çeşitli arka planlara yerleştirmeyi deneyin. Örneğin, beyaz arka planlı bir stüdyo, dış mekan veya iç mekan ortamları.
3. **Stil:** Son olarak, istediğiniz resim stilini ekleyin. *Stiller* genel (tablo, fotoğraf, eskiz) veya çok özel (pastel boya, kömür çizimi, izometrik 3D) olabilir. Stilleri de birleştirebilirsiniz.

İstemin ilk sürümünü yazdıktan sonra, istediğiniz görüntüye ulaşana kadar daha fazla ayrıntı ekleyerek isteminizi iyileştirin. Tekrar önemlidir.
Önce temel fikrinizi belirleyin, ardından oluşturulan resim vizyonunuza yakın olana kadar bu temel fikri iyileştirin ve genişletin.

|  |  |  |
| --- | --- | --- |
| gerçekçi örnek resim 1   İstem: İlkbaharda bir gölün yanındaki park | Fotoğraf gerçekliğinde örnek resim 2   İstem: İlkbaharda bir gölün yanındaki park, **güneş gölün üzerinde batıyor, altın saat** | gerçekçi örnek resim 3   İstem: İlkbaharda bir gölün kenarındaki park, ***güneş gölün üzerinde batıyor, altın saat, kırmızı kır çiçekleri*** |

Imagen modelleri, istemleriniz kısa veya uzun ve ayrıntılı olsa da fikirlerinizi ayrıntılı görüntülere dönüştürebilir. Mükemmel sonucu elde edene kadar ayrıntı ekleyerek istemleri yineleyin ve vizyonunuzu geliştirin.

|  |  |
| --- | --- |
| Kısa istemler, hızlı bir şekilde resim üretmenize olanak tanır.  Imagen 4 kısa istem örneği   İstem: 20'li yaşlarında bir kadının yakın çekim fotoğrafı, sokak fotoğrafı, film karesi, soluk turuncu sıcak tonlar | Daha uzun istemler, belirli ayrıntılar eklemenize ve görüntünüzü oluşturmanıza olanak tanır.  Imagen 4 uzun istem örneği   İstem: Sokak fotoğrafçılığı tarzında çekilmiş, 20'li yaşlarında bir kadının büyüleyici fotoğrafı. Resim, turuncu ve sıcak tonların kullanıldığı bir film karesi gibi görünmeli. |

Imagen istemi yazmayla ilgili ek öneriler:

- **Açıklayıcı bir dil kullanın**: Imagen'e net bir resim sunmak için ayrıntılı sıfatlar ve zarflar kullanın.
- **Bağlam bilgisi verin**: Gerekirse yapay zekanın anlamasına yardımcı olmak için arka plan bilgilerini ekleyin.
- **Belirli sanatçılardan veya stillerden bahsedin**: Aklınızda belirli bir estetik varsa belirli sanatçılardan veya sanat akımlarından bahsetmek faydalı olabilir.
- **İstem mühendisliği araçlarını kullanın**: İstemlerinizi hassaslaştırmanıza ve en iyi sonuçları elde etmenize yardımcı olacak istem mühendisliği araçlarını veya kaynaklarını inceleyin.
- **Kişisel ve grup resimlerinizdeki yüz ayrıntılarını iyileştirme**: Yüz ayrıntılarını fotoğrafın odak noktası olarak belirtin (örneğin, istemde "portre" kelimesini kullanın).

### Resimlerde metin oluşturma

Imagen modelleri, resimlere metin ekleyerek daha yaratıcı görüntü üretme olanakları sunar. Bu özellikten en iyi şekilde yararlanmak için aşağıdaki bilgileri kullanın:

- **Güvenle yineleme yapın**: İstediğiniz görünümü elde edene kadar görüntüleri yeniden oluşturmanız gerekebilir. Imagen'in metin entegrasyonu hâlâ gelişmektedir ve bazen birden fazla deneme en iyi sonuçları verir.
- **Kısa tutun**: En iyi sonuç için metni 25 karakterle sınırlayın.
- **Birden fazla ifade**: Ek bilgi sağlamak için iki veya üç farklı ifadeyle denemeler yapın. Daha net kompozisyonlar için üç ifadeyi aşmayın.

  ![Imagen 4 ile metin oluşturma örneği](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_generate-text.png?hl=tr)

  İstem: Başlık olarak kalın yazı tipiyle "Summerland" metninin yer aldığı bir poster. Bu metnin altında "Summer never felt so good" (Yaz hiç bu kadar güzel olmamıştı) sloganı yer alıyor.
- **Kılavuz Yerleşimi**: Imagen, metni yönlendirildiği şekilde yerleştirmeye çalışsa da zaman zaman farklılıklar olabilir. Bu özellik sürekli olarak geliştirilmektedir.
- **Inspire yazı tipi stili**: Imagen'in seçimlerini ince bir şekilde etkilemek için genel bir yazı tipi stili belirtin. Yazı tipinin bire bir kopyalanmasını beklemeyin ancak yaratıcı yorumlar bekleyebilirsiniz.
- **Yazı tipi boyutu**: Yazı tipi boyutu oluşturmayı etkilemek için bir yazı tipi boyutu veya genel bir boyut göstergesi (örneğin, *küçük*, *orta*, *büyük*) belirtin.

### İstem parametrelendirme

Çıkış sonuçlarını daha iyi kontrol etmek için Imagen'e girişleri parametrelendirmeniz faydalı olabilir. Örneğin, müşterilerinizin işletmeleri için logo oluşturabilmesini ve logoların her zaman düz renk bir arka plan üzerinde oluşturulmasını istediğinizi varsayalım. Ayrıca, müşterinin menüden seçebileceği seçenekleri de sınırlamak istiyorsunuz.

Bu örnekte, aşağıdakine benzer şekilde parametreli bir istem oluşturabilirsiniz:

```
A {logo_style} logo for a {company_area} company on a solid color background. Include the text {company_name}.
```

Müşteri, özel kullanıcı arayüzünüzde bir menü kullanarak parametreleri girebilir ve seçtiği değer, Imagen'in aldığı istemi doldurur.

Örneğin:

1. İstem: `A minimalist logo for a health care company on a solid color background. Include the text Journey.`

   ![Imagen 4 istem parametreleştirme örneği 1](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_healthcare.png?hl=tr)
2. İstem: `A modern logo for a software company on a solid color background. Include the text Silo.`

   ![Imagen 4 istem parametrelendirme örneği 2](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_software.png?hl=tr)
3. İstem: `A traditional logo for a baking company on a solid color background. Include the text Seed.`

   ![Imagen 4 istem parametreleştirme örneği 3](https://ai.google.dev/static/gemini-api/docs/images/imagen/imagen3_prompt-param_baking.png?hl=tr)

### Gelişmiş istem yazma teknikleri

Fotoğrafçılık tanımlayıcıları, şekiller ve malzemeler, tarihi sanat akımları ve resim kalitesi değiştiricileri gibi özelliklere dayalı daha spesifik istemler oluşturmak için aşağıdaki örnekleri kullanın.

#### Fotoğrafçılık

- İstem şunları içerir: *"... fotoğrafı"*

Bu stili kullanmak için Imagen'a fotoğraf aradığınızı net bir şekilde belirten anahtar kelimelerle başlayın. İstemlerinize *"Şunun fotoğrafı:" ifadesiyle başlayın. . ."*. Örneğin:

|  |  |  |
| --- | --- | --- |
| gerçekçi örnek resim 1   İstem: **Mutfakta ahşap bir yüzeyin üzerinde** kahve çekirdeklerinin  fotoğrafı | Fotoğraf gerçekliğinde örnek resim 2   İstem: Mutfak tezgahında **bir** çikolata çubuğunun | gerçekçi örnek resim 3   İstem: Arka planda su bulunan modern bir binanın **fotoğrafı** |

Resim kaynağı: Her resim, Imagen 4 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

##### Fotoğrafçılık değiştiricileri

Aşağıdaki örneklerde, fotoğrafa özel çeşitli değiştiricileri ve parametreleri görebilirsiniz. Daha hassas kontrol için birden fazla değiştiriciyi birleştirebilirsiniz.

1. **Kamera Yakınlığı** - *Uzaktan çekilen yakın çekim*

   |  |  |
   | --- | --- |
   | yakın çekim kamera örnek resmi   İstem: Kahve çekirdeklerinin **yakın çekim** fotoğrafı | Uzaklaştırılmış kamera örnek resmi   İstem: Dağınık bir mutfakta küçük bir kahve çekirdeği torbasının **uzaklaştırılmış** fotoğrafı |
2. **Kamera Konumu** - *aerial, from below* (havadan, aşağıdan)

   |  |  |
   | --- | --- |
   | Kuş bakışı fotoğraf örneği   İstem: Gökdelenlerin bulunduğu bir şehir merkezinin **havadan fotoğrafı** | alttan görünüm örnek resmi   İstem: **Aşağıdan çekilmiş, mavi gökyüzünün göründüğü bir orman örtüsü fotoğrafı aşağıdan** |
3. **Işıklandırma**: *doğal, dramatik, sıcak, soğuk*

   |  |  |
   | --- | --- |
   | doğal ışıklandırma örnek resmi   İstem: Modern bir koltuğun stüdyo fotoğrafı, **doğal ışıklandırma** | Etkileyici aydınlatma örnek resmi   İstem: Modern bir koltuğun **etkileyici ışıklandırmayla** çekilmiş stüdyo fotoğrafı |
4. **Kamera Ayarları** *- hareket bulanıklığı, Odağı Yumuşat, bokeh, portre*

   |  |  |
   | --- | --- |
   | hareket bulanıklığı örnek resmi   İstem: **Hareket bulanıklığı** olan bir arabanın içinden çekilmiş, gökdelenlerle dolu bir şehir fotoğrafı | Odağı Yumuşat örnek resmi   İstem: Gece, şehirdeki bir köprünün **odağı yumuşatılmış** fotoğrafı |
5. **Lens türleri** - *35 mm, 50 mm, balık gözü, geniş açı, makro*

   |  |  |
   | --- | --- |
   | Makro lens örnek resmi   İstem: Yaprak fotoğrafı, **makro lens** | Balık gözü lens örnek resmi   İstem: sokak fotoğrafçılığı, New York, **balık gözü lens** |
6. **Film türleri** - *siyah beyaz, polaroid*

   |  |  |
   | --- | --- |
   | polaroid fotoğraf örneği resim   İstem: Güneş gözlüğü takan bir köpeğin **Polaroid portresi** | siyah beyaz fotoğraf örneği   İstem: Güneş gözlüğü takan bir köpeğin **siyah beyaz fotoğrafı** |

Resim kaynağı: Her resim, Imagen 4 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

### İllüstrasyon ve sanat

- İstem şunları içerir: *"... painting resmi"*, *"Bir sketch..."*

Sanat stilleri, kurşun kalemle çizilmiş eskizler gibi tek renkli stillerden hiper gerçekçi dijital sanat eserlerine kadar çeşitlilik gösterir. Örneğin, aşağıdaki resimlerde farklı stillerle aynı istem kullanılmıştır:

*"Arka planda gökdelenler olan, köşeli ve sportif bir elektrikli sedanın [art style or creation technique] resmi"*

|  |  |  |
| --- | --- | --- |
| Sanat örnek resimleri   İstem: Köşeli bir...**teknik kalem çizimi** | Sanat örnek resimleri   İstem: Köşeli bir...**karakalem çizimi** | Sanat örnek resimleri   İstem: Köşeli bir...**renkli kalem çizimi** |

|  |  |  |
| --- | --- | --- |
| Sanat örnek resimleri   İstem: Köşeli bir...**pastel boya resmi** | Sanat örnek resimleri   İstem: Köşeli bir...**dijital sanatı** | Sanat örnek resimleri   İstem: Köşeli bir...**art deco (poster)** |

Resim kaynağı: Her resim, Imagen 2 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

##### Şekiller ve malzemeler

- İstem şunları içeriyor: *"...yapılmış..."*, *"...şeklinde..."*

Bu teknolojinin güçlü yönlerinden biri, başka şekilde zor veya imkansız olan görüntüler oluşturabilmenizdir. Örneğin, şirket logonuzu farklı materyaller ve dokularla yeniden oluşturabilirsiniz.

|  |  |  |
| --- | --- | --- |
| Şekiller ve materyaller örneği resim 1   İstem: **Peynirden yapılmış** bir spor çantası | şekiller ve malzemeler örneği resim 2   İstem: Kuş **şeklinde** neon tüpler | şekiller ve malzemeler örneği resim 3   İstem: **kağıttan yapılmış** bir koltuk, stüdyo fotoğrafı, origami tarzı |

Resim kaynağı: Her resim, Imagen 4 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

#### Tarihi sanat referansları

- İstem şunları içeriyor: *"...tarzında..."*

Bazı stiller yıllar içinde ikonik hale geldi. Aşağıda, deneyebileceğiniz bazı tarihi resim veya sanat tarzları hakkında fikirler verilmiştir.

*"[art period or movement]
 tarzında bir resim üret: rüzgar çiftliği"*

|  |  |  |
| --- | --- | --- |
| empresyonizm örneği resim   İstem: **Empresyonist bir tablo *stilinde*** resim üretme: rüzgar çiftliği | Rönesans dönemi örneği   İstem: **Rönesans dönemi tablosu *stilinde*** bir rüzgar santrali resmi oluştur | pop art örnek resmi   İstem: **Pop art*tarzında*** bir rüzgar çiftliği görüntüsü oluştur |

Resim kaynağı: Her resim, Imagen 4 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

#### Resim kalitesi değiştiricileri

Belirli anahtar kelimeler, modelin yüksek kaliteli bir öğe aradığınızı anlamasını sağlayabilir. Kalite değiştiricilere örnek olarak şunlar verilebilir:

- **Genel Değiştiriciler** - *yüksek kaliteli, güzel, stilize edilmiş*
- **Fotoğraflar** - *4K, HDR, Studio Photo*
- **Sanat, İllüstrasyon** - *Profesyonel, ayrıntılı*

Aşağıda, kalite değiştiricileri içermeyen istemlere ve aynı istemin kalite değiştiricileri içeren versiyonuna dair birkaç örnek verilmiştir.

|  |  |
| --- | --- |
| Değiştiriciler olmadan mısır örneği resmi   İstem (kalite değiştiriciler yok): Mısır koçanı fotoğrafı | Değiştiricilerle birlikte mısır örneği resmi   İstem (kalite değiştiricilerle): **4K HDR kalitesinde**   bir mısır koçanı fotoğrafı **çeken bir   profesyonel fotoğrafçı** |

Resim kaynağı: Her resim, Imagen 4 modeliyle ilgili metin istemi kullanılarak oluşturulmuştur.

#### En boy oranları

Imagen ile görüntü üretme özelliği, beş farklı görüntü en-boy oranı ayarlamanıza olanak tanır.

1. **Kare** (1:1, varsayılan): Standart bir kare fotoğraf. Bu en boy oranının yaygın kullanım alanları arasında sosyal medya gönderileri yer alır.
2. **Tam ekran** (4:3): Bu en boy oranı genellikle medyada veya filmlerde kullanılır.
   Ayrıca çoğu eski (geniş ekran olmayan) TV'nin ve orta formatlı kameraların boyutlarıdır. Yatay olarak daha fazla sahneyi yakalar (1:1 ile karşılaştırıldığında). Bu nedenle, fotoğrafçılık için tercih edilen en boy oranıdır.

   |  |  |
   | --- | --- |
   | en boy oranı örneği   İstem: Piyano çalan bir müzisyenin parmaklarının yakın çekimi, siyah beyaz film, vintage (4:3 en boy oranı) | en-boy oranı örneği   İstem: Lüks bir restoran için patates kızartmasının yemek dergisi tarzında profesyonel bir stüdyo fotoğrafı (4:3 en-boy oranı) |
3. **Dikey tam ekran** (3:4): Bu, 90 derece döndürülmüş tam ekran en boy oranıdır. Bu sayede, 1:1 en boy oranına kıyasla sahnenin daha fazlası dikey olarak yakalanabilir.

   |  |  |
   | --- | --- |
   | en boy oranı örneği   İstem: Yürüyüş yapan bir kadın, botlarının bir su birikintisine yansıyan yakın çekimi, arka planda büyük dağlar, reklam tarzında, dramatik açılar (3:4 en-boy oranı) | en boy oranı örneği   İstem: mistik bir vadide akan nehrin havadan çekilmiş fotoğrafı (3:4 en-boy oranı) |
4. **Geniş ekran** (16:9): Bu oran, 4:3'ün yerini almıştır ve artık TV'ler, monitörler ve cep telefonu ekranları (yatay) için en yaygın en boy oranıdır.
   Arka planın daha fazlasını (ör. manzaralar) yakalamak istediğinizde bu en boy oranını kullanın.

   ![en boy oranı örneği](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_16-9_man.png?hl=tr)

   İstem: Plajda oturan, baştan aşağı beyaz giyinmiş bir adam, yakın çekim, altın saat ışığı (16:9 en-boy oranı)
5. **Dikey** (9:16): Bu oran, geniş ekranın döndürülmüş halidir. Bu, kısa video uygulamaları (ör. YouTube Shorts) tarafından popüler hale getirilen nispeten yeni bir en-boy oranıdır. Binalar, ağaçlar, şelaleler veya benzeri diğer nesneler gibi güçlü dikey yönlere sahip uzun nesneler için kullanın.

   ![en boy oranı örneği](https://ai.google.dev/static/gemini-api/docs/images/imagen/aspect-ratios_9-16_skyscraper.png?hl=tr)

   İstem: Arka planda güzel bir gün batımı olan, devasa, modern, görkemli ve destansı bir gökdelenin dijital görüntüsü (9:16 en-boy oranı)

#### Fotoğraf gerçekliğinde görüntüler

Görüntü üretme modelinin farklı sürümleri, sanatsal ve fotogerçekçi çıkışların bir karışımını sunabilir. Oluşturmak istediğiniz konuya göre daha fotogerçekçi sonuçlar elde etmek için istemlerde aşağıdaki ifadeleri kullanın.

| Kullanım alanı | Lens türü | Odak uzaklıkları | Ek bilgiler |
| --- | --- | --- | --- |
| Kişiler (portreler) | Asal sayı, yakınlaştırma | 24-35mm | Siyah beyaz film, Film noir, Alan derinliği, Çift tonlu (iki renkten bahsedin) |
| Yiyecek, böcek, bitki (nesneler, natürmort) | Makro | 60-105mm | Yüksek ayrıntı, hassas odaklama, kontrollü ışıklandırma |
| Spor, vahşi yaşam (hareket) | Telefoto yakınlaştırma | 100-400mm | Yüksek deklanşör hızı, aksiyon veya hareket takibi |
| Astronomik, manzara (geniş açı) | Geniş Açı | 10-24mm | Uzun pozlama süreleri, keskin odak, uzun pozlama, pürüzsüz su veya bulutlar |

##### Portreler

| Kullanım alanı | Lens türü | Odak uzaklıkları | Ek bilgiler |
| --- | --- | --- | --- |
| Kişiler (portreler) | Asal sayı, yakınlaştırma | 24-35mm | Siyah beyaz film, Film noir, Alan derinliği, Çift tonlu (iki renkten bahsedin) |

Imagen, tablodaki birkaç anahtar kelimeyi kullanarak aşağıdaki portreleri oluşturabilir:

|  |  |  |  |
| --- | --- | --- | --- |
| portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği |

İstem: *35 mm portre, mavi ve gri çift tonlu bir kadın*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği | portre fotoğrafçılığı örneği |

İstem: *35 mm portre, film noir tarzında bir kadın*  
Model: `imagen-4.0-generate-001`

##### Nesneler

| Kullanım alanı | Lens türü | Odak uzaklıkları | Ek bilgiler |
| --- | --- | --- | --- |
| Yiyecek, böcek, bitki (nesneler, natürmort) | Makro | 60-105mm | Yüksek ayrıntı, hassas odaklama, kontrollü ışıklandırma |

Imagen, tablodaki birkaç anahtar kelimeyi kullanarak aşağıdaki nesne resimlerini oluşturabilir:

|  |  |  |  |
| --- | --- | --- | --- |
| Nesne fotoğrafı örneği | Nesne fotoğrafı örneği | Nesne fotoğrafı örneği | Nesne fotoğrafı örneği |

İstem: *leaf of a prayer plant, macro lens, 60mm*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| Nesne fotoğrafı örneği | Nesne fotoğrafı örneği | Nesne fotoğrafı örneği | Nesne fotoğrafı örneği |

İstem: *a plate of pasta, 100mm Macro lens*  
Model: `imagen-4.0-generate-001`

##### Hareket

| Kullanım alanı | Lens türü | Odak uzaklıkları | Ek bilgiler |
| --- | --- | --- | --- |
| Spor, vahşi yaşam (hareket) | Telefoto yakınlaştırma | 100-400mm | Yüksek deklanşör hızı, aksiyon veya hareket takibi |

Imagen, tablodaki birkaç anahtar kelimeyi kullanarak aşağıdaki hareketli görüntüleri oluşturabilir:

|  |  |  |  |
| --- | --- | --- | --- |
| hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği |

İstem: *a winning touchdown, hızlı deklanşör hızı, hareket takibi*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği | hareketli fotoğrafçılık örneği |

İstem: *Ormanda koşan bir geyik, yüksek deklanşör hızı, hareket takibi*  
Model: `imagen-4.0-generate-001`

##### Geniş Açı

| Kullanım alanı | Lens türü | Odak uzaklıkları | Ek bilgiler |
| --- | --- | --- | --- |
| Astronomik, manzara (geniş açı) | Geniş Açı | 10-24mm | Uzun pozlama süreleri, keskin odak, uzun pozlama, pürüzsüz su veya bulutlar |

Tablodaki birkaç anahtar kelimeyi kullanarak Imagen, aşağıdaki geniş açılı fotoğrafları oluşturabilir:

|  |  |  |  |
| --- | --- | --- | --- |
| Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği |

İstem: *an expansive mountain range, landscape wide angle 10mm*  
Model: `imagen-4.0-generate-001`

|  |  |  |  |
| --- | --- | --- | --- |
| Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği | Geniş açılı fotoğraf örneği |

İstem: *Ayın fotoğrafı, astro fotoğrafçılık, 10 mm geniş açı*  
Model: `imagen-4.0-generate-001`

## Model sürümleri

### Imagen 4

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | **Gemini API**  `imagen-4.0-generate-001`  `imagen-4.0-ultra-generate-001`  `imagen-4.0-fast-generate-001` |
| saveDesteklenen veri türleri | **Giriş**  Metin  **Çıkış**  Resimler |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  480 jeton (metin)  **Çıkış resimleri**  1 ila 4 (Ultra/Standart/Hızlı) |
| calendar\_monthSon güncelleme | Haziran 2025 |

### Imagen 3

Imagen 3 modeli [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
