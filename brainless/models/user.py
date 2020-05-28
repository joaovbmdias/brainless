"""
User module containing the user class and related user methods
TODO: conditional rule for account.client_secret, mandatory only if necessary (OAuth2)
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db, CONST_OAUTH
from models.account import Account

class User(db.Model):
    """ User class """
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    accounts = db.relationship('Account', backref='user', lazy=True)

    def __init__(self, username, password, first_name=None, last_name=None):
        self.user_id = None
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class UserSchema(SQLAlchemyAutoSchema):
    """ UserSchema class """
    class Meta:
        """ Meta class classification """
        model = User
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
