# Resilient Azure API Client

A production-grade Python utility designed to interface securely with Azure services via `DefaultAzureCredential`, featuring robust error handling, schema response checking, and exponential backoff retry policies.

## Features
- **Secure Authentication:** Integrates with Azure Key Vault using managed identity rules (`DefaultAzureCredential`).
- **Resilience:** Gracefully handles timeouts, rate limits (429), and server crashes (500) using exponential backoff.
- **Strict Schema Enforcement:** Fails fast with explicit custom exceptions on malformed payloads.
- **Structured Logging:** Zero print statements; completely auditable tracking via Python's standard `logging` library.

##HOW TO RUN 
-create a python environment- python -m venv venv
-activate environments in windows-venv\Scripts\Activate
-install packages required -pip freeze >requirements.py
-run python main.py
