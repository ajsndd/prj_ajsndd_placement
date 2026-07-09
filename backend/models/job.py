from datetime import datetime, timezone
from database import db

class JobPosition(db.Model):
    __tablename__ = 'tblJobPosition'
    
    job_id = db.Column(db.Integer, primary_key=True)
    job_company_id = db.Column(db.Integer, db.ForeignKey('tblCompany.company_id'), nullable=False)
    job_title = db.Column(db.String, nullable=False)
    job_description = db.Column(db.String)
    job_location = db.Column(db.String)
    job_salary = db.Column(db.Float)
    job_type = db.Column(db.Integer, db.ForeignKey('tblJobType.job_type_id'))    
    job_skills_required = db.Column(db.String) 
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<JobPosition id={self.job_id}, title={self.job_title}, Company ID: {self.job_company_id}>'
