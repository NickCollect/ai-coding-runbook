---
source_url: https://ai.google.dev/gemini-api/docs/batch-api?hl=id
fetched_at: 2026-05-25T05:21:42.356105+00:00
title: "Batch API \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Deep Research Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=id) kini tersedia dalam pratinjau dengan perencanaan kolaboratif, visualisasi, dukungan MCP, dan lainnya.

![](https://ai.google.dev/_static/images/translated.svg?hl=id)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [Beranda](https://ai.google.dev/?hl=id)
- [Gemini API](https://ai.google.dev/gemini-api?hl=id)
- [Dokumen](https://ai.google.dev/gemini-api/docs?hl=id)

Kirim masukan

# Batch API

Gemini Batch API dirancang untuk memproses permintaan dalam volume besar
secara asinkron dengan biaya [50% dari biaya standar](https://ai.google.dev/gemini-api/docs/pricing?hl=id).
Waktu penyelesaian target adalah 24 jam, tetapi dalam sebagian besar kasus, waktu penyelesaiannya jauh lebih cepat.

Gunakan Batch API untuk tugas berskala besar yang tidak mendesak seperti pra-pemrosesan data atau menjalankan evaluasi yang tidak memerlukan respons langsung.

## Membuat tugas batch

Ada dua cara untuk mengirimkan permintaan Anda di Batch API:

- **[Permintaan inline](#inline-requests):** Daftar objek
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=id#GenerateContentRequest) yang disertakan langsung dalam permintaan pembuatan batch Anda. Cara ini cocok untuk batch yang lebih kecil yang menjaga ukuran total permintaan di bawah 20 MB. **Output** yang ditampilkan dari model adalah daftar objek `inlineResponse`.
- **[File input](#input-file):** File [JSON Lines (JSONL)](https://jsonlines.org/)
  dengan setiap baris berisi objek
  [`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=id#GenerateContentRequest) lengkap.
  Metode ini direkomendasikan untuk permintaan yang lebih besar. **Output** yang ditampilkan dari model adalah file JSONL dengan setiap barisnya berupa `GenerateContentResponse` atau objek status.

### Permintaan inline

Untuk permintaan dalam jumlah kecil, Anda dapat langsung menyematkan objek
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=id#GenerateContentRequest) objek
dalam [`BatchGenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=id#request-body). Contoh
berikut memanggil metode
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=id#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
dengan permintaan inline:

### Python

```
from google import genai
from google.genai import types

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'Tell me a one-sentence joke.'}],
            'role': 'user'
        }]
    },
    {
        'contents': [{
            'parts': [{'text': 'Why is the sky blue?'}],
            'role': 'user'
        }]
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "inlined-requests-job-1",
    },
)

print(f"Created batch job: {inline_batch_job.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'Tell me a one-sentence joke.'}],
            role: 'user'
        }]
    },
    {
        contents: [{
            parts: [{'text': 'Why is the sky blue?'}],
            role: 'user'
        }]
    }
]

const response = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});

console.log(response);
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-X POST \
-H "Content-Type:application/json" \
-d '{
    "batch": {
        "display_name": "my-batch-requests",
        "input_config": {
            "requests": {
                "requests": [
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-1"
                        }
                    },
                    {
                        "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]},
                        "metadata": {
                            "key": "request-2"
                        }
                    }
                ]
            }
        }
    }
}'
```

### File input

Untuk kumpulan permintaan yang lebih besar, siapkan file JSON Lines (JSONL). Setiap baris dalam
file ini harus berupa objek JSON yang berisi kunci yang ditentukan pengguna dan objek permintaan, dengan permintaan adalah objek
[`GenerateContentRequest`](https://ai.google.dev/api/batch-mode?hl=id#GenerateContentRequest) yang valid. Kunci yang ditentukan pengguna digunakan dalam respons untuk menunjukkan output mana yang merupakan hasil dari permintaan mana. Misalnya, permintaan dengan kunci yang ditentukan sebagai `request-1` akan memiliki respons yang dianotasi dengan nama kunci yang sama.

File ini diupload menggunakan [File API](https://ai.google.dev/gemini-api/docs/files?hl=id). Ukuran file maksimum yang diizinkan untuk file input adalah 2 GB.

Berikut adalah contoh file JSONL. Anda dapat menyimpannya dalam file bernama `my-batch-requests.json`:

```
{"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generation_config": {"temperature": 0.7}}}
{"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
```

Mirip dengan permintaan inline, Anda dapat menentukan parameter lain seperti petunjuk sistem, alat, atau konfigurasi lainnya di setiap JSON permintaan.

Anda dapat mengupload file ini menggunakan [File API](https://ai.google.dev/gemini-api/docs/files?hl=id) seperti
yang ditunjukkan dalam contoh berikut. Jika menggunakan input multimodal, Anda dapat mereferensikan file lain yang diupload dalam file JSONL.

### Python

```
import json
from google import genai
from google.genai import types

client = genai.Client()

# Create a sample JSONL file
with open("my-batch-requests.jsonl", "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}]}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

# Upload the file to the File API
uploaded_file = client.files.upload(
    file='my-batch-requests.jsonl',
    config=types.UploadFileConfig(display_name='my-batch-requests', mime_type='jsonl')
)

print(f"Uploaded file: {uploaded_file.name}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});
const fileName = "my-batch-requests.jsonl";

// Define the requests
const requests = [
    { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "Describe the process of photosynthesis." }] }] } },
    { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "What are the main ingredients in a Margherita pizza?" }] }] } }
];

// Construct the full path to file
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, fileName); // __dirname is the directory of the current script

async function writeBatchRequestsToFile(requests, filePath) {
    try {
        // Use a writable stream for efficiency, especially with larger files.
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });

        writeStream.on('error', (err) => {
            console.error(`Error writing to file ${filePath}:`, err);
        });

        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }

        writeStream.end();

        console.log(`Successfully wrote batch requests to ${filePath}`);

    } catch (error) {
        // This catch block is for errors that might occur before stream setup,
        // stream errors are handled by the 'error' event.
        console.error(`An unexpected error occurred:`, error);
    }
}

// Write to a file.
writeBatchRequestsToFile(requests, filePath);

// Upload the file to the File API.
const uploadedFile = await ai.files.upload({file: 'my-batch-requests.jsonl', config: {
    mimeType: 'jsonl',
}});
console.log(uploadedFile.name);
```

### REST

```
tmp_batch_input_file=batch_input.tmp
echo -e '{"contents": [{"parts": [{"text": "Describe the process of photosynthesis."}]}], "generationConfig": {"temperature": 0.7}}\n{"contents": [{"parts": [{"text": "What are the main ingredients in a Margherita pizza?"}]}]}' > batch_input.tmp
MIME_TYPE=$(file -b --mime-type "${tmp_batch_input_file}")
NUM_BYTES=$(wc -c < "${tmp_batch_input_file}")
DISPLAY_NAME=BatchInput

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
-D "${tmp_header_file}" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "X-Goog-Upload-Protocol: resumable" \
-H "X-Goog-Upload-Command: start" \
-H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
-H "Content-Type: application/jsonl" \
-d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
-H "Content-Length: ${NUM_BYTES}" \
-H "X-Goog-Upload-Offset: 0" \
-H "X-Goog-Upload-Command: upload, finalize" \
--data-binary "@${tmp_batch_input_file}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
```

Contoh berikut memanggil metode
[`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=id#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
dengan file input yang diupload menggunakan File API:

### Python

```
from google import genai

# Assumes `uploaded_file` is the file object from the previous step
client = genai.Client()
file_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=uploaded_file.name,
    config={
        'display_name': "file-upload-job-1",
    },
)

print(f"Created batch job: {file_batch_job.name}")
```

### JavaScript

```
// Assumes `uploadedFile` is the file object from the previous step
const fileBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: uploadedFile.name,
    config: {
        displayName: 'file-upload-job-1',
    }
});

console.log(fileBatchJob);
```

### REST

```
# Set the File ID taken from the upload response.
BATCH_INPUT_FILE='files/123456'
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:batchGenerateContent \
-X POST \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" \
-d "{
    'batch': {
        'display_name': 'my-batch-requests',
        'input_config': {
            'file_name': '${BATCH_INPUT_FILE}'
        }
    }
}"
```

Saat membuat tugas batch, Anda akan mendapatkan nama tugas yang ditampilkan. Gunakan nama ini
untuk [memantau](#batch-job-status) status tugas serta
[mengambil hasilnya](#retrieve-batch-results) setelah tugas selesai.

Berikut adalah contoh output yang berisi nama tugas:

```
Created batch job from file: batches/123456789
```

### Dukungan penyematan batch

Anda dapat menggunakan Batch API untuk berinteraksi dengan
[model Penyematan](https://ai.google.dev/gemini-api/docs/embeddings?hl=id) untuk mendapatkan throughput yang lebih tinggi.
Untuk membuat tugas batch penyematan dengan [permintaan inline](#inline-requests)
atau [file input](#input-file), gunakan `batches.create_embeddings` API dan
tentukan model penyematan.

### Python

```
from google import genai

client = genai.Client()

# Creating an embeddings batch job with an input file request:
file_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    src={'file_name': uploaded_batch_requests.name},
    config={'display_name': "Input embeddings batch"},
)

# Creating an embeddings batch job with an inline request:
batch_job = client.batches.create_embeddings(
    model="gemini-embedding-2",
    # For a predefined list of requests `inlined_requests`
    src={'inlined_requests': inlined_requests},
    config={'display_name': "Inlined embeddings batch"},
)
```

### JavaScript

```
// Creating an embeddings batch job with an input file request:
let fileJob;
fileJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    src: {fileName: uploadedBatchRequests.name},
    config: {displayName: 'Input embeddings batch'},
});
console.log(`Created batch job: ${fileJob.name}`);

// Creating an embeddings batch job with an inline request:
let batchJob;
batchJob = await client.batches.createEmbeddings({
    model: 'gemini-embedding-2',
    // For a predefined a list of requests `inlinedRequests`
    src: {inlinedRequests: inlinedRequests},
    config: {displayName: 'Inlined embeddings batch'},
});
console.log(`Created batch job: ${batchJob.name}`);
```

Baca bagian Penyematan di [Cookbook Batch API](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb)
untuk mengetahui contoh lainnya.

### Konfigurasi permintaan

Anda dapat menyertakan konfigurasi permintaan apa pun yang akan digunakan dalam permintaan non-batch standar. Misalnya, Anda dapat menentukan suhu, petunjuk sistem, atau bahkan meneruskan modalitas lainnya. Contoh berikut menunjukkan contoh permintaan inline yang berisi petunjuk sistem untuk salah satu permintaan:

### Python

```
inline_requests_list = [
    {'contents': [{'parts': [{'text': 'Write a short poem about a cloud.'}]}]},
    {'contents': [{
        'parts': [{
            'text': 'Write a short poem about a cat.'
            }]
        }],
    'config': {
        'system_instruction': {'parts': [{'text': 'You are a cat. Your name is Neko.'}]}}
    }
]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Write a short poem about a cloud.'}]}]},
    {contents: [{parts: [{text: 'Write a short poem about a cat.'}]}],
     config: {systemInstruction: {parts: [{text: 'You are a cat. Your name is Neko.'}]}}}
]
```

Demikian pula, Anda dapat menentukan alat yang akan digunakan untuk permintaan. Contoh berikut
menunjukkan permintaan yang mengaktifkan [alat Google Penelusuran](https://ai.google.dev/gemini-api/docs/google-search?hl=id):

### Python

```
inlined_requests = [
{'contents': [{'parts': [{'text': 'Who won the euro 1998?'}]}]},
{'contents': [{'parts': [{'text': 'Who won the euro 2025?'}]}],
 'config':{'tools': [{'google_search': {}}]}}]
```

### JavaScript

```
inlineRequestsList = [
    {contents: [{parts: [{text: 'Who won the euro 1998?'}]}]},
    {contents: [{parts: [{text: 'Who won the euro 2025?'}]}],
     config: {tools: [{googleSearch: {}}]}}
]
```

Anda juga dapat menentukan [output terstruktur](https://ai.google.dev/gemini-api/docs/structured-output?hl=id).
Contoh berikut menunjukkan cara menentukan untuk permintaan batch Anda.

### Python

```
import time
from google import genai
from pydantic import BaseModel, TypeAdapter

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()

# A list of dictionaries, where each is a GenerateContentRequest
inline_requests = [
    {
        'contents': [{
            'parts': [{'text': 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    },
    {
        'contents': [{
            'parts': [{'text': 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            'role': 'user'
        }],
        'config': {
            'response_mime_type': 'application/json',
            'response_schema': list[Recipe]
        }
    }
]

inline_batch_job = client.batches.create(
    model="gemini-3.5-flash",
    src=inline_requests,
    config={
        'display_name': "structured-output-job-1"
    },
)

# wait for the job to finish
job_name = inline_batch_job.name
print(f"Polling status for job: {job_name}")

while True:
    batch_job_inline = client.batches.get(name=job_name)
    if batch_job_inline.state.name in ('JOB_STATE_SUCCEEDED', 'JOB_STATE_FAILED', 'JOB_STATE_CANCELLED', 'JOB_STATE_EXPIRED'):
        break
    print(f"Job not finished. Current state: {batch_job_inline.state.name}. Waiting 30 seconds...")
    time.sleep(30)

print(f"Job finished with state: {batch_job_inline.state.name}")

# print the response
for i, inline_response in enumerate(batch_job_inline.dest.inlined_responses, start=1):
    print(f"\n--- Response {i} ---")

    # Check for a successful response
    if inline_response.response:
        # The .text property is a shortcut to the generated text.
        print(inline_response.response.text)
```

### JavaScript

```
import {GoogleGenAI, Type} from '@google/genai';

const ai = new GoogleGenAI({});

const inlinedRequests = [
    {
        contents: [{
            parts: [{text: 'List a few popular cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    },
    {
        contents: [{
            parts: [{text: 'List a few popular gluten free cookie recipes, and include the amounts of ingredients.'}],
            role: 'user'
        }],
        config: {
            responseMimeType: 'application/json',
            responseSchema: {
            type: Type.ARRAY,
            items: {
                type: Type.OBJECT,
                properties: {
                'recipeName': {
                    type: Type.STRING,
                    description: 'Name of the recipe',
                    nullable: false,
                },
                'ingredients': {
                    type: Type.ARRAY,
                    items: {
                    type: Type.STRING,
                    description: 'Ingredients of the recipe',
                    nullable: false,
                    },
                },
                },
                required: ['recipeName'],
            },
            },
        }
    }
]

const inlinedBatchJob = await ai.batches.create({
    model: 'gemini-3.5-flash',
    src: inlinedRequests,
    config: {
        displayName: 'inlined-requests-job-1',
    }
});
```

Berikut menunjukkan contoh output tugas ini:

```
--- Response 1 ---
[
  {
    "recipe_name": "Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 1/4 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Oatmeal Raisin Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 cup packed light brown sugar",
      "1/2 cup granulated sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "1 1/2 cups all-purpose flour",
      "1 teaspoon baking soda",
      "1 teaspoon ground cinnamon",
      "1/2 teaspoon salt",
      "3 cups old-fashioned rolled oats",
      "1 cup raisins"
    ]
  },
  {
    "recipe_name": "Sugar Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "1 1/2 cups granulated sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "2 3/4 cups all-purpose flour",
      "1 teaspoon baking powder",
      "1/2 teaspoon salt"
    ]
  }
]

--- Response 2 ---
[
  {
    "recipe_name": "Gluten-Free Chocolate Chip Cookies",
    "ingredients": [
      "1 cup (2 sticks) unsalted butter, softened",
      "3/4 cup granulated sugar",
      "3/4 cup packed light brown sugar",
      "2 large eggs",
      "1 teaspoon vanilla extract",
      "2 1/4 cups gluten-free all-purpose flour blend (with xanthan gum)",
      "1 teaspoon baking soda",
      "1/2 teaspoon salt",
      "1 1/2 cups chocolate chips"
    ]
  },
  {
    "recipe_name": "Gluten-Free Peanut Butter Cookies",
    "ingredients": [
      "1 cup (250g) creamy peanut butter",
      "1/2 cup (100g) granulated sugar",
      "1/2 cup (100g) packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1/2 teaspoon baking soda",
      "1/4 teaspoon salt"
    ]
  },
  {
    "recipe_name": "Gluten-Free Oatmeal Raisin Cookies",
    "ingredients": [
      "1/2 cup (1 stick) unsalted butter, softened",
      "1/2 cup granulated sugar",
      "1/2 cup packed light brown sugar",
      "1 large egg",
      "1 teaspoon vanilla extract",
      "1 cup gluten-free all-purpose flour blend",
      "1/2 teaspoon baking soda",
      "1/2 teaspoon ground cinnamon",
      "1/4 teaspoon salt",
      "1 1/2 cups gluten-free rolled oats",
      "1/2 cup raisins"
    ]
  }
]
```

## Memantau status tugas

Gunakan nama operasi yang diperoleh saat membuat tugas batch untuk melakukan polling statusnya.
Kolom status tugas batch akan menunjukkan statusnya saat ini. Tugas batch dapat berada dalam salah satu status berikut:

- `JOB_STATE_PENDING`: Tugas telah dibuat dan menunggu untuk diproses oleh layanan.
- `JOB_STATE_RUNNING`: Tugas sedang berlangsung.
- `JOB_STATE_SUCCEEDED`: Tugas berhasil diselesaikan. Anda kini dapat mengambil hasilnya.
- `JOB_STATE_FAILED`: Tugas gagal. Periksa detail error untuk mengetahui informasi selengkapnya.
- `JOB_STATE_CANCELLED`: Tugas dibatalkan oleh pengguna.
- `JOB_STATE_EXPIRED`: Tugas telah berakhir karena berjalan atau tertunda selama lebih dari 48 jam. Tugas tidak akan memiliki hasil untuk diambil.
  Anda dapat mencoba mengirimkan tugas lagi atau membagi permintaan menjadi batch yang lebih kecil.

Anda dapat melakukan polling status tugas secara berkala untuk memeriksa penyelesaian.

### Python

```
import time
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"  # (e.g. 'batches/your-batch-id')
batch_job = client.batches.get(name=job_name)

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

print(f"Polling status for job: {job_name}")
batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(30) # Wait for 30 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")
if batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
let batchJob;
const completedStates = new Set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
]);

try {
    batchJob = await ai.batches.get({name: inlinedBatchJob.name});
    while (!completedStates.has(batchJob.state)) {
        console.log(`Current state: ${batchJob.state}`);
        // Wait for 30 seconds before polling again
        await new Promise(resolve => setTimeout(resolve, 30000));
        batchJob = await client.batches.get({ name: batchJob.name });
    }
    console.log(`Job finished with state: ${batchJob.state}`);
    if (batchJob.state === 'JOB_STATE_FAILED') {
        // The exact structure of `error` might vary depending on the SDK
        // This assumes `error` is an object with a `message` property.
        console.error(`Error: ${batchJob.state}`);
    }
} catch (error) {
    console.error(`An error occurred while polling job ${batchJob.name}:`, error);
}
```

### Polling dan webhook

**Bosan melakukan polling?** Gemini kini mendukung
[Webhook](https://ai.google.dev/gemini-api/docs/webhooks?hl=id) untuk memproses penyelesaian secara asinkron.
Daripada terus memanggil `GET / operations`, berlanggananlah `batch.succeeded` secara langsung untuk mengizinkan Gemini API mengirim notifikasi real-time ke server Anda saat operasi asinkron atau operasi yang berjalan lama selesai.

### Python

```
from google import genai

client = genai.Client()

webhook = client.webhooks.create(
    name="MyBatchWebhook",
    subscribed_events=["batch.succeeded", "batch.failed"],
    uri="https://my-api.com/gemini-callback",
)

print(f"Created webhook: {webhook.name}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI();

async function createWebhook() {
  const webhook = await client.webhooks.create({
    name: "MyBatchWebhook",
    subscribed_events: ["batch.succeeded", "batch.failed"],
    uri: "https://my-api.com/gemini-callback",
  });

  console.log(`Created webhook: ${webhook.name}`);
}

createWebhook();
```

### REST

```
curl -X POST \
  "https://generativelanguage.googleapis.com/v1/webhooks?webhook_id=my-example-webhook-123" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GOOGLE_API_KEY" \
  -d '{
    "name": "My Example Webhook",
    "uri": "https://my-api.com/gemini-callback",
    "subscribed_events": ["batch.succeeded", "batch.failed"]
  }'
```

## Mengambil hasil

Setelah status tugas menunjukkan bahwa tugas batch Anda berhasil, hasilnya akan tersedia di kolom `response`.

### Python

```
import json
from google import genai

client = genai.Client()

# Use the name of the job you want to check
# e.g., inline_batch_job.name from the previous step
job_name = "YOUR_BATCH_JOB_NAME"
batch_job = client.batches.get(name=job_name)

if batch_job.state.name == 'JOB_STATE_SUCCEEDED':

    # If batch job was created with a file
    if batch_job.dest and batch_job.dest.file_name:
        # Results are in a file
        result_file_name = batch_job.dest.file_name
        print(f"Results are in file: {result_file_name}")

        print("Downloading result file content...")
        file_content = client.files.download(file=result_file_name)
        # Process file_content (bytes) as needed
        print(file_content.decode('utf-8'))

    # If batch job was created with inline request
    # (for embeddings, use batch_job.dest.inlined_embed_content_responses)
    elif batch_job.dest and batch_job.dest.inlined_responses:
        # Results are inline
        print("Results are inline:")
        for i, inline_response in enumerate(batch_job.dest.inlined_responses):
            print(f"Response {i+1}:")
            if inline_response.response:
                # Accessing response, structure may vary.
                try:
                    print(inline_response.response.text)
                except AttributeError:
                    print(inline_response.response) # Fallback
            elif inline_response.error:
                print(f"Error: {inline_response.error}")
    else:
        print("No results found (neither file nor inline).")
else:
    print(f"Job did not succeed. Final state: {batch_job.state.name}")
    if batch_job.error:
        print(f"Error: {batch_job.error}")
```

### JavaScript

```
// Use the name of the job you want to check
// e.g., inlinedBatchJob.name from the previous step
const jobName = "YOUR_BATCH_JOB_NAME";

try {
    const batchJob = await ai.batches.get({ name: jobName });

    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        console.log('Found completed batch:', batchJob.displayName);
        console.log(batchJob);

        // If batch job was created with a file destination
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);

            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });

            // Process fileContentBuffer (Buffer) as needed
            console.log(fileContentBuffer.toString('utf-8'));
        }

        // If batch job was created with inline responses
        else if (batchJob.dest?.inlinedResponses) {
            console.log("Results are inline:");
            for (let i = 0; i < batchJob.dest.inlinedResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    // Accessing response, structure may vary.
                    if (inlineResponse.response.text !== undefined) {
                        console.log(inlineResponse.response.text);
                    } else {
                        console.log(inlineResponse.response); // Fallback
                    }
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        }

        // If batch job was an embedding batch with inline responses
        else if (batchJob.dest?.inlinedEmbedContentResponses) {
            console.log("Embedding results found inline:");
            for (let i = 0; i < batchJob.dest.inlinedEmbedContentResponses.length; i++) {
                const inlineResponse = batchJob.dest.inlinedEmbedContentResponses[i];
                console.log(`Response ${i + 1}:`);
                if (inlineResponse.response) {
                    console.log(inlineResponse.response);
                } else if (inlineResponse.error) {
                    console.error(`Error: ${inlineResponse.error}`);
                }
            }
        } else {
            console.log("No results found (neither file nor inline).");
        }
    } else {
        console.log(`Job did not succeed. Final state: ${batchJob.state}`);
        if (batchJob.error) {
            console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
        }
    }
} catch (error) {
    console.error(`An error occurred while processing job ${jobName}:`, error);
}
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null > batch_status.json

if jq -r '.done' batch_status.json | grep -q "false"; then
    echo "Batch has not finished processing"
fi

batch_state=$(jq -r '.metadata.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    if [[ $(jq '.response | has("inlinedResponses")' batch_status.json) = "true" ]]; then
        jq -r '.response.inlinedResponses' batch_status.json
        exit
    fi
    responses_file_name=$(jq -r '.response.responsesFile' batch_status.json)
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
    -H "x-goog-api-key: $GEMINI_API_KEY" 2> /dev/null
elif [[ $batch_state = "JOB_STATE_FAILED" ]]; then
    jq '.error' batch_status.json
elif [[ $batch_state == "JOB_STATE_CANCELLED" ]]; then
    echo "Batch was cancelled by the user"
elif [[ $batch_state == "JOB_STATE_EXPIRED" ]]; then
    echo "Batch expired after 48 hours"
fi
```

## Mencantumkan tugas batch

Anda dapat mencantumkan tugas batch terbaru.

### Python

```
batch_jobs = client.batches.list()

# Optional query config:
# batch_jobs = client.batches.list(config={'page_size': 5})

for batch_job in batch_jobs:
    print(batch_job)
```

### JavaScript

```
const batchJobs = await ai.batches.list();

// Optional query config:
// const batchJobs = await ai.batches.list({config: {'pageSize': 5}});

for await (const batchJob of batchJobs) {
    console.log(batchJob);
}
```

### REST

```
curl https://generativelanguage.googleapis.com/v1beta/batches \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Membatalkan tugas batch

Anda dapat membatalkan tugas batch yang sedang berlangsung menggunakan namanya. Saat dibatalkan, tugas akan berhenti memproses permintaan baru.

### Python

```
client.batches.cancel(name=batch_job_to_cancel.name)
```

### JavaScript

```
await ai.batches.cancel({name: batchJobToCancel.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Cancel the batch
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME:cancel \
-H "x-goog-api-key: $GEMINI_API_KEY" \

# Confirm that the status of the batch after cancellation is JOB_STATE_CANCELLED
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Content-Type:application/json" 2> /dev/null | jq -r '.metadata.state'
```

## Menghapus tugas batch

Anda dapat menghapus tugas batch yang ada menggunakan namanya. Saat dihapus, tugas akan berhenti memproses permintaan baru dan dihapus dari daftar tugas batch.

### Python

```
client.batches.delete(name=batch_job_to_delete.name)
```

### JavaScript

```
await ai.batches.delete({name: batchJobToDelete.name});
```

### REST

```
BATCH_NAME="batches/123456" # Your batch job name

# Delete the batch job
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## Membuat gambar dalam batch

Jika Anda menggunakan [Gemini Nano Banana](https://ai.google.dev/gemini-api/docs/image-generation?hl=id) dan perlu membuat banyak
gambar, Anda dapat menggunakan Batch API untuk mendapatkan
[batas frekuensi](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id) yang lebih tinggi dengan imbalan waktu penyelesaian hingga
24 jam.

Anda dapat menggunakan permintaan inline untuk batch permintaan kecil (di bawah 20 MB) atau file input JSONL untuk batch besar (direkomendasikan untuk pembuatan gambar):

Permintaan inline
File input

### Python

```
import json
import time
import base64
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# 1. Create and upload file
file_name = "my-batch-image-requests.jsonl"
with open(file_name, "w") as f:
    requests = [
        {"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}},
        {"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}
    ]
    for req in requests:
        f.write(json.dumps(req) + "\n")

uploaded_file = client.files.upload(
    file=file_name,
    config=types.UploadFileConfig(display_name='my-batch-image-requests', mime_type='jsonl')
)
print(f"Uploaded file: {uploaded_file.name}")

# 2. Create batch job
file_batch_job = client.batches.create(
    model="gemini-3-pro-image-preview",
    src=uploaded_file.name,
    config={
        'display_name': "file-image-upload-job-1",
    },
)
print(f"Created batch job: {file_batch_job.name}")

# 3. Monitor job status
job_name = file_batch_job.name
print(f"Polling status for job: {job_name}")

completed_states = set([
    'JOB_STATE_SUCCEEDED',
    'JOB_STATE_FAILED',
    'JOB_STATE_CANCELLED',
    'JOB_STATE_EXPIRED',
])

batch_job = client.batches.get(name=job_name) # Initial get
while batch_job.state.name not in completed_states:
  print(f"Current state: {batch_job.state.name}")
  time.sleep(10) # Wait for 10 seconds before polling again
  batch_job = client.batches.get(name=job_name)

print(f"Job finished with state: {batch_job.state.name}")

# 4. Retrieve results
if batch_job.state.name == 'JOB_STATE_SUCCEEDED':
    result_file_name = batch_job.dest.file_name
    print(f"Results are in file: {result_file_name}")
    print("Downloading result file content...")
    file_content_bytes = client.files.download(file=result_file_name)
    file_content = file_content_bytes.decode('utf-8')
    # The result file is also a JSONL file. Parse and print each line.
    for line in file_content.splitlines():
      if line:
        parsed_response = json.loads(line)
        if 'response' in parsed_response and parsed_response['response']:
            for part in parsed_response['response']['candidates'][0]['content']['parts']:
              if part.get('text'):
                print(part['text'])
              elif part.get('inlineData'):
                print(f"Image mime type: {part['inlineData']['mimeType']}")
                data = base64.b64decode(part['inlineData']['data'])
        elif 'error' in parsed_response:
            print(f"Error: {parsed_response['error']}")
elif batch_job.state.name == 'JOB_STATE_FAILED':
    print(f"Error: {batch_job.error}")
```

### JavaScript

```
import {GoogleGenAI} from '@google/genai';
import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from 'url';

const ai = new GoogleGenAI({});

async function run() {
    // 1. Create and upload file
    const fileName = "my-batch-image-requests.jsonl";
    const requests = [
        { "key": "request-1", "request": { "contents": [{ "parts": [{ "text": "A big letter A surrounded by animals starting with the A letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } },
        { "key": "request-2", "request": { "contents": [{ "parts": [{ "text": "A big letter B surrounded by animals starting with the B letter" }] }], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]} } }
    ];
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    const filePath = path.join(__dirname, fileName);

    try {
        const writeStream = fs.createWriteStream(filePath, { flags: 'w' });
        for (const req of requests) {
            writeStream.write(JSON.stringify(req) + '\n');
        }
        writeStream.end();
        console.log(`Successfully wrote batch requests to ${filePath}`);
    } catch (error) {
        console.error(`An unexpected error occurred writing file:`, error);
        return;
    }

    const uploadedFile = await ai.files.upload({file: fileName, config: { mimeType: 'jsonl' }});
    console.log(`Uploaded file: ${uploadedFile.name}`);

    // 2. Create batch job
    const fileBatchJob = await ai.batches.create({
        model: 'gemini-3-pro-image-preview',
        src: uploadedFile.name,
        config: {
            displayName: 'file-image-upload-job-1',
        }
    });
    console.log(fileBatchJob);

    // 3. Monitor job status
    let batchJob;
    const completedStates = new Set([
        'JOB_STATE_SUCCEEDED',
        'JOB_STATE_FAILED',
        'JOB_STATE_CANCELLED',
        'JOB_STATE_EXPIRED',
    ]);

    try {
        batchJob = await ai.batches.get({name: fileBatchJob.name});
        while (!completedStates.has(batchJob.state)) {
            console.log(`Current state: ${batchJob.state}`);
            // Wait for 10 seconds before polling again
            await new Promise(resolve => setTimeout(resolve, 10000));
            batchJob = await ai.batches.get({ name: batchJob.name });
        }
        console.log(`Job finished with state: ${batchJob.state}`);
    } catch (error) {
        console.error(`An error occurred while polling job ${fileBatchJob.name}:`, error);
        return;
    }

    // 4. Retrieve results
    if (batchJob.state === 'JOB_STATE_SUCCEEDED') {
        if (batchJob.dest?.fileName) {
            const resultFileName = batchJob.dest.fileName;
            console.log(`Results are in file: ${resultFileName}`);
            console.log("Downloading result file content...");
            const fileContentBuffer = await ai.files.download({ file: resultFileName });
            const fileContent = fileContentBuffer.toString('utf-8');
            for (const line of fileContent.split('\n')) {
                if (line) {
                    const parsedResponse = JSON.parse(line);
                    if (parsedResponse.response) {
                        for (const part of parsedResponse.response.candidates[0].content.parts) {
                            if (part.text) {
                                console.log(part.text);
                            } else if (part.inlineData) {
                                console.log(`Image mime type: ${part.inlineData.mimeType}`);
                            }
                        }
                    } else if (parsedResponse.error) {
                        console.error(`Error: ${parsedResponse.error}`);
                    }
                }
            }
        } else {
            console.log("No result file found.");
        }
    } else if (batchJob.state === 'JOB_STATE_FAILED') {
         console.error(`Error: ${typeof batchJob.error === 'string' ? batchJob.error : batchJob.error.message || JSON.stringify(batchJob.error)}`);
    }
}
run();
```

### REST

```
# 1. Create and upload file
echo '{"key": "request-1", "request": {"contents": [{"parts": [{"text": "A big letter A surrounded by animals starting with the A letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' > my-batch-image-requests.jsonl
echo '{"key": "request-2", "request": {"contents": [{"parts": [{"text": "A big letter B surrounded by animals starting with the B letter"}]}], "generation_config": {"responseModalities": ["TEXT", "IMAGE"]}}}' >> my-batch-image-requests.jsonl

# Follow File API guide to upload: https://ai.google.dev/gemini-api/docs/files#upload_a_file
# This example assumes you have uploaded the file and set BATCH_INPUT_FILE to its name (e.g., files/abcdef123)
BATCH_INPUT_FILE="files/your-uploaded-file-name"

# 2. Create batch job
printf -v request_data '{
    "batch": {
        "display_name": "my-batch-file-image-requests",
        "input_config": { "file_name": "%s" }
    }
}' "$BATCH_INPUT_FILE"
curl https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:batchGenerateContent \
  -X POST \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" \
  -d "$request_data" > created_batch.json

BATCH_NAME=$(jq -r '.name' created_batch.json)
echo "Created batch job: $BATCH_NAME"

# 3. Poll job status until completion by repeating the following command:
curl https://generativelanguage.googleapis.com/v1beta/$BATCH_NAME \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type:application/json" > batch_status.json

echo "Current status:"
jq '.' batch_status.json

# 4. If state is JOB_STATE_SUCCEEDED, download results file
batch_state=$(jq -r '.state' batch_status.json)
if [[ $batch_state = "JOB_STATE_SUCCEEDED" ]]; then
    responses_file_name=$(jq -r '.dest.fileName' batch_status.json)
    echo "Job succeeded. Downloading results from $responses_file_name..."
    curl https://generativelanguage.googleapis.com/download/v1beta/$responses_file_name:download?alt=media \
      -H "x-goog-api-key: $GEMINI_API_KEY" > batch_results.jsonl
    echo "Results saved to batch_results.jsonl"
fi
```

## Detail teknis

- **Model yang didukung:** Batch API mendukung berbagai model Gemini.
  Lihat halaman [Model](https://ai.google.dev/gemini-api/docs/models?hl=id) untuk mengetahui dukungan setiap model
  terhadap Batch API. Modalitas yang didukung untuk Batch API sama dengan yang didukung di API interaktif (atau non-batch).
- **Harga:** Penggunaan Batch API dikenai harga 50% dari biaya API interaktif standar untuk model yang setara. Lihat [halaman harga](https://ai.google.dev/gemini-api/docs/pricing?hl=id)
  untuk mengetahui detailnya. Lihat halaman [batas frekuensi](https://ai.google.dev/gemini-api/docs/rate-limits?hl=id#batch-mode)
  untuk mengetahui detail batas frekuensi untuk fitur ini.
- **Tujuan Tingkat Layanan (SLO):** Tugas batch dirancang untuk diselesaikan dalam waktu penyelesaian 24 jam. Banyak tugas dapat diselesaikan jauh lebih cepat, bergantung pada ukuran dan beban sistem saat ini.
- **Caching:** [Caching konteks](https://ai.google.dev/gemini-api/docs/caching?hl=id) diaktifkan
  untuk permintaan batch. Jika permintaan dalam batch Anda menghasilkan hit cache, token yang di-cache akan dikenai harga yang sama seperti traffic API non-batch.

## Praktik terbaik

- **Gunakan file input untuk permintaan besar:** Untuk permintaan dalam jumlah besar,
  selalu gunakan metode input file
  untuk pengelolaan yang lebih baik dan untuk menghindari batas ukuran permintaan untuk
  panggilan [`BatchGenerateContent`](https://ai.google.dev/api/batch-mode?hl=id#google.ai.generativelanguage.v1beta.BatchService.BatchGenerateContent)
  itu sendiri. Perhatikan bahwa ada batas ukuran file 2 GB per file input.
- **Penanganan error:** Periksa `batchStats` untuk `failedRequestCount` setelah tugas selesai. Jika menggunakan output file, uraikan setiap baris untuk memeriksa apakah baris tersebut adalah `GenerateContentResponse` atau objek status yang menunjukkan error untuk permintaan tertentu tersebut. Lihat [panduan
  pemecahan masalah](https://ai.google.dev/gemini-api/docs/troubleshooting?hl=id#error-codes) untuk mengetahui kumpulan lengkap
  kode error.
- **Kirim tugas satu kali:** Pembuatan tugas batch tidak bersifat idempoten.
  Jika Anda mengirim permintaan pembuatan yang sama dua kali, dua tugas batch terpisah akan dibuat.
- **Bagi batch yang sangat besar:** Meskipun waktu penyelesaian target adalah 24 jam, waktu pemrosesan sebenarnya dapat bervariasi berdasarkan beban sistem dan ukuran tugas.
  Untuk tugas besar, pertimbangkan untuk membaginya menjadi batch yang lebih kecil jika hasil sementara diperlukan lebih cepat.

## Langkah berikutnya

- Lihat [notebook Batch API](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Batch_mode.ipynb?hl=id)
  untuk mengetahui contoh lainnya.
- Lapisan kompatibilitas OpenAI mendukung Batch API. Baca contoh di halaman
  [Kompatibilitas OpenAI](https://ai.google.dev/gemini-api/docs/openai?hl=id#batch).

Kirim masukan

Kecuali dinyatakan lain, konten di halaman ini dilisensikan berdasarkan [Lisensi Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), sedangkan contoh kode dilisensikan berdasarkan [Lisensi Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Untuk mengetahui informasi selengkapnya, lihat [Kebijakan Situs Google Developers](https://developers.google.com/site-policies?hl=id). Java adalah merek dagang terdaftar dari Oracle dan/atau afiliasinya.

Terakhir diperbarui pada 2026-05-19 UTC.

Ada masukan untuk kami?

[[["Mudah dipahami","easyToUnderstand","thumb-up"],["Memecahkan masalah saya","solvedMyProblem","thumb-up"],["Lainnya","otherUp","thumb-up"]],[["Informasi yang saya butuhkan tidak ada","missingTheInformationINeed","thumb-down"],["Terlalu rumit/langkahnya terlalu banyak","tooComplicatedTooManySteps","thumb-down"],["Sudah usang","outOfDate","thumb-down"],["Masalah terjemahan","translationIssue","thumb-down"],["Masalah kode / contoh","samplesCodeIssue","thumb-down"],["Lainnya","otherDown","thumb-down"]],["Terakhir diperbarui pada 2026-05-19 UTC."],[],[]]
