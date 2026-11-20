---
name: conversion-design
description: Design, build or review pages that convert and look made by a real studio, including landing pages, sales pages, opt-ins, order forms, upsells, thank-you pages and websites. Covers the House Rules, 20 named visual directions, the Style Block, the hierarchy test with pass or fail checks, a page checker script and the ship checklist. Use for every page or funnel build, redesign or design review.
---

# Conversion design

Every page has two jobs: look like a real studio made it, and move one reader to one action. This skill turns both into a process with a test at the end, so the hierarchy is right every time and nothing ships on taste alone.

It's built from the traits shared by the 124 funnel templates in [galleries/funnel-templates-124.md](../../galleries/funnel-templates-124.md), the House Rules that kept those pages consistent, and the rules the best open design skills agree on (listed in [ai-skills/README.md](../../ai-skills/README.md)).

## Read first

- From `my-business/BRAIN.md`: the avatar, the offer, the proof bank, the voice, and the Style block (section 10) if it exists.
- The page's place in the funnel: [funnel-types](../funnel-types/SKILL.md) lists the pages of each funnel.
- The persuasion order: [purchase-decision-journey](../purchase-decision-journey/SKILL.md) for the beliefs this page must create, [17p-sections](../17p-sections/SKILL.md) for the section menu.

## Workflow

1. **Page plan.** Write the page's one job, the reader's awareness level, the sections in order (chosen from the 17P menu, never all of them by default), the one call to action and where proof sits. Five to ten lines.
2. **Style Block.** If the Brain has one, use it. If not, follow "Pick a direction" in [references/directions.md](references/directions.md): offer three named directions, recommend one, and ask the owner to approve. Save the approved Style Block to the Style block in section 10 of the Brain. It's reused on every page after this.
3. **Copy before layout.** Get the real copy from the Copywriter (17P sections, CONVERSIONS check, anti-slop pass). Design around real words. Placeholder text hides hierarchy problems.
4. **Build** with the House Rules in the build tool's rules file or project instructions ([references/house-rules.md](references/house-rules.md)). Tokens for every colour and font, mobile first at 390px.
5. **Motion.** One entrance on the hero, one signature moment, small hover and press feedback. Guardrails are in [references/directions.md](references/directions.md#motion).
6. **Hierarchy test.** Run Part A and Part B below. Fix every fail and test again.
7. **Ship checklist.** Run [references/ship-checklist.md](references/ship-checklist.md), then hand to the QA agent, who runs the hierarchy test again independently.

When something looks wrong and you can't name it, find the symptom in [references/fixes.md](references/fixes.md).

## The hierarchy test

A page passes only when every check passes at both 390px and 1440px wide. Each check is pass or fail with evidence. "Looks fine" is not evidence.

### Part A: code checks (script)

```
python3 skills/conversion-design/scripts/page_check.py --funnel path/to/page.html
python3 skills/conversion-design/scripts/page_check.py [YOUR PAGE URL]
```

Leave out `--funnel` on a website home page that needs a menu. Add `--ship` on launch day so leftover [BRACKETS] fail. The script checks one H1, heading order, eyebrow labels, competing buttons, weak button text, dashes, emoji, leftover variables, alt text, form labels, gradient text, font count and token contrast. It also prints the H1 and H2 outline for check B3. Contrast pairs: `page_check.py contrast "#fff" "#111"`.

### Part B: screenshot checks

Take screenshots at 390 x 844 and 1440 x 900, first screen and full page. If your tool can open a browser, take them yourself. If it can't, ask the owner for a phone and a desktop screenshot.

| # | Check | Passes when |
|---|---|---|
| B1 | Squint | Blur the screenshot or step back. You can name, in order: the headline, then the proof or main visual, then the button. If two things fight for first place, shrink one. |
| B2 | Hero in five seconds | The first screen shows what it is, who it's for, what they get and the button, without scrolling, at both widths. The headline is 3 lines or fewer at 390px. |
| B3 | Skim | Read only the H1 and H2s (the script prints them). They tell the argument in order. Each H2 is a full claim its section proves ("Most people avoid the dentist for the same five reasons."), never a label like "Features" or "Testimonials". |
| B4 | One action | One solid button style. Every main button goes to the same next step. At most one solid button per screen. Secondary actions are text links. |
| B5 | Scale steps | Three type levels per section at most: heading, body, small. Each level at least 1.25 times the next. Body 16 to 18px. H1 at least 2.25 times body at 390px and 3 times at 1440px, never above 6rem. |
| B6 | Accent | The accent colour appears only on the main button and up to two highlights per screen. |
| B7 | Spacing | More space above a heading than below it (about 1.5 times). Space between sections at least twice the space inside them. Related items sit closer than unrelated ones. |
| B8 | Reading path | A strong left edge. Text is left-aligned, except short centred lines of two lines or fewer. Equal left and right page edges. No sideways scroll at 320px. |
| B9 | One focal point | Each section has one lead element: a photo, the product, a diagram or a big type moment. At most one row of equal cards on the whole page. |
| B10 | Proof next to claims | A proof element, or a labelled [TESTIMONIAL] slot, within one screen of every main button. Numbers sit inside the sentence they prove. |
| B11 | Readable | Body text 16px or more, lines of 65 to 75 characters on desktop, AA contrast (4.5:1 body, 3:1 large text), including text on photos and coloured sections. |
| B12 | No scaffolds | No eyebrow labels above section headings (a hero pre-headline that calls out the reader in a full phrase is fine), gradient text, glass cards, glowing blobs, emoji icons, decorative 01/02/03, three stats under the hero, stock people posing as customers or centred-everything layouts. |

### Report

```
HIERARCHY TEST: [page name], 390 and 1440
A  Code checks: 0 FAIL, 2 WARN (glass on sticky bar: kept, it sits over photos)
B1 Squint: PASS. Headline, then product shot, then button.
B4 One action: FAIL. Two solid buttons in the hero. Fix: the second is now a text link.
...
Result: FAIL (1). After fixes: PASS on all 12.
```

## Starting numbers

These come from the templates and are a safe start for any Style Block. Change them only with a reason.

- Body 16 to 18px, line height 1.5 to 1.65. Headings line height 1.0 to 1.15, tracking -0.02 to -0.03em, `text-wrap: balance`.
- H2 around `clamp(34px, 4.2vw, 56px)`. H1 one clear step above it.
- Content width 1200 to 1280px. Side gutters `clamp(20px, 4.5vw, 72px)`.
- Buttons 48 to 52px tall, one radius scale for the whole page (for example 12, 22 and 36px, or all square).
- Entrance easing `cubic-bezier(.16, 1, .3, 1)`, 600 to 1000ms. Hovers 150 to 250ms.
- One section per screen, generous space, a soft shadow with an offset when depth is needed (never a glow).

## Rules that override taste

- The owner's approved Style Block and brand assets win over any default in this skill.
- Real proof only. Missing prices, results, testimonials, logos, ratings and dates stay in [BRACKETS] until the owner fills them.
- Light or dark is chosen from where and when the reader sees the page, never from the industry.
- References are for structure and mood. Never copy words, images, logos or code from another site.
- Every error state on a page says what went wrong and what to do next, with a link to the place to fix it.

## Handoffs

- Copy comes from the Copywriter. Page plans for whole funnels come from the Funnel agent.
- The Coding agent builds what can't be built in the page tool. The QA agent runs the hierarchy test and the ship checklist before anything goes live.
- Going live, connecting a domain or turning on payments always needs the owner's approval.
