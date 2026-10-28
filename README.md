# skill-advisor

> Português: [README.pt-BR.md](README.pt-BR.md)

A Claude Code skill that **reads your project and tells you which skills to use, when they are worth it, and when they are not**, in your own language. Built for people with dozens of plugins who are burning tokens on skills they never use.

## What it does
- **Detects your stack** from files, dependencies, scripts and docs (`detectar.py`, plain Python, no network, no model tokens).
- **Suggests skills** by stack (`regras.json`): Expo, Next.js, Python, Cloudflare Workers, Kotlin, Swift, Remotion, Supabase, static sites, and more.
- **Explains when each is worth using** (`catalogo/`): what it does, worth it when, not worth it when, token cost.
- **Speaks your language.** Descriptions are English; the skill translates them for you. The script outputs Portuguese and English natively.
- **Flags what is missing** and shows where to get it. **It never installs anything without your explicit yes.**
- **`uso.py`** reads your local transcripts and shows which skills you really use, so you can decide what is worth the space it takes.

## Install
As a plugin (recommended), from a clone of this repo:
```
/plugin marketplace add <path-or-url-of-this-repo>
/plugin install skill-advisor
```
Or as a standalone skill: copy `skills/skill-advisor/` to `~/.claude/skills/` and keep the repo next to it (the skill looks for `detectar.py` two folders above its `SKILL.md`).

## Use
Say "suggest skills" inside a project, or run the detector yourself:
```
python detectar.py              # full report for the current folder
python detectar.py --lang en    # force a language (pt or en)
python uso.py --catalogo        # what you actually use vs. what has a card
```

## Optional: automatic suggestion at session start
Add to your `settings.json`. It prints about 3 lines when a session starts in a project folder, and nothing elsewhere:
```json
"hooks": {
  "SessionStart": [
    { "matcher": "startup",
      "hooks": [ { "type": "command", "command": "python /path/to/skill-advisor/detectar.py --curto", "timeout": 10 } ] }
  ]
}
```
Hooks run commands on your machine; read `detectar.py` first (it only reads files in the project folder).

## Privacy and safety
Everything runs locally. Nothing is sent anywhere. The detector only reads file names, dependency lists and the first 30 KB of README/CLAUDE.md/AGENTS.md. `uso.py` only reads your local transcripts.

## Contribute
Add stacks to `regras.json`, cards to `catalogo/`, or a language. See [CONTRIBUTING.md](CONTRIBUTING.md). MIT license.
