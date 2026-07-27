---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=ar
fetched_at: 2026-07-27T04:44:35.953045+00:00
title: "\u0627\u0644\u0628\u064a\u0626\u0627\u062a \u0641\u064a \u0627\u0644\u0648\u0643\u0644\u0627\u0621 \u0627\u0644\u0645\u064f\u062f\u0627\u0631\u064a\u0646 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

أصبحت [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ar) متاحة الآن للجميع. ننصحك باستخدام واجهة برمجة التطبيقات هذه للوصول إلى جميع أحدث الميزات والنماذج.

![](https://ai.google.dev/_static/images/translated.svg?hl=ar)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [الصفحة الرئيسية](https://ai.google.dev/?hl=ar)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ar)
- [المستندات](https://ai.google.dev/gemini-api/docs?hl=ar)

إرسال ملاحظات

# البيئات في الوكلاء المُدارين

البيئات هي مساحات معزولة في Linux تتم إدارتها وتوفّر للوكلاء مكانًا معزولاً لتنفيذ الرموز البرمجية والاحتفاظ بالملفات. وهي منفصلة عن سياق التفاعل، لذا يمكنك إعادة استخدام البيئة نفسها في تفاعلات متعددة أو البدء من جديد في أي وقت.

يوضّح المثال التالي كيفية إنشاء تفاعل مع بيئة بعيدة جديدة واسترداد معرّفها:

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

## المَعلمة `environment`

تقبل المَعلمة `environment` ثلاثة أشكال:

| النموذج | مثال | حالات الاستخدام |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | توفير وضع حماية جديد |
| رقم تعريف البيئة | `environment="env_abc123"` | إعادة استخدام بيئة اختبار حالية تتضمّن جميع ملفاتها وحِزمها |
| عنصر الإعداد | `environment={...}` | توفير بيئة اختبار جديدة تتضمّن مصادر أو قواعد شبكة أو كليهما |

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

## ضبط بيئة

إحدى طرق إعداد بيئة هي إخبار الوكيل بما تحتاج إلى تثبيته.
يتعامل مع حلّ المشاكل المتعلقة بالتبعيات واستكشاف الأخطاء وحلّها. بعد أن تصبح البيئة جاهزة، احفظ `environment_id` وأعِد استخدامه.

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

### التحميل من مصدر

إذا كنت تعرف بالضبط الملفات التي يحتاجها الوكيل، يمكنك تحميلها في طلب واحد بدلاً من تكرار العملية. يقبل عنصر الضبط `environment` مصفوفة `sources` تتضمّن ثلاثة أنواع:

| نوع المصدر | قيمة `type` | الوصف | الحدّ |
| --- | --- | --- | --- |
| مستودع Git | `repository` | يستنسخ هذا الأمر مستودعًا من عنوان URL إلى البيئة التجريبية في `target`. | ‫500 ميغابايت |
| Cloud Storage | `gcs` | تنسخ هذه السمة ملفًا أو دليلاً من Cloud Storage إلى وضع الحماية في `target`. | 2 غيغابايت |
| المحتوى المضمّن | `inline` | يكتب محتوى نصيًا أوليًا في ملف في وضع الحماية على `target`. | ‫1 ميغابايت لكل ملف، و2 ميغابايت إجمالاً |

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

يمكنك الجمع بين الطريقتين: تثبيت المصادر المعروفة بشكل تعريفي، ثم تكرار العملية مع تفاعلات المتابعة لتثبيت الحِزم أو تشغيل نصوص الإعداد البرمجية. لا يمكنك ضبط الجذر (`/`) كهدف عند إضافة مصدر مخصّص، بل عليك دائمًا تحديد دليل فرعي.

### المصادر الخاصة

يمكنك أيضًا تنزيل البيانات من مستودعات GitHub الخاصة أو حِزم Cloud Storage الخاصة من خلال إضافة بيانات الاعتماد في إعدادات الشبكة:

بالنسبة إلى **مستودعات Git الخاصة**، استخدِم مصادقة `Basic` مع [رمز الوصول الشخصي (PAT) في GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
ترميز الرمز المميز باستخدام `x-oauth-basic` كاسم المستخدم:

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

بالنسبة إلى **حِزم Cloud Storage الخاصة**، استخدِم رمزًا مميزًا عاديًا من النوع Bearer لبروتوكول OAuth 2.0:

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

## البرامج المثبَّتة مسبقًا

يعمل وضع الحماية على نظام التشغيل Ubuntu ويتضمّن أوقات تشغيل وحِزم شائعة
مثبّتة مسبقًا. يمكن للوكيل تثبيت حِزم إضافية في وقت التشغيل باستخدام `pip
install` أو `npm install`. تظل الحِزم المثبَّتة أثناء التفاعل متوفّرة عند إعادة استخدام `environment_id` نفسه.

| الفئة | الحِزم المثبَّتة مسبقًا |
| --- | --- |
| **أدوات UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | ‫`numpy`، `pandas`، `requests`، `google-genai`، `beautifulsoup4`، `pyyaml`، `ast-grep-cli` |
| **Node.js 22** | ‫`create-next-app`، `create-vite`، `typescript` |

## إعدادات الشبكة

تتضمّن البيئات تلقائيًا إمكانية وصول غير محدودة إلى الشبكة الصادرة. استخدِم الحقل
`network` لحصر عدد الزيارات الصادرة على نطاقات محدّدة. تحدّد كل قاعدة `domain` وكائن `transform` اختياري لإدراج العناوين في الطلبات المطابقة. يمكن أن تكون هذه العناوين فريدة لكل تفاعل، ويمكنك تعديلها للبيئة نفسها.

| الحقل | النوع | الوصف |
| --- | --- | --- |
| `domain` | `string` | النطاق المطلوب مطابقته استخدِم اسم مضيف مطابقًا أو `*` لجميع النطاقات. |
| `transform` | `object` | كائن يحتوي على أزواج مفتاح/قيمة مسطّحة تمثّل العناوين المطلوب إدراجها في الطلبات المطابقة، مثل `{"Authorization": "Bearer ..."}`. |

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

عند ضبط قائمة مسموح بها، لا يُسمح إلا بالطلبات التي يتم إرسالها إلى النطاقات المدرَجة بشكل صريح. يمكنك استخدام أحرف بدل لمطابقة النطاقات الفرعية (مثل `{"domain":
"*.example.com"}`)، ولكن يُرجى العِلم أنّ ذلك لا يطابق النطاق الجذر
`example.com`، الذي يجب إضافته بشكل منفصل. للسماح بجميع الزيارات الأخرى، مثل توجيه النطاقات غير المدرَجة بدون رؤوس رسائل مُدرَجة، أضِف `{"domain": "*"}` كإدخال شامل.

### بيانات الاعتماد

يمكنك إضافة بيانات اعتماد ليستخدمها برنامجك من خلال إضافة عمليات تحويل العناوين. يتم إدخال بيانات الاعتماد في عناوين HTTP المعنية من خلال خادم وكيل للخروج، ولا يتم عرضها مطلقًا داخل وضع الحماية كمتغيرات بيئية أو ملفات.

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

### إيقاف إمكانية الوصول إلى الشبكة

لحظر جميع عمليات الوصول إلى الشبكة الصادرة، اضبط `network` على `disabled`:

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

### إعادة تحميل بيانات الاعتماد

تنتهي صلاحية بيانات الاعتماد، مثل رموز الدخول ومفاتيح واجهة برمجة التطبيقات القصيرة الأمد.
يمكنك إعادة تحميلها من خلال تمرير `environment_id` الحالي مع إعداد `network` جديد في التفاعل التالي. تحلّ قواعد الشبكة الجديدة محل القواعد السابقة بالكامل، مع الحفاظ على حالة نظام الملفات في البيئة (الحِزم والملفات والمستودعات المثبّتة).

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

## مراحل نشاط البيئة

تتّبع البيئات دورة الحياة التالية:

| ولاية | السلوك |
| --- | --- |
| **تاريخ الإنشاء** | يتم توفيرها عندما يحدّد أحد التفاعلات `environment: "remote"` أو كائن إعداد. |
| **نشطة** | يتم تشغيلها أثناء إجراء تفاعل. |
| **غير مستخدَم من قِبل أي برنامج حاليًا** | تم أخذ لقطة تلقائية وتوقّفت بعد 15 دقيقة من عدم النشاط. |
| **بلا إنترنت** | تم الاحتفاظ بها لمدة 7 أيام منذ آخر نشاط. يمكن استئنافها من خلال إدخال رقم تعريفها. |
| **تم الحذف** | تتم إزالتها من النظام تلقائيًا بعد انتهاء مدة الاحتفاظ بالبيانات لمدة 7 أيام أو عند حذفها يدويًا. |

## Environments API

يمكنك استخدام Environments API لإدارة جلسات وضع الحماية آليًا.
يتيح لك تعداد البيئات اكتشاف أرقام تعريف الجلسات النشطة واستعادة الحالة
في حال انتهاء اتصال العميل أثناء تنفيذ مهمة طويلة الأمد. يمكنك أيضًا فحص بيانات الجلسة الوصفية وحذف البيئات بشكل صريح عند انتهاء مهام سير العمل بدلاً من انتظار انتهاء صلاحية TTL تلقائيًا.

### عرض قائمة بالبيئات

تعرض هذه السمة قائمة بالبيئات النشطة التابعة لمشروعك. استخدِم مَعلمات تقسيم الصفحات
للتحكّم في حجم مجموعة الردود.

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

ستبدو الاستجابة مشابهة لما يلي:

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

### الحصول على بيئة

استرداد البيانات الوصفية وتفاصيل الإعدادات لبيئة معيّنة من خلال اسم المورد

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

ستبدو الاستجابة مشابهة لما يلي:

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

### حذف بيئة

يجب إنهاء البيئة وحذفها بشكل صريح لتنظيف موارد وضع الحماية عند انتهاء المهام أو خطوط الأنابيب.

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

## تنزيل ملفات من البيئة

ينشئ الوكيل ملفات داخل وضع الحماية أثناء التنفيذ. يمكنك تنزيل لقطة البيئة الكاملة كملف tar باستخدام Files API:

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

## الأسعار والمراجع

تعمل كل بيئة مع تخصيصات ثابتة للموارد:

| المورد | القيمة |
| --- | --- |
| **وحدة المعالجة المركزية** | 4 نوى |
| **الذاكرة** | 16 غيغابايت |

**لا يتم تحصيل رسوم** مقابل حوسبة البيئة (وحدة المعالجة المركزية والذاكرة والتنفيذ في وضع الحماية) خلال فترة المعاينة. اطّلِع على [الأسعار](https://ai.google.dev/gemini-api/docs/pricing?hl=ar#pricing-for-agents) لمعرفة تكاليف رموز وكلاء الدعم.

## القيود

- **حالة المعاينة:** البيئات والوكلاء المُدارون في مرحلة المعاينة. قد تتغيّر الميزات والمخططات.
- **حجم المصدر المضمّن:** يقتصر حجم المصادر المضمّنة على 1 ميغابايت لكل ملف، و2 ميغابايت إجمالاً في جميع الملفات.
- **حجم المصدر**: يقتصر حجم مستودعات Git على 500 ميغابايت، ومستودعات Cloud Storage على 2 غيغابايت.
- **بدء تشغيل البيئة:** يستغرق توفير بيئة جديدة مدة تصل إلى 5 ثوانٍ تقريبًا. قد تؤدي مستودعات المصادر الكبيرة إلى زيادة هذا الوقت.
- **انتهاء صلاحية البيئة:** يتم الاحتفاظ بالبيئات غير النشطة بلا إنترنت لمدة 7 أيام قبل انتهاء صلاحيتها باستخدام عملية التنظيف التلقائي حسب مدة البقاء (TTL). سيؤدي إدخال معرّف بيئة منتهي الصلاحية أو غير صالح إلى عرض الخطأ `404 Not Found`.
- **توافق الملفات:** يقتصر عمل الوكيل حاليًا على قراءة الملفات النصية وملفات الصور. لا تتوفّر بعد إمكانية استخدام الملفات الثنائية.
- **عدم الربط من الجذر:** لا يمكنك ضبط الجذر (`/`) كهدف عند إضافة مصدر مخصّص، ويجب دائمًا تحديد دليل فرعي.

## الخطوات التالية

- [نظرة عامة على الوكلاء](https://ai.google.dev/gemini-api/docs/agents?hl=ar): تعرَّف على المفاهيم الأساسية للوكلاء المُدارين.
- [البدء السريع](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ar): ابدأ إنشاء محادثات مترابطة وبث المحتوى.
- [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ar): استكشِف الإمكانات والأدوات واختيار النماذج والأسعار الخاصة بالوكيل التلقائي.
- [إنشاء وكلاء مخصّصين](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ar): يمكنك تحديد الوكلاء الخاصين بك باستخدام `AGENTS.md` و`SKILL.md`.

إرسال ملاحظات

إنّ محتوى هذه الصفحة مرخّص بموجب [ترخيص Creative Commons Attribution 4.0‏](https://creativecommons.org/licenses/by/4.0/) ما لم يُنصّ على خلاف ذلك، ونماذج الرموز مرخّصة بموجب [ترخيص Apache 2.0‏](https://www.apache.org/licenses/LICENSE-2.0). للاطّلاع على التفاصيل، يُرجى مراجعة [سياسات موقع Google Developers‏](https://developers.google.com/site-policies?hl=ar). إنّ Java هي علامة تجارية مسجَّلة لشركة Oracle و/أو شركائها التابعين.

تاريخ التعديل الأخير: 2026-07-23 (حسب التوقيت العالمي المتفَّق عليه)

هل تريد مشاركة ملاحظاتك معنا؟

[[["يسهُل فهم المحتوى.","easyToUnderstand","thumb-up"],["ساعَدني المحتوى في حلّ مشكلتي.","solvedMyProblem","thumb-up"],["غير ذلك","otherUp","thumb-up"]],[["لا يحتوي على المعلومات التي أحتاج إليها.","missingTheInformationINeed","thumb-down"],["الخطوات معقدة للغاية / كثيرة جدًا.","tooComplicatedTooManySteps","thumb-down"],["المحتوى قديم.","outOfDate","thumb-down"],["ثمة مشكلة في الترجمة.","translationIssue","thumb-down"],["مشكلة في العيّنات / التعليمات البرمجية","samplesCodeIssue","thumb-down"],["غير ذلك","otherDown","thumb-down"]],["تاريخ التعديل الأخير: 2026-07-23 (حسب التوقيت العالمي المتفَّق عليه)"],[],[]]
