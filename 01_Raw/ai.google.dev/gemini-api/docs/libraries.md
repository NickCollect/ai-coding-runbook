---
source_url: https://ai.google.dev/gemini-api/docs/libraries?hl=tr
fetched_at: 2026-08-31T06:32:18.303279+00:00
title: "Gemini API kitapl\u0131klar\u0131 \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API kitaplıkları

Gemini API ile geliştirme yaparken **Google GenAI SDK**'yı kullanmanızı öneririz.
Bunlar, en popüler diller için geliştirdiğimiz ve bakımını yaptığımız resmi, üretime hazır kitaplıklardır. Bu işlevler [genel kullanıma](https://ai.google.dev/gemini-api/docs/libraries?hl=tr#new-libraries) sunulmuştur ve tüm resmi belgelerimizde ve örneklerimizde kullanılmaktadır.

Gemini API'yi kullanmaya yeni başladıysanız [Başlangıç kılavuzumuzu](https://ai.google.dev/gemini-api/docs/get-started?hl=tr) inceleyerek başlayın.

## Dil desteği ve yükleme

Google GenAI SDK; Python, JavaScript/TypeScript, Go ve Java dillerinde kullanılabilir. Her dilin kitaplığını paket yöneticilerini kullanarak yükleyebilir veya daha fazla bilgi için GitHub depolarını ziyaret edebilirsiniz:

### Python

- Kitaplık: [`google-genai`](https://pypi.org/project/google-genai)
- GitHub deposu: [googleapis/python-genai](https://github.com/googleapis/python-genai)
- Yükleme: `pip install google-genai`

### JavaScript

- Kitaplık: [`@google/genai`](https://www.npmjs.com/package/@google/genai)
- GitHub deposu: [googleapis/js-genai](https://github.com/googleapis/js-genai)
- Yükleme: `npm install @google/genai`

### Go

- Kitaplık: [`google.golang.org/genai`](https://pkg.go.dev/google.golang.org/genai)
- GitHub deposu: [googleapis/go-genai](https://github.com/googleapis/go-genai)
- Yükleme: `go get google.golang.org/genai`

### Java

- Kitaplık: `google-genai`
- GitHub deposu: [googleapis/java-genai](https://github.com/googleapis/java-genai)
- Yükleme: Maven kullanıyorsanız bağımlılıklarınıza aşağıdakileri ekleyin:

```
<dependencies>
  <dependency>
    <groupId>com.google.genai</groupId>
    <artifactId>google-genai</artifactId>
    <version>1.0.0</version>
  </dependency>
</dependencies>
```

### C#

- Kitaplık: `Google.GenAI`
- GitHub deposu: [googleapis/dotnet-genai](https://googleapis.github.io/dotnet-genai/)
- Yükleme: `dotnet add package Google.GenAI`

## Genel kullanıma sunulma

Google GenAI SDK, Mayıs 2025 itibarıyla tüm desteklenen platformlarda genel kullanıma sunuldu ve Gemini API'ye erişmek için önerilen kitaplıklar oldu.
Kararlıdırlar, üretim amaçlı kullanım için tam olarak desteklenirler ve aktif olarak bakımları yapılır.
Bu planlar, en yeni özelliklere erişim sağlar ve Gemini ile çalışırken en iyi performansı sunar.

Eski kitaplıklarımızdan birini kullanıyorsanız en yeni özelliklere erişebilmek ve Gemini ile çalışırken en iyi performansı elde edebilmek için geçiş yapmanızı önemle tavsiye ederiz. Daha fazla bilgi için [eski kitaplıklar](https://ai.google.dev/gemini-api/docs/libraries?hl=tr#previous-sdks) bölümünü inceleyin.

## Eski kitaplıklar ve taşıma

Eski kitaplıklarımızdan birini kullanıyorsanız [yeni kitaplıklara geçmenizi](https://ai.google.dev/gemini-api/docs/migrate?hl=tr) öneririz.

Eski kitaplıklar, son özelliklere (ör. [Live API](https://ai.google.dev/gemini-api/docs/live?hl=tr) ve [Veo](https://ai.google.dev/gemini-api/docs/video?hl=tr)) erişim sağlamaz ve 30 Kasım 2025'ten itibaren kullanımdan kaldırılır.

Her eski kitaplığın destek durumu farklıdır. Ayrıntılı bilgi için aşağıdaki tabloya bakın:

| Dil | Eski kitaplık | Destek durumu | Önerilen kitaplık |
| --- | --- | --- | --- |
| **Python** | `google-generativeai` | Aktif olarak sürdürülmüyor | `google-genai` |
| **JavaScript/TypeScript** | `@google/generativeai` | Aktif olarak sürdürülmüyor | `@google/genai` |
| **Go** | `google.golang.org/generative-ai` | Aktif olarak sürdürülmüyor | `google.golang.org/genai` |
| **Dart ve Flutter** | `google_generative_ai` | Aktif olarak sürdürülmüyor | [Genkit Dart](https://genkit.dev/docs/dart/get-started/) veya [Firebase AI Logic](https://pub.dev/packages/firebase_ai)'i kullanın. |
| **Swift** | `generative-ai-swift` | Aktif olarak sürdürülmüyor | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=tr)'i kullanma |
| **Android** | `generative-ai-android` | Aktif olarak sürdürülmüyor | [Firebase AI Logic](https://firebase.google.com/products/firebase-ai-logic?hl=tr)'i kullanma |

**Java geliştiricileri için not:** Gemini API için Google tarafından sağlanan eski bir Java SDK'sı olmadığından önceki bir Google kitaplığından geçiş yapılması gerekmez. Doğrudan [Dil desteği ve yükleme](#install) bölümündeki yeni kitaplıkla başlayabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-22 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-22 UTC."],[],[]]
