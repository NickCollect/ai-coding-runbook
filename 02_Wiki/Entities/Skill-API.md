---
type: entity
name: Skill-API
aliases: [skills (API) / skill versions / managed agent skill management]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

Managed Agent 的 remote skill 管理 API —— `/v1/skills`，让 client upload / list / version 自定义 skill 给 agent 用（**与本地 [[Skill]] 区分**）。

## 关键属性

- **Beta headers**：`anthropic-beta: skills-2025-10-02` + `managed-agents-2026-04-01`（如果用在 managed agent 上下文） [[skills-index--beta-api]]
- **Skill endpoints**：
  - `POST /v1/skills` —— Create（返回 `id` / `display_title` / `latest_version` / `source` / `type` / `created_at` / `updated_at`）
  - `GET /v1/skills` —— List
  - `GET /v1/skills/{skill_id}` —— Retrieve
  - `DELETE /v1/skills/{skill_id}` —— Delete（返回 `{id, type}`） [[skills-index--beta-api]]
- **Versions sub-resource**：
  - `POST /v1/skills/{id}/versions` —— Create new version（返回 `id` / `skill_id` / `version` / `name` / `description` / `directory` / `type` / `created_at`）
  - `GET /v1/skills/{id}/versions` —— List
  - `GET /v1/skills/{id}/versions/{version}` —— Retrieve
  - `DELETE /v1/skills/{id}/versions/{version}` —— Delete [[skills-versions-index--beta-api]]
- **Pin to agent**：[[Managed-agent]] 创建/更新时通过 `skills[].version` 字段 pin 特定 skill 版本 [[agents-index--beta-api]]
- **vs 本地 [[Skill]]**：
  - **[[Skill]]** —— Claude Code / plugin 本地 SKILL.md artifact
  - **Skill-API** —— Anthropic API beta resource，server-managed，用于 [[Managed-agent]]
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + 双 beta header

## 出现来源

_28 summaries reference this entity_ ——
- [[skills-index--beta-api]] / [[skills-create--beta-api]] / [[skills-list--beta-api]] / [[skills-retrieve--beta-api]] / [[skills-delete--beta-api]]
- [[skills-versions-index--beta-api]] / [[skills-versions-create--beta-api]] / [[skills-versions-list--beta-api]] / [[skills-versions-retrieve--beta-api]] / [[skills-versions-delete--beta-api]]
- [[skills--ma]] / [[skills-guide--bwc]] / [[agents-index--beta-api]] / [[agents-create--beta-api]] / [[onboarding--ma]] / [[agent-setup--ma]]

## 相关

- [[Skill]] —— 本地 skill artifact（不同 product）
- [[Managed-agent]] —— pin skill version 进 agent 配置
- [[MCP-server]] —— 平行的 capability 接入方式
