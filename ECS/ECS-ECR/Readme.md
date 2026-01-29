# 🚀 Lab AWS – Docker → ECR

Premier lab pratique pour préparer une image **Docker WordPress** destinée à un futur déploiement sur **ECS Fargate**.

---

## 🎯 Objectifs

- ✅ Créer un **repository ECR**
- ✅ Tester localement l’image Docker
- ✅ Pousser l’image vers **AWS ECR**

> Focus volontaire sur **Docker & ECR**.  
> Le déploiement sur **ECS Fargate** arrive dans le prochain lab.

---

## 🛠️ Technologies

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=FF9900)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![ECR](https://img.shields.io/badge/ECR-FF9900?style=flat-square)
![Fargate](https://img.shields.io/badge/Fargate-FF9900?style=flat-square)

---

## 📝 Pré-requis

- Compte AWS avec droits pour ECR
- Docker installé sur ta machine
- AWS CLI configuré (`aws configure`)

---

## 🚀 Étapes du lab

### 1️⃣ Créer un repository ECR

```bash
aws ecr create-repository --repository-name wordpress-lab --region ca-central-1


docker build -t wordpress-lab .
