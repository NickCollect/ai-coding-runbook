---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/robotics-overview?hl=tr
fetched_at: 2026-09-21T05:56:55.005004+00:00
title: "Gemini Robotics ER \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Gemini Robotics ER

Gemini Robotics ER (embodied reasoning) modelleri, robotların fiziksel dünyayı algılamasına ve bu dünyayla etkileşime girmesine olanak tanıyan görme-dil modelleridir (VLMs). Görsel verileri yorumlar, mekansal ve zamansal akıl yürütme yapar, çok adımlı görevleri planlar, robotları ve araçları yönetir.

## Modeller

Gemini Robotics ER 2 modeli, Gemini Robotics'in en yeni modelidir.
Bu, robotların çevrelerini tam olarak anlamalarını sağlayan güncellenmiş akıl yürütme modelimizdir. Robotların ajan tabanlı düzenlemesi (ör. VLA'ları kullanma), ilerleme anlayışı ve başarı tespiti dahil olmak üzere robot videosunu anlama, enstrüman okuma, işaret etme ve uzamsal akıl yürütme gibi somut akıl yürütme yetenekleri konusunda uzmanlaşmıştır.

Gemini Robotics ER 2 modeli iki model uç noktası sunar:

- **`gemini-robotics-er-2-preview`**: Standart ER 2 modeli. Geliştirilmiş uzamsal akıl yürütme, video anı bulma, video ilerleme sınıflandırması, çoklu robot düzenleme ve çok adımlı araç kullanımı ile Gemini 3.5 Flash'ın üzerine inşa edilmiştir.
- **`gemini-robotics-er-2-streaming-preview`**: [Live API](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr) aracılığıyla gerçek zamanlı yayın için optimize edilmiştir. Sürekli ses ve görüntü girişini işleyen düşük gecikmeli robot aracıları için bu modeli kullanın.

Gemini Robotics ER 1.6 kullanıyorsanız API çağrılarınızda `model="gemini-robotics-er-1.6-preview"` yerine `model="gemini-robotics-er-2-preview"` veya `model="gemini-robotics-er-2-streaming-preview"` koyarak Gemini Robotics ER 2'ye yükseltin. Gemini Robotics ER 1.6 modelinin [Ağustos ayının sonunda](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#robotics-models) kapatılacağını unutmayın.

[Google AI Studio'da Gemini Robotics ER 2'yi deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-2-preview&hl=tr)

## Robotik özellikleri

Gemini Robotics ER, bir dizi somut akıl yürütme özelliğini destekler.
Daha fazla bilgi edinmek için bir özellik seçin:

| Kapasite | Açıklama | Kılavuz |
| --- | --- | --- |
| Uzamsal akıl yürütme | Nesneleri işaretleme, videoda izleme, sınırlayıcı kutularla algılama ve yörünge planlama | [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=tr) |
| Ajan tabanlı vizyon | Resim işleme araçlarından yararlanarak diğer özellikleri geliştirmek için kod yürütmeyi kullanın. | [Temsilci tabanlı vizyon](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=tr) |
| Görev düzenleme | Uzun vadeli görevleri tamamlamak için uzamsal akıl yürütmeyi özel robot API'leriyle birleştirin. | [Görev düzenleme](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=tr) |
| Akış (yalnızca Gemini Robotics ER 2 Akış uç noktası) | Düşük gecikmeli işlev çağrısıyla anlık robot temsilciler için çift yönlü akış. | [Robotik için akış](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr) |
| Video ilerleme (yalnızca Gemini Robotics ER 2) | Sürekli video feed'lerinden anları bulma ve ilerleme sınıflandırması. | [Video anlama](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=tr) (Video understanding) |

## Başlarken

Aşağıdaki örnekte, bir resimdeki nesneler bulunur ve bunların normalleştirilmiş 2D koordinatları ile etiketleri döndürülür. Bu çıkışı, robot işlemleri oluşturmak için doğrudan bir robotik API'ye veya VLA modeline iletebilirsiniz.

### Python

```
from google import genai
from google.genai import types

PROMPT = """
          Point to no more than 10 items in the image. The label returned
          should be an identifying name for the object detected.
          The answer should follow the json format: [{"point": <point>,
          "label": <label1>}, ...]. The points are in [y, x] format
          normalized to 0-1000.
        """
client = genai.Client()

uploaded_file = client.files.upload(file="my-image.png")

response = client.models.generate_content(
    model="gemini-robotics-er-2-preview",
    contents=[
        types.Part.from_uri(
            file_uri=uploaded_file.uri,
            mime_type=uploaded_file.mime_type
        ),
        PROMPT
    ],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="high")
    ),
)

print(response.text)
```

### REST

```
# First, ensure you have the image file locally.
# Encode the image to base64
IMAGE_BASE64=$(base64 -w 0 my-image.png)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-robotics-er-2-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/png",
              "data": "'"${IMAGE_BASE64}"'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. The label returned should be an identifying name for the object detected. The answer should follow the json format: [{\"point\": [y, x], \"label\": <label1>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {
        "thinkingLevel": "high"
      }
    }
  }'
```

Çıktı, her biri `point` (normalleştirilmiş `[y, x]` koordinatları) ve nesneyi tanımlayan bir `label` içeren nesnelerden oluşan bir JSON dizisi olacaktır.

### JSON

```
[
  {"point": [376, 508], "label": "small banana"},
  {"point": [287, 609], "label": "larger banana"},
  {"point": [223, 303], "label": "pink starfruit"},
  {"point": [435, 172], "label": "paper bag"},
  {"point": [270, 786], "label": "green plastic bowl"},
  {"point": [488, 775], "label": "metal measuring cup"},
  {"point": [673, 580], "label": "dark blue bowl"},
  {"point": [471, 353], "label": "light blue bowl"},
  {"point": [492, 497], "label": "bread"},
  {"point": [525, 429], "label": "lime"}
]
```

Aşağıdaki resimde, bu noktaların nasıl gösterilebileceğine dair bir örnek verilmiştir:

![Resimdeki nesnelerin noktalarını gösteren bir örnek](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png?hl=tr)

## İşleyiş şekli

Gemini Robotics ER, doğal dil istemleriyle resim, video veya ses girişlerini kabul eder. Nesneleri tanımlar, sahne bağlamı ve mekansal ilişkiler hakkında akıl yürütür ve koordinatlar veya sınırlayıcı kutular gibi yapılandırılmış çıkışlar döndürür.

Gemini Robotics ER de temsilci tabanlıdır: Karmaşık görevleri alt görevlere ayırır ve robot işlevlerinizi çağırarak veya oluşturulan kodu çalıştırarak bunları yerine getirir. Örneğin, "elmaları kaseye koy" ifadesi; bulma, kavrama ve yerleştirme adımlarından oluşan bir diziye dönüşür.

Gemini'ın araç çağrılarını nasıl yürüttüğü hakkında ayrıntılı bilgi için [İşlev
çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting&hl=tr#how-it-works) bölümüne bakın.

## Güvenlik

Gemini Robotics ER, güvenlik göz önünde bulundurularak üretilmiş olsa da robotun etrafında güvenli bir ortam sağlamak sizin sorumluluğunuzdadır. Üretken yapay zeka modelleri hata yapabilir ve fiziksel robotlar hasara neden olabilir. Daha fazla bilgi edinmek için [Google DeepMind robotik güvenlik sayfasını](https://deepmind.google/models/gemini-robotics/safety?hl=tr) ziyaret edin.

## En iyi uygulamalar

1. Sade ve doğal dil kullanın. Robottan ne yapmasını istediğinizi bir kişiye anlatır gibi açıklayın. Bir terim çalışmıyorsa yaygın bir eş anlamlıyı deneyin.
2. Görsel girişi optimize edin. Resmi göndermeden önce küçük veya net olmayan nesneleri kırpın ya da yakınlaştırın. Işık ve düşük renk kontrastı algılamayı etkileyebilir.
3. Karmaşık görevleri adımlara ayırın. Modelin odaklanmasını sağlamak ve doğruluğu artırmak için her adımı ayrı bir istem olarak gönderin.
4. Yüksek hassasiyetli görevler için birden çok kez sorgulama yapın ve sonuçların ortalamasını alın. Bu fikir birliği yaklaşımı, mekansal çıktılardaki varyansı azaltır.

## Sınırlamalar

Gemini Robotics ER ile geliştirme yaparken aşağıdaki sınırlamaları göz önünde bulundurun:

- **API anahtarı kısıtlamaları:** Gemini API, kısıtlanmamış API anahtarlarından gelen istekleri kabul etmez ve `403 Forbidden` hatasını döndürür. [AI Studio](https://aistudio.google.com/api-keys?hl=tr)'da kısıtlamalar ekleyerek API anahtarınızı güvenli hale getirin.
  Ayrıntılar için [Sınırsız API anahtarlarını güvenli hale getirme](https://ai.google.dev/gemini-api/docs/api-key?hl=tr#secure-unrestricted-keys) konusuna bakın.
- **Gecikme süresi ve performans:** Karmaşık sorgular, yüksek çözünürlüklü girişler veya yüksek düşünce seviyeleri, işleme sürelerinin artmasına neden olabilir. Düşünme seviyesi için gecikme ve performans arasında iyi bir denge sağlamak üzere orta seviyeyi kullanın.
- **Halüsinasyonlar:** Tüm büyük dil modelleri gibi Gemini Robotics ER modelleri de zaman zaman "halüsinasyon" görebilir veya yanlış bilgi verebilir. Bu durum özellikle belirsiz istemlerde ya da dağıtım dışı girişlerde görülür.
- **İstem kalitesine bağlılık:** Çıkış kalitesi, giriş isteminin netliğine bağlıdır. Net ve iyi yapılandırılmış istemler kullanın.
- **Hesaplama maliyeti:** Özellikle video girişleriyle veya yüksek `thinking_budget` ile modelin çalıştırılması, hesaplama kaynaklarını tüketir ve maliyetlere neden olur.
  Daha fazla bilgi için [Düşünme](https://ai.google.dev/gemini-api/docs/generate-content/thinking?hl=tr) sayfasına bakın.
- **Giriş türleri:** Her moddaki sınırlamalarla ilgili ayrıntılar için aşağıdaki konulara bakın.
  - [Resim girişleri](https://ai.google.dev/gemini-api/docs/generate-content/image-understanding?hl=tr#technical-details-image)
  - [Video girişleri](https://ai.google.dev/gemini-api/docs/generate-content/video-understanding?hl=tr#supported-formats)
  - [Ses girişleri](https://ai.google.dev/gemini-api/docs/generate-content/audio?hl=tr#supported-formats)

## Gizlilik Uyarısı

Bu belgede referans verilen modellerin ("Robotik Modeller") çalışmak ve donanımınızı talimatlarınıza uygun şekilde hareket ettirmek için video ve ses verilerinden yararlandığını kabul edersiniz. Bu nedenle, Robotik Modelleri, tanımlanabilir kişilerden elde edilen veriler (ör. ses, görüntü ve benzerlik verileri ("Kişisel Veriler")) Robotik Modeller tarafından toplanacak şekilde çalıştırabilirsiniz. Robotik Modelleri Kişisel Veri toplayacak şekilde çalıştırmayı seçerseniz, bu tür tanımlanabilir kişilerin, Kişisel Verilerinin [https://ai.google.dev/gemini-api/terms](https://ai.google.dev/gemini-api/terms?hl=tr) adresinde bulunan Gemini API Ek Hizmet Şartları'nda ("Şartlar") belirtildiği şekilde Google'a sağlanabileceği ve Google tarafından kullanılabileceği konusunda yeterince bilgilendirilip onay vermediği sürece Robotik Modellerle etkileşime girmesine veya Robotik Modellerin bulunduğu alanda bulunmasına izin vermeyeceğinizi kabul edersiniz. Bu durum, "Google Verilerinizi Nasıl Kullanır?" başlıklı bölüm uyarınca da geçerlidir. Bu tür bir bildirimin, Şartlar'da belirtildiği şekilde Kişisel Verilerin toplanmasına ve kullanılmasına izin vermesini sağlayacak ve yüz bulanıklaştırma gibi teknikler kullanarak ve Robotik Modelleri, mümkün olduğunca kimliği belirlenebilen kişilerin bulunmadığı alanlarda çalıştırarak Kişisel Verilerin toplanmasını ve dağıtılmasını en aza indirmek için ticari olarak makul çabayı göstereceksiniz.

## Fiyatlandırma

Fiyatlandırma ve kullanılabilir bölgeler hakkında ayrıntılı bilgi için [fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasına bakın.

## Model uç noktaları

### Gemini Robotics ER 2 Önizlemesi

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-2-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış jetonu sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Destekleniyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Destekleniyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Destekleniyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Destekleniyor  **[İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Destekleniyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Desteklenmiyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Destekleniyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)** (Thinking)  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Destekleniyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Destekleniyor  **[Esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıpları](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) başlıklı makaleyi inceleyin.  - Önizleme: `gemini-robotics-er-2-preview` |
| calendar\_monthSon güncelleme | Temmuz 2026 |
| id\_cardModel kartı | [Model kartı](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=tr) |

### Gemini Robotics ER 2 Streaming Preview

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-2-streaming-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış jetonu sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Desteklenmiyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Desteklenmiyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Desteklenmiyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Desteklenmiyor  **[İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Desteklenmiyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Destekleniyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Desteklenmiyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)** (Thinking)  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Desteklenmiyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Desteklenmiyor  **[Esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıpları](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) başlıklı makaleyi inceleyin.  - Önizleme: `gemini-robotics-er-2-streaming-preview` |
| calendar\_monthSon güncelleme | Temmuz 2026 |
| id\_cardModel kartı | [Model kartı](https://deepmind.google/models/model-cards/gemini-robotics-er-2/?hl=tr) |

### Gemini Robotics ER 1.6 Önizlemesi

| Mülk | Açıklama |
| --- | --- |
| id\_cardModel kodu | `gemini-robotics-er-1.6-preview` |
| saveDesteklenen veri türleri | **Girişler**  Metin, resim, video, ses  **Çıkış**  Metin |
| token\_autoJeton sınırları[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) | **Giriş jetonu sınırı**  131.072  **Çıkış jetonu sınırı**  65.536 |
| handymanÖzellikler | **[Ses üretme](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr)**  Desteklenmiyor  **[Önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr)**  Destekleniyor  **[Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr)**  Destekleniyor  **[Bilgisayar kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr)**  Destekleniyor  **[Dosya arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)**  Destekleniyor  **[İşlev çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)**  Destekleniyor  **[Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)**  Destekleniyor  **[Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)**  Desteklenmiyor  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr)**  Desteklenmiyor  **[Arama temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)**  Destekleniyor  **[Yapılandırılmış çıkışlar](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr)**  Destekleniyor  **[Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)** (Thinking)  Destekleniyor  **[URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)**  Destekleniyor |
| speedTüketim seçenekleri | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr)**  Destekleniyor  **[Esnek çıkarım](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr)**  Desteklenmiyor  **[Öncelik çıkarımı](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr)**  Desteklenmiyor |
| 123Sürümler | Daha fazla bilgi için [model sürümü kalıpları](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#model-versions) başlıklı makaleyi inceleyin.  - Önizleme: `gemini-robotics-er-1.6-preview` |
| calendar\_monthSon güncelleme | Aralık 2025 |
| cognition\_2Son güncel bilgi tarihi | Ocak 2025 |

## Sırada ne var?

- [Uzamsal akıl yürütme](https://ai.google.dev/gemini-api/docs/generate-content/robotics-spatial?hl=tr): işaretleme, izleme, sınırlayıcı kutular, yörüngeler.
- [Ajan tabanlı yetenekler](https://ai.google.dev/gemini-api/docs/generate-content/robotics-agentic?hl=tr): Kod yürütme, enstrüman okuma, görüntü açıklama.
- [Görev düzenleme](https://ai.google.dev/gemini-api/docs/generate-content/robotics-orchestration?hl=tr): Özel robot API'leri içeren uzun vadeli görevler.
- [Yayın özellikli robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr): Gerçek zamanlı çift yönlü yayın (yalnızca Gemini Robotics ER 2).
- [Video anlama](https://ai.google.dev/gemini-api/docs/generate-content/robotics-video-progress?hl=tr): Anları bulma ve ilerleme sınıflandırması (yalnızca Gemini Robotics ER 2).
- [Google DeepMind robotik güvenlik](https://deepmind.google/models/gemini-robotics/safety?hl=tr): Model ailesinin arkasındaki güvenlik araştırması.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-08 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-08 UTC."],[],[]]
