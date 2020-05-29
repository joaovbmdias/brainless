from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db, CONST_OAUTH, CONST_CALENDAR
from models.calendar import Calendar
from models.project import Project

class Account(db.Model):
    """ Account class """
    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    account_type = db.Column(db.String(32), nullable=False, default=CONST_CALENDAR)
    authentication_type = db.Column(db.String(32), nullable=False, default=CONST_OAUTH)
    provider = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    client_id = db.Column(db.String(32), nullable=False)
    client_secret = db.Column(db.String(32), nullable=True)
    sync_frequency = db.Column(db.Integer, nullable=False, default=5)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    calendars = db.relationship('Calendar', backref='account', lazy=True)
    projects = db.relationship('Project', backref='account', lazy=True)

    def __init__(self, name, provider, user_id, client_id, client_secret, sync_frequency=5, account_type=CONST_CALENDAR, authentication_type=CONST_OAUTH):
        self.account_id = None
        self.name = name
        self.account_type = account_type
        self.authentication_type = authentication_type
        self.provider = provider
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.sync_frequency = sync_frequency
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
