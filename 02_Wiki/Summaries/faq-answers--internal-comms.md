---
type: summary
source: 01_Raw/github/anthropics/skills/skills/internal-comms/examples/faq-answers.md
title: "FAQ Answers (internal-comms skill example)"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Example prompt template from the `internal-comms` skill — for an assistant that summarizes/answers questions across a company.

**Goal**: find big company-wide confusion sources + give summarized answers. Examples: recent corporate events (fundraising, exec changes), upcoming launches, hiring progress, vision/focus shifts.

**Tool sources**:
- **Slack**: questions in posts with many responses, questions with reactions/thumbs-up showing support
- **Email**: emails with FAQs written directly
- **Documents**: Google Drive docs, calendar event linked docs (direct or inferred)

**Output format**:
- *Question*: [insert question - 1 sentence]
- *Answer*: [insert answer - 1-2 sentences]

**Guidelines**:
- Be holistic — capture entire company, not just user/team
- Base answers on official company communications when possible
- Indicate uncertainty clearly
- Link to authoritative sources (docs, announcements, emails)
- Professional but approachable tone
- Flag if question requires executive input or official response
