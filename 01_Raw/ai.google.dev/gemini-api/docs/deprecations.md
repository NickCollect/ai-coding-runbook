---
source_url: https://ai.google.dev/gemini-api/docs/deprecations?hl=tr
fetched_at: 2026-09-14T05:47:07.278327+00:00
title: "Gemini deste\u011fi sonland\u0131r\u0131lan \u00f6zellikler \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini desteği sonlandırılan özellikler

Bu sayfada, Gemini API'deki [kararlı (GA)](https://ai.google.dev/gemini-api/docs/models?hl=tr#stable) ve [önizleme](https://ai.google.dev/gemini-api/docs/models?hl=tr#preview) modelleri için bilinen desteği sonlandırma planları listelenmektedir. "**Desteğin sonlandırılması**", bir model için artık destek sağlamadığımızı ve modelin yakın gelecekte "**kapatılacağını**" duyurmamızdır. Bir model "**kapatıldığında**" tamamen devre dışı bırakılır ve uç nokta artık kullanılamaz.

Desteği sonlandırma duyuruları [Sürüm notları](https://ai.google.dev/gemini-api/docs/changelog?hl=tr) sayfasında yapılır ve duyurulan en erken kapatma tarihleri bu sayfada takip edilir.
Daha önce kapatılmış modeller gri arka planla gösterilir.

## Gemini 3 modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-3.6-flash` | 21 Temmuz 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3.5-flash-lite` | 21 Temmuz 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3.5-flash` | 19 Mayıs 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3.1-flash-image` | 28 Mayıs 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3-pro-image` | 28 Mayıs 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3.1-flash-lite` | 7 Mayıs 2026 | 7 Mayıs 2027 | `gemini-3.5-flash-lite` |
| Modelleri önizleme | | | |
| `gemini-3.1-flash-image-preview` | 26 Şubat 2026 | 25 Haziran 2026 | `gemini-3.1-flash-image` |
| `gemini-3.1-pro-preview` | 19 Şubat 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-3-pro-image-preview` | 20 Kasım 2025 | 25 Haziran 2026 | `gemini-3-pro-image` |
| `gemini-3-flash-preview` | 17 Aralık 2025 | Kapatma tarihi duyurulmadı | `gemini-3.6-flash` |
| `gemini-3-pro-preview` | 18 Kasım 2025 | 9 Mart 2026 | `gemini-3.1-pro-preview` |
| `gemini-3.1-flash-lite-preview` | 3 Mart 2026 | 25 Mayıs 2026 | `gemini-3.1-flash-lite` |

## Gemini 2.5 Pro modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-2.5-pro` | 17 Haziran 2025 | 16 Ekim 2026 | `gemini-3.1-pro-preview` |
| Modelleri önizleme | | | |
| `gemini-2.5-pro-preview-03-25` | 3 Mart 2025 | 2 Aralık 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-05-06` | 6 Mayıs 2025 | 2 Aralık 2025 | `gemini-3.1-pro-preview` |
| `gemini-2.5-pro-preview-06-05` | 5 Haziran 2025 | 2 Aralık 2025 | `gemini-3.1-pro-preview` |

## Gemini 2.5 Flash modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-2.5-flash` | 17 Haziran 2025 | 16 Ekim 2026 | `gemini-3.6-flash` |
| `gemini-2.5-flash-image` | 2 Ekim 2025 | 2 Ekim 2026 | `gemini-3.1-flash-image-preview` |
| `gemini-2.5-flash-lite` | 22 Temmuz 2025 | 16 Ekim 2026 | `gemini-3.1-flash-lite` |
| Modelleri önizleme | | | |
| `gemini-2.5-flash-lite-preview-09-2025` | 25 Eylül 2025 | 31 Mart 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.5-flash-preview-05-20` | 20 Mayıs 2025 | 18 Kasım 2025 | `gemini-3.6-flash` |
| `gemini-2.5-flash-image-preview` | 7 Mayıs 2025 | 15 Ocak 2026 | `gemini-2.5-flash-image` |
| `gemini-2.5-flash-preview-09-25` | 25 Eylül 2025 | 17 Şubat 2026 | `gemini-3.6-flash` |

## Gemini 2.0 modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-2.0-flash` | 5 Şubat 2025 | 1 Haziran 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-001` | 5 Şubat 2025 | 1 Haziran 2026 | `gemini-3.6-flash` |
| `gemini-2.0-flash-lite` | 25 Şubat 2025 | 1 Haziran 2026 | `gemini-3.1-flash-lite` |
| `gemini-2.0-flash-lite-001` | 25 Şubat 2025 | 1 Haziran 2026 | `gemini-3.1-flash-lite` |
| Modelleri önizleme | | | |
| `gemini-2.0-flash-preview-image-generation` | 7 Mayıs 2025 | 14 Kasım 2025 | `gemini-2.5-flash-image` |
| `gemini-2.0-flash-lite-preview` | 5 Şubat 2025 | 9 Aralık 2025 | `gemini-2.5-flash-lite` |
| `gemini-2.0-flash-lite-preview-02-05` | 5 Şubat 2025 | 9 Aralık 2025 | `gemini-2.5-flash-lite` |

## Live API modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-2.0-flash-live-001` | 9 Nisan 2025 | 9 Aralık 2025 | `gemini-3.1-flash-live-preview` |
| Modelleri önizleme | | | |
| `gemini-3.1-flash-live-preview` | 11 Mart 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-2.5-flash-native-audio-preview-12-2025` | 12 Aralık 2025 | Kapatma tarihi duyurulmadı | `gemini-3.1-flash-live-preview` |
| `gemini-live-2.5-flash-preview` | 17 Haziran 2025 | 9 Aralık 2025 | `gemini-3.1-flash-live-preview` |

## Ses modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| Modelleri önizleme | | | |
| `gemini-3.1-flash-tts-preview` | 13 Nisan 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-2.5-flash-preview-tts` | 20 Mayıs 2025 | Kapatma tarihi duyurulmadı | `gemini-3.1-flash-tts-preview` |
| `gemini-2.5-pro-preview-tts` | 20 Mayıs 2025 | Kapatma tarihi duyurulmadı | `gemini-3.1-flash-tts-preview` |

## Yerleştirme modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `gemini-embedding-2` | 22 Nisan 2026 | Kapatma tarihi duyurulmadı |  |
| `gemini-embedding-001` | 14 Temmuz 2025 | 14 Temmuz 2026 | `gemini-embedding-2` |
| `text-embedding-004` | 9 Nisan 2024 | 14 Ocak 2026 | `gemini-embedding-2` |
| Modelleri önizleme | | | |
| `embedding-2-preview` | 10 Mart 2026 | 10 Ağustos 2026 | `gemini-embedding-2` |
| `embedding-001` | 9 Nisan 2024 | 30 Ekim 2025 | `gemini-embedding-2` |
| `embedding-gecko-001` |  | 30 Ekim 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp` |  | 30 Ekim 2025 | `gemini-embedding-2` |
| `gemini-embedding-exp-03-07` |  | 30 Ekim 2025 | `gemini-embedding-2` |

## Imagen modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `imagen-4.0-generate-001` | 24 Haziran 2025 | 17 Ağustos 2026 | `gemini-3.1-flash-image` |
| `imagen-4.0-ultra-generate-001` | 24 Haziran 2025 | 17 Ağustos 2026 | `gemini-3.1-flash-image` |
| `imagen-4.0-fast-generate-001` | 24 Haziran 2025 | 17 Ağustos 2026 | `gemini-3.1-flash-image` |
| `imagen-3.0-generate-002` | 6 Şubat 2025 | 10 Kasım 2025 | `imagen-4.0-generate-001` |
| Modelleri önizleme | | | |
| `imagen-4.0-generate-preview-06-06` | 24 Haziran 2025 | 17 Şubat 2026 | `imagen-4.0-generate-001` |
| `imagen-4.0-ultra-generate-preview-06-06` | 24 Haziran 2025 | 17 Şubat 2026 | `imagen-4.0-ultra-generate-001` |

## Veo modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `veo-3.0-generate-001` | 9 Eylül 2025 | 30 Haziran 2026 | `veo-3.1-generate-preview` veya [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=tr)'daki GA modelleri |
| `veo-3.0-fast-generate-001` | 9 Eylül 2025 | 30 Haziran 2026 | `veo-3.1-fast-generate-preview` veya [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=tr)'daki GA modelleri |
| `veo-2.0-generate-001` | 9 Nisan 2025 | 30 Haziran 2026 | `veo-3.1-generate-preview` veya [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate?hl=tr)'daki GA modelleri |
| Modelleri önizleme | | | |
| `veo-3.1-lite-generate-preview` | 31 Mart 2026 | Kapatma tarihi duyurulmadı |  |
| `veo-3.1-generate-preview` | 15 Ekim 2025 | Kapatma tarihi duyurulmadı |  |
| `veo-3.1-fast-generate-preview` | 15 Ekim 2025 | Kapatma tarihi duyurulmadı |  |
| `veo-3.0-generate-preview` | 31 Temmuz 2025 | 12 Kasım 2025 | `veo-3.1-generate-preview` |
| `veo-3.0-fast-generate-preview` | 31 Temmuz 2025 | 12 Kasım 2025 | `veo-3.1-fast-generate-preview` |

## Lyria modelleri

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| `lyria-3-clip-preview` | 25 Mart 2026 | Kapatma tarihi duyurulmadı |  |
| `lyria-3-pro-preview` | 25 Mart 2026 | Kapatma tarihi duyurulmadı |  |
| `lyria-realtime-exp` | 20 Mayıs 2025 | Kapatma tarihi duyurulmadı |  |

## Robotik modeller

| **Model** | **Yayınlanma tarihi** | **Kapatma tarihi** | **Önerilen değiştirme** |
| --- | --- | --- | --- |
| Modelleri önizleme | | | |
| `gemini-robotics-er-1.6-preview` | 14 Nisan 2026 | Kapanış tarihi duyurulmadı |  |
| `gemini-robotics-er-1.5-preview` | 25 Eylül 2025 | 30 Nisan 2026 | `gemini-robotics-er-1.6-preview` |

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-12 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-12 UTC."],[],[]]
