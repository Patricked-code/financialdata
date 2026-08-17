# P1 SOURCE — SOLIBRA / SLBC

Date de vérification initiale : 2026-08-09  
Dernière revérification live et SHA : 2026-08-17

Statut : `P1_INVENTORIED / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE`

- Ticker : `SLBC`
- Dossier Drive : `1U41GdtRNU8QYqHYI8WdLJlwv1vFaukVy`
- Dossiers directs : **28 = 1998–2025**
- snapshot précédent : **65 PDF**
- live strict parent-scoped : **70 PDF**
- delta : **+5 PDF**
- total SOURCE global V17 : **3 075 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v17_20260817.md`
- registre SHA : `inventory/hashes/SLBC.csv`

Le delta V17 a été enregistré avant tout SHA SLBC, conformément à la gouvernance SOURCE.

## Résultat SHA-256

- PDF matérialisés : **70/70** ;
- signatures `%PDF-` valides : **70/70** ;
- tailles validées : **70/70** ;
- SHA-256 calculés : **70/70** ;
- SHA-256 uniques : **70** ;
- groupes `EXACT_DUPLICATE` : **0**.

Le registre GitHub `inventory/hashes/SLBC.csv` a été revalidé après commit. Le fichier de calcul local avait des fins de ligne CRLF ; sa représentation canonique LF produit exactement le blob GitHub `6b54e3cfc5f6616e274846ec041b1b758b491251`. Il n'existe donc pas de divergence de contenu entre le registre calculé et le registre persisté.

## Particularités SOURCE

- historique long avec rapports annuels, états financiers et publications périodiques ;
- nombreuses variantes historiques suffixées `_2`, `_3`, `_4`, `_5` ;
- publications CAC et assemblées générales présentes dans les années récentes ;
- un erratum d'avis de convocation AGO est présent dans 2025 et reste dans SOURCE ;
- aucune variante n'est supprimée ou fusionnée sur la seule base de son nom ;
- les variantes historiques présentent de forts écarts de taille et sont toutes conservées comme objets physiques distincts.

## Relation de version prouvée — S1 2020

Deux objets physiques correspondent au rapport d'activité du premier semestre 2020 :

- `2020_Rapport_S1_SLBC.pdf` — **489 986 octets** — SHA-256 `b244c5a878c1100f63b01e237ed0eea12c2f61c93f3b402e14aaf28f6c36d4a4` ;
- `rapport_dactivite_du_premier_semestre_2020_-_solibra_ci.pdf` — **490 460 octets** — SHA-256 `c3eefce467ff4098bb17d2cba0bc1d17213dfec783a6038633411be03ffea6b4`.

Les deux PDF ont des octets et des SHA différents : ils ne sont donc **pas** `EXACT_DUPLICATE`.

Leur première et unique page rendue est visuellement identique et produit le même SHA-256 d'image rendue (`cd318801a3d85f37db97e04bd3a754e0cb80dd02ad0cb590c09bcec0b4d6408e`). Ils sont qualifiés `VERSION_OF` / représentations physiques équivalentes du même document économique. Aucun `SUPERSEDES` n'est déclaré, faute de preuve explicite d'annulation-remplacement.

## Règles de preuve appliquées

- un suffixe n'implique ni doublon ni ordre de version ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `VERSION_OF` et `SUPERSEDES` restent distincts ;
- les objets non strictement financiers restent conservés s'ils sont physiquement présents dans le périmètre SOURCE ;
- aucune source physique n'est supprimée lors de la réconciliation.

## P1 restant pour SLBC

Le hash physique est terminé. Restent dans les chantiers transversaux :

1. qualifier, lorsque les preuves le permettent, les relations sémantiques/versionnelles entre certaines variantes historiques ;
2. réconcilier le corpus Drive avec les collectes BRVM fraîches dans P1-FRESH ;
3. compléter le manifeste documentaire canonique et les relations de provenance/version ;
4. conserver l'erratum 2025 et les autres documents non financiers dans l'historique SOURCE.

## Point de reprise

`SLBC_LIVE=70 | DELTA=+5 | SHA=70/70 | UNIQUE_SHA=70 | EXACT_DUPLICATE_GROUPS=0 | GLOBAL_SOURCE=3075 | NEXT=PRSC_LIVE_RECHECK_AND_SHA`
