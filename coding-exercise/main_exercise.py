import mailer
from main import get_data, url

data = get_data(url, use_cache=True)
print(data)

message = ""
for article in data['articles']:
    title = article['title']
    description = article['description']

    message += f'Title: {title}\n'
    message += f'Description: {description}\n\n'

mailer.send_mail("top news for today", message)
