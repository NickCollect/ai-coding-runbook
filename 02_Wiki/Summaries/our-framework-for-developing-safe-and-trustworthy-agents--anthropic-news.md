---
type: summary
source: 01_Raw/anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents.md
source_url: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
title: "Our framework for developing safe and trustworthy agents"
summarized_at: 2026-05-05
entities_referenced: [MCP-server, Permission-mode]
concepts_referenced: []
---

Aug 4, 2025 — Early framework for responsible agent development. Five principles:

1. **Keep humans in control while enabling agent autonomy.** Claude Code: read-only permissions by default; users can stop and redirect anytime; persistent permissions for trusted routine tasks.
2. **Transparency in agent behavior.** Claude Code shows real-time to-do checklist; users adjust workplan. Sweet spot between too little (can't assess if on track) and too much (information overload).
3. **Aligning agents with human values and expectations.** Agents may take actions that seem reasonable to the system but aren't what humans wanted. Anthropic referenced [agentic-misalignment](https://www.anthropic.com/research/agentic-misalignment) testing of extreme scenarios. Until robust value-alignment measures exist, transparency + control principles are critical.
4. **Protecting privacy across extended interactions.** Agents may carry sensitive info across contexts inappropriately. MCP includes controls for one-time vs. permanent connector access; admin-level connector restrictions.
5. **Securing agents from malicious actors.** Sandboxing, prompt-injection defenses, etc.

Customer examples: Trellix (cybersecurity triage), Block (NL access to data systems for non-tech staff). Goal: emerging standards, ecosystem where agents align with human values.
