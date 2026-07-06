---
source_url: https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=tr
fetched_at: 2026-07-06T05:06:55.276872+00:00
title: "Ara\u015ft\u0131rma i\u00e7in Gemini ile ke\u015ffi h\u0131zland\u0131r\u0131n \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)

# Araştırma için Gemini ile keşfi hızlandırın

[Gemini API anahtarı edinme](https://aistudio.google.com/apikey?hl=tr)

Gemini modelleri, çeşitli disiplinlerdeki temel araştırmaları ilerletmek için kullanılabilir.
Araştırmalarınızda Gemini'ı kullanabileceğiniz yöntemler:

- **Model çıkışlarını analiz etme ve kontrol etme**: Daha ayrıntılı analiz için model tarafından oluşturulan bir yanıt adayını `CitationMetadata` gibi araçlarla inceleyebilirsiniz. Ayrıca `responseSchema`, `topP` ve `topK` gibi model oluşturma ve çıkışlarla ilgili seçenekleri de yapılandırabilirsiniz. [Daha fazla bilgi edinin](https://ai.google.dev/api/generate-content?hl=tr).
- **Çok formatlı girişler**: Gemini, görüntüleri, sesleri ve videoları işleyerek heyecan verici birçok araştırma yönü sunar. [Daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/vision?hl=tr).
- **Uzun bağlam özellikleri**: Gemini 3.0 Flash ve Pro, 1 milyon parçalık bağlam penceresiyle birlikte gelir. [Daha fazla bilgi edinin](https://ai.google.dev/gemini-api/docs/long-context?hl=tr).
- **Grow with Google**: Üretim kullanım alanları için API ve Google AI Studio üzerinden Gemini modellerine hızlıca erişin. Google Cloud tabanlı bir platform arıyorsanız Gemini Enterprise Agent Platform ek destekleyici altyapı sağlayabilir.

Google, akademik araştırmaları desteklemek ve çığır açan araştırmalar yapmak için [Gemini Academic Program](https://ai.google.dev/gemini-api/docs/gemini-for-research?hl=tr#gemini-academic-program) aracılığıyla bilim insanlarına ve akademik araştırmacılara Gemini API kredilerine erişim imkanı sunar.

## Gemini'ı kullanmaya başlayın

Gemini API ve Google AI Studio, Google'ın en yeni modelleriyle çalışmaya başlamanıza ve fikirlerinizi ölçeklenebilir uygulamalara dönüştürmenize yardımcı olur.

### Python

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="How large is the universe?",
)

print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.5-flash",
    contents: "How large is the universe?",
  });
  console.log(response.text);
}

await main();
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "How large is the universe?"}]
    }]
   }'
```

## Öne çıkan akademisyenler

![](https://ai.google.dev/static/site-assets/images/diyi-yang.png?hl=tr)

"Araştırmamızda Gemini, görsel dil modeli (VLM) olarak ele alınmakta ve farklı ortamlardaki temsilci davranışları sağlamlık ve güvenlik açısından incelenmektedir. Şimdiye kadar, VLM temsilcileri bilgisayar görevlerini yerine getirirken Gemini'ın pop-up pencereler gibi dikkat dağıtıcı unsurlara karşı ne kadar sağlam olduğunu değerlendirdik ve video girişine dayalı olarak sosyal etkileşimi, zamansal olayları ve risk faktörlerini analiz etmek için Gemini'dan yararlandık."

[Diyi Yang'ın Web Sitesi](https://cs.stanford.edu/~diyiy/)

![](https://ai.google.dev/static/site-assets/images/lerrel-pinto.png?hl=tr)

"Uzun bağlam penceresi sayesinde Gemini Pro ve Flash, açık sözcük dağarcığına sahip mobil manipülasyon projemiz OK-Robot'ta bize yardımcı oluyor. Gemini, robotun "hafızası" üzerinden karmaşık doğal dil sorgularına ve komutlarına olanak tanır. Bu durumda, robotun uzun bir çalışma süresi boyunca yaptığı önceki gözlemler söz konusudur. Mahi Shafiullah ile birlikte, görevleri robotun gerçek dünyada yürütebileceği kodlara ayırmak için de Gemini'ı kullanıyoruz."

[Lerrel Pinto'nun Web Sitesi](https://www.lerrelpinto.com/)

## Gemini Academic Program

[Desteklenen ülkelerdeki](https://ai.google.dev/gemini-api/docs/available-regions?hl=tr) nitelikli akademik araştırmacılar (ör. öğretim üyeleri, personel ve doktora öğrencileri), araştırma projeleri için Gemini API kredileri ve daha yüksek hız sınırları almak üzere başvurabilir. Bu destek, bilimsel deneylerde daha yüksek işleme hızı elde edilmesini ve araştırmaların ilerlemesini sağlar.

Aşağıdaki bölümde yer alan araştırma alanlarıyla özellikle ilgileniyoruz ancak farklı bilimsel disiplinlerden gelen başvuruları da kabul ediyoruz:

- **Değerlendirmeler ve karşılaştırmalar**: Doğruluk, güvenlik, talimatlara uyma, muhakeme ve planlama gibi alanlarda güçlü bir performans sinyali sağlayabilen, topluluk tarafından onaylanmış değerlendirme yöntemleri.
- **İnsanlığın yararına bilimsel keşifleri hızlandırma**: Nadir ve ihmal edilen hastalıklar, deneysel biyoloji, malzeme bilimi ve sürdürülebilirlik gibi alanlar da dahil olmak üzere disiplinler arası bilimsel araştırmalarda yapay zekanın potansiyel uygulamaları.
- **Vücutlandırma ve etkileşimler**: Vücutlandırılmış yapay zeka, ortam etkileşimleri, robotik ve insan-bilgisayar etkileşimi alanlarındaki yeni etkileşimleri araştırmak için büyük dil modellerinden yararlanma.
- **Yeni özellikler**: Akıl yürütme ve planlamayı geliştirmek için gereken yeni aracı özelliklerini ve çıkarım sırasında özelliklerin nasıl genişletilebileceğini (ör. Gemini Flash'i kullanarak) keşfetme.
- **Çok formatlı etkileşim ve anlama**: Çeşitli görevlerde analiz, muhakeme ve planlama için çok formatlı temel modellerdeki eksiklikleri ve fırsatları belirleme.

Uygunluk: Yalnızca geçerli bir akademik kuruma veya akademik araştırma kuruluşuna bağlı kişiler (öğretim üyeleri, araştırmacılar veya benzeri) başvurabilir. API erişiminin ve kredilerin Google'ın takdiri doğrultusunda verileceğini ve kaldırılacağını unutmayın. Başvuruları aylık olarak inceleriz.

### Gemini API ile araştırmaya başlama

[Hemen başvurun](https://forms.gle/HMviQstU8PxC5iCt5)

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-01 UTC.

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-01 UTC."],[],[]]
