[English](README.md) | **简体中文**

# Launch Receipts（发布凭据）

**把你做的东西公开发布，不吹牛，也不被删帖。这是一个 Agent 技能：为每一句发布宣传配上凭据，像陌生人第一次接触那样测试你的项目，并为每个渠道各写一篇诚实的帖子。**

东西做完了，接下来要告诉别人，而大多数小项目恰恰在这里摔跟头：帖子写着"极速"，第一个评论者就去实测；快速开始在干净机器上第二步就跑不通；同一段话发到五个社区，在哪儿看都像广告；一篇 Show HN 点进去却是等待名单；作者去吃午饭，二十个问题没人回。

Launch Receipts 像做审计一样带你走完一次发布：

- **先写发布卡。** 一句平实的话说明是什么、给谁用、准确的试用路径，以及这次发布你*唯一*想要的东西。写任何帖子之前先冻结。
- **没有凭据，就不许宣称。** 每条宣称都有编号和一张陌生人能核对的凭据：SHOWN、RUN、FILE、NUMBER 或 QUOTE。"据我所知"（STATED）和"快了"（WISH）不算凭据，它们只能进"局限"一行。
- **冷读与干净试用路径。** 让一个没见过项目的读者看 30 秒，回答五个问题。再让人在干净机器上严格照 README 操作并计时，记下每一个隐藏依赖、注册墙或缺失的 Key。
- **五道门，三种判定。** TRYABLE 可试、TRUE 属实、SAFE 安全、LEGIBLE 易懂、PRESENT 在场。判定 GO、SOFT（先小范围分享）或 HOLD。一次 HOLD 远比一次搞砸的发布便宜。
- **按匹配度和真实规则选渠道。** Show HN、Product Hunt、Reddit、X、Bluesky、Mastodon、Lobsters、Newsletter、Awesome 列表、V2EX、即刻、社群聊天。读完当天的规则后，按受众、切题、诉求匹配、身份四项打分。
- **一个渠道，一篇文字。** 每篇帖子都表明身份、带一行局限、只提一个具体请求，并提前写好八个尖锐问题的回答。
- **发布当天回复台和第 7 天复盘。** 每条评论分类（BUG、CONFUSED、WISH、COMPARE、PRAISE、HOSTILE）并跟进；大家看不懂的地方当天就改进 README；复盘衡量的是你的诉求，而不是 Star 数。
- **从不代发，从不拉票。** Agent 起草，你来发布。

## 功能一览

| | |
|---|---|
| 适用对象 | 开源仓库、命令行工具、库、网页应用、移动应用、Agent 技能和插件、业余项目、大版本重新发布 |
| 产出 | `launch/` 文件夹：SHIPCARD、RECEIPTS、COLDREAD、GATE、VENUES、posts/、HARDQ、DESK、AFTERWORD |
| 凭据类型 | SHOWN、RUN、FILE、NUMBER、QUOTE（以及不算凭据的 STATED、WISH） |
| 门禁 | 五道门，判定 GO / SOFT / HOLD |
| 渠道卡片 | 12 个渠道的中英文卡片：常见规则、格式、被删原因，附匹配度打分表 |
| 检查脚本 | `scripts/receipts.py`：对不存在或不够格的凭据、拉票语句、超长文本报错；对无凭据数字、中英文吹嘘词、未表明身份给出警告；按 X 规则计算加权长度；去掉标记生成最终文本 |
| 安全 | 截图用虚构数据、推广前检查密钥、不用马甲、不刷票、不自动发帖 |
| 双语 | 完整的中英文技能文件、渠道卡片和完整示例 |

## 安装

技能就是包含 `SKILL.md`（英文）和 `SKILL.zh-CN.md`（中文）的整个文件夹。请复制整个文件夹，让 `scripts/`、`references/` 和 `examples/` 一起带上。

**Claude Code**

```bash
git clone https://github.com/fangdididi/launch-receipts.git ~/.claude/skills/launch-receipts
```

**Codex / 读取 `~/.agents/skills` 的 Agent**

```bash
git clone https://github.com/fangdididi/launch-receipts.git ~/.agents/skills/launch-receipts
```

**Cursor**（项目技能目录）

```bash
git clone https://github.com/fangdididi/launch-receipts.git .cursor/skills/launch-receipts
```

**其他 Agent**（Gemini CLI、GitHub Copilot、OpenCode、Windsurf、Cline、Kimi、各类聊天应用）：把 `SKILL.zh-CN.md` 或 `SKILL.md` 粘贴进它的指令或项目规则，或者让它从本仓库地址安装。没有命令行环境时用不了检查脚本，但每一步都可以手工完成。

## 使用方法

打开你的项目，直接用自然语言说：

```
用 launch-receipts 帮我准备这个开源项目的发布，V2EX 和即刻都要。
帮我写一篇 Show HN，但每一句宣传都要先核对。
我上次发布没人理，帮我做一次冷读，看看问题在哪。
下周要在 Product Hunt 和 Reddit 发布我们的应用，帮我做计划。
I want to launch this repo. Use launch-receipts.
```

Agent 会：

1. 读项目、填好发布卡，然后问你这次发布的唯一诉求。
2. 列出它想写的每一条宣称，为每条找到或向你索取凭据。
3. 做冷读和干净环境试用路径测试，并提出 README 修改建议。
4. 检查五道门，给出 GO、SOFT 或 HOLD 及原因。
5. 读取每个候选渠道当前的规则，打分，建议主渠道和日期。
6. 每个渠道写一篇带凭据编号的帖子，外加尖锐问题清单。
7. 发布当天，帮你在回复台记录里分类并回复评论。
8. 第 7 天，写复盘。

检查脚本命令：

```bash
python3 scripts/receipts.py venues                                  # 已知的长度限制
python3 scripts/receipts.py lint posts/v2ex.md --receipts RECEIPTS.md --venue long
python3 scripts/receipts.py lint posts/title.txt --receipts RECEIPTS.md --venue hn-title
python3 scripts/receipts.py count posts/x.md --venue x              # X 加权长度（中文算 2）
python3 scripts/receipts.py strip posts/x.md > x.final.txt          # 去掉 [R#] 标记
```

`lint` 有错误时以退出码 1 结束，可以放进发布前检查清单或 CI。

## 示例

`examples/tidemark/` 是一个虚构命令行工具的完整发布包，它按拍摄日期重命名照片。冷读发现了一个隐藏依赖，门禁判定 HOLD，修了一天后变成 GO。里面有 Show HN 标题和正文、X 帖子、中文 V2EX 帖子、尖锐问题、回复台记录和复盘。中文概览见 `examples/tidemark/LAUNCH.zh-CN.md`。

检查脚本对故意写坏的草稿的输出：

```
$ python3 scripts/receipts.py lint examples/tidemark/posts/bad-draft.md --receipts examples/tidemark/RECEIPTS.md --venue long
ERROR line 1   WEAK-RECEIPT  [R3] is WISH, not a receipt (FILE, NUMBER, QUOTE, RUN, SHOWN)
WARN  line 3   BARE-NUMBER   number without a receipt: It saves you 90% of the time you spend organising photos.
ERROR line 5   NO-RECEIPT    [R12] is not in the receipts file
ERROR line 7   VOTE-ASK      asks for votes; ask for tries or feedback instead
WARN  draft    NO-DISCLOSURE nothing says you made this ('I built ...')
-- 3 error(s), 2 warning(s)
```

最终发出的中文帖（节选）：

```
[分享创造] Tidemark：按拍摄日期给照片改名的命令行小工具，先预览、可撤销

我做了一个小工具……动文件之前先列一张"旧名 → 新名"的预览表 [R2]。
……
局限：完全没在 Windows 上测过；能读哪些格式取决于 exiftool……
最想要的帮助：拿你手里比较少见的相机或手机的照片跑一下，如果报错，把错误原文贴在回复或 Issue 里。
```

## 文件结构

```
launch-receipts/
├── SKILL.md                      # 技能（英文）
├── SKILL.zh-CN.md                # 技能（中文）
├── README.md / README.zh-CN.md
├── references/
│   ├── venues.md                 # 渠道卡片 + 匹配度打分表
│   └── venues.zh-CN.md
├── scripts/
│   └── receipts.py               # lint / count / strip / venues（仅标准库，只读）
├── tests/
│   └── test_receipts.py          # python3 -m unittest discover -s tests
├── examples/tidemark/            # 完整的虚构发布包
│   ├── SHIPCARD.md  RECEIPTS.md  COLDREAD.md  GATE.md  VENUES.md
│   ├── HARDQ.md  DESK.md  AFTERWORD.md  LAUNCH.zh-CN.md
│   └── posts/  show-hn.title.txt  show-hn.md  x.md  v2ex.md  bad-draft.md
└── LICENSE
```

## 小贴士

- 先写局限，再写功能列表。
- 展示产品正在干活，而不是落地页在描述它。
- 发帖当天再读一遍渠道规则；渠道卡片只是起点。
- 承认零用户没关系，假装有热度才有关系。
- Star 和点赞是噪音；对照你的唯一诉求去数试用、Bug 报告和贡献者。

## 许可证

MIT © fangdididi
