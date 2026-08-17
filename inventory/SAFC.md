# P1 SOURCE — SAFCA Côte d'Ivoire / SAFC

Date : 2026-08-17
Statut : `FILE_INVENTORIED / LIVE_RECHECKED_NO_DELTA / HASH_PENDING / VERSION_REVIEW`

- Ticker : `SAFC`
- Dossier Drive canonique : `1UhiUIVuMBHzRSt6jikV22wJoytCZk2j_`
- Dossiers directs : **27**
- Couverture observée : `1998–2014`, puis `2016–2025`; **2015 absent**
- Snapshot manifeste avant recheck : **73 PDF**
- Recheck live strict par les **27 parent IDs réels** + `mimeType='application/pdf'` : **73 PDF**
- Delta live : **0**
- SOURCE global : **reste V18 = 3 077 PDF** ; aucun checkpoint supplémentaire n'est requis pour SAFC avant SHA.

## Particularités SOURCE vérifiées au recheck 2026-08-17

- historique long, nombreux rapports annuels et collisions de noms `_2/_3/_4/_5` ;
- les suffixes ne sont jamais interprétés comme doublons ou versions sans preuve SHA/contenu ;
- périodes `T4` réellement présentes (2021 et 2024) ;
- périodes `T2` réellement présentes (2023 et 2025) ;
- 2020 contient deux fichiers d'états financiers distinctement nommés ;
- CAC/attestations et états financiers présents selon les années ;
- 2024 comporte T4, CAC annuel et rapport annuel ; 2025 comporte T1 et T2 ;
- le recheck parent-scoped retrouve aussi des fichiers dont le nom n'est pas limité au ticker, notamment `rapport_dactivites_-_4ieme_trimestre_2022_-_alios_finance_safca_ci.pdf` et `rapport_dactivites_-_4e_trimestre_2024_-_safca_ci.pdf` : le périmètre SOURCE est donc défini par l'arborescence canonique, pas par une recherche de chaîne `SAFC`.

## Règle

T1/T2/T3/T4/S1/S2 font partie des périodes documentaires reconnues. L'absence du dossier 2015 reste une lacune SOURCE, jamais une invitation à reconstruire des documents. Les 73 objets physiques restent tous conservés jusqu'au verdict SHA et à la revue de versions.

## Passe suivante exacte

1. matérialiser les **73/73 PDF** de la liste parent-scoped ;
2. valider taille locale et signature `%PDF-` ;
3. calculer SHA-256 sur 100 % ;
4. identifier les groupes exacts sans supprimer aucun objet ;
5. revoir les familles de versions/collisions de noms par contenu ;
6. créer `inventory/hashes/SAFC.csv` et le valider post-commit contre le blob GitHub ;
7. finaliser ce fichier, le manifeste, `SUIVI.md` et `TODO.md` ;
8. passer ensuite à `PALC`.

## Restant transversal

`SHA256 = IN_PROGRESS` ; `VERSION_LINKS = IN_PROGRESS` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = NOT_COMPLETE`.
