from datetime import datetime, timezone
from database import db

class Application(db.Model):
    __tablename__ = 'tblApplication'
    
    app_id = db.Column(db.Integer, primary_key=True)
    app_job_id = db.Column(db.Integer, db.ForeignKey('tblJobPosition.job_id'), nullable=False)
    app_student_id = db.Column(db.Integer, db.ForeignKey('tblStudent.student_id'), nullable=False)
    app_placement_id = db.Column(db.Integer, db.ForeignKey('tblPlacement.placement_id'), nullable=True)
    app_status = db.Column(db.Integer, db.ForeignKey('tblAppStatus.status_id'), nullable=False) # Applied / Shortlisted / Selected / Rejected
    app_date = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Application ID: {self.app_id}, Job ID: {self.app_job_id}, Student ID: {self.app_student_id}, Status: {self.app_status}, Placement ID: {self.app_placement_id}>'