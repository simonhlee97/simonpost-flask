import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///simonpostcom.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False