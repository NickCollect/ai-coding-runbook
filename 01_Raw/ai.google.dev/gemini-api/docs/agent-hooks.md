---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=ko
fetched_at: 2026-09-14T05:51:44.813478+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

이제 Gemini 3.8 Flash를 사용할 수 있습니다. [사용해 보기](https://aistudio.google.com/prompts/new_chat?model=gemini-3.8-flash&hl=ko).

![](https://ai.google.dev/_static/images/translated.svg?hl=ko)

Google은 AI 기술을 사용하여 콘텐츠를 사용자의 기본 언어로 번역합니다. AI 번역에는 오류가 있을 수 있습니다.

- [홈](https://ai.google.dev/?hl=ko)
- [Gemini API](https://ai.google.dev/gemini-api?hl=ko)

의견 보내기

# Hooks

후크를 사용하면 에이전트가 코드를 실행하거나 원격 샌드박스 내에서 파일을 수정하기 직전 또는 직후에 맞춤 스크립트 또는 외부 HTTP 요청을 실행할 수 있습니다. 후크를 사용하여 다음과 같은 자동 가드레일 및 백그라운드 워크플로로 에이전트 루프를 확장합니다.

- 위험도가 높은 셸 명령어 또는 제한된 파일 읽기가 실행되기 전에 **안전 및 액세스 가드레일 적용**
- 에이전트가 파일을 만들거나 수정한 직후에 **데이터 파이프라인 변환 자동화**
- 도구 실행 후 **엔터프라이즈 감사 원격 분석 스트리밍** 을 외부 모니터링 시스템으로

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "security-gate": {
        "pre_tool_execution": [
            {
                "matcher": "code_execution",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/gate.py",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

gate_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
"""

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Run `rm -rf /tmp/forbidden` using code_execution.",
    tools=[{"type": "code_execution"}],
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/gate.py",
                "content": gate_script,
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

const hooksConfig = {
    "security-gate": {
        pre_tool_execution: [
            {
                matcher: "code_execution",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/gate.py",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const gateScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
cmd = str(data.get("tool_call", {}).get("args", {}))
if "rm -rf" in cmd:
    print(json.dumps({"decision": "deny", "reason": "Destructive command blocked by security gate."}))
else:
    print(json.dumps({"decision": "allow"}))
`;

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Run `rm -rf /tmp/forbidden` using code_execution.",
    tools: [{ type: "code_execution" }],
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                target: ".agents/hooks-scripts/gate.py",
                content: gateScript,
            },
        ],
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
      "input": [{"type": "text", "text": "Run `rm -rf /tmp/forbidden` using code_execution."}],
      "tools": [{"type": "code_execution"}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"security-gate\": {\"pre_tool_execution\": [{\"matcher\": \"code_execution\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/gate.py\", \"timeout\": 10}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/gate.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\ncmd = str(data.get(\"tool_call\", {}).get(\"args\", {}))\nif \"rm -rf\" in cmd:\n    print(json.dumps({\"decision\": \"deny\", \"reason\": \"Destructive command blocked by security gate.\"}))\nelse:\n    print(json.dumps({\"decision\": \"allow\"}))\n"
              }
          ]
      }
  }'
```

## 지원되는 수명 주기 이벤트

후크는 샌드박스 내에서 2개의 이벤트를 지원합니다.

| 이벤트 | 실행 시점 | 기능 |
| --- | --- | --- |
| `pre_tool_execution` | 도구가 실행되기 직전 | 실행되기 전에 도구를 승인 (`allow`)하거나 차단 (`deny`)할 수 있습니다. 차단되면 모델은 거부 사유를 확인하고 이에 맞게 조정합니다. |
| `post_tool_execution` | 도구가 완료된 직후 | 코드 형식 지정, 단위 테스트 실행, 원격 분석 로깅과 같은 후속 작업을 실행합니다. 완료된 작업을 차단하거나 실행취소할 수 없습니다. |

### `pre_tool_execution`

도구가 실행되기 직전에 실행됩니다. 스크립트는 `stdin`에서 도구 호출 세부정보를 읽고 결정 JSON (`allow` 또는 `deny`)을 `stdout`으로 출력합니다.

**입력 페이로드 (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "rm -rf /tmp/forbidden",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

**출력 응답 (`stdout`):**

도구 호출을 승인하려면 다음을 실행하세요.

```
{
  "decision": "allow"
}
```

도구 호출을 차단하고 모델에 의견을 반환하려면 다음을 실행하세요.

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

후크가 명령어를 거부하면 도구 호출이 즉시 건너뛰어집니다. 에이전트는 현재 턴 내에서 거부 사유가 포함된 오류 결과를 확인합니다. 그러면 모델은 대체 명령어를 선택하거나 사용자에게 차단을 설명하여 자체적으로 수정할 수 있습니다.

스크립트가 인식할 수 없는 JSON, 일반 텍스트 또는 `{"decision": "deny"}` 이외의 항목을 출력하면 런타임은 응답을 승인 (`allow`)으로 처리합니다.

### `post_tool_execution`

도구가 완료된 직후에 실행됩니다. 스크립트는 `stdin`에서 실행 세부정보와 오류 상태를 읽습니다.

**입력 페이로드 (`stdin`):**

```
{
  "tool_call": {
    "name": "code_execution",
    "args": {
      "code": "python3 /workspace/app.py",
      "language": "bash"
    }
  },
  "environment_id": "env_xyz789"
}
```

셸 명령어가 표준 오류 (`stderr`)에 오류를 출력하거나 파일 시스템 작업이 실패하면 오류 텍스트가 포함된 `"error"` 필드가 페이로드에 포함됩니다. 오류 없이 명령어가 성공하면 `"error"` 필드가 완전히 생략됩니다.

**출력 응답 (`stdout`):**

```
{}
```

도구 후크는 코드 형식 지정 또는 로깅과 같은 백그라운드 작업에만 엄격하게 실행되므로 런타임은 `stdout`에서 반환된 결정 값을 무시합니다.

## 구성 검색

런타임은 샌드박스 환경 내의 `.agents/hooks.json` 또는 `/.agents/hooks.json`에서 후크 정의를 자동으로 검색합니다. 지원되는 [환경 소스](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#mount_from_a_source)를 사용하여 맞춤 스크립트와 함께 `hooks.json`을 제공할 수 있습니다.

- **저장소 마운트**: `AGENTS.md`와 함께 `.agents/hooks.json`이 포함된 Git 저장소입니다.
- **Cloud Storage (`gcs`)**: 환경에 복사된 `hooks.json`이 포함된 GCS 버킷입니다.
- **인라인 소스**: `environment.sources`에 전달되는 원시 JSON 문자열 및 스크립트 콘텐츠입니다. `client.interactions.create` 호출 시

### `hooks.json` 스키마

`hooks.json` 파일은 이벤트 정의 (`pre_tool_execution` 또는 `post_tool_execution`)를 맞춤 이름으로 그룹화합니다. 각 그룹을 독립적으로 사용 설정하거나 중지할 수 있습니다.

```
{
  "security-gate": {
    "enabled": true,
    "pre_tool_execution": [
      {
        "matcher": "code_execution",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/gate.py",
            "timeout": 10
          }
        ]
      }
    ]
  },
  "auto-format": {
    "post_tool_execution": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 /.agents/hooks-scripts/auto_lint.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

### 일치자 구문 및 규칙

`hooks.json`의 각 규칙 그룹은 `matcher` 및 `hooks` 속성을 사용하여 핸들러가 실행되는 시점과 방법을 정의합니다.

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `enabled` | `boolean` | 선택사항입니다. 그룹을 중지하려면 `false`로 설정합니다 (기본값은 `true`). |
| `matcher` | `string` | 컨테이너 내에서 대상 도구 이름과 일치하는 정규 표현식 패턴입니다. |
| `hooks` | `array` | 핸들러 정의 (`command` 또는 `http`)의 정렬된 목록입니다. 핸들러는 선언 순서대로 순차적으로 실행됩니다. |

#### 정규 표현식 평가 작동 방식

에이전트가 샌드박스 내에서 도구를 호출하면 런타임은 표준 RE2 정규 표현식을 사용하여 도구의 컨테이너 이름을 `matcher` 패턴과 비교하여 평가합니다. 정규 표현식이 도구 이름과 일치하면 `hooks` 배열의 모든 핸들러가 순서대로 실행됩니다. 여러 규칙 그룹이 동일한 도구와 일치하면 해당하는 모든 핸들러 배열이 실행됩니다.

코드 실행 (`code_execution`) 또는 파일 시스템 작업 (`read_file`, `write_file`, `list_files`, `delete_file`)과 같은 모든 기본 제공 컨테이너 도구 이름을 타겟팅할 수 있습니다.

#### 일반적인 일치자 표현식

- `"code_execution"`: 셸 명령어 및 스크립트 실행과 정확히 일치하는 문자열입니다.
- `"write_file"`: 파일 시스템 파일 생성 및 디스크 쓰기와 정확히 일치합니다.
- `"read_file|write_file"`: 파이프 분리는 단일 규칙에서 여러 특정 도구 이름과 일치합니다.
- `".*_file"`: `_file` (예: `read_file`, `write_file`, `delete_file`)로 끝나는 모든 도구와 일치하는 정규 표현식 와일드카드입니다. 표준 RE2 정규 표현식에는 `.*`이 필요합니다. `*_file`과 같은 간단한 셸 글로브는 잘못된 정규 표현식 구문이며 일치하지 않습니다.
- `".*"` 또는 `"*"` 또는 `""`: 컨테이너 내의 모든 단일 도구 호출을 가로채는 캐치올 패턴입니다.

## 핸들러 유형

### 명령어 후크

명령어 후크는 샌드박스 내에서 셸 명령어 또는 스크립트를 실행합니다. 스크립트는 `stdin`에서 이벤트 JSON을 수신하고 `stdout`에서 결정 JSON을 출력합니다.

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `type` | `string` | `"command"`여야 합니다. |
| `command` | `string` | 샌드박스 내에서 실행할 명령어 줄입니다 (예: `python3 /.agents/hooks-scripts/gate.py`). |
| `timeout` | `integer` | 제한 시간(초)입니다. 기본값: `30` |

### HTTP 후크

HTTP 후크는 샌드박스 네트워크 내에서 직접 외부 HTTPS URL로 이벤트 JSON을 POST 요청으로 전송합니다. 대상 서버는 정확히 동일한 JSON 형식 (`{"decision": "allow"}` 또는 `{"decision": "deny", "reason": "..."}`)을 사용하여 HTTP 응답 본문에 결정을 반환합니다.

| 필드 | 유형 | 설명 |
| --- | --- | --- |
| `type` | `string` | `"http"`여야 합니다. |
| `url` | `string` | 이벤트 페이로드를 게시할 외부 HTTPS 엔드포인트입니다. |
| `headers` | `object` | 민감하지 않은 맞춤 헤더의 선택적 키-값 쌍입니다 (예: `{"X-Event-Source": "agent-sandbox"}`). 인증 사용자 인증 정보의 경우 네트워크 프록시를 대신 사용하세요. |
| `timeout` | `integer` | 제한 시간(초)입니다. 기본값: `30` |

#### 이그레스 프록시 및 토큰 변환

HTTP 후크는 샌드박스 네트워크 네임스페이스 내에서 직접 실행되므로 나가는 요청은 투명한 이그레스 프록시를 통과합니다. 이 아키텍처는 다음과 같은 두 가지 중요한 보안 이점을 제공합니다.

- **네트워크 허용 목록:** 대상 엔드포인트는 환경의 `network.allowlist`에서 명시적으로 허용되어야 합니다. 루프백 트래픽 (`127.0.0.1` 또는 `localhost`)은 프록시에 의해 차단됩니다. 항상 허용 목록에 있는 외부 엔드포인트를 타겟팅하세요.
- **토큰 변환:** `.agents/hooks.json` 내에 API 키 또는 비밀 전달자 토큰을 저장하거나 컨테이너에 마운트할 필요가 없습니다. 대신 [네트워크 구성](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#network-configuration) (`network.allowlist.transform`)에서 토큰 변환 규칙을 구성합니다. 이그레스 프록시는 나가는 HTTP 후크 트래픽을 자동으로 가로채고 샌드박스를 나가기 전에 실제 인증 헤더를 와이어에 삽입합니다.

## 런타임에서 결정 및 실패를 처리하는 방법

- **동기식 대기:** 에이전트는 계속하기 전에 후크가 완료될 때까지 일시중지하고 기다립니다.
- **도구 실행 차단:** 도구 후크가 `{"decision": "deny", "reason": "<your reason>"}`를 반환하면 런타임은 도구 호출을 즉시 취소합니다. 모델은 대화 기록에서 거부 사유를 확인하고 안전한 대안을 선택하거나 사용자에게 차단을 설명하여 이에 맞게 조정합니다.
- **스크립트 비정상 종료, HTTP 오류, 제한 시간 처리:** 명령어 스크립트가 비정상 종료되거나 (0이 아닌 종료 상태) HTTP 후크가 2xx가 아닌 상태 코드 (예: 4xx 또는 5xx 서버 오류)를 반환하거나 작업이 제한 시간 초과되거나 인식할 수 없는 JSON을 반환하면 런타임은 이를 승인 (`allow`)으로 처리합니다. 도구 실행은 정상적으로 계속되므로 손상된 스크립트 또는 연결할 수 없는 원격 분석 서버로 인해 애플리케이션이 교착 상태에 빠지지 않습니다.

## 일반적인 사용 사례

### 데이터 개인 정보 보호 및 규정 준수를 위한 다중 턴 복구

후크가 개인 식별 정보 (PII) 또는 기밀 재무 기록이 포함된 디렉터리와 같은 제한된 리소스에 대한 액세스를 차단하는 경우 다음 호출에서 `previous_interaction_id`를 전달하여 동일한 환경에서 턴을 계속할 수 있습니다. 에이전트는 거부 설명을 읽고 승인된 공개 테이블을 대신 쿼리하여 자동으로 복구합니다.

### Python

```
import json
from google import genai

client = genai.Client()

hooks_config = {
    "privacy-gate": {
        "pre_tool_execution": [
            {
                "matcher": "read_file",
                "hooks": [
                    {
                        "type": "command",
                        "command": "python3 /.agents/hooks-scripts/check_privacy.py",
                        "timeout": 5,
                    }
                ],
            }
        ]
    }
}

check_privacy_script = """#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
"""

# Step 1: Agent attempts to read confidential PII records and is intercepted
int_1 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            },
            {
                "type": "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                "content": check_privacy_script,
            },
            {
                "type": "inline",
                "target": "workspace/private/employees.json",
                "content": '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                "type": "inline",
                "target": "workspace/public/summary.json",
                "content": '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
)
print(int_1.output_text)

# Step 2: Continue in the same environment using previous_interaction_id; agent recovers with public tables
int_2 = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment=int_1.environment_id,
    previous_interaction_id=int_1.id,
)
print(int_2.output_text)
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const hooksConfig = {
    "privacy-gate": {
        pre_tool_execution: [
            {
                matcher: "read_file",
                hooks: [
                    {
                        type: "command",
                        command: "python3 /.agents/hooks-scripts/check_privacy.py",
                        timeout: 5,
                    },
                ],
            },
        ],
    },
};

const checkPrivacyScript = `#!/usr/bin/env python3
import sys, json
data = json.load(sys.stdin)
path = str(data.get("tool_call", {}).get("args", {}).get("path", ""))

if "/private/" in path:
    resp = {
        "decision": "deny",
        "reason": "Access to confidential \`/private/\` records is blocked by PII compliance policy. Query approved \`/public/\` summary tables instead."
    }
else:
    resp = {"decision": "allow"}

print(json.dumps(resp))
`;

const int1 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to read `/workspace/private/employees.json` and summarize the employee details.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                "target": ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
            {
                type: "inline",
                "target": ".agents/hooks-scripts/check_privacy.py",
                content: checkPrivacyScript,
            },
            {
                type: "inline",
                "target": "workspace/private/employees.json",
                content: '{"employees": [{"id": 1, "salary": 150000, "ssn": "000-00-0000"}]}',
            },
            {
                type: "inline",
                "target": "workspace/public/summary.json",
                content: '{"department": "Engineering", "team_size": 42, "status": "active"}',
            },
        ],
    },
});
console.log(int1.output_text);

const int2 = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Understood. Please read the approved `/workspace/public/summary.json` file instead and provide the summary.",
    environment: int1.environment_id,
    previous_interaction_id: int1.id,
});
console.log(int2.output_text);
```

### REST

```
# Step 1: Attempt to access restricted PII directory (blocked by hook)
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": [{"type": "text", "text": "Use your filesystem tool to read /workspace/private/employees.json and summarize the employee details."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"privacy-gate\": {\"pre_tool_execution\": [{\"matcher\": \"read_file\", \"hooks\": [{\"type\": \"command\", \"command\": \"python3 /.agents/hooks-scripts/check_privacy.py\", \"timeout\": 5}]}]}}"
              },
              {
                  "type": "inline",
                  "target": ".agents/hooks-scripts/check_privacy.py",
                  "content": "#!/usr/bin/env python3\nimport sys, json\ndata = json.load(sys.stdin)\npath = str(data.get(\"tool_call\", {}).get(\"args\", {}).get(\"path\", \"\"))\nif \"/private/\" in path:\n    resp = {\"decision\": \"deny\", \"reason\": \"Access to confidential `/private/` records is blocked by PII compliance policy. Query approved `/public/` summary tables instead.\"}\nelse:\n    resp = {\"decision\": \"allow\"}\nprint(json.dumps(resp))\n"
              },
              {
                  "type": "inline",
                  "target": "workspace/private/employees.json",
                  "content": "{\"employees\": [{\"id\": 1, \"salary\": 150000, \"ssn\": \"000-00-0000\"}]}"
              },
              {
                  "type": "inline",
                  "target": "workspace/public/summary.json",
                  "content": "{\"department\": \"Engineering\", \"team_size\": 42, \"status\": \"active\"}"
              }
          ]
      }
  }'

# Step 2: Continue in the same environment using $ENV_ID and $INTERACTION_ID from the previous response
# curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
#   -H "Content-Type: application/json" \
#   -H "x-goog-api-key: $GEMINI_API_KEY" \
#   -d '{
#       "agent": "antigravity-preview-05-2026",
#       "input": [{"type": "text", "text": "Understood. Please read the approved /workspace/public/summary.json file instead and provide the summary."}],
#       "environment": "'"$ENV_ID"'",
#       "previous_interaction_id": "'"$INTERACTION_ID"'"
#   }'
```

### 외부 감사 로깅 및 원격 분석

파일을 읽거나 수정할 때마다 샌드박스 내에서 외부 모니터링 서버로 실시간 감사 이벤트를 전송합니다.

- **여러 도구 일치:** 일치자는 표준 정규 표현식을 사용하므로 파이프 (`read_file|write_file`) 또는 와일드카드 (`.*_file`)를 사용하여 단일 규칙에서 여러 도구를 결합할 수 있습니다.
- **구성에 비밀번호를 포함하지 않음:** 환경의 [네트워크 구성](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko#network-configuration) (`network.allowlist.transform`)에서 인증 토큰을 정의합니다. 이그레스 프록시는 나가는 요청에 실제 전달자 토큰을 자동으로 삽입합니다.

### Python

```
import json
from google import genai

client = genai.Client()

# Define hook without secrets; the egress proxy injects headers dynamically
hooks_config = {
    "audit-logging": {
        "post_tool_execution": [
            {
                "matcher": "read_file|write_file",
                "hooks": [
                    {
                        "type": "http",
                        "url": "https://telemetry.example.com/api/v1/agent-events",
                        "timeout": 10,
                    }
                ],
            }
        ]
    }
}

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/hooks.json",
                "content": json.dumps(hooks_config, indent=2),
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "telemetry.example.com",
                    "transform": {
                        "Authorization": "Bearer telemetry_secret_token_123",
                    },
                },
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

// Define hook without secrets; the egress proxy injects headers dynamically
const hooksConfig = {
    "audit-logging": {
        post_tool_execution: [
            {
                matcher: "read_file|write_file",
                hooks: [
                    {
                        type: "http",
                        url: "https://telemetry.example.com/api/v1/agent-events",
                        timeout: 10,
                    },
                ],
            },
        ],
    },
};

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Use your filesystem tool to create `/workspace/audit.log` containing 'event 1', then immediately read it back using your filesystem read tool.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/hooks.json",
                content: JSON.stringify(hooksConfig, null, 2),
            },
        ],
        network: {
            allowlist: [
                {
                    domain: "telemetry.example.com",
                    transform: {
                        Authorization: "Bearer telemetry_secret_token_123",
                    },
                },
                { domain: "*" },
            ],
        },
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
      "input": [{"type": "text", "text": "Use your filesystem tool to create /workspace/audit.log containing event 1, then immediately read it back using your filesystem read tool."}],
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/hooks.json",
                  "content": "{\"audit-logging\": {\"post_tool_execution\": [{\"matcher\": \"read_file|write_file\", \"hooks\": [{\"type\": \"http\", \"url\": \"https://telemetry.example.com/api/v1/agent-events\", \"timeout\": 10}]}]}}"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "telemetry.example.com",
                      "transform": {
                          "Authorization": "Bearer telemetry_secret_token_123"
                      }
                  },
                  {"domain": "*"}
              ]
          }
      }
  }'
```

## 제한사항

- **샌드박스 도구 범위:** 후크는 샌드박스 내의 기본 제공 도구(코드 실행(`code_execution`) 및 파일 시스템 작업(`read_file`, `write_file`, `list_files`, `delete_file`))를 가로챕니다. 컨테이너 외부에서 처리되는 맞춤 함수 호출(`function`) 또는 외부 모델 컨텍스트 프로토콜(`mcp_server`) 도구에는 실행되지 않습니다.
- **네트워크 허용 목록:** HTTP 후크는 컨테이너 네트워크 내에서 실행됩니다. 환경의 `network.allowlist`에서 대상 URL을 명시적으로 허용해야 합니다. 루프백 주소 (`localhost`, `127.0.0.1`)는 프록시에 의해 차단됩니다.
- **오류 시 자동 승인:** 후크 스크립트가 비정상 종료되거나 (0이 아닌 종료 상태) 제한 시간 초과되거나 실패하면 런타임은 실패를 로깅하고 도구 호출이 계속되도록 허용합니다. 이렇게 하면 손상된 린터 스크립트 또는 정지된 프로세스로 인해 애플리케이션이 교착 상태에 빠지지 않습니다.
- **샌드박스 구성 보호:** 후크는 컨테이너 샌드박스 내에서 실행되므로 파일 시스템 쓰기 도구 또는 셸 코드 실행 권한이 있는 에이전트는 쓰기 가능한 작업공간 내에서 로컬 `.agents/hooks.json` 또는 스크립트를 수정할 수 있습니다. 컨테이너 후크를 자동화된 정책 안내 및 운영 가드레일로 사용합니다. 신뢰할 수 없는 모델 실행에 대해 엄격한 변조 방지 기능이 필요한 경우 읽기 전용 저장소에서 구성 소스를 마운트합니다.

## 다음 단계

- 영구 [원격 샌드박스 및 환경](https://ai.google.dev/gemini-api/docs/agent-environment?hl=ko)을 구성하는 방법을 알아봅니다.
- [Antigravity 에이전트](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=ko)의 기능과 기본 제공 도구를 살펴봅니다.
- 다중 턴 세션 및 스트리밍에 관한 [Interactions API 개요](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=ko)를 검토합니다.

의견 보내기

달리 명시되지 않는 한 이 페이지의 콘텐츠에는 [Creative Commons Attribution 4.0 라이선스](https://creativecommons.org/licenses/by/4.0/)에 따라 라이선스가 부여되며, 코드 샘플에는 [Apache 2.0 라이선스](https://www.apache.org/licenses/LICENSE-2.0)에 따라 라이선스가 부여됩니다. 자세한 내용은 [Google Developers 사이트 정책](https://developers.google.com/site-policies?hl=ko)을 참조하세요. 자바는 Oracle 및/또는 Oracle 계열사의 등록 상표입니다.

최종 업데이트: 2026-09-11(UTC)

의견을 전달하고 싶나요?

[[["이해하기 쉬움","easyToUnderstand","thumb-up"],["문제가 해결됨","solvedMyProblem","thumb-up"],["기타","otherUp","thumb-up"]],[["필요한 정보가 없음","missingTheInformationINeed","thumb-down"],["너무 복잡함/단계 수가 너무 많음","tooComplicatedTooManySteps","thumb-down"],["오래됨","outOfDate","thumb-down"],["번역 문제","translationIssue","thumb-down"],["샘플/코드 문제","samplesCodeIssue","thumb-down"],["기타","otherDown","thumb-down"]],["최종 업데이트: 2026-09-11(UTC)"],[],[]]
