from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.event import Event
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_

class Calendar(db.Model, Template):
    """ Calendar class """
    __tablename__ = 'calendar'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    brain_enabled = db.Column(db.String(1), nullable=False, default='Y')
    __created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __edited_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    events = db.relationship('Event', backref='calendar', lazy=True)

    def __init__(self, name, guid, account_id, id=None, brain_enabled='Y'):
        self.name = name
        self.guid = guid
        self.account_id = account_id
        self.id = id
        self.brain_enabled = brain_enabled

    def exists(self):

        try:
            existing_calendar = Calendar.query.filter(or_(Calendar.id == self.id, 
                                                         and_(Calendar.guid == self.guid, 
                                                              Calendar.account_id == self.account_id))).one()   
        except NoResultFound:
            return None

        return existing_calendar

    def synchronize(self, sync_data):

        existing_calendar = self.exists()

        if existing_calendar is None:
            self.create()
            print('create: ' + str(self.id))
        else:
            self.update()
            print('updated')
        
        print(self)
        #print(sync_data)

class CalendarSchema(SQLAlchemyAutoSchema):
    """ CalendarSchema class """
    class Meta:
        """ Meta class classification """
        model = Calendar
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
