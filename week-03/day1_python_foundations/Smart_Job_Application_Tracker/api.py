import requests
import time
from requests.exceptions import HTTPError, RequestException, Timeout

from config import APP_URL, MAX_RETRIES, TIMEOUTS
from logger import logger


def get_api_app():
    for attempt in range(MAX_RETRIES+1):
        try:
            response=requests.get(APP_URL,timeout=TIMEOUTS)

            response.raise_for_status()
            data=response.json()

            if not isinstance(data,dict):
                raise ValueError("Value Error")
            if 'title' not in data or 'completed'not in data:
                raise FileNotFoundError()
            print("API TITLE:",data['title'])
            print("Completed:",data['completed'])
            return data
        except Timeout:
            logger.warning(f"Attempt {attempt + 1}: Request timed out.")
        except HTTPError as er:
            status=er.response.status_code
            if status<500:
                logger.error("Succeffully loging in %s",er)
                break
            else:
                logger.warning("Somethin went wrong %s",er)
        except RequestException as er:
            logger.error("API ERROR:%s",er)
            break
        if attempt<MAX_RETRIES:
            time.sleep(2**attempt)

    print("API IS CURRENTLTY UNAVALIBALE")
    logger.error("API is currently unavailable after retries.")


