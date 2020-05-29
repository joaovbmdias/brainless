from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db, CONST_OAUTH, CONST_CALENDAR
from models.event import Event

class Account(db.Model):
    """ Account class """
    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    account_type = db.Column(db.String(32), nullable=False)
    authentication_type = db.Column(db.String(32), nullable=False)
    provider = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    client_id = db.Column(db.String(32), nullable=False)
    client_secret = db.Column(db.String(32), nullable=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    events = db.relationship('Event', backref='account', lazy=True)

    def __init__(self, name, provider, user_id, client_id, client_secret, account_type=CONST_CALENDAR, authentication_type=CONST_OAUTH):
        self.account_id = None
        self.name = name
        self.account_type = account_type
        self.authentication_type = authentication_type
        self.provider = provider
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class AccountSchema(SQLAlchemyAutoSchema):
    """ AccountSchema class """
    class Meta:
        """ Meta class classification """
        model = Account
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
