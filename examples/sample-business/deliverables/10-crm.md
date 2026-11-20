# CRM: pipeline, tags, fields and a 50-contact cleanup

```
Agent: CRM   Task: Propose the pipeline, tag rules and fields, and clean a sample of 50 contacts   Date: 2026-11-20
Status: Draft for approval
Used: Brain sections 3, 5 and 10, the approval rules, skills purchase-decision-journey, client-formula
Placeholders to fill: none
Decision needed: Yes to the fixes, the stage changes and the 2 merges below? They wait for you, except tags and notes.
```

I read the pipeline, tags and fields as they are, and changed nothing except what your standing rule allows: tags and notes. The 50 contacts are the export you sent on November 19. That export gets deleted from `my-business/` when this is done.

## The pipeline

The default stages you said yes to in setup, plus one: Not now, for people like Tom who said they'll write when they're ready. Here's what each stage means for Nap Time Strength.

| Stage | Who's in it | Next step |
|---|---|---|
| Lead | Downloaded the planner, nothing else yet | The planner emails |
| Engaged | Replied, clicked 3 emails in a row, or sent a DM | Sales reads the conversation |
| Qualified | Told us their kids' ages and the time they have, and an offer fits | Sales sends the offer |
| Offer sent | Got a price or a link for Back in 12 or 1:1 | One follow-up, then wait |
| Won | Paid today | Access and the welcome email |
| Onboarding | The first 7 days after buying | Workout 1, then the week-1 emails |
| Active | In the 12 weeks | The weekly emails |
| Ascend | Finished the kit, or asked what's next | The Back in 12 waitlist |
| Alumni | Finished Back in 12 or 1:1 | A check-in every 90 days |
| Lost | Said no, got a refund or unsubscribed | Nothing, ever, unless they write first |
| Not now | Said "later" in their own words | No follow-up. We wait for them to write |

Contacts with no consent go in a separate Cold pipeline and never get marketing emails.

## Tag rules

One prefix per kind, lower case, hyphens between words:

- `source:` youtube, instagram, referral, partner, expo-2025
- `bought:` starter-kit, fridge-cards, strong-back, back-in-12, 1to1
- `interest:` back-in-12, 1to1
- `waitlist:` back-in-12-jan-2027
- `status:` unsubscribed, refunded, check-email
- `consent:` unknown

## Fields

The team needs these, and nothing more: first name, last name, email, phone (optional), time zone (Automations sends at 8:30 pm their time), stage, next step with a due date, and the kit start date (for the week 1 to 4 emails).

Nothing about kids, health or pregnancy goes into a field. If someone tells us, it stays in the conversation.

## The 50 contacts: every change

45 of the 50 have at least one change. 5 need none: #1, #17, #23, #32 and #38.

**Names, to capital first letters (6).** Waits for your yes.
#4 "MAYA R." to "Maya R.", #9 "jordan b." to "Jordan B.", #13 "priya" to "Priya", #21 "LEAH" to "Leah", #30 "omar k" to "Omar K.", #44 "nina p" to "Nina P."

**Emails, trimmed and in lower case (3).** Waits for your yes.
#7 "Hana.Ito@Example.com " to "hana.ito@example.com", #18 " ben.c@example.com" to "ben.c@example.com", #36 "CARLA.M@EXAMPLE.COM" to "carla.m@example.com"

**An email I didn't change (1).** Done, it's a tag.
#27 luca.f@example.con ends in ".con". I didn't guess the right address. Tagged `status:check-email`, so Support can ask Luca next time he writes.

**Phones, to one format (4).** Waits for your yes.
#3 "5550100142" to "+1 555 010 0142", #12 "(555) 010-0178" to "+1 555 010 0178", #25 "555.010.0133" to "+1 555 010 0133", #41 "+15550100190" to "+1 555 010 0190"

**Source tags, from the planner form's "How did you find me?" (9).** Done, tags.
#2, #5, #11, #19 and #33 got `source:youtube`. #8, #24 and #39 got `source:instagram`. #47 got `source:referral`.

**Old buyer tags, replaced with `bought:starter-kit` (7).** The new tag is added. Removing the old ones waits for your yes.
"kit buyer" on #6, #14, #22 and #35. "Kit-Buyer" on #16 and #40. "bought kit" on #29.

**Contacts with no stage (7).** Waits for your yes.
#10, #20, #31 and #45 to Lead (the planner only). #14 and #22 to Active (bought in late October). #48 to Onboarding (bought on November 17).

**Unsubscribed, but still on the newsletter list (2).** Waits for your yes.
#26 and #43 come off the list. Their `status:unsubscribed` tag stays.

**No consent on record (3).** Waits for your yes.
#37, #46 and #50 came from a 2025 expo sign-up sheet with no opt-in recorded. They move to the Cold pipeline with `source:expo-2025` and `consent:unknown`, and get no marketing emails.

**Possible duplicates (2 merges).** Waits for your yes.
- #15 Sam Lee (sam.lee@example.com) and #34 Samantha Lee (s.lee@example.com) have the same phone number.
- #28 Alex Kim (alex.kim@example.com) and #42 Alex Kim (akim@example.com) have the same name, and both downloaded the planner.

A merge keeps the full history of both records. No contact gets deleted.

**Notes (1).** Done, it's a note. Moving him to Not now waits for your yes.
#49 Tom: "Wait for him to get in touch." From Sales, November 18.

## PIPELINE

```
PIPELINE: week of November 16 (the 50-contact sample, after the changes)
Lead 19  Engaged 9  Qualified 3  Offer sent 1  Won 1
Onboarding 2  Active 6  Ascend 1  Alumni 1  Lost 3  Not now 1
Cold pipeline: 3
Stuck over 7 days: Noor, Qualified, 11 days (missed her call on November 9, Sales sent one kind message). Next step: wait for her reply.
                   Sofia, Engaged, 9 days (asked about the Back in 12 payment plan). Next step: Sales sends the 3 x $109 option when doors open on December 28.
Follow-ups due: Priya, waitlist link, November 21, Sales. Ben, the Strong Back answer, after your answer, Sales. Carla, one question, November 24, Sales.
Cleanup waiting for a yes: 2 merges, 33 fixes
```

Note added after approval: Dana said yes to everything except the 2 merges. Sam and Samantha Lee are sisters who share a phone, and the two Alex Kims are different people. New rule in `my-business/team/crm.md`: merge only when the email address matches exactly.
