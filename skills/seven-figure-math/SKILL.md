---
name: seven-figure-math
description: Reverse engineer prices and goals into KPIs with the four levels of 7 Figure Math (Reach, Conversions, Sales, Ascend), the Profit Maximizer value ladder and the old way versus new way funnel math. Use when setting goals, pricing a funnel, planning ad spend, reading weekly numbers or deciding which part of the funnel to fix next.
---

# 7 Figure Math

Reverse engineer your prices and goals into KPIs before you build anything. The numbers tell you which page to build, what you can afford to pay for a customer, and which part of the funnel to fix first.

## The four levels

| Level | Example volume | Measured by | What moves it |
|---|---|---|---|
| Reach | 1,000,000 impressions | Cost per mille (CPM) | Content, hooks, ad creative, audience |
| Conversions | 10,000 leads | Cost per lead (CPL) | Lead magnet, opt-in page, offer angle |
| Sales | 1,000 customers | Cost per purchase (CPP) | Offer, sales page, order form, bump, upsells |
| Ascend | 100 clients | Cost per client | Onboarding, results, back-end offer, sales calls |

The example ratios: 1% of impressions become leads, 10% of leads become customers, 10% of customers become clients. Every business has its own ratios. Use the example only until you have real numbers.

## Old way: why cashflow is everything when scaling

| Step | Cost | Result |
|---|---|---|
| Ad | $5 per click | Visitor |
| Landing page | $30 per opt-in | Lead |
| Order form | $300 per sale | A $30 customer |
| Call | $2,700 per client | A $3k client |

The math doesn't work. Spend $3,000 and get 100 leads, 10 customers and 1 client: $300 profit. Add expenses and you're losing money.

## New way: make the numbers work in your favor

| Step | Cost | Result |
|---|---|---|
| Ad | $5 per click | Visitor |
| Landing page | $50 per order | Customer |
| Upsells | $50 average order value | Repeat buyer |
| Back-end sale | $0 per client | Free $3k clients |

Spend $3,000 and get 60 customers at break-even plus 1 client: $3,000 profit. You can now scale ad spend, because the funnel breaks even and every client is free.

The rule behind it: build the front end so customers pay for their own ads (a low-ticket offer with an order bump and upsells), and back-end clients cost close to nothing. Whoever can afford to spend the most to get a customer wins the market.

## The Profit Maximizer: ascend people from leads

| Step | Price | Its job |
|---|---|---|
| Freebie | Free | Get leads and build trust. A free tool beats a PDF. |
| Low ticket offers | $1 to $100 | Impress them so they want more |
| Automated offers | $100 to $1,000 | Scale with a mass market offer |
| Back-end offer | $1,000 to $10K+ | Direct access and more help |

Each step should be the obvious next move after the one before it. The back end sells best to people who already got a win from a cheaper step.

## Plan with the calculator

```
python3 skills/seven-figure-math/scripts/kpi_calc.py plan --goal 100000 --aov 50 --backend 3000 \
    --ascend 0.02 --lead-to-sale 0.10 --reach-to-lead 0.01
```

It prints the volume needed at each level and the break-even targets: CPP at or under the average order value, the CPL and CPM that match, and the back-end revenue on top. To check a test or a past month:

```
python3 skills/seven-figure-math/scripts/kpi_calc.py check --spend 3000 --leads 100 --customers 10 \
    --aov 30 --clients 1 --backend 3000
```

That example prints the old way above: $300 result, $2,700 net cost per client. Swap in `--customers 60 --aov 50` and it prints the new way: break-even front end, $0 net cost per client.

No ads yet? Use `--spend 0`. It shows the rates (reach to lead, lead to sale) and the break-even CPL and CPP for the day ads start.

## Use it

1. **Set the Numbers card** in the Brain: the goal (Q6), prices from the value ladder, the four target volumes and the break-even CPP. Show the owner and get one approval.
2. **Weekly** (Analytics agent): actual against target for each level. Use the four-level table to show it.
3. **Fix the weakest level first**, in order from the top. A sales page can't fix missing traffic, and more traffic makes a broken offer lose money faster.
   - Reach low: more content, new hooks, new angles (Content, Creator and Copywriter agents).
   - Conversions low: a better lead magnet or opt-in page (Funnel and Design agents).
   - Sales low or CPP above the average order value: the offer, the price block, an order bump or an upsell (Copywriter and Funnel agents).
   - Ascend low: onboarding, the first win, follow-up and sales calls (Support, CRM and Sales agents).
4. **Raise the average order value before the ad budget.** A bump and one upsell often turn a losing front end into a break-even one.

## Rules

- These are planning numbers, never promises. Any example shown to customers carries the line "Results vary. These numbers are an example, not a guarantee."
- Revenue and profit are private. Agents use them for decisions and keep them out of public content and outside tools.
- Ad spend changes need the owner's approval, every time.
