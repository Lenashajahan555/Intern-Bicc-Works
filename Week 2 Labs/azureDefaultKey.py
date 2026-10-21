#Import all the packages needed

from azure.identity import DefaultAzureCredential,CredentialUnavailableError
from azure.keyvault.secrets import SecretClient
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG)


#Create a DefaultCredential

try:
    credentials=DefaultAzureCredential()
    vault_url = os.environ["VAULT_URL"]
    secret_name="DemoKey"
    

    client=SecretClient(vault_url=vault_url,credential=credentials)
    secret=client.get_secret(secret_name)

    print(f"Secret Value:{secret.value}")

except CredentialUnavailableError as er:
    print("Failed Due TO Connetion")






