# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

**Statut : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS / BATCH_FAST**

### Socle P1

- [x] créer le socle `inventory/` ;
- [x] vérifier les 48 dossiers société ;
- [x] identifier/analyser `telecharger_rapports_brvm.py` ;
- [x] documenter le collecteur V2 futur ;
- [x] créer `ROADMAP.md` ;
- [x] activer `P1-R PDF_RECOGNITION_DISCOVERY` ;
- [x] documenter les premières règles de reconnaissance vérifiées sur contenu réel.

### Émetteurs inventoriés au niveau dossiers/fichiers

- [x] SIVC — 53 fichiers.
- [x] BOABF — 57 fichiers.
- [x] BOAB — 59 fichiers.
- [x] BOAC — 60 fichiers.
- [x] BOAM — 44 fichiers.
- [x] BOAN — 60 fichiers.
- [x] BOAS — 43 fichiers.
- [x] BNBC — 28 dossiers 1998–2025, 78 fichiers.
- [x] BICC — 28 dossiers 1998–2025, 61 fichiers.
- [x] BIIC — 2 dossiers, 2 fichiers ; corpus sparse.
- [x] AGLC — 28 dossiers 1998–2025, 60 fichiers.
- [x] CFAC — 26 dossiers, 94 fichiers.
- [x] CIEC — 29 dossiers, 61 fichiers ; deep pilot existant.
- [x] CBIBF — 4 dossiers, 8 fichiers ; 2022 vide.
- [x] SEMC — 25 dossiers, 54 fichiers ; `divers`, 2002 absent.
- [x] ECOC — 9 dossiers 2017–2025, 32 fichiers ; couples `_rev` à réconcilier.
- [x] ETIT — 23 dossiers 2003–2025, 81 fichiers ; corpus dense, multi-devise.
- [ ] 31 autres émetteurs.

**Total recensé sur les 17 premiers émetteurs : 907 fichiers.**

### P1-R — reconnaissance PDF

- [x] stratégie générale : `docs/PDF_RECOGNITION_STRATEGY.md` ;
- [x] profil BICC 2022 : états financiers bancaires, bilan/passif/hors-bilan/résultat ;
- [x] profil BIIC T2 2025 : tableau d'activité + variations + narratif/perspectives ;
- [x] profil ETIT 2023 : états consolidés IFRS, bi-devise USD/FCFA, attribution du résultat ;
- [x] confirmer T2 sur le contenu visible ;
- [x] documenter `DOCUMENT_METADATA_MISMATCH` ;
- [x] documenter stock vs flow selon contexte de tableau ;
- [x] documenter tableau vs narratif avec unités/arrondis différents ;
- [x] documenter framework comptable vs scope indépendants ;
- [x] documenter `ownership_attribution_raw` comme dimension candidate ;
- [ ] multiplier les profils représentatifs hors banque : utility, industrie, télécom, agriculture, logistique, automobile, etc.

### Passes transversales P1 encore ouvertes

- [ ] produire le manifeste machine-lisible consolidé ;
- [ ] collecter/calculer les SHA-256 ;
- [ ] établir doublons exacts et relations de version ;
- [ ] résoudre les périodes économiques depuis le contenu ;
- [ ] valider l'attribution émetteur/document ;
- [ ] mesurer la couverture documentaire réelle ;
- [ ] réconcilier l'historique avec la BRVM courante.

## P1-FRESH — Collecteur BRVM V2

- [x] analyser la V1 ;
- [x] définir le design incrémental/versionné ;
- [ ] manifeste de référence ;
- [ ] `--dry-run` ;
- [ ] comparaison distante ;
- [ ] SHA-256 / validation PDF ;
- [ ] `first_seen_at` / `last_seen_at` ;
- [ ] gestion révisions/doublons/nouveaux slugs ;
- [ ] tests de non-régression ;
- [ ] téléchargement incrémental seulement après validation.

## P2 — Schéma RAW v1

À figer après couverture P1/P1-R suffisante.

## P3 — Extraction RAW exhaustive

Appliquer les profils/règles à tous les documents SOURCE validés.

## P4 — Contrôle / qualité / lineage

Contrôles sans correction silencieuse de la source.

## P5 — MAPPED

Mapping sémantique explicite et versionné.

## P6 — CANONICAL

Harmonisation multi-sociétés/périodes/unités/scopes.

## P7 — DERIVED

Calculs internes reproductibles avec formule et IDs d'entrée.

## P8 — ANALYTICS

Ratios, valorisation, rankings, screener, alertes, scoring et IA/NLP.

## Rappel permanent

**Ne jamais créer de branche. Tout travail se fait sur `main`.**
