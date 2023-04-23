import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    FLASK_RUN_PORT=8080
    FLASK_RUN_HOST="127.0.0.1"
