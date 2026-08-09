# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

**Statut : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS**

### Socle P1

- [x] Créer `inventory/README.md`.
- [x] Créer `inventory/P1_ROOT_MANIFEST.md`.
- [x] Vérifier les 48 dossiers société à la racine.
- [x] Identifier et documenter `telecharger_rapports_brvm.py`.
- [x] Définir la méthode d'inventaire direct depuis Drive.
- [x] Documenter la règle d'attribution émetteur (`D024`).

### Émetteurs inventoriés au niveau dossiers/fichiers

- [x] SIVC — Air Liquide Côte d'Ivoire : 22 dossiers annuels, 53 fichiers ; hash en attente.
- [x] BOABF — Bank of Africa Burkina Faso : 18 dossiers (dont `divers`), 57 fichiers ; hash partiel.
- [x] BOAB — Bank of Africa Bénin : 29 dossiers (1998–2025 + `divers`), 59 fichiers ; anomalie d'attribution à revoir ; hash en attente.
- [ ] 45 autres émetteurs.

### Travail à réaliser pour chaque société

- [ ] inventorier tous les dossiers ;
- [ ] inventorier tous les fichiers ;
- [ ] enregistrer identifiant source, chemin, nom, taille, hash, dates et type ;
- [ ] détecter doublons binaires ;
- [ ] détecter versions/révisions probables ;
- [ ] déterminer les périodes économiques réellement couvertes ;
- [ ] identifier les années couvertes par des fichiers rangés dans `divers` ;
- [ ] valider l'attribution du document à l'émetteur ;
- [ ] mesurer la couverture documentaire réelle.

### Sous-étapes transversales encore ouvertes

- [ ] produire un inventaire machine lisible consolidé des 48 sociétés ;
- [ ] collecter/calculer les hash de tous les fichiers ;
- [ ] rapprocher les candidats `_2/_3/...` par hash/contenu ;
- [ ] relier les documents explicitement `annule et remplace` ;
- [ ] revoir les fichiers potentiellement hors périmètre ;
- [ ] résoudre les périodes économiques depuis le contenu, pas le classement.

## P2 — Schéma RAW v1

À ne pas commencer avant couverture P1 suffisante.

## P3 — Extraction RAW exhaustive

À commencer seulement après couverture P1 suffisante.

## P4 — Contrôles qualité

À développer avec l'extraction RAW, sans corriger silencieusement la source.

## P5 — MAPPED / CANONICAL

À ne commencer qu'après couverture RAW suffisante.

## P6 — DERIVED / ANALYTICS

À traiter ultérieurement.

## Rappel permanent

**Ne jamais créer de branche. Tout travail de ce dépôt se fait sur `main`.**
