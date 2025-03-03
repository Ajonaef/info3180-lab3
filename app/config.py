import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ajonae$')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('Ma8bf83375ab1fd') 
    MAIL_PASSWORD = os.environ.get('9ee4332c63dae3') 
