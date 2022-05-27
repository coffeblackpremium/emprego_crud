from flask import Flask, Response, request, render_template, url_for, redirect, abort, config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum
from models import db, SchoolModel
from flask_mysqldb import MySQL
from models import year_in_school
from flask_migrate import Migrate
from generate_ra import generate_ra
import random


#App Create
app = Flask(__name__)

#Database
db.init_app(app)


## Migrations
migrate = Migrate()
migrate.init_app(app, db)


app.config.from_object('config.Config')


@app.route('/registrar', methods=['GET','POST'])
def registrar():
    year_schools = ['1°Ano', '2°Ano', '3°Ano']
    if request.method == 'GET':
        return render_template("register/create.html", year_schools=year_schools)
    
    if request.method == 'POST':
        id_student = request.form['id_student']
        name = request.form['name']
        age = request.form['age']
        year_school = request.form['year_school']
        ra = generate_ra()
        school = SchoolModel(id_student=id_student,name=name, age=age, year_school=year_school, ra=ra)
        db.session.add(school)
        db.session.commit()
        return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    schools = SchoolModel.query.all()
    return render_template("index.html", schools = schools)

@app.route('/<int:id>')
def show(id):
    schools = SchoolModel.query.filter_by(id_student=id).first()
    if schools:
        return render_template('students/show_student.html', schools=schools)
    return f'O Aluno de ID = {id} não existe'

@app.route('/<int:id>/update', methods = ['GET', 'POST'])
def update(id):
    year_schools = ['1°Ano', '2°Ano', '3°Ano']
    schools = SchoolModel.query.filter_by(id_student=id).first()
    if request.method == 'POST':
        if schools:
            db.session.delete(schools)
            db.session.commit()

            id_student = request.form['id_student']
            name = request.form['name']
            age = request.form['age']
            year_school = request.form['year_school']
            ra = generate_ra()
            schools = SchoolModel(id_student=id, name=name, age=age, year_school=year_school, ra=ra)

            db.session.add(schools)
            db.session.commit()
            return redirect(f'/')
        return f'O Aluno de ID= {id} não existe'
    return render_template('students/update_student.html', schools=schools, year_schools=year_schools)

@app.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    schools = SchoolModel.query.filter_by(id_student=id).first()
    if request.method == 'POST':
        if schools:
            db.session.delete(schools)
            db.session.commit()
            print('Deletou')
            return redirect('/')
        abort(404)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()