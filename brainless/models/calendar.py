from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.event import Event

class Calendar(db.Model):
    """ Calendar class """
    __tablename__ = 'calendar'

    calendar_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    events = db.relationship('Event', backref='calendar', lazy=True)

    def __init__(self, name, guid, account_id):
        self.calendar_id = None
        self.name = name
        self.guid = guid
        self.account_id = account_id
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp  = datetime.utcnow

class CalendarSchema(SQLAlchemyAutoSchema):
    """ CalendarSchema class """
    class Meta:
        """ Meta class classification """
        model = Calendar
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
