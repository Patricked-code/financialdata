# DATA_MODEL — financialdata

Ce document décrit le modèle conceptuel cible. Il ne constitue pas encore une migration SQL définitive.

## 1. Principe

Le cœur du modèle doit être suffisamment générique pour absorber les différences sectorielles sans perdre la fidélité documentaire.

Une observation RAW est identifiée conceptuellement par :

`source + position + libellé publié + période + périmètre + unité + valeur`

## 2. Tables source et documents

### `issuers`
Référentiel des émetteurs.

### `securities`
Titres/instruments associés aux émetteurs.

### `issuer_names_history`
Candidate pour l'historique des dénominations légales/commerciales.

Champs conceptuels : `issuer_id`, `name_raw`, `name_type`, `valid_from`, `valid_to`, `source_document_id`.

### `source_folders`
Arborescences/document collections.

### `documents`
Métadonnées de chaque fichier/document.

### `source_versions`
Relations entre versions, révisions, remplacements et doublons.

### `document_pages`
Pages physiques/logiques.

### `document_sections`
Sections détectées : bilan, résultat, hors-bilan, activité, commentaire, audit, etc.

### `tables_raw`
Tables détectées dans les documents.

### `table_cells_raw`
Cellules brutes, avec géométrie si disponible.

## 3. Tables de faits RAW

### `financial_facts_raw`
Faits comptables/financiers publiés.

### `operating_facts_raw`
KPI opérationnels physiques ou métier.

Exemples : abonnés, tonnes, GWh, hectares, volumes, véhicules, transactions.

### `segment_facts_raw`
Faits ventilés par segment/activité lorsque la structure justifie une table dédiée.

### `contractual_facts_raw`
Faits liés aux concessions, contrats, périmètres gérés pour compte de tiers et autres droits/obligations contractuels.

### `corporate_facts_raw`
Capital, actionnariat, dividendes publiés, nombre d'actions, dirigeants, corporate actions, etc.

### `audit_facts_raw`
Opinion, type d'assurance, commissaires aux comptes, dates, réserves, observations et statuts.

### `text_disclosures_raw`
Commentaires, perspectives, risques, événements, définitions de KPI, explications de gestion et autres textes utiles.

### `event_facts_raw` — candidate
Événements datés/chiffrés : cession, augmentation de capital, changement de contrôle, arrêt de site, split, fusion, événement post-clôture, etc.

### `regulatory_facts_raw` — candidate
Ratios prudentiels, limites réglementaires, CET1, levier, solvabilité et autres normes publiées.

### `context_facts_raw` — à confirmer
Données de marché ou de contexte publiées dans le document d'un émetteur mais ne concernant pas directement l'émetteur.

### `esg_facts_raw` — à confirmer
Données ESG/HSE/impact structurées si le volume justifie une table spécialisée.

## 4. Extraction et qualité

### `extraction_runs`
Traçabilité de chaque exécution d'extraction.

### `extraction_issues`
Ambiguïtés, erreurs, incohérences ou besoins de revue.

## 5. Champs conceptuels communs aux faits

Selon le type de fait :

- `fact_id`
- `issuer_id`
- `security_id`
- `document_id`
- `page_id`
- `section_id`
- `table_id`
- `row_index`
- `column_index`
- `source_row_code`
- `source_label_raw`
- `source_parent_label_raw`
- `source_sub_label_raw`
- `source_column_label_raw`
- `period_start`
- `period_end`
- `period_label_raw`
- `period_type_raw`
- `period_basis`
- `comparative_period`
- `raw_value_text`
- `numeric_value`
- `source_currency`
- `source_unit_raw`
- `source_multiplier`
- `fact_origin`
- `value_nature`
- `fact_nature_raw`
- `geography_raw`
- `segment_raw`
- `activity_raw`
- `entity_scope_raw`
- `economic_scope_raw`
- `accounting_scope_raw`
- `consolidation_scope_raw`
- `subject_scope_raw`
- `reference_entity_raw`
- `reference_product_raw`
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
- `extraction_method`
- `confidence`
- `validation_status`
- `source_locator`
- `notes`

Tous ne doivent pas être présents dans chaque table ; l'implémentation physique sera décidée après validation du schéma v1.

## 6. Valeurs de nature

### `fact_origin`

- `PUBLISHED`
- `DERIVED`

Le RAW d'ingestion doit normalement être `PUBLISHED`.

### `value_nature`

Exemples :

- `STOCK`
- `FLOW`
- `RATE`
- `OTHER`

### `fact_nature_raw`

Exemples :

- `ACTUAL`
- `FORECAST`
- `GUIDANCE`
- `TARGET`

## 7. Périmètres comptables

Ne pas confondre :

- comptes individuels SYSCOHADA ;
- comptes individuels IFRS ;
- comptes consolidés IFRS ;
- données Groupe ;
- données filiale/pays ;
- actifs/passifs gérés pour compte de tiers ;
- données de marché externes citées dans un rapport.

## 8. Unités

Le modèle doit accepter notamment :

- XOF/FCFA ;
- milliers/millions/milliards ;
- % ;
- nombre ;
- tonnes ;
- kilotonnes ;
- hectares ;
- GWh ;
- Mo/Go ;
- transactions ;
- véhicules ;
- unités de produits ;
- USD/baril ;
- toute unité explicitement publiée.

La normalisation d'unité vient après conservation de l'unité source.

## 9. Contraintes conceptuelles

- pas d'écrasement silencieux ;
- pas de déduplication prématurée ;
- pas de mapping sémantique dans le RAW ;
- `NULL` si illisible ;
- une source peut publier plusieurs périodes ;
- un même fait économique peut exister dans plusieurs documents ;
- une valeur source incohérente reste conservée et reçoit une issue qualité.

## 10. Statut

Le modèle est **conceptuellement validé pour démarrer le schéma RAW v1**, mais les tables candidates doivent encore être confirmées pendant l'extraction exhaustive.
