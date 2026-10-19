import json

with open("config.json",'r',encoding="utf-8")as f:
    config=json.load(f)

DATA_FILE=config['data_file']
LOGGING=config['logg']
MAX_RETRIES=config["max_retries"]
TIMEOUTS=config["timeouts"]
APP_URL=config["app_url"]