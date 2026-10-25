# Repository-wide instructions — Próspera +

🚨 **ALERTA MÁXIMO: obrigatório em toda alteração.**

Before implementing any feature, fix, refactor, integration, dependency update, build, or release:
1. Read `ALERTA-MAXIMO-QUALIDADE.md` at repository root.
2. Consult the relevant sections of `docs/PLANO-MESTRE-OFICIAL-PROSPERA-MAIS.md`.
3. Inspect existing behavior and dependencies before editing; preserve persisted data, existing features, navigation and identifiers unless explicitly authorized.
4. Define acceptance checks, then test the changed behavior and its interactions with related modules.
5. Review the diff, run relevant static/syntax checks, automated tests, regression checks, and build checks.
6. For critical flows, test on a real Android device when available. If unavailable, mark this explicitly as PENDING.
7. Report actual evidence, failures, and unexecuted checks. Never claim a check passed if it was not run.

A successful build alone does not prove functional correctness. An implemented API call does not prove that the returned data is correct or consistently used in the UI, history, calculations, and exports. Missing checks are PENDING; critical failures block approval until corrected and retested.

Follow the detailed status definitions and required evidence in `ALERTA-MAXIMO-QUALIDADE.md`.
