# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées.
- [x] snapshot initial : 2 950 PDF ; V2 2 957 ; V3 2 964 ; V4 2 981 ; V5 2 996 ; V6 2 999 ; V7 3 011 ; V8 3 013 ; V9 3 028 ; V10 3 031 ; V11 courant **3 041 PDF**.
- [x] checkpoint courant : `inventory/P1_48_ISSUERS_CHECKPOINT_v11_20260810.md`.
- [x] index live : `inventory/p1_issuer_manifest.csv`.
- [ ] continuer la revérification live société par société pendant les passes transversales.

### Document manifest

- [x] schéma : `docs/P1_DOCUMENT_MANIFEST_SCHEMA.md` ; stratégie shards : `docs/P1_MANIFEST_SHARDING.md` ; maître : `inventory/p1_document_manifest.csv`.
- [x] maître consolidé : **14 / 3 041** lignes.
- [x] BIIC : 2/2 Drive IDs, tailles et SHA ; registre `inventory/hashes/BIIC.csv`.
- [x] BOAS : 43/43 Drive IDs, tailles et SHA ; registre `inventory/hashes/BOAS.csv`.
- [x] ECOC : 42/42 Drive IDs, tailles et SHA ; revue `inventory/reviews/ECOC_VERSION_REVIEW_20260811.md`.
- [ ] backfill métadonnées temporelles + shards compatibles des corpus hashés.
- [ ] poursuivre tous les autres émetteurs.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43.
- [x] total SHA effectivement calculés : **393 / 3 041**.
- [x] groupes de doublons exacts prouvés : **4** dans `inventory/p1_duplicate_groups.csv`.
- [ ] BOAM : revérification live puis SHA 100 %.

### Doublons / versions

- [x] CBIBF S1 2024 plain + `_2` : exact duplicate.
- [x] SHEC EF 2022 `_2` + `_3` : exact duplicate.
- [x] SHEC EF 2025 plain + `_2` : exact duplicate.
- [x] ECOC EF 2021 plain + `_2` : exact duplicate.
- [x] ECOC T1 2023 et annuel 2024 : corrections/supersessions validées ; T3 2024 : aucune supersession sémantique démontrée.
- [x] BIIC : 2 SHA distincts, aucun doublon.
- [x] BOAS : 43 SHA distincts ; variantes historiques `_2/_3` et EF 2017 binaires distinctes ; aucune fusion par nom.
- [ ] relations sémantiques/version restantes.

### Périodes / qualité

- [x] BOAS `divers_Rapport_S1_BOAS.pdf` résolu visuellement comme **S1 2019**, daté du **09/09/2019**.
- [x] BOAS dossier 2013 toujours vide en PDF direct ; ne pas inventer une absence économique.
- [x] règle réaffirmée : le dossier `divers` ne dicte jamais la période.
- [ ] périodes économiques fines depuis contenu pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM courante et collecteur V2 pour les nouveautés, dont BOAS 2026.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`BOAM_LIVE_RECHECK_AND_SHA`, puis poursuivre les corpus non hashés par taille croissante.
