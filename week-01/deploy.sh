#!/bin/bash
# Automated Azure Deployment Script

RESOURCE_GROUP="rg-demo1-dev"
LOCATION="eastus"
STORAGE_NAME="storageaccdemo011"

echo "Creating resource group..."
az group create --name rg-demo1-dev --location eastus

echo "Creating storage account..."
az storage account create --name storageaccdemo011 --resource-group rg-demo1-dev  --location eastus --sku Standard_LRS

echo "Deployment completed successfully."
