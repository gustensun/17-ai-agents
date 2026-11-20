# Coding: the brief for the free week planner tool

```
Agent: Coding   Task: One-page brief for the free 20-Minute Week Planner as a web tool   Date: 2026-11-19
Status: Draft for approval, revision 1
Used: Brain sections 5, 6 and 10 (Style block and Tool map), the Creator's note of November 18, skills founder-method, conversion-design, digital-product-fastlane
Placeholders to fill: [PREVIEW LINK], [SUPPORT EMAIL]
Decision needed: Yes to this brief? Then I build a clickable demo with sample data and send you the preview. It stays a demo until after the January group starts (the Funnel plan).
```

Changed after your note ("Add the Plan B day to the result."): the result screen now shows the Plan B day under the 3 slots, with the 2-day rule in one line, and the emailed week has it too.

## The three questions

1. **Who is it for, in one sentence?** Parents of kids under 5 who used to train and want this week's 3 workouts of 20 minutes planned around naps.
2. **Which three tasks does it take off their plate?** Finding three 20-minute slots in a week that keeps changing. Picking which workout goes on which day. Planning the Plan B day before they need it.
3. **Where do customers and sales already live?** Contacts and tags in [CRM], the planner emails in [EMAIL TOOL], pages and checkout in [FUNNEL SOFTWARE], payments in [PAYMENTS]. The tool rebuilds none of it. It sends the contact to the same planner form, so workflow 1 from Automations runs unchanged.

From the Creator's note: the tool asks for nap times before the email, so the plan is useful first, and the email is how they keep it.

## Screens

1. **Start.** "Plan this week's 3 workouts around nap time", one line on what they'll get, and a "Start" button.
2. **Naps.** For each day, the usual nap start and length, or "no nap" or "it moves". A "Same every day" switch fills the week in one tap.
3. **Other free 20 minutes.** Optional: after bedtime, early morning, weekend mornings.
4. **Equipment.** One kettlebell, two dumbbells, or nothing yet (then the result adds one line on what to get first).
5. **Your week.** 3 slots on different days, each with the time and Workout A, B or C. Under them, the Plan B day and the 2-day rule: "Miss one? It moves to Plan B. Never miss two planned days in a row." Buttons: "Email me my week" (first name and email) and "Print".
6. **Sent.** "Your week is on its way to [their email]." Next step: add the first workout to their phone's calendar.

## The planning rules

- Never two workouts on the same day, and never a workout on the Plan B day.
- Spread the 3 slots with a rest day between them where the week allows it.
- The Plan B day is the first free day after the last slot, or Saturday if nothing is free.
- A nap marked "it moves" gets a backup slot the same evening.

## States

- **Loading:** only while the email sends: "Sending your week". The plan itself appears at once.
- **Empty:** fewer than 3 days with time: "Pick at least 3 days. After bedtime counts." With 2 days, the plan uses them and makes the third day the Plan B day.
- **Error:** the email doesn't send: "Your week didn't send. Check the email address, or print it now. If it happens again, write to [SUPPORT EMAIL] and I'll send it to you." The Print button stays on screen.
- **Success:** the Sent screen, with the next step.

## Stack and style

- Plain HTML, CSS and JavaScript, deployed to [HOSTING] from [CODE HOST], on your own accounts.
- The demo uses sample data, sends nothing and needs no [DATABASE].
- The real version posts to the planner form in [FUNNEL SOFTWARE]. Any key goes into the [HOSTING] secret settings, never into the code.
- The approved Style block: Sand and moss colours, Barlow Condensed for headings, the timer arc filling as the week appears, and no countdown timers.

## Tests before QA

- Works at 390px and 1440px.
- Every step works with the keyboard alone, with visible focus, a label on every field and AA contrast from the Style block.
- The rules hold for 3 sample weeks: naps every day, naps that move, and a week with only 2 free days.
- Every error says what happened and what to do, with the link or button to do it.
- No contact data in the demo or in [CODE HOST].

After your yes, the demo goes to [PREVIEW LINK] with sample data, and QA gets the link with these tests.

Saved to `my-business/builds/planner-tool/brief-2026-11-19.md`.
