from datetime import datetime, timezone
from database import db

class Placement(db.Model):
    __tablename__ = 'tblPlacement'
    
    placement_id = db.Column(db.Integer, primary_key=True)
    placemnt_company_id = db.Column(db.Integer, db.ForeignKey('tblCompany.company_id'), nullable=False)
    placemnt_student_id = db.Column(db.Integer, db.ForeignKey('tblStudent.student_id'), nullable=False)
    placemnt_job_id = db.Column(db.Integer, db.ForeignKey('tblJobPosition.job_id'), nullable=False)
    placemnt_position = db.Column(db.String, nullable=False)
    placement_eligibility_criteria = db.Column(db.String, nullable=False)
    placemnt_salary = db.Column(db.Float)
    placement_application_deadline = db.Column(db.DateTime)
    placemnt_joining_date = db.Column(db.DateTime)
    placment_status = db.Column(db.Integer, db.ForeignKey('tblPlacementStatus.status_id'), nullable=False) # Applied / Shortlisted / Selected / Rejected
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Placement id={self.placement_id}, Company ID: {self.placemnt_company_id}, Student ID: {self.placemnt_student_id}, Job ID: {self.placemnt_job_id}>'
        