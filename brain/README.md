# The Brain

Your agents are only as good as what they know. This folder holds the shared part of that knowledge. Your private part lives in `my-business/`, which the setup interview creates and git ignores.

| File | What it is | Who writes it |
|---|---|---|
| [CORE.md](CORE.md) | House rules, writing and design rules, the Purchase Decision Journey and 7 Figure Math. The same for every business. | This repo |
| [BRAIN-TEMPLATE.md](BRAIN-TEMPLATE.md) | The 11 sections the interview fills in. It becomes `my-business/BRAIN.md`. | The COO, with you |
| [templates/taste-log.md](templates/taste-log.md) | Your ratings and the reasons behind them. | You, through the agents |
| [templates/log.md](templates/log.md) | One line per finished task. | Every agent |
| [templates/queue.md](templates/queue.md) | The one idea queue. Nothing gets built without a yes. | You and every agent |

## What lives in my-business/

The COO creates this folder during setup. Never commit it to a public repo. The `.gitignore` in this repo already keeps it out.

```
my-business/
  BRAIN.md            your answers, built from the 40 questions
  interview.md        interview progress, so you can pause and continue
  voice-samples.txt   2 or 3 pieces you wrote or said yourself
  allow.txt           phrases and devices that belong to your voice
  team.md             which agents you installed, and their levels
  team/<agent>.md     each agent's setup (cmo.md, sales.md...): role, tasks, cadence, outcome, connections
  taste-log.md        your ratings
  log.md              finished work
  queue.md            ideas waiting for a yes
  faq.md              answers the Support agent uses, approved by you
  automations.md      every live workflow: what it does, its trigger, how to switch it off
  examples/<agent>/   outputs you rated 4 or 5, kept as examples
  drafts/             work waiting for approval
  research/           research reports
  finance/            the Accounting agent's files and ledger
  skills/<name>/      your own skills (see skills/INDEX.md)
  clients/<client>/   one BRAIN.md per client, if you work with clients
```

## How the Brain gets better

1. Setup builds the first version from your interview and the research (stages 1 to 3 in [setup/PROTOCOL.md](../setup/PROTOCOL.md)).
2. Every rating you give goes into the taste log, with your reason.
3. When you give the same reason twice, the agent proposes a rule for its setup file.
4. After 3 approved outputs, the agent proposes an upgrade in the weekly review (stage 8).
5. When something in your business changes (a new offer, a new price, new proof), say "update my brain". The COO asks only the questions that changed and adds a line to the changelog.
