from .db import db

class Employee(db.Document):
    # id = db.StringField(required=True, unique=True)
    name = db.StringField(required=True,unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)