# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

- [x] Initialiser `README.md`.
- [x] Fixer la règle Git `main` uniquement.
- [x] Créer `GOVERNANCE.md`.
- [x] Créer `AGENTS.md`.
- [x] Créer `CLAUDE.md`.
- [x] Créer `SUIVI.md`.
- [x] Créer `DECISIONS.md`.
- [x] Créer `TODO.md`.
- [x] Créer `ARCHITECTURE.md`.
- [x] Créer `DATA_MODEL.md`.
- [x] Créer `SOURCES.md`.
- [x] Créer la gouvernance BRVM détaillée sous `docs/`.
- [x] Créer la matrice de découverte des 48 sociétés sous `docs/`.
- [x] Vérifier la présence du kit documentaire sur `main`.
- [x] Vérifier qu'aucune branche de travail n'a été créée pendant l'initialisation.

**Statut P0 : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS**

### Socle P1

- [x] Créer `inventory/README.md`.
- [x] Créer `inventory/P1_ROOT_MANIFEST.md`.
- [x] Vérifier les 48 dossiers société à la racine.
- [x] Identifier et documenter `telecharger_rapports_brvm.py`.
- [x] Définir la méthode d'inventaire direct depuis Drive.

### Émetteurs inventoriés au niveau dossiers/fichiers

- [x] SIVC — Air Liquide Côte d'Ivoire : 22 dossiers annuels, 53 fichiers ; hash en attente.
- [x] BOABF — Bank of Africa Burkina Faso : 18 dossiers (dont `divers`), 57 fichiers ; hash partiel.
- [ ] 46 autres émetteurs.

### Travail à réaliser pour chaque société

- [ ] inventorier tous les dossiers ;
- [ ] inventorier tous les fichiers ;
- [ ] enregistrer identifiant source, chemin, nom, taille, hash, dates et type ;
- [ ] détecter doublons binaires ;
- [ ] détecter versions/révisions probables ;
- [ ] déterminer les périodes économiques réellement couvertes ;
- [ ] identifier les années couvertes par des fichiers rangés dans `divers` ;
- [ ] mesurer la couverture documentaire réelle.

### Sous-étapes transversales encore ouvertes

- [ ] produire un inventaire machine lisible consolidé des 48 sociétés ;
- [ ] collecter/calculer les hash de tous les fichiers ;
- [ ] rapprocher les candidats `_2/_3/...` par hash/contenu ;
- [ ] relier les documents explicitement `annule et remplace` ;
- [ ] résoudre les périodes économiques depuis le contenu, pas le classement.

## P2 — Schéma RAW v1

- [ ] formaliser les tables universelles ;
- [ ] intégrer géométrie des tableaux ;
- [ ] intégrer scopes/dimensions extensibles ;
- [ ] intégrer provenance/versioning ;
- [ ] valider `event_facts_raw` ;
- [ ] valider `regulatory_facts_raw` ;
- [ ] décider si `context_facts_raw` est nécessaire ;
- [ ] décider si `esg_facts_raw` est nécessaire ;
- [ ] écrire migrations SQL ;
- [ ] tester les contraintes d'intégrité.

## P3 — Extraction RAW exhaustive

À commencer seulement après couverture P1 suffisante.

## P4 — Contrôles qualité

À développer parallèlement à l'extraction RAW, sans corriger silencieusement la source.

## P5 — MAPPED / CANONICAL

À ne commencer qu'après couverture RAW suffisante.

## P6 — DERIVED / ANALYTICS

À traiter ultérieurement.

## Rappel permanent

**Ne jamais créer de branche. Tout travail de ce dépôt se fait sur `main`.**
