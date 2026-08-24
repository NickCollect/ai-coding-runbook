---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=th
fetched_at: 2026-08-24T02:31:55.788452+00:00
title: "\u0e2a\u0e20\u0e32\u0e1e\u0e41\u0e27\u0e14\u0e25\u0e49\u0e2d\u0e21\u0e43\u0e19 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

ตอนนี้ [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=th) พร้อมให้บริการแก่ผู้ใช้ทั่วไปแล้ว เราขอแนะนำให้ใช้ API นี้เพื่อเข้าถึงฟีเจอร์และโมเดลล่าสุดทั้งหมด

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google ใช้เทคโนโลยี AI เพื่อแปลเนื้อหาเป็นภาษาที่คุณต้องการ การแปลโดย AI อาจมีข้อผิดพลาด

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สภาพแวดล้อมใน Agent ที่มีการจัดการ

สภาพแวดล้อมคือแซนด์บ็อกซ์ Linux ที่มีการจัดการ ซึ่งช่วยให้ตัวแทนมีพื้นที่ที่แยกต่างหากเพื่อรันโค้ดและเก็บไฟล์ไว้ โดยสภาพแวดล้อมจะแยกออกจากบริบทการโต้ตอบ คุณจึงใช้สภาพแวดล้อมเดียวกันซ้ำในการโต้ตอบหลายครั้งหรือเริ่มต้นใหม่ได้ทุกเมื่อ

ตัวอย่างต่อไปนี้แสดงวิธีสร้างการโต้ตอบกับสภาพแวดล้อมระยะไกลใหม่และดึงข้อมูลรหัสของการโต้ตอบ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas and matplotlib, verify the imports, and print the versions.",
    environment="remote",
)

print(f"Environment ID: {interaction.environment_id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas and matplotlib, verify the imports, and print the versions.",
    environment: "remote",
});

console.log(`Environment ID: ${interaction.environment_id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## พารามิเตอร์ `environment`

พารามิเตอร์ `environment` ยอมรับ 3 รูปแบบ ดังนี้

| ฟอร์ม | ตัวอย่าง | กรณีที่ควรใช้ |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | จัดเตรียมแซนด์บ็อกซ์ใหม่ |
| รหัสสภาพแวดล้อม | `environment="env_abc123"` | ใช้แซนด์บ็อกซ์ที่มีอยู่ซ้ำพร้อมไฟล์และแพ็กเกจทั้งหมด |
| ออบเจ็กต์การกำหนดค่า | `environment={...}` | จัดเตรียมแซนด์บ็อกซ์ใหม่ที่มีแหล่งที่มา กฎเครือข่าย หรือทั้ง 2 อย่าง |

ตัวอย่างต่อไปนี้แสดงวิธีใช้พารามิเตอร์ `environment` 3 วิธี

### Python

```
from google import genai

client = genai.Client()

# Fresh sandbox
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a hello world script.",
    environment="remote",
)

# Reuse an existing sandbox
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Modify the script to accept a name argument.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# New sandbox with sources
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List all files and summarize the project.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            }
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Fresh sandbox
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a hello world script.",
    environment: "remote",
});

// Reuse an existing sandbox
const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Modify the script to accept a name argument.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

// New sandbox with sources
const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List all files and summarize the project.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### REST

```
# Fresh sandbox
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d "{
    \"agent\": \"antigravity-preview-05-2026\",
    \"input\": [{\"type\": \"text\", \"text\": \"Modify the script to accept a name argument.\"}],
    \"environment\": \"$ENV_ID\",
    \"previous_interaction_id\": \"$INTERACTION_ID\"
}"

# New sandbox with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "List all files and summarize the project."}],
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            }
        ]
    }
}'
```

## กำหนดค่าสภาพแวดล้อม

วิธีหนึ่งในการตั้งค่าสภาพแวดล้อมคือการบอกตัวแทนว่าคุณต้องการติดตั้งอะไร
ตัวแทนจะจัดการการแก้ปัญหาการพึ่งพาอาศัยกันและการแก้ปัญหา เมื่อสภาพแวดล้อมพร้อมแล้ว ให้บันทึก `environment_id` แล้วนำไปใช้ซ้ำ

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment="remote",
)

# Reuse the configured environment
interaction_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction.id,
)

# Reuse the configured environment
interaction_3 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Using the tools in /workspace/tools, list the files.",
    environment=interaction.environment_id,
    previous_interaction_id=interaction_2.id,
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    environment: "remote",
});

const interaction2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Clone https://github.com/octocat/Spoon-Knife into /workspace/tools. Run the test suite and fix any missing dependencies.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction.id,
});

const interaction3 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Using the tools in /workspace/tools, list the files.",
    environment: interaction.environment_id,
    previous_interaction_id: interaction2.id,
});
console.log(interaction.output_text);
```

### REST

```
# Create interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### ติดตั้งจากแหล่งที่มา

หากทราบแน่ชัดว่าตัวแทนต้องการไฟล์ใด ให้ติดตั้งไฟล์เหล่านั้นในการเรียกใช้ครั้งเดียวแทนการวนซ้ำ ออบเจ็กต์การกำหนดค่า `environment` ยอมรับอาร์เรย์ `sources` 3 ประเภท ดังนี้

| ประเภทแหล่งที่มา | ค่า `type` | คำอธิบาย | ขีดจำกัด |
| --- | --- | --- | --- |
| ที่เก็บ Git | `repository` | โคลนที่เก็บจาก URL ลงในแซนด์บ็อกซ์ที่ `target` | 500 MB |
| Cloud Storage | `gcs` | คัดลอกไฟล์หรือไดเรกทอรีจาก Cloud Storage ลงในแซนด์บ็อกซ์ที่ `target` | 2 GB |
| เนื้อหาแบบอินไลน์ | `inline` | เขียนเนื้อหาข้อความดิบลงในไฟล์ในแซนด์บ็อกซ์ที่ `target` | 1 MB ต่อไฟล์, รวม 2 MB |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List all files under /workspace and describe what you find.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife",
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data",
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md",
            },
        ],
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List all files under /workspace and describe what you find.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/octocat/Spoon-Knife",
                target: "/workspace/spoon-knife",
            },
            {
                type: "gcs",
                source: "gs://cloud-samples-data/bigquery/us-states/",
                target: "/workspace/gcs-data",
            },
            {
                type: "inline",
                content: "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                target: "/workspace/notes/readme.md",
            },
        ],
    },
});

console.log(interaction.output_text);
```

### REST

```
# Create interaction with sources
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "List all files under /workspace and describe what you find.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/octocat/Spoon-Knife",
                "target": "/workspace/spoon-knife"
            },
            {
                "type": "gcs",
                "source": "gs://cloud-samples-data/bigquery/us-states/",
                "target": "/workspace/gcs-data"
            },
            {
                "type": "inline",
                "content": "# Project Notes\n\n- Analyze state population data\n- Create visualizations\n",
                "target": "/workspace/notes/readme.md"
            }
        ]
    }
}'
```

คุณสามารถใช้ทั้ง 2 แนวทางร่วมกันได้ นั่นคือ ติดตั้งแหล่งที่มาที่ทราบแบบประกาศ จากนั้นวนซ้ำด้วยการโต้ตอบติดตามผลเพื่อติดตั้งแพ็กเกจหรือเรียกใช้สคริปต์การตั้งค่า คุณไม่สามารถตั้งค่ารูท (`/`) เป็นเป้าหมายเมื่อเพิ่มแหล่งที่มาที่กำหนดเองได้ คุณต้องระบุไดเรกทอรีย่อยเสมอ

### ฮุก

นอกจากนี้ คุณยังติดตั้งไฟล์การกำหนดค่า `.agents/hooks.json` และสคริปต์การดักจับที่กำหนดเองลงในแซนด์บ็อกซ์เพื่อบังคับใช้การป้องกันด้านความปลอดภัยหรือเรียกใช้การตรวจสอบอัตโนมัติทุกครั้งที่เครื่องมือทำงานได้ด้วย ดูคำจำกัดความของสคีมาและโค้ดตัวอย่างได้ที่ [ฮุก](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=th)

### แหล่งที่มาแบบส่วนตัว

นอกจากนี้ คุณยังดาวน์โหลดจากที่เก็บ GitHub แบบส่วนตัวหรือ Bucket ของ Cloud Storage แบบส่วนตัวได้โดยเพิ่มข้อมูลเข้าสู่ระบบในการกำหนดค่าเครือข่าย ดังนี้

สำหรับ**ที่เก็บ Git แบบส่วนตัว** ให้ใช้การตรวจสอบสิทธิ์ `Basic` ด้วย
[โทเค็นเพื่อการเข้าถึงส่วนบุคคล (PAT) ของ GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
เข้ารหัสโทเค็นโดยใช้ `x-oauth-basic` เป็นชื่อผู้ใช้

```
echo -n "x-oauth-basic:ghp_YourPATHere" | base64
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run the test for my backend app and fix any issue.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run the test for my backend app and fix any issue.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app"
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Run the test for my backend app and fix any issue.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

สำหรับ**Bucket ของ Cloud Storage แบบส่วนตัว** ให้ใช้โทเค็น Bearer ของ OAuth 2.0 มาตรฐาน

```
gcloud auth print-access-token
```

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the discrepancies across the data in workspace",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "*.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    },
)
```

### JavaScript

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the discrepancies across the data in workspace",
    environment: {
        type: "remote",
        sources: [
            {
                type: "gcs",
                source: "gs://my-private-bucket/data",
                target: "/workspace",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    domain: "*"
                }
            ]
        }
    },
});
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the discrepancies across the data in workspace",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "gcs",
                "source": "gs://my-private-bucket/data",
                "target": "/workspace"
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer YOUR_GCS_TOKEN"
                    }
                },
                {
                    "domain": "*"
                }
            ]
        }
    }
}'
```

## ซอฟต์แวร์ที่ติดตั้งไว้ล่วงหน้า

แซนด์บ็อกซ์ทำงานบน Ubuntu และมาพร้อมกับรันไทม์และแพ็กเกจทั่วไปที่ติดตั้งไว้ล่วงหน้า ตัวแทนสามารถติดตั้งแพ็กเกจเพิ่มเติมในรันไทม์ได้โดยใช้ `pip
install` หรือ `npm install` แพ็กเกจที่ติดตั้งระหว่างการโต้ตอบจะยังคงอยู่เมื่อคุณใช้ `environment_id` เดียวกันซ้ำ

| หมวดหมู่ | แพ็กเกจที่ติดตั้งไว้ล่วงหน้า |
| --- | --- |
| **เครื่องมือ UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## การกำหนดค่าเครือข่าย

โดยค่าเริ่มต้น สภาพแวดล้อมจะมีการเข้าถึงเครือข่ายขาออกแบบไม่จำกัด ใช้ช่อง `network` เพื่อจำกัดการรับส่งข้อมูลขาออกไปยังโดเมนที่เฉพาะเจาะจง กฎแต่ละข้อจะระบุ `domain` และออบเจ็กต์ `transform` ที่ไม่บังคับเพื่อแทรกส่วนหัวลงในคำขอที่ตรงกัน ส่วนหัวเหล่านี้อาจไม่ซ้ำกันต่อการโต้ตอบ และคุณสามารถอัปเดตส่วนหัวสำหรับสภาพแวดล้อมเดียวกันได้

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `domain` | `string` | โดเมนที่จะจับคู่ ใช้ชื่อโฮสต์ที่แน่นอนหรือ `*` สำหรับโดเมนทั้งหมด |
| `transform` | `object` | ออบเจ็กต์ที่มีคู่คีย์-ค่าแบบแบนซึ่งแสดงถึงส่วนหัวที่จะแทรกลงในคำขอที่ตรงกัน เช่น `{"Authorization": "Bearer ..."}` |

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                {"domain": "pypi.org"},
                {"domain": "*"},
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Fetch the latest issues from the GitHub API for my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_your_github_token"
                    },
                },
                { domain: "pypi.org" },
                { domain: "*" },
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Fetch the latest issues from the GitHub API for my-org/my-repo."}],
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_your_github_token"
                    }
                },
                {"domain": "pypi.org"},
                {"domain": "*"}
            ]
        }
    }
}'
```

เมื่อตั้งค่ารายการที่อนุญาตไว้ ระบบจะอนุญาตเฉพาะคำขอที่ส่งไปยังโดเมนที่ระบุไว้อย่างชัดเจนเท่านั้น คุณสามารถใช้ไวลด์การ์ดเพื่อจับคู่โดเมนย่อย (เช่น `{"domain":
"*.example.com"}`) แต่โปรดทราบว่าไวลด์การ์ดนี้จะไม่จับคู่โดเมนราก
`example.com` ซึ่งต้องเพิ่มแยกต่างหาก หากต้องการอนุญาตการรับส่งข้อมูลอื่นๆ ทั้งหมด เช่น การกำหนดเส้นทางโดเมนที่ไม่ได้ระบุไว้โดยไม่มีส่วนหัวที่แทรก ให้เพิ่ม `{"domain": "*"}` เป็นรายการแบบครอบคลุม

### ข้อมูลเข้าสู่ระบบ

คุณสามารถเพิ่มข้อมูลเข้าสู่ระบบเพื่อให้ตัวแทนใช้ได้โดยเพิ่มการแปลงส่วนหัว พร็อกซีขาออกจะแทรกข้อมูลเข้าสู่ระบบในส่วนหัว HTTP ที่เกี่ยวข้อง โดยข้อมูลเข้าสู่ระบบจะไม่แสดงในแซนด์บ็อกซ์เป็นตัวแปรสภาพแวดล้อมหรือไฟล์

### Python

```
import subprocess
from google import genai

# Fetch a short-lived access token from your local gcloud CLI
gcloud_token = subprocess.check_output(
    ["gcloud", "auth", "print-access-token"], text=True
).strip()

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": f"Bearer {gcloud_token}"
                    },
                }
            ]
        },
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

import { execSync } from "child_process";

const gcloudToken = execSync("gcloud auth print-access-token").toString().trim();

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": `Bearer ${gcloudToken}`
                    },
                }
            ]
        }
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer <YOUR_GCLOUD_TOKEN>"
                    }
                }
            ]
        }
    }
}'
```

### ปิดใช้การเข้าถึงเครือข่าย

หากต้องการบล็อกการเข้าถึงเครือข่ายขาออกทั้งหมด ให้ตั้งค่า `network` เป็น `disabled`

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the local files only.",
    environment={
        "type": "remote",
        "network": "disabled",
    },
)

print(interaction.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Analyze the local files only.",
    environment: {
        type: "remote",
        network: "disabled",
    },
});

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

### รีเฟรชข้อมูลเข้าสู่ระบบ

ข้อมูลเข้าสู่ระบบ เช่น โทเค็นเพื่อการเข้าถึงและคีย์ API ที่มีอายุสั้นจะหมดอายุ
คุณสามารถรีเฟรชข้อมูลเข้าสู่ระบบได้โดยส่ง `environment_id` ที่มีอยู่พร้อมกับการกำหนดค่า `network` ใหม่ในการโต้ตอบครั้งถัดไป กฎเครือข่ายใหม่จะแทนที่กฎก่อนหน้าทั้งหมด ขณะที่สถานะระบบไฟล์ของสภาพแวดล้อม (แพ็กเกจ ไฟล์ ที่เก็บที่ติดตั้ง) จะยังคงอยู่

### Python

```
from google import genai

client = genai.Client()

# First interaction: use an initial token
first = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        },
    },
)

# Later: refresh the token on the same environment
result = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Now download the file reports/q1.csv from the same bucket.",
    environment={
        "type": "remote",
        "environment_id": first.environment_id,
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First interaction: use an initial token
const first = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "List the files in gs://my-bucket/reports/ using the GCS JSON API.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer INITIAL_TOKEN"
                    },
                }
            ]
        }
    },
});

// Later: refresh the token on the same environment
const result = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Now download the file reports/q1.csv from the same bucket.",
    environment: {
        type: "remote",
        environment_id: first.environment_id,
        network: {
            allowlist: [
                {
                    domain: "storage.googleapis.com",
                    transform: {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    },
                }
            ]
        }
    },
});

console.log(result.output_text);
```

### REST

```
# Use the environment_id from a previous interaction
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Now download the file reports/q1.csv from the same bucket.",
    "environment": {
        "type": "remote",
        "environment_id": "<ENVIRONMENT_ID_FROM_PREVIOUS_INTERACTION>",
        "network": {
            "allowlist": [
                {
                    "domain": "storage.googleapis.com",
                    "transform": {
                        "Authorization": "Bearer REFRESHED_TOKEN"
                    }
                }
            ]
        }
    }
}'
```

## วงจรการใช้งานสภาพแวดล้อม

สภาพแวดล้อมมีวงจรการใช้งานดังนี้

| สถานะ | พฤติกรรม |
| --- | --- |
| **สร้างแล้ว** | จัดเตรียมเมื่อการโต้ตอบระบุ `environment: "remote"` หรือออบเจ็กต์การกำหนดค่า |
| **ใช้งานอยู่** | ทำงานอยู่ขณะที่การโต้ตอบอยู่ระหว่างดำเนินการ |
| **ไม่มีการใช้งาน** | สร้างสแนปช็อตอัตโนมัติและหยุดทำงานหลังจากไม่มีการใช้งานเป็นเวลา 15 นาที |
| **ออฟไลน์** | เก็บไว้ 7 วันนับตั้งแต่ใช้งานครั้งล่าสุด กลับมาใช้งานต่อได้โดยส่งรหัส |
| **ลบแล้ว** | นำออกจากระบบโดยอัตโนมัติหลังจากระยะเวลาการเก็บรักษา TTL 7 วันหมดอายุหรือเมื่อลบด้วยตนเอง |

## Environments API

คุณสามารถใช้ Environments API เพื่อจัดการเซสชันแซนด์บ็อกซ์แบบเป็นโปรแกรมได้
การแจกแจงสภาพแวดล้อมช่วยให้คุณค้นหารหัสเซสชันที่ใช้งานอยู่และกู้คืนสถานะได้หากการเชื่อมต่อไคลเอ็นต์สิ้นสุดลงระหว่างงานที่ใช้เวลานาน นอกจากนี้ คุณยังตรวจสอบข้อมูลเมตาของเซสชันและลบสภาพแวดล้อมอย่างชัดเจนได้เมื่อเวิร์กโฟลว์เสร็จสิ้นแทนที่จะรอให้ TTL หมดอายุโดยอัตโนมัติ

### แสดงรายการสภาพแวดล้อม

แสดงรายการสภาพแวดล้อมที่ใช้งานอยู่ซึ่งเป็นของโปรเจ็กต์ของคุณ ใช้พารามิเตอร์การแบ่งหน้าเพื่อควบคุมขนาดกลุ่มการตอบกลับ

### Python

```
from google import genai

client = genai.Client()

for env in client.environments.list(page_size=10):
    print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const response = await client.environments.list({ pageSize: 10 });
for (const env of response.environments) {
    console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments?pageSize=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

คำตอบจะมีลักษณะคล้ายกับตัวอย่างต่อไปนี้

```
{
  "environments": [
    {
      "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
      "type": "remote"
    },
    {
      "environment_id": "362b738275a1d74af6f1c62bc050da73",
      "type": "remote"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

### รับสภาพแวดล้อม

ดึงข้อมูลเมตาและรายละเอียดการกำหนดค่าสำหรับสภาพแวดล้อมที่เฉพาะเจาะจงตามชื่อทรัพยากร

### Python

```
from google import genai

client = genai.Client()

env = client.environments.get(name="environments/YOUR_ENVIRONMENT_ID")
print(f"Environment ID: {env.environment_id}, Type: {env.type}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const env = await client.environments.get({ name: "environments/YOUR_ENVIRONMENT_ID" });
console.log(`Environment ID: ${env.environment_id}, Type: ${env.type}`);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

คำตอบจะมีลักษณะคล้ายกับตัวอย่างต่อไปนี้

```
{
  "environment_id": "140128b2a13c12c00a5a0d8cf7af9469",
  "type": "remote",
  "sources": [
    {
      "type": "repository",
      "source": "https://github.com/octocat/Spoon-Knife",
      "target": "/workspace/spoon-knife"
    }
  ],
  "network": {
    "allowlist": [
      {
        "domain": "api.github.com"
      },
      {
        "domain": "github.com"
      }
    ]
  }
}
```

### ลบสภาพแวดล้อม

ยุติและลบสภาพแวดล้อมอย่างชัดเจนเพื่อล้างทรัพยากรแซนด์บ็อกซ์เมื่องานหรือไปป์ไลน์เสร็จสิ้น

### Python

```
from google import genai

client = genai.Client()

client.environments.delete(name="environments/YOUR_ENVIRONMENT_ID")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

await client.environments.delete({ name: "environments/YOUR_ENVIRONMENT_ID" });
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/environments/YOUR_ENVIRONMENT_ID" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

## ดาวน์โหลดไฟล์จากสภาพแวดล้อม

ตัวแทนจะสร้างไฟล์ภายในแซนด์บ็อกซ์ระหว่างการดำเนินการ คุณสามารถดาวน์โหลดสแนปช็อตสภาพแวดล้อมแบบเต็มเป็นไฟล์ tar ได้โดยใช้ Files API ดังนี้

### Python

```
import os
import requests
import tarfile
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment="remote",
)

env_id = interaction.environment_id
api_key = os.environ.get("GEMINI_API_KEY")

response = requests.get(
    f"https://generativelanguage.googleapis.com/v1beta/files/environment-{env_id}:download",
    params={"alt": "media"},
    headers={"x-goog-api-key": api_key},
    allow_redirects=True,
)

with open("snapshot_env.tar", "wb") as f:
    f.write(response.content)

os.makedirs("extracted_env_snapshot", exist_ok=True)
with tarfile.open("snapshot_env.tar") as tar:
    tar.extractall(path="extracted_env_snapshot")

print(os.listdir("extracted_env_snapshot"))
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";
import { execSync } from "child_process";
import * as fs from "fs";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Write a file environments_test.txt with content 'Environments' inside the sandbox.",
    environment: "remote",
});

const envId = interaction.environment_id;
const apiKey = process.env.GEMINI_API_KEY || "";

const url = `https://generativelanguage.googleapis.com/v1beta/files/environment-${envId}:download?alt=media`;
const response = await fetch(url, {
    headers: {
        "x-goog-api-key": apiKey,
    },
});

if (!response.ok) {
    throw new Error(`Failed to download file: ${response.statusText}`);
}

const buffer = Buffer.from(await response.arrayBuffer());
fs.writeFileSync("snapshot_env.tar", buffer);

if (!fs.existsSync("extracted_env_snapshot")) {
    fs.mkdirSync("extracted_env_snapshot");
}
execSync("tar -xf snapshot_env.tar -C extracted_env_snapshot");

console.log(fs.readdirSync("extracted_env_snapshot"));
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Write a file environments_test.txt with content '\''Environments'\'' inside the sandbox.",
    "environment": "remote"
}'
# Step 2: Download snapshot (reusing environment ID from Step 1)
# curl -L -X GET "https://generativelanguage.googleapis.com/v1beta/files/environment-$ENV_ID:download?alt=media" \
#   -H "x-goog-api-key: $API_KEY" \
#   -o snapshot.tar
```

## ราคาและทรัพยากร

สภาพแวดล้อมแต่ละรายการทำงานด้วยการจัดสรรทรัพยากรแบบคงที่ ดังนี้

| ทรัพยากร | ค่า |
| --- | --- |
| **CPU** | 4 แกน |
| **หน่วยความจำ** | 16 GB |

ระบบจะ**ไม่เรียกเก็บเงิน** ค่าคอมพิวต์ของสภาพแวดล้อม (CPU, หน่วยความจำ, การดำเนินการแซนด์บ็อกซ์) ในช่วงระยะเวลาแสดงตัวอย่าง ดูค่าใช้จ่ายโทเค็นของตัวแทนได้ที่
[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#pricing-for-agents)สำหรับ

## ข้อจำกัด

- **สถานะแสดงตัวอย่าง:** สภาพแวดล้อมและตัวแทนที่มีการจัดการอยู่ในช่วงแสดงตัวอย่าง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **ขนาดแหล่งที่มาแบบอินไลน์:** แหล่งที่มาแบบอินไลน์จำกัดไว้ที่ 1 MB ต่อไฟล์ และรวม 2 MB สำหรับไฟล์ทั้งหมด
- **ขนาดแหล่งที่มา**: ที่เก็บ Git จำกัดไว้ที่ 500 MB และที่เก็บ Cloud Storage จำกัดไว้ที่ 2 GB
- **การเริ่มต้นสภาพแวดล้อม:** การจัดเตรียมสภาพแวดล้อมใหม่ใช้เวลาสูงสุดประมาณ 5 วินาที ที่เก็บแหล่งที่มาขนาดใหญ่อาจทำให้ใช้เวลานานขึ้น
- **การหมดอายุของสภาพแวดล้อม:** ระบบจะเก็บสภาพแวดล้อมแบบออฟไลน์ที่ไม่มีการใช้งานไว้ 7 วันก่อนที่จะหมดอายุโดยใช้การล้างข้อมูล TTL อัตโนมัติ การส่งรหัสสภาพแวดล้อมที่หมดอายุหรือ
  ไม่ถูกต้องจะแสดงข้อผิดพลาด `404 Not Found`
- **การรองรับไฟล์:** ปัจจุบันตัวแทนอ่านได้เฉพาะไฟล์ข้อความและรูปภาพ ยังไม่รองรับไฟล์ไบนารี
- **ไม่สามารถติดตั้งจากรูทได้:** คุณไม่สามารถตั้งค่ารูท (`/`) เป็นเป้าหมายเมื่อเพิ่มแหล่งที่มาที่กำหนดเองได้ คุณต้องระบุไดเรกทอรีย่อยเสมอ

## ขั้นตอนถัดไป

- [ภาพรวมของตัวแทน](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของตัวแทนที่มีการจัดการ
- [คู่มือเริ่มใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): เริ่มสร้างด้วยการสนทนาไปมาและการสตรีม
- [ตัวแทน Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): สำรวจความสามารถ เครื่องมือ การเลือกโมเดล และราคาสำหรับตัวแทนเริ่มต้น
- [การสร้างตัวแทนที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th): กำหนดตัวแทนของคุณเองโดยใช้ `AGENTS.md` และ `SKILL.md`
- [ฮุก](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=th): บังคับใช้การป้องกันด้านความปลอดภัยและเรียกใช้การตรวจสอบผลข้างเคียงภายในแซนด์บ็อกซ์

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-08-19 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-08-19 UTC"],[],[]]
