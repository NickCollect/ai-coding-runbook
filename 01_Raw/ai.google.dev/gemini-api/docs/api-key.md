---
source_url: https://ai.google.dev/gemini-api/docs/api-key?hl=tr
fetched_at: 2026-10-12T06:56:33.528212+00:00
title: "Gemini API anahtarlar\u0131n\u0131 kullanma \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API anahtarlarını kullanma

Gemini API'yi kullanmak için isteklerinizin kimliğini doğrulamanız gerekir. Standart veya yetkilendirme API anahtarı kullanarak kimliğinizi doğrulayabilirsiniz.

[Gemini API anahtarı oluşturma veya görüntüleme](https://aistudio.google.com/apikey?hl=tr)

## API anahtarı türleri: standart ve yetkilendirme

API anahtarları, Gemini API'ye erişim sağlar ancak güvenlik özellikleri farklıdır. Gemini API, güvenliği artırmak için standart API anahtarlarından yetkilendirme anahtarlarına geçiş yapıyor:

- **Standart API anahtarları**: İstekleri, faturalandırma ve kota amaçlarıyla bir Google Cloud projesiyle ilişkilendirin. Standart anahtarlar arayanı tanımlamadığından destekleyebilecekleri izinlerin ve erişim denetiminin ayrıntı düzeyi sınırlıdır.
- **Yetkilendirme (auth) anahtarları**: Doğrudan bir Google Cloud hizmet hesabına bağlıdır. Yetkilendirme anahtarı kullandığınızda istekleriniz, bağlı hizmet hesabının kimliği altında işlenir. Bu sayede ayrıntılı erişim kontrolü sağlanır. Yetkilendirme anahtarları varsayılan olarak Generative Language API (Gemini API) ile sınırlıdır ve sistemlerimiz tarafından tespit edilen sızdırılmış anahtarların kullanımını hızlı bir şekilde durduran, hızlı etkili sızdırılmış anahtar zorunluluğu sağlar.

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
5. İçe aktarma işlemi tamamlandıktan sonra, kontrol panelindeki **API Anahtarları** sayfasına giderek bu projede bir anahtar oluşturun.

### Anahtar oluşturma izinleriyle ilgili sorunları giderme

**API anahtarı oluştur** düğmesi kullanılamıyorsa ve şu mesajı gösteriyorsa:
*"Bu projede anahtar oluşturma izniniz yok"*, gerekli IAM izinlerine sahip değilsiniz.

Google Cloud projenizin veya kuruluşunuzun yöneticisinden aşağıdaki izinleri içeren bir rol (ör. Proje Düzenleyici) vermesini isteyin:

- `resourcemanager.projects.get`: AI Studio'nun projeyi doğrulamasını sağlar.
- `apikeys.keys.create`: Anahtar oluşturmaya izin verir.
- `serviceusage.services.enable`: Generative Language API'nin etkinleştirilmesini sağlar.
- `iam.serviceAccounts.create`: Bağlı hizmet hesabını oluşturmak için gereklidir.
- `iam.serviceAccountApiKeyBindings.create`: Hizmet hesabını API anahtarına bağlar.

Yönetici erişimi alamıyorsanız anahtarlarınızı oluşturmak için bir kuruluşla ilişkili olmayan yeni bir Google Cloud projesi oluşturabilirsiniz.

## Google Cloud Console'da anahtar oluşturma

Google AI Studio yalnızca kısıtlanmamış veya Gemini API ile kısıtlanmış anahtarları gösterir. AI Studio'yu kullanamıyorsanız veya tüm API anahtarlarınızı tek bir yerden yönetmek istiyorsanız [API anahtarı oluşturma](https://cloud.google.com/docs/authentication/api-keys?hl=tr#create) ile ilgili Cloud belgelerini inceleyin. Gemini API anahtarı oluşturmak için anahtarın bir [hizmet hesabına](https://cloud.google.com/iam/docs/service-account-overview?hl=tr) bağlanması gerekir.

## Ortamınızı kurma

Anahtarınız olduğunda ortamınızı, uygulamalarınızda güvenli bir şekilde kullanacak şekilde yapılandırın.

### 1. seçenek: Ortam değişkenlerini kullanma (önerilir)

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

### 2. seçenek: API anahtarını kodda açıkça belirtin

İstemciyi başlatırken API anahtarını açıkça iletebilirsiniz. Bu işlemi yalnızca ortam değişkenlerini kullanamıyorsanız yapın.

### Python

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const interaction = await ai.interactions.create({
    model: "gemini-3.8-flash",
    input: "Explain how AI works in a few words",
  });
  console.log(interaction.output_text);
}

main();
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;

Client client = Client.builder().apiKey("YOUR_API_KEY").build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("Explain how AI works in a few sentences."))
        .build();

Interaction interaction =
    client.interactions.create(CreateInteractionRequestBody.of(params)).interaction().get();

System.out.println(interaction.outputText().orElse(""));
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "YOUR_API_KEY",
    })
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("Explain how AI works in a few sentences."),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }
    if res.Interaction.OutputText != nil {
        fmt.Println(*res.Interaction.OutputText)
    }
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H 'Content-Type: application/json' \
  -H "x-goog-api-key: YOUR_API_KEY" \
  -X POST \
  -d '{
    "model": "gemini-3.8-flash",
    "input": "Explain how AI works in a few words"
  }'
```

## Güvenlik ve sır yönetimi

Gemini API anahtarınızı şifre gibi kullanın. Tehlikeye girerse diğer kullanıcılar projenizin kotasını kullanabilir, beklenmedik faturalandırma ücretlerine neden olabilir ve özel kaynaklara erişebilir.

### Önemli güvenlik kuralları

- **Anahtarları gizli tutun**: API anahtarlarını asla Git gibi kaynak denetim sistemlerine işlemeyin.
- **Üretimde anahtarları asla istemci tarafında kullanıma sunmayın**: API anahtarlarını doğrudan web veya mobil uygulamalara sabit kodlamayın. İstemci tarafı kodunda derlenen anahtarlar kullanıcılar tarafından çıkarılabilir. İstemci tarafı uygulamaların güvenliğini sağlamak için gerçek API çağrılarını yapmak üzere bir arka uç proxy sunucusu çalıştırın.

### Gizli veri yönetimiyle ilgili en iyi uygulamalar

- **Ortam değişkenleri**: Anahtarları yapılandırma dosyaları yerine ortam değişkenlerinden okuyun.
- **Secret Manager**: Üretim için anahtarlarınızı [Google Cloud Secret Manager](https://cloud.google.com/secret-manager?hl=tr) gibi güvenli bir gizli anahtar deposunda saklayın.
- **Faturalandırma uyarıları**: Kullanım veya maliyetlerde artış olması durumunda sizi bilgilendirmek için Google Cloud Console'da faturalandırma uyarıları ayarlayın.

### Sızıntı yanıtı yapılacaklar listesi

API anahtarınızın sızdırıldığından şüpheleniyorsanız:

1. **Yeni bir anahtar oluşturun**: Google AI Studio'da veya Cloud Console'da yedek bir anahtar oluşturun.
2. **Uygulamanızı güncelleyin**: Kodunuzu yeni anahtarı kullanarak dağıtın.
3. **Güvenliği ihlal edilmiş anahtarı devre dışı bırakın veya silin**: Yeni anahtar doğrulandıktan sonra Cloud Console'da sızdırılan anahtarı devre dışı bırakın. Uygulama kapalı kalma süresini önlemek için yeni anahtar tamamen etkinleşene kadar eski anahtarı silmeyin.
4. **Kullanımı denetleme**: Yetkisiz etkinliği belirlemek için Google Cloud Console'da faturalandırma günlüklerini ve API kullanımını kontrol edin.

## Anahtarlarınızı kısıtlama ve güvenliğini sağlama

API anahtarlarınıza kısıtlamalar eklemek, bir anahtarın güvenliği ihlal edilirse oluşabilecek potansiyel zararı en aza indirir.

### İstek kaynağı kısıtlamaları uygulama

Kaynak kısıtlamaları, anahtarınızı kullanabilecek IP adreslerini, web sitelerini veya uygulamaları sınırlar.

1. [Google Cloud Console kimlik bilgileri sayfasına](https://console.cloud.google.com/apis/credentials?hl=tr) gidin.
2. Projenizi seçin ve kısıtlamak istediğiniz API anahtarının adını tıklayın.
3. **Uygulama kısıtlamaları** bölümünde **IP adresleri**'ni (veya ortamınız için uygun kısıtlama türünü) seçin.
4. İzin verilen IP adreslerini veya aralıklarını belirtin, ardından **Kaydet**'i tıklayın.

### Sınırsız standart API anahtarlarının güvenliğini sağlama

Gemini API'yi kullanmaya devam etmek için tüm sınırsız anahtarları güvenli hale getirmeniz gerekir.

#### 1. yöntem: Anahtarı yalnızca Gemini API ile sınırlayın (AI Studio)

Anahtarı yalnızca Gemini API için kullanıyorsanız doğrudan AI Studio'da güvenli hale getirin:

1. [Google AI Studio](https://aistudio.google.com/api-keys?hl=tr)'daki **API Anahtarları** sayfasında **Kısıtlanmamış** etiketiyle işaretlenmiş anahtarları bulun.
2. Fareyle etiketin üzerine gelin ve iletişim kutusunda **Kısıtlama ekle**'yi tıklayın.
3. **Yalnızca Gemini API ile kısıtla**'yı seçin.
4. Onaylamak için **Anahtarı kısıtla**'yı tıklayın.

#### 2. yöntem: Anahtarı diğer hizmetler için kısıtlama (Google Cloud Console)

Anahtar diğer Google API'leriyle paylaşılıyorsa (önerilmez) Cloud Console'da kısıtlayın. **Not: Bu anahtar kullanılarak yapılan Gemini API istekleri, bu kısıtlamalar uygulandıktan sonra başarısız olur.**

1. [Google Cloud Console kimlik bilgileri sayfasını](https://console.cloud.google.com/apis/credentials?hl=tr) ziyaret edin.
2. Projeyi ve API anahtarını seçin.
3. **API kısıtlamaları** bölümünde, bu anahtarın erişmesini istediğiniz API'leri seçmek için **API kısıtlamalarını seçin** açılır listesini kullanın. **Generative
   Language API**'yi seçmeyin.
4. **Kaydet**'i tıklayın. Gemini API'yi kullanmaya devam etmek için AI Studio'da ayrı ve kısıtlanmış bir anahtar oluşturun.

### Etkin olmayan engellenmiş anahtarlar

7 Mayıs 2026'dan itibaren Gemini API, uzun süredir kullanılmayan sınırsız API anahtarlarını engeller. Bu anahtarlar, Yapay Zeka Studio'da **Engellendi** etiketini gösterir. Devam etmek için yeni bir anahtar oluşturmanız veya mevcut bir kısıtlanmış anahtarı kullanmanız gerekir.

## Kimlik doğrulama anahtarına geçiş yapma

Yeni bir kimlik doğrulama API anahtarı oluşturmak ve uygulamalarınızı güncellemek için aşağıdaki adımları uygulayın:

1. [AI Studio API anahtarları sayfasına](https://aistudio.google.com/api-keys?hl=tr) gidin.
2. **Standart** olarak listelenen anahtarları belirlemek için **Anahtar Türü** sütununu kontrol edin.
3. Yeni bir anahtar oluşturmak için **API anahtarı oluştur**'u tıklayın. AI Studio'da oluşturulan tüm yeni anahtarlar otomatik olarak kimlik doğrulama anahtarı olarak oluşturulur.
4. Yeni kimlik doğrulama API anahtarını kopyalayın.
5. Uygulama kodunuzu, ortam değişkenlerinizi ve tüm dağıtım yapılandırmalarınızı yeni kimlik doğrulama API anahtarını kullanacak şekilde güncelleyin.
6. Uygulamanızın yeni anahtarla doğru şekilde çalıştığını onaylamak için test edin.
7. Doğrulama işlemi tamamlandıktan sonra kötüye kullanımı önlemek için eski trafik anahtarınızı silin veya iptal edin.

## Sınırlamalar

Google AI Studio, proje ve anahtar yönetimiyle ilgili aşağıdaki sınırlamaları uygular:

- Google AI Studio'nun **Projeler** sayfasında tek seferde en fazla 10 proje oluşturabilirsiniz.
- **API anahtarları** ve **Projeler** sayfalarında en fazla 100 anahtar ve 50 proje gösterilir.
- Yalnızca kısıtlanmamış veya özellikle Generative Language API (Gemini API) ile kısıtlanmış API anahtarları gösterilir.

Gelişmiş proje yönetimi için veya anahtarları başka kısıtlamalarla değiştirmek için [Google Cloud Console kimlik bilgileri sayfasını](https://console.cloud.google.com/apis/credentials?hl=tr) kullanın.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-10-06 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-10-06 UTC."],[],[]]
