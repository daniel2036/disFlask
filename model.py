from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Student(db.Model):
    __tablename__='student'
    student_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    roll_number=db.Column(db.String,unique=True,nullable=False)
    email=db.Column(db.String)
    first_name=db.Column(db.String,nullable=False)
    last_name=db.Column(db.String, nullable=False)
    courses=db.relationship('Course',backref='student',secondary='enrollments')

class Course(db.Model):
    __tablename__='course'
    course_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    course_code=db.Column(db.String,unique=True,nullable=False)
    course_name=db.Column(db.String,nullable=False)
    course_description=db.Column(db.String)

class Enrollments(db.Model):
    __tablename__='enrollments'
    enrollment_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    estudent_id=db.Column(db.Integer,db.ForeignKey('student.student_id'),nullable=False)
    ecourse_id=db.Column(db.Integer,db.ForeignKey('course.course_id'),nullable=False)
    students = db.relationship('Student',backref='student')
    courses = db.relationship('Course',backref='course')
 

 



