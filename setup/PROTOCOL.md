# Setup protocol

The COO runs this protocol the first time you open the repo in your AI tool. It's a conversation: the COO asks, you answer, and nothing gets installed until you say yes. Plan for about 30 minutes for stages 0 to 4. Sharing your website, sales page and a few past posts at the start makes it shorter.

Start by telling the COO "set up my AI team" (or type /setup in Claude Code). Say "continue setup" to pick up where you left off.

| Stage | What happens | What you get |
|---|---|---|
| 0. Welcome | Pick your path, share what you have, choose how long to spend | A plan for the session |
| 1. Interview | The 40 context questions, voice samples and your rules | `my-business/interview.md` |
| 2. Research | Avatar grid, competitors and outliers | `my-business/research/` |
| 3. Brain | The COO writes your Brain and you confirm it | `my-business/BRAIN.md` |
| 4. Team plan | A starter team, explained, for your yes | `my-business/team.md` |
| 5. Install | 2 or 3 questions per agent, then the install | `my-business/team/<agent>.md` |
| 6. Training round | Each agent's first task, your rating, one revision | `my-business/taste-log.md` |
| 7. Go live | Cadence, the first weekly plan, how to talk to the team | Your first brief |
| 8. Weekly upgrade | Agents learn from your ratings | Better setup files every week |

## Rules for the COO during setup

- One step per message. Show where you are, for example "Stage 1, round 3 of 11".
- Ask, then wait. Never answer for the owner.
- When the owner is unsure, suggest 2 or 3 options built from their earlier answers. Mark the one they accept as [ASSUMPTION].
- Create `my-business/` first and check that `.gitignore` lists it before you write anything private.
- Save progress to `my-business/interview.md` after every round.
- When something fails, say what happened, what to do and where. Example: "I can't write files yet. In Claude Code, accept the file permission prompt or run /permissions. Install steps: setup/install.md."
- Follow the house rules in [brain/CORE.md](../brain/CORE.md), privacy above all.

## Stage 0: Welcome

Introduce yourself in two sentences, then ask these three questions, one at a time.

1. **"Which path fits you best right now?"**
   - Founder: you sell a service (done for you, done with you, consulting, an agency).
   - Digital product: you sell, or want to sell, a course, template, tool, community or membership.
   - Affiliate: you recommend other companies' products and earn a commission.
   - Not sure yet: the COO helps you pick during the offer round.
2. **"Is there anything I can read first?"** A website, a sales page, social profiles, past emails, a brand doc, a pitch deck, call transcripts. Read all of it, prefill as many of the 40 answers as you can, and mark each one "prefilled, please confirm".
3. **"How much time do you have today?"**
   - About 15 minutes: the minimum Brain and one agent.
   - 30 to 45 minutes: stages 0 to 5.
   - Any time: pause and say "continue setup" later.

**The minimum Brain** is three things: who you serve (Q23), what you sell and what it costs (Q7, Q14, Q9), and 2 or 3 samples of how you sound. With those, agents can start working. Everything else fills in over time and is marked [MISSING: Qx] until then.

## Stage 1: Interview

1. Ask the 40 questions in 11 rounds from [40-context-questions.md](40-context-questions.md), word for word, one round per message. Use the follow-up when an answer is thin. Skip questions that were prefilled and confirmed.
2. After each round, play back what you heard in 3 short lines and ask "Anything to fix?"
3. If the owner has no offer yet, pause at round 5. Shape one with [skills/winning-offer-formula](../skills/winning-offer-formula/SKILL.md), plus [skills/digital-product-fastlane](../skills/digital-product-fastlane/SKILL.md) for a product, [skills/client-formula](../skills/client-formula/SKILL.md) for a service, or [skills/affiliate-fastlane](../skills/affiliate-fastlane/SKILL.md) for an affiliate. Come back with a draft for the owner to confirm.
4. Then ask for five extras, one per message:
   - **Voice samples.** "Paste 2 or 3 things you wrote or said yourself: a post, an email, a DM, a video transcript. Unedited is best." Save them to `my-business/voice-samples.txt`.
   - **Your devices.** "Do you use any phrases on purpose that might look like a habit to someone else? A question you always ask, a line you always open with?" Save them to `my-business/allow.txt`, one per line.
   - **Never list.** "What should we never say, show or promise?" Skip it if Q40's follow-up already covered it.
   - **Approvals.** "By default I'll ask before anything is sent, published, spent, deleted or changed live, and before anyone is contacted. Do you want anything stricter?"
   - **Private planning (optional).** "If you want the team to plan against real numbers, share your goal and where you are today. It stays in the PRIVATE section of your Brain and never appears anywhere else. You can skip this."

## Stage 2: Research

The Research agent runs this stage if it's in the plan. Otherwise the COO runs it. Use [skills/deep-market-research](../skills/deep-market-research/SKILL.md).

1. **Avatar grid.** Fill the 5 boxes (external problems, external goals, internal problems, internal goals, experiences) from real sources: reviews of competing products, comments, forums, community posts, search suggestions. Note the source of each line and keep the customer's exact words.
2. **Competitors.** The 3 to 5 competitors from Q35, plus the do-it-yourself and do-nothing options: their offer, price, promise and proof, and the gap the owner could own.
3. **Outliers.** If the owner makes content, find 10 posts or videos in their niche from the last 90 days that got at least 2 times the channel's usual views. Method: [skills/outlier-research](../skills/outlier-research/SKILL.md).
4. Show a one-screen summary and ask: "What here surprises you, and what's wrong?" Fix what's wrong.

If your AI tool can't search the web, say so and offer two options: turn on web search (see [install.md](install.md#connect-your-tools)), or run the prompt in the deep market research skill in any AI app with web search and paste the answer back.

## Stage 3: Brain build

1. Copy [brain/BRAIN-TEMPLATE.md](../brain/BRAIN-TEMPLATE.md) to `my-business/BRAIN.md` and fill every section from the interview and the research.
2. Mark gaps `[MISSING: Qx]`. Never fill a gap with a guess.
3. Build the Voice card. Run `python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --profile my-business/voice-samples.txt`, read the samples yourself, and fill in the card. If Python isn't installed, read the samples and fill the card by hand.
4. Fill in the Winning Offer Formula, the value ladder, the 12-belief map and the style block from the answers. Mark anything you inferred as [ASSUMPTION].
5. Show the owner a one-page summary: who they serve, what they sell, the promise, the mechanism, the proof they have, the proof they're missing, and how they sound. Ask "Is this you?" and edit until they say yes.
6. Copy the files in `brain/templates/` to `my-business/` (taste-log.md, log.md, queue.md) and add the first line to the changelog.

## Stage 4: Team plan

1. Pick a starter team from [starter-teams.md](starter-teams.md) using the path, the stage of the business and the hours the owner has each week. When in doubt, recommend fewer agents: 4 to 6 is plenty to start.
2. Show the plan as a short list: each agent, its first task, and why it belongs in the team now. Name 2 or 3 agents to add later and the signal that says it's time.
3. Ask "Shall I install this team?" Wait for a yes or for edits, then save the plan to `my-business/team.md`.

## Stage 5: Install

For each agent in the confirmed plan, in order:

1. Read its card in [agents/](../agents/README.md).
2. Ask its setup questions (listed at the end of each card) in one message. Show the default answer for each so the owner can reply "default".
3. Write `my-business/team/<agent>.md` with the five parts of the setup:
   - **Role:** the job in one sentence, for this business.
   - **Tasks:** the tasks the owner wants, picked from the card.
   - **Cadence and deliverables:** when it runs and what it hands over each time.
   - **Outcome:** the number or result that shows it's working.
   - **Connections:** which tools from the Tool map it reads or writes, and with what access.
   Add the autonomy level (Assistant unless the owner chose otherwise), the approvals that apply, and any standing rules.
4. In Claude Code, also write `.claude/agents/<name>.md`: the frontmatter and text of the card, followed by the setup file. Other tools load the card and the setup file whenever the agent is needed ([install.md](install.md)).
5. If a tool isn't connected yet, install the agent anyway. Mark the connection "not connected", say what connecting it would let the agent do, and link to [install.md](install.md#connect-your-tools). Until then the agent works on whatever the owner pastes in.

## Stage 6: Training round

Each new agent does the first task on its card, using the owner's real business.

1. The agent delivers with the standard header from brain/CORE.md and runs its own quality check before handing over.
2. The owner rates the work from 1 to 5 with one sentence on why. The COO adds it to `my-business/taste-log.md`.
3. The agent revises once. If the note says what to do, the agent also adds it to its setup file as a rule ([how](../brain/templates/taste-log.md#from-ratings-to-rules)). A revision rated 4 or 5 is saved to `my-business/examples/<agent>/`.
4. If an agent scores 3 or lower twice, the COO asks the owner one question about what's missing (usually context, a sample or a rule), adds the answer to the Brain or the setup file, and the agent tries once more.

Train up to 2 agents per sitting. The rest do their training round the first time they're used.

## Stage 7: Go live

1. Set the cadence from each setup file: daily, weekly or only when asked. If the AI tool can schedule tasks, set them up after the owner says yes. Otherwise the owner says "daily brief" or "weekly brief" and the COO runs the round.
2. Write the first weekly plan: the top 3 priorities that serve the Brain's goal, the agent that owns each one, and the finish line for each.
3. Explain how to work with the team: talk to the COO about anything, or call an agent by name ("Copywriter, write..."). Every output arrives as a draft for approval.

## Stage 8: Weekly upgrade

Once a week, as part of the weekly brief:

1. Each agent with 3 or more approved outputs since its last upgrade reads its taste log entries and proposes up to 3 changes to its setup file: new rules, better defaults, a better first step. The owner approves each change.
2. The COO suggests autonomy changes when an agent has earned them, for example Assistant to Employee after about 10 approved outputs with no Blocker issues. Only the owner decides.
3. The COO lists agents nobody used in 2 weeks and suggests pausing them, and lists the [MISSING] answers that would help most.
4. Every change gets a line in the Brain's changelog.

## What the owner can say

| Say | What happens |
|---|---|
| "set up my AI team" | Starts this protocol |
| "continue setup" | Picks up where you stopped |
| "add an agent" | Stages 4 and 5 for one more agent |
| "update my brain" | Asks only what changed, then updates BRAIN.md and the changelog |
| "daily brief" or "weekly brief" | The COO's report |
| "rate this 4, because..." | Adds a taste log entry |
| "show my queue" | The idea queue, with a recommended next pick |
| "new client: [NAME]" | Runs the 40 questions for a client and saves them in `my-business/clients/` |
