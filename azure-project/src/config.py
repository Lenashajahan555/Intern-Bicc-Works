import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ENDPOINT = os.getenv("API_ENDPOINT", "https://resource.openai.azure.com/opena/v1")
    KEY_VAULT_URL = os.getenv("KEY_VAULT_URL", "https://keyvaultname.vault.azure.et/")
    SECRET_NAME = os.getenv("SECRET_NAME", "name")
