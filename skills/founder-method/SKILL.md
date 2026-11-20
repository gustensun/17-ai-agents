---
name: founder-method
description: Plan and build an AI operating system (an app with a context layer, AI agents and one approvals queue, connected to the CRM the business already sells from) with the FOUNDER Method, seven steps from Focus to Refine and cut, with the five layers, six guardrails, a simple stack and the checklist. Use when the owner wants their own AI OS, a client portal or dashboard with AI, or any app that puts AI agents on top of an existing sales system.
---

# The FOUNDER Method: build your AI OS

An AI OS sits between what you know and the system you already sell from.

| Your context | Your AI OS | Your sales system |
|---|---|---|
| What the AI learns from: docs, calls and links, brand voice and writing, offers and funnels, research and examples | Where the work happens: a chat and voice assistant, specialist AI agents, one approvals queue, and the content, pages, emails and graphics they make | Your system of record: the CRM and pipelines, funnels and checkout, courses and email |

This repo is the context layer and the agents. The FOUNDER Method turns them into an app.

## What you'll have at the end

1. **A one-page brief:** who the OS serves and the work it takes off their plate.
2. **A clickable demo:** screens you can show and test before any backend exists.
3. **A context layer:** your knowledge, voice and offers, read first by every AI feature.
4. **Your first agent:** it drafts the work, and nothing ships until you approve it.
5. **A live app:** connected to your CRM, running on your own API keys.

## The five layers

Build from the bottom up. Start with Context: every layer above it gets better when the AI knows the business.

| Layer | What it is |
|---|---|
| 5 Connections | Each user connects their own API keys. MCP lets Claude or Codex work inside it. |
| 4 Execution | The system you already sell from: CRM, funnels, courses, email. |
| 3 Creation | Where drafts are made and approved: content, pages, emails, graphics. |
| 2 Intelligence | The AI that does the work: chat, voice and specialist agents. |
| 1 Context | What the AI knows: docs, brand voice, offers and approved facts. |

## The seven steps

| Step | Do this | Done when |
|---|---|---|
| F: Focus | Pick one user and one path. Name your user in one sentence, list their weekly tasks and pick the three biggest. | You have a one-page brief. |
| O: Own your system | Build on top of where sales already live. Name your [CRM], decide what the OS adds on top, and never rebuild what already works. | You know exactly what the OS adds. |
| U: Upload context | Give the AI what it needs to know. Collect docs, calls, offers and writing, turn them into short approved facts, and make every AI feature read them first. | The AI explains your business correctly. |
| N: Nail the demo | Clickable screens before any backend. Turn the brief into one detailed build prompt, generate the screens with sample data, and click through them the way your user would. | Someone understands it without your help. |
| D: Delegate to agents | Agents draft, you approve. Start with one agent for your biggest time cost, send every draft to one approvals queue, and the AI never overwrites what you wrote unless asked. | The agent saves you time every week. |
| E: Engineer the stack | Login, data, your own keys, MCP. Add login, a database and auto-deploy, let each user connect their own API keys, and add an MCP server so Claude or Codex can work inside it. | The app is live on your own domain. |
| R: Refine and cut | Test every release and remove what you skip. Use the OS yourself every day for a week, write a test for every release, and cut every screen you skip. | Every page earns its place. |

In this repo, the Brain and the setup interview cover step U, the agent cards cover step D, and `my-business/queue.md` with the approval rules is the approvals queue.

## The six guardrails

1. **Approve everything.** Nothing publishes or sends on its own.
2. **One idea queue.** Every AI idea lands in approvals first.
3. **Protect your work.** AI never overwrites what you wrote unless asked.
4. **Don't rebuild the CRM.** Your system of record stays in charge.
5. **Bring your own keys.** Each user connects their own accounts.
6. **Cut ruthlessly.** If you don't use a screen, remove it.

## A simple stack

Keep the stack simple, so your effort goes into the AI layer.

| Part | Start with |
|---|---|
| Front end | Plain HTML, CSS and JavaScript |
| Back end | Serverless functions on [HOSTING] |
| Data and login | [DATABASE] for accounts, the database and file storage |
| AI models | [AI MODEL PROVIDER], plus [VOICE PROVIDER] if you want voice |
| System of record | The [CRM] you already sell from |
| Build loop | Claude Code or Codex writes it, [CODE HOST] stores it, [HOSTING] deploys it |

## The checklist

Tick off each item before you move to the next step.

- **F Focus:** one-sentence user and outcome written. Weekly tasks listed. Top three tasks chosen. One-page brief saved.
- **O Own your system:** system of record named. What the OS adds is written down. Nothing rebuilt that it already does. The data you need from it is listed.
- **U Upload context:** docs, calls and offers collected. Writing samples added. Short facts written and approved. The AI explains your business correctly.
- **N Demo:** build prompt written. Demo screens with sample data. Clicked through as the user.
- **D Agents:** first agent picked. Approvals queue working. No AI overwrites without asking.
- **E Stack:** login, database and auto-deploy. Users add their own keys. MCP server live on your domain.
- **R Refine:** used daily for a week. A test for every release. Unused screens removed.

## The first assignment

Write the one-page brief before you build anything. Answer three questions:

1. Who is this OS for, in one sentence?
2. Which three weekly tasks will it take off their plate?
3. Where do your customers and sales already live?

The Coding agent builds from the brief, QA tests every release, and the owner approves each step before the next one starts. Keys never go in the code or in the repo: each user adds their own in the app's settings.
