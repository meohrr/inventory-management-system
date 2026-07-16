# 📦 Inventory Management System on AWS

A production-style Inventory Management System built with **Flask** and deployed on **Amazon Web Services (AWS)** using industry best practices such as Auto Scaling, Load Balancing, IAM Roles, Amazon RDS, CloudWatch Monitoring, Amazon S3 Backups, and AWS Systems Manager.

---

## 🚀 Project Overview

This project demonstrates how to deploy a scalable and highly available web application on AWS.

The application is hosted on Amazon EC2 behind an Application Load Balancer and Auto Scaling Group. The backend database is hosted on Amazon RDS MySQL. Monitoring is implemented using Amazon CloudWatch and Amazon SNS, while database backups are stored securely in Amazon S3. AWS Systems Manager Session Manager is used for secure server management without relying on SSH.

---

## 🏗️ AWS Architecture

> Add your architecture diagram here.

```
Users
   │
Application Load Balancer
   │
Auto Scaling Group
   │
Amazon EC2 (Flask + Gunicorn)
   │
Amazon RDS (MySQL)
   │
Amazon S3 (Database Backups)

CloudWatch → SNS Email Alerts

Systems Manager → Session Manager
```

---

## ☁️ AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon EC2 | Host the Flask application |
| Application Load Balancer | Distribute incoming traffic |
| Auto Scaling Group | Automatically replace unhealthy instances and scale capacity |
| Amazon RDS MySQL | Managed relational database |
| Amazon S3 | Store database backups |
| IAM | Secure access using roles and policies |
| Amazon CloudWatch | Monitor infrastructure and application health |
| Amazon SNS | Email notifications for alarms |
| AWS Systems Manager | Secure EC2 management without SSH |

---

## ✨ Features

- User Authentication
- Product Management
- Inventory Tracking
- Amazon RDS Database
- Application Load Balancer
- Auto Scaling
- CloudWatch Monitoring
- SNS Email Alerts
- IAM Role Based Access
- Secure Database Backups to Amazon S3
- AWS Systems Manager Session Manager

---

## 🛠️ Technologies Used

- Python
- Flask
- Gunicorn
- HTML
- Bootstrap
- MySQL
- Linux (Ubuntu)
- AWS

---

## 📂 Project Structure

```
inventory-management-system/
├── app.py
├── config.py
├── requirements.txt
├── templates/
├── static/
├── README.md
└── screenshots/
```

---

## 🔒 Security

- IAM Roles
- Least Privilege IAM Policies
- Private Amazon RDS
- Secure Session Manager Access
- Database Backup Strategy

---

## 📈 Monitoring

- CloudWatch Metrics
- CloudWatch Alarms
- Amazon SNS Email Notifications

---

## 💾 Backup & Recovery

Database backups are created using:

```bash
mysqldump
```

Backups are uploaded securely to Amazon S3 using an IAM Role attached to the EC2 instance.

---

## 📚 Skills Demonstrated

- AWS EC2
- VPC
- Application Load Balancer
- Auto Scaling
- Amazon RDS
- Amazon S3
- IAM
- CloudWatch
- SNS
- Systems Manager
- Linux Administration
- Flask Deployment
- Gunicorn

---

## 👨‍💻 Author

Sayooj ks
