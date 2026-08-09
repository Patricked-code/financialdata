# P1-R PROFILE — BIIC — Rapport d'activité T2 2025

Source : `2025_Rapport_T2_BIIC.pdf`
Drive ID : `1FVWVJUyuixp-AmhsUMp4flMfQE9APELs`
Date d'inspection : 2026-08-09
Statut : `VISUALLY_VERIFIED / NATIVE_TEXT / METADATA_MISMATCH`

## Identité visible du document

Titre visible : `RAPPORT D’ACTIVITÉ AU DEUXIEME TRIMESTRE 2025`.

Le contenu et le logo identifient BIIC — Banque Internationale pour l’Industrie et le Commerce.

## Anomalie de métadonnées PDF

Le champ `Title` interne du PDF observé par `pdfinfo` mentionne un fichier relatif à `Société Générale CI` et au `3ème trimestre 2025`, alors que le contenu visible est BIIC T2 2025.

Règle :

- conserver les métadonnées PDF brutes ;
- ne jamais les utiliser seules pour attribuer l'émetteur, le type ou la période ;
- comparer métadonnées, nom source et contenu visible ;
- en cas de contradiction : `DOCUMENT_METADATA_MISMATCH / REVIEW_REQUIRED` ;
- l'identité documentaire validée doit reposer sur la preuve visible/contextuelle, sans supprimer la métadonnée erronée.

## Structure observée

2 pages.

### Page 1 — Tableau d'activités et de résultats

Deux sous-tableaux :

- `Indicateurs de bilan` ;
- `Indicateurs de compte de résultat`.

Unité : `Données financières (en millions de FCFA)`.

Colonnes :

- `juin-25`
- `déc.-24`
- `juin-24`
- `Variation / Valeur`
- `Variation / %`

Exemples de lignes :

- Crédits nets à la clientèle ;
- Dépôts de la clientèle ;
- Titres ;
- Total Bilan ;
- Produit Net Bancaire (PNB) ;
- Frais généraux ;
- Résultat brut d'exploitation ;
- Coût Net du Risque ;
- Résultat avant impôts ;
- Résultat Net.

### Page 2 — Narratif

Sections :

- `COMMENTAIRE DE LA DIRECTION SUR L’ACTIVITE` ;
- `Indicateurs de résultat` ;
- `Indicateurs de bilan` ;
- `PERSPECTIVES 2025`.

Le narratif republie certaines valeurs sous une autre unité/arrondi, par exemple en milliards de FCFA, alors que le tableau est en millions de FCFA.

## Patterns de reconnaissance confirmés

### T2 est une période documentaire réelle

Le contenu visible confirme explicitement le deuxième trimestre 2025. Le classifieur de périodes doit reconnaître `T2`, pas seulement T1/T3/S1/S2.

### Une même colonne peut avoir des natures économiques différentes selon le sous-tableau

Dans `Indicateurs de bilan`, une date telle que `juin-25` désigne un stock à date.

Dans `Indicateurs de compte de résultat`, `juin-25` représente une performance cumulée sur une période se terminant en juin.

Donc `period_label_raw` seul ne suffit pas : il faut aussi `value_nature_raw` / type d'état / contexte de table.

### Variations publiées

`Variation Valeur` et `Variation %` sont explicitement publiées. Elles peuvent être conservées en RAW comme observations `PUBLISHED`, même si elles sont mathématiquement recalculables plus tard.

### Table + narratif = observations documentaires distinctes

Une même réalité peut être publiée :

- dans le tableau en millions ;
- dans le commentaire en milliards avec arrondi ;
- avec un pourcentage narratif.

Ne pas fusionner silencieusement ces représentations dans RAW. Les relier plus tard si nécessaire.

### Perspectives

La section `PERSPECTIVES 2025` est narrative/future-looking et doit rester distincte des résultats réalisés (`ACTUAL` vs `FORECAST/GUIDANCE/TARGET` lorsque applicable).

## Types de faits candidats

- `financial_facts_raw` : indicateurs de bilan/résultat ;
- `text_disclosures_raw` : commentaires de direction et perspectives ;
- faits variation publiés : `financial_facts_raw` avec nature/measure explicite ou représentation adaptée dans le schéma final.
