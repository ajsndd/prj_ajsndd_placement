from datetime import datetime, timezone
from database import db

class Gender(db.Model):
    __tablename__ = 'tblGender'

    gender_id = db.Column(db.Integer, primary_key=True)
    gender_name = db.Column(db.String, unique=True, nullable=False)
    gender_description = db.Column(db.String)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Gender {self.gender_name}, id={self.gender_id}>'
        