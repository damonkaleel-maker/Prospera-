# 🚨 ALERTA MÁXIMO — CRITÉRIO OBRIGATÓRIO DE QUALIDADE

Esta regra é obrigatória para toda implementação, correção, refatoração, integração, atualização, compilação ou publicação do Próspera +.

**Não considerar uma tarefa concluída apenas porque o código foi escrito, o arquivo foi alterado ou a compilação terminou.** Cada afirmação de conclusão precisa corresponder a uma verificação realmente executada e registrada.

Antes de alterar:
1. Consultar o Plano Mestre Oficial e os documentos relevantes.
2. Entender o comportamento existente, os dados persistidos, os identificadores e as dependências entre módulos.
3. Definir critérios de aceite e testes específicos para a mudança.
4. Preservar funcionalidades, interface, IDs, dados e compatibilidade, salvo autorização explícita para mudar.

Depois de alterar:
1. Revisar o diff e procurar efeitos colaterais.
2. Executar verificações de sintaxe, análise estática e/ou testes automatizados adequados.
3. Testar cálculos com exemplos de referência, limites, entradas inválidas e casos extremos.
4. Verificar integrações de ponta a ponta: origem do dado → transformação → cálculo → tela → histórico → exportação, conforme aplicável.
5. Testar persistência: salvar, editar, reabrir, excluir quando permitido e migrar dados sem perda ou duplicação.
6. Executar testes de regressão nos módulos relacionados.
7. Compilar o APK e examinar o resultado da automação.
8. Testar no Android real os fluxos críticos sempre que o aparelho estiver disponível. Se não estiver, registrar explicitamente como pendente; nunca alegar teste real.
9. Registrar evidências, resultado, limitações conhecidas e próximos passos.

## Portão de liberação
- **BLOQUEADO:** há falha, inconsistência crítica, dado incorreto, regressão ou requisito obrigatório não atendido.
- **PENDENTE:** falta executar uma verificação necessária ou não há evidência suficiente.
- **APROVADO:** todos os critérios aplicáveis passaram e há evidência verificável.
- A compilação bem-sucedida, isoladamente, não aprova a funcionalidade.
- Uma consulta implementada não prova que a resposta está correta nem que chegou corretamente à interface.
- Nunca afirmar que algo foi testado, corrigido, compilado ou publicado sem confirmação real.

## Regras de integridade financeira
- Conferir que transferências não sejam contabilizadas como receita ou despesa indevida.
- Evitar lançamentos duplicados e divergência entre saldo, movimentações, gráficos e relatórios.
- Validar valores, datas, taxas, unidades, períodos, arredondamentos e cenários extremos.
- Não marcar pagamento como concluído sem satisfazer as regras financeiras aplicáveis.
- Não apresentar dados antigos/cacheados como atualização confirmada.
- Diferenciar claramente taxa mensal, acumulado em 12 meses e hipótese de inflação futura.
- Garantir que telas, histórico e exportações usem os mesmos dados e definições.

## Segurança e preservação
- Nunca colocar segredos, tokens privados ou credenciais no APK, HTML público, logs ou repositório.
- Não apagar nem redefinir localStorage ou outros dados persistidos como solução rápida.
- Não remover funções nem alterar navegação/identificadores existentes sem necessidade e autorização.
- Preferir mudanças pequenas, revisáveis e reversíveis.
- Não misturar uma correção localizada com uma reformulação ampla não solicitada.

## Registro obrigatório por tarefa
Documentar: objetivo; arquivos/módulos afetados; requisitos consultados; testes executados; resultados observados; testes não executados; riscos/limitações; estado final (BLOQUEADO, PENDENTE ou APROVADO); e link do commit/execução quando disponível.

**Regra final:** se uma verificação não foi executada, marcar como PENDENTE. Se houver falha, bloquear a aprovação, corrigir e repetir os testes afetados. Este alerta tem prioridade sobre a pressa de entregar.
