---
type: summary
source: 01_Raw/docs.cursor.com/docs--enterprise--privacy-and-data-governance.md
source_url: https://cursor.com/docs/enterprise/privacy-and-data-governance
title: "Enterprise 隐私与数据治理"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

理解数据如何流经 Cursor 对安全审查至关重要。数据离开本地环境有三条路径。

**三条数据流**：
1. **索引过程**：代码临时发送以生成嵌入向量，原始代码丢弃；仅存储单向数学向量（无法逆向还原）、混淆后的文件路径和行号
2. **LLM 请求**：启用 Privacy Mode 时，代码不被存储和训练（与 OpenAI/Anthropic/Google Vertex/xAI 均有合同 ZDR 协议）；Enterprise 团队默认开启 Privacy Mode
3. **Cloud Agents**：唯一需要存储代码的功能，在隔离 VM 中运行，repo 加密副本在 Agent 完成后删除；如安全策略禁止代码存储可不启用 Cloud Agents

**Privacy Mode 强制执行**：Team Dashboard → Settings 启用，可防止成员关闭；结合 Allowed Team IDs MDM 策略阻止员工在企业设备上使用未开启 Privacy Mode 的个人账号。

**数据加密**：传输中 TLS 1.2+，静态 AES-256；企业客户可使用 CMEK（客户管理加密密钥）加密 Embeddings 和 Cloud Agent 数据，控制密钥轮换。

**合规合同**：GDPR 合规 DPA，所有子处理商均有 DPA；SOC 2 Type II 认证见 Trust Center。
