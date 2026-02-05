# 📦 AWS SAM / Lambda — Lab avec Hooks de déploiement

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&style=flat-square)
![Lambda](https://img.shields.io/badge/Lambda-Function-purple?logo=aws-lambda&style=flat-square)
![SAM](https://img.shields.io/badge/AWS-SAM-blue?logo=amazon-aws&style=flat-square)
![Hooks](https://img.shields.io/badge/Deploy-Hooks-lightgrey?style=flat-square)
![DevOps](https://img.shields.io/badge/DevOps-Cloud-green?style=flat-square)

---

## 🎯 Objectif du lab

Lab volontairement **simple et pédagogique** autour du déploiement d’une fonction **AWS Lambda Python** à l’aide de **AWS SAM**, avec l’utilisation de **hooks de déploiement** pour automatiser les validations et les tests.

---

## 🧪 Objectifs techniques

- Déployer une fonction Lambda Python avec AWS SAM  
- Utiliser un hook **pre-deploy** pour :
  - valider le template CloudFormation
  - exécuter des tests automatisés
- Utiliser un hook **post-deploy** pour :
  - lire les outputs CloudFormation
  - exécuter un smoke test
- Forcer l’échec du déploiement si un hook échoue

---

## 🛠️ Technologies utilisées

- AWS Cloud
- AWS Lambda
- AWS SAM
- AWS CloudFormation
- AWS CLI
- CodeDeploy Hooks
- Python

---

## 📁 Structure du projet

## Structure du projet

![Structure du projet(docs/structure-projet.png)

---

## ✅ Comportement attendu

- Échec du hook **pre-deploy** → déploiement interrompu
- Échec des tests → stack non déployée
- Échec du hook **post-deploy** → déploiement marqué comme failed

