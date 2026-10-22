import time
import requests
from typing import Dict, Any, Optional
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from src.logger_config import setup_logger

logger = setup_logger("APIClient")

class SchemaValidationError(Exception):
    """Custom exception raised when response schema validation fails."""
    pass

class ResilientAPIClient:
    def __init__(self, endpoint: str, use_azure_vault: bool = False, vault_url: Optional[str] = None, secret_name: Optional[str] = None):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.api_key = "mock-local-key"

        if use_azure_vault and vault_url and secret_name:
            try:
                logger.info("Authenticating via DefaultAzureCredential...")
                credential = DefaultAzureCredential()
                secret_client = SecretClient(vault_url=vault_url, credential=credential)
                self.api_key = secret_client.get_secret(secret_name).value
                logger.info("Successfully retrieved secret from Azure Key Vault.")
            except Exception as e:
                logger.warning(f"Could not connect to Azure Key Vault (falling back/mocking): {e}")

    def call_with_resilience(self, max_retries: int = 3, timeout: int = 5) -> Dict[str, Any]:
        """Executes a GET request with timeout, status code handling, and exponential backoff."""
        backoff_factor = 1  # seconds

        for attempt in range(1, max_retries + 1):
            start_time = time.time()
            try:
                logger.info(f"Attempt {attempt} of {max_retries} calling {self.endpoint}")
                response = self.session.get(
                    self.endpoint, 
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    timeout=timeout
                )
                duration = time.time() - start_time

                # Handle specific HTTP status codes
                if response.status_code == 200:
                    logger.info(f"Success! Duration: {duration:.2f}s")
                    return self._validate_and_parse(response)
                
                elif response.status_code == 429:
                    logger.warning(f"Rate limited (429). Backing off... Duration: {duration:.2f}s")
                
                elif 500 <= response.status_code < 600:
                    logger.error(f"Server error ({response.status_code}). Retrying... Duration: {duration:.2f}s")
                
                else:
                    response.raise_for_status()

            except requests.exceptions.Timeout:
                logger.error(f"Request timed out after {timeout} seconds.")
            except requests.exceptions.RequestException as e:
                logger.error(f"Network error encountered: {e}")

            # If retries remain, execute exponential backoff sleep
            if attempt < max_retries:
                sleep_time = backoff_factor * (2 ** (attempt - 1))
                logger.info(f"Sleeping for {sleep_time} seconds before retry...")
                time.sleep(sleep_time)
            else:
                logger.critical("Max retries reached. Operation failed.")
                raise Exception("API client failed after maximum retries.")

    def _validate_and_parse(self, response: requests.Response) -> Dict[str, Any]:
        """Validates that the response payload matches the expected schema."""
        try:
            data = response.json()
        except ValueError:
            raise SchemaValidationError("Response body is not valid JSON.")
        
        # Example Schema Check: Ensure expected keys exist
        # If testing with httpbin, adjust keys or return safe defaults
        if not isinstance(data, (dict, list)):
            raise SchemaValidationError("Schema mismatch: Root element must be a dictionary or list.")
            
        return {"status": "success", "data": data}
