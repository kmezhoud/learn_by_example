from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Creates the application object 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digin.db'
db = SQLAlchemy(app)

# Import Views from the app module. (DO NOT Confuse with app variable)
from app import views

# Import is at the end to avoid circular reference
