import sys
from src.client import ResilientAPIClient
from src.config import Config

if __name__ == "__main__":
    print("\n==========================================")
    print("      RUNNING RESILIENT API CLIENT        ")
    print("==========================================\n")
    
    # Initialize client using endpoint from Config (.env or fallback)
    client = ResilientAPIClient(endpoint=Config.API_ENDPOINT)
    
    try:
        result = client.call_with_resilience(max_retries=3, timeout=5)
        print("\n--- [FINAL OUTPUT RECEIVED] ---")
        print(result)
        print("--------------------------------\n")
    except Exception as e:
        print(f"\n[EXECUTION HALTED]: {e}\n")
