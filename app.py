from flask import Flask, Response, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from models import db, SchoolModel
from flask_mysqldb import MySQL
from models import year_in_school
import random

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

def generate_ra():
    numbers_ra = 0
    for i in range(0, 7):
        number_random = random.randrange(1000, 200000)
        numbers_ra += int(str(number_random) + str(i))
    return numbers_ra

with app.app_context():
    db.create_all()

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/registrar', methods=['GET','POST'])
def registrar():
    year_school = ['1°Ano', '2°Ano', '3°Ano']
    if request.method == 'GET':
        return render_template("register/create.html", year_school=year_school)
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        year_school = request.form['year_school']
        ra = generate_ra()
        school = SchoolModel(name=name, age=age, year_school=year_school, ra=ra)
        db.session.add(school)
        db.session.commit()
        return redirect('/')
@app.route('/')
def index():
    schools = SchoolModel.query.all()
    return render_template("index.html", schools = schools)


if __name__ == "__main__":
    app.run()