---
source_url: https://ai.google.dev/gemini-api/docs/changelog?hl=tr
fetched_at: 2026-08-17T02:35:34.203317+00:00
title: "S\u00fcr\u00fcm notlar\u0131 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Sürüm notları

Bu sayfada, Gemini API'deki güncellemeler belgelenmektedir.

## 21 Temmuz 2026

- **Gemini 3.6 Flash ve Gemini 3.5 Flash-Lite'ın genel kullanıma sunulması**:
  En yeni 3.x Flash modellerimizin kararlı ve üretime hazır sürümleri yayınlandı:

  - **Gemini 3.6 Flash** (`gemini-3.6-flash`): 3.5 Flash'e kıyasla daha düşük bir fiyatla daha iyi jeton verimliliği ve kod/aracı planlama özellikleri sunar. Ayrıca, geliştiricilerin çıkış ayrıntılarıyla ilgili geri bildirimlerini de dikkate alır.
  - **Gemini 3.5 Flash-Lite** (`gemini-3.5-flash-lite`): Yüksek hacimli otomasyon için tasarlanmış, düşük gecikmeli ve son derece uygun maliyetli bir alt aracı seçeneği sunar.

  Daha fazla bilgi için [En yeni Gemini modeli](https://ai.google.dev/gemini-api/docs/latest-model?hl=tr) kılavuzuna bakın.
- **Desteği sonlandırılan parametreler**: `temperature`, `top_p` ve `top_k` örnekleme parametrelerinin desteği sonlandırıldı. Ayrıntılı bilgi için [En Yeni Gemini Modeli](https://ai.google.dev/gemini-api/docs/latest-model?hl=tr#sampling-parameter-deprecation) başlıklı makaleyi inceleyin.

## 6 Temmuz 2026

- Etkileşimler API'si için [geliştirici günlükleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) desteği: Desteklenen Interactions API çağrılarına ait günlükler artık [AI Studio kontrol panelinde](https://aistudio.google.com/logs?hl=tr) görüntülenebilir.

## 30 Haziran 2026

- **Herkese açık önizleme sürümündeki Gemini Omni Flash**: `gemini-omni-flash-preview` tarihinde yayınlandı.
  Bu model, yüksek hızlı video üretimi ve sohbet tarzında video düzenleme için tasarlanmış yüksek performanslı bir çok formatlı modeldir. [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr)'yi kullanarak metin açıklamalarından 720p çözünürlükte 3-10 saniyelik videolar oluşturabilir veya hareketsiz görüntüleri canlandırabilirsiniz. Ardından, çıktıları sohbet ederek düzenleyip iyileştirebilirsiniz. Başlamak için [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/omni?hl=tr) kılavuzuna ve [Gemini Omni Flash](https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash?hl=tr) model kartına göz atın.
- Ultra düşük gecikme süresi ve uygun maliyetli görüntü üretme ve düzenleme için optimize edilmiş yerleşik çok formatlı modelimiz `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) genel kullanıma sunuldu. [Gemini 3.1
  Flash Lite Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image?hl=tr) model
  kartını ve [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) kılavuzunu inceleyin.

## 24 Haziran 2026

- **Bilgisayar Kullanımı**: Gemini 3.5 Flash'teki [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) aracı için herkese açık önizleme desteği kullanıma sunuldu. Bu sürümde; amaçlarla basitleştirilmiş işlemler, tarayıcı, mobil ve masaüstü ortamları için yerleşik destek, yapılandırılabilir güvenlik politikaları ve gelişmiş istem enjeksiyonu algılama özellikleri yer alıyor.

## 17 Haziran 2026

- **Konuşma üretimi için akış desteği**: `streamGenerateContent` (ve Interactions API'deki `stream: true`) üzerinden akış artık `gemini-3.1-flash-tts-preview` modeli için destekleniyor. Daha fazla bilgi edinmek için [Metin Okuma](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr#streaming) kılavuzuna bakın.

## 15 Haziran 2026

- **Desteğin sonlandırılmasıyla ilgili duyuru**: Aşağıdaki resim oluşturma modellerinin desteği sonlandırılıyor ve bu modeller **17 Ağustos 2026**'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - **Imagen 4 ve Gemini 3 Image modelleri**:

    - `imagen-4.0-generate-001`
    - `imagen-4.0-ultra-generate-001`
    - `imagen-4.0-fast-generate-001`

    Kodunuzu daha yeni kararlı veya önizleme uç noktalarına taşımak için [Gemini desteğinin sonlandırılması](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr#imagen-models) sayfasına bakın.
- **Desteğin sonlandırılması duyurusu**: Aşağıdaki video üretim modellerinin desteği sonlandırılıyor ve bu modeller **30 Haziran 2026**'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - **Veo modelleri**:

    - `veo-2.0-generate-001`
    - `veo-3.0-generate-001`
    - `veo-3.0-fast-generate-001`

    Hizmet kesintilerini önlemek için entegrasyonunuzu, Veo 3.1 önizleme modeli kimliklerini (`veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`) veya [Gemini Enterprise Agent Platformu](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=tr) üzerinden kullanılabilen 3.1 GA modellerini kullanacak şekilde güncelleyin.
- **Desteği sonlandırma duyurusu**: Deneysel GMP Bağlamsal Görünüm aracı (Google Haritalar ile Temellendirme için sabit bir arayüz) [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). Kapatılma tarihi: **15 Haziran 2026**.

## 1 Haziran 2026

- Aşağıdaki Gemini 2.0 modelleri artık [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

  Bunun yerine [`gemini-3.5-flash`](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr) veya
  [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) kullanın.

## 28 Mayıs 2026

- Yerel görsel modellerimiz olan [Gemini 3.1 Flash Image](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image?hl=tr) ve [Gemini 3 Pro Image](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image?hl=tr)'in genel kullanıma açık (GA) sürümleri `gemini-3.1-flash-image` (Nano Banana 2) ve `gemini-3-pro-image` (Nano Banana Pro) yayınlandı.
- **Video-resim üretme desteği**: Artık yüksek kaliteli küçük resimler, sinematik film posterleri veya özet infografikler oluşturmak için bir metin istemiyle birlikte çok formatlı bağlam olarak bir video dosyası (doğrudan yükleme yoluyla veya herkese açık bir YouTube URL'si olarak) iletebilirsiniz. Bu özellik yalnızca `gemini-3.1-flash-image` modelinde desteklenir. Daha fazla bilgi edinmek için [Video-görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#video-to-image) kılavuzuna bakın.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-3.1-flash-image-preview` ve
  `gemini-3-pro-image-preview` modellerinin desteği sonlandırıldı ve 25 Haziran 2026'da [kullanımdan kaldırılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 25 Mayıs 2026

- `gemini-3.1-flash-lite-preview` modeli [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). Bunun yerine [`gemini-3.1-flash-lite`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr) kullanın.

## 19 Mayıs 2026

- `gemini-3.5-flash` tarihinde, [Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash?hl=tr)'ın genel kullanıma sunulan (GA) sürümü yayınlandı. Bu model, temsilci ve kodlama görevlerinde sürekli olarak en üst düzey performans sunan en akıllı modelimizdir. Bu model artık `gemini-flash-latest`'ın temelini oluşturuyor.
- **Gemini API'de Yönetilen Ajanlar**'ı genel önizleme sürümünde kullanıma sundu. Bu sayede geliştiriciler, güvenli ve yalıtılmış Google tarafından barındırılan Linux sandbox ortamlarında çalışan bağımsız ve durum bilgisi olan aracıları oluşturup dağıtabilir. Daha fazla bilgi edinmek için [Aracıya genel bakış](https://ai.google.dev/gemini-api/docs/agents?hl=tr) sayfasını ve [Hızlı Başlangıç](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=tr) kılavuzunu inceleyin.
- Genel amaçlı **Antigravity Agent** adlı yönetilen aracı,
  [`antigravity-preview-05-2026`](https://ai.google.dev/gemini-api/docs/models/antigravity-preview-05-2026?hl=tr), genel önizlemeye sunduk.
  Antigravity ajanı, sandbox kapsayıcısında bağımsız olarak planlama yapabilir, akıl yürütebilir, kod yazıp yürütebilir, dosyaları yönetebilir ve web'de gezinebilir. Kod örnekleri ve spesifikasyonlar için [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=tr) kılavuzuna bakın.

## 7 Mayıs 2026

- Hız, ölçek ve maliyet verimliliği için optimize edilmiş [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=tr)'ın genel kullanıma sunulan (GA) sürümü `gemini-3.1-flash-lite` tarihinde yayınlandı.
- Kullanımdan kaldırma duyurusu: `gemini-3.1-flash-lite-preview` modeli 11.05.2026'da kullanımdan kaldırılacak ve 25 Mayıs 2026'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 6 Mayıs 2026

- **Yaklaşan önemli değişiklik**: [Etkileşimler API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) istek ve yanıt şeması (`outputs` → `steps`) ve çıkış biçimi yapılandırması (`response_format`) değişiyor. Yeni şema, **26 Mayıs**'ta varsayılan şema olacak ve eski şema **8 Haziran**'da kaldırılacak.
  Ayrıntılar için [taşıma kılavuzuna](https://ai.google.dev/gemini-api/docs/interactions-breaking-changes-may-2026?hl=tr) bakın.

## 5 Mayıs 2026

- Çok formatlı aramayı desteklemek için **Dosya Arama** güncellendi. Artık `gemini-embedding-2` modelini kullanarak resimleri yerel olarak yerleştirebilir ve arayabilirsiniz.
  Temellendirme meta verileri artık görsel alıntılar için `media_id` ve bilgilerin nerede bulunduğunu gösteren `page_numbers` içeriyor. Daha fazla bilgi için [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) kılavuzuna bakın.

## 4 Mayıs 2026

- Toplu API ve uzun süren işlemler için yoklama iş akışlarının yerini alacak şekilde Gemini API'de etkinlik temelli [Web kancası](https://ai.google.dev/gemini-api/docs/webhooks?hl=tr) desteği kullanıma sunuldu.

## 30 Nisan 2026

- `gemini-robotics-er-1.5-preview` modeli [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). Bunun yerine [`gemini-robotics-er-1.6-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-robotics-er-1.6-preview?hl=tr) kullanın.

## 22 Nisan 2026

- `gemini-embedding-2` genel kullanıma sunuldu (GA). Daha fazla bilgi için [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) (Yerleştirmeler) sayfasını inceleyin.

## 21 Nisan 2026

- Ortak planlama, görselleştirme desteği, MCP sunucusu entegrasyonu ve Dosya Arama özelliklerini içeren [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) aracının yeni sürümleri yayınlandı:

  - [`deep-research-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-preview-04-2026?hl=tr): Hız ve verimlilik için tasarlanmıştır. İstemci kullanıcı arayüzüne geri aktarılmak için idealdir.
  - [`deep-research-max-preview-04-2026`](https://ai.google.dev/gemini-api/docs/models/deep-research-max-preview-04-2026?hl=tr): Otomatik bağlam toplama ve sentezleme için maksimum kapsam.

## 15 Nisan 2026

- Uygun maliyetli, etkileyici ve yönlendirilebilir metin okuma modelimiz [Gemini 3.1 Flash TTS Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview?hl=tr)'u kullanıma sunduk. Daha fazla bilgi edinmek için [Metin Okuma](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) belgelerini inceleyin.

## 14 Nisan 2026

- Güncellenmiş robotik modelimiz `gemini-robotics-er-1.6-preview` yayınlandı.
  Artık enstrüman okuma, gelişmiş mekansal ve fiziksel muhakeme yetenekleri gibi yeni özelliklere sahip. Daha fazla bilgi için [Gemini Robotics-ER](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr) sayfasını ve [blogu](https://deepmind.google/blog/gemini-robotics-er-1-6?hl=tr) inceleyin.
- Kullanımdan kaldırma duyurusu: `gemini-robotics-er-1.5-preview` modeli, 30 Nisan 2026'da saat 19:00 (TSİ) itibarıyla [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 2 Nisan 2026

- `gemma-4-26b-a4b-it` ve `gemma-4-31b-it`, [Gemma 4](https://ai.google.dev/gemma/docs/core?hl=tr)'ün kullanıma sunulması kapsamında [AI Studio](https://aistudio.google.com?hl=tr)'da ve Gemini API üzerinden kullanıma sunuldu.

## 1 Nisan 2026

- Maliyet veya süreyi optimize etmek için daha fazla seçenek sunan yeni [Flex](https://ai.google.dev/gemini-api/docs/flex-inference?hl=tr) ve [Priority](https://ai.google.dev/gemini-api/docs/priority-inference?hl=tr) çıkarım katmanları kullanıma sunuldu.

## 31 Mart 2026

- En uygun maliyetli [video üretme](https://ai.google.dev/gemini-api/docs/video?hl=tr) modelimiz olan Veo 3.1 Lite Önizleme [`veo-3.1-lite-generate-preview`](https://ai.google.dev/gemini-api/docs/models/veo-3.1-lite-generate-preview?hl=tr)'yi kullanıma sunduk. Bu model, hızlı yineleme ve yüksek hacimli uygulamalar oluşturmak için tasarlandı.
- `gemini-2.5-flash-lite-preview-09-2025` modeli kapatıldı. Bunun yerine [`gemini-3.1-flash-lite-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) kullanın.

## 26 Mart 2026

- [`gemini-3.1-flash-live-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview?hl=tr), anında diyalog ve ses odaklı yapay zeka uygulamaları için tasarlanmış en yeni ses-ses (A2A) modeli olarak kullanıma sunuldu. Başlamak için [Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=tr) belgelerini okuyun.

## 25 Mart 2026

- [Lyria 3](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) müzik üretme modellerini kullanıma sunduk: [`lyria-3-clip-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview?hl=tr)
  (30 saniyelik klipler) ve [`lyria-3-pro-preview`](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview?hl=tr)
  (tam uzunlukta şarkılar). Her iki model de metin ve resim girişlerini kabul eder ve yüksek kaliteli, 48 kHz stereo ses üretir. Ayrıntılar ve kod örnekleri için [Müzik üretimi](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) kılavuzuna bakın.

## 23 Mart 2026

- AI Studio'da [ön ödemeli ve sonradan ödemeli faturalandırma planları](https://ai.google.dev/gemini-api/docs/billing?hl=tr) kullanıma sunuldu. Mevcut hesaplar etkilenebilir. Daha fazla bilgi için [Faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) belgelerini inceleyin.

## 18 Mart 2026

- Yeni [Yerleşik Araçlar ve İşlev Çağırma Kombinasyonu](https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr) özelliğini kullanıma sunduk. Bu özellik sayesinde, Gemini'ın yerleşik araçları ile özel işlev çağırma araçları tek bir API çağrısında kullanılabiliyor.
- [Google Haritalar ile temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr#supported_models)
  artık Gemini 3 modellerinde destekleniyor.

## 16 Mart 2026

- Daha iyi bir kullanıcı faturalandırma deneyimi için yenilenen [Kullanım Katmanları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#about-billing) ve [Faturalandırma Hesabı harcama sınırları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#tier-spend-caps) kullanıma sunuldu.

## 12 Mart 2026

- AI Studio'da faturalandırmaya [proje düzeyinde harcama sınırları](https://ai.google.dev/gemini-api/docs/billing?hl=tr#project-spend-caps) eklendi.

## 10 Mart 2026

- İlk çok formatlı yerleştirme modelimiz olan `gemini-embedding-2-preview` yayınlandı.
  Metin, resim, video, ses ve PDF girişlerini destekler. Tüm formatları birleşik bir yerleştirme alanına eşler. Daha fazla bilgi edinmek için [Embeddings](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) başlıklı makaleyi inceleyin.
- Desteğin sonlandırılmasıyla ilgili duyuru: `gemini-2.5-flash-lite-preview-09-2025` modeli 31 Mart 2026'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 9 Mart 2026

- Gemini 3 Pro Preview modeli [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr). `gemini-3-pro-preview` artık [`gemini-3.1-pro-preview`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr) değerini gösteriyor.

## 3 Mart 2026

- Gemini 3 serisindeki ilk Flash-Lite modeli olan Gemini 3.1 Flash-Lite önizlemesini kullanıma sundu. Özellikler, belirli güncellemeler ve geliştirici yönergeleri için [model sayfasını](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=tr) inceleyin.

## 26 Şubat 2026

- Hız ve yüksek hacimli kullanım alanları için optimize edilmiş yüksek verimli bir model olan [Gemini 3.1 Flash Image Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image-preview?hl=tr) ve Nano Banana 2'yi kullanıma sunduk.
- Desteğin sonlandırılması duyurusu: Gemini 3 Pro Önizleme (`gemini-3-pro-preview`), 9 Mart 2026'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 19 Şubat 2026

- Yeni Gemini 3 serisi ailesinin en yeni modeli olan [Gemini 3.1 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=tr)'ni yayınladık.
- Bash ve araç karışımıyla geliştirme yapan kullanıcılar için özel araçlara öncelik vermede daha iyi olan ayrı bir uç nokta `gemini-3.1-pro-preview-customtools` kullanıma sunuldu.

## 18 Şubat 2026

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modellerin 1 Haziran 2026'da [kapatılacak](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.0-flash`
  - `gemini-2.0-flash-001`
  - `gemini-2.0-flash-lite`
  - `gemini-2.0-flash-lite-001`

## 17 Şubat 2026

- Aşağıdaki modeller [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr):

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`

## 29 Ocak 2026

- `gemini-3-pro-preview` ve `gemini-3-flash-preview`'da Bilgisayar Kullanımı aracı için destek kullanıma sunuldu.

## 21 Ocak 2026

- `latest` takma adları değiştirildi:

  - `gemini-pro-latest`, `gemini-3-pro-preview` ile değiştirildi
  - `gemini-flash-latest`, `gemini-3-flash-preview` ile değiştirildi

## 15 Ocak 2026

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modellerin [desteği](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr) 17 Şubat 2026'da sonlandırılacak:

  - `gemini-2.5-flash-preview-09-25`
  - `imagen-4.0-generate-preview-06-06`
  - `imagen-4.0-ultra-generate-preview-06-06`
- `gemini-2.5-flash-image-preview` modeli kapatıldı.

## 14 Ocak 2026

- `text-embedding-004` modeli [kapatıldı](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr).

## 13 Ocak 2026

- [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) için 4K çıkış çözünürlükleri eklendi ve tüm çözünürlüklerdeki dikey videolar için daha fazla destek sunuldu.

## 12 Ocak 2026

- Model yaşam döngüsü özelliği kullanıma sunuldu. Bazı modeller artık yaşam döngüsü aşamasını ve desteğin sonlandırılma zaman çizelgesini belirtecek. Daha fazla bilgi için aşağıdaki belgelere bakın:

  - [Model aşamaları](https://ai.google.dev/api/generate-content?hl=tr#ModelStatus)

## 8 Ocak 2026

- Cloud Storage paketleri ve Gemini API için veri girişi kaynağı olarak herkese açık ve özel DB önceden imzalanmış URL'leri desteklemeye başladık. Dosya boyutu sınırı da 20 MB'tan 100 MB'a yükseltildi. Ayrıntılar için [Dosya giriş yöntemleri kılavuzu](https://ai.google.dev/gemini-api/docs/file-input-methods?hl=tr) başlıklı makaleyi inceleyin.

## 19 Aralık 2025

- v1beta'da Etkileşimler API'sinde geriye dönük uyumsuzluk içeren bir değişiklik yapıldı. `total_reasoning_tokens` alanı, düşünce modellerindeki "düşünceler" kavramıyla daha iyi uyum sağlamak için `total_thought_tokens` olarak yeniden adlandırıldı.

## 17 Aralık 2025

- `gemini-3-flash-preview` ile Gemini 3 Flash Önizlemesi kullanıma sunuldu. Bu model, daha büyük modellerle rekabet edebilecek hızda ve öncü düzeyde performans sunar ancak maliyeti çok daha düşüktür. Geliştirilmiş görsel ve mekansal akıl yürütme ile üretken kodlama özellikleri. Aşağıdakiler de dahil olmak üzere bazı yeni özelliklerle ilgili dokümanları okuyun:

  - [Çok formatlı işlev yanıtları](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#multimodal)
  - [Görüntülerle kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#images)

## 12 Aralık 2025

- `gemini-2.5-flash-native-audio-preview-12-2025`,
  Live API için yeni bir yerel ses modeli yayınlandı. Bu güncelleme, modelin karmaşık iş akışlarını yönetme becerisini geliştirir. Daha fazla bilgi edinmek için [Live API kılavuzu](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-live?hl=tr)'yu inceleyin.

## 11 Aralık 2025

- Interactions API kullanıma sunuldu. Bu API, Gemini modelleri ve temsilcilerle etkileşim kurmak için tek bir arayüz sağlar. Daha fazla bilgi edinmek için [Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) kılavuzuna bakın.
- Gemini Deep Research Agent'ı önizleme sürümünde kullanıma sundu. Çok adımlı araştırma görevleri için sonuçları bağımsız olarak planlayabilir, yürütebilir ve sentezleyebilir. Ayrıntılı bilgi için [Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) kılavuzuna bakın.

## 10 Aralık 2025

- Gelişmiş ifade, hassas hız ve sorunsuz diyalog gibi özellikler ekleyerek [metin okuma modellerimizi](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) geliştirdik. Bu kapsamda, Gemini 2.5 Flash TTS önizlemesi (düşük gecikme için optimize edilmiştir) ve Gemini 2.5 Pro TTS önizlemesi (kalite için optimize edilmiştir) kullanıma sunuldu.

## 9 Aralık 2025

- Aşağıdaki Gemini Live API modelleri artık kullanılamıyor:
  - `gemini-2.0-flash-live-001`
  - `gemini-live-2.5-flash-preview`

## 5 Aralık 2025

- [Google Arama ile Temellendirme](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) için Gemini 3 faturalandırması 5 Ocak 2026'da başlayacak.

## 4 Aralık 2025

- Kullanımdan kaldırma duyurusu: `gemini-2.5-flash-image-preview` modeli 15 Ocak 2026'da kapatılacak.

## 3 Aralık 2025

- Desteği sonlandırma duyurusu: `text-embedding-004` modeli 14 Ocak 2026'da kapatılacak.

## 20 Kasım 2025

- Nano Banana modelinin bir sonraki sürümü olan `gemini-3-pro-image-preview` Gemini 3 Pro Görüntü Önizleme'yi kullanıma sunduk. Daha fazla bilgi için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) sayfasını inceleyin.

## 18 Kasım 2025

- `gemini-3-pro-preview` adlı ilk Gemini 3 serisi modelimizi kullanıma sunduk. Bu model, güçlü ajan tabanlı ve kodlama özellikleriyle gelişmiş akıl yürütme ve çok formatlı anlama yetenekleri sunuyor.

  Gemini 3 Pro önizlemesi, zeka ve performanstaki iyileştirmelerin yanı sıra aşağıdaki konularda yeni davranışlar sunar:

  - [Medya çözünürlüğü](https://ai.google.dev/gemini-api/docs/media-resolution?hl=tr)
  - [Düşünce imzaları](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr)
  - [Düşünme düzeyleri](https://ai.google.dev/gemini-api/docs/thinking?hl=tr#thinking-levels)

  Geçiş, yeni özellikler ve spesifikasyonlar için [Gemini 3 Geliştirici Kılavuzu](https://ai.google.dev/gemini-api/docs/gemini-3?hl=tr)'nu okuyun.

## 11 Kasım 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modeller kapatılacak:

  - 12 Kasım:

    - `veo-3.0-fast-generate-preview`
    - `veo-3.0-generate-preview`
  - 14 Kasım:

    - `gemini-2.0-flash-exp-image-generation`
    - `gemini-2.0-flash-preview-image-generation`

## 10 Kasım 2025

- Aşağıdaki model kapatıldı:

  - `imagen-3.0-generate-002`

  Bunun yerine [Imagen 4](https://ai.google.dev/gemini-api/docs/imagen?hl=tr#imagen-4)'ü kullanın. Daha fazla bilgi için [Gemini desteği sonlandırma tablosuna](https://ai.google.dev/gemini-api/docs/deprecations?hl=tr) bakın.

## 6 Kasım 2025

- Dosya Arama API'sini herkese açık önizlemeye sunduk. Böylece geliştiriciler, yanıtları kendi verilerine dayandırabilir. Daha fazla bilgi için yeni [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) sayfasını inceleyin.

## 4 Kasım 2025

- [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) için resimlerin giriş jetonu sayısı 1.290'dan 258'e düşürülerek resim düzenleme maliyeti azaltıldı.
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

- Gemini API için yeni [günlük kaydı ve veri kümeleri](https://ai.google.dev/gemini-api/docs/logs-datasets?hl=tr) aracını kullanıma sundu.

## 20 Ekim 2025

- Aşağıdaki Gemini Live API modelleri artık kullanılamıyor:

  - `gemini-2.5-flash-preview-native-audio-dialog`
  - `gemini-2.5-flash-exp-native-audio-thinking-dialog`

  Bunun yerine `gemini-2.5-flash-native-audio-preview-09-2025` kullanabilirsiniz.
- Desteğin sonlandırılması duyurusu: `gemini-2.0-flash-live-001` ve `gemini-live-2.5-flash-preview` için 9 Aralık 2025'te destek sonlandırılacak.

## 17 Ekim 2025

- **Google Haritalar ile Temellendirme** artık genel olarak kullanılabilir. Daha fazla bilgi için [Google Haritalar ile Temellendirme](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) belgelerine bakın.

## 15 Ekim 2025

- [Veo 3.1 ve 3.1 Fast](https://ai.google.dev/gemini-api/docs/video?hl=tr#veo-3.1) modellerini herkese açık önizleme sürümünde yayınladık. Bu modellerde aşağıdaki gibi yeni özellikler yer alıyor:

  - Veo ile oluşturulan videoların süresini uzatma
  - Video oluşturmak için en fazla üç resimden referans alma
  - Videolar oluşturmak için ilk ve son kare görüntülerini sağlama

  Bu lansmanla birlikte Veo 3 çıkış video süreleri için 4, 6 ve 8 saniyelik seçenekler de eklendi.
- Desteğin sonlandırılması duyurusu: `veo-3.0-generate-preview` ve `veo-3.0-fast-generate-preview` için 12 Kasım 2025'te kapatılacak.

## 7 Ekim 2025

- [Gemini 2.5 Bilgisayar Kullanımı Önizlemesi](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) kullanıma sunuldu

## 2 Ekim 2025

- Gemini 2.5 Flash Image GA'yı kullanıma sunduk: [Gemini ile görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr)

## 29 Eylül 2025

- Aşağıdaki Gemini 1.5 modelleri artık kullanılamıyor:
  - `gemini-1.5-pro`
  - `gemini-1.5-flash-8b`
  - `gemini-1.5-flash`

## 25 Eylül 2025

- Gemini Robotics-ER 1.5 modelinin önizleme sürümü yayınlandı. Modeli robotik uygulamanızda nasıl kullanacağınızı öğrenmek için [Robotik uygulamalarına genel bakış](https://ai.google.dev/gemini-api/docs/robotics-overview?hl=tr) bölümüne bakın.
- Aşağıdaki önizleme modelleri kullanıma sunuldu:

  - `gemini-2.5-flash-preview-09-2025`
  - `gemini-2.5-flash-lite-preview-09-2025`

  Ayrıntılı bilgi için [Modeller](https://ai.google.dev/gemini-api/docs/models?hl=tr) sayfasına bakın.

## 23 Eylül 2025

- `gemini-2.5-flash-native-audio-preview-09-2025`, Live API için geliştirilmiş işlev çağırma ve konuşma kesme işleme özelliklerine sahip yeni bir yerel ses modeli yayınlandı. Daha fazla bilgi edinmek için [Live API kılavuzu](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-native-audio)'yu inceleyin.

## 16 Eylül 2025

- Desteğin sonlandırılmasıyla ilgili duyuru: Aşağıdaki modellerin desteği Ekim 2025'te sonlandırılacak:

  - `embedding-001`
  - `embedding-gecko-001`
  - `gemini-embedding-exp-03-07` (`gemini-embedding-exp`)

  En yeni yerleştirme modeliyle ilgili ayrıntılar için [Yerleştirmeler](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) sayfasına bakın.

## 10 Eylül 2025

- [Toplu API'deki Embeddings modeli](https://ai.google.dev/gemini-api/docs/batch-api?hl=tr#batch-embedding) için destek kullanıma sunuldu ve toplu sorgulara başlamanın daha da kolay yollarını sunmak amacıyla Toplu API, [OpenAI uyumluluk kitaplığına](https://ai.google.dev/gemini-api/docs/openai?hl=tr#batch) eklendi.

## 9 Eylül 2025

- Veo 3 ve Veo 3 Fast GA'yı kullanıma sunduk. Bu sürümlerde daha düşük fiyatlandırma ve en-boy oranları, çözünürlük ve başlangıç için yeni seçenekler sunuluyor. Daha fazla bilgi için [Veo dokümanlarını](https://ai.google.dev/gemini-api/docs/video?hl=tr#model-features) inceleyin.

## 26 Ağustos 2025

- En yeni yerel görüntü üretme modelimiz [Gemini 2.5 Görüntü Önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-image-preview)'yi kullanıma sunduk.

## 18 Ağustos 2025

- Genel kullanıma sunulan [URL bağlamı aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr), istemlere ek bağlam olarak URL'ler sağlayan bir araçtır. `gemini-2.0-flash` modeliyle URL bağlamı kullanımına yönelik destek
  (deneysel sürümde kullanılabilir) bir hafta içinde sonlandırılacak.

## 14 Ağustos 2025

- Imagen 4 Ultra, Standard ve Fast modelleri genel kullanıma sunuldu (GA). Daha fazla bilgi edinmek için [Imagen](https://ai.google.dev/gemini-api/docs/imagen?hl=tr) sayfasına bakın.

## 7 Ağustos 2025

- `allow_adult` ayarı artık kısıtlı bölgelerde kullanılabilir. Ayrıntılar için [Veo](https://ai.google.dev/gemini-api/docs/video?example=dialogue&hl=tr#veo-model-parameters) sayfasına bakın.

## 31 Temmuz 2025

- Veo 3 Preview modeli için görselden video oluşturma özelliğini kullanıma sunduk.
- Veo 3 Fast Preview modelini kullanıma sunduk.
- Veo 3 hakkında daha fazla bilgi edinmek için [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) sayfasını ziyaret edin.

## 22 Temmuz 2025

- Hızlı, düşük maliyetli ve yüksek performanslı Gemini 2.5 modelimiz `gemini-2.5-flash-lite`'ı kullanıma sunduk. Daha fazla bilgi için [Gemini 2.5
  Flash-Lite](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-lite) başlıklı makaleyi inceleyin.

## Temmuz 17, 2025

- Veo'nun en yeni güncellemesi olan `veo-3.0-generate-preview`'yı kullanıma sunduk. Bu güncelleme, sesli video üretme özelliğini içeriyor. Veo 3 hakkında daha fazla bilgi edinmek için [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr) sayfasını ziyaret edin.
- Imagen 4 Standard ve Ultra için artırılmış hız sınırları. Daha fazla bilgi için [Hız sınırları](https://ai.google.dev/gemini-api/docs/rate-limits?hl=tr) sayfasını ziyaret edin.

## 14 Temmuz 2025

- Metin yerleştirme modelimizin kararlı sürümü olan `gemini-embedding-001` yayınlandı. Daha fazla bilgi edinmek için [gömme](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr) başlıklı makaleyi inceleyin. `gemini-embedding-exp-03-07`
  modeli 14 Ağustos 2025'te kullanımdan kaldırılacak.

## 7 Temmuz 2025

- Gemini API Toplu İşlem Modu kullanıma sunuldu. İstekleri toplu olarak gönderin ve bunları işlenmek üzere eşzamansız olarak gönderin. Daha fazla bilgi edinmek için [Toplu Mod](https://ai.google.dev/gemini-api/docs/batch-mode?hl=tr) başlıklı makaleyi inceleyin.

## 26 Haziran 2025

- Önizleme modelleri `gemini-2.5-pro-preview-05-06` ve `gemini-2.5-pro-preview-03-25` artık en yeni kararlı sürüme `gemini-2.5-pro` yönlendiriliyor.
- `gemini-2.5-pro-exp-03-25` kapatıldı.

## 24 Haziran 2025

- Imagen 4 Ultra ve Standard Preview modelleri yayınlandı. Daha fazla bilgi için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) sayfasına bakın.

## 17 Haziran 2025

- En güçlü modelimizin kararlı sürümü olan `gemini-2.5-pro`'ı yayınladık. Bu sürümde artık uyarlanabilir düşünme özelliği bulunuyor. Daha fazla bilgi edinmek için [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro) ve [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin. `gemini-2.5-pro-preview-05-06`
  26 Haziran 2025'te `gemini-2.5-pro` adresine yönlendirilecek.
- İlk kararlı 2.5 Flash modelimiz olan `gemini-2.5-flash`'i yayınladık. Daha fazla bilgi için [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash) başlıklı makaleyi inceleyin.
  `gemini-2.5-flash-preview-04-17`, 15 Temmuz 2025'te kullanımdan kaldırılacak.
- Düşük maliyetli ve yüksek performanslı bir Gemini 2.5 modeli olan `gemini-2.5-flash-lite-preview-06-17`'ı kullanıma sundu. Daha fazla bilgi için [Gemini 2.5 Flash-Lite Önizlemesi](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-lite) başlıklı makaleyi inceleyin.

## 5 Haziran 2025

- En güçlü modelimizin yeni sürümü olan `gemini-2.5-pro-preview-06-05`'ı yayınladık. Bu sürümde artık uyarlanabilir düşünme özelliği bulunuyor. Daha fazla bilgi edinmek için [Gemini 2.5 Pro Önizlemesi](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-06-05) ve [Düşünme](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makalelere göz atın.
  `gemini-2.5-pro-preview-05-06`, 26 Haziran 2025'te `gemini-2.5-pro` adresine yönlendirilecek.

## 27 Mayıs 2025

- Kullanılabilen son ince ayar modeli olan Gemini 1.5 Flash 001 kapatıldı.
  İnce ayar özelliği artık hiçbir modelde desteklenmiyor.
  [Gemini API ile ince ayar yapma](https://ai.google.dev/gemini-api/docs/model-tuning?hl=tr) başlıklı makaleyi inceleyin.

## 20 Mayıs 2025

**API güncellemeleri:**

- Kırpma aralıkları ve yapılandırılabilir kare hızı örnekleme kullanılarak [özel video ön işleme](https://ai.google.dev/gemini-api/docs/video-understanding?hl=tr#customize-video-processing) desteği kullanıma sunuldu.
- Aynı `generateContent` isteğinde [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) ve [Google Arama ile temellendirme](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) yapılandırmasını destekleyen çoklu araç kullanımını kullanıma sunduk.
- Live API'de [asenkron işlev çağrıları](https://ai.google.dev/gemini-api/docs/live-tools?hl=tr#async-function-calling) için destek kullanıma sunuldu.
- İstemlere ek bağlam olarak URL'ler sağlamak için deneysel bir [URL bağlam aracı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) kullanıma sunuldu.

**Model güncellemeleri:**

- Fiyat-performans ve uyarlanabilir düşünme için optimize edilmiş bir Gemini [önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#model-versions) modeli olan `gemini-2.5-flash-preview-05-20`'ı kullanıma sunduk. Daha fazla bilgi edinmek için [Gemini 2.5 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview) ve [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin.
- Bir veya iki konuşmacıyla [konuşma üretebilen](https://ai.google.dev/gemini-api/docs/speech-generation?hl=tr) [`gemini-2.5-pro-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-tts) ve [`gemini-2.5-flash-preview-tts`](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview-tts) modellerini kullanıma sundu.
- Gerçek zamanlı olarak [müzik üreten](https://ai.google.dev/gemini-api/docs/music-generation?hl=tr) `lyria-realtime-exp` modelini kullanıma sundu.
- `gemini-2.5-flash-preview-native-audio-dialog` ve
  `gemini-2.5-flash-exp-native-audio-thinking-dialog`,
  yerel ses çıkışı özelliklerine sahip Live API için yeni Gemini modelleri yayınlandı. Daha fazla bilgi edinmek için [Live API kılavuzu](https://ai.google.dev/gemini-api/docs/live-guide?hl=tr#native-audio-output) ve [Gemini 2.5 Flash Native Audio](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-native-audio) başlıklı dokümanları inceleyin.
- `gemma-3n-e4b-it` Önizleme sürümü yayınlandı. [AI Studio](https://aistudio.google.com?hl=tr)'da ve Gemini API aracılığıyla [Gemma 3n](https://ai.google.dev/gemma/docs/3n?hl=tr) lansmanı kapsamında kullanılabilir.

## 7 Mayıs 2025

- Resim oluşturma ve düzenleme için önizleme modeli olan `gemini-2.0-flash-preview-image-generation`'ı kullanıma sundu. Daha fazla bilgi edinmek için [Görüntü üretme](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr) ve [Gemini 2.0 Flash Image Generation Önizlemesi](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.0-flash-preview-image-generation) başlıklı makaleleri inceleyin.

## 6 Mayıs 2025

- En güçlü modelimizin yeni sürümü olan `gemini-2.5-pro-preview-05-06`'ı yayınladık. Bu sürümde kod ve işlev çağrısı konusunda iyileştirmeler yapıldı. `gemini-2.5-pro-preview-03-25`
  modelin yeni sürümüne otomatik olarak yönlendirilir.

## 17 Nisan 2025

- Fiyat-performans ve uyarlanabilir düşünme için optimize edilmiş bir Gemini [önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#model-versions) modeli olan `gemini-2.5-flash-preview-04-17`'ı kullanıma sunduk. Daha fazla bilgi edinmek için [Gemini 2.5 Flash Önizlemesi](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-flash-preview) ve [Thinking](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) başlıklı makaleleri inceleyin.

## 16 Nisan 2025

- [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.0-flash) için bağlam önbelleğe alma özelliği kullanıma sunuldu.

## 9 Nisan 2025

**Model güncellemeleri:**

- Genel kullanıma sunulan (GA) bir metin ve resimden videoya model olan `veo-2.0-generate-001`'ı kullanıma sunduk. Bu model, ayrıntılı ve sanatsal açıdan incelikli videolar oluşturabiliyor. Daha fazla bilgi edinmek için [Veo belgelerine](https://ai.google.dev/gemini-api/docs/video?hl=tr) göz atın.
- Faturalandırmanın etkinleştirildiği [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) modelinin herkese açık önizleme sürümü olan `gemini-2.0-flash-live-001` yayınlandı.

  - **Gelişmiş Oturum Yönetimi ve Güvenilirlik**

    - **Oturuma Devam Etme:** Geçici ağ kesintileri sırasında oturumları etkin tutun. API artık sunucu tarafında oturum durumu depolamayı (24 saate kadar) destekliyor ve yeniden bağlanıp kaldığınız yerden devam etmenizi sağlayan tutma yerleri (session\_resumption) sunuyor.
    - **Bağlam sıkıştırma sayesinde daha uzun oturumlar:** Önceki zaman sınırlarının ötesinde etkileşimlere olanak tanır. Bağlam penceresi sıkıştırmasını, bağlam uzunluğunu otomatik olarak yönetmek için kayan pencere mekanizmasıyla yapılandırın. Bu sayede, bağlam sınırları nedeniyle ani sonlandırmalar önlenir.
    - **Graceful Disconnect Notification:** Bağlantının ne zaman kapanacağına dair `GoAway` sunucu mesajı alın. Bu mesaj, sonlandırmadan önce bağlantının sorunsuz bir şekilde kapatılmasını sağlar.
  - **Etkileşim Dinamikleri Üzerinde Daha Fazla Kontrol**
  - **Yapılandırılabilir Ses Etkinliği Algılama (VAD):** Hassasiyet seviyelerini seçin veya otomatik VAD'yi tamamen devre dışı bırakıp manuel dönüş kontrolü için yeni istemci etkinliklerini (`activityStart`, `activityEnd`) kullanın.
  - **Yapılandırılabilir Kesinti İşleme:** Kullanıcı girişinin modelin yanıtını kesip kesmeyeceğine karar verin.
  - **Yapılandırılabilir Konuşma Kapsamı:** API'nin tüm ses ve video girişlerini sürekli olarak mı işleyeceğini yoksa yalnızca son kullanıcı konuşurken mi yakalayacağını seçin.
  - **Yapılandırılabilir Medya Çözünürlüğü:** Giriş medyası için çözünürlüğü seçerek kalite veya jeton kullanımı için optimizasyon yapın.
  - **Daha zengin çıkış ve özellikler**
  - **Genişletilmiş Ses ve Dil Seçenekleri:** Ses çıkışı için iki yeni ses ve 30 yeni dil arasından seçim yapın. Çıkış dili artık `speechConfig` içinde yapılandırılabilir.
  - **Metin Akışı:** Metin yanıtlarını oluşturuldukça artımlı olarak alarak kullanıcılara daha hızlı bir şekilde gösterebilirsiniz.
  - **Jeton Kullanımı Raporlama:** Sunucu mesajlarının `usageMetadata` alanında sağlanan ayrıntılı jeton sayılarıyla kullanım hakkında bilgi edinin. Bu sayılar, biçime ve istem veya yanıt aşamalarına göre ayrılır.

## 4 Nisan 2025

- Faturalandırmanın etkin olduğu herkese açık önizleme Gemini 2.5 Pro sürümü `gemini-2.5-pro-preview-03-25` yayınlandı. `gemini-2.5-pro-exp-03-25` uygulamasını ücretsiz katmanda kullanmaya devam edebilirsiniz.

## 25 Mart 2025

- Düşünme modunun varsayılan olarak her zaman açık olduğu, herkese açık deneysel bir Gemini modeli olan `gemini-2.5-pro-exp-03-25`'ı kullanıma sundu.
  Daha fazla bilgi için [Gemini 2.5 Pro Deneysel](https://ai.google.dev/gemini-api/docs/models?hl=tr#gemini-2.5-pro-preview-03-25) başlıklı makaleyi inceleyin.

## 12 Mart 2025

**Model güncellemeleri:**

- Görüntü oluşturma ve düzenleme özelliklerine sahip deneysel [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/image-generation?hl=tr#gemini) modelini kullanıma sunduk.
- `gemma-3-27b-it` sürümü yayınlandı. [AI Studio](https://aistudio.google.com?hl=tr)'da ve Gemini API üzerinden [Gemma 3](https://ai.google.dev/gemma/docs/core?hl=tr) lansmanı kapsamında kullanılabilir.

**API güncellemeleri:**

- Medya kaynağı olarak [YouTube URL'leri](https://ai.google.dev/gemini-api/docs/vision?hl=tr#youtube) için destek eklendi.
- 20 MB'tan küçük [satır içi video](https://ai.google.dev/gemini-api/docs/vision?hl=tr#inline-video) ekleme desteği eklendi.

## 11 Mart 2025

**SDK güncellemeleri:**

- [TypeScript ve JavaScript için Google Gen AI SDK](https://googleapis.github.io/js-genai)'nın herkese açık önizleme sürümü yayınlandı.

## 7 Mart 2025

**Model güncellemeleri:**

- Herkese açık önizleme sürümünde `gemini-embedding-exp-03-07`, Gemini tabanlı bir [deneysel](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr) gömme modeli yayınlandı.

## 28 Şubat 2025

**API güncellemeleri:**

- `gemini-2.0-pro-exp-02-05`'ye [Araç olarak Arama](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) desteği eklendi. Bu deneysel model, Gemini 2.0 Pro'ya dayanmaktadır.

## 25 Şubat 2025

**Model güncellemeleri:**

- Hız, ölçek ve maliyet verimliliği için optimize edilmiş [Gemini 2.0 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash-lite)'ın genel kullanıma sunulan (GA) sürümü `gemini-2.0-flash-lite` yayınlandı.

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

- [OpenAI kitaplıklarının uyumluluğu](https://ai.google.dev/gemini-api/docs/openai?hl=tr) ile ilgili güncellemeler.

## 6 Şubat 2025

**Model güncellemeleri:**

- `imagen-3.0-generate-002`, [Gemini API'deki Imagen 3](https://ai.google.dev/gemini-api/docs/imagen?hl=tr)'ün genel kullanıma açık (GA) sürümü yayınlandı.

**SDK güncellemeleri:**

- [Java için Google Gen AI SDK](https://github.com/googleapis/java-genai)'nın genel önizleme sürümünü yayınladık.

## 5 Şubat 2025

**Model güncellemeleri:**

- Yalnızca metin çıkışını destekleyen [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash)'in genel kullanıma sunulmuş (GA) sürümü `gemini-2.0-flash-001` yayınlandı.
- `gemini-2.0-pro-exp-02-05`,
  Gemini 2.0 Pro'nun [deneysel](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr) herkese açık
  önizleme sürümü yayınlandı.
- Maliyet verimliliği için optimize edilmiş deneysel bir herkese açık önizleme [modeli](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash-lite) olan `gemini-2.0-flash-lite-preview-02-05`'ı kullanıma sundu.

**API güncellemeleri:**

- Kod yürütmeye [dosya girişi ve grafik çıkışı](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr#input-output) desteği eklendi.

**SDK güncellemeleri:**

- [Python için Google Gen AI SDK](https://googleapis.github.io/python-genai/)'yı genel kullanıma sunulma tarihi (GA) olarak belirledi.

## 21 Ocak 2025

**Model güncellemeleri:**

- `gemini-2.0-flash-thinking-exp-01-21`, [Gemini 2.0 Flash Thinking Model](https://ai.google.dev/gemini-api/docs/thinking?hl=tr)'in temelini oluşturan modelin en yeni önizleme sürümü yayınlandı.

## 19 Aralık 2024

**Model güncellemeleri:**

- Gemini 2.0 Flash Thinking Modu'nu genel önizlemeye sunduk. Düşünme Modu, modelin yanıt oluştururken düşünce sürecini görmenizi sağlayan ve daha güçlü akıl yürütme özelliklerine sahip yanıtlar üreten bir test zamanı hesaplama modelidir.

  Gemini 2.0 Flash Thinking Modu hakkında daha fazla bilgiyi [genel bakış sayfamızda](https://ai.google.dev/gemini-api/docs/thinking-mode?hl=tr) bulabilirsiniz.

## 11 Aralık 2024

**Model güncellemeleri:**

- [Gemini 2.0 Flash Experimental](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-2.0-flash), genel önizleme için kullanıma sunuldu. Gemini 2.0 Flash Experimental'ın özelliklerinin kısmi listesi şunları içerir:
  - Gemini 1.5 Pro'dan iki kat daha hızlı
  - Live API'miz ile çift yönlü yayın
  - Metin, resim ve konuşma şeklinde çok formatlı yanıt üretimi
  - Kod yürütme, Arama, işlev çağırma ve daha fazlası gibi özellikleri kullanmak için çok aşamalı etkileşimli akıl yürütme ile yerleşik araç kullanımı

Gemini 2.0 Flash hakkında daha fazla bilgiyi [genel bakış sayfamızda](https://ai.google.dev/gemini-api/docs/models/gemini-v2?hl=tr) bulabilirsiniz.

## 21 Kasım 2024

**Model güncellemeleri:**

- Daha da güçlü bir deneysel Gemini API modeli olan `gemini-exp-1121` yayınlandı.

**Model güncellemeleri:**

- `gemini-1.5-flash-latest` ve `gemini-1.5-flash` model takma adları, `gemini-1.5-flash-002` kullanacak şekilde güncellendi.
  - `top_k` parametresinde değişiklik: `gemini-1.5-flash-002`
    modeli, 1 ile 41 (hariç) arasındaki `top_k` değerlerini destekler.
    40'tan büyük değerler 40 olarak değiştirilir.

## 14 Kasım 2024

**Model güncellemeleri:**

- Güçlü bir deneysel Gemini API modeli olan `gemini-exp-1114`'ı yayınladı.

## 8 Kasım 2024

**API güncellemeleri:**

- OpenAI kitaplıklarında / REST API'sinde [Gemini desteği](https://ai.google.dev/gemini-api/docs/openai?hl=tr) eklendi.

## 31 Ekim 2024

**API güncellemeleri:**

- [Google Arama ile Temellendirme desteği](https://ai.google.dev/gemini-api/docs/grounding?hl=tr) eklendi.

## 3 Ekim 2024

**Model güncellemeleri:**

- En küçük Gemini API modelimizin kararlı sürümü olan `gemini-1.5-flash-8b-001`'ı yayınladık.

## 24 Eylül 2024

**Model güncellemeleri:**

- Gemini 1.5 Pro ve 1.5 Flash'in iki yeni kararlı sürümü `gemini-1.5-pro-002` ve `gemini-1.5-flash-002` genel kullanıma sunuldu.
- `gemini-1.5-pro-latest` model kodu `gemini-1.5-pro-002`, `gemini-1.5-flash-latest` model kodu ise `gemini-1.5-flash-002` kullanacak şekilde güncellendi.
- `gemini-1.5-flash-8b-exp-0827` yerine `gemini-1.5-flash-8b-exp-0924` sürümü yayınlandı.
- Gemini API ve AI Studio için [sivil bütünlük güvenlik filtresi](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr#safety-filters) yayınlandı.
- Python ve NodeJS'de Gemini 1.5 Pro ve 1.5 Flash için iki yeni parametre desteği kullanıma sunuldu:
  [`frequencyPenalty`](https://ai.google.dev/api/generate-content?hl=tr#FIELDS.frequency_penalty) ve
  [`presencePenalty`](https://ai.google.dev/api/generate-content?hl=tr#FIELDS.presence_penalty).

## 19 Eylül 2024

**AI Studio güncellemeleri:**

- Kullanıcıların yanıt kalitesiyle ilgili geri bildirimde bulunabilmesi için model yanıtlarına beğenme ve beğenmeme düğmeleri eklendi.

**API güncellemeleri:**

- Google Cloud kredileri için destek eklendi. Bu krediler artık Gemini API kullanımında kullanılabilir.

## 17 Eylül 2024

**AI Studio güncellemeleri:**

- Bir istemi ve istemi uygulamak için gereken kodu Colab not defterine aktaran **Colab'de aç** düğmesi eklendi. Bu özellik henüz araçlarla (JSON modu, işlev çağrısı veya kod yürütme) istem oluşturmayı desteklemiyor.

## 13 Eylül 2024

**AI Studio güncellemeleri:**

- Kullanım alanınıza en uygun olanı bulmak için yanıtları modeller ve istemler arasında karşılaştırmanıza olanak tanıyan karşılaştırma modu desteği eklendi.

## 30 Ağustos 2024

**Model güncellemeleri:**

- Gemini 1.5 Flash, [model yapılandırması aracılığıyla JSON şeması sağlamayı](https://ai.google.dev/gemini-api/docs/json-mode?hl=tr#supply-schema-in-config) destekler.

## 27 Ağustos 2024

**Model güncellemeleri:**

- Aşağıdaki [deneysel modeller](https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr) yayınlandı:
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

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro)'nun yeni deneme sürümü `gemini-1.5-pro-exp-0801` yayınlandı.

## 12 Temmuz 2024

**Model güncellemeleri:**

- Gemini 1.0 Pro Vision desteği, Google AI hizmetlerinden ve araçlarından kaldırıldı.

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

- Gemini 1.0 Pro Vision desteği sonlandırıldı.

## 23 Mayıs 2024

**Model güncellemeleri:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro)
  (`gemini-1.5-pro-001`) genel kullanıma sunuldu.
- [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-flash)
  (`gemini-1.5-flash-001`) genel kullanıma sunuldu.

## 14 Mayıs 2024

**API güncellemeleri:**

- Gemini 1.5 Pro için 2 milyon parçalık bağlam penceresi kullanıma sunuldu (bekleme listesi).
- Gemini 1.0 Pro için kullandıkça öde [faturalandırma](https://ai.google.dev/gemini-api/docs/billing?hl=tr) özelliği kullanıma sunuldu. Gemini 1.5 Pro ve Gemini 1.5 Flash faturalandırma özellikleri yakında kullanıma sunulacak.
- Gemini 1.5 Pro'nun yakında kullanıma sunulacak ücretli katmanı için daha yüksek hız sınırları kullanıma sunuldu.
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr)'ye yerleşik video desteği eklendi.
- [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr)'ye düz metin desteği eklendi.
- Aynı anda birden fazla çağrı döndüren paralel işlev çağrısı desteği eklendi.

## 10 Mayıs 2024

**Model güncellemeleri:**

- Önizleme sürümünde [Gemini 1.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) kullanıma sunuldu.

## 9 Nisan 2024

**Model güncellemeleri:**

- [Gemini 1.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr#gemini-1.5-pro) (`gemini-1.5-pro-latest`) önizleme sürümü yayınlandı.
- 768'den küçük [esnek yerleştirme](https://ai.google.dev/gemini-api/docs/embeddings?hl=tr#elastic-embedding) boyutlarını destekleyen yeni bir metin yerleştirme modeli olan `text-embeddings-004`'yı kullanıma sundu.

**API güncellemeleri:**

- İstemlerde kullanılmak üzere medya dosyalarını geçici olarak depolamak için [File API](https://ai.google.dev/api/rest/v1beta/files?hl=tr)'yi kullanıma sunduk.
- Metin, resim ve ses verileriyle istem yazma (*çok formatlı* istem yazma olarak da bilinir) desteği eklendi. Daha fazla bilgi için [Medya ile istem oluşturma](https://ai.google.dev/gemini-api/docs/prompting_with_media?hl=tr) başlıklı makaleyi inceleyin.
- Beta sürümünde [Sistem talimatları](https://ai.google.dev/gemini-api/docs/system-instructions?hl=tr) yayınlandı.
- İşlev çağrısı için yürütme davranışını tanımlayan [işlev çağrısı modu](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#function_calling_mode) eklendi.
- `response_mime_type` yapılandırma seçeneği için destek eklendi. Bu seçenek, yanıtları [JSON biçiminde](https://ai.google.dev/gemini-api/docs/api-overview?hl=tr#json) istemenize olanak tanır.

## 19 Mart 2024

**Model güncellemeleri:**

- Google AI Studio'da veya Gemini API ile [Gemini 1.0 Pro'yu ayarlama](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/) desteği eklendi.

## 13 Aralık 2023

**Model güncellemeleri:**

- gemini-pro: Çok çeşitli görevler için yeni metin modeli. Yetenek ve verimlilik arasında denge kurar.
- gemini-pro-vision: Çok çeşitli görevler için yeni çok formatlı model.
  Kapasite ve verimliliği dengeler.
- embedding-001: Yeni yerleştirme modeli.
- aqa: Oluşturulan yanıtları temellendirmek için metin pasajlarını kullanarak soruları yanıtlamak üzere eğitilmiş, özel olarak ayarlanmış yeni bir model.

Daha fazla bilgi için [Gemini modelleri](https://ai.google.dev/gemini-api/docs/models/gemini?hl=tr) başlıklı makaleyi inceleyin.

**API sürümü güncellemeleri:**

- v1: Kararlı API kanalı.
- v1beta: Beta kanalı. Bu kanalda geliştirme aşamasında olabilecek özellikler var.

Daha fazla bilgi için [API sürümleri konusuna](https://ai.google.dev/gemini-api/docs/api-versions?hl=tr) bakın.

**API güncellemeleri:**

- `GenerateContent`, sohbet ve metin için tek bir birleşik uç noktadır.
- Akış, `StreamGenerateContent` yöntemiyle kullanılabilir.
- Çok formatlı özellik: Resim, yeni bir desteklenen format
- Yeni beta özellikleri:
  - [İşlev Çağırma](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr)
  - [Semantic Retriever](https://ai.google.dev/gemini-api/docs/semantic_retrieval?hl=tr)
  - Kaynaklı Soru Yanıtlama (AQA)
- Güncellenen aday sayısı: Gemini modelleri yalnızca 1 aday döndürür.
- Farklı güvenlik ayarları ve güvenlik derecelendirmesi kategorileri. Daha fazla bilgi için [güvenlik ayarları](https://ai.google.dev/gemini-api/docs/safety-settings?hl=tr) başlıklı makaleyi inceleyin.
- Modelleri ayarlama, Gemini modellerinde henüz desteklenmemektedir (Çalışmalar devam etmektedir).

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
