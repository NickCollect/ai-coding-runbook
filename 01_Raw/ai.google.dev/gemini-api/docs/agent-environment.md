---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=he
fetched_at: 2026-08-03T04:39:50.054096+00:00
title: "\u05e1\u05d1\u05d9\u05d1\u05d5\u05ea \u05d1\u05e1\u05d5\u05db\u05e0\u05d9\u05dd \u05de\u05e0\u05d5\u05d4\u05dc\u05d9\u05dd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=he) זמין עכשיו לכלל המשתמשים. מומלץ להשתמש ב-API הזה כדי לקבל גישה לכל התכונות והמודלים העדכניים.

![](https://ai.google.dev/_static/images/translated.svg?hl=he)

‫Google משתמשת בטכנולוגיית AI כדי לתרגם תוכן לשפה המועדפת עליך. בתרגומים כאלו עשויות להיות שגיאות.

- [דף הבית](https://ai.google.dev/?hl=he)
- [Gemini API](https://ai.google.dev/gemini-api?hl=he)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=he)

שליחת משוב

# סביבות בסוכנים מנוהלים

סביבות הן ארגזי חול מנוהלים של Linux שנותנים לסוכנים מקום מבודד להרצת קוד ולשמירת קבצים. הן מנותקות מהקשר האינטראקציה, כך שאפשר לעשות שימוש חוזר באותה סביבה בכמה אינטראקציות או להתחיל מחדש בכל שלב.

בדוגמה הבאה מוסבר איך ליצור אינטראקציה עם סביבה מרוחקת חדשה ולאחזר את המזהה שלה:

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

## הפרמטר `environment`

הפרמטר `environment` מקבל שלוש צורות:

| טופס | דוגמה | מתי להשתמש? |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | הקצאת ארגז חול חדש. |
| מזהה הסביבה | `environment="env_abc123"` | שימוש חוזר בארגז חול קיים עם כל הקבצים והחבילות שלו. |
| אובייקט הגדרה | `environment={...}` | הקצאת ארגז חול חדש עם מקורות, כללי רשת או שניהם. |

בדוגמאות הבאות מודגם השימוש בשלוש הדרכים בפרמטר `environment`.

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

## הגדרת סביבה

אחת הדרכים להגדיר סביבה היא להגיד לסוכן מה צריך להתקין.
הוא מטפל ברזולוציית תלות ובפתרון בעיות. אחרי שהסביבה מוכנה, שומרים את `environment_id` ומשתמשים בו שוב.

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

### טעינה ממקור

אם אתם יודעים בדיוק אילו קבצים הסוכן צריך, אפשר לצרף אותם בקריאה אחת במקום לחזור על הפעולה. אובייקט ההגדרה `environment` מקבל מערך `sources` עם שלושה סוגים:

| סוג מקור | ערך של `type` | תיאור | מגבלה |
| --- | --- | --- | --- |
| מאגר Git | `repository` | משכפל מאגר מכתובת URL אל ארגז החול בנתיב `target`. | ‫500MB |
| Cloud Storage | `gcs` | מעתיק קובץ או ספרייה מ-Cloud Storage אל ארגז החול בנתיב `target`. | 2‎ GB |
| תוכן מוטבע | `inline` | כותב תוכן טקסט גולמי לקובץ בארגז החול בכתובת `target`. | ‫1MB לכל קובץ, 2MB בסך הכול |

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

אפשר לשלב בין שתי הגישות: להגדיר מקורות מוכרים באופן הצהרתי, ואז לחזור על הפעולות עם אינטראקציות המשך כדי להתקין חבילות או להריץ סקריפטים להגדרה. כשמוסיפים מקור בהתאמה אישית, אי אפשר להגדיר את השורש (`/`) כיעד, אלא תמיד צריך לציין תיקיית משנה.

### מקורות פרטיים

אפשר גם להוריד ממאגרי GitHub פרטיים או ממאגרי Cloud Storage פרטיים על ידי הוספת פרטי הכניסה להגדרות הרשת:

בשביל **מאגרי Git פרטיים**, משתמשים באימות `Basic` עם [אסימון גישה אישי (PAT) של GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
מבצעים קידוד של האסימון באמצעות `x-oauth-basic` כשם המשתמש:

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

בשביל **מאגרי Cloud Storage פרטיים**, משתמשים באסימון Bearer רגיל מסוג OAuth 2.0:

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

## תוכנה שהותקנה מראש

ארגז החול פועל ב-Ubuntu ומגיעה עם סביבות זמן ריצה וחבילות נפוצות שהותקנו מראש. הסוכן יכול להתקין חבילות נוספות בזמן הריצה באמצעות `pip
install` או `npm install`. חבילות שהותקנו במהלך אינטראקציה נשמרות כשמשתמשים מחדש באותו `environment_id`.

| קטגוריה | חבילות שהותקנו מראש |
| --- | --- |
| **כלים של UNIX** | מיקס של `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| ‫**Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| ‫**Node.js 22** | `create-next-app`,‏ `create-vite`,‏ `typescript` |

## הגדרת רשת

כברירת מחדל, לסביבות יש גישה בלתי מוגבלת לרשת יוצאת. אפשר להשתמש בשדה `network` כדי להגביל את התנועה היוצאת לדומיינים ספציפיים. כל כלל מציין אובייקט `domain` ואובייקט `transform` אופציונלי להוספת כותרות לבקשות תואמות. הכותרות האלה יכולות להיות ייחודיות לכל אינטראקציה, ואפשר לעדכן אותן לאותה סביבה.

| שדה | סוג | תיאור |
| --- | --- | --- |
| `domain` | `string` | הדומיין שצריך להתאים. צריך להשתמש בשם מארח מדויק או ב-`*` לכל הדומיינים. |
| `transform` | `object` | אובייקט שמכיל צמדי מפתח/ערך שטוחים שמייצגים כותרות להוספה לבקשות תואמות, למשל `{"Authorization": "Bearer ..."}`. |

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

כשמוגדרת רשימת היתרים, רק בקשות לדומיינים שמופיעים בה במפורש מורשות. אפשר להשתמש בתווים כלליים לחיפוש כדי להתאים לתת-דומיינים (למשל, `{"domain":
"*.example.com"}`), אבל חשוב לזכור שהם לא מתאימים לדומיין הבסיסי `example.com`, שצריך להוסיף אותו בנפרד. כדי לאפשר את כל התנועה האחרת, כמו ניתוב של דומיינים שלא מופיעים ברשימה ללא הוספת כותרות, מוסיפים את `{"domain": "*"}` כרשומה כללית.

### פרטי כניסה

אפשר להוסיף פרטי כניסה לסוכן באמצעות הוספה של טרנספורמציות של כותרות. פרטי הכניסה מוזרקים בכותרות ה-HTTP המתאימות על ידי שרת proxy ליציאה, והם אף פעם לא נחשפים בתוך ארגז החול כמשתני סביבה או כקבצים.

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

### השבתת הגישה לרשת

כדי לחסום את כל הגישה לרשת היוצאת, מגדירים את `network` לערך `disabled`:

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

### רענון פרטי הכניסה

תוקף פרטי הכניסה, כמו אסימוני גישה ומפתחות API לטווח קצר, פג.
כדי לרענן אותם, מעבירים את `environment_id` הקיים יחד עם הגדרה חדשה של `network` באינטראקציה הבאה. הכללים החדשים של הרשת מחליפים לחלוטין את הכללים הקודמים, ומצב מערכת הקבצים של הסביבה (חבילות מותקנות, קבצים, מאגרי מידע) נשמר.

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

## מחזור החיים של סביבה

מחזור החיים של סביבות הוא כזה:

| מדינה (State) | התנהגות |
| --- | --- |
| **נוצר** | ההקצאה מתבצעת כשבאינטראקציה מצוין `environment: "remote"` או אובייקט הגדרה. |
| **פעיל** | פועל בזמן שהאינטראקציה מתבצעת. |
| **בלי פעילות** | הצילום האוטומטי של התמונות יופעל וייעצר אחרי 15 דקות של חוסר פעילות. |
| **אופליין** | הנתונים נשמרים למשך 7 ימים מאז הפעילות האחרונה. אפשר להמשיך את התהליך באמצעות העברת המזהה שלו. |
| **נמחק** | הם מוסרים מהמערכת באופן אוטומטי אחרי שתוקף השמירה (TTL) של תוך 7 ימים פג, או אחרי מחיקה ידנית. |

## Environments API

אתם יכולים להשתמש ב-Environments API כדי לנהל באופן פרוגרמטי סשנים של ארגז חול.
כשמפרטים סביבות, אפשר לגלות מזהי סשנים פעילים ולשחזר מצב אם חיבור לקוח מסתיים במהלך משימה ארוכה. אפשר גם לבדוק את המטא-נתונים של הסשן ולמחוק במפורש סביבות כשזרימות העבודה מסתיימות, במקום לחכות שתוקף ה-TTL יפוג באופן אוטומטי.

### הצגת רשימת סביבות

רשימת סביבות פעילות ששייכות לפרויקט. משתמשים בפרמטרים של חלוקה לדפים כדי לקבוע את גודל קבוצת התגובות.

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

התגובה אמורה להיראות כך:

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

### קבלת סביבה

הסוכן מאחזר מטא נתונים ופרטי הגדרה של סביבה ספציפית לפי שם המשאב שלה.

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

התגובה אמורה להיראות כך:

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

### מחיקת סביבה

כדי לנקות את משאבי ארגז החול, צריך לסיים ולמחוק סביבה באופן מפורש אחרי שמסיימים את המשימות או את צינורות הנתונים.

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

## הורדת קבצים מהסביבה

הסוכן יוצר קבצים בתוך ארגז החול במהלך ההפעלה. אפשר להוריד את תמונת המצב המלאה של הסביבה כקובץ TAR באמצעות Files API:

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

## מחירים ומשאבים

כל סביבה פועלת עם הקצאות משאבים קבועות:

| משאב | ערך |
| --- | --- |
| **CPU** | ‫4 ליבות |
| **זיכרון** | ‫16GB |

במהלך תקופת התצוגה המקדימה, **לא נחייב** על מחשוב בסביבה (CPU, זיכרון, הרצה בארגז חול). מידע על עלויות של טוקנים של סוכנים זמין במאמר בנושא [תמחור](https://ai.google.dev/gemini-api/docs/pricing?hl=he#pricing-for-agents).

## מגבלות

- **סטטוס התצוגה המקדימה:** סביבות ונציגים מנוהלים נמצאים בתצוגה מקדימה. יכולים להיות שינויים בתכונות ובסכימות.
- **גודל מקור מוטבע:** הגודל המקסימלי של מקורות מוטבעים הוא ‎1 MB לכל קובץ, ו-‎2 MB בסך הכול בכל הקבצים.
- **גודל המקור**: מאגרי Git מוגבלים ל-500MB ומאגרי Cloud Storage מוגבלים ל-2GB.
- **הפעלת הסביבה:** הקצאת סביבה חדשה נמשכת עד 5 שניות. אם מאגרי המקור גדולים, יכול להיות שהזמן הזה יתארך.
- **תפוגה של סביבה:** סביבות אופליין לא פעילות נשמרות למשך 7 ימים לפני שהן מתפוגות באמצעות ניקוי אוטומטי של TTL. העברה של מזהה סביבה שפג תוקפו או שהוא לא תקין מחזירה שגיאת `404 Not Found`.
- **תמיכה בקבצים:** בשלב הזה, הסוכן מוגבל לקריאת קובצי טקסט ותמונות. עדיין אין תמיכה בקבצים בינאריים.
- **אי אפשר לבצע הרכבה מהשורש:** אי אפשר להגדיר את השורש (`/`) כיעד כשמוסיפים מקור מותאם אישית, ותמיד צריך לציין תת-ספרייה.

## המאמרים הבאים

- [סקירה כללית על סוכנים](https://ai.google.dev/gemini-api/docs/agents?hl=he): מידע על המושגים המרכזיים של סוכנים מנוהלים.
- [מדריך למתחילים](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=he): איך מתחילים ליצור שיחות רב-שלביות וסטרימינג.
- ‫[Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=he): מידע על היכולות, הכלים, בחירת המודל והתמחור של הסוכן שמוגדר כברירת מחדל.
- [יצירת סוכנים בהתאמה אישית](https://ai.google.dev/gemini-api/docs/custom-agents?hl=he): הגדרת סוכנים משלכם באמצעות `AGENTS.md` ו-`SKILL.md`.

שליחת משוב

אלא אם צוין אחרת, התוכן של דף זה הוא ברישיון [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) ודוגמאות הקוד הן ברישיון [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). לפרטים, ניתן לעיין ב[מדיניות האתר Google Developers‏](https://developers.google.com/site-policies?hl=he).‏ Java הוא סימן מסחרי רשום של חברת Oracle ו/או של השותפים העצמאיים שלה.

עדכון אחרון: 2026-07-23 (שעון UTC).

רוצה לתת לנו משוב?

[[["התוכן קל להבנה","easyToUnderstand","thumb-up"],["התוכן עזר לי לפתור בעיה","solvedMyProblem","thumb-up"],["סיבה אחרת","otherUp","thumb-up"]],[["חסרים לי מידע או פרטים","missingTheInformationINeed","thumb-down"],["התוכן מורכב מדי או עם יותר מדי שלבים","tooComplicatedTooManySteps","thumb-down"],["התוכן לא עדכני","outOfDate","thumb-down"],["בעיה בתרגום","translationIssue","thumb-down"],["בעיה בדוגמאות/בקוד","samplesCodeIssue","thumb-down"],["סיבה אחרת","otherDown","thumb-down"]],["עדכון אחרון: 2026-07-23 (שעון UTC)."],[],[]]
