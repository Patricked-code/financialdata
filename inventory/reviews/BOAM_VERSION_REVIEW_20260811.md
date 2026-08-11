# BOAM — revue binaire et de version SOURCE

Date : 2026-08-11
Émetteur : Bank of Africa Mali (`BOAM`)
Statut : `BINARY_REVIEW_COMPLETE / EXPLICIT_REV_PREDECESSOR_NOT_FOUND`

## Règle appliquée

Chaque objet Drive reste conservé. Les suffixes `_2`, `_3`, `_4` et `_rev` ne sont jamais interprétés seuls comme doublon ou supersession.

## Résultat binaire global

- 44 / 44 PDF matérialisés ;
- 44 / 44 tailles Drive ↔ fichiers locaux validées ;
- 42 SHA uniques ;
- 2 groupes de doublons binaires exacts.

## Collisions de taille examinées

### T3 / T4 2019

- `2019_Rapport_T4_BOAM.pdf` — 86 241 octets — SHA `876b172e6f5b64288b62e708332d4b78eab17dd0356d75eec339d18283ac1561` ;
- `2019_Rapport_T3_BOAM.pdf` — 86 241 octets — SHA `1b1ebde09b0571420296e1cbfab6522b8bcba3ef0dc16102c2a1f6a164a05724` ;
- verdict : même taille mais `BINARY_DISTINCT`.

### EF / rapport CAC annuel 2023

- `2023_Etats_Financiers_BOAM.pdf` ;
- `2023_Rapport_CAC_Annuel_BOAM.pdf` ;
- 824 078 octets chacun ;
- SHA commun `77f20998d8b1def30299a400bbe4584093fb54a6e40d05f7ab5fa7721896e31e` ;
- verdict : `EXACT_DUPLICATE`. Les deux objets physiques sont conservés et reliés.

### Rapports CAC annuels 2024 plain / `_2`

- 742 080 octets chacun ;
- SHA commun `dc403fad3b516f6a94eecefafb56db518987c5fb3097edd0d68a7ffe8077f207` ;
- verdict : `EXACT_DUPLICATE`. Les deux objets physiques sont conservés et reliés.

## `2021_Etats_Financiers_BOAM_rev.pdf`

- 946 214 octets ;
- SHA `ab2c020c621d63911d9611d22507931a617b72ac5fdcc0d32dfcd9d00d8c1a82` ;
- PDF image de 4 pages ;
- revue visuelle : états financiers BOA Mali au 30/06/2021 avec comparatifs, certifiés/signés par commissaires aux comptes ;
- aucune mention visible `annule et remplace`, `corrigé`, `révision` ou équivalent n'a été trouvée ;
- recherche Drive globale ciblée `2021 Etats Financiers BOAM` : aucun prédécesseur BOAM 2021 distinct retrouvé ;
- verdict : `PREDECESSOR_NOT_FOUND / NO_SUPERSESSION_PROVEN` ;
- la terminaison `_rev` reste une propriété du nom historique, pas une preuve suffisante de relation de version.

## Variantes historiques 2011 / 2012

Les variantes 2011 `_2/_3/_4` et 2012 `_2/_3` ont des tailles et des SHA distincts. Elles restent toutes des objets SOURCE indépendants ; aucune relation sémantique n'est inférée sans revue documentaire dédiée.
