# P1-R PROFILE — ETIT 2023 états financiers consolidés

Date : 2026-08-09
Statut : `VERIFIED_ON_RENDERED_PDF`

## Source

- Émetteur : Ecobank Transnational Incorporated
- Ticker : `ETIT`
- Document : `2023_Etats_Financiers_ETIT.pdf`
- Drive ID : `1F1SVX_IHyXZjaNrx2cJ5LVfwjE1eAGoj`
- Pages : 6
- Générateur PDF : Microsoft Excel / Microsoft 365
- Texte natif : oui

## Classification vérifiée

- `document_type = FINANCIAL_STATEMENTS_AND_RESULTS_RELEASE`
- `accounting_framework_raw = IFRS`
- `consolidation_scope_raw = CONSOLIDATED`
- `period_end = 2023-12-31`
- comparatif : exercice 2022

## Patterns de reconnaissance

### Page de synthèse bi-devise

Le tableau `Chiffres Clés` publie chaque métrique avec :

- 2023 en milliers USD ;
- 2023 en millions FCFA ;
- 2022 en milliers USD ;
- 2022 en millions FCFA ;
- variation USD ;
- variation FCFA.

Règle : chaque couple métrique × période × devise/unité est une observation publiée distincte. Les variations USD et FCFA sont également deux observations `PUBLISHED` distinctes et ne doivent pas être remplacées par un recalcul unique.

### États détaillés

Compte de résultat consolidé et état consolidé de la situation financière en `milliers de Dollars EU`, comparatifs 2023/2022. Valeurs négatives représentées par parenthèses.

### Attribution du résultat

Le résultat net consolidé est décomposé en :

- résultat net, part du Groupe ;
- détenteurs autres capitaux propres ;
- intérêts minoritaires.

Règle candidate : conserver `ownership_attribution_raw` ou une dimension équivalente. Ne pas attribuer automatiquement l'intégralité du résultat consolidé aux actionnaires du Groupe.

### Résultat par action

Le document publie résultat de base et dilué par action, exprimés en cents USD ; ce sont des facts `PUBLISHED`.

## Particularités de reconnaissance

- `source_currency` doit être au niveau du fact ;
- `source_unit_raw` et `source_multiplier` sont indispensables ;
- `consolidation_scope_raw` et `accounting_framework_raw` sont explicitement déterminables ;
- la page narrative peut republier des montants arrondis en milliards USD/FCFA : conserver séparément avant réconciliation ;
- `ownership_attribution_raw` est documenté comme candidat, non implémenté SQL à ce stade.

## Contrôles futurs P3/P4

- cohérence Total actif = Total passif et capitaux propres ;
- somme des composantes d'attribution vs résultat consolidé, uniquement comme contrôle, jamais comme correction silencieuse ;
- relations de conversion USD/FCFA observables mais aucune conversion interne ne remplace les valeurs publiées ;
- conservation de la provenance page/table/cellule.
