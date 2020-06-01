"""
User module containing the user class and related user methods
TODO: conditional rule for account.client_secret, mandatory only if necessary (OAuth2)
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.account import Account
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_

class User(db.Model, Template):
    """ User class """
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=True)
    last_name = db.Column(db.String(32), nullable=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    accounts = db.relationship('Account', backref='user', lazy=True)

    def exists(self):

        try:
            existing_user = User.query.filter(or_(User.username == self.username, User.user_id == self.user_id)).one() 
        except NoResultFound:
            return None

        return existing_user

class UserSchema(SQLAlchemyAutoSchema):
    """ UserSchema class """
    class Meta:
        """ Meta class classification """
        model = User
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
