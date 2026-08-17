# TODO — financialdata

Dépôt canonique : `Patricked-code/financialdata`. Travail direct sur `main` uniquement.

## P1 — SOURCE

**IN_PROGRESS / INVENTORY_48_COMPLETE / TRANSVERSE_PASSES_ACTIVE**

### Inventaire

- [x] 48 / 48 sociétés inventoriées ; état live V14 **3 060 PDF**.
- [x] checkpoint `inventory/P1_48_ISSUERS_CHECKPOINT_v14_20260817.md` ; index `inventory/p1_issuer_manifest.csv`.
- [x] SIBC revérifié : **49 PDF** au lieu de 46, delta `+3` persisté avant hash.
- [x] SIVC revérifié : **53 PDF**, aucun delta ; 22 dossiers annuels contrôlés, 2024 toujours vide.
- [x] SEMC revérifié : **54 PDF**, aucun delta ; 25 dossiers directs contrôlés individuellement.
- [x] BOABF revérifié : **57 PDF**, aucun delta ; 18 dossiers directs contrôlés.
- [x] BOAB revérifié : **59 PDF**, aucun delta ; 29 dossiers parents contrôlés.
- [x] BOAC revérifié : **74 PDF** au lieu de 60, delta `+14` persisté avant SHA dans V14.
- [ ] continuer la revérification live société par société, prochain corpus : **BOAN** (snapshot 60).

### Document manifest

- [x] schéma/sharding/maître créés ; maître consolidé **14 / 3 060**.
- [x] registres SHA avec Drive IDs + tailles disponibles pour les corpus hashés, y compris BOAB 59/59 et BOAC 74/74.
- [ ] backfill métadonnées temporelles et shards compatibles pour les corpus hashés.
- [ ] poursuivre tous les émetteurs jusqu'à consolidation complète du manifeste.

### SHA-256

- [x] TRITRAF 8/8 ; CBIBF 15/15 ; ORAC 21/21 ; SICC 36/36 ; MVSC 35/35 ; UNLC 23/23 ; ORGT 35/35 ; SHEC 39/39 ; STAC 53/53 ; NSBC 41/41 ; ECOC 42/42 ; BIIC 2/2 ; BOAS 43/43 ; BOAM 44/44 ; SCRC 45/45 ; TTLS 47/47 ; SIBC 49/49 ; SIVC 53/53 ; SEMC 54/54 ; BOABF 57/57 ; BOAB 59/59 ; BOAC 74/74.
- [x] total SHA calculés : **875 / 3 060** (**28,59 %**).
- [x] restant non hashé : **2 185 PDF**.
- [x] groupes exacts : **11**.
- [x] BOAB : **59 SHA uniques / 0 groupe exact**.
- [x] BOAC : **73 SHA uniques / 1 groupe exact**.
- [ ] prochain : **BOAN** après revérification live stricte.

### Doublons / versions

- [x] onze groupes exacts documentés dans `inventory/p1_duplicate_groups.csv`.
- [x] BOAC S1 2021 plain / `_2` : `EXACT_DUPLICATE`, SHA `7e69b8618e901a4bb72442989a23913f47f268b9093c0a380461d5626ede0c97`.
- [x] BOAC EF 2019 plain / `_2` : même taille 314 350 octets mais SHA différents, donc `NOT_EXACT_DUPLICATE`.
- [x] BOABF `divers_Etats_Financiers_BOABF.pdf` / `_2` : `EXACT_DUPLICATE`, SHA `cda4d28d932b4b1c715a83170279d312000cfce9e4f1b487597d3db1b3821979`.
- [x] SIBC T1 2017 plain / `_2` / `_3` : `EXACT_DUPLICATE`, SHA `3446b816e1a15b4a8d2df8bfeff775dbaa7166b52823c0d8d2bf8f1b06fc6b23`.
- [x] SIBC S1 2022 plain / `_2` : `EXACT_DUPLICATE`, SHA `b96ab01184f501d6f726250132108e742d8b5ede7ca862ce088b5aa29d7c88ec`.
- [x] SIVC : aucune duplication exacte parmi 53 sources ; variantes historiques `_2` à `_5` binaires distinctes.
- [x] SEMC : aucune duplication exacte parmi 54 sources ; variantes historiques `_2` à `_5` binaires distinctes.
- [x] BOAB : aucune duplication exacte parmi 59 sources.
- [x] SIVC T3 2025 : source explicitement `annule et remplace`, document rendu et confirmé T3 2025 ERIUM Côte d'Ivoire ; cible précédente absente du Drive courant.
- [ ] SIVC T3 2025 : retrouver la cible remplacée via P1-FRESH/BRVM puis renseigner `supersedes_source_file_id` sans supposition.
- [ ] relations sémantiques/version restantes hors verdict binaire.

### Identité / périodes / qualité

- [x] BOAC `divers_Rapport_S1_BOAC.pdf` = **S1 2022**, confirmé depuis le contenu.
- [x] BOAC `fiche_ci_0.pdf` = **information boursière S1 2017**, confirmé depuis le contenu.
- [x] BOAB : `avis_ndeg232...tpci_590_2021-2031...pdf` identifié comme publication du **Trésor Public de Côte d'Ivoire / TPCI 5,90 % 2021-2031**, donc anomalie d'attribution BOAB à préserver et corriger en aval sans supprimer la source.
- [x] BOABF paire `divers` : preuve visuelle **FY 2017**, exercice clos le 31/12/2017.
- [x] SIVC : continuité Air Liquide Côte d'Ivoire → ERIUM Côte d'Ivoire confirmée pour le symbole `SIVC` ; préserver l'historique des noms.
- [x] BOAS `divers_Rapport_S1_BOAS.pdf` = S1 2019, preuve visuelle.
- [x] SCRC `divers_Attestation_CAC_Annuel_SCRC.pdf` = attestation CAC S1 2017, preuve visuelle.
- [x] TTLS `divers_Rapport_CAC_Annuel_TTLS.pdf` = rapport général et rapports spéciaux CAC **FY 2020**, exercice clos le 31/12/2020, preuve texte native.
- [x] SEMC `divers_Attestation_CAC_Annuel_SEMC.pdf` = attestation CAC relative au rapport semestriel **S1 2020**, période 01/01/2020–30/06/2020, preuve visuelle.
- [x] règle renforcée : noms/dossiers ne dictent jamais la période ; le contenu source prévaut.
- [ ] périodes économiques fines pour l'ensemble du corpus.
- [ ] P1-FRESH / réconciliation BRVM et collecteur V2 pour les deltas distants.

## P1-R

Profils vérifiés : BICC 2022, BIIC T2 2025, ETIT 2023. Deep pilots : BOABF, CIEC, NTLC, SNTS.

## P2 → P8

Ne pas démarrer l'extraction RAW exhaustive avant couverture P1/P1-R suffisante.

## Prochaine action

`BOAN_LIVE_RECHECK_AND_SHA` puis `AGLC_LIVE_RECHECK_AND_SHA`, ensuite poursuite par taille croissante.
