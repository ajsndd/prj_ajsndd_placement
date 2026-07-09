from datetime import datetime, timezone
from database import db

print("Loading Company model")
class Company(db.Model):
    __tablename__ = 'tblCompany'
    
    company_id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, unique=True, nullable=False)
    company_email = db.Column(db.String, unique=True, nullable=False)
    company_industry = db.Column(db.String)
    company_location = db.Column(db.String)
    company_address = db.Column(db.String)
    company_description = db.Column(db.String)
    company_website = db.Column(db.String)
    company_hr_contact_number = db.Column(db.String)
    company_user_id = db.Column(db.Integer, db.ForeignKey('tblUser.usr_id'), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))



    def __repr__(self):
        return f'<Company id={self.company_id}, name={self.company_name}, User ID: {self.company_user_id}>'
    
    