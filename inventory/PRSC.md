# P1 SOURCE — Tractafric Motors Côte d'Ivoire / PRSC

Date de vérification initiale : 2026-08-09  
Dernière revérification live et SHA : 2026-08-17

Statut : `P1_INVENTORIED / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE`

- Ticker : `PRSC`
- Dossier Drive : `1uA4PVTKVuFPpR8uaQ87ORw3mzAIZ3f_h`
- snapshot précédent : **68 PDF**
- live strict parent-scoped : **70 PDF**
- delta net : **+2 PDF**
- dossiers directs live observés : **25** — `1998–2007`, puis `2011–2025`
- les dossiers `2008`, `2009`, `2010` décrits lors de l'inventaire initial ne sont pas visibles dans l'arborescence live actuelle ; ce delta de structure est documenté sans suppression de trace historique
- total SOURCE global V18 : **3 077 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md`
- registre SHA : `inventory/hashes/PRSC.csv`

Le delta V18 a été enregistré avant tout SHA PRSC.

## Résultat SHA-256

- PDF matérialisés : **70/70** ;
- signatures `%PDF-` valides : **70/70** ;
- tailles validées : **70/70** ;
- SHA-256 calculés : **70/70** ;
- SHA-256 uniques : **70** ;
- groupes `EXACT_DUPLICATE` : **0**.

Le registre `inventory/hashes/PRSC.csv` a été construit avec fins de ligne LF et revalidé après commit. Le blob attendu calculé localement et le blob GitHub sont identiques : `78c6332bf1849eae6dff57f37e910d5ce2863348`.

## Périmètre SOURCE et noms génériques

Deux objets live valides n'utilisent pas le ticker `PRSC` dans leur nom :

- `rapport_d27activite_1er_sem_2017_tmci.pdf` — Drive `1u7f5paNLrX9QDwWstf1rKb4aiSfPRT2o` ;
- `tractafric_motors_ci_-_rapport_dactivites_t1_2023.pdf` — Drive `1yaoRVLzT-hf7cG2vYMZ4ZKK55wkcBYgc`.

Cela confirme qu'une recherche par nom/ticker ne peut pas servir de définition canonique du corpus. Le live count est construit par parents Drive réels + MIME PDF.

## Relations et variantes — revue 2023–2025

### États financiers 2023

- `2023_Etats_Financiers_PRSC.pdf` — **850 439 octets** — SHA `c55474bd2906c60db0200f60ac415482db5c55baf34a68a4b27c5ce96f84b7dc` — 3 pages ;
- `2023_Etats_Financiers_PRSC_rev.pdf` — **176 741 octets** — SHA `54996ba5f9bb4be18b42129011aa68d44a30b3ad0f5b393e90f62c966a54b5b2` — 1 page.

Le premier est un jeu d'états financiers SYSCOHADA détaillé clos au 31/12/2023. Le second est une synthèse annuelle explicitement intitulée `ETATS FINANCIERS DE SYNTHESE ANNUELS AU 31.12.2023`. Les deux portent sur le même exercice économique sous des représentations/documentations différentes : relation `VERSION_OF` au niveau sémantique. Ils ne sont pas `EXACT_DUPLICATE`.

Le suffixe `_rev` n'est pas utilisé comme preuve de `SUPERSEDES`. Aucune relation d'annulation-remplacement n'est enregistrée sans formulation explicite dans la source.

### Rapports S1 2023

Trois objets physiques distincts sont présents :

- `2023_Rapport_S1_PRSC.pdf` — **203 992 octets** — SHA `1c6d354363938821d0a0af07b8e6700250bacb372b4995690ea7a44bec57dd43` — 1 page numérique ;
- `2023_Rapport_S1_PRSC_2.pdf` — **552 867 octets** — SHA `5b1c6f2e5e8fa28a33c9c4475db50a33ac87f6278600a1525c7fb7127e140e05` — 2 pages scannées ;
- `2023_Rapport_S1_PRSC_3.pdf` — **563 221 octets** — SHA `0542dae86a42af3cc96fbf23461966ee0d5d2d41f40ac0cd7a4ada88d42c15bd` — 2 pages scannées.

Leurs premières pages rendues sont distinctes. Aucune fusion sémantique automatique n'est donc appliquée au-delà du fait qu'ils sont rangés dans le même millésime/périmètre SOURCE.

### États financiers 2024

Trois objets physiquement distincts :

- `2024_Etats_Financiers_PRSC.pdf` — **686 931 octets** — SHA `a8166b7149b5333948eaa8bf8562435605c7f0141614b9a12a5da26ed7902759` — états annuels 31/12/2024 ;
- `2024_Etats_Financiers_PRSC_2.pdf` — **286 119 octets** — SHA `521a9634dc4003d716a2f41e058bf0f43392cca539c395ee57947031ed51e2e2` — états annuels 31/12/2024 ;
- `2024_Etats_Financiers_PRSC_3.pdf` — **145 953 octets** — SHA `8d39be3d4f888a1c702c04efe21fca943a98c74a65cb1e2655b5faa993897612` — états clos au 30/06/2024, durée 6 mois.

Le `_3` est donc un document semestriel et ne doit pas être fusionné avec les deux annuels. Les deux annuels restent des représentations physiques distinctes ; aucune relation `SUPERSEDES` n'est inférée du suffixe.

### États financiers 2025

- `2025_Etats_Financiers_PRSC.pdf` — **1 015 364 octets** — SHA `c5175f838afaaed295c775428415a24dbc969604910914a7c176621204645a2e` ;
- `2025_Etats_Financiers_PRSC_2.pdf` — **972 070 octets** — SHA `53247bd5800dccde3d233f4c88df4f6b47c834f8086e6265d8d3b5a70f211e43`.

Les deux sont des scans de 3 pages mais leurs binaires et premières pages rendues diffèrent. Aucun `EXACT_DUPLICATE`, aucune fusion automatique et aucun `SUPERSEDES` sans preuve explicite.

## Particularités SOURCE

- historique long avec nombreuses variantes de rapports annuels ;
- grands écarts de taille entre variantes anciennes, confirmant que les suffixes ne sont pas des preuves de doublon ;
- attestations CAC et rapports T1/S1/T3 présents dans le corpus récent ;
- deux noms génériques expliquent pourquoi le parent-scoped est nécessaire ;
- aucune source physique n'est supprimée, renommée ou fusionnée pendant la réconciliation.

## Règles de preuve appliquées

- les dossiers et suffixes ne dictent pas seuls période, doublon ou ordre de version ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `VERSION_OF` et `SUPERSEDES` restent distincts ;
- aucune disparition de dossier live n'autorise à supprimer une trace historique ;
- aucun objet physiquement présent sous les parents SOURCE n'est écarté à cause de son nom.

## P1-R

Les faits automobile/ventes/volumes/marques/parts de marché restent compatibles avec les faits opérationnels et dimensions produit/segment déjà prévus. Aucune nouvelle dimension n'est ajoutée sur la seule base de cet inventaire.

## P1 restant pour PRSC

Le hash physique est terminé. Restent dans les chantiers transversaux :

1. compléter les relations sémantiques/versionnelles seulement lorsque les preuves documentaires le permettent ;
2. réconcilier le corpus Drive avec P1-FRESH/BRVM ;
3. backfiller le manifeste documentaire canonique et les périodes économiques fines ;
4. conserver l'historique des structures de dossiers et des variantes physiques.

## Point de reprise

`PRSC_LIVE=70 | DELTA=+2 | SHA=70/70 | UNIQUE_SHA=70 | EXACT_DUPLICATE_GROUPS=0 | GLOBAL_SOURCE=3077 | NEXT=SAFC_LIVE_RECHECK_AND_SHA`
