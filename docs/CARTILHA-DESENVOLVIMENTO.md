# Cartilha de Desenvolvimento — Próspera +

> **Objetivo:** construir uma APK Android de finanças por etapas, começando pela interface e pela navegação, depois implementando as funcionalidades locais e somente no final as integrações externas.
>
> **Regra central:** nenhuma etapa é considerada concluída sem critérios de aceite e evidências verificáveis. Uma compilação bem-sucedida, isoladamente, não prova que o aplicativo está funcionando.

## 1. Princípios do projeto

1. **Interface primeiro:** aprovar as telas, componentes, hierarquia visual e navegação antes de implementar toda a lógica financeira.
2. **Desenvolvimento incremental:** entregar uma etapa pequena, testá-la e só então avançar.
3. **Preservar o que funciona:** antes de substituir código, auditar o repositório e identificar recursos, dados e comportamentos existentes.
4. **Uma fonte de verdade:** saldos e relatórios devem derivar de dados consistentes, sem duplicar lançamentos ou contar transferências como receita/despesa.
5. **Offline em primeiro lugar:** as funcionalidades pessoais essenciais devem funcionar sem conexão quando tecnicamente possível, com dados locais persistentes.
6. **Segurança desde o início:** não armazenar Client Secret, chaves privadas ou tokens privilegiados no APK, no código-fonte público ou nos logs.
7. **Provas, não suposições:** registrar comandos executados, resultados dos testes, versões e artefatos produzidos.
8. **Mudanças controladas:** commits pequenos, histórico preservado e nenhuma exclusão de repositório ou dado sem autorização explícita e verificação prévia.

## 2. Fases, entregas e critérios de aceite

### Fase 0 — Auditoria e definição da base

**Atividades**
- Identificar repositório oficial, branch padrão, estrutura de pastas, tecnologias e workflows.
- Inventariar telas, funcionalidades, regras financeiras, testes, dados locais e integrações existentes.
- Registrar falhas atuais com logs e passos reproduzíveis.
- Identificar segredos expostos sem copiar seus valores para relatórios; se houver exposição, planejar revogação/rotação.
- Definir a versão de referência e uma estratégia de recuperação.

**Entrega:** relatório de auditoria e decisão documentada sobre continuar a base existente ou iniciar uma base limpa.

**Aceite:** o repositório oficial e o ponto de partida estão identificados; riscos, falhas e recursos existentes foram documentados. Nenhum código é substituído antes dessa verificação.

### Fase 1 — Especificação visual

**Atividades**
- Definir nome, logotipo, paleta, tipografia, espaçamentos, ícones, cartões, campos e estados dos componentes.
- Descrever o conteúdo e as ações de cada tela.
- Mapear navegação, estados vazios, erros, carregamento, confirmação e acessibilidade.
- Registrar as decisões em `docs/UI_GUIDE.md` e o escopo em `docs/SPECIFICATION.md`.

**Direção visual inicial proposta:** premium escura, preto profundo, dourado fosco e verde esmeralda como destaque. A identidade definitiva deve ser aprovada antes de ser tratada como requisito fechado.

**Navegação inicial proposta**
- Início
- Movimentações
- Novo lançamento (ação central)
- Gráficos
- Mais (ferramentas secundárias)

**Tela Início:** saldo disponível, entradas e saídas do período, patrimônio bruto e líquido, últimas movimentações e indicadores compactos. Evitar excesso de gráficos na tela inicial.

**Tela Mais:** investimentos, pagamentos, projetos, metas, alocação, simulações, categorias, Open Finance e configurações, conforme o escopo aprovado.

**Entrega:** guia visual, mapa de telas e protótipo navegável com dados fictícios.

**Aceite:** todas as telas previstas podem ser percorridas; botões e destinos estão definidos; o responsável pelo produto aprova a interface antes da implementação integral das regras financeiras.

### Fase 2 — Base Android e APK inicial

**Atividades**
- Confirmar a tecnologia apropriada após a auditoria. Para uma aplicação Android nativa, avaliar Kotlin, Jetpack Compose e Room.
- Separar interface, regras de negócio e camada de dados.
- Configurar build reproduzível e workflow do GitHub Actions.
- Gerar uma APK de desenvolvimento, instalá-la e abri-la num aparelho ou emulador.
- Definir identificador do aplicativo, versionamento e assinatura de release com segurança.

**Entrega:** APK-base instalável com navegação inicial.

**Aceite:** build concluído; APK instalada e iniciada; telas principais abrem sem falhas; nenhuma credencial sensível embutida; logs e versão do artefato registrados.

### Fase 3 — Funcionalidades locais, em incrementos

Implementar e testar uma área por vez, sem integrar bancos nesta fase.

Ordem sugerida:
1. Modelos de dados e persistência local.
2. Receitas, despesas e edição/exclusão de lançamentos.
3. Transferências entre contas.
4. Categorias, filtros, busca e histórico.
5. Cálculos de saldo e resumo mensal.
6. Patrimônio bruto/líquido e contas/ativos conforme o escopo.
7. Orçamentos, alocação percentual, metas e projetos.
8. Investimentos e simuladores, com premissas e fórmulas documentadas.
9. Gráficos, relatórios e exportações.
10. Preferências, acessibilidade e estados de erro.

**Regras financeiras obrigatórias**
- Transferência entre contas próprias não é receita nem despesa consolidada.
- Editar ou excluir um lançamento deve recalcular os indicadores corretamente.
- Não duplicar lançamentos ao atualizar a tela, reabrir o app ou repetir uma operação.
- Definir explicitamente o período, moeda, arredondamento e regras de cada cálculo.
- Testar casos de borda: valores zero, negativos quando aplicáveis, datas, lançamentos repetidos e ausência de dados.
- Não apresentar estimativas de investimento como rendimento garantido.

**Entrega:** funcionalidades locais persistentes e testadas por módulo.

**Aceite:** testes unitários relevantes aprovados; dados sobrevivem ao fechamento e à reabertura; saldo e relatórios batem com cenários de referência; fluxos críticos funcionam offline.

### Fase 4 — Auditoria, testes e regressão

Executar testes em camadas:

- **Unitários:** cálculos, validações e regras de negócio.
- **Integração:** repositório, banco local e migrações.
- **Interface:** navegação, formulários, mensagens, acessibilidade e estados.
- **Instrumentados/emulador:** instalação limpa, inicialização e fluxos críticos.
- **Regressão:** repetir testes existentes após cada mudança relevante.
- **Manual:** validar no aparelho Android-alvo e em tamanhos de tela pertinentes.

Manter um plano em `docs/TEST_PLAN.md` com identificador do teste, pré-condições, passos, resultado esperado, resultado obtido e evidência.

**Aceite:** não há falhas bloqueadoras conhecidas; testes obrigatórios passam; falhas não resolvidas são explicitamente registradas e impedem declarar a versão aprovada. Uma execução iniciada, mas não finalizada, não conta como aprovada.

### Fase 5 — Integrações externas (por último)

Somente após a base local estar estável:
- Definir provedor, permissões, consentimento, limites, custos e tratamento de erros.
- Usar backend protegido quando forem necessárias credenciais privilegiadas.
- Manter segredos fora do APK, dos commits e dos logs.
- Tratar expiração, revogação, reconexão, indisponibilidade e sincronização.
- Evitar duplicação de transações importadas; definir identificadores e regras de conciliação.
- Explicar ao usuário quais dados serão acessados e por quê.
- Testar a integração separadamente da lógica local e validar o retorno ao aplicativo após autorização.

**Entrega:** integração documentada e testada, com consentimento e segurança adequados.

**Aceite:** nenhum segredo privilegiado no cliente; consentimento e falhas tratados; sincronização idempotente; testes com cenários de sucesso, cancelamento, expiração e indisponibilidade.

### Fase 6 — Release e manutenção

- Executar toda a suíte de testes de release.
- Gerar APK assinada e identificar versão, commit e workflow.
- Validar instalação/atualização e preservar dados do usuário.
- Arquivar relatórios, checksums e artefatos de cada release.
- Publicar como aprovada somente uma versão que cumpriu os critérios de aceite.

## 3. Organização sugerida do código

A estrutura final deve refletir a tecnologia escolhida após a auditoria. Para uma aplicação nativa, uma referência possível é:

```text
app/
  src/main/
    ... interface e navegação
    ... domínio/regras financeiras
    ... dados, banco local e repositórios
    ... integrações isoladas
  src/test/          testes unitários
  src/androidTest/   testes instrumentados
docs/
  SPECIFICATION.md
  UI_GUIDE.md
  TEST_PLAN.md
.github/
  workflows/         automação de build e testes
```

Esta é uma organização indicativa, não uma ordem para mover ou apagar arquivos existentes sem auditoria.

## 4. Procedimento obrigatório para cada alteração

1. Descrever o problema e como reproduzi-lo.
2. Identificar a causa com evidência; não apenas repetir tentativas.
3. Definir a alteração mínima e os riscos.
4. Fazer um commit pequeno e identificável.
5. Executar os testes diretamente relacionados.
6. Executar a compilação e os testes de regressão pertinentes.
7. Verificar o diff para detectar mudanças não solicitadas.
8. Registrar resultado, logs relevantes e limitações.
9. Só marcar como resolvido quando houver evidência de sucesso.
10. Se falhar, registrar a nova evidência e investigar a causa — não declarar conclusão.

## 5. Critérios de aprovação de uma APK

Uma APK só pode ser marcada como **APROVADA** quando todos os critérios obrigatórios da versão forem satisfeitos:

- [ ] Build de release concluído.
- [ ] Testes unitários obrigatórios aprovados.
- [ ] Testes de integração obrigatórios aprovados.
- [ ] Testes instrumentados de interface concluídos e aprovados.
- [ ] Instalação e inicialização verificadas em ambiente limpo.
- [ ] Navegação e fluxos financeiros críticos verificados.
- [ ] Persistência e migração de dados verificadas.
- [ ] Segurança básica e ausência de segredos no cliente verificadas.
- [ ] Regressões avaliadas.
- [ ] Artefato, versão, commit e evidências registrados.

Se algum teste estiver pendente, interrompido ou sem evidência, o estado é **PENDENTE**, não aprovado. Se algum teste obrigatório falhar, o estado é **REPROVADO** até a correção e repetição do teste.

## 6. Uso do GitHub

- Usar um repositório oficial e branches com nomes claros.
- Preferir mudanças pequenas, commits descritivos e revisão de diff.
- Executar build e testes automaticamente em pull requests.
- Separar artefatos de desenvolvimento e releases aprovadas.
- Não apagar repositórios, branches, histórico ou dados para “limpar” erros sem autorização explícita e plano de preservação.
- Não colocar tokens, senhas, chaves privadas, dados bancários reais ou arquivos de usuários no repositório.
- Proteger a branch principal e restringir releases a resultados verificados.

## 7. Referências técnicas

- Android Developers — arquitetura: https://developer.android.com/topic/architecture
- Android Developers — testes: https://developer.android.com/training/testing
- Material Design 3: https://m3.material.io/
- OWASP Mobile Application Security (MASVS/MASTG): https://mas.owasp.org/

As referências orientam a engenharia; decisões específicas de produto, interface, cálculos e integrações devem ser documentadas e aprovadas neste projeto.

## 8. Estado inicial do plano

- [ ] Confirmar o repositório oficial e auditar sua situação atual.
- [ ] Documentar o inventário de telas e funcionalidades existentes.
- [ ] Aprovar a identidade visual e a navegação.
- [ ] Criar o protótipo navegável.
- [ ] Aprovar a base técnica e gerar a APK inicial.
- [ ] Implementar funcionalidades locais por módulos.
- [ ] Concluir testes e auditorias.
- [ ] Implementar integrações externas.
- [ ] Aprovar e registrar a release final.

**Status inicial:** planejamento documentado. Nenhuma fase deve ser considerada concluída apenas pela existência desta cartilha; cada uma exige execução e evidências próprias.
