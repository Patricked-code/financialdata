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
- [x] V6 : **2 999 PDF** après UNLC `+3`.
- [x] V7 : **3 011 PDF** après ORGT `+12`.
- [x] V8 : **3 013 PDF** après SHEC `+2`.
- [x] V9 courant : **3 028 PDF** après STAC `+15`.
- [x] checkpoint courant : `inventory/P1_48_ISSUERS_CHECKPOINT_v9_20260809.md`.
- [x] index live : `inventory/p1_issuer_manifest.csv`.
- [ ] continuer la revérification live société par société pendant les passes transversales.

### Document manifest

- [x] schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md`.
- [x] stratégie shards : `docs/P1_MANIFEST_SHARDING.md`.
- [x] maître créé : `inventory/p1_document_manifest.csv`.
- [x] maître consolidé : **14 / 3 028** lignes.
- [x] BIIC 2/2.
- [x] TRITRAF 8/8.
- [x] CBIBF 15/15 dans `inventory/manifests/CBIBF.csv`.
- [x] ORAC 21/21 dans `inventory/manifests/ORAC.csv`.
- [x] SICC : 36/36 Drive IDs, parents, tailles et SHA identifiés.
- [x] MVSC : 35/35 Drive IDs, parents, tailles et SHA identifiés.
- [x] UNLC : 23/23 Drive IDs, parents, tailles et SHA identifiés.
- [x] ORGT : 35/35 Drive IDs, parents, tailles et SHA identifiés.
- [x] SHEC : 39/39 Drive IDs, parents, tailles et SHA identifiés.
- [x] STAC : 53/53 Drive IDs, parents, tailles et SHA identifiés.
- [ ] backfill métadonnées temporelles + shards compatibles SICC/MVSC/UNLC/ORGT/SHEC/STAC.
- [ ] NSBC : revérifier le total live avant hash.
- [ ] poursuivre ensuite tous les autres émetteurs.

### SHA-256

- [x] TRITRAF 8/8.
- [x] CBIBF 15/15 — `inventory/hashes/CBIBF.csv`.
- [x] ORAC 21/21 — `inventory/hashes/ORAC.csv`.
- [x] SICC 36/36 — `inventory/hashes/SICC.csv`.
- [x] MVSC 35/35 — `inventory/hashes/MVSC.csv`.
- [x] UNLC 23/23 — `inventory/hashes/UNLC.csv`.
- [x] ORGT 35/35 — `inventory/hashes/ORGT.csv`.
- [x] SHEC 39/39 — `inventory/hashes/SHEC.csv`.
- [x] STAC 53/53 — `inventory/hashes/STAC.csv`.
- [x] total SHA : **265 / 3 028**.
- [x] groupes de doublons exacts : **3** dans `inventory/p1_duplicate_groups.csv`.
- [ ] poursuivre NSBC puis corpus courts suivants.

### Doublons / versions

- [x] CBIBF S1 2024 plain + `_2` : `EXACT_DUPLICATE`.
- [x] SHEC EF 2022 `_2` + `_3` : `EXACT_DUPLICATE`.
- [x] SHEC EF 2025 plain + `_2` : `EXACT_DUPLICATE`.
- [x] TRITRAF 2004 plain + `_2` : SHA différents.
- [x] ORAC : annuels `_rev` / `_2` non fusionnés.
- [x] SICC : variantes `_2` / `_3` non fusionnées.
- [x] MVSC : variantes `_2` / `_3` et EF 2019 non fusionnés.
- [x] UNLC : annuels 2020 plain / `_2` non fusionnés.
- [x] ORGT : paires EF/CAC proches non fusionnées.
- [x] SHEC EF 2021 plain / `_2` et EF 2023 plain / `_2` : binaires distincts.
- [x] STAC séries `_2/_3/_4` et EF 2019 `_rev` : tous binaires distincts.
- [ ] relations sémantiques/version restantes.

### Qualité / cohérence

- [x] ORAC : tailles du registre SHA revalidées contre Drive ; hashes confirmés.
- [x] MVSC/UNLC/ORGT/SHEC/STAC : contrôle taille Drive ↔ fichier hashé appliqué pendant la passe.
- [ ] backfill des métadonnées temporelles des shards incomplets.
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
