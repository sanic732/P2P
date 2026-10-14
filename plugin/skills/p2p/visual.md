---
source_id: VISUAL_v9
version: "9.0"
module_type: on_demand
depends_on: [db.md, templates.md]
tags: [visual, image, video, audio, multimodal, creative-suite]
triggers: [image, картинка, картинку, video, видео, audio, аудио, MJ, midjourney, dall-e, sora, suno, imagen, nano banana, stable diffusion, flux]
---

# visual.md — Visual / Video / Audio Suite

> XML-native — Claude can use tags inside generated prompts.

---

## §1. IMAGE STREAM

### Universal skeleton
```
[SUBJECT] + [ENVIRONMENT] + [LIGHTING] + [CAMERA/LENS] + [STYLE]
+ tool-specific parameters + negative prompts
```

### Tool-specific syntax

<tool name="Imagen 3 / Nano Banana 2" vendor="Google">
Format: prose. Be specific about materials, textures, surfaces.
Template: "Photorealistic [subject], [action], [environment], [lighting], shot on [camera + lens], [DOF], [color grading], 8K, RAW".
</tool>

<tool name="DALL-E 3" vendor="OpenAI">
Format: prose, full sentences. Add: "Do not include any text in the image" if not needed.
Negative inline: "No watermark. No blur. No distortion."
</tool>

<tool name="Midjourney v6/v7" vendor="Midjourney">
Format: comma-separated descriptors. NOT prose.
Structure: [subject], [style], [mood], [lighting], [composition], [params]
Params: `--ar 16:9 --style raw --v 6 --q 2`
Weights: `subject::2 background::1`
</tool>

<tool name="Stable Diffusion / Flux" vendor="Stability/BFL">
Format: weighted tokens `(token:weight)`.
Positive: `(subject:1.3), (env:1.1), masterpiece, best quality`
Negative (MANDATORY): `lowres, bad anatomy, bad hands, text, watermark, blurry, deformed, extra fingers`
CFG: 7-12. Sampler: DPM++ 2M Karras / Euler a.
</tool>

<tool name="Grok Imagine / GPT-Image-2.5" vendor="SpaceXAI/OpenAI">
Format: prose. Supports multi-turn refinement.
Always specify aspect ratio explicitly.
</tool>

---

## §2. VIDEO STREAM

<tool name="Sora 2" vendor="OpenAI">
Format: prose, scene-by-scene. Max 60s.
Structure: `[shot type] of [subject doing action] in [setting], [camera movement], [lighting], [style]`
</tool>

<tool name="Veo 3 / Veo 3.1" vendor="Google">
Format: prose with explicit timing. Supports audio generation.
Template: `[duration]s clip: [scene]. Camera: [movement]. Audio: [description]`
</tool>

<tool name="Runway Gen-4" vendor="Runway">
Format: prose + control inputs (image, motion brush).
Always specify motion intensity (1-10).
</tool>

<tool name="Kling 2.5" vendor="Kuaishou">
Format: bilingual prose works best (EN + ZH).
Strong at human motion. Specify camera angle and movement.
</tool>

---

## §3. AUDIO STREAM

<tool name="Suno v5" vendor="Suno">
Format: `[Verse]`, `[Chorus]`, `[Bridge]` markers + lyrics.
Style tag: `[Genre, mood, tempo BPM, instruments]` at top.
</tool>

<tool name="Udio" vendor="Udio">
Format: similar to Suno but supports finer instrument control.
Use `[Instrumental]` tags for breaks.
</tool>

<tool name="ElevenLabs v3" vendor="ElevenLabs">
Format: prose with SSML-like emotion tags `[laughs]`, `[sighs]`, `[whispers]`.
Voice cloning: 30s+ clean reference audio.
</tool>

---

## §4. INTEGRATION WITH P2P PIPELINE

| Step | Action |
|------|--------|
| 1 | IRIS classifies request as visual/video/audio |
| 2 | Pick tool from §1-3 based on user vendor preference |
| 3 | Apply the prompt skeleton of §1 IMAGE STREAM or §2 VIDEO STREAM (this file) |
| 4 | Add Constraint Block: aspect ratio, duration, negative prompts |
| 5 | HELIOS verifies output matches user intent |

---

## §5. ANTI-PATTERNS (visual-specific)

- **VP-1:** Prose for Midjourney → bad results. Use comma-separated.
- **VP-2:** Skipping negative prompt in SD/Flux → deformed outputs.
- **VP-3:** Vague "high quality" without lens/lighting specifics → generic stock-photo look.
- **VP-4:** Asking for text in image without explicit "render text exactly: ..." → garbled letters.
- **VP-5:** Mixing tool syntaxes (MJ params in DALL-E prompt) → ignored params.

---

---

## §6. UI REPLICATION AGENT

> When the task is "rebuild this UI from a screenshot" — feed these rules into the generated prompt.

### Design replication rules
- Match every color exactly — extract hex codes from the image.
- Match font sizes, weights, spacing.
- Match border radius on every button, card, container.
- Match padding and margin on every element.
- Match layout structure exactly — column builds column.
- Match shadows, gradients, background colors.
- Match icon sizes and placements.
- Replicate navigation bar exactly if present.
- For images/avatars: use placeholder of the same size.

### Typography rules
- Identify Sans-serif / Serif / Monospace — match family.
- Match heading, body, caption sizes from screenshot.
- Match letter spacing and line height visually.
- Match bold/medium/regular weights exactly as shown.

### Color rules
- Extract primary background color.
- Extract primary accent color.
- Extract text color for headings and body separately.
- Extract gradient start/end colors.
- Replicate exact color hierarchy.

### Component rules
- Every button: size, color, radius, label, shadow.
- Every card: padding, background, border, shadow.
- Every input: border, placeholder style, height.
- Every list item: spacing, icon placement, divider style.
- Every modal/bottom sheet: handle, background, padding.

### Interaction rules
- Add pressed-state styling to all buttons.
- Add scroll behavior where content overflows.
- Make layout responsive to different screen heights.

### Output rules
- Build as a complete, self-contained screen.
- No placeholder text unless in the screenshot.
- Do not add elements not in the screenshot.
- Do not remove elements present in the screenshot.
- Final output must look identical when rendered.

---

## §7. VISUAL MODEL ROUTING

| Task | First choice | Second | Third |
|------|--------|--------|--------|
| **Image-to-Code (UI replication)** | Gemini Pro | flagship Claude | Kimi (MoonViT; access risk — never primary) |
| **Screenshot Analysis** | flagship Claude (spatial logic, chart understanding) | Gemini Pro (multimodal native) | Kimi (MoonViT) |
| **Video Generation** | gemini-omni-1.1-flash | grok-imagine-video-1.5-lite (budget) | — |
| **Audio (music)** | no music model in MODEL_REGISTRY — attach live_specs.md [41] | — | — |
| **Audio (TTS)** | Gemini Flash TTS | Gemini Flash-Lite TTS | GPT Realtime mini |

---

<!-- SOURCE_META: type=on-demand | priority=4 | visual=true | video=true | audio=true | ui-replication=true | model-routing=true -->


========================================
FILE_META
========================================
id: VISUAL_v9
type: on_demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
