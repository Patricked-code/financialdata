# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

**Statut : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS / BATCH_FAST**

### Progression P1

- [x] **42 / 48 émetteurs** inventoriés au niveau dossiers/fichiers.
- [x] **2 689 PDF** recensés.
- [ ] **6 émetteurs** restent à inventorier : `TTLS`, `PRSC`, `TRITRAF`, `UNLC`, `UNXC`, `SHEC`.

### Lot 38–42

- [x] SOGC — 28 dossiers 1998–2025, **106 PDF** ; total parenté 37 + 69.
- [x] SLBC — 28 dossiers 1998–2025, **65 PDF**.
- [x] SNTS — 27 dossiers, **101 PDF** ; 2016 absent ; fichier ONATEL rangé sous Sonatel 2017 → `issuer_assignment_status = REVIEW_REQUIRED`.
- [x] SCRC — 11 dossiers (2016–2025 + `divers`), **45 PDF** ; T4 2017 observé et `divers` CAC à dater par contenu.
- [x] TTLC — 28 dossiers 1998–2025, **101 PDF** ; total parenté 34 + 67.

### P1-R — reconnaissance PDF

- [x] profils BICC 2022, BIIC T2 2025, ETIT 2023 ;
- [x] métadonnées PDF non souveraines ;
- [x] STOCK vs FLOW selon contexte ;
- [x] variations publiées = RAW PUBLISHED ;
- [x] framework comptable vs scope indépendants ;
- [x] limites techniques de recherche ≠ total SOURCE ;
- [x] T1/T2/T3/T4/S1/S2 supportés ;
- [x] attribution émetteur peut être `REVIEW_REQUIRED` même si le fichier est physiquement rangé dans un dossier société ;
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
