---
source_id: VISUAL_V8C
version: 8.4.7-C
module_type: on_demand
depends_on: [!!db_v8C.md, !templates.md]
tags: [visual, image, video, audio, multimodal, creative-suite]
triggers: [image, картинка, картинку, video, видео, audio, аудио, MJ, midjourney, dall-e, sora, suno, imagen, nano banana, stable diffusion, flux]
---

# !visual.md — Visual / Video / Audio Suite (v8C.3)

> Перенос из v7C.2 `!visual_suite.md`. Replaces menu item 14 CREATIVE SUITE.
> XML-native — Claude может использовать теги внутри генерируемых промптов.

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

<tool name="Grok Imagine / GPT-Image-1" vendor="xAI/OpenAI">
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
| 3 | Apply Template I (Image) or Template V (Video) from !templates.md |
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

## §6. UI REPLICATION AGENT (port from v7C.2)

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

## §7. VISUAL MODEL ROUTING (port from v7C.2)

| Task | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| **Image-to-Code (UI replication)** | Kimi K2.5 (MoonViT-3D, OCRBench 92.3%) | GLM-4.6V (image→code, PDF/UI reverse) | Qwen3-VL (OCR 99.2%), Gemini 3.1 Pro |
| **Screenshot Analysis** | Claude Opus 4.7 (spatial logic, chart understanding) | Gemini 3.1 Pro (multimodal native) | Kimi K2.5 (MoonViT-3D) |
| **Video Generation** | Veo 3.1 (highest quality, native audio) | Sora 2 (continuity) | Runway Gen-4 (style transfer) / Kling 2.5 (human motion) |
| **Audio (music)** | Suno v5 / Udio | — | — |
| **Audio (TTS)** | ElevenLabs v3 | — | — |

---

<!-- SOURCE_META: type=on-demand | priority=4 | visual=true | video=true | audio=true | ui-replication=true | model-routing=true | ported-from=v7C.2 -->


========================================
FILE_META
========================================
id: VISUAL_V8C
type: on_demand
edition: CLAUDE_NATIVE
invariants_passed: [I1_yaml, I2_api_strings, I3_deadlines, I4_g_errors, I5_version_metadata, I6_xml_native, I7_agents_8]
========================================
