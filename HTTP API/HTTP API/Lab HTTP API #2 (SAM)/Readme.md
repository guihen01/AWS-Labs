
# 🚀 AWS Lab — SAM (Serverless Application Model) & HTTP API

![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&style=flat-square)
![SAM](https://img.shields.io/badge/AWS%20SAM-Serverless-blue?style=flat-square)
![Lambda](https://img.shields.io/badge/Lambda-Function-purple?logo=aws-lambda&style=flat-square)
![API Gateway](https://img.shields.io/badge/API%20Gateway-HTTP%20API-blue?style=flat-square)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.0-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&style=flat-square)
![IaC](https://img.shields.io/badge/IaC-Infra-red?style=flat-square)

Lab pratique démontrant le déploiement d’une **HTTP API** et d’une **fonction Lambda** en **Infrastructure as Code (IaC)** à l’aide de **AWS SAM**.

---

## 🎯 Objectifs du Lab

- Déployer une **HTTP API** et une **fonction Lambda** via **AWS SAM**  
- Définir l’infrastructure avec un **template YAML**  
- Déployer l’infrastructure via la **SAM CLI**  
- Exploiter la spécification **OpenAPI 3.0 (YAML)** pour l’API  

---

## 🧱 Technologies utilisées

- **AWS SAM** (Serverless Application Model)  
- **AWS Lambda**  
- **Amazon API Gateway** (HTTP API)  
- **OpenAPI 3.0**  
- **YAML**  
- **Python 3.11**  

---

## ⚙️ Prérequis

- Compte AWS actif  
- AWS CLI configurée  
- AWS SAM CLI installée  
- Python 3.x  
- Connaissances de base en YAML et OpenAPI  

---

## 🚀 Workflow rapide

```bash
# Construire l’application
sam build

✅ Résultat attendu

Une HTTP API fonctionnelle exposée via API Gateway, déclenchant une fonction Lambda, entièrement déployée via SAM YAML.
La réponse attendue pour un test simple :

{
  "statusCode": 200,
  "body": "Hello from Lambda!"
}
# Déployer avec guide interactif
sam deploy --guided

# Tester le endpoint HTTP API
curl https://<api-id>.execute-api.<region>.amazonaws.com/hello
