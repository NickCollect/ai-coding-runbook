---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=th
fetched_at: 2026-05-25T05:18:34.152075+00:00
title: "\u0e2a\u0e20\u0e32\u0e1e\u0e41\u0e27\u0e14\u0e25\u0e49\u0e2d\u0e21\u0e43\u0e19 Agent \u0e17\u0e35\u0e48\u0e21\u0e35\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Gemini Deep Research](https://ai.google.dev/gemini-api/docs/deep-research?hl=th) พร้อมให้บริการในเวอร์ชันพรีวิวแล้วตอนนี้ โดยมีฟีเจอร์การวางแผนร่วมกัน การแสดงภาพข้อมูล การรองรับ MCP และอื่นๆ

![](https://ai.google.dev/_static/images/translated.svg?hl=th)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [หน้าแรก](https://ai.google.dev/?hl=th)
- [Gemini API](https://ai.google.dev/gemini-api?hl=th)
- [เอกสาร](https://ai.google.dev/gemini-api/docs?hl=th)

ส่งความคิดเห็น

# สภาพแวดล้อมใน Agent ที่มีการจัดการ

สภาพแวดล้อมคือแซนด์บ็อกซ์ Linux ที่มีการจัดการซึ่งช่วยให้เอเจนต์มีพื้นที่แยกต่างหากสำหรับ
เรียกใช้โค้ดและคงไฟล์ไว้ โดยจะแยกออกจากบริบทการโต้ตอบ คุณจึงนำสภาพแวดล้อมเดียวกันไปใช้ซ้ำในการโต้ตอบหลายครั้งหรือเริ่มใหม่ได้ทุกเมื่อ

ตัวอย่างต่อไปนี้แสดงวิธีสร้างการโต้ตอบกับสภาพแวดล้อมระยะไกลใหม่และดึงข้อมูลรหัส

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas and matplotlib, verify the imports, and print the versions.",
    "environment": "remote"
}'
```

## พารามิเตอร์ `environment`

พารามิเตอร์ `environment` ยอมรับ 3 รูปแบบ ได้แก่

| แบบฟอร์ม | ตัวอย่าง | กรณีที่ควรใช้ |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | จัดสรรแซนด์บ็อกซ์ใหม่ |
| รหัสสภาพแวดล้อม | `environment="env_abc123"` | นำแซนด์บ็อกซ์ที่มีอยู่พร้อมไฟล์และแพ็กเกจทั้งหมดมาใช้ซ้ำ |
| ออบเจ็กต์การกำหนดค่า | `environment={...}` | จัดสรรแซนด์บ็อกซ์ใหม่ที่มีแหล่งที่มา กฎเครือข่าย หรือทั้งสองอย่าง |

ตัวอย่างต่อไปนี้แสดงวิธีใช้พารามิเตอร์ `environment`
3 วิธี

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": [{"type": "text", "text": "Write a hello world script."}],
    "environment": "remote"
}'

# Reuse an existing sandbox (replace $ENV_ID and $INTERACTION_ID with values from the previous response)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H "Api-Revision: 2026-05-20" \
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
-H "Api-Revision: 2026-05-20" \
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

วิธีหนึ่งในการตั้งค่าสภาพแวดล้อมคือการบอก Agent ว่าคุณต้องการติดตั้งอะไร
โดยจะจัดการการแก้ปัญหาการขึ้นต่อกันและการแก้ปัญหา เมื่อสภาพแวดล้อมพร้อมแล้ว ให้บันทึก `environment_id` แล้วนำไปใช้ซ้ำ

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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Install pandas, matplotlib, and seaborn. Verify all imports work and print the installed versions.",
    "environment": "remote"
}'
```

### เมานต์จากแหล่งที่มา

หากคุณทราบว่าเอเจนต์ต้องการไฟล์ใดบ้าง ให้ติดตั้งไฟล์เหล่านั้นในการเรียกใช้ครั้งเดียว
แทนที่จะทำซ้ำ `environment`ออบเจ็กต์การกำหนดค่ารับ`sources`อาร์เรย์
ที่มี 3 ประเภท ดังนี้

| ประเภทแหล่งที่มา | ค่า `type` | คำอธิบาย | ขีดจำกัด |
| --- | --- | --- | --- |
| ที่เก็บ Git | `repository` | โคลนที่เก็บจาก URL ลงในแซนด์บ็อกซ์ที่ `target` | 500 MB |
| Cloud Storage | `gcs` | คัดลอกไฟล์หรือไดเรกทอรีจาก Cloud Storage ไปยังแซนด์บ็อกซ์ที่ `target` | 2 GB |
| เนื้อหาในบรรทัด | `inline` | เขียนเนื้อหาข้อความดิบไปยังไฟล์ในแซนด์บ็อกซ์ที่ `target` | 1 MB ต่อไฟล์ รวม 2 MB |

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
-H "Api-Revision: 2026-05-20" \
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

คุณสามารถใช้ทั้ง 2 วิธีร่วมกันได้ โดยประกาศแหล่งที่มาที่รู้จัก จากนั้นทำซ้ำ
ด้วยการโต้ตอบติดตามผลเพื่อติดตั้งแพ็กเกจหรือเรียกใช้สคริปต์การตั้งค่า คุณไม่สามารถ
ตั้งค่ารูท (`/`) เป็นเป้าหมายเมื่อเพิ่มแหล่งที่มาที่กำหนดเองได้ คุณต้องระบุ
ไดเรกทอรีย่อยเสมอ

### แหล่งข้อมูลส่วนตัว

นอกจากนี้ คุณยังดาวน์โหลดจากที่เก็บ GitHub ส่วนตัวหรือที่เก็บข้อมูล Cloud
Storage ส่วนตัวได้โดยเพิ่มข้อมูลเข้าสู่ระบบในการกำหนดค่าเครือข่าย ดังนี้

สำหรับ**ที่เก็บ Git ส่วนตัว** ให้ใช้การตรวจสอบสิทธิ์ `Basic` ด้วย
[โทเค็นการเข้าถึงส่วนตัวของ GitHub
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
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
-H "Api-Revision: 2026-05-20" \
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

สำหรับ**ที่เก็บข้อมูล Cloud Storage แบบส่วนตัว** ให้ใช้โทเค็นสำหรับผู้ถือ OAuth 2.0 มาตรฐาน

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
-H "Api-Revision: 2026-05-20" \
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

แซนด์บ็อกซ์ทำงานบน Ubuntu และมาพร้อมกับรันไทม์และแพ็กเกจทั่วไปที่
ติดตั้งไว้ล่วงหน้า เอเจนต์สามารถติดตั้งแพ็กเกจเพิ่มเติมในขณะรันไทม์ได้โดยใช้ `pip
install` หรือ `npm install` แพ็กเกจที่ติดตั้งระหว่างการโต้ตอบจะยังคงอยู่เมื่อ
คุณใช้ `environment_id` เดิมซ้ำ

| หมวดหมู่ | แพ็กเกจที่ติดตั้งไว้ล่วงหน้า |
| --- | --- |
| **เครื่องมือ UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## การกำหนดค่าเครือข่าย

โดยค่าเริ่มต้น สภาพแวดล้อมจะมีสิทธิ์เข้าถึงเครือข่ายขาออกแบบไม่จำกัด ใช้ฟิลด์
`network` เพื่อจำกัดการรับส่งขาออกไปยังโดเมนที่เฉพาะเจาะจง แต่ละกฎ
จะระบุออบเจ็กต์ `domain` และออบเจ็กต์ `transform` ที่ไม่บังคับเพื่อแทรกส่วนหัวลงในคำขอที่ตรงกัน
ส่วนหัวเหล่านี้อาจไม่ซ้ำกันต่อการโต้ตอบแต่ละครั้ง และคุณสามารถอัปเดตส่วนหัวสำหรับสภาพแวดล้อมเดียวกันได้

| ช่อง | ประเภท | คำอธิบาย |
| --- | --- | --- |
| `domain` | `string` | โดเมนที่จะจับคู่ ใช้ชื่อโฮสต์ที่แน่นอนหรือ `*` สำหรับโดเมนทั้งหมด |
| `transform` | `object` | ออบเจ็กต์ที่มีคู่คีย์-ค่าแบบเรียบซึ่งแสดงถึงส่วนหัวที่จะแทรกลงในคำขอที่ตรงกัน เช่น `{"Authorization": "Bearer ..."}` |

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
-H "Api-Revision: 2026-05-20" \
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

เมื่อตั้งค่ารายการที่อนุญาต ระบบจะอนุญาตเฉพาะคำขอไปยังโดเมนที่ระบุไว้อย่างชัดเจนเท่านั้น
คุณใช้ไวลด์การ์ดเพื่อจับคู่โดเมนย่อยได้ (เช่น `{"domain":
"*.example.com"}`) แต่โปรดทราบว่าไวลด์การ์ดนี้จะไม่จับคู่โดเมนราก
`example.com` ซึ่งต้องเพิ่มแยกต่างหาก หากต้องการอนุญาตการรับส่งอื่นๆ ทั้งหมด เช่น การกำหนดเส้นทางโดเมนที่ไม่ได้อยู่ในรายการโดยไม่มีส่วนหัวที่แทรก ให้เพิ่ม `{"domain": "*"}` เป็นรายการที่ครอบคลุมทั้งหมด

### ข้อมูลเข้าสู่ระบบ

คุณเพิ่มข้อมูลเข้าสู่ระบบเพื่อให้เอเจนต์ใช้ได้โดยการเพิ่มการเปลี่ยนส่วนหัว พร็อกซีขาออกจะแทรกข้อมูลเข้าสู่ระบบในส่วนหัว HTTP ที่เกี่ยวข้อง แต่จะไม่แสดงข้อมูลดังกล่าวภายในแซนด์บ็อกซ์เป็นตัวแปรสภาพแวดล้อมหรือไฟล์

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
-H "Api-Revision: 2026-05-20" \
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
-H "Api-Revision: 2026-05-20" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the local files only.",
    "environment": {
        "type": "remote",
        "network": "disabled"
    }
}'
```

## วงจรของสภาพแวดล้อม

สภาพแวดล้อมมีวงจรดังนี้

| รัฐ | พฤติกรรม |
| --- | --- |
| **สร้างแล้ว** | จัดสรรเมื่อการโต้ตอบระบุ `environment: "remote"` หรือออบเจ็กต์การกำหนดค่า |
| **ใช้งานอยู่** | การเรียกใช้ขณะที่การโต้ตอบกำลังดำเนินการ |
| **ไม่มีการใช้งาน** | ถ่ายภาพอัตโนมัติและหยุดหลังจากไม่มีการใช้งาน 15 นาที |
| **ออฟไลน์** | เก็บไว้เป็นเวลา 7 วันนับตั้งแต่ใช้งานครั้งล่าสุด กลับมาทำงานต่อได้โดยส่งรหัส |
| **ลบแล้ว** | นำออกจากระบบแล้ว |

## ดาวน์โหลดไฟล์จากสภาพแวดล้อม

Agent จะสร้างไฟล์ภายในแซนด์บ็อกซ์ระหว่างการดำเนินการ คุณดาวน์โหลดภาพรวมสภาพแวดล้อมทั้งหมดเป็นไฟล์ tar ได้โดยใช้ Files API ดังนี้

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
-H "Api-Revision: 2026-05-20" \
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

## ราคาและแหล่งข้อมูล

แต่ละสภาพแวดล้อมจะทำงานโดยมีการจัดสรรทรัพยากรแบบคงที่ ดังนี้

| ทรัพยากร | ค่า |
| --- | --- |
| **CPU** | 4 แกน |
| **หน่วยความจำ** | 16 GB |

ระบบจะ**ไม่เรียกเก็บเงิน**สำหรับการประมวลผลสภาพแวดล้อม (CPU, หน่วยความจำ, การดำเนินการในแซนด์บ็อกซ์) ในช่วงระยะเวลาแสดงตัวอย่าง
ดู[ราคา](https://ai.google.dev/gemini-api/docs/pricing?hl=th#pricing-for-agents)สำหรับ
ค่าใช้จ่ายของโทเค็นเอเจนต์

## ข้อจำกัด

- **สถานะเวอร์ชันตัวอย่าง:** สภาพแวดล้อมและตัวแทนที่มีการจัดการอยู่ในเวอร์ชันตัวอย่าง ฟีเจอร์และสคีมาอาจมีการเปลี่ยนแปลง
- **ขนาดแหล่งข้อมูลในบรรทัด:** แหล่งข้อมูลในบรรทัดจำกัดไว้ที่ 1 MB ต่อไฟล์ และ 2 MB โดยรวมในทุกไฟล์
- **ขนาดแหล่งข้อมูล**: ที่เก็บ Git มีขนาดจำกัดอยู่ที่ 500 MB และที่เก็บ Cloud Storage มีขนาดจำกัดอยู่ที่ 2 GB
- **การเริ่มต้นสภาพแวดล้อม:** การจัดสรรสภาพแวดล้อมใหม่จะใช้เวลาไม่เกิน 5 วินาทีโดยประมาณ ที่เก็บแหล่งข้อมูลขนาดใหญ่อาจทำให้เวลาในการดำเนินการนานขึ้น
- **การรองรับไฟล์:** ปัจจุบันเอเจนต์อ่านได้เฉพาะไฟล์ข้อความและรูปภาพ ยังไม่พร้อมให้บริการรองรับไฟล์ไบนารี
- **ไม่สามารถติดตั้งจากรูท:** คุณไม่สามารถตั้งค่ารูท (`/`) เป็นเป้าหมายเมื่อเพิ่มแหล่งที่มาที่กำหนดเองได้ คุณต้องระบุไดเรกทอรีย่อยเสมอ

## ขั้นตอนถัดไป

- [ภาพรวมของ Agent](https://ai.google.dev/gemini-api/docs/agents?hl=th): ดูข้อมูลเกี่ยวกับแนวคิดหลักของ Agent ที่มีการจัดการ
- [เริ่มต้นใช้งานฉบับย่อ](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=th): เริ่มสร้างด้วยการสนทนาแบบหลายรอบและการสตรีม
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=th): สำรวจความสามารถ เครื่องมือ และราคาของเอเจนต์เริ่มต้น
- [การสร้าง Agent ที่กำหนดเอง](https://ai.google.dev/gemini-api/docs/custom-agents?hl=th): กำหนด Agent ของคุณเองโดยใช้ `AGENTS.md` และ `SKILL.md`

ส่งความคิดเห็น

เนื้อหาของหน้าเว็บนี้ได้รับอนุญาตภายใต้[ใบอนุญาตที่ต้องระบุที่มาของครีเอทีฟคอมมอนส์ 4.0](https://creativecommons.org/licenses/by/4.0/) และตัวอย่างโค้ดได้รับอนุญาตภายใต้[ใบอนุญาต Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) เว้นแต่จะระบุไว้เป็นอย่างอื่น โปรดดูรายละเอียดที่[นโยบายเว็บไซต์ Google Developers](https://developers.google.com/site-policies?hl=th) Java เป็นเครื่องหมายการค้าจดทะเบียนของ Oracle และ/หรือบริษัทในเครือ

อัปเดตล่าสุด 2026-05-20 UTC

หากต้องการบอกให้เราทราบเพิ่มเติม

[[["เข้าใจง่าย","easyToUnderstand","thumb-up"],["แก้ปัญหาของฉันได้","solvedMyProblem","thumb-up"],["อื่นๆ","otherUp","thumb-up"]],[["ไม่มีข้อมูลที่ฉันต้องการ","missingTheInformationINeed","thumb-down"],["ซับซ้อนเกินไป/มีหลายขั้นตอนมากเกินไป","tooComplicatedTooManySteps","thumb-down"],["ล้าสมัย","outOfDate","thumb-down"],["ปัญหาเกี่ยวกับการแปล","translationIssue","thumb-down"],["ตัวอย่าง/ปัญหาเกี่ยวกับโค้ด","samplesCodeIssue","thumb-down"],["อื่นๆ","otherDown","thumb-down"]],["อัปเดตล่าสุด 2026-05-20 UTC"],[],[]]
