---
name: context-interview
description: Run the 40 context questions as a short spoken or typed interview and turn the answers into the Brain (my-business/BRAIN.md). Use during setup, when the owner starts a new offer, project or client, or when an agent finds a Brain section empty.
---

# Context interview

AI can't write for a business it doesn't know. This interview collects what every agent needs, once, and saves it where all of them read it. The owner talks, the interviewer listens, asks one follow-up when an answer is thin, and writes the Brain.

Who runs it: the COO during setup, the CMO for a new offer or client, and any agent that finds a Brain section empty (it asks only the missing questions, then hands back to its task).

## Before the first question

1. Ask the owner to share anything that already exists: a website, a sales page, social profiles, past emails, a brand document, call transcripts. Read it all first.
2. Prefill every answer you can find in that material. In each round, show the prefilled answers as "Here's what I found, correct anything that's off" and ask only for what's missing.
3. Tell the owner how it works in two lines: 11 short rounds, talk or type, "skip" and "I don't know yet" are both fine, progress saves after every round.

## Rules

- One round per message, 1 to 6 questions. Show progress: "Round 3 of 11".
- Use the questions word for word, in the round order from [setup/40-context-questions.md](../../setup/40-context-questions.md). That file also has the follow-up for each question.
- One follow-up per thin answer, never more. Then move on.
- "Skip": mark the answer as missing in the Brain and continue. Never invent an answer to fill a gap.
- "I don't know yet": offer 2 or 3 options built from earlier answers. The owner picks, edits or skips.
- After each round, play back what you heard in 3 short lines so the owner can correct it, then save the round to `my-business/interview.md`.
- Voice answers are welcome. Long and messy beats short and polished. Keep the owner's own phrases: they become the Voice card and the customer language.
- Revenue, profit and personal finances never go into the Brain's shared sections. If the owner wants numbers stored, they go in the PRIVATE section.
- If the owner pauses, stop. "Continue setup" resumes at the next unanswered question.

## The 40 questions (original order)

1. What's your name?
2. What's the business/brand name for this offer?
3. What's your industry and sub-niche?
4. Who do you want your customers to see you as?
5. Describe your brand in 3-5 words:
6. What's the goal of this specific project?
7. What's the offer name?
8. What's included in the offer?
9. How much does the offer cost?
10. What's the problem you solve?
11. What are the pain points they experience due to the problem?
12. What's the promised outcome?
13. What are the direct and in-direct results in their life after your solution?
14. Describe your offer in a 1 line elevator pitch:
15. What are 3 credibility factors that make you a trusted authority?
16. What are some strong opinions you have that reflect your brand?
17. What's your epiphany/backstory that led you here?
18. What are your biggest wins that help build trust?
19. What's the process to getting the outcome?
20. What have they tried before that didn't work and why?
21. What's the "new opportunity" they haven't tried yet?
22. How and why is your solution unique to them?
23. Who's the perfect customer avatar?
24. What are common values for your dream customers?
25. What's a common enemy you both have?
26. What's currently holding them back?
27. What are some limiting beliefs they have around your offer?
28. What are some limiting beliefs they have about themselves?
29. What are some limiting beliefs they have about effort/time needed?
30. What are some limiting beliefs they have around investing in this?
31. What's the opportunity cost of inaction and staying the same?
32. Who are they comparing you to and how is this different?
33. Are you doing a special live launch deal or straight to evergreen?
34. What makes this a no-brainer deal if they act right now?
35. Who are your competitors?
36. What softwares do you currently use for your websites, landing pages and funnels?
37. How do you want your visual brand identity to look and feel?
38. Do you currently have any images, brand assets, visual guides or logos we should use?
39. Do you have any reviews or testimonials we can use?
40. Anything else you think is important to know or include?

## Round order

| Round | Topic | Questions |
|---|---|---|
| 1 | You and your brand | Q1, Q2, Q3, Q4, Q5, Q16 |
| 2 | The project | Q6, Q33 |
| 3 | Your customer | Q23, Q24, Q25, Q26 |
| 4 | The problem | Q10, Q11, Q20, Q31 |
| 5 | The offer | Q7, Q14, Q8, Q9, Q12, Q13 |
| 6 | The mechanism | Q19, Q21, Q22 |
| 7 | Story and proof | Q17, Q15, Q18, Q39 |
| 8 | Objections and limiting beliefs | Q27, Q28, Q29, Q30 |
| 9 | Competition and positioning | Q35, Q32, Q34 |
| 10 | Brand assets and tech | Q37, Q38, Q36 |
| 11 | Anything else | Q40 |

## Writing the Brain

1. Copy [brain/BRAIN-TEMPLATE.md](../../brain/BRAIN-TEMPLATE.md) to `my-business/BRAIN.md` if it doesn't exist yet.
2. Put each answer in its section. Every section header lists its question numbers.
3. Fill the derived cards from the answers:
   - **Voice card:** 3 to 5 phrases the owner actually said, words they use, words they'd never use (Q5 follow-up), and their strong opinions (Q16).
   - **Winning Offer Formula table:** Who from Q23, Outcome Q12, Problem Q10, Vehicle Q19, Source Q15 and Q18, Time Q29, Fee Q9, Risk Q30 and Q31, Priority Q33 and Q34 (see [winning-offer-formula](../winning-offer-formula/SKILL.md)).
   - **12-belief map:** which proof or section earns each belief (see [purchase-decision-journey](../purchase-decision-journey/SKILL.md)).
   - **Numbers:** the project goal (Q6) run through [seven-figure-math](../seven-figure-math/SKILL.md).
4. Mark every missing answer as `[MISSING: Qn]` so agents can see the gap and ask for it later.
5. Show the owner a one-screen summary of the Brain and ask for one approval. Log the date in the Brain's changelog.

## Clients

When the owner builds for a client, run the same interview with the client and save it to `my-business/clients/<client>/BRAIN.md`. Agents working on that client read the client's Brain and write in the client's voice, for the client's market.

## Done when

Every round is answered, skipped or marked missing, the derived cards are filled, the owner approved the summary, and `my-business/interview.md` shows "complete".
