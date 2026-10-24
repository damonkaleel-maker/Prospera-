# Plano Mestre — Compra Simples, Compra Avançada e IPCA
**Projeto:** Próspera +  
**Data:** 24/10/2026  
**Status:** especificação funcional registrada para implementação e validação.

## 1. Objetivo
A área de compra deve ajudar a pessoa a decidir, no momento da compra, entre pagar à vista, parcelar ou esperar. A explicação deve ser clara e popular, com detalhes disponíveis sem deixar a tela principal carregada.

## 2. Compra Simples — dados de entrada
- Nome/descrição do produto (opcional).
- Preço à vista.
- Valor de cada parcela e quantidade de parcelas.
- Desconto à vista, entrada, juros e taxas/custos extras, quando conhecidos.
- Rendimento líquido mensal estimado do dinheiro, como hipótese editável e claramente identificada.
- Prazo para esperar antes de comprar, quando a alternativa esperar for analisada.
- Renda mensal disponível e reserva financeira, opcionais; sem esses dados, avisar que a avaliação do orçamento é parcial.

## 3. Resultados obrigatórios
- Total à vista e total parcelado, incluindo entrada e custos informados.
- Diferença em reais entre alternativas.
- Valor presente estimado das parcelas, com a taxa de desconto informada.
- Poder de compra atual e estimativa de poder de compra no prazo escolhido.
- Valor futuro necessário para preservar o poder de compra atual.
- Comparação de três alternativas: comprar à vista, comprar parcelado e esperar.
- Resumo, recomendação explicada e três pontuações independentes de 0 a 100.

## 4. Índice de Vantagem da Compra (0–100)
Cada alternativa recebe uma nota própria. A nota deve resultar de regras documentadas e consistentes, considerando custo total/valor presente, taxas, impacto no orçamento e preservação da reserva quando esses dados forem fornecidos. Não tratar dados desconhecidos como se fossem conhecidos; exibir aviso quando a análise estiver incompleta.

| Nota | Cor | Mensagem popular |
|---|---|---|
| 0–19 | Vermelho escuro | NÃO FAÇA ESSE NEGÓCIO! Use apenas se os dados sustentarem alerta muito grave. |
| 20–39 | Vermelho | CUIDADO! Essa compra pode sair cara. |
| 40–59 | Laranja | CALMA! Vale pensar melhor. |
| 60–74 | Amarelo | PODE VALER A PENA. Confira as condições. |
| 75–89 | Azul | BOA ESCOLHA! As condições parecem favoráveis. |
| 90–100 | Verde | ÓTIMO NEGÓCIO! As condições parecem muito vantajosas. |

Exibir número, cor, mensagem e explicação — nunca depender somente da cor. A nota não é garantia de resultado. Confirmar compatibilidade com a regra global de cores do aplicativo antes de integrar, pois em outras áreas o verde pode estar reservado ao status concluído.

## 5. Poder de compra e valor do dinheiro
Separar claramente três conceitos:
- **Valor nominal:** quantidade de reais.
- **Poder de compra:** bens e serviços que o dinheiro consegue comprar, aproximados pela inflação medida ou assumida.
- **Valor presente:** equivalência hoje de pagamentos futuros, de acordo com uma taxa de desconto explicitada.

Para corrigir historicamente valores, utilizar os números-índice oficiais do IPCA e a metodologia do IBGE. Para períodos futuros, usar uma hipótese de inflação identificada como estimativa, não como fato.

Fórmulas de referência:
- Valor futuro para preservar o poder de compra = valor atual × (1 + inflação anual)^(meses/12).
- Poder de compra em reais de hoje = valor futuro / (1 + inflação anual)^(meses/12).
- Valor presente de um pagamento futuro = pagamento / (1 + taxa mensal)^n; somar os valores presentes das parcelas.
- Para taxas mensais variáveis, compor as taxas multiplicativamente, sem somar percentuais como se fossem equivalentes.

Exemplo didático, não previsão: R$ 1.000 hoje e inflação hipotética de 5% em 12 meses. Seriam necessários R$ 1.050 no futuro para manter o poder de compra. R$ 1.000 recebidos daqui a 12 meses equivaleriam a cerca de R$ 952,38 em poder de compra atual.

## 6. IPCA — fonte e estratégia de consulta
Fonte principal: IBGE/SIDRA. Usar a API estruturada para que a consulta ocorra dentro do aplicativo, sem exigir que a pessoa abra um navegador.

Referências oficiais:
- Página do IPCA: https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-ipca.html
- Tabela 1737 do SIDRA: https://sidra.ibge.gov.br/tabela/1737
- Documentação da API de agregados do IBGE: https://servicodados.ibge.gov.br/api/docs/agregados?versao=3
- Calculadora oficial do IBGE: https://www.ibge.gov.br/explica/inflacao.php?ind=sinapi

Implementação e validação:
1. Consultar dados estruturados oficiais do IBGE/SIDRA; confirmar tabela, variável, território, unidade, formato e endpoint antes de utilizar os dados nos cálculos.
2. Solicitar apenas os períodos/dados necessários; evitar baixar toda a série em cada atualização.
3. Definir timeout e tratar falha HTTP, falta de internet, resposta vazia ou JSON inesperado.
4. Validar o valor e o mês de referência antes de substituir o último dado salvo.
5. Mostrar mês/ano de referência do IPCA e data/hora da consulta separadamente.
6. Só informar sucesso quando a resposta tiver sido validada.
7. Em caso de falha, preservar o último dado válido e informar: “Não foi possível atualizar. Exibindo dado salvo de [mês/ano]”.
8. Armazenar o último resultado válido para uso offline, identificando-o como dado salvo, não atualização em tempo real.
9. Oferecer link “Ver fonte oficial” como alternativa de conferência, sem depender do navegador para atualizar o cálculo no aplicativo.

## 7. Botão Atualizar IPCA
- Visual amarelo e compacto, com ícone de atualização e texto curto “Atualizar IPCA”.
- Posicionado junto ao indicador IPCA, sem competir com a ação principal.
- Durante a consulta, indicar carregamento no próprio botão e impedir cliques repetidos.
- Exibir resultado ou erro em mensagem curta, sem recarregar toda a tela.
- Manter área de toque acessível no Android, mesmo com aparência compacta.
- Não apagar dados locais nem a última consulta válida quando a atualização falhar.

## 8. Organização da interface
- Compra Simples: compacta, com campos essenciais, três notas, recomendação e explicação resumida.
- “Mais informações”: seção expansível para custos detalhados, hipótese de inflação, rendimento e fórmulas.
- Compra Avançada: manter análises aprofundadas e parâmetros adicionais.
- Preservar navegação, IDs, recursos existentes e dados locais; não recriar o aplicativo do zero.
- Não contar transferências internas como renda ou despesa se a regra financeira atual as exclui.

## 9. Testes de aceitação
- Botão IPCA amarelo, compacto, acessível e sem quebrar o layout.
- Consulta válida atualiza o valor e o mês de referência corretamente.
- Falha de rede, timeout, resposta vazia ou inválida preserva o último dado válido.
- Não mostrar sucesso quando a consulta falhar.
- Distinguir inflação histórica oficial de estimativa futura.
- Total parcelado inclui entrada, juros e custos informados sem duplicação.
- Testar valores zero, campos opcionais vazios, prazos variados, arredondamentos e valores extremos.
- Mostrar as três notas com as faixas corretas e uma justificativa compreensível.
- Não emitir recomendação categórica se faltarem dados relevantes.
- Testar no Android, inclusive modo offline, e confirmar que os dados existentes permanecem intactos.

## 10. Limitações e transparência
O IPCA mede a inflação observada de uma cesta de consumo; não prevê exatamente a inflação futura de cada produto ou pessoa. A nota é uma estimativa orientativa, não aconselhamento financeiro personalizado nem garantia de que a compra será boa.

## 11. Próxima etapa técnica
Implementar esta especificação no código existente, inspecionando primeiro o arquivo e a função atuais de consulta IPCA. Depois executar testes da requisição real, validar a data de referência, revisar a interface e gerar uma nova compilação. O registro desta especificação, por si só, não significa que o código já foi alterado ou que a integração está corrigida.