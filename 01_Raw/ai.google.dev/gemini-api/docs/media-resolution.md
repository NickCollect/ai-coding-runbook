---
source_url: https://ai.google.dev/gemini-api/docs/media-resolution?hl=tr
fetched_at: 2026-10-12T06:50:42.852407+00:00
title: "Medya \u00e7\u00f6z\u00fcn\u00fcrl\u00fc\u011f\u00fc \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Medya çözünürlüğü

`media_resolution` parametresi, medya girişleri için ayrılan **maksimum jeton sayısını** belirleyerek Gemini API'nin resim, video, ses ve PDF belgeleri gibi medya girişlerini nasıl işleyeceğini kontrol eder. Bu sayede, yanıt kalitesini gecikme ve maliyetle dengelemenize olanak tanır. Görsel ve belge girişleri, çözünürlük ayarına göre jeton dağıtımını ölçeklendirirken ses girişleri, tüm çözünürlük seviyelerinde saniyede sabit bir hızda jetonlaştırılır. Farklı ayarlar, varsayılan değerler ve bunların jetonlarla nasıl eşleştiği hakkında bilgi edinmek için [Jeton sayıları](#token-counts) bölümüne bakın.

İsteğinizdeki (yalnızca Gemini 3) medya çözünürlüğünü tek tek medya nesneleri (içerik öğeleri) için yapılandırabilirsiniz.

## İçerik öğesi başına medya çözünürlüğü (yalnızca Gemini 3)

Gemini 3, isteğinizdeki her bir medya nesnesi için medya çözünürlüğünü ayarlamanıza olanak tanır ve jeton kullanımında ayrıntılı optimizasyon sunar. Tek bir istekte çözünürlük düzeylerini karıştırabilirsiniz. Örneğin, karmaşık bir şema için yüksek çözünürlük, basit bir bağlamsal resim için düşük çözünürlük kullanabilirsiniz.

### Python

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/image.jpg")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=[
        {"type": "text", "text": "Describe this image:"},
        {
            "type": "image",
            "uri": myfile.uri,
            "mime_type": myfile.mime_type,
            "resolution": "high"
        }
    ]
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/image.jpg",
    config: { mime_type: "image/jpeg" },
  });

  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: [
      { type: "text", text: "Describe this image:" },
      {
        type: "image",
        uri: myfile.uri,
        mime_type: myfile.mimeType,
        resolution: "high"
      }
    ],
  });
  console.log(interaction.output_text);
}

await main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.Content;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.ImageContent;
import com.google.genai.gaos.models.interactions.ImageContentMimeType;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.interactions.TextContent;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.List;

Client client = new Client();

Content textContent = TextContent.builder().text("Describe the details in this high-resolution image.").build();
Content imageContent =
    ImageContent.builder()
        .uri("gs://cloud-samples-data/generative-ai/image/scones.jpg")
        .mimeType(ImageContentMimeType.IMAGE_JPEG)
        .build();

List<Content> contents = Arrays.asList(textContent, imageContent);

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.ofContent(contents))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

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

    uploadedFile, err := client.Files.UploadFromPath(ctx, "path/to/image.jpg", nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput([]interactions.Content{
                interactions.NewContent(interactions.TextContent{
                    Text: "Describe the details in this high-resolution image.",
                }),
                interactions.NewContent(interactions.ImageContent{
                    URI:        genai.Ptr(uploadedFile.URI),
                    MimeType:   interactions.ImageContentMimeType(uploadedFile.MIMEType).ToPointer(),
                    Resolution: interactions.MediaResolutionHigh.ToPointer(),
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
# First upload the file using the Files API, then use the URI:
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.8-flash",
    "input": [
      {"type": "text", "text": "Describe this image:"},
      {
        "type": "image",
        "uri": "YOUR_FILE_URI",
        "mime_type": "image/jpeg",
        "resolution": "high"
      }
    ]
  }'
```

## Kullanılabilir çözünürlük değerleri

Gemini API, medya çözünürlüğü için aşağıdaki düzeyleri tanımlar:

- `unspecified`: Varsayılan ayardır. Bu seviyenin jeton sayısı, Gemini 3 ile önceki Gemini modelleri arasında önemli ölçüde farklılık gösterir.
- `low`: Daha düşük jeton sayısı, daha hızlı işlem ve daha düşük maliyetle sonuçlanır ancak daha az ayrıntı içerir.
- `medium`: Ayrıntı, maliyet ve gecikme arasında denge.
- `high`: Daha yüksek jeton sayısı, gecikme ve maliyet artışı karşılığında modelin çalışması için daha fazla ayrıntı sağlar.
- `ultra_high` (Yalnızca içerik öğesi başına): En yüksek jeton sayısıdır. [Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) gibi belirli kullanım alanları için gereklidir.

`high` seçeneğinin çoğu kullanım alanında optimum performans sağladığını unutmayın.

Bu seviyelerin her biri için oluşturulan jetonların tam sayısı hem **medya türüne** (resim, video, ses, PDF) hem de **model sürümüne** bağlıdır.

## Jeton sayıları

Aşağıdaki tablolarda, her model ailesi için her `media_resolution` değeri ve medya türüne ait yaklaşık jeton sayıları özetlenmektedir.

**Gemini 3 modelleri**

| MediaResolution | Resim | Video | Ses | PDF |
| --- | --- | --- | --- | --- |
| `unspecified` (Varsayılan) | 1120 | 70 | 25 (saniyede) | 560 |
| `low` | 280 | 70 | 25 (saniyede) | 280 + Yerel Metin |
| `medium` | 560 | 70 | 25 (saniyede) | 560 + Yerel Metin |
| `high` | 1120 | 280 | 25 (saniyede) | 1.120 + Yerel Metin |
| `ultra_high` | 2240 | Yok | Yok | Yok |

## Doğru çözünürlüğü seçme

- **Varsayılan (`unspecified`):** Varsayılanla başlayın. En yaygın kullanım alanlarında kalite, gecikme ve maliyet arasında iyi bir denge sağlamak için ayarlanmıştır.
- **`low`:** Maliyet ve gecikmenin çok önemli olduğu, ayrıntılı bilgilerin ise daha az kritik olduğu senaryolarda kullanılır.
- **`medium` / `high`:** Görev, medyada karmaşık ayrıntıların anlaşılmasını gerektirdiğinde çözünürlüğü artırın. Bu özellik genellikle karmaşık görsel analiz, grafik okuma veya yoğun belge anlama için gereklidir.
- **`ultra_high`**: Yalnızca içerik öğesi başına ayar için kullanılabilir. Bilgisayar kullanımı gibi belirli kullanım alanları veya testlerin `high` üzerinde net bir iyileşme gösterdiği durumlarda önerilir.
- **İçerik öğesi başına kontrol (Gemini 3):** Jeton kullanımını optimize eder. Örneğin, birden fazla resim içeren bir istemde karmaşık bir diyagram için `high`, daha basit bağlamsal resimler için `low` veya `medium` kullanın.

**Önerilen ayarlar**

Aşağıda, desteklenen her medya türü için önerilen medya çözünürlüğü ayarları listelenmiştir.

| Medya Türü | Önerilen Ayar | Maksimum jeton sayısı | Kullanım Yönergeleri |
| --- | --- | --- | --- |
| **Resimler** | `high` | 1120 | Maksimum kaliteyi sağlamak için çoğu görüntü analizi görevinde önerilir. |
| **PDF'ler** | `medium` | 560 | Belge anlamak için idealdir. Kalite genellikle `medium`'da doygunluğa ulaşır. `high`'ya yükseltmek, standart belgeler için OCR sonuçlarını nadiren iyileştirir. |
| **Video** (Genel) | `low` (veya `medium`) | 70 (kare başına) | **Not:** Video için `low` ve `medium` ayarları, bağlam kullanımını optimize etmek amacıyla aynı şekilde (70 jeton) değerlendirilir. Bu, çoğu eylem tanıma ve açıklama görevi için yeterlidir. |
| **Video** (Metin ağırlıklı) | `high` | 280 (kare başına) | Yalnızca kullanım alanında yoğun metinlerin (OCR) veya video karelerindeki küçük ayrıntıların okunması gerektiğinde zorunludur. |
| **Ses** | `unspecified` (Varsayılan) | 25 (saniyede) | Ses, desteklenen tüm çözünürlük ayarlarında (`unspecified`, `low`, `medium` ve `high`) saniyede 25 jeton sabit hızında jetonlaştırılır. |

Kalite, gecikme ve maliyet arasında en iyi dengeyi bulmak için farklı çözünürlük ayarlarının uygulamanız üzerindeki etkisini her zaman test edin ve değerlendirin.

## Video işleme modlarıyla ilişki

`media_resolution` ve işleme parametreleri, video girişinin farklı yönlerini kontrol eder:

- `media_resolution`, her karenin **çözünürlüğünü** (kare başına jeton sayısı) kontrol eder.
- `processing` / `media_processing` kontrolleri, **videodaki hangi içeriğin** bağlama yükleneceğini belirler.

İkisini de aynı video girişinde ayarlayabilirsiniz. Örneğin, uzun bir videoda toplam jeton kullanımını en aza indirmek için düşük medya çözünürlüğüyle agentic işlemeyi kullanabilirsiniz.

Video işleme modları hakkında ayrıntılı bilgi için [Agentic video understanding](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#agentic-video-understanding) (Agentic video anlama) kılavuzuna bakın.

## Sürüm uyumluluğu özeti

- `resolution` ayarını tek tek içerik öğelerinde belirleme **yalnızca Gemini 3 modellerinde** kullanılabilir.

## Sonraki adımlar

- Gemini API'nin çok formatlı özellikleri hakkında daha fazla bilgiyi [görüntü anlama](https://ai.google.dev/gemini-api/docs/image-understanding?hl=tr), [video anlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr), [ses anlama](https://ai.google.dev/gemini-api/docs/audio?hl=tr) ve [doküman anlama](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) kılavuzlarında bulabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
