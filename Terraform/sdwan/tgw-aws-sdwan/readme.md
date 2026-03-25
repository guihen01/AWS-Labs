# 🚀 Terraform Lab # — AWS Modular Architecture (Transit Gateway)

![Terraform](https://img.shields.io/badge/Terraform-1.0+-623CE4?logo=terraform)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazonaws)
![IaC](https://img.shields.io/badge/IaC-Terraform-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)


## 📌 Overview
This project demonstrates a **production-style Terraform architecture** using a modular approach.
The goal is to design a scalable and reusable infrastructure on AWS, based on a **Hub & Spoke model with Transit Gateway**.

## 🏗️ Architecture

- 3 VPCs:
- PROD
- DEV
- EDGE (cEdge simulation)
- 1 Transit Gateway (central hub)
- VPC Attachments
- EC2 instances (SD-WAN simulation)

👉 The Transit Gateway enables communication between all VPCs.

## 🧠 Design Principles

- Modular architecture (reusable components)
- Environment separation (dev / prod ready)
- Scalable infrastructure
- Clean and maintainable code
## ⚙️ Requirements

- Terraform >= 1.0
- AWS Account
- AWS CLI configured

## 🚀 Deployment

```bash
cd environments/dev

terraform init
terraform validate
terraform plan
terraform apply
🧪 Tests
✅ Terraform checks
•	terraform validate 
•	terraform fmt 
•	terraform plan 
🌐 Network tests
•	Ping between VPCs (DEV ↔ PROD ↔ EDGE) 
•	Validate routing via Transit Gateway 
•	Traceroute between instances

