# FD-AGENT-ARRIVAL-V1 — Entrée canonique de tout agent codeur

**Déclencheur humain :** « Connecte-toi au dépôt Patricked-code/financialdata en tant qu'agent codeur et poursuis le chantier. »

Cette phrase est une demande de **reprise de travail gouvernée**, pas une autorisation illimitée et pas une nouvelle instance d'orchestration. L'agent connecté doit suivre **les opérations ci-dessous, dans cet ordre**, sans dépendre du contenu d'une conversation précédente.

## 1. Connexion, identité et accès

1. Utiliser le connecteur GitHub disponible ; sélectionner le compte **Patricked-code**, vérifier l'identité avec son action de profil et ouvrir **Patricked-code/financialdata**.
2. Obtenir le SHA courant de `main`. Une autorisation de lecture n'est pas une permission d'écriture. Ne pas prétendre disposer d'un terminal, d'un jeton, de secrets ou de droits qui ne sont pas disponibles.
3. Respecter `GOVERNANCE.md` : **branche unique main, aucune PR/branche, aucun force push**. La procédure d'un autre dépôt ne remplace pas cette autorité.

## 2. Lecture canonique avant toute programmation

Lire les contenus réels, à `main`, de : `GOVERNANCE.md`, `AGENTS.md`, `CLAUDE.md`, `factory/CONTINUITY.md`, `factory/HANDOFF.json`, `factory/state.json`, `factory/blueprints.json`, `SUIVI.md`, `DECISIONS.md`, `TODO.md`, `ROADMAP.md`, `ARCHITECTURE.md`, `DATA_MODEL.md`, `SOURCES.md`, puis les fichiers spécifiques aux travaux.

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
| `APPROVED_WORK_AVAILABLE` | Utiliser **le workflow existant** `factory-autonomy.yml` et sa chaîne PLAN → CODE → VALIDATE → PUBLISH → ATTEST |
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
