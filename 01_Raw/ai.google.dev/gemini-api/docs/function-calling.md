---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=tr
fetched_at: 2026-08-17T02:32:05.993000+00:00
title: "Gemini API ile i\u015flev \u00e7a\u011f\u0131rma \u00a0|\u00a0 Google AI for Developers"
---

[Etkileşimler API'si](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=tr) artık genel kullanıma sunulmuştur. En yeni özelliklere ve modellere erişmek için bu API'yi kullanmanızı öneririz.

![](https://ai.google.dev/_static/images/translated.svg?hl=tr)

Google, içerikleri tercih ettiğiniz dile çevirmek için yapay zeka teknolojisini kullanır. Yapay zeka çevirilerinde hata olabilir.

- [Ana Sayfa](https://ai.google.dev/?hl=tr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=tr)
- [Dokümanlar](https://ai.google.dev/gemini-api/docs?hl=tr)

Geri bildirim gönderin

# Gemini API ile işlev çağırma

İşlev çağırma, modelleri harici araçlara ve API'lere bağlamanıza olanak tanır.
Model, metin yanıtları oluşturmak yerine belirli işlevlerin ne zaman çağrılacağını belirler ve gerçek dünyadaki işlemleri gerçekleştirmek için gerekli parametreleri sağlar.
Bu sayede model, doğal dil ile gerçek dünyadaki işlemler ve veriler arasında köprü görevi görebilir. İşlev çağrısının 3 temel kullanım alanı vardır:

- [**İşlem Yapma:**](#meeting) API'leri kullanarak harici sistemlerle etkileşim kurun. Örneğin, randevu planlayın, fatura oluşturun, e-posta gönderin veya akıllı ev cihazlarını kontrol edin.
- [**Bilgileri Artırma:**](#weather) Veritabanları, API'ler ve bilgi tabanları gibi harici kaynaklardaki bilgilere erişin.
- [**Özellikleri genişletme:**](#chart) Hesaplama yapmak ve modelin sınırlamalarını genişletmek için harici araçlar kullanın (ör. hesap makinesi kullanma veya grafik oluşturma).

Bu kullanım alanlarının örneklerine aşağıdan göz atabilirsiniz:

### Toplantı planlama

Bu örnekte, katılımcılarla belirli bir zamanda toplantı planlayan bir işlevin nasıl tanımlanacağı gösterilmektedir. Bu işlev, modelin kullanıcı isteklerini ayrıştırmasına ve harici sistemlerdeki işlemleri tetiklemek için yapılandırılmış bağımsız değişkenler döndürmesine olanak tanır.

### Python

```
from google import genai

schedule_meeting_function = {
    "type": "function",
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {"type": "array", "items": {"type": "string"}},
            "date": {"type": "string", "description": "Date (e.g., '2024-07-29')"},
            "time": {"type": "string", "description": "Time (e.g., '15:00')"},
            "topic": {"type": "string", "description": "The meeting topic."},
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about Q3 planning.",
    tools=[{"type": "function", **schedule_meeting_function}],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const scheduleMeetingFunction = {
  type: 'function',
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: 'object',
    properties: {
      attendees: { type: 'array', items: { type: 'string' } },
      date: { type: 'string', description: 'Date (e.g., "2024-07-29")' },
      time: { type: 'string', description: 'Time (e.g., "15:00")' },
      topic: { type: 'string', description: 'The meeting topic.' },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.',
  tools: [scheduleMeetingFunction],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about Q3 planning.",
    "tools": [{
        "type": "function",
        "name": "schedule_meeting",
        "description": "Schedules a meeting with specified attendees at a given time and date.",
        "parameters": {
          "type": "object",
          "properties": {
            "attendees": {"type": "array", "items": {"type&quot;: "string"}},
            "date": {"type": "string"},
            "time": {"type": "string"},
            "topic": {"type": "string"}
          },
          "required": ["attendees", "date", "time", "topic"]
        }
    }]
  }'
```

### Hava Durumunu Öğrenme

Bu örnekte, bir konumun sıcaklık verilerini alan bir işlevin nasıl tanımlanacağı gösterilmektedir. Bu sayede model, gerçek zamanlı veya harici bilgi gerektiren sorgulara yanıt vermek için harici API'leri çağırabilir.

### Python

```
from google import genai

weather_function = {
    "type": "function",
    "name": "get_current_temperature",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What's the temperature in London?",
    tools=[weather_function],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherFunctionDeclaration = {
  type: 'function',
  name: 'get_current_temperature',
  description: 'Gets the current temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: {
        type: 'string',
        description: 'The city name, e.g. San Francisco',
      },
    },
    required: ['location'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "What's the temperature in London?",
  tools: [weatherFunctionDeclaration],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What'\''s the temperature in London?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type";: "object",
        "properties": {
          "location": {"type": "string", "description": "The city name"}
        },
        "required": ["location"]
      }
    }]
  }'
```

### Grafik oluşturma

Bu örnekte, yapılandırılmış verilerden çubuk grafik oluşturan bir işlevin nasıl tanımlanacağı gösterilmektedir. Bu sayede, modelin hesaplama yapmak veya görsel öğeler oluşturmak için harici araçları nasıl kullanabileceği gösterilmektedir:

### Python

```
from google import genai

create_chart_function = {
    "type": "function",
    "name": "create_bar_chart",
    "description": "Creates a bar chart given a title, labels, and values.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "The title for the chart."},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}},
        },
        "required": ["title", "labels", "values"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model=";gemini-3.6-flash",
    input="Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
    tools=[create_chart_function],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const createChartFunctionDeclaration = {
  type: 'function',
  name: 'create_bar_chart',
  description: 'Creates a bar chart given a title, labels, and values.',
  parameters: {
    type: 'object',
    properties: {
      title: { type: 'string', description: 'The title for the chart.' },
      labels: { type: 'array', items: { type: 'string' } },
      values: { type: 'array', items: { type: 'number' } },
    },
    required: ['title', 'labels', 'values'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "Create a bar chart titled 'Quarterly Sales' with Q1: 50000, Q2: 75000, Q3: 60000.",
  tools: [createChartFunctionDeclaration],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Create a bar chart titled '\''Quarterly Sales'\'' with Q1: 50000, Q2: 75000, Q3: 60000.",
    "tools": [{
        "type": "function",
        "name": "create_bar_chart",
        "description": "Creates a bar chart given a title, labels, and values.",
        "parameters": {
          "type": "object",
          "properties": {
            "title": {"type": "string"},
            "labels": {"type": "array", "items": {"type": "string"}},
            "values": {"type": "array", "items": {"type": "number"}}
          },
          "required": ["title", "labels", "values"]
        }
    }]
  }'
```

## İşlev çağrısının işleyiş şekli

![İşlev çağrısına genel bakış](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=tr)

İşlev çağırma, uygulamanız, model ve harici işlevler arasında yapılandırılmış bir etkileşimi içerir:

1. **İşlev Bildirimini Tanımla:** İşlevin adını, parametrelerini ve amacını modele tanımlayın.
2. **İşlev bildirimleriyle LLM'yi çağırma:** Kullanıcı istemini, işlev bildirimiyle birlikte modele gönderin.
3. **İşlev Kodunu Yürütme (Sizin Sorumluluğunuz):** Model, işlevi *yürütmez*. Adı ve bağımsız değişkenleri ayıklayıp uygulamanızda yürütün.
4. **Kullanıcı dostu yanıt oluşturma:** Son ve kullanıcı dostu bir yanıt için sonucu modele geri gönderin.

Bu işlem birden fazla dönüşte tekrarlanabilir. Model, tek bir dönüşte ([paralel işlev çağrısı](#parallel_function_calling)) ve sırayla ([bileşik işlev çağrısı](#compositional_function_calling)) birden fazla işlev çağrısını destekler.

### 1. adım: Bir işlev bildirimi tanımlayın

### Python

```
set_light_values_declaration = {
    "type": "function",
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool&>quot;, "warm"],
                "description": "Color temperature",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

def set_light_values(brightness: int, color_temp: str) - dict:
    """Set the brightness and color temperature of a room light."""
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
const setLightValuesTool = {
  type: 'function',
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: 'object',
    properties: {
      brightness: { type: 'number', description: 'Light level from 0 to 100' },
      color_temp: { type: 'string', enum: ['daylight', 'cool', 'warm'] },
    },
    required: ['brightness', 'color_temp'],
  },
};

function setLightValues(brightness, color_temp) {
  return { brightness: brightness, colorTemperature: color_temp };
}
```

### 2. adım: İşlev beyanlarıyla modeli çağırın

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Turn the lights down to a romantic level",
    tools=[set_light_values_declaration],
)

fc_step = next(s for s in interaction.steps if s.type == "function_call")
print(fc_step)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Turn the lights down to a romantic level',
  tools: [setLightValuesTool],
});

const fcStep = in>teraction.steps.find(s = s.type === 'function_call');
console.log(fcStep);
```

Model, `type`, `name` ve `arguments` ile `function_call` adımını döndürüyor:

```
type='function_call'
name='set_light_values'
arguments={'color_temp': &#39;warm', 'brightness': 25}
```

### 3. adım: İşlevi yürütün

### Python

```
fc_step = next(s for s in interaction.steps if s.type == "function_call")

if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)
    print(f"Function execution result: {result}")
```

### JavaScript

```
const fcStep = interaction.steps.find(s => s.type === 'function_call');

let result;
if (fcStep.name === 'set_light_values') {
  result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### 4. adım: Sonucu modele geri gönderin

### Python

```
final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=[
        {
            "type": "function_result",
            "name": fc_step.name,
            "call_id": fc_step.id,
            "result": [{"type": "text", "text": json.dumps(result)}],
        }
    ],
    tools=[set_light_values_declaration],
    previous_interaction_id=interaction.id,
)

print(final_interaction.output_text)
```

### JavaScript

```
const finalInteraction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: [{
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  }],
  tools: [setLightValuesTool],
  previous_interaction_id: interaction.id,
});

console.log(finalInteraction.output_text);
```

### Durum bilgisiz işlev çağrısı

Ayrıca, istemci tarafında sohbet geçmişini yönetip `store=false` ayarını yaparak işlev çağrısını durumsuz modda da kullanabilirsiniz.

Durum bilgisiz modda, görüşmenin tam geçmişini sonraki her isteğin `input` alanına iletmeniz gerekir. Bu geçmiş şunları içermelidir:
1. İlk `user_input` adım.
2. 1. dönüşte döndürülen tüm model tarafından oluşturulan adımlar (`thought` ve `function_call` adımları dahil) alındığı gibi.
3. Çalıştırılan işlevinizin çıkışını içeren `function_result` adımı.

### Python

```
from google import genai
import json

client = genai.Client()

history = [
    {
        "type": "user_input",
        "content": [{"type": "text", "text": "Turn the lights down to a romantic level"}]
    }
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

for step in interaction.steps:
    history.append(step.model_dump())

fc_step = next(s for s in interaction.steps if s.type == "function_call")
if fc_step.name == "set_light_values":
    result = set_light_values(**fc_step.arguments)

history.append({
    "type": "function_result",
    "name": fc_step.name,
    "call_id": fc_step.id,
    "result": [{"type": "text", "text": json.dumps(result)}],
})

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    store=False,
    input=history,
    tools=[set_light_values_declaration],
)

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

async function main() {
  const history = [
    {
      type: "user_input",
      content: [{ type: "text", text: "Turn the lights down to a romantic level" }]
    }
  ];

  const interaction = await client.interactions.create({
    model: "gemini-3.6-flash",
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  history.push(...interaction.st>eps);

  const fcStep = interaction.steps.find(s = s.type === 'function_call');
  let result;
  if (fcStep.name === 'set_light_values') {
    result = setLightValues(fcStep.arguments.brightness, fcStep.arguments.color_temp);
  }

  history.push({
    type: 'function_result',
    name: fcStep.name,
    call_id: fcStep.id,
    result: [{ type: 'text', text: JSON.stringify(result) }]
  });

  const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    store: false,
    input: history,
    tools: [setLightValuesTool],
  });

  console.log(finalInteraction.output_text);
}

await main();
```

### REST

```
# Turn 1: Send request with tools and store: false
RESPONSE1=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "store": false,
    "input": [
      {
        "type": "user_input",
        "content": "Turn the lights down to a romantic level"
      }
    ],
    "tools": [{
      "type": "function",
      "name": "set_light_values",
      "description": "Sets the brightness and color temperature of a light.",
      "parameters": {
        "type": "object",
        "properties": {
          "brightness": {"type": "integer", "description": "Light level from 0 to 100"},
          "color_temp": {"type": "string", "enum": ["daylight", "cool", "warm"]}
        },
        "required": ["brightness", "color_temp"]
      }
    }]
  }')

# Extract model steps (thought, function_call)
MODEL_STEPS=$(echo "$RESPONSE1" | jq '.steps')

# Extract function call details to execute
FC_NAME=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .name')
FC_ID=$(echo "$RESPONSE1" | jq -r '.steps[] | select(.type=="function_call") | .id')

# Assume local execution returns: {"brightness": 25, "colorTemperature": "warm"}
RESULT="{\"brightness\": 25, \"colorTemperature\": \"warm\"}"

# Reconstruct history for Turn 2
HISTORY=$(jq -n \
  --argjson first_input '[{"type": "user_input", "content": "Turn the lights down to a romantic level"}]' \
  --argjson model_steps "$MODEL_STEPS" \
  --arg fc_name "$FC_NAME" \
  --arg fc_id "$FC_ID" \
  --arg result "$RESULT" \
  '$first_input + $model_steps + [{"type": "function_result", "name": $fc_name, "call_id": $fc_id, "result": [{"type": "text", "text": $result}]}]')

# Turn 2: Send the full history
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"model\": \"gemini-3.6-flash\",
    \"store\": false,
    \"input\": $HISTORY,
    \"tools\": [{
      \"type\": \"function\",
      \"name\": \"set_light_values\",
      \"description\": \"Sets the brightness and color temperature of a light.\",
      \"parameters\": {
        \"type\": \"object\",
        \"properties\": {
          \"brightness\": {\"type\": \"integer\"},
          \"color_temp\": {\"type\": \"string\"}
        },
        \"required\": [\"brightness\", \"color_temp\"]
      }
    }]
  }"
```

## İşlev beyanları

İşlev bildirimi, araç olarak iletilir ve şunları içerir:

- `type` (dize): Özel işlevler için `"function"` olmalıdır.
- `name` (dize): Benzersiz işlev adı (alt çizgi veya camelCase kullanın).
- `description` (dize): İşlevin amacının net açıklaması.
- `parameters` (nesne): İşlevin beklediği giriş parametreleri.
  - `type` (dize): Genel veri türü (ör. `object`).
  - `properties` (nesne): Tür ve açıklamaya sahip bireysel parametreler.
  - `required` (dizi): Zorunlu parametre adları.

## Düşünebilen modellerle işlev çağırma

Gemini 3 serisi modeller, işlev çağrısını iyileştiren dahili bir ["düşünme"](https://ai.google.dev/gemini-api/docs/thinking?hl=tr) süreci kullanır. SDK'lar, [düşünce imzalarını](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=tr) sizin için otomatik olarak işler.

## Paralel işlev çağırma

Bağımsız olduklarında aynı anda birden fazla işlevi çağırma:

### Python

```
power_disco_ball = {"type": "function", "name": "power_disco_ball", "description": "Powers the disco ball.",
    "parameters": {"type": "object", "properties": {"power": {"type": "boolean"}}, "required": ["power"]}}
start_music = {"type": "function", "name": "start_music", "description": "Play music.",
    "parameters": {"type": "object", "properties": {"energetic": {"type": "boolean"}, "loud": {"type": "boolean"}}, "required": ["energetic", "loud"]}}
dim_lights = {"type": "function", "name": "dim_lights", "description": "Dim the lights.",
    "parameters": {"type": "object", "properties": {"brightness": {"type": "number"}}, "required": ["brightness"]}}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Turn this place into a party!",
    tools=[power_disco_ball, start_music, dim_lights],
    generation_config={"tool_choice": "any"},
)

for step in interaction.steps:
    if step.type == "function_call":
        args = ", ".join(f"{key}={val}" for key, val in step.arguments.items())
        print(f"{step.name}({args})")
```

### JavaScript

```
const powerDiscoBall = { type: 'function', name: 'power_disco_ball', description: 'Powers the disco ball.',
  parameters: { type: 'object', properties: { power: { type: 'boolean' } }, required: ['power'] } };
const startMusic = { type: 'function', name: 'start_music', description: 'Play music.',
  parameters: { type: 'object', properties: { energetic: { type: 'boolean' }, loud: { type: 'boolean' } }, required: ['energetic', 'loud'] } };
const dimLights = { type: 'function', name: 'dim_lights', description: 'Dim the lights.',
  parameters: { type: 'object', properties: { brightness: { type: 'number' } }, required: ['brightness'] } };

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: 'Turn this place into a party!',
  tools: [powerDiscoBall, startMusic, dimLights],
  generation_config: { tool_choice: 'any' },
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`${step.name}(${JSON.stringify(step.arguments)})`);
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "Turn this place into a party!",
    "tools": [
      {
        "type": "function",
        "name": "power_disco_ball",
        "description": "Powers the disco ball.",
        "parameters": {
          "type": "object",
          "properties": {
            "power": {"type": "boolean"}
          },
          "required": ["power"]
        }
      },
      {
        "type": "function",
        "name": "start_music",
        "description": "Play music.",
        "parameters": {
          "type": "object",
          "properties": {
            "energetic": {"type": "boolean"},
            "loud": {"type": "boolean&quot;}
          },
          "required": ["energetic", "loud"]
        }
      },
      {
        "type": "function",
        "name": "dim_lights",
        "description": "Dim the lights.",
        "parameters": {
          "type": "object",
          "properties": {
            "brightness": {"type": "number"}
          },
          "required": ["brightness"]
        }
      }
    ]
  }'
```

## Bileşik işlev çağrısı

Karmaşık istekler için birden fazla işlev çağrısını birlikte zincirleyin (ör. önce konumu alın, ardından bu konumun hava durumunu alın).

### Python

```
get_weather_forecast_declaration = {
    "type": "function",
    "name": "get_weather_forecast",
    "description": "Gets the current weather temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The location"},
        },
        "required": ["location"],
    },
}

set_thermostat_temperature_declaration = {
    "type": "function",
    "name": "set_thermostat_temperature",
    "description": "Sets the thermostat to a desired temperature.",
    "parameters": {
        "type": "object",
        "properties": {
            "temperature": {
                "type": "integer",
                "description": "The temperature in Celsius",
            },
        },
        "required": ["temperature"],
    },
}

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    tools=[
        get_weather_forecast_declaration,
        set_thermostat_temperature_declaration,
    ],
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function to call: {step.name}")
        print(f"Arguments: {step.arguments}")
    elif hasattr(step, "content") and step.content:
         for part in step.content:
             if hasattr(part, "text"):
                 print(part.text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const getWeatherForecastTool = {
  type: 'function',
  name: 'get_weather_forecast',
  description: 'Gets the current weather temperature for a given location.',
  parameters: {
    type: 'object',
    properties: {
      location: { type: 'string', description: 'The location' },
    },
    required: ['location'],
  },
};

const setThermostatTemperatureTool = {
  type: 'function',
  name: 'set_thermostat_temperature',
  description: 'Sets the thermostat to a desired temperature.',
  parameters: {
    type: 'object',
    properties: {
      temperature: {
        type: 'integer',
        description: 'The temperature in Celsius',
      },
    },
    required: ['temperature'],
  },
};

const interaction = await client.interactions.create({
  model: 'gemini-3.6-flash',
  input: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
  tools: [
    getWeatherForecastTool,
    setThermostatTemperatureTool,
  ],
});

for (const step of interaction.steps) {
  if (step.type === 'function_call') {
    console.log(`Function to call: ${step.name}`);
    console.log(`Arguments: ${JSON.stringify(step.arguments)}`);
  } else if (step.content) {
    for (const part of step.content) {
      if (part.text) {
        console.log(part.text);
      }
    }
  }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "If it'\''s warmer than 20°C in London, set the thermostat to 20°C, otherwise 18°C.",
    "tools": [
      {
        "type": "function",
        "name": "get_weather_forecast",
        "description": "Gets the current weather temperature for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string"}
          },
          "required": ["location"]
        }
      },
      {
        "type": "function",
        "name": "set_thermostat_temperature&quot;,
        "description": "Sets the thermostat to a desired temperature.",
        "parameters": {
          "type": "object",
          "properties": {
            "temperature": {"type": "integer"}
          },
          "required": ["temperature"]
        }
      }
    ]
  }'
```

## İşlev çağırma modları

`generation_config` içindeki `tool_choice` seçeneğini kullanarak modelin araçları nasıl kullanacağını kontrol edin:

- `auto` (Varsayılan): Model, bir işlevi çağırmaya mı yoksa doğrudan yanıt vermeye mi karar verir.
- `any`: Model, her zaman bir işlev çağrısı tahmin edecek şekilde sınırlandırılmıştır.
- `none`: Modelin işlev çağrıları yapması yasaktır.
- `validated`: Model, işlev şemasına uygunluğu sağlar.

### Python

```
generation_config = {
    "tool_choice": {
        "allowed_tools": {
            "mode": "any",
            "tools&quot;: ["get_current_temperature"]
        }
    }
}
```

### JavaScript

```
const generation_config = {
  tool_choice: {
    allowed_tools: {
      mode: 'any',
      tools: ['get_current_temperature';]
    }
  }
};
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the temperature in Boston?",
    "tools": [{
      "type": "function",
      "name": "get_current_temperature",
      "description": "Gets the current temperature for a given location.",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string"}
        },
        "required": ["location"]
      }
    }],
    "generation_config": {
      "tool_choice": {
        "allowed_tools": {
          "mode": "any",
          "tools": ["get_current_temperature"]
        }
      }
    }
  }'
```

## Çok amaçlı araç kullanımı

Yerleşik araçları işlev çağrısıyla birleştirerek aynı istekte birden fazla aracı etkinleştirebilirsiniz. Gemini 3 modelleri, Etkileşimler'de yerleşik araçları kullanıma hazır işlev çağrılarıyla birleştirebilir. `previous_interaction_id` iletildiğinde yerleşik araç bağlamı otomatik olarak dolaşıma girer.

### Python

```
from google import genai
import json

client = genai.Client()

get_weather = {
    "type": "function",
    "name": "get_weather",
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

tools = [
    {"type": "google_search"},
    get_weather               
]

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the northernmost city in the United States? What's the weather like there today?",
    tools=tools
)

for step in interaction.steps:
    if step.type == "function_call":
        print(f"Function call: {step.name} (ID: {step.id})")
        result = {"response": "Very cold. 22 degrees Fahrenheit."}
        interaction_2 = client.interactions.create(
            model="gemini-3.6-flash",
            previous_interaction_id=interaction.id,
            tools=tools,
            input=[{
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [{"type": "text", "text": json.dumps(result)}]
            }]
        )

        print(interaction_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state, e.g. San Francisco, CA' }
        },
        required: ['location']
    }
};

const tools = [
    {type: 'google_search'}, // Built-in tool
    weatherTool            
];

let interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: "What is the northernmost city in the United States? What's the weather like there today?",
    tools: tools
});

for (const step of interaction.steps) {
    if (step.type === 'function_call') {
        console.log(`Function call: ${step.name} (ID: ${step.id})`);
        const result = {response: "Very cold. 22 degrees Fahrenheit."};
        const interaction_2 = await client.interactions.create({
            model: 'gemini-3.6-flash',
            previous_interaction_id: interaction.id,
            tools: tools,
            input: [{
                type: 'function_result',
                name: step.name,
                call_id: step.id,
                result: [{ type: 'text', text: JSON.stringify(result) }]
            }]
        });

        console.log(interaction_2.output_text);
    }
}
```

### REST

```
# Turn 1: Send request with built-in google_search tool and custom weather tool
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "input": "What is the northernmost city in the United States? What'\''s the weather like there today?",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ]
  }'

# Turn 2: Provide function result and pass previous_interaction_id
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "INTERACTION_ID",
    "tools": [
      {"type": "google_search"},
      {
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
          &quot;type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}
          },
          "required": ["location"]
        }
      }
    ],
    "input": [
      {
        "type": "function_result",
        "name": "get_weather",
        "call_id": "call_123",
        "result": [{"type": "text", "text": "{\"response\": \"Very cold. 22 degrees Fahrenheit.\"}"}]
      }
    ]
  }'
```

## Çok formatlı işlev yanıtları

Gemini 3 serisi modeller için, modele gönderdiğiniz işlev yanıtı bölümlerine çok formatlı içerik ekleyebilirsiniz. Model, daha bilinçli bir yanıt üretmek için bu çok formatlı içeriği bir sonraki turda işleyebilir.

Bir işlev yanıtına çok formatlı veriler eklemek için bu verileri `function_result` adımının `result` alanına bir veya daha fazla içerik bloğu olarak ekleyin. Her içerik bloğu `type` değerini belirtmelidir (ör. `"text"`, `"image"`).

Aşağıdaki örnekte, bir etkileşimde görüntü verileri içeren bir işlev yanıtının modele nasıl geri gönderileceği gösterilmektedir:

### Python

```
import base64
from google import genai
import requests

client = genai.Client()

tool_call = next(s for s in interaction.steps if s.type == "function_call")

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content

base64_image_data = base64.b64encode(image_bytes).decode("utf-8")

final_interaction = client.interactions.create(
    model="gemini-3.6-flash",
    previous_interaction_id=interaction.id,
    input=[
        {
            "type": "function_result",
            "name": tool_call.name,
            "call_id": tool_call.id,
            "result": [
                {"type": "text", "text": "instrument.jpg"},
                {
                    "type": "image",
                    "mime_type": "image/jpeg",
                    "data": base64_image_data,
                },
            ],
        }
    ],
)

print(final_interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const toolCall = interaction.step>s.find(s = s.type === 'function_call');

const base64ImageData = "BASE64_IMAGE_DATA";

const finalInteraction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    previous_interaction_id: interaction.id,
    input: [{
        type: 'function_result',
        name: toolCall.name,
        call_id: toolCall.id,
        result: [
            { type: 'text', text: 'instrument.jpg' },
            {
                type: 'image',
                mime_type: 'image/jpeg',
                data: base64ImageData,
            }
        ]
    }]
});

console.log(finalInteraction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemini-3.6-flash",
    "previous_interaction_id": "INTERACTION_ID",
    "input": [
      {
        "type": "function_result",
        "name": "get_image",
        "call_id": "call_123",
        "result": [
          {"type": "text", "text": "instrument.jpg"},
          {
            "type": "image",
            "mime_type": "image/jpeg",
            "data": "BASE64_IMAGE_DATA"
          }
        ]
      }
    ]
  }'
```

## Yapılandırılmış çıkışla işlev çağırma

Gemini 3 serisi modellerde, işlev çağrısını [yapılandırılmış çıkışla](https://ai.google.dev/gemini-api/docs/structured-output?hl=tr) birleştirerek tutarlı biçimde biçimlendirilmiş yanıtlar alın.

## Uzak MCP (Model Context Protocol)

Etkileşimler API'si, modele harici araçlara ve hizmetlere erişim sağlamak için uzak MCP sunucularına bağlanmayı destekler. Araç yapılandırmasında sunucu `name` ve `url` bilgilerini siz sağlarsınız.

Uzak MCP'yi kullanırken aşağıdaki kısıtlamalara dikkat edin:

- **Sunucu türleri**: Uzak MCP yalnızca akışa uygun HTTP sunucularıyla çalışır. SSE (Server-Sent Events) sunucuları desteklenmez.
- **Adlandırma**: MCP sunucusu adları `-` karakterini içermemelidir. Bunun yerine `snake_case` sunucu adlarını kullanın.

| Alan | Tür | Zorunlu | Açıklama |
| --- | --- | --- | --- |
| `type` | `string` | Evet | `"mcp_server"` olmalıdır. |
| `name` | `string` | Hayır | MCP sunucusunun görünen adı. |
| `url` | `string` | Hayır | MCP sunucusu uç noktasının tam URL'si. |
| `headers` | `object` | Hayır | Sunucuya yapılan her istekle birlikte HTTP başlıkları olarak gönderilen anahtar/değer çiftleri (örneğin, kimlik doğrulama jetonları). |
| `allowed_tools` | `array` | Hayır | Ajanın sunucudan hangi araçları çağırabileceğini kısıtlayın. |

### Örnek

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="Check the weather in San Francisco.",
    tools=[
        {
            "type": "mcp_server",
            "name": "weather",
            "url";: "https://gemini-api-demos.uc.r.appspot.com/mcp",
        }
    ]
)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'Check the weather in San Francisco.',
    tools: [
        {
            type: 'mcp_server',
            name: 'weather',
            url: 'https://gemini-api-demos.uc.r.appspot.com/mcp'
        }
    ]
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.6-flash",
    "input": "Check the weather in San Francisco.",
    "tools": [
        {
            "type": "mcp_server",
            &quot;name": "weather",
            "url": "https://gemini-api-demos.uc.r.appspot.com/mcp"
        }
    ]
}'
```

## Araç çağrılarını yayınlama

Model, akışla birlikte kullanılan araçlarda akışta `step.delta` etkinlikleri dizisi olarak işlev çağrıları oluşturur. Araç bağımsız değişkenleri, `arguments` kullanılarak kısmi bağımsız değişkenler olarak yayınlanabilir. Bu farkları, tam araç çağrılarını yeniden oluşturmak için toplamanız gerekir.

### Python

```
import json
from google import genai

client = genai.Client()

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Gets the weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The city and state"}
        },
        "required": ["location"]
    }
}

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="What is the weather in Paris?",
    tools=[weather_tool],
    stream=True
)

current_calls = {}
tool_calls = []

for event in stream:
    if event.event_type == "step.start":
        if event.step.type == "function_call":
            current_calls[event.index] = {
                "id": event.step.id,
                "name": event.step.name,
                "arguments": ""
            }
            if hasattr(event.step, "arguments") and event.step.arguments:
                if isinstance(event.step.arguments, dict):
                    current_calls[event.index]["arguments"] = json.dumps(event.step.arguments)
                else:
                    current_calls[event.index]["arguments"] = event.step.arguments
    elif event.event_type == "step.delta":
        if event.delta.type == "arguments":
            if event.index in current_calls:
                current_calls[event.index]["arguments"] += event.delta.partial_arguments
        elif event.delta.type == "text":
            print(event.delta.text, end="", flush=True)

    elif event.event_type == "interaction.completed":
        for index, call in current_calls.items():
            args = call["arguments"]
            if args:
                args = json.loads(args)
            else:
                args = {}

            tool_calls.append({
                "type": "function_call",
                "id": call["id"],
                "name": call["name"],
                "arguments": args
            })

        print(f"\nFinal tool calls ready to execute:")
        print(json.dumps(tool_calls, indent=2))
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

const client = new GoogleGenAI({});

const weatherTool = {
    type: 'function',
    name: 'get_weather',
    description: 'Gets the weather for a given location.',
    parameters: {
        type: 'object',
        properties: {
            location: { type: 'string', description: 'The city and state' }
        },
        required: ['location']
    }
};

const stream = await client.interactions.create({
    model: 'gemini-3.6-flash',
    input: 'What is the weather in Paris?',
    tools: [weatherTool],
    stream: true,
});

const currentCalls = new Map();
let toolCalls = [];

for await (const event of stream) {
    const evType = event.event_type;
    if (evType === 'step.start') {
        if (event.step.type === 'function_call') {
            currentCalls.set(event.index, {
                id: event.step.id,
                name: event.step.name,
                arguments: ''
            });
            if (event.step.arguments) {
                if (typeof event.step.arguments === 'object') {
                    currentCalls.get(event.index).arguments = JSON.stringify(event.step.arguments);
                } else {
                    currentCalls.get(event.index).arguments = event.step.arguments;
                }
            }
        }
    } else if (evType === 'step.delta') {
        if (event.delta.type === 'arguments') {
            if (currentCalls.has(event.index)) {
                currentCalls.get(event.index).arguments += event.delta.partial_arguments;
            }
        } else if (event.delta.type === 'text') {
            process.stdout.write(event.delta.text);
        }
    } else if (evT>ype === 'interaction.completed' || evType === 'interaction.complete') {
        toolCalls = Array.from(currentCalls.values()).map(call = ({
            type: 'function_call',
            id: call.id,
            name: call.name,
            arguments: call.arguments ? JSON.parse(call.arguments) : {}
        }));
        console.log('\nFinal tool calls ready to execute:');
        console.log(JSON.stringify(toolCalls, null, 2));
    }
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions?alt=sse" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "model": "gemini-3.6-flash",
    "input": "What is the weather in Paris?",
    "tools": [{
        "type": "function",
        "name": "get_weather",
        "description": "Gets the weather for a given location.",
        "parameters": {
            "type": "object",
            "properties&quot;: {
                "location": {"type": "string", "description": "The city and state"}
            },
            "required": ["location"]
        }
    }],
    "stream": true
}'
```

## En iyi uygulamalar

- **İşlev ve Parametre Açıklamaları:** Net ve spesifik olun.
- **Adlandırma:** Boşluk veya özel karakter içermeyen açıklayıcı adlar kullanın.
- **Güçlü Tür Belirleme:** Belirli türleri (tam sayı, dize, enum) kullanın.
- **Araç Seçimi:** Etkin araç sayısını en fazla 10-20 olarak ayarlayın.
- **İstem Mühendisliği:** Bağlam ve talimatlar sağlayın.
- **Doğrulama:** İşlev çağrılarını yürütmeden önce doğrulayın.
- **Hata İşleme:** Hataların etkili bir şekilde yönetilmesini sağlayın.
- **Güvenlik:** Harici API'ler için uygun kimlik doğrulama yöntemini kullanın.

## Araç öncesi metin şartları için geçici çözümler

**Sorun:** İsteminizde modelin yapılandırılmış metin (XML, YAML, JSON vb.) çıkışı vermesi gerekiyorsa (ör. `<UPDATE>...</UPDATE>`) hemen önce yapıldığında araç çağrısı bazen `Malformed_Function_Call` ile başarısız olabilir.

**Çözümler:** Aşağıdaki geçici çözümler bu sorunu giderir:

- **TERCİH EDİLEN:** Modele, araç öncesi notlarını ham metin yerine özel bir `update()` işlev çağrısının içine yerleştirmesini söyleyin (ayrıntılar aşağıda).
- Modele, notları yapılandırılmış metin yerine Markdown başlıkları (`# UPDATE`, `## PLAN`) olarak yazmasını söyleyin.
- Modelin, araç çağrılarından önce metin çıkışı yapmasını zorunlu kılmayın.

### Tercih edilen geçici çözüm: Çalışma notlarını özel bir işlev çağrısına sarmalama

Orijinal talimat yerine:

```
Before calling a tool, in every response you MUST first output a single `<UPDATE>` part as specified, don't skip this part or any of required sub-tags with<in `UP>DATE`.
```

Güncellenen bu talimatı kullanın:

```
Before calling any other tool, in every response you MUST first call `update` with all required parameters (previous_step, plan, next_step, external).
```

Ayrıca, müşteri isteğindeki eski `<UPDATE>` XML biçimine yapılan tüm referansları güncelleyin. Ardından, güncelleme işlevi için ilgili işlev beyanını ekleyin:

```
{
  "name": "update",
  "description": "Update working notes (previous step analysis, plan, next step, external note).",
  "parameters": {
    "type": "OBJECT",
    "properties": {
      "previous_step": {
        "type": "STRING",
        "description": "Key findings and outcomes since the previous step."
      },
      "plan": {
        "type": "STRING",
        "description": "The current status of the plan."
      },
      "next_step": {
        "type": "STRING",
        "description": "Brief explanation of the immediate next action according to the plan."
      },
      "external": {
        ";type": "STRING",
        "description": "A short, plain-language note shown to the User about what you are ABOUT TO DO next."
      }
    },
    "required": [
      "previous_step",
      "plan",
      "next_step",
      "external"
    ]
  }
}
```

Ardından model, aynı adımda iki çağrı yapar: yapılandırılmış XML'nin yerini alan `update()` çağrısı ve yapmak istediği gerçek işlev çağrısı.

## Notlar ve sınırlamalar

- Yalnızca [OpenAPI şemasının bir alt kümesi](https://ai.google.dev/api/rest/v1beta/cachedContents?hl=tr#FunctionDeclaration) desteklenir.
- `any` modunda API, çok büyük veya derin iç içe yerleştirilmiş şemaları reddedebilir.
- Python'da desteklenen parametre türleri sınırlıdır.

Geri bildirim gönderin

Aksi belirtilmediği sürece bu sayfanın içeriği [Creative Commons Atıf 4.0 Lisansı](https://creativecommons.org/licenses/by/4.0/) altında ve kod örnekleri [Apache 2.0 Lisansı](https://www.apache.org/licenses/LICENSE-2.0) altında lisanslanmıştır. Ayrıntılı bilgi için [Google Developers Site Politikaları](https://developers.google.com/site-policies?hl=tr)'na göz atın. Java, Oracle ve/veya satış ortaklarının tescilli ticari markasıdır.

Son güncelleme tarihi: 2026-07-30 UTC.

Bize geri bildirimde bulunmak mı istiyorsunuz?

[[["Anlaması kolay","easyToUnderstand","thumb-up"],["Sorunumu çözdü","solvedMyProblem","thumb-up"],["Diğer","otherUp","thumb-up"]],[["İhtiyacım olan bilgiler yok","missingTheInformationINeed","thumb-down"],["Çok karmaşık / çok fazla adım var","tooComplicatedTooManySteps","thumb-down"],["Güncel değil","outOfDate","thumb-down"],["Çeviri sorunu","translationIssue","thumb-down"],["Örnek veya kod sorunu","samplesCodeIssue","thumb-down"],["Diğer","otherDown","thumb-down"]],["Son güncelleme tarihi: 2026-07-30 UTC."],[],[]]
