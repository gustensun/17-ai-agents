# Fixes by symptom

Find the symptom, paste the matching fix into the build tool, and add a screenshot if the tool takes images (fixes get far more accurate). Fix one problem per message: five fixes in one message come back as five half-fixes. After any fix, check 390px again and rerun the hierarchy test.

| # | Symptom | Fix |
|---|---|---|
| F1 | It looks like every other AI page | [Too generic](#f1-too-generic) |
| F2 | Purple gradients, glass, emoji, icon grids | [AI-made look](#f2-ai-made-look) |
| F3 | Broken or cramped on a phone | [Bad mobile](#f3-bad-mobile) |
| F4 | The first screen doesn't grab anyone | [Weak hero](#f4-weak-hero) |
| F5 | Slow to load, janky scroll | [Slow](#f5-slow) |
| F6 | Doesn't look or sound like the brand | [Off-brand](#f6-off-brand) |
| F7 | People don't click the button | [Weak call to action](#f7-weak-call-to-action) |
| F8 | Too much going on | [Cluttered](#f8-cluttered) |
| F9 | Feels risky or salesy | [Low trust](#f9-low-trust) |
| F10 | Copy reads like a robot wrote it | [Sounds like AI](#f10-sounds-like-ai) |
| F11 | People reach the price and leave | [Weak price block](#f11-weak-price-block) |
| F12 | Forms get started but not finished | [Form friction](#f12-form-friction) |
| F13 | Pages in the funnel don't match | [Inconsistent design](#f13-inconsistent-design) |
| F14 | The builder keeps undoing fixes or drifting | [Builder drift](#f14-builder-drift) |

## F1. Too generic

```
This page could be for any business. Fix it without changing the structure.
1. Hero: rewrite the headline so only the avatar in the Brain would think "this is me". Use their exact words. Name the outcome and the pain.
2. Replace every vague phrase ("grow your business", "take it to the next level") with a concrete outcome.
3. Add at least 2 niche-specific details per section: their tools, their moments, their objections. No invented numbers.
4. Apply the Style Block harder. The named direction should be obvious on the first screen. Use the display font.
5. Add the motif in 2 or 3 places.
Show the before and after for the hero and the 3 most changed sections.
```

## F2. AI-made look

```
The page looks AI-generated. Strip it.
Remove: gradients and gradient text, glass cards, glowing blobs, default purple or blue, emoji icons, small uppercase labels above headings, 01/02/03 section numbers, three-stat strips under the hero, centred-everything layouts.
Rebuild at least half of the equal icon + heading + text card grids as something else: a list with outcome-first lines, a big photo with copy beside it, a comparison, a quote, a simple diagram.
Then: one palette from the Style Block, the accent only on the main button and a few highlights, one card style, one radius scale, real depth (soft shadow with offset, no glow).
List every change.
```

## F3. Bad mobile

```
Fix this page at 390px, then check 320px.
1. Hero: headline 3 lines max, button full width and visible without scrolling. Cut words before you shrink type.
2. No sideways scroll anywhere. Find what overflows and fix it.
3. Stack all splits: text first, image second.
4. Body text 16px or more. Tap targets 44px or more with space between.
5. Tables and comparisons become stacked cards.
6. Nothing hidden under a sticky bar. Only one button on screen at a time.
7. Section padding tighter than desktop, with clear space above every heading.
List each fix and the section it was in.
```

## F4. Weak hero

```
Rebuild only the first screen. It must answer in 5 seconds: what is this, who is it for, what do I get, what do I do next.
Give 3 versions, each with headline, subheadline, button text and a visual idea:
A. Outcome-led: how to [outcome] without [pain].
B. Problem-led: the exact pain.
C. Proof-led: the strongest real proof from the Brain (skip if there is none).
Headline under 10 words if possible. One solid button. The visual shows the real thing (the owner, the product, the result). Nothing else competes on the first screen. Build the one you'd ship and say why.
```

## F5. Slow

```
Make this page fast without changing how it looks.
1. Images: WebP or AVIF, max 2x shown width, largest under 350 KB, width and height set, lazy-load below the fold, preload the hero image.
2. Fonts: 2 families and 4 files max, font-display: swap, preconnect.
3. Scripts: remove unused code, replace heavy libraries used for small effects with CSS, defer third-party scripts.
4. Video, embeds, maps and 3D load only near the screen, with a poster image first.
5. Motion: transform and opacity only.
6. Layout shift under 0.1: reserve space for everything that loads late.
Report page weight before and after, and what you removed.
```

## F6. Off-brand

```
Re-align this page to the Brain and the Style Block.
1. Replace every colour that isn't a Style Block token. 6 max.
2. Only the display and text fonts, with the weights and spacing in the Style Block.
3. Rewrite any line that doesn't sound like the voice samples. Remove every word on the never-say list.
4. Remove imagery that doesn't match the photo style. Use [PHOTO: what] slots where the owner's photos belong.
5. Logo in the header and footer, the motif in 2 or 3 places.
6. Every colour and font comes from CSS variables so it can't drift again.
```

## F7. Weak call to action

```
People aren't clicking. Fix the calls to action.
1. One action: every main button goes to the same next step. Turn competing buttons into text links or remove them.
2. Solid, high contrast (4.5:1 or more), the same style everywhere, 48px tall on mobile.
3. Button text: a verb plus what they get. Give 5 options for the main button.
4. Placement: hero, after the offer or main proof, after the guarantee, and at the end. On long pages, a sticky mobile button after the hero.
5. Next to every main button: one line of real proof or reassurance (testimonial, guarantee, "takes 2 minutes").
6. Remove nav and outbound links on funnel pages.
```

## F8. Cluttered

```
Simplify this page.
1. Cut any section that doesn't move the buyer closer to the one action. Say which you cut and why.
2. One idea per section, one section per screen.
3. 3 type sizes per section max. 2 colours on screen besides the background.
4. Double the space between sections. More space above headings than below.
5. Paragraphs 3 lines or less on desktop.
6. Remove decoration that carries no meaning.
Keep every real proof element and the main button.
```

## F9. Low trust

```
Make this page trustworthy. Never add fake proof.
1. Proof next to every claim and every button, from the Brain. Where there is none, a labelled [TESTIMONIAL: what kind] or [RESULT] slot.
2. A real face: the owner's photo and a short true story near the top or the offer.
3. Remove hype: exclamation marks, all caps, "insane", "guaranteed results", fake urgency, timers that reset.
4. Add the plain facts: what exactly they get, how access works, how to get help, the refund policy, who the owner is.
5. State the guarantee in plain words next to the price, or what happens if it's not a fit.
6. A FAQ that answers the 5 biggest objections honestly.
7. Footer: real business name, contact, privacy, terms and refund links.
```

## F10. Sounds like AI

```
Rewrite the copy so it sounds like the owner. Keep every fact and [BRACKET].
Run the anti-ai-slop-writing skill and its scanner on the copy. Fix every HARD finding.
Add: the owner's voice from the Voice card, the avatar's real words, one specific detail per section, mixed sentence length.
Show the new copy.
```

## F11. Weak price block

```
Rebuild the price section, top to bottom: everything they get (outcome first), real value per item only if true, the price (big and clear), payment plan if offered, one line on why it's priced this way, the button, the guarantee right under it, one real testimonial or a [TESTIMONIAL] slot.
Remove any fake "was" price or fake total value.
Plans: 3 max, with the difference in plain words. Highlight one only if the owner says which.
Answer "is it worth it?" with the cost of not solving the problem, using only facts from the Brain.
On mobile, price, button and guarantee fit on one screen.
```

## F12. Form friction

```
People start the form but don't finish. Fix it.
1. Cut every field that isn't needed now. Opt-in: first name and email. Checkout: only what payment and delivery need.
2. Visible labels above each field. Placeholder text is never the label.
3. The right keyboard on mobile and autofill on every field.
4. Long forms: one question per step, a progress bar, a back button, answers saved between steps.
5. Errors under the field, in plain words, saying how to fix it, checked as they leave the field.
6. The button says what happens: "Get my checklist", "Complete my order".
7. Reassurance next to the button: privacy line, guarantee or how long it takes. Only if true.
8. After submit: a real success state, then the next page.
```

## F13. Inconsistent design

```
The pages in this funnel don't look like one brand.
1. Pull one set of tokens (colours, fonts, sizes, spacing, radius, shadows) from the best page and apply it everywhere.
2. One button style, one card style, one form style on every page.
3. The same header and footer on every page (simplified on checkout and upsell pages).
4. The same words for the same things: offer name, price, guarantee, dates. Flag any page where a fact differs.
5. The same motion rules on every page.
List what changed on each page.
```

## F14. Builder drift

Use when the build tool starts ignoring the rules, undoing fixes or changing things nobody asked for.

```
Stop. Before you change anything else:
1. Re-read the Brain summary, the Style Block and the House Rules (pasted below).
2. List the last 3 changes you made and whether each followed the rules.
3. Undo any change I didn't ask for.
4. From now on, only change what I ask for in each message. If a fix needs a bigger change, ask first.
Reply with the list and "Ready". Don't build yet.
```
