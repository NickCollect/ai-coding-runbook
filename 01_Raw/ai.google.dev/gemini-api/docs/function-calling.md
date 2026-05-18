---
source_url: https://ai.google.dev/gemini-api/docs/function-calling?hl=id
fetched_at: 2026-05-18T05:12:05.219523+00:00
title: "Gemini generateContent API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [generateContent API](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Panggilan fungsi dengan Gemini API

Panggilan fungsi memungkinkan Anda menghubungkan model ke alat dan API eksternal.
Daripada membuat respons teks, model menentukan kapan harus memanggil fungsi tertentu dan memberikan parameter yang diperlukan untuk menjalankan tindakan di dunia nyata.
Hal ini memungkinkan model bertindak sebagai jembatan antara bahasa alami dan tindakan serta data dunia nyata. Panggilan fungsi memiliki 3 kasus penggunaan utama:

- **Meningkatkan Pengetahuan:** Mengakses informasi dari sumber eksternal seperti database, API, dan pusat informasi.
- **Memperluas Kemampuan:** Menggunakan alat eksternal untuk melakukan komputasi dan memperluas batasan model, seperti menggunakan kalkulator atau membuat diagram.
- **Mengambil Tindakan:** Berinteraksi dengan sistem eksternal menggunakan API, seperti
  menjadwalkan janji temu, membuat invoice, mengirim email, atau mengontrol
  perangkat smart home.

Get Weather
Schedule Meeting
Create Chart

### Python

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"ID: {function_call.id}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{
      functionDeclarations: [scheduleMeetingFunctionDeclaration]
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`ID: ${functionCall.id}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

### REST

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."
          }
        ]
      }
    ],
    "tools": [
      {
        "functionDeclarations": [
          {
            "name": "schedule_meeting",
            "description": "Schedules a meeting with specified attendees at a given time and date.",
            "parameters": {
              "type": "object",
              "properties": {
                "attendees": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "List of people attending the meeting."
                },
                "date": {
                  "type": "string",
                  "description": "Date of the meeting (e.g., '2024-07-29')"
                },
                "time": {
                  "type": "string",
                  "description": "Time of the meeting (e.g., '15:00')"
                },
                "topic": {
                  "type": "string",
                  "description": "The subject or topic of the meeting."
                }
              },
              "required": ["attendees", "date", "time", "topic"]
            }
          }
        ]
      }
    ]
  }'
```

## Cara kerja panggilan fungsi

![ringkasan
panggilan fungsi](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png?hl=id)

Panggilan fungsi melibatkan interaksi terstruktur antara aplikasi Anda, model, dan fungsi eksternal. Berikut perincian prosesnya:

1. **Tentukan deklarasi fungsi:** Tentukan deklarasi fungsi dalam kode aplikasi Anda. Deklarasi Fungsi menjelaskan nama,
   parameter, dan tujuan fungsi ke model.
2. **Memanggil API dengan deklarasi fungsi:** Kirim perintah pengguna beserta
   deklarasi fungsi ke model. Alat ini menganalisis permintaan dan menentukan
   apakah panggilan fungsi akan bermanfaat. Jika ya, model akan merespons dengan objek JSON terstruktur
   yang berisi nama fungsi, argumen, dan `id` unik
   (`id` ini kini selalu ditampilkan oleh API untuk model Gemini 3\*).
3. **Jalankan kode fungsi (tanggung jawab Anda):** Model *tidak*
   menjalankan fungsi itu sendiri. Aplikasi Anda bertanggung jawab untuk
   memproses respons dan memeriksa panggilan fungsi. Jika
   - **Ya**: Ekstrak nama, argumen, dan `id` fungsi, lalu jalankan
     fungsi yang sesuai di aplikasi Anda.
   - **Tidak:** Model telah memberikan respons teks langsung terhadap perintah
     (alur ini kurang ditekankan dalam contoh, tetapi merupakan kemungkinan hasil).
4. **Buat respons yang mudah dipahami pengguna:** Jika fungsi dijalankan, ambil
   hasilnya dan kirim kembali ke model, pastikan Anda menyertakan `id` yang cocok
   dalam giliran percakapan berikutnya. LLM akan menggunakan hasilnya untuk membuat respons akhir yang mudah digunakan dan menggabungkan informasi dari panggilan fungsi.

Proses ini dapat diulang di beberapa giliran, sehingga memungkinkan interaksi dan alur kerja yang kompleks. Model ini juga mendukung pemanggilan beberapa fungsi
dalam satu giliran ([panggilan fungsi paralel](#parallel_function_calling)), secara
berurutan ([panggilan fungsi komposit](#compositional_function_calling)),
dan dengan alat Gemini bawaan ([penggunaan multi-alat](#native-tools)).

\* **Selalu petakan ID fungsi:** Gemini 3 kini selalu menampilkan
`id` unik dengan setiap `functionCall`. Sertakan `id` ini persis seperti yang ada di
`functionResponse` agar model dapat memetakan hasil Anda secara akurat kembali ke
permintaan asli.

### Langkah 1: Tentukan deklarasi fungsi

Tentukan fungsi dan deklarasinya dalam kode aplikasi yang memungkinkan
pengguna menyetel nilai cahaya dan membuat permintaan API. Fungsi ini dapat memanggil
layanan atau API eksternal.

### Python

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
```

### JavaScript

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}
```

### Langkah 2: Panggil model dengan deklarasi fungsi

Setelah menentukan deklarasi fungsi, Anda dapat meminta model untuk
menggunakannya. Model ini menganalisis perintah dan deklarasi fungsi serta memutuskan apakah akan merespons secara langsung atau memanggil fungsi. Jika fungsi dipanggil, objek respons akan berisi saran panggilan fungsi.

### Python

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [
    types.Content(
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]
    )
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{
    functionDeclarations: [setLightValuesFunctionDeclaration]
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [
  {
    role: 'user',
    parts: [{ text: 'Turn the lights down to a romantic level' }]
  }
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

Kemudian, model akan menampilkan objek `functionCall` dalam skema yang kompatibel dengan OpenAPI yang menentukan cara memanggil satu atau beberapa fungsi yang dideklarasikan untuk merespons pertanyaan pengguna.

### Python

```
id='8f2b1a3c' args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

### JavaScript

```
{
  id: '8f2b1a3c',
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}
```

### Langkah 3: Jalankan kode fungsi set\_light\_values

Ekstrak detail panggilan fungsi dari respons model, uraikan argumen
, dan jalankan fungsi `set_light_values`.

### Python

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")
```

### JavaScript

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### Langkah 4: Buat respons yang mudah dipahami pengguna dengan hasil fungsi dan panggil model lagi

Terakhir, kirim hasil eksekusi fungsi kembali ke model agar model dapat menggabungkan informasi ini ke dalam respons akhirnya kepada pengguna.

### Python

```
from google import genai
from google.genai import types

# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
    id=tool_call.id,
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

client = genai.Client()
final_response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=config,
    contents=contents,
)

print(final_response.text)
```

### JavaScript

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result },
  id: tool_call.id
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

Tindakan ini menyelesaikan alur panggilan fungsi. Model berhasil menggunakan fungsi `set_light_values` untuk melakukan tindakan permintaan pengguna.

## Deklarasi fungsi

Saat menerapkan panggilan fungsi dalam perintah, Anda membuat objek `tools`,
yang berisi satu atau beberapa `function declarations`. Anda menentukan fungsi menggunakan
JSON, khususnya dengan [subset pilihan](https://ai.google.dev/api/caching?hl=id#Schema)
dari format [skema OpenAPI](https://spec.openapis.org/oas/v3.0.3#schemaw). Deklarasi
fungsi tunggal dapat mencakup parameter berikut:

- `name` (string): Nama unik untuk fungsi (`get_weather_forecast`,
  `send_email`). Gunakan nama deskriptif tanpa spasi atau karakter khusus
  (gunakan garis bawah atau camelCase).
- `description` (string): Penjelasan yang jelas dan mendetail tentang tujuan dan kemampuan fungsi. Hal ini sangat penting agar model memahami kapan harus menggunakan fungsi tersebut. Bersikaplah spesifik dan berikan contoh jika diperlukan ("Menemukan bioskop berdasarkan lokasi dan secara opsional judul film yang saat ini diputar di bioskop").
- `parameters` (objek): Menentukan parameter input yang diharapkan fungsi.
  - `type` (string): Menentukan jenis data keseluruhan, seperti `object`.
  - `properties` (objek): Mencantumkan setiap parameter, masing-masing dengan:
    - `type` (string): Jenis data parameter, seperti `string`,
      `integer`, `boolean, array`.
    - `description` (string): Deskripsi tujuan dan format parameter. Berikan contoh dan batasan ("Kota dan negara bagian, misalnya, 'San Francisco, CA' atau kode pos, misalnya, '95616'").
    - `enum` (array, opsional): Jika nilai parameter berasal dari set
      tetap, gunakan "enum" untuk mencantumkan nilai yang diizinkan, bukan hanya
      mendeskripsikannya dalam deskripsi. Hal ini meningkatkan akurasi ("enum":
      ["daylight", "cool", "warm"]).
  - `required` (array): Array string yang mencantumkan nama parameter yang
    wajib agar fungsi dapat beroperasi.

Anda juga dapat membuat `FunctionDeclarations` langsung dari fungsi Python menggunakan
`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Panggilan fungsi dengan model penalaran

Model seri Gemini 3 dan 2.5 menggunakan proses ["penalaran"](https://ai.google.dev/gemini-api/docs/thinking?hl=id) internal untuk memproses permintaan. Peningkatan ini secara signifikan meningkatkan performa panggilan fungsi, sehingga model dapat menentukan dengan lebih baik kapan harus memanggil fungsi dan parameter mana yang harus digunakan. Karena Gemini API tidak memiliki status, model menggunakan
[tanda tangan pemikiran](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id) untuk mempertahankan konteks
di seluruh percakapan multi-giliran.

Bagian ini membahas pengelolaan lanjutan tanda tangan pemikiran dan hanya
diperlukan jika Anda membuat permintaan API secara manual (misalnya, melalui REST) atau
memanipulasi histori percakapan.

**Jika Anda menggunakan [SDK GenAI Google](https://ai.google.dev/gemini-api/docs/libraries?hl=id) (library resmi kami), Anda tidak perlu mengelola proses ini**. SDK
secara otomatis menangani langkah-langkah yang diperlukan, seperti yang ditunjukkan dalam
[contoh](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-4) sebelumnya.

### Mengelola histori percakapan secara manual

Jika Anda mengubah histori percakapan secara manual, alih-alih mengirimkan
[respons sebelumnya yang lengkap](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#step-4), Anda
harus menangani `thought_signature` yang disertakan dalam giliran model dengan benar.

Ikuti aturan berikut untuk memastikan konteks model dipertahankan:

- Selalu kirim `thought_signature` kembali ke model di dalam
  [`Part`](https://ai.google.dev/api?hl=id#request-body-structure) aslinya.
- **Selalu sertakan `id` yang persis sama dari `function_call` di
  `function_response` Anda agar API dapat memetakan hasil ke permintaan yang benar.**
- Jangan gabungkan `Part` yang berisi tanda tangan dengan `Part` yang tidak berisi tanda tangan. Hal ini
  merusak konteks posisi pemikiran.
- Jangan menggabungkan dua `Parts` yang keduanya berisi tanda tangan, karena string
  tanda tangan tidak dapat digabungkan.

#### Tanda tangan pemikiran Gemini 3

Di Gemini 3, [`Part`](https://ai.google.dev/api?hl=id#request-body-structure) respons model
dapat berisi tanda tangan pemikiran.
Meskipun kami umumnya merekomendasikan menampilkan tanda tangan dari semua jenis `Part`, meneruskan tanda tangan pemikiran kembali adalah wajib untuk panggilan fungsi. Kecuali jika Anda memanipulasi histori percakapan secara manual, Google GenAI SDK akan menangani tanda tangan pemikiran secara otomatis.

Jika Anda memanipulasi histori percakapan secara manual, lihat halaman
[Tanda Tangan Pemikiran](https://ai.google.dev/gemini-api/docs/thought-signatures?hl=id) untuk mendapatkan panduan
dan detail lengkap tentang cara menangani tanda tangan pemikiran untuk Gemini 3.

##### Memeriksa tanda tangan pemikiran

Meskipun tidak diperlukan untuk penerapan, Anda dapat memeriksa respons untuk melihat
`thought_signature` untuk tujuan proses debug atau edukasi.

### Python

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))
```

### JavaScript

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}
```

Pelajari lebih lanjut batasan dan penggunaan tanda tangan pemikiran, serta model pemikiran secara umum, di halaman [Pemikiran](https://ai.google.dev/gemini-api/docs/thinking?hl=id#signatures).

## Panggilan fungsi paralel

Selain panggilan fungsi satu giliran, Anda juga dapat memanggil beberapa fungsi sekaligus. Panggilan fungsi paralel memungkinkan Anda menjalankan beberapa fungsi
sekaligus dan digunakan saat fungsi tidak saling bergantung. Hal ini berguna dalam skenario seperti mengumpulkan data dari beberapa sumber independen, seperti mengambil detail pelanggan dari berbagai database atau memeriksa tingkat inventaris di berbagai gudang atau melakukan beberapa tindakan seperti mengubah apartemen Anda menjadi disko.

Saat model memulai beberapa panggilan fungsi dalam satu giliran, Anda tidak perlu menampilkan objek `function_result` dalam urutan yang sama dengan objek `function_call` yang diterima. Gemini API memetakan setiap hasil kembali ke
panggilan yang sesuai menggunakan `id` dari output model. Dengan demikian, Anda dapat
mengeksekusi fungsi secara asinkron dan menambahkan hasilnya ke daftar saat
fungsi selesai.

### Python

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}
```

### JavaScript

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
  }
};
```

Konfigurasi mode panggilan fungsi untuk mengizinkan penggunaan semua alat yang ditentukan.
Untuk mempelajari lebih lanjut, Anda dapat membaca tentang
[mengonfigurasi panggilan fungsi](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#function_calling_modes).

### Python

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-3-flash-preview", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args}) - ID: {fn.id}")
```

### JavaScript

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{
        functionDeclarations: houseFns
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-3-flash-preview',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args}) - ID: ${fn.id}`);
}
```

Setiap hasil yang dicetak mencerminkan satu panggilan fungsi yang telah diminta model. Untuk mengirimkan kembali hasilnya, sertakan respons dalam urutan yang sama seperti
yang diminta.

Python SDK mendukung [panggilan fungsi otomatis](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#automatic_function_calling_python_only), yang secara otomatis mengonversi fungsi Python menjadi deklarasi, menangani siklus eksekusi panggilan fungsi dan respons untuk Anda. Berikut adalah contoh untuk kasus penggunaan disko.

### Python

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Panggilan fungsi komposit

Pemanggilan fungsi komposit atau berurutan memungkinkan Gemini merangkai beberapa panggilan fungsi untuk memenuhi permintaan yang kompleks. Misalnya, untuk menjawab "Dapatkan suhu di lokasi saya saat ini", Gemini API mungkin pertama-tama memanggil fungsi `get_current_location()`, diikuti dengan fungsi `get_weather()` yang menggunakan lokasi sebagai parameter.

Contoh berikut menunjukkan cara menerapkan panggilan fungsi komposit menggunakan Python SDK dan panggilan fungsi otomatis.

### Python

Contoh ini menggunakan fitur panggilan fungsi otomatis dari
Python SDK `google-genai`. SDK secara otomatis mengonversi fungsi Python ke skema yang diperlukan, menjalankan panggilan fungsi saat diminta oleh model, dan mengirimkan hasilnya kembali ke model untuk menyelesaikan tugas.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Output yang Diinginkan**

Saat menjalankan kode, Anda akan melihat SDK mengatur panggilan fungsi. Model pertama-tama memanggil `get_weather_forecast`, menerima
suhu, lalu memanggil `set_thermostat_temperature` dengan
nilai yang benar berdasarkan logika dalam perintah.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

### JavaScript

Contoh ini menunjukkan cara menggunakan JavaScript/TypeScript SDK untuk melakukan panggilan fungsi komposit menggunakan loop eksekusi manual.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [
  {
    functionDeclarations: [
      {
        name: "get_weather_forecast",
        description:
          "Gets the current weather temperature for a given location.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            location: {
              type: Type.STRING,
            },
          },
          required: ["location"],
        },
      },
      {
        name: "set_thermostat_temperature",
        description: "Sets the thermostat to a desired temperature.",
        parameters: {
          type: Type.OBJECT,
          properties: {
            temperature: {
              type: Type.NUMBER,
            },
          },
          required: ["temperature"],
        },
      },
    ],
  },
];

// Prompt for the model
let contents = [
  {
    role: "user",
    parts: [
      {
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
      },
    ],
  },
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
      id: functionCall.id,
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [
        {
          functionCall: functionCall,
        },
      ],
    });
    contents.push({
      role: "user",
      parts: [
        {
          functionResponse: functionResponsePart,
        },
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}
```

**Output yang Diinginkan**

Saat menjalankan kode, Anda akan melihat SDK mengatur panggilan fungsi. Model pertama-tama memanggil `get_weather_forecast`, menerima
suhu, lalu memanggil `set_thermostat_temperature` dengan
nilai yang benar berdasarkan logika dalam perintah.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

Panggilan fungsi komposit adalah fitur [Live
API](https://ai.google.dev/gemini-api/docs/live?hl=id) bawaan. Artinya, Live API dapat menangani panggilan fungsi yang mirip dengan Python SDK.

### Python

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [
    {'code_execution': {}},
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}
]

await run(prompt, tools=tools, modality="AUDIO")
```

### JavaScript

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [
  { codeExecution: {} },
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }
];

await run(prompt, tools=tools, modality="AUDIO")
```

## Mode panggilan fungsi

Gemini API memungkinkan Anda mengontrol cara model menggunakan alat yang disediakan (deklarasi fungsi). Secara khusus, Anda dapat menetapkan mode dalam
the.`function_calling_config`.

- `VALIDATED`: Mode default untuk kombinasi alat (saat alat bawaan atau output terstruktur juga diaktifkan). Model dibatasi untuk memprediksi panggilan fungsi atau bahasa alami, dan memastikan kepatuhan skema fungsi. Jika
  `allowed_function_names` tidak diberikan, model akan memilih dari semua
  deklarasi fungsi yang tersedia. Jika `allowed_function_names` diberikan, model akan memilih dari kumpulan fungsi yang diizinkan. Mode ini mengurangi panggilan fungsi yang salah format (dibandingkan dengan mode `AUTO`).
- `AUTO`: Mode default saat hanya alat function\_declarations yang diaktifkan.
  Model memutuskan apakah akan menghasilkan respons bahasa alami atau menyarankan panggilan fungsi berdasarkan perintah dan konteks.
- `ANY`: Model dibatasi untuk selalu memprediksi panggilan fungsi dan
  memastikan kepatuhan skema fungsi. Jika `allowed_function_names` tidak
  ditentukan, model dapat memilih dari deklarasi fungsi yang diberikan.
  Jika `allowed_function_names` diberikan sebagai daftar, model hanya dapat memilih
  dari fungsi dalam daftar tersebut. Gunakan mode ini saat Anda memerlukan respons panggilan
  fungsi untuk setiap perintah (jika berlaku).
- `NONE`: Model *dilarang* melakukan panggilan fungsi. Hal ini setara dengan mengirim permintaan tanpa deklarasi fungsi apa pun. Gunakan ini untuk
  menonaktifkan panggilan fungsi untuk sementara tanpa menghapus definisi alat Anda.

### Python

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)
```

### JavaScript

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};
```

## Panggilan fungsi otomatis (khusus Python)

Saat menggunakan Python SDK, Anda dapat menyediakan fungsi Python secara langsung sebagai alat.
SDK mengonversi fungsi ini menjadi deklarasi, mengelola eksekusi panggilan fungsi, dan menangani siklus respons untuk Anda. Tentukan fungsi Anda dengan
petunjuk jenis dan docstring. Untuk hasil yang optimal, sebaiknya gunakan
[string dokumen gaya Google.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
SDK kemudian akan otomatis:

1. Mendeteksi respons panggilan fungsi dari model.
2. Panggil fungsi Python yang sesuai dalam kode Anda.
3. Kirim respons fungsi kembali ke model.
4. Menampilkan respons teks akhir model.

Saat ini, SDK tidak mengurai deskripsi argumen ke dalam slot deskripsi properti deklarasi fungsi yang dihasilkan. Sebagai gantinya, seluruh docstring dikirim sebagai deskripsi fungsi tingkat teratas.

### Python

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

Anda dapat menonaktifkan panggilan fungsi otomatis dengan:

### Python

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Deklarasi skema fungsi otomatis

API ini dapat mendeskripsikan salah satu jenis berikut. Jenis `Pydantic` diizinkan, asalkan kolom yang ditentukan di dalamnya juga terdiri dari jenis yang diizinkan. Jenis dict (seperti `dict[str: int]`) tidak didukung dengan baik di sini, jadi jangan
menggunakannya.

### Python

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

Untuk melihat tampilan skema yang diinferensikan, Anda dapat mengonversinya menggunakan
[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

### Python

```
from google import genai
from google.genai import types

def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

client = genai.Client()
fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())
```

## Penggunaan multi-alat: Menggabungkan alat bawaan dengan pemanggilan fungsi

Anda dapat mengaktifkan beberapa alat, menggabungkan alat bawaan dengan panggilan fungsi dalam
permintaan yang sama.

Model Gemini 3 dapat menggabungkan alat bawaan dengan panggilan fungsi secara langsung,
berkat fitur sirkulasi konteks alat. Baca halaman tentang
[Menggabungkan alat bawaan dan panggilan fungsi](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) untuk mempelajari lebih lanjut.

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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),  # Built-in tool
          function_declarations=[getWeather]       # Custom tool
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [
    types.Content(
        role="user",
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]
    ),
    response.candidates[0].content,
    types.Content(
        role="user",
        parts=[types.Part(
            function_response=types.FunctionResponse(
                name="getWeather",
                response={"response": "Very cold. 22 degrees Fahrenheit."},
                id=response.candidates[0].content.parts[2].function_call.id
            )
        )]
    )
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[
        types.Tool(
          google_search=types.ToolGoogleSearch(),
          function_declarations=[getWeather]
        ),
      ],
      include_server_side_tool_invocations=True
    ),
)
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

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
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [
      { googleSearch: {} },
      { functionDeclarations: [getWeather] }
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [
        {
            role: "user",
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]
        },
        response1.candidates[0].content,
        {
            role: "user",
            parts: [{
                functionResponse: {
                    name: "getWeather",
                    response: {response: "Very cold. 22 degrees Fahrenheit."},
                    id: functionCallId
                }
            }]
        }
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

Untuk model sebelum seri Gemini 3, gunakan
[Live API](https://ai.google.dev/gemini-api/docs/live-api/tools?hl=id).

## Respons fungsi multimodal

Untuk model seri Gemini 3, Anda dapat menyertakan konten multimodal di
bagian respons fungsi yang Anda kirim ke model. Model dapat memproses konten multimodal ini pada giliran berikutnya untuk menghasilkan respons yang lebih informatif.
Jenis MIME berikut didukung untuk konten multimodal dalam respons fungsi:

- **Gambar**: `image/png`, `image/jpeg`, `image/webp`
- **Dokumen**: `application/pdf`, `text/plain`

Untuk menyertakan data multimodal dalam respons fungsi, sertakan sebagai satu atau beberapa
bagian yang berada dalam bagian `functionResponse`. Setiap bagian multimodal harus
berisi `inlineData`. Jika Anda mereferensikan bagian multimodal dari
dalam kolom `response` terstruktur, bagian tersebut harus berisi `displayName` unik.

Anda juga dapat mereferensikan bagian multimodal dari dalam kolom `response`
terstruktur dari bagian `functionResponse` menggunakan format referensi JSON
`{"$ref": "<displayName>"}`. Model mengganti referensi dengan konten multimodal saat memproses respons. Setiap `displayName` hanya dapat
dirujuk satu kali di kolom `response` terstruktur.

Contoh berikut menunjukkan pesan yang berisi `functionResponse` untuk
fungsi bernama `get_image` dan bagian bertingkat yang berisi data gambar dengan
`displayName: "instrument.jpg"`. Kolom `functionResponse`'s `response`
mereferensikan bagian gambar ini:

### Python

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [
  types.Content(role="user", parts=[types.Part(text=prompt)]),
  response_1.candidates[0].content,
  types.Content(
    role="user",
    parts=[
        types.Part.from_function_response(
          id=function_call.id,
          name=function_call.name,
          response=function_response_data,
          parts=[function_response_multimodal_data]
        )
    ],
  )
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

### JavaScript

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [
  { role: 'user', parts: [{ text: prompt }] },
  response1.candidates[0].content,
  {
    role: 'user',
    parts: [
      {
        functionResponse: {
          id: functionCall.id,
          name: functionCall.name,
          response: functionResponseData,
          parts: [functionResponseMultimodalData]
        },
      },
    ],
  },
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

### REST

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      ...,
      {
        "role": "user",
        "parts": [
        {
            "functionResponse": {
              "name": "get_image",
              "id": "UNIQUE_CALL_ID_HERE",
              "response": {
                "image_ref": {
                  "$ref": "instrument.jpg"
                }
              },
              "parts": [
                {
                  "inlineData": {
                    "displayName": "instrument.jpg",
                    "mimeType":"'"$MIME_TYPE"'",
                    "data": "'"$IMAGE_B64"'"
                  }
                }
              ]
            }
          }
        ]
      }
    ]
  }'
```

## Panggilan fungsi dengan Output terstruktur

Untuk model seri Gemini 3, Anda dapat menggunakan panggilan fungsi dengan
[output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id). Hal ini memungkinkan model memprediksi panggilan fungsi atau output yang sesuai dengan skema tertentu. Hasilnya, Anda akan menerima respons yang diformat secara konsisten saat model tidak menghasilkan panggilan fungsi.

## Model context protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) adalah
standar terbuka untuk menghubungkan aplikasi AI dengan alat dan data eksternal.
MCP menyediakan protokol umum bagi model untuk mengakses konteks, seperti fungsi (alat), sumber data (resource), atau perintah yang telah ditentukan sebelumnya.

SDK Gemini memiliki dukungan bawaan untuk MCP, sehingga mengurangi kode boilerplate dan
menawarkan
[panggilan alat otomatis](https://ai.google.dev/gemini-api/docs/function-calling?hl=id#automatic_function_calling_python_only)
untuk alat MCP. Saat model membuat panggilan alat MCP, SDK klien Python dan JavaScript dapat otomatis menjalankan alat MCP dan mengirimkan respons kembali ke model dalam permintaan berikutnya, melanjutkan loop ini hingga tidak ada lagi panggilan alat yang dilakukan oleh model.

Di sini, Anda dapat menemukan contoh cara menggunakan server MCP lokal dengan Gemini dan SDK `mcp`.

### Python

Pastikan [SDK `mcp`](https://modelcontextprotocol.io/introduction) versi terbaru diinstal di platform pilihan Anda.

```
pip install mcp
```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```

### JavaScript

Pastikan `mcp` SDK versi terbaru diinstal di platform pilihan Anda.

```
npm install @modelcontextprotocol/sdk
```

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();
```

### Batasan dengan dukungan MCP bawaan

Dukungan MCP bawaan adalah fitur [eksperimental](https://ai.google.dev/gemini-api/docs/models?hl=id#preview)
di SDK kami dan memiliki batasan berikut:

- Hanya alat yang didukung, bukan resource atau perintah
- Fitur ini tersedia untuk Python dan JavaScript/TypeScript SDK.
- Perubahan yang menyebabkan gangguan mungkin terjadi dalam rilis mendatang.

Integrasi server MCP secara manual selalu menjadi opsi jika batas ini membatasi apa yang Anda bangun.

## Model yang didukung

Bagian ini mencantumkan model dan kemampuan panggilan fungsinya. Model eksperimental tidak disertakan. Anda dapat menemukan ringkasan kemampuan yang komprehensif di halaman [ringkasan model](https://ai.google.dev/gemini-api/docs/models?hl=id).

| Model | Panggilan fungsi | Panggilan fungsi paralel | Panggilan fungsi komposit |
| --- | --- | --- | --- |
| [Pratinjau Gemini 3.1 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite?hl=id) | ✔️ | ✔️ | ✔️ |
| [Pratinjau Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview?hl=id) | ✔️ | ✔️ | ✔️ |
| [Pratinjau Gemini 3 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview?hl=id) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro?hl=id) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash?hl=id) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite?hl=id) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash?hl=id) | ✔️ | ✔️ | ✔️ |

## Praktik terbaik

- **Deskripsi Fungsi dan Parameter:** Jelaskan dengan sangat jelas dan spesifik dalam deskripsi Anda. Model mengandalkan hal ini untuk memilih fungsi yang benar
  dan memberikan argumen yang sesuai.
- **Penamaan:** Gunakan nama fungsi deskriptif (tanpa spasi, titik, atau tanda hubung).
- **Pengetikan Kuat:** Gunakan jenis tertentu (integer, string, enum) untuk parameter guna mengurangi error. Jika parameter memiliki serangkaian nilai valid yang terbatas, gunakan
  enum.
- **Pemilihan Alat:** Meskipun model dapat menggunakan sejumlah alat yang tidak terbatas,
  terlalu banyak alat dapat meningkatkan risiko pemilihan alat yang salah atau
  tidak optimal. Untuk hasil terbaik, berikan hanya alat yang relevan untuk konteks atau tugas, idealnya menjaga set aktif hingga maksimum 10-20. Pertimbangkan pemilihan alat dinamis berdasarkan konteks percakapan jika Anda memiliki banyak alat.
- **Rekayasa Perintah:**
  - Berikan konteks: Beri tahu model perannya (misalnya, "Anda adalah asisten cuaca yang berguna").
  - Berikan petunjuk: Tentukan cara dan waktu penggunaan fungsi (misalnya, "Jangan
    menebak tanggal; selalu gunakan tanggal mendatang untuk perkiraan.").
  - Mendorong klarifikasi: Instruksikan model untuk mengajukan pertanyaan klarifikasi jika diperlukan.
  - Lihat [Alur kerja agentik](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id#agentic-workflows)
    untuk mengetahui strategi lebih lanjut dalam mendesain perintah ini. Berikut adalah contoh [petunjuk sistem](https://ai.google.dev/gemini-api/docs/prompting-strategies?hl=id#agentic-si-template) yang telah diuji.
- **Temperatur:** Gunakan temperatur rendah (misalnya, 0) untuk panggilan fungsi yang lebih deterministik dan andal.
- **Validasi:** Jika panggilan fungsi memiliki konsekuensi yang signifikan (misalnya,
  melakukan pemesanan), validasi panggilan dengan pengguna sebelum mengeksekusinya.
- **Periksa Alasan Selesai:** Selalu periksa [`finishReason`](https://ai.google.dev/api/generate-content?hl=id#FinishReason)
  dalam respons model untuk menangani kasus saat model gagal membuat
  panggilan fungsi yang valid.
- **Penanganan Error**: Terapkan penanganan error yang andal dalam fungsi Anda untuk
  menangani input yang tidak terduga atau kegagalan API dengan baik. Menampilkan pesan error yang informatif
  yang dapat digunakan model untuk menghasilkan respons yang bermanfaat bagi
  pengguna.
- **Keamanan:** Perhatikan keamanan saat memanggil API eksternal. Gunakan
  mekanisme autentikasi dan otorisasi yang sesuai. Hindari mengekspos data sensitif dalam panggilan fungsi.
- **Batas Token:** Deskripsi dan parameter fungsi dihitung dalam batas token input Anda. Jika Anda mencapai batas token, pertimbangkan untuk membatasi jumlah fungsi atau panjang deskripsi, memecah tugas yang kompleks menjadi serangkaian fungsi yang lebih kecil dan lebih terfokus.
- **Kombinasi bash dan alat kustom** Bagi mereka yang membangun dengan kombinasi bash dan alat kustom, Pratinjau Gemini 3.1 Pro hadir dengan endpoint terpisah yang tersedia melalui API yang disebut [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview?hl=id#gemini-31-pro-preview-customtools).

## Catatan dan batasan

- Penempatan bagian panggilan fungsi: Saat menggunakan deklarasi fungsi kustom
  [bersama alat bawaan](https://ai.google.dev/gemini-api/docs/tool-combination?hl=id) (seperti Google
  Penelusuran), model dapat menampilkan campuran bagian `functionCall`, `toolCall`, dan
  `toolResponse` dalam satu giliran. Oleh karena itu, jangan menganggap
  `functionCall` akan selalu menjadi item terakhir dalam array bagian. Jika Anda mengurai respons JSON secara manual, selalu lakukan iterasi melalui array bagian, bukan mengandalkan posisi.
- Hanya [subset skema OpenAPI](https://ai.google.dev/api/caching?hl=id#FunctionDeclaration) yang didukung.
- Untuk mode `ANY`, API dapat menolak skema yang sangat besar atau bertingkat dalam. Jika
  Anda mengalami error, coba sederhanakan parameter fungsi dan skema respons
  dengan mempersingkat nama properti, mengurangi nesting, atau membatasi
  jumlah deklarasi fungsi.
- Jenis parameter yang didukung di Python terbatas.
- Panggilan fungsi otomatis hanya merupakan fitur Python SDK.

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-13 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-13 UTC."],[],[]]
