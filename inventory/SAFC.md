# P1 SOURCE — SAFCA Côte d'Ivoire / SAFC

Date : 2026-08-17
Statut : `FILE_INVENTORIED / LIVE_RECHECKED_NO_DELTA / SHA256_COMPLETE / VERSION_REVIEW`

- Ticker : `SAFC`
- Dossier Drive canonique : `1UhiUIVuMBHzRSt6jikV22wJoytCZk2j_`
- Dossiers directs : **27**
- Couverture observée : `1998–2014`, puis `2016–2025`; **2015 absent**
- Snapshot manifeste avant recheck : **73 PDF**
- Recheck live strict par les **27 parent IDs réels** + `mimeType='application/pdf'` : **73 PDF**
- Delta live : **0**
- SOURCE global : **V18 = 3 077 PDF** ; aucun checkpoint supplémentaire requis pour SAFC.

## Résultat SHA-256

- **73/73** objets matérialisés ;
- **73/73** signatures `%PDF-` valides ;
- tailles locales validées contre les tailles Drive lors de la matérialisation ;
- **72 SHA-256 uniques** ;
- **1 groupe de doublon exact** ;
- registre : `inventory/hashes/SAFC.csv` ;
- blob GitHub final du registre : `4d68e2f99a3d8a90fe70ecf858c7064924f27dd3`, identique au blob calculé localement avant écriture.

### Groupe exact SAFC

Les deux objets suivants ont exactement **1 475 293 octets** et le même SHA-256 `85f0a68ee4e126d93fcb09dafbf644e24b61454d428974787391c6f5cde8884c` :

- `2007_Rapport_Annuel_SAFC.pdf` — Drive `1yiuRPP_1xjt3Uf6kXuQW0qsCbycnAQAE` ;
- `2007_Rapport_Annuel_SAFC_3.pdf` — Drive `17r4c57N8NDTcfcksxDmRcXSOJicEXlrp`.

Relation : `EXACT_DUPLICATE`. Les deux objets physiques restent conservés ; aucune suppression silencieuse.

## Particularités SOURCE vérifiées

- historique long, nombreux rapports annuels et collisions de noms `_2/_3/_4/_5` ;
- hors groupe 2007 prouvé par SHA, aucun suffixe n'est interprété comme doublon ;
- périodes `T4` réellement présentes (2021, 2022 et 2024) ;
- périodes `T2` réellement présentes (2023 et 2025) ;
- 2020 contient deux fichiers d'états financiers physiquement distincts ;
- CAC/attestations et états financiers présents selon les années ;
- 2024 comporte T4, CAC annuel et rapport annuel ; 2025 comporte T1 et T2 ;
- le recheck parent-scoped retrouve aussi des noms génériques, notamment `rapport_dactivites_-_4ieme_trimestre_2022_-_alios_finance_safca_ci.pdf` et `rapport_dactivites_-_4e_trimestre_2024_-_safca_ci.pdf` : le périmètre SOURCE est défini par l'arborescence canonique, pas par une recherche de chaîne `SAFC`.

## Règle

T1/T2/T3/T4/S1/S2 font partie des périodes documentaires reconnues. L'absence du dossier 2015 reste une lacune SOURCE, jamais une invitation à reconstruire des documents. Les relations de version non exactes restent à qualifier par contenu ; aucun `SUPERSEDES` n'est déduit d'un suffixe ou d'un nom seul.

## Point de reprise

SAFC est fermé pour la passe binaire. Prochain corpus : **PALC** — recheck live strict avant tout SHA.

## Restant transversal

`SHA256 = COMPLETE` ; `VERSION_LINKS = PARTIAL` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
