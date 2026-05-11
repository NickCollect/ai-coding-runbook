---
source_url: https://ai.google.dev/gemini-api/docs/migrate-to-cloud?hl=tr
fetched_at: 2026-05-11T05:05:40.012890+00:00
title: "Gemini Developer API ile Gemini Enterprise Agent Platform aras\u0131ndaki farklar \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini Developer API ile Gemini Enterprise Agent Platform arasındaki farklar

Google, Gemini ile üretken yapay zeka çözümleri geliştirirken iki API ürünü sunar: [Gemini Developer API](https://ai.google.dev/gemini-api/docs?hl=tr) ve [Gemini Enterprise Agent Platform API](https://cloud.google.com/gemini-enterprise-agent-platform/overview?hl=tr).

Gemini Developer API, Gemini destekli uygulamalar oluşturmak, üretime hazır hale getirmek ve ölçeklendirmek için en hızlı yolu sunar. Çoğu geliştirici, belirli kurumsal kontroller gerekmediği sürece Gemini Developer API'yi kullanmalıdır.

Gemini Enterprise Ajan Platformu, Google Cloud Platform tarafından desteklenen üretken yapay zeka uygulamaları oluşturmak ve dağıtmak için kurumsal kullanıma hazır özellikler ve hizmetlerden oluşan kapsamlı bir ekosistem sunar.

Kısa süre önce bu hizmetler arasında geçiş yapmayı kolaylaştırdık. Hem Gemini Developer API hem de Gemini Enterprise Agent Platform API artık birleştirilmiş [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) üzerinden erişilebilir.

## Kod karşılaştırması

Bu sayfada, metin oluşturma için Gemini Developer API ile Gemini Enterprise Agent Platform hızlı başlangıçları arasında yan yana kod karşılaştırmaları yer almaktadır.

### Python

Hem Gemini Developer API hem de Gemini Enterprise Agent Platform hizmetlerine `google-genai` kitaplığı üzerinden erişebilirsiniz. `google-genai`'ı yükleme talimatları için [kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasına bakın.

### Gemini Developer API

```
from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### Gemini Enterprise Agent Platform API

```
from google import genai

client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript ve TypeScript

Hem Gemini Developer API hem de Gemini Enterprise Agent Platform hizmetlerine `@google/genai` kitaplığı üzerinden erişebilirsiniz. `@google/genai`'ı yükleme talimatları için [kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasına bakın.

### Gemini Developer API

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Gemini Enterprise Agent Platform API

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({
  vertexai: true,
  project: 'your_project',
  location: 'your_location',
});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

Hem Gemini Developer API hem de Gemini Enterprise Agent Platform hizmetlerine `google.golang.org/genai` kitaplığı üzerinden erişebilirsiniz. `google.golang.org/genai`'ı yükleme talimatları için [kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasına bakın.

### Gemini Developer API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your Google API key
const apiKey = "your-api-key"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Gemini Enterprise Agent Platform API

```
import (
  "context"
  "encoding/json"
  "fmt"
  "log"
  "google.golang.org/genai"
)

// Your GCP project
const project = "your-project"

// A GCP location like "us-central1"
const location = "some-gcp-location"

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, &genai.ClientConfig
  {
        Project:  project,
      Location: location,
      Backend:  genai.BackendVertexAI,
  })

  // Call the GenerateContent method.
  result, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Tell me about New York?"), nil)

}
```

### Diğer kullanım alanları ve platformlar

Diğer platformlar ve kullanım alanları için [Gemini Developer API Belgeleri](https://ai.google.dev/gemini-api/docs?hl=tr) ve [Gemini Enterprise Agent Platform belgelerindeki](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=tr) kullanım alanına özel kılavuzlara bakın.

## Taşımayla ilgili dikkat edilmesi gereken noktalar

Taşıma işlemi yaptığınızda:

- Kimlik doğrulaması yapmak için Google Cloud hizmet hesaplarını kullanmanız gerekir. Daha fazla bilgi için [Gemini Enterprise Ajan Platformu belgelerini](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/overview?hl=tr) inceleyin.
- Mevcut Google Cloud projenizi (API anahtarınızı oluşturmak için kullandığınız proje) kullanabilir veya [yeni bir Google Cloud projesi oluşturabilirsiniz](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=tr).
- Desteklenen bölgeler, Gemini Developer API ile Gemini Enterprise Agent Platform API arasında farklılık gösterebilir. [Google Cloud'da üretken yapay zeka için desteklenen bölgelerin](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/learn/locations-genai?hl=tr) listesine bakın.
- Google AI Studio'da oluşturduğunuz tüm modellerin Gemini Enterprise Agent Platform'da yeniden eğitilmesi gerekir.

Gemini Developer API için Gemini API anahtarınızı artık kullanmanız gerekmiyorsa güvenlikle ilgili en iyi uygulamaları izleyerek anahtarı silin.

API anahtarını silmek için:

1. [Google Cloud API Kimlik Bilgileri](https://console.cloud.google.com/apis/credentials?hl=tr) sayfasını açın.
2. Silmek istediğiniz API anahtarını bulup **İşlemler** simgesini tıklayın.
3. **API anahtarını sil**'i seçin.
4. **Kimliği sil** kalıcı öğesinde **Sil**'i seçin.

   API anahtarının silinmesinin etkili olması birkaç dakika sürer. Yayma işlemi tamamlandıktan sonra, silinen API anahtarını kullanan tüm trafik reddedilir.

## Sonraki adımlar

- Gemini Enterprise Ajan Platformu'ndaki üretken yapay zeka çözümleri hakkında daha fazla bilgi edinmek için [Gemini Enterprise Ajan Platformu'nda üretken yapay zekaya genel bakış](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/docs/multimodal/overview?hl=tr) başlıklı makaleyi inceleyin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
