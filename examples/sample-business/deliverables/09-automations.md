# Automations: the build sheet for the Starter Kit funnel

```
Agent: Automations   Task: Map the follow-up for the Starter Kit funnel as a build sheet. Build nothing yet   Date: 2026-11-19
Status: Draft for approval, revision 1
Used: Brain sections 5 and 10, the approval rules, the Funnel plan of November 19, the CRM tag rules, skills funnel-types, funnel-formula
Placeholders to fill: [DOMAIN]
Decision needed: Yes to this build sheet? Then I build the 5 workflows switched off, test them with the test contact and send you the report. Switching each one on needs a second yes.
```

Changed after your note ("The Day 3 email sends at 6 am. My people read at 9 pm."): every planner and onboarding email now sends at 8:30 pm in the contact's own time zone, so it sits near the top of the inbox at 9. That's a rule in my setup file now.

The test contact is "Test Contact" at hello+test@[DOMAIN], your business address with +test, tagged `test`. Real contacts never get a test message.

## The 5 workflows

```
WORKFLOW: 1. Planner opt-in and the planner emails
Trigger: the planner form is sent on the opt-in page in [FUNNEL SOFTWARE]
Filters: leaves out anyone tagged status:unsubscribed or bought:starter-kit. Someone who downloads the planner twice doesn't restart the emails
Actions: add the source tag from the form's "How did you find me?" field, set stage Lead,
         send email 0 (the planner) right away,
         wait 1 day, email 1 at 8:30 pm their time,
         wait 2 days, email 2 (Day 3) at 8:30 pm their time,
         wait 2 days, email 3 (Day 5) at 8:30 pm their time,
         wait 2 days, email 4 (Day 7, the kit) at 8:30 pm their time,
         then the weekly email, Sundays at 8:30 pm their time
Goal or exit: buys the kit (they move to workflow 2), or unsubscribes   Owner: Automations. Copy: Copywriter
Test: the test contact fills in the form with the waits cut to 2 minutes. Email 0 arrives within a minute, emails 1 to 4 arrive in order, and a second form fill sends nothing new. With the test contact's time zone set 3 hours ahead, the send time moves with it
```

```
WORKFLOW: 2. Kit bought: tag, access, welcome and weeks 1 to 4
Trigger: a Starter Kit payment succeeds in [PAYMENTS]
Filters: every buyer
Actions: tag bought:starter-kit, plus bought:fridge-cards or bought:strong-back if they took the bump or the upsell,
         set stage Won, and stop workflow 1,
         access comes from [COMMUNITY]'s own connection to [PAYMENTS], which you switch on once in [COMMUNITY]'s settings,
         send the welcome email right away (the login link and "do workout 1 today"),
         the next day, set stage Onboarding. On day 7, set stage Active,
         weeks 1 to 4: one onboarding email a week at 8:30 pm their time,
         week 4: the Back in 12 waitlist email, with one line about 1:1
Goal or exit: the week 4 email is sent, or a refund (workflow 5)   Owner: Automations. Access: [COMMUNITY]
Test: the test contact buys in [PAYMENTS] test mode with the bump and the upsell. Expect 3 tags, access in [COMMUNITY], the welcome email within 5 minutes, then the week emails in order with the waits cut short
```

```
WORKFLOW: 3. Back in 12 waitlist
Trigger: the waitlist form is sent (from the week 4 email, or a link from Sales)
Filters: leaves out anyone tagged status:unsubscribed
Actions: tag waitlist:back-in-12-jan-2027 and interest:back-in-12,
         set stage Ascend if they bought the kit, or Engaged if they didn't,
         send "You're on the list" right away, with the dates: doors open December 28, the group starts January 11
Goal or exit: joins Back in 12 (tag bought:back-in-12), or unsubscribes. The doors-open emails come later, from the Copywriter   Owner: Automations
Test: the test contact joins the waitlist twice. One confirmation, the tags once, and the right stage for a buyer and for a non-buyer
```

```
WORKFLOW: 4. Checkout started, not finished
Trigger: an email is entered on the order form, and no payment follows within 1 hour
Filters: only contacts already on the list by their own opt-in. Leaves out buyers and anyone unsubscribed
Actions: one email at 8:30 pm their time: the 30-day money-back guarantee, the login by email, and one question ("Anything you'd want to know first?")
Goal or exit: they buy, or the one email is sent. There's never a second one   Owner: Automations. Copy: Copywriter
Test: the test contact starts checkout and stops. One email that evening, and nothing after it. Then a test buy within the hour, and no email at all
```

```
WORKFLOW: 5. Refund
Trigger: you issue a refund in [PAYMENTS]
Filters: every refund
Actions: tag status:refunded and keep the bought tags for the history,
         access ends through the same [COMMUNITY] connection,
         stop workflow 2, set stage Lost, and send no win-back emails
Goal or exit: done in one pass   Owner: you issue the refund, Automations does the rest
Test: a test-mode refund on the test contact. Access ends, the onboarding emails stop, and nothing else goes out
```

## Before I build

- Switch on [COMMUNITY]'s connection to [PAYMENTS] once. The steps are in [setup/install.md](../../../setup/install.md#connect-your-tools). Without it, workflow 2 can't give access.
- The time zone field comes from the form's hidden field (the time zone of the device). If it's empty, the email uses [EMAIL TOOL]'s default time zone, which I set to yours.
- Unsubscribes and stop replies end every workflow above, and no contact can get the same email twice.

After the tests, every live workflow goes into `my-business/automations.md`: what it does, its trigger, where it lives and how to switch it off.

## My setup

Saved to `my-business/team/automations.md`: emails send at 8:30 pm in the contact's time zone, never early in the morning.

Saved to `my-business/drafts/automations/build-sheet-2026-11-19.md`.
