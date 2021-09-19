from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

"""
HOW TO MIGRATE - PT ONE

Uncomment flask_migrate, flask_script imports.
Uncomment migrate, manager, and mager.add Objects

Goto Models.py file
"""

#from flask_migrate import Migrate, MigrateCommand
#from flask_script import Manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '69420Vibe'

db = SQLAlchemy(app)
#migrate = Migrate(app, db)

#manager = Manager(app)
#manager.add_command('db', MigrateCommand)#

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from cghoa import routes

