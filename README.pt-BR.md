# skill-advisor

> English: [README.md](README.md)

Skill do Claude Code que **lê o seu projeto e diz quais skills usar, quando valem a pena e quando não**, no seu idioma. Feita para quem tem dezenas de plugins e gasta tokens com skills que nunca usa.

## O que faz
- **Detecta a stack** por arquivos, dependências, scripts e docs (`detectar.py`, Python puro, sem rede e sem gastar tokens do modelo).
- **Sugere skills** por stack (`regras.json`): Expo, Next.js, Python, Cloudflare Workers, Kotlin, Swift, Remotion, Supabase, sites estáticos e mais.
- **Explica quando vale usar** (`catalogo/`): o que faz, vale quando, não vale quando, custo em tokens.
- **Fala o seu idioma.** As descrições vêm em inglês; a skill traduz. O script já responde em português e inglês.
- **Avisa o que falta** e mostra onde conseguir. **Nunca instala nada sem o seu "sim" explícito.**
- **`uso.py`** lê suas transcrições locais e mostra quais skills você realmente usa.

## Instalar
Como plugin (recomendado), em um passo (Claude Code 2.1.275 ou mais novo):
```
/plugin install skill-advisor --marketplace moraesmattheus/skill-advisor
```
Ou em dois passos, no terminal:
```
claude plugin marketplace add moraesmattheus/skill-advisor
claude plugin install skill-advisor@skill-advisor
```
Ou como skill avulsa: copie `skills/skill-advisor/` para `~/.claude/skills/` e mantenha o repositório ao lado (a skill procura o `detectar.py` duas pastas acima do `SKILL.md`).

## Usar
Diga "sugerir skills" dentro de um projeto, ou rode o detector:
```
python detectar.py              # relatório da pasta atual
python detectar.py --lang en    # força o idioma (pt ou en)
python uso.py --catalogo        # o que você usa de verdade x o que tem ficha
```

## Opcional: sugestão automática ao abrir a sessão
Veja o trecho de `settings.json` no [README em inglês](README.md#optional-automatic-suggestion-at-session-start). Hooks rodam comandos na sua máquina; leia o `detectar.py` antes (ele só lê arquivos da pasta do projeto).

## Privacidade
Tudo roda localmente. Nada é enviado. O detector lê só nomes de arquivos, listas de dependências e os primeiros 30 KB de README/CLAUDE.md/AGENTS.md.

## Contribuir
Veja [CONTRIBUTING.md](CONTRIBUTING.md). Licença MIT.
