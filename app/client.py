import requests

def fetch_url(url):
    response = requests.get(url, timeout=5)

    return response.status_code
