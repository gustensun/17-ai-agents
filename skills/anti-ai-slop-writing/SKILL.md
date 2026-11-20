---
name: anti-ai-slop-writing
description: Write, rewrite or audit any copy so it reads as specific and written by the owner, for posts, emails, sales pages, ads, scripts, DMs and articles. Use it as the final pass on every piece of copy before it goes to the owner. Not for offer, funnel or framework strategy.
---

# Anti AI slop writing

Produce writing that only this owner could have written, about this subject, for this reader. Better writing is the goal, and getting past a detector is a side effect at most. Apply the skill silently: the owner gets the writing, without a report on how it was cleaned.

One test governs every sentence: could it have been written for almost anyone, about almost anything? If yes, replace it with the specific thing or cut it.

## How this skill is built

- Word-level tells change with every model release, so the phrase lists live in `scripts/slop_scan.py` and the script checks them. Don't memorize them.
- Naming a phrase to avoid makes a model more likely to write it. Draft from the positive rules below. Don't open [references/tells.md](references/tells.md) until a first draft exists, and never paste phrase lists into prompts for other agents.
- Structure outlasts vocabulary: even sentence lengths, staged reveals, tidy groups of three. The script measures those too.

## Workflow

1. **Brief.** Settle five things from the request, the Brain and the conversation: the reader, the one job of the piece, the claim in one sentence, the evidence you have (numbers, names, dates, quotes, what happened), and where the voice comes from (the Voice card in `my-business/BRAIN.md` and `my-business/voice-samples.txt`).
2. **Fill gaps honestly.** Where a fact is missing, write a bracketed placeholder such as `[RESULT: X leads in Y days]`. For selling copy (sales pages, ads, offer emails), if the offer, the avatar, the proof or the price is missing from the Brain, ask one round of up to five questions first. If the owner says "just write it", use placeholders and state your assumptions in one line.
3. **Load what applies.** Read the matching section of [references/formats.md](references/formats.md). Read [references/voice.md](references/voice.md) when samples exist or the owner asks for their own voice.
4. **Draft** from the drafting rules. When another skill already shaped the draft (for example the 17P sections), keep its structure and start at step 5.
5. **Scan.** Save the draft to a file and run the scanner (commands below). Add `--keep "exact phrase"` for each phrase the owner requires. For text under about 60 words, skip to step 7.
6. **Fix.** Rewrite every HARD finding. Keep a REVIEW finding only if it's the precise word, sounds like the owner, and isn't part of a cluster. When a fix is unclear, read that category in [references/tells.md](references/tells.md). Rewrite the thought: a synonym for a flagged word leaves the same empty sentence.
7. **Read through** against the questions below.
8. **Rescan** after any edit.

Done when the scan reports zero HARD findings, each remaining REVIEW finding can be defended in one sentence, and every read-through question passes.

## Drafting rules

1. Open on the most specific true thing available: a number, a moment, a decision, a named person.
2. Say what the thing is, with no warm-up about what it isn't. Where the logic turns, write "but".
3. Give the mechanism behind each claim: what causes what, and how the reader could check.
4. Take a position. Choose, rank, and name what the choice costs.
5. Use the literal phrase. Write "is" and "has". Call each thing by one name throughout.
6. Show stakes through consequences (money, time, what broke) and let the reader judge the importance.
7. Let the content set the shape. List as many items as exist, give big points more room than small ones, and add headings or bullets only where a reader would scan.
8. Write the way the owner talks: their contractions, first person, direct address, casual qualifiers, the occasional aside in parentheses.
9. Keep real texture: the inconvenient fact, the failed first attempt, the partial result, the exact words someone used.
10. Match intensity to the event. A small fix gets a plain sentence.
11. Stop on the last useful fact or instruction.

## Read-through questions

- **Swap:** could a competitor publish this under their own name unchanged?
- **Mechanism:** does each claim say how or why?
- **Judgment:** is there a position someone could disagree with?
- **Truth:** does every number, quote and result come from the Brain, the owner or a cited source?
- **Voice:** read aloud, would the owner say this to a customer?
- **Ending:** does it stop on substance?
- **Deletion:** which sentence could go with no loss? Cut it.

## Modes

- **Write:** the full workflow.
- **Rewrite:** keep the owner's facts, claims, order and rough length. Where a line is generic because the detail is missing, insert up to three bracketed placeholders instead of inventing.
- **Audit** (the owner wants critique, not new copy): run the scan, read [references/tells.md](references/tells.md), then report findings by severity. Lead with the biggest substance problem, because missing specifics outweigh any phrase. Report a repeated pattern once, with a count. The shape of each finding:

```
HARD, line 3: "<quoted line>"
Pattern: says what the thing isn't before saying what it is.
Rewrite: "<replacement built from the owner's facts>"
```

## Hard rules

- Never invent facts, numbers, quotes, testimonials, anecdotes or experience.
- Never fake humanity with planted typos, fake hesitation or forced slang.
- No em or en dashes in delivered copy, unless the owner asks to keep them (then scan with `--allow-dashes`).
- Phrases, keywords, legal text, calls to action and quotes the owner requires stay word for word, even when the scan flags them.
- Keep the owner's real quirks. A flagged pattern that appears in their samples, or in `my-business/allow.txt`, is theirs.
- Deliver only the writing, with the standard header from brain/CORE.md. No process notes and no offer of more versions. One closing line may list the placeholders that need the owner's facts.

When rules conflict, rank them: truth, the owner's explicit requirements, the owner's voice, specificity, clarity, brevity, polish.

## The owner's devices

The scanner flags patterns that are common in generated text, and some of them may be part of the owner's real voice: a question they always ask, a three-step way of teaching, a line their audience knows them for. During setup the COO asks about these and saves them in `my-business/allow.txt`, one per line. An entry is an exact phrase, or `category:salesy` for a whole category. The scanner then lists them as INFO. Keep them at about the rate the owner uses them. Dashes and invented proof never become allowed.

## Scanner commands

```
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --allow my-business/allow.txt draft.md
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --voice my-business/voice-samples.txt draft.md
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --profile my-business/voice-samples.txt
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --keep "exact phrase" draft.md
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --strict draft.md
python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --json draft.md
```

- `--strict` makes exclamation marks and emoji HARD. Use it when the Voice card says the owner never uses them.
- The exit code is 1 while any HARD finding remains, so other scripts can block on it.
- Skipped: fenced code, inline code, links, HTML comments, block quotes (customer quotes stay word for word; add `--scan-quotes` to include them) and anything between `<!-- slop-scan: off -->` and `<!-- slop-scan: on -->`.
- It needs Python 3 and nothing else. On Windows, use `python` or `py` instead of `python3`.

## Keeping it current

New tells show up with new models. When the owner or an agent spots the same one twice, add it to the patterns in `scripts/slop_scan.py` (a regular expression, a category and a severity), add a line to that category in [references/tells.md](references/tells.md), and run `python3 tools/check_repo.py`.
