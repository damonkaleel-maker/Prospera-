# Cartilha do usuário — Como avaliar uma compra no Próspera +
**Versão:** 1.0 — 24/10/2026

## Para que serve?
Use a análise para comparar pagar à vista, parcelar ou esperar. O aplicativo calcula os custos informados e explica as vantagens e os riscos estimados. O resultado depende da qualidade dos dados preenchidos.

## Passo 1 — Informe o produto e o preço
Preencha o nome do produto se quiser, o preço à vista e os dados de parcelamento. Confira se o valor da parcela corresponde à oferta real. Inclua entrada, juros, frete, tarifas e outros custos conhecidos para evitar comparar preços incompletos.

## Passo 2 — Compare o custo total
Preço da parcela × quantidade de parcelas é apenas o começo. Some a entrada e as taxas adicionais. Compare esse total ao preço final à vista, já descontados os descontos aplicáveis.

Exemplo: preço à vista R$ 1.000; 10 parcelas de R$ 110; sem entrada ou taxas extras. Total parcelado = R$ 1.100. A diferença nominal é R$ 100 a mais no parcelamento. Isso ainda não considera o rendimento que o dinheiro poderia gerar, nem o efeito no orçamento.

## Passo 3 — Entenda o valor do dinheiro no tempo
R$ 1.000 hoje e R$ 1.000 daqui a um ano têm o mesmo valor nominal, mas podem ter poder de compra diferente. Se a inflação hipotética for 5% em um ano, seriam necessários R$ 1.050 no futuro para comprar uma cesta equivalente à de R$ 1.000 hoje. É um exemplo matemático, não uma previsão.

## Passo 4 — O que o IPCA informa?
O IPCA é o índice oficial de inflação calculado pelo IBGE. Ele mede a variação de preços de uma cesta de consumo. O índice histórico ajuda a corrigir valores passados e entender a inflação observada; não prevê exatamente o preço futuro de um produto nem a inflação pessoal de cada família.

Fonte principal: https://sidra.ibge.gov.br/tabela/1737
Documentação da API: https://servicodados.ibge.gov.br/api/docs/agregados?versao=3
Página do IPCA: https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-ipca.html

## Passo 5 — Atualize o IPCA
Toque no botão amarelo e compacto “Atualizar IPCA”. O aplicativo deve buscar os dados diretamente da API oficial, validar a resposta e mostrar o mês de referência. A data de consulta e o mês de referência são informações diferentes.

Se estiver sem internet ou a fonte não responder, o app deve manter o último dado válido e informar que está usando dados salvos. Não interprete isso como atualização recém-concluída.

## Passo 6 — Compare à vista, parcelado e esperar
- **À vista:** considere o desconto, o custo total e quanto dinheiro sobrará para emergências.
- **Parcelado:** considere o custo total, juros, taxas, valor mensal e o custo de oportunidade do dinheiro mantido disponível.
- **Esperar:** estime o prazo e a inflação futura com uma hipótese explícita; lembre-se de que preço, disponibilidade e necessidade podem mudar.

Não existe uma opção sempre melhor. Pagar à vista pode reduzir o custo, mas ser inadequado se consumir toda a reserva. Parcelar pode preservar liquidez, mas sair mais caro. Esperar pode permitir acumular dinheiro, mas o preço futuro é incerto.

## Passo 7 — Entenda as notas de 0 a 100
Cada alternativa recebe sua própria nota. A nota resume os critérios configurados; não é probabilidade de sucesso nem garantia de economia.

| Pontuação | Cor | Mensagem |
|---|---|---|
| 0–19 | Vermelho escuro | NÃO FAÇA ESSE NEGÓCIO! Apenas quando houver evidência suficiente de condição muito desfavorável. |
| 20–39 | Vermelho | CUIDADO! Essa compra pode sair cara. |
| 40–59 | Laranja | CALMA! Vale pensar melhor. |
| 60–74 | Amarelo | PODE VALER A PENA. Confira as condições. |
| 75–89 | Azul | BOA ESCOLHA! As condições parecem favoráveis. |
| 90–100 | Verde | ÓTIMO NEGÓCIO! As condições parecem muito vantajosas. |

O sistema deve explicar os motivos da nota. Se não houver renda, despesas ou reserva informadas, deve avisar que a avaliação do orçamento é incompleta. As cores precisam respeitar as regras visuais globais do app e não devem ser a única forma de comunicar o resultado.

## Passo 8 — Leia a recomendação
A recomendação deve dizer qual alternativa parece financeiramente mais vantajosa e por quê. Exemplos de motivos: desconto à vista significativo; parcelamento com custo total elevado; parcela que compromete muito da renda informada; ou pagamento à vista que deixa a reserva insuficiente.

Evitar afirmações absolutas quando os dados forem incompletos. “Melhor opção pelos dados informados” é mais honesto do que prometer que uma compra é sempre boa.

## Glossário rápido
- **Preço nominal:** quantidade de reais anunciada ou paga.
- **Custo total:** soma de entrada, parcelas, juros e taxas conhecidas.
- **Poder de compra:** quantidade aproximada de bens e serviços que o dinheiro pode comprar.
- **Inflação histórica:** variação de preços observada em período passado.
- **Inflação estimada:** hipótese usada para simular o futuro; pode não se confirmar.
- **Valor presente:** estimativa do equivalente hoje de um pagamento futuro usando uma taxa de desconto.
- **Reserva financeira:** dinheiro disponível para imprevistos e necessidades importantes.

## Aviso
Esta cartilha é educativa. A simulação depende dos dados informados, das hipóteses escolhidas e da disponibilidade das fontes. Ela não garante preços futuros nem substitui uma avaliação pessoal do orçamento.