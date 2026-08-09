# SOURCES — financialdata

Ce fichier enregistre les corpus et sources utilisés par le projet. Il ne remplace pas la provenance au niveau de chaque document/fait.

## 1. Corpus BRVM principal

### Google Drive — RAPO / Rapport V2

Arborescence historique de référence :

- dossier `RAPO` : `https://drive.google.com/drive/folders/1pabkvo_ch9ekBt7LqaJPbrgDez1IJtWd`
- sous-dossier `Rapport V2` : `https://drive.google.com/drive/folders/1dsobS8AStWqa1ds3RAnmNS1jnGZWmJy2`

Organisation observée :

`RAPO / Rapport V2 / [SOCIÉTÉ - TICKER] / [ANNÉE] / [DOCUMENTS]`

Un sous-dossier `divers` peut contenir des documents couvrant des périodes absentes des dossiers annuels.

### Script Python historique présent à la racine

- nom : `telecharger_rapports_brvm.py`
- Drive ID : `1F1WRVMG4C27EOTMq5Gt9FT9Mosv-Rryz`
- MIME : `text/x-python`
- taille : `14546` octets
- rôle : téléchargement automatique des rapports depuis `brvm.org`
- mapping embarqué : 48 sociétés / slugs historiques

La liste directe du dossier constitue la preuve de présence de ce fichier ; une recherche Drive textuelle antérieure l'avait manqué.

Le script est une **source historique de collecte**, pas une source de vérité pour les périodes économiques. Il déduit l'année principalement du nom du fichier et peut utiliser l'année de publication comme approximation.

Le plan d'évolution est documenté dans `docs/BRVM_COLLECTOR_V2_PLAN.md`.

## 2. Source BRVM officielle courante

Source primaire de fraîcheur :

`https://www.brvm.org/fr/rapports-societe-cotes/<slug>`

Les pages courantes publient les rapports par émetteur avec des catégories telles que :

- rapports annuels ;
- états financiers ;
- rapports semestriels ;
- rapports trimestriels ;
- commentaires sur l'activité.

Les PDF observés en 2026 restent servis sous des URLs de type :

`https://www.brvm.org/sites/default/files/<nom>.pdf`

### Rôle dans le projet

Le Drive `Rapport V2` est le corpus historique existant à inventorier.

Le site BRVM courant est la source à comparer au manifeste pour identifier :

- nouveaux documents ;
- nouvelles années ;
- corrections/remplacements ;
- changements de catalogue ;
- nouveaux émetteurs/slugs ;
- documents distants absents du corpus historique.

### Deltas déjà observés au 2026-08-09

BOAC :

- page courante : EF 2025 + T1 2026 visibles ;
- Drive inventorié : 2025 T1/S1/T3, pas de dossier 2026 ;
- statut : `REMOTE_DELTA_IDENTIFIED`.

BOAM :

- page courante : T3 2025 + EF 2025 + T1 2026 visibles, en plus de T1/S1 2025 ;
- Drive inventorié : T1/S1 2025, pas de dossier 2026 ;
- statut : `REMOTE_DELTA_IDENTIFIED`.

Ces constats prouvent que le corpus historique doit être réconcilié périodiquement avec la source BRVM courante.

## 3. Document de gouvernance conceptuelle historique

Document Drive :

`BRVM_RAW_DATABASE — Gouvernance, architecture et observations conceptuelles`

URL : `https://docs.google.com/document/d/1eF6E0McUZQbgd2uGPIXEGSYEqjhI6crs0CRCQuZ1ST4`

GitHub `financialdata` est désormais la mémoire persistante opérationnelle. Le document Drive reste une source historique de conception.

## 4. Pilote BOABF

Dossier société :

`https://drive.google.com/drive/folders/1hQwExoX3z7LZKg89inSre8bKGjFoZ-lP`

Observations déjà établies : dossiers 2009–2025 + `divers`, années directes parfois vides, doublons binaires, scans et PDF texte natif, rapports d'activité, états financiers, CAC, fiches boursières.

## 5. Sources futures

Le projet pourra intégrer, après documentation : publications BRVM officielles, sites investisseurs, régulateurs, bourses, documents officiels de sociétés et autres archives vérifiables.

Toute nouvelle source doit être enregistrée avant ou lors de sa première utilisation systématique.

## 6. Sources révisables et versionnées

Le registre des sources est vivant. Une source peut être revue, enrichie, reclassée, remplacée par une meilleure version ou dépréciée pour les usages futurs.

Une révision ne supprime jamais l'historique.

Statuts recommandés : `ACTIVE`, `UNDER_REVIEW`, `SUPERSEDED`, `DUPLICATE`, `DEPRECATED_FOR_FUTURE_USE`, `REVIEW_REQUIRED`.

Les faits RAW existants restent liés à la version exacte de la source dont ils proviennent.

## 7. Hiérarchie de preuve

Lorsque plusieurs sources publient la même donnée, conserver chaque document, observation, provenance, date, statut d'audit/certification, relation de version et incohérence.

La réconciliation appartient aux couches de contrôle/mapping/canonicalisation, pas à l'ingestion RAW.

## 8. Métadonnées minimales par document

- fournisseur/source ;
- identifiant externe ;
- URL ou chemin ;
- dossier parent ;
- nom de fichier ;
- type MIME ;
- taille ;
- hash ;
- date de création/modification si disponible ;
- date de publication si déterminable ;
- première/dernière observation sur la source courante ;
- période(s) économique(s) réellement couverte(s) ;
- société/ticker ;
- type documentaire ;
- présence de texte natif ;
- besoin éventuel de rendu/OCR ;
- relation de version/doublon ;
- statut de source/revue ;
- statut d'attribution à l'émetteur.

## 9. Règle PDF

Ordre : texte natif → inspection/rendu visuel → OCR uniquement en dernier recours.

Un document sans texte natif n'est jamais considéré comme vide sur cette seule base.

## 10. Règle de complétude

La complétude doit être mesurée à partir des documents et périodes réellement présents et comparée, lorsque nécessaire, au catalogue BRVM courant.

Ne pas se fier uniquement aux noms de fichiers/dossiers ou au nombre de dossiers annuels.
