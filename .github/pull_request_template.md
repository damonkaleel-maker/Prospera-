## 🚨 ALERTA MÁXIMO — CRITÉRIO OBRIGATÓRIO DE QUALIDADE

Consulte [ALERTA-MAXIMO-QUALIDADE.md](../ALERTA-MAXIMO-QUALIDADE.md) e o Plano Mestre antes de implementar. Não aprove uma alteração só porque compila.

### Escopo e preservação
- [ ] Consultei os requisitos relevantes do Plano Mestre.
- [ ] Revisei dependências e impactos em outros módulos.
- [ ] Preservei dados existentes, navegação, identificadores e funções não relacionadas.
- [ ] Revisei o diff em busca de efeitos colaterais e riscos de segurança.

### Evidências de validação
- [ ] Sintaxe/análise estática verificada (registrar comando e resultado).
- [ ] Cálculos testados com exemplos conhecidos, limites e entradas inválidas.
- [ ] Integrações entre módulos verificadas.
- [ ] Persistência e reabertura dos dados verificadas, quando aplicável.
- [ ] Testes de regressão executados nos módulos relacionados.
- [ ] Compilação/CI verificada, quando aplicável.
- [ ] Teste no Android real executado para fluxos críticos, ou marcado explicitamente como PENDENTE se não disponível.
- [ ] Nenhuma falha crítica ou inconsistência conhecida permanece sem tratamento.

### Registro obrigatório
- **Testes executados e resultados:**
- **Testes pendentes e motivo:**
- **Limitações/riscos conhecidos:**
- **Estado:** BLOQUEADO / PENDENTE / APROVADO

Não marque uma caixa sem evidência. Teste não executado é PENDENTE. Falha crítica bloqueia aprovação.
