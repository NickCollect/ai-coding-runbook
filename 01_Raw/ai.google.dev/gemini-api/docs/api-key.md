---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=tr
fetched_at: 2026-05-05T19:45:39.623618+00:00
title: "Gemini API anahtarlar\u0131n\u0131 kullanma \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=tr) artık işbirlikçi planlama, görselleştirme, MCP desteği ve daha fazlasıyla önizleme sürümünde kullanılabilir.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API anahtarlarını kullanma

Gemini API'yi kullanmak için API anahtarı gerekir. Bu sayfada, Google AI Studio'da anahtarlarınızı nasıl oluşturup yöneteceğiniz ve bunları kodunuzda kullanmak için ortamınızı nasıl ayarlayacağınız açıklanmaktadır.

[Gemini API anahtarı oluşturma veya görüntüleme](https://aistudio.google.com/app/apikey?hl=tr)

## API Anahtarları

Tüm Gemini API anahtarlarınızı [Google AI Studio](https://aistudio.google.com/app/apikey?hl=tr) **API anahtarları** sayfasından oluşturup yönetebilirsiniz.

API anahtarınız olduğunda Gemini API'ye bağlanmak için aşağıdaki seçenekleri kullanabilirsiniz:

- [API anahtarınızı ortam değişkeni olarak ayarlama](#set-api-env-var)
- [API anahtarınızı açıkça sağlama](#provide-api-key-explicitly)

İlk test için bir API anahtarını sabit kodlayabilirsiniz ancak bu işlem güvenli olmadığından yalnızca geçici olarak yapılmalıdır. API anahtarını sabit kodlamayla ilgili örnekleri [API anahtarını açıkça sağlama](#provide-api-key-explicitly) bölümünde bulabilirsiniz.

## Google Cloud projeleri

[Google Cloud projeleri](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=tr), Google Cloud hizmetlerini (ör. Gemini API) kullanmak, faturalandırmayı yönetmek ve ortak çalışanları ve izinleri kontrol etmek için temel öneme sahiptir. Google AI Studio, Google Cloud projelerinize yönelik basit bir arayüz sunar.

Henüz proje oluşturmadıysanız yeni bir proje oluşturmanız veya Google Cloud'dan Google AI Studio'ya bir proje aktarmanız gerekir. Google AI Studio'daki **Projeler** sayfasında, Gemini API'yi kullanmak için yeterli izne sahip tüm anahtarlar gösterilir. Talimatlar için [projeleri içe aktarma](#import-projects) bölümüne bakın.

### Varsayılan proje

Yeni kullanıcılar için Google AI Studio, Hizmet Şartları'nı kabul ettikten sonra kullanım kolaylığı sağlamak amacıyla varsayılan bir Google Cloud projesi ve API anahtarı oluşturur. Bu projeyi Google AI Studio'da yeniden adlandırmak için **Kontrol paneli**'ndeki **Projeler** görünümüne gidin, bir projenin yanındaki 3 nokta ayarlar düğmesini tıklayın ve **Projeyi yeniden adlandır**'ı seçin. Mevcut kullanıcılar veya Google Cloud hesapları olan kullanıcılar için varsayılan proje oluşturulmaz.

## Projeleri içe aktarma

Her Gemini API anahtarı bir Google Cloud projesiyle ilişkilendirilir. Varsayılan olarak Google AI Studio, Cloud projelerinizin tümünü göstermez. **Projeleri İçe Aktar** iletişim kutusunda adı veya proje kimliğini arayarak istediğiniz projeleri içe aktarmanız gerekir. Erişiminiz olan projelerin tam listesini görüntülemek için Cloud Console'u ziyaret edin.

Henüz içe aktarılmış projeniz yoksa Google Cloud projesi içe aktarmak ve anahtar oluşturmak için aşağıdaki adımları uygulayın:

1. [Google AI Studio](https://aistudio.google.com?hl=tr)'ya gidin.
2. Soldaki yan panelden **Kontrol Paneli**'ni açın.
3. **Projeler**'i seçin.
4. **Projeler** sayfasında **Projeleri içe aktar** düğmesini seçin.
5. İçe aktarmak istediğiniz Google Cloud projesini arayıp seçin ve **İçe aktar** düğmesini tıklayın.

Bir proje içe aktarıldıktan sonra **Kontrol Paneli** menüsünden **API Anahtarları** sayfasına gidin ve yeni içe aktardığınız projede bir API anahtarı oluşturun.

## Sınırlamalar

Google AI Studio'da API anahtarlarını ve Google Cloud projelerini yönetmeyle ilgili sınırlamalar aşağıda verilmiştir.

- Google AI Studio **Projeler** sayfasında tek seferde en fazla 10 proje oluşturabilirsiniz.
- Projeleri ve anahtarları adlandırabilir, yeniden adlandırabilirsiniz.
- **API anahtarları** ve **Projeler** sayfalarında en fazla 100 anahtar ve 50 proje gösterilir.
- Yalnızca kısıtlaması olmayan veya Generative Language API ile kısıtlanmış API anahtarları gösterilir.

API anahtarlarını değiştirme ve kısıtlama dahil olmak üzere projelerinize ek yönetim erişimi için [Google Cloud Console kimlik bilgileri sayfasını](https://console.cloud.google.com/apis/credentials?hl=tr) ziyaret edin.
Cloud Console'da projenizi seçebilir, mevcut bir API anahtarını tıklayabilir ve ardından bu anahtarı **Generative Language API** ile sınırlayabilirsiniz.

## API anahtarını ortam değişkeni olarak ayarlama

`GEMINI_API_KEY` veya `GOOGLE_API_KEY` ortam değişkenini ayarlarsanız [Gemini API kitaplıklarından](https://ai.google.dev/gemini-api/docs/libraries?hl=tr) biri kullanılırken API anahtarı istemci tarafından otomatik olarak alınır. Bu değişkenlerden yalnızca birini ayarlamanız önerilir. Ancak her ikisi de ayarlanırsa `GOOGLE_API_KEY` öncelikli olur.

REST API'yi veya tarayıcıda JavaScript'i kullanıyorsanız API anahtarını açıkça sağlamanız gerekir.

API anahtarınızı farklı işletim sistemlerinde ortam değişkeni olarak yerel olarak nasıl ayarlayabileceğinizi aşağıda bulabilirsiniz.
`GEMINI_API_KEY`

### Linux/macOS - Bash

Bash, yaygın bir Linux ve macOS terminal yapılandırmasıdır. Aşağıdaki komutu çalıştırarak yapılandırma dosyanızın olup olmadığını kontrol edebilirsiniz:

```
~/.bashrc
```

Yanıt "No such file or directory" (Böyle bir dosya veya dizin yok) ise bu dosyayı oluşturmanız ve aşağıdaki komutları çalıştırarak açmanız ya da `zsh` kullanmanız gerekir:

```
touch ~/.bashrc
open ~/.bashrc
```

Ardından, aşağıdaki dışa aktarma komutunu ekleyerek API anahtarınızı ayarlamanız gerekir:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dosyayı kaydettikten sonra aşağıdaki komutu çalıştırarak değişiklikleri uygulayın:

```
source ~/.bashrc
```

### macOS - Zsh

Zsh, yaygın bir Linux ve macOS terminal yapılandırmasıdır. Aşağıdaki komutu çalıştırarak yapılandırma dosyanızın olup olmadığını kontrol edebilirsiniz:

```
~/.zshrc
```

Yanıt "No such file or directory" (Böyle bir dosya veya dizin yok) ise bu dosyayı oluşturmanız ve aşağıdaki komutları çalıştırarak açmanız ya da `bash` kullanmanız gerekir:

```
touch ~/.zshrc
open ~/.zshrc
```

Ardından, aşağıdaki dışa aktarma komutunu ekleyerek API anahtarınızı ayarlamanız gerekir:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dosyayı kaydettikten sonra aşağıdaki komutu çalıştırarak değişiklikleri uygulayın:

```
source ~/.zshrc
```

### Windows

1. Arama çubuğunda "Ortam Değişkenleri"ni arayın.
2. **Sistem Ayarları**'nı değiştirmeyi seçin. Bu işlemi yapmak istediğinizi onaylamanız gerekebilir.
3. Sistem ayarları iletişim kutusunda **Ortam
   Değişkenleri** etiketli düğmeyi tıklayın.
4. **Kullanıcı değişkenleri** (mevcut kullanıcı için) veya **Sistem değişkenleri** (makineyi kullanan tüm kullanıcılar için geçerlidir) altında **Yeni...** seçeneğini tıklayın.
5. Değişken adını `GEMINI_API_KEY` olarak belirtin. Değişken değeri olarak Gemini API anahtarınızı belirtin.
6. Değişiklikleri uygulamak için **Tamam**'ı tıklayın.
7. Yeni değişkeni almak için yeni bir terminal oturumu (cmd veya Powershell) açın.

## API anahtarını açıkça sağlama

Bazı durumlarda, API anahtarını açıkça sağlamak isteyebilirsiniz. Örneğin:

- Basit bir API çağrısı yapıyorsunuz ve API anahtarını sabit kodlamayı tercih ediyorsunuz.
- Gemini API kitaplıklarının ortam değişkenlerini otomatik olarak keşfetmesine güvenmek zorunda kalmadan açık kontrol istiyorsanız
- Ortam değişkenlerinin desteklenmediği bir ortamda (ör.web) kullanıyorsunuz veya REST çağrıları yapıyorsunuz.

Aşağıda, API anahtarını açıkça nasıl sağlayabileceğinize dair örnekler verilmiştir:

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain how AI works in a few words",
  });
  console.log(response.text);
}

main();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey:  "YOUR_API_KEY",
        Backend: genai.BackendGeminiAPI,
    })
    if err != nil {
        log.Fatal(err)
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-3-flash-preview",
        genai.Text("Explain how AI works in a few words"),
        nil,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}
```

### Java

```
package com.example;

import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().apiKey("YOUR_API_KEY").build();

    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## API anahtarınızın güvenliğini sağlama

Gemini API anahtarınızı şifre gibi kullanın. Tehlikeye girerse diğer kullanıcılar projenizin kotasını kullanabilir, ücret ödemenize neden olabilir (faturalandırma etkinse) ve dosyalar gibi özel verilerinize erişebilir.

### Önemli güvenlik kuralları

- **Anahtarları gizli tutun**: Gemini'ın API anahtarları, uygulamanızın kullandığı hassas verilere erişebilir.

  - **API anahtarlarını hiçbir zaman kaynak denetimine işlemeyin.** API anahtarınızı Git gibi sürüm denetim sistemlerine işlemeyin.
  - **API anahtarlarını hiçbir zaman istemci tarafında kullanmayın.** API anahtarınızı üretimdeki web veya mobil uygulamalarda doğrudan kullanmayın. İstemci tarafı kodundaki anahtarlar (JavaScript/TypeScript kitaplıklarımız ve REST çağrıları dahil) ayıklanabilir.
- **Erişimi kısıtlama**: Mümkün olduğunda API anahtarı kullanımını belirli IP adresleri, HTTP yönlendirenleri veya Android/iOS uygulamalarıyla kısıtlayın.
- **Kullanımı kısıtlama**: Her anahtar için yalnızca gerekli API'leri etkinleştirin.
- **Düzenli denetimler yapın**: API anahtarlarınızı düzenli olarak denetleyin ve belirli aralıklarla döndürün.

### En iyi uygulamalar

- **API anahtarlarıyla sunucu tarafı çağrıları kullanma** API anahtarınızı kullanmanın en güvenli yolu, anahtarın gizli tutulabileceği bir sunucu tarafı uygulamasından Gemini API'yi çağırmaktır.
- **İstemci tarafı erişimi için kısa ömürlü jetonları kullanma (yalnızca Live API):** Live API'ye doğrudan istemci tarafı erişimi için kısa ömürlü jetonları kullanabilirsiniz. Daha düşük güvenlik riskleri içerir ve üretimde kullanıma uygun olabilir. Daha fazla bilgi için [geçici jetonlar](https://ai.google.dev/gemini-api/docs/ephemeral-tokens?hl=tr) kılavuzunu inceleyin.
- **Anahtarınıza kısıtlamalar eklemeyi düşünün:** [API anahtarı kısıtlamaları](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys?hl=tr#add-api-restrictions) ekleyerek anahtarın izinlerini sınırlayabilirsiniz.
  Bu, anahtarın sızdırılması durumunda olası zararı en aza indirir.

Genel en iyi uygulamalar için bu [destek makalesini](https://support.google.com/googleapi/answer/6310037?hl=tr) de inceleyebilirsiniz.

## API anahtarı oluşturma sorunlarını giderme

Google AI Studio'da **API anahtarı oluştur** düğmesi kullanılamıyor görünebilir ve "*Bu projede anahtar oluşturma izniniz yok*" mesajı gösterilebilir.

Bu durum, yeni bir anahtar oluşturmak için projede gerekli izinlere sahip olmadığınızda ortaya çıkar:

- **`resourcemanager.projects.get`**: AI Studio'nun projenin varlığını doğrulamasına olanak tanır.
- **`apikeys.keys.create`**: API anahtarının oluşturulmasına olanak tanır.
- **`serviceusage.services.enable`**: Gemini API'nin projede etkin olmasını sağlamak için gereklidir.

İzinlerinizi düzeltmek için proje yöneticinizden veya proje bir [kuruluşa](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access?hl=tr) aitse kuruluşunuzun yöneticisinden yukarıda listelenen izinlere sahip bir rol (ör. Proje Düzenleyici veya özel rol) vermesini isteyin.

Bir projeye yönetim erişiminiz yoksa anahtarlarınızı oluşturmak için bir kuruluşla ilişkilendirilmemiş yeni bir proje oluşturabilirsiniz.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-04-29 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-04-29 UTC."],[],[]]
