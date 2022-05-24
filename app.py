from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from models import db, SchoolModel
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object('config.Config')
mysql = MySQL(app)
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()

@app.route('/registrar')
def registrar():
    if request.method == 'GET':
        return render_template("register/create.html")
    
    if request.method == 'POST':
        student_ra = request.form['students_ra']
        name = request.form['name']
        age = request.form['age']
        year_school = request.form['year_school']
        school = SchoolModel(name=name, student_ra=student_ra, age=age, year_school=year_school)
        db.session.add(school)
        db.session.commit()
        return redirect('/')

@app.route('/')
def index():
    schools = SchoolModel.query.all()
    return render_template("index.html", schools = schools)


if __name__ == "__main__":
    app.run()