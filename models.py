
from flask_login import UserMixin
import pyotp

from extensions import db





class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=False, default=pyotp.random_base32)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    borrower_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    due_date = db.Column(db.String(100), nullable=True)
    pickup_location = db.Column(db.String(150), nullable=True)
