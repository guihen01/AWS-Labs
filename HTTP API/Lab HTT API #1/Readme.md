
# 🚀 Lab AWS – API Gateway + Lambda via YAML

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&style=flat-square) ![Lambda](https://img.shields.io/badge/Lambda-Function-purple?logo=aws-lambda&style=flat-square) ![API Gateway](https://img.shields.io/badge/API%20Gateway-HTTP%20API-blue?style=flat-square) ![YAML](https://img.shields.io/badge/YAML-OpenAPI-lightgrey?style=flat-square) ![DevOps](https://img.shields.io/badge/DevOps-Cloud-green?style=flat-square)

Lab pratique montrant comment faire fonctionner un **endpoint `/dev/hello`** importé via **YAML OpenAPI**, exactement comme si on le créait manuellement dans la console AWS.

---

## Objectifs du Lab

- 🔹 Créer une **Lambda simple** (`Hello World`)  
- 🔹 **Importer OpenAPI** dans **API Gateway**  
- 🔹 Ajouter la **permission Lambda → API Gateway**  
- 🔹 Déployer le **stage dev**  
- 🔹 Tester le endpoint → ✅ réponse OK  

💡 Ce lab met l’accent sur les étapes souvent oubliées lors du passage au YAML : **permissions et déploiement de stage**.

---

## Résultat attendu

```json
{
  "statusCode": 200,
  "body": "Hello from Lambda!"
}
