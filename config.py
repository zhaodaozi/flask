# encoding: utf-8
import os

# session secret key
SECRET_KEY = os.urandom(24)

#mysql config ,mysql version 5.6.42
HOSTNAME = "127.0.0.1"
USERNAME = "root"
PASSWORD = "root"
PORT = "3306"
DATABASE = "flask"
DB_URI = "mysql+mysqldb://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8".format(USERNAME=USERNAME,
                                                                                                  PASSWORD=PASSWORD,
                                                                                                  HOSTNAME=HOSTNAME,
                                                                                                  PORT=PORT,
                                                                                                  DATABASE=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True
