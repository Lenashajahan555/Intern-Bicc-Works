import json

from config import DATA_FILE
def load_application():
    try:
        with open(DATA_FILE,encoding="utf-8")as f:
            return  json.load(f)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        print("JSon Decorder Warning")

def save_application(applications):
    with open(DATA_FILE,'w',encoding="utf-8")as f:
        json.dump(applications,f,indent=4)

