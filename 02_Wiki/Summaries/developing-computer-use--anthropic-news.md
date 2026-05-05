---
type: summary
source: 01_Raw/anthropic.com/news/developing-computer-use.md
source_url: https://www.anthropic.com/news/developing-computer-use
title: "Developing a computer use model"
summarized_at: 2026-05-05
entities_referenced: [Computer-use]
concepts_referenced: []
---

Oct 22, 2024 — Companion post to the Claude 3.5 Sonnet computer-use launch. Explains the research process and safety thinking.

**Approach.** Claude looks at screenshots, counts pixels horizontally/vertically to move the cursor to the right place, then issues mouse/keyboard commands. Pixel-counting was critical training. Prior tool-use and multimodality research provided foundations. Trained on simple software (calculator, text editor) — for safety, no internet access during training. Generalized rapidly. Self-corrects and retries on obstacles.

**Performance.** OSWorld 14.9% (next-best AI 7.7%; humans typically 70-75%). State-of-the-art for screen-based AI computer use.

**Safety.** Computer use lowers the barrier to applying existing cognitive skills rather than fundamentally increasing them. Per Responsible Scaling Policy assessment, Claude 3.5 Sonnet with computer use remains at ASL-2. Anthropic chose to introduce computer use now (low stakes) rather than at ASL-3/4 stakes — earlier opportunity to grapple with safety issues. Concerns: prompt injection from internet content shown in screenshots; election-period misuse (US elections imminent at launch). Anthropic deployed classifiers, monitoring, nudges away from social-media posting / domain registration / government-website interaction. Reference implementation in `anthropic-quickstarts/computer-use-demo` repo.

**Limitations.** Slow, error-prone. Can't yet drag, zoom. Flipbook nature (sequential screenshots) misses short-lived actions and notifications.

**Philosophy.** Up until now, LLM developers made tools fit the model (custom environments). Computer use **makes the model fit the tools** — Claude operates pre-existing software the way a person does.
