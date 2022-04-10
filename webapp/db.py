
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from app import app
import os

load_dotenv()

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASENAME=os.getenv('DATABASENAME')
HOSTNAME =os.getenv('HOSTNAME')

DB_URL = 'postgresql://{0}:{1}@{2}:5432/{3}'.format(USER,PASSWORD,HOSTNAME,DATABASENAME)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

# migrate = Migrate(app, db) 

# def get_db(db):
#     try:
#         db = db.
