# Privacy Policy — P2P (Prompt to Prompt)

Effective: 14 October 2026

P2P is a Claude plugin made of plain-text skill and agent files. It contains no scripts, hooks or MCP servers, and it has no servers of its own.

## What P2P collects

Nothing. The author of P2P does not receive, store or process any data from you or from your conversations.

## Where your data goes

Everything you write is processed by Claude under Anthropic’s terms and privacy policy. P2P adds no recipient of its own and makes no background network calls: it downloads nothing and sends nothing anywhere.

## Web search

When a task needs current information, the QUORUM roles may search the web or read a page you point them to. They use the tools of your Claude app and name their sources.

## Files

P2P writes files only when you ask:

- `/p2p:capsule save` writes the session state to your project folder;
- your profile goes to `p2p.config.md` only if you choose to save it (menu item 17).

Nothing else is written. These files stay with you; you can read, edit or delete them at any time. The QUORUM agents read and search; they cannot write files or run commands.

## Reports

`/p2p:report` builds a report with facts about P2P only: which features ran, routes, target models, where P2P went wrong, and your rating if you give one. It never contains the text of your requests, prompts or files, names of people, projects or companies, paths, addresses, keys or passwords. You see the report in full, and P2P never sends it. If you choose to share it as an issue in this repository, it becomes public on GitHub under GitHub’s terms.

## Optional Live Specs file

If you download `live_specs.md` from the releases page and attach it, Claude reads it like any other file you provide.

## Children

P2P is not intended for users under 18.

## Changes and contact

Changes to this policy are published in this file; its commit history shows every change. Questions: open an issue at https://github.com/sanic732/P2P/issues.
