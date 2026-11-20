# Start here

Five minutes to understand this repo and take the first step.

## What you're setting up

A team of 17 AI agents that work inside your AI tool. You talk to one of them, the COO. It interviews you about your business, writes your Brain (one file every agent reads), recommends a small team to start with and hands each task to the right agent. Every piece of work comes back to you as a draft, and nothing goes out without your yes.

No coding needed. You talk to the COO in plain words, typed or dictated.

## What you need

- **An AI tool.** Claude Code or Codex works best, because the agents can keep your files and pass work to each other. Cursor and Gemini CLI work the same way. A chat app (ChatGPT, Claude, Gemini) works with a copy and paste setup.
- **30 to 45 minutes** for the first session. You can pause any time and say "continue setup" later.
- **Optional, and it saves time:** your website or sales page, your social profiles, and 2 or 3 things you wrote yourself (a post, an email, a DM).

## Your first session

1. **Get the files.** On the repo page, click **Code**, then **Download ZIP**, and unzip it.
2. **Open the folder in your tool.** Steps for each tool are in [setup/install.md](setup/install.md). In a chat app, follow [chat/README.md](chat/README.md) instead.
3. **Say "set up my AI team".** In Claude Code you can type `/setup`.
4. **Answer the questions.** 11 short rounds, and the COO shows where you are ("Round 3 of 11"). "Skip" and "I don't know yet" are both fine.
5. **Check your Brain.** The COO shows a one-page summary and asks "Is this you?" Fix anything that's off.
6. **Approve your starter team.** Usually 4 to 6 agents, picked for your path and your stage ([starter teams](setup/starter-teams.md)).
7. **Train the first agents.** Each one does its first task on your business. Rate it from 1 to 5 with one sentence on why, and it revises once. Train up to 2 agents per sitting.

## What to say after setup

| Say | What happens |
|---|---|
| "daily brief" or "weekly brief" | The COO's report: today's top 3, decisions, what's blocked |
| "Copywriter, write the opt-in page" | Call any agent by name |
| "rate this 4, because the headline is too long" | The agent learns from it, and the rating goes in your taste log |
| "update my brain" | The COO asks only what changed |
| "add an agent" | One more agent, with its 2 or 3 setup questions |
| "show my queue" | Your ideas, with the one to do next |
| "new client: [NAME]" | The 40 questions for a client, saved separately |

## Good to know

- **Start small.** Most people get more done with 4 to 6 agents than with all 17. Add one when a real bottleneck shows up.
- **Your ratings train the team.** A number and one sentence on why. The why teaches more than the number.
- **See what good looks like.** The [sample business](examples/sample-business/README.md) shows a finished Brain, all 17 first deliverables and every rating from one training week.
- **Your data stays with you.** Everything about your business lives in `my-business/`, which git ignores. Keep your copy private.

## If you get stuck

The fixes for the most common problems are in [install.md](setup/install.md#when-something-goes-wrong). Or ask the COO "what went wrong?" and it tells you what to do next and where.
