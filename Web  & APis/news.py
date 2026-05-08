import requests

api_key = "9d5c5a09df9246c0bbda7c952bd72c96"
keyword = "war"
url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&pageSize=5"

data = requests.get(url).json()
articles = data["articles"]

for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")