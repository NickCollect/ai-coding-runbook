---
source_url: https://ai.google.dev/gemini-api/docs/custom-agents?hl=vi
fetched_at: 2026-08-31T06:37:16.756398+00:00
title: "T\u1ea1o t\u00e1c nh\u00e2n \u0111\u01b0\u1ee3c qu\u1ea3n l\u00fd \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

[Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview?hl=vi) hiện đã được phát hành rộng rãi. Bạn nên sử dụng API này để truy cập vào tất cả các tính năng và mô hình mới nhất.

![](https://ai.google.dev/_static/images/translated.svg?hl=vi)

Google sử dụng công nghệ AI để dịch nội dung sang ngôn ngữ bạn ưu tiên. Bản dịch bằng AI có thể có lỗi.

- [Trang chủ](https://ai.google.dev/?hl=vi)
- [Gemini API](https://ai.google.dev/gemini-api?hl=vi)
- [Tài liệu](https://ai.google.dev/gemini-api/docs?hl=vi)

Gửi ý kiến phản hồi

# Tạo tác nhân được quản lý

Các tác nhân được quản lý trên Gemini API cho phép bạn mở rộng tác nhân Antigravity bằng các hướng dẫn, kỹ năng và dữ liệu của riêng bạn. Bạn có thể [tuỳ chỉnh tác nhân nội tuyến](#customize-inline) tại thời điểm tương tác hoặc [lưu cấu hình](#save-agent) dưới dạng một tác nhân được quản lý mà bạn gọi bằng mã nhận dạng.

## Tuỳ chỉnh tác nhân Antigravity

Cách nhanh nhất để tạo một tác nhân tuỳ chỉnh là truyền cấu hình nội tuyến trong khi tạo một lượt tương tác mới mà không cần bước đăng ký. Bạn có thể mở rộng tác nhân theo một số cách chính:

- **[Lựa chọn mô hình](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#model-selection)**: Chọn mô hình Gemini cơ bản thông qua biểu tượng `agent_config` (mặc định là **Gemini 3.7 Flash**).
- **Hướng dẫn hệ thống**: Truyền văn bản nội tuyến qua `system_instruction` để định hình hành vi.
- **Công cụ**: Ghi đè các công cụ mặc định (Thực thi mã, Tìm kiếm, Ngữ cảnh URL), đăng ký các máy chủ MCP từ xa hoặc xác định các hàm tuỳ chỉnh (Gọi hàm).
- **Tệp và kỹ năng**: Gắn các tệp như `AGENTS.md` và `SKILL.md` vào môi trường.

Sau đây là ví dụ về cách truyền cả ba tham số nội tuyến:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a slide deck.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",        
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
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
    input: "Analyze the Q1 revenue data and create a slide deck.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",        
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "agent": "antigravity-preview-05-2026",
    "input": "Analyze the Q1 revenue data and create a slide deck.",
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            }
        ]
    }
}'
```

Mọi thứ đều được xác định tại thời điểm tương tác. Bạn không cần đăng ký trước bất cứ thông tin nào. Khung vận hành tác nhân Antigravity cung cấp thời gian chạy (thực thi mã, quản lý tệp, truy cập web) và các lớp cấu hình của bạn ở trên cùng.

### Công cụ và hướng dẫn về hệ thống

Bạn có thể tuỳ chỉnh hành vi và khả năng của tác nhân cho một lượt tương tác cụ thể bằng cách sử dụng các tham số `system_instruction` và `tools`.

- **Hướng dẫn của hệ thống**: Sử dụng tham số `system_instruction` để truyền văn bản nội tuyến định hình hành vi của tác nhân. Đây là lựa chọn lý tưởng cho những điều chỉnh nhanh mà bạn muốn thay đổi cho mỗi cuộc gọi. `system_instruction` và `AGENTS.md` là các giá trị cộng thêm; cả hai đều được áp dụng khi xuất hiện.
- **Công cụ**: Theo mặc định, tác nhân Antigravity có quyền truy cập vào `code_execution`, `google_search` và `url_context`. Bạn có thể ghi đè danh sách này bằng cách truyền tham số `tools` tại thời điểm tương tác. Bạn cũng có thể đăng ký [các máy chủ MCP từ xa](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#mcp-servers) hoặc xác định [các hàm tuỳ chỉnh (gọi hàm)](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#function-calling) để kết nối tác nhân với các API và cơ sở dữ liệu của riêng bạn. Để biết thông tin chi tiết về các công cụ hiện có, hãy xem bài viết [Antigravity Agent: Các công cụ được hỗ trợ](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#supported-tools).

### Tuỳ chỉnh dựa trên tệp

#### Cấu trúc thư mục tác nhân

Mặc dù có thể truyền cấu hình nội tuyến, nhưng bạn nên sắp xếp các tệp của tác nhân trong một thư mục có cấu trúc. Điều này giúp bạn quản lý, quản lý phiên bản và gắn vào môi trường của tác nhân dễ dàng hơn.

Thư mục dự án tác nhân điển hình có dạng như sau:

```
my-agent/
├── AGENTS.md        # Instructions on how the agent should operate
├── skills/          # Custom skills (subfolders and SKILL.md files)
│   └── slide-maker/
│       └── SKILL.md
└── workspace/       # Initial data files and knowledge
```

Thời gian chạy Antigravity sẽ quét `.agents/` (và gốc của môi trường) để tìm các tệp này.

#### AGENTS.md

Tác nhân sẽ tự động tải `.agents/AGENTS.md` (hoặc `/.agents/AGENTS.md`) từ môi trường dưới dạng hướng dẫn hệ thống khi khởi động. Sử dụng `AGENTS.md` cho các định nghĩa về vai trò ở dạng dài, hướng dẫn chi tiết và hướng dẫn mà bạn muốn quản lý phiên bản cùng với mã của mình.

Gắn `AGENTS.md` bằng nguồn cùng dòng:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Analyze the Q1 revenue data and create a report.",
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
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
    input: "Analyze the Q1 revenue data and create a report.",
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Analyze the Q1 revenue data and create a report.",
      "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/AGENTS.md",
                  "content": "Always use matplotlib for charts. Include a summary table in every report."
              }
          ]
      }
  }'
```

#### Kỹ năng: SKILL.md

වන Các kỹ năng là những tệp mở rộng khả năng của đặc vụ. Đặt các thiết bị này trong `.agents/skills/<skill-name>/SKILL.md` và harness sẽ tự động phát hiện và đăng ký chúng.

```
.agents/
├── AGENTS.md
└── skills/
    └── slide-maker/
        └── SKILL.md
```

Gắn một kỹ năng bằng nguồn cùng dòng:

### Python

```
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Create a presentation about our Q1 results.",
    system_instruction="You create presentations from data.",
    environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
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
    input: "Create a presentation about our Q1 results.",
    system_instruction: "You create presentations from data.",
    environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html",
            },
        ],
    },
}, { timeout: 300000 });

console.log(interaction.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Create a presentation about our Q1 results.",
      "system_instruction": "You create presentations from data.",
      "environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "inline",
                  "target": ".agents/skills/slide-maker/SKILL.md",
                  "content": "---\nname: slide-maker\ndescription: Create HTML slide decks\n---\n# Slide Maker\n\nWhen asked to create a presentation:\n1. Analyze the input data\n2. Create an HTML slide deck with reveal.js\n3. Save to /workspace/output/slides.html"
              }
          ]
      }
  }'
```

Các kỹ năng được tải từ `.agents/skills/` và `/.agents/skills/` đều được phát hiện tự động.

## Tạo một tác nhân được quản lý

Sau khi lặp lại cấu hình, bạn có thể tạo cấu hình đó dưới dạng một tác nhân được quản lý bằng `agents.create`. Nhờ đó, bạn có thể gọi tác nhân theo mã nhận dạng mà không cần lặp lại cấu hình mỗi lần.

`id` mà bạn chỉ định khi tạo một tác nhân được quản lý phải là duy nhất cho dự án của bạn và không được bắt đầu bằng các tiền tố dành riêng (ví dụ: `google-`, `gemini-`). Hãy xem [Các hạn chế về mã nhận dạng tác nhân](#agent-id-restrictions) để biết danh sách đầy đủ các tiền tố bị hạn chế.

### Từ các nguồn

Chỉ định `base_agent`, `id`, `agent_config`, `system_instruction` và `base_environment` bằng các nguồn. Nền tảng này cung cấp một hộp cát mới chứa các tệp của bạn trên mọi lệnh gọi. Hãy xem phần [Môi trường](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi) để biết các loại nguồn có sẵn (Git, GCS, nội tuyến).

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="data-analyst",
    base_agent="antigravity-preview-05-2026",
    agent_config={
        "type": "antigravity",
        "model": "gemini-3.7-flash",
    },
    system_instruction="You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates",
            },
        ],
    },
)

print(f"Created agent: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "data-analyst",
    base_agent: "antigravity-preview-05-2026",
    agent_config: {
        type: "antigravity",
        model: "gemini-3.7-flash",
    },
    system_instruction: "You are a data analyst. Always include visualizations and export results as PDF.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "inline",
                target: ".agents/AGENTS.md",
                content: "Always use matplotlib for charts. Include a summary table in every report.",
            },
            {
                type: "inline",
                target: ".agents/skills/slide-maker/SKILL.md",
                content: "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results.",
            },
            {
                type: "repository",
                source: "https://github.com/my-org/analysis-templates",
                target: "/workspace/templates",
            },
        ],
    },
});

console.log(`Created agent: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-d '{
    "id": "data-analyst",
    "base_agent": "antigravity-preview-05-2026",
    "agent_config": {
        "type": "antigravity",
        "model": "gemini-3.7-flash"
    },
    "system_instruction": "You are a data analyst. Always include visualizations and export results as PDF.",
    "base_environment": {
        "type": "remote",
        "sources": [
            {
                "type": "inline",
                "target": ".agents/AGENTS.md",
                "content": "Always use matplotlib for charts. Include a summary table in every report."
            },
            {
                "type": "inline",
                "target": ".agents/skills/slide-maker/SKILL.md",
                "content": "---\nname: slide-maker\n---\n# Slide Maker\nCreate HTML slide decks from data analysis results."
            },
            {
                "type": "repository",
                "source": "https://github.com/my-org/analysis-templates",
                "target": "/workspace/templates"
            }
        ]
    }
}'
```

### Từ một môi trường hiện có (phân nhánh)

Lặp lại với tác nhân Antigravity cơ bản cho đến khi môi trường phù hợp (đã cài đặt các gói, tệp ở đúng vị trí), sau đó phân nhánh tác nhân này thành một tác nhân được quản lý.

### Python

```
from google import genai

client = genai.Client()

# Step 1: set up the environment interactively
interaction = client.interactions.create(
    agent="antigravity-preview-05-2026",
    input="Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment="remote",
)

# Step 2: fork that environment into a managed agent

agent = client.agents.create(
    id="my-data-analyst",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment=interaction.environment_id,
)

print(f"Forked agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    agent: "antigravity-preview-05-2026",
    input: "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
    environment: "remote",
}, { timeout: 300000 });

const agent = await client.agents.create({
    id: "my-data-analyst",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You are a data analyst. Use the template at /workspace/template.py for all reports.",
    base_environment: interaction.environment_id,
});

console.log(`Forked agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "antigravity-preview-05-2026",
      "input": "Install pandas, matplotlib, and seaborn. Create an analysis template at /workspace/template.py.",
      "environment": "remote"
  }'
```

### Có quy tắc mạng

Bạn có thể khoá quyền truy cập đi hoặc chèn thông tin đăng nhập khi lưu một tác nhân được quản lý. Aware For the full allowlist schema, credential patterns, and wildcards, see [Environments: Network configuration](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi#network-configuration) (Môi trường: Cấu hình mạng).

Ví dụ sau đây sẽ tạo một tác nhân `issue-resolver` chỉ có thể truy cập vào GitHub và PyPI, với thông tin đăng nhập được chèn cho GitHub:

### Python

```
from google import genai

client = genai.Client()

agent = client.agents.create(
    id="issue-resolver",
    base_agent="antigravity-preview-05-2026",
    system_instruction="You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment={
        "type": "remote",
        "sources": [
            {
                "type": "repository",
                "source": "https://github.com/my-org/backend",
                "target": "/workspace/repo",
            }
        ],
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(f"Created issue-resolver agent successfully: {agent.id}")
```

### JavaScript

```
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const agent = await client.agents.create({
    id: "issue-resolver",
    base_agent: "antigravity-preview-05-2026",
    system_instruction: "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
    base_environment: {
        type: "remote",
        sources: [
            {
                type: "repository",
                source: "https://github.com/my-org/backend",
                target: "/workspace/repo",
            }
        ],
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Basic YOUR_BASE64_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        }
    },
});

console.log(`Created issue-resolver agent successfully: ${agent.id}`);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "id": "issue-resolver",
      "base_agent": "antigravity-preview-05-2026",
      "system_instruction": "You resolve GitHub issues. Clone the repo, find the bug, write the fix, run the tests, and open a PR.",
      "base_environment": {
          "type": "remote",
          "sources": [
              {
                  "type": "repository",
                  "source": "https://github.com/my-org/backend",
                  "target": "/workspace/repo"
              }
          ],
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Basic YOUR_BASE64_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Gọi tác nhân

Gọi tác nhân được quản lý bằng mã nhận dạng tác nhân bằng cách tạo một lượt tương tác mới. Mỗi lệnh gọi sẽ phân nhánh môi trường cơ sở, vì vậy, mọi lượt chạy đều bắt đầu từ đầu.

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment="remote",
)

print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data from /workspace/templates/sample.csv and create a slide deck.",
      "environment": "remote"
  }'
```

Đối với các cuộc trò chuyện nhiều lượt và phát trực tuyến, hãy xem phần [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi). Các mẫu `previous_interaction_id` và `environment` tương tự cũng áp dụng cho các tác nhân được quản lý.

Các tác nhân được quản lý cũng hỗ trợ việc thực thi và huỷ trong nền. Để biết thông tin chi tiết và ví dụ về mã, hãy xem bài viết [Antigravity Agent: Background execution](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi#background-execution) (Tác nhân chống trọng lực: Thực thi ở chế độ nền).

## Ghi đè cấu hình khi gọi

Bạn có thể ghi đè cấu hình mạng `system_instruction`, `tools` và `environment` mặc định của tác nhân khi tạo một lượt tương tác. Thao tác này cho phép bạn sửa đổi hành vi, khả năng hoặc thông tin đăng nhập của tác nhân cho một lần chạy cụ thể mà không thay đổi định nghĩa tác nhân đã lưu trữ.

### Ghi đè hướng dẫn và công cụ hệ thống

### Python

```
result = client.interactions.create(
    agent="data-analyst",
    input="Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction="You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools=[{"type": "code_execution"}], # Override to only use code execution
    environment="remote",
)
print(result.output_text)
```

### JavaScript

```
const result = await client.interactions.create({
    agent: "data-analyst",
    input: "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
    system_instruction: "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
    tools: [{ type: "code_execution" }], // Override to only use code execution
    environment: "remote",
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "data-analyst",
      "input": "Analyze Q1 revenue data, but do not create a slide deck. Just output a summary table.",
      "system_instruction": "You are a data analyst. Focus ONLY on summary tables. Ignore default instructions about slides.",
      "tools": [{"type": "code_execution"}],
      "environment": "remote"
  }'
```

### Ghi đè cấu hình mạng (làm mới thông tin đăng nhập)

Nếu tác nhân được quản lý của bạn có thông tin đăng nhập mạng được tích hợp vào `base_environment`, bạn có thể ghi đè thông tin đăng nhập đó tại thời điểm gọi để làm mới mã thông báo đã hết hạn hoặc xoay khoá API. Truyền một đối tượng `environment` có cấu hình `network` mới. Các quy tắc mạng mới sẽ thay thế hoàn toàn các quy tắc trước đó cho hoạt động tương tác đó. Các nguồn (tệp, kho lưu trữ) của môi trường cơ sở sẽ được giữ nguyên.

### Python

```
# Invoke the agent with a fresh token, overriding the base_environment credentials
result = client.interactions.create(
    agent="issue-resolver",
    input="Fix issue #42 and open a PR.",
    environment={
        "type": "remote",
        "network": {
            "allowlist": [
                {
                    "domain": "api.github.com",
                    "transform": {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                {"domain": "pypi.org"},
            ]
        },
    },
)

print(result.output_text)
```

### JavaScript

```
// Invoke the agent with a fresh token, overriding the base_environment credentials
const result = await client.interactions.create({
    agent: "issue-resolver",
    input: "Fix issue #42 and open a PR.",
    environment: {
        type: "remote",
        network: {
            allowlist: [
                {
                    domain: "api.github.com",
                    transform: {
                        "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                    },
                },
                { domain: "pypi.org" },
            ]
        },
    },
}, { timeout: 300000 });

console.log(result.output_text);
```

### REST

```
curl -X POST "https://generativelanguage.googleapis.com/v1beta/interactions" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -d '{
      "agent": "issue-resolver",
      "input": "Fix issue #42 and open a PR.",
      "environment": {
          "type": "remote",
          "network": {
              "allowlist": [
                  {
                      "domain": "api.github.com",
                      "transform": {
                          "Authorization": "Bearer ghp_REFRESHED_TOKEN"
                      }
                  },
                  {"domain": "pypi.org"}
              ]
          }
      }
  }'
```

## Quản lý nhân viên hỗ trợ

Bạn có thể liệt kê, nhận và xoá các tác nhân.

### Liệt kê các tác nhân

### Python

```
agents = client.agents.list()
for a in agents.agents:
    print(f"{a.id}: {a.description}")
```

### JavaScript

```
const agents = await client.agents.list();
if (agents.agents) {
    for (const a of agents.agents) {
        console.log(`${a.id}: ${a.description}`);
    }
}
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Nhận tác nhân

### Python

```
agent = client.agents.get(id="data-analyst")
print(agent)
```

### JavaScript

```
const agent = await client.agents.get("data-analyst");
console.log(agent);
```

### REST

```
curl -X GET "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

### Xoá một nhân viên hỗ trợ

Thao tác xoá sẽ loại bỏ cấu hình. Các môi trường và hoạt động tương tác hiện có do tác nhân tạo ra sẽ không bị ảnh hưởng.

### Python

```
client.agents.delete(id="data-analyst")
```

### JavaScript

```
await client.agents.delete("data-analyst");
```

### REST

```
curl -X DELETE "https://generativelanguage.googleapis.com/v1beta/agents/data-analyst" \
  -H "x-goog-api-key: $GEMINI_API_KEY"
```

## Thông tin tham khảo về định nghĩa tác nhân

| Trường | Loại | Bắt buộc | Mô tả |
| --- | --- | --- | --- |
| `id` | chuỗi | Có | Giá trị nhận dạng riêng biệt của tác nhân trong dự án trên đám mây Google. Dùng để gọi tác nhân. Không được sử dụng tiền tố dành riêng. Xem [Hạn chế về mã nhận dạng của tác nhân](#agent-id-restrictions). |
| `description` | chuỗi | Không | Nội dung mô tả mà con người có thể đọc được về tác nhân. |
| `base_agent` | chuỗi | Có | Mã nhận dạng tác nhân cơ sở (ví dụ: `antigravity-preview-05-2026`). |
| `agent_config` | đối tượng | Không | Cấu hình cho tác nhân cơ sở, bao gồm cả lựa chọn mô hình (`{"type": "antigravity", "model": "gemini-3.7-flash"}`). Mặc định là `gemini-3.7-flash` nếu bị bỏ qua. Không thể ghi đè vào thời điểm tương tác đối với các nhân viên hỗ trợ được đặt tên. |
| `system_instruction` | chuỗi | Không | Lời nhắc hệ thống xác định hành vi và tính cách. |
| `tools` | mảng | Không | Các công cụ mà trợ lý có thể sử dụng. ഓം Nếu bị bỏ qua, giá trị mặc định sẽ là `code_execution`, `google_search` và `url_context`. Các công cụ được hỗ trợ bao gồm `code_execution`, `google_search`, `url_context`, `mcp_server` và các định nghĩa `function` tuỳ chỉnh. |
| `base_environment` | chuỗi hoặc đối tượng | Không | `"remote"`, `environment_id` hoặc một đối tượng cấu hình có `sources` và `network`. Xem phần Môi trường. |

### Các hạn chế về mã nhận dạng tác nhân

Khi tạo một tác nhân được quản lý, `id` mà bạn chỉ định phải tuân theo các quy tắc sau:

- Giá trị này phải dành riêng cho dự án trên đám mây của bạn trên Google Cloud.
- Tên này **không** được bắt đầu bằng bất kỳ tiền tố dành riêng nào sau đây (không phân biệt chữ hoa chữ thường), nếu không, quá trình tạo sẽ thất bại:
  - `antigravity-`
  - `veo-`
  - `omni-`
  - `lyria-`
  - `imagen-`
  - `gemma-`
  - `gemini-`
  - `google-`
  - `youtube-`
  - `android-`
  - `chrome-`
  - `pixel-`
  - `waze-`
  - `fitbit-`
  - `nest-`
  - `kaggle-`

## Quy trình lặp lại

1. **Tạo nguyên mẫu** bằng tác nhân Antigravity cơ bản. Truyền hướng dẫn hệ thống và các nguồn môi trường nội tuyến. Kiểm tra hướng dẫn, kỹ năng và chế độ thiết lập môi trường một cách tương tác.
2. **Ổn định** môi trường. Cài đặt các gói, gắn nguồn, xác minh mọi thứ đều hoạt động.
3. **Duy trì** dưới dạng một tác nhân được quản lý bằng cách tạo một tác nhân mới, từ các nguồn hoặc bằng cách phân nhánh môi trường.
4. **Cập nhật** định nghĩa về tác nhân. Thay đổi chỉ dẫn hệ thống, chuyển đổi kỹ năng hoặc thêm nguồn. Lần gọi tiếp theo sẽ lấy cấu hình mới.

## Các điểm hạn chế

- **Trạng thái xem trước**: Các tác nhân được quản lý đang ở giai đoạn xem trước. Các tính năng và giản đồ có thể thay đổi.
- **Tác nhân và mô hình cơ sở**: Chỉ `antigravity-preview-05-2026` được hỗ trợ dưới dạng `base_agent`. Các lựa chọn về mô hình được hỗ trợ trong `agent_config` là `gemini-3.7-flash` (mặc định), `gemini-3.6-flash`, `gemini-3.5-flash` và `gemini-3.5-flash-lite`. Đối với các tác nhân được đặt tên, bạn không thể ghi đè mô hình tại thời điểm tương tác.
- **Không có tính năng quản lý phiên bản**: Hiện chưa có tính năng quản lý phiên bản và khôi phục phiên bản cũ của tác nhân.
- **спортивные ставки**
- Bạn có thể có tối đa 1.000 nhân viên hỗ trợ được quản lý.

## Bước tiếp theo

- [Tổng quan về tác nhân](https://ai.google.dev/gemini-api/docs/agents?hl=vi): Tìm hiểu về các khái niệm cốt lõi của tác nhân được quản lý.
- [Bắt đầu nhanh](https://ai.google.dev/gemini-api/docs/managed-agents-quickstart?hl=vi): Bắt đầu xây dựng bằng các cuộc trò chuyện nhiều lượt và tính năng phát trực tuyến.
- Sponsored by [Antigravity Agent](https://ai.google.dev/gemini-api/docs/antigravity-agent?hl=vi): Khám phá các chức năng, công cụ và giá của tác nhân mặc định.
- [Môi trường của tác nhân](https://ai.google.dev/gemini-api/docs/agent-environment?hl=vi): Định cấu hình hộp cát, nguồn và mạng.
- [Managed Agents API trên Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents?hl=vi): Để tạo các tác nhân được quản lý có cơ chế quản trị tổ chức tích hợp.

Gửi ý kiến phản hồi

Trừ phi có lưu ý khác, nội dung của trang này được cấp phép theo [Giấy phép ghi nhận tác giả 4.0 của Creative Commons](https://creativecommons.org/licenses/by/4.0/) và các mẫu mã lập trình được cấp phép theo [Giấy phép Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0). Để biết thông tin chi tiết, vui lòng tham khảo [Chính sách trang web của Google Developers](https://developers.google.com/site-policies?hl=vi). Java là nhãn hiệu đã đăng ký của Oracle và/hoặc các đơn vị liên kết với Oracle.

Cập nhật lần gần đây nhất: 2026-08-19 UTC.

Bạn muốn chia sẻ thêm với chúng tôi?

[[["Dễ hiểu","easyToUnderstand","thumb-up"],["Giúp tôi giải quyết được vấn đề","solvedMyProblem","thumb-up"],["Khác","otherUp","thumb-up"]],[["Thiếu thông tin tôi cần","missingTheInformationINeed","thumb-down"],["Quá phức tạp/quá nhiều bước","tooComplicatedTooManySteps","thumb-down"],["Đã lỗi thời","outOfDate","thumb-down"],["Vấn đề về bản dịch","translationIssue","thumb-down"],["Vấn đề về mẫu/mã","samplesCodeIssue","thumb-down"],["Khác","otherDown","thumb-down"]],["Cập nhật lần gần đây nhất: 2026-08-19 UTC."],[],[]]
