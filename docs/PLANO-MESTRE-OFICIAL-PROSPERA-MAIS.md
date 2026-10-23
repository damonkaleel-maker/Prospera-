# PLANO MESTRE OFICIAL — PRÓSPERA +

**Versão:** 1.0 — ponto de partida para consolidação  
**Data de consolidação inicial:** 23/10/2026  
**Plataforma-alvo:** Android (APK), com foco de uso pessoal em Samsung Galaxy A35  
**Idioma e convenções:** português brasileiro; moeda BRL (R$); datas e números no padrão brasileiro  
**Status:** especificação-base. A inclusão deste documento no repositório não certifica que os recursos já estejam implementados, que os testes tenham passado ou que exista APK aprovado.

## 1. Finalidade e autoridade do documento

Este documento reúne os requisitos, decisões de produto, regras financeiras, diretrizes visuais, arquitetura pretendida, testes e critérios de aceite conhecidos para o Próspera +. É o ponto de partida para consolidar o passo a passo de desenvolvimento e auditoria.

Em caso de divergência, não presumir que o código esteja correto apenas por existir. Comparar o código e o comportamento real com este plano, registrar evidências e resolver divergências explicitamente. Atualizações futuras devem indicar o que mudou, por que mudou e quais testes comprovam a mudança.

### Regras invioláveis
1. Não reconstruir o aplicativo do zero nem substituir a implementação existente sem auditoria e autorização explícita.
2. Não remover recursos, identificadores, fluxos ou dados existentes sem análise de impacto e aprovação.
3. Preservar os identificadores de interface e as chaves de armazenamento existentes sempre que possível.
4. Não apagar nem migrar destrutivamente dados locais; toda migração deve ser compatível, validada e reversível quando viável.
5. Não contar transferências internas como receita ou despesa e não duplicar movimentações, ativos, saldos ou resultados.
6. Não declarar uma correção, teste, emulação ou build como concluído sem evidência verificável.
7. Não colocar Client Secret, tokens privados, credenciais ou chaves privilegiadas no APK, no código público ou em logs.
8. Alterar a interface, a navegação e a identidade visual somente dentro do escopo aprovado.
9. Validar fórmulas financeiras com casos de referência, premissas explícitas e arredondamento documentado.
10. Quando uma causa-raiz for encontrada, corrigir a causa e suas ocorrências relacionadas, em vez de repetir verificações sem mudança comprovada.

## 2. Identidade visual e experiência

A direção visual é **premium, sofisticada e executiva**, com tema escuro e uma central de comando financeira.

- Base: preto profundo e azul-marinho escuro.
- Destaques: dourado fosco, prata/cinza e detalhes em verde-esmeralda ou ciano, usados com moderação.
- Vermelho: situação crítica ou risco.
- Amarelo: atenção ou pendência.
- Azul: planejamento ou informação.
- Verde: **exclusivamente estado concluído**, conforme regra expressa do produto; não usar verde como estado genérico de andamento.
- Layout compacto, legível e adaptado a telas móveis.
- Página inicial sem gráficos grandes; preferir indicadores claros e gráficos pequenos.
- Não mover botões, abas ou controles já estabelecidos sem justificativa e aprovação.
- Manter acessibilidade: contraste, áreas de toque adequadas, foco visível, rótulos compreensíveis e suporte a escalas de texto.

## 3. Navegação principal

A navegação inferior desejada contém cinco ações:
1. **Início** — painel geral.
2. **Movimentações** — receitas, despesas, transferências e registros financeiros.
3. **Novo lançamento** — ação central para registrar rapidamente.
4. **Gráficos / Análises** — visualização de tendências e indicadores.
5. **Mais** — páginas secundárias e configurações.

Identificadores de páginas a preservar e conferir no código:
- `page-dashboard`
- `page-movements`
- `page-graphs`
- `page-advanced`
- `page-investments`
- `page-payments`
- `page-projects`
- `page-allocation`
- `page-goals`
- `page-analytics`
- `page-openfinance`
- `page-categories`
- `page-settings`

A presença de um ID nesta lista é requisito de auditoria, não prova de que a página esteja funcional. Mapear cada página, seu acesso, suas ações e seus estados.

## 4. Início — central de comando

Apresentar, de forma resumida:
- Saldo disponível.
- Entradas e saídas no período selecionado.
- Patrimônio bruto e líquido.
- Dívidas e obrigações relevantes.
- Indicadores de metas e projetos.
- Alertas financeiros realmente aplicáveis.
- Resumo compacto e legível, sem simulações detalhadas na tela inicial.

Definições:
- **Saldo disponível** deve refletir recursos disponíveis de acordo com a regra de contas adotada, sem incluir valores indisponíveis como dinheiro livre.
- **Patrimônio bruto** representa ativos antes das obrigações.
- **Patrimônio líquido** considera ativos menos passivos.
- Não somar o mesmo ativo em mais de uma área nem somar transferência interna como nova receita ou despesa.
- Exibir período, data de atualização e origem dos dados quando isso for relevante.

## 5. Movimentações

Recursos esperados:
- Lista de movimentações com busca, filtros, ordenação e agrupamento por período.
- Filtros por todas, receitas, despesas, transferências e alocações, conforme a estrutura efetivamente adotada.
- Detalhe e edição de lançamento, quando permitido.
- Identificador único por registro e proteção contra salvamento duplicado.
- Categorias, data, valor, descrição e vínculos opcionais com metas, projetos, reservas, dívidas ou investimentos.
- Valores e totais recalculados após inclusão, edição ou exclusão válida.
- Importações e integrações futuras devem detectar duplicatas e preservar a origem do registro.

### Regra contábil básica
- Receita aumenta a entrada de recursos.
- Despesa reduz recursos.
- Transferência entre contas próprias movimenta valores entre contas, mas não é receita nem despesa consolidada.
- Alocação orçamentária não deve, por si só, criar uma segunda movimentação financeira.
- Estornos e correções devem manter trilha de auditoria quando aplicável.

## 6. Novo lançamento

Oferecer lançamento rápido e lançamento avançado. Os campos devem variar de acordo com o tipo, sem exigir dados irrelevantes.

Tipos e vínculos possíveis:
- Receita.
- Despesa.
- Transferência.
- Alocação orçamentária.
- Meta ou reserva.
- Projeto ou obra.
- Dívida, empréstimo ou obrigação.
- Ativo ou investimento.

Validar valor, data, categoria e tipo. Mostrar confirmação clara antes de ações destrutivas. Evitar que pressionar duas vezes ou repetir uma operação gere dois registros.

## 7. Categorias e orçamento

Categorias conhecidas a preservar ou confirmar:
- Casa
- Compras
- Alimentos
- Investimentos
- Saúde
- Projetos
- Metas
- Reserva
- Obra do Reino

Permitir organizar categorias e acompanhar valores planejados versus realizados. Não alterar silenciosamente categorias já associadas a registros antigos.

### Alocação percentual
A alocação é calculada sobre o valor definido como excedente disponível, não automaticamente sobre toda entrada bruta. Exemplo: entrada de R$ 1.000, despesas/compromissos de R$ 500 e excedente de R$ 500; uma categoria configurada em 20% recebe uma sugestão de R$ 100.

- Mostrar a base usada no cálculo.
- Validar percentuais e indicar quando o total ultrapassar 100%.
- Explicar se percentuais são aplicados ao excedente, à entrada ou a outra base escolhida.
- Não mover dinheiro nem criar lançamentos automaticamente sem confirmação explícita.
- Evitar alocação duplicada após recálculo ou reabertura da tela.

## 8. Metas e reservas

Permitir criar metas com nome, valor-alvo, prazo, prioridade, progresso e contribuições vinculadas. Reservas devem ser distinguíveis de saldo livre e não podem ser contadas duas vezes no patrimônio.

- Separar progresso financeiro do progresso de execução.
- Mostrar valor acumulado, valor restante e prazo.
- Tratar retiradas e ajustes com consistência.
- Estados visuais devem respeitar a regra de cores deste documento.

## 9. Projetos e obras

Cada projeto pode conter orçamento, limite de gastos, prazo, descrição, itens, movimentações vinculadas, andamento e notas.

- Acompanhar orçamento previsto, valor gasto e saldo do orçamento.
- Exibir progresso financeiro e progresso físico/operacional separadamente.
- Permitir exportação para PDF e CSV quando implementada.
- Não inferir que o projeto está concluído apenas porque o orçamento foi totalmente gasto.
- Não contabilizar novamente movimentações que já aparecem no livro financeiro.

## 10. Dívidas, empréstimos e pagamentos

Registrar credor, saldo devedor, parcelas, vencimentos, taxas e condições conhecidas. Diferenciar o valor original da dívida, o saldo atual e os pagamentos realizados.

- Cada pagamento deve reduzir o saldo correspondente uma única vez.
- Não duplicar uma parcela como despesa e como pagamento de dívida no consolidado.
- Exibir vencimentos e compromissos com clareza.
- Simulações devem separar premissas fornecidas de estimativas.
- Não presumir taxas, contratos ou condições que não foram informadas.

## 11. Inteligência de investimentos

Área dedicada à análise e comparação de investimentos, incluindo, conforme aplicável:
- CDB e RDB.
- LCI e LCA.
- Tesouro Direto.
- Criptoativos.
- Consórcio.
- Imóveis e leilões.
- Outros investimentos ou ativos configuráveis.

Informações que podem ser necessárias, de acordo com o produto:
- Aporte inicial e aportes recorrentes.
- Prazo e datas.
- Rentabilidade informada (por exemplo, percentual do CDI ou taxa fixa).
- Indexador e periodicidade.
- Impostos, taxas, carência e liquidez.
- IOF quando aplicável ao prazo e produto.
- Valor bruto, descontos estimados e valor líquido.
- Inflação usada na projeção e resultado real estimado.
- Riscos, limitações e premissas.

Não aplicar a mesma fórmula tributária a produtos diferentes. Isenção, tributação, garantia, liquidez e regras regulatórias precisam ser verificadas em fontes oficiais e conforme a legislação vigente antes de serem apresentadas como fato.

### Comparações e indicadores
- Permitir comparação lado a lado sob premissas equivalentes.
- Identificar claramente valores estimados versus valores observados.
- Informar data e fonte para CDI, Selic, IPCA e demais referências.
- Apresentar a metodologia de classificação ou pontuação; não chamar uma nota de garantia de retorno.
- Não prometer rentabilidade nem ocultar risco de perda.
- Diferenciar retorno nominal e retorno real, após inflação.
- Tratar criptoativos e outros ativos voláteis com indicação de risco adequada.

## 12. Simulação $$$

Reunir calculadoras e cenários financeiros, incluindo investimentos, financiamento, consórcio, compra à vista versus parcelada e impacto da inflação.

Para compra à vista versus parcelada, considerar somente dados informados ou fontes verificáveis: preço à vista, total parcelado, datas, taxa de desconto ou retorno alternativo e inflação quando pertinente. Mostrar fórmula, premissas, resultado e limitações. Não declarar uma opção universalmente melhor sem considerar as condições do cenário.

A calculadora de IPCA deve usar dados de fonte oficial, identificar o período e a data de atualização e ter tratamento para falha de rede ou ausência de dados. Não inventar índices nem apresentar um valor antigo como atual.

## 13. Gráficos e análises

Oferecer gráficos compactos e úteis para:
- Entradas e saídas ao longo do tempo.
- Gastos por categoria.
- Evolução do saldo e do patrimônio.
- Orçado versus realizado.
- Progresso de metas e projetos.
- Distribuição de ativos, quando os dados forem suficientes.

Todo gráfico deve indicar período, unidade e base de cálculo. Gráficos e totais precisam reconciliar com as movimentações subjacentes. Não exibir gráfico enganoso quando faltarem dados.

## 14. Obra do Reino

Área específica para organização de compromissos e atividades espirituais, conforme requisitos já discutidos:
- Leituras bíblicas.
- Estudos e reflexões.
- Anotações.
- Práticas e compromissos.
- Agenda e projetos de serviço.
- Categoria financeira associada, quando houver gasto ou contribuição.

O registro espiritual não deve gerar movimentação financeira automaticamente. Qualquer vínculo financeiro deve ser explícito e não duplicar registros existentes.

## 15. Open Finance — integração posterior

A integração foi planejada para uma etapa posterior à estabilização das funções locais. Instituições prioritárias mencionadas: Nubank e PagBank. Provedor considerado: Pluggy.

Arquitetura de segurança pretendida:
**Aplicativo Android → backend protegido → provedor Open Finance → dados autorizados → aplicativo.**

- Nunca incluir Client Secret, tokens privados ou credenciais privilegiadas no APK ou repositório público.
- Segredos devem ficar em backend seguro, com permissões mínimas, rotação e logs sem credenciais.
- Só mostrar conexão estabelecida quando houver confirmação real do provedor e do backend.
- Exibir estado de conexão, autorização, falha, expiração e sincronização de forma honesta.
- Tratar consentimento, revogação, escopo autorizado e proteção dos dados.
- Não usar dados bancários reais em testes automatizados sem autorização e proteção apropriadas.
- A integração só deve ser iniciada após requisitos locais, persistência e testes de regressão estarem estabilizados.

## 16. Calculadora discreta

Identificadores já mencionados:
- `mfCalcFab`
- `mfCalcPanel`

A calculadora deve ser acessível sem ocupar permanentemente a tela, não deve abrir o teclado Android sem necessidade e deve permitir aplicar o resultado a um campo quando solicitado. Validar divisão por zero, entrada inválida, separador decimal brasileiro e precisão monetária. Não substituir um valor existente sem ação explícita do usuário.

## 17. Exportação e relatórios

PDF, CSV e impressão/compartilhamento devem ser testados no Android real ou em ambiente equivalente.

- Informar período e filtros aplicados.
- Usar valores e totais reconciliados com a fonte.
- Escapar conteúdo CSV para evitar corrupção de colunas e fórmulas interpretadas indevidamente por planilhas.
- Tratar caracteres acentuados e nomes longos.
- Exibir mensagens de sucesso ou falha com base no resultado real da operação.
- Não afirmar que o arquivo foi gerado sem verificar a existência ou o resultado da exportação.

## 18. Persistência e migração de dados

A implementação existente usa ou usou armazenamento local via `localStorage`. O formato atual precisa ser inventariado antes de qualquer mudança.

- Registrar todas as chaves, estruturas, versões e dependências encontradas.
- Não limpar o armazenamento para “resolver” problemas.
- Criar migrações versionadas, idempotentes e testadas, com estratégia de recuperação.
- Validar leitura, gravação, atualização e reabertura do aplicativo.
- Não presumir que dados locais estejam sincronizados com nuvem ou protegidos por backup.
- Garantir que atualizações preservem dados existentes.
- Evitar mudanças de nomes de chaves sem camada de compatibilidade.

## 19. Android, repositório e compilação

Arquivos e caminhos previamente mencionados, a confirmar na árvore atual:
- `app/src/main/assets/index.html`
- `code.gs` e `index.html` do projeto antigo em Google Apps Script
- Workflow `gerar-apk.yml`

O alvo atual é um APK Android independente da interface do Google Apps Script, quando essa arquitetura for confirmada no repositório. A compilação deve usar versões de SDK, ferramentas e dependências compatíveis, licenças aceitas de forma documentada e configurações reproduzíveis.

A Build 47 foi citada anteriormente como referência desejada. Antes de tratá-la como versão oficial, verificar se o artefato existe, sua origem, commit, hash, assinatura e compatibilidade. Não presumir que seja a versão mais recente ou aprovada apenas por menção anterior.

Não apagar builds, históricos, branches ou repositórios sem autorização explícita e verificação do alvo. Este plano deve servir como referência independente para evitar perda de requisitos.

## 20. Auditoria técnica e financeira

A auditoria deve atravessar todas as camadas:
1. Requisitos e fluxos.
2. Interface e acessibilidade.
3. Estado, eventos e navegação.
4. Regras de negócio.
5. Cálculos e arredondamento.
6. Persistência, migrações e integridade de dados.
7. Exportação e importação.
8. Integrações e segurança.
9. Android, permissões e ciclo de vida.
10. Workflow, dependências e artefato APK.
11. Testes unitários, integração, interface e instrumentados.

Para cada problema, registrar:
- Identificador e gravidade.
- Sintoma reproduzível.
- Causa-raiz confirmada ou hipótese ainda não confirmada.
- Arquivo, função e fluxo afetados.
- Correção proposta e alteração realizada.
- Teste que falhava antes e passa depois.
- Testes de regressão executados.
- Evidência, commit e status final.

Não marcar uma hipótese como causa-raiz confirmada sem evidência. Se um teste não puder ser executado, registrar o bloqueio e não o classificar como aprovado.

## 21. Plano de testes e critérios de aceite

### Testes mínimos
- Unitários das regras de cálculo e validação.
- Integração entre movimentações, saldos, categorias, metas, projetos e dívidas.
- Persistência após fechar e reabrir o aplicativo.
- Migração de dados antigos sem perda.
- Interface: navegação, formulários, filtros, teclado, rolagem, estados vazios e mensagens de erro.
- Instrumentados em Android/emulador limpo, quando disponíveis.
- Regressão de todas as áreas modificadas e dos fluxos financeiros críticos.
- Exportação PDF/CSV.
- Verificação de dependências, permissões e exposição de segredos.
- Compilação do APK e inspeção do artefato final.

### Casos financeiros de referência
Criar casos explícitos para:
- Transferência entre contas próprias não altera receita/despesa consolidada.
- Uma movimentação aparece uma única vez nos totais.
- Uma alocação de 20% sobre excedente de R$ 500 resulta em R$ 100 sugeridos.
- Patrimônio líquido corresponde a ativos menos passivos, segundo a definição adotada.
- Pagamento de dívida reduz o saldo devedor uma única vez.
- Cálculos de investimentos respeitam produto, prazo, taxas, tributos e arredondamento.
- Resultado real e nominal são diferenciados.
- Dados ausentes ou desatualizados são identificados e não inventados.

### Critérios de aprovação
Uma build só pode ser chamada de aprovada quando:
- A compilação termina com sucesso.
- Os testes obrigatórios aplicáveis foram executados e passaram.
- Os testes de interface/instrumentados exigidos não estão pendentes.
- Não existem falhas críticas ou altas sem decisão documentada.
- O APK final corresponde ao commit validado.
- O artefato foi localizado e verificado.
- Há evidência reproduzível do resultado.

## 22. Passo a passo de consolidação

1. **Congelar e registrar a linha de base:** commit atual, branch, árvore de arquivos, workflow, artefatos e estado real dos testes.
2. **Inventariar o código:** mapear cada página, botão, ID, função, chave local e fluxo existente para os requisitos deste plano.
3. **Construir uma matriz de rastreabilidade:** requisito → arquivo/função → teste → evidência → status.
4. **Reproduzir as falhas existentes:** capturar logs completos, etapa exata, ambiente e passos mínimos para reprodução.
5. **Identificar causas-raiz:** diferenciar erro de código, configuração, dependência, ambiente, teste e workflow.
6. **Corrigir por prioridade e em mudanças pequenas:** começar por falhas bloqueadoras e integridade financeira; não misturar mudanças não relacionadas.
7. **Executar testes direcionados:** demonstrar que cada correção resolve a falha original.
8. **Executar regressão:** validar recursos existentes e requisitos relacionados.
9. **Auditar cálculos e persistência:** usar casos de referência e dados de teste controlados.
10. **Validar interface e Android:** executar testes de UI/instrumentados e emulação limpa quando disponíveis.
11. **Gerar e inspecionar o APK:** relacionar o artefato ao commit, conferir instalação, inicialização e funções principais.
12. **Registrar o resultado:** atualizar matriz, evidências, pendências e decisões.
13. **Consolidar este plano:** alterar a versão do documento somente com motivo, data, escopo e impacto registrados.

Não iniciar a etapa seguinte como se a anterior estivesse aprovada quando existirem bloqueios críticos sem tratamento ou evidência.

## 23. Pendências iniciais a verificar no repositório

Estas são verificações em aberto, não afirmações de falha:
- Inventário atual de páginas, IDs e funções.
- Correspondência entre cada requisito e o código existente.
- Formato e integridade dos dados em `localStorage`.
- Fórmulas e casos de teste de cada simulador.
- Fonte oficial, data de atualização e tratamento offline de CDI/IPCA.
- Funcionamento real de PDF/CSV no Android.
- Estado da arquitetura Android e dependências.
- Estado atual do workflow de compilação.
- Resultado efetivo dos testes unitários, de interface e instrumentados.
- Existência, hash, assinatura e proveniência de cada APK candidato.
- Ausência de segredos no código, histórico público, logs e artefatos.

## 24. Modelo de registro de requisito/falha

Para cada item, usar o seguinte modelo:

- **ID:**
- **Requisito ou falha:**
- **Comportamento esperado:**
- **Comportamento observado:**
- **Arquivo/função/fluxo:**
- **Causa-raiz:** confirmada / hipótese / desconhecida
- **Correção:**
- **Teste de reprodução:**
- **Teste de regressão:**
- **Evidência e commit:**
- **Status:** pendente / em análise / corrigido não validado / validado / bloqueado
- **Risco residual:**

## 25. Regra permanente de conclusão

O objetivo não é apenas produzir uma compilação, mas entregar um aplicativo coerente com os requisitos, que preserve dados, calcule corretamente, mantenha a segurança e tenha evidências verificáveis de funcionamento. Toda afirmação de conclusão deve ser proporcional às verificações realmente executadas.

**Este documento é a linha de partida da consolidação. Ele não substitui a inspeção do código nem declara funcionalidades implementadas.**
