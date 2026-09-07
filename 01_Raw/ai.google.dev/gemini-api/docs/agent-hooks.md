---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=zh-TW
fetched_at: 2026-09-07T05:39:09.170997+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw) 現已正式發布。建議使用這個 API，存取所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-tw)

Google 會運用 AI 技術將內容翻譯成你偏好的語言，但可能會出錯。

- [首頁](https://ai.google.dev/?hl=zh-tw)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-tw)
- [文件](https://ai.google.dev/gemini-api/docs?hl=zh-tw)

提供意見

# Hooks

您可以使用 Hook 在代理程式執行程式碼或修改遠端沙箱內的檔案前後，執行自訂指令碼或外部 HTTP 要求。使用掛鉤擴充代理迴圈，並搭配自動防護措施和背景工作流程，例如：

- **強制執行安全和存取防護措施**，再執行高風險的殼層指令或受限的檔案讀取作業。
- **在代理程式建立或修改檔案後，自動轉換資料管道**。
- 工具執行後，**將企業稽核遙測資料串流至外部監控系統**。

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

## 支援的生命週期事件

沙箱中的 Hook 支援 2 個事件：

| 事件 | 觸發時機 | 用途 |
| --- | --- | --- |
| `pre_tool_execution` | 工具執行前 | 可以在工具執行前核准 (`allow`) 或封鎖 (`deny`) 工具。遭到封鎖時，模型會看到拒絕原因並進行調整。 |
| `post_tool_execution` | 工具執行完畢後 | 執行後續工作，例如格式化程式碼、執行單元測試或記錄遙測資料。無法封鎖或復原已完成的動作。 |

### `pre_tool_execution`

在工具執行前觸發。您的指令碼會從 `stdin` 讀取工具呼叫詳細資料，並將決策 JSON (`allow` 或 `deny`) 輸出至 `stdout`。

**輸入酬載 (`stdin`)：**

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

**輸出回覆 (`stdout`)：**

如要核准工具呼叫：

```
{
  "decision": "allow"
}
```

如要封鎖工具呼叫並將意見回饋傳回模型，請執行下列操作：

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

如果掛鉤拒絕指令，系統會立即略過工具呼叫。代理程式會在目前的對話輪次中看到錯誤結果，其中包含拒絕原因。接著，模型可以選擇替代指令或向使用者說明封鎖原因，藉此自我修正。

如果指令碼輸出無法辨識的 JSON、純文字或 `{"decision": "deny"}` 以外的任何內容，執行階段會將回應視為核准 (`allow`)。

### `post_tool_execution`

工具完成後立即觸發。指令碼會從 `stdin` 讀取執行詳細資料和任何錯誤狀態。

**輸入酬載 (`stdin`)：**

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

如果殼層指令將錯誤輸出至標準錯誤 (`stderr`) 或檔案系統作業失敗，酬載中會包含含有錯誤文字的 `"error"` 欄位。如果指令順利執行且未發生錯誤，系統會完全省略 `"error"` 欄位。

**輸出回覆 (`stdout`)：**

```
{}
```

由於工具後續掛鉤僅適用於程式碼格式化或記錄等背景工作，因此執行階段會忽略 `stdout` 傳回的任何決策值。

## 設定探索

執行階段會自動從沙箱環境中的 `.agents/hooks.json` 或 `/.agents/hooks.json` 探索 Hook 定義。您可以使用任何支援的[環境來源](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#mount_from_a_source)，在自訂指令碼旁提供 `hooks.json`：

- **存放區掛接**：包含 `.agents/hooks.json` 和 `AGENTS.md` 的 Git 存放區。
- **Cloud Storage (`gcs`)**：包含複製到環境中的 `hooks.json` 的 GCS bucket。
- **內嵌來源**：呼叫 `client.interactions.create` 時，以 `environment.sources` 傳遞的原始 JSON 字串和指令碼內容。

### `hooks.json` 個結構定義

`hooks.json` 檔案會將事件定義 (`pre_tool_execution` 或 `post_tool_execution`) 分組到自訂名稱下。你可以分別啟用或停用各個群組：

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

### 比對器語法和規則

`hooks.json` 中的每個規則群組都會使用 `matcher` 和 `hooks` 屬性，定義處理常式觸發的時機和方式：

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `enabled` | `boolean` | (選用步驟) 設為 `false` 即可停用群組 (預設為 `true`)。 |
| `matcher` | `string` | 規則運算式模式，用於比對容器內的目標工具名稱。 |
| `hooks` | `array` | 處理常式定義的已排序清單 (`command` 或 `http`)。處理常式會依宣告順序依序執行。 |

#### 規則運算式評估的運作方式

當代理在沙箱中叫用工具時，執行階段會使用標準 RE2 規則運算式，根據 `matcher` 模式評估工具的容器名稱。如果規則運算式與工具名稱相符，`hooks` 陣列中的所有處理常式會依序執行。如果多個規則群組符合同一項工具，系統會執行所有對應的處理常式陣列。

您可以指定任何內建容器工具名稱：執行程式碼 (`code_execution`) 或檔案系統作業 (`read_file`、`write_file`、`list_files` 和 `delete_file`)。

#### 常見的比對運算式

- `"code_execution"`：完全比對殼層指令和指令碼執行的字串。
- `"write_file"`：完全符合檔案系統檔案建立和磁碟寫入作業。
- `"read_file|write_file"`：以直立線分隔，在單一規則中比對多個特定工具名稱。
- `".*_file"`：規則運算式萬用字元，可比對任何以 `_file` 結尾的工具 (例如 `read_file`、`write_file` 或 `delete_file`)。標準 RE2 規則運算式需要 `.*`；簡單的殼層 glob (例如 `*_file`) 是無效的規則運算式語法，無法比對。
- `".*"` 或 `"*"` 或 `""`：攔截容器內每個工具呼叫的萬用模式。

## 處理常式類型

### 指令掛鉤

指令掛鉤會在沙箱內執行殼層指令或指令碼。指令碼會在 `stdin` 接收事件 JSON，並在 `stdout` 輸出決策 JSON。

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `type` | `string` | 必須為 `"command"`。 |
| `command` | `string` | 要在沙箱內執行的指令列 (例如 `python3 /.agents/hooks-scripts/gate.py`)。 |
| `timeout` | `integer` | 逾時時間 (以秒為單位)。預設：`30`。 |

### HTTP 勾點

HTTP 勾點會從沙箱網路內部，以 POST 要求的形式，將事件 JSON 直接傳送至外部 HTTPS 網址。目標伺服器會使用完全相同的 JSON 格式 (`{"decision": "allow"}` 或 `{"decision": "deny", "reason": "..."}`)，在 HTTP 回應主體中傳回決策。

| 欄位 | 類型 | 說明 |
| --- | --- | --- |
| `type` | `string` | 必須為 `"http"`。 |
| `url` | `string` | 要將事件酬載 POST 至的外部 HTTPS 端點。 |
| `headers` | `object` | 非機密自訂標頭的選用鍵/值組合 (例如 `{"X-Event-Source": "agent-sandbox"}`)。如需驗證憑證，請改用網路 Proxy。 |
| `timeout` | `integer` | 逾時時間 (以秒為單位)。預設：`30`。 |

#### 輸出 Proxy 和權杖轉換

由於 HTTP 勾點會直接從沙箱網路命名空間內執行，因此輸出要求會通過透明輸出 Proxy。這種架構可提供 2 項重要安全性優勢：

- **網路許可清單：**環境的 `network.allowlist` 必須明確允許目標端點。Proxy 會封鎖迴路流量 (`127.0.0.1` 或 `localhost`)，請一律以許可清單中的外部端點為目標。
- **權杖轉換：**您不需要在 `.agents/hooks.json` 內儲存 API 金鑰或密鑰持有者權杖，也不必將這些權杖掛接到容器。請改為在[網路設定](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#network-configuration) (`network.allowlist.transform`) 中設定權杖轉換規則。輸出 Proxy 會自動攔截外送 HTTP Hook 流量，並在離開沙箱前，在網路上插入實際的驗證標頭。

## 執行階段如何處理決策和失敗

- **同步等待：**代理程式會暫停並等待掛鉤完成，然後再繼續。
- **封鎖工具執行：**如果工具前置掛鉤傳回 `{"decision": "deny", "reason": "<your reason>"}`，執行階段會立即取消工具呼叫。模型會在對話記錄中看到拒絕原因，並選擇安全替代方案或向使用者說明封鎖原因，藉此調整回應。
- **處理指令碼當機、HTTP 錯誤和逾時：**如果指令碼當機 (非零結束狀態)、HTTP 勾點傳回非 2xx 狀態碼 (例如 4xx 或 5xx 伺服器錯誤)，或作業逾時或傳回無法辨識的 JSON，執行階段會將其視為核准 (`allow`)。工具執行作業會正常繼續，因此損毀的指令碼或無法連線的遙測伺服器絕不會導致應用程式死結。

## 常見用途

### 多輪對話復原功能，確保資料隱私權和法規遵循

如果 Hook 封鎖受限資源的存取權 (例如含有個人識別資訊 (PII) 或機密財務記錄的目錄)，您可以在下一次呼叫時傳遞 `previous_interaction_id`，繼續在相同環境中進行回合。代理程式會讀取拒絕說明，並改為查詢核准的公開資料表，自動復原。

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

### 外部稽核記錄和遙測

每當讀取或修改檔案時，從沙箱內部將即時稽核事件傳送至外部監控伺服器。

- **比對多個工具：**由於比對器使用標準規則運算式，因此您可以在單一規則中，使用直立線 (`read_file|write_file`) 或萬用字元 (`.*_file`) 組合多個工具。
- **避免在設定中加入密鑰：**在環境的[網路設定](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw#network-configuration) (`network.allowlist.transform`) 中定義驗證權杖。輸出 Proxy 會在傳送要求時自動插入實際的承載權杖。

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

## 限制

- **沙箱工具範圍：**掛鉤會攔截沙箱內的內建工具：執行程式碼 (`code_execution`) 和檔案系統作業 (`read_file`、`write_file`、`list_files` 和 `delete_file`)。掛鉤不會針對自訂函式呼叫 (`function`) 或在容器外處理的外部 Model Context Protocol (`mcp_server`) 工具觸發。
- **網路許可清單：**HTTP 勾點會在容器網路內執行。您必須在環境的 `network.allowlist` 中明確允許目標網址。Proxy 會封鎖迴路位址 (`localhost`、`127.0.0.1`)。
- **發生錯誤時自動核准：**如果 Hook 指令碼當機 (非零的結束狀態)、逾時或失敗，執行階段會記錄失敗情形，並允許工具呼叫繼續執行。這樣一來，損毀的 Linter 指令碼或閒置的程序就不會導致應用程式死結。
- **沙箱設定保護：**由於 Hook 會在容器沙箱內執行，因此具備檔案系統寫入工具或殼層程式碼執行權限的代理程式，可以修改可寫入工作區中的本機 `.agents/hooks.json` 或指令碼。使用容器掛鉤做為自動政策指引和作業防護措施；如果需要嚴格防範不受信任的模型執行作業遭到竄改，請從唯讀存放區掛接設定來源。

## 後續步驟

- 瞭解如何設定永久[遠端沙箱和環境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-tw)。
- 探索 [Antigravity 代理程式](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-tw)的功能和內建工具。
- 如要瞭解多輪對話工作階段和串流，請參閱 [Interactions API 總覽](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-tw)。

提供意見

除非另有註明，否則本頁面中的內容是採用[創用 CC 姓名標示 4.0 授權](https://creativecommons.org/licenses/by/4.0/)，程式碼範例則為[阿帕契 2.0 授權](https://www.apache.org/licenses/LICENSE-2.0)。詳情請參閱《[Google Developers 網站政策](https://developers.google.com/site-policies?hl=zh-tw)》。Java 是 Oracle 和/或其關聯企業的註冊商標。

上次更新時間：2026-07-30 (世界標準時間)。

想進一步說明嗎？

[[["容易理解","easyToUnderstand","thumb-up"],["確實解決了我的問題","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["缺少我需要的資訊","missingTheInformationINeed","thumb-down"],["過於複雜/步驟過多","tooComplicatedTooManySteps","thumb-down"],["過時","outOfDate","thumb-down"],["翻譯問題","translationIssue","thumb-down"],["示例/程式碼問題","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["上次更新時間：2026-07-30 (世界標準時間)。"],[],[]]
