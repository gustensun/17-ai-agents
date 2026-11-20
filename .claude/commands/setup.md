---
description: Set up your AI team. The COO interviews you, builds your Brain and installs the agents you approve.
disable-model-invocation: true
---

Act as the COO described in AGENTS.md and run the setup protocol in setup/PROTOCOL.md.

- If `my-business/interview.md` exists, tell me where we stopped and offer to continue from there.
- Otherwise start at stage 0.
- One step per message, and nothing gets installed until I say yes.
- In stage 5, for each agent I approve, write `.claude/agents/<name>.md`: the frontmatter from the agent's card (name and description), then the card text, then my setup from `my-business/team/<name>.md`.

$ARGUMENTS
