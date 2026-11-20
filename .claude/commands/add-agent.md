---
description: Add one agent to your team. Runs the team plan and install steps for that agent only.
argument-hint: agent name, for example copywriter
disable-model-invocation: true
---

Act as the COO described in AGENTS.md and add this agent to my team: $ARGUMENTS

1. If I didn't name one, recommend the agent that would remove my biggest bottleneck right now, based on my Brain, my log and setup/starter-teams.md, and ask me to confirm.
2. Read its card in `agents/`, explain its first task in two lines, and ask its setup questions in one message with the defaults shown.
3. Write `my-business/team/<name>.md` and `.claude/agents/<name>.md` as in stage 5 of setup/PROTOCOL.md, then update `my-business/team.md`.
4. Offer to run its training round (stage 6) now.
