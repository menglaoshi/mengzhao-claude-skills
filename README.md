# 微信公众号爆款内容创作 Skill

梦钊的公众号内容创作 skill。

适用于 **OpenAI Codex / Claude Code / 其他支持 markdown skill 的 AI agent 工具**。

这个 skill 专注两个垂直领域：

- **AIGC 学习**
- **审美想象力提升**

它覆盖从选题、标题、开头、正文、HTML 排版、配图、封面图，到公众号编辑器中转交付的一整套流程。

---

## 它能帮你做什么

| 你说什么 | Skill 会做什么 |
|---------|---------------|
| "帮我想这周的选题" | 自动按"五维选题挖掘法"做网页研究，给出 8-15 个打分排序好的选题候选 |
| "写一篇关于 X 的爆款文" | 先给 8 个标题，再给 2 个开头，再给完整正文，并自检 |
| "帮我改改这篇" | 按打开率/完读率/转发率精准诊断问题，针对性改 |
| "为什么这篇没流量" | 用"复盘四问"框架给出诊断和下周方向 |
| "帮我做 AIGC 教程" | 自动切换到 AIGC 领域的语言风味和读者画像 |
| "拆解一下 [艺术家]" | 自动切换到审美领域，启用结构 D（拆解爆款型） |
| "写完后做成 HTML" | 输出白底、冷峻程序员代码风的单文件 HTML |
| "帮我配图" | 生成文章内信息图、清单图、截图位或本地配图资产 |
| "复制到公众号丢图怎么办" | 生成 `.docx` 中转版，方便从 Word/WPS 复制到公众号编辑器 |
| "帮我做封面图" | 生成带标题或无字版公众号封面图提示词，并保存项目资产 |

---

## 文件结构

```
wechat-viral-content/
├── README.md                          ← 你现在看的这个
├── SKILL.md                           ← Skill 主入口（agent 从这里开始）
├── agents/
│   └── openai.yaml                     ← OpenAI/Codex 展示元信息
├── references/
│   ├── platform-mechanics.md          ← 2025-2026 公众号算法机制 + 复盘框架
│   ├── topic-research.md              ← 选题方法论 + 网页浏览研究流程
│   ├── writing-craft.md               ← 行文工艺总规范
│   ├── domain-aigc.md                 ← AIGC 领域：读者/语言/选题/范本
│   ├── domain-aesthetic.md            ← 审美领域：读者/语言/选题/风格
│   ├── image-layout.md                ← 配图、封面图、DOCX 中转规范
│   └── html-layout.md                 ← 白底代码风 HTML 排版规范
├── assets/
│   ├── title-formulas.md              ← 10+ 标题公式 + 打分流程
│   ├── article-templates.md           ← 5 种文章结构模板
│   ├── cover-image-prompts.md         ← 公众号封面图提示词模板
│   └── template.html                  ← 单文件 HTML 模板
├── scripts/
│   └── illustrate_html.py             ← HTML 图片占位替换辅助脚本
```

本地项目文件夹中可额外保留 `wechat-viral-content.zip` 作为分享安装包；GitHub 仓库默认只发布源码与说明。

---

## 在 Claude Code 中使用

### 方式 1：放到项目目录

```bash
# 把整个文件夹放到你的工作目录
cd ~/your-wechat-project
# 把 wechat-viral-content/ 文件夹放进来
```

之后跟 Claude Code 对话时，它会自动注意到 `SKILL.md` 文件。或者你也可以在对话开始时手动告诉它：

> 请读取 `./wechat-viral-content/SKILL.md` 并按它的指引帮我工作。

### 方式 2：放到全局 Skills 目录（推荐）

```bash
# macOS / Linux 示例
mkdir -p ~/.codex/skills/
cp -r wechat-viral-content ~/.codex/skills/

# 之后在任何对话里直接说"用 wechat-viral-content skill 帮我写一篇 AIGC 文章"
```

---

## 在 OpenAI Codex CLI 中使用

Codex CLI 同样支持读取本地 markdown 文件作为上下文：

```bash
cd ~/your-wechat-project
# 确保 wechat-viral-content/ 在当前目录

# 启动 codex 时把 SKILL.md 加入上下文
codex
```

在对话中告诉它：

> 请读取 `./wechat-viral-content/SKILL.md` 并按它的指引帮我工作。从现在开始所有公众号相关任务都参考这个 skill。

Codex 会按 `SKILL.md` 里的"何时加载哪个引用文件"指引，按需读取 `references/` 和 `assets/` 下的具体文件。

---

## 典型对话示例

### 例 1：想本周选题

> 你：帮我想本周的选题，AIGC 方向，重点是工具测评和副业变现。
> 
> Agent：[读取 SKILL.md 和 references/domain-aigc.md] 我来按五维选题挖掘法去研究 → [开始 web_search 抖音/小红书/X/Hacker News 等] → [输出 12 个打分排序的候选] → 我推荐先做 Top 3，你想从哪个开始？

### 例 2：直接写文章

> 你：写一篇关于"普通人怎么用 Claude 做副业"的爆款文。
> 
> Agent：[读取相关文件] 先给你 8 个标题方向 → [输出标题] → 选第 3 个？好，开头我写 2 个版本 → [输出开头] → 选 A？开始写正文，用结构 A（故事引子型）→ [完整正文] → Pre-Flight Checklist 自检通过。

### 例 3：改稿子

> 你：[贴文章] 这篇阅读 3000 但转发不到 1%，怎么改？
> 
> Agent：[读取 platform-mechanics.md 和 writing-craft.md] 诊断：你的完读率应该不错，但缺社交货币和结尾金句。具体三个改法：①重写结尾 ②加入一段身份共鸣段落 ③把第 4 段那个论点单独成段并加粗 → [给出具体改稿]

### 例 4：输出 HTML

> 你：把这篇文章做成冷峻的程序员代码风 HTML。
>
> Agent：[读取 html-layout.md 和 template.html] 整理标题、导语、章节、图位和金句 → 生成一个白底、简约、无 JS 的单文件 HTML。

### 例 5：公众号编辑器中转

> 你：从 HTML 复制到公众号编辑器图片丢了，有没有别的通路？
>
> Agent：[读取 image-layout.md] 判断是公众号编辑器清洗 HTML → 生成 `.docx` 中转版 → 把信息图渲染成 PNG 嵌入 Word → 你从 Word/WPS 全选复制到公众号编辑器。

### 例 6：封面图

> 你：帮我生成一张带标题的公众号封面图，要吸睛。
>
> Agent：[读取 cover-image-prompts.md] 提取标题、领域、情绪、视觉隐喻 → 调用图像生成 → 保存到 `article-assets/<slug>/cover-title-<slug>.png`。

---

## 自定义建议

这个 skill 是基于通用方法论 + 两个领域的画像写的。**用 1-2 个月后，你应该回来更新它**：

1. **更新 `references/domain-aigc.md` 和 `references/domain-aesthetic.md` 里的"信息源头清单"**：把你实际用得最顺手的源头加进去
2. **沉淀你自己的"高分篇结构"**：把你账号上数据最好的 3-5 篇的结构提炼出来，加进 `assets/article-templates.md`
3. **维护你的"标题数据库"**：每篇文章发完后，把"标题 + 打开率"记录到 `assets/title-formulas.md` 末尾，时间长了形成你专属的标题命中率库
4. **维护你的"封面图风格"**：把高点击封面图的提示词沉淀到 `assets/cover-image-prompts.md`

---

## 反馈循环

每写完一篇文章并发布后，建议：

1. 24 小时后回来告诉 agent："这篇文章数据：阅读 X，完读率 Y%，转发率 Z%。"
2. Agent 会按"复盘四问"框架分析问题
3. 把分析结果作为下一篇的方向输入

跑 4-6 周后，你会形成一个 **数据驱动的内容生产飞轮**，而不是凭感觉发文。

---

## 注意事项

- **Skill 不是替代你的判断力**——它是放大器。最终的内容判断、立场表达、对真实读者的理解，必须是你自己的
- **不要被方法论框死**——所有规则都有例外。如果你的直觉强烈反对某个建议，相信直觉
- **保持垂直**——这个 skill 是为"AIGC + 审美"两个方向调优的。如果某天你想写完全无关的领域（如美食、母婴），需要新建一个 domain 文件，不要硬套
- **不要把生成示例当成标准答案**——示例文章、封面图、DOCX 只是交付通路演示，真正发布前仍然要按你的账号调性微调
