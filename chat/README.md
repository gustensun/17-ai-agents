# The team in a chat app

Use the agents in ChatGPT, Claude, Gemini or any chat app that has projects (custom GPTs, Projects, Gems) and file uploads. Each agent lives in its own project, and you keep the files on your computer.

If you can use Claude Code, Codex, Cursor or Gemini CLI, start there instead ([install.md](../setup/install.md)). Those tools keep your Brain, ratings and drafts in files on their own, and the COO hands work between agents for you.

## What you need

- A chat app with projects or custom assistants and file uploads.
- The repo on your computer. On the repo page, click **Code**, then **Download ZIP**, and unzip it ([Get the files](../setup/install.md#get-the-files)).
- A folder on your computer called `my-business` for your own files. It's the master copy of everything you upload.
- 30 to 45 minutes for the interview, in one sitting or several.

## Step 1: The interview

1. Open a new chat outside any project and paste the whole of [SETUP-PROMPT.md](SETUP-PROMPT.md).
2. Answer the 11 rounds. Talk or type. "Skip" and "I don't know yet" are both fine.
3. At the end you get your Brain in one block. Copy it into a file called `BRAIN.md` in `my-business`, and save your voice samples there as `voice-samples.txt`.
4. The COO recommends a starting team, usually 4 to 6 agents ([starter teams](../setup/starter-teams.md)).

If the chat gets long, say "save progress". Then start a new chat, paste the prompt and the saved block, and say "continue setup".

## Step 2: One project per agent

Make one project for each agent in your team, starting with the COO.

| Part of the project | What goes in |
|---|---|
| Name | The agent and your business, for example "Copywriter: [BUSINESS]" |
| Instructions | The agent's whole card from [agents/](../agents/README.md) |
| Files | `BRAIN.md`, [brain/CORE.md](../brain/CORE.md), the skill files listed under "Skills" on the card, and the taste file listed under "Taste" |

For each skill, upload its `SKILL.md`. If the skill folder has a `references` folder, upload those files too when your app allows it. Three skills come with a Python script: the writing scanner, the KPI calculator and the page checker. Apps that can run code can use a script if you upload it. In other apps, the agent does the same check by reading.

Where to make the projects:

- ChatGPT: a project or a custom GPT.
- Claude: a project.
- Gemini: a Gem.
- Other apps: anything called a project, assistant, agent or space, with an instructions box and files.

## Step 3: The first chat with each agent

1. Say "Read your card and my Brain, then ask me your setup questions." The agent asks 2 or 3 questions from its card and writes your answers as one block. Save it as `my-business/team/<agent>.md` (for example `copywriter.md`) and upload it to the project.
2. Give it the first task on its card (the "First task" section).
3. Rate the work from 1 to 5 with one sentence on why: "rate this 4, because the headline is too long." The agent revises once and writes the taste log line for you.
4. Paste the line into a file called `taste-log.md` (start from [the template](../brain/templates/taste-log.md)) and upload the new version to the project. Agents read their own ratings before every task.
5. Train up to 2 agents per sitting, as in [stage 6 of the protocol](../setup/PROTOCOL.md#stage-6-training-round).

A finished training week, with all 17 deliverables and every rating, is in the [sample business](../examples/sample-business/README.md).

## Step 4: Day to day

- **Plans and briefs.** Ask the COO project for the "daily brief" or "weekly brief". It can't see the other projects, so paste in what's new first: finished work, new ratings, this week's numbers.
- **Handoffs.** When one agent's work goes to another, the agent writes a handoff note in the format from [brain/CORE.md](../brain/CORE.md#formats). Paste the note and the work into the next agent's project.
- **Brain changes.** Say "update my brain" in the COO project. It asks only what changed and gives you the new Brain. Save it in `my-business` and upload it to every project.
- **Tools.** Most chat apps can connect to other software under Connectors, Apps or Integrations in the settings. Start read-only. Every send, publish, spend or delete still needs your yes.

## When something gets in the way

| What happens | What to do |
|---|---|
| The agents can't see each other's work | Paste the handoff note and the work into the next agent's project. |
| A project still has an old Brain or taste log | Upload the newest file from `my-business` and delete the old one from the project. |
| A long chat forgets the start | Start a new chat in the same project. The card, the Brain and your ratings load again every time. |
| The instructions box is too small | Every card is under 8,000 characters. If your app allows less, upload the card as a file and write "Follow the agent card in the files" in the instructions. |
| You want the briefs to arrive on their own | Use the app's scheduled tasks if it has them. Otherwise ask for the brief when you sit down. |
| The agent can't open a link | Paste the text of the page instead, or turn on web search in the app's settings. |
| Copying files between projects takes too long | Move to a coding agent (below). |

## Moving to a coding agent later

When the copying gets old, open the repo folder in Claude Code or Codex ([install.md](../setup/install.md)). Put your `my-business` folder inside the repo folder, and merge the taste logs into one `my-business/taste-log.md`. The setup files are already where the agents look for them, in `my-business/team/`. Then say "continue setup". The COO reads what you already have and picks up from there.
