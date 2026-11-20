# Install

The team runs inside the AI tool you already use. Pick your tool below, open this folder in it, and say "set up my AI team". The COO does the rest in a conversation (see [PROTOCOL.md](PROTOCOL.md)).

Tools that can read and write files on your computer get the most out of this repo, because the agents keep your Brain, ratings and drafts in `my-business/`. Chat apps work too, with a copy and paste setup.

## Get the files

1. On the repo page, click **Code**, then **Download ZIP**, and unzip it. Or, with git installed:

```
git clone <repo-url> my-ai-team
cd my-ai-team
```

2. Keep your copy private. Your answers stay in `my-business/`, which `.gitignore` keeps out of git. If you want your own copy on GitHub, push it to a new **private** repo and run `git status` before every push to check that nothing from `my-business/` is listed.
3. Optional: install Python 3 so the agents can run the writing scanner (`skills/anti-ai-slop-writing/scripts/slop_scan.py`). Everything else works without it.

## Claude Code

1. Install Claude Code: [Claude Code docs](https://code.claude.com/docs/en/overview).
2. Open a terminal in the folder and run `claude`. It reads `CLAUDE.md`, which loads the COO's rules from `AGENTS.md`.
3. Type `/setup`. Other commands: `/brief` for the daily or weekly brief, `/add-agent` to add one agent.
4. Setup installs each agent you approve as a subagent in `.claude/agents/`. The COO hands work to them, or you can call one by name: "Use the copywriter agent to write the opt-in page." How subagents work: [Claude Code subagents](https://code.claude.com/docs/en/sub-agents).
5. Optional, Mac and Linux: let Claude Code find the skills on its own with `ln -s ../skills .claude/skills`. On Windows, skip this. The agents read the `skills/` folder directly either way.

## Codex

1. Install Codex: [Codex on GitHub](https://github.com/openai/codex).
2. Run `codex` in the folder. Codex reads `AGENTS.md` automatically.
3. Say "set up my AI team". Codex has no separate agent files, so the COO switches roles: it loads `agents/NN-name.md` and `my-business/team/<agent>.md` whenever an agent is needed.

## Cursor

1. Open the folder in Cursor. Cursor reads `AGENTS.md` as project rules.
2. Open the agent chat and say "set up my AI team".
3. The COO loads each agent card when it's needed, the same way as in Codex.

## Gemini CLI

1. Install Gemini CLI: [Gemini CLI on GitHub](https://github.com/google-gemini/gemini-cli).
2. Run `gemini` in the folder. It reads `GEMINI.md`, which loads `AGENTS.md`.
3. Say "set up my AI team".

## Other coding agents

Any tool that reads `AGENTS.md` works the same way ([agents.md](https://agents.md) lists them). If yours doesn't, start with: "Read AGENTS.md and follow it. Then set up my AI team."

## Chat apps

For ChatGPT, Claude, Gemini or any chat app with projects, custom assistants or uploaded files.

1. Open a new chat and paste the whole of [chat/SETUP-PROMPT.md](../chat/SETUP-PROMPT.md). It runs the 40 question interview and gives you your Brain in one block at the end.
2. Save that block as a file called `BRAIN.md`.
3. Make one project (or custom assistant) per agent you want:
   - Instructions: paste the agent's card from [agents/](../agents/README.md). Every card is under 8,000 characters so it fits most instruction boxes.
   - Files: upload `BRAIN.md`, [brain/CORE.md](../brain/CORE.md) and the skill files listed on the card.
4. Start each chat with the card's first task. Rate what you get and add the rating to the project files, so the agent learns your taste.

More detail: [chat/README.md](../chat/README.md).

## Connect your tools

Step 5 of setting up an agent is connecting it to your data and tools. Agents work without connections (you paste things in), and they do much more once they can read your inbox, CRM or analytics.

1. **Start read-only.** Give an agent read access first. Add write access once you trust its drafts.
2. **Use the connector or MCP server your tool offers.** MCP (Model Context Protocol) is the standard way AI tools connect to other software: [modelcontextprotocol.io](https://modelcontextprotocol.io). Most [CRM], [EMAIL TOOL], [CALENDAR], [STORAGE] and [ANALYTICS] tools have one.
   - Claude Code: `claude mcp add` ([Claude Code MCP](https://code.claude.com/docs/en/mcp)).
   - Codex: `codex mcp add`, or a `[mcp_servers.<name>]` table in `~/.codex/config.toml` ([Codex MCP](https://developers.openai.com/codex/mcp)).
   - Cursor: `.cursor/mcp.json` in the project, or the MCP section of Cursor's settings ([Cursor MCP](https://cursor.com/docs/mcp)).
   - Gemini CLI: `mcpServers` in `settings.json` ([Gemini CLI MCP](https://geminicli.com/docs/tools/mcp-server/)).
   - Chat apps: look for Connectors, Apps or Integrations in the settings.
3. **Keys stay out of chat.** Never paste an API key into a conversation or a markdown file. Put it in a `.env` file (git ignores it) or in your tool's secret settings.
4. **Write it down.** After connecting a tool, tell the COO "update my brain: [TOOL] is connected, read only". The Tool map in your Brain and the agent's setup file get updated.

## Updating

Run `git pull` (or download the ZIP again) to get new cards and skills. Your `my-business/` folder is never touched. Keep your changes in `my-business/team/<agent>.md` and leave the files in `agents/` and `skills/` as they are, so updates never overwrite your work.

## When something goes wrong

| What you see | What to do |
|---|---|
| The COO doesn't know about setup | Say "Read AGENTS.md and follow it", or check that you opened the repo folder itself, not the folder above it. |
| "I can't write files" | Claude Code: accept the permission prompt or run `/permissions`. Cursor: use the agent chat. Chat apps: use [chat/SETUP-PROMPT.md](../chat/SETUP-PROMPT.md). |
| `/setup` isn't listed | Start `claude` from inside the repo folder so it finds `.claude/commands/`. |
| The scanner won't run | Install Python 3 from [python.org](https://www.python.org/downloads/), then run `python3 skills/anti-ai-slop-writing/scripts/slop_scan.py --help`. On Windows, use `python` or `py`. |
| An agent can't reach a tool | Check the connection steps above, then tell the COO "test the [TOOL] connection". The agent says what it can see. |
| Agents sound generic | Your Brain is missing voice samples or proof. Say "update my brain" and add 2 or 3 samples and your best results. |
| My answers showed up in `git status` | Check that `.gitignore` still lists `my-business/`, then run `git rm -r --cached my-business` before you commit. |
