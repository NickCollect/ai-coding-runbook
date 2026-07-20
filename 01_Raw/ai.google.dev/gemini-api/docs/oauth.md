---
source_url: https://ai.google.dev/gemini-api/docs/oauth?hl=tr
fetched_at: 2026-07-20T04:46:58.220764+00:00
title: "OAuth ile kimlik do\u011frulama h\u0131zl\u0131 ba\u015flang\u0131\u00e7 k\u0131lavuzu \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# OAuth ile kimlik doğrulama hızlı başlangıç kılavuzu

Gemini API'de kimlik doğrulamanın en kolay yolu, [Gemini API'yi kullanmaya başlama kılavuzunda](https://ai.google.dev/gemini-api/docs/get-started?hl=tr) açıklandığı gibi bir API anahtarı yapılandırmaktır. Daha katı erişim kontrollerine ihtiyacınız varsa bunun yerine OAuth kullanabilirsiniz. Bu kılavuz, OAuth ile kimlik doğrulama ayarlamanıza yardımcı olacaktır.

Bu kılavuzda, test ortamı için uygun olan basitleştirilmiş bir kimlik doğrulama yaklaşımı kullanılmaktadır. Üretim ortamı için, uygulamanıza uygun [erişim kimlik bilgilerini seçmeden](https://developers.google.com/workspace/guides/create-credentials?hl=tr#choose_the_access_credential_that_is_right_for_you) önce [kimlik doğrulama ve yetkilendirme](https://developers.google.com/workspace/guides/auth-overview?hl=tr) hakkında bilgi edinin.

## Hedefler

- OAuth için Cloud projenizi ayarlama
- Uygulama varsayılan kimlik bilgilerini ayarlama
- `gcloud auth` kullanmak yerine programınızdaki kimlik bilgilerini yönetin

## Ön koşullar

Bu hızlı başlangıç kılavuzunu çalıştırmak için ihtiyacınız olanlar:

- [Google Cloud projesi](https://developers.google.com/workspace/guides/create-project?hl=tr)
- [gcloud CLI'nın yerel olarak yüklenmiş olması](https://cloud.google.com/sdk/docs/install?hl=tr)

## Cloud projenizi oluşturma

Bu hızlı başlangıcı tamamlamak için önce Cloud projenizi ayarlamanız gerekir.

### 1. API'yi etkinleştirme

Google API'lerini kullanmadan önce bir Google Cloud projesinde etkinleştirmeniz gerekir.

- Google Cloud Console'da Google Generative Language API'yi etkinleştirin.

  [API'yi etkinleştirme](https://console.cloud.google.com/flows/enableapi?apiid=generativelanguage.googleapis.com&hl=tr)

### 2. OAuth kullanıcı rızası ekranını yapılandırma

Ardından, projenin OAuth kullanıcı rızası ekranını yapılandırın ve kendinizi test kullanıcısı olarak ekleyin. Cloud projeniz için bu adımı zaten tamamladıysanız bir sonraki bölüme geçin.

1. Google Cloud Console'da **Menü** > **Google Auth platform** > **Overview**'a (Genel bakış) gidin.

   [Google Auth platformuna gidin](https://console.developers.google.com/auth/overview?hl=tr)
2. Proje yapılandırma formunu doldurun ve **Kitle** bölümünde kullanıcı türünü **Harici** olarak ayarlayın.
3. Formun geri kalanını doldurun, Kullanıcı Verileri Politikası şartlarını kabul edin ve **Oluştur**'u tıklayın.
4. Şimdilik kapsam eklemeyi atlayıp **Kaydet ve Devam Et**'i tıklayabilirsiniz. Gelecekte, Google Workspace kuruluşunuzun dışında kullanılacak bir uygulama oluşturduğunuzda, uygulamanızın gerektirdiği yetkilendirme kapsamlarını ekleyip doğrulamanız gerekir.
5. Test kullanıcıları ekleyin:

   1. Google Auth platformunun [Kitle sayfasına](https://console.developers.google.com/auth/audience?hl=tr) gidin.
   2. **Test kullanıcıları** bölümünde **Kullanıcı ekle**'yi tıklayın.
   3. E-posta adresinizi ve yetkili diğer test kullanıcılarını girip **Kaydet**'i tıklayın.

### 3. Masaüstü uygulaması için kimlik bilgilerini yetkilendirme

Son kullanıcı olarak kimlik doğrulamak ve uygulamanızdaki kullanıcı verilerine erişmek için bir veya daha fazla OAuth 2.0 istemci kimliği oluşturmanız gerekir. İstemci kimliği, tek bir uygulamanın Google OAuth sunucularına tanıtılması için kullanılır. Uygulamanız birden fazla platformda çalışıyorsa her platform için ayrı bir istemci kimliği oluşturmanız gerekir.

1. Google Cloud Console'da **Menü** > **Google Auth platformu** > **İstemciler**'e gidin.

   [Kimlik Bilgileri'ne gidin](https://console.developers.google.com/auth/clients?hl=tr)
2. **Create Client**'ı (İstemci Oluştur) tıklayın.
3. **Uygulama türü** > **Masaüstü uygulaması**'nı tıklayın.
4. **Ad** alanına, kimliğin adını yazın. Bu ad yalnızca Google Cloud Console'da gösterilir.
5. **Oluştur**'u tıklayın. Yeni istemci kimliğinizi ve istemci gizli anahtarınızı gösteren, oluşturulan OAuth istemcisi ekranı görünür.
6. **Tamam**'ı tıklayın. Yeni oluşturulan kimlik bilgisi, **OAuth 2.0 İstemci Kimlikleri** altında görünür.
7. JSON dosyasını kaydetmek için indir düğmesini tıklayın. `client_secret_<identifier>.json` olarak kaydedilir. `client_secret.json` olarak yeniden adlandırın ve çalışma dizininize taşıyın.

## Uygulama Varsayılan Kimlik Bilgileri'ni ayarlama

`client_secret.json` dosyasını kullanılabilir kimlik bilgilerine dönüştürmek için dosyanın konumunu `gcloud auth application-default login` komutunun `--client-id-file` bağımsız değişkenine iletin.

```
gcloud auth application-default login \
    --client-id-file=client_secret.json \
    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
```

Bu eğitimdeki basitleştirilmiş proje kurulumu, **"Google bu uygulamayı doğrulamadı."** iletişim kutusunu tetikler. Bu normal bir durumdur. **"Devam"**'ı seçin.

Bu işlem, sonuç jetonunu iyi bilinen bir konuma yerleştirir. Böylece jetona `gcloud` veya istemci kitaplıkları tarafından erişilebilir.

```` ```
gcloud auth application-default login   

    --no-browser
    --client-id-file=client_secret.json   

    --scopes='https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/generative-language.retriever'
``` ````

Uygulama Varsayılan Kimlik Bilgileri (ADC) ayarlandıktan sonra, çoğu dildeki istemci kitaplıklarının bunları bulmak için çok az yardıma veya hiç yardıma ihtiyacı olmaz.

### Curl

Bu işlemin çalıştığını test etmenin en hızlı yolu, curl kullanarak REST API'ye erişmek için kullanmaktır:

```
access_token=$(gcloud auth application-default print-access-token)
project_id=<MY PROJECT ID>
curl -X GET https://generativelanguage.googleapis.com/v1/models \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer ${access_token}" \
    -H "x-goog-user-project: ${project_id}" | grep '"name"'
```

### Python

Python'da istemci kitaplıkları bunları otomatik olarak bulur:

```
pip install google-genai
```

Bunu test etmek için kullanılabilecek minimum komut dosyası:

```
from google import genai

client = genai.Client()
print('Available base models:', [m.name for m in client.models.list()])
```

## Sonraki adımlar

Bu işlem işe yararsa [metin verilerinizde semantik almayı](https://ai.google.dev/docs/semantic_retriever?hl=tr) deneyebilirsiniz.

## Kimlik bilgilerini kendiniz yönetme [Python]

Çoğu durumda, istemci kimliğinden (`client_secret.json`) erişim jetonu oluşturmak için `gcloud` komutunu kullanamazsınız. Google, bu süreci uygulamanızda yönetmenize olanak tanıyan birçok dilde kitaplıklar sunar. Bu bölümde, süreç Python'da gösterilmektedir. Bu tür bir prosedürün diğer dillerdeki benzer örneklerini [Drive API belgelerinde](https://developers.google.com/drive/api/quickstart/python?hl=tr) bulabilirsiniz.

### 1. Gerekli kitaplıkları yükleme

Python için Google istemci kitaplığını ve Gemini istemci kitaplığını yükleyin.

```
pip install --upgrade -q google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install google-genai
```

### 2. Kimlik bilgisi yöneticisini yazma

Yetkilendirme ekranlarını tıklamanız gereken sayıyı en aza indirmek için çalışma dizininizde `load_creds.py` adlı bir dosya oluşturun. Bu dosya, daha sonra yeniden kullanılabilecek veya süresi dolarsa yenilenebilecek bir `token.json` dosyasını önbelleğe alır.

`client_secret.json` dosyasını `genai.configure` ile kullanılabilir bir jetona dönüştürmek için aşağıdaki kodla başlayın:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/generative-language.retriever']

def load_creds():
    """Converts `client_secret.json` to a credential object.

    This function caches the generated tokens to minimize the use of the
    consent screen.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
```

### 3. Programınızı yazma

Şimdi `script.py` özelliğinizi oluşturun:

```
import pprint
from google import genai
from load_creds import load_creds

creds = load_creds()

client = genai.Client(credentials=creds)

print()
print('Available base models:', [m.name for m in client.models.list()])
```

### 4. Programınızı çalıştırma

Çalışma dizininizde örneği çalıştırın:

```
python script.py
```

Komut dosyasını ilk kez çalıştırdığınızda bir tarayıcı penceresi açılır ve erişimi yetkilendirmeniz istenir.

1. Henüz Google Hesabınızda oturum açmadıysanız oturum açmanız istenir. Birden fazla hesapta oturum açtıysanız **projenizi yapılandırırken "Test Hesabı" olarak ayarladığınız hesabı seçtiğinizden emin olun.**
2. Yetkilendirme bilgileri dosya sisteminde saklandığı için örnek kodu bir sonraki çalıştırmanızda yetkilendirme istenmez.

Kimlik doğrulama işlemini başarıyla ayarladınız.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-01 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-01 UTC."],[],[]]
