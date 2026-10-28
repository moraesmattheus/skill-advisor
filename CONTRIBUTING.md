# Contributing / Contribuindo

## Add a stack rule / Adicionar regra de stack
Edit `regras.json`. Each rule: `id`, `quando` (any of `arquivos`, `pacotes`, `texto`, `sem`, `arquivos_min`), `skills` (`plugin:skill`, or `conector:Name`), and a reason in `pt` and `en`. A leading `/` in `arquivos` means "project root only". Use `exceto` to skip a rule when another matched.

## Add a card / Adicionar ficha
Run `python uso.py --catalogo`, see "used without a card", and add to `catalogo/<group>.md`:

```
### `plugin:skill`
- **Faz:** one sentence.
- **Vale quando:** a concrete situation.
- **Não vale quando:** when it is overkill or gets in the way.
- **Por quê:** the reason. **Custo:** baixo, médio or alto (tokens).
```

## Rules / Regras
- Only describe what you used or read in the skill; mark guesses as "not tested".
- No personal data, project names, paths or tokens.
- Stay offline: scripts must not make network calls.
- Open a pull request. Translations of cards are welcome in `catalogo/<lang>/`.
