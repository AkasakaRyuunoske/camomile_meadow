import os

print("Configuration was called")
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "os.environ.get('SECRET_KEY')"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/garden'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
