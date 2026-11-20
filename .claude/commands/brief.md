---
description: The COO's brief. Add "weekly" for the weekly version with numbers, ratings and upgrades.
argument-hint: daily or weekly
disable-model-invocation: true
---

Act as the COO described in AGENTS.md and give me my brief: $ARGUMENTS

- Daily unless I said weekly. Use the brief formats in AGENTS.md and agents/01-coo.md.
- Read `my-business/log.md`, `my-business/queue.md`, `my-business/taste-log.md` and each installed agent's setup file first.
- For the weekly brief, also run stage 8 of setup/PROTOCOL.md: propose upgrades for agents with 3 or more approved outputs since their last upgrade.
- If `my-business/BRAIN.md` doesn't exist, tell me to run /setup first.
