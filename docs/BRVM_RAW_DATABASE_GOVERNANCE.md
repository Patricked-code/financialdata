# BRVM RAW DATABASE — Gouvernance et observations conceptuelles

Date de consolidation initiale GitHub : 2026-08-09  
Statut : **DOCUMENT CANONIQUE DE CONCEPTION**

Ce document migre dans `financialdata` les règles et observations conceptuelles construites pendant l'exploration du corpus BRVM `RAPO / Rapport V2`.

Il complète `GOVERNANCE.md`, qui reste prioritaire pour les règles de dépôt et de travail.

## 1. Principe général

Toute nouvelle particularité observée dans un document doit être documentée avant de provoquer une évolution du schéma.

Journal logique :

`date + société + ticker + document + période + observation + preuve + risque + impact RAW + règle adoptée + statut`

Statuts :

- `OBSERVED`
- `VALIDATED`
- `IMPLEMENTED`
- `REVIEW_REQUIRED`

## 2. Architecture

`SOURCE → RAW → MAPPED → CANONICAL → DERIVED → ANALYTICS`

Systèmes transversaux :

- lineage/versioning ;
- data quality.

## 3. Principes RAW non négociables

### 3.1 Une observation publiée = une ligne RAW

Une ligne contenant deux périodes produit deux observations.

### 3.2 Valeur originale + machine

Toujours conserver :

```text
raw_value_text = "95 363 599 043"
numeric_value  = 95363599043
```

### 3.3 Unités d'origine

Conserver l'unité et le multiplicateur avant normalisation : FCFA, milliers, millions, GWh, tonnes, hectares, %, nombre, transactions, $/baril, etc.

### 3.4 Comparatifs

Toutes les colonnes comparatives publiées sont des observations : N, N-1, FY précédent, T1 précédent, S1 précédent, etc.

### 3.5 Période économique

Le millésime du dossier/fichier ne détermine pas la période. Lire le contenu.

### 3.6 Doublons

Les doublons documentaires ne sont pas fusionnés en RAW.

### 3.7 Versions

Les fichiers `_rev`, corrigés ou remplacés sont historisés.

### 3.8 Illisible

Une cellule illisible n'est jamais inventée : `numeric_value = NULL`, `validation_status = REVIEW_REQUIRED`.

### 3.9 Ratios publiés

ROA, ROE, PER, P/B, variation %, rendement ou autre ratio explicitement publié reste `PUBLISHED`.

### 3.10 Texte

Commentaires de gestion, perspectives, risques, gouvernance, contrats, certifications et événements sont conservés.

### 3.11 Géométrie

Prévoir table/ligne/colonne/cellule et bounding box lorsque la méthode d'extraction le permet.

### 3.12 Immutabilité

Une correction d'extraction crée une nouvelle version/supersession ; elle ne détruit pas silencieusement l'ancienne.

## 4. BOABF — banque

### B01 — PNB historiquement absent

Des anciens états bancaires ne publient pas nécessairement le PNB.

**Règle** : ne pas fabriquer le PNB en RAW.

### B02 — Sous-postes très fins

Exemples : effets commerciaux, autres concours clientèle, comptes ordinaires débiteurs, épargne à vue, dettes à vue/terme, hors-bilan.

**Règle** : extraire lignes, sous-lignes, sous-totaux et totaux.

### B03 — Codes comptables de ligne

**Règle** : préserver `source_row_code`.

### B04 — Périodes cumulatives

T1, S1, 9M et FY peuvent être cumulatifs. Le terme « deuxième semestre » peut dans certaines publications représenter une situation annuelle cumulée.

**Règle** : déterminer `period_basis` depuis le contenu.

### B05 — Année absente du dossier mais présente ailleurs

Un dossier annuel vide ne prouve pas l'absence de données. BOABF possède notamment une source 2017 rangée dans `divers`.

### B06 — Doublons binaires

Deux fichiers différents peuvent être identiques au hash.

### B07 — Même résultat publié plusieurs fois

Conserver chaque occurrence avec son `document_id`.

### B08 — Bilan vs hors-bilan

Préserver la nature du tableau via `section_type_raw`/`statement_side_raw`.

## 5. Industrie / SYSCOHADA — NTLC et autres industriels

### N01 — Neutralité sectorielle

Le RAW doit absorber ventes de marchandises, produits fabriqués, matières, stocks, transport, services extérieurs, valeur ajoutée, EBE et résultat d'exploitation.

### N02 — Codes SYSCOHADA

Préserver les codes de rubrique lorsqu'ils sont publiés.

### N03 — TAFIRE / ressources-emplois / TFT

CAFG, variation BFE, investissements, autofinancement et flux publiés sont des faits RAW.

### N04 — Signes

Une valeur négative publiée est conservée telle quelle.

### N05 — Affectation et dividendes

L'affectation du résultat et le dividende par action publiés sont des faits source.

### N06 — Révisions

Les versions `_rev` restent distinctes.

### N07 — Fiches boursières hybrides

Un même document peut contenir comptabilité, données boursières, actionnariat, dirigeants et corporate actions.

### N08 — Ratios boursiers publiés

ROA/ROE/PER/P-B publiés ne sont pas recalculés dans RAW.

### N09 — Graphiques

Un graphique sans valeurs tabulées ne doit pas être converti en série exacte sans méthode de digitisation et niveau de confiance explicites.

## 6. Télécom — SNTS / ORAC / ONTBF

### T01 — KPI opérationnels

Parcs mobile/fixe/internet, data, 4G, fibre, mobile money et autres KPI doivent être conservés.

### T02 — Géographie

Un même KPI peut être publié par pays et au niveau Groupe.

### T03 — Segments

Retail, Wholesale, Data, Internet, Mobile Money et autres segments restent tels que publiés.

### T04 — Métriques proches mais différentes

Exemple : utilisateurs inscrits ≠ utilisateurs actifs.

### T05 — Unités non monétaires

Nombre de clients, Mo/Go, transactions, foyers raccordables, etc.

### T06 — IFRS consolidé

Droits d'usage, passifs locatifs, actifs de contrats clients, intérêts minoritaires et résultat global doivent être supportés.

### T07 — Mouvements

Les tableaux de flux et capitaux propres requièrent `movement_type_raw` lorsque pertinent.

### T08 — KPI propriétaires

Exemples : EBITDAaL, eCapex, Parc FMI. La définition source doit être conservée.

### T09 — ESG

Emplois, formations, énergie renouvelable, CO2, arbres plantés et autres données chiffrées ne doivent pas être perdues dans le texte.

### T10 — Classification documentaire

Un document peut porter des mentions telles que `Restricted`/`Interne`. Ces mentions sont des métadonnées documentaires à préserver sans en déduire automatiquement une règle d'accès externe.

## 7. Utility / concession — CIEC / SODECI

### U01 — Plusieurs périmètres économiques

Une société peut distinguer ses opérations propres et des opérations gérées pour le compte d'une autorité/secteur.

### U02 — Sémantique contractuelle

Une modification de convention peut changer la signification économique d'une ligne.

### U03 — Actifs/passifs pour compte de tiers

Ne pas les interpréter automatiquement comme actifs/passifs économiques propres.

### U04 — Monétaire + physique

Une même activité peut être publiée en FCFA et en GWh/nombre de branchements/clients.

### U05 — Stock vs flow

Total clients à une date ≠ nouveaux clients sur la période.

### U06 — Unités historiques

Les unités peuvent changer dans le temps.

### U07 — Individual vs consolidated

Un document peut contenir comptes individuels et consolidés ; préserver le scope et le standard comptable.

### U08 — Contrats/concessions

Créer/conserver les facts contractuels et le texte pertinent.

## 8. Logistique — AGLC / MOVIS

### L01 — Activités physiques

Tonnages, manutention, transit, entreposage, maritime, levage et bases logistiques doivent être acceptés par `operating_facts_raw`.

### L02 — Événement exceptionnel

MOVIS montre qu'un résultat net peut être dominé par une cession de site.

**Règle** : conserver l'événement daté/chiffré et sa relation au commentaire financier. `event_facts_raw` est une table candidate.

## 9. Automobile — CFAC / PRSC

### A01 — Données émetteur vs marché

Un rapport peut publier :

- ventes propres ;
- taille du marché automobile ;
- parts de marché ;
- données par marque.

**Règle** : utiliser des dimensions du type `subject_scope_raw`, `reference_entity_raw`, `product_raw`, `brand_raw`.

### A02 — Système normal / références comptables

Les états peuvent contenir références/notes de formulaires SYSCOHADA à préserver lorsque utiles à la localisation source.

## 10. Agriculture / plantations — PALC / SPHC / SOGC / SICC / SCRC

### AG01 — Quantités et prix moyens

Produits agricoles publiés en tonnes, unités, prix moyen et montant.

### AG02 — Surfaces

Hectares, surfaces matures/immatures et autres stades doivent être supportés.

Dimensions candidates : `crop_raw`, `site_raw`, `maturity_stage_raw`, `area_unit_raw`.

### AG03 — Campagnes

Une campagne agricole peut chevaucher deux années civiles.

Dimensions candidates : `campaign_label_raw`, `season_raw`.

### AG04 — Sites

Les performances/événements peuvent être rattachés à un site ou une plantation.

### AG05 — Événements opérationnels

Vols, arrêt de site, réduction de surface cultivable, météo ou autres événements peuvent expliquer la production et doivent rester dans les disclosures/events lorsqu'ils sont publiés.

## 11. BTP — STAC

### BTP01 — Projet/chantier

Le revenu peut dépendre du démarrage d'un projet particulier.

Dimension candidate : `project_raw` / `contract_raw`.

### BTP02 — Prévisions

Les rapports peuvent publier une prévision annuelle en plus du réalisé intermédiaire.

**Règle** : distinguer `ACTUAL`, `FORECAST`, `GUIDANCE`, `TARGET` via `fact_nature_raw` ou équivalent.

## 12. Finance réglementée — SAFC et banques

### RGF01 — Ratios prudentiels

CET1, levier, limites sur immobilisations et autres normes peuvent être explicitement publiés.

**Règle** : conserver comme facts `PUBLISHED`; `regulatory_facts_raw` est une table candidate.

### RGF02 — Changement de contrôle

Un rachat/changement de contrôle doit être traité comme événement corporate daté, sans en déduire automatiquement un changement d'issuer_id.

## 13. Audit / CAC

### CAC01 — Plusieurs niveaux d'assurance

Distinguer :

- audit ;
- attestation ;
- examen limité ;
- rapport sur états financiers résumés ;
- rapport spécial ;
- conventions réglementées.

### CAC02 — Statut des comptes vs statut du rapport

Des comptes peuvent être annoncés comme audités tandis qu'un rapport CAC est encore en cours de finalisation.

**Règle** : `financial_statement_status_raw` et `audit_report_status_raw` doivent être distinguables.

### CAC03 — IFRS individuel

IFRS ne signifie pas automatiquement consolidé. Servair publie des états individuels IFRS.

## 14. Identité émetteur

### ID01 — Changement de nom

Un émetteur peut changer de dénomination juridique/commerciale tout en conservant une continuité boursière.

Exemples observés : Crown SIEM/Eviosys Packaging SIEM ; Air Liquide/Erium ; Total/TotalEnergies ; SAFCA/Alios Finance selon les publications.

**Règle** : conserver `document_legal_name_raw` et prévoir un historique de noms après validation de continuité juridique.

## 15. Hydrocarbures / bitume

### H01 — Unités sectorielles

Les publications peuvent combiner CA/résultat avec kilotonnes et indicateurs en $/baril.

**Règle** : `source_unit_raw` doit être universel.

### H02 — Volumes

Préserver les volumes vendus et autres KPI d'activité lorsqu'ils sont explicitement publiés.

## 16. Tabac

### TB01 — Volumes/références

Les publications peuvent commenter des volumes et des références commerciales précises.

### TB02 — Changement fiscal

Un changement de régime de TVA/prix peut modifier la comparabilité historique.

**Règle** : conserver le contexte textuel/réglementaire ; ne pas corriger les séries RAW.

## 17. Édition / textile / biens de consommation

Les publications peuvent contenir des effets saisonniers, rentrée scolaire, nouveaux marchés, produits, cessions d'actifs et faits exceptionnels.

**Règle** : préserver `product_raw`, `geography_raw`, `event` et disclosures lorsqu'explicitement publiés.

## 18. Dénomination et sujets externes

Une donnée présente dans un rapport n'est pas nécessairement une donnée de l'émetteur.

Prévoir :

- `subject_scope_raw`
- `reference_entity_raw`
- `reference_product_raw`
- `product_raw`
- `brand_raw`

## 19. Règles transversales consolidées

1. Le modèle RAW est universel.
2. Le secteur détermine les familles de facts, pas la traçabilité.
3. Une donnée est identifiée par source + position + libellé + période + périmètre + unité + valeur.
4. Les dimensions sont optionnelles et extensibles.
5. Pas de normalisation sémantique dans RAW.
6. `PUBLISHED` et `DERIVED` sont séparés.
7. Versions/doublons/restatements sont historisés.
8. Les définitions de KPI sont conservées.
9. Distinguer période, publication, audit, approbation et disponibilité.
10. La base doit permettre une lecture point-in-time.
11. Les textes peuvent être indispensables à la compréhension d'un chiffre.
12. Aucun calcul analytique n'est requis pour constituer le RAW.
13. Un document sans texte natif n'est pas vide.
14. Un émetteur peut publier des faits concernant une autre entité/le marché.
15. Réalisé et prévision ne doivent jamais être confondus.
16. Audit, examen limité et attestation sont distincts.
17. IFRS et consolidation sont deux dimensions différentes.

## 20. Statut de couverture

Au 2026-08-09 :

- `DISCOVERY_PASS_48_ISSUERS_COMPLETE`
- `RAW_EXTRACTION_ALL_DOCUMENTS = NOT_COMPLETE`

Les pilotes conceptuels les plus approfondis sont BOABF, NTLC, SNTS et CIEC.

La prochaine phase doit être l'inventaire documentaire complet puis l'extraction RAW exhaustive, société par société.

## 21. Règle Git spécifique

Toutes les évolutions de ce document et de son implémentation sont réalisées directement sur `main` dans `Patricked-code/financialdata`.

**Aucune branche ne doit être créée.**
