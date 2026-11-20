# Analytics: the first scorecard

```
Agent: Analytics   Task: First scorecard for the Starter Kit funnel, week of November 10   Date: 2026-11-17
Status: Draft for approval, revision 1
Used: Brain section 2 (Numbers card), skills seven-figure-math, funnel-flywheel, outlier-research
Placeholders to fill: [LINK: page settings in [FUNNEL SOFTWARE]]
Decision needed: none
```

Changed after your note ("Say what 5.2% means in customers."): every rate now says what it means in people.

```
SCORECARD: week of November 10   Sources: [CHANNELS], [CRM], [PAYMENTS], November 10 to 16, against November 3 to 9
Level        Actual                                        Target    Last week
Reach        13,100 views (YouTube 8,900, Instagram 4,200)  13,950    12,400
Conversions  248 planner leads, no ad spend                233       210
Sales        13 kit customers, AOV $33.38                  14, $37   12, $33.92
Ascend       0 new 1:1 clients, Back in 12 waitlist 41     0.5       0, waitlist 35
Content: best: the YouTube follow-along nap-time kettlebell workout, 2.6 times the channel median
         weakest: the Instagram post answering protein questions, 0.4 times the median
Weakest number: Sales, lead to kit 5.2% against 6%. Fix: the sales page fixes from QA's audit, owner Funnel, due November 24
Alerts: the upsell was taken by fewer than 1 in 10 buyers for the second week in a row
PRIVATE, owner only: off. You chose to keep revenue and profit out of your reports (setup answer 3)
```

Weekly targets are the monthly Numbers card divided by 4.3.

## What the numbers mean

- **Reach is 6% under target, and leads are 6% over.** 1.89% of views became a planner lead, so traffic isn't what's holding sales back this week.
- **Lead to kit is 5.2%, so 13 of 248 leads bought.** At 6%, the same 248 leads would have been 15 customers, 2 more than this week.
- **The bump went to 4 of 13 buyers (31%)**, against 35%. At 35% it would have been 5 of 13, 1 more.
- **The upsell went to 1 of 13 buyers (8%)**, against 15%. At 15% it would have been 2 of 13. Last week was 1 of 12, so the upsell is the second weak spot.
- **The average order is $33.38**, against $37. The bump and the upsell close that gap, so the fixes start on the sales page and then move to the upsell page.

## Weakest number and the one fix

Sales: 5.2% of leads buy, against 6%. QA audits the kit sales page today. Its top 3 fixes go to the Copywriter and Funnel, and they go live after your yes. Owner: Funnel. Due: Tuesday, November 24. I'll compare the week after the fixes with this one.

## The check script

Run with the week's numbers and no ad spend:

```
python3 skills/seven-figure-math/scripts/kpi_calc.py check --spend 0 --impressions 13100 --leads 248 --customers 13 --aov 33.38
```

```
7 FIGURE MATH: CHECK
No ad spend in this period (organic only), so there is no CPM, CPL or CPP to check.
The rates below still show where people drop off.
Reach to lead: 1.89% of 13,100 views or impressions
Leads: 248   Lead to sale: 5.2%
Customers: 13   Average order value: 33.38
If ads start at these rates, break-even is a CPL of 1.75 and a CPP of 33.38.
```

The script also prints a revenue line. It's left out here, because your reports have no PRIVATE section.

If ads started today, each lead could cost at most $1.75 to break even. At the targets (6% and $37), that rises to $2.22, and the Numbers card's cost target of $2.20 sits just under it. Ads can wait until the sales page and the upsell are closer to target.

## Missing numbers

- **Sales page visits.** [ANALYTICS] isn't on the sales page or the checkout, so I can't see where people leave between the page and the order form. Fix: paste the tracking code into the page settings in [FUNNEL SOFTWARE] ([LINK: page settings in [FUNNEL SOFTWARE]]). Steps: [setup/install.md](../../../setup/install.md#connect-your-tools).
- **Email clicks for the planner emails.** These come from the CRM agent's Friday report. The first one is due November 20.

Saved to `my-business/reports/scorecard-2026-11-17.md`.
