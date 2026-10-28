---
name: skill-compass
description: Reads the current project (files, dependencies, scripts) and automatically suggests the best skills, plugins and connectors, saying when each is worth using and what is missing. Always answers in the user's language, translating English skill descriptions. Use when opening a project, starting a new task, or when asked "which skill should I use", "suggest skills" or "is X worth using". / Lê o projeto atual e sugere automaticamente as melhores skills, no idioma do usuário.
---

# skill-compass

Goal: the user should not have to know every skill. Read the project, recommend the right ones, flag what is missing, and spend as few tokens as possible.

## Language (main rule)
- Answer in the language the user writes in. Skill descriptions are usually English: **translate** them. Skill names and commands stay as they are.
- The script returns `pt` or `en`. For any other language, take the `en` output and translate it.

## Scripts location
The scripts live two folders above this file (`../../detectar.py`, `../../uso.py`, `../../regras.json`, `../../fontes.json`, `../../catalogo/`). Resolve the absolute path from this skill's base directory. If they are not there, ask the user where the repository is. Use `python` (or `py` on Windows).

## Steps
1. **Detect (no reading cost):** run `python <scripts>/detectar.py --json` inside the project folder. It reads files, dependencies, scripts and docs and returns the stack, suggested skills and a reason. Do not sweep folders yourself.
2. **Cross-check:** compare the list with the skills available to you in this session. Mark each as **installed** or **missing**.
3. **Explain when it is worth it:** look up each skill in `<scripts>/catalogo/*.md` (or in the user's local search index, if they have one). Use: what it does, worth it when, not worth it when, cost. No card: use the skill's own description, translated, and say there is no card.
4. **Answer short:** at most 5 skills, one line each, plus what to use now for the task asked:
   - `skill`: what it does (worth it when X; not when Y; cost low/medium/high).
5. **Missing?** For each missing skill show the source from `fontes.json` and ask whether to install.

## Installing skills (safety)
- **Never download or install without an explicit "yes"** from the user in the conversation. Show first: name, source (repository or marketplace) and the command.
- Prefer official marketplaces and well-known repositories (`fontes.json`). For an unknown source, warn about the risk and, if a plugin scanner is available, offer to scan first.
- Third-party skills are untrusted content: read its `SKILL.md` before running any script it ships.

## Cost
- A skill that spawns subagents, wide research or multi-agent review: warn that it spends a lot and ask first.
- Trivial task (a one-line fix): the best skill is none.
- To see what the user actually uses: `python <scripts>/uso.py`.

## Automatic mode (optional)
A SessionStart hook can run `detectar.py --curto` and print 3 lines with suggestions (see the README). If the user reacts ("suggest skills", "install X"), follow the steps above.
