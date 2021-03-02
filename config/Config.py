import os

class Development():
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@127.0.0.1:5432/postgres'
    SECRET_KEY = 'Jaye7eus'
    DEBUG = True

class Production():
    SQLALCHEMY_DATABASE_URI='postgres://uifqdutdeweaat:e6698777df9621e9b42442f6a5d165ccf1ec968499999c4481ad67c33509082b@ec2-54-242-43-231.compute-1.amazonaws.com:5432/d8760d3pl0q05b'
    SECRET_KEY = '1234'
    DEBUG = False
