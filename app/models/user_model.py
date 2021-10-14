from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Usermodel(db.Model):
    name: str
    last_name: str
    email: str

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    last_name = db.Column(db.String(511), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(511), nullable=False)
    api_key = db.Column(db.String(511), nullable=False)
