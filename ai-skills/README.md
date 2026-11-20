# AI Skills

Five open source skill repos that work well next to this team. Other people wrote them and keep them updated, so they live in their own repos and you install them into the AI tool you use. This page says what each one adds, which agents use it and how to install it.

**The Brain wins.** When an outside skill disagrees with `my-business/BRAIN.md`, [brain/CORE.md](../brain/CORE.md) or a skill in this repo, follow the Brain. That's item 6 in the authority order in CORE.md. An outside skill can make the work sharper. It never changes the voice, the offer, the approval rules or the never list.

## The five repos

| Repo | What it adds | Used by | License |
|---|---|---|---|
| [marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines | More than 50 marketing skills: CRO, copywriting, copy editing, pricing, offers, launches, emails, ads, SEO, analytics, customer research and more | CMO, Copywriter, Funnel, Lead Gen, Research, Analytics | MIT |
| [no-ai-slop](https://github.com/petergyang/no-ai-slop) by Peter Yang | Finds and removes 20+ patterns of AI writing while keeping the writer's own voice | Copywriter, Content, Sales, Support, and anyone who writes | MIT |
| [last30days](https://github.com/mvanhorn/last30days-skill) by Matt Van Horn | Searches what people said about a topic in the last 30 days on Reddit, X, YouTube, TikTok, Hacker News and more | Research, Creator, Content, Sales | MIT |
| [impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus | A design vocabulary for coding agents: commands to steer a design (bolder, quieter, typeset, layout), review it (critique, audit) and finish it (polish, harden, adapt), plus checks for AI-looking design | Design, Coding, Funnel, QA | Apache-2.0 |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) by Leonxlnx | Art direction for websites: reference images, a design system and a real browser check before a page counts as done | Design, Coding, Funnel | MIT |

## Install

**The easy way.** Paste this into your main agent, with the link of the repo you want:

```
Install the skills from [REPO LINK] for this project. Then tell me what you installed, where you put it and how I use it.
```

**The commands.** Run these in a terminal in your project folder. `npx` needs [Node.js](https://nodejs.org).

| Repo | Command |
|---|---|
| marketingskills | `npx skills add coreyhaines31/marketingskills`, or only the ones you want: `npx skills add coreyhaines31/marketingskills --skill cro copywriting` |
| no-ai-slop | `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` |
| last30days | `npx skills add mvanhorn/last30days-skill -g` |
| impeccable | `npx impeccable install`, then restart your AI tool and run `/impeccable init` (in Codex: `$impeccable init`) |
| taste-skill | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` |

**Claude Code plugins.** Four of the repos also install as Claude Code plugins. For each one, run the first line, then the second:

```
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills

/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days

/plugin marketplace add Leonxlnx/taste-skill
/plugin install taste-skill@taste-skill

/plugin marketplace add pbakaus/impeccable
```

For impeccable, open `/plugin` after the first line and install it from the list.

**If a skill doesn't show up.** The `npx skills` installer asks which AI tool to install for. When an agent runs it for you, it can skip that question and put the files in `.agents/skills/`, which Claude Code doesn't read. Run it again with the tool named, like `npx skills add coreyhaines31/marketingskills -a claude-code`, then start a new session. Each repo's README has the current steps if a command has changed.

## How the team uses them

- **Writing.** Every agent that writes uses [anti-ai-slop-writing](../skills/anti-ai-slop-writing/SKILL.md) from this repo first, with its scanner. no-ai-slop is a second check. When the two disagree, the phrases in `my-business/allow.txt` and the Voice card in the Brain decide.
- **Design.** [conversion-design](../skills/conversion-design/SKILL.md) is built from the 124 funnel templates plus the rules impeccable and taste-skill agree on: real hierarchy, real images, fewer effects and a browser check before shipping. Use impeccable's critique and polish commands and taste-skill's browser check as extra passes. The Style block in the Brain sets the look.
- **Research.** last30days finds what people said this month. [deep-market-research](../skills/deep-market-research/SKILL.md) and [outlier-research](../skills/outlier-research/SKILL.md) decide what to do with it. Reddit, Hacker News and GitHub work with no setup. A setup wizard adds X, YouTube, TikTok and other sources, and some of those need their own keys.
- **Marketing.** marketingskills covers ground this repo doesn't, like SEO, ad platforms and pricing pages. Use it with the frameworks here: an offer still goes through the [Winning Offer Formula](../skills/winning-offer-formula/SKILL.md) and a page through [17p-sections](../skills/17p-sections/SKILL.md).

When an agent uses an outside skill on a piece of work, it names the skill in the handoff note, so you know where an idea came from.

## Before you install any skill

1. Read its `SKILL.md` first. Skills are instructions, and some come with scripts your AI tool can run.
2. Install from repos you trust, and check the license if you plan to share or sell what you build with it.
3. Never paste API keys or passwords into a chat. If a skill needs a key, follow its README and keep the key in your AI tool's settings or a local file that isn't committed.
4. Nothing from the PRIVATE section of the Brain goes into an outside service a skill calls.
5. Tell the COO which skills you installed and which agents should use them. The COO lists them in each agent's setup file, `my-business/team/<agent>.md`.

## Your own skills

Put skills you write yourself in `my-business/skills/<name>/SKILL.md`. The steps are in [skills/INDEX.md](../skills/INDEX.md). Updates to this repo never touch `my-business/`.
