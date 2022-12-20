import requests
from secret.newsapi_apikey import API_KEY
from api_cache import APICache

url = f'https://newsapi.org/v2/everything?q=tesla' \
      f'&from=2022-11-20&sortBy=publishedAt' \
      f'&apiKey={API_KEY}'

USE_CACHE = True

cache = APICache(url)
if USE_CACHE and cache:
    print('using cache...')
    data = cache
else:
    print('using requests...')
    request = requests.get(url)
    data = request.json()
    print(data)
    cache.update(data)


