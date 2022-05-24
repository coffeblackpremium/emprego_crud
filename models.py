import enum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

db = SQLAlchemy()

year_in_school = ('1°Ano', '2°Ano', '3°Ano')
year_in_school_enum = Enum(*year_in_school, name="year_in_school")

class SchoolModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    student_ra = db.Column(db.String(7))
    age = db.Column(db.Date())
    year_school = db.Column(year_in_school_enum)

    def __init__(self, name,student_ra, age, year_school):
        self.name = name
        self.student_ra = student_ra
        self.age = age
        self.year_school = year_school

    def __repr__(self):
        return f'{self.name}:{self.ra_student}'