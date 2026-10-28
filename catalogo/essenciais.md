# Fichas: quando vale a pena usar (essenciais)

Formato fixo para cada skill: o que faz, quando vale, quando não vale, por quê, custo em tokens (baixo, médio, alto).
Fonte: descrições dos plugins + uso real nas transcrições do autor. São julgamentos, não testes formais. Corrija com PR.

## Planejar e pensar

### `anthropic-skills:planejamento`
- **Faz:** organiza uma ideia em plano, roteiro, checklist ou cronograma.
- **Vale quando:** o pedido é vago ("quero montar X") e precisa virar passos.
- **Não vale quando:** a tarefa já é clara e pequena; só atrasa.
- **Por quê:** estruturar antes evita retrabalho em projetos grandes. **Custo:** baixo.

### `anthropic-skills:deep-research`
- **Faz:** pesquisa profunda em várias fontes com relatório.
- **Vale quando:** decisão que depende de fatos externos atuais (ferramenta, preço, lei).
- **Não vale quando:** a resposta está no projeto ou o modelo já sabe.
- **Por quê:** a busca ampla compensa só se o erro custa caro. **Custo:** alto.

### `anthropic-skills:conselheiro-critico`
- **Faz:** dá crítica honesta a uma ideia ou decisão.
- **Vale quando:** você quer contraponto antes de investir tempo.
- **Não vale quando:** já decidiu e só quer executar. **Custo:** baixo.

## Documentos

### `anthropic-skills:docx` / `pdf` / `pptx` / `xlsx`
- **Fazem:** criam e editam Word, PDF, apresentações e planilhas.
- **Valem quando:** a entrega precisa ser o arquivo Office/PDF final.
- **Não valem quando:** Markdown ou página HTML resolve. **Custo:** médio (geram arquivo e conferem).

### `anthropic-skills:notebooklm-mcp` (e `notebooklm-*`)
- **Faz:** consulta e alimenta seus cadernos do NotebookLM.
- **Vale quando:** a resposta deve vir das suas fontes (estudo, mentor de negócios, programação).
- **Não vale quando:** pergunta geral. **Custo:** baixo.

## Código e qualidade

### `engineering:code-review` e `code-review`
- **Fazem:** revisam mudanças procurando bugs.
- **Valem quando:** antes de publicar ou abrir PR.
- **Não valem quando:** edição trivial de texto/CSS. **Custo:** médio; o modo `ultra` é alto e cobrado à parte.

### `engineering:debug`
- **Faz:** investiga um erro por hipóteses.
- **Vale quando:** o bug não é óbvio ou já falhou uma tentativa.
- **Não vale quando:** a mensagem de erro já aponta a linha. **Custo:** médio.

### `engineering:testing-strategy`
- **Faz:** define o que testar e como.
- **Vale quando:** projeto novo ou sem testes.
- **Não vale quando:** script de uso único. **Custo:** baixo.

### `engineering:documentation`
- **Faz:** escreve README, runbook e guia.
- **Vale quando:** o projeto vai ser retomado em outra sessão (ótimo para `docs/ESTADO.md`).
- **Não vale quando:** comentário de uma linha. **Custo:** baixo.

### `engineering:architecture` / `system-design`
- **Fazem:** decisão de arquitetura e desenho de sistema.
- **Valem quando:** escolher entre abordagens antes de codar (banco, sincronização, camadas).
- **Não valem quando:** ajuste pequeno. **Custo:** médio.

### `simplify`
- **Faz:** limpa o código que você acabou de mudar (reuso, simplicidade).
- **Vale quando:** depois de uma feature grande.
- **Não vale quando:** buscar bugs (use `code-review`). **Custo:** médio.

### `security-review`
- **Faz:** revisão de segurança da branch.
- **Vale quando:** mexeu em login, tokens, entrada de dados, `.env`.
- **Não vale quando:** só visual. **Custo:** médio.

### `ultrapowers-dev:testing-tdd`
- **Faz:** guia de testes primeiro (TDD).
- **Vale quando:** lógica com regras (cálculos, regras de negócio). **Não vale quando:** página estática. **Custo:** baixo.

### `ultrapowers-dev:resilience`
- **Faz:** retries, timeouts e falhas parciais.
- **Vale quando:** robôs que chamam sites e APIs externas. **Não vale quando:** código local simples. **Custo:** baixo.

### `ultrapowers-dev:python-best-practices` / `javascript-best-practices`
- **Fazem:** convenções modernas da linguagem.
- **Valem quando:** começando módulo novo ou limpando código antigo.
- **Não valem quando:** corrigir uma linha. **Custo:** baixo.

### `ultrapowers-dev:browser-automation`
- **Faz:** padrões para automatizar navegador (formulários, extração).
- **Vale quando:** robôs de vaga e scraping. **Não vale quando:** existe API. **Custo:** baixo.

## Interface e design

### `frontend-design:frontend-design`
- **Faz:** direção visual com identidade, sem cara de template.
- **Vale quando:** criar página/app novo e a aparência importa.
- **Não vale quando:** ajustar um botão. **Custo:** médio.

### `ultrapowers-dev:web-design-guidelines`
- **Faz:** revisa UI contra boas práticas e acessibilidade.
- **Vale quando:** antes de entregar uma tela. **Custo:** baixo.

### `design-skills:accessibility-audit`
- **Faz:** auditoria WCAG com correções.
- **Vale quando:** o site é público ou para clientes. **Não vale quando:** protótipo interno. **Custo:** médio.

### `design-skills:ux-writing`
- **Faz:** revisa textos de botões, erros e vazios.
- **Vale quando:** polir app antes de mostrar. **Custo:** baixo.

### `figma:figma-use` e `figma:figma-design-to-code`
- **Fazem:** editar designs no Figma e transformar um design em código.
- **Valem quando:** há link do Figma. `figma-use` é obrigatório antes de escrever no arquivo.
- **Não valem quando:** não há Figma. **Custo:** médio/alto (muitas ferramentas).

## Mobile

### `expo:expo-router` / `expo-native-ui` / `expo-ui`
- **Fazem:** navegação, UI nativa e componentes no Expo.
- **Valem quando:** trabalhando num app Expo. **Custo:** baixo.

### `expo:eas-update` / `eas-app-stores`
- **Fazem:** atualização OTA e publicação nas lojas.
- **Valem quando:** vai publicar ou corrigir app já publicado. **Custo:** baixo.

### `expo:expo-upgrade`
- **Faz:** atualiza a versão do Expo/SDK.
- **Vale quando:** projeto parado e desatualizado. **Não vale quando:** funciona e não precisa. **Custo:** médio.

## Cloudflare

### `cloudflare` / `wrangler` / `workers-best-practices`
- **Fazem:** guiam Workers, deploy e boas práticas.
- **Valem quando:** o projeto usa Workers/Pages. **Não valem quando:** hospedagem em outro lugar. **Custo:** baixo/médio.

## Marketing e carreira

### `marketing-skills:copywriting` / `cro` / `seo-audit`
- **Fazem:** texto que vende, conversão e auditoria de SEO.
- **Valem quando:** páginas de venda, landing, anúncios. **Não valem quando:** texto interno. **Custo:** baixo/médio.

### `marketing-skills:video`
- **Faz:** orienta produção de vídeo com IA e Remotion.
- **Vale quando:** pasta `videos`. **Custo:** baixo.

### `ojobinho:*` e `career-desk:cv-tailor` / `interview-prep`
- **Fazem:** avaliar vaga, adaptar currículo sem inventar fatos e preparar entrevista.
- **Valem quando:** candidatura real com vaga em mãos. **Não valem quando:** só navegando vagas. **Custo:** baixo.

## Sessão e configuração

### `skill-creator`
- **Faz:** cria e melhora skills.
- **Vale quando:** você repete a mesma instrução em várias sessões. **Custo:** médio.

### `update-config`
- **Faz:** mexe em `settings.json`, hooks e permissões.
- **Vale quando:** quer automação que o Claude não faz sozinho ("sempre que X, faça Y"). **Custo:** baixo.

### `loop` / `schedule`
- **Fazem:** repetem ou agendam tarefas.
- **Valem quando:** monitoramento recorrente. **Não valem quando:** tarefa única. **Custo:** pode ser alto se rodar muito; defina intervalo longo.

### `graphify`
- **Faz:** grafo de conhecimento do código e documentos.
- **Vale quando:** projeto grande que você quer entender sem ler tudo. **Não vale quando:** projeto pequeno (o RAG basta). **Custo:** médio na geração, baixo depois.

