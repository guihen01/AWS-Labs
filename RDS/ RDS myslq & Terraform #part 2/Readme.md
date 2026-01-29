# 🗄️ AWS RDS MySQL — Recréation du lab avec Terraform

![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?logo=terraform&style=flat-square)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&style=flat-square)
![RDS](https://img.shields.io/badge/Amazon%20RDS-Database-blue?style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql&style=flat-square)
![DevOps](https://img.shields.io/badge/DevOps-Cloud-green?style=flat-square)

Suite directe du lab précédent réalisé via **AWS CLI**, ce lab propose la **recréation exacte** d’une **base Amazon RDS MySQL**, cette fois en **Infrastructure as Code (IaC)** à l’aide de **Terraform**.

---

## 🎯 Objectifs du Lab

- ✅ Recréer la **même instance RDS MySQL** que dans le lab AWS CLI
- ✅ Comprendre la **structure minimale** d’un projet Terraform
- ✅ Maîtriser le cycle **`terraform init / plan / apply / destroy`**
- ✅ Valider le déploiement via des **vérifications post-création**

---

## 🧱 Architecture


---

## ⚙️ Prérequis

- AWS CLI configurée
- Terraform installé
- Un compte AWS actif

---

## 🚀 Workflow Terraform

```bash
terraform init
terraform plan
terraform apply
terraform destroy

