# P1 SOURCE — Vivo Energy Côte d'Ivoire / SHEC

Date : 2026-08-09
Statut : `P1_INVENTORIED / LIVE_SOURCE_DELTA_DETECTED`

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

## Règle

Le total live est obtenu sans filtre de nom, uniquement par les 10 dossiers parents et `mimeType = application/pdf`. Les variantes d'états financiers plain / `_2` / `_3` restent séparées jusqu'au verdict SHA-256. Le rapport de carence IFRS est conservé comme famille documentaire SOURCE distincte ; il ne justifie pas à lui seul une nouvelle table RAW avant inspection du contenu.

## P1-R

T2 est déjà une période reconnue. Les faits énergie/distribution/produits/volumes sont compatibles avec le modèle opérationnel/segment existant. Aucune nouvelle dimension conceptuelle n'est requise par cette passe.

## Restant transversal

`DOCUMENT_MANIFEST_SHEC = IN_PROGRESS` ; `SHA256_SHEC = NOT_COMPLETE` ; `VERSION_LINKS = NOT_COMPLETE` ; `ECONOMIC_PERIODS = NOT_COMPLETE` ; `REMOTE_FRESHNESS = ACTIVE_DELTA_OBSERVED`.
