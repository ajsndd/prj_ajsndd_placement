from datetime import datetime, timezone
from database import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'tblUser'
    
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_name = db.Column(db.String, nullable=False)
    usr_email = db.Column(db.String, unique=True, nullable=False)
    usr_password = db.Column(db.String, nullable=False)
    usr_role = db.Column(db.Integer, db.ForeignKey('tblRole.role_id'), nullable=False)
    usr_description = db.Column(db.String)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f'<User name={self.usr_name}, id={self.usr_id}>'
    
    def set_password(self, password):
        self.usr_password = generate_password_hash(password)  
    def check_password(self, password):
        return check_password_hash(self.usr_password, password)

        