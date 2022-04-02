from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Account(db.Model):   
    __tablename__ = 'Account'


    name = db.Column(db.String(45), nullable=False)
    ID = db.Column(db.String(45), primary_key=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)  
    gender = db.Column(db.String(45), nullable=False)
    birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(45), nullable=False)

    def __init__(self, name, ID, password, gender, birth, email):
        self.name = name
        self.ID = ID
        self.password = password
        self.gender = gender
        self.birth = birth
        self.email = email

class Preference(db.Model):

    __tablename__ = 'preference'

    id = db.Column(db.String(45), primary_key=True, nullable=False)
    preference1 = db.Column(db.String(45), nullable=True)  
    preference2 = db.Column(db.String(45), nullable=True)
    preference3 = db.Column(db.Date, nullable=True)

    def __init__(self, id, preference1, preference2, preference3):
        self.id = id
        self.preference1 = preference1
        self.preference2 = preference2
        self.preference3 = preference3