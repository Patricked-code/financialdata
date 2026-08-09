# ARCHITECTURE — financialdata

## 1. Architecture générale

Le projet suit une architecture en couches strictement séparées :

```text
0 SOURCE
  ↓
1 RAW
  ↓
2 MAPPED
  ↓
3 CANONICAL
  ↓
4 DERIVED
  ↓
5 ANALYTICS
```

Deux systèmes traversent toutes les couches :

- `LINEAGE / VERSIONING`
- `DATA QUALITY`

## 2. SOURCE

Contient ou référence les fichiers originaux : PDF, XLS/XLSX, CSV, pages officielles, documents Drive, etc.

Attributs essentiels :

- source provider ;
- identifiant externe ;
- URL/chemin ;
- nom de fichier ;
- MIME/type ;
- taille ;
- hash ;
- dates ;
- société/dossier de rattachement ;
- statut de version/doublon.

La source originale n'est jamais modifiée.

## 3. RAW

Représentation fidèle des publications.

Le RAW est :

- granulaire ;
- traçable ;
- immuable/versionné ;
- sectoriellement neutre ;
- non normalisé sémantiquement ;
- capable d'héberger données financières, opérationnelles, réglementaires, contractuelles, corporate, audit et disclosures textuels.

Exemple :

```text
source_label_raw = CREANCES SUR LA CLIENTELE
raw_value_text   = 95 363 599 043
numeric_value    = 95363599043
source_currency  = XOF
source_unit_raw  = FCFA
period_end       = 2009-12-31
fact_origin      = PUBLISHED
```

## 4. MAPPED

Interprétation contrôlée du RAW vers des concepts métier.

Exemple :

```text
CREANCES SUR LA CLIENTELE
→ CUSTOMER_LOANS
```

Le mapping ajoute une interprétation ; il ne remplace pas le RAW.

## 5. CANONICAL

Harmonisation multi-émetteurs et multi-périodes :

- métrique canonique ;
- société/titre ;
- période ;
- devise ;
- unité ;
- standard comptable ;
- périmètre ;
- géographie ;
- segment ;
- autres dimensions validées.

La couche canonique doit rester reliée aux observations RAW sources.

## 6. DERIVED

Valeurs reconstruites/calculées :

- croissance ;
- trimestre autonome ;
- TTM ;
- CAGR ;
- marges ;
- ratios recalculés ;
- agrégations ;
- conversions éventuelles.

Chaque résultat dérivé doit stocker :

- formule ;
- version de formule ;
- identifiants des inputs ;
- date de calcul ;
- méthode ;
- statut qualité.

## 7. ANALYTICS

Usages finaux :

- ratios ;
- scores ;
- comparables ;
- valorisations ;
- screeners ;
- classements ;
- alertes ;
- analyses statistiques ;
- analyses IA.

Cette couche ne doit jamais devenir une source de vérité rétroactive pour le RAW.

## 8. Lineage et versioning

Toute donnée doit permettre de remonter vers :

`analytics/derived → canonical → mapped → raw → document → source originale`

Cas à gérer :

- doublon exact ;
- révision ;
- remplacement ;
- restatement ;
- correction d'extraction ;
- source publiée plusieurs fois ;
- même valeur dans plusieurs documents.

## 9. Data quality

Les contrôles doivent produire des statuts et issues sans modifier arbitrairement les données sources.

Exemples :

- bilan déséquilibré dans la publication ;
- total incohérent ;
- variation publiée incohérente ;
- unité ambiguë ;
- cellule illisible ;
- période incertaine ;
- périmètre non résolu ;
- doublon probable ;
- document scanné nécessitant inspection.

## 10. Dimensions transversales

Selon le document, une observation peut porter :

- `geography_raw`
- `segment_raw`
- `activity_raw`
- `entity_scope_raw`
- `economic_scope_raw`
- `accounting_scope_raw`
- `consolidation_scope_raw`
- `subject_scope_raw`
- `reference_entity_raw`
- `product_raw`
- `brand_raw`
- `project_raw`
- `contract_raw`
- `campaign_label_raw`
- `season_raw`
- `site_raw`
- `crop_raw`
- `maturity_stage_raw`
- `movement_type_raw`
- `value_nature`
- `fact_nature_raw`

Ces dimensions sont optionnelles et ne doivent pas être forcées lorsqu'elles ne sont pas publiées.

## 11. Flux de travail documentaire

Pour chaque société :

1. inventaire des dossiers et documents ;
2. détection versions/doublons ;
3. lecture d'anciens et récents formats ;
4. classification des familles documentaires ;
5. extraction ;
6. validation ;
7. enregistrement des issues ;
8. mise à jour de `SUIVI.md` ;
9. documentation des nouvelles particularités ;
10. seulement ensuite extension éventuelle du schéma.

## 12. Règle Git de l'architecture

Cette architecture et ses migrations sont développées directement sur `main`. **Aucune branche ne doit être créée.**
