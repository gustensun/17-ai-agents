# Ship checklist

Run it on every page before it goes to QA, and once per funnel the day before launch. Most traffic is on a phone, so check mobile first, then open the page on a real phone and tap every button with your thumb.

## Mobile (390px and 320px, plus 768 and 1024)

- [ ] The hero shows what it is, who it's for and the button without scrolling
- [ ] No sideways scroll at 320px
- [ ] Body text at least 16px. Headlines don't break into one word per line
- [ ] Every button and link at least 44px tall, with space between tap targets
- [ ] Buttons full width on mobile
- [ ] Splits stack text first, then image
- [ ] Nothing sits under a fixed bar or overlaps anything else
- [ ] A sticky button (if used) never shows at the same time as another button
- [ ] Forms use the right keyboard (email, tel, number) and autofill
- [ ] The menu is a full-screen panel that says open or closed (website pages only)

## Conversion

- [ ] One job, one action, every main button goes to the same next step
- [ ] The main button is solid, high contrast and the same style everywhere
- [ ] Proof within one scroll of every main button
- [ ] Price block in order: what you get, real value, price, payment options, guarantee, button
- [ ] Every link works. Every form sends. The thank-you page loads after a real submit
- [ ] No fake testimonials, ratings, logos, countdowns or "only 3 left"
- [ ] Every [BRACKET] filled with a real fact (`page_check.py --ship` passes)

## Speed

- [ ] Largest image under 350 KB, all images under 1.2 MB total
- [ ] Images in WebP or AVIF, with width and height set, lazy-loaded below the fold
- [ ] Max 2 font families and 4 font files
- [ ] No layout shift while loading (CLS under 0.1)
- [ ] Lighthouse performance 90 or higher on mobile

## Access

- [ ] Contrast AA: 4.5:1 body, 3:1 large text, including text on photos and coloured sections
- [ ] Visible focus ring on every link, button and field. A skip link
- [ ] One H1, headings in order
- [ ] Alt text on images, visible labels on every field
- [ ] Works with prefers-reduced-motion

## Polish

- [ ] Favicon, page title, meta description, share image
- [ ] Text selection colour, focus rings and scrollbars match the palette
- [ ] Current year in the footer. Privacy, terms and refund policy linked
- [ ] No em dashes, no slop words, no leftover `{{variables}}`
- [ ] Error messages say what to do next and link to where to fix it

## Click-test the funnel

Go through the whole funnel like a buyer, page by page, and fill this table:

| Page | Item | Works (yes or no) | Fix |
|---|---|---|---|

Cover: every button's target, every form (submits, shows success, passes name, email and offer on), what the thank-you page says happens next, links that leak the buyer out of the funnel, the order bump adding to the total, upsell accept and decline both working, and tracking events for page view, opt-in, purchase (with value) and booking.

## The day before launch

- [ ] Page titles, descriptions and share images on every page
- [ ] noindex on thank-you, upsell, downsell and confirmation pages
- [ ] Analytics and pixels installed, with events for opt-in, purchase and booking
- [ ] The opt-in or purchase triggers the right email. Tested with a real address
- [ ] Payments in live mode, one real test purchase made and refunded
- [ ] A 404 page that links back to the main page
- [ ] Domain connected, HTTPS on, www and non-www both work

Going live needs the owner's approval. The QA agent reports pass, fail or "owner needs to check this" for each line.
