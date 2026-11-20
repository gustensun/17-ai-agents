#!/usr/bin/env python3
"""kpi_calc.py: turn a revenue goal and prices into the KPI targets of 7 Figure Math.

Plan a goal (works backwards from revenue):
  python3 skills/seven-figure-math/scripts/kpi_calc.py plan --goal 100000 --aov 50 --backend 3000 \
      --ascend 0.02 --lead-to-sale 0.10 --reach-to-lead 0.01

Check a test or a past month (works forwards from ad spend):
  python3 skills/seven-figure-math/scripts/kpi_calc.py check --spend 3000 --leads 100 --customers 10 \
      --aov 30 --clients 1 --backend 3000

Organic only (no ads): use --spend 0 to see the rates and the break-even targets for later.

All money is in one currency, whatever the owner uses. Rates are decimals: 0.10 means 10%.
These are planning numbers, never promises. Python 3 standard library only.
"""

import argparse
import sys


def money(x):
    return f"{x:,.2f}"


def plan(a):
    per_customer = a.aov + a.ascend * a.backend
    if per_customer <= 0:
        print("The average order value and back-end numbers give zero revenue per customer. Check --aov, "
              "--backend and --ascend.")
        return 2
    customers = a.goal / per_customer
    leads = customers / a.lead_to_sale
    reach = leads / a.reach_to_lead
    clients = customers * a.ascend
    max_cpp = a.aov
    max_cpl = a.aov * a.lead_to_sale
    max_cpm = max_cpl * a.reach_to_lead * 1000
    print("7 FIGURE MATH: PLAN")
    print(f"Goal: {money(a.goal)} in revenue")
    print(f"Revenue per customer: {money(per_customer)} ({money(a.aov)} front end + "
          f"{a.ascend:.1%} x {money(a.backend)} back end)")
    print()
    print(f"{'Level':<13}{'Volume needed':>16}   Break-even target for the front end")
    print(f"{'Reach':<13}{reach:>16,.0f}   CPM at or under {money(max_cpm)}")
    print(f"{'Conversions':<13}{leads:>16,.0f}   CPL at or under {money(max_cpl)}")
    print(f"{'Sales':<13}{customers:>16,.0f}   CPP at or under {money(max_cpp)} (the average order value)")
    print(f"{'Ascend':<13}{clients:>16,.1f}   Cost per client close to zero when the front end breaks even")
    print()
    print("Rule: if CPP stays at or under the average order value, the front end pays for its own ads and")
    print("every back-end client is profit. Raise the average order value (order bump, upsells) before you")
    print("raise the ad budget.")
    if a.cpp is not None:
        spend = customers * a.cpp
        front = customers * (a.aov - a.cpp)
        back = clients * a.backend
        print()
        print(f"At a CPP of {money(a.cpp)}: ad spend {money(spend)}, front-end result {money(front)}, "
              f"back-end revenue {money(back)}, total before other costs {money(front + back)}.")
    return 0


def check_organic(a, rev_front, rev_back):
    print("No ad spend in this period (organic only), so there is no CPM, CPL or CPP to check.")
    print("The rates below still show where people drop off.")
    if a.impressions and a.leads:
        print(f"Reach to lead: {a.leads / a.impressions:.2%} of {a.impressions:,.0f} views or impressions")
    if a.leads:
        print(f"Leads: {a.leads:,.0f}   Lead to sale: {a.customers / a.leads:.1%}")
    print(f"Customers: {a.customers:,.0f}   Average order value: {money(a.aov)}")
    if a.clients:
        print(f"Clients: {a.clients:,.0f}")
    if a.leads and a.customers:
        print(f"If ads start at these rates, break-even is a CPL of {money(a.aov * a.customers / a.leads)} "
              f"and a CPP of {money(a.aov)}.")
    print(f"Total revenue {money(rev_front + rev_back)} (front end {money(rev_front)}, back end {money(rev_back)}). "
          "Revenue goes in the PRIVATE section of a report, for the owner only.")
    return 0


def check(a):
    if a.spend < 0 or a.customers < 0:
        print("Give the ad spend (--spend, use 0 for an organic period) and the number of customers (--customers).")
        return 2
    rev_front = a.customers * a.aov
    rev_back = a.clients * a.backend
    print("7 FIGURE MATH: CHECK")
    if a.spend == 0:
        return check_organic(a, rev_front, rev_back)
    cpp = a.spend / a.customers if a.customers else float("inf")
    if a.impressions:
        print(f"CPM: {money(a.spend / a.impressions * 1000)}")
    if a.leads:
        print(f"Leads: {a.leads:,.0f}   CPL: {money(a.spend / a.leads)}   "
              f"Lead to sale: {a.customers / a.leads:.1%}")
    print(f"Customers: {a.customers:,.0f}   CPP: {money(cpp)}   Average order value: {money(a.aov)}")
    if a.clients:
        net = max(a.spend - rev_front, 0) / a.clients
        print(f"Clients: {a.clients:,.0f}   Net cost per client after front-end revenue: {money(net)}")
    print(f"Front-end revenue {money(rev_front)} against ad spend {money(a.spend)}: "
          f"{'breaks even or better' if rev_front >= a.spend else 'below break-even'}.")
    print(f"Total revenue {money(rev_front + rev_back)}, result before other costs "
          f"{money(rev_front + rev_back - a.spend)}.")
    if rev_front < a.spend:
        gap = (a.spend - rev_front) / a.customers if a.customers else 0
        print(f"To break even on the front end, lift the average order value by {money(gap)} per customer, "
              "or lower CPP with a better ad, page or offer.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="KPI targets from 7 Figure Math.")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("plan", help="work backwards from a revenue goal")
    p.add_argument("--goal", type=float, required=True, help="revenue goal for the period")
    p.add_argument("--aov", type=float, required=True, help="front-end average order value, bumps and upsells included")
    p.add_argument("--backend", type=float, default=0, help="back-end offer price")
    p.add_argument("--ascend", type=float, default=0, help="share of customers who buy the back end, e.g. 0.02")
    p.add_argument("--lead-to-sale", type=float, default=0.10, help="share of leads or visitors who buy")
    p.add_argument("--reach-to-lead", type=float, default=0.01, help="share of impressions that become leads")
    p.add_argument("--cpp", type=float, help="optional: a real or expected cost per purchase")
    c = sub.add_parser("check", help="check a test or a past period")
    c.add_argument("--spend", type=float, required=True)
    c.add_argument("--customers", type=float, required=True)
    c.add_argument("--aov", type=float, required=True)
    c.add_argument("--impressions", type=float, default=0)
    c.add_argument("--leads", type=float, default=0)
    c.add_argument("--clients", type=float, default=0)
    c.add_argument("--backend", type=float, default=0)
    a = ap.parse_args()
    if a.cmd == "plan":
        for name in ("lead_to_sale", "reach_to_lead"):
            v = getattr(a, name)
            if not 0 < v <= 1:
                print(f"--{name.replace('_', '-')} is a decimal between 0 and 1, for example 0.10 for 10%.")
                return 2
        if not 0 <= a.ascend <= 1:
            print("--ascend is a decimal between 0 and 1, for example 0.02 for 2%.")
            return 2
        return plan(a)
    if a.cmd == "check":
        return check(a)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
