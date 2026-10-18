import requests
from requests.exceptions import RequestException,Timeout,HTTPError

def get_checker():
    url="https://pokeapi.co/api/v2/pokemon/pikachu"
    try:

        response=requests.get(url,timeout=4.0)
        response.raise_for_status()
        check=response.json()

        print(f"Name:{check.get('name')}")
        print(f"Hieght:{check.get('height')}")
        print(f"Weight:{check.get('weight')}")

    except HTTPError as er:
        status_code= er.response.status_code
        if status_code>=500:
            print(f"Server Crashes{status_code}")
        else:
            print(f"Pokemon Does'nt Exist{status_code}")
    except Timeout:
        print(f"The Time Exceeds 4SEC Only")
    except RequestException as er:
        print(f"The Network Not Secured:{er} ")

if __name__=="__main__":
    get_checker()