import requests


def fetch(url):
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return res.json()
        else:
            print(f"Xato: {url} => {res.status_code}")
            return None
    except Exception as e:
        print(f"Internet muammo: {url} => {e}")
        return None