# TODO — financialdata

Backlog canonique. Tout travail se fait directement sur `main`.

## P0 — Gouvernance

**COMPLETE**

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire émetteurs

- [x] 48 / 48 émetteurs.
- [x] 2 950 PDF recensés.
- [x] `inventory/P1_48_ISSUERS_CHECKPOINT.md`.
- [x] `inventory/p1_issuer_manifest.csv`.

### Document manifest

- [x] schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
- [x] fichier : `inventory/p1_document_manifest.csv`.
- [x] seed puis expansion initiale : **12 / 2 950** lignes.
- [x] BIIC : **2 / 2** documents présents dans le manifeste.
- [x] TRITRAF : **8 / 8** documents présents dans le manifeste.
- [ ] compléter jusqu'à **2 950 / 2 950**.

### SHA-256

- [x] TRITRAF : **8 / 8** hashes calculés et enregistrés.
- [x] les deux variantes TRITRAF 2004 ont des hashes différents : doublon binaire exclu.
- [ ] SHA global : **8 / 2 950**.

### Prochains corpus à traiter

- [ ] CBIBF — 8 PDF.
- [ ] ORAC — 14 PDF.
- [ ] SICC — 19 PDF.
- [ ] MVSC — 20 PDF.
- [ ] UNLC — 20 PDF.

### Autres passes transversales

- [ ] relations de versions/révisions ;
- [ ] périodes économiques depuis contenu ;
- [ ] attribution émetteur/document ;
- [ ] couverture documentaire ;
- [ ] réconciliation BRVM courante / P1-FRESH.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023.
Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

Séquence : `P2 RAW SCHEMA → P3 RAW EXTRACTION → P4 QUALITY/LINEAGE → P5 MAPPED → P6 CANONICAL → P7 DERIVED → P8 ANALYTICS`.
