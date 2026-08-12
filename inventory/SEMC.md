# P1 SOURCE — Crown SIEM / EVIOSYS PACKAGING SIEM Côte d'Ivoire / SEMC

Date de vérification : 2026-08-12
Statut : `P1_INVENTORIED / LIVE_SOURCE_RECHECKED_NO_DELTA / SHA256_COMPLETE`

- Ticker : `SEMC`
- Dossier Drive : `1tgcfrvdREP78qWgCtI639Ppk_xpuJq5T`
- Dossiers directs : **25** = 24 années + `divers`
- PDF live vérifiés : **54**

## Couverture observée

Années présentes : 1999–2001 puis 2003–2023. **2002 absent**. Aucun dossier 2024/2025 observé dans cette passe. Un dossier `divers` est présent.

## Revérification live 2026-08-12

La première recherche multi-parent Drive n'a renvoyé qu'un sous-ensemble et n'a donc pas été utilisée comme preuve de complétude. La revérification a été reprise strictement **dossier parent par dossier parent** sur les 25 dossiers directs.

Résultat physique :

- snapshot précédent : **54 PDF** ;
- live strict : **54 PDF** ;
- delta : **0** ;
- total projet V13 inchangé : **3 046 PDF**.

Comptage par dossier :

| Dossier | PDF |
|---|---:|
| 1999 | 1 |
| 2000 | 1 |
| 2001 | 1 |
| 2003 | 2 |
| 2004 | 2 |
| 2005 | 1 |
| 2006 | 3 |
| 2007 | 2 |
| 2008 | 3 |
| 2009 | 3 |
| 2010 | 3 |
| 2011 | 4 |
| 2012 | 4 |
| 2013 | 2 |
| 2014 | 2 |
| 2015 | 2 |
| 2016 | 1 |
| 2017 | 4 |
| 2018 | 3 |
| 2019 | 3 |
| 2020 | 2 |
| 2021 | 1 |
| 2022 | 1 |
| 2023 | 2 |
| divers | 1 |
| **TOTAL** | **54** |

## SHA-256

- **54 / 54 PDF matérialisés et hashés** ;
- **54 / 54 tailles Drive ↔ fichiers locaux validées** ;
- **54 SHA uniques** ;
- **0 groupe de doublons binaires exacts** dans SEMC ;
- registre : `inventory/hashes/SEMC.csv`.

Les nombreuses variantes historiques `_2`, `_3`, `_4`, `_5` ne sont donc pas des doublons binaires exacts. Elles restent des objets SOURCE distincts ; leurs éventuelles relations sémantiques/version doivent être déterminées par le contenu et non par leur suffixe.

## Résolution de `divers_Attestation_CAC_Annuel_SEMC.pdf`

- Drive ID : `1k-kGfM10MvHbKipidlxStHPyhG04B-I4` ;
- taille : **131 426 octets** ;
- SHA-256 : `ac83e5f2febcdac12010813509043228b8920eb808063377634337306010c54b` ;
- PDF : **3 pages** ;
- couche texte native exploitable : **absente** ;
- document rendu visuellement, sans OCR.

La preuve visuelle établit :

- émetteur visible : **CROWN SIEM S.A.** ;
- nature : **attestation des commissaires aux comptes sur le tableau d'activité et de résultat et le rapport d'activité semestriel** ;
- date de situation : **30 juin 2020** ;
- période couverte explicitement dans le corps : **1er janvier au 30 juin 2020** ;
- période économique résolue : **S1 2020** ;
- date de l'attestation : **Abidjan, le 3 décembre 2020** ;
- commissaires aux comptes visibles : PricewaterhouseCoopers et ECR International.

Verdict :

`ECONOMIC_PERIOD = 2020-01-01 → 2020-06-30 / S1 / CONTENT_VISUALLY_RESOLVED`

Le nom `divers_Attestation_CAC_Annuel_SEMC.pdf` ne doit donc pas être interprété comme une attestation annuelle : le contenu prouve qu'il s'agit d'une attestation relative au **premier semestre 2020**.

## Identité / dénomination

L'historique de dénomination Crown SIEM / EVIOSYS PACKAGING SIEM reste à préserver comme historique d'un même émetteur `SEMC` tant qu'aucune preuve juridique n'impose une scission. Les sources historiques ne sont jamais renommées rétroactivement.

## Restant transversal

`SHA256 = COMPLETE_54_OF_54` ; `EXACT_DUPLICATES = NONE_54_UNIQUE` ; `VERSION_LINKS = CONTENT_REVIEW_REMAINING_FOR_BINARY_DISTINCT_VARIANTS` ; `ECONOMIC_PERIODS = PARTIAL_WITH_DIVERS_S1_2020_RESOLVED` ; `REMOTE_FRESHNESS = RECHECKED_NO_DELTA`.
