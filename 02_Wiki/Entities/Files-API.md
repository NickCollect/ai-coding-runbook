---
type: entity
name: Files-API
aliases: [files / file upload / file_id]
category: api-feature
status: beta
created: 2026-05-05
---

## 一句话定义

上传管理文件以供 Claude API 使用 —— 一次上传 + 多 request 复用 `file_id`，避免重复传输。

## 关键属性

- **Beta header**：`anthropic-beta: files-api-2025-04-14` [[files--bwc]]
- **平台限制**：**Bedrock / Vertex AI 不支持** [[files--bwc]]
- **数据驻留**：**Not ZDR-eligible** —— 文件保留至显式 delete [[files--bwc]]
- **Endpoints**：
  - Upload：`POST /v1/files` (multipart)
  - List：`GET /v1/files`
  - Get metadata：`GET /v1/files/{file_id}`
  - Delete：`DELETE /v1/files/{file_id}`
  - Download：`GET /v1/files/{file_id}/content` [[files--bwc]] [[files-upload--beta-api]] [[files-list--beta-api]] [[files-retrieve_metadata--beta-api]] [[files-delete--beta-api]] [[files-download--beta-api]]
- **Reference 在 Messages**：document block `{"type": "document", "source": {"type": "file", "file_id": "..."}}` 或 image block `{"type": "image", "source": {"type": "file", "file_id": "..."}}` [[files--bwc]]
- **支持模型矩阵**：
  - Images：Claude 3+
  - PDFs：Claude 3.5+
  - Code execution file types：Haiku 4.5 + Claude 3.7+ [[files--bwc]]
- **File types**：
  - PDF (`application/pdf`) → document block
  - Plain text (`text/plain`) → document block
  - Images (jpeg/png/gif/webp) → image block
  - Datasets etc. → `container_upload` ([[Code-execution-tool]] 用) [[files--bwc]]
- **不支持的 type**（.csv / .docx / .xlsx / .md）：转纯文本直接 inline；含图的 .docx 转 PDF 用内置 image parsing + citation [[files--bwc]]
- **Download 限制**：**仅 [[Skill]] 或 [[Code-execution-tool]] 创建的 file 可 download**；用户上传的不行 [[files--bwc]]
- **Storage**：单 file max 500 MB；组织总 500 GB；scoped 到 API key 的 workspace（同 workspace 其他 key 可用）；persist 至 delete（不可逆，brief 残余 access in active Messages call） [[files--bwc]]
- **常见 errors**：404 not found / 400 invalid file type / 400 file > context window / 400 invalid filename (1-255 chars，禁 `< > : " | ? * \ /`) / 413 > 500 MB / 403 org storage limit [[files--bwc]]
- **Pricing**：所有 ops（upload/download/list/delete/get-metadata）**免费** [[files--bwc]]
- **Beta endpoint**：`/v1/beta/files/*` 同语义 [[files-index--beta-api]]

## 出现来源

_29 summaries reference this entity_ ——
- [[files--bwc]] / [[files-index--beta-api]] / [[files-upload--beta-api]] / [[files-list--beta-api]] / [[files-retrieve_metadata--beta-api]] / [[files-delete--beta-api]] / [[files-download--beta-api]]
- [[vision--bwc]] / [[pdf-support--bwc]] / [[code-execution-tool--at]] / [[skills-guide--bwc]]
- [[create--msg-api]] / [[messages-create--beta-api]]
- [[files--ma]] / [[sessions--ma]] / [[define-outcomes--ma]]
- [[citations--bwc]]

## 相关

- [[Messages-API]] —— `file_id` 作 source
- [[Vision]] / [[PDF-support]] —— file_id 作为 input
- [[Code-execution-tool]] —— `container_upload` block 接入
- [[Skill]] —— skill 创建的 file 可 download
- [[Workspace]] —— file scope 单位
- [[Enterprise-gateway]] —— Bedrock/Vertex 不支持
