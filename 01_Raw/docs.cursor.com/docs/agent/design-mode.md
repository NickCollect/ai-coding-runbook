---
source_url: https://cursor.com/docs/agent/design-mode
fetched_at: 2026-11-02T07:00:21.150087+00:00
fetch_method: mintlify_md
---

# Design Mode

Design Mode lets you direct agents by leaving notes on your running app. Open the browser in the [Agents Window](https://cursor.com/docs/agent/agents-window.md), click **Annotate**, and point at what you want changed: an element, an area, or text on the page. Cursor sends each note to the agent with the context it needs, and the agent edits the code while you move on to the next change.

UI work tends to be spatial. Instead of describing a change in a sentence, you point at it. Each note includes the details of what you picked and a screenshot, so the agent can find the right code.

Click an element in the running app, prompt against that selected element, and let the agent edit the code.

## Open Design Mode

Design Mode lives in the browser inside the Agents Window. Click **Annotate** in the browser toolbar, or focus the browser and press Cmd + Shift + D. The command palette lists the same action as **Toggle Design Mode**.

Until you open Design Mode for the first time, the **Annotate** button shows a **Try Annotate** preview with a short demo. After you've left more than five notes, the button shows only its icon.

A hint row along the top of the page shows the gestures for each step. To exit, click the exit button in the hint row, press the shortcut again, or press Esc. Esc first cancels a markup stroke, a text edit, or an open note, and exits once nothing else is open.

Annotate is available in Cursor 3.24.18 or later. Earlier versions show a pen icon labeled **Design Mode** in the browser toolbar instead.

## Ways to direct the agent

Each note starts with something you pick on the page.

### Select an element

Click any element to select it and open a note, then type the change. Before you click, press Arrow Up or Arrow Down to move the highlight to the element's parent or child.

### Select multiple elements

Hold Shift and click more elements to add them to the same note. Multi-select helps when the change depends on a relationship between elements. Reference two components and ask the agent to make one match the other, remove repeated content, or adjust a group together.

Select multiple elements and describe how they should change together.

### Mark an area

Drag across the page to box in an area, then describe the change. Hold Shift to lock the drag to one axis, or Option to draw the box from its center.

While you mark an area, the hint row shows the markup tools **Draw**, **Ellipse**, **Rectangle**, and **Arrow**. Circle a crowded section or point at the part that needs work. Press Cmd + Z to undo markup.

### Edit text in place

Double-click a text element to edit its text on the page. Press Return to save the edit or Esc to revert it. Text edits always wait for [Send](https://cursor.com/docs/agent/design-mode.md#send-notes).

### Edit CSS properties

On a note for a single element, click **Edit CSS properties** to open a CSS inspector for that element. Filter the list to find a property and change its value. Cursor sends your CSS edits with the note.

### Dictate a note

Speak a note instead of typing it. Once a note has text or CSS edits, it shows a **Dictate** button. Click it, or hold it while you talk.

Use voice input and drawing together to describe a change.

## Send notes

The **Batch edits** switch in the note card controls whether each note goes to the agent on its own. It starts off.

- **Batch edits off.** Press Return in an element or area note to send it to the agent right away. The button reads **Send note**.
- **Batch edits on.** Notes collect on the page as numbered pins, and a **Send** button with a count replaces **Annotate** in the browser toolbar. One click sends every pending note as one message.

Text edits always wait for **Send**, whichever way the switch is set. Open the list next to **Send** to review pending notes, or remove them all with **Clear All**. Sending every pending note also exits Design Mode. If you exit with notes still pending, **Send** stays in the toolbar until you send or clear them.

Press Cmd + L in a note or a text edit to put its content in the chat input instead of sending it or holding it for **Send**.

Hold Option and click an element to add it straight to the chat input without opening a note. With a note open, Option + click adds the element to that note.

## Keyboard shortcuts

| Action                                    | Shortcut               |
| :---------------------------------------- | :--------------------- |
| Toggle Design Mode                        | Cmd + Shift + D        |
| Add elements to a note                    | Shift + click          |
| Highlight the parent or child element     | Arrow Up or Arrow Down |
| Mark an area                              | Drag                   |
| Edit text on the page                     | Double-click           |
| Send or save a note                       | Return                 |
| Add a note or text edit to the chat input | Cmd + L                |
| Add an element to the chat input          | Option + click         |
| Undo markup                               | Cmd + Z                |
| Cancel the current step or exit           | Esc                    |

## What the agent sees

Each note you send gives the agent your text and two kinds of context:

- **Element details.** For each picked element, the agent gets the tag, id, classes, attributes, a CSS-style selector path, the first 200 characters of visible text, and the element's size and position. It also gets six computed styles: color, background color, font size, font family, display, and position. In React, Vue, and Svelte apps, the details include the component name and component stack, so the agent can find the source.
- **A screenshot.** Cursor crops the screenshot to the element, or to the area with your markup drawn on it, when you save the note.

## Canvas tabs

[Canvas](https://cursor.com/docs/agent/tools/canvas.md) tabs keep the older pen-icon **Design Mode** toggle. There, notes go straight to the chat, **Batch edits** doesn't apply, and in-place text editing isn't available. Drag to draw freehand, or hold Shift and drag to draw a box.

## Work in flow

When you refine an interface, one edit usually leads to the next. You adjust a component, notice the spacing around it, then see how another component should match.

Design Mode lets you send those edits as you notice them. Point at one element, describe the change, move to another part of the page, and send another note before the first one finishes. Cursor handles a note sent while the agent works like any [follow-up you type](https://cursor.com/docs/agent/overview.md#queued-messages). To collect a round of notes and send them together, turn on **Batch edits**. If your dev server hot reloads, the changes appear in the running app as the agent finishes.

This flow works best with a fast model that is strong at interface work. We recommend [Composer 2.5](/blog/composer-2-5).

## Related

- [Agents Window](https://cursor.com/docs/agent/agents-window.md)
- [Browser](https://cursor.com/docs/agent/tools/browser.md)


---

## Sitemap

[Overview of all docs pages](/llms.txt)
