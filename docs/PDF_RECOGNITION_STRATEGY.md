# PDF RECOGNITION STRATEGY — reconnaissance des données pour création de bases

Date : 2026-08-09

Statut : `ACTIVE_DESIGN_DURING_P1`

## 1. Finalité

L'inventaire documentaire n'est pas une fin. Sa finalité est de permettre au projet de reconnaître automatiquement les structures et données publiées dans les PDF BRVM afin d'alimenter des bases de données structurées, traçables et sectoriellement neutres.

Le projet doit apprendre/reconnaître :

- type de document ;
- type d'état financier ;
- tableaux ;
- lignes et sous-lignes ;
- codes réglementaires/SYSCOHADA lorsqu'ils existent ;
- en-têtes de colonnes ;
- périodes ;
- comparatifs ;
- unités et multiplicateurs ;
- devises ;
- périmètres individuel/consolidé/concession/segment/géographie ;
- valeurs monétaires ;
- valeurs physiques ;
- ratios publiés ;
- faits opérationnels ;
- corporate actions ;
- audit/CAC ;
- événements ;
- commentaires/narratifs utiles.

## 2. Accélération de P1

P1 passe en mode `BATCH_FAST`.

Au lieu d'un traitement très détaillé émetteur par émetteur :

1. inventorier les métadonnées Drive par lots d'émetteurs ;
2. enregistrer rapidement dossiers, fichiers, IDs, tailles, types et anomalies ;
3. réserver les vérifications lourdes de hash/périodes à une passe transversale ;
4. sélectionner en parallèle des PDF représentatifs pour construire les profils de reconnaissance.

Les inventaires Markdown individuels restent utiles pour anomalies et résumé, mais ne doivent pas devenir le goulot d'étranglement du projet.

## 3. P1-R — Reconnaissance documentaire en parallèle

Nouvelle sous-phase autorisée pendant P1 : `P1-R PDF_RECOGNITION_DISCOVERY`.

Elle n'est pas encore l'extraction RAW exhaustive.

Pour chaque grand type d'émetteur/document, examiner un échantillon représentatif :

- rapport annuel ancien ;
- rapport annuel récent ;
- états financiers détaillés récents ;
- publication T1/T3/S1/S2 ;
- rapport/attestation CAC ;
- document `divers` ou atypique ;
- version révisée/annule-remplace lorsqu'elle existe.

Objectif : reconnaître les structures récurrentes et exceptions nécessaires au futur moteur d'extraction.

## 4. Profil de document

Chaque famille de PDF peut être décrite par un `document_profile` comprenant :

- `document_type`
- `issuer_sector`
- `accounting_framework_raw`
- `statement_type`
- `page_patterns`
- `section_markers`
- `table_markers`
- `header_patterns`
- `row_code_patterns`
- `period_header_patterns`
- `unit_patterns`
- `currency_patterns`
- `scope_patterns`
- `value_formats`
- `negative_value_patterns`
- `percentage_patterns`
- `note_reference_patterns`
- `audit_markers`
- `corporate_action_markers`
- `operating_metric_patterns`
- `known_exceptions`

Ces profils sont des aides à reconnaissance. Ils ne remplacent jamais la conservation du texte/source original.

## 5. Chaîne de reconnaissance cible

`PDF`
→ `DOCUMENT CLASSIFICATION`
→ `PAGE/SECTION CLASSIFICATION`
→ `TABLE DETECTION`
→ `TABLE GEOMETRY / CELLS`
→ `ROW/COLUMN INTERPRETATION`
→ `PERIOD / UNIT / CURRENCY / SCOPE RESOLUTION`
→ `FACT CANDIDATES`
→ `VALIDATION`
→ `RAW DATABASE`

## 6. Familles de données à reconnaître

### Comptables/financières

- bilan / situation financière ;
- compte de résultat ;
- TAFIRE ;
- tableau de flux ;
- variation des capitaux propres ;
- hors bilan ;
- affectation du résultat ;
- dividendes ;
- notes financières chiffrées.

### Opérationnelles

Exemples déjà observés :

- abonnés, clients, lignes, 4G, fibre, Orange Money ;
- GWh/MWh, branchements, raccordements ;
- tonnes/kilotonnes ;
- hectares, campagnes agricoles ;
- véhicules, marques, parts de marché ;
- tonnage manutention/transit ;
- projets/chantiers ;
- production/ventes physiques ;
- prix moyens.

### Corporate / gouvernance / audit

- actionnariat ;
- capital ;
- nombre d'actions ;
- AG ;
- dates de décisions ;
- changements de nom/contrôle ;
- augmentation de capital ;
- fusion/cession ;
- opinion CAC ;
- examen limité ;
- attestation ;
- événements exceptionnels.

### Réglementaires

- ratios prudentiels ;
- CET1 ;
- levier ;
- limites réglementaires ;
- données de concession/contrat public ;
- autres indicateurs explicitement publiés.

## 7. Règle de reconnaissance

Le moteur peut proposer une interprétation, mais RAW doit toujours conserver :

- `source_label_raw` ;
- `raw_value_text` ;
- source/document/page/table/cellule ;
- en-tête source ;
- période brute ;
- unité brute ;
- scope brut ;
- méthode de reconnaissance ;
- confiance ;
- statut de validation.

Une reconnaissance incertaine reste `REVIEW_REQUIRED`.

## 8. Reconnaissance des nombres

Le parseur devra gérer au minimum :

- espaces et espaces insécables ;
- séparateurs de milliers ;
- virgule/point décimal ;
- parenthèses négatives ;
- signe moins ;
- pourcentages ;
- valeurs en milliers/millions/milliards ;
- FCFA/XOF et autres devises ;
- unités physiques ;
- `N/A`, tirets, blancs et valeurs non applicables.

Toujours conserver le texte brut en parallèle de la valeur numérique parsée.

## 9. Reconnaissance des périodes

Ne jamais se contenter du dossier/nom de fichier.

Reconnaître dans le PDF :

- date de clôture ;
- T1/T2/T3/T4 ;
- S1/S2 ;
- 9 mois ;
- annuel ;
- comparatifs N-1 ;
- exercices antérieurs ;
- périodes de campagne ;
- dates de stock vs périodes de flux.

## 10. Reconnaissance des scopes

Le futur moteur doit pouvoir distinguer notamment :

- individuel vs consolidé ;
- société vs groupe ;
- opérations propres vs opérations pour compte de tiers/concession ;
- pays/géographie ;
- segment d'activité ;
- produit/marque ;
- marché externe vs émetteur ;
- actuel vs forecast/guidance/target.

## 11. Stratégie de généralisation

Ne pas créer un parseur différent pour chacune des 48 sociétés.

Construire :

1. règles universelles ;
2. profils par famille de document ;
3. extensions sectorielles ;
4. exceptions documentées ;
5. mécanisme de confiance/revue.

## 12. Relation avec P2/P3

P1-R permet de découvrir les patterns et de préparer le modèle.

P2 figera le schéma RAW à partir de ces observations.

P3 appliquera ensuite la reconnaissance/extraction de façon exhaustive à tous les documents validés.

Ainsi, reconnaître des patterns pendant P1 n'est pas une violation de `SOURCE before RAW` : on apprend la structure sans prétendre avoir encore extrait exhaustivement toute la base.

## 13. Objectif de vitesse

Le projet doit privilégier :

- traitement par lots ;
- reconnaissance réutilisable ;
- registres machine-lisibles ;
- automatisation des tâches répétitives ;
- revue humaine uniquement sur ambiguïtés/anomalies.

Le Markdown documente les décisions et anomalies ; il ne doit pas remplacer les futurs manifestes et bases machine-lisibles.
