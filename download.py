import requests 

USER_AGENT = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36"
def get(url):
    return requests.get(
        url = url,
        headers = {"User-Agent" : USER_AGENT}
    )

