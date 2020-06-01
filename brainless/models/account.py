from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db, CONST_OAUTH, CONST_CALENDAR
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_
from models.calendar import Calendar
from models.project import Project
from models.template import Template

class Account(db.Model, Template):
    """ Account class """
    __tablename__ = 'account'

    account_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    account_type = db.Column(db.String(32), nullable=False, default=CONST_CALENDAR)
    authentication_type = db.Column(db.String(32), nullable=False, default=CONST_OAUTH)
    provider = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    client_id = db.Column(db.String(32), nullable=False)
    client_secret = db.Column(db.String(32), nullable=True)
    sync_frequency = db.Column(db.Integer, nullable=False, default=5)
    last_sync = db.Column(db.DateTime, nullable=True, default=None)
    next_sync = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    calendars = db.relationship('Calendar', backref='account', lazy=True)
    projects = db.relationship('Project', backref='account', lazy=True)
    
    def exists(self):

        try:
            existing_account = (Account.query.filter(or_(and_(Account.name == self.name ,Account.user_id == self.user_id), 
                                                         and_(Account.provider == self.provider, Account.client_id == self.client_id),
                                                             (Account.account_id == self.account_id)))).one() 
        except NoResultFound:
            return None

        return existing_account

    def synchronize(self):

        if self.account_type == CONST_CALENDAR:
            for cal in self.calendars:
                cal.synchronize()

        elif account.account_type == CONST_TASK:
            for pr in account.projects:
                pr.synchronize()

class AccountSchema(SQLAlchemyAutoSchema):
    """ AccountSchema class """
    class Meta:
        """ Meta class classification """
        model = Account
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
