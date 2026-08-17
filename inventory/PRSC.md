# P1 SOURCE — Tractafric Motors Côte d'Ivoire / PRSC

Date de vérification initiale : 2026-08-09  
Dernière revérification live : 2026-08-17

Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / HASH_PENDING`

- Ticker : `PRSC`
- Dossier Drive : `1uA4PVTKVuFPpR8uaQ87ORw3mzAIZ3f_h`
- snapshot précédent : **68 PDF**
- live strict parent-scoped : **70 PDF**
- delta net : **+2 PDF**
- dossiers directs live observés : **25** — `1998–2007`, puis `2011–2025`
- les dossiers `2008`, `2009`, `2010` décrits lors de l'inventaire initial ne sont pas visibles dans l'arborescence live actuelle ; ce delta de structure est documenté sans déduction sur les fichiers historiques
- total SOURCE global V18 : **3 077 PDF**
- checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v18_20260817.md`

Le delta V18 est enregistré avant tout SHA PRSC.

## Particularités SOURCE

- historique long avec collisions et variantes de rapports annuels ;
- `2023_Etats_Financiers_PRSC.pdf` + `2023_Etats_Financiers_PRSC_rev.pdf` ;
- plusieurs variantes S1 2023 ;
- 2024 comporte trois fichiers d'états financiers ;
- 2025 comporte deux états financiers, S1 et T1 ;
- un objet live est nommé `tractafric_motors_ci_-_rapport_dactivites_t1_2023.pdf` : le périmètre ne peut donc pas être construit par simple recherche du ticker `PRSC`.

## Règles de preuve

- les dossiers et suffixes ne dictent pas seuls période, doublon ou ordre de version ;
- `EXACT_DUPLICATE` exige un SHA-256 identique ;
- `VERSION_OF` et `SUPERSEDES` restent distincts ;
- aucune disparition de dossier live n'autorise à supprimer une trace historique ;
- aucun objet physiquement présent sous les parents SOURCE n'est écarté à cause de son nom.

## P1-R

Les faits automobile/ventes/volumes/marques/parts de marché sont compatibles avec les faits opérationnels et dimensions produit/segment déjà prévues. Aucune nouvelle dimension n'est ajoutée sur la seule base de cet inventaire.

## P1 restant immédiat

1. matérialiser **70/70** PDF live ;
2. valider signatures et tailles ;
3. calculer SHA-256 exhaustif ;
4. produire `inventory/hashes/PRSC.csv` ;
5. revoir les collisions exactes et relations de version, notamment EF 2023 plain/`_rev`, S1 2023 et variantes EF 2024/2025 ;
6. revalider le registre GitHub après commit ;
7. fermer PRSC seulement après ces contrôles.

## Point de reprise

`PRSC_SNAPSHOT=68 | PRSC_LIVE=70 | DELTA=+2 | GLOBAL_SOURCE=3077 | HASH=PENDING`
