# P1 SOURCE — NSIA Banque Côte d'Ivoire / NSBC

Date : 2026-08-10
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / VERSION_REVIEW_PARTIAL`

- Ticker : `NSBC`
- Dossier Drive : `1FzP9fR9x025gJw18qziXs2Dxusyv0vP1`
- Dossiers directs : **10** = années `2017` à `2025` + `divers`
- Premier inventaire de session : **38 PDF**
- État Drive live revérifié par parents + MIME : **41 PDF**
- Delta live : **+3 PDF**
- Répartition live : 2017=3 ; 2018=6 ; 2019=7 ; 2020=4 ; 2021=5 ; 2022=4 ; 2023=4 ; 2024=4 ; 2025=3 ; divers=1.
- Matérialisation brute Drive : **41 / 41 effectuée** pendant la passe du 2026-08-10.

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
- dates textuelles : 29 avril 2019 → 24 mai 2019.

Verdict sémantique : `CORRECTED_VERSION_OF / SUPERSEDES = VALIDATED`.

### États financiers 2021 — annulation et remplacement explicites

`2021_Etats_Financiers_NSBC_rev.pdf` contient : **« LE PRÉSENT COMMUNIQUÉ ANNULE ET REMPLACE LA PARUTION DU 04 AVRIL 2022 »**.

- résultat net 2021 : 20 998 → 23 713 M FCFA ;
- capitaux propres et ressources assimilées : 129 809 → 132 524 M FCFA ;
- dates textuelles observées : 1er avril 2022 dans la première publication ; 12 mai 2022 dans la publication de remplacement.

Verdict sémantique : `SUPERSEDES = VALIDATED`. La première publication reste conservée comme vérité point-in-time historique ; elle n'est jamais supprimée du RAW.

### États financiers 2019 — relation encore à qualifier

`2019_Etats_Financiers_NSBC.pdf` et `_2.pdf` sont deux objets physiques de tailles différentes (**1 325 452** vs **8 069 372 octets**) : ils ne peuvent donc pas être des doublons binaires exacts. Les deux fichiers n'exposent pas de texte natif exploitable via le connecteur ; la relation sémantique précise reste `VISUAL_REVIEW_REQUIRED`.

## Règle

Le total live est obtenu uniquement par les 10 dossiers parents et `mimeType = application/pdf`, sans filtre de nom. Un suffixe `_rev`/`_2` n'établit jamais à lui seul une relation. En revanche, les mentions source « Version corrigée » ou « annule et remplace » valident une relation de correction/supersession. Les deux versions et tous leurs facts restent conservés, avec lineage point-in-time.

## Hash / qualité binaire

Les **41 fichiers ont été téléchargés/matérialisés**, avec tailles Drive enregistrées pendant la passe. Le calcul SHA-256 local n'a pas encore pu être exécuté car le runtime de calcul de la session renvoie une erreur technique avant exécution. Aucun SHA ni verdict global de doublon NSBC n'est donc inventé.

## Gouvernance

Les cas T1 2019 et FY 2021 ont été ajoutés au document canonique Drive `BRVM_RAW_DATABASE — Gouvernance, architecture et observations conceptuelles` le 2026-08-10.

## Restant transversal

`DOCUMENT_MANIFEST_NSBC = PARTIAL_METADATA_READY` ; `SHA256_NSBC = BLOCKED_RUNTIME_NOT_COMPUTED` ; `VERSION_LINKS = 2_VALIDATED + 1_VISUAL_REVIEW_REQUIRED` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
