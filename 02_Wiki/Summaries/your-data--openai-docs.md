---
type: summary
source: 01_Raw/docs.openai.com/docs/guides/your-data.md
source_url: https://platform.openai.com/docs/guides/your-data
title: "OpenAI — 数据控制与隐私"
summarized_at: 2026-05-05
entities_referenced: [Prompt-caching]
concepts_referenced: []
---

## 核心要点

OpenAI API 数据保留、零数据保留（ZDR）、数据驻留（Data Residency）及企业密钥管理（EKM）的完整说明。

### 核心原则

**自 2023 年 3 月 1 日起**：API 数据不用于训练模型（除非用户明确同意）。

### 数据存储类型

- **滥用监控日志**：用于执行使用政策，默认保留 30 天
- **应用状态**：部分 API 功能需要持久化数据以完成任务

### 三种数据控制选项

| 选项 | 说明 |
|---|---|
| **Modified Abuse Monitoring** | 从滥用监控日志中排除 customer content |
| **Zero Data Retention (ZDR)** | 同上 + `/v1/responses` 和 `/v1/chat/completions` 的 `store` 参数始终被视为 `false` |
| **Safety Retention** | 特定客户的 gpt-5.5/gpt-5.5-pro 可能保留检测为潜在违规的内容 |

ZDR 和 Modified Abuse Monitoring 需提前申请并获得 OpenAI 批准。

### 关键端点数据保留

- `/v1/responses`：默认 30 天；ZDR 下 `store` 始终为 false
- `/v1/conversations`：无 30 天 TTL，保留至删除
- `/v1/assistants`、`/v1/threads`：删除后 30 天彻底清除；未删除则永久保留
- `/v1/embeddings`、`/v1/audio`、`/v1/moderations`：ZDR 完全兼容

### 数据驻留（Data Residency）

可配置 OpenAI 基础设施的地理位置。支持地区：
- **美国**（US）：支持区域处理
- **欧洲**（EEA + 瑞士）：支持区域处理，需 ZDR/MAM
- 澳大利亚、加拿大、日本、印度、新加坡、韩国、英国、阿联酋：仅区域存储

数据驻留：`gpt-5.5`/`gpt-5.5-pro`/`gpt-5.4`/`gpt-5.4-pro` 加价 10%。

### 企业密钥管理（EKM）

使用外部 KMS（AWS KMS、GCP、Azure Key Vault）对 OpenAI 上的 customer content 加密。
