---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/media-resolution?hl=tr
fetched_at: 2026-09-21T05:46:16.143086+00:00
title: "Medya \u00e7\u00f6z\u00fcn\u00fcrl\u00fc\u011f\u00fc \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Medya çözünürlüğü

`media_resolution` parametresi, medya girişleri için ayrılan **maksimum jeton sayısını** belirleyerek Gemini API'nin resim, video, ses ve PDF belgeleri gibi medya girişlerini nasıl işleyeceğini kontrol eder. Bu sayede, yanıt kalitesini gecikme ve maliyetle dengelemenize olanak tanır. Görsel ve belge girişleri, çözünürlük ayarına göre jeton dağıtımını ölçeklendirirken ses girişleri, tüm çözünürlük seviyelerinde saniyede sabit bir hızda jetonlaştırılır. Farklı ayarlar, varsayılan değerler ve bunların jetonlarla nasıl eşleştiği hakkında bilgi edinmek için [Jeton sayıları](#token-counts) bölümüne bakın.

Medya çözünürlüğünü iki şekilde yapılandırabilirsiniz:

- [Bölüm başına](#per-part-media-resolution) (yalnızca Gemini 3)
- `generateContent` isteğinin tamamı (tüm çok formatlı modeller) için [küresel olarak](#global-media-resolution)

## Bölüm başına medya çözünürlüğü (yalnızca Gemini 3)

Gemini 3, isteğinizdeki her bir medya nesnesi için medya çözünürlüğünü ayarlamanıza olanak tanır. Böylece, jeton kullanımını ayrıntılı bir şekilde optimize edebilirsiniz. Tek bir istekte çözünürlük seviyelerini karıştırabilirsiniz. Örneğin, karmaşık bir şema için yüksek çözünürlük, bağlamsal bir resim için ise düşük çözünürlük kullanabilirsiniz. Bu ayar, belirli bir bölüm için tüm genel yapılandırmaları geçersiz kılar. Varsayılan ayarlar için [Jeton sayıları](#token-counts) bölümüne bakın.

### Python

```
from google import genai
from google.genai import types

# The media_resolution parameter for parts is available in the v1beta API version.
client = genai.Client(
  http_options={
      'api_version': 'v1beta',
  }
)

# Replace with your image data
with open('path/to/image1.jpg', 'rb') as f:
    image_bytes_1 = f.read()

# Create parts with different resolutions
image_part_high = types.Part.from_bytes(
    data=image_bytes_1,
    mime_type='image/jpeg',
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

model_name = 'gemini-3.1-pro-preview'

response = client.models.generate_content(
    model=model_name,
    contents=["Describe these images:", image_part_high]
)
print(response.text)
```

### JavaScript

```
// Example: Setting per-part media resolution in JavaScript
import { GoogleGenAI, MediaResolution, Part } from '@google/genai';
import * as fs from 'fs';
import { Buffer } from 'buffer'; // Node.js

const ai = new GoogleGenAI({ httpOptions: { apiVersion: 'v1beta' } });

// Helper function to convert local file to a Part object
function fileToGenerativePart(path, mimeType, mediaResolution) {
    return {
        inlineData: { data: Buffer.from(fs.readFileSync(path)).toString('base64'), mimeType },
        mediaResolution: { 'level': mediaResolution }
    };
}

async function run() {
    // Create parts with different resolutions
    const imagePartHigh = fileToGenerativePart('img.png', 'image/png', Part.MediaResolutionLevel.MEDIA_RESOLUTION_HIGH);
    const model_name = 'gemini-3.1-pro-preview';
    const response = await ai.models.generateContent({
        model: model_name,
        contents: ['Describe these images:', imagePartHigh]
        // Global config can still be set, but per-part settings will override
        // config: {
        //   mediaResolution: MediaResolution.MEDIA_RESOLUTION_MEDIUM
        // }
    });
    console.log(response.text);
}
run();
```

### REST

```
# Replace with paths to your images
IMAGE_PATH="path/to/image.jpg"

# Base64 encode the images
BASE64_IMAGE1=$(base64 -w 0 "$IMAGE_PATH")

MODEL_ID="gemini-3.1-pro-preview"

echo '{
    "contents": [{
      "parts": [
        {"text": "Describe these images:"},
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "'"$BASE64_IMAGE1"'",
          },
          "media_resolution": {"level": "MEDIA_RESOLUTION_HIGH"}
        }
      ]
    }]
  }' > request.json

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d @request.json
```

## Genel medya çözünürlüğü

`GenerationConfig` kullanarak bir istekteki tüm medya bölümleri için varsayılan bir çözünürlük ayarlayabilirsiniz. Bu özellik tüm çok formatlı modellerde desteklenir. Bir istek hem genel hem de [bölüm bazında ayarları](#per-part-media-resolution) içeriyorsa söz konusu öğe için bölüm bazında ayar öncelikli olur.

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# Prepare standard image part
with open('image.jpg', 'rb') as f:
    image_bytes = f.read()
image_part = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')

# Set global configuration
config = types.GenerateContentConfig(
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_HIGH
)

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=["Describe this image:", image_part],
    config=config
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI, MediaResolution } from '@google/genai';
import * as fs from 'fs';

const ai = new GoogleGenAI({ });

async function run() {
   // ... (Image loading logic) ...

   const response = await ai.models.generateContent({
      model: 'gemini-3.8-flash',
      contents: ["Describe this image:", imagePart],
      config: {
         mediaResolution: MediaResolution.MEDIA_RESOLUTION_HIGH
      }
   });
   console.log(response.text);
}
run();
```

### REST

```
# ... (Base64 encoding logic) ...

curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [...],
    "generation_config": {
      "media_resolution": "MEDIA_RESOLUTION_HIGH"
    }
  }'
```

## Kullanılabilir çözünürlük değerleri

Gemini API, medya çözünürlüğü için aşağıdaki düzeyleri tanımlar:

- `MEDIA_RESOLUTION_UNSPECIFIED`: Varsayılan ayardır. Bu seviyenin jeton sayısı, Gemini 3 ile önceki Gemini modelleri arasında önemli ölçüde farklılık gösterir.
- `MEDIA_RESOLUTION_LOW`: Daha düşük jeton sayısı, daha hızlı işlem ve daha düşük maliyet sağlar ancak daha az ayrıntı içerir.
- `MEDIA_RESOLUTION_MEDIUM`: Ayrıntı, maliyet ve gecikme arasında denge.
- `MEDIA_RESOLUTION_HIGH`: Daha yüksek jeton sayısı, gecikme ve maliyet artışı karşılığında modelin çalışması için daha fazla ayrıntı sağlar.
- `MEDIA_RESOLUTION_ULTRA_HIGH` (Yalnızca bölüm başına): En yüksek jeton sayısı, [bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) gibi belirli kullanım alanları için gereklidir.

`MEDIA_RESOLUTION_HIGH`'nın çoğu kullanım alanı için optimum performans sağladığını unutmayın.

Bu seviyelerin her biri için oluşturulan jetonların tam sayısı hem **medya türüne** (resim, video, ses, PDF) hem de **model sürümüne** bağlıdır.

## Jeton sayıları

Aşağıdaki tablolarda, her model ailesi için `media_resolution` değeri ve medya türü başına yaklaşık jeton sayıları özetlenmektedir.

**Gemini 3 modelleri**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MediaResolution** | **Resim** | **Video** | **Ses** | **PDF** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Varsayılan) | 1120 | 70 | 25 (saniyede) | 560 |
| `MEDIA_RESOLUTION_LOW` | 280 | 70 | 25 (saniyede) | 280 + Yerel Metin |
| `MEDIA_RESOLUTION_MEDIUM` | 560 | 70 | 25 (saniyede) | 560 + Yerel Metin |
| `MEDIA_RESOLUTION_HIGH` | 1120 | 280 | 25 (saniyede) | 1.120 + Yerel Metin |
| `MEDIA_RESOLUTION_ULTRA_HIGH` | 2240 | Yok | Yok | Yok |

**Gemini 2.5 modelleri**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **MediaResolution** | **Resim** | **Video** | **Ses** | **PDF (taranmış)** | **PDF (Yerel)** |
| `MEDIA_RESOLUTION_UNSPECIFIED` (Varsayılan) | 256 + Pan & Scan (~2048) | 256 | 32 (saniyede) | 256 + OCR | 256 + Yerel Metin |
| `MEDIA_RESOLUTION_LOW` | 64 | 64 | 32 (saniyede) | 64 + OCR | 64 + Yerel Metin |
| `MEDIA_RESOLUTION_MEDIUM` | 256 | 256 | 32 (saniyede) | 256 + OCR | 256 + Yerel Metin |
| `MEDIA_RESOLUTION_HIGH` | 256 + Pan & Scan | 256 | 32 (saniyede) | 256 + OCR | 256 + Yerel Metin |

## Doğru çözünürlüğü seçme

- **Varsayılan (`UNSPECIFIED`):** Varsayılanla başlayın. En yaygın kullanım alanlarında kalite, gecikme ve maliyet arasında iyi bir denge sağlamak için ayarlanmıştır.
- **`LOW`:** Maliyet ve gecikmenin öncelikli olduğu, ayrıntılı bilgilerin daha az önemli olduğu senaryolarda kullanılır.
- **`MEDIUM` / `HIGH`:** Görev, medyada yer alan karmaşık ayrıntıların anlaşılmasını gerektirdiğinde çözünürlüğü artırın. Bu özellik genellikle karmaşık görsel analiz, grafik okuma veya yoğun belge anlama için gereklidir.
- **`ULTRA HIGH`**: Yalnızca parça başına ayar için kullanılabilir. Bilgisayar kullanımı gibi belirli kullanım alanları veya testlerin `HIGH` üzerinde net bir iyileşme gösterdiği durumlarda önerilir.
- **Bölüm bazında kontrol (Gemini 3):** Jeton kullanımını optimize eder. Örneğin, birden fazla resim içeren bir istemde karmaşık bir diyagram için `HIGH`, daha basit bağlamsal resimler için ise `LOW` veya `MEDIUM` kullanın.

**Önerilen ayarlar**

Aşağıda, desteklenen her medya türü için önerilen medya çözünürlüğü ayarları listelenmiştir.

|  |  |  |  |
| --- | --- | --- | --- |
| **Medya Türü** | **Önerilen Ayar** | **Maksimum Jeton Sayısı** | **Kullanım Yönergeleri** |
| **Resimler** | `MEDIA_RESOLUTION_HIGH` | 1120 | Maksimum kaliteyi sağlamak için çoğu görüntü analizi görevinde önerilir. |
| **PDF'ler** | `MEDIA_RESOLUTION_MEDIUM` | 560 | Belge anlamak için idealdir. Kalite genellikle `medium`'da doygunluğa ulaşır. `high`'ya yükseltmek, standart belgeler için OCR sonuçlarını nadiren iyileştirir. |
| **Video** (Genel) | `MEDIA_RESOLUTION_LOW` (veya `MEDIA_RESOLUTION_MEDIUM`) | 70 (kare başına) | **Not:** Video için `low` ve `medium` ayarları, bağlam kullanımını optimize etmek amacıyla aynı şekilde (70 jeton) değerlendirilir. Bu, çoğu eylem tanıma ve açıklama görevi için yeterlidir. |
| **Video** (Metin ağırlıklı) | `MEDIA_RESOLUTION_HIGH` | 280 (kare başına) | Yalnızca kullanım alanında yoğun metinlerin (OCR) veya video karelerindeki küçük ayrıntıların okunması gerektiğinde zorunludur. |
| **Ses** | `MEDIA_RESOLUTION_UNSPECIFIED` (Varsayılan) | Gemini 3 için 25 (saniyede), Gemini 2.5 için 32 (saniyede) | Ses, desteklenen tüm çözünürlük ayarlarında (`unspecified`, `low`, `medium` ve `high`) saniyede sabit bir hızda belirteçleştirilir. |

Kalite, gecikme ve maliyet arasında en iyi dengeyi bulmak için farklı çözünürlük ayarlarının uygulamanız üzerindeki etkisini her zaman test edin ve değerlendirin.

## Video işleme modlarıyla ilişki

`media_resolution` ve işleme parametreleri, video girişinin farklı yönlerini kontrol eder:

- `media_resolution`, her karenin **çözünürlüğünü** (kare başına jeton sayısı) kontrol eder.
- `processing` / `media_processing` kontrolleri, **videodaki hangi içeriğin** bağlama yükleneceğini belirler.

İkisini de aynı video girişinde ayarlayabilirsiniz. Örneğin, uzun bir videoda toplam jeton kullanımını en aza indirmek için düşük medya çözünürlüğüyle agentic işlemeyi kullanabilirsiniz.

Video işleme modları hakkında ayrıntılı bilgi için [Agentic video understanding](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=tr#agentic-video-understanding) (Agentic video anlama) kılavuzuna bakın.

## Sürüm uyumluluğu özeti

- `MediaResolution` numaralandırması, medya girişi destekleyen tüm modellerde kullanılabilir.
- Her enum düzeyiyle ilişkili jeton sayıları, Gemini 3 modelleri ile önceki Gemini sürümleri arasında **farklıdır**.
- `media_resolution` ayarını tek tek `Part` nesnelerde belirleme **yalnızca Gemini 3 modellerinde** kullanılabilir.

## Sonraki adımlar

- Gemini API'nin çok formatlı özellikleri hakkında daha fazla bilgiyi [görüntü anlama](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=tr), [Video Anlama](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=tr), [Ses Anlama](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=tr) ve [Doküman Anlama](https://ai.google.dev/gemini-api/docs/generate-content/document-processing?hl=tr) kılavuzlarında bulabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-19 UTC."],[],[]]
