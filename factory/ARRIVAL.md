# FD-AGENT-ARRIVAL-V1 — Entrée canonique de tout agent codeur

## 0. Choix d'exécution — priorité à l'agent déjà connecté

**VOIE A — AGENT CONNECTÉ (sans clé API fournisseur additionnelle)** : la phrase « Je suis agent codeur » active le **protocole** de travail pour un agent ChatGPT/Claude déjà connecté et effectivement autorisé à lire/écrire sur ce dépôt. L'agent **est** le moteur de codage : il lit les `.md`, utilise les outils GitHub disponibles, qualifie ou sélectionne les tâches du registre existant, écrit le code autorisé, lance/vérifie les tests disponibles, consulte la CI, laisse les SHA/runs et la prochaine action, puis recommence tant qu'un travail sûr et admissible existe. Il **n'a pas à attendre `ANTHROPIC_API_KEY` ou `ANTHROPIC_MODEL`**. La commande `python -m factory.entry` est facultative si le client ne donne qu'un connecteur GitHub ; ses vérifications sont alors effectuées directement par le connecteur.

**VOIE B — GÉNÉRATEUR HÉBERGÉ (facultatif)** : `.github/workflows/factory-autonomy.yml` peut fonctionner hors conversation. Ses templates déterministes n'utilisent pas de modèle. Pour générer un **nouveau code non couvert par un template**, ce workflow *sans agent connecté* doit disposer d'une véritable capacité de modèle configurée, aujourd'hui `factory/provider.py` et ses paramètres Anthropic. Cela n'est **pas** un prérequis de la voie A.

**Boucle obligatoire d'un agent connecté — `FD_AGENT_AUTO_CONTINUE` :** `OBSERVE GITHUB → RECONCILE STATE/CI → SELECT WORK → VERIFY DEPENDENCIES/OWNERSHIP/WRITE SCOPE → CODE USING NATIVE AGENT → TEST → VERIFY EXACT SHA/CI → RECORD EVIDENCE AND NEXT_ACTION → RECOMPUTE → CONTINUE`. Inspirée du protocole documentaire de la PR #95 du MCP, **sans copier ses autorités**.

- Réutiliser `factory/engine.py`, `tasking.py`, `program_factory.py`, `state.json`, `SUIVI.md` et `HANDOFF.json`. Ne pas créer de file parallèle, de faux claim ou de tâche DONE.
- Avant chaque écriture, réobserver `main` et les tâches/runs concurrents. Si un writer du workflow agit ou si le HEAD change, **STOP_WRITE → REOBSERVE → RECONCILE**. Écrire seulement selon les permissions réellement disponibles et les chemins autorisés.
- Les preuves `CI SUCCESS`, les critères du blueprint et le statut `DONE` sont distincts. Ne pas achever une tâche seulement parce qu'un message affirme que le code est prêt.
- Si aucun travail READY n'existe, continuer la **qualification du programme** et les travaux de code justifiés par de vraies sources ; un besoin de PDF/Drive, permission absente ou action destructive non autorisée est un blocage local, pas un motif pour inventer des faits.
- À la fin de chaque lot, consigner le `NEXT_ACTION`, réévaluer le backlog et enchaîner sans question de permission générique lorsque toutes les autorisations sont déjà satisfaites. La continuation au-delà de la session dépend des workflows hébergés ou du prochain agent reconnecté.



**Déclencheur humain :** « Connecte-toi au dépôt Patricked-code/financialdata en tant qu'agent codeur et poursuis le chantier. »

Cette phrase est une demande de **reprise de travail gouvernée**, pas une autorisation illimitée et pas une nouvelle instance d'orchestration. L'agent connecté doit suivre **les opérations ci-dessous, dans cet ordre**, sans dépendre du contenu d'une conversation précédente.

## 1. Connexion, identité et accès

1. Utiliser le connecteur GitHub disponible ; sélectionner le compte **Patricked-code**, vérifier l'identité avec son action de profil et ouvrir **Patricked-code/financialdata**.
2. Obtenir le SHA courant de `main`. Une autorisation de lecture n'est pas une permission d'écriture. Ne pas prétendre disposer d'un terminal, d'un jeton, de secrets ou de droits qui ne sont pas disponibles.
3. Respecter `GOVERNANCE.md` : **branche unique main, aucune PR/branche, aucun force push**. La procédure d'un autre dépôt ne remplace pas cette autorité.

## 2. Lecture canonique avant toute programmation

**Premier passage obligatoire : ordre canonique de `README.md` et `GOVERNANCE.md`.** Lire les onze documents suivants depuis le HEAD réel de `main`, **dans cet ordre et sans intercaler les fichiers d'exécution `factory/`** :

1. `GOVERNANCE.md`
2. `AGENTS.md`
3. `CLAUDE.md`
4. `SUIVI.md`
5. `DECISIONS.md`
6. `TODO.md`
7. `ARCHITECTURE.md`
8. `DATA_MODEL.md`
9. `SOURCES.md`
10. `docs/BRVM_RAW_DATABASE_GOVERNANCE.md`
11. `docs/ISSUER_DISCOVERY_MATRIX.md`

**Deuxième passage : projection et exécution**, sans reconstruire le modèle : `ROADMAP.md`, `factory/CONTINUITY.md`, `factory/HANDOFF.json`, `factory/state.json`, `factory/blueprints.json`, `factory/PROGRAM_FACTORY.md` et les autres fichiers nécessaires à la tâche. Ensuite observer la CI, sélectionner le travail admissible et appliquer `FD_AGENT_AUTO_CONTINUE`.

**Hiérarchie :** la gouvernance et la provenance des sources prévalent. Pour l'état d'exécution, les preuves GitHub vivantes et `factory/state.json` prévalent sur un résumé historique ou sur le présent document.

## 3. Handshake d'arrivée, sans mutation

Si un clone/runner Python 3.11 autorisé est disponible :

    python -m factory.entry --agent chatgpt-session --role coder

Le résultat JSON `FD-AGENT-ARRIVAL-V1` indique le programme, les tâches disponibles, les tâches à qualifier, les erreurs d'audit, le run en attente et la décision de reprise. **Cette commande n'écrit rien et ne simule pas une prise en charge distante.**

Si l'agent n'a que le connecteur GitHub (sans terminal), reproduire ses vérifications en lisant `factory/state.json`, `factory/blueprints.json`, les manifests, le dernier SHA `main` et les runs de GitHub Actions ; signaler explicitement que l'exécution de la commande n'a pas eu lieu. Ne jamais inventer une admission exécutée.

## 4. Interpréter strictement la décision

| Décision | Action autorisée |
|---|---|
| `BLOCKED_BY_AUDIT` | Diagnostiquer les erreurs réelles et préparer une correction non destructive |
| `CI_ATTESTATION_REQUIRED` | Vérifier le run exact et faire réconcilier l'état avant une autre tâche |
| `APPROVED_WORK_AVAILABLE` | **Agent connecté :** coder avec ses capacités natives et les outils GitHub autorisés ; **workflow hébergé :** utiliser `factory-autonomy.yml`. Dans les deux cas, respecter PLAN → CODE → VALIDATE → PUBLISH → ATTEST et les preuves exigées. |
| `PROGRAM_QUALIFICATION_REQUIRED` | Reprendre les travaux `BACKLOG` du programme prioritaire ; vérifier les sources ; constituer et tester un **blueprint versionné, admissible et borné**, en réutilisant `factory/tasking.py` |
| `NO_ADMISSIBLE_WORK` | Rechercher le prochain besoin justifié dans `ROADMAP.md`/`TODO.md` ; ne pas fabriquer une réussite |
| `BLOCKED` | Préserver les preuves et demander uniquement la permission réellement manquante |

Un simple statut historique `BACKLOG` n'accorde pas automatiquement une permission `READY`. Les tâches nécessitant des PDF/Drive externes ne sont pas terminées sans examen des octets ou des données de source attendues.

## 5. Cycle commun, unique, sans régression

`Mandat → Programme → Tâche candidate → Blueprint admissible → UTL PLAN/CODE/VALIDATE/PUBLISH/ATTEST → Tests → Preuves GitHub → Attestation → Prochaine tâche`.

Aucune seconde queue ou gouvernance ne doit être créée. La seule projection d'état du programme est `factory/state.json`. Les fichiers `factory/tasking.py`, `factory/coder.py`, `factory/publisher.py` sont des adaptateurs du même moteur `factory/engine.py`.

Avant une écriture sur `main`, vérifier l'absence de conflit avec le writer GitHub Actions, le SHA courant, les chemins autorisés et la sauvegarde de l'historique. Utiliser le workflow hébergé pour la publication automatique. La modification du code généré, les tests et le commit doivent être attestés, non simplement annoncés.

Après chaque étape, enrichir le journal et la mémoire `SUIVI.md` / `DECISIONS.md` / `TODO.md` selon leur rôle. En cas d'échec, consigner `BLOCKED` avec les preuves ; ne pas prétendre à l'absence absolue de toute régression.

## 6. Réponse attendue de l'agent à son arrivée

Rapporter de façon vérifiable : compte et dépôt connectés ; SHA réel de `main` ; Continuity ID ; révision du registre ; dernière attestation ; programme actif ; éventuel blocage ; tâche admissible ou prochaine tâche à qualifier ; actions effectivement exécutées ; prochaine action. Continuer le travail autorisé si des outils sont disponibles, sans attendre une nouvelle explication du propriétaire.

**Limite :** cette instruction n'est pas un déclencheur magique dans toutes les applications. Un agent doit disposer d'un accès GitHub effectif et lire le dépôt. L'exécution 24/7 appartient au workflow GitHub hébergé, non à la conversation elle-même.

## Arrivée après D040 — analyse programmatique automatique

Lorsqu'une nouvelle conversation arrive et constate `PROGRAM_QUALIFICATION_REQUIRED`, consulter `factory/PROGRAM_FACTORY.md` et `python -m factory.program_factory` (ou son équivalent par le connecteur GitHub). La sélection du programme et la création des blueprints autorisés sont désormais raccordées à la phase `reconcile` du workflow existant. Les nouvelles tâches éligibles doivent conserver `source_task_id`, dépendances, preuves SHA et statut READY. Ne pas réexécuter les tâches historique DONE ni lancer une opération nécessitant des fichiers externes absents.
