import urllib.request, json
from .models import Articles, News

#getting api key

api_key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['ALL_NEWS_API_URL']
    articles_url = app.config ['ARTICLES_BASE_URL']

