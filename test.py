from os import environ, path
from dotenv import load_dotenv

load_dotenv()

user = environ.get('USERDB')
password = environ.get('PASSWORD')
server = environ.get('SERVER')
db_name = environ.get('DB_NAME')
print(user, password, server, db_name)