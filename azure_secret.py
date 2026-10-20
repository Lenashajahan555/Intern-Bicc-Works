#import azure identity ,azure keyvault identity

from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv
import os

#load the envirnoments 
load_dotenv()

#Retrive the envirnoments
client_id= os.environ['APP_ID']
vault_url=os.environ['VAULT_URL']
tenent_id=os.environ['TENANT_ID']
client_secret=os.environ['SECRET_ID']

secret_name="DemoKey"


#CREATE CREDENTIALS 
credentials=ClientSecretCredential(
    client_id=client_id,
    tenant_id=tenent_id,
    client_secret=client_secret)

#Create a secret client

secret_client=SecretClient(
    vault_url=vault_url,credential=credentials
)

#RETRIVE THE SECRET client
secret=secret_client.get_secret(secret_name)

#PRINT THE SECRET VALUE
print(f"The secret value:{secret.value}")