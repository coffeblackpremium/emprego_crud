from os import environ, path
from dotenv import load_dotenv
from flask_mysqldb import MySQL


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    TESTING = True
    DEBUG = True
    FLASK_ENV = 'dev'
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    #Banco de Dados
    MYSQL_HOST = environ.get('SERVER') 
    MYSQL_USER = environ.get('USERDB')
    MYSQL_PASSWORD = environ.get('PASSWORD')
    MYSQL_DB = environ.get('DB_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False