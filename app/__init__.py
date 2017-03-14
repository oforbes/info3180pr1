import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://projone:projone@localhost/projone"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
db=SQLAlchemy(app)
db.create_all()

from app import views, models
