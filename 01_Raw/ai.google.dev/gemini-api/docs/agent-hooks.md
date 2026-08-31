---
source_url: https://ai.google.dev/gemini-api/docs/agent-hooks?hl=zh-CN
fetched_at: 2026-08-31T06:31:11.733848+00:00
title: "Hooks \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn) 现已正式发布。我们建议使用此 API 来访问所有最新功能和模型。

![](https://ai.google.dev/_static/images/translated.svg?hl=zh-cn)

Google 会使用 AI 技术将内容翻译成您偏好的语言。AI 翻译可能包含错误。

- [首页](https://ai.google.dev/?hl=zh-cn)
- [Gemini API](https://ai.google.dev/gemini-api?hl=zh-cn)
- [文档](https://ai.google.dev/gemini-api/docs?hl=zh-cn)

发送反馈

# Hooks

借助钩子，您可以在代理在其远程沙盒中执行代码或修改文件之前或之后运行自定义脚本或外部 HTTP 请求。使用钩子通过自动化安全措施和后台工作流来扩展代理循环，例如：

- 在执行高风险 shell 命令或受限文件读取操作之前，**强制执行安全和访问权限限制**。
- 在代理创建或修改文件后立即**自动执行数据流水线转换**。
- 在工具执行后，将企业审核遥测数据**流式传输**到外部监控系统。

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

## 支持的生命周期事件

钩子支持沙盒内的 2 个事件：

| 活动 | 触发时间 | 作用 |
| --- | --- | --- |
| `pre_tool_execution` | 工具运行前 | 可以在工具执行之前批准 (`allow`) 或屏蔽 (`deny`) 该工具。被屏蔽后，模型会看到您的拒绝原因并进行调整。 |
| `post_tool_execution` | 工具运行结束后立即执行 | 运行后续任务，例如格式化代码、运行单元测试或记录遥测数据。无法阻止或撤消已完成的操作。 |

### `pre_tool_execution`

在工具执行之前立即触发。脚本从 `stdin` 读取工具调用详细信息，并将其决策 JSON（`allow` 或 `deny`）输出到 `stdout`。

**输入载荷 (`stdin`)**：

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

**输出响应 (`stdout`)**：

批准工具调用：

```
{
  "decision": "allow"
}
```

如需阻止工具调用并向模型返回反馈，请执行以下操作：

```
{
  "decision": "deny",
  "reason": "Destructive command blocked by security gate."
}
```

如果钩子拒绝了命令，则会立即跳过工具调用。代理会在当前对话轮次中看到包含拒绝原因的错误结果。然后，模型可以通过选择替代命令或向用户说明屏蔽原因来进行自我修正。

如果脚本输出无法识别的 JSON、纯文本或除 `{"decision": "deny"}` 之外的任何内容，运行时会将该响应视为审批 (`allow`)。

### `post_tool_execution`

在工具完成时立即触发。您的脚本会从 `stdin` 读取执行详情和任何错误状态。

**输入载荷 (`stdin`)**：

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

如果 shell 命令将错误输出到标准错误 (`stderr`) 或文件系统操作失败，则载荷中会包含一个包含错误文本的 `"error"` 字段。如果命令成功执行且未出现错误，则系统会完全省略 `"error"` 字段。

**输出响应 (`stdout`)**：

```
{}
```

由于后工具钩子仅针对代码格式设置或日志记录等后台任务运行，因此运行时会忽略在 `stdout` 上返回的任何决策值。

## 配置发现

运行时会自动从沙盒环境中的 `.agents/hooks.json` 或 `/.agents/hooks.json` 中发现钩子定义。您可以使用任何受支持的[环境来源](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn#mount_from_a_source)，在自定义脚本旁边提供 `hooks.json`：

- **代码库装载**：包含 `.agents/hooks.json` 和 `AGENTS.md` 的 Git 代码库。
- **Cloud Storage (`gcs`)**：包含已复制到环境中的 `hooks.json` 的 GCS 存储分区。
- **内嵌来源**：调用 `client.interactions.create` 时在 `environment.sources` 中传递的原始 JSON 字符串和脚本内容。

### `hooks.json` 个架构

`hooks.json` 文件用于将事件定义（`pre_tool_execution` 或 `post_tool_execution`）归入自定义名称下。您可以单独启用或停用每个群组：

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

### 匹配器语法和规则

`hooks.json` 中的每个规则组都使用 `matcher` 和 `hooks` 属性定义了处理程序的触发时间和方式：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `enabled` | `boolean` | 可选。设置为 `false` 可停用相应群组（默认为 `true`）。 |
| `matcher` | `string` | 用于匹配容器内目标工具名称的正则表达式模式。 |
| `hooks` | `array` | 处理程序定义（`command` 或 `http`）的有序列表。处理程序按声明顺序依次运行。 |

#### 正则表达式评估的运作方式

当代理在沙盒内调用工具时，运行时会使用标准 RE2 正则表达式针对您的 `matcher` 模式评估工具的容器名称。如果正则表达式与工具名称匹配，则 `hooks` 数组中的所有处理程序将按顺序执行。如果多个规则组与同一工具匹配，则所有相应的处理程序数组都会运行。

您可以指定任何内置容器工具名称：代码执行 (`code_execution`) 或文件系统操作（`read_file`、`write_file`、`list_files` 和 `delete_file`）。

#### 常见的匹配器表达式

- `"code_execution"`：针对 shell 命令和脚本执行的精确字符串匹配。
- `"write_file"`：文件系统文件创建和磁盘写入的完全匹配。
- `"read_file|write_file"`：竖线分隔符可在单个规则中匹配多个特定工具名称。
- `".*_file"`：与任何以 `_file` 结尾的工具（例如 `read_file`、`write_file` 或 `delete_file`）匹配的正则表达式通配符。标准 RE2 正则表达式需要 `.*`；简单的 shell glob（例如 `*_file`）是无效的正则表达式语法，将无法匹配。
- `".*"` 或 `"*"` 或 `""`：捕获容器内每个工具调用的全能型模式。

## 处理程序类型

### 命令钩子

命令钩子在沙盒内执行 shell 命令或脚本。该脚本在 `stdin` 上接收事件 JSON，并在 `stdout` 上输出决策 JSON。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `string` | 必须为 `"command"`。 |
| `command` | `string` | 要在沙盒内运行的命令行（例如 `python3 /.agents/hooks-scripts/gate.py`）。 |
| `timeout` | `integer` | 超时时间（以秒为单位）。默认值：`30`。 |

### HTTP 钩子

HTTP 钩子会直接从沙盒网络内部将事件 JSON 作为 POST 请求发送到外部 HTTPS 网址。目标服务器使用完全相同的 JSON 格式（`{"decision": "allow"}` 或 `{"decision": "deny", "reason": "..."}`）在 HTTP 响应正文中返回其决策。

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `type` | `string` | 必须为 `"http"`。 |
| `url` | `string` | 用于向其 POST 事件载荷的外部 HTTPS 端点。 |
| `headers` | `object` | 非敏感自定义标头（例如 `{"X-Event-Source": "agent-sandbox"}`）的可选键值对。对于身份验证凭据，请改用网络代理。 |
| `timeout` | `integer` | 超时时间（以秒为单位）。默认值：`30`。 |

#### 出站代理和令牌转换

由于 HTTP 钩子直接从沙盒网络命名空间内部执行，因此出站请求会通过透明的出站代理。此架构可为您带来 2 项关键的安全优势：

- **网络许可名单**：必须在环境的 `network.allowlist` 中明确允许目标端点。环回流量（`127.0.0.1` 或 `localhost`）会被代理阻止；请始终以已列入许可名单的外部端点为目标。
- **令牌转换**：您无需在 `.agents/hooks.json` 中存储 API 密钥或不记名令牌，也无需将其装载到容器中。您可以在[网络配置](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn#network-configuration) (`network.allowlist.transform`) 中配置令牌转换规则。出站代理会自动拦截出站 HTTP 钩子流量，并在离开沙盒之前在网络上注入真实的身份验证标头。

## 运行时如何处理决策和失败

- **同步等待**：代理会暂停并等待您的钩子完成，然后再继续。
- **阻止工具执行**：如果您的工具前钩子返回 `{"decision": "deny", "reason": "<your reason>"}`，运行时会立即取消工具调用。模型会在对话记录中看到您的拒绝原因，然后选择安全的替代方案或向用户说明屏蔽原因，从而进行调整。
- **处理脚本崩溃、HTTP 错误和超时**：如果命令脚本崩溃（非零退出状态）、HTTP hook 返回非 2xx 状态代码（例如 4xx 或 5xx 服务器错误），或者操作超时或返回无法识别的 JSON，运行时会将其视为批准 (`allow`)。工具执行会正常继续，因此损坏的脚本或无法访问的遥测服务器永远不会导致应用死锁。

## 常见应用场景

### 针对数据隐私权和合规性的多轮对话恢复

当钩子阻止对受限资源（例如包含个人身份信息 [PII] 或机密财务记录的目录）的访问时，您可以在下一次调用中传递 `previous_interaction_id`，以在同一环境中继续执行回合。代理会读取拒绝说明，并通过查询已获批准的公开表自动恢复。

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

### 外部审核日志记录和遥测

在读取或修改文件时，从沙盒内部向外部监控服务器发送实时审核事件。

- **匹配多个工具**：由于匹配器使用标准正则表达式，因此您可以使用竖线 (`read_file|write_file`) 或通配符 (`.*_file`) 在单个规则中组合多个工具。
- **不要在配置中包含密钥**：在环境的[网络配置](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn#network-configuration) (`network.allowlist.transform`) 中定义身份验证令牌。出站代理会自动在出站请求中注入实际的令牌。

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

- **沙盒工具范围**：钩子会拦截沙盒内的内置工具：代码执行 (`code_execution`) 和文件系统操作（`read_file`、`write_file`、`list_files` 和 `delete_file`）。它们不会针对自定义函数调用 (`function`) 或在容器外部处理的外部 Model Context Protocol (`mcp_server`) 工具触发。
- **网络许可名单**：HTTP hook 在容器网络内运行。您必须在环境的 `network.allowlist` 中明确允许目标网址。环回地址（`localhost`、`127.0.0.1`）被代理屏蔽。
- **在出现错误时自动批准**：如果钩子脚本崩溃（退出状态不为零）、超时或失败，运行时会记录失败情况，并允许工具调用继续进行。这样可确保损坏的 lint 脚本或挂起的进程永远不会导致应用死锁。
- **沙盒配置保护**：由于钩子在容器沙盒内执行，因此具有文件系统写入工具或 shell 代码执行权限的代理可以修改可写入工作区中的本地 `.agents/hooks.json` 或脚本。使用容器钩子作为自动化政策指南和操作护栏；如果需要针对不受信任的模型执行提供严格的防篡改功能，请从只读代码库装载配置源。

## 后续步骤

- 了解如何配置持久性[远程沙盒和环境](https://ai.google.dev/gemini-api/docs/agent-environment?hl=zh-cn)。
- 探索 [Antigravity 智能体](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=zh-cn)的功能和内置工具。
- 查看[Interactions API 概览](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=zh-cn)，了解多轮会话和流式传输。

发送反馈

如未另行说明，那么本页面中的内容已根据[知识共享署名 4.0 许可](https://creativecommons.org/licenses/by/4.0/)获得了许可，并且代码示例已根据 [Apache 2.0 许可](https://www.apache.org/licenses/LICENSE-2.0)获得了许可。有关详情，请参阅 [Google 开发者网站政策](https://developers.google.com/site-policies?hl=zh-cn)。Java 是 Oracle 和/或其关联公司的注册商标。

最后更新时间 (UTC)：2026-07-30。

需要向我们提供更多信息？

[[["易于理解","easyToUnderstand","thumb-up"],["解决了我的问题","solvedMyProblem","thumb-up"],["其他","otherUp","thumb-up"]],[["没有我需要的信息","missingTheInformationINeed","thumb-down"],["太复杂/步骤太多","tooComplicatedTooManySteps","thumb-down"],["内容需要更新","outOfDate","thumb-down"],["翻译问题","translationIssue","thumb-down"],["示例/代码问题","samplesCodeIssue","thumb-down"],["其他","otherDown","thumb-down"]],["最后更新时间 (UTC)：2026-07-30。"],[],[]]
