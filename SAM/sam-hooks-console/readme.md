LAB – AWS SAM / CodeDeploy Hooks

Objectif du lab
---------------
Déployer une fonction Lambda Python avec AWS SAM.
Mettre en place des hooks de déploiement afin de valider automatiquement le déploiement.

Objectifs détaillés
-------------------
1. Déployer une fonction Lambda Python via AWS SAM
2. Utiliser un hook pre-deploy pour :
   - valider le template CloudFormation
   - lancer des tests automatisés
3. Utiliser un hook post-deploy pour :
   - lire les outputs CloudFormation
   - exécuter un smoke test
4. Le déploiement doit échouer automatiquement si un hook échoue

Technologies utilisées
----------------------
- AWS SAM
- AWS CloudFormation
- AWS Lambda (Python)
- CodeDeploy hooks
- AWS CLI

Comportement attendu
--------------------
- Si la validation du template échoue, le déploiement est interrompu
- Si les tests pre-deploy échouent, le déploiement est interrompu
- Si le smoke test post-deploy échoue, le déploiement est marqué comme failed
