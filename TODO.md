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
- [x] Analyser complètement le fonctionnement du collecteur V1.
- [x] Documenter le plan d'évolution incrémental dans `docs/BRVM_COLLECTOR_V2_PLAN.md`.
- [x] Définir la méthode d'inventaire direct depuis Drive.
- [x] Documenter la règle d'attribution émetteur (`D024`).
- [x] Documenter le statut `REMOTE_DELTA_IDENTIFIED` (`D028`).

### Émetteurs inventoriés au niveau dossiers/fichiers

- [x] SIVC — 22 dossiers annuels, 53 fichiers ; hash en attente.
- [x] BOABF — 18 dossiers dont `divers`, 57 fichiers ; hash partiel.
- [x] BOAB — 29 dossiers, 59 fichiers ; anomalie d'attribution à revoir ; hash en attente.
- [x] BOAC — 19 dossiers, 60 fichiers ; delta BRVM courant identifié ; hash en attente.
- [x] BOAM — 16 dossiers, 44 fichiers ; delta BRVM courant identifié ; hash en attente.
- [ ] 43 autres émetteurs.

### Travail à réaliser pour chaque société

- [ ] inventorier tous les dossiers ;
- [ ] inventorier tous les fichiers ;
- [ ] enregistrer identifiant source, chemin, nom, taille, hash, dates et type ;
- [ ] détecter doublons binaires ;
- [ ] détecter versions/révisions probables ;
- [ ] déterminer les périodes économiques réellement couvertes ;
- [ ] identifier les années couvertes par des fichiers rangés dans `divers` ;
- [ ] valider l'attribution du document à l'émetteur ;
- [ ] mesurer la couverture documentaire réelle ;
- [ ] lorsque pertinent, comparer au catalogue BRVM courant et enregistrer le delta.

### Sous-étapes transversales encore ouvertes

- [ ] produire un inventaire machine lisible consolidé des 48 sociétés ;
- [ ] collecter/calculer les hash de tous les fichiers ;
- [ ] rapprocher les candidats `_2/_3/...` par hash/contenu ;
- [ ] relier les documents explicitement `annule et remplace` ;
- [ ] revoir les fichiers potentiellement hors périmètre ;
- [ ] résoudre les périodes économiques depuis le contenu ;
- [ ] réconcilier l'inventaire historique avec les documents BRVM courants.

## Collecteur BRVM V2 — après P1

- [x] analyser la V1 historique ;
- [x] définir le design incrémental/versionné ;
- [ ] créer le manifeste machine-lisible de référence ;
- [ ] implémenter un mode `--dry-run` ;
- [ ] comparer source distante et manifeste sans télécharger ;
- [ ] ajouter SHA-256 / validation PDF ;
- [ ] ajouter `first_seen_at` / `last_seen_at` ;
- [ ] gérer même URL / nouveau hash ;
- [ ] gérer `annule/remplace/corrige` ;
- [ ] détecter nouveaux émetteurs/slugs ;
- [ ] valider la non-régression ;
- [ ] seulement ensuite activer le téléchargement incrémental.

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
