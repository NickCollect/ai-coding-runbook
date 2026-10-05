---
source_url: https://ai.google.dev/gemini-api/docs/agent-credentials?hl=ko
fetched_at: 2026-10-05T06:47:12.313985+00:00
title: "\uad00\ub9ac \uc5d0\uc774\uc804\ud2b8\uc758 \uc0ac\uc6a9\uc790 \uc778\uc99d \uc815\ubcf4 \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)
- [문서](https://ai.google.dev/gemini-api/docs?hl=ko)

의견 보내기

# 관리 에이전트의 사용자 인증 정보

사용자 인증 정보는 서버에서 관리하는 보안 비밀로, 에이전트가 에이전트 환경에 보안 비밀을 입력하지 않고도 서드 파티 서비스에 연결할 수 있습니다. 사용자는 사용자 인증 정보를 한 번 저장하고 ID로 참조하면 이그레스 프록시가 요청 시 이를 확인하고 삽입합니다.

보안 비밀 값은 쓰기 전용입니다. 저장된 후에는 어떤 엔드포인트에서도 반환되지 않으므로 보안이 취약한 에이전트가 사용 중인 토큰을 다시 읽을 수 없습니다.

사용자 인증 정보를 사용하는 기본 위치는 [`environment.network`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko)의 네트워크 허용 목록입니다. 먼저 보안 비밀을 저장합니다.

### Python

```
from google import genai

client = genai.Client()

credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)

print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### 자바스크립트

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});

console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

그런 다음 인증하는 도메인에 연결합니다.

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Triage the open issues in my-org/my-repo.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {"domain": "api.github.com", "credential": "github-production"},
                {"domain": "*"},
            ]
        },
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Triage the open issues in my-org/my-repo.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                { domain: "api.github.com", credential: "github-production" },
                { domain: "*" },
            ],
        },
    },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Triage the open issues in my-org/my-repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "api.github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "*"},
                    },
                }))),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Triage the open issues in my-org/my-repo.",
    "environment": {
        "type": "remote",
        "network": {
            "allowlist": [
                { "domain": "api.github.com", "credential": "github-production" },
                { "domain": "*" }
            ]
        }
    }
}'
```

이제 에이전트는 `api.github.com`에 인증된 요청을 전송하며 토큰은 샌드박스 내에 존재하지 않습니다.

## 사용자 인증 정보 유형

모든 사용자 인증 정보에는 프록시가 어떤 필드를 허용하고 어떻게 적용하는지 결정하는 `type`가 있습니다.

| 유형 | 사용 사례 | 동작 |
| --- | --- | --- |
| `bearer_token` | 개인 액세스 토큰, 봇 토큰, 정적 API 키 | 프록시가 토큰을 요청 헤더로 삽입합니다. 새로고침 로직이 없습니다. |
| `oauth2` | OAuth 앱 및 사용자 위임 흐름 | 프록시는 갱신 토큰을 액세스 토큰으로 교환하고 만료되면 새로고침합니다. |
| `environment_variable` | 프로세스 환경에서 보안 비밀을 읽는 클라이언트 SDK | 에이전트의 환경에 자리표시자가 표시됩니다. 프록시는 아웃바운드 요청에서 실제 보안 비밀을 대체합니다. |

## 네트워크 허용 목록의 사용자 인증 정보 사용

허용 목록 규칙에 `credential`를 추가하면 프록시가 해당 도메인으로 전송되는 모든 아웃바운드 요청을 인증합니다. 이는 에이전트에게 비공개 API, 비공개 저장소 또는 비공개 버킷에 대한 액세스 권한을 부여하는 데 권장되는 방법입니다.

동일한 허용 목록에서 인증된 규칙과 인증되지 않은 규칙을 혼합할 수 있습니다.

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Sync the open Jira issues into the tracking sheet in my repo.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/your-org/backend",
                "target": "/backend-app",
            }
        ],
        "network": {
            "allowlist": [
                {"domain": "github.com", "credential": "github-production"},
                {"domain": "api.atlassian.com", "credential": "jira-oauth"},
                {"domain": "*.googleapis.com"},
            ]
        },
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Sync the open Jira issues into the tracking sheet in my repo.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/your-org/backend",
                target: "/backend-app",
            },
        ],
        network: {
            allowlist: [
                { domain: "github.com", credential: "github-production" },
                { domain: "api.atlassian.com", credential: "jira-oauth" },
                { domain: "*.googleapis.com" },
            ],
        },
    },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Sync the open Jira issues into the tracking sheet in my repo."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Sources: []interactions.Source{
                    {
                        Type:   interactions.SourceTypeRepository.ToPointer(),
                        Source: genai.Ptr("https://github.com/your-org/backend"),
                        Target: genai.Ptr("/backend-app"),
                    },
                },
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "github.com", Credential: genai.Ptr("github-production")},
                        {Domain: "api.atlassian.com", Credential: genai.Ptr("jira-oauth")},
                        {Domain: "*.googleapis.com"},
                    },
                }))),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Sync the open Jira issues into the tracking sheet in my repo.",
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
                { "domain": "github.com", "credential": "github-production" },
                { "domain": "api.atlassian.com", "credential": "jira-oauth" },
                { "domain": "*.googleapis.com" }
            ]
        }
    }
}'
```

프록시는 요청별로 사용자 인증 정보를 확인하므로 `oauth2` 사용자 인증 정보는 액세스 토큰을 투명하게 새로고침합니다. 액세스 토큰이 만료되어도 장기 실행 상호작용이 중단되지 않습니다.

### `credential` 및 `transform` 결합

허용 목록 규칙은 규칙에 직접 헤더를 설정하는 인라인 [`transform`](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#private-sources) 객체도 허용합니다. 두 메커니즘 모두 와이어의 이그레스 프록시에 의해 적용되므로 두 경우 모두 헤더 값이 샌드박스 내에 존재하지 않습니다. 두 필드는 동일한 규칙에 표시될 수 있습니다.

| 규칙 구성 | 동작 |
| --- | --- |
| `credential`만 지원 | 프록시는 사용자 인증 정보를 확인하고 도메인에 대한 모든 요청에 헤더를 삽입합니다. |
| `transform`만 지원 | 정적 헤더 삽입 작성한 헤더는 그대로 전송됩니다. |
| 둘 다 | 사용자 인증 정보가 먼저 적용된 다음 `transform`가 맨 위에 병합됩니다. 두 헤더가 동일한 키를 설정하는 경우 명시적 `transform` 헤더가 우선합니다. |
| 둘 다 아님 | 도메인이 허용되고 헤더가 삽입되지 않습니다. |

사용자 인증 정보는 비밀번호를 한 번 저장하고 프로젝트의 모든 환경, 에이전트, 트리거에서 참조하려는 경우와 액세스 토큰 새로고침 및 순환을 처리하려는 경우에 사용하는 것이 좋습니다. 인라인 `transform`은 값이 단일 호출에 속하는 경우에 적합합니다. 예를 들어 상호작용을 만들기 직전에 직접 생성하는 토큰이 있습니다.

두 가지를 결합하는 것이 일반적입니다. 사용자 인증 정보는 인증 헤더를 전달하고 `transform`는 동일한 요청에서 업스트림 서비스가 예상하는 다른 항목을 추가합니다.

```
{
    "domain": "api.atlassian.com",
    "credential": "jira-oauth",
    "transform": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

인라인 `transform`에서 사용자 인증 정보로 보안 비밀을 이동하려면 `POST /credentials`로 저장하고 `transform`의 인증 헤더를 `"credential": "<id>"`로 바꾸고 나머지 `transform` 객체는 그대로 둡니다.

## MCP 서버에서 사용자 인증 정보 사용

원격 MCP 서버는 동일한 `credential` 필드를 사용합니다. `mcp_server` 도구에서 설정하면 프록시가 해당 서버에 대한 모든 요청에 인증 헤더를 삽입합니다.

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Create a new issue in my-org/my-repo",
    environment="remote",
    tools=[{
        "type": "mcp_server",
        "name": "github",
        "url": "https://api.githubcopilot.com/mcp",
        "credential": "github-production",
    }],
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Create a new issue in my-org/my-repo",
    environment: "remote",
    tools: [{
        type: "mcp_server",
        name: "github",
        url: "https://api.githubcopilot.com/mcp",
        credential: "github-production",
    }],
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Create a new issue in my-org/my-repo"),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Network: genai.Ptr(interactions.NewNetwork(interactions.NewEnvironmentNetworkEgressAllowlist(interactions.Allowlist{
                    Allowlist: []interactions.AllowlistEntry{
                        {Domain: "api.githubcopilot.com", Credential: genai.Ptr("github-production")},
                    },
                }))),
            })),
            Tools: []interactions.Tool{
                interactions.NewTool(interactions.MCPServer{
                    Name: genai.Ptr("github"),
                    URL:  genai.Ptr("https://api.githubcopilot.com/mcp"),
                }),
            },
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Create a new issue in my-org/my-repo",
    "environment": "remote",
    "tools": [
        {
            "type": "mcp_server",
            "name": "github",
            "url": "https://api.githubcopilot.com/mcp",
            "credential": "github-production"
        }
    ]
}'
```

`credential`와 `headers`은 허용 목록과 동일한 우선순위 규칙을 따릅니다.
인증 정보가 먼저 적용되고 `headers`가 맨 위에 병합되므로 둘 다 동일한 키를 설정하면 명시적 헤더가 우선합니다.

```
{
    "type": "mcp_server",
    "name": "jira",
    "url": "https://jira.atlassian.com/mcp",
    "credential": "jira-oauth",
    "headers": {
        "X-Atlassian-Workspace": "my-workspace-id"
    }
}
```

인라인 `headers`에서 보안 비밀을 인증 정보로 이동하려면 `POST /credentials`로 저장하고 `headers`의 인증 항목을 `credential`로 바꿉니다.
다른 헤더는 원래 위치에 유지합니다.

## 사용자 인증 정보를 환경 변수로 사용

일부 클라이언트 라이브러리는 요청 헤더로 허용하는 대신 프로세스 환경에서 보안 비밀을 읽습니다. 소켓 모드 및 긴 폴링 클라이언트는 일반적인 사례입니다.

`environment_variable` 사용자 인증 정보를 `environment.env` 아래의 변수 이름에 바인딩합니다.

### Python

```
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Run the sync script and check notifications.",
    environment={
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": {"credential": "slack-bot-token"},
        },
    },
)
```

### 자바스크립트

```
const interaction = await client.interactions.create({
    agent: "antigravity-preview-09-2026",
    input: "Run the sync script and check notifications.",
    environment: {
        type: "remote",
        env: {
            NODE_ENV: "production",
            SLACK_BOT_TOKEN: { credential: "slack-bot-token" },
        },
    },
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/interactions"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Interactions.Create(ctx, operations.CreateInteractionRequest{
        Body: operations.NewCreateInteractionRequestBody(interactions.CreateAgentInteraction{
            Agent: interactions.AgentOption("antigravity-preview-09-2026"),
            Input: interactions.NewInteractionsInput("Run the sync script and check notifications."),
            Environment: genai.Ptr(interactions.NewCreateAgentInteractionEnvironment(interactions.Environment{
                Env: genai.Ptr(interactions.NewEnv(map[string]interactions.EnvVar{
                    "NODE_ENV":        {Value: genai.Ptr("production")},
                    "SLACK_BOT_TOKEN": {Credential: genai.Ptr("slack-bot-token")},
                })),
            })),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Println(res.Interaction.GetOutputText())
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-09-2026",
    "input": "Run the sync script and check notifications.",
    "environment": {
        "type": "remote",
        "env": {
            "NODE_ENV": "production",
            "SLACK_BOT_TOKEN": { "credential": "slack-bot-token" }
        }
    }
}'
```

`env`는 리터럴 문자열과 사용자 인증 정보 참조를 나란히 허용합니다. 리터럴 문자열이 일반 일반 텍스트 변수로 컨테이너에 삽입됩니다.

사용자 인증 정보 참조는 아닙니다. 변수는 자리표시자 `__GEMINI_CRED_<credential-id>__`를 수신하고 프록시는 사용자 인증 정보의 `trusted_domains`에 있는 도메인으로 전송되는 아웃바운드 요청에 대해서만 실제 비밀번호를 스왑합니다. 다른 도메인에 대한 요청은 거부되므로 보안 비밀이 경계를 벗어나지 않으며 자리표시자가 대신 전송되지 않습니다.

모든 `environment_variable` 사용자 인증 정보에 `trusted_domains`를 설정합니다. 보안 비밀을 사용할 수 있는 범위를 지정하는 컨트롤입니다.

## 사용자 인증 정보 만들기

모든 생성 요청에는 `type`와 해당 유형에 필요한 필드가 필요합니다.

REST를 직접 호출할 때는 모든 필드 이름이 snake\_case를 사용합니다. camelCase 필드를 전송하면 `400`가 반환됩니다.

### Bearer 토큰

Bearer 토큰 사용자 인증 정보에는 `token`만 필요합니다.

### Python

```
credential = client.credentials.create(
    id="github-production",
    type="bearer_token",
    token="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
)
```

### 자바스크립트

```
const credential = await client.credentials.create({
    id: "github-production",
    type: "bearer_token",
    token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:    "github-production",
            Token: "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "github-production",
    "type": "bearer_token",
    "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}'
```

응답은 메타데이터만 반환하고 토큰은 반환하지 않습니다.

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

기본적으로 프록시는 `Authorization: Bearer <token>`를 전송합니다. `header_name` 및 `prefix`를 재정의하여 다른 것을 예상하는 서비스를 타겟팅합니다.

### Python

```
credential = client.credentials.create(
    id="my-api-key",
    type="bearer_token",
    token="key_xxxxxxxxxxxx",
    header_name="x-goog-api-key",
    prefix="",
)
```

### 자바스크립트

```
const credential = await client.credentials.create({
    id: "my-api-key",
    type: "bearer_token",
    token: "key_xxxxxxxxxxxx",
    header_name: "x-goog-api-key",
    prefix: "",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.HTTPBearerConfig{
            ID:         "my-api-key",
            Token:      "key_xxxxxxxxxxxx",
            HeaderName: genai.Ptr("x-goog-api-key"),
            Prefix:     genai.Ptr(""),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "my-api-key",
    "type": "bearer_token",
    "token": "key_xxxxxxxxxxxx",
    "header_name": "x-goog-api-key",
    "prefix": ""
}'
```

이 구성은 헤더 `x-goog-api-key: key_xxxxxxxxxxxx`를 생성합니다.

다음 표는 `header_name`와 `prefix`가 결합되는 방식을 보여줍니다.

| 구성 | 삽입된 헤더 |
| --- | --- |
| `{"token": "ghp_xxx"}` | `Authorization: Bearer ghp_xxx` |
| `{"token": "sk_live_xxx"}` | `Authorization: Bearer sk_live_xxx` |
| `{"token": "key_xxx", "header_name": "x-goog-api-key", "prefix": ""}` | `x-goog-api-key: key_xxx` |
| `{"token": "mytoken", "header_name": "X-API-Token", "prefix": ""}` | `X-API-Token: mytoken` |

### OAuth2

OAuth2 사용자 인증 정보에는 `client_id`, `client_secret`, `refresh_token`, `token_url`이 필요합니다. `scopes` 필드는 선택사항입니다.

### Python

```
credential = client.credentials.create(
    id="jira-oauth",
    type="oauth2",
    client_id="my-client-id",
    client_secret="my-client-secret",
    token_url="https://auth.atlassian.com/oauth/token",
    refresh_token="rt_xxxxxxxxxxxxxxxxxxxx",
    scopes=["read:jira-work", "write:jira-work"],
)
```

### 자바스크립트

```
const credential = await client.credentials.create({
    id: "jira-oauth",
    type: "oauth2",
    client_id: "my-client-id",
    client_secret: "my-client-secret",
    token_url: "https://auth.atlassian.com/oauth/token",
    refresh_token: "rt_xxxxxxxxxxxxxxxxxxxx",
    scopes: ["read:jira-work", "write:jira-work"],
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.OAuth2Config{
            ID:           "jira-oauth",
            ClientID:     "my-client-id",
            ClientSecret: "my-client-secret",
            TokenURL:     "https://auth.atlassian.com/oauth/token",
            RefreshToken: "rt_xxxxxxxxxxxxxxxxxxxx",
            Scopes:       []string{"read:jira-work", "write:jira-work"},
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created OAuth2 credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "jira-oauth",
    "type": "oauth2",
    "client_id": "my-client-id",
    "client_secret": "my-client-secret",
    "token_url": "https://auth.atlassian.com/oauth/token",
    "refresh_token": "rt_xxxxxxxxxxxxxxxxxxxx",
    "scopes": ["read:jira-work", "write:jira-work"]
}'
```

OAuth2 사용자 인증 정보를 만들면 `token_url`에 대해 실시간 토큰 교환이 실행되어 구성이 작동하는지 확인합니다. 자격 증명은 제공자가 `access_token`가 포함된 성공적인 토큰 응답을 반환하는 경우에만 저장됩니다. JSON 응답과 form-urlencoded 응답이 모두 허용됩니다.

즉, 생성 시 유효하고 만료되지 않은 갱신 토큰이 필요합니다. 제공업체가 교환을 거부하면 오류가 반환됩니다.

```
{
  "error": {
    "message": "OAuth token validation failed with HTTP 403: {\"error\":\"unauthorized_client\",\"error_description\":\"refresh_token is invalid\"}",
    "code": "invalid_request"
  }
}
```

저장되면 프록시는 액세스 토큰이 만료될 때마다 갱신합니다. 제공업체가 갱신 중에 갱신 토큰을 순환하고 새 토큰을 반환하면 새 토큰이 저장된 토큰을 자동으로 대체합니다.

### 환경 변수

`environment_variable` 사용자 인증 정보에는 `value` 및 `injection_location`가 필요합니다.

### Python

```
credential = client.credentials.create(
    id="slack-bot-token",
    type="environment_variable",
    value="xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains=["*.slack.com", "slack.com"],
    injection_location="header",
)
```

### 자바스크립트

```
const credential = await client.credentials.create({
    id: "slack-bot-token",
    type: "environment_variable",
    value: "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    trusted_domains: ["*.slack.com", "slack.com"],
    injection_location: "header",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Create(ctx, operations.CreateCredentialRequest{
        Body: credentials.NewCredentialCreateParams(credentials.EnvironmentVariableConfig{
            ID:                "slack-bot-token",
            Value:             "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
            TrustedDomains:    []string{"*.slack.com", "slack.com"},
            InjectionLocation: credentials.NewEnvironmentVariableConfigInjectionLocation(credentials.InjectionLocationEnumHeader),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Created environment variable credential: %s\n", res.Credential.ID)
}
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/credentials" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "slack-bot-token",
    "type": "environment_variable",
    "value": "xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx",
    "trusted_domains": ["*.slack.com", "slack.com"],
    "injection_location": "header"
}'
```

`injection_location` 필드는 아웃바운드 요청에서 보안 비밀을 대체할 위치를 프록시에 알려줍니다. `header`, `query` 또는 `body`를 단일 문자열로 또는 서비스에 두 개 이상이 필요한 경우 배열로 허용합니다.

```
"injection_location": ["header", "query"]
```

대체는 나열된 위치에서만 발생합니다. 자리표시자를 다른 곳으로 전달하는 요청은 전송되지 않고 거부됩니다.

사용자 인증 정보를 변수 이름에 바인딩하려면 [사용자 인증 정보를 환경 변수로 사용](#environment-variables)을 참고하세요.

### 생성된 ID

`id` 필드는 선택사항입니다. 생략하면 서비스에서 UUID를 생성합니다.

```
{
  "id": "9e545973-4330-49bb-9a44-930cea9fbe3c",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-07-15T10:00:00.000000000Z"
}
```

상호작용 전반에서 사용할 안정적이고 읽기 쉬운 참조가 필요한 경우 자체 ID를 제공합니다. ID는 리소스 경로에 표시되므로 하이픈이나 밑줄이 있는 소문자 영숫자를 사용하는 것이 좋습니다.

## 사용자 인증 정보 나열

프로젝트에 속한 사용자 인증 정보를 나열합니다. 페이지로 나누기 매개변수를 사용하여 응답 배치 크기를 제어합니다.

### Python

```
response = client.credentials.list(page_size=10)
for credential in response.credentials:
    print(f"Credential ID: {credential.id}, Type: {credential.type}")
```

### 자바스크립트

```
const response = await client.credentials.list({ page_size: 10 });
for (const credential of response.credentials) {
    console.log(`Credential ID: ${credential.id}, Type: ${credential.type}`);
}
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.List(ctx, operations.ListCredentialsRequest{
        PageSize: genai.Ptr(10),
    })
    if err != nil {
        log.Fatal(err)
    }

    for _, cred := range res.CredentialListResponse.Credentials {
        fmt.Printf("Credential ID: %s, Type: %v\n", cred.ID, cred.GetType())
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials?page_size=10" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

대답에는 메타데이터만 포함됩니다.

```
{
  "credentials": [
    {
      "id": "github-production",
      "type": "bearer_token",
      "status": "active",
      "create_time": "2026-07-15T10:00:00.000000000Z",
      "update_time": "2026-07-15T10:00:00.000000000Z"
    },
    {
      "id": "jira-oauth",
      "type": "oauth2",
      "status": "active",
      "create_time": "2026-07-15T10:05:00.000000000Z",
      "update_time": "2026-07-15T10:05:00.000000000Z"
    }
  ],
  "next_page_token": "Cj...5aE="
}
```

다음 페이지를 가져오기 위해 `next_page_token`를 `page_token`로 다시 전달합니다. 더 이상 결과가 없으면 이 필드는 생략됩니다.

| 매개변수 | 유형 | 설명 |
| --- | --- | --- |
| `page_size` | 정수 | 페이지당 최대 사용자 인증 정보 수입니다. |
| `page_token` | 문자열 | 이전 응답의 `next_page_token`에서 가져온 토큰입니다. |

## 사용자 인증 정보 가져오기

ID로 특정 사용자 인증 정보의 메타데이터를 가져옵니다.

### Python

```
credential = client.credentials.get(id="github-production")
print(f"Credential ID: {credential.id}, Status: {credential.status}")
```

### 자바스크립트

```
const credential = await client.credentials.get("github-production");
console.log(`Credential ID: ${credential.id}, Status: ${credential.status}`);
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Get(ctx, operations.GetCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Credential ID: %s, Status: %v\n", res.Credential.ID, res.Credential.GetStatus())
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

응답은 다음과 유사합니다.

```
{
  "id": "github-production",
  "type": "bearer_token",
  "status": "active",
  "create_time": "2026-07-15T10:00:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

존재하지 않는 사용자 인증 정보를 요청하면 `404`이 반환됩니다.

```
{
  "error": {
    "message": "Result not found.; GetCredential call failed",
    "code": "not_found"
  }
}
```

## 사용자 인증 정보 순환

허용 목록 규칙, 도구 정의 또는 이를 참조하는 환경 변수를 수정하지 않고 보안 비밀을 바꿉니다. 회전은 다음 프록시 확인 시 적용됩니다.

요청에는 `type`와 변경하려는 필드가 포함되어야 합니다. 생략한 필드는 현재 값을 유지합니다.

Bearer 토큰을 순환합니다.

### Python

```
credential = client.credentials.update(
    id="github-production",
    type="bearer_token",
    token="ghp_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### 자바스크립트

```
const credential = await client.credentials.update("github-production", {
    type: "bearer_token",
    token: "ghp_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "github-production",
        Body: credentials.NewCredentialUpdate(credentials.HTTPBearerUpdateConfig{
            Token: genai.Ptr("ghp_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "bearer_token",
    "token": "ghp_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

OAuth2 갱신 토큰을 순환합니다.

### Python

```
credential = client.credentials.update(
    id="jira-oauth",
    type="oauth2",
    refresh_token="rt_new_xxxxxxxxxxxxxxxxxxxx",
)
```

### 자바스크립트

```
const credential = await client.credentials.update("jira-oauth", {
    type: "oauth2",
    refresh_token: "rt_new_xxxxxxxxxxxxxxxxxxxx",
});
```

### Go

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/credentials"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    res, err := client.Credentials.Update(ctx, operations.UpdateCredentialRequest{
        ID: "jira-oauth",
        Body: credentials.NewCredentialUpdate(credentials.OAuth2UpdateConfig{
            RefreshToken: genai.Ptr("rt_new_xxxxxxxxxxxxxxxxxxxx"),
        }),
    })
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("Updated credential %s at %v\n", res.Credential.ID, res.Credential.GetUpdateTime())
}
```

### REST

```
curl -X PATCH "https://generativelanguage.googleapis.com/v1beta/credentials/jira-oauth" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "type": "oauth2",
    "refresh_token": "rt_new_xxxxxxxxxxxxxxxxxxxx"
}'
```

대답에는 새로운 `update_time`가 반영됩니다.

```
{
  "id": "jira-oauth",
  "type": "oauth2",
  "status": "active",
  "create_time": "2026-07-15T10:05:00.000000000Z",
  "update_time": "2026-08-01T14:30:00.000000000Z"
}
```

사용자 인증 정보의 `type`는 생성 시 고정됩니다. 이를 변경하려면 사용자 인증 정보를 삭제하고 새 사용자 인증 정보를 만드세요.

## 사용자 인증 정보 삭제

더 이상 필요하지 않은 경우 사용자 인증 정보와 저장된 비밀번호를 삭제합니다.

### Python

```
client.credentials.delete(id="github-production")
```

### 자바스크립트

```
await client.credentials.delete("github-production");
```

### Go

```
package main

import (
    "context"
    "log"

    "google.golang.org/genai"
    "google.golang.org/genai/interactions/models/operations"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    _, err = client.Credentials.Delete(ctx, operations.DeleteCredentialRequest{
        ID: "github-production",
    })
    if err != nil {
        log.Fatal(err)
    }
}
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/credentials/github-production" \
-H "x-goog-api-key: $GEMINI_API_KEY"
```

삭제에 성공하면 빈 객체가 반환됩니다.

```
{}
```

ID를 여전히 참조하는 허용 목록 규칙, 도구 또는 환경 변수는 해결되지 않으므로 먼저 업데이트하세요.

## 필드 참조

모든 사용자 인증 정보에 공통적인 필드:

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | 문자열 | 아니요 | 고유 식별자입니다. 생략하면 UUID로 생성됩니다. |
| `type` | 문자열 | 예 | `bearer_token`, `oauth2`, `environment_variable` 중 하나입니다. |
| `status` | 문자열 | 읽기 전용 | 인증 정보의 현재 상태입니다. |
| `create_time` | 문자열 | 읽기 전용 | RFC 3339 생성 타임스탬프입니다. |
| `update_time` | 문자열 | 읽기 전용 | 마지막 업데이트의 RFC 3339 타임스탬프입니다. |

`bearer_token` 필드:

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `token` | 문자열 | 예 | 쓰기 전용입니다. 토큰 값입니다. |
| `header_name` | 문자열 | 아니요 | 삽입할 헤더입니다. 기본값은 `Authorization`입니다. |
| `prefix` | 문자열 | 아니요 | 값 접두사입니다. 기본값은 `Bearer`입니다. 없음은 `""`로 설정됩니다. |

`oauth2` 필드:

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `client_id` | 문자열 | 예 | OAuth2 클라이언트 ID입니다. |
| `client_secret` | 문자열 | 예 | 쓰기 전용입니다. OAuth2 클라이언트 보안 비밀번호입니다. |
| `refresh_token` | 문자열 | 예 | 쓰기 전용입니다. 액세스 토큰을 획득하는 데 사용되는 갱신 토큰입니다. |
| `token_url` | 문자열 | 예 | 제공업체 토큰 엔드포인트입니다. |
| `scopes` | 배열 | 아니요 | 요청할 OAuth 범위입니다. |

`environment_variable` 필드:

| 필드 | 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `value` | 문자열 | 예 | 쓰기 전용입니다. 보안 비밀 값입니다. |
| `injection_location` | 문자열 또는 배열 | 예 | 보안 비밀을 대체할 위치입니다. `header`, `query`, `body` 중 하나 이상입니다. |
| `trusted_domains` | 배열 | 아니요 | 대체에 승인된 도메인 패턴입니다. |

## 오류

오류는 `message` 및 `code`이 포함된 JSON 객체를 반환합니다.

```
{
  "error": {
    "message": "Credential 'github-production' already exists.; CreateCredential call failed",
    "code": "aborted"
  }
}
```

| HTTP 상태 | `code` | 원인 |
| --- | --- | --- |
| 400 | `invalid_request` | 필수 입력란이 누락되었거나, 알 수 없는 필드가 있거나, 지원되지 않는 `type`가 있거나, OAuth2 유효성 검사에 실패했습니다. |
| 404 | `not_found` | 해당 ID의 사용자 인증 정보가 없습니다. |
| 409 | `aborted` | 이미 이 ID를 사용하는 사용자 인증 정보가 있습니다. |

알 수 없는 필드는 무시되지 않고 거부되며 오류에 필드 이름이 지정됩니다.

```
{
  "error": {
    "message": "Unknown parameter 'headerName'. Did you mean 'header_name'?",
    "code": "invalid_request"
  }
}
```

## 다음 단계

- [환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko): 에이전트가 코드를 실행하고 파일을 유지하는 방법을 알아봅니다.
- [에이전트 개요](https://ai.google.dev/gemini-api/docs/agents?hl=ko): 관리 에이전트의 핵심 개념을 알아봅니다.
- [맞춤 에이전트 빌드](https://ai.google.dev/gemini-api/docs/custom-agents?hl=ko): `AGENTS.md` 및 `SKILL.md`를 사용하여 자체 에이전트를 정의합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-24(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-24(UTC)"],[],[]]
