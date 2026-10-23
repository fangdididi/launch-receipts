#!/usr/bin/env python3
"""receipts.py - read-only checks for launch posts.

Commands
  lint  DRAFT --receipts RECEIPTS.md [--venue NAME]   check a draft post
  strip DRAFT                                          print the draft without [R#] tags
  count DRAFT [--venue NAME]                           show length against venue limits
  venues                                               list known venue limits

Drafts mark each factual claim with a receipt tag such as [R3]. The receipts
file is a markdown table whose first column is the id (R1, R2, ...) and whose
second column is the kind (SHOWN, RUN, FILE, NUMBER, QUOTE). Anything else in
that column (STATED, WISH, blank) is not a receipt and cannot back a claim.

Standard library only. Never writes files, never posts anything.
"""
import argparse
import re
import sys
import unicodedata

KINDS = {"SHOWN", "RUN", "FILE", "NUMBER", "QUOTE"}

# name -> (limit, how it is counted, note)
VENUES = {
    "hn-title": (80, "chars", "Hacker News title; start with 'Show HN: '"),
    "ph-tagline": (60, "chars", "Product Hunt tagline"),
    "ph-desc": (260, "chars", "Product Hunt description"),
    "x": (280, "x-weighted", "X post; CJK counts 2, each URL counts 23"),
    "bsky": (300, "graphemes", "Bluesky post"),
    "reddit-title": (300, "chars", "Reddit post title"),
    "gh-desc": (350, "chars", "GitHub repository description"),
    "long": (40000, "chars", "any long post body (Show HN text, Reddit, V2EX, blog)"),
}

TAG_RE = re.compile(r"\[R(\d+)\]")
URL_RE = re.compile(r"https?://\S+")
VOTE_RE = re.compile(
    r"\b(up-?vote|upvoting|vote for (us|me|it)|give (us|me) a vote|smash that|"
    r"please vote|votes? appreciated)\b|点赞|求赞|投票|投一票|帮忙顶|顶一下|求顶|刷票",
    re.I,
)
HYPE_EN = [
    "best", "fastest", "first", "only", "revolutionary", "game-changing",
    "game changer", "blazing", "blazingly", "seamless", "seamlessly",
    "effortless", "effortlessly", "world-class", "cutting-edge", "next-gen",
    "unparalleled", "magical", "supercharge", "10x", "100x", "insanely",
    "the future of", "never again", "zero effort",
]
HYPE_ZH = ["最快", "最好", "最强", "第一", "唯一", "颠覆", "革命性", "极致", "秒杀",
           "遥遥领先", "神器", "史上", "全网", "无敌", "零成本", "一键搞定"]
DISCLOSE_RE = re.compile(
    r"\b(i|we) (built|made|wrote|created|maintain|am building|are building)\b|"
    r"\bmy (project|tool|app|side project|library|cli)\b|\bour (project|tool|app)\b|"
    r"我(做|写|开发|搞)了|我(做|写|开发)的|我们(做|开发)了|自己(做|写)的",
    re.I,
)
HYPE_EN_RE = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(w) for w in HYPE_EN) + r")(?![\w-])", re.I
)
VERSION_RE = re.compile(r"\bv?\d+(\.\d+){1,3}\b")
NUMBER_RE = re.compile(r"\d")


def load_receipts(text):
    """Return {id: kind} from a markdown table. Only real receipt kinds count."""
    found = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        m = re.fullmatch(r"R(\d+)", cells[0], re.I)
        if m:
            found[int(m.group(1))] = cells[1].upper()
    return found


def sentences(text):
    """Split into rough sentences, keeping line structure for reporting."""
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        for part in re.split(r"(?<=[.!?;])\s+|(?<=[。！？；])", line):
            if part.strip():
                out.append((n, part.strip()))
    return out


def has_number(sentence):
    s = URL_RE.sub("", sentence)
    s = TAG_RE.sub("", s)
    s = VERSION_RE.sub("", s)
    # identifiers such as IMG_4412.JPG, M2, H1, utf8 are names, not claims
    s = re.sub(r"[A-Za-z_][A-Za-z0-9_-]*\d[A-Za-z0-9_.-]*", "", s)
    return bool(NUMBER_RE.search(s))


def hype_words(sentence):
    words = [m.group(1).lower() for m in HYPE_EN_RE.finditer(sentence)]
    words += [w for w in HYPE_ZH if w in sentence]
    return words


def length(text, how):
    text = text.strip()
    if how == "x-weighted":
        total = 0
        rest = URL_RE.sub("", text)
        total += 23 * len(URL_RE.findall(text))
        for ch in rest:
            eaw = unicodedata.east_asian_width(ch)
            total += 2 if eaw in ("W", "F") else 1
        return total
    if how == "graphemes":
        return sum(1 for ch in text if not unicodedata.combining(ch)
                   and ch not in "\u200d\ufe0f")
    return len(text)


def lint(draft, receipts_text, venue=None):
    """Return list of (level, line, code, message). level is ERROR or WARN."""
    receipts = load_receipts(receipts_text) if receipts_text is not None else {}
    issues = []
    for n, s in sentences(draft):
        tags = [int(t) for t in TAG_RE.findall(s)]
        for t in tags:
            kind = receipts.get(t)
            if kind is None:
                issues.append(("ERROR", n, "NO-RECEIPT", f"[R{t}] is not in the receipts file"))
            elif kind not in KINDS:
                issues.append(("ERROR", n, "WEAK-RECEIPT",
                               f"[R{t}] is {kind or 'blank'}, not a receipt ({', '.join(sorted(KINDS))})"))
        if VOTE_RE.search(s):
            issues.append(("ERROR", n, "VOTE-ASK", "asks for votes; ask for tries or feedback instead"))
        if not tags:
            if has_number(s):
                issues.append(("WARN", n, "BARE-NUMBER", f"number without a receipt: {s[:70]}"))
            for w in hype_words(s):
                issues.append(("WARN", n, "HYPE", f"'{w}' without a receipt; cut it or prove it"))
    if venue and venue not in ("hn-title", "ph-tagline", "reddit-title", "gh-desc"):
        if not DISCLOSE_RE.search(TAG_RE.sub("", draft)):
            issues.append(("WARN", 0, "NO-DISCLOSURE", "nothing says you made this ('I built ...')"))
    if venue:
        limit, how, _ = VENUES[venue]
        used = length(TAG_RE.sub("", draft), how)
        if used > limit:
            issues.append(("ERROR", 0, "TOO-LONG", f"{used}/{limit} for {venue}"))
        if venue == "hn-title" and not draft.strip().startswith("Show HN:"):
            issues.append(("WARN", 0, "HN-PREFIX", "Show HN titles start with 'Show HN: '"))
    return issues


def strip_tags(text):
    text = re.sub(r"\s*\[R\d+\]", "", text)
    return text


def main(argv=None):
    p = argparse.ArgumentParser(description="Read-only checks for launch posts.")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("lint"); a.add_argument("draft"); a.add_argument("--receipts", required=True)
    a.add_argument("--venue", choices=sorted(VENUES))
    b = sub.add_parser("strip"); b.add_argument("draft")
    c = sub.add_parser("count"); c.add_argument("draft"); c.add_argument("--venue", choices=sorted(VENUES))
    sub.add_parser("venues")
    args = p.parse_args(argv)

    if args.cmd == "venues":
        for k, (lim, how, note) in VENUES.items():
            print(f"{k:13} {lim:4} {how:11} {note}")
        return 0
    draft = open(args.draft, encoding="utf-8").read()
    if args.cmd == "strip":
        sys.stdout.write(strip_tags(draft))
        return 0
    if args.cmd == "count":
        names = [args.venue] if args.venue else list(VENUES)
        clean = strip_tags(draft)
        for k in names:
            lim, how, _ = VENUES[k]
            used = length(clean, how)
            print(f"{k:13} {used:4}/{lim:<4} {'OK' if used <= lim else 'OVER'}")
        return 0
    receipts = open(args.receipts, encoding="utf-8").read()
    issues = lint(draft, receipts, args.venue)
    for level, n, code, msg in issues:
        where = f"line {n}" if n else "draft"
        print(f"{level:5} {where:8} {code:13} {msg}")
    errors = sum(1 for i in issues if i[0] == "ERROR")
    warns = len(issues) - errors
    print(f"-- {errors} error(s), {warns} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
