class Config:
    '''
    General configuration parent class
    '''
    ALL_NEWS_API_URL ='https://newsapi.org/v2/sources?apiKey=00f22307b89f4bebb7e7c6cc4dc67921'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=00f22307b89f4bebb7e7c6cc4dc67921'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True