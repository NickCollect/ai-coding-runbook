---
source_url: https://ai.google.dev/gemini-api/docs/api-errors?hl=tr
fetched_at: 2026-09-28T06:13:37.858703+00:00
title: "API hatalar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# API hataları

Bu sayfada, tüm Interactions API hata kodları için referans sağlanmakta, hata yanıtı biçimi açıklanmakta ve API'nin farklı istek türleri için hataları nasıl ilettiği anlatılmaktadır.

## Standart API hata kodları

Bu genel istek düzeyindeki hata kodları, standart HTTP durum kodlarına karşılık gelir.
Hataları programatik olarak işlemek için uygulama mantığınızdaki `code` alanını kullanın.

| Kod | HTTP Durumu | Açıklama | Önerilen işlem |
| --- | --- | --- | --- |
| `invalid_request` | 400 Hatalı İstek | İstek yükü yanlış biçimlendirilmiş veya geçersiz parametreler içeriyor. | İstek söz diziminizi ve parametrelerinizi [API referansıyla](https://ai.google.dev/api/interactions-api?hl=tr) karşılaştırarak kontrol edin. |
| `failed_precondition` | 400 Hatalı İstek | Bir ön koşul karşılanmadığı için (ör. faturalandırma devre dışı bırakılmış) istek işlenemiyor. | Proje faturalandırma durumunu veya hesap ön koşullarını doğrulayın. |
| `out_of_range` | 416 İstenen Aralık Karşılanamıyor | İstek parametresi geçerli aralığın dışında. | Parametre değerlerini ve sınırlarını kontrol edin. |
| `parameter_unknown` | 400 Hatalı İstek | İstek bilinmeyen bir parametre içeriyor. | Tanınmayan parametreyi kaldırıp tekrar deneyin. |
| `authentication` | 401 Yetkilendirilmedi | API anahtarı eksik, geçersiz veya süresi dolmuş. | [API anahtarınızı](https://ai.google.dev/gemini-api/docs/api-key?hl=tr) doğrulayın. |
| `payment_required` | 402 Ödeme Gerekli | Ön ödeme kredisi bakiyeniz tükendi. | Faturalandırma hesabınıza [kredi ekleyin](https://ai.google.dev/gemini-api/docs/billing?hl=tr#buy-credits) veya [otomatik para yükleme](https://ai.google.dev/gemini-api/docs/billing?hl=tr#auto-reload) özelliğini etkinleştirin. Yeniden denemeyin: Kredi eklenene kadar istek başarılı olmaz. |
| `permission_denied` | 403 Yasak | API anahtarınızın bu kaynak için izni yok. | API anahtarı izinlerinizi ve proje erişiminizi kontrol edin. |
| `not_found` | 404 Bulunamadı | İstenen kaynak bulunamadı. | Kaynak yolunu ve parametreleri doğrulayın. |
| `model_not_found` | 404 Bulunamadı | Belirtilen model bulunamadı. | Model adını doğrulayın veya farklı bir modele geri dönün. |
| `already_exists` | 409 Çakışma | Oluşturmayı denediğiniz varlık zaten mevcut. | Yeniden oluşturmadan önce kaynağın mevcut olup olmadığını kontrol edin. |
| `aborted` | 409 Çakışma | İşlem, çakışma veya eşzamanlılık kontrolü hatası nedeniyle iptal edildi. | İsteği daha yüksek bir uygulama düzeyinde yeniden deneyin. |
| `rate_limit_exceeded` | 429 Çok Fazla İstek Var | Dakika veya saniye başına istek ya da jeton sınırını aştınız. | Bekleyin ve eksponansiyel geri yüklemeyle yeniden deneyin. |
| `quota_exceeded` | 429 Çok Fazla İstek Var | Günlük kotanızı aştınız. | Kota sıfırlanana kadar bekleyin veya kota artışı isteyin. |
| `too_many_requests` | 429 Çok Fazla İstek Var | Kısa süre içinde çok fazla istek gönderdiniz. | Bekleyin ve eksponansiyel geri yüklemeyle yeniden deneyin. |
| `cancelled` | 499 İstemci İsteği Kapattı | İstemci, istek tamamlanmadan önce iptal etti. | Herhangi bir işlem yapmanız gerekmez. Bu durum genellikle istemcinin bağlantısının kesildiği anlamına gelir. |
| `api_error` | 500 Dahili Sunucu Hatası | Sunucuda beklenmeyen bir hata oluştu. | İsteği yeniden deneyin. Sorun devam ederse destek ekibiyle iletişime geçin. |
| `unimplemented` | 501 Uygulanmadı | İşlem veya özellik uygulanmamış ya da desteklenmiyor. | API özelliklerini kontrol edin veya desteklenen bir özelliğe geçin. |
| `service_unavailable` | 503 Hizmet Kullanılamıyor | Hizmet geçici olarak aşırı yüklü veya kapalı. | Bekleyin ve eksponansiyel geri yüklemeyle yeniden deneyin. |
| `deadline_exceeded` | 504 Ağ Geçidi Zaman Aşımı | İstek, son tarihe kadar tamamlanmadı. | Sunucu varsayılanını kullanmak için istemci son tarihi ayarını kaldırın veya artırın. |

## Oluşturma engellenen kodlar

Bu hata kodları, politika, güvenlik veya içerik kısıtlamaları nedeniyle modelin çıkışının engellendiğini gösterir. Bu kodlardan birini aldığınızda girişinizi değiştirip tekrar deneyin.

| Kod | Açıklama |
| --- | --- |
| `safety` | Güvenlik ihlalleri (zararlı içerik) nedeniyle istek engellendi. |
| `recitation` | Telif hakkı veya alıntı kısıtlamaları nedeniyle istek engellendi. |
| `language` | Desteklenmeyen bir dil, isteği engelledi. |
| `prohibited_content` | Yasaklanmış içerik kuralları nedeniyle istek engellendi. |
| `spii` | Hassas kimlik bilgileri kısıtlamaları nedeniyle istek engellendi. |
| `blocklist` | Engellenenler listesindeki yasaklanmış terimler isteği engelledi. |
| `image_safety` | Güvenlik ihlalleri nedeniyle görüntü oluşturma engellendi. |
| `image_prohibited_content` | Yasaklanmış içerik kuralları, görüntü oluşturmayı engelledi. |
| `image_recitation` | Telif hakkı veya alıntı kısıtlamaları, görüntü oluşturmayı engelledi. |
| `image_other` | Belirtilmeyen nedenlerle görüntü üretme işlemi engellendi. |
| `content_blocked` | Belirtilmeyen bir politika nedeniyle istek engellendi. |

## Üretim hata kodları

Bu hata kodları, modelin oluşturduğu çıkışla ilgili yapısal bir sorun olduğunu (ör. hatalı biçimlendirilmiş bir işlev çağrısı veya bildirilmemiş bir araç çağrısı) gösterir.

| Kod | Açıklama |
| --- | --- |
| `malformed_function_call` | Model, ayrıştırılamayan bir işlev çağrısı oluşturdu. |
| `malformed_tool_call` | Model, ayrıştırılamayan bir araç çağrısı oluşturdu. |
| `unexpected_tool_call` | Model, istekte belirtilmeyen bir aracı çağırdı. |
| `no_image` | Model, resim üretemedi. |
| `too_many_tool_calls` | Model, izin verilenden daha fazla araç çağrısı oluşturdu. |
| `missing_thought_signature` | Yanıtta gerekli düşünce imzası eksik. |

## Hata yanıtı biçimi

Etkileşimler API'sinden gelen tüm hatalar, `error` ve `message` içeren bir `code` nesnesi döndürür. Örneğin, desteklenmeyen bir araç türü iletildiğinde şu yanıt döndürülür:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'. Supported values: 'function', 'code_execution', 'mcp_server', 'filesystem', 'google_maps', 'google_search', 'bash', 'computer_use', 'file_search', 'url_context'."
  }
}
```

| Alan | Tür | Açıklama |
| --- | --- | --- |
| `code` | dize | `snake_case` içinde makine tarafından okunabilir bir hata kodu. |
| `message` | dize | Neyin yanlış gittiğine dair, kullanıcılar tarafından okunabilir bir açıklama. |

## Hatalar nasıl iletilir?

API, standart bir HTTP isteği mi yoksa akış (SSE) isteği mi gönderdiğinize bağlı olarak hataları farklı şekilde iletir.

### Standart HTTP istekleri

Standart (akış olmayan) istekler için API, HTTP yanıt durum kodunu (ör. `400 Bad Request`, `401 Unauthorized` veya `429 Too Many Requests`) ayarlar ve JSON yanıt gövdesinde bir `error` nesnesi döndürür:

```
{
  "error": {
    "code": "invalid_request",
    "message": "The value 'invalid_tool_type_xyz' is not supported for 'type' at 'tools[0]'."
  }
}
```

### Akış (SSE) istekleri

Akış istekleri (`stream: true`) için API, `event_type` değeri `"error"` olarak ayarlanmış Server-Sent Events (SSE) akışı üzerinden hata etkinlikleri gönderir. `error` alanı aynı `code` ve `message` yapısını içerir:

```
{
  "event_type": "error",
  "error": {
    "code": "not_found",
    "message": "Failed to get completed interaction: Result not found."
  }
}
```

Tam SSE etkinlik şeması için [Interactions API Referansı](https://ai.google.dev/api/interactions-api?hl=tr)'na bakın.

## Sırada ne var?

- [API sorunlarını giderme](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=tr): Sık karşılaşılan sorunları ve hata senaryolarını çözün.
- [Hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr): İstek sınırları ve kota işleme hakkında bilgi edinin.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-20 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-20 UTC."],[],[]]
