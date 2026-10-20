from azure.identity import DefaultAzureCredential,ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from requests.exceptions import HTTPError,Timeout,RequestException
from azure.core.exceptions import HttpResponseError, ServiceRequestError
import json,requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()



print("----Attemping Azure Key Vault Operations-------")
try:
    credentials=DefaultAzureCredential()
    vault_url=os.environ['VAULT_URL']
    secret_id=os.environ['SECRET_ID']

    secret_name="DemoKey"
    client=SecretClient(vault_url=vault_url,credential=credentials)
    secret=client.get_secret(secret_name)
    print(f"Successfully retrieved secret '{secret_name}' from Key Vault.")

except HttpResponseError as er:
    status=er.status()
    if status and status>=500:
        print(f"Server Issue Due to Status Eror of{status}")

    elif status==400:
        print(f"Error: Secret '{secret_name}' was not found in the vault.")
    else:
        print(f"Error Occured for {secret_name}")

except ServiceRequestError as er:
    print("Due to network issue Failed !!")

try:
    print("----Attempting Api Operations-----")
    #Call a Public API"
    url="https://world.openpetfoodfacts.org/api/v0/product/20106836.json"

    response=requests.get(url,timeout=4.0)
    response.raise_for_status
    #Parse THE DATA
    data=response.json()

    print(f"Code:",data.get('code'))

except Timeout:
    print("The Time Limit Has Benn Exceeded")
except HTTPError as er:
    status=er.raise_for_status()
    if status>=500 or status>=400:
        print(f"Server Has Been Low Due Due Status Code of {status}")
    else:
        print("TRY Again")

except RequestException as er:
    print(f"Network Issue due to {er}")
