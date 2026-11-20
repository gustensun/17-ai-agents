# Tells: what each scanner category means and how to fix it

Read this after a scan, or when auditing someone's text. Don't read it before the first draft: the examples here are the phrases you're trying not to write.

Section names match the category names in the scanner output.

<!-- slop-scan: off -->

## Judging a REVIEW finding

A REVIEW hit is evidence, and you still make the call. Keep the wording only if it passes all three tests:

1. **Density.** It stands alone. Two or more hits from the same category in a short piece make a pattern, and one of them goes. Fog words need about one hit per 500 words before they're raised as REVIEW. Below that they're listed as INFO, so long pieces aren't punished for ordinary words.
2. **Precision.** It's the most exact word for the thing. "Robust" for a bridge rated to 40 tonnes passes. "Robust" for a newsletter fails.
3. **Voice.** The owner would say it out loud, or it appears in their samples or `my-business/allow.txt`.

Fix by rewriting the thought. Replacing one fog word with a fancier one keeps the empty sentence and adds a second tell.

## The method, in four examples

Remove the slogan, add an observation, expose the mechanism, keep the claim proportional.

| Before | After |
|---|---|
| It's not about creating more content. It's about creating meaningful connections. | Posting twice as often did nothing for sales. Replying to the people already commenting did. |
| Our innovative solution streamlines your workflow and unlocks sustainable growth. | It imports the order, drafts the reply, and puts both in the same inbox. The support team no longer copies customer details between three tabs. |
| Like many entrepreneurs, Sarah felt overwhelmed. Everything changed when she discovered the power of focus. | Sarah had four offers, two half-built funnels, and no clear answer when someone asked what to buy first. She paused three of the offers and sent all new leads to the remaining one. |
| AI is a powerful tool, but it can never replace human creativity. | AI produced 30 usable headlines in five minutes. It could not tell which promise our customers would distrust; the sales-call recordings could. |

The "after" lines need facts. If the owner hasn't supplied them, write a placeholder.

## HARD categories

### artifact
Leftovers from a chat session: citation tokens (oaicite, contentReference, turn0search0, [cite: 1]), tracking parameters such as utm_source=chatgpt.com, knowledge-cutoff disclaimers, "as an AI language model", "I hope this helps", "Certainly! Here's". Delete them. These are the only conclusive tells.

### contrast
Defining a thing by what it isn't: "It's not X. It's Y", "not just X but Y", "less like a tool and more like a partner", "more than an X, it's a Y", "the real problem isn't X", "you don't need more X, you need Y", "not because X, but because Y". This is the most overused generated structure. State the positive claim alone. Keep a contrast only when the reader really holds the first belief and you can say who told them.

- Before: "This isn't a course. It's a system."
- After: "You get 14 templates and a weekly call. There are no video lessons."

### pivot
Announcing information before giving it: "Here's the thing", "Here's why:", "The result?", "The best part?", "And honestly?", "Then everything changed", "Fast forward to", "Make no mistake". Delete the announcement and join the question to its answer.

- Before: "The result? Burnout."
- After: "I burned out in week six."

Some owners use one of these on purpose (a signature "The best part?" for example). That goes in `my-business/allow.txt`, and the scanner then lists it as INFO.

### bait
Lines written for the feed algorithm: "Agree?" or "Thoughts?" as a last line, "Comment GUIDE and I'll send it", "Follow for more", "Unpopular opinion:", "what nobody tells you", "Let that sink in", "Read that again", "Save this for later". Remove them unless the owner explicitly requires the call to action (then pass it with --keep).

### opener
First lines that fit any topic: "In today's fast-paced world", "In the ever-evolving landscape of", "Have you ever wondered", "Let's dive in", "I hope this email finds you well", "Imagine a world where", "Now more than ever". Start on the fact, the event or the decision.

### closer
Last lines that fit any topic: "In conclusion", "At the end of the day", "The choice is yours", "The key takeaway is", "Take the first step today", "You've got this", "Only time will tell", "Please don't hesitate to reach out", "One thing is certain". End on the last useful fact or the concrete next action.

### dash
Em dashes, and en dashes outside number ranges. Readers treat them as a signal, and the house rules ban them. Use a comma, a period, a colon or parentheses. For ranges, use a hyphen: 3-5.

### leftover
A template variable that was never filled, like {{first_name}}. Fill it, or turn it into a [BRACKET] placeholder the owner can see.

## REVIEW categories: wording

### fog
Abstract business words that sound like meaning: unlock, unleash, empower, elevate, leverage, utilize, foster, facilitate, navigate, harness, streamline, robust, seamless, holistic, impactful, innovative, cutting-edge, transformative, synergy, landscape, ecosystem, realm, tapestry, catalyst, cornerstone, pivotal, myriad, plethora, delve, testament, meticulous, embark, paradigm, bespoke, curated, supercharge, next-level, world-class, best-in-class, state-of-the-art. Rewrite the sentence around the concrete action, number or mechanism.

- Before: "We leverage AI to streamline your onboarding."
- After: "New clients fill in one form. The AI turns it into the welcome email, the project board and the first call agenda."

### hype
Words bigger than the evidence: insane, crazy, mind-blowing, jaw-dropping, skyrocket, explode, massive, epic, secret sauce, game-changing, revolutionary, life-changing, unbelievable, guaranteed results, overnight success, on autopilot, 10x your. Use the number or the result instead, and let the reader judge the size.

- Before: "This funnel will skyrocket your sales."
- After: "The same traffic bought 41 times in March, up from 17 in February, after we moved the price under the headline."

### outcome
Results with no unit: "drive meaningful results", "deliver real value", "gain a competitive edge", "maximize ROI", "future-proof", "tailored to your unique needs", "a powerful combination", "sustainable growth", "take it to the next level". Name the observable result and how it's measured, or cut the claim.

### profundity
Maxims everyone agrees with and nobody learns from: "Consistency is key", "Clarity is everything", "Every challenge is an opportunity", "Success starts with...", "Small changes create big results", "The best products solve real problems". Replace the maxim with the specific lesson from this situation.

### engagement
Stock friendliness: "You're not alone", "We've got you covered", "Whether you're a beginner or an expert", "No matter where you are on your journey", "Ready to get started?", "If that sounds familiar", "Let's unpack". Cut it, or ask a question only when the answer matters.

### salesy
Template sales lines: "Struggling to...", "Tired of...", "What if you could...", "Say goodbye to...", "Finally, a...", "Designed with you in mind", "Everything you need, all in one place", "Work smarter, not harder", "Your journey starts here", "No more X. No more Y." Describe the buyer's real situation in their words instead. Some of these work when they name a specific moment ("Tired of rewriting the same proposal every Sunday night?"), and some owners use them on purpose, which is what `allow.txt` is for.

### support
Stock service lines: "Thank you for bringing this to our attention", "We understand how frustrating this must be", "Rest assured", "We appreciate your patience", "At your earliest convenience", "I wanted to reach out". Open with the reason for the message, then the answer and the steps.

### urgency
Pressure without a fact: "Act now", "Limited time only", "Hurry", "Before it's too late", "Selling out fast", "Only 3 spots left", "Won't last long". Only state urgency that's real, with the actual date or number from the Brain. Fake scarcity breaks house rule 1.

### dash-substitute
A spaced hyphen used as a dash, like "fast - and cheap". Use a comma, a period or a colon.

### exclamation and emoji
Energy borrowed from punctuation. Let the sentence carry it. Keep them only when the owner writes this way and the format suits it. With --strict they're HARD.

### contrast (soft)
"Not only X but also Y" is a REVIEW finding because it's sometimes the plainest way to say two things. If one of the two things is the point, say that one.

## REVIEW categories: rhythm and shape

These look at the whole text, so the line number is often "whole text".

### staccato
Three or more very short sentences in a row ("No fluff. No filler. Just results."). Join them or vary them. In spoken scripts this can be fine.

### even-rhythm
Sentence lengths are too similar across the piece. Let important points run longer and small ones stay short.

### one-line-paragraphs
Most paragraphs are one sentence. Group related sentences into paragraphs of two to four, unless the format is a script or a short caption.

### repeated-opener
Three sentences in a row start with the same word. Vary the openings, or merge the sentences into a list if they really are parallel.

### questions
Four or more questions in a short piece. Answer them, or keep only the one the reader is really asking.

### triplets
Many lists of exactly three. Use the number of items that really exist. Two strong points beat three overlapping ones.

## INFO

### placeholder
A bracketed fact the owner still has to fill in, like [PRICE] or [RESULT: X in Y days]. Listed so nothing ships with a gap. List every one at the end of the deliverable.

<!-- slop-scan: on -->

## Adding a new tell

1. Confirm it's a pattern: it appeared in at least two drafts, from at least two different prompts.
2. Add it to the matching list in `scripts/slop_scan.py` with a category and a severity. HARD is for patterns that are wrong in every context. REVIEW is for patterns that are sometimes the right words.
3. Add one before and after example to its section here, inside the scanner-off region.
4. Run `python3 tools/check_repo.py` to make sure the repo still passes.
