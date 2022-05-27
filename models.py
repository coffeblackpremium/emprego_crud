import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

year_in_school = ('1°Ano', '2°Ano', '3°Ano')
year_in_school_enum = Enum(*year_in_school, name="year_in_school")

class SchoolModel(db.Model):
    __tablename__ = "table"

    id_student = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    year_school = db.Column(db.String(5))
    ra = db.Column(db.Integer())
    age = db.Column(db.Date())

    def __init__(self, id_student,name, age, year_school, ra):
        self.id_student = id_student
        self.name = name
        self.year_school = year_school
        self.ra = ra
        self.age = age

    def __repr__(self):
        return f'{self.name}'