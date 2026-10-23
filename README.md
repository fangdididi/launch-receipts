**English** | [简体中文](README.zh-CN.md)

# Launch Receipts

**Take what you built public without hype and without getting your post removed. An agent skill that backs every launch claim with a receipt, tests your project the way a stranger meets it, and writes one honest post per venue.**

You finished the thing. Now you have to tell people, and that is where most small projects stumble: the post says "blazing fast" and the first commenter measures it; the quick start breaks at step two on a clean machine; the same paragraph lands in five communities and reads like spam in all of them; a Show HN turns out to be a waitlist; the maker goes to lunch and twenty questions go unanswered.

Launch Receipts is an agent skill that walks you through a launch like an audit:

- **Ship card first.** One plain sentence of what it is, who it is for, the exact try path, and the *one* thing you want from this launch. Frozen before any post is written.
- **No receipt, no claim.** Every claim gets an id and a receipt a stranger can check: SHOWN, RUN, FILE, NUMBER or QUOTE. "As far as I know" (STATED) and "soon" (WISH) are not receipts; they move to the limits line.
- **Cold read and clean try path.** A fresh reader gets 30 seconds and five questions. Then someone follows the README literally on a clean machine with a stopwatch, and every hidden dependency, signup wall or missing key is logged.
- **Five doors, three verdicts.** TRYABLE, TRUE, SAFE, LEGIBLE, PRESENT. GO, SOFT (quiet share first) or HOLD. A HOLD is cheaper than a burned launch.
- **Venues by fit and by their real rules.** Show HN, Product Hunt, Reddit, X, Bluesky, Mastodon, Lobsters, newsletters, awesome lists, V2EX, Jike, community chats. Scored on audience, on-topic, ask match and standing, after reading today's rules.
- **One venue, one text.** Each post has a disclosure, a limits line and one specific ask, plus eight hard questions answered in advance.
- **Launch-day desk and day-7 afterword.** Every comment typed (BUG, CONFUSED, WISH, COMPARE, PRAISE, HOSTILE) and acted on; confusion goes into the README the same day; the afterword measures the ask, not the stars.
- **Never posts, never asks for votes.** The agent drafts. You post.

## Features

| | |
|---|---|
| Works for | open-source repos, CLIs, libraries, web apps, mobile apps, agent skills and plugins, side projects, major relaunches |
| Output | `launch/` folder: SHIPCARD, RECEIPTS, COLDREAD, GATE, VENUES, posts/, HARDQ, DESK, AFTERWORD |
| Receipt kinds | SHOWN, RUN, FILE, NUMBER, QUOTE (and the non-receipts STATED, WISH) |
| Gate | five doors, verdict GO / SOFT / HOLD |
| Venue cards | 12 venues in English and Chinese with typical rules, formats and removal reasons, plus a fit scoring sheet |
| Linter | `scripts/receipts.py`: flags unknown or weak receipts, vote requests, over-length text; warns on bare numbers, hype words (English and Chinese) and missing disclosure; counts X-weighted length; strips tags for the final text |
| Safety | fictional data in screenshots, secrets check before promotion, no sock puppets, no vote rings, no auto-posting |
| Bilingual | full English and Chinese skill files, venue cards and worked example |

## Installation

The skill is the folder containing `SKILL.md` (English) and `SKILL.zh-CN.md` (Chinese). Copy the whole folder so `scripts/`, `references/` and `examples/` come with it.

**Claude Code**

```bash
git clone https://github.com/fangdididi/launch-receipts.git ~/.claude/skills/launch-receipts
```

**Codex / agents that read `~/.agents/skills`**

```bash
git clone https://github.com/fangdididi/launch-receipts.git ~/.agents/skills/launch-receipts
```

**Cursor** (project skills folder)

```bash
git clone https://github.com/fangdididi/launch-receipts.git .cursor/skills/launch-receipts
```

**Any other agent** (Gemini CLI, GitHub Copilot, OpenCode, Windsurf, Cline, Kimi, chat apps): paste `SKILL.md` into its instructions or project rules, or ask it to install the skill from this repository URL. For Chinese conversations use `SKILL.zh-CN.md`. Without a shell you lose the linter, but every step works by hand.

## Usage

Open your project and ask in plain words:

```
I want to launch this repo. Use launch-receipts.
Write me a Show HN for this, but check every claim first.
My last launch got nothing. Run the cold read and tell me why.
Plan a Product Hunt and Reddit launch for our app next week.
用 launch-receipts 帮我准备这个开源项目的发布，V2EX 和即刻都要。
```

The agent will:

1. Read the project and fill in the ship card, then ask you for the one launch ask.
2. List every claim it is tempted to make and find or request a receipt for each.
3. Run the cold read and the clean try path, and propose README fixes.
4. Check the five doors and give GO, SOFT or HOLD with reasons.
5. Read each candidate venue's current rules, score fit, and propose a main venue and dates.
6. Write one post per venue, tagged with receipt ids, plus the hard-questions sheet.
7. On launch day, help you sort and answer comments in the desk log.
8. On day 7, write the afterword.

Linter commands:

```bash
python3 scripts/receipts.py venues                                  # known length limits
python3 scripts/receipts.py lint posts/show-hn.md --receipts RECEIPTS.md --venue long
python3 scripts/receipts.py lint posts/title.txt  --receipts RECEIPTS.md --venue hn-title
python3 scripts/receipts.py count posts/x.md --venue x              # X-weighted length
python3 scripts/receipts.py strip posts/x.md > x.final.txt          # remove [R#] tags
```

`lint` exits with code 1 when there are errors, so you can use it in a pre-launch checklist or CI.

## Example

`examples/tidemark/` is a complete launch kit for a fictional CLI that renames photos by capture date. The cold read caught a hidden dependency, the gate said HOLD, the fix took a day, then GO. It includes a Show HN title and text, an X post, a Chinese V2EX post, hard questions, a desk log and an afterword. Chinese overview: `examples/tidemark/LAUNCH.zh-CN.md`.

What the linter says about the deliberately bad draft:

```
$ python3 scripts/receipts.py lint examples/tidemark/posts/bad-draft.md --receipts examples/tidemark/RECEIPTS.md --venue long
ERROR line 1   WEAK-RECEIPT  [R3] is WISH, not a receipt (FILE, NUMBER, QUOTE, RUN, SHOWN)
WARN  line 3   BARE-NUMBER   number without a receipt: It saves you 90% of the time you spend organising photos.
ERROR line 5   NO-RECEIPT    [R12] is not in the receipts file
ERROR line 7   VOTE-ASK      asks for votes; ask for tries or feedback instead
WARN  draft    NO-DISCLOSURE nothing says you made this ('I built ...')
-- 3 error(s), 2 warning(s)
```

And the post that actually shipped:

```
Show HN: Tidemark - rename photos to their capture date, with preview and undo

I built Tidemark because my photo backups were 14 folders of IMG_4412.JPG ...
It reads the capture date and shows a dry-run table of old and new names before it touches anything [R2].
...
Limits: I have not tested it on Windows at all. ...
What would help most: run it on files from an unusual camera or phone and, if it fails, paste the error text.
```

## File structure

```
launch-receipts/
├── SKILL.md                      # the skill (English)
├── SKILL.zh-CN.md                # the skill (Chinese)
├── README.md / README.zh-CN.md
├── references/
│   ├── venues.md                 # venue cards + fit scoring sheet
│   └── venues.zh-CN.md
├── scripts/
│   └── receipts.py               # lint / count / strip / venues (stdlib only, read-only)
├── tests/
│   └── test_receipts.py          # python3 -m unittest discover -s tests
├── examples/tidemark/            # full fictional launch kit
│   ├── SHIPCARD.md  RECEIPTS.md  COLDREAD.md  GATE.md  VENUES.md
│   ├── HARDQ.md  DESK.md  AFTERWORD.md  LAUNCH.zh-CN.md
│   └── posts/  show-hn.title.txt  show-hn.md  x.md  v2ex.md  bad-draft.md
└── LICENSE
```

## Tips

- Write the limits line before the feature list.
- Show the product doing its job, not the landing page describing it.
- Read each venue's rules on the day you post; the venue cards are a starting point.
- Zero users is fine to admit. Fake traction is not.
- Stars and points are noise; count tries, bug reports and contributors against your one ask.

## License

MIT © fangdididi
