from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    phone = db.Column(db.String(15))
    def get_id(self):
        return str(self.user_id)

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class FamilyMember(db.Model):
    __tablename__ = 'familymembers'
    member_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
        db.ForeignKey('users.user_id'))
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    relation = db.Column(db.String(50))

class Medicine(db.Model):
    __tablename__ = 'medicines'
    medicine_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
        db.ForeignKey('users.user_id'))
    member_id = db.Column(db.Integer,
        db.ForeignKey('familymembers.member_id'))
    category_id = db.Column(db.Integer,
        db.ForeignKey('categories.category_id'))
    name = db.Column(db.String(100))
    quantity = db.Column(db.Integer, default=1)
    purchase_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')

class Alert(db.Model):
    __tablename__ = 'alerts'
    alert_id = db.Column(db.Integer, primary_key=True)
    medicine_id = db.Column(db.Integer,
        db.ForeignKey('medicines.medicine_id'))
    user_id = db.Column(db.Integer,
        db.ForeignKey('users.user_id'))
    alert_type = db.Column(db.String(50))
    is_read = db.Column(db.Boolean, default=False)
