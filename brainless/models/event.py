from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db

class Event(db.Model):
    """ Event class """
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.calendar_id'), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name, start_datetime, end_datetime, guid, calendar_id):
        self.event_id = None
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.guid = guid
        self.calendar_id = calendar_id
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp  = datetime.utcnow

class EventSchema(SQLAlchemyAutoSchema):
    """ EventSchema class """
    class Meta:
        """ Meta class classification """
        model = Event
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
