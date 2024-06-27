import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'instance', 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
