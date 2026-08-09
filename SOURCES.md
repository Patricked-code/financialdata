# SOURCES — financialdata

Ce fichier enregistre les corpus et sources utilisés par le projet. Il ne remplace pas la provenance au niveau de chaque document/fait.

## 1. Corpus BRVM principal

### Google Drive — RAPO / Rapport V2

Arborescence de référence explorée pour les sociétés cotées BRVM.

- dossier `RAPO` : `https://drive.google.com/drive/folders/1pabkvo_ch9ekBt7LqaJPbrgDez1IJtWd`
- sous-dossier `Rapport V2` : `https://drive.google.com/drive/folders/1dsobS8AStWqa1ds3RAnmNS1jnGZWmJy2`

Organisation observée :

`RAPO / Rapport V2 / [SOCIÉTÉ - TICKER] / [ANNÉE] / [DOCUMENTS]`

Un sous-dossier `divers` peut contenir des documents couvrant des périodes absentes des dossiers annuels.

## 2. Document de gouvernance conceptuelle historique

Document Drive ayant servi à consolider les observations avant initialisation du présent dépôt :

`BRVM_RAW_DATABASE — Gouvernance, architecture et observations conceptuelles`

URL : `https://docs.google.com/document/d/1eF6E0McUZQbgd2uGPIXEGSYEqjhI6crs0CRCQuZ1ST4`

À compter de l'initialisation de `financialdata`, GitHub devient la mémoire persistante opérationnelle. Le document Drive reste une source historique de conception et ne doit pas être supprimé.

## 3. Pilote BOABF

Dossier société :

`https://drive.google.com/drive/folders/1hQwExoX3z7LZKg89inSre8bKGjFoZ-lP`

Nom : `Bank of Africa Burkina Faso - BOABF`.

Observations déjà établies :

- dossiers directs 2009 à 2025 + `divers` ;
- certains dossiers annuels directs peuvent être vides ;
- des documents rangés dans `divers` peuvent combler des périodes historiques ;
- présence de doublons binaires exacts ;
- mélange de PDF avec texte natif et de scans ;
- rapports d'activité, états financiers, attestations CAC, fiches boursières et documents divers.

## 4. Sources futures

Le projet pourra intégrer, après documentation :

- publications BRVM officielles ;
- sites investisseurs des émetteurs ;
- régulateurs ;
- bourses ;
- documents officiels de sociétés ;
- autres fichiers structurés ou archives vérifiables.

Toute nouvelle source doit être ajoutée à ce fichier avant ou lors de sa première utilisation systématique.

## 5. Hiérarchie de preuve

Lorsque plusieurs sources publient la même donnée, ne pas choisir arbitrairement une valeur et supprimer les autres.

Conserver :

- chaque document ;
- chaque observation ;
- la provenance ;
- les dates ;
- le statut de certification/audit ;
- la relation entre versions ;
- les éventuelles incohérences.

La réconciliation appartient aux couches de contrôle/mapping/canonicalisation, pas à l'ingestion RAW.

## 6. Métadonnées minimales par document

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
- période(s) économique(s) réellement couverte(s) ;
- société/ticker ;
- type documentaire ;
- présence de texte natif ;
- besoin éventuel de rendu/OCR ;
- relation de version/doublon.

## 7. Règle PDF

Ordre :

1. texte natif ;
2. inspection/rendu visuel des pages ;
3. OCR uniquement en dernier recours.

Un document sans texte natif n'est jamais considéré comme vide sur cette seule base.

## 8. Règle de complétude

La complétude doit être mesurée à partir des **documents et périodes réellement présents**, et non seulement à partir :

- des noms de fichiers ;
- des noms de dossiers ;
- du nombre de dossiers annuels ;
- du ticker apparaissant dans le nom du fichier.

Les recherches doivent être recoupées par l'arborescence exacte lorsque les tickers courts provoquent des résultats ambigus.
