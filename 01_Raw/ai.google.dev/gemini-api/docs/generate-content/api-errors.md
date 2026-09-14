---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-errors?hl=tr
fetched_at: 2026-09-14T05:41:36.565786+00:00
title: "API hatalar\u0131 \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# API hataları

Bu sayfada, `GenerateContent` API'si tarafından döndürülen arka uç hata kodları için bir referans sağlanmakta, gRPC hata yanıtı biçimi açıklanmakta ve sorun giderme adımları sunulmaktadır.

## HTTP hata kodları

Aşağıdaki tabloda, yaygın olarak görülen arka uç hata kodları, nedenleriyle ilgili açıklamalar ve önerilen çözümler listelenmektedir:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP Kodu** | **Durum** | **Açıklama** | **Örnek** | **Çözüm** |
| 400 | INVALID\_ARGUMENT | İstek metni yanlış biçimlendirilmiş. | İsteğinizde yazım hatası var veya zorunlu bir alan eksik. | İstek biçimi, örnekler ve desteklenen sürümler için [API referansına](https://ai.google.dev/api?hl=tr) bakın. Daha yeni bir API sürümündeki özellikleri daha eski bir uç nokta ile kullanmak hatalara neden olabilir. |
| 400 | FAILED\_PRECONDITION | Gemini API ücretsiz katmanı ülkenizde kullanılamıyor. Lütfen Google AI Studio'da projenizde faturalandırmayı etkinleştirin. | Ücretsiz katmanın desteklenmediği bir bölgede istekte bulunuyorsunuz ve Google AI Studio'daki projenizde faturalandırmayı etkinleştirmediniz. | Gemini API'yi kullanmak için [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'yu kullanarak ücretli bir plan oluşturmanız gerekir. |
| 403 | PERMISSION\_DENIED | API anahtarınız gerekli izinlere sahip değil. | Yanlış API anahtarını kullanıyorsunuz. [Uygun kimlik doğrulama](https://ai.google.dev/gemini-api/docs/model-tuning?hl=tr) işleminden geçmeden ayarlanmış bir modeli kullanmaya çalışıyorsunuz. | API anahtarınızın ayarlandığından ve doğru erişime sahip olduğundan emin olun. Ayrıca, ince ayarlı modelleri kullanmak için uygun kimlik doğrulama sürecinden geçtiğinizden emin olun. |
| 404 | NOT\_FOUND | İstenen kaynak bulunamadı. | İsteğinizde referans verilen bir resim, ses veya video dosyası bulunamadı. | İsteğinizdeki tüm parametrelerin API sürümünüz için geçerli olup olmadığını kontrol edin. |
| 429 | RESOURCE\_EXHAUSTED | API'nin hız sınırlarından birini (RPM, TPM, RPD, harcama vb.) aştınız. | Çok fazla istek gönderiyor, çok fazla jeton kullanıyor veya hesabınızın fatura geçmişi ve katmanı için harcamaya dayalı sınırları aşıyorsunuz. | Modelin [hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr) dahilinde olduğunuzu doğrulayın. Bekleyin ve kısa bir süre sonra tekrar deneyin. İsteklerinizin sıklığını veya boyutunu azaltın. Gerekirse [hız sınırı artışı isteyin](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr#request-rate-limit-increase). |
| 499 | İPTAL EDİLDİ | İşlem iptal edildi (genellikle arayan tarafından). | İstemci, API yanıt vermeyi tamamlamadan önce bağlantıyı kapattı. | İstemcinizin veya ağ altyapınızın bağlantıyı erken kapatıp kapatmadığını kontrol edin (ör. istemci tarafında zaman aşımı nedeniyle). |
| 500 | ŞİRKET İÇİ | Google'dan kaynaklanan beklenmeyen bir hata oluştu. | Giriş bağlamınız çok uzun. | Devam eden olaylar için [Gemini API durum sayfasını](https://aistudio.google.com/status?hl=tr) kontrol edin. Giriş bağlamınızı azaltın veya geçici olarak başka bir modele (ör. Gemini 2.5 Pro'dan Gemini 2.5 Flash'e) geçip sorunun çözülüp çözülmediğini kontrol edin. Dilerseniz biraz bekleyip isteğinizi yeniden deneyebilirsiniz. Yeniden denedikten sonra sorun devam ederse lütfen Google AI Studio'daki **Geri bildirim gönder** düğmesini kullanarak sorunu bildirin. |
| 503 | UNAVAILABLE | Hizmet geçici olarak aşırı yüklü veya kapalı olabilir. | Hizmetin kapasitesi geçici olarak dolmuş olabilir. | Devam eden olaylar için [Gemini API durum sayfasını](https://aistudio.google.com/status?hl=tr) kontrol edin. Geçici olarak başka bir modele (ör. Gemini 2.5 Pro'dan Gemini 2.5 Flash'e) geçip çalışıp çalışmadığını kontrol edin. Dilerseniz biraz bekleyip isteğinizi yeniden deneyebilirsiniz. Yeniden denedikten sonra sorun devam ederse lütfen Google AI Studio'daki **Geri bildirim gönder** düğmesini kullanarak sorunu bildirin. |
| 504 | DEADLINE\_EXCEEDED | Hizmet, işleme işlemini son tarihe kadar tamamlayamıyor. | İsteminiz (veya bağlamınız), zamanında işlenemeyecek kadar büyük. | Bu hatayı önlemek için istemci isteğinizde daha büyük bir "zaman aşımı" ayarlayın. |

## Hata yanıtı biçimi

Bir `GenerateContent` isteği başarısız olduğunda API, HTTP durum kodunu (ör. `400 Bad Request`, `403 Forbidden` veya `429 Too Many Requests`) ayarlar ve gRPC durum ayrıntılarını içeren bir JSON yanıt gövdesi döndürür:

```
{
  "error": {
    "code": 400,
    "message": "API key not valid. Please pass a valid API key.",
    "status": "INVALID_ARGUMENT",
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "reason": "API_KEY_INVALID",
        "domain": "googleapis.com",
        "metadata": {
          "service": "generativelanguage.googleapis.com"
        }
      },
      {
        "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
        "locale": "en-US",
        "message": "API key not valid. Please pass a valid API key."
      }
    ]
  }
}
```

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `code` | tam sayı | HTTP durum kodu. |
| `message` | dize | Hatayla ilgili, kullanıcıların okuyabileceği bir açıklama. |
| `status` | dize | `SCREAMING_CASE` içindeki gRPC durum kodu. |
| `details` | dizi | `ErrorInfo` veya `LocalizedMessage` gibi ek hata bağlamı. |

## Sırada ne var?

- [API sorunlarını giderme](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=tr): Sık karşılaşılan sorunları ve hata senaryolarını çözün.
- [Hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr): İstek sınırları ve kota işleme hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-11 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-11 UTC."],[],[]]
