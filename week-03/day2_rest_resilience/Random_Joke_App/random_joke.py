import json
import requests

url="https://official-joke-api.appspot.com/random_joke"
print(f"SENDING HTTP REQUEST TO :{url}")

response=requests.get(url)

print(f" status code:{response.status_code}")

if response.status_code==200:
    print("Success! The server understood and processed the request.\n")

    print("---Parse Into Dictionory----")
    print(response.text)



    data=response.json()
    print("---Jokes-----")
    print(f"Name:{data.get("setup")}")
    print(f"Username:{data.get("punchline")}")


else:
    print("the joke is not been has got a error")

