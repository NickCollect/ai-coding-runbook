---
type: summary
source: 01_Raw/code.claude.com/docs/en/voice-dictation.md
source_url: https://code.claude.com/docs/en/voice-dictation
title: "Voice dictation"
summarized_at: 2026-05-05
entities_referenced: [Native-interface, Settings, IDE-integration]
concepts_referenced: []
---

Voice dictation in Claude Code CLI: speak prompts, stream-transcribed live into prompt input, mix with typing. Enable via `/voice`. Hold mode (push-to-talk, default) or tap mode.

**Requirements**:
- v2.1.69+ (tap mode v2.1.116+).
- Audio streamed to Anthropic servers (not local).
- **Claude.ai account only** — NOT available with API key, Bedrock, Vertex, Foundry.
- Doesn't consume messages/tokens, doesn't count toward `/usage` limits.
- Local microphone access required — doesn't work in Claude Code on the web or SSH. WSL needs WSLg (WSL2 on Win 11). Linux: built-in native module → fallback to `arecord` (ALSA utils) or `rec` (SoX).
- VS Code extension also supports it but NOT in VS Code Remote (SSH/Dev Containers/Codespaces).

**Enable**: `/voice`, `/voice hold`, `/voice tap`, `/voice off`. First enable triggers macOS mic permission prompt. Persist via settings:
```json
{ "voice": { "enabled": true, "mode": "tap" } }
```

**Hold mode**: hold `Space` → warmup ("keep holding…") → live waveform → release to finalize. Warmup detects via key-repeat events; first 1-2 chars typed are auto-removed when recording activates. Single Space tap still types space (no rapid repeat). Transcript inserted at cursor position. Can mix dictation + typing. `"autoSubmit": true` sends prompt on release if ≥3 words.

**Tap mode**: single tap to start, second tap to send. No warmup. First tap only starts recording when input empty. Auto-submits when transcript ≥3 words. Stops on 15s silence or 2 min total.

Recognition tuned for coding vocabulary (regex, OAuth, JSON, localhost). Project name + git branch added as recognition hints.

**Languages** (uses same `language` setting as Claude responses; defaults to English; VS Code extension also reads VS Code's `accessibility.voice.speechLanguage`):

Czech, Danish, Dutch, English, French, German, Greek, Hindi, Indonesian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Turkish, Ukrainian. Set via BCP 47 code or name in `/config` or settings.

**Rebind**: `voice:pushToTalk` in `Chat` context, default `Space`. Set in `~/.claude/keybindings.json`. Hold mode: avoid bare letter (key-repeat issue); use modifier combos like `meta+k` (no warmup). Tap mode: any key works.

**Troubleshoot**:
- `Voice mode requires a Claude.ai account` → API key/third-party detected. `/login` to use Claude.ai.
- macOS terminal not in Mic settings → `tccutil reset Microphone <bundle-id>` (e.g., `com.apple.Terminal`, `com.googlecode.iterm2`), Cmd+Q terminal, relaunch, `/voice` again.
- Linux `No audio recording tool found` → install SoX.
- Hold mode doesn't trigger → key-repeat may be OS-disabled; switch to tap mode.
- Tap mode types space instead of recording → input not empty; clear first.
