# P1 SOURCE — Total Sénégal / TTLS

Date : 2026-08-11
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA256_COMPLETE / DIVERS_PERIOD_RESOLVED`

- Ticker : `TTLS`
- Dossier Drive : `1yX73IPdGDnVtDhfzTPCj3X8z7tK11WQ2`
- Dossiers directs : **11** = années `2016–2025` + `divers`
- Snapshot précédent : **45 PDF**
- Revérification live stricte par dossiers parents + MIME : **47 PDF**
- Delta live : **+2 PDF**
- Nouveau total projet V12 : **3 043 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v12_20260811.md`

## Particularités SOURCE

- 2016 comporte trois états financiers (`plain`, `_2`, `_3`) + rapport S1 ;
- 2017 comporte T1, bilan semestriel du contrat de liquidité, projet de publication des états financiers de synthèse 2017 et états financiers 2017 ;
- 2018 comporte S1, CAC annuel, états financiers et deux rapports annuels physiques ;
- 2021–2024 contiennent plusieurs familles et variantes financières ;
- 2024 compte **7 objets physiques** dans la revérification live ;
- 2025 contient T1/S1/T3.

## SHA-256

- **47 / 47 PDF matérialisés et hashés** ;
- **47 / 47 tailles Drive ↔ fichiers hashés validées** ;
- **46 SHA uniques** ;
- **1 groupe de doublon binaire exact** dans TTLS ;
- registre : `inventory/hashes/TTLS.csv`.

### Doublon exact TTLS

- `2018_Rapport_Annuel_TTLS.pdf` ;
- `2018_Rapport_Annuel_TTLS_2.pdf` ;
- 3 058 310 octets chacun ;
- SHA commun `46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237` ;
- groupe `SHA256:46b4ee85f5ad173c2de754c1054b0118b18e3a9758acec3db59cc56358275237`.

Les deux objets Drive restent conservés en SOURCE. Aucune suppression silencieuse.

### Variantes binaires distinctes

Les multiples états financiers 2016, 2021, 2022, 2023 et 2024 ont des tailles et/ou des SHA distincts. Aucun autre groupe exact n'a été trouvé dans les 47 fichiers.

## Résolution du fichier `divers`

`divers_Rapport_CAC_Annuel_TTLS.pdf` :

- Drive ID `1VZoogAwkgUD8qZw0TAEQUZdHLKpd3j6I` ;
- 2 407 682 octets ;
- SHA `5b2d8758401c37be78cd8e90191ac583e3f01f0215109129bacd632b9f8de4a2` ;
- 68 pages ;
- couche texte native exploitable ;
- titre : **« Rapport général et rapports spéciaux des commissaires aux comptes »** ;
- période explicitement publiée : **« Exercice clos le 31 décembre 2020 »** ;
- le rapport général précise : **« Etats financiers annuels - Exercice clos le 31 décembre 2020 »** ;
- période résolue : `FY_2020` ;
- type documentaire : rapport général et rapports spéciaux des commissaires aux comptes sur les états financiers annuels 2020.

Le dossier `divers` n'a donc aucune valeur pour déterminer la période économique ; le contenu du document prévaut.

## Règle

Les noms, dossiers et suffixes ne déterminent jamais seuls la période, le doublon ou la relation de version. Les objets physiques restent séparés jusqu'au verdict SHA/contenu.

## Restant transversal

`SHA256 = COMPLETE_47_OF_47` ; `DIVERS_PERIOD = RESOLVED_FY_2020` ; `VERSION_LINKS = CONTENT_REVIEW_REMAINING_FOR_BINARY_DISTINCT_VARIANTS` ; `ECONOMIC_PERIODS = PARTIAL` ; `REMOTE_FRESHNESS = RECHECKED_DELTA_PLUS_2`.
