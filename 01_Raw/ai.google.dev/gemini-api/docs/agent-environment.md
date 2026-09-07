---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=fr
fetched_at: 2026-09-07T05:46:01.575908+00:00
title: "Environnements dans les agents g\u00e9r\u00e9s \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

L'[API Interactions](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=fr) est désormais en disponibilité générale. Nous vous recommandons d'utiliser cette API pour accéder à toutes les dernières fonctionnalités et tous les derniers modèles.

![](https://ai.google.dev/_static/images/translated.svg?hl=fr)

Google utilise la technologie IA pour traduire le contenu dans votre langue préférée. Les traductions générées par IA peuvent contenir des erreurs.

- [Accueil](https://ai.google.dev/?hl=fr)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fr)
- [Docs](https://ai.google.dev/gemini-api/docs?hl=fr)

Envoyer des commentaires

# Environnements dans les agents gérés

Les environnements sont des bacs à sable Linux gérés qui offrent aux agents un espace isolé pour exécuter du code et conserver des fichiers. Ils sont dissociés du contexte d'interaction. Vous pouvez donc réutiliser le même environnement dans plusieurs interactions ou repartir de zéro à tout moment.

L'exemple suivant montre comment créer une interaction avec un nouvel environnement distant et récupérer son ID :

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

## Paramètre `environment`

Le paramètre `environment` accepte trois formes :

| Formulaire | Exemple | Quand les utiliser ? |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | Provisionner un nouveau bac à sable. |
| ID de l'environnement | `environment="env_abc123"` | Réutiliser un bac à sable existant avec tous ses fichiers et packages. |
| Objet de configuration | `environment={...}` | Provisionner un nouveau bac à sable avec des sources, des règles réseau ou les deux. |

Les exemples suivants illustrent les trois façons d'utiliser le paramètre `environment`.

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

## Configurer un environnement

Une façon de configurer un environnement consiste à indiquer à l'agent ce que vous devez installer.
Il gère la résolution des dépendances et le dépannage. Une fois l'environnement prêt, enregistrez l'`environment_id` et réutilisez-le.

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

### Monter à partir d'une source

Si vous savez exactement quels fichiers l'agent doit utiliser, montez-les en un seul appel au lieu d'itérer. L'objet de configuration `environment` accepte un tableau `sources` avec trois types :

| Type de source | Valeur `type` | Description | Limite |
| --- | --- | --- | --- |
| Dépôt Git | `repository` | Clone un dépôt à partir d'une URL dans le bac à sable au niveau de `target`. | 500 Mo |
| Cloud Storage | `gcs` | Copie un fichier ou un répertoire de Cloud Storage dans le bac à sable au niveau de `target`. | 2 Go |
| Contenu intégré | `inline` | Écrit du contenu texte brut dans un fichier du bac à sable au niveau de `target`. | 1 Mo par fichier, 2 Mo au total |

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

Vous pouvez combiner les deux approches : monter des sources connues de manière déclarative, puis itérer avec des interactions de suivi pour installer des packages ou exécuter des scripts de configuration. Vous ne pouvez pas définir la racine (`/`) comme cible lorsque vous ajoutez une source personnalisée. Vous devez toujours spécifier un sous-répertoire.

### Accroches

Vous pouvez également monter un fichier de configuration `.agents/hooks.json` et des scripts d'interception personnalisés dans le bac à sable pour appliquer des garde-fous de sécurité ou exécuter des validations automatisées chaque fois que des outils sont exécutés. Pour obtenir des définitions de schéma et des exemples de code, consultez [Accroches](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fr).

### Sources privées

Vous pouvez également télécharger des données à partir de dépôts GitHub privés ou de buckets Cloud Storage privés en ajoutant les identifiants dans la configuration réseau :

Pour les **dépôts Git privés**, utilisez l'`Basic` authentification avec votre
[jeton d'accès personnel GitHub
(PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
Encodez le jeton à l'aide de `x-oauth-basic` comme nom d'utilisateur :

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

Pour les **buckets Cloud Storage privés**, utilisez un jeton de support OAuth 2.0 standard :

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

## Logiciel pré-installé

Le bac à sable s'exécute sur Ubuntu et est fourni avec des environnements d'exécution et des packages courants pré-installés. L'agent peut installer des packages supplémentaires au moment de l'exécution à l'aide de `pip
install` ou `npm install`. Les packages installés lors d'une interaction sont conservés lorsque vous réutilisez le même `environment_id`.

| Catégorie | Packages pré-installés |
| --- | --- |
| **Outils UNIX** | `curl`, `wget`, `git`, `rsync`, `unzip`, `ripgrep`, `fd-find`, `gawk`, `bc`, `tree`, `which`, `lsof`, `htop`, `jq`, `iproute2`, `procps`, `gcloud CLI` |
| **Python 3.12** | `numpy`, `pandas`, `requests`, `google-genai`, `beautifulsoup4`, `pyyaml`, `ast-grep-cli` |
| **Node.js 22** | `create-next-app`, `create-vite`, `typescript` |

## Configuration du réseau

Par défaut, les environnements disposent d'un accès réseau sortant illimité. Utilisez le champ `network` pour limiter le trafic sortant à des domaines spécifiques. Chaque règle spécifie un `domain` et un objet `transform` facultatif pour injecter des en-têtes dans les requêtes correspondantes. Ces en-têtes peuvent être uniques pour chaque interaction, et vous pouvez les mettre à jour pour le même environnement.

| Champ | Type | Description |
| --- | --- | --- |
| `domain` | `string` | Domaine à mettre en correspondance. Utilisez un nom d'hôte exact ou `*` pour tous les domaines. |
| `transform` | `object` | Objet contenant des paires clé/valeur plates représentant les en-têtes à injecter dans les requêtes correspondantes, par exemple `{"Authorization": "Bearer ..."}`. |

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

Lorsqu'une liste d'autorisation est définie, seules les requêtes adressées aux domaines explicitement listés sont autorisées. Vous pouvez utiliser des caractères génériques pour mettre en correspondance des sous-domaines (par exemple, `{"domain":
"*.example.com"}`), mais notez que cela ne correspond pas au domaine racine
`example.com`, qui doit être ajouté séparément. Pour autoriser tout autre trafic, tel
que le routage de domaines non listés sans en-têtes injectés, ajoutez `{"domain": "*"}` comme entrée
générique.

### Identifiants

Vous pouvez ajouter des identifiants à utiliser par votre agent en ajoutant des transformations d'en-tête. Les identifiants sont injectés dans les en-têtes HTTP respectifs par un proxy de sortie. Ils ne sont jamais exposés dans le bac à sable en tant que variables d'environnement ou fichiers.

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

### Désactiver l'accès au réseau

Pour bloquer tout accès réseau sortant, définissez `network` sur `disabled` :

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

### Actualiser les identifiants

Les identifiants tels que les jetons d'accès et les clés API à courte durée de vie expirent.
Vous pouvez les actualiser en transmettant l'`environment_id` existant avec une nouvelle configuration `network` lors de la prochaine interaction. Les nouvelles règles réseau remplacent complètement les précédentes, tandis que l'état du système de fichiers de l'environnement (packages installés, fichiers, dépôts) est conservé.

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

## Cycle de vie de l'environnement

Les environnements suivent ce cycle de vie :

| État | Comportement |
| --- | --- |
| **Créé** | Provisionné lorsqu'une interaction spécifie `environment: "remote"` ou un objet de configuration. |
| **Actif** | En cours d'exécution pendant une interaction. |
| **Inactif** | Instantané automatique et arrêté après 15 minutes d'inactivité. |
| **Hors connexion** | Conservé pendant sept jours depuis la dernière activité. Peut être repris en transmettant son ID. |
| **Supprimé** | Supprimé automatiquement du système après l'expiration de la durée de conservation TTL de sept jours ou lors d'une suppression manuelle. |

## API Environments

Vous pouvez utiliser l'API Environments pour gérer les sessions de bac à sable de manière programmatique.
L'énumération des environnements vous permet de découvrir les ID de session actifs et de récupérer l'état si une connexion client se termine lors d'une tâche de longue durée. Vous pouvez également inspecter les métadonnées de session et supprimer explicitement les environnements lorsque les workflows se terminent au lieu d'attendre l'expiration automatique de la durée de conservation TTL.

### Répertorier les environnements

Répertoriez les environnements actifs appartenant à votre projet. Utilisez les paramètres de pagination pour contrôler la taille de lot des réponses.

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

La réponse ressemble à ce qui suit :

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

### Obtenir un environnement

Récupérez les métadonnées et les informations de configuration d'un environnement spécifique par son nom de ressource.

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

La réponse ressemble à ce qui suit :

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

### Supprimer un environnement

Arrêtez et supprimez explicitement un environnement pour libérer de l'espace sur les ressources du bac à sable lorsque vos tâches ou pipelines sont terminés.

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

## Télécharger des fichiers depuis l'environnement

L'agent crée des fichiers dans le bac à sable lors de l'exécution. Vous pouvez télécharger l'instantané complet de l'environnement sous forme de fichier tar à l'aide de l'API Files :

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

## Tarifs et ressources

Chaque environnement s'exécute avec des allocations de ressources fixes :

| Ressource | Valeur |
| --- | --- |
| **Processeur** | 4 cœurs |
| **Mémoire** | 16 Go |

Le calcul de l'environnement (processeur, mémoire, exécution du bac à sable) **n'est pas facturé** pendant la période de preview. Consultez
[Tarifs](https://ai.google.dev/gemini-api/docs/pricing?hl=fr#pricing-for-agents) pour
connaître les coûts des jetons d'agent.

## Limites

- **État de la preview** : les environnements et les agents gérés sont en preview. Les fonctionnalités et les schémas peuvent changer.
- **Taille de la source intégrée** : les sources intégrées sont limitées à 1 Mo par fichier et à 2 Mo au total pour tous les fichiers.
- **Taille de la source** : les dépôts Git sont limités à 500 Mo et les dépôts Cloud Storage à 2 Go.
- **Démarrage de l'environnement** : le provisionnement d'un nouvel environnement prend jusqu'à cinq secondes. Les grands dépôts sources peuvent augmenter ce délai.
- **Expiration de l'environnement** : les environnements hors connexion inactifs sont conservés pendant sept jours avant d'expirer à l'aide du nettoyage automatique de la durée de conservation TTL. La transmission d'un ID d'environnement expiré ou non valide renvoie une erreur `404 Not Found`.
- **Compatibilité avec les fichiers** : l'agent est actuellement limité à la lecture de fichiers texte et image. La compatibilité avec les fichiers binaires n'est pas encore disponible.
- **Aucun montage à partir de la racine** : vous ne pouvez pas définir la racine (`/`) comme cible lorsque vous ajoutez une source personnalisée. Vous devez toujours spécifier un sous-répertoire.

## Étape suivante

- [Présentation des agents](https://ai.google.dev/gemini-api/docs/agents?hl=fr) : découvrez les concepts de base des agents gérés.
- [Guide de démarrage rapide](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=fr) : commencez à créer des conversations multitours et des flux.
- [Agent Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=fr) : découvrez les fonctionnalités, les outils, la sélection de modèles et les tarifs de l'agent par défaut.
- [Créer des agents personnalisés](https://ai.google.dev/gemini-api/docs/custom-agents?hl=fr) : définissez vos propres agents à l'aide de `AGENTS.md` et `SKILL.md`.
- [Accroches](https://ai.google.dev/gemini-api/docs/agent-hooks?hl=fr) : appliquez des garde-fous de sécurité et exécutez des validations d'effets secondaires dans le bac à sable.

Envoyer des commentaires

Sauf indication contraire, le contenu de cette page est régi par une licence [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/), et les échantillons de code sont régis par une licence [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Pour en savoir plus, consultez les [Règles du site Google Developers](https://developers.google.com/site-policies?hl=fr). Java est une marque déposée d'Oracle et/ou de ses sociétés affiliées.

Dernière mise à jour le 2026/08/19 (UTC).

Voulez-vous nous donner plus d'informations ?

[[["Facile à comprendre","easyToUnderstand","thumb-up"],["J'ai pu résoudre mon problème","solvedMyProblem","thumb-up"],["Autre","otherUp","thumb-up"]],[["Il n'y a pas l'information dont j'ai besoin","missingTheInformationINeed","thumb-down"],["Trop compliqué/Trop d'étapes","tooComplicatedTooManySteps","thumb-down"],["Obsolète","outOfDate","thumb-down"],["Problème de traduction","translationIssue","thumb-down"],["Mauvais exemple/Erreur de code","samplesCodeIssue","thumb-down"],["Autre","otherDown","thumb-down"]],["Dernière mise à jour le 2026/08/19 (UTC)."],[],[]]
