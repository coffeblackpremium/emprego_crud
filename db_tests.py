import mysql.connector
from os import environ, path
from dotenv import load_dotenv

mydb = mysql.connector.connect(
    host=str(environ.get("SERVER")),
    user=str(environ.get("USERDB")),
    passwd=str(environ.get("PASSWORD"))
)

my_cursor = mydb.cursor()

#my_cursor.execute("use school_crud")

my_cursor.execute("SHOW DATABASES")




for db in my_cursor:
    print(db)
