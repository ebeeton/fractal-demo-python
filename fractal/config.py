""" Application configuration. """
from os import environ

class Config():
    """ Configure the application. """
    SECRET_KEY = environ.get('SECRET_KEY') or 'Demo20211127'
