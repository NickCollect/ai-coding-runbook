---
source_url: https://ai.google.dev/gemini-api/docs/generate-content/tool-combination?hl=tr
fetched_at: 2026-07-06T05:17:43.362648+00:00
title: "Yerle\u015fik ara\u00e7lar\u0131 ve i\u015flev \u00e7a\u011fr\u0131lar\u0131n\u0131 birle\u015ftirme \u00a0|\u00a0 Gemini Generate Content API (Legacy) \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Generate Content API](https://ai.google.dev/gemini-api/docs/generate-content/get-started?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Yerleşik araçları ve işlev çağrılarını birleştirme

Gemini, araç çağrılarının bağlam geçmişini koruyup ortaya çıkararak `google_search` gibi [yerleşik araçların](https://ai.google.dev/gemini-api/docs/tools?hl=tr) ve [işlev çağrılarının](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) (*özel araçlar* olarak da bilinir) tek bir üretimde birleştirilmesine olanak tanır. Yerleşik ve özel araç kombinasyonları, karmaşık ve etkili iş akışlarına olanak tanır. Örneğin, model, belirli iş mantığınızı çağırmadan önce kendisini gerçek zamanlı web verilerine dayandırabilir.

Aşağıda, `google_search` ile yerleşik ve özel araç kombinasyonlarının ve özel bir işlevin `getWeather` etkinleştirildiği bir örnek verilmiştir:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
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

# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),  # Built-in tool
                function_declarations=[getWeather]       # Custom tool
            ),
        ],
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)
function_call_id = None
for part in response.candidates[0].content.parts:
    if part.function_call:
        print(f"Function call: {part.function_call.name} (ID: {part.function_call.id})")
        function_call_id = part.function_call.id

# Turn 2: Manually build history to circulate both tool and function context
history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    # Response from Turn 1 includes tool_call, tool_response, and thought_signatures
    response.candidates[0].content,
    # Return the function_response
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=function_call_id # Match the ID from the function_call
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=history,
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch(),
                function_declarations=[getWeather]
            ),
        ],
        # This flag needs to be enabled for built-in tool context circulation and tool combination
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True
        )
    ),
)

for part in response_2.candidates[0].content.parts:
    if part.text:
        print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.getGenerativeModel({
        model: "gemini-3.5-flash",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    // This flag needs to be enabled for built-in tool context circulation and tool combination
    const toolConfig = { includeServerSideToolInvocations: true };

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;

    for (const part of response1.candidates[0].content.parts) {
        if (part.functionCall) {
            console.log(`Function call: ${part.functionCall.name} (ID: ${part.functionCall.id})`);
        }
    }

    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    // Turn 2: Manually build history to circulate both tool and function context
    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        // Response from Turn 1 includes tool_call, tool_response, and thought_signatures
        response1.candidates[0].content,
        // Return the function_response
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId // Match the ID from the function_call
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });

    for (const part of result2.response.candidates[0].content.parts) {
        if (part.text) {
            console.log(part.text);
        }
    }
}

run();
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    "github.com/google/generative-ai-go/genai"
    "google.golang.org/api/option"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, option.WithAPIKey(os.Getenv("GEMINI_API_KEY")))
    if err != nil {
        log.Exit(err)
    }
    defer client.Close()

    getWeather := &genai.FunctionDeclaration{
        Name:        "getWeather",
        Description: "Get the weather in a given location",
        Parameters: &genai.Schema{
            Type: genai.Object,
            Properties: map[string]*genai.Schema{
                "location": {
                    Type:        genai.String,
                    Description: "The city and state, e.g. San Francisco, CA",
                },
            },
            Required: []string{"location"},
        },
    }

    model := client.GenerativeModel("gemini-3.5-flash")
    model.Tools = []*genai.Tool{
        {GoogleSearch: &genai.GoogleSearch{}}, // Built-in tool
        {FunctionDeclarations: []*genai.FunctionDeclaration{getWeather}}, // Custom tool
    }
    ist := true
    model.ToolConfig = &genai.ToolConfig{
        IncludeServerSideToolInvocations: &ist, // This flag needs to be enabled for built-in tool context circulation and tool combination
    }

    chat := model.StartChat()

    // Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
    prompt := genai.Text("What is the northernmost city in the United States? What's the weather like there today?")
    resp1, err := chat.SendMessage(ctx, prompt)
    if err != nil {
        log.Exitf("SendMessage failed: %v", err)
    }

    if resp1 == nil || len(resp1.Candidates) == 0 || resp1.Candidates[0].Content == nil {
        log.Exit("empty response from model")
    }

    var functionCallID string
    for _, part := range resp1.Candidates[0].Content.Parts {
        switch p := part.(type) {
        case genai.FunctionCall:
            fmt.Printf("Function call: %s (ID: %s)\n", p.Name, p.ID)
            if p.Name == "getWeather" {
                functionCallID = p.ID
            }
        }
    }

    if functionCallID == "" {
        log.Exit("no getWeather function call in response")
    }

    // Turn 2: Provide function result back to model.
    // Chat history automatically includes tool_call, tool_response, and thought_signatures from Turn 1.
    fr := genai.FunctionResponse{
        Name: "getWeather",
        ID:   functionCallID,
        Response: map[string]any{
            "response": "Very cold. 22 degrees Fahrenheit.",
        },
    }

    resp2, err := chat.SendMessage(ctx, fr)
    if err != nil {
        log.Exitf("SendMessage for turn 2 failed: %v", err)
    }

    if resp2 == nil || len(resp2.Candidates) == 0 || resp2.Candidates[0].Content == nil {
        log.Exit("empty response from model in turn 2")
    }

    for _, part := range resp2.Candidates[0].Content.Parts {
        if txt, ok := part.(genai.Text); ok {
            fmt.Println(string(txt))
        }
    }
}
```

### REST

```
# Turn 1: Initial request with Google Search (built-in) and getWeather (custom) tools enabled
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [{
    "role": "user",
    "parts": [{
      "text": "What is the northernmost city in the United States? What'\''s the weather like there today?"
    }]
  }],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'

# Turn 2: Manually build history to circulate both tool and function context
# The following request assumes you have captured candidates[0].content from Turn 1 response,
# and extracted function_call.id for getWeather.
# Replace FUNCTION_CALL_ID and insert candidate content from turn 1.
curl -X POST "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
  "contents": [
    {
      "role": "user",
      "parts": [{"text": "What is the northernmost city in the United States? What'\''s the weather like there today?"}]
    },
    YOUR_CANDIDATE_CONTENT_FROM_TURN_1_RESPONSE,
    {
      "role": "user",
      "parts": [{
        "functionResponse": {
          "name": "getWeather",
          "id": "FUNCTION_CALL_ID",
          "response": {"response": "Very cold. 22 degrees Fahrenheit."}
        }
      }]
    }
  ],
  "tools": [{
    "googleSearch": {}
  }, {
    "functionDeclarations": [{
      "name": "getWeather",
      "description": "Get the weather in a given location",
      "parameters": {
          "type": "OBJECT",
          "properties": {
              "location": {
                  "type": "STRING",
                  "description": "The city and state, e.g. San Francisco, CA"
              }
          },
          "required": ["location"]
      }
    }]
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}'
```

## İşleyiş şekli

Gemini 3 modelleri, yerleşik ve özel araç kombinasyonlarını etkinleştirmek için *araç bağlamı dolaşımını* kullanır. Araç bağlamı dolaşımı, yerleşik araçların bağlamını korumayı ve kullanıma sunmayı, ayrıca bu bağlamı aynı çağrıdaki özel araçlarla paylaşmayı mümkün kılar.

### Araç kombinasyonunu etkinleştirme

- Araç bağlamı dolaşımını etkinleştirmek için `include_server_side_tool_invocations` işaretini `true` olarak ayarlamanız gerekir.
- Birleştirme davranışını tetiklemek için kullanmak istediğiniz yerleşik araçlarla birlikte [`function_declarations`](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr#function-declarations) öğesini ekleyin.
  - `function_declarations` öğesini dahil etmezseniz işaret ayarlandığı sürece araç bağlamı dolaşımı, dahil edilen yerleşik araçlar üzerinde çalışmaya devam eder.

### API, parçaları döndürür

API, tek bir yanıtta yerleşik araç çağrısı için `toolCall` ve `toolResponse` bölümlerini döndürür. İşlev (özel araç) çağrısı için API, `functionCall` çağrı bölümünü döndürür. Kullanıcı, bir sonraki dönüşte `functionResponse` bölümünü sağlar.

- `toolCall` ve `toolResponse`: API, sunucu tarafında hangi araçların çalıştırıldığının bağlamını ve bunların yürütülmesinin sonucunu bir sonraki dönüş için korumak amacıyla bu bölümleri döndürür.
- `functionCall` ve `functionResponse`: API, işlev çağrısını kullanıcının doldurması için gönderir ve kullanıcı sonucu işlev yanıtında geri gönderir (bu bölümler, Gemini API'deki tüm [işlev çağrıları](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) için standarttır ve araç kombinasyonu özelliğine özgü değildir).
- (Yalnızca [kod yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) aracı)
  `executableCode` ve `codeExecutionResult`:
  Kod yürütme aracı kullanılırken `functionCall` ve `functionResponse` yerine API, `executableCode` (model tarafından oluşturulan ve yürütülmesi amaçlanan kod) ve `codeExecutionResult` (yürütülebilir kodun sonucu) değerlerini döndürür.

Bağlamı korumak ve araç kombinasyonlarını etkinleştirmek için, içerdiği tüm [alanlar](#critical-fields) da dahil olmak üzere tüm parçaları her dönüşte modele geri göndermeniz gerekir.

### Döndürülen parçalardaki kritik alanlar

[API tarafından döndürülen belirli bölümler](#api-returns-parts) `id`, `tool_type` ve `thought_signature` alanlarını içerir. Bu alanlar, araç bağlamının korunması (ve dolayısıyla araç kombinasyonları) için kritik öneme sahiptir. Sonraki isteklerinizde tüm bölümleri *yanıtta verildiği şekilde* döndürmeniz gerekir.

- `id`: Bir çağrıyı yanıtıyla eşleyen benzersiz tanımlayıcı. `id`, araç bağlamı dolaşımından bağımsız olarak **tüm işlev çağrısı yanıtlarında ayarlanır**.
  İşlev yanıtında, API'nin işlev çağrısında sağladığı `id` ile aynı *değeri sağlamanız gerekir*. Yerleşik araçlar, araç çağrısı ile araç yanıtı arasındaki `id` değerini otomatik olarak paylaşır.
  - Tüm araçla ilgili bölümlerde bulunur: `toolCall`, `toolResponse`,
    `functionCall`, `functionResponse`, `executableCode`, `codeExecutionResult`
- `tool_type`: Kullanılan aracı tanımlar; yerleşik araç veya (ör. `URL_CONTEXT`) ya da işlev (ör. `getWeather`) adı.
  - `toolCall` ve `toolResponse` bölümlerinde bulunur.
- `thought_signature`: **API tarafından döndürülen her bölümde** yerleştirilmiş gerçek şifrelenmiş bağlam. Düşünce imzaları olmadan bağlam yeniden oluşturulamaz. Her dönüşte tüm bölümler için düşünce imzalarını döndürmezseniz model hata verir.
  - *Tüm* parçalarda bulunur.

### Araca özgü veriler

Bazı yerleşik araçlar, araç türüne özel ve kullanıcı tarafından görülebilen veri bağımsız değişkenleri döndürür.

| Araç | Kullanıcı tarafından görülebilen araç çağrısı bağımsız değişkenleri (varsa) | Kullanıcı tarafından görülebilen araç yanıtı (varsa) |
| --- | --- | --- |
| **GOOGLE\_SEARCH** | `queries` | `search_suggestions` |
| **GOOGLE\_MAPS** | `queries` | `places` `google_maps_widget_context_token` |
| **URL\_CONTEXT** | `urls` Göz atılacak URL'ler | `urls_metadata` `retrieved_url`: Göz atılan URL'ler `url_retrieval_status`: Göz atma durumu |
| **FILE\_SEARCH** | Yok | Yok |

## Örnek araç kombinasyonu isteği yapısı

Aşağıdaki istek yapısında, "ABD'deki en kuzeydeki şehir hangisidir?" isteminin istek yapısı gösterilmektedir. Bugün hava nasıl?" Bu araç, yerleşik Gemini araçları `google_search` ve `code_execution` ile özel bir işlevi `get_weather` birleştirir.

```
{
  "model": "models/gemini-3.5-flash",
  "contents": [{
    "parts": [{
      "text": "What is the northernmost city in the United States? What's the weather like there today?"
    }],
    "role": "user"
  }, {
    "parts": [{
      "thoughtSignature": "...",
      "toolCall": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "args": {
          "queries": ["northernmost city in the United States"]
        },
        "id": "a7b3k9p2"
      }
    }, {
      "thoughtSignature": "...",
      "toolResponse": {
        "toolType": "GOOGLE_SEARCH_WEB",
        "response": {
          "search_suggestions": "..."
        },
        "id": "a7b3k9p2"
      }
    }, {
      "functionCall": {
        "name": "getWeather",
        "args": {
          "city": "Utqiaġvik, Alaska"
        },
        "id": "m4q8z1v6"
      },
      "thoughtSignature": "..."
    }],
    "role": "model"
  }, {
    "parts": [{
      "functionResponse": {
        "name": "getWeather",
        "response": {
          "response": "Very cold. 22 degrees Fahrenheit."
        },
        "id": "m4q8z1v6"
      }
    }],
    "role": "user"
  }],
  "tools": [{
    "functionDeclarations": [{
      "name": "getWeather"
    }]
  }, {
    "googleSearch": {
    }
  }, {
    "codeExecution": {
    }
  }],
  "toolConfig": {
    "includeServerSideToolInvocations": true
  }
}
```

## Token'lar ve fiyatlandırma

İsteklerdeki `toolCall` ve `toolResponse` bölümlerinin `prompt_token_count` kapsamında sayıldığını unutmayın. Bu ara araç adımları artık görünür olduğundan ve size geri döndürüldüğünden sohbet geçmişinin bir parçasıdır. Bu durum yalnızca *istekler* için geçerlidir, *yanıtlar* için geçerli değildir.

Google Arama aracı bu kuralın istisnasıdır. Google Arama, sorgu düzeyinde kendi fiyatlandırma modelini zaten uyguladığından jetonlar iki kez ücretlendirilmez ([Fiyatlandırma](https://ai.google.dev/gemini-api/docs/pricing?hl=tr) sayfasına bakın).

Daha fazla bilgi için [Parçalar](https://ai.google.dev/gemini-api/docs/tokens?hl=tr) sayfasını okuyun.

## Sınırlamalar

- `include_server_side_tool_invocations` işareti etkinleştirildiğinde varsayılan olarak `VALIDATED` modu kullanılır (`AUTO` modu desteklenmez).
- `google_search` gibi yerleşik araçlar konum ve mevcut saat bilgilerini kullandığından `system_instruction` veya `function_declaration.description` cihazınızda çakışan konum ve saat bilgileri varsa araç kombinasyonu özelliği iyi çalışmayabilir.

## Desteklenen araçlar

Standart araç bağlamı dolaşımı, sunucu tarafı (yerleşik) araçlar için geçerlidir.
Kod Yürütme de sunucu tarafı bir araçtır ancak bağlam dolaşımı için kendi yerleşik çözümüne sahiptir. Bilgisayar Kullanımı ve işlev çağırma, istemci tarafı araçlardır.
Ayrıca bağlam dolaşımı için yerleşik çözümleri vardır.

| Araç | Yürütme tarafı | Bağlam Dolaşımı Desteği |
| --- | --- | --- |
| [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr) | Sunucu tarafı | Destekleniyor |
| [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr) | Sunucu tarafı | Destekleniyor |
| [Kod Yürütme](https://ai.google.dev/gemini-api/docs/code-execution?hl=tr) | Sunucu tarafı | Desteklenir (yerleşik, `executableCode` ve `codeExecutionResult` parçaları kullanılır) |
| [Bilgisayar Kullanımı](https://ai.google.dev/gemini-api/docs/computer-use?hl=tr) | İstemci tarafı | Desteklenir (yerleşik, `functionCall` ve `functionResponse` parçaları kullanılır) |
| [Özel işlevler](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) | İstemci tarafı | Desteklenir (yerleşik, `functionCall` ve `functionResponse` parçaları kullanılır) |

## Sırada ne var?

- Gemini API'deki [işlev çağrısı](https://ai.google.dev/gemini-api/docs/function-calling?hl=tr) hakkında daha fazla bilgi edinin.
- Desteklenen araçları keşfedin:
  - [Google Arama](https://ai.google.dev/gemini-api/docs/google-search?hl=tr)
  - [Google Haritalar](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=tr)
  - [URL bağlamı](https://ai.google.dev/gemini-api/docs/url-context?hl=tr)
  - [Dosya Arama](https://ai.google.dev/gemini-api/docs/file-search?hl=tr)

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-06-23 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-06-23 UTC."],[],[]]
