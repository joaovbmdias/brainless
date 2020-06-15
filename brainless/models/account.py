from datetime               import datetime, timedelta
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration          import db
from sqlalchemy.orm.exc     import NoResultFound
from sqlalchemy             import or_, and_
from models.calendar        import Calendar
from models.project         import Project
from models.template        import Template
import constants            as const
import providers.provider   as provider

class Account(db.Model, Template):
    """ Account class """
    __tablename__ = 'account'

    id                  = db.Column(db.Integer,    primary_key=True)
    name                = db.Column(db.String(50), unique=True,             nullable=False)
    account_type        = db.Column(db.String(15), nullable=False,          default=const.CALENDAR)
    authentication_type = db.Column(db.String(15), nullable=False)
    provider            = db.Column(db.String(32), nullable=False)
    username            = db.Column(db.String(64), nullable=True)
    password            = db.Column(db.String(64), nullable=True)
    client_id           = db.Column(db.String(64), nullable=True)
    client_secret       = db.Column(db.String(64), nullable=True)
    api_token           = db.Column(db.String(64), nullable=True)
    sync_frequency      = db.Column(db.Integer,    nullable=False,          default=1)
    last_sync           = db.Column(db.DateTime,   nullable=True,           default=None)
    next_sync           = db.Column(db.DateTime,   nullable=False,          default=datetime.utcnow)
    __created_timestamp = db.Column(db.DateTime,   default=datetime.utcnow)
    __edited_timestamp  = db.Column(db.DateTime,   default=datetime.utcnow,  onupdate=datetime.utcnow)
    user_id             = db.Column(db.Integer,    db.ForeignKey('user.id'), nullable=False)

    calendars = db.relationship('Calendar', backref='account', lazy=True, cascade="save-update, merge, delete")
    projects = db.relationship('Project', backref='account', lazy=True, cascade="save-update, merge, delete")

    def __init__(self, name, provider, user_id, client_id, client_secret, authentication_type, username, password, api_token, id=None, account_type=const.CALENDAR, sync_frequency=5):
        self.id = id
        self.name = name
        self.account_type = account_type
        self.authentication_type = authentication_type
        self.provider = provider
        self.user_id = user_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.api_token = api_token
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

        authentication_data = {'provider': self.provider,
                               'username': self.username,
                               'password': self.password,
                               'client_id': self.client_id,
                               'client_secret': self.client_secret,
                               'api_token': self.api_token,
                               'account_type': self.account_type}

        account_data = provider.get_data(authentication_data)

        if self.account_type in [const.CALENDAR, const.ALL_DATA]:

            calendar_data = account_data[const.CALENDAR]
            synced_calendars = []

            for cal in calendar_data:

                local = Calendar(id=None,
                                 name = cal['name'],
                                 guid = cal['guid'],
                                 account_id = self.id,
                                 brain_enabled = 'Y')

                calendar = local.read()

                if calendar is None:
                    calendar = local
                else:
                    calendar.name = ''
                
                calendar.synchronize(cal['events'])

                synced_calendars.append(calendar.id)

            not_synced = Calendar.query.filter(~Calendar.id.in_(synced_calendars)).all()

            for cal in not_synced:
                cal.synchronize(None)

        if self.account_type in [const.TASK, const.ALL_DATA]:

            task_data = account_data[const.TASK]
            synced_projects = []

            for pr in task_data:
                local = Project(id = None,
                                name = pr['name'],
                                guid = pr['guid'],
                                account_id = self.id,
                                brain_enabled = 'Y')
                            
                project = local.read()

                if project is None:
                    project = local
                else:
                    project.name = pr['name']
                
                project.synchronize(pr['tasks'])

                synced_projects.append(project.id)

            not_synced = Project.query.filter(~Project.id.in_(synced_projects)).all()

            for pr in not_synced:
                pr.synchronize(None)
        
        self.last_sync = datetime.utcnow()
        self.next_sync = datetime.utcnow() + timedelta(minutes=self.sync_frequency)
        self.update()


class AccountSchema(SQLAlchemyAutoSchema):
    """ AccountSchema class """
    class Meta:
        """ Meta class classification """
        model = Account
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
