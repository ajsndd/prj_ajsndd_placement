from datetime import datetime, timezone
from database import db

class Role(db.Model):
    __tablename__ = 'tblRole'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, unique=True, nullable=False)
    role_description = db.Column(db.String)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Role {self.role_name}, id={self.role_id}>'