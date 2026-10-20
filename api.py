import requests
from requests.exceptions import HTTPError,RequestException,Timeout
import datetime
import json 

try:
    #Call A Public Api 
    url="https://world.openpetfoodfacts.org/api/v0/product/20106836.json"
    
    response=requests.get(url,timeout=3.0)
    response.raise_for_status()
#parse the json 
    data=response.json()
    print(f"CODE :",data.get('code'))


except Timeout:
    print("Time has been Exceeded Try Next Time :")
except HTTPError as er:

    status=er.response.status_code
    print(f"HTTP Error occurred: Status code {status}")
    if status<=500 or status<=400:
        print("Server is Down {er.status}")

    if status<=400:
        print("Something Went wrong ")

except RequestException as er:
    print(f"network error occured:{er}")


    







