from datetime import datetime
from cghoa import db, login_manager
from flask_login import UserMixin


"""
HOW TO MIGRATE - PT TWO

Uncomment manager import
Uncomment manager.run()

In CMD run the following commands

python run.py db migrate
python run.py db upgrade
"""

#from cghoa import manager

@login_manager.user_loader
def loadUser(userID):
    return User.query.get(int(userID))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    imageFile = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.id}', {self.password})"

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(25), nullable=False, default="Coventry Glen")
    date = db.Column(db.DateTime(40), nullable=False, default=datetime.utcnow)
    dateText = db.Column(db.String(25), nullable=False, default=datetime.utcnow)
    timeText = db.Column(db.String(25), nullable=False)
    time = db.Column(db.Time(40), nullable=False)
    link = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f"Meeting('{self.host}', '{self.date}', '{self.time}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75), nullable=False)
    location = db.Column(db.String(25), nullable=False)
    timeText = db.Column(db.String(25), nullable=False)
    dateText = db.Column(db.String(25), nullable=False, default=datetime.utcnow)
    date = db.Column(db.DateTime(40), nullable=False, default=datetime.utcnow)
    time = db.Column(db.Time(40), nullable=False)

    def __repr__(self):
        return f"Event('{self.title}', '{self.location}', '{self.date}', '{self.time}')"

class MailingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))

    def __repr__(self):
        return f"{self.email}"

#manager.run()