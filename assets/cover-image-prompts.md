# 公众号封面图提示词模板

读这个文件的场景：用户要求做封面图、首图、题图、公众号头图、信息流配图，尤其是要“吸睛”“有设计感”“带标题”。

---

## 封面图目标

公众号封面图不是文章内配图。它只服务三个目标：

1. **信息流里能停住手指**：缩略图状态下标题和主体要清楚。
2. **一眼看懂文章气质**：AIGC 是理性、工具、反思、未来感；审美是质感、留白、判断力。
3. **和标题互相放大**：不要只做氛围图，封面必须帮助标题成立。

---

## 生成前先提取 5 个变量

从文章里提取：

```text
title: 文章标题，必须逐字准确
domain: AIGC / 审美 / 其他
emotion: 焦虑 / 顿悟 / 共鸣 / 爽感 / 反差
visual_metaphor: 核心视觉隐喻，例如镜子、窗口、坐标、手稿、分岔路
cover_role: 标题封面 / 无字封面 / 朋友圈分享图 / 视频号横封面
```

如果用户没有特别说明，默认：

```text
cover_role: 标题封面
ratio: 16:9 horizontal
style: premium editorial digital poster
background: bright or light neutral
text: include exact Chinese title
```

---

## AIGC 封面通用提示词

```text
Use case: ads-marketing
Asset type: WeChat official account cover image, 16:9 horizontal, high-resolution
Primary request: Generate a visually striking cover image for a Chinese WeChat article with the exact title text: “{{TITLE}}”
Scene/backdrop: {{VISUAL_METAPHOR}} expressed through a refined AI-era visual scene; thoughtful, premium, not corporate stock.
Style/medium: premium editorial digital poster, minimalist but eye-catching, refined technology magazine aesthetic, crisp typography, strong visual hierarchy.
Composition/framing: title is the main focus, large bold Chinese typography, readable at small mobile thumbnail size; visual motif supports the title without clutter; balanced negative space.
Color palette: warm white / soft gray background, deep charcoal text, cyan-green accent, a small amount of electric blue; high contrast and clean.
Text (verbatim): “{{TITLE}}”
Constraints: The Chinese title must be spelled exactly as provided, no extra words, no English subtitle, no logo, no watermark. Keep text sharp and legible.
Avoid: dark background, busy sci-fi interface, generic robot face, corporate handshake, smiling office people, excessive gradients, tiny unreadable text, misspelled Chinese characters.
```

---

## 审美封面通用提示词

```text
Use case: ads-marketing
Asset type: WeChat official account cover image, 16:9 horizontal, high-resolution
Primary request: Generate a visually refined cover image for a Chinese WeChat article with the exact title text: “{{TITLE}}”
Scene/backdrop: {{VISUAL_METAPHOR}} rendered as a quiet editorial still life or art-magazine composition.
Style/medium: premium editorial art direction, restrained, tactile, high taste, not commercial poster.
Composition/framing: clear first-viewport subject, generous negative space, title readable in mobile thumbnail.
Color palette: light neutral background, deep charcoal text, one restrained accent color.
Text (verbatim): “{{TITLE}}”
Constraints: Chinese title must be exact, no extra words, no logo, no watermark.
Avoid: overdecorated collage, stock-photo feeling, luxury cliches, excessive serif ornament, misspelled Chinese characters.
```

---

## 无字封面提示词

用于用户想自己在公众号后台加标题，或担心 AI 生成中文字不稳。

```text
Use case: ads-marketing
Asset type: WeChat official account cover image, 16:9 horizontal, high-resolution, no text
Primary request: Generate a cover image for a Chinese WeChat article titled “{{TITLE}}”, but do not render any text inside the image.
Scene/backdrop: {{VISUAL_METAPHOR}}
Style/medium: premium editorial digital poster, strong central metaphor, clean negative space reserved for title overlay.
Composition/framing: leave a clean title-safe area on the left third; subject on the right third; readable and striking as a small thumbnail.
Color palette: light neutral background, deep charcoal visual details, cyan-green accent.
Constraints: no text, no letters, no logos, no watermark.
Avoid: clutter, busy UI, stock-photo corporate people, dark background.
```

---

## 质量检查

- [ ] 标题是否逐字正确？
- [ ] 缩略图状态下是否还能看清标题？
- [ ] 主体和标题是否不互相抢？
- [ ] 是否符合文章情绪，而不是只是“好看”？
- [ ] 是否避免了机器人脸、握手、办公室人群等廉价 AI 视觉？
- [ ] 是否已保存到项目目录，而不是只留在生成器默认目录？
