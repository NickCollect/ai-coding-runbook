---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar
fetched_at: 2026-06-08T05:34:00.255784+00:00
title: "\u0627\u0644\u0628\u064a\u0626\u0627\u062a \u0641\u064a \u0627\u0644\u0648\u0643\u0644\u0627\u0621 \u0627\u0644\u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

تتوفّر الآن ميزة [Deep Research من Gemini](https://ai.google.dev/gemini-api/docs/deep-research?hl=ar) في إصدار تجريبي يتضمّن ميزات التخطيط التعاوني والتصوّر ودعم MCP والمزيد.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البيئات في الوكلاء المُدارين

البيئات هي صناديق حماية مُدارة في Linux تمنح الوكلاء مكانًا معزولاً لتنفيذ الرموز البرمجية والاحتفاظ بالملفات. وهي منفصلة عن سياق التفاعل، لذا يمكنك إعادة استخدام البيئة نفسها في تفاعلات متعددة أو البدء من جديد في أي وقت.

يوضّح المثال التالي كيفية إنشاء تفاعل مع بيئة بعيدة جديدة واسترداد رقم تعريفها:

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

## المَعلمة `environment`

تقبل المَعلمة `environment` ثلاثة أشكال:

| النموذج | مثال | حالات الاستخدام |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | توفير صندوق حماية جديد |
| رقم تعريف البيئة | `environment="env_abc123"` | إعادة استخدام صندوق حماية حالي مع جميع ملفاته وحِزمه |
| كائن الإعداد | `environment={...}` | توفير صندوق حماية جديد مع مصادر أو قواعد شبكة أو كليهما |

توضّح الأمثلة التالية الطرق الثلاث لاستخدام المَعلمة `environment`.

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

## ضبط بيئة

إحدى طرق إعداد بيئة هي إخبار الوكيل بما تحتاج إلى تثبيته.
يتولّى الوكيل حلّ التبعيات وتحديد المشاكل وحلّها. بعد أن تصبح البيئة جاهزة، احفظ `environment_id` وأعِد استخدامه.

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

### الربط من مصدر

إذا كنت تعرف الملفات التي يحتاجها الوكيل بالضبط، يمكنك ربطها في طلب واحد بدلاً من تكرار العملية. يقبل كائن إعداد `environment` مصفوفة `sources` تتضمّن ثلاثة أنواع:

| نوع المصدر | قيمة `type` | الوصف | الحدّ |
| --- | --- | --- | --- |
| مستودع Git | `repository` | يستنسخ مستودعًا من عنوان URL إلى صندوق الحماية في `target`. | 500 ميغابايت |
| Cloud Storage | `gcs` | ينسخ ملفًا أو دليلًا من Cloud Storage إلى صندوق الحماية في `target`. | 2 غيغابايت |
| محتوى مضمّن | `inline` | يكتب محتوى نصيًا خامًا في ملف في صندوق الحماية في `target`. | 1 ميغابايت لكل ملف، و2 ميغابايت إجمالاً |

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

يمكنك الجمع بين الطريقتَين: ربط المصادر المعروفة بشكلٍ إعلاني، ثم تكرار العملية باستخدام تفاعلات المتابعة لتثبيت الحِزم أو تشغيل النصوص البرمجية للإعداد. لا يمكنك ضبط الجذر (`/`) كهدف عند إضافة مصدر مخصّص، ويجب دائمًا تحديد دليل فرعي.

### المصادر الخاصة

يمكنك أيضًا التنزيل من مستودعات Github الخاصة أو حِزم Cloud Storage الخاصة عن طريق إضافة بيانات الاعتماد في إعدادات الشبكة:

بالنسبة إلى **مستودعات Git الخاصة**، استخدِم `Basic` المصادقة مع
[رمز الوصول الشخصي في GitHub
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
يمكنك ترميز الرمز المميّز باستخدام `x-oauth-basic` كاسم المستخدم:

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

بالنسبة إلى **حِزم Cloud Storage الخاصة**، استخدِم رمزًا مميّزًا عاديًا من نوع OAuth 2.0 Bearer:

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

## البرامج المثبَّتة مسبقًا

يعمل صندوق الحماية على Ubuntu ويأتي مع أوقات تشغيل وحِزم شائعة مثبَّتة مسبقًا. يمكن للوكيل تثبيت حِزم إضافية في وقت التشغيل باستخدام `pip
install` أو `npm install`. تظل الحِزم المثبَّتة أثناء التفاعل محفوظة عند إعادة استخدام `environment_id` نفسه.

| الفئة | الحِزم المثبَّتة مسبقًا |
| --- | --- |
| **أدوات UNIX** | `curl` و`wget` و`git` و`rsync` و`unzip` و`ripgrep` و`fd-find` و`gawk` و`bc` و`tree` و`which` و`lsof` و`htop` و`jq` و`iproute2` و`procps` و`gcloud CLI` |
| **Python 3.12** | `numpy` و`pandas` و`requests` و`google-genai` و`beautifulsoup4` و`pyyaml` و`ast-grep-cli` |
| **Node.js 22** | `create-next-app` و`create-vite` و`typescript` |

## إعدادات الشبكة

تتضمّن البيئات تلقائيًا إمكانية الوصول إلى الشبكة الصادرة بدون أي قيود. استخدِم الحقل `network` لحظر الزيارات الصادرة إلى نطاقات معيّنة. تحدّد كل قاعدة `domain` وكائن `transform` اختياريًا لإضافة عناوين إلى الطلبات المطابقة. يمكن أن تكون هذه العناوين فريدة لكل تفاعل، ويمكنك تعديلها للبيئة نفسها.

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `domain` | `string` | النطاق المطلوب مطابقته استخدِم اسم مضيف مطابقًا أو `*` لجميع النطاقات. |
| `transform` | `object` | كائن يحتوي على أزواج مفتاح/قيمة مسطّحة تمثّل العناوين المطلوب إضافتها إلى الطلبات المطابقة، مثلاً `{"Authorization": "Bearer ..."}`. |

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

عند ضبط قائمة مسموح بها، لا يُسمح إلا بالطلبات الموجّهة إلى النطاقات المُدرَجة بشكلٍ صريح. يمكنك استخدام أحرف البدل لمطابقة النطاقات الفرعية (مثلاً، `{"domain":
"*.example.com"}`)، ولكن يُرجى العِلم أنّ ذلك لا يطابق النطاق الرئيسي
`example.com`، الذي يجب إضافته بشكلٍ منفصل. للسماح بجميع الزيارات الأخرى، مثل
توجيه النطاقات غير المُدرَجة بدون إضافة عناوين، أضِف `{"domain": "*"}` كإدخال
شامل.

### بيانات الاعتماد

يمكنك إضافة بيانات اعتماد ليستخدمها وكيلك عن طريق إضافة عمليات تحويل العناوين. يتم إدخال بيانات الاعتماد في عناوين HTTP المعنيّة من خلال وكيل الخروج، ولا يتم عرضها مطلقًا داخل صندوق الحماية كمتغيّرات بيئية أو ملفات.

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

### إيقاف إمكانية الوصول إلى الشبكة

لحظر جميع إمكانية الوصول إلى الشبكة الصادرة، اضبط `network` على `disabled`:

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

## دورة حياة البيئة

تتّبِع البيئات دورة الحياة التالية:

| الحالة | السلوك |
| --- | --- |
| **تم الإنشاء** | يتم توفيرها عندما يحدّد أحد التفاعلات `environment: "remote"` أو كائن إعداد. |
| **نشطة** | تكون قيد التشغيل أثناء تقدّم التفاعل. |
| **غير مستخدَم من قِبل أي برنامج حاليًا** | يتم أخذ لقطة تلقائية وإيقافها بعد 15 دقيقة من عدم النشاط. |
| **بلا إنترنت** | يتم الاحتفاظ بها لمدة 7 أيام منذ آخر نشاط. يمكن استئنافها عن طريق تمرير رقم تعريفها. |
| **تم الحذف** | تمت إزالتها من النظام. |

## تنزيل الملفات من البيئة

ينشئ الوكيل ملفات داخل صندوق الحماية أثناء التنفيذ. يمكنك تنزيل لقطة البيئة الكاملة كملف tar باستخدام Files API:

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

## الأسعار والمراجع

تعمل كل بيئة مع تخصيصات موارد ثابتة:

| المورد | القيمة |
| --- | --- |
| **وحدة المعالجة المركزية** | 4 أنوية |
| **الذاكرة** | 16 غيغابايت |

**لا يتم تحصيل رسوم** مقابل حوسبة البيئة (وحدة المعالجة المركزية والذاكرة وتنفيذ صندوق الحماية) خلال فترة المعاينة. راجِع
[الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#pricing-for-agents) لمعرفة
تكاليف الرموز المميّزة للوكيل.

## القيود

- **حالة المعاينة:** البيئات والوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **حجم المصدر المضمّن:** يقتصر حجم المصادر المضمّنة على 1 ميغابايت لكل ملف، و2 ميغابايت إجمالاً لجميع الملفات.
- **حجم المصدر**: يقتصر حجم مستودعات Git على 500 ميغابايت ومستودعات Cloud Storage على 2 غيغابايت.
- **بدء تشغيل البيئة:** يستغرق توفير بيئة جديدة ما يصل إلى 5 ثوانٍ تقريبًا. قد يؤدي استخدام مستودعات مصادر كبيرة إلى زيادة هذا الوقت.
- **تنسيقات الملفات المتوافقة:** يقتصر الوكيل حاليًا على قراءة الملفات النصية وملفات الصور. ولا تتوفّر بعد إمكانية قراءة الملفات الثنائية.
- **لا يمكن الربط من الجذر:** لا يمكنك ضبط الجذر (`/`) كهدف عند إضافة مصدر مخصّص، ويجب دائمًا تحديد دليل فرعي.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): تعرَّف على المفاهيم الأساسية للوكلاء المُدارين.
- [دليل البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): ابدأ في إنشاء محادثات متعددة الأدوار وبث المحتوى.
- [وكيل Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): استكشِف الإمكانات والأدوات والأسعار للوكيل التلقائي.
- [إنشاء وكلاء مخصّصين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar): حدِّد الوكلاء الخاصين بك باستخدام `AGENTS.md` و`SKILL.md`.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-05-20 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-05-20 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
