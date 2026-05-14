# 公众号文章配图规范

读这个文件的场景：用户要求给公众号文章配图、做首图、把 HTML 占位图换成真实图片、生成可截图转发的图文视觉，或希望把配图流程沉淀到 skill。

---

## 输出目标

配图的目标不是“把页面填满”，而是提高完读率和转发率：

- 首图让信息流里的人一眼知道这篇文章的气质和主题
- 中段图帮助读者在滑动中重新进入文章
- 方法图 / 清单图承担收藏和截图转发
- 案例图提高可信度，避免文章只剩观点

默认视觉保持 `html-layout.md` 的冷峻代码风：白色底、窄版正文、少量冷色强调、强信息结构，不做营销海报、不做暖色卡片、不做无意义氛围图。配图也优先做浅色版本，避免复制到公众号编辑器后出现浅字看不清。

如果用户的目标是“直接复制到微信公众号编辑器”，优先把方法图、清单图、流程图做成**纯 HTML/CSS 信息图区块**，不要依赖本地 `<img src="...">`。本地图片、SVG、base64 图片在复制到公众号编辑器时都可能丢失或被过滤。

如果用户已经反馈 HTML/CSS 信息图区块复制后仍被公众号编辑器清洗，切换到 `.docx` 中转：把图形区块渲染成 PNG 并嵌入 Word 文档，让用户从 Word / WPS / Pages 全选复制到公众号编辑器。这个路径通常比浏览器 HTML 复制更稳定。

---

## 配图数量

按文章类型决定图片密度：

| 文章类型 | 建议图片 |
|---------|---------|
| AIGC 观点 / 行业观察 | 1 张首图 + 2-3 张解释图 |
| AIGC 工具测评 / 教程 | 1 张首图 + 3-5 张真实截图或步骤图 |
| AIGC 个人反思 | 1 张首图 + 1-2 张概念图 + 1 张清单图 |
| 审美拆解 | 1 张首图 + 5-8 张作品 / 细节 / 对比图 |
| 审美训练方法 | 1 张首图 + 3-5 张示例图 / 清单图 |

宁可少而准，不要为了“好看”堆图。每张图必须回答一个问题：这张图让读者更懂了什么？

---

## 图片类型

### 1. 首图

用途：信息流打开率 + 文章第一屏气质。

要求：
- 横图优先，推荐 16:9 或 4:3
- 标题或主题必须清楚，但文字不要超过 16 个字
- 缩略图状态下主体仍然看得清
- AIGC 方向优先使用工具界面、终端、工作流、对比结构
- 审美方向优先使用真实作品、摄影局部、构图对比

### 2. 解释图

用途：把抽象观点视觉化。

常用结构：
- 三步法：来源 / 上下文 / 反例
- 对照图：错误做法 vs 正确做法
- 流程图：输入 / 判断 / 输出 / 核查
- 坐标图：效率 / 判断力 / 风险 / 责任

### 3. 清单图

用途：收藏、转发、截图。

要求：
- 只放 3-7 条，避免密密麻麻
- 每条不超过 18 个中文字符
- 图片标题本身能独立传播
- 和正文结尾的行动建议绑定

### 4. 真实截图 / 来源图

用途：增强可信度。

要求：
- 工具测评、教程、案例文优先使用真实截图
- 涉及第三方数据、报告、论文时，图片说明写清来源
- 不要伪造产品界面、数据图、论文截图

---

## 本地资产规则

为每篇文章创建独立目录：

```text
article-assets/<article-slug>/
```

命名建议：

```text
cover-<topic>.svg
step-01-<topic>.svg
checklist-<topic>.svg
screenshot-<tool-name>.png
```

HTML 中使用相对路径：

```html
<figure class="article-image">
  <img src="article-assets/aigc-self/cover-aigc-self.svg" alt="一句准确描述图片内容的替代文本">
</figure>
<p class="caption">caption: 这张图解释什么，或来源是什么。</p>
```

不要把项目页面引用的图片留在临时目录、下载目录或 AI 工具默认生成目录。

如果要求复制到公众号编辑器，优先使用这种 HTML 信息图区块：

```html
<div class="html-visual" role="img" aria-label="来源、上下文、反例三步事实核查图">
  <div class="visual-label">// VERIFY BEFORE FORWARDING</div>
  <p class="visual-title">把“它说了”改成“我核过”</p>
  <div class="visual-grid three">
    <div class="visual-panel">
      <span class="visual-num">STEP 01</span>
      <p class="visual-panel-title">来源</p>
      <p class="visual-sub">找到原文、报告或官方页面</p>
    </div>
  </div>
</div>
```

---

## 什么时候用 AI 生成图，什么时候直接画 SVG

用 AI 生成图：
- 需要照片感、插画感、复杂场景、人物背影、质感封面
- 需要同一主题的多张风格化视觉
- 用户明确要“生成图片”“AI 配图”“封面图”

直接画 SVG / HTML 图：
- 流程图、清单图、对比图、终端风界面、方法论卡片
- 需要文字非常准确
- 需要可控、可离线、可继续编辑
- 需要复制到微信公众号编辑器时，优先用 HTML/CSS 信息图区块，而不是 SVG 文件

AIGC 类公众号默认优先使用 SVG/HTML 方法图，因为它们信息稳定、文字可控，和冷峻代码风更一致。

---

## 配图脚本

本 skill 提供一个无依赖脚本：

```bash
python scripts/illustrate_html.py --html wechat-article.html --plan > image-plan.json
```

它会扫描 HTML 里的 `.media-slot` 占位框，输出一个可编辑的 JSON 配图计划。

填好图片路径后执行：

```bash
python scripts/illustrate_html.py --html wechat-article.html --config image-plan.json --apply
```

脚本会：
- 自动补齐 `.article-image` CSS
- 把 `.media-slot` 替换为 `<figure><img></figure>`
- 保留或替换 caption
- 可选插入首图

如果文章已经没有 `.media-slot`，也可以手动插入 `<figure class="article-image">`。脚本用于批量稳定处理，不强制每次都用。

---

## AI 生成图提示词骨架

如果用户要的是公众号后台封面图、首图、题图，优先读取 `assets/cover-image-prompts.md`。下面的骨架适合文章内图或简单首图，正式封面图要更强调缩略图识别度和标题准确性。

适合首图 / 封面草稿：

```text
Use case: productivity-visual
Asset type: WeChat article cover image, 16:9
Primary request: 为一篇题为《拥抱AI前先拥抱自己》的 AIGC 反思文章生成首图
Scene/backdrop: dark minimalist workspace, AI interface reflected in a mirror, self-check notes beside a laptop
Style/medium: refined editorial digital illustration, code-inspired, restrained
Composition/framing: centered composition, clear subject, readable at thumbnail size
Color palette: white or very light background, cool cyan-green accent, muted blue-gray
Text: no embedded text unless the user explicitly asks
Avoid: busy stock-photo look, smiling corporate people, warm marketing palette, fake logos, watermarks
```

适合方法图：

```text
Use case: infographic-diagram
Asset type: WeChat article in-body explainer graphic, 16:9
Primary request: 把“来源 / 上下文 / 反例”三步事实核查法做成冷峻代码风信息图
Style/medium: vector-like infographic, terminal UI, minimal lines
Composition/framing: three columns, each column one keyword and one short explanation
Color palette: white or very light background, cyan-green accent, dark gray text
Text: 来源, 上下文, 反例
Avoid: decorative illustrations, crowded text, emoji, gradients, fake app logos
```

---

## 交付前检查

- [ ] 首图是否能在缩略图状态下看清主题？
- [ ] 每张图是否服务一个明确论点？
- [ ] 如果要直接复制到公众号，是否避免了外部 `<img>` 依赖？
- [ ] 如果使用图片文件，图片路径是否为项目内相对路径？
- [ ] `alt` 是否准确描述图片内容？
- [ ] `caption` 是否说明图的用途或来源？
- [ ] 真实截图和数据图是否没有伪造来源？
- [ ] HTML 没有遗留 `IMAGE SLOT`、`TODO` 或模板说明？
- [ ] 移动端图片是否不溢出正文宽度？
