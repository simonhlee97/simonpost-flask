import os


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '72try8u6r54e4s3wdy(*(!mn982323u'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///simonpostcom.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False