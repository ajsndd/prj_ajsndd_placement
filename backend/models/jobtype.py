from datetime import datetime, timezone
from database import db

class JobType(db.Model):
    __tablename__ = 'tblJobType'
    
    job_type_id = db.Column(db.Integer, primary_key=True)
    job_type_name = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<JobType id={self.job_type_id}, name={self.job_type_name}>'
