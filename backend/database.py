import os
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


BASE = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE, 'placement_portal.db')
SCHEMA = os.path.join(BASE, 'schema.sql')

from models.application import Application
from models.appstatus import AppStatus
from models.company import Company
from models.gender import Gender
from models.job import JobPosition
from models.jobtype import JobType
from models.placement import Placement
from models.placementstatus import PlacementStatus
from models.role import Role
from models.student import Student
from models.user import User

def db_exists():
    return os.path.exists(DB_PATH)

def drop_db():
    if db_exists():
        print('dropping database...', DB_PATH)
        os.remove(DB_PATH)

def reset_db():
    drop_db()
    create_db() 
    
def create_db(app):
    with app.app_context():
        print('creating new database...', DB_PATH)
        db.create_all()
        update_application_status()
        update_gender()
        update_jobtype()
        update_placement_status()
        update_role()
        update_user()

def init_db(app):
        print("Initializing the database..." + DB_PATH)
        if not db_exists():
            create_db(app)

def update_application_status():
    from models.appstatus import AppStatus
    applied = AppStatus(status_name="Applied")
    shortlisted = AppStatus(status_name="Shortlisted")
    rejected = AppStatus(status_name="Rejected")
    selected = AppStatus(status_name="Selected")
    db.session.add(applied)
    db.session.add(shortlisted)
    db.session.add(rejected)
    db.session.add(selected)
    db.session.commit()

def update_gender():
    from models.gender import Gender
    male = Gender(gender_name="Male")
    female = Gender(gender_name="Female")
    transgender = Gender(gender_name="Transgender")
    db.session.add(male)
    db.session.add(female)
    db.session.add(transgender)
    db.session.commit()

def update_jobtype():
    from models.jobtype import JobType
    full_time = JobType(job_type_name="Full-time")
    part_time = JobType(job_type_name="Part-time")
    internship = JobType(job_type_name="Internship")
    db.session.add(full_time)
    db.session.add(part_time)
    db.session.add(internship)
    db.session.commit()

def update_placement_status():
    from models.placementstatus import PlacementStatus
    pending = PlacementStatus(status_name="Pending")
    approved = PlacementStatus(status_name="Approved")
    rejected = PlacementStatus(status_name="Rejected")
    closed = PlacementStatus(status_name="Closed")
    db.session.add(pending)
    db.session.add(approved)
    db.session.add(rejected)
    db.session.add(closed)
    db.session.commit()


def update_role():
    from models.role import Role
    admin = Role(role_name="admin", role_description="Administrator")
    student = Role(role_name="student", role_description="Student")
    company = Role(role_name="company", role_description="Company")
    db.session.add(admin)
    db.session.add(student)
    db.session.add(company)
    db.session.commit()

def update_user():
    from models.user import User
    from models.role import Role
    admin_role = Role.query.filter_by(role_name="admin").first()
    if admin_role:
        admin_user = User(
            usr_name="admin",
            usr_email="admin@ajeesh.com",
            usr_password="admin",
            usr_description="Administrator user",
            usr_role=admin_role.role_id
        )
        db.session.add(admin_user)
        db.session.commit()

