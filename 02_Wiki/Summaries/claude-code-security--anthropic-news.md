---
type: summary
source: 01_Raw/anthropic.com/news/claude-code-security.md
source_url: https://www.anthropic.com/news/claude-code-security
title: "Making frontier cybersecurity capabilities available to defenders"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Feb 20, 2026 — **Claude Code Security** launched as limited research preview, built into Claude Code on the web. Scans codebases for security vulnerabilities and suggests targeted patches for human review. Available to Enterprise and Team customers; expedited free access for open-source maintainers.

**How it works.** Unlike rule-based static analysis (matches known patterns — exposed passwords, outdated encryption), Claude Code Security reads and reasons about code like a human researcher: understands component interactions, traces data flow, catches business-logic flaws and broken access control. Multi-stage verification: Claude re-examines each finding, attempts to prove/disprove it, filters false positives, assigns severity + confidence ratings. Findings appear in dashboard for analyst review; patches require human approval.

**Track record.** Built on a year of Frontier Red Team cybersecurity work — competitive Capture-the-Flag events, Pacific Northwest National Laboratory critical-infrastructure-defense partnership. Using Opus 4.6, the team **found over 500 vulnerabilities in production open-source codebases** that had gone undetected for decades. Triage and responsible disclosure underway with maintainers.

**Framing.** Same capabilities help attackers — release to defenders is intentional defensive parity. AI is expected to scan a significant share of the world's code soon. Apply at claude.com/contact-sales/security.
