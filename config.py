import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-is-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASET_URL') or \
        "mysql+pymysql://admin:134679as!#@myflaskdb.ch8eewmwhrfk.us-east-2.rds.amazonaws.com:3306/myFlaskApp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['rpgxp13@gmail.com']