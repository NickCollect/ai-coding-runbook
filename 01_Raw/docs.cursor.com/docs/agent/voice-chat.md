---
source_url: https://cursor.com/docs/agent/voice-chat
fetched_at: 2026-11-09T07:30:16.068918+00:00
fetch_method: mintlify_md
---

# Voice chat

Voice chat is a realtime spoken conversation with an agent. You talk, the agent talks back, and you can hand it coding work without typing. Voice chat works in the [Agents Window](https://cursor.com/docs/agent/agents-window.md), the IDE, on web, and in [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md).

Voice chat is separate from [dictation](https://cursor.com/docs/agent/prompting.md#voice-input). Dictation turns your speech into text in the chat input. Voice chat is a two-way conversation where the agent answers out loud.

## Start a voice chat

### Open an agent chat

In the Agents Window, open any chat, including a new one. In the IDE, open a chat with at least one message.

### Clear the chat input

When the agent is idle and the chat input is empty, a waveform button appears where **Send** usually is. While the agent runs, **Stop** takes that spot.

### Click Start voice chat

Click the waveform button, labeled **Start voice chat**. The microphone button next to it starts dictation instead.

### Allow microphone access

Allow microphone access if your computer, browser, or phone asks. The call connects. Start talking, or the agent will check in after a few seconds.

On iOS, you can also start a call with Siri. See [iOS](https://cursor.com/docs/agent/voice-chat.md#ios).

## How it works

Voice chat is speech-to-speech. You speak to a voice agent, and it replies in a natural voice while you keep the conversation going. When you ask for code changes, the voice agent hands the work to the coding agent in that chat and keeps talking with you while the work runs.

During a call, the voice agent can:

- **Hand off work.** Send a task or follow-up to the coding agent in the current chat.
- **Answer questions about your work.** Read diffs, runs, and agents to tell you what changed and what's still running. These lookups are read-only.
- **Search this agent's history.** Search earlier messages and calls with this agent.
- **Switch Project workers.** In a [Project](https://cursor.com/docs/agent/projects.md) with workers, move the call to a different worker.
- **Hang up.** End the call when you say you're done.

The coding agent decides what's worth saying. It speaks short progress notes while it works, a brief answer when it finishes, and an update when workers it started report back. If the coding agent doesn't write a spoken update for a turn, the call reads its written reply instead.

The call transcript appears in the chat. Cloud agent transcripts sync to your other devices while the call is live, unless Privacy Mode is on.

## Models

Voice chat runs on Grok Voice. Grok Voice handles listening and speaking. The coding agent in the chat keeps using the model you picked for it.

Pick your default voice in the **Voice** or **Agent Voice** settings. Voice chat offers many named voices, including Ara, Eve, Leo, Rex, and Sal.

You can also change the voice during a call. That choice sticks to the agent you're talking to. An agent with its own saved voice uses it instead of your default.

## Requirements

- **A supported surface.** Use the Agents Window, the IDE, web, or the Cursor iOS app.
- **A signed-in account.** Sign in to Cursor with your account. Sessions authenticated with an API key can't start voice chat.
- **Microphone permission.** Allow Cursor to use your microphone when your operating system or browser asks. If you denied it earlier, Cursor shows "Microphone blocked. Allow it in your system or browser settings." On iOS, it shows "Microphone blocked. Allow it in Settings." Turn microphone access back on there, then start the call again.

## iOS

[Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md) supports a few extras for calls on the go:

- **Siri.** Say "Hey Siri, call Cursor" to start a call with a new agent. Your iPhone needs to be unlocked.
- **Live Activity.** When iOS can't show the call on the system call screen, the call appears on the Lock Screen and in the Dynamic Island. Mute and hang up from the Lock Screen or the expanded Dynamic Island; the compact Dynamic Island doesn't show those controls.

## Call limits

- **Silence.** By default, a call hangs up after about 10 minutes of silence from you while the agent has no work in progress.
- **Daily limit.** There's a daily limit on voice calls. If you reach it, Cursor tells you when you can call again.

## Privacy

With [Privacy Mode](https://cursor.com/docs/enterprise/privacy-and-data-governance.md) on, voice chat runs with zero data retention.

## Voice chat and dictation

|                      | Voice chat                     | Dictation                                                                                                   |
| -------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Button               | Waveform, **Start voice chat** | Microphone: **Start voice input** in the Agents Window, **Voice Input** in the IDE, **Record voice** on iOS |
| What you get         | A spoken reply from the agent  | Text in the chat input                                                                                      |
| Who sends the prompt | The voice agent hands off work | You review and send                                                                                         |
| Shortcut             | None                           | Cmd Shift Space in the IDE. Hold Ctrl M to talk in the Agents Window.                                       |

Earlier releases called dictation Voice Mode. In the IDE, Cmd Shift Space still toggles dictation. See [Voice input](https://cursor.com/docs/agent/prompting.md#voice-input).

## FAQ

### Why don't I see the Start voice chat button?

The waveform button shows only when the agent is idle and the chat input is empty. Clear any text in the input, or wait for the agent to finish. In the IDE, the chat also needs at least one message.

The button is hidden in:

- Subagents and Project workers
- Archived chats
- Claude Code chats
- Chats owned by another teammate

In the IDE, it's also hidden for cloud agents that are still streaming and when dictation is turned off. If none of these apply, update Cursor.

### Why does my call fail with "Realtime voice requires sign-in"?

The **Start voice chat** button shows even when you're signed out or using an API key, but the call itself needs a signed-in Cursor account. Sign in to Cursor with your account, then start the call again.

### Can I keep working while I'm on a call?

Yes. The coding agent keeps running while you talk, and it speaks short updates when there's something to report.

### Does voice chat read every reply aloud?

Usually not. The coding agent chooses short spoken updates, and the full replies stay in the chat. When it doesn't write a spoken update for a turn, the call reads its written reply.

## Related

- [Voice chat changelog](/changelog/voice-chat)
- [Prompting agents](https://cursor.com/docs/agent/prompting.md)
- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
