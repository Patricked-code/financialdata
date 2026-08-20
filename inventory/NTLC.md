# P1 SOURCE — Nestlé Côte d'Ivoire / NTLC

Date : 2026-08-20
Statut : `P1_INVENTORIED / DEEP_PILOT_ALREADY_EXISTS / LIVE_RECHECK_COMPLETE / SHA256_COMPLETE`

- Ticker : `NTLC`
- Dossier Drive canonique : `1LMpOZwGEtDm0cn8TcEPUJbodOPMU3exU`
- Dossiers directs live : **28**, continus de `1998` à `2025`
- Snapshot avant recheck : **81 PDF**
- Recheck live strict parent-scoped : **85 PDF**
- Delta live : **+4**
- SOURCE global : **V22 = 3 137 PDF**
- Checkpoint : `inventory/P1_48_ISSUERS_CHECKPOINT_v22_20260819.md`

## Preuve de cardinal live

Le corpus a été recompté sur deux sous-périmètres disjoints des mêmes dossiers enfants pour rendre le cardinal indépendant de la troncature d'affichage du connecteur :

- années `1998–2011` : **33 PDF** ;
- années `2012–2025` : **52 PDF** ;
- total live : **85 PDF**.

Le périmètre SOURCE est défini par les parent IDs Drive réels, jamais par une recherche ticker seule.

## SHA-256 / intégrité physique

- **85/85 PDF** matérialisés depuis la whitelist Drive live ;
- **85/85** signatures `%PDF-` valides ;
- **85 SHA-256 uniques** ;
- **0 groupe `EXACT_DUPLICATE`** ajouté par NTLC ;
- registre : `inventory/hashes/NTLC.csv` ;
- sérialisation canonique : **LF**, 14 239 octets ;
- blob Git local et GitHub validé bit-for-bit : `90cd7791f2a57754ba3a21f873c8f1a18b543cf2`.

Une première écriture textuelle du registre a produit un blob divergent et n'a jamais été considérée comme valide. Le registre a été remplacé par le blob construit directement depuis les octets du CSV local, puis revalidé après fast-forward de `main`.

## Doublons / versions

Aucun SHA-256 ne collisionne dans les 85 objets : aucun doublon exact NTLC.

### États financiers 2024

- `2024_Etats_Financiers_NTLC.pdf` : 4 pages, export Microsoft Excel, états financiers de synthèse au **31.12.2024** ;
- `2024_Etats_Financiers_NTLC_rev.pdf` : 1 page, représentation PDFium/DocuSign, même période et mêmes principaux chiffres de bilan 2024/2023 ;
- les octets, tailles, pagination et représentation diffèrent ;
- qualification conservatrice : même famille économique / relation de version-représentation à conserver pour revue `VERSION_OF`, **pas** `EXACT_DUPLICATE` et **aucun `SUPERSEDES`** sans preuve explicite.

### États financiers 2023

Les deux objets `2023_Etats_Financiers_NTLC.pdf` et `_2.pdf` portent le même exercice au **31.12.2023**, mais présentent des formats/contenus comparatifs différents et des octets distincts. Ils restent deux objets SOURCE physiques ; aucune substitution ni relation `SUPERSEDES` n'est inférée.

### Historique multi-suffixes

Les familles historiques `_2`, `_3`, `_4` présentent des tailles et représentations très hétérogènes. Elles ne sont jamais fusionnées ou qualifiées sur le seul nom de fichier. Les documents semestriels, trimestriels, CAC et annuels modernes restent également des rôles documentaires distincts.

## P1-R

NTLC a déjà servi de deep pilot industrie : stocks, ventes, matières, EBE, dividendes, document annuel original vs révision DocuSign, distinction tableau/narratif et faits corporate/audit. Cette analyse n'est pas refaite de zéro ; les vérifications transversales de complétude P1 sont désormais ajoutées.

## État final P1 transverse pour NTLC

`LIVE_RECHECK = COMPLETE` ; `SHA256 = COMPLETE` ; `EXACT_DUPLICATES = 0` ; `REGISTRY_BLOB = 90cd7791f2a57754ba3a21f873c8f1a18b543cf2` ; `VERSION_REVIEW = CONSERVATIVE_COMPLETE_FOR_JUSTIFIED_FAMILIES` ; `REMOTE_FRESHNESS = LIVE_RECHECK_COMPLETE_FOR_CURRENT_SCOPE`.

## Suite

Poursuivre le prochain corpus réellement non hashé selon le manifeste/TODO courant, sans réouvrir NTLC sauf nouvelle preuve SOURCE ou nouveau delta live.
