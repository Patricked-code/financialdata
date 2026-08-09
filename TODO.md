# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées.
- [x] snapshot initial : **2 950 PDF**.
- [x] V2 : **2 957 PDF** après CBIBF `+7`.
- [x] V3 : **2 964 PDF** après ORAC `+7`.
- [x] V4 : **2 981 PDF** après SICC `+17`.
- [x] V5 : **2 996 PDF** après MVSC `+15`.
- [x] V6 courant : **2 999 PDF** après UNLC `+3`.
- [x] checkpoint courant : `inventory/P1_48_ISSUERS_CHECKPOINT_v6_20260809.md`.
- [x] index live : `inventory/p1_issuer_manifest.csv`.
- [ ] continuer la revérification live société par société pendant les passes transversales.

### Document manifest

- [x] schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
- [x] stratégie shards : `docs/P1_MANIFEST_SHARDING.md`.
- [x] maître créé : `inventory/p1_document_manifest.csv`.
- [x] maître consolidé : **14 / 2 999** lignes.
- [x] BIIC 2/2.
- [x] TRITRAF 8/8.
- [x] CBIBF 15/15 dans `inventory/manifests/CBIBF.csv`.
- [x] ORAC 21/21 dans `inventory/manifests/ORAC.csv`.
- [x] SICC : 36/36 Drive IDs, parents, tailles et SHA identifiés.
- [x] MVSC : 35/35 Drive IDs, parents, tailles et SHA identifiés.
- [x] UNLC : 23/23 Drive IDs, parents, tailles et SHA identifiés.
- [ ] backfill métadonnées temporelles + shards compatibles SICC/MVSC/UNLC.
- [ ] ORGT : revérifier le total live avant hash.
- [ ] poursuivre ensuite tous les autres émetteurs.

### SHA-256

- [x] TRITRAF 8/8.
- [x] CBIBF 15/15 — `inventory/hashes/CBIBF.csv`.
- [x] ORAC 21/21 — `inventory/hashes/ORAC.csv`.
- [x] SICC 36/36 — `inventory/hashes/SICC.csv`.
- [x] MVSC 35/35 — `inventory/hashes/MVSC.csv`.
- [x] UNLC 23/23 — `inventory/hashes/UNLC.csv`.
- [x] total SHA : **138 / 2 999**.
- [x] premier groupe de doublon exact : `inventory/p1_duplicate_groups.csv`.
- [ ] poursuivre ORGT puis corpus courts suivants.

### Doublons / versions

- [x] CBIBF S1 2024 plain + `_2` : `EXACT_DUPLICATE`, SHA commun `8fb042a2...`.
- [x] TRITRAF 2004 plain + `_2` : SHA différents.
- [x] ORAC : 21 contenus binaires uniques ; annuels `_rev` / `_2` non fusionnés.
- [x] SICC : 36 contenus binaires uniques ; variantes `_2` / `_3` non fusionnées.
- [x] MVSC : 35 contenus binaires uniques ; variantes `_2` / `_3` et EF 2019 non fusionnés.
- [x] UNLC : 23 contenus binaires uniques ; annuels 2020 plain / `_2` non fusionnés.
- [ ] relations sémantiques/version restantes.

### Qualité / cohérence

- [x] ORAC : correction des `file_size_bytes` du registre SHA après revalidation Drive ; hashes confirmés.
- [x] MVSC/UNLC : contrôle taille Drive ↔ fichier hashé appliqué pendant la passe.
- [ ] backfill des métadonnées temporelles SICC/MVSC/UNLC.
- [ ] appliquer systématiquement taille Drive ↔ taille du fichier hashé avant statut final.

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
