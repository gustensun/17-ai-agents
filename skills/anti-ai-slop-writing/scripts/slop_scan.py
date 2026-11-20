#!/usr/bin/env python3
"""slop_scan.py: find the habits that make writing read as AI-generated.

Standard library only. Works on Mac, Windows and Linux with Python 3.8+.

Usage
  python3 slop_scan.py draft.md                 scan one or more files
  python3 slop_scan.py -                        scan text from stdin
  python3 slop_scan.py --allow allow.txt draft.md
                                                downgrade the owner's allowed devices
  python3 slop_scan.py --keep "exact phrase" draft.md
                                                never flag a required phrase
  python3 slop_scan.py --voice samples.txt draft.md
                                                compare the draft with the owner's samples
  python3 slop_scan.py --profile samples.txt    print a voice profile of writing samples
  python3 slop_scan.py --strict draft.md        emoji and exclamation marks become HARD
  python3 slop_scan.py --json draft.md          machine-readable output

Severity
  HARD    must be fixed before anything is delivered
  REVIEW  keep only if it is the exact word, sounds like the owner and stands alone
  INFO    for your attention (placeholders to fill, the owner's own habits)

Exit code is 1 when any HARD finding remains, so other tools can block on it.

Regions between <!-- slop-scan: off --> and <!-- slop-scan: on --> are skipped,
along with fenced code blocks, inline code, URLs and HTML comments. Block quotes
(lines starting with >) are skipped too, because customer quotes stay verbatim.
Use --scan-quotes to include them.

The allow file has one entry per line. An entry is either an exact phrase
("What if you could") or a category id ("category:salesy"). Lines starting with
# are comments.
"""

import argparse
import json
import os
import re
import statistics
import sys
from collections import Counter

APOS = "['\u2019]"  # straight or curly apostrophe

# ---------------------------------------------------------------------------
# Patterns. Each entry: (category, severity, regex, fix)
# ---------------------------------------------------------------------------

FIX = {
    "artifact": "Delete it. Chat leftovers are the clearest sign of pasted AI text.",
    "dash": "Use a comma, period, colon or parentheses. For number ranges use a hyphen (3-5).",
    "contrast": "Say what the thing is, alone. Keep a contrast only when the reader truly holds the first belief.",
    "pivot": "Delete the announcement and give the information.",
    "bait": "Remove it unless the owner asked for this exact call to action (then pass it with --keep).",
    "opener": "Start on the fact, the event or the decision.",
    "closer": "Stop on the last useful fact or the concrete next step.",
    "leftover": "A template variable was never filled. Fill it or turn it into a [BRACKET] placeholder.",
    "fog": "Rewrite the sentence around the concrete action, number or mechanism. A synonym keeps the empty sentence.",
    "hype": "Match the word to the evidence. Use the number or the result instead.",
    "outcome": "Name the observable result and how it is measured, or cut the claim.",
    "profundity": "Replace the maxim with the specific lesson from this situation.",
    "engagement": "Cut it, or ask a question only when the answer matters.",
    "salesy": "Describe the buyer's real situation in their words. Allowed when it names a specific moment, or when it is in the owner's allowed devices.",
    "support": "Open with the reason for the message, then the answer and the steps.",
    "urgency": "Only state urgency that is real, with the actual date or number from the brain.",
    "dash-substitute": "A spaced hyphen used as a dash. Use a comma, period or colon.",
    "exclamation": "Let the sentence carry the energy. Keep only if the owner writes this way.",
    "emoji": "Remove unless the owner asked for emoji in this format.",
    "staccato": "Three or more very short sentences in a row read as a template. Join or vary them.",
    "even-rhythm": "Sentence lengths are too even. Let important points run longer and small ones stay short.",
    "one-line-paragraphs": "Most paragraphs are one sentence. Group related sentences into paragraphs of two to four.",
    "repeated-opener": "Several sentences in a row start with the same word. Vary the openings.",
    "questions": "Many rhetorical questions in a short piece. Answer them or cut them.",
    "triplets": "Many lists of exactly three. Use the number of items that really exist.",
    "placeholder": "A fact the owner still needs to fill in.",
}

P = []


def add(cat, sev, pattern, flags=re.IGNORECASE):
    P.append((cat, sev, re.compile(pattern, flags)))


# artifact (HARD)
for pat in [
    r"oaicite", r"contentReference\[", r"\bturn\d+(search|news|view|file)\d+\b",
    r"\[cite:\s*\d+\]", r"utm_source=chatgpt\.com", r"\bas an ai (language )?model\b",
    r"\bi hope this helps\b", r"^\s*(certainly|absolutely|sure|great question)[!,.]\s",
    r"\bmy (knowledge|training) (cutoff|cut-off|data)\b", r"\bi (can't|cannot|am unable to) browse\b",
    r"\bas of my last (update|training)\b",
]:
    add("artifact", "HARD", pat)

# dash (HARD)
add("dash", "HARD", "\u2014", 0)
add("dash", "HARD", "\u2013", 0)
add("dash", "HARD", r"(?<=\w) -- (?=\w)", 0)

# contrast (HARD)
for pat in [
    rf"\b(it|this|that){APOS}?s?\s*(is\s+)?not\s+(just\s+|only\s+|about\s+|really\s+)?[^.?!\n]{{1,60}}[.,;:]\s*(it|this|that)({APOS}s|\s+is)\b",
    rf"\b(it|this|that|he|she|they)\s+(isn{APOS}t|wasn{APOS}t|aren{APOS}t|weren{APOS}t)\s+(just\s+|only\s+|about\s+)?[^.?!\n]{{1,50}}[.,;:]\s*(it|this|that|he|she|they)({APOS}s|{APOS}re|\s+is|\s+was|\s+are|\s+were)\b",
    r"\bnot\s+just\s+[^.?!\n]{1,60}?,?\s+but\b",
    r"\bless\s+(like|about|of)\s+[^.?!\n]{1,40}\s+and\s+more\s+(like|about|of)\b",
    rf"\bmore\s+than\s+(just\s+)?an?\s+[^.?!\n]{{1,30}}[,.;]\s*it{APOS}s\b",
    rf"\bthe\s+real\s+(problem|issue|question|secret|reason|work)\s+(isn{APOS}t|is\s+not|wasn{APOS}t)\b",
    rf"\byou{APOS}re\s+not\s+(selling|buying|building|paying\s+for)\s+[^.?!\n]{{1,40}}[.,;]\s*you{APOS}re\s+(selling|buying|building|paying\s+for)\b",
    rf"\b(you\s+)?don{APOS}t\s+need\s+(more|another|a|an)\s+[^.?!\n]{{1,40}}[.,;]\s*you\s+need\b",
    r"\bnot\s+because\s+[^.?!\n]{1,50},\s*but\s+because\b",
    rf"\bthe\s+question\s+(isn{APOS}t|is\s+not)\s+(whether|if)\b",
    rf"\bit{APOS}s\s+not\s+about\s+[^.?!\n]{{1,60}}[.,;]\s*it{APOS}s\s+about\b",
    rf"\b[^.?!\n]{{1,40}}\s+doesn{APOS}t\s+replace\s+[^.?!\n]{{1,30}}[.,;]\s*it\s+(amplifies|multiplies|enhances)\b",
]:
    add("contrast", "HARD", pat)
add("contrast", "REVIEW", r"\bnot\s+only\s+[^.?!\n]{1,60}\bbut\s+also\b")

# pivot (HARD)
for pat in [
    rf"\bhere{APOS}s\s+the\s+(thing|kicker|catch|deal|truth|secret|twist|problem)\b",
    rf"\bhere{APOS}s\s+(why|how|what)\s*:",
    rf"\bhere{APOS}s\s+where\s+it\s+gets\b",
    r"(?:^\s*(?:[-*+]\s+|\d+[.)]\s+)?(?:\*\*)?|(?<=[.!?:]\s)|(?<=[.!?:]\s\s))(?:and\s+)?the\s+(result|takeaway|best\s+part|kicker|catch|answer|truth|secret|twist|outcome)\s*\?",
    r"\band\s+honestly\s*\?",
    r"\bthen\s+everything\s+changed\b",
    rf"\bthat{APOS}s\s+where\s+the\s+magic\s+happens\b",
    r"\bfast\s+forward\s+to\b",
    r"\bspoiler\s+alert\b",
    r"\bmake\s+no\s+mistake\b",
    r"\bbut\s+that\s+(was|is)\s+only\s+(part|half)\s+of\s+the\s+story\b",
]:
    add("pivot", "HARD", pat)

# bait (HARD)
for pat in [
    r"^\s*(agree|thoughts|right)\s*\?\s*$",
    r"\bfollow\s+(me\s+)?for\s+more\b",
    r"\bunpopular\s+opinion\s*:",
    r"\bhard\s+truth\s*:",
    r"\bwhat\s+nobody\s+tells\s+you\b",
    r"\blet\s+that\s+sink\s+in\b",
    r"\bread\s+that\s+again\b",
    r"\brepost\s+if\b",
    r"\bsave\s+this\s+(post\s+)?for\s+later\b",
    r"\bcomment\s+[\"'\u201c]?[A-Z]{3,}[\"'\u201d]?\s+(below\s+)?(and|to)\b",
]:
    add("bait", "HARD", pat)

# opener (HARD)
for pat in [
    rf"\bin\s+today{APOS}s\s+(fast[-\s]paced|digital|ever[-\s]changing|modern|competitive)\b",
    r"\bin\s+(the|an|this)\s+ever[-\s](evolving|changing)\b",
    r"\bhave\s+you\s+ever\s+wondered\b",
    rf"\blet{APOS}s\s+(dive|jump)\s+(in|into|right\s+in)\b",
    r"\bi\s+hope\s+this\s+(email|message|note)\s+finds\s+you\b",
    r"\bnow\s+more\s+than\s+ever\b",
    r"\bin\s+the\s+(age|era)\s+of\s+(ai|artificial)\b",
    r"\bimagine\s+a\s+world\s+where\b",
    r"\bas\s+technology\s+continues\s+to\b",
]:
    add("opener", "HARD", pat)

# closer (HARD)
for pat in [
    r"\bin\s+conclusion\b",
    r"\bat\s+the\s+end\s+of\s+the\s+day\b",
    r"\bthe\s+choice\s+is\s+yours\b",
    r"\bthe\s+key\s+takeaway\b",
    r"\btake\s+the\s+first\s+step\s+today\b",
    rf"\byou{APOS}ve\s+got\s+this\b",
    r"\bonly\s+time\s+will\s+tell\b",
    rf"\b(don{APOS}t|do\s+not)\s+hesitate\s+to\s+(reach|contact|ask)\b",
    r"\bthe\s+possibilities\s+are\s+endless\b",
    r"\bthe\s+future\s+is\s+bright\b",
    r"\bthe\s+journey\s+is\s+(only\s+|just\s+)*beginning\b",
    r"\bto\s+sum\s+(it\s+)?up\b",
    r"\bone\s+thing\s+is\s+(certain|clear)\b",
]:
    add("closer", "HARD", pat)

# leftover template variables (HARD)
add("leftover", "HARD", r"\{\{\s*[^}]+\s*\}\}", 0)

# fog (REVIEW, density-based)
FOG = (
    "unlock|unleash|empower|empowering|elevate|leverage|utilize|utilise|foster|facilitate|"
    "navigate|harness|revolutionize|revolutionise|reimagine|redefine|reshape|streamline|"
    "robust|seamless|seamlessly|holistic|impactful|innovative|cutting-edge|transformative|"
    "synergy|synergies|tapestry|realm|landscape|ecosystem|catalyst|cornerstone|beacon|"
    "interplay|multifaceted|pivotal|myriad|plethora|delve|delves|testament|meticulous|"
    "embark|endeavor|endeavour|paradigm|bespoke|curated|supercharge|turbocharge|"
    "next-level|world-class|best-in-class|state-of-the-art"
)
add("fog", "REVIEW", rf"\b({FOG})\b")

# hype (REVIEW)
add("hype", "REVIEW", r"\b(insane|insanely|crazy|mind[-\s]?blowing|jaw[-\s]?dropping|skyrocket\w*|explode|exploding|"
    r"massive|epic|secret\s+sauce|game[-\s]?chang\w*|revolutionary|life[-\s]?changing|unbelievable|"
    r"guaranteed\s+results|overnight\s+success|on\s+autopilot|10x\s+your)\b")

# generic outcomes (REVIEW)
add("outcome", "REVIEW", r"\b(drive|deliver|unlock|achieve)\s+(meaningful|real|lasting|incredible)\s+(results|outcomes|value|growth)\b")
add("outcome", "REVIEW", r"\b(gain|get)\s+a\s+competitive\s+edge\b|\bmaximi[sz]e\s+(your\s+)?roi\b|\bfuture[-\s]proof\b|"
    r"\btailored\s+to\s+your\s+unique\s+needs\b|\ba\s+powerful\s+combination\b|\bsustainable\s+growth\b|"
    r"\btake\s+(it|your\s+\w+|things)\s+to\s+the\s+next\s+level\b")

# fake profundity (REVIEW)
add("profundity", "REVIEW", r"\b(consistency|context|clarity|focus)\s+is\s+(key|everything|king)\b|\bevery\s+challenge\s+is\s+an\s+opportunity\b|"
    r"\bsuccess\s+starts\s+with\b|\bsmall\s+changes\s+(can\s+)?(create|make|lead\s+to)\s+big\b|\bthe\s+best\s+\w+\s+solve\s+real\s+problems\b")

# generic engagement (REVIEW)
add("engagement", "REVIEW", rf"\byou{APOS}re\s+not\s+alone\b|\bwe{APOS}ve\s+got\s+you\s+covered\b|\bwhether\s+you{APOS}re\s+an?\s+\w+\s+or\b|"
    rf"\bno\s+matter\s+where\s+you\s+are\s+(on|in)\s+your\s+journey\b|\bready\s+to\s+get\s+started\s*\?|"
    rf"\bif\s+(that|this)\s+sounds\s+familiar\b|\blet{APOS}s\s+(unpack|explore)\b")

# generic sales lines (REVIEW, often allowed by the owner)
add("salesy", "REVIEW", rf"\b(struggling\s+to|tired\s+of|what\s+if\s+you\s+could|say\s+goodbye\s+to|finally,\s+a|"
    rf"designed\s+with\s+you\s+in\s+mind|everything\s+you\s+need,?\s+all\s+in\s+one\s+place|"
    rf"work\s+smarter,?\s+not\s+harder|your\s+journey\s+starts\s+here|one\s+platform\.\s+endless|powerful\s+yet\s+simple)\b")
add("salesy", "REVIEW", r"\bno\s+more\s+\w+[^.?!\n]{0,30}\.\s+no\s+more\b")

# support and email stock lines (REVIEW)
add("support", "REVIEW", r"\bthank\s+you\s+for\s+bringing\s+this\s+to\s+our\s+attention\b|\bwe\s+understand\s+how\s+frustrating\b|"
    r"\brest\s+assured\b|\bwe\s+appreciate\s+your\s+patience\b|\bat\s+your\s+earliest\s+convenience\b|\bi\s+wanted\s+to\s+reach\s+out\b")

# fake urgency (REVIEW)
add("urgency", "REVIEW", rf"\bact\s+now\b|\blimited\s+time\s+only\b|\bhurry\b|\bbefore\s+it{APOS}s\s+too\s+late\b|\bselling\s+out\s+fast\b|"
    r"\bonly\s+\d+\s+(spots|seats|places|copies)\s+left\b|\bwon't\s+last\s+long\b")

# dash substitute (REVIEW): a spaced hyphen inside a sentence
add("dash-substitute", "REVIEW", r"(?<=[A-Za-z,)]) - (?=[A-Za-z(])", 0)

# placeholders (INFO)
add("placeholder", "INFO", r"\[[A-Z][A-Z0-9 _/&:,'\-]{1,60}\]", 0)

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U0001F900-\U0001F9FF\u2B50\u2B06\u2B07\u2934\u2935\u203C\u2049]"
)
EXCLAIM_RE = re.compile(r"(?<![!<\[])!(?![\[=(])")

HARD_SET = {"artifact", "dash", "contrast", "pivot", "bait", "opener", "closer", "leftover"}

# ---------------------------------------------------------------------------
# Text preparation
# ---------------------------------------------------------------------------

URL_RE = re.compile(r"https?://\S+|www\.\S+")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
MD_LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")


def prepare(text, scan_quotes=False):
    """Return a list of (line_number, cleaned_line). Skipped regions become empty."""
    out = []
    in_fence = False
    off = False
    for i, raw in enumerate(text.splitlines(), start=1):
        line = raw
        low = line.strip().lower()
        if "<!-- slop-scan: off -->" in low:
            off = True
            out.append((i, ""))
            continue
        if "<!-- slop-scan: on -->" in low:
            off = False
            out.append((i, ""))
            continue
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            in_fence = not in_fence
            out.append((i, ""))
            continue
        if in_fence or off:
            out.append((i, ""))
            continue
        if not scan_quotes and line.lstrip().startswith(">"):
            out.append((i, ""))
            continue
        line = HTML_COMMENT_RE.sub(" ", line)
        line = INLINE_CODE_RE.sub(" ", line)
        line = MD_LINK_TARGET_RE.sub("]", line)
        line = URL_RE.sub(" ", line)
        out.append((i, line))
    return out


SENT_SPLIT = re.compile(r"(?<=[.?!])\s+(?=[A-Z0-9\"'\u201c(\[])")


def prose_lines(lines):
    """Lines that are prose (not headings, list items, tables or empty)."""
    res = []
    for n, l in lines:
        s = l.strip()
        if not s or s.startswith("#") or s.startswith("|") or re.match(r"^([-*+]|\d+[.)])\s", s) or s.startswith("---"):
            continue
        res.append((n, s))
    return res


def sentences(text):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    return [s for s in SENT_SPLIT.split(text) if s.strip()]


def words(text):
    return re.findall(r"[A-Za-z\u00C0-\u024F']+", text)


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------


def load_allow(path):
    phrases, cats = [], set()
    if not path:
        return phrases, cats
    if not os.path.exists(path):
        print(f"Note: no allow file at {path}, so nothing is allowed yet. The COO creates it in stage 1 "
              "of setup/PROTOCOL.md, or you can create it yourself with one phrase per line.", file=sys.stderr)
        return phrases, cats
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.lower().startswith("category:"):
                cats.add(s.split(":", 1)[1].strip().lower())
            else:
                phrases.append(s.lower())
    return phrases, cats


def scan_text(text, args, allow_phrases=(), allow_cats=(), habit_cats=()):
    lines = prepare(text, scan_quotes=args.scan_quotes)
    keep = [k.lower() for k in (args.keep or [])]
    findings = []

    def record(cat, sev, n, snippet, context=None):
        snip = snippet.strip()
        low = snip.lower()
        if any(k and (k in low or (len(low) > 3 and low in k)) for k in keep):
            return
        if cat == "dash" and args.allow_dashes:
            return
        note = ""
        if cat in allow_cats or any(p in low or (len(low) > 3 and low in p) for p in allow_phrases):
            sev, note = "INFO", "allowed by the owner's list"
        elif cat in habit_cats and sev == "REVIEW":
            sev, note = "INFO", "the owner's own habit (found in samples)"
        shown = (context or snip).strip()
        findings.append({"line": n, "severity": sev, "category": cat, "match": shown[:120], "note": note})

    total_words = 0
    for n, l in lines:
        if not l.strip():
            continue
        total_words += len(words(l))
        for cat, sev, rx in P:
            for m in rx.finditer(l):
                record(cat, sev, n, m.group(0))
        for m in EMOJI_RE.finditer(l):
            record("emoji", "HARD" if args.strict else "REVIEW", n, m.group(0))
        if EXCLAIM_RE.search(l):
            record("exclamation", "HARD" if args.strict else "REVIEW", n, "!", context=l.strip()[:80])

    # density rule for fog: below one hit per 500 words (minimum 2) it is INFO
    fog_hits = [f for f in findings if f["category"] == "fog" and f["severity"] == "REVIEW"]
    if fog_hits and len(fog_hits) < max(2, total_words / 500.0):
        for f in fog_hits:
            f["severity"], f["note"] = "INFO", f["note"] or "single use, check it is the exact word"

    # shape checks on prose
    pl = prose_lines(lines)
    prose = " ".join(s for _, s in pl)
    sents = sentences(prose)
    if len(sents) >= 3:
        run = 0
        for idx, s in enumerate(sents):
            if len(words(s)) <= 4:
                run += 1
                if run == 3:
                    findings.append({"line": _line_of(pl, s), "severity": "REVIEW", "category": "staccato", "match": s[:80], "note": ""})
            else:
                run = 0
    lengths = [len(words(s)) for s in sents if words(s)]
    if len(lengths) >= 8:
        mean = statistics.mean(lengths)
        sd = statistics.pstdev(lengths)
        if mean > 0 and sd / mean < 0.3:
            findings.append({"line": 0, "severity": "REVIEW", "category": "even-rhythm", "match": f"mean {mean:.1f} words, spread {sd:.1f}", "note": ""})
    openers = [words(s)[0].lower() for s in sents if words(s)]
    for i in range(len(openers) - 2):
        if openers[i] == openers[i + 1] == openers[i + 2] and openers[i] not in {"the", "a", "you", "i"}:
            findings.append({"line": 0, "severity": "REVIEW", "category": "repeated-opener", "match": f"three sentences start with '{openers[i]}'", "note": ""})
            break
    q = sum(1 for s in sents if s.strip().endswith("?"))
    if total_words and total_words < 400 and q >= 4:
        findings.append({"line": 0, "severity": "REVIEW", "category": "questions", "match": f"{q} questions in {total_words} words", "note": ""})
    paras = [p for p in re.split(r"\n\s*\n", "\n".join(s for _, s in lines)) if p.strip()]
    prose_paras = [p for p in paras if not p.strip().startswith(("#", "|", "-", "*")) and not re.match(r"^\d+[.)]\s", p.strip())]
    if len(prose_paras) >= 6:
        single = sum(1 for p in prose_paras if len(sentences(p)) <= 1)
        if single / len(prose_paras) > 0.7:
            findings.append({"line": 0, "severity": "REVIEW", "category": "one-line-paragraphs", "match": f"{single} of {len(prose_paras)} paragraphs are one sentence", "note": ""})
    trip = len(re.findall(r"\b[\w'-]+(?: [\w'-]+)?, [\w'-]+(?: [\w'-]+)?,? (?:and|or) [\w'-]+\b", prose))
    if total_words >= 150 and trip / max(1.0, total_words / 300.0) > 3:
        findings.append({"line": 0, "severity": "REVIEW", "category": "triplets", "match": f"{trip} lists of three", "note": ""})

    return findings, total_words


def _line_of(pl, sentence):
    probe = sentence[:25]
    for n, s in pl:
        if probe in s:
            return n
    return 0


# ---------------------------------------------------------------------------
# Voice profile
# ---------------------------------------------------------------------------

STOP = set("""a an the and or but if then so of to in on at by for with from as is are was were be been being it its
this that these those i you he she we they me him her us them my your his our their not no do does did have has had
will would can could should just very really than too also into out up down over about more most some any all what
which who whom when where why how there here""".split())


def profile(text):
    lines = prepare(text, scan_quotes=True)
    prose = " ".join(l for _, l in lines if l.strip())
    sents = sentences(prose)
    lengths = [len(words(s)) for s in sents if words(s)]
    w = [x.lower() for x in words(prose)]
    n = max(1, len(w))
    contractions = sum(1 for x in w if "'" in x)
    first = sum(1 for x in w if x in {"i", "me", "my", "i'm", "i've", "i'd", "i'll"})
    you = sum(1 for x in w if x in {"you", "your", "you're", "you've", "you'll"})
    top = Counter(x for x in w if x not in STOP and len(x) > 3).most_common(15)
    opens = Counter(words(s)[0].lower() for s in sents if words(s)).most_common(8)
    return {
        "words": len(w),
        "sentences": len(lengths),
        "sentence_length_median": statistics.median(lengths) if lengths else 0,
        "sentence_length_spread": round(statistics.pstdev(lengths), 1) if len(lengths) > 1 else 0,
        "contractions_per_100_words": round(100 * contractions / n, 1),
        "first_person_per_100_words": round(100 * first / n, 1),
        "you_per_100_words": round(100 * you / n, 1),
        "questions_per_10_sentences": round(10 * sum(1 for s in sents if s.endswith("?")) / max(1, len(sents)), 1),
        "exclamations_per_10_sentences": round(10 * prose.count("!") / max(1, len(sents)), 1),
        "parentheses": prose.count("("),
        "top_words": [t for t, _ in top],
        "common_openers": [t for t, _ in opens],
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser(description="Find AI writing tells in a draft.")
    ap.add_argument("files", nargs="*", help="files to scan, or - for stdin")
    ap.add_argument("--allow", help="file with the owner's allowed phrases and categories")
    ap.add_argument("--keep", action="append", help="exact phrase the owner requires (repeatable)")
    ap.add_argument("--voice", help="writing samples to compare against and learn habits from")
    ap.add_argument("--profile", help="print a voice profile of a samples file and exit")
    ap.add_argument("--strict", action="store_true", help="emoji and exclamation marks are HARD")
    ap.add_argument("--allow-dashes", action="store_true", help="the owner asked to keep dashes")
    ap.add_argument("--scan-quotes", action="store_true", help="also scan block quotes")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args()

    if args.profile:
        with open(args.profile, encoding="utf-8") as fh:
            prof = profile(fh.read())
        if args.json:
            print(json.dumps(prof, indent=2))
        else:
            for k, v in prof.items():
                print(f"{k.replace('_', ' ')}: {v}")
        return 0

    if not args.files:
        ap.print_help()
        return 2

    allow_phrases, allow_cats = load_allow(args.allow)
    habit_cats = set()
    voice_prof = None
    if args.voice and not os.path.exists(args.voice):
        print(f"Note: no samples file at {args.voice}, so the voice check is skipped. Add 2 or 3 pieces the owner "
              "wrote to that file (setup/PROTOCOL.md, stage 1).", file=sys.stderr)
        args.voice = None
    if args.voice:
        with open(args.voice, encoding="utf-8") as fh:
            vt = fh.read()
        voice_prof = profile(vt)
        vf, _ = scan_text(vt, argparse.Namespace(keep=[], allow_dashes=True, scan_quotes=True, strict=False))
        counts = Counter(f["category"] for f in vf if f["severity"] == "REVIEW")
        habit_cats = {c for c, k in counts.items() if k >= 2}

    results = {}
    any_hard = False
    for path in args.files:
        text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        f, wc = scan_text(text, args, allow_phrases, allow_cats, habit_cats)
        f.sort(key=lambda x: ({"HARD": 0, "REVIEW": 1, "INFO": 2}[x["severity"]], x["line"]))
        results[path] = {"words": wc, "findings": f}
        if voice_prof is not None:
            results[path]["draft_profile"] = profile(text)
            results[path]["voice_profile"] = voice_prof
        if any(x["severity"] == "HARD" for x in f):
            any_hard = True

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 1 if any_hard else 0

    for path, r in results.items():
        f = r["findings"]
        hard = sum(1 for x in f if x["severity"] == "HARD")
        rev = sum(1 for x in f if x["severity"] == "REVIEW")
        info = sum(1 for x in f if x["severity"] == "INFO")
        print(f"{path}  ({r['words']} words)")
        seen_fix = set()
        for x in f:
            where = f"line {x['line']}" if x["line"] else "whole text"
            note = f"  [{x['note']}]" if x["note"] else ""
            print(f"  {x['severity']:<7}{x['category']:<20}{where}: \"{x['match']}\"{note}")
            if x["severity"] != "INFO" and x["category"] not in seen_fix:
                print(f"  {'':<7}{'':<20}fix: {FIX.get(x['category'], '')}")
                seen_fix.add(x["category"])
        if voice_prof is not None:
            d, v = r["draft_profile"], r["voice_profile"]
            print("  voice check (draft vs samples):")
            for k in ["sentence_length_median", "sentence_length_spread", "contractions_per_100_words",
                      "first_person_per_100_words", "you_per_100_words", "questions_per_10_sentences"]:
                print(f"    {k.replace('_', ' ')}: {d[k]} vs {v[k]}")
        verdict = "Not ready: fix every HARD finding." if hard else (
            "Ready after review: defend or fix each REVIEW finding." if rev else "Clean.")
        print(f"  Summary: {hard} HARD, {rev} REVIEW, {info} INFO. {verdict}\n")
    return 1 if any_hard else 0


if __name__ == "__main__":
    sys.exit(main())
