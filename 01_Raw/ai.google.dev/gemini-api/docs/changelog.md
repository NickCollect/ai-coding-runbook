---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=tr
fetched_at: 2026-11-02T07:01:11.555926+00:00
title: "S\u00fcr\u00fcm notlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

Gemini 4 Argon hemen oynayabilirsiniz. [Deneyin](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=tr).

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Sürüm notları

Bu sayfada, Gemini API ile ilgili güncellemeler yer alır.

## 30 Ekim 2026

- **Bilgisayar Kullanımı genel kullanıma sunuldu (GA)**: [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) aracı, Interactions ve GenerateContent API'lerinde genel kullanıma sunuldu (GA).

## 27 Ekim 2026

- **Gemini API CLI (`gemini-api`) beta**: Yapay zeka kodlama aracıları, komut dosyaları ve CI ardışık düzenleri için durum bilgisi olmayan, sıfır bağımlılıklı bir komut satırı istemcisi olan [Gemini API CLI](https://ai.google.dev/gemini-api/docs/cli?hl=tr) (`gemini-api`) kullanıma sunuldu. Metin ve medya oluşturmak, dosyaları analiz etmek ve [Gemini tarafından yönetilen temsilcileri](https://ai.google.dev/gemini-api/docs/agents?hl=tr) çalıştırmak için [Interactions API](https://ai.google.dev/gemini-api/docs/interactions?hl=tr)'de `gemini-api` kullanın. Başlamak için [Gemini API CLI kılavuzuna](https://ai.google.dev/gemini-api/docs/cli?hl=tr) göz atın.

## 26 Ekim 2026

- **Generate Content API depolama alanı varsayılan olarak etkin**: Ücretli katmanda Generate Content API'yi (`generateContent`, `streamGenerateContent` ve `batchGenerateContent`) kullanan yeni projeler, artık istekleri varsayılan olarak depoluyor (`store=true`). Bu, Interactions API ile uyumludur. Mevcut projeler geçerli ayarlarını korur. Kapsam dışında kalmak için isteklerde `store=false` değerini ayarlayın veya [Günlükler ve Veri Kümeleri](https://aistudio.google.com/logs?hl=tr) kontrol panelinin **Ayarlar** panelinde Content API günlük kaydı oluşturma ayarını devre dışı bırakın. Ayrıntılar için [Günlükler ve veri kümeleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr#configure-logging) bölümüne bakın.

## 13 Ekim 2026

- **Gemini 4 Argon (`gemini-4-argon`) genel kullanıma sunulma tarihi (GA)**: Karmaşık kodlama, ajan tabanlı, matematik ve fen bilimleri görevleri için tasarlanmış en yetenekli modelimiz olan [Gemini 4 Argon](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=tr) (`gemini-4-argon`) kullanıma sunuldu.

  API değişiklikleri, fiyatlandırma ve taşıma kılavuzu için [Gemini 4 Argon'daki yenilikler](https://ai.google.dev/gemini-api/docs/latest-model?hl=tr) başlıklı makaleyi inceleyin.

## 8 Ekim 2026

- **Gemini 3.7 Flash'in kullanımdan kaldırılması**:
  [`gemini-3.7-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.7?hl=tr) kullanımdan kaldırıldı ve yerine [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=tr) getirildi.
  Bu model artık Google AI Studio'da seçilemiyor ve `gemini-3.7-flash` için API istekleri otomatik olarak `gemini-3.8-flash` modeline yönlendiriliyor. Model dizesini `gemini-3.8-flash` olarak güncelleyin ve [Gemini 3.8 Flash kılavuzunu](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=tr) inceleyin.
- **Gemini 3.5 Flash'ın desteğinin sonlandırılması**:
  [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5?hl=tr) desteği sonlandırıldı ve yerine [`gemini-3.6-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=tr) getirildi.
  Bu model artık Google AI Studio'da seçilemiyor ve `gemini-3.5-flash` için API istekleri otomatik olarak `gemini-3.6-flash` modeline yönlendiriliyor. Model dizesini `gemini-3.6-flash` (veya [`gemini-3.8-flash`](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=tr)) olarak güncelleyin ve [Gemini 3.6 Flash kılavuzunu](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=tr) inceleyin.
- **Deep Research Agent `deep-research-pro-preview-12-2025` desteğinin sonlandırılması**:
  `deep-research-pro-preview-12-2025` temsilcisi için destek sonlandırıldı ve **23 Ekim 2026**'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#managed-agents).

  İsteklerinizi daha yeni [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) temsilci sürümlerinden birine taşıyın:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=tr):
    Hız ve verimlilik için tasarlanmıştır. İstemci kullanıcı arayüzüne geri akış için idealdir.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=tr):
    Otomatik bağlam toplama ve sentezleme için maksimum kapsamlılık.

  Geçiş yapmak için `interactions.create` isteklerinizdeki `agent` parametresini `deep-research-pro-preview-12-2025` yerine `deep-research-preview-04-2026` (veya `deep-research-max-preview-04-2026`) olarak güncelleyin.

## 6 Ekim 2026

- **Gemini Nano Banana 2.1 genel kullanıma sunuldu**: En yeni yüksek verimli görüntü üretme ve etkileşimli düzenleme modeli olan [Gemini Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=tr) (`gemini-nano-banana-2.1`) kullanıma sunuldu. Nano Banana 2'nin ([`gemini-3.1-flash-image`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr)) güncellenmiş bir sürümü olan bu model, Flash düzeyinde hız ve maliyet verimliliği sunarken görsel kalite, isteme uyma, çok turlu karakter tutarlılığı, metin oluşturma ve geniş ile panoramik en boy oranı oluşturma (`1:4`, `4:1`, `1:8`, `8:1`) konularında `1K`, `2K` ve `4K` çözünürlüklerinde önemli iyileştirmeler sağlar.

  Başlamak için [Görüntü üretme kılavuzuna](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) göz atın.
- **Desteği sonlandırma duyurusu**: `gemini-3.1-flash-image` modelinin desteği sonlandırıldı (kullanımdan kaldırılma tarihi açıklanmadı). [`gemini-nano-banana-2.1`](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1?hl=tr)'e geçiş yapın.

## 22 Eylül 2026

- **Gemini 3.8 Flash TTS ve Gemini 3.8 Flash-Lite TTS genel kullanıma sunuldu (GA)**: Yeni nesil metin okuma (TTS) ses modellerimizi ve Gemini API Voices uç noktasını (`/v1beta/voices`) kullanıma sunduk:

  - **[Gemini 3.8 Flash TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts?hl=tr)
    (`gemini-3.8-flash-tts`)**: Stüdyo kalitesinde ses doğruluğu, nüanslı oyunculuk, bölgesel lehçeler ve uzun biçimli çok turlu kararlılık için tasarlanmış amiral gemisi yaratıcı TTS modeli.
  - **[Gemini 3.8 Flash-Lite TTS](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-lite-tts?hl=tr)
    (`gemini-3.8-flash-lite-tts`)**: Yüksek gönderim hacimli üretim ve gerçek zamanlı sesli temsilci kaskadları için `gemini-3.1-flash-tts-preview` modelinin yerini alacak şekilde tasarlanmış, hızlı ve uygun maliyetli TTS modeli.
  - **[Ses tasarımı](https://ai.google.dev/gemini-api/docs/voice-design?hl=tr),
    [ses kopyalama](https://ai.google.dev/gemini-api/docs/voice-replication?hl=tr) ve
    [Genişletilmiş Ses Kitaplığı](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#voice-library)**:
    Yazılı istemlerden kalıcı özel ses karakterleri oluşturun, rıza doğrulamasıyla sesleri kopyalayın ve 150'den fazla önceden oluşturulmuş ve özel sesle sorgu yapın.

  Başlamak için [Metin Okuma kılavuzuna](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) bakın.

## 18 Eylül 2026

- **Gemini 2.5 modellerine erişimle ilgili güncelleme**: Herkes için güvenilir performans sağlamak amacıyla 2.5 modellerine erişimi, geçmişte bu modelleri aktif olarak kullanan kişilerle sınırlandırıyoruz. Bu modeller kullanımdan kaldırılmamıştır ve bir sonraki duyuruya kadar API üzerinden sunulmaya devam edecektir. Yeni projelerinizde en yeni modellerimiz olan 3.5 Flash-Lite veya 3.8 Flash'i kullanın. Bu sayede hem devam eden eski iş akışları hem de yeni uygulamalar için yeterli kapasiteyi koruyabiliriz.

## 17 Eylül 2026

- **Antigravity Agent 09-2026**: `antigravity-preview-09-2026` yayınlandı. Bu sürüm, `antigravity-preview-05-2026` sürümünün yerini alır ve bu sürümü kullanımdan kaldırır.

  Uzak bir korumalı alanda (`environment: "remote"`) çalışıyorsanız ve yalnızca `output_text` veya `model_output` adımlarını okuyorsanız kullanıcı aracısı dizesini güncelleyin. Başka bir değişiklik yapmanız gerekmez.

  Araçları yerel olarak çalıştırıyorsanız (`local_environment`) veya `function_call` adımlarını ayrıştırıyorsanız yerleşik araçlar değişti. Parametrelerde snake\_case yerine PascalCase kullanılır ve dosya düzenlemelerinde tam yeniden yazma yerine satır aralığı değiştirmeleri kullanılır.

  | Kapasite | 05-2026 | 09-2026 |
  | --- | --- | --- |
  | Dosya oluşturma | `write_file(path, content)` | `write_to_file(TargetFile, CodeContent, Overwrite, Description)` |
  | Dosya düzenleme | `write_file(path, content)`, tamamen yeniden yazma | `replace_file_content(TargetFile, StartLine, EndLine, TargetContent, ReplacementContent)` |
  | Dosya okuma | `read_file(path, offset, limit)`, bayt ofsetleri | `view_file(AbsolutePath, StartLine, EndLine, ContentOffset)` |
  | Dizin listesi | `list_files(path)` | `list_dir(DirectoryPath)` |
  | Dosya ve Kod Arama Aracı | Yok, temsilciler kabuk komutları kullandı | `find_by_name(SearchDirectory, Pattern, MaxDepth)` ve `grep_search(SearchPath, Query, IsRegex)` |
  | Kabuk yürütme | `code_execution(command, timeout_seconds)` | Değiştirilmemiş |
  | Web araması | `google_search(queries)` | Değiştirilmemiş |

  [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr) kılavuzunu inceleyin.
  `antigravity-preview-05-2026`, 5 Ekim 2026'da kullanımdan kaldırılacak. Bu değişiklik, [desteği sonlandırılan özellikler](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#managed-agents) sayfasından takip edilebilir.

## 15 Eylül 2026

- **Gemini 3.8 Live ve Gemini 3.8 Live Extended Thinking genel kullanıma sunuldu
  (GA)**: Live API'yi kullanan anlık ses uygulamaları için iki yeni sesten sese model yayınlandı:

  - **Gemini 3.8 Live** ([`gemini-3.8-live`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live?hl=tr)): Çoğu düşük gecikmeli sesli asistan deneyimi ve akıl yürütme gecikmesi olmadan gerçek zamanlı diyalog için varsayılan seçenek. İç içe yerleştirilmiş akıl yürütme, varsayılan eşzamansız işlev çağrısı ve tam oturum istemci içerik güncellemeleri gibi özellikler sunar.
  - **Gemini 3.8 Live Genişletilmiş Düşünme**
    ([`gemini-3.8-live-extended-thinking`](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking?hl=tr)): Canlı sesli etkileşimler sırasında arka planda akıl yürütmeyi destekleyen, yüksek akıl yürütme kapasitesine sahip sesten sese model. Arka planda daha fazla akıl yürütme gerektiğinde önerilir.

  Başlamak için [Live API kılavuzunu](https://ai.google.dev/gemini-api/docs/live-api?hl=tr), [Özellikler kılavuzunu](https://ai.google.dev/gemini-api/docs/live-api/capabilities?hl=tr) ve [Düşünme kılavuzunu](https://ai.google.dev/gemini-api/docs/live-api/thinking?hl=tr) inceleyin.

## 3 Eylül 2026

- **Lyria 3.5 genel kullanıma sunuldu**: Google'ın müzik üretme modelinin yeni nesli kullanıma sunuldu:

  - [`lyria-3.5`](https://ai.google.dev/gemini-api/docs/models/lyria-3.5?hl=tr):
    Daha iyi müzikal tutarlılık, doğal vokaller, ayrıntılı süre ve yapısal kontrol ile tam uzunlukta şarkı üretimi.

  Model, metin ve resim girişlerini destekler ve yüksek kaliteli 44,1 kHz stereo ses üretir. Ayrıntılar ve kod örnekleri için [Müzik üretimi](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) kılavuzuna bakın.

## 2 Eylül 2026

- **Gemini 3.8 Flash genel kullanıma sunuldu**: Uzun vadeli yazılım mühendisliği, otonom temsilciler ve karmaşık kurumsal iş akışları için tasarlanmış en akıllı Flash modelimiz olan `gemini-3.8-flash` kullanıma sunuldu.

  Başlamak için [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash?hl=tr) model sayfasını ve [Gemini 3.8 Flash kılavuzunu](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8?hl=tr) inceleyin.

## 1 Eylül 2026

- **Temsilci video anlama**: Interactions ve GenerateContent API'lerinde Gemini 3.7 Flash, 3.6 Flash ve 3.5 Flash-Lite için temsilci video anlama özelliği kullanıma sunuldu. Model, video zaman çizelgelerinde dinamik olarak gezinerek transkript, kare veya ses parçası isteyebilir. Bu yaklaşım, statik işlemeye kıyasla uzun içerikler için% 88'e kadar daha az jeton kullanır.

  Başlamak için [Temsilci tabanlı video yorumlama](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#agentic-video-understanding) kılavuzuna bakın.

## 27 Ağustos 2026

- **Gemini Omni Flash genel kullanıma sunuldu**: Hızlı, etkileşimli video üretimi ve düzenleme modelimizin genel kullanıma sunulan sürümü `gemini-omni-1.1-flash` yayınlandı. Bu sürümde önemli yeni özellikler sunulmaktadır:

  - **Video uzantısı**: `extend` görevini kullanarak veya doğrudan bir istemle klibin sonunda devam bölümleri oluşturarak mevcut videoları sorunsuz bir şekilde uzatın.
  - **Ara değer hesaplama (ilk + son kare)**: En fazla 2 resim içeren `image_to_video` görevini kullanarak iki resim arasında geçiş yapan bir video oluşturun.
  - **Çözünürlük kontrolü**: `video_config` içindeki yeni `resolution` parametresi; `360p`, `720p` (varsayılan), `1080p` ve `4k` çıkışlarını destekler.
    1080p ve 4K çıkışlar, çözünürlük yükseltme kullanılarak oluşturulur.

  Mevcut `gemini-omni-flash-preview` uç noktası 30 Eylül 2026'da kullanımdan kaldırılacak.

  Başlamak için [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=tr) model sayfasını ve [Omni kılavuzunu](https://ai.google.dev/gemini-api/docs/omni?hl=tr) inceleyin.

## 26 Ağustos 2026

- **Gemini 3.5 Transcribe genel kullanıma sunuldu**: Gemini'ın ses anlama özelliğine dayalı iki özel konuşma metni modeli yayınlandı:

  - **Gemini 3.5 Transcribe** (`gemini-3.5-transcribe`): 85'ten fazla dilde ifade tabanlı dil algılama, konuşmacı ayırt etme, kelime düzeyinde zaman damgaları ve özel kelime listesi ağırlıklandırma (1.000 terime kadar) özellikleriyle yüksek doğruluk ve düşük gecikme süreli, akışsız konuşmayı metne dönüştürme.
  - **Gemini 3.5 Transcribe Live** (`gemini-3.5-transcribe-live`):
    Live API'yi kullanarak WebSockets üzerinden düşük gecikmeli, çift yönlü akışlı konuşmayı metne dönüştürme özelliği. Geçici ve kesinleşmiş transkript etkinliklerini, akıllı transkript modunu ve birden fazla ses etkinliği algılama (VAD) stratejisini destekler.

  Başlamak için [Ses transkripti kılavuzuna](https://ai.google.dev/gemini-api/docs/transcribe?hl=tr), [Canlı transkript kılavuzuna](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe?hl=tr) ve [Gemini 3.5 Transcribe model sayfasına](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe?hl=tr) göz atın.

## 13 Ağustos 2026

- **Gemini 3.7 Flash genel kullanıma sunuldu**: Kodlama ve temsilciler için şimdiye kadarki en akıllı ve verimli modelimizi kullanıma sunduk:

  - **Gemini 3.7 Flash** (`gemini-3.7-flash`): Yazılım mühendisliği, web geliştiricisi ve ajan tabanlı iş akışlarında önemli iyileştirmeler sunan bu model, 31 Aralık 2026'ya kadar tanıtım fiyatıyla kullanılabilir.

  Başlamak için [Gemini 3.7 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.7-flash?hl=tr) model sayfasını ve [En yeni model kılavuzunu](https://ai.google.dev/gemini-api/docs/latest-model?hl=tr) inceleyin.

## 30 Temmuz 2026

- **Gemini Robotics ER 2 genel önizlemede**: Robotik için iki yeni somutlaştırılmış akıl yürütme modeli uç noktası yayınlandı:

  - `gemini-robotics-er-2-preview`: Gelişmiş uzamsal akıl yürütme, temsilci tabanlı kod yürütme, çok adımlı araç düzenleme, videoda an bulma, ilerleme sınıflandırması ve çoklu robot koordinasyonu.
  - `gemini-robotics-er-2-streaming-preview`: Live API kullanılarak gerçek zamanlı metin akışı için optimize edilmiştir. Çift yönlü ses ve video girişiyle düşük gecikmeli robot temsilciler sağlar.

  Her iki model uç noktası da metin, resim, video ve ses girişlerini kabul eder ve fiziksel robot eylemleri için engelleme davranışıyla işlev çağrısını destekler.
  Başlamak için [Gemini Robotics ER'ye genel bakış](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr) başlıklı makaleyi inceleyin. Gerçek zamanlı akış kullanım alanları için [Akış ile robotik](https://ai.google.dev/gemini-api/docs/robotics-streaming?hl=tr) başlıklı makaleyi inceleyin.
- **Desteğin sonlandırılmasıyla ilgili duyuru**: `gemini-robotics-er-1.6-preview` modeli 31 Ağustos 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 21 Temmuz 2026

- **Gemini 3.6 Flash ve Gemini 3.5 Flash-Lite genel kullanıma sunuldu**:
  En yeni 3.x Flash modellerimizin kararlı ve üretime hazır sürümleri yayınlandı:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): 3.5 Flash'e kıyasla daha düşük bir fiyat noktasında daha iyi token verimliliği ve kod/temsilci planlama özellikleri sunarak geliştiricilerin çıktı ayrıntı düzeyiyle ilgili geri bildirimlerini ele alır.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): Yüksek hacimli otomasyon için tasarlanmış, düşük gecikmeli ve son derece uygun maliyetli bir alt temsilci seçeneği sunar.

  Daha fazla bilgi için [Gemini 3.6 Flash kılavuzunu](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=tr) inceleyin.
- **Desteği sonlandırılan parametreler**: `temperature`, `top_p` ve `top_k` örnekleme parametrelerinin desteği sonlandırıldı. Ayrıntılar için
  [Gemini 3.6 Flash kılavuzuna](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.6?hl=tr#sampling-parameter-deprecation)
  bakın.

## 6 Temmuz 2026

- Interactions API için [geliştirici günlükleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) desteği: Desteklenen Interactions API çağrılarına ait günlükler artık [AI Studio kontrol panelinde](https://aistudio.google.com/logs?hl=tr) görüntülenebilir.

## 30 Haziran 2026

- **Genel Önizleme'de Gemini Omni Flash**: Yüksek hızlı video üretimi ve etkileşimli video düzenleme için tasarlanmış yüksek performanslı çok formatlı bir model olan `gemini-omni-flash-preview` kullanıma sunuldu. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)'yi kullanarak metin açıklamalarından 720p çözünürlükte 3-10 saniyelik videolar oluşturabilir veya hareketsiz görüntüleri canlandırabilir, ardından çıktıları sohbet yoluyla düzenleyip iyileştirebilirsiniz. Başlamak için [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=tr) kılavuzuna ve [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=tr) model kartına göz atın.
- Ultra düşük gecikme süresi ve uygun maliyetli görüntü üretme ve düzenleme için optimize edilmiş yerleşik çok formatlı modelimiz `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) genel kullanıma sunuldu. [Gemini 3.1 Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=tr) model kartını ve [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) kılavuzunu inceleyin.

## 24 Haziran 2026

- **Bilgisayar Kullanımı**: Gemini 3.5 Flash'te [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) aracı için genel önizleme desteği kullanıma sunuldu. Bu sürümde, niyetlerle basitleştirilmiş işlemler, tarayıcı, mobil ve masaüstü ortamları için yerleşik destek, yapılandırılabilir güvenlik politikaları ve gelişmiş istem enjeksiyonu tespiti yer alıyor.

## 17 Haziran 2026

- **Konuşma üretimi için akış desteği**: `streamGenerateContent` (ve Interactions API'de `stream: true`) üzerinden akış artık `gemini-3.1-flash-tts-preview` modeli için destekleniyor. Daha fazla bilgi edinmek için [Metin Okuma](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#streaming) kılavuzunu inceleyin.

## 15 Haziran 2026

- **Desteği sonlandırma duyurusu**: Aşağıdaki görüntü üretme modellerinin desteği sonlandırılacak ve **17 Ağustos 2026**'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - **Imagen 4 ve Gemini 3 Image modelleri**:
    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

  Kodunuzu daha yeni kararlı veya önizleme uç noktalarına taşımak için [Gemini'da desteği sonlandırılan özellikler](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#imagen-models) sayfasını inceleyin.
- **Desteği sonlandırma duyurusu**: Aşağıdaki video üretim modellerine verilen destek sonlandırılacak ve bu modeller **30 Haziran 2026**'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - **Veo modelleri**:
    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

  Hizmet kesintilerini önlemek için entegrasyonunuzu Veo 3.1 önizleme model kimliklerini (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) veya [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=tr) üzerinden erişilebilen 3.1 GA modellerini kullanacak şekilde güncelleyin.
- **Desteği sonlandırma duyurusu**: Deneysel GMP Bağlam Görünümü aracı (Google Haritalar ile Temellendirme çıkışları için sabit bir arayüz) **15 Haziran 2026**'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

## 1 Haziran 2026

- Aşağıdaki Gemini 2.0 modelleri [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Bunun yerine [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) veya [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) kullanın.

## 28 Mayıs 2026

- Yerel görsel modellerimiz [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr) ve [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=tr)'ın genel kullanıma sunulan (GA) sürümleri olan `gemini-3.1-flash-image` (Nano Banana 2) ve `gemini-3-pro-image` (Nano Banana Pro) kullanıma sunuldu.
- **Videodan görüntü üretme desteği**: Artık yüksek kaliteli küçük resimler, sinematik film afişleri veya özet infografikler oluşturmak için yazılı istemle birlikte çok formatlı bağlam olarak bir video dosyası (doğrudan yükleme veya herkese açık YouTube URL'si olarak) iletebilirsiniz. Bu özellik yalnızca `gemini-3.1-flash-image` modelinde desteklenir. Daha fazla bilgi edinmek için [Videodan görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#video-to-image) kılavuzunu inceleyin.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-3.1-flash-image-preview` ve `gemini-3-pro-image-preview` modelleri için destek sonlandırıldı ve bu modeller 25 Haziran 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 25 Mayıs 2026

- `gemini-3.1-flash-lite-preview` modeli [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). Bunun yerine [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) kullanın.

## 19 Mayıs 2026

- Temsilci ve kodlama görevlerinde sürekli olarak üst düzey performans sunan en akıllı modelimiz [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr)'ın genel kullanıma sunulan (GA) sürümü `gemini-3.5-flash` tarihinde yayınlandı. Bu model artık `gemini-flash-latest`'ın temelini oluşturuyor.
- **Gemini API'de Yönetilen Ajanlar**, genel önizleme sürümünde kullanıma sunuldu. Bu sayede geliştiriciler, Google tarafından barındırılan güvenli ve yalıtılmış Linux korumalı alan ortamlarında çalışan otonom ve durum bilgisi olan aracılar oluşturup dağıtabilir. Daha fazla bilgi edinmek için [Temsilcilere genel bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr) sayfasını ve [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) kılavuzunu inceleyin.
- Genel amaçlı **Antigravity Agent** yönetilen temsilcisi [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=tr), genel önizleme sürümünde kullanıma sunuldu.
  Antigravity ajanı; bağımsız olarak planlama yapabilir, akıl yürütebilir, kod yazıp çalıştırabilir, dosyaları yönetebilir ve korumalı alan kapsayıcısında web'de gezinebilir. Kod örnekleri ve teknik özellikler için [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr) kılavuzuna bakın.

## 7 Mayıs 2026

- Hız, ölçek ve maliyet verimliliği için optimize edilmiş [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr)'ın genel kullanıma sunulan (GA) sürümü `gemini-3.1-flash-lite` tarihinde yayınlandı.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-3.1-flash-lite-preview` modeline verilen destek 11 Mayıs 2026'da sonlandırılacak ve model 25 Mayıs 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 6 Mayıs 2026

- **Yakında yapılacak zarar veren değişiklik**: [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) istek ve yanıt şeması (`outputs` → `steps`) ile çıkış formatı yapılandırması (`response_format`) değişiyor. Yeni şema **26 Mayıs**'ta varsayılan şema olacak ve eski şema **8 Haziran**'da kaldırılacak.
  Ayrıntılar için
  [geçiş rehberini](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=tr)
  inceleyin.

## 5 Mayıs 2026

- **Dosya Arama**, çok formatlı aramayı destekleyecek şekilde güncellendi. Artık `gemini-embedding-2` modelini kullanarak görüntüleri yerel olarak yerleştirebilir ve arayabilirsiniz.
  Temellendirme meta verileri artık görsel alıntılar için `media_id` ve bilgilerin nerede bulunduğunu gösteren `page_numbers` içeriyor. Daha fazla bilgi edinmek için [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) kılavuzunu inceleyin.

## 4 Mayıs 2026

- Batch API ve uzun süreli işlemler için yoklama iş akışlarının yerini alacak, etkinliğe dayalı [Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=tr) desteği Gemini API'de kullanıma sunuldu.

## 30 Nisan 2026

- `gemini-robotics-er-1.5-preview` modeli [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). Bunun yerine [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=tr) kullanın.

## 22 Nisan 2026

- `gemini-embedding-2`, genel kullanıma sunuldu (GA). Daha fazla bilgi için [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) (Yerleştirmeler) sayfasını inceleyin.

## 21 Nisan 2026

- Ortak planlama, görselleştirme desteği, MCP sunucusu entegrasyonu ve dosya arama özelliklerine sahip [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) temsilcisinin yeni sürümleri yayınlandı:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=tr): Hız ve verimlilik için tasarlanmıştır. İstemci kullanıcı arayüzüne geri akış için idealdir.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=tr): Otomatik bağlam toplama ve sentezleme için maksimum kapsamlılık.

## 15 Nisan 2026

- Maliyet açısından verimli, etkileyici ve yönlendirilebilir metin okuma modelimiz [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=tr)'u kullanıma sunduk. Daha fazla bilgi edinmek için [Text-to-Speech](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) belgelerini okuyun.

## 14 Nisan 2026

- Güncellenmiş robotik modelimiz `gemini-robotics-er-1.6-preview` yayınlandı.
  Artık enstrüman okuma, gelişmiş uzamsal ve fiziksel akıl yürütme gibi yeni özelliklere sahip. Daha fazla bilgi edinmek için [Gemini Robotics ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr) sayfasını ve [blogu](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=tr) inceleyin.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-robotics-er-1.5-preview` modeli, 30 Nisan 2026 saat 09:00'da (PST) [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 2 Nisan 2026

- [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=tr) lansmanı kapsamında `gemma-4-26b-a4b-it` ve `gemma-4-31b-it` modellerini kullanıma sunduk. Bu modelleri [AI Studio](https://aistudio.google.com?hl=tr)'da ve Gemini API üzerinden kullanabilirsiniz.

## 1 Nisan 2026

- Maliyet veya gecikmeyi optimize etmek için daha fazla seçenek sunan yeni [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr) ve [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) çıkarım katmanları kullanıma sunuldu.

## 31 Mart 2026

- Hızlı iterasyon ve yüksek hacimli uygulamalar oluşturmak için tasarlanmış, en uygun maliyetli [video üretim](https://ai.google.dev/gemini-api/docs/video?hl=tr) modelimiz olan Veo 3.1 Lite Preview'u ([`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=tr)) kullanıma sunduk.
- `gemini-2.5-flash-lite-preview-09-2025` modeli kullanımdan kaldırıldı. Bunun yerine [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) kullanın.

## 26 Mart 2026

- Gerçek zamanlı diyalog ve ses öncelikli yapay zeka uygulamaları için tasarlanmış en yeni sesten sese (A2A) model olan [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=tr)'ı kullanıma sunduk. Başlamak için [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr) belgelerini okuyun.

## 25 Mart 2026

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) müzik üretme modelleri kullanıma sunuldu: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=tr) (30 saniyelik klipler) ve [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=tr) (tam uzunlukta şarkılar). Her iki model de metin ve görüntü girişlerini kabul eder ve yüksek kaliteli, 48 kHz stereo ses üretir. Ayrıntılar ve kod örnekleri için [Müzik üretimi](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) kılavuzuna bakın.

## 23 Mart 2026

- AI Studio'da [ön ödemeli ve sonradan ödemeli faturalandırma planları](https://ai.google.dev/gemini-api/docs/billing?hl=tr) kullanıma sunuldu. Mevcut hesaplar etkilenebilir. Daha fazla bilgi için [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) belgelerini okuyun.

## 18 Mart 2026

- Yeni [Yerleşik Araçlar ve İşlev Çağrısı Kombinasyonu](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) özelliği kullanıma sunuldu. Bu özellik sayesinde Gemini'ın yerleşik araçlarını, özel işlev çağrısı araçlarıyla birlikte tek bir API çağrısında kullanabilirsiniz.
- [Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr#supported_models),
  artık Gemini 3 modellerinde destekleniyor.

## 16 Mart 2026

- Daha iyi bir kullanıcı faturalandırma deneyimi için yenilenen [Kullanım Katmanları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#about-billing) ve [Faturalandırma Hesabı harcama sınırları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#tier-spend-caps) kullanıma sunuldu.

## 12 Mart 2026

- AI Studio'da faturalandırma için [proje düzeyinde harcama sınırları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#project-spend-caps) kullanıma sunuldu.

## 10 Mart 2026

- İlk çok formatlı yerleştirme modelimiz olan `gemini-embedding-2-preview` kullanıma sunuldu.
  Metin, resim, video, ses ve PDF girişlerini destekler ve tüm modaliteleri birleşik bir yerleştirme alanına eşler. Daha fazla bilgi edinmek için [Yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) başlıklı makaleyi inceleyin.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-2.5-flash-lite-preview-09-2025` modeli 31 Mart 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 9 Mart 2026

- Gemini 3 Pro Preview modeli [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). `gemini-3-pro-preview` artık [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) değerini gösteriyor.

## 3 Mart 2026

- Gemini 3 serisinin ilk Flash-Lite modeli olan Gemini 3.1 Flash-Lite Preview'u kullanıma sunduk. Teknik özellikler, belirli güncellemeler ve geliştirici kılavuzu için [model sayfasını](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) okuyun.

## 26 Şubat 2026

- Hız ve yüksek hacimli kullanım alanları için optimize edilmiş, yüksek verimliliğe sahip bir model olan Nano Banana 2, [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr) kullanıma sunuldu.
- Desteği sonlandırma duyurusu: Gemini 3 Pro Preview (`gemini-3-pro-preview`) 9 Mart 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 19 Şubat 2026

- Yeni Gemini 3 serisi ailesinin en son sürümü olan [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) kullanıma sunuldu.
- Bash ve araçları birlikte kullanan kullanıcılar için özel araçları önceliklendirmede daha iyi olan ayrı bir uç nokta (`gemini-3.1-pro-preview-customtools`) kullanıma sunuldu.

## 18 Şubat 2026

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modeller 1 Haziran 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 Şubat 2026

- Aşağıdaki modeller [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 Ocak 2026

- `gemini-3-pro-preview` ve `gemini-3-flash-preview` dillerinde bilgisayar kullanımı aracı için destek kullanıma sunuldu.

## 21 Ocak 2026

- `latest` takma adları değiştirildi:

  - `gemini-pro-latest`, `gemini-3-pro-preview` olarak değiştirildi
  - `gemini-flash-latest`, `gemini-3-flash-preview` olarak değiştirildi

## 15 Ocak 2026

- Desteği sonlandırma duyurusu: Aşağıdaki modeller 17 Şubat 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` modeli kullanımdan kaldırıldı.

## 14 Ocak 2026

- `text-embedding-004` modeli [kullanımdan kaldırıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 13 Ocak 2026

- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) için 4K çıkış çözünürlükleri ve tüm çözünürlüklerde dikey videolar için daha fazla destek eklendi.

## 12 Ocak 2026

- Model yaşam döngüsü özelliği kullanıma sunuldu. Bazı modeller artık yaşam döngüsü aşamasını ve desteği sonlandırma zaman çizelgesini belirtecek. Daha fazla bilgi için aşağıdaki belgelere bakın:

  - [Model aşamaları](https://ai.google.dev/api/generate-content?hl=tr#ModelStatus)

## 8 Ocak 2026

- Gemini API için veri giriş kaynağı olarak Cloud Storage paketleri ve herkese açık ve özel DB önceden imzalanmış URL'leri için destek kullanıma sunuldu. Dosya boyutu sınırı da 20 MB'tan 100 MB'a yükseltildi. Ayrıntılar için [Dosya giriş yöntemleri kılavuzu](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr)'nu inceleyin.

## 19 Aralık 2025

- v1beta sürümünde Interactions API'de zarar veren bir değişiklik yapıldı. `total_reasoning_tokens` alanı, düşünme modellerindeki "düşünceler" kavramına daha iyi uyum sağlaması için `total_thought_tokens` olarak yeniden adlandırıldı.

## 17 Aralık 2025

- Gemini 3 Flash Preview'u (`gemini-3-flash-preview`) kullanıma sunduk. Bu model, daha büyük modellerle rekabet edebilecek düzeyde hızlı ve üstün performans sunarken maliyeti de çok daha düşük. Gelişmiş görsel ve uzamsal akıl yürütme ve temsilci tabanlı kodlama özellikleriyle. Aşağıdakiler de dahil olmak üzere bazı yeni özelliklerle ilgili belgeleri okuyun:

  - [Çok formatlı işlev yanıtları](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#multimodal)
  - [Resimlerle kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#images)

## 12 Aralık 2025

- Live API için yeni bir yerel ses modeli olan `gemini-2.5-flash-native-audio-preview-12-2025` kullanıma sunuldu. Bu güncellemeyle model, karmaşık iş akışlarını daha iyi yönetebilecek. Daha fazla bilgi için [Live API kılavuzuna](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-native-audio-preview-12-2025?hl=tr) sayfasına bakın.

## 11 Aralık 2025

- Interactions API kullanıma sunuldu. Bu API, Gemini modelleri ve temsilcileriyle etkileşim kurmak için birleşik bir arayüz sağlar. Daha fazla bilgi edinmek için [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) kılavuzunu inceleyin.
- Gemini Deep Research temsilcisini önizleme sürümünde kullanıma sunduk. Çok adımlı araştırma görevleri için sonuçları otonom olarak planlayabilir, uygulayabilir ve sentezleyebilir. Ayrıntılar için [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) kılavuzuna bakın.

## 10 Aralık 2025

- [Metin okuma modellerimizde](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) geliştirmeler yaptık. Gemini 2.5 Flash TTS önizlemesi (düşük gecikme için optimize edildi) ve Gemini 2.5 Pro TTS önizlemesi (kalite için optimize edildi) artık daha etkileyici, daha hassas tempoya sahip ve daha akıcı diyaloglar sunuyor.

## 9 Aralık 2025

- Aşağıdaki Gemini Live API modelleri kullanımdan kaldırıldı:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 Aralık 2025

- [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) için Gemini 3 faturalandırması 5 Ocak 2026'da başlayacak.

## 4 Aralık 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-2.5-flash-image-preview` modeli 15 Ocak 2026'da kullanımdan kaldırılacak.

## 3 Aralık 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: `text-embedding-004` modeli 14 Ocak 2026'da kullanımdan kaldırılacak.

## 20 Kasım 2025

- Nano Banana modelinin bir sonraki sürümü olan Gemini 3 Pro Image Preview (`gemini-3-pro-image-preview`) kullanıma sunuldu. Daha fazla bilgi için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) sayfasını okuyun.

## 18 Kasım 2025

- Güçlü temsilci ve kodlama özelliklerine sahip, son teknoloji akıl yürütme ve çok formatlı anlama modelimiz olan ilk Gemini 3 serisi model `gemini-3-pro-preview`'ü kullanıma sunduk.

  Gemini 3 Pro Preview, zeka ve performans iyileştirmelerinin yanı sıra aşağıdaki konularda yeni davranışlar sunar:

  - [Medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/media-resolution?hl=tr)
  - [Düşünce imzaları](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr)
  - [Düşünme düzeyleri](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#thinking-levels)

  Taşıma, yeni özellikler ve teknik özellikler için [Gemini 3 Geliştirici Kılavuzu](https://ai.google.dev/gemini-api/docs/gemini-3?hl=tr)'nu okuyun.

## 11 Kasım 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modeller kapatılacak:

  - 12 Kasım:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 Kasım:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 Kasım 2025

- Aşağıdaki model kullanımdan kaldırıldı:

  - `imagen-3.0-generate-002`

  Bunun yerine [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=tr#imagen-4)'ü kullanın. Daha fazla bilgi için [Gemini'da kullanımdan kaldırılan özellikler tablosuna](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr) bakın.

## 6 Kasım 2025

- File Search API'yi genel önizlemeye açarak geliştiricilerin yanıtları kendi verilerine dayandırmasına olanak tanıdık. Daha fazla bilgi için yeni [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) sayfasını okuyun.

## 4 Kasım 2025

- [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)'da resimler için giriş parça sayısı 1.290'dan 258'e düşürülerek resim düzenleme maliyeti azaltıldı.
- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modeller kapatılacak:

  - 18 Kasım:

    - `gemini-2.5-flash-lite-preview-06-17`
    - `gemini-2.5-flash-preview-05-20`
  - 2 Aralık:

    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-thinking-exp-01-21`
    - `gemini-2.0-flash-thinking-exp-1219`
    - `gemini-2.5-pro-preview-03-25`
    - `gemini-2.5-pro-preview-05-06`
    - `gemini-2.5-pro-preview-06-05`
  - 9 Aralık:

    - `gemini-2.0-flash-lite-preview`
    - `gemini-2.0-flash-lite-preview-02-05`
    - `gemini-2.0-flash-exp`
    - `gemini-2.0-pro-exp`
    - `gemini-2.0-pro-exp-02-05`

## 29 Ekim 2025

- Gemini API için yeni [günlük kaydı ve veri kümeleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) aracı kullanıma sunuldu.

## 20 Ekim 2025

- Aşağıdaki Gemini Live API modelleri kullanımdan kaldırıldı:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Bunun yerine `gemini-2.5-flash-native-audio-preview-09-2025` kullanabilirsiniz.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-2.0-flash-live-001` ve `gemini-live-2.5-flash-preview`, 9 Aralık 2025'te kullanımdan kaldırılacak.

## 17 Ekim 2025

- **Google Haritalar ile Temellendirme** artık genel kullanıma sunuldu. Daha fazla bilgi için [Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) belgelerini inceleyin.

## 15 Ekim 2025

- [Veo 3.1 ve 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=tr#veo-3.1) modellerini genel önizleme sürümünde kullanıma sunduk. Bu modellerde aşağıdaki yeni özellikler yer alıyor:

  - Veo tarafından oluşturulan videoların süresi uzatılıyor.
  - Video oluşturmak için en fazla üç resme referans verme
  - Video oluşturmak için ilk ve son kare resimlerini sağlama

  Bu lansmanla birlikte Veo 3 çıkış videosu süreleri için daha fazla seçenek (4, 6 ve 8 saniye) eklendi.
- Desteğin sonlandırılmasıyla ilgili duyuru: `veo-3.0-generate-preview` ve `veo-3.0-fast-generate-preview`, 12 Kasım 2025'te kullanımdan kaldırılacak.

## 7 Ekim 2025

- [Gemini 2.5 Computer Use Preview](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) kullanıma sunuldu.

## 2 Ekim 2025

- Gemini 2.5 Flash Image genel kullanıma sunuldu: [Gemini ile görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)

## 29 Eylül 2025

- Aşağıdaki Gemini 1.5 modelleri artık kullanımdan kaldırıldı:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 Eylül 2025

- Gemini Robotics ER 1.5 modeli önizleme sürümünde kullanıma sunuldu. Modeli robotik uygulamanızda nasıl kullanacağınızı öğrenmek için [Robotik'e genel bakış](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr) başlıklı makaleyi inceleyin.
- Aşağıdaki önizleme modelleri kullanıma sunuldu:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Ayrıntılar için [Modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasına bakın.

## 23 Eylül 2025

- Live API için geliştirilmiş işlev çağrısı ve konuşma kesintisi yönetimi özelliklerine sahip yeni bir yerel ses modeli olan `gemini-2.5-flash-native-audio-preview-09-2025` kullanıma sunuldu. Daha fazla bilgi için [Live API kılavuzuna](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-native-audio) sayfasına bakın.

## 16 Eylül 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modeller Ekim 2025'te kullanımdan kaldırılacak:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  En yeni yerleştirme modeliyle ilgili ayrıntılar için [Yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) sayfasını inceleyin.

## 10 Eylül 2025

- [Batch API'deki yerleştirme modeli](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#batch-embedding) için destek yayınlandı ve toplu sorguları kullanmaya başlamanın daha kolay yolları için Batch API, [OpenAI uyumluluk kitaplığına](https://ai.google.dev/gemini-api/docs/openai?hl=tr#batch) eklendi.

## 9 Eylül 2025

- Veo 3 ve Veo 3 Fast'in genel kullanıma sunulan sürümleri, daha düşük fiyatlar ve en boy oranları, çözünürlük ve başlangıç değeri için yeni seçeneklerle kullanıma açıldı. Daha fazla bilgi için [Veo belgelerini](https://ai.google.dev/gemini-api/docs/video?hl=tr#model-features) okuyun.

## 26 Ağustos 2025

- En yeni yerel görüntü üretme modelimiz olan [Gemini 2.5 Image Preview](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-image-preview)'u kullanıma sunduk.

## 18 Ağustos 2025

- İstemlere ek bağlam olarak URL'ler sağlamak için kullanılan [URL bağlamı aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) genel kullanıma sunuldu. `gemini-2.0-flash` modeliyle URL bağlamı kullanma desteği (deneysel sürümde kullanılabilir) bir hafta içinde sonlandırılacak.

## 14 Ağustos 2025

- Imagen 4 Ultra, Standard ve Fast modelleri genel kullanıma sunuldu. Daha fazla bilgi için [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=tr) sayfasını inceleyin.

## 7 Ağustos 2025

- `allow_adult` ayarı artık kısıtlı bölgelerde kullanılabilir. Ayrıntılar için
  [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=tr#veo-model-parameters)
  sayfasına bakın.

## 31 Temmuz 2025

- Veo 3 Preview modeli için resimden video üretme özelliği kullanıma sunuldu.
- Veo 3 Fast Preview modeli kullanıma sunuldu.
- Veo 3 hakkında daha fazla bilgi edinmek için [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) sayfasını ziyaret edin.

## 22 Temmuz 2025

- Hızlı, düşük maliyetli ve yüksek performanslı Gemini 2.5 modelimiz `gemini-2.5-flash-lite` kullanıma sunuldu. Daha fazla bilgi için [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-lite) başlıklı makaleyi inceleyin.

## Temmuz 17, 2025

- Veo'nun ses üreten model ile video üretme özelliğini sunan en yeni güncellemesi `veo-3.0-generate-preview` kullanıma sunuldu. Veo 3 hakkında daha fazla bilgi edinmek için [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) sayfasını ziyaret edin.
- Imagen 4 Standard ve Ultra için sıklık sınırlamaları artırıldı. Daha fazla bilgi için [Sıklık sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr) sayfasını ziyaret edin.

## 14 Temmuz 2025

- Metin yerleştirme modelimizin kararlı sürümü olan `gemini-embedding-001` kullanıma sunuldu. Daha fazla bilgi edinmek için [yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) bölümüne bakın. `gemini-embedding-exp-03-07` modeli 14 Ağustos 2025'te kullanımdan kaldırılacak.

## 7 Temmuz 2025

- Gemini API Toplu Modu kullanıma sunuldu. İstekleri toplu olarak gruplandırıp eşzamansız olarak işlenmek üzere gönderme Daha fazla bilgi edinmek için [Toplu İşlem Modu](https://ai.google.dev/gemini-api/docs/batch-mode?hl=tr)'nu inceleyin.

## 26 Haziran 2025

- `gemini-2.5-pro-preview-05-06` ve `gemini-2.5-pro-preview-03-25` önizleme modelleri artık en yeni kararlı sürüm olan `gemini-2.5-pro` modeline yönlendiriliyor.
- `gemini-2.5-pro-exp-03-25` kapatıldı.

## 24 Haziran 2025

- Imagen 4 Ultra ve Standard Preview modelleri yayınlandı. Daha fazla bilgi edinmek için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) sayfasını inceleyin.

## 17 Haziran 2025

- En güçlü modelimizin kararlı sürümü olan `gemini-2.5-pro`'yı kullanıma sunduk. Bu model artık uyarlanabilir düşünme özelliğine sahip. Daha fazla bilgi edinmek için [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro) ve [Düşünen](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin. `gemini-2.5-pro-preview-05-06`,
  26 Haziran 2025'te `gemini-2.5-pro` adresine yönlendirilecek.
- İlk kararlı 2.5 Flash modelimiz olan `gemini-2.5-flash` yayınlandı. Daha fazla bilgi için [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash) başlıklı makaleyi inceleyin.
  `gemini-2.5-flash-preview-04-17`, 15 Temmuz 2025'te kullanımdan kaldırılacak.
- Düşük maliyetli ve yüksek performanslı Gemini 2.5 modeli `gemini-2.5-flash-lite-preview-06-17` kullanıma sunuldu. Daha fazla bilgi için [Gemini 2.5 Flash-Lite Preview](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-lite) başlıklı makaleyi inceleyin.

## 5 Haziran 2025

- En güçlü modelimizin uyarlanabilir düşünme özelliğine sahip yeni sürümü `gemini-2.5-pro-preview-06-05`'yı kullanıma sunduk. Daha fazla bilgi edinmek için [Gemini 2.5 Pro Preview](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-06-05) ve [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin.
  `gemini-2.5-pro-preview-05-06`, 26 Haziran 2025'te `gemini-2.5-pro` adresine yönlendirilecek.

## 27 Mayıs 2025

- Kullanılabilen son ince ayar modeli olan Gemini 1.5 Flash 001 kapatıldı.
  İnce ayar artık hiçbir modelde desteklenmiyor.
  [Gemini API ile ince ayar yapma](https://ai.google.dev/gemini-api/docs/model-tuning?hl=tr) başlıklı makaleyi inceleyin.

## 20 Mayıs 2025

**API güncellemeleri:**

- Kırpma aralıkları ve yapılandırılabilir kare hızı örneklemesi kullanılarak [özel video ön işleme](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#customize-video-processing) desteği kullanıma sunuldu.
- Aynı `generateContent` isteğinde [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/grounding?hl=tr)'yi yapılandırmayı destekleyen çoklu araç kullanımı kullanıma sunuldu.
- Live API'de [eşzamansız işlev çağrıları](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr#async-function-calling) için destek kullanıma sunuldu.
- İstemlere ek bağlam olarak URL sağlamak için deneysel bir [URL bağlamı aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) kullanıma sunuldu.

**Model güncellemeleri:**

- Fiyat-performans ve uyarlanabilir düşünme için optimize edilmiş bir Gemini [önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#model-versions) modeli olan `gemini-2.5-flash-preview-05-20` kullanıma sunuldu. Daha fazla bilgi edinmek için [Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview) ve [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin.
- Bir veya iki konuşmacıyla [konuşma üretebilen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-tts) ve [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview-tts) modelleri kullanıma sunuldu.
- Anında [müzik üreten](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) `lyria-realtime-exp` modelini kullanıma sunduk.
- Yerel ses çıkışı özelliklerine sahip yeni Gemini modelleri olan `gemini-2.5-flash-preview-native-audio-dialog` ve `gemini-2.5-flash-exp-native-audio-thinking-dialog`, Live API için kullanıma sunuldu. Daha fazla bilgi için [Live API kılavuzuna](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#native-audio-output) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-native-audio) sayfasına bakın.
- [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=tr) lansmanı kapsamında `gemma-3n-e4b-it` önizlemesi yayınlandı. Bu önizlemeye [AI Studio](https://aistudio.google.com?hl=tr)'dan ve Gemini API üzerinden erişebilirsiniz.

## 7 Mayıs 2025

- Görüntü üretme ve düzenleme için önizleme modeli olan `gemini-2.0-flash-preview-image-generation` kullanıma sunuldu. Daha fazla bilgi için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) ve [Gemini 2.0 Flash Preview Görüntü Üretme](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.0-flash-preview-image-generation) başlıklı makaleleri inceleyin.

## 6 Mayıs 2025

- En güçlü modelimizin yeni sürümü olan `gemini-2.5-pro-preview-05-06`, kod ve işlev çağrısı iyileştirmeleriyle kullanıma sunuldu. `gemini-2.5-pro-preview-03-25`
  otomatik olarak modelin yeni sürümüne yönlendirir.

## 17 Nisan 2025

- Fiyat-performans ve uyarlanabilir düşünme için optimize edilmiş bir Gemini [önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#model-versions) modeli olan `gemini-2.5-flash-preview-04-17` kullanıma sunuldu. Daha fazla bilgi edinmek için [Gemini 2.5 Flash Preview](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview) ve [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin.

## 16 Nisan 2025

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.0-flash) için bağlam önbelleğe alma özelliği kullanıma sunuldu.

## 9 Nisan 2025

**Model güncellemeleri:**

- Ayrıntılı ve sanatsal açıdan incelikli videolar oluşturabilen, genel kullanıma sunulan (GA) metinden ve görüntüden videoya dönüştürme modeli `veo-2.0-generate-001` kullanıma sunuldu. Daha fazla bilgi için [Veo belgelerine](https://ai.google.dev/gemini-api/docs/video?hl=tr) bakın.
- Faturalandırmanın etkin olduğu [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) modelinin genel önizleme sürümü olan `gemini-2.0-flash-live-001` kullanıma sunuldu.

  - **Gelişmiş oturum yönetimi ve güvenilirlik**

    - **Oturum devam ettirme:** Geçici ağ kesintileri sırasında oturumları etkin tutun. API artık sunucu tarafı oturum durumu depolama alanını (24 saate kadar) destekliyor ve yeniden bağlanıp kaldığınız yerden devam etmeniz için tutamaçlar (session\_resumption) sağlıyor.
    - **Bağlam sıkıştırma ile daha uzun oturumlar:** Önceki zaman sınırlarını aşan daha uzun etkileşimleri etkinleştirin. Bağlam uzunluğunu otomatik olarak yönetmek ve bağlam sınırları nedeniyle ani sonlandırmaları önlemek için kayan pencere mekanizmasıyla bağlam penceresi sıkıştırmasını yapılandırın.
    - **Sorunsuz Bağlantı Kesme Bildirimi:** Bir bağlantının ne zaman kapanacağını belirten bir `GoAway` sunucu mesajı alarak bağlantı sonlandırılmadan önce sorunsuz bir şekilde işlem yapabilirsiniz.
  - **Etkileşim dinamikleri üzerinde daha fazla kontrol**
  - **Yapılandırılabilir Ses Etkinliği Algılama (VAD):** Hassasiyet seviyelerini seçin veya otomatik VAD'yi tamamen devre dışı bırakın ve manuel sıra kontrolü için yeni istemci etkinliklerini (`activityStart`, `activityEnd`) kullanın.
  - **Yapılandırılabilir kesinti yönetimi:** Kullanıcı girişinin modelin yanıtını kesintiye uğratıp uğratmayacağına karar verin.
  - **Yapılandırılabilir Sıra Kapsamı:** API'nin tüm ses ve video girişlerini sürekli olarak mı işleyeceğini yoksa yalnızca son kullanıcının konuştuğu algılandığında mı yakalayacağını seçin.
  - **Yapılandırılabilir medya çözünürlüğü:** Giriş medyasının çözünürlüğünü seçerek kaliteyi veya jeton kullanımını optimize edin.
  - **Daha zengin çıkış ve özellikler**
  - **Genişletilmiş Ses ve Dil Seçenekleri:** Ses çıkışı için iki yeni ses ve 30 yeni dil arasından seçim yapabilirsiniz. Çıkış dili artık `speechConfig` üzerinden yapılandırılabilir.
  - **Metin akışı:** Metin yanıtlarını oluşturuldukça parça parça alarak kullanıcıya daha hızlı gösterilmesini sağlayın.
  - **Jeton kullanımı raporlama:** Sunucu mesajlarının `usageMetadata` alanında, modaliteye ve istem ya da yanıt aşamalarına göre ayrılmış ayrıntılı jeton sayılarıyla kullanım hakkında bilgi edinin.

## 4 Nisan 2025

- Faturalandırmanın etkin olduğu, genel önizleme Gemini 2.5 Pro sürümü olan `gemini-2.5-pro-preview-03-25` kullanıma sunuldu. `gemini-2.5-pro-exp-03-25` ürününü ücretsiz katmanda kullanmaya devam edebilirsiniz.

## 25 Mart 2025

- Düşünebilen modun varsayılan olarak her zaman açık olduğu, herkese açık deneysel Gemini modeli `gemini-2.5-pro-exp-03-25` kullanıma sunuldu.
  Daha fazla bilgi için [Gemini 2.5 Pro Experimental](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-03-25) başlıklı makaleyi inceleyin.

## 12 Mart 2025

**Model güncellemeleri:**

- Görüntü üretme ve düzenleme özelliklerine sahip deneysel bir [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#gemini) modeli kullanıma sunuldu.
- [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=tr) lansmanı kapsamında `gemma-3-27b-it` tarihinde kullanıma sunulan bu model, [AI Studio](https://aistudio.google.com?hl=tr)'da ve Gemini API üzerinden kullanılabilir.

**API güncellemeleri:**

- Medya kaynağı olarak [YouTube URL'leri](https://ai.google.dev/gemini-api/docs/vision?hl=tr#youtube) için destek eklendi.
- 20 MB'tan küçük [satır içi video](https://ai.google.dev/gemini-api/docs/vision?hl=tr#inline-video) ekleme desteği eklendi.

## 11 Mart 2025

**SDK güncellemeleri:**

- [TypeScript ve JavaScript için Google Üretken Yapay Zeka SDK](https://googleapis.github.io/js-genai)'sının genel önizleme sürümü yayınlandı.

## 7 Mart 2025

**Model güncellemeleri:**

- Genel önizleme sürümünde Gemini tabanlı [deneysel](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr) bir yerleştirme modeli olan `gemini-embedding-exp-03-07` kullanıma sunuldu.

## 28 Şubat 2025

**API güncellemeleri:**

- Gemini 2.0 Pro'yu temel alan deneysel bir model olan `gemini-2.0-pro-exp-02-05`'e [araç olarak Arama](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) desteği eklendi.

## 25 Şubat 2025

**Model güncellemeleri:**

- Hız, ölçek ve maliyet verimliliği için optimize edilmiş [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash-lite)'ın genel kullanıma sunulan (GA) sürümü olan `gemini-2.0-flash-lite` yayınlandı.

## 19 Şubat 2025

**AI Studio güncellemeleri:**

- [Ek bölgeler](https://ai.google.dev/gemini-api/docs/available-regions?hl=tr) (Kosova, Grönland ve Faroe Adaları) için destek.

**API güncellemeleri:**

- [Ek bölgeler](https://ai.google.dev/gemini-api/docs/available-regions?hl=tr) (Kosova, Grönland ve Faroe Adaları) için destek.

## 18 Şubat 2025

**Model güncellemeleri:**

- Gemini 1.0 Pro artık desteklenmiyor. Desteklenen modellerin listesi için [Gemini modelleri](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) başlıklı makaleyi inceleyin.

## 11 Şubat 2025

**API güncellemeleri:**

- [OpenAI kitaplıkları uyumluluğu](https://ai.google.dev/gemini-api/docs/openai?hl=tr) ile ilgili güncellemeler.

## 6 Şubat 2025

**Model güncellemeleri:**

- [Gemini API'de Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=tr)'ün genel kullanıma sunulan (GA) sürümü olan `imagen-3.0-generate-002` kullanıma sunuldu.

**SDK güncellemeleri:**

- [Java için Google Üretken Yapay Zeka SDK](https://github.com/googleapis/java-genai)'nın genel önizleme sürümü yayınlandı.

## 5 Şubat 2025

**Model güncellemeleri:**

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash)'in yalnızca metin çıkışını destekleyen, genel kullanıma sunulmuş (GA) sürümü olan `gemini-2.0-flash-001` kullanıma sunuldu.
- Gemini 2.0 Pro'nun [deneysel](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr)
  genel önizleme sürümü olan `gemini-2.0-pro-exp-02-05` kullanıma sunuldu.
- Maliyet verimliliği için optimize edilmiş, deneysel bir genel önizleme [modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash-lite) olan `gemini-2.0-flash-lite-preview-02-05` kullanıma sunuldu.

**API güncellemeleri:**

- Kod yürütme özelliğine [dosya girişi ve grafik çıkışı](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#input-output) desteği eklendi.

**SDK güncellemeleri:**

- [Python için Google Gen AI SDK](https://googleapis.github.io/python-genai/)'yı genel kullanıma sunduk.

## 21 Ocak 2025

**Model güncellemeleri:**

- [Gemini 2.0 Hızlı Düşünen Modeli'nin](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) arkasındaki modelin en yeni önizleme sürümü olan `gemini-2.0-flash-thinking-exp-01-21` kullanıma sunuldu.

## 19 Aralık 2024

**Model güncellemeleri:**

- Gemini 2.0 Hızlı Düşünen Modu, genel önizleme için kullanıma sunuldu. Düşünen Mod, modelin yanıt üretirken düşünme sürecini görmenizi sağlayan ve daha güçlü akıl yürütme özellikleriyle yanıtlar üreten bir test zamanı hesaplama modelidir.

  Gemini 2.0 Flash Hızlı Düşünen Modu hakkında daha fazla bilgiyi [genel bakış sayfamızda](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=tr) bulabilirsiniz.

## 11 Aralık 2024

**Model güncellemeleri:**

- [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash), genel önizleme için kullanıma sunuldu. Gemini 2.0 Flash Experimental'ın özelliklerinin bir kısmı şunlardır:
  - Gemini 1.5 Pro'dan iki kat daha hızlı
  - Live API ile çift yönlü akış
  - Metin, resim ve konuşma biçiminde çok formatlı yanıt üretimi
  - Kod yürütme, Arama, işlev çağrısı ve daha fazlası gibi özellikleri kullanmak için çok adımlı akıl yürütme ile yerleşik araç kullanımı

Gemini 2.0 Flash hakkında daha fazla bilgiyi [genel bakış sayfamızda](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=tr) bulabilirsiniz.

## 21 Kasım 2024

**Model güncellemeleri:**

- Daha da güçlü bir deneysel Gemini API modeli olan `gemini-exp-1121` kullanıma sunuldu.

**Model güncellemeleri:**

- `gemini-1.5-flash-latest` ve `gemini-1.5-flash` model takma adları, `gemini-1.5-flash-002` kullanacak şekilde güncellendi.
  - `top_k` parametresini değiştirin: `gemini-1.5-flash-002` modeli, 1 ile 41 (hariç) arasındaki `top_k` değerlerini destekler.
    40'tan büyük değerler 40 olarak değiştirilir.

## 14 Kasım 2024

**Model güncellemeleri:**

- Güçlü ve deneysel bir Gemini API modeli olan `gemini-exp-1114` kullanıma sunuldu.

## 8 Kasım 2024

**API güncellemeleri:**

- OpenAI kitaplıklarında/REST API'de [Gemini desteği](https://ai.google.dev/gemini-api/docs/openai?hl=tr) eklendi.

## 31 Ekim 2024

**API güncellemeleri:**

- [Google Arama ile Temellendirme desteği](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) eklendi.

## 3 Ekim 2024

**Model güncellemeleri:**

- En küçük Gemini API modelimizin kararlı sürümü olan `gemini-1.5-flash-8b-001` kullanıma sunuldu.

## 24 Eylül 2024

**Model güncellemeleri:**

- Gemini 1.5 Pro ve 1.5 Flash'ın iki yeni kararlı sürümü olan `gemini-1.5-pro-002` ve `gemini-1.5-flash-002` genel kullanıma sunuldu.
- `gemini-1.5-pro-latest` model kodu `gemini-1.5-pro-002`, `gemini-1.5-flash-latest` model kodu ise `gemini-1.5-flash-002` kullanacak şekilde güncellendi.
- `gemini-1.5-flash-8b-exp-0827` yerine `gemini-1.5-flash-8b-exp-0924` yayınlandı.
- Gemini API ve AI Studio için [sivil bütünlük güvenlik filtresi](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr#safety-filters) kullanıma sunuldu.
- Python ve NodeJS'de Gemini 1.5 Pro ve 1.5 Flash için iki yeni parametre desteği yayınlandı:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=tr#FIELDS.frequency_penalty) ve
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=tr#FIELDS.presence_penalty).

## 19 Eylül 2024

**AI Studio güncellemeleri:**

- Kullanıcıların yanıtların kalitesiyle ilgili geri bildirim gönderebilmesi için model yanıtlarına beğenme ve beğenmeme düğmeleri eklendi.

**API güncellemeleri:**

- Artık Gemini API kullanımı için kullanılabilen Google Cloud kredileri için destek eklendi.

## 17 Eylül 2024

**AI Studio güncellemeleri:**

- İstemi ve çalıştırma kodunu Colab not defterine aktaran **Colab'de aç** düğmesi eklendi. Bu özellik henüz araçlarla (JSON modu, işlev çağrısı veya kod yürütme) istem oluşturmayı desteklemiyor.

## 13 Eylül 2024

**AI Studio güncellemeleri:**

- Karşılaştırma modu desteği eklendi. Bu mod, kullanım alanınıza en uygun modeli bulmak için modeller ve istemler genelinde yanıtları karşılaştırmanıza olanak tanır.

## 30 Ağustos 2024

**Model güncellemeleri:**

- Gemini 1.5 Flash, [model yapılandırması aracılığıyla JSON şeması sağlamayı](https://ai.google.dev/gemini-api/docs/json-mode?hl=tr#supply-schema-in-config) destekler.

## 27 Ağustos 2024

**Model güncellemeleri:**

- Aşağıdaki [deneysel modeller](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr) kullanıma sunuldu:
  - `gemini-1.5-pro-exp-0827`
  - `gemini-1.5-flash-exp-0827`
  - `gemini-1.5-flash-8b-exp-0827`

## 9 Ağustos 2024

**API güncellemeleri:**

- [PDF işleme](https://ai.google.dev/gemini-api/docs/document-processing?hl=tr) desteği eklendi.

## 5 Ağustos 2024

**Model güncellemeleri:**

- Gemini 1.5 Flash için ince ayar desteği kullanıma sunuldu.

## 1 Ağustos 2024

**Model güncellemeleri:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro)'nun yeni bir deneme sürümü olan `gemini-1.5-pro-exp-0801` kullanıma sunuldu.

## 12 Temmuz 2024

**Model güncellemeleri:**

- Google AI hizmetleri ve araçlarından Gemini 1.0 Pro Vision desteği kaldırıldı.

## 27 Haziran 2024

**Model güncellemeleri:**

- Gemini 1.5 Pro'nun 2 milyon parçalık bağlam penceresi genel kullanıma sunuldu.

**API güncellemeleri:**

- [Kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) için destek eklendi.

## 18 Haziran 2024

**API güncellemeleri:**

- [Bağlam önbelleğe alma](https://ai.google.dev/gemini-api/docs/caching?hl=tr) için destek eklendi.

## 12 Haziran 2024

**Model güncellemeleri:**

- Gemini 1.0 Pro Vision kullanımdan kaldırıldı.

## 23 Mayıs 2024

**Model güncellemeleri:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) genel kullanıma sunuldu.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) genel kullanıma sunuldu.

## 14 Mayıs 2024

**API güncellemeleri:**

- Gemini 1.5 Pro için 2 milyon parçalık bağlam penceresi kullanıma sunuldu (bekleme listesi).
- Gemini 1.0 Pro için kullandıkça öde [faturalandırması](https://ai.google.dev/gemini-api/docs/billing?hl=tr) kullanıma sunuldu. Gemini 1.5 Pro ve Gemini 1.5 Flash faturalandırması yakında kullanıma sunulacak.
- Gemini 1.5 Pro'nun yakında kullanıma sunulacak ücretli katmanı için daha yüksek kullanım sınırları getirildi.
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr)'ye yerleşik video desteği eklendi.
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr)'ye düz metin desteği eklendi.
- Aynı anda birden fazla çağrı döndüren paralel fonksiyon çağırma desteği eklendi.

## 10 Mayıs 2024

**Model güncellemeleri:**

- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-flash) (`gemini-1.5-flash-latest`) önizleme sürümü kullanıma sunuldu.

## 9 Nisan 2024

**Model güncellemeleri:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro) (`gemini-1.5-pro-latest`) önizleme sürümü kullanıma sunuldu.
- 768'in altındaki [esnek yerleştirme](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr#elastic-embedding) boyutlarını destekleyen yeni bir metin yerleştirme modeli (`text-embeddings-004`) kullanıma sunuldu.

**API güncellemeleri:**

- İstemlerde kullanılacak medya dosyalarını geçici olarak depolamak için [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr) kullanıma sunuldu.
- *Çok formatlı* istem olarak da bilinen metin, resim ve ses verileriyle istem oluşturma desteği eklendi. Daha fazla bilgi edinmek için [Medyayla istem oluşturma](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=tr) başlıklı makaleyi inceleyin.
- [Sistem talimatları](https://ai.google.dev/gemini-api/docs/system-instructions?hl=tr) beta sürümünde kullanıma sunuldu.
- İşlev çağrısının yürütme davranışını tanımlayan [işlev çağrısı modu](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#function_calling_mode) eklendi.
- [JSON biçiminde](https://ai.google.dev/gemini-api/docs/api-overview?hl=tr#json) yanıt istemenize olanak tanıyan `response_mime_type` yapılandırma seçeneği için destek eklendi.

## 19 Mart 2024

**Model güncellemeleri:**

- Google AI Studio'da veya Gemini API ile [Gemini 1.0 Pro'yu ayarlama](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) desteği eklendi.

## 13 Aralık 2023

**Model güncellemeleri:**

- gemini-pro: Çok çeşitli görevler için yeni metin modeli. Yetenek ve verimlilik arasında denge kurar.
- gemini-pro-vision: Çok çeşitli görevler için yeni çok formatlı model.
  Yetenek ve verimlilik arasında denge kurar.
- embedding-001: Yeni yerleştirme modeli.
- aqa: Oluşturulan yanıtları temellendirmek için metin pasajlarını kullanarak soruları yanıtlamak üzere eğitilmiş, özel olarak ayarlanmış yeni bir model.

Daha fazla bilgi için [Gemini modelleri](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) başlıklı makaleyi inceleyin.

**API sürümü güncellemeleri:**

- v1: Kararlı API kanalı.
- v1beta: Beta kanalı. Bu kanalda geliştirme aşamasında olabilecek özellikler var.

Daha fazla bilgi için [API sürümleri konusuna](https://ai.google.dev/gemini-api/docs/api-versions?hl=tr) bakın.

**API güncellemeleri:**

- `GenerateContent`, sohbet ve metin için tek bir birleştirilmiş uç noktadır.
- `StreamGenerateContent` yöntemiyle akış yapılabilir.
- Çok formatlı özellik: Resim, desteklenen yeni bir modalitedir.
- Yeni beta özellikleri:
  - [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
  - Attributed Question Answering (AQA)
- Güncellenen aday sayısı: Gemini modelleri yalnızca 1 aday döndürür.
- Farklı SafetySettings ve SafetyRating kategorileri. Daha fazla bilgi için [güvenlik ayarlarına](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) göz atın.
- Modelleri ayarlama özelliği, Gemini modellerinde henüz desteklenmemektedir (çalışmalar devam etmektedir).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-30 UTC."],[],[]]
