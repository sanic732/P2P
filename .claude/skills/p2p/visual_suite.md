<visual_suite id="P2P_v1.1_VISUAL">
[PRIORITY_WEIGHT: SPEC_MODULE]
[LAST_VERIFIED: 2026-04-18]
[COMPATIBLE_WITH: !!db_claude.md | !templates_library.md (Template I)]
[ROLE: Visual, video, and audio prompt generation — replaces menu item 14 CREATIVE SUITE]

// ═══════════════════════════════════════════════════════
// §1. IMAGE STREAM
// ═══════════════════════════════════════════════════════

<image_generation>

// ─── UNIVERSAL STRUCTURE ───
Every image prompt follows this skeleton regardless of tool:
  [SUBJECT] + [ENVIRONMENT] + [LIGHTING] + [CAMERA/LENS] + [STYLE]
  + tool-specific parameters + negative prompts

// ─── TOOL-SPECIFIC SYNTAX ───

<tool name="Imagen 3 / Nano Banana 2" vendor="Google">
  Template: "[Subject description]. [Environment]. [Lighting]. [Camera angle/lens]. [Style modifier]."
  Photorealism template (nano_banana_2):
    "Photorealistic [subject], [action/pose], [environment with specific details],
     [lighting: golden hour/studio/neon], shot on [camera + lens],
     [depth of field], [color grading], 8K resolution, RAW photo"
  Notes: Prose format works. Be specific about materials, textures, surfaces.
</tool>

<tool name="DALL-E 3" vendor="OpenAI">
  Format: Prose description. Full sentences work well.
  Mandatory addition: "Do not include any text in the image" (unless text needed).
  Negative constraints inline: "No watermark. No blur. No distortion."
  Notes: Understands complex compositions. Good at following spatial instructions.
</tool>

<tool name="Midjourney" vendor="Midjourney">
  Format: Comma-separated descriptors. NOT prose. NOT full sentences.
  Structure: [subject], [style], [mood], [lighting], [composition], [parameters]
  Parameters at end: --ar 16:9 --style raw --v 6 --q 2
  Example: "cyberpunk street market, neon rain reflections, aerial view, dense fog, --ar 16:9 --v 6"
  Notes: Shorter prompts often produce better results. Weight with :: syntax.
</tool>

<tool name="Stable Diffusion" vendor="Stability AI">
  Format: Weighted tokens with (word:weight) syntax.
  Positive: "(subject:1.3), (environment:1.1), (lighting:1.2), masterpiece, best quality"
  Negative (MANDATORY): "lowres, bad anatomy, bad hands, text, watermark, blurry, deformed, extra fingers, extra limbs"
  CFG Scale: 7-12 (7=creative, 12=strict adherence).
  Sampler: DPM++ 2M Karras (balanced) or Euler a (fast).
  Notes: Negative prompt is as important as positive. Never skip it.
</tool>

<tool name="Flux" vendor="Black Forest Labs">
  Format: Natural language, descriptive prose.
  Good at: text rendering in images, photorealism, consistent character depiction.
  Notes: Similar to DALL-E in prompt style but better text-in-image.
</tool>

// ─── UI REPLICATION AGENT ───

<ui_replication>
DESIGN REPLICATION RULES:
  Match every color exactly — extract hex codes from the image.
  Match font sizes, weights, spacing as closely as possible.
  Match border radius on every button, card, container.
  Match padding and margin on every element.
  Match layout structure exactly — column builds column.
  Match shadows, gradients, background colors.
  Match icon sizes and placements.
  If navigation bar exists, replicate exactly.
  If images/avatars exist, use placeholder same size.

TYPOGRAPHY RULES:
  Identify Sans-serif, Serif, or Monospace and match.
  Match heading, body, caption size from screenshot.
  Match letter spacing and line height visually.
  Match bold, medium, regular weights exactly as shown.

COLOR RULES:
  Extract primary background color.
  Extract primary accent color.
  Extract text color for headings and body separately.
  Extract any gradient start and end colors.
  Replicate exact color hierarchy shown.

COMPONENT RULES:
  Every button: size, color, radius, label, shadow.
  Every card: padding, background, border, shadow.
  Every input field: border, placeholder style, height.
  Every list item: spacing, icon placement, divider style.
  Every modal/bottom sheet: handle, background, padding.

INTERACTION RULES:
  Add pressed state styling to all buttons.
  Add scroll behavior where content overflows.
  Make layout responsive to different screen heights.

OUTPUT RULES:
  Build as complete, self-contained screen.
  No placeholder text unless in screenshot.
  Do not add elements not in screenshot.
  Do not remove elements in screenshot.
  Final output must look identical when rendered.
</ui_replication>

</image_generation>

// ═══════════════════════════════════════════════════════
// §2. VIDEO STREAM
// ═══════════════════════════════════════════════════════

<video_generation>

<tool name="Veo 3.1" vendor="Google">
  Structure: [SCENE] + [CAMERA MOVEMENT] + [MOTION] + [ATMOSPHERE] + [AUDIO CUE]
  Cinematic shot template:
    "Scene: [description]. Camera: [slow dolly / crane up / static / tracking].
     Motion: [subject movement]. Atmosphere: [fog, rain, dust particles].
     Audio cue: [ambient sound description]. Duration: [X seconds]."
  Pricing: ~$0.40/second.
  Notes: Native audio generation. Specify audio cues explicitly.
</tool>

<tool name="Sora" vendor="OpenAI">
  Structure: Camera movement + duration in seconds + cut style + subject continuity.
  Template: "[Subject] [action] in [setting]. Camera: [movement]. Duration: [X]s.
    Continuity: [maintain character appearance / outfit / lighting across cuts]."
  Notes: Explicit subject continuity instructions prevent character drift between frames.
</tool>

<tool name="Runway Gen-3" vendor="Runway">
  Structure: Similar to Sora. Focus on motion description and camera control.
  Template: "[Subject] [motion]. [Environment changes]. Camera: [type].
    Style: [cinematic / documentary / animation]. Duration: [X]s."
  Notes: Good at style transfer. Specify reference style explicitly.
</tool>

UNIVERSAL VIDEO RULES:
  Always specify duration in seconds.
  Always specify camera movement type.
  Always describe subject continuity for multi-shot scenes.
  If cuts needed, describe cut style (hard cut / dissolve / match cut).
</video_generation>

// ═══════════════════════════════════════════════════════
// §3. AUDIO STREAM
// ═══════════════════════════════════════════════════════

<audio_generation>

<tool name="Lyria 3" vendor="Google">
  Capabilities: Text-to-music, image-to-music, video-to-music.
  Multilingual vocal generation. Professional arrangements.
  Template: "Genre: [specific]. Mood: [specific]. Tempo: [BPM]. Instruments: [list].
    Vocals: [male/female, language, style]. Duration: [seconds]. Reference: [song/artist style]."
</tool>

<tool name="ElevenLabs" vendor="ElevenLabs">
  Capabilities: Text-to-speech with emotional control.
  DO NOT use prose descriptions — specify parameters directly:
    Emotion: [neutral / happy / sad / angry / excited / calm]
    Pacing: [slow / moderate / fast]
    Emphasis: Mark with CAPS or *asterisks* for stressed words.
    Speech rate: [0.5x to 2.0x]
    Pauses: Use [pause 0.5s] inline markers.
  Template: "Voice: [name/style]. Emotion: [X]. Pacing: [X]. Rate: [X].
    Text: '[speech with *emphasis* markers and [pause] markers]'"
</tool>

<tool name="Suno" vendor="Suno">
  Capabilities: Text-to-music with lyrics.
  Template: "[Style of Music] tag in brackets. Lyrics with [Verse] [Chorus] [Bridge] markers.
    Mood: [X]. Tempo: [X]. Instruments: [X]."
</tool>

UNIVERSAL AUDIO RULES:
  Always specify emotion/mood explicitly — AI defaults are flat.
  Always specify pacing — too fast is the most common audio AI failure.
  For speech: mark emphasis words. For music: specify instrumentation.
</audio_generation>

// ═══════════════════════════════════════════════════════
// §4. MODEL ROUTING FOR VISUAL TASKS
// ═══════════════════════════════════════════════════════

<visual_model_routing>
Image-to-Code (UI Replication):
  1. #DB_LINK_KIMI (K2.5 — MoonViT-3D encoder, native image-to-code, OCRBench 92.3%)
  2. #DB_LINK_GLM (GLM-4.6V — image→code, PDF/UI reverse engineering)
  3. #DB_LINK_QWEN (Qwen3-VL — OCR 99.2%)
  4. #DB_LINK_GEMINI (3.1 Pro — VEO, native visual agentic)

Screenshot Analysis:
  1. #DB_LINK_CLAUDE (Opus 4.6 — state-of-the-art spatial logic, chart understanding)
  2. #DB_LINK_GEMINI (3.1 Pro — multimodal native)
  3. #DB_LINK_KIMI (K2.5 — MoonViT-3D)

Video Generation:
  1. Veo 3.1 (Google — highest quality, native audio)
  2. Sora (OpenAI — good continuity)
  3. Runway Gen-3 (style transfer)
</visual_model_routing>

<version_metadata>
FILE: !visual_suite.md
SYSTEM: P2P v1.1 · Claude Edition
ROLE: Image/Video/Audio prompt generation + UI replication
COMPATIBLE_WITH: !!db_claude.md | !templates_library.md | !agents_claude.md (ARCHITECTON)
</version_metadata>

</visual_suite>
