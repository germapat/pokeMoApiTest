import requests

def poke_api(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return {}