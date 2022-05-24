from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)


@app.route('/')
def hello():
    return "This is first Site!"