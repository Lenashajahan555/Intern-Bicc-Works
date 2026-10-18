
# Azure Automated Deployment Script

This repository contains an automated deployment script written for Microsoft Azure. The script streamlines resource provisioning while adhering to cloud security best practices.

---

## 🚀 Features
* **Automated Provisioning:** Quickly creates resource groups and storage accounts using the Azure CLI.
* **Security First:** Designed with zero hardcoded credentials, secret keys, or passwords.
* **Idempotent Teardown Ready:** Easily pair with cleanup commands to manage your cloud environment efficiently.

---

## 🛠️ Prerequisites
Before running the script, ensure you have the following installed and configured:
* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* Active Azure Subscription (logged in via `az login`)

---

## 📂 Project Structure
```text
├── deploy.sh       # Main Azure CLI deployment script
└── README.md       # Project documentation
