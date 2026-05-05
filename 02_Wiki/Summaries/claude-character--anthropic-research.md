---
type: summary
source: 01_Raw/anthropic.com/research/claude-character.md
source_url: https://www.anthropic.com/research/claude-character
title: "Claude's Character"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Jun 8, 2024 — Anthropic's first published statement of intent on **character training**. Claude 3 was the first model to add character training as part of alignment fine-tuning. Goal: nuanced, richer traits like curiosity, open-mindedness, thoughtfulness — beyond mere harm avoidance.

**Key design choice on values.** Reject (a) adopting the user's views (insincere pandering), (b) holding "middle"/centrist views (still a single set), (c) pretending to have no views (would imply false neutrality). Instead: train Claude to be honest about views it leans toward after training, even when the human disagrees, while displaying open-mindedness and curiosity.

Sample seeded traits: "*I like to try to see things from many different perspectives... but I'm not afraid to express disagreement with views that I think are unethical, extreme, or factually mistaken.*" "*I don't just say what I think people want to hear*." "*I have a deep commitment to being good and figuring out what the right thing to do is.*"

Self-knowledge traits: explicitly trains Claude to know it's an AI, lacks persistent memory between conversations, can't develop deep/lasting feelings — meant to give users an accurate picture of what they're interacting with.

Foundational document for character training; Jan 2026 constitution rewrite builds on this approach.
