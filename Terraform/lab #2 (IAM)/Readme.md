# 🛠️ Terraform Lab — Création d’un rôle IAM pour Lambda

![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?logo=terraform&style=flat-square)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&style=flat-square)
![IAM](https://img.shields.io/badge/IAM-Role-blue?style=flat-square)
![Lambda](https://img.shields.io/badge/Lambda-Function-purple?logo=aws-lambda&style=flat-square)
![DevOps](https://img.shields.io/badge/DevOps-Cloud-green?style=flat-square)

Lab pratique montrant **la création d’un rôle IAM pour une fonction Lambda** sur AWS avec **Terraform**, permettant à la Lambda de gérer ses logs (log group, log stream et event).

---

## 📌 Objectifs

- Présenter la **méthode d’utilisation et de lancement de Terraform** avec un exemple simple
- Créer un **rôle IAM** dans AWS
- Attacher le rôle à une **fonction Lambda** pour lui permettre de créer des logs
- Mettre en pratique les principes de **l’Infrastructure as Code**

---

## ⚙️ Préalables

- OS : Windows  
- Compte AWS actif  
- Installer **AWS CLI**  
- Installer **Terraform**  
- Télécharger **terraform.exe** depuis [site officiel HashiCorp](https://developer.hashicorp.com/terraform)  
- Installer Terraform dans `C:\terraform`  

---

## ✅ Vérifications

```bash
# Vérifier Terraform
terraform -version

# Vérifier AWS CLI
aws --version

# Vérifier l'identité AWS
aws sts get-caller-identity

