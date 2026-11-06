# FD-AUTONOMY-V1 — mandat, registre et point de reprise canonique

Date de construction : 2026-11-06. Dépôt : Patricked-code/financialdata, branche unique main.

## Mandat immuable

Construire un dispositif autonome de programmes, tâches, unités de travail, codage, validation CI et reprise. Continuer ROADMAP.md, TODO.md, SUIVI.md, DECISIONS.md, GOV...; préserver les documents PDF, les manifestes, la provenance RAW, les versions et les décisions. Aucun Codex, aucune dépendance MCP, aucun système concurrent. La politique main-only demeure obligatoire.

## Autorités et chaîne de continuité

- Gouvernance de premier rang : GOVERNANCE.md, AGENTS.md, CLAUDE.md.
- Mandat métier et programme : README.md, ROADMAP.md, DATA_MODEL.md, ARCHITECTURE.md.
- Travaux existants : TODO.md, SUIVI.md, DECISIONS.md.
- Projection opérationnelle unique : factory/state.json (projet, programmes, tâches, UTL, agents, events).
- Tâches autonomes gouvernées : factory/blueprints.json (version, dépendances, limites d'écriture et critères).
- Moteur unique : factory/engine.py ; extension additive tasking.py ; adaptateurs coder.py et publisher.py.
- Preuves : factory/evidence/, journal événementiel SHA-chaîné dans state.json, GitHub Actions run ID et commit SHA.
- Exécution hébergée : .github/workflows/factory-autonomy.yml, périodique ou manuelle.
- Validation indépendante : .github/workflows/factory-validation.yml.

## Circuit canonique

ADMISSION → IMPORT ROADMAP/TODO → FABRIQUE TASK BLUEPRINT → UTL PLAN/CODE/VALIDATE/PUBLISH/ATTEST → ADMISSIBILITÉ (READY, dépendances DONE, chemins autorisés) → GÉNÉRATION MODÈLE SANS ÉCRITURE → VALIDATION ISOLÉE SANS SECRET → PUBLISH SUR main AVEC SHA ATTENDU → PUBLISHED_PENDING_CI → ATTESTATION DU RUN SUCCÈS/ÉCHEC → DONE/BLOCKED → TÂCHE SUIVANTE.

Les travaux historiques TODO ne sont jamais rendus auto-exécutables implicitement : une carte versionnée explicite est requise. Cela évite d'inventer des données à partir de libellés insuffisants.

## Coordonnées de reprise

Continuity ID : FD-AUTONOMY-V1.
Première base de développement : commit 22deeae0e55d7d5a4c60515d107968444f1b9380.
Premiers travaux gouvernés :
1. FD-AUTO-P1-MANIFEST-CHECKER : validation non destructive des CSV P1.
2. FD-AUTO-P1-HASH-CHECKER : contrôle non destructif des SHA-256 (dépend du précédent).

Pour reprendre : lire cette page et SUIVI.md, vérifier main et state.json, consulter le dernier workflow run et ses artefacts. Si PUBLISHED_PENDING_CI, réconcilier le run GitHub avant tout nouveau travail. Ne jamais marquer DONE à partir d'un simple commit ou d'un test non attesté. En cas d'échec, conserver BLOCKED et les preuves, sans effacer de données.

## Droits et séparation des rôles

- Validate / generated tests : contents:read, sans clé de modèle.
- Generate : contents:read + ANTHROPIC_API_KEY temporaire, sans écriture Git.
- Reconcile : contents:write et actions:read ; uniquement state.json.
- Publish : contents:write et actions:write ; exclusivement chemins Python bornés et preuves.
- Writer global : groupe GitHub Actions de concurrence unique. Git push normal (jamais --force), SHA de base vérifié. Aucun droit admin / secret manager / écriture aux données SOURCE.

## Activation externe indispensable

Le workflow est installé mais ne doit pas être déclaré agent IA actif avant : GitHub Settings > Secrets and variables > Actions.
- Secret : ANTHROPIC_API_KEY, détenue par le propriétaire du compte fournisseur, jamais commitée.
- Variable : ANTHROPIC_MODEL, identifiant d'un modèle Claude encore disponible auprès du fournisseur.
- Variable : FD_AUTONOMY_ENABLED = true, activation explicite après validation et acceptation de la consommation API.
Le scheduler fonctionne toutes les quinze minutes et une continuation est demandée explicitement après publication. GitHub peut retarder les runs de schedule. Les permissions réelles du token doivent permettre à l'agent de pousser sur main selon les règles du dépôt.

Les modèles GitHub Models ne sont pas une solution de repli (service retiré en juillet 2026) ; ni Codex ni Copilot ne sont utilisés.

## Definition of Done à vérifier

Tests unitaires verts, audits P1 verts, génération réelle validée, publication effective sur main, conclusion du run GitHub SUCCESS, état DONE avec preuve, second travail sélectionné automatiquement ; absence de mutation SOURCE comparée à la baseline. Tant qu'une des étapes manque, le statut global est PARTIAL / NOT_RUNTIME_ATTESTED.
