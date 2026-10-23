# Checkpoint de continuidade — Próspera +

**Atualizado em:** 23/10/2026 (horário de Brasília)  
**Repositório:** https://github.com/damonkaleel-maker/Prospera-  
**Branch:** `main`

## Estado confirmado
- O projeto é um aplicativo Android, com interface em WebView carregando `app/src/main/assets/index.html`.
- O workflow de APK é `.github/workflows/android-apk.yml`.
- A configuração do SDK foi corrigida para instalar `platforms;android-35 build-tools;35.0.0`.
- Execuções anteriores `39902409966` e `39902571720` terminaram com sucesso e geraram APK.
- O workflow foi atualizado no commit `dbe2679490947b58255779da231c64597ba142e4` para, após uma build bem-sucedida e verificação do APK, apagar todas as execuções anteriores desse workflow, sejam sucesso ou falha, preservando a execução atual.
- A regra nova ainda precisa ser validada por uma execução concluída; não afirmar que o histórico antigo já foi apagado até conferir o resultado.

## Execução de validação em andamento
- Run ID: `39902760521`
- Link: https://github.com/damonkaleel-maker/Prospera-/actions/runs/39902760521
- Objetivo: confirmar que a build termina com sucesso e que a limpeza remove todas as execuções anteriores, mantendo a atual.

## Próximas ações — retomar nesta ordem
1. Consultar o estado e os jobs da execução `39902760521`.
2. Se falhar, inspecionar logs e corrigir a causa real antes de tentar novamente.
3. Se a build passar, conferir se o APK `prospera-mais-debug-apk` foi publicado e se a etapa de limpeza terminou com sucesso.
4. Consultar as execuções restantes e confirmar que só ficou a execução atual do workflow `android-apk.yml`. Se houver execuções anteriores, investigar por que não foram removidas; não declarar sucesso sem essa verificação.
5. Entregar o link de download do APK mais recente.
6. Deixar explícito que build bem-sucedida não comprova teste funcional em um Samsung Galaxy A35; ainda é necessário instalar e testar o app no aparelho.
7. Não repetir compilações sem motivo. Depois da validação da limpeza, voltar ao objetivo principal do projeto: validar o APK e depois continuar a auditoria/implementação funcional e visual, sem tratar integração Open Finance como prioridade agora.

## Requisitos importantes do projeto
- Nome: **Próspera +**; alvo: APK Android para Samsung Galaxy A35.
- Preservar dados locais e funcionalidades existentes; não remover recursos nem alterar visual/fluxos sem justificativa.
- Visual premium escuro, com preto profundo, dourado fosco, cinza e verde esmeralda de destaque.
- Navegação inferior: Início, Movimentações, botão central Novo lançamento, Análises e Aplicações.
- Open Finance fica para uma etapa posterior; nunca incluir segredos ou tokens no APK/repositório público.
- Ser preciso sobre o que foi realmente testado e não prometer que funções estão operacionais sem evidência.

## Como retomar
Ao voltar, começar por este checkpoint e pela execução `39902760521`. Atualizar este arquivo com o resultado confirmado antes de iniciar uma nova etapa.
