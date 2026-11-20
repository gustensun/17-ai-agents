# 17 AI Agents

A ready-made AI team for founders, digital product creators and affiliates. 17 specialist agents share one Brain about your business, learn your taste from your ratings, and bring every piece of work to you as a draft for your yes.

It runs inside the AI tool you already use: Claude Code, Codex, Cursor, Gemini CLI or any tool that reads `AGENTS.md`. Chat apps like ChatGPT, Claude and Gemini work too, with a copy and paste setup.

New here? Read [START-HERE.md](START-HERE.md) first. It takes 5 minutes.

## How it works

1. **The interview.** Your main agent, the COO, asks the [40 context questions](setup/40-context-questions.md) in 11 short rounds. Talk or type. Share your website and a few past posts first, and it fills in what it can so you answer less.
2. **The Brain.** Your answers become one file that every agent reads before it works: your customer, your offer, your proof, your voice and your numbers.
3. **The team.** The COO recommends 4 to 6 agents to start with, from your path (founder, digital product or affiliate) and your stage ([starter teams](setup/starter-teams.md)). You can install all 17 if you want them.
4. **The training round.** Each agent does its first task on your real business. You rate it from 1 to 5 with one sentence on why, and it revises once. Your notes become rules in its setup file, so the next draft starts closer.
5. **Work.** Talk to the COO about anything, or call an agent by name. Nothing is sent, published, spent or deleted without your yes.

The whole setup is in [setup/PROTOCOL.md](setup/PROTOCOL.md).

## Start

| You use | Do this | Steps |
|---|---|---|
| Claude Code | Open the repo folder, run `claude` and type `/setup` | [install.md](setup/install.md#claude-code) |
| Codex, Cursor or Gemini CLI | Open the repo folder and say "set up my AI team" | [install.md](setup/install.md) |
| ChatGPT, Claude, Gemini or another chat app | Paste [chat/SETUP-PROMPT.md](chat/SETUP-PROMPT.md) into a new chat | [chat/README.md](chat/README.md) |

## The team

| Department | Agents |
|---|---|
| Lead | [COO](agents/01-coo.md): builds your team, plans the week and hands work to the others |
| Strategy | [CMO](agents/02-cmo.md), [Research](agents/03-research.md), [Creator](agents/04-creator.md) |
| Marketing | [Content](agents/05-content.md), [Copywriter](agents/06-copywriter.md), [Design](agents/07-design.md) |
| Build | [Funnel](agents/08-funnel.md), [Automations](agents/09-automations.md), [Coding](agents/11-coding.md), [QA](agents/12-qa.md) |
| Customers | [CRM](agents/10-crm.md), [Support](agents/13-support.md), [Lead Gen](agents/14-lead-gen.md), [Sales](agents/15-sales.md) |
| Numbers | [Accounting](agents/16-accounting.md), [Analytics](agents/17-analytics.md) |

Each agent's job, cadence and tools: [agents/README.md](agents/README.md). To see all 17 at work for one made-up business, with the owner's ratings: [examples/sample-business](examples/sample-business/README.md).

## What's inside

| Folder | What's in it |
|---|---|
| [brain/](brain/README.md) | The house rules every agent follows, and the template your Brain is built from |
| [agents/](agents/README.md) | The 17 agent cards, each under 8,000 characters so it fits most instruction boxes |
| [skills/](skills/INDEX.md) | 22 frameworks the agents work from: offers, funnels, copy, design, content, sales, numbers |
| [taste/](taste/README.md) | Bad, good and great examples, so the agents learn the standard |
| [galleries/](galleries/README.md) | 181 offers, 100 product ideas, 124 funnel and website templates, 1,550 paid communities and 332 outlier videos |
| [ai-skills/](ai-skills/README.md) | 5 outside skill repos worth adding, with install steps |
| [setup/](setup/PROTOCOL.md) | The setup protocol, the 40 questions, starter teams and install steps |
| [chat/](chat/README.md) | The setup for chat apps |
| [examples/](examples/sample-business/README.md) | A finished Brain and one deliverable per agent, for a made-up business |
| [tools/](tools/check_repo.py) | The quality check this repo runs before every change |

## Rules the agents never bend

- **Truth.** No invented proof, numbers, quotes or results. A gap gets a placeholder.
- **Approvals.** They ask before anything is sent, published, spent, deleted or changed live, and before anyone is contacted.
- **Privacy.** Your answers live in `my-business/`, which git ignores. Revenue, profit and personal finances stay in the PRIVATE section of your Brain and never appear in content or go to outside tools.
- **Errors.** When something fails, the agent says what happened, what to do and where to fix it.

Keep your copy private. If you put it on GitHub, use a private repo.

## Updates

Run `git pull` or download the ZIP again. Your `my-business/` folder is never touched. Put your own changes in `my-business/team/<agent>.md`, so updates never overwrite them ([install.md](setup/install.md#updating)).

## Credits

Created by Gusten Sun. The outside skills in [ai-skills/](ai-skills/README.md) belong to their authors and keep their own licenses. Everything else is under the [MIT License](LICENSE).
