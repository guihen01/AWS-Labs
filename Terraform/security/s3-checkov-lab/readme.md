# 🔐 Terraform + Checkov Lab (AWS S3)

![Terraform](https://img.shields.io/badge/Terraform-1.5%2B-623CE4?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-S3-FF9900?logo=amazonaws&logoColor=white)
![Checkov](https://img.shields.io/badge/Security-Checkov-2E8B57)
![DevSecOps](https://img.shields.io/badge/DevSecOps-Workflow-blue)
![IaC](https://img.shields.io/badge/IaC-Terraform-informational)

🔐 Terraform + Checkov Lab (AWS S3)

📌 Overview
This project demonstrates a DevSecOps workflow using Terraform and Checkov to scan Infrastructure as Code (IaC) locally before deployment.
The lab intentionally starts with an insecure S3 bucket configuration, then applies security best practices after identifying issues with Checkov.
________________________________________
🎯 Objectives
•	Provision AWS infrastructure using Terraform
•	Identify security misconfigurations using Checkov
•	Apply remediation to meet cloud security best practices
•	Simulate a real-world DevSecOps workflow
________________________________________
🧱 Project Structure
terraform-checkov-lab/
├── provider.tf
├── main.tf
├── variables.tf
├── outputs.tf
├── environments/
│   └── dev/
│       └── terraform.tfvars
├── .checkov.yaml
└── README.md
________________________________________
⚙️ Prerequisites
•	Terraform >= 1.5
•	AWS CLI configured (aws configure)
•	Python 3.8+
Install Checkov:
pip install checkov
________________________________________
🚀 Usage
1. Initialize Terraform
terraform init
________________________________________
2. Review execution plan
terraform plan -var-file=environments/dev/terraform.tfvars
________________________________________
3. Run security scan
checkov -d .
🔎 This step scans Terraform code using Checkov to detect misconfigurations.
________________________________________
4. Apply infrastructure
terraform apply -var-file=environments/dev/terraform.tfvars
________________________________________
🚨 Initial Misconfigurations (Intentional)
The initial Terraform code includes:
•	Public S3 bucket access
•	No encryption enabled
•	No versioning
•	Missing logging configuration
👉 These issues are detected by Checkov during the scan.
________________________________________
🔒 Remediation (Secure Version)
The secure version includes:
•	Blocking all public access
•	Enabling server-side encryption (AES256)
•	Enabling versioning
•	Applying proper tagging
________________________________________
🔁 DevSecOps Workflow
Write Terraform → Plan → Scan (Checkov) → Fix → Apply
This simulates a real CI/CD pipeline with integrated security checks.
________________________________________
💡 Key Learnings
•	Infrastructure as Code security best practices
•	Terraform project structuring
•	Static analysis with Checkov
•	DevSecOps mindset (shift-left security)
________________________________________
🚀 Future Improvements
•	Remote backend (S3 + DynamoDB)
•	CI/CD integration (GitHub Actions)
•	Custom Checkov policies
•	Multi-environment support (dev / prod)
________________________________________
📂 Author
Henri Guillot
Cloud & Network Engineer
________________________________________
🏷️ Tags
Terraform AWS S3 DevSecOps Checkov Cloud Security
________________________________________

