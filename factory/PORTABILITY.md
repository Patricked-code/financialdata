# Portable factory — procédure pour un autre dépôt GitHub

Le dépôt `Patricked-code/financialdata` est un **exemple vérifié**, pas une autorité transversale. Copier directement ses décisions, ses données BRVM, sa règle main-only ou les identifiants `FD-*` serait une erreur.

## Instruction pour un nouvel agent connecté à GitHub

« Analyse entièrement `OWNER/REPO` avec le compte GitHub autorisé, et installe ou raccorde une usine de développement autonome gouvernée inspirée des fonctions vérifiées dans `Patricked-code/financialdata`. Commence par découvrir la gouvernance, le code, l'infrastructure, les workflows, les dépendances et les protections réelles du dépôt cible. Réutilise ses moteurs existants et sa mémoire ; aucune réinitialisation, aucune queue parallèle et aucune perte de données. Intègre des projets/programmes/tâches/UTL, un registre d'état persistant, l'admission des agents, un codeur réel, des tests métier, CI, contrôles de permissions, publication gouvernée, vérification du SHA, preuves runtime, reprise, supervision et enchaînement automatique. Les règles de branchement, de PR, de déploiement et de secrets proviennent **uniquement** du dépôt cible. Ne pas utiliser Codex. Vérifie par des runs réels, ne déclarer DONE qu'après attestation, documenter les écarts et fournir les liens SHA/CI. »

## Stratégie d'installation

1. **Audit d'autorité** : lire README/AGENTS/CLAUDE/GOVERNANCE, identifier le vrai système de travaux et l'état GitHub live. Aucune copie aveugle.
2. **Matrice de compatibilité** : associer projet → programmes → tâches → UTL → codeur → CI → déploiements au code existant. Réutiliser d'abord.
3. **Premier raccordement** : choisir les modules adaptés (moteur standard Python ou moteur natif déjà présent). Isoler adaptateurs du coeur. Ne pas reprendre les tables, chiffres, titres, documents ou fonds de FinancialData.
4. **Sécurité** : permissions minimales par job ; génération séparée des secrets de publication ; provenance des éléments historiques ; aucun code issu d'une tâche exécuté sans validation ; verrou/lease distribué selon l'hébergement.
5. **Test de bout en bout** : une tâche réellement admissible → modification réelle → tests métier → CI → publication selon gouvernance → attestation runtime → seconde tâche → reprise après interruption.
6. **Permanence** : registre durable dans le dépôt ou stockage gouverné existant, checkpoints, preuves, indicateurs d'échec, relance hébergée et alertes. La conversation ne constitue pas le runtime.
7. **Livraison** : consigner Continuity ID propre au dépôt cible, SHA, run IDs, checklist de non-régression, prochaines tâches réelles et blocages.

## Conventions adaptables

Les fichiers de référence `factory/engine.py`, `tasking.py`, `coder.py`, `publisher.py`, `CONTINUITY.md` et `ARRIVAL.md` montrent les responsabilités attendues. Reprendre les **interfaces et garanties** utiles, pas forcément les mêmes fichiers ni le même fournisseur de modèle. L'identité `FD-AUTONOMY-V1` est réservée au chantier FinancialData ; chaque autre dépôt reçoit sa propre racine de continuité non ambiguë.

L'installation automatique des droits GitHub ne doit jamais être présumée. Le nouveau dépôt peut imposer PR, revues, environnements protégés ou approbations. Les protéger au lieu de les supprimer.
