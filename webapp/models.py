from db import db
import enum 



class UserType(enum.Enum):
    TAX_PAYER = "Tax Payer"
    TAX_ACCOUNTANT = "Tax Accountant"
    ADMIN = "Admin"

class TaxDue(enum.Enum):
    PAID = "Paid"
    NEW = "New"
    DELAYED = "Delayed"

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    user_type = db.Column(db.Enum(UserType))

class TaxPayer(db.Model):
    pan_no = db.Column(db.Integer, primary_key = True)
    user = db.relationship('User')
    status = db.Column(db.Enum(TaxDue))
    tax_due = db.Column(db.Integer)

