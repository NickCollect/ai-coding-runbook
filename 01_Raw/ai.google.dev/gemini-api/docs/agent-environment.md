---
source_url: https://ai.google.dev/gemini-api/docs/agent-environment?hl=ja
fetched_at: 2026-07-20T04:39:20.929505+00:00
title: "\u30de\u30cd\u30fc\u30b8\u30c9 \u30a8\u30fc\u30b8\u30a7\u30f3\u30c8\u306e\u74b0\u5883 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ja) の一般提供を開始しました。この API を使用して、最新の機能とモデルにアクセスすることをおすすめします。

![](https://ai.google.dev/_static/images/translated.svg?hl=ja)

Google uses AI technology to translate content into your preferred language. AI translations can contain errors.

- [ホーム](https://ai.google.dev/?hl=ja)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ja)
- [ドキュメント](https://ai.google.dev/gemini-api/docs?hl=ja)

フィードバックを送信

# マネージド エージェントの環境

環境は、エージェントがコードを実行してファイルを永続化するための隔離された場所を提供する、マネージド Linux サンドボックスです。インタラクション コンテキストから切り離されているため、複数のインタラクションで同じ環境を再利用したり、いつでも新たに開始したりできます。

次の例は、新しいリモート環境でインタラクションを作成してその ID を取得する方法を示しています。

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

## `environment` パラメータ

`environment` パラメータは次の 3 つの形式を受け入れます。

| フォーム | 例 | 使用する場面 |
| --- | --- | --- |
| `"remote"` | `environment="remote"` | 新しいサンドボックスをプロビジョニングします。 |
| 環境 ID | `environment="env_abc123"` | すべてのファイルとパッケージを含む既存のサンドボックスを再利用します。 |
| 構成オブジェクト | `environment={...}` | ソース、ネットワーク ルール、またはその両方を使用して新しいサンドボックスをプロビジョニングします。 |

次の例は、`environment` パラメータの 3 つの使用方法を示しています。

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

## 環境を構成する

環境を設定する方法の 1 つは、インストールする必要があるものをエージェントに伝えることです。依存関係の解決とトラブルシューティングを処理します。環境の準備ができたら、`environment_id` を保存して再利用します。

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

### ソースからマウントする

エージェントに必要なファイルが正確にわかっている場合は、反復処理ではなく、1 回の呼び出しでマウントします。`environment` 構成オブジェクトは、次の 3 つの型を含む `sources` 配列を受け入れます。

| ソースタイプ | `type` 値 | 説明 | 上限 |
| --- | --- | --- | --- |
| Git リポジトリ | `repository` | URL から `target` のサンドボックスにリポジトリのクローンを作成します。 | 500 MB |
| Cloud Storage | `gcs` | Cloud Storage から `target` のサンドボックスにファイルまたはディレクトリをコピーします。 | 2 GB |
| インライン コンテンツ | `inline` | `target` のサンドボックス内のファイルに未加工のテキスト コンテンツを書き込みます。 | 1 ファイルあたり 1 MB、合計 2 MB |

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

両方のアプローチを組み合わせることができます。既知のソースを宣言的にマウントし、フォローアップのインタラクションでパッケージをインストールしたり、設定スクリプトを実行したりします。カスタムソースを追加するときに、ルート（`/`）をターゲットとして設定することはできません。常にサブディレクトリを指定する必要があります。

### プライベート ソース

ネットワーク構成に認証情報を追加することで、非公開の GitHub リポジトリまたは非公開の Cloud Storage バケットからダウンロードすることもできます。

**非公開 Git リポジトリ**の場合は、[GitHub 個人アクセス トークン（PAT）](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)を使用して `Basic` 認証を行います。ユーザー名として `x-oauth-basic` を使用してトークンをエンコードします。

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

**非公開の Cloud Storage バケット**の場合は、標準の OAuth 2.0 署名なしトークンを使用します。

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

## プリインストールされているソフトウェア

サンドボックスは Ubuntu で実行され、ランタイムと一般的なパッケージがプリインストールされています。エージェントは、`pip
install` または `npm install` を使用して、実行時に追加のパッケージをインストールできます。インタラクション中にインストールされたパッケージは、同じ `environment_id` を再利用しても保持されます。

| カテゴリ | プリインストールされているパッケージ |
| --- | --- |
| **UNIX ツール** | `curl`、`wget`、`git`、`rsync`、`unzip`、`ripgrep`、`fd-find`、`gawk`、`bc`、`tree`、`which`、`lsof`、`htop`、`jq`、`iproute2`、`procps`、`gcloud CLI` |
| **Python 3.12** | `numpy`、`pandas`、`requests`、`google-genai`、`beautifulsoup4`、`pyyaml`、`ast-grep-cli` |
| **Node.js 22** | `create-next-app`、`create-vite`、`typescript` |

## ネットワークの構成

デフォルトでは、環境には無制限のアウトバウンド ネットワーク アクセスがあります。`network` フィールドを使用して、送信トラフィックを特定のドメインに制限します。各ルールは、一致するリクエストにヘッダーを挿入する `domain` と、オプションの `transform` オブジェクトを指定します。これらのヘッダーはインタラクションごとに一意にすることができ、同じ環境で更新できます。

| フィールド | タイプ | 説明 |
| --- | --- | --- |
| `domain` | `string` | 照合するドメイン。すべてのドメインに正確なホスト名または `*` を使用します。 |
| `transform` | `object` | 一致するリクエストに挿入するヘッダーを表すフラットな Key-Value ペアを含むオブジェクト（例: `{"Authorization": "Bearer ..."}`）。 |

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

許可リストが設定されている場合、明示的にリストされているドメインへのリクエストのみが許可されます。ワイルドカードを使用してサブドメイン（`{"domain":
"*.example.com"}` など）を照合できますが、ルートドメイン `example.com` は照合されません。ルートドメインは別途追加する必要があります。ヘッダーが挿入されていない未登録ドメインのルーティングなど、他のすべてのトラフィックを許可するには、キャッチオール エントリとして `{"domain": "*"}` を追加します。

### 認証情報

ヘッダー変換を追加することで、エージェントが使用する認証情報を追加できます。認証情報は、下り（外向き）プロキシによってそれぞれの HTTP ヘッダーに挿入されます。サンドボックス内で環境変数やファイルとして公開されることはありません。

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

### ネットワーク アクセスを無効にする

すべての送信ネットワーク アクセスをブロックするには、`network` を `disabled` に設定します。

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

### 認証情報を更新する

アクセス トークンや短期 API キーなどの認証情報が期限切れになります。既存の `environment_id` と新しい `network` 構成を次のインタラクションで渡すことで、更新できます。新しいネットワーク ルールは以前のルールを完全に置き換えますが、環境のファイル システムの状態（インストールされたパッケージ、ファイル、リポジトリ）は保持されます。

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

## 環境のライフサイクル

環境は次のライフサイクルに従います。

| 州 | 動作 |
| --- | --- |
| **作成日** | インタラクションで `environment: "remote"` または構成オブジェクトが指定されたときにプロビジョニングされます。 |
| **有効** | インタラクションが進行中に実行されます。 |
| **アイドル状態** | 自動スナップショットが作成され、15 分間操作がないと停止します。 |
| **オフライン** | 最後にアクティブになってから 7 日間保持されます。ID を渡すことで再開できます。 |
| **削除しました** | システムから削除されました。 |

## 環境からファイルをダウンロードする

エージェントは実行中にサンドボックス内にファイルを作成します。Files API を使用して、環境のスナップショット全体を tar ファイルとしてダウンロードできます。

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

## 料金とリソース

各環境は、固定リソース割り当てで実行されます。

| リソース | 値 |
| --- | --- |
| **CPU** | 4 コア |
| **メモリ** | 16 GB |

プレビュー期間中は、環境コンピューティング（CPU、メモリ、サンドボックス実行）は**課金されません**。エージェント トークンの費用については、[料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja#pricing-for-agents)をご覧ください。

## 制限事項

- **プレビュー ステータス:** 環境とマネージド エージェントはプレビュー版です。機能とスキーマは変更される可能性があります。
- **インライン ソースのサイズ:** インライン ソースは、ファイルあたり 1 MB、すべてのファイルで合計 2 MB に制限されています。
- **ソースサイズ**: Git リポジトリは 500 MB、Cloud Storage リポジトリは 2 GB に制限されています。
- **環境の起動:** 新しい環境のプロビジョニングには最大 5 秒かかります。ソース リポジトリが大きいと、この時間が長くなることがあります。
- **ファイル サポート:** 現在、エージェントはテキスト ファイルと画像ファイルの読み取りに制限されています。バイナリ ファイルのサポートはまだ利用できません。
- **ルートからのマウントなし:** カスタムソースを追加するときにルート（`/`）をターゲットとして設定することはできません。常にサブディレクトリを指定する必要があります。

## 次のステップ

- [エージェントの概要](https://ai.google.dev/gemini-api/docs/agents?hl=ja): マネージド エージェントの基本コンセプトについて学習します。
- [クイックスタート](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=ja): マルチターン会話とストリーミングを使用して構築を開始します。
- [Antigravity エージェント](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ja): デフォルトのエージェントの機能、ツール、料金を確認します。
- [カスタム エージェントの構築](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ja): `AGENTS.md` と `SKILL.md` を使用して独自のエージェントを定義します。

フィードバックを送信

特に記載のない限り、このページのコンテンツは[クリエイティブ・コモンズの表示 4.0 ライセンス](https://creativecommons.org/licenses/by/4.0/)により使用許諾されます。コードサンプルは [Apache 2.0 ライセンス](https://www.apache.org/licenses/LICENSE-2.0)により使用許諾されます。詳しくは、[Google Developers サイトのポリシー](https://developers.google.com/site-policies?hl=ja)をご覧ください。Java は Oracle および関連会社の登録商標です。

最終更新日 2026-07-06 UTC。

ご意見をお聞かせください

[[["わかりやすい","easyToUnderstand","thumb-up"],["問題の解決に役立った","solvedMyProblem","thumb-up"],["その他","otherUp","thumb-up"]],[["必要な情報がない","missingTheInformationINeed","thumb-down"],["複雑すぎる / 手順が多すぎる","tooComplicatedTooManySteps","thumb-down"],["最新ではない","outOfDate","thumb-down"],["翻訳に関する問題","translationIssue","thumb-down"],["サンプル / コードに問題がある","samplesCodeIssue","thumb-down"],["その他","otherDown","thumb-down"]],["最終更新日 2026-07-06 UTC。"],[],[]]
