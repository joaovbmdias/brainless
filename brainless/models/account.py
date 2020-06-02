from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
import constants as const
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_
from models.calendar import Calendar
from models.project import Project
from models.template import Template
import providers.apple as apple

class Account(db.Model, Template):
    """ Account class """
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    account_type = db.Column(db.String(32), nullable=False, default=const.CONST_CALENDAR)
    authentication_type = db.Column(db.String(32), nullable=False, default=const.CONST_OAUTH)
    provider = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    client_id = db.Column(db.String(32), nullable=False)
    client_secret = db.Column(db.String(32), nullable=True)
    sync_frequency = db.Column(db.Integer, nullable=False, default=5)
    last_sync = db.Column(db.DateTime, nullable=True, default=None)
    next_sync = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    __edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    calendars = db.relationship('Calendar', backref='account', lazy=True)
    projects = db.relationship('Project', backref='account', lazy=True)

    def __init__(self, name, provider, user_id, client_id, client_secret, id=None, account_type=const.CONST_CALENDAR, authentication_type=const.CONST_OAUTH, sync_frequency=5):
        self.__created_timestamp = datetime.utcnow()
        self.__edited_timestamp = datetime.utcnow()
        self.id = id
        self.name = name
        self.account_type = account_type
        self.authentication_type = authentication_type
        self.provider = provider
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.sync_frequency = sync_frequency
        self.last_sync = datetime.utcnow()
        self.next_sync = datetime.utcnow()
    
    def exists(self):

        try:
            existing_account = (Account.query.filter(or_(and_(Account.name == self.name ,Account.user_id == self.user_id), 
                                                         and_(Account.provider == self.provider, Account.client_id == self.client_id),
                                                             (Account.id == self.id)))).one() 
        except NoResultFound:
            return None

        return existing_account

    def synchronize(self):

        account_data = {}

        if self.provider == const.CONST_APPLE:
            account_data = apple.get_data(self.client_id, self.client_secret, self.account_type)

        elif self.provider == const.CONST_GOOGLE:
            print('GOOGLE')
        
        elif self.provider == const.CONST_DOIST:
            print('DOIST')

        calendar_data = account_data['calendar']
        task_data = account_data['task']

        for cal, events in calendar_data.items():
            
            calendar = Calendar(calendar_id=None,
                                name = None,
                                guid = cal,
                                account_id = self.id,
                                brain_enabled = None)

            calendar.synchronize(events)


class AccountSchema(SQLAlchemyAutoSchema):
    """ AccountSchema class """
    class Meta:
        """ Meta class classification """
        model = Account
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
