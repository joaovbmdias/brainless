"""
Configuration module for the Brainless application
Contains all globally used contants and objects
"""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy

# providers
CONST_APPLE = 'APPLE'
CONST_GOOGLE = 'GOOGLE'
CONST_DOIST = 'DOIST'

# account types
CONST_CALENDAR = 'CALENDAR'
CONST_TASK = 'TASK'

# authentication types
CONST_OAUTH='OAUTH2'

# configurations
CONST_PERIOD = 10

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connexion_app = connexion.App(__name__, specification_dir=os.path.join(basedir, 'swagger'))

#get the underlying flask app
app = connexion_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'brainless.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Read the swagger.yml file to configure the endpoints
connexion_app.add_api('swagger.yaml')
