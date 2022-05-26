from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

server = environ.get('SERVER') 
user = environ.get('USERDB')
password = environ.get('PASSWORD')
db_name = environ.get('DB_NAME')

class Config:

    TESTING = True
    DEBUG = True
    FLASK_ENV = 'dev'
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    #Banco de Dados
    SQLALCHEMY_DATABASE_URI = fr'mysql+pymysql://{user}:{password}@{server}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False