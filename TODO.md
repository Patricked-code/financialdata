# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées.
- [x] snapshot initial : 2 950 PDF.
- [x] état live revérifié : **2 957 PDF** après delta CBIBF +7.
- [x] checkpoint v2 : `inventory/P1_48_ISSUERS_CHECKPOINT_v2_20260809.md`.
- [x] index live : `inventory/p1_issuer_manifest.csv`.

### Document manifest

- [x] schéma défini.
- [x] `inventory/p1_document_manifest.csv` créé.
- [x] couverture actuelle : **14 / 2 957**.
- [x] BIIC 2/2.
- [x] TRITRAF 8/8.
- [ ] CBIBF : 2/15 actuellement dans le manifeste ; ajouter les 13 autres.
- [ ] poursuivre ORAC, SICC, MVSC, UNLC puis autres émetteurs.

### SHA-256

- [x] TRITRAF 8/8.
- [x] CBIBF 2/15.
- [x] total SHA : **10 / 2 957**.
- [x] premier groupe de doublon exact enregistré : `inventory/p1_duplicate_groups.csv`.
- [ ] compléter CBIBF puis corpus suivants.

### Doublons / versions

- [x] CBIBF S1 2024 plain + `_2` : `EXACT_DUPLICATE`, même SHA `8fb042a2...`.
- [x] TRITRAF 2004 plain + `_2` : SHA différents, doublon binaire exclu.
- [ ] relations sémantiques/version restantes.

### Autres passes

- [ ] périodes économiques depuis contenu ;
- [ ] attribution émetteur/document ;
- [ ] couverture documentaire ;
- [ ] P1-FRESH / réconciliation BRVM courante.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.
