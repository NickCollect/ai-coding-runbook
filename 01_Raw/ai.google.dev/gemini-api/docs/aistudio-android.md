---
source_url: https://ai.google.dev/gemini-api/docs/aistudio-android?hl=tr
fetched_at: 2026-07-20T04:41:42.988829+00:00
title: "Google AI Studio'da Android uygulamalar\u0131 geli\u015ftirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Google AI Studio'da Android uygulamaları geliştirme

Google AI Studio, doğal dil isteminden yerel Android uygulamaları oluşturmanıza olanak tanır. İstediğiniz uygulamayı tanımlayın. [Antigravity Agent](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=tr#antigravity-agent), eksiksiz bir Kotlin ve [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=tr) projesi oluşturur. Tarayıcınızdan uygulamanızı tarayıcı tabanlı bir Android emülatöründe önizleyebilir, fiziksel bir cihaza yükleyebilir ve test için yayınlayabilirsiniz.

## Başlayın

Android uygulaması geliştirmeye başlamak için:

1. Sol taraftaki gezinme panelini kullanarak Google AI Studio'da [Oluşturma modu](https://aistudio.google.com/apps?hl=tr)'na gidin.
2. Platform seçiciden **Android**'i seçin.
3. Oluşturmak istediğiniz uygulamayı açıklayan bir istem girin (örneğin, *"Yerel depolama alanına sahip günlük görev takipçisi oluştur"* veya *"Basit bir hesap makinesi oluştur"*).
4. Ajan, projeyi oluşturur ve tarayıcı tabanlı Android emülatöründe başlatır.

Ardından, web deneyiminde olduğu gibi sohbet panelini kullanarak uygulamanızı yineleyebilirsiniz. Temsilci, Android projenizdeki tüm dosyaları yönetir ve değişiklikleri kod tabanına yayar.

## Tarayıcı tabanlı Android emülatörü

Android emülatörü tamamen bulutta çalışır ve tarayıcınıza yayın yapar.
Android SDK'yı, Android Studio'yu veya yerel bir emülatörü yüklemeniz gerekmez.

Emülatör şunları sağlar:

- **Pixel benzeri cihaz simülasyonu**: Uygulamanızla gerçek bir cihazda olduğu gibi dokunarak, kaydırarak ve etkileşimde bulunarak test edin.
- **Döndürme desteği**: Dikey ve yatay yön arasında geçiş yapın.
- **Canlı önizleme**: Temsilci kodda değişiklik yaptığında uygulama yeniden oluşturulur ve emülatör otomatik olarak yenilenir.

### Emülatör sınırlamaları

Tarayıcı tabanlı emülatör, tüm donanım özelliklerini desteklemez. Aşağıdakiler emülatörde kullanılamaz:

- Kamera ve fotoğraf çekme
- NFC ve Bluetooth
- GPS (konum simüle ediliyor)
- Google Play Hizmetleri (Google ile Oturum Açma, Haritalar ve diğer Play Hizmetleri özellikleri gerçek cihazda çalışır ancak emülatörde çalışmaz)

## ADB'nin yüklü olduğu bir cihaza yükleme

Oluşturulan APK'yı, USB ile bilgisayarınıza bağlı fiziksel bir Android cihaza doğrudan yükleyebilirsiniz. Bu işlem, tarayıcı üzerinden cihazınızla iletişim kurmak için [WebUSB](https://developer.chrome.com/docs/capabilities/usb?hl=tr)'yi kullanır. Yerel ADB kurulumu gerekmez.

### Ön koşullar

- WebUSB'yi destekleyen bir Chrome veya Edge tarayıcı
- [Geliştirici Seçenekleri ve USB üzerinden hata ayıklama](https://developer.android.com/studio/debug/dev-options?hl=tr)'nın etkin olduğu bir Android cihaz.
- Cihazınızı bilgisayarınıza bağlayan bir USB kablosu

### Uygulamayı cihazınıza yükleyin

1. Önizleme panelinde **Cihaza Yükle**'yi tıklayın.
2. Tarayıcının USB cihaz seçicisinden Android cihazınızı seçin.
3. APK, cihazınıza aktarılıp yüklenir.
4. Uygulama otomatik olarak başlatılır.

## Play Store'da yayınlama

Android uygulamanızı [Google Play Console](https://play.google.com/console?hl=tr)'un dahili test kanalında yayınlayabilirsiniz. Bu kanal, uygulamayı 100'e kadar test kullanıcısına dağıtmanıza olanak tanır.

### Ön koşullar

- [Google Play Geliştirici hesabı](https://play.google.com/console/signup?hl=tr)
  (bir defalık 25 ABD doları kayıt ücreti gerekir).
- Play Console'da tamamlanmış bir geliştirici profili.

### Uygulamanızı yayınlama

1. Google AI Studio'da **Ayarlar > Yayınla**'yı açın.
2. **Play Store'da yayınla**'yı tıklayın.
3. Google Play Geliştirici Hesabınızla kimliğinizi doğrulayın.
4. AI Studio, APK'yı imzalar, uygulama girişini oluşturur (veya yeni bir sürüm yükler) ve dahili test kanalında yayınlar.
5. Test kullanıcılarınızla paylaşabileceğiniz bir bağlantı alırsınız.

AI Studio, yönetilen bir anahtar deposu kullanarak APK imzalama işlemini otomatik olarak yönetir. Uygulama girişini (simge, ekran görüntüleri, açıklama) daha sonra Play Console'da özelleştirebilirsiniz.

## Oluşturulan içerikler

Bir Android uygulaması oluşturduğunuzda aracı, aşağıdaki yapıya sahip standart bir Gradle tabanlı proje oluşturur:

- **Derleme yapılandırması**: Kotlin DSL kullanılarak `build.gradle.kts` dosyaları (proje ve uygulama düzeyi).
- **Kullanıcı arayüzü katmanı**: [Material 3](https://m3.material.io/) temalı [Jetpack Compose](https://developer.android.com/develop/ui/compose?hl=tr) bileşenleri.
- **Mimari**: ViewModel'ler ve veri sınıflarıyla tek etkinlikli mimari.
- **Kaynaklar**: `AndroidManifest.xml`, drawables, dizeler ve diğer Android kaynakları.

Aracı, Gradle bağımlılıklarını otomatik olarak yönetir ve gerektiğinde Maven ile Google depolarından paketler ekler.

Oluşturulan kodu, önizleme panelindeki **Kod** sekmesini kullanarak görüntüleyebilir ve düzenleyebilirsiniz. Android Studio'da geliştirmeye devam etmek için projeyi **ZIP dosyası** olarak indirin.

## Sınırlamalar

AI Studio'da Android uygulaması oluşturma ile ilgili aşağıdaki sınırlamalar vardır:

### Platform sınırlamaları

- **Yalnızca istemci tarafı**: Android uygulamaları, sunucu tarafı bileşeni içermez.
  Sunucu çalışma zamanı gerektiren özellikler (sır yönetimi, çok oyunculu, Firebase, Google Workspace API'leri) kullanılamaz.
- **Tek etkinlikli mimari**: Yalnızca tek etkinlikli, tek modüllü projeler desteklenir.
- **Yalnızca Jetpack Compose**: Uygulamalar Kotlin ve Jetpack Compose kullanır. Java ve XML düzenleri desteklenmez.
- **NDK veya yerel kod yok**: C ve C++ kodu desteklenmez.
- **Wear OS veya Android TV yok**: Yalnızca telefon ve tablet form faktörleri desteklenir.

### Dışa aktarma sınırlamaları

- **Yalnızca ZIP olarak indirme**: Projeyi ZIP dosyası olarak indirebilirsiniz. GitHub dışa aktarma özelliği, Android projelerinde henüz kullanılamamaktadır.

## Sırada ne var?

- [Google AI Studio'da uygulama geliştirme](https://ai.google.dev/gemini-api/docs/aistudio-build-mode?hl=tr)
- [Tam Yığın Uygulamaları Geliştirme](https://ai.google.dev/gemini-api/docs/aistudio-fullstack?hl=tr) (web)
- [Uygulama Galerisi](https://aistudio.google.com/apps?source=showcase&hl=tr)'ndeki örneklere bakın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-05-19 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-05-19 UTC."],[],[]]
