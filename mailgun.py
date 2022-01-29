import requests
import json
def get_validate():
    return requests.get(
        "https://api.mailgun.net/v4/address/validate",
        auth=("api", "8754a381b4f02a24c4d9f82c5cd8bf89-054ba6b6-eacaee4e"),
        params={"address": "obohedward@gmail.com"})
# print(get_validate().json())
# https://emailverification.whoisxmlapi.com/api/v2?apiKey=at_LQvO4zBKs0miCOsLJsYyawo1zrgVk&emailAddress=support@whoisxmlapi.com

def validate():
    return requests.get(
        "https://emailverification.whoisxmlapi.com/api/v2?apiKey=at_LQvO4zBKs0miCOsLJsYyawo1zrgVk&emailAddress=obohedward@gmail.com")
print(validate().json())
