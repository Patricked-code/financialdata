# TODO — financialdata

Backlog canonique. Ne pas considérer une tâche terminée tant que le résultat n'est pas vérifié et que `SUIVI.md` n'est pas mis à jour.

## P0 — Gouvernance initiale

**Statut : COMPLETE.**

## P1 — Inventaire documentaire exhaustif

**Statut : IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_OPEN**

### Inventaire dossiers/fichiers par émetteur

- [x] **48 / 48 émetteurs** inventoriés.
- [x] **2 950 PDF** recensés.
- [x] checkpoint global : `inventory/P1_48_ISSUERS_CHECKPOINT.md`.

### Lot final 43–48

- [x] TTLS — 11 dossiers (2016–2025 + `divers`), **45 PDF**.
- [x] PRSC — 28 dossiers 1998–2025, **68 PDF**.
- [x] TRITRAF — 7 dossiers 1998–2004, **8 PDF** ; corpus historique sparse.
- [x] UNLC — 9 dossiers (2016–2023 + `divers`), **20 PDF** ; pas de dossier 2024/2025 observé.
- [x] UNXC — 28 dossiers 1998–2025, **83 PDF**.
- [x] SHEC — 10 dossiers 2016–2025, **37 PDF**.

### P1-R — reconnaissance PDF

- [x] profils BICC 2022, BIIC T2 2025, ETIT 2023 ;
- [x] métadonnées PDF non souveraines ;
- [x] STOCK vs FLOW selon contexte ;
- [x] variations publiées = RAW PUBLISHED ;
- [x] framework comptable vs scope indépendants ;
- [x] limites techniques de recherche ≠ total SOURCE ;
- [x] T1/T2/T3/T4/S1/S2 supportés ;
- [x] attribution émetteur peut être `REVIEW_REQUIRED` ;
- [x] deep pilots BOABF/CIEC/NTLC/SNTS conservés sans duplication ;
- [ ] nouveaux profils uniquement lorsqu'un nouveau pattern réel apparaît.

### P1 — passes transversales maintenant prioritaires

- [ ] créer le manifeste machine-lisible document par document ;
- [ ] enregistrer identifiant Drive, parent, émetteur attendu, nom, taille, type, dates source et statut d'attribution ;
- [ ] collecter/calculer les SHA-256 des **2 950 PDF** ;
- [ ] établir les doublons binaires ;
- [ ] établir les relations `VERSION_OF / REVISED_BY / SUPERSEDES / POSSIBLE_DUPLICATE` ;
- [ ] résoudre les périodes économiques depuis le contenu ;
- [ ] valider l'attribution émetteur/document ;
- [ ] calculer la couverture documentaire réelle ;
- [ ] réconcilier avec la BRVM courante.

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

À figer après couverture suffisante des passes P1 transversales et P1-R.

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
