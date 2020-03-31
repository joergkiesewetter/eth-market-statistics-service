import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    BASE_PATH = '/data/final/'
    PATH_REALIZED_MARKET_CAP = BASE_PATH + 'realized_market_cap/'
    PATH_TOKEN_HOLDER_STATS = BASE_PATH + 'token_holder_stats/'
    PATH_TOP_TOKEN_HOLDER = BASE_PATH + 'top_token_holder/'
    PATH_TOP_TOKEN_HOLDER_NORMALIZED = BASE_PATH + 'top_token_holder_normalized/'


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
