import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class BaseConfig(object):
    JSON_SORT_KEYS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEVELOPMENT')


class LocalConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_LOCAL')


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PRODUCTION')


class TestingConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TESTING')