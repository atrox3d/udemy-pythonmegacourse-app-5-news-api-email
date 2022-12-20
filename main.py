import requests
from secret.newsapi_apikey import API_KEY
from api_cache import APICache
import mailer


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


if __name__ == '__main__':
    topic = "tesla"
    url = f'https://newsapi.org/v2/everything?' \
          f'q={topic}' \
          f'&from=2022-11-20' \
          f'&language=en' \
          f'&pageSize=20' \
          f'&sortBy=publishedAt' \
          f'&apiKey={API_KEY}'

    data = get_data(url, use_cache=True)
    print(len(data['articles']))
    print(data)

    message = ""
    for article in data['articles'][:20]:
        title = article['title']
        description = article['description']
        link = article['url']

        message += f'Title: {title}\n'
        message += f'Description: {description}\n'
        message += f'{link}\n\n'

    mailer.send_mail("top news for today", message)

