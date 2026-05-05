---
type: qa
topic: model-selection
created: 2026-05-05
sources:
  - 02_Wiki/Synthesis/model-selection-guide.md
  - 02_Wiki/Synthesis/context-window-pricing.md
  - 02_Wiki/Synthesis/multimodal-guide.md
  - 02_Wiki/Entities/Extended-thinking.md
---

# Model Selection Q&A

## Q: Claude Opus 4.7 vs Sonnet 4.6 — 实际使用建议？
**A:** 日常 coding 和企业工作流首选 **Sonnet 4.6**（$3/$15 per MTok，1M context beta，开发者 70% 偏好 Sonnet 4.6 > Sonnet 4.5）；仅在最难 coding 任务、复杂 agentic orchestration、高分辨率 vision 或需要 xhigh effort 时升级到 **Opus 4.7**（$5/$25 per MTok，CursorBench 70% vs Sonnet 4.6 58%）。注意 Opus 4.7 引入新 tokenizer，同等输入消耗约 1.0–1.35× token，迁移前需实测真实成本。
*来源：[[model-selection-guide]]*

---

## Q: 哪个模型最便宜？（截至 2026-05-05）
**A:** **Gemini 2.5 Flash-Lite** $0.10/$0.40 per MTok，是所有主流稳定版模型中最便宜。Gemini 2.5 Flash $0.30/$2.50 次之。Claude 内部最便宜是 Haiku 4.5（$1/$5），OpenAI 最便宜是 GPT-5.4 mini（$0.75/$4.50）。
*来源：[[context-window-pricing]]*

---

## Q: 需要 extended thinking 用哪个？
**A:** Claude 生态内：Opus 4.7（仅支持 adaptive thinking，无 `budget_tokens`）、Opus 4.6 / Sonnet 4.6（支持 adaptive 和 extended thinking，可设 `budget_tokens`）。Gemini：2.5 Flash / 2.5 Pro 通过 `thinking_config` 控制 thinking level，Gemini 3 系列同样支持。OpenAI：gpt-5.x 内置 reasoning effort 控制（none/low/medium/high/xhigh），但 reasoning tokens 不暴露给用户。
*来源：[[Extended-thinking]]、[[context-window-pricing]]、[[model-selection-guide]]*

---

## Q: 批量处理 100 万 token 推荐哪个？
**A:** 成本优先：**Gemini 2.5 Flash-Lite**（Batch 50% 后 $0.05/$0.20）最低；其次 **Claude Haiku 4.5 + Message Batches API**（50% 后 $0.50/$2.50）。若单文档超 200k tokens，Haiku 4.5 的 context window 可能不够（推测 200k，*需确认*），需改用 Sonnet 4.6（1M context，Batch 后 $1.50/$7.50）。
*来源：[[context-window-pricing]]、[[model-selection-guide]]*

---

## Q: GPT-5.5 vs GPT-5.4 定价差多少？
**A:** GPT-5.5：$5/$30 per MTok；GPT-5.4：$2.50/$15 per MTok。Input 贵 2×，output 贵 2×。两者 context window 相同（1,050,000 tokens）。超过 272k tokens 时两者均有长上下文溢价（input ×2、output ×1.5）。
*来源：[[context-window-pricing]]*

---

## Q: Gemini 2.5 Pro 的 context window 是多少？
**A:** **1,000,000 tokens（1M）**，与 Gemini 2.5 Flash 相同。定价分段：≤200K 时 $1.25/$10，>200K 时 $2.50/$15 per MTok。
*来源：[[context-window-pricing]]*

---

## Q: 哪个模型支持 video input？
**A:** 目前仅 **Gemini** 系列原生支持视频输入（MP4/MOV/AVI/WEBM/3GPP 等，最大 20GB，支持 YouTube URL 直链）。Claude 不支持视频输入，OpenAI 的视频输入能力在当前 wiki raw 文件中未记录（not documented）。
*来源：[[multimodal-guide]]*

---

## Q: OpenAI 的 o-series 和 GPT 系列区别？
**A:** 待确认（数据截至 2026-05-05）。当前 wiki raw 文件中，OpenAI 主力前沿模型为 gpt-5.5 / gpt-5.4 / gpt-5.4-mini；旧版 o3、o4-mini 已从主定价页移除。models--openai-docs.md 显示 gpt-5.x 全系列内置 reasoning effort 控制（none/low/medium/high/xhigh），传统 o-series 的独立身份已基本合并进 GPT 系列。o-series 与 GPT 系列的具体差异需核实 platform.openai.com 最新文档。
*来源：[[context-window-pricing]]、[[models--openai-docs]]*

---

## Q: Gemini Flash 和 Flash Thinking 区别？
**A:** Gemini API 没有独立的 "Flash Thinking" 模型。Thinking 是 **Gemini 2.5 Flash / Gemini 3 Flash** 内置的功能，通过 `thinking_config` 的 `thinking_level`（low/medium/high）控制。Thinking 关闭时为标准 Flash；开启后推理能力提升，latency 和成本随 budget 增加。Thinking tokens 按 output token 计费。
*来源：[[thinking--gemini-docs]]*

---

## Q: 多模态任务首选哪个厂商？
**A:** 覆盖最广选 **Gemini**：唯一原生支持音频（6 格式，25 token/秒）+ 视频（9 格式，1 fps 采样）+ 超长 PDF（1000 页）+ HEIC/HEIF 图像。**Claude** 擅长高分辨率图像（Opus 4.7，2576px）、PDF 引用（Citations API）和永久文件存储（Files API）。**OpenAI** 擅长图像生成与理解一体化（GPT Image 2 + vision），以及 computer-use 精确坐标（detail:original）。
*来源：[[multimodal-guide]]*
