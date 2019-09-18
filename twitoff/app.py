#My application

from flask import Flask, render_template, request
from .models import db, User, Tweet
from decouple import config

#make our own app factory
def create_app():
    #create server
    app = Flask(__name__)

    #add config later:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['ENV'] = config('ENV')

    #add in database init later
    db.init_app(app)

    #create the route
    @app.route("/")

    #define the function
    def root():
        users = User.query.all()
        return render_template('base.html', title="Home", users=users)

    return app
