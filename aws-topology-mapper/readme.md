# AWS Live Topology

# AWS Live Topology

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![AWS](https://img.shields.io/badge/AWS-boto3-orange)
![Diagrams](https://img.shields.io/badge/Diagrams-Graphviz-success)
![License](https://img.shields.io/badge/License-MIT-green)

Generate a **live network and infrastructure diagram** of your AWS environment automatically using **Python, boto3 and Diagrams (Graphviz)**.

This project scans your AWS account and produces a PNG diagram that reflects the **real architecture** at the time of execution.

No manual drawing. No Visio. No guesswork.

---

## What this script discovers

- VPCs
- Public and Private Subnets (deduced from Route Tables)
- Internet Gateway
- NAT Gateway (real Route Table → NAT links)
- EC2 / ECS instances placed in the correct subnets
- Application Load Balancers in public subnets
- RDS instances in private subnets
- VPC Endpoints

The diagram is a **live snapshot** of your AWS network and infrastructure.

Run it again later → the diagram updates with your changes.

---

## Requirements

- WSL / Linux / macOS
- Python 3.10+
- AWS CLI configured (`aws configure`)
- Graphviz installed

---

## 1. Install Graphviz

```bash
sudo apt update
sudo apt install graphviz -y
dot -V

