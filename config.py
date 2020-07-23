import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    MARKET_BASE_PATH = '/market-data/final/'
    MARKET_PATH_REALIZED_MARKET_CAP = MARKET_BASE_PATH + 'realized_market_cap/'
    MARKET_PATH_TOKEN_HOLDER_STATS = MARKET_BASE_PATH + 'token_holder_stats/'
    MARKET_PATH_TOP_TOKEN_HOLDER = MARKET_BASE_PATH + 'top_token_holder/'
    MARKET_PATH_TOP_TOKEN_HOLDER_NORMALIZED = MARKET_BASE_PATH + 'top_token_holder_normalized/'

    TERRA_BASE_PATH = '/terra-data/final/'
    TERRA_PATH_GENERAL = TERRA_BASE_PATH + 'general'
    TERRA_PATH_PAYMENTS = TERRA_BASE_PATH + 'payments'
    TERRA_PATH_TRANSACTIONS = TERRA_BASE_PATH + 'transactions'
    TERRA_PATH_USER = TERRA_BASE_PATH + 'user'
    TERRA_PATH_ROLLING_RETENTION = TERRA_BASE_PATH + 'rolling_retention'

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
