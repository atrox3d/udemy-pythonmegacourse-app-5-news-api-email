import requests
from secret.newsapi_apikey import API_KEY
from api_cache import APICache


def get_data(url, use_cache=False):
    cache = APICache(url)
    if use_cache and cache:
        print('using cache...')
        data = cache
    else:
        print('using requests...')
        request = requests.get(url)
        data = request.json()
        cache.update(data)
    return data


url = f'https://newsapi.org/v2/everything?q=tesla' \
      f'&from=2022-11-20&sortBy=publishedAt' \
      f'&apiKey={API_KEY}'

if __name__ == '__main__':
    data = get_data(url, use_cache=True)

