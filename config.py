import os

class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitchuser:12345@localhost/pitchez' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'   

class ProdConfig(Config):
    """
    Production configuration child class
    """
    # SQLALCHEMY_DATABASE_URI = $(heroku config:get DATABASE_URL -a macypitch)  
    SQLALCHEMY_DATABASE_URI =  os.environ.get("DATABASE_URL")

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitchuser:12345@localhost/pitchez'
    

class DevConfig(Config):
    """
    Development config child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitchuser:12345@localhost/pitchez'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}