---
source_url: https://ai.google.dev/gemini-api/docs/partner-integration?hl=tr
fetched_at: 2026-06-01T06:09:04.158203+00:00
title: "\u0130\u015f orta\u011f\u0131 ve kitapl\u0131k entegrasyonlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# İş ortağı ve kitaplık entegrasyonları

Bu kılavuzda, Gemini API'nin üzerinde kitaplıklar, platformlar ve ağ geçitleri oluşturmaya yönelik mimari stratejiler özetlenmektedir. Resmi üretken yapay zeka SDK'ları, Direct API (REST/gRPC) ve OpenAI uyumluluk katmanının kullanımı arasındaki teknik avantaj ve dezavantajlar ayrıntılı olarak açıklanır.

Diğer geliştiriciler için araçlar (ör. açık kaynaklı çerçeveler, kurumsal ağ geçitleri veya SaaS toplayıcılar) oluşturuyorsanız ve bağımlılık temizliği, paket boyutu ya da özellik eşliği için optimizasyon yapmanız gerekiyorsa bu kılavuzdan yararlanın.

## İş ortağı entegrasyonu nedir?

İş ortağı, Gemini API ile son kullanıcı geliştiricileri arasında entegrasyon oluşturan herkesi ifade eder. İş ortaklarını dört arketipte sınıflandırıyoruz. Hangisiyle en çok eşleştiğinizi belirlemek doğru entegrasyon yolunu seçmenize yardımcı olur.

#### Ekosistem çerçevesi

- **Kim olduğunuz:** Açık kaynaklı bir çerçeve (ör. LangChain, LlamaIndex, Spring AI) veya dile özgü istemcilerin bakımını yapan kişi.
- **Hedefiniz:** Geniş kapsamlı uyumluluk. Kitaplığınızın, kullanıcınızın seçtiği herhangi bir ortamda çakışmaya neden olmadan çalışmasını istiyorsunuz.

#### Çalışma zamanı ve uç platform

- **Kim olduğunuz:** Kod yürütmenin kısıtlanmış ortamlarda gerçekleştiği SaaS platformları, yapay zeka ağ geçitleri veya bulut altyapısı sağlayıcıları (ör. Vercel, Cloudflare, Zapier).
- **Hedefiniz:** Performans. Düşük gecikme süresi, minimum paket boyutu ve hızlı soğuk başlatma gerekir.

#### Toplayıcı

- **Kim olduğunuz:** Birçok farklı büyük dil modeli sağlayıcısında (ör. OpenAI, Anthropic, Google) erişimi tek bir arayüzde normalleştiren platformlar, proxy'ler veya dahili "Model Bahçeleri".
- **Hedefiniz:** Taşınabilirlik ve tekdüzelik.

#### Kurumsal ağ geçidi

- **Kimler için:** Büyük şirketlerdeki dahili platform mühendisliği ekipleri, yüzlerce dahili geliştirici için "altın yollar" oluşturuyor.
- **Hedefiniz:** Standartlaştırma, yönetim ve birleştirilmiş kimlik doğrulama.

## Bir bakışta karşılaştırma

**Küresel en iyi uygulama:** Seçilen yoldan bağımsız olarak tüm iş ortakları [`x-goog-api-client`
üstbilgisini](#client-id) göndermelidir.

| Şu durumlarda: | Önerilen yol | Temel avantaj | Önemli denge | En iyi uygulama |
| --- | --- | --- | --- | --- |
| **Kurumsal ağ geçidi, ekosistem çerçevesi** | **[Google GenAI SDK'sı](#genai-sdk)** | **Gemini Enterprise Ajan Platformu'nun eşitliği ve hızı** Türler, kimlik doğrulama ve karmaşık özellikler (ör. dosya yüklemeleri) için yerleşik işleme. Google Cloud'a sorunsuz taşıma | **Bağımlılık ağırlığı.** Geçişli bağımlılıklar karmaşık olabilir ve kontrolünüz dışında kalabilir. Desteklenen dillerle (Python/Node/Go/Java) sınırlıdır. | **Sürümleri kilitleme** Ekipler arasında kararlılığı sağlamak için dahili temel resimlerinizdeki SDK sürümlerini sabitleyin. |
| **Ekosistem çerçevesi, uç platformlar ve toplayıcılar** | **[Direct API](#rest)**  *(REST / gRPC)* | **Bağımlılık yok.** HTTP istemcisini ve tam paket boyutunu kontrol edersiniz. Tüm API ve model özelliklerine tam erişim. | **Yüksek geliştirici ek yükü.** JSON yapıları derinlemesine iç içe yerleştirilebilir ve sıkı manuel doğrulama ile tür kontrolü gerektirir. | **OpenAPI spesifikasyonlarını kullanın.** Türleri manuel olarak yazmak yerine resmi spesifikasyonlarımızı kullanarak otomatik olarak oluşturun. |
| **Yalnızca metin tabanlı iş akışları gerektiren OpenAI SDK'larını kullanan toplayıcı**  *(Eski taşınabilirlik için optimizasyon)* | **[OpenAI uyumluluğu](#openai)** | **Anında taşınabilirlik.** Mevcut OpenAI uyumlu kodları veya kitaplıkları yeniden kullanın. | **Özellik tavanı.** Modele özgü özellikler (doğal video reklam, önbelleğe alma) kullanılamayabilir. | **Taşıma planı.** Hızlı doğrulama için bu yöntemi kullanın ancak API özelliklerinin tamamından yararlanmak için Direct API'ye yükseltmeyi planlayın. |

## Google GenAI SDK entegrasyonu

Desteklenen dillerde en az kod satırı gerektiğinden, çerçeveler için [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/libraries?hl=tr)'sını uygulamak genellikle en basit yoldur.

Dahili platform ekipleri için temel çıktı genellikle ürün mühendislerinin güvenlik politikalarına uyarken hızlı hareket etmesini sağlayan bir "altın yol"dur.

**Avantajları:**

- **Gemini Enterprise Ajan Platformu'na taşıma için birleşik arayüz:** Dahili geliştiriciler genellikle API anahtarlarını (Gemini API) kullanarak prototip oluşturur ve üretim uyumluluğu için Gemini Enterprise Ajan Platformu'na (IAM) dağıtım yapar. SDK, bu kimlik doğrulama farklılıklarını soyutlar.
  Benzer şekilde, çerçeveler için tek bir kod yolu uygulayabilir ve iki kullanıcı grubunu destekleyebilirsiniz.
- **İstemci tarafı yardımcıları:** SDK, karmaşık görevler için standart kodları azaltan deyimsel yardımcı programlar içerir.
  - *Örnekler:* Doğrudan istemlerde `PIL` görüntü nesnelerini destekleme, otomatik işlev çağrısı ve kapsamlı türler.
- **İlk günden itibaren özellik erişimi:** Yeni API özellikleri, SDK'lar aracılığıyla kullanıma sunulur.
- **Geliştirilmiş kod oluşturma desteği:** Yerel SDK yüklemesi, tür tanımlarını ve doküman dizelerini kodlama asistanlarına (ör. Cursor, Copilot) sunar.
  Bu bağlam, ham REST istekleri oluşturmaya kıyasla kod oluşturma doğruluğunu artırır.

**Değiş-tokuş:**

- **Bağımlılık ağırlığı ve karmaşıklığı:** SDK'ların kendi bağımlılıkları vardır. Bu bağımlılıklar, paket boyutunu artırabilir ve potansiyel olarak tedarik zinciri riski oluşturabilir.
- **Sürüm oluşturma:** Yeni API özellikleri genellikle minimum SDK sürümlerine sabitlenir.
  Yeni özelliklere veya modellere erişmek için kullanıcıları güncellemeye zorlamanız gerekebilir. Bu durumda, kullanıcılarınızı etkileyen geçişli bağımlılıklar değiştirilebilir.
- **Protokol sınırları:** SDK'lar, ana API için yalnızca HTTPS'yi, Canlı API için ise WebSocket'leri (WSS) destekler. gRPC, üst düzey SDK istemcileri kullanılarak desteklenmez.
- **Dil desteği:** SDK'lar, *mevcut* dil sürümlerini destekler. Destek sonu (EOL) sürümlerini (ör. Python 3.9) desteklemeniz gerekiyorsa bir çatallanmayı sürdürmeniz gerekir.

**En iyi uygulama:**

- **Sürümleri kilitleme:** Ekipler arasında kararlılığı sağlamak için dahili temel resimlerinizdeki SDK sürümünü sabitleyin.

## Doğrudan API entegrasyonu

Binlerce geliştiriciye kitaplık dağıtıyorsanız, kısıtlanmış bir ortamda çalışıyorsanız veya Gemini'ın en yeni özelliklerini gerektiren bir toplayıcı oluşturuyorsanız REST veya gRPC kullanarak doğrudan API ile entegrasyon yapmanız gerekebilir.

**Avantajları:**

- **Tüm özelliklere erişim:** OpenAI uyumluluk katmanının aksine, API'yi doğrudan kullanmak Gemini'a özgü özellikleri (ör. File API'ye yükleme, içerik önbelleğe alma oluşturma ve çift yönlü Live API kullanma) etkinleştirir.
- **Minimum bağımlılıklar:** Bağımlılıkların boyut veya denetim maliyetleri nedeniyle hassas olduğu bir ortamda. API'yi doğrudan `fetch` gibi standart bir kitaplık veya `httpx` gibi bir sarmalayıcı aracılığıyla kullanmak kitaplığınızın hafif kalmasını sağlar.
- **Dilden bağımsız:** Dil kısıtlaması olmadığından bu, SDK'ların kapsamadığı diller (ör. Rust, PHP ve Ruby) için tek yoldur.
- **Performans:** Direct API'nin başlatma ek yükü yoktur. Bu sayede, sunucusuz işlevlerdeki soğuk başlatmalar en aza indirilir.

**Değiş-tokuş:**

- **Gemini Enterprise Ajan Platformu'nun manuel olarak uygulanması:** SDK'dan farklı olarak, API'nin doğrudan kullanılması, AI Studio (API anahtarı) ile Gemini Enterprise Ajan Platformu (IAM) arasındaki kimlik doğrulama farklılıklarını otomatik olarak işlemez. Her iki ortamı da desteklemek istiyorsanız ayrı kimlik doğrulama işleyicileri uygulamanız gerekir.
- **Yerel türler veya yardımcılar yok:** İstek nesneleri için kod tamamlamaları veya derleme zamanı kontrolleri almazsınız. Bunları kendiniz uygulamanız gerekir. İstemci "yardımcıları" (ör. işlevden şemaya dönüştürücüler) olmadığından bu mantığı kendiniz manuel olarak yazmanız gerekir.

**En iyi uygulama**

Kitaplığınız için tür tanımları oluşturmak üzere kullanabileceğiniz, makine tarafından okunabilir bir spesifikasyon sunuyoruz. Böylece, bu tanımları manuel olarak yazmak zorunda kalmazsınız. Derleme işleminiz sırasında spesifikasyonu indirin, türleri oluşturun ve derlenmiş kodu gönderin.

- **Uç nokta:** `https://generativelanguage.googleapis.com/$discovery/OPENAPI3_0`

## OpenAI SDK entegrasyonu

Modelden bağımsız özellikler yerine birleşik şemaya (OpenAI Chat Completions) öncelik veren bir platformsanız bu, en hızlı rotanızdır.

**Avantajları:**

- **Kolaylık:** Genellikle `baseURL` ve `apiKey` değiştirerek Gemini desteği ekleyebilirsiniz. Bu, "Kendi Anahtarını Getir" uygulamalarını entegre etmenin ve yeni kod yazmadan Gemini desteği eklemenin hızlı bir yoludur.
- **Kısıtlamalar:** Bu yol yalnızca OpenAI SDK ile sınırlıysanız ve File API gibi gelişmiş Gemini özelliklerine ya da Google Arama ile Temellendirme gibi araçlar için manuel olarak destek eklemeniz gerekmiyorsa önerilir.

**Değiş-tokuş:**

- **Özellik sınırlamaları:** Uyumluluk katmanı, temel Gemini özelliklerini sınırlar. Kullanılabilen sunucu tarafı araçlar platformlar arasında farklılık gösterir ve Gemini API araçlarıyla çalışmak için manuel olarak işlenmesi gerekebilir.
- **Çeviri ek yükü:** OpenAI şeması, Gemini'ın mimarisiyle bire bir eşlenmediğinden uyumluluk katmanını kullanmak, çözmek için ek uygulama çalışması gerektiren bazı karmaşıklıklara yol açar. Örneğin, kullanıcının "arama" aracını doğru platform aracıyla eşlemek gibi.
  Özel durumların önemli ölçüde kullanılması gerekiyorsa her platform için özel bir SDK veya API kullanmak daha faydalı olabilir.

**En iyi uygulama**

Mümkün olduğunda doğrudan Gemini API ile entegrasyon yapın. Ancak maksimum uyumluluk için farklı sağlayıcıların farkında olan ve araç ile mesaj eşlemeyi sizin için yapabilen bir kitaplık kullanmayı düşünebilirsiniz.

## Tüm iş ortakları için en iyi uygulama: istemci tanımlama

Platform veya kitaplık olarak Gemini API'ye çağrı yaparken `x-goog-api-client` üstbilgisini kullanarak istemcinizi tanımlamanız gerekir.

Bu, Google'ın belirli trafik segmentlerinizi tanımlamasına olanak tanır. Kitaplığınız belirli bir hata modeli üretiyorsa hata ayıklama konusunda yardımcı olmak için sizinle iletişime geçebiliriz.

`company-product/version` biçimini kullanın (ör. `acme-framework/1.2.0`).

### Uygulama örnekleri

### GenAI SDK

SDK, API istemcisini sağladığınızda özel başlığınızı otomatik olarak kendi dahili başlıklarına ekler.

```
from google import genai

client = genai.Client(
    api_key="...",
    http_options={
        "headers": {
            "x-goog-api-client": "acme-framework/1.2.0",
        }
    }
)
```

### Direct API (REST)

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -H 'x-goog-api-client: acme-framework/1.2.0' \
    -d '{...}'
```

### OpenAI SDK'sı

```
from openai import OpenAI

client = OpenAI(
    api_key="...",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    default_headers={
        "x-goog-api-client": "acme-framework-oai/1.2.0",
    }
)
```

## Sonraki adımlar

- GenAI SDK'ları hakkında bilgi edinmek için [kitaplığa genel bakış](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) sayfasını ziyaret edin.
- [API referansına](https://ai.google.dev/api?hl=tr) göz atın.
- [OpenAI uyumluluk kılavuzunu](https://ai.google.dev/gemini-api/docs/openai?hl=tr) okuyun.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
