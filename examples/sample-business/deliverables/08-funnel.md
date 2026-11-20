# Funnel: the Starter Kit funnel plan

```
Agent: Funnel   Task: Recommend the funnel for the Starter Kit and map every page   Date: 2026-11-19
Status: Draft for approval, revision 1
Used: Brain sections 2, 5, 8 and 10, the approval rules, skills funnel-strategy, funnel-types, funnel-formula, seven-figure-math, conversions-framework
Placeholders to fill: [LINK: sales page], [LINK: order form], [LINK: upsell page]
Decision needed: Yes to this plan? Then the QA fixes go into the sales page as drafts, and they go live after your yes on the pages.
```

Changed after your note ("Add the planner tool as the freebie later, not now."): the printable PDF stays the freebie. The free web tool moves to "Later" at the bottom, after the January group starts, and the Coding demo stays a demo until then.

## The three questions

- **Price point:** $27, so a low-ticket funnel that pays for itself, with the free planner in front.
- **Traffic:** warm now (YouTube, Instagram and the list). Cold later, with ads, once the sales page and the upsell reach target.
- **Launch:** evergreen for the kit. Back in 12 runs live twice a year, with real dates.

## FUNNEL PLAN

```
FUNNEL PLAN: Nap Time Starter Kit
Price point: $27 -> low-ticket funnel (self-liquidating), with the free planner in front
Traffic: warm now, from YouTube, Instagram and the list. Cold later, with ads, once the sales page and the upsell reach target
Launch: evergreen. Back in 12 runs live (doors December 28 to January 8, the group starts January 11)
Why this funnel: A $27 kit is an easy yes for a parent who already watches Dana, so one sales page with a bump and an upsell can sell it. The bump and the upsell lift the average order toward $37, which is what lets ads pay for themselves later. Kit buyers are the people who join Back in 12 and 1:1, so the funnel's real job is to fill that list.
Journey:
  1. Planner opt-in page. Job: trade the planner for an email. Action: "Send me the planner"
  2. Thank-you page. Job: deliver the planner and show the next step. Action: "See the Starter Kit", at the normal $27
  3. Starter Kit sales page. Job: sell the kit. Action: "Get the kit"
  4. Order form with the Fridge Cards bump, $9, never pre-ticked. Job: take the payment. Action: "Start today"
  5. Upsell page: Strong Back Add-On, $47, the same price as everywhere else. Job: offer the next thing they need. Action: "Add it for $47", or the text link "No thanks"
  6. Confirmation page. Job: get workout 1 done today. Action: "Start workout 1"
After each step:
  Opt-in: the planner email right away, a source tag, stage Lead, then the planner emails
  Kit bought: tag bought:starter-kit, stage Won, access through [COMMUNITY]'s own connection to [PAYMENTS], the welcome email
  Bump or upsell bought: tag bought:fridge-cards or bought:strong-back
  The day after buying: stage Onboarding. Day 7: stage Active. Weeks 1 to 4: the onboarding emails
  Week 4: the Back in 12 waitlist email, with one line about 1:1
Next offers: bump Fridge Cards $9, upsell Strong Back Add-On $47, back end Back in 12 ($297 or 3 x $109), then 1:1 ($1,500)
Non-buyers: the planner emails, then one email a week. Downsell: none, because the kit is already $27. YouTube and Instagram keep earning trust
Break-even CPP: $33.38 at this week's numbers, $37 at target
```

Every funnel page has one job and one button, and no menu. The thank-you page shows the kit at its normal price, with no countdown and no "today only".

## The numbers

Run on the week of November 10, with no ad spend. The line that matters from the output:

```
python3 skills/seven-figure-math/scripts/kpi_calc.py check --spend 0 --impressions 13100 --leads 248 --customers 13 --aov 33.38
```

```
If ads start at these rates, break-even is a CPL of 1.75 and a CPP of 33.38.
```

And at the Numbers card targets (60,000 views, 1,000 leads and 60 customers a month, and a $37 average order):

```
python3 skills/seven-figure-math/scripts/kpi_calc.py check --spend 0 --impressions 60000 --leads 1000 --customers 60 --aov 37
```

```
If ads start at these rates, break-even is a CPL of 2.22 and a CPP of 37.00.
```

Assumptions, labeled:

- The rates hold when traffic changes from warm to cold. They usually drop, so the first ad test is small. Analytics sets the size.
- The bump goes to 35% of buyers and the upsell to 15%. This week it was 31% and 8%.
- The script's revenue line is left out, because your reports have no PRIVATE section.

Ads wait until two weeks in a row at 6% lead to kit or better, with the upsell at 15% or better.

## Build sheet: the QA fixes

The funnel is live, so the Funnel Formula starts at Design: Define is the Brain, and Deploy waits for your yes.

| Page | Change | Copy | Design | Automations | Tracking |
|---|---|---|---|---|---|
| Sales page, hero | Headline of 3 lines or fewer at 390px. "Watch a workout" becomes a text link | Copywriter's 3 options | Line count at 390px, one solid button | None | Headline test after launch, 100 visitors per version or more |
| Sales page, first button | Lena's quote and photo under it | Copywriter | Proof within one screen of the button | None | None |
| Sales page, price | The $1,500 anchor above, the guarantee line under the button, the mom of twins' review next to it | Copywriter | Price card with the soft shadow, from the Style block | None | None |
| Sales page, H2s and FAQ | Three claims for the label H2s, Support's FAQ answer 4 word for word | Copywriter | None | None | None |
| Sales page and order form | The [ANALYTICS] code in the page settings | None | None | None | Analytics checks the first visits come through |
| Upsell page | Read it after the sales page fixes, as the second weak spot | Copywriter, next week | Design, next week | None | Upsell rate every Friday |

Handoffs sent: copy to the Copywriter (delivered November 19), layout notes to Design, and the tags and emails to Automations. Design waits for your yes on the copy, and the pages go live only after your yes on the pages. QA tests the drafts on Friday, November 20.

## Later

- **The free web planner as the freebie.** After the January group starts, and after Coding's tested version. It would replace the PDF on step 1, with the same emails behind it.
- **Ads.** After the two weeks at target above.

Saved to `my-business/funnels/starter-kit-plan-2026-11-19.md`.
