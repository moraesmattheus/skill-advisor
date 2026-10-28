"""Le o projeto atual e recomenda skills, sem gastar tokens do modelo.

Uso:
    py detectar.py                 # relatorio completo da pasta atual
    py detectar.py CAMINHO         # outra pasta
    py detectar.py --curto         # 3 a 5 linhas (usado pelo hook de inicio de sessao)
    py detectar.py --json          # saida para a skill processar
    py detectar.py --lang en|pt    # idioma (padrao: o do sistema)
Regras em regras.json; fontes de instalacao em fontes.json. Nada sai do PC.
"""
import argparse
import fnmatch
import json
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
IGNORAR = {
    "node_modules", ".git", ".venv", "venv", "__pycache__", "dist", "build", ".gradle", ".expo", "out",
    ".next", ".cache", ".turbo", ".wrangler", ".kotlin", ".pytest_cache", "graphify-out",
}
DOCS = ("README.md", "CLAUDE.md", "AGENTS.md")
TEXTOS = {
    "pt": {"projeto": "Projeto", "sinais": "Sinais", "sugestoes": "Skills sugeridas", "comandos": "Comandos do projeto",
           "nada": "Nenhum sinal claro de stack aqui; nenhuma skill sugerida.", "dica": "Diga \"sugerir skills\" para o plano completo ou \"instalar <skill>\" para baixar (peço confirmação).",
           "verificar": "Confira quais estão instaladas; as que faltam têm fonte em fontes.json."},
    "en": {"projeto": "Project", "sinais": "Signals", "sugestoes": "Suggested skills", "comandos": "Project commands",
           "nada": "No clear stack signals here; no skills suggested.", "dica": "Say \"suggest skills\" for the full plan or \"install <skill>\" to download (I will ask first).",
           "verificar": "Check which are installed; missing ones have a source in fontes.json."},
}


def idioma(escolha):
    if escolha in TEXTOS:
        return escolha
    try:
        import ctypes
        return "pt" if (ctypes.windll.kernel32.GetUserDefaultUILanguage() & 0x3FF) == 0x16 else "en"
    except Exception:
        return "pt" if os.environ.get("LANG", "").lower().startswith("pt") else "en"


def varrer(raiz, profundidade=3, limite=3000):
    arquivos = []
    base = len(raiz.parts)
    for atual, dirs, nomes in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in IGNORAR]
        if len(Path(atual).parts) - base >= profundidade:
            dirs[:] = []
        for n in nomes:
            arquivos.append((Path(atual) / n).relative_to(raiz).as_posix())
        if len(arquivos) >= limite:
            break
    return arquivos


def pacotes(raiz):
    achados, scripts = set(), []
    for pj in [raiz / "package.json", *raiz.glob("*/package.json")]:
        if pj.parent != raiz and pj.parent.name in IGNORAR:
            continue
        try:
            dados = json.loads(pj.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for chave in ("dependencies", "devDependencies"):
            achados.update((dados.get(chave) or {}).keys())
        if pj.parent == raiz:
            scripts = list((dados.get("scripts") or {}).keys())
    for req in [raiz / "requirements.txt", *raiz.glob("*/requirements.txt")]:
        try:
            for linha in req.read_text(encoding="utf-8", errors="ignore").splitlines():
                nome = re.split(r"[=<>~\[;\s]", linha.strip().lower())[0]
                if nome and not nome.startswith("#"):
                    achados.add(nome)
        except OSError:
            pass
    pyproject = raiz / "pyproject.toml"
    if pyproject.exists():
        achados.update(re.findall(r"[\"']([a-z0-9_.-]+)[><=~\[ ]", pyproject.read_text(encoding="utf-8", errors="ignore").lower()))
    return achados, scripts


def texto_docs(raiz):
    partes = []
    for d in DOCS:
        f = raiz / d
        if f.is_file():
            partes.append(f.read_text(encoding="utf-8", errors="ignore")[:30000].lower())
    return "\n".join(partes)


def casa_arquivo(padrao, arquivos):
    if padrao.startswith("/"):  # so na raiz do projeto
        return any(fnmatch.fnmatch(a, padrao[1:]) for a in arquivos if "/" not in a)
    if "/" in padrao:
        return any(fnmatch.fnmatch(a, padrao) for a in arquivos)
    return any(fnmatch.fnmatch(a.rsplit("/", 1)[-1], padrao) for a in arquivos)


def avaliar(raiz):
    arquivos = varrer(raiz)
    pkgs, scripts = pacotes(raiz)
    texto = texto_docs(raiz)
    regras = json.loads((RAIZ / "regras.json").read_text(encoding="utf-8"))
    ativas = []
    for r in regras:
        q = r["quando"]
        ok = (
            any(casa_arquivo(p, arquivos) for p in q.get("arquivos", []))
            or any(p in pkgs for p in q.get("pacotes", []))
            or any(t in texto for t in q.get("texto", []))
            or any(not (raiz / s).exists() for s in q.get("sem", []))
            or ("arquivos_min" in q and len(arquivos) >= q["arquivos_min"])
        )
        if ok:
            ativas.append(r)
    ids = {r["id"] for r in ativas}
    ativas = [r for r in ativas if not set(r.get("exceto", [])) & ids]
    sinais = [r for r in ativas if "sem" not in r["quando"] and "arquivos_min" not in r["quando"]]
    if not sinais:
        return [], scripts
    return ativas, scripts


def principais(ativas, limite):
    vistos, saida = set(), []
    for r in ativas:
        for s in r["skills"]:
            if s not in vistos:
                vistos.add(s)
                saida.append((s, r))
    return saida[:limite] if limite else saida


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("caminho", nargs="?", default=".")
    ap.add_argument("--curto", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lang", default="auto")
    args = ap.parse_args()
    raiz = Path(args.caminho).resolve()
    lang = idioma(args.lang)
    t = TEXTOS[lang]
    ativas, scripts = avaliar(raiz)
    if args.json:
        print(json.dumps({"projeto": raiz.name, "idioma": lang, "regras": [r["id"] for r in ativas],
                          "skills": [{"skill": s, "motivo": r[lang]} for s, r in principais(ativas, 0)],
                          "scripts": scripts}, ensure_ascii=False, indent=2))
        return
    if not ativas:
        if not args.curto:
            print(t["nada"])
        return
    ids = ", ".join(r["id"] for r in ativas)
    if args.curto:
        top = principais(ativas, 5)
        print(f"[skill-advisor] {t['projeto']}: {raiz.name} ({ids})")
        print(f"{t['sugestoes']}: " + ", ".join(s for s, _ in top))
        print(t["dica"])
        return
    print(f"# {t['projeto']}: {raiz.name}\n{t['sinais']}: {ids}\n")
    print(f"## {t['sugestoes']}")
    for r in ativas:
        print(f"- {r[lang]}\n  -> " + ", ".join(r["skills"]))
    if scripts:
        print(f"\n## {t['comandos']}\n" + ", ".join(scripts))
    print(f"\n{t['verificar']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
