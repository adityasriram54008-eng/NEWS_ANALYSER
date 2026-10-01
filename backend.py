import requests

API_KEY = "9e5609838c2c482491361790dec782ab"

def get_info(topic):
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content
