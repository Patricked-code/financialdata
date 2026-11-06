# Protocole local d'admission, développement et continuité des agents

Statut : initial implementation. Autorités : GOVERNANCE.md, AGENTS.md, SUIVI.md. Cette page ne délègue aucune autorité Git supplémentaire.

## Admission
1. Lire l'ensemble de la mémoire canonique dans son ordre de priorité.
2. Vérifier la branche et le dernier SHA de main.
3. Lancer bootstrap : projection des phases ROADMAP et des travaux TODO, sans écraser les travaux existants.
4. Lancer audit : les erreurs sont bloquantes ; les warnings sont des écarts identifiés à traiter.
5. S'enregistrer avec admit et la capacité réellement disponible (audit ou coder).

## Construction et admissibilité
Les tâches TODO sont importées avec identité déterministe FD-T-*, source TODO.md et programme d'appartenance FD-P*. Leur priorité et leurs dépendances peuvent être enrichies dans factory/state.json après revue, sans réécrire la source TODO. Deux tâches d'audit FD-A-* sont fournies en tant que contrôles automatisables.

La sélection n'admet que BACKLOG avec toutes dépendances DONE et une capacité autorisée. Une tâche CLAIMED par un agent est retrouvée automatiquement par cet agent lors de sa reconnexion. Aucune reprise abusive du claim d'un autre agent n'est autorisée.

## Exécution
Le moteur run peut exécuter les audits identifiés. Pour une tâche agent_code, next fournit l'élément de travail ; le moteur ne produit pas de code IA à la place du codeur, et run ne simule jamais une exécution.

L'agent codeur :
- inspecte la base réelle et la provenance ;
- écrit des changements additifs compatibles ;
- développe tests de non-régression et cas d'échec attendus ;
- exécute les tests et contrôles ;
- conserve la provenance et le lien vers le commit exact ;
- consigne le résultat avec complete ou un blocage prouvé avec block ;
- actualise la mémoire du projet.

## Publication
Main uniquement ; jamais créer une branche ni une PR. Contrôler le SHA attendu avant commit ; publier le commit selon les permissions en vigueur ; vérifier le résultat de GitHub Actions. Une preuve locale n'est pas une attestation d'une exécution GitHub ; ne pas les confondre.

## Continuité
Le cycle suivant reprend par next/run, sans recréer des tâches déjà enregistrées. Les événements sont chaînés SHA-256 pour détecter l'altération de state.json. Ce chaînage ne constitue pas une signature ou une preuve externe immuable.

## Frontière MCP
La fabrique est indépendante. Un futur adaptateur peut exposer catalogues, tâches, claims et preuves au MCP, sans changer ici la source d'autorité ni créer un orchestrateur MCP concurrent.
