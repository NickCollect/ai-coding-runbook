---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/api-key?hl=tr
fetched_at: 2026-09-28T06:12:21.052714+00:00
title: "Gemini API anahtarlar\u0131n\u0131 kullanma \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs/generate-content?hl=tr)

Geri bildirim gönderin

# Gemini API anahtarlarını kullanma

Gemini API'yi kullanmak için isteklerinizin kimliğini doğrulamanız gerekir. Standart veya yetkilendirme API anahtarı kullanarak kimliğinizi doğrulayabilirsiniz.

[Gemini API anahtarı oluşturma veya görüntüleme](https://aistudio.google.com/apikey?hl=tr)

## API anahtarı türleri: standart ve yetkilendirme

API anahtarları, Gemini API'ye erişim sağlar ancak güvenlik özellikleri farklıdır. Gemini API, güvenliği artırmak için standart API anahtarlarından yetkilendirme anahtarlarına geçiş yapıyor:

- **Standart API anahtarları**: Faturalandırma ve kota amacıyla istekleri bir Google Cloud projesiyle ilişkilendirin. Standart anahtarlar arayanı tanımlamadığından destekleyebilecekleri izinlerin ve erişim denetiminin ayrıntı düzeyi sınırlıdır.
- **Yetkilendirme (auth) anahtarları**: Doğrudan bir Google Cloud hizmet hesabına bağlıdır. Yetkilendirme anahtarı kullandığınızda istekleriniz, bu bağlı hizmet hesabının kimliği altında işlenir ve ayrıntılı erişim kontrolü sağlanır. Yetkilendirme anahtarları varsayılan olarak Generative Language API (Gemini API) ile sınırlıdır ve sistemlerimiz tarafından algılanan sızdırılmış anahtarların kullanımını hızlı bir şekilde durduran, hızlı etkili sızdırılmış anahtar zorunluluğu sağlar.

Gemini API, güvenli kullanımı sağlamak için standart anahtarlardan kimlik doğrulama anahtarlarına geçiş yapacak:

- **Varsayılan kimlik doğrulama anahtarları**: 28 Mayıs 2026'dan itibaren Google AI Studio'da oluşturulan tüm yeni API anahtarları otomatik olarak kimlik doğrulama anahtarı olarak oluşturulacak.
- **Kısıtlanmamış anahtarlar reddedildi**: Gemini API, **kısıtlanmamış standart anahtarlardan** gelen istekleri reddeder. Açık kısıtlamalar uygulanmış standart API anahtarları çalışmaya devam eder. Bu kısıtlama, herkese açık olarak paylaşılan veya diğer hizmetlere bağlanan anahtarların yetkisiz kullanımını engeller.

## Google AI Studio'da API anahtarlarını yönetme

Projelerinizi ve anahtarlarınızı doğrudan [Google AI Studio](https://aistudio.google.com/apikey?hl=tr)'da yönetebilirsiniz.

### Google Cloud projeleri

Her Gemini API anahtarı bir [Google Cloud projesiyle](https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=tr) ilişkilendirilir.
Google Cloud projeleri faturalandırmayı, ortak çalışanları ve izinleri yönetir. Google AI Studio, bu projelere erişmek için basit bir arayüz sunar.

- **Varsayılan proje**: Yeni bir kullanıcıysanız Google AI Studio, Hizmet Şartları'nı kabul ettikten sonra otomatik olarak varsayılan bir Google Cloud projesi ve API anahtarı oluşturur. Kontrol panelinizdeki **Projeler** görünümüne giderek bu projeyi yeniden adlandırabilirsiniz.
- **Mevcut projeler**: Google Cloud hesabınız varsa AI Studio varsayılan bir proje oluşturmaz. Bunun yerine mevcut projelerinizi içe aktarmanız gerekir.

### Projeleri içe aktarma

Google AI Studio, varsayılan olarak Google Cloud projelerinizin tümünü göstermez. Kullanmak istediğiniz projeleri içe aktarmanız gerekir:

1. [Google AI Studio](https://aistudio.google.com?hl=tr)'ya gidin.
2. Soldaki panelden **Kontrol Paneli**'ni açın ve **Projeler**'i seçin.
3. **Projeleri içe aktar** düğmesini tıklayın.
4. İçe aktarmak istediğiniz Google Cloud projesini arayıp seçin ve **İçe aktar**'ı tıklayın.
5. İçe aktarıldıktan sonra, kontrol panelindeki **API Anahtarları** sayfasına giderek bu projede anahtar oluşturun.

### Anahtar oluşturma izinleriyle ilgili sorunları giderme

**API anahtarı oluştur** düğmesi kullanılamıyorsa ve şu mesajı gösteriyorsa:
*"Bu projede anahtar oluşturma izniniz yok"*, gerekli IAM izinlerine sahip değilsiniz demektir.

Google Cloud projenizin veya kuruluşunuzun yöneticisinden size aşağıdaki izinleri içeren bir rol (ör. Proje Düzenleyici) vermesini isteyin:

- `resourcemanager.projects.get`: AI Studio'nun projeyi doğrulamasını sağlar.
- `apikeys.keys.create`: Anahtar oluşturmaya izin verir.
- `serviceusage.services.enable`: Generative Language API'nin etkinleştirilmesini sağlar.
- `iam.serviceAccounts.create`: Bağlı hizmet hesabını oluşturmak için gereklidir.
- `iam.serviceAccountApiKeyBindings.create`: Hizmet hesabını API anahtarına bağlar.

Yönetici erişimi alamıyorsanız anahtarlarınızı oluşturmak için bir kuruluşla ilişkili olmayan yeni bir Google Cloud projesi oluşturabilirsiniz.

## Ortamınızı kurma

Anahtarınız olduğunda ortamınızı, uygulamalarınızda güvenli bir şekilde kullanacak şekilde yapılandırın.

### Ortam değişkenlerini kullanın (önerilir)

`GEMINI_API_KEY` veya `GOOGLE_API_KEY` ortam değişkenini ayarlayın. Gemini API istemci kitaplıkları bu değişkenleri otomatik olarak algılar ve kullanır. Her ikisi de ayarlanmışsa `GOOGLE_API_KEY` öncelikli olur.

Değişkeni ayarlamak için işletim sisteminizi seçin:

### Linux/macOS - Bash

Bir bash yapılandırma dosyanızın olup olmadığını doğrulayın:

```
~/.bashrc
```

Yoksa bir tane oluşturup açın:

```
touch ~/.bashrc && open ~/.bashrc
```

Dosyanın sonuna dışa aktarma komutunu ekleyin:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dosyayı kaydedin ve değişiklikleri uygulayın:

```
source ~/.bashrc
```

### macOS - Zsh

zsh yapılandırma dosyanızın olup olmadığını doğrulayın:

```
~/.zshrc
```

Yoksa bir tane oluşturup açın:

```
touch ~/.zshrc && open ~/.zshrc
```

Dışa aktarma komutunu ekleyin:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

Dosyayı kaydedin ve değişiklikleri uygulayın:

```
source ~/.zshrc
```

### Windows

1. Windows arama çubuğunda "Environment Variables" (Ortam Değişkenleri) ifadesini arayın.
2. Sistem Özellikleri iletişim kutusunda **Ortam Değişkenleri**'ni tıklayın.
3. **Kullanıcı değişkenleri** veya **Sistem değişkenleri** altında **Yeni...** seçeneğini tıklayın.
4. Değişken adını `GEMINI_API_KEY`, değeri ise API anahtarınız olarak ayarlayın.
5. Kaydetmek için **Tamam**'ı tıklayın. Değişkeni yüklemek için yeni bir terminal oturumu açın.

### API anahtarını kodda açıkça belirtme

İstemciyi başlatırken API anahtarını açıkça iletebilirsiniz. Bu işlemi yalnızca ortam değişkenlerini kullanamıyorsanız yapın.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain how AI works in a few words"
)
print(response.text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-3.8-flash",
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
        "gemini-3.8-flash",
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
            "gemini-3.8-flash",
            "Explain how AI works in a few words",
            null);

    System.out.println(response.text());
  }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"       -H 'Content-Type: application/json'       -H "x-goog-api-key: YOUR_API_KEY"       -X POST       -d '{
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

## Güvenlik ve sır yönetimi

Gemini API anahtarınızı şifre gibi kullanın. Tehlikeye girerse diğer kullanıcılar projenizin kotasını kullanabilir, beklenmedik faturalandırma ücretlerine neden olabilir ve özel kaynaklara erişebilir.

### Önemli güvenlik kuralları

- **Anahtarları gizli tutun**: API anahtarlarını asla Git gibi kaynak kontrol sistemlerine işlemeyin.
- **Üretimde anahtarları asla istemci tarafında kullanmayın**: API anahtarlarını doğrudan web veya mobil uygulamalara sabit kodlamayın. İstemci tarafı kodunda derlenen anahtarlar kullanıcılar tarafından çıkarılabilir. İstemci tarafı uygulamaları güvenli hale getirmek için gerçek API çağrılarını yapmak üzere bir arka uç proxy sunucusu çalıştırın.

### Gizli veri yönetimiyle ilgili en iyi uygulamalar

- **Ortam değişkenleri**: Anahtarları yapılandırma dosyaları yerine ortam değişkenlerinden okuyun.
- **Secret Manager**: Üretim için anahtarlarınızı [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=tr) gibi güvenli bir gizli anahtar deposunda saklayın.
- **Faturalandırma uyarıları**: Kullanım veya maliyetlerde artış olması durumunda sizi bilgilendirmek için Google Cloud Console'da faturalandırma uyarıları ayarlayın.

### Sızıntı yanıtı kontrol listesi

API anahtarınızın sızdırıldığından şüpheleniyorsanız:

1. **Yeni bir anahtar oluşturun**: Google AI Studio veya Cloud Console'da yedek bir anahtar oluşturun.
2. **Uygulamanızı güncelleyin**: Kodunuzu yeni anahtarı kullanarak dağıtın.
3. **Güvenliği ihlal edilmiş anahtarı devre dışı bırakma veya silme**: Yeni anahtar doğrulandıktan sonra Cloud Console'da sızdırılmış anahtarı devre dışı bırakın. Uygulama kapalı kalma süresini önlemek için yeni anahtar tamamen etkinleşene kadar eski anahtarı silmeyin.
4. **Kullanımı denetleme**: Yetkisiz etkinliği belirlemek için Google Cloud Console'da faturalandırma günlüklerini ve API kullanımını kontrol edin.

## Anahtarlarınızı kısıtlama ve güvenliğini sağlama

API anahtarlarınıza kısıtlamalar eklemek, bir anahtarın güvenliği ihlal edilirse oluşabilecek olası zararı en aza indirir.

### İstek kaynağı kısıtlamaları uygulama

Kaynak kısıtlamaları, anahtarınızı kullanabilecek IP adreslerini, web sitelerini veya uygulamaları sınırlar.

1. [Google Cloud Console Kimlik Bilgileri sayfasına](https://console.cloud.google.com/apis/credentials?hl=tr) gidin.
2. Projenizi seçin ve kısıtlamak istediğiniz API anahtarının adını tıklayın.
3. **Uygulama kısıtlamaları** bölümünde **IP adresleri**'ni (veya ortamınız için uygun kısıtlama türünü) seçin.
4. İzin verilen IP adreslerini veya aralıklarını belirtin, ardından **Kaydet**'i tıklayın.

### Sınırsız standart API anahtarlarının güvenliğini sağlama

Gemini API'yi kullanmaya devam etmek için tüm sınırsız anahtarları güvenli hale getirmeniz gerekir.

#### Anahtarı yalnızca AI Studio üzerinden Gemini API ile kısıtlama

Anahtarı yalnızca Gemini API için kullanıyorsanız doğrudan AI Studio'da güvenli hale getirin:

1. [Google AI Studio](https://aistudio.google.com/api-keys?hl=tr)'daki **API Anahtarları** sayfasında, **Sınırsız** etiketiyle işaretlenmiş anahtarları bulun.
2. İmleci etiketin üzerine getirip iletişim kutusunda **Kısıtlama ekle**'yi tıklayın.
3. **Yalnızca Gemini API ile kısıtla**'yı seçin.
4. Onaylamak için **Anahtarı kısıtla**'yı tıklayın.

#### Google Cloud Console üzerinden anahtarı diğer hizmetler için kısıtlama

Anahtar diğer Google API'leriyle paylaşılıyorsa (önerilmez) Cloud Console'da kısıtlayın. **Not: Bu anahtarı kullanan Gemini API istekleri, bu kısıtlamalar uygulandıktan sonra başarısız olur.**

1. [Google Cloud Console Kimlik Bilgileri sayfasını](https://console.cloud.google.com/apis/credentials?hl=tr) ziyaret edin.
2. Projeyi ve API anahtarını seçin.
3. **API kısıtlamaları** bölümünde **Anahtarı kısıtla**'yı seçin.
4. Açılır listeden, bu anahtarın erişmesini istediğiniz API'leri seçin. **Generative Language API**'yi seçmeyin.
5. **Kaydet**'i tıklayın. Gemini API'yi kullanmaya devam etmek için AI Studio'da ayrı ve kısıtlanmış bir anahtar oluşturun.

### Etkin olmayan engellenmiş anahtarlar

7 Mayıs 2026'dan itibaren Gemini API, uzun süredir kullanılmayan sınırsız API anahtarlarını engeller. Bu anahtarlar, AI Studio'da **Engellendi** etiketini gösterir. Devam etmek için yeni bir anahtar oluşturmanız veya mevcut bir kısıtlanmış anahtarı kullanmanız gerekir.

## Kimlik doğrulama anahtarına geçiş yapma

Yeni bir kimlik doğrulama API anahtarı oluşturmak ve uygulamalarınızı güncellemek için aşağıdaki adımları uygulayın:

1. [AI Studio API anahtarları sayfasına](https://aistudio.google.com/api-keys?hl=tr) gidin.
2. **Standart** olarak listelenen anahtarları belirlemek için **Anahtar Türü** sütununu kontrol edin.
3. Yeni bir anahtar oluşturmak için **API anahtarı oluştur**'u tıklayın. AI Studio'da oluşturulan tüm yeni anahtarlar otomatik olarak kimlik doğrulama anahtarı olarak oluşturulur.
4. Yeni kimlik doğrulama API anahtarını kopyalayın.
5. Uygulama kodunuzu, ortam değişkenlerinizi ve tüm dağıtım yapılandırmalarınızı yeni kimlik doğrulama API anahtarını kullanacak şekilde güncelleyin.
6. Uygulamanızı test ederek yeni anahtarla doğru şekilde çalıştığını doğrulayın.
7. Doğrulama işlemi tamamlandıktan sonra kötüye kullanımı önlemek için eski trafik anahtarınızı silin veya iptal edin.

## Sınırlamalar

Google AI Studio, proje ve anahtar yönetimiyle ilgili aşağıdaki sınırlamaları uygular:

- Google AI Studio'nun **Projeler** sayfasında tek seferde en fazla 10 proje oluşturabilirsiniz.
- **API anahtarları** ve **Projeler** sayfalarında en fazla 100 anahtar ve 50 proje gösterilir.
- Yalnızca kısıtlanmamış veya özellikle Generative Language API (Gemini API) ile kısıtlanmış API anahtarları gösterilir.

Gelişmiş proje yönetimi için veya anahtarları başka kısıtlamalarla değiştirmek için [Google Cloud Console kimlik bilgileri sayfasını](https://console.cloud.google.com/apis/credentials?hl=tr) kullanın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-25 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-25 UTC."],[],[]]
