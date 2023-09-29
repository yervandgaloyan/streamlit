import logging
import requests

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)

app_id = "616310436467206"
app_secret = "a72586abdcd599710bace7b163220c7e"
user_short_token = "EAAIwhZCSjEgYBO38ZC02UrmWHxCJw8jWlFZAzR9PlKnLPW4DvWohgwblfnyLlZBjmnfa8A0ZBijDw5BOiZAe3lZAgSglrIY7KyZCDcK1GsCnHxRGx6vBgyS0Vk6UxZC1T9EoA2ZCYtzubtgDGzlAf4SJSD85TKxJS9yCPFe6nlTBCtcfH1yDoZBfkxAf1guAcooFOvfPiG2Fa9T"

url = "https://graph.facebook.com/oauth/access_token"

payload = {
    "grant_type": "fb_exchange_token",
    "client_id": app_id,
    "client_secret": app_secret,
    "fb_exchange_token": user_short_token,
}

try:
    response = requests.get(
        url,
        params=payload,
        timeout=5,
    )

except requests.exceptions.Timeout as e:
    logging.error("TimeoutError", e)

else:

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error("HTTPError", e)

    else:
        response_json = response.json()
        logging.info(response_json)
        user_long_token = response_json["access_token"]

"""
print(response_json)
{'access_token': 'EAAPxxxx', 'token_type': 'bearer', 'expires_in': 5183614}
"""