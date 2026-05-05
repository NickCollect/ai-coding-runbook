---
type: entity
name: User-profile
aliases: [user profiles / end-user profile / BetaManagedAgentsUserProfile]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

代表 end-user identity 的资源 —— 应用代用户调 API 时通过 `user_profile_id` 关联 Messages / managed agent 等请求。

## 关键属性

- **Beta header**：`user-profiles-2026-03-24`（+ `managed-agents-2026-04-01` 在 managed agent 场景） [[user_profiles-index--beta-api]]
- **Endpoints**：
  - `POST /v1/user_profiles` —— Create (optional `external_id`, `metadata`)
  - `GET /v1/user_profiles` —— List
  - `GET /v1/user_profiles/{id}` —— Retrieve
  - `POST /v1/user_profiles/{id}` —— Update (`external_id`, `metadata`)
  - `POST /v1/user_profiles/{id}/enrollment_url` —— Create Enrollment URL（返回 one-time URL 给 end-user enroll/link） [[user_profiles-index--beta-api]] [[user_profiles-create_enrollment_url--beta-api]]
- **使用方式**：在 [[Messages-API]] 或 [[Managed-agent]] session 调用时引用 `user_profile_id` 关联 end-user
- **Auth**：`X-Api-Key` + `anthropic-version: 2023-06-01` + beta header

## 出现来源

_13 summaries reference this entity_ ——
- [[user_profiles-index--beta-api]] / [[user_profiles-create--beta-api]] / [[user_profiles-list--beta-api]] / [[user_profiles-retrieve--beta-api]] / [[user_profiles-update--beta-api]] / [[user_profiles-create_enrollment_url--beta-api]]
- [[messages-create--beta-api]] / [[onboarding--ma]] / [[multi-agent--ma]]

## 相关

- [[Messages-API]] / [[Managed-agent]] —— 引用 `user_profile_id`
