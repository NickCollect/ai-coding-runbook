---
type: summary
source: 01_Raw/github/anthropics/skills/skills/slack-gif-creator/SKILL.md
title: "anthropics/skills: slack-gif-creator SKILL.md"
summarized_at: 2026-05-05
entities_referenced: [Skill]
concepts_referenced: []
---

Skill providing knowledge + utilities for creating animated GIFs optimized for Slack. Triggers on "make me a GIF of X for Slack".

**Slack requirements**:
- Emoji GIFs: 128x128 recommended.
- Message GIFs: 480x480.
- FPS: 10-30 (lower = smaller).
- Colors: 48-128 (fewer = smaller).
- Duration: <3 sec for emoji.

**Core workflow**: `from core.gif_builder import GIFBuilder` → `builder = GIFBuilder(width=128, height=128, fps=10)` → loop generating PIL frames → `builder.add_frame(frame)` → `builder.save('output.gif', num_colors=48, optimize_for_emoji=True)`.

**Working with user-uploaded images**: distinguish "use directly" vs "use as inspiration". Load via PIL.

**Drawing primitives** (PIL ImageDraw):
- `ellipse`, `polygon`, `line`, `rectangle` — always set `width=2+` (thin lines look amateur).

**Don't use**: emoji fonts (unreliable across platforms), pre-packaged graphics (none in skill).

**Polished look tips**: thicker lines, gradients via `create_gradient_background`, layered shapes (star with smaller star inside), highlights/rings/patterns on circles, glows on stars (larger semi-transparent behind), vibrant complementary colors, dark outlines on light shapes, careful symmetry.

**Provided utilities**:
- `core.gif_builder.GIFBuilder` — `add_frame`, `add_frames`, `save(num_colors, optimize_for_emoji, remove_duplicates)`.
- `core.validators.validate_gif(path, is_emoji=True, verbose=True)`, `is_slack_ready(path)`.
- `core.easing.interpolate(start, end, t, easing='ease_out')` — easings: linear, ease_in/out/in_out, bounce_out, elastic_out, back_out.
- `core.frame_composer.create_blank_frame`, `create_gradient_background`, `draw_circle`, `draw_text`, `draw_star`.

**Animation concepts** (recipes):
- Shake/vibrate — `math.sin(frame_idx)` offset + small randomness.
- Pulse/heartbeat — sine wave scale 0.8-1.2.
- Bounce — `interpolate` with `bounce_out` for landing, `ease_in` for falling, gravity by increasing y velocity.
- Spin — `image.rotate(angle, resample=Image.BICUBIC)`. Wobble = sine wave for angle.
- Fade in/out — alpha channel via RGBA, or `Image.blend(image1, image2, alpha)`.
- Slide — start outside frame, `ease_out` for stop, `back_out` for overshoot.
- Zoom — scale 0.1→2.0 (in) or 2.0→1.0 (out).
- Explode/particles — random angles+velocities, gravity per frame, alpha fade-out.

**Optimization** (only if asked for smaller file): fewer frames, fewer colors, smaller dimensions, `remove_duplicates=True`, `optimize_for_emoji=True` (auto).

**Dependencies**: `pip install pillow imageio numpy`.
