"""
User module containing the user class and related user methods
TODO: add events and accounts relationship to users class
TODO: how to safely store user.password, account.client_id, account.client_secret
TODO: conditional rule for account.client_secret, mandatory only if necessary (OAuth2)
TODO: add account.user_id foreign key
"""

from datetime import datetime
from marshmallow_sqlalchemy import ModelSchema
from configuration import db

class Account(db.Model):
    """ Account class """
    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    provider = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    client_id = db.Column(db.String(32), nullable=False)
    client_secret = db.Column(db.String(32))
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, provider, user_id, client_id, client_secret):
        self.account_id = None
        self.name = name
        self.provider = provider
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

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

    def __init__(self, username, password, first_name, last_name):
        self.user_id = None
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        #self.events = []
        self.accounts = []
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class UserSchema(ModelSchema):
    """ UserSchema class """
    class Meta:
        """ Meta class classification """
        model = User
        sqla_session = db.session
        include_fk = True
        include_relationships = True

class AccountSchema(ModelSchema):
    """ AccountSchema class """
    class Meta:
        """ Meta class classification """
        model = Account
        sqla_session = db.session
        include_fk = True
        include_relationships = True
