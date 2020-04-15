from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

Uploads = "./app/static/profilepics"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://fcbukntnschnkh:8bfad00e3784bc4a25a92a508814e3397265e57caaed9f4b6dbf148edde5ae23@ec2-52-87-135-240.compute-1.amazonaws.com:5432/dc0so6841jcak0
"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['Uploads'] = Uploads

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
