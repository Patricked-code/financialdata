# P1 — CHECKPOINT 48 ÉMETTEURS

Date : 2026-08-09
Statut : `INVENTORY_COMPLETE_48_OF_48 / TRANSVERSE_PASSES_OPEN`

## Résultat

Les **48 dossiers société** du corpus `RAPO / Rapport V2` ont désormais un inventaire P1 documenté dans `inventory/`.

Total des PDF recensés au niveau dossiers/fichiers : **2 950**.

Ce total ne signifie PAS que les 2 950 PDF ont déjà été extraits en RAW. Il clôt uniquement la passe d'inventaire dossiers/fichiers par émetteur.

## Comptes par émetteur

| # | Ticker | PDF |
|---:|---|---:|
| 1 | SIVC | 53 |
| 2 | BOABF | 57 |
| 3 | BOAB | 59 |
| 4 | BOAC | 60 |
| 5 | BOAM | 44 |
| 6 | BOAN | 60 |
| 7 | BOAS | 43 |
| 8 | BNBC | 78 |
| 9 | BICC | 61 |
| 10 | BIIC | 2 |
| 11 | AGLC | 60 |
| 12 | CFAC | 94 |
| 13 | CIEC | 61 |
| 14 | CBIBF | 8 |
| 15 | SEMC | 54 |
| 16 | ECOC | 32 |
| 17 | ETIT | 81 |
| 18 | FTSC | 88 |
| 19 | MVSC | 20 |
| 20 | NEIC | 86 |
| 21 | NTLC | 81 |
| 22 | NSBC | 38 |
| 23 | ONTBF | 91 |
| 24 | ORGT | 23 |
| 25 | ORAC | 14 |
| 26 | PALC | 75 |
| 27 | SAFC | 73 |
| 28 | SPHC | 124 |
| 29 | ABJC | 82 |
| 30 | STAC | 38 |
| 31 | SGBC | 87 |
| 32 | SIBC | 46 |
| 33 | CABC | 90 |
| 34 | SICC | 19 |
| 35 | STBC | 91 |
| 36 | SMBC | 106 |
| 37 | SDCC | 92 |
| 38 | SOGC | 106 |
| 39 | SLBC | 65 |
| 40 | SNTS | 101 |
| 41 | SCRC | 45 |
| 42 | TTLC | 101 |
| 43 | TTLS | 45 |
| 44 | PRSC | 68 |
| 45 | TRITRAF | 8 |
| 46 | UNLC | 20 |
| 47 | UNXC | 83 |
| 48 | SHEC | 37 |
|  | **TOTAL** | **2 950** |

## Règles de comptage appliquées

1. Les dossiers société sont ceux de la racine canonique Drive `Rapport V2`.
2. Un plafond de recherche à 100 résultats n'est jamais interprété comme un total SOURCE.
3. Lorsqu'une recherche ticker atteignait/plafonnait, le corpus a été recompté par groupes de dossiers parents.
4. Les résultats globaux hors dossier société ont été exclus du compte.
5. Les variantes `_2`, `_3`, `_rev`, etc. restent des documents SOURCE distincts tant que hash/contenu n'ont pas établi leur relation.
6. Les dossiers vides ou historiques courts restent des états SOURCE valides.
7. La présence physique d'un document sous un dossier société ne valide pas à elle seule son attribution à l'émetteur.

## Anomalies déjà identifiées à préserver

- SNTS 2017 contient un document nommé ONATEL : `issuer_assignment_status = REVIEW_REQUIRED` au futur manifeste.
- Plusieurs sociétés contiennent des fichiers `_rev` ou plusieurs états financiers pour la même année : `VERSION_REVIEW_REQUIRED`.
- Plusieurs dossiers `divers` contiennent des états financiers/CAC dont la période devra être résolue depuis le contenu.
- Certains corpus sont lacunaires ou très courts : ne jamais synthétiser les documents manquants.

## Ce qui reste ouvert dans P1

`INVENTORY_COMPLETE_48_OF_48` ne signifie pas `P1_COMPLETE`.

Passes transversales obligatoires :

1. manifeste machine-lisible document par document ;
2. SHA-256 de chaque fichier ;
3. doublons binaires et relations de versions/révisions ;
4. périodes économiques réelles depuis le contenu ;
5. attribution émetteur/document ;
6. couverture documentaire réelle ;
7. réconciliation avec le catalogue BRVM courant / P1-FRESH.

## Prochain état

`P1_TRANSVERSE → MACHINE_READABLE_MANIFEST → SHA256 → DUPLICATES/VERSIONS → ECONOMIC_PERIODS → ISSUER_ASSIGNMENT → FRESHNESS`
