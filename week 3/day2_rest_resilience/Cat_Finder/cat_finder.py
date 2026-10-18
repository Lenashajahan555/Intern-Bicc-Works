import requests
from requests.exceptions import Timeout,RequestException,HTTPError

def get_cat_find():
    url="https://catfact.ninja/fact](https://catfact.ninja/fact"

    print(f"Fetching a random cat fact with a 3-second timeout...\n")

    try:

        response=requests.get(url,timeout=3.0)

        response.raise_for_status()
        cat=response.json()

        print("---Find Fact-----\n")
        print(f"Fact:{cat.get('fact')}")
    except HTTPError as err:
        status_code = err.response.status_code
        print(f"HTTP Error occurred: Status code {status_code}")
        if status_code >= 500:
            print("-> Server-side error (500-level). Handled gracefully!")
        else:
            print("-> Page or resource not found.")

    except Timeout:
        print("The time Exceeds only for 3sec")
    except RequestException as err:
        print(f"network error occured:{err} ")


if __name__=="__main__":
    get_cat_find()
