from flask import Flask
# from flask_migrate import Migrate

app = Flask(__name__)
# migrate = Migrate(app, db) 

@app.route("/")
def all():
    return "select /signup or /login"

@app.route("/signup")
def signup():
    return "ok"