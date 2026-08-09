# P1 SOURCE — Vivo Energy Côte d'Ivoire / SHEC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED / SHA_COMPLETE`

- Ticker : `SHEC`
- Dossier Drive : `1U7RJ1DevoTrrFsxGAOyFrm5wQrTpl3aE`
- Dossiers directs : **10**, années `2016–2025` complètes
- Premier inventaire de session : **37 PDF**
- État Drive live revérifié par parents + MIME : **39 PDF**
- Delta live : **+2 PDF**

## Particularités SOURCE

- 2016 : rapport d'activité T3 historique au nom source `veci_...` ;
- 2018 : T1, S1, états financiers, attestation CAC annuelle et rapport annuel ;
- 2021 : T1, S1, T3, deux états financiers et un `rapport_de_carence_-_ifrs_-_vivo_energy_ci.pdf` ;
- 2022 : T1, S1, T3 et **trois états financiers physiques** ;
- 2023 : S1, T3 et **deux états financiers physiques** ;
- 2024 : T1, T2 et T3 ;
- 2025 : S1, T3 et **deux états financiers physiques**.

## SHA-256

Les **39 PDF** ont été matérialisés depuis Drive et hashés avec contrôle des tailles.

- `SHA256_SHEC = COMPLETE_39_39` ;
- contenus binaires uniques : **37 / 39** ;
- groupes de doublons binaires exacts trouvés chez SHEC : **2** ;
- registre SHA : `inventory/hashes/SHEC.csv` ;
- groupes exacts : `inventory/p1_duplicate_groups.csv`.

### Groupe exact 2022

- `2022_Etats_Financiers_SHEC_2.pdf` ;
- `2022_Etats_Financiers_SHEC_3.pdf` ;
- taille commune : **288 635 octets** ;
- SHA-256 commun : `acdab75be25743dc0837258d686cfc5f2e2c6f76518078e6becc9a94ddb40f86`.

Le fichier `2022_Etats_Financiers_SHEC.pdf` sans suffixe est distinct : SHA `f89382a6df04d4d360f245548c0c8d5217e6172410c235a63aeb7c6065f75f08`.

### Groupe exact 2025

- `2025_Etats_Financiers_SHEC.pdf` ;
- `2025_Etats_Financiers_SHEC_2.pdf` ;
- taille commune : **280 229 octets** ;
- SHA-256 commun : `b88401ae19d81d9dcd4a1723cd1929bad8c0269dfa811c06e7c9b878b58b61c0`.

### Variantes non binaires

- états financiers 2021 plain / `_2` : tailles et SHA différents ;
- états financiers 2023 plain / `_2` : tailles et SHA différents.

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 10 dossiers parents et `mimeType = application/pdf`. Les sources appartenant à un même groupe exact restent toutes conservées physiquement dans SOURCE ; seul leur `binary_duplicate_group_id` les relie. Le rapport de carence IFRS est conservé comme famille documentaire SOURCE distincte ; il ne justifie pas à lui seul une nouvelle table RAW avant inspection du contenu.

## P1-R

T2 est déjà une période reconnue. Les faits énergie/distribution/produits/volumes sont compatibles avec le modèle opérationnel/segment existant. Aucune nouvelle dimension conceptuelle n'est requise par cette passe.

## Restant transversal

`DOCUMENT_MANIFEST_SHEC = ROW_COVERAGE_39_39 / SHARD_BACKFILL_PENDING` ; `SHA256_SHEC = COMPLETE_39_39` ; `BINARY_DUPLICATE_GROUPS_SHEC = 2` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
