"""Mostra quais skills voce realmente usa, lendo as transcricoes locais do Claude Code.

Uso:
    py uso.py                      # ranking de uso (todas as transcricoes)
    py uso.py --pasta CAMINHO      # outra pasta de transcricoes
    py uso.py --catalogo           # compara com as fichas de catalogo/ (usadas x sem uso)
Nada sai do PC. Serve para decidir quais skills/plugins valem o espaco que ocupam.
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).parent
PADRAO = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude") / "projects"


def contar(pasta):
    usos = defaultdict(lambda: {"vezes": 0, "sessoes": set(), "projetos": set()})
    vistos = set()
    for arq in pasta.rglob("*.jsonl"):
        projeto = arq.relative_to(pasta).parts[0]
        with arq.open(encoding="utf-8", errors="ignore") as f:
            for linha in f:
                if '"name":"Skill"' not in linha:
                    continue
                try:
                    msg = json.loads(linha).get("message") or {}
                except ValueError:
                    continue
                conteudo = msg.get("content")
                if not isinstance(conteudo, list):
                    continue
                for bloco in conteudo:
                    if isinstance(bloco, dict) and bloco.get("type") == "tool_use" and bloco.get("name") == "Skill":
                        if bloco.get("id") in vistos:
                            continue
                        vistos.add(bloco.get("id"))
                        nome = (bloco.get("input") or {}).get("skill")
                        if nome:
                            u = usos[nome]
                            u["vezes"] += 1
                            u["sessoes"].add(arq.stem)
                            u["projetos"].add(projeto)
    return usos


def fichas():
    nomes = set()
    for md in (RAIZ / "catalogo").glob("*.md"):
        nomes.update(re.findall(r"^### `([^`]+)`", md.read_text(encoding="utf-8"), flags=re.M))
    return nomes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta", type=Path, default=PADRAO)
    ap.add_argument("--catalogo", action="store_true")
    args = ap.parse_args()
    usos = contar(args.pasta)
    print("| Skill | Vezes | Sessoes | Projetos |\n|---|--:|--:|--:|")
    for nome, u in sorted(usos.items(), key=lambda kv: -kv[1]["vezes"]):
        print(f"| {nome} | {u['vezes']} | {len(u['sessoes'])} | {len(u['projetos'])} |")
    por_plugin = defaultdict(int)
    for nome, u in usos.items():
        por_plugin[nome.split(":")[0] if ":" in nome else "(usuario)"] += u["vezes"]
    print("\nPor plugin:", ", ".join(f"{k}={v}" for k, v in sorted(por_plugin.items(), key=lambda kv: -kv[1])))
    if args.catalogo:
        com_ficha = fichas()
        print(f"\nFichas no catalogo: {len(com_ficha)}")
        print("Usadas sem ficha (vale escrever):", ", ".join(sorted(set(usos) - com_ficha)) or "nenhuma")
        print("Com ficha e nunca usadas:", ", ".join(sorted(com_ficha - set(usos))) or "nenhuma")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
