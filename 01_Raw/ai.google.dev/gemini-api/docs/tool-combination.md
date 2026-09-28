---
source_url: https://ai.google.dev/gemini-api/docs/tool-combination?hl=tr
fetched_at: 2026-09-28T06:17:33.807188+00:00
title: "Yerle\u015fik ara\u00e7lar\u0131 ve i\u015flev \u00e7a\u011fr\u0131lar\u0131n\u0131 birle\u015ftirme \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yerleşik araçları ve işlev çağrılarını birleştirme

Gemini, araç çağrılarının bağlam geçmişini koruyup ortaya çıkararak `google_search` gibi [yerleşik araçların](https://ai.google.dev/gemini-api/docs/tools?hl=tr) ve [işlev çağrılarının](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) (*özel araçlar* olarak da bilinir) tek bir etkileşimde birleştirilmesine olanak tanır. Yerleşik ve özel araç kombinasyonları, karmaşık ve etkileşimli iş akışlarına olanak tanır. Örneğin, model, belirli iş mantığınızı çağırmadan önce kendisini gerçek zamanlı web verileriyle temellendirebilir.

Aşağıda, `google_search` ile yerleşik ve özel araç kombinasyonlarını ve özel bir işlevi `getWeather` etkinleştiren bir örnek verilmiştir:

### Python

```
# This will only work for SDK newer than 2.0.0
from google import genai

client = genai.Client()

getWeather = {
    "type": "function",
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

# The Interactions API manages context automatically across tool calls.
# The model will first use Google Search, then call getWeather.
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=[
        {"type": "google_search"},
        getWeather,
    ],
)

# Process steps: the interaction contains search results and a function call
for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} with args: {step.arguments}")
        # In a real application, you would execute the function here
        # and provide the result back to the model.
```

### JavaScript

```
// This will only work for SDK newer than 2.0.0
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    type: "function",
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "object",
        properties: {
            location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

// The Interactions API manages context automatically across tool calls.
// The model will first use Google Search, then call getWeather.
const interaction = await client.interactions.create({
    model: "gemini-3.8-flash",
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: [
        { type: "google_search" },
        getWeather,
    ],
});

// Process steps: the interaction contains search results and a function call
for (const step of interaction.steps) {
    if (step.type === "function_call") {
        console.log(`Function call: ${step.name} with args: ${JSON.stringify(step.arguments)}`);
        // In a real application, you would execute the function here
        // and provide the result back to the model.
    }
}
```

### Java

```
import com.google.genai.Client;
import com.google.genai.gaos.models.interactions.CreateModelInteraction;
import com.google.genai.gaos.models.interactions.Function;
import com.google.genai.gaos.models.interactions.GoogleSearch;
import com.google.genai.gaos.models.interactions.Interaction;
import com.google.genai.gaos.models.interactions.InteractionsInput;
import com.google.genai.gaos.models.interactions.Model;
import com.google.genai.gaos.models.operations.CreateInteractionRequestBody;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

Client client = new Client();

Map<String, Object> parameters = new HashMap<>();
parameters.put("type", "object");

Function customFunc =
    Function.builder()
        .name("get_user_location")
        .description("Retrieves user current location.")
        .parameters(parameters)
        .build();

CreateModelInteraction params =
    CreateModelInteraction.builder()
        .model(Model.of("gemini-3.8-flash"))
        .input(InteractionsInput.of("What is the weather like where I am right now?"))
        .tools(Arrays.asList(customFunc, new GoogleSearch()))
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
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    customFunc := interactions.NewTool(interactions.Function{
        Name:        genai.Ptr("get_user_location"),
        Description: genai.Ptr("Retrieves user current location."),
        Parameters: map[string]any{
            "type": "object",
        },
    })

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateModelInteraction{
            Model: interactions.Model("gemini-3.8-flash"),
            Input: interactions.NewInteractionsInput("What is the weather like where I am right now?"),
            Tools: []interactions.Tool{
                customFunc,
                interactions.NewTool(interactions.GoogleSearch{}),
            },
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
# Specifies the API revision to avoid breaking changes when they become default
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "model": "gemini-3.8-flash",
  "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
  "tools": [
    { "type": "google_search" },
    {
      "type": "function",
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "object",
          "properties": {
              "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }
  ]
}'
```

## İşleyiş şekli

Gemini 3 modelleri, yerleşik ve özel araç kombinasyonlarını etkinleştirmek için *araç bağlamı dolaşımını* kullanır. Araç bağlamı dolaşımı, yerleşik araçların bağlamını korumayı ve kullanıma sunmayı, aynı etkileşimde özel araçlarla paylaşmayı mümkün kılar.

### Araç kombinasyonunu etkinleştirme

- Birleştirme davranışını tetiklemek için kullanmak istediğiniz yerleşik araçlarla birlikte [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#function-declarations)'ı ekleyin.

### API, iade adımlarını döndürür

API, etkileşim yanıtında yerleşik araç çağrıları ve işlev (özel araç) çağrıları için ayrı adımlar döndürür:

- **Yerleşik araç adımları**: API, bu adımları otomatik olarak yönetir ve dönüşler arasında bağlamı korur.
- **İşlev çağrısı adımları**: API, özel işlevleriniz için `function_call` adım döndürür. İşlevi yürütür ve sonucu geri sağlarsınız.

### Döndürülen adımlardaki kritik alanlar

Döndürülen adımlardaki belirli alanlar, araç bağlamını korumak ve araç kombinasyonlarını etkinleştirmek için çok önemlidir:

- **`id`**: `function_call` ve `function_response` adımlarında bulunur. Bir görüşmeyi yanıtıyla eşleyen benzersiz tanımlayıcı.
- **`signature`**: `thought` adımlarının yanı sıra Gemini 3 ve sonraki modeller için tüm araç çağrısı (ör. `function_call`) ve sonuç (ör. `function_response`) adımlarında bulunur. Bu şifrelenmiş bağlam, etkileşimler arasında **araç bağlamı dolaşımını** sağlar.

**Bu alanları yönetme:**

- **Durumlu Mod (Önerilen)**: `previous_interaction_id` kullandığınızda sunucu hem `id` hem de `signature` alanlarını otomatik olarak işler.
- **Durumsuz Mod**: Konuşma geçmişini manuel olarak yönetirken, kimliği doğrulamak ve bağlamı korumak için sonraki isteklerde hem `id` hem de `signature` alanlarını modele geri ilettiğinizden emin olmanız gerekir. Tam yanıt nesnesini geçmişe geri iletirseniz resmi SDK'lar bunu otomatik olarak işler.

### Araca özgü veriler

Bazı yerleşik araçlar, araç türüne özel ve kullanıcı tarafından görülebilen veri bağımsız değişkenleri döndürür.

| Araç | Kullanıcı tarafından görülebilen araç çağrısı bağımsız değişkenleri (varsa) | Kullanıcı tarafından görülebilen araç yanıtı (varsa) |
| --- | --- | --- |
| **google\_search** | `queries` | `search_suggestions` |
| **google\_maps** | `queries` | `places` `google_maps_widget_context_token` |
| **url\_context** | `urls` Taranacak URL'ler | `status`: Göz atma durumu `retrieved_url`: Göz atılan URL'ler |
| **file\_search** | Yok | Yok |

## Token'lar ve fiyatlandırma

İsteklerdeki yerleşik araç çağrısı bölümlerinin `prompt_token_count` sınırına dahil edildiğini unutmayın. Bu ara araç adımları artık görünür olduğundan ve size geri döndürüldüğünden görüşme geçmişinin bir parçasıdır. Bu durum yalnızca *istekler* için geçerlidir, *yanıtlar* için geçerli değildir.

Google Arama aracı bu kuralın istisnasıdır. Google Arama, sorgu düzeyinde kendi fiyatlandırma modelini zaten uyguladığından jetonlar iki kez ücretlendirilmez ([Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasına bakın).

Daha fazla bilgi için [Parçalar](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) sayfasını okuyun.

## Sınırlamalar

- Araç bağlamı dolaşımı etkinleştirildiğinde varsayılan olarak `validated` modu kullanılır (`auto` modu desteklenmez).
- `google_search` gibi yerleşik araçlar konum ve mevcut saat bilgilerini kullandığından `system_instruction` veya `function_declaration.description` cihazınızda çakışan konum ve saat bilgileri varsa araç kombinasyonu özelliği iyi çalışmayabilir.

## Desteklenen araçlar

Standart araç bağlamı dolaşımı, sunucu tarafı (yerleşik) araçlar için geçerlidir.
Kod yürütme de sunucu tarafı bir araçtır ancak bağlam dolaşımı için kendi yerleşik çözümüne sahiptir. Bilgisayar Kullanımı ve işlev çağrısı, istemci tarafı araçlardır ve bağlam dolaşımı için yerleşik çözümleri de vardır.

| Araç | Yürütme tarafı | Bağlam Dolaşımı Desteği |
| --- | --- | --- |
| [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) | Sunucu tarafı | Destekleniyor |
| [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) | Sunucu tarafı | Desteklenir (yerleşik, `code_execution` ve `code_execution_result` adımlarını kullanır) |
| [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) | İstemci tarafı | Desteklenir (yerleşik, `function_call` ve `function_response` adımlarını kullanır) |
| [Özel işlevler](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) | İstemci tarafı | Desteklenir (yerleşik, `function_call` ve `function_response` adımlarını kullanır) |

## Sırada ne var?

- Gemini API'deki [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) hakkında daha fazla bilgi edinin.
- Desteklenen araçları keşfedin:
  - [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)
  - [Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)
  - [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)
  - [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-09-24 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-09-24 UTC."],[],[]]
