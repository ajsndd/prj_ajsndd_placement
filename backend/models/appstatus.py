from datetime import datetime, timezone
from database import db

class AppStatus(db.Model):
    __tablename__ = 'tblAppStatus'
    
    status_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String, nullable=False) # Applied / Shortlisted / Selected / Rejected
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<AppStatus id={self.status_id}, name={self.status_name}>'