from datetime import datetime, timezone
from database import db

class PlacementStatus(db.Model):
    __tablename__ = 'tblPlacementStatus'
    
    status_id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String, nullable=False)  # pending/approved/rejected/closed
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<PlacementStatus ID: {self.status_id}, Name: {self.status_name}>'  
    