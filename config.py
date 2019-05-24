import os

class Config:
    """
    General configuration child class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://christine:mulish@localhost/pitches_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://christine:mulish@localhost/pitches'

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
    