# P1-R PROFILE — BICC 2022 — États financiers bancaires

Source : `bilan_et_compte_de_resultat_bicici_31_12_2022_.pdf`
Drive ID : `1Ro2XM1WHUSc2knXYrqe5GU66tXVqMABr`
Date d'inspection : 2026-08-09
Statut : `VISUALLY_VERIFIED / NATIVE_TEXT`

## Structure observée

PDF natif issu d'Excel, 1 page A4.

Titre visible : `ETATS FINANCIERS AU 31 DECEMBRE 2022`.

Blocs logiques :

1. `I- BILAN ET HORS BILAN AU 31 DECEMBRE 2022`
   - ACTIF à gauche ;
   - PASSIF à droite ;
   - deux colonnes comparatives `31/12/2021` et `31/12/2022` ;
   - unité publiée : `En Millions de FCFA` ;
   - sous-bloc HORS BILAN avec `ENGAGEMENTS DONNES` et `ENGAGEMENTS RECUS`.
2. `II- COMPTE DE RESULTAT AU 31 DECEMBRE 2022`
   - deux colonnes comparatives 2021/2022 ;
   - unité : millions de FCFA ;
   - lignes détaillées et agrégats intermédiaires.
3. Note de bas de page : date d'arrêté des comptes et référence au rapport des Commissaires aux Comptes.

## Patterns de reconnaissance

### Tableau côte à côte

Le moteur doit savoir qu'une même zone horizontale peut contenir deux sous-tableaux sémantiques indépendants : `ACTIF` et `PASSIF`.

Ne pas aplatir une ligne ACTIF avec la ligne PASSIF située visuellement sur la même hauteur.

### Périodes répétées

Le header `Montant au 31/12/2021` / `Montant au 31/12/2022` est répété pour plusieurs sous-tableaux. La période doit être rattachée à chaque cellule/fait.

### Unité héritée

`En Millions de FCFA` apparaît dans le header de tableau et s'applique aux valeurs du bloc. Conserver :

- `source_unit_raw = Millions de FCFA`
- `source_multiplier = 1000000`
- `currency = XOF/FCFA` après résolution contrôlée.

### Hiérarchie / agrégats

Exemples visibles :

- `CAPITAUX PROPRES ET RESSOURCES`
- `TOTAL ACTIF`
- `TOTAL PASSIF`
- `ENGAGEMENTS DONNES`
- `ENGAGEMENTS RECUS`
- `PRODUIT NET BANCAIRE`
- `RESULTAT BRUT D'EXPLOITATION`
- `RESULTAT D'EXPLOITATION`
- `RESULTAT AVANT IMPOT`
- `RESULTAT NET`

Le moteur doit conserver le libellé source et permettre une relation parent/agrégat sans calculer ni remplacer la valeur publiée.

## Types de faits candidats

- `financial_facts_raw` : bilan et compte de résultat ;
- `financial_facts_raw` ou domaine dédié : hors-bilan/engagements ;
- `audit_facts_raw` / `corporate_facts_raw` : note sur arrêté des comptes et CAC selon règle finale.

## Règles confirmées

- les tableaux bancaires peuvent être côte à côte ;
- la géométrie de table est nécessaire, le texte seul ne suffit pas toujours à préserver la sémantique ;
- les comparatifs N-1 doivent produire des observations RAW distinctes ;
- les agrégats publiés restent des faits `PUBLISHED`, même s'ils pourraient être recalculés ;
- la note documentaire de bas de page fait partie de la provenance et peut contenir des dates/statuts utiles.
