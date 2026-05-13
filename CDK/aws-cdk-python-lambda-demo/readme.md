
# AWS CDK Beginner Lab – S3 & Lambda with Python

Beginner-friendly hands-on lab using AWS CDK with Python to deploy AWS infrastructure as code.

This project demonstrates how to:
- Deploy an Amazon S3 bucket
- Deploy an AWS Lambda function
- Use AWS CDK with Python
- Generate CloudFormation templates automatically
- Manage infrastructure using Infrastructure as Code (IaC)

This is the first project in a larger AWS CDK learning series.

---

# Technologies Used

- AWS CDK
- Python 3
- AWS Lambda
- Amazon S3
- AWS CloudFormation
- Node.js
- AWS CLI

---

# Architecture

```text
Python CDK Application
        ↓
AWS CDK
        ↓
CloudFormation
        ↓
AWS Resources
   ├── S3 Bucket
   └── Lambda Function
