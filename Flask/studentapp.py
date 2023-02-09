from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
#db = SQLAlchemy(app)

@app.route('/')

def index():
    return "Welcome to Student Info App"