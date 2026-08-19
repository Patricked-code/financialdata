# P1 SOURCE — Ecobank Transnational Incorporated / ETIT

Date : 2026-08-19
Statut : `P1_INVENTORIED / P1-R_PROFILED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE`

- Ticker : `ETIT`
- Dossier Drive canonique : `183KoqvNUQNaj6kdfw80PkkIGupbvuSia`
- Dossiers directs live : **23**, continus de `2003` à `2025`
- Snapshot avant recheck : **81 PDF**
- Recheck live strict parent-scoped : **100 PDF**
- Delta live : **+19**
- SOURCE global : **V21 = 3 133 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v21_20260818.md`

## Preuve de cardinal live

Le résultat global atteint le plafond de 100 du connecteur. Le cardinal a donc été recompté sur deux sous-périmètres disjoints des mêmes dossiers enfants :

- années `2003–2014` : **51 PDF** ;
- années `2015–2025` : **49 PDF** ;
- total live : **100 PDF**.

Le corpus contient des noms non normalisés ou portant des identités de filiales du groupe. Le périmètre reste défini par les dossiers SOURCE réels, jamais par une recherche ticker seule.

## SHA-256 / intégrité

- **100 / 100** objets matérialisés ;
- **100 / 100** signatures `%PDF-` valides ;
- tailles locales validées ;
- **100 SHA-256 uniques** ;
- **0 groupe de doublons binaires exacts ETIT** ;
- registre : `inventory/hashes/ETIT.csv` ;
- sérialisation registre : LF ;
- taille registre : **16 796 octets** ;
- SHA-256 du registre : `fdd32fb8839a9dc60f0cf5161b7926a45b3c0eefdb295bb88c10484526fb2d2d` ;
- Git blob local attendu : `908ac3c78239e14204ea21849775ed2eb75eb292` ;
- Git blob GitHub post-commit : `908ac3c78239e14204ea21849775ed2eb75eb292` ;
- validation bit-for-bit : **OK**.

Aucun objet SOURCE n'a été supprimé, fusionné ou renommé.

## Revue sémantique ciblée

- `2020_Rapport_S1_ETIT.pdf` et `2020_Rapport_S1_ETIT_2.pdf` : documents compagnons du même semestre, respectivement tableau d'activité et rapport d'examen limité ; pas des doublons, pas de `SUPERSEDES`.
- `2021_Rapport_S1_ETIT.pdf` et `2021_Rapport_S1_ETIT_2.pdf` : même logique de documents compagnons ; pas des doublons, pas de `SUPERSEDES`.
- `2021_Etats_Financiers_ETIT_2.pdf` publie des résultats 2021 **non audités** tandis que `2021_Etats_Financiers_ETIT.pdf` publie les résultats 2021 **audités**. Même exercice économique, publications distinctes conservées ; relation de famille/version possible, sans `SUPERSEDES` faute de preuve explicite d'annulation/remplacement.
- `2022_Rapport_T3_ETIT.pdf` et `_2` couvrent le même troisième trimestre mais présentent de petites différences chiffrées ; ils appartiennent à une même famille de publication, sont non exacts et restent tous deux SOURCE ; aucun `SUPERSEDES` n'est inféré.
- `2018_Etats_Financiers_ETIT.pdf` est une publication de résultats 2018 alors que `_2` contient les états financiers consolidés de l'exercice 2018 : même période, formes documentaires distinctes.
- `2018_Rapport_Annuel_ETIT_2.pdf` porte sur Ecobank Côte d'Ivoire alors que le rapport annuel plain porte sur le Groupe Ecobank : l'identité/scope interne prévaut sur le suffixe ; ces deux fichiers ne sont pas traités comme versions l'un de l'autre.

## P1-R — ETIT 2023

Document inspecté : `2023_Etats_Financiers_ETIT.pdf` (Drive ID `1F1SVX_IHyXZjaNrx2cJ5LVfwjE1eAGoj`).

Vérifications :

- 6 pages, PDF Excel natif ;
- états financiers **consolidés IFRS** ;
- compte de résultat et situation financière détaillés en **milliers de dollars US** ;
- page de synthèse publie simultanément **milliers USD** et **millions FCFA** ;
- variations publiées peuvent différer entre USD et FCFA ;
- résultat consolidé ventilé entre `part du Groupe`, `détenteurs autres capitaux propres` et `intérêts minoritaires`.

Conséquence de modélisation : `source_currency` reste au niveau du fact. Nouvelle dimension candidate documentée : `ownership_attribution_raw`. Aucune modification SQL pendant P1.

## Restant transversal

`SHA256 = COMPLETE` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.

## Prochaine action

Poursuivre le corpus réellement non hashé suivant après vérification des registres : **NTLC**.
