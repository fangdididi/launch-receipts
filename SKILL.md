---
name: launch-receipts
description: Take something you built (a repo, app, CLI, library, agent skill, site) public without hype and without getting removed. Freezes a ship card with one launch ask, inventories every claim against a receipt (something a stranger can see, run, open or count), runs a cold-read and a clean-machine try-path test, gates the launch GO / SOFT / HOLD, picks venues by fit and their actual rules (Show HN, Product Hunt, Reddit, X, Bluesky, V2EX, Jike, newsletters, awesome lists), writes a separate post per venue with a limits line and pre-answered hard questions, then runs a launch-day reply desk and a day-7 afterword. Never posts, never asks for votes. Use when someone says "help me launch this", "write a Show HN", "how do I announce my project", "prepare a Product Hunt launch", or "nobody noticed my repo".
---

# Launch Receipts

> A launch post is a list of promises. Each one should come with a receipt the reader can check in under a minute.

## What this skill is

Launch Receipts is a method for taking a finished-enough project public. It is not a hype generator. It treats a launch like a short, honest exchange with strangers: you show them something they can try, you say exactly what it does and does not do, you ask for one thing, and you stay to answer.

You come out with a `launch/` folder:

| File | What it holds |
|---|---|
| `SHIPCARD.md` | one-sentence what, who it is for, the try path, the single launch ask, what you will not claim |
| `RECEIPTS.md` | every claim you might make, each with a receipt id, kind and evidence |
| `COLDREAD.md` | the stranger test on your README or landing page, and the clean-machine try-path log |
| `GATE.md` | five doors, each OPEN or SHUT, and the verdict GO / SOFT / HOLD |
| `VENUES.md` | the venues considered, their rules as read today, fit score, the chosen plan and dates |
| `posts/*.md` | one post per venue, written for that venue, claims tagged with receipt ids |
| `HARDQ.md` | the eight hardest questions you expect, answered before anyone asks |
| `DESK.md` | the launch-day reply log: every comment typed, answered, and acted on |
| `AFTERWORD.md` | day-7 numbers against the ask, what confused people, what changed |

## The problem it solves

Most launches of small projects fail in one of five boring ways:

1. **The post promises things the project cannot show.** "Blazing fast", "works everywhere", "the only tool that...". The first commenter tries it, it does not hold, and the thread turns.
2. **Strangers cannot get to the good part.** A signup wall, a missing API key, a 900 MB install, a broken quick-start step. Interest dies at step two.
3. **The post breaks the venue's rules.** A landing page on Show HN, a bare link in a subreddit that only allows Saturday showcases, an upvote request on Product Hunt. Removed, sometimes banned.
4. **One text is pasted everywhere.** Each audience wants a different first sentence. Copy-paste reads as spam to all of them.
5. **The maker disappears.** Questions go unanswered for hours, confusion is never fed back into the README, and a week later nobody remembers what was learned.

Launch Receipts puts a check in front of each failure.

## When to use it

- You built something and want people outside your circle to try it.
- You are about to write a Show HN, a Product Hunt page, a Reddit post, an X or Bluesky thread, a V2EX "分享创造" post, or a newsletter pitch.
- A previous launch got no response and you want to know why before trying again.
- You shipped a major overhaul and wonder whether it deserves a second launch.

Not for: paid ad campaigns, press embargoes, fundraising announcements, or growth hacking. And never for vote rings, sock-puppet accounts, or bulk messaging. The skill refuses those.

## Hard rules

1. **No receipt, no claim.** A claim may appear in a post only if `RECEIPTS.md` backs it with a receipt of kind SHOWN, RUN, FILE, NUMBER or QUOTE. STATED and WISH are not receipts.
2. **Ask for tries and feedback, never votes.** Not in the post, not in DMs, not in a group chat "just to get it started".
3. **Disclose.** Every post says you made it.
4. **One venue, one text.** Posts may share facts, never sentences.
5. **A limits line in every post longer than a title.** Say what it does not do yet.
6. **Fictional data in every public screenshot.** No real names, emails, tokens, internal hosts or customer data.
7. **The agent drafts; the person posts.** The skill never logs in, submits, schedules, or replies on anyone's behalf.

## Step by step

### Step 1. Ship card (freeze it before writing any post)

Read the repo or site first: README, the main entry point, the quick start, the license, recent commits, open issues. Skip build output, lock files, `.env*`, keys and anything ignored for privacy reasons.

Then write `SHIPCARD.md`:

```
What (one sentence, no adjectives):
For (a specific person in a specific moment):
Try path (exact first command or URL, and what success looks like):
Cost to try (free / account needed / key needed / paid):
Status (prototype / usable / stable) and what is missing:
The one ask (pick ONE: tries + bug reports / feedback on X / contributors for Y / first paying users / stars as a bookmark):
Will not claim (things that sound good but you cannot show):
Owner on launch day and hours available:
```

If you cannot fill "What" without an adjective, or "For" without the word "everyone", stop and ask the maker. Those two lines decide every post that follows.

### Step 2. Receipt inventory

List every claim you are tempted to make: features, speed, size, compatibility, privacy, comparisons, user counts, quotes. Give each a row in `RECEIPTS.md`:

| id | kind | claim | evidence |
|---|---|---|---|
| R1 | RUN | renames a 2,000-photo folder in about 4 s | `time tidemark ./sample` on a 2022 laptop, output pasted |
| R2 | SHOWN | shows a dry-run table before touching files | screenshot `docs/preview.png` with fictional photo names |
| R3 | WISH | works on Windows | never tested |

Receipt kinds:

- **SHOWN**: a screenshot, GIF or short clip of the real product doing the thing.
- **RUN**: a command anyone can run, with the output you observed and the machine you ran it on.
- **FILE**: a path and line in the public repo (a test, a config, a license).
- **NUMBER**: a measured figure with its method, sample and date.
- **QUOTE**: a real person's words, with their permission to quote.

Not receipts:

- **STATED**: true as far as you know, but nothing a stranger can check. Rephrase as intent ("designed for..."), or move it to the limits line, or drop it.
- **WISH**: not true yet. It belongs in the roadmap or the limits line, never in a feature list.

Comparisons with other tools need a RUN or NUMBER receipt that a reader could reproduce, with the other tool's version. Otherwise describe your own approach and let the reader compare.

Superlatives ("fastest", "first", "only", "最强", "唯一") are claims too. They almost never survive this step. Good.

### Step 3. Cold read and try path

**Cold read.** Give the README or landing page to a fresh agent session or a person who has never seen it. Allow 30 seconds of reading. Ask five questions and record the answers word for word in `COLDREAD.md`:

1. What is this?
2. Who is it for?
3. How do I try it right now?
4. What does it cost me (money, account, data)?
5. Why would I use this instead of what I already use?

Every wrong or empty answer is a README fix, made before launch. The usual fixes: move the one-sentence "What" to the first line, put the try command above the fold, add one real screenshot, add a "not for" line.

**Try path.** Follow the README exactly on a clean machine, container, fresh browser profile or new account. Log each step with the time taken and any barrier:

```
00:00 open README
00:40 `pipx install tidemark`  ok
01:10 `tidemark --dry-run ~/Pictures/sample`  FAIL: needs exiftool, README does not say so
...
04:30 first success (preview table shown)
Barriers: hidden dependency (exiftool)
```

Barriers to look for: signup or email wall, API key, payment card, hidden system dependency, OS-specific step, large download, sample data that is not provided, a quick-start that uses a newer version than the release.

Target: first success in under five minutes for a developer tool and under one minute for a web app, with no barrier the post does not mention.

### Step 4. The gate

Check five doors in `GATE.md`. Each is OPEN or SHUT with one line of evidence.

| Door | OPEN when |
|---|---|
| TRYABLE | the try path works from clean, and every barrier is named in the post |
| TRUE | every claim in the drafts has a receipt; WISH items sit in the limits line |
| SAFE | license present; no secrets in repo history you are about to promote; screenshots use fictional data; a way to report security issues |
| LEGIBLE | the cold read answered all five questions correctly after fixes |
| PRESENT | someone who can answer questions is free for the first four hours after the main post |

Verdict:

- **GO**: all five OPEN. Proceed to the main venue.
- **SOFT**: TRUE and SAFE are OPEN but one other door is SHUT. Do a quiet share in one friendly place (a community where you already take part, your own followers) to shake out problems, then re-check.
- **HOLD**: TRUE or SAFE is SHUT, or two or more doors are SHUT. Do not post. List what to fix.

A HOLD is a good outcome. A launch can be done once per venue; a fix can be done any time.

### Step 5. Venue fit

Read `references/venues.md` for venue cards, then **open each venue's current rules page or sidebar** before planning. Rules change; the card is a starting point, not the rule.

Score each candidate venue 0 to 2 on four questions and write the result in `VENUES.md`:

- **Audience**: do the people there match the "For" line?
- **On-topic**: does the project meet the venue's definition (for example, Show HN wants something people can try, not a signup page)?
- **Ask match**: does the venue reward your one ask (feedback, users, contributors)?
- **Standing**: does the maker already take part there, or is it a place that welcomes first-time sharers?

Pick one **main** venue (highest score, must be 2 on On-topic) and at most two **supporting** venues. Space them at least a day apart so you can fix what the main venue finds. Note each venue's timing quirks (for example, Product Hunt days run on Pacific time).

### Step 6. Write the posts

One file per venue in `posts/`. Every post follows the same discipline but not the same words:

- **First line**: what it is, for whom, in the venue's language. A title is a description, not a slogan.
- **Why it exists**: two or three sentences of the maker's real reason. Specific beats impressive.
- **Show it**: the try command or link, and one SHOWN receipt.
- **What it does**: three or four tagged claims at most.
- **Limits line**: "It does not yet...", from the WISH and STATED rows.
- **The one ask**: specific. "If it fails on your camera's files, paste the error" beats "feedback welcome".
- **Disclosure**: "I built this" in the post itself.

Tag every factual sentence with its receipt id, like `[R1]`. Then check and clean:

```bash
python3 scripts/receipts.py lint launch/posts/show-hn.title.txt --receipts launch/RECEIPTS.md --venue hn-title
python3 scripts/receipts.py lint launch/posts/show-hn.md --receipts launch/RECEIPTS.md --venue long
python3 scripts/receipts.py count launch/posts/x.md --venue x
python3 scripts/receipts.py strip launch/posts/x.md > launch/posts/x.final.txt
```

`lint` fails on unknown or weak receipts, vote requests and over-length text; it warns on bare numbers, hype words and missing disclosure. Fix every error; read every warning.

Also write `HARDQ.md`: the eight questions most likely to sting, with short honest answers. Always include: "How is this different from X?", "Why not just use a script?", "What data does it touch or send?", "Is it maintained / will it be?", "What does it cost now and later?", "Why should I trust a new project with my files?" Answer from receipts; "I don't know yet" is allowed.

### Step 7. Launch-day desk

The maker posts. The agent helps keep `DESK.md`, one row per comment:

| time | where | type | gist | reply sent | action |
|---|---|---|---|---|---|

Types: **BUG** (it broke), **CONFUSED** (they misread something), **WISH** (feature request), **COMPARE** (vs another tool), **PRAISE**, **HOSTILE**.

Reply rules:

- Answer within the PRESENT window; first replies matter most.
- Thank criticism, then answer the substance. Never argue tone.
- BUG: reproduce, fix if small, reply with the commit or issue link.
- CONFUSED: two people confused the same way means the README changes today. Reply after the change.
- COMPARE: describe your approach honestly; do not trash the other tool.
- HOSTILE: answer once if there is a real point, otherwise leave it.
- Never reply from another account, never ask friends to comment, never edit the post to add claims without receipts.

### Step 8. Day-7 afterword

Write `AFTERWORD.md`:

- The one ask against what happened (tries, bug reports, contributors), with numbers and how they were counted. Stars and points go in a separate "noise" line.
- Top three confusions and what changed because of them.
- Bugs found by strangers, fixed or open.
- Which receipts held up, which claims were challenged.
- Next moment worth sharing (a major change, a real user story). Minor versions are not a relaunch.

## Example

The `examples/tidemark/` folder contains a complete kit for a fictional CLI that renames photos by capture date: ship card, receipts, cold read with a hidden dependency found, gate verdict that went from HOLD to GO, venue plan, a Show HN post, an X post, a Chinese V2EX post, hard questions, a sample desk log and an afterword. Run the linter on its posts to see clean output, and on `examples/tidemark/posts/bad-draft.md` to see what it catches.

A compressed version:

```
Ship card   What: a command-line tool that renames photos to their capture date, with a dry-run preview and an undo file.
            For: people with years of camera and phone photos named IMG_4412.JPG.
            Ask: tries on unusual cameras + bug reports with the error text.
Receipts    R1 RUN speed on sample folder, R2 SHOWN preview, R4 FILE undo test, R3 WISH Windows -> limits line.
Cold read   Q3 failed: hidden exiftool dependency. README fixed, try path now 2 min 10 s.
Gate        HOLD (TRYABLE shut) -> GO after fix.
Venues      main Show HN (2,2,2,1), supporting r/DataHoarder on its allowed day, X to own followers next day.
Show HN     "Show HN: Tidemark - rename photos to their capture date, with preview and undo"
```

## Tips

- A BARE-NUMBER warning on a sentence about yourself ("my backups were 14 folders") can stay: it is a story, not a product claim. A number about the product cannot.
- Write the limits line first. It makes every other sentence more believable.
- The best SHOWN receipt is the product in the middle of doing its job, not the landing page.
- If you need the word "simply" in a quick start, the quick start is too long.
- Put the try command in the first screen of the README; people read titles and the first five lines.
- A project with zero users can still launch honestly. "Nobody but me has used this yet" is a fine sentence.
- Chinese venues: V2EX's "分享创造" node, Jike, and WeChat groups each expect different tone. Write in natural Chinese, not translated English, and keep the same receipts.
- Re-run the cold read after launch day. The README that survived the desk is usually much better than the one you launched with.
- If the verdict keeps coming out HOLD, the project may need another week, not a better post.
