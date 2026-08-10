# P1 SOURCE — NSIA Banque Côte d'Ivoire / NSBC

Date : 2026-08-10
Statut : `P1_HASH_COMPLETE / LIVE_SOURCE_DELTA_DETECTED / VERSION_REVIEW_PARTIAL`

- Ticker : `NSBC`
- Dossier Drive : `1FzP9fR9x025gJw18qziXs2Dxusyv0vP1`
- Dossiers directs : **10** = années `2017` à `2025` + `divers`
- Premier inventaire de session : **38 PDF**
- État Drive live revérifié par parents + MIME : **41 PDF**
- Delta live : **+3 PDF**
- Répartition live : 2017=3 ; 2018=6 ; 2019=7 ; 2020=4 ; 2021=5 ; 2022=4 ; 2023=4 ; 2024=4 ; 2025=3 ; divers=1.
- Matérialisation brute Drive : **41 / 41**.
- Taille Drive ↔ taille locale : **41 / 41 validée**.
- SHA-256 : **41 / 41 calculés**.
- Contenus binaires uniques : **41 / 41**.
- Doublons binaires exacts NSBC : **0**.
- Registre : `inventory/hashes/NSBC.csv`.

## Particularités SOURCE

- `divers_Etats_Financiers_NSBC.pdf` nécessite résolution de période depuis le contenu ;
- 2019 contient `2019_Rapport_T1_NSBC.pdf` et `2019_Rapport_T1_NSBC_rev.pdf` ;
- 2019 contient aussi deux états financiers physiques (`plain` et `_2`) ;
- 2021 contient `2021_Etats_Financiers_NSBC.pdf` et `2021_Etats_Financiers_NSBC_rev.pdf` ;
- T1/S1/T3, états financiers et CAC/attestations présents selon années ;
- 2024 inclut un communiqué distinct.

## Relations de version validées par contenu

### T1 2019 — correction explicite

`2019_Rapport_T1_NSBC_rev.pdf` est explicitement marqué **« Version corrigée »** et précise que les chiffres au 31/03/2018 ont été corrigés conformément au Plan Comptable Bancaire révisé.

- période courante 31/03/2019 inchangée : PNB 15 877 M FCFA ; résultat avant impôts 3 573 M ; résultat net 2 817 M ;
- comparatif 31/03/2018 : PNB 17 511 → 17 380 M ; RAI 6 573 → 2 620 M ; RN 5 363 → 2 057 M ;
- variations/narratif : baisse RAI/RN de -46%/-47% dans la première publication → hausse +36%/+37% dans la version corrigée ;
- dates textuelles : 29 avril 2019 → 24 mai 2019 ;
- SHA plain : `34b4805b96abce8d8282ee9d170f49222d7e7522cd654c4f09e05f0f9dbd6378` ;
- SHA rev : `9fe48c0fa362f11d609749e8d8d9c307e736c8085ee854cb2496053e8d5cfac0`.

Verdict : `CORRECTED_VERSION_OF / SUPERSEDES = VALIDATED` ; deux contenus binaires distincts.

### États financiers 2021 — annulation et remplacement explicites

`2021_Etats_Financiers_NSBC_rev.pdf` contient : **« LE PRÉSENT COMMUNIQUÉ ANNULE ET REMPLACE LA PARUTION DU 04 AVRIL 2022 »**.

- résultat net 2021 : 20 998 → 23 713 M FCFA ;
- capitaux propres et ressources assimilées : 129 809 → 132 524 M FCFA ;
- dates textuelles observées : 1er avril 2022 dans la première publication ; 12 mai 2022 dans la publication de remplacement ;
- SHA plain : `14c973172307e8e20ecadde4d566f5a871bd957f43349c8c1137f6bd2b593858` ;
- SHA rev : `b7d3a1117eb945d3a446112fe917456a29aa535c0a1a5fe67e58620e5902d179`.

Verdict : `SUPERSEDES = VALIDATED`. La première publication reste conservée comme vérité point-in-time historique ; elle n'est jamais supprimée du RAW.

### États financiers 2019 — relation encore à qualifier

`2019_Etats_Financiers_NSBC.pdf` et `_2.pdf` sont deux objets physiques distincts :
- tailles : **1 325 452** vs **8 069 372 octets** ;
- SHA plain : `dbb70783c34f0c00848bf2bc7b37ab793853b59ea1da4c80e91a7935d1d3428e` ;
- SHA `_2` : `28d9fa10a49c5b0f9ceaee05bb1427657c886ac3786d32e2f7044b8c6a34794a`.

Verdict binaire : `DISTINCT`. La relation sémantique précise reste `VISUAL_REVIEW_REQUIRED` car aucun texte natif exploitable n'est exposé par le connecteur.

## Règle

Un suffixe `_rev`/`_2` n'établit jamais à lui seul une relation. Les mentions source « Version corrigée » ou « annule et remplace » valident une correction/supersession. Les deux versions et tous leurs facts restent conservés avec lineage point-in-time. Le SHA établit uniquement l'identité binaire, pas l'ordre sémantique des versions.

## Gouvernance

Les cas T1 2019 et FY 2021 ont été ajoutés au document canonique Drive `BRVM_RAW_DATABASE — Gouvernance, architecture et observations conceptuelles` le 2026-08-10.

## Restant transversal

`DOCUMENT_MANIFEST_NSBC = PARTIAL_METADATA_READY` ; `SHA256_NSBC = COMPLETE_41_OF_41` ; `EXACT_DUPLICATES_NSBC = 0` ; `VERSION_LINKS = 2_VALIDATED + 1_VISUAL_REVIEW_REQUIRED` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
