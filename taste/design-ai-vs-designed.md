# Design: generated or designed

A page that looks generated loses trust before anyone reads a word. This file shows what "generated" looks like, what a designed page does instead, and the same hero three ways. The rules and the test are in [skills/conversion-design](../skills/conversion-design/SKILL.md). This is the picture to keep in your head while you use them.

## The same hero, three ways

The offer from [copy-bad-vs-great.md](copy-bad-vs-great.md): a done-for-you content and email service for coaches, consultants and service providers.

### A. Generated

> - A purple-to-blue gradient behind everything, and a glowing blob behind the headline.
> - A pill label above the headline: "AI-POWERED".
> - Gradient text in the headline: "Supercharge Your Growth".
> - Everything centred, with two buttons of equal weight: "Get Started" and "Learn More".
> - Three stats under the hero: "10x", "500+", "24/7".
> - Then a row of three equal cards, each with an emoji icon.

Nothing on this screen says what the service is, who it's for or what happens next, so no reader can tell whether it's for them.

### B. Clean

- One palette from the Style block on a plain background. The accent colour sits on the button only.
- A left-aligned headline that says the offer, 3 lines or fewer on a phone.
- One solid button, "Get a free 15 minute call", and a text link for people who'd rather send a message.
- A real photo of the owner.

It's clear and honest. But the reader still has to imagine the product.

### C. Designed

- Everything in B, plus the real deliverable on the first screen: one week of a client's content calendar, filled in, with one email open beside it.
- One proof element within a screen of the button: a client quote with a name and a result, or a labelled [TESTIMONIAL] slot.
- One motif from the owner's world that repeats down the page, for example an editor's margin notes in the accent colour.
- One signature motion moment: the calendar fills in once as the page loads. Everything else stays still.
- Read alone, the H1 and the H2s tell the whole argument.

## Generated or designed, element by element

| Element | Looks generated | Looks designed |
|---|---|---|
| Colour | Purple or blue gradients and glows | One palette from the Style block, with the accent on the button and up to two highlights |
| Headline | Gradient text and a vague verb | Solid colour, and the offer or the result in the reader's words |
| Above headings | A small uppercase label over every heading | The heading carries the section. At most one hero pre-headline, when it calls out the reader |
| Layout | Everything centred, every section the same height | A strong left edge, with sections sized by importance |
| Cards | Rows of three equal cards: icon, heading, two lines | One row of cards at most. Lists, photos, quotes, comparisons and diagrams instead |
| Icons | Emoji, or a mix of icon sets | One icon set with one stroke weight, or no icons |
| Numbers | Three neat stats under the hero | Real numbers inside the sentence they prove, or [BRACKETS] |
| Photos | Stock people smiling at laptops | The owner, the product and the real work, or a labelled box until the asset exists |
| Proof | Logos without permission, star ratings, "trusted by thousands" | Named testimonials with results, within a screen of each button |
| Buttons | Two or three styles, "Get Started", "Learn More" | One solid style, with a verb and what they get |
| Motion | Everything fades and floats in | One hero entrance, one signature moment, small hover feedback |
| Type | A system font for the headline and many sizes | A display face with character, and three levels per section |

## App screens and dashboards

The same standard, for the Coding agent.

| Moment | Looks generated | Looks designed |
|---|---|---|
| Empty state | "No data" | What goes here, why it's empty and the button that fills it: "No leads yet. Connect your form to start collecting them." |
| Error | "Something went wrong" | What happened, what to do and a link to the place to do it |
| Loading | A spinner with no end | A skeleton of the real layout, and a message if it takes more than a few seconds |
| Forms | Placeholder text used as the label | A visible label, the right keyboard on phones and errors under the field |
| Navigation | A new layout on every screen | The same menu in the same place, with the current page marked |
| Demo data | Lorem ipsum and "John Doe" | Sample data that looks like the owner's business, marked as sample |
| Actions | Five buttons with equal weight | One primary action per screen |

## Before you hand it over

- The hierarchy test in [conversion-design](../skills/conversion-design/SKILL.md) passes at 390px and 1440px.
- `page_check.py` shows 0 FAIL.
- Squint at the screenshot. You can name the headline, then the proof or the main visual, then the button, in that order.
