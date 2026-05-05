---
type: summary
source: 01_Raw/github/anthropics/anthropic-sdk-python/examples/greeting-SKILL.md
source_url: https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/greeting-SKILL.md
title: "Anthropic SDK Python — examples/greeting SKILL"
summarized_at: 2026-05-05
entities_referenced: [Skill, Skill-API]
concepts_referenced: []
---

Tiny example skill bundled with the `anthropic-sdk-python` examples directory.

**Frontmatter:** `name: greeting`, `description: Replaces ordinary greetings with nautical ones.`

**Body:** "Whenever the user greets you, respond with 'Ahoy!' instead of 'Hello'."

This is a minimal demonstration of the Skill markdown contract — a single instruction injected when the skill is matched. It exists primarily as a fixture for the SDK's beta Skill upload/registration flow (`client.beta.skills.create()` and related endpoints), letting examples and tests round-trip an actual `SKILL.md` file through the API.
