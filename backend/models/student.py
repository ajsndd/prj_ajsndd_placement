from datetime import datetime, timezone
from database import db

class Student(db.Model):
    __tablename__ = 'tblStudent'
    
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String, unique=True, nullable=False)
    student_email = db.Column(db.String, unique=True, nullable=False)
    student_phone = db.Column(db.String)
    student_dob = db.Column(db.Date)
    student_gender = db.Column(db.Integer, db.ForeignKey('tblGender.gender_id'), nullable=False)
    student_college = db.Column(db.String)
    student_branch = db.Column(db.String)
    student_year_of_passing = db.Column(db.Integer)
    student_education = db.Column(db.String)
    student_cgpa = db.Column(db.Float)
    student_skills = db.Column(db.String)
    student_resume = db.Column(db.String)
    student_user_id = db.Column(db.Integer, db.ForeignKey('tblUser.usr_id'), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Student name={self.student_name}, id={self.student_id}, usr_id={self.student_user_id}>'
        