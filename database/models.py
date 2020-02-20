from .db import db;
from flask_bcrypt import generate_password_hash, check_password_hash;

class Employee(db.Document):
    # id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True,unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)

class User(db.Document):
    username = db.StringField(required=True,unique=True)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8');
    def check_password(self,password):
        return check_password_hash(self.password,password)
