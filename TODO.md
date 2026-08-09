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

### Progression P1

- [x] **37 / 48 émetteurs** inventoriés au niveau dossiers/fichiers.
- [x] **2 271 PDF** recensés.
- [ ] **11 émetteurs** restent à inventorier.

### Lot 33–37

- [x] CABC — 29 dossiers (1998–2025 + `divers`), **90 PDF**.
- [x] SICC — 25 dossiers, **19 PDF** ; 2014 absent, pas de dossier 2024/2025 observé.
- [x] STBC — 29 dossiers (1998–2025 + `divers`), **91 PDF** ; plusieurs révisions 2025.
- [x] SMBC — 28 dossiers 1998–2025, **106 PDF** ; total vérifié par scission 36 + 70 car la recherche ticker plafonnait à 100.
- [x] SDCC — 29 dossiers (1998–2025 + `divers`), **92 PDF** ; total vérifié par scission 36 + 56 ; SYSCOHADA révisé + IFRS individuel + IFRS consolidé observés.

### P1-R — reconnaissance PDF

- [x] profils BICC 2022, BIIC T2 2025, ETIT 2023 ;
- [x] métadonnées PDF non souveraines ;
- [x] STOCK vs FLOW selon contexte ;
- [x] variations publiées = RAW PUBLISHED ;
- [x] framework comptable vs scope indépendants ;
- [x] limites techniques de recherche ≠ total SOURCE ;
- [x] T1/T2/T3/T4/S1/S2 supportés ;
- [x] préserver les deep pilots BOABF/CIEC/NTLC/SNTS sans duplication ;
- [ ] créer de nouveaux profils uniquement sur nouveau pattern réel.

### Passes transversales P1 encore ouvertes

- [ ] manifeste machine-lisible consolidé ;
- [ ] SHA-256 globaux ;
- [ ] doublons exacts et relations de version ;
- [ ] périodes économiques depuis contenu ;
- [ ] attribution émetteur/document ;
- [ ] couverture documentaire réelle ;
- [ ] réconciliation avec BRVM courante.

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
