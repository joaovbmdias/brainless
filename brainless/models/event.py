from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.template import Template
from sqlalchemy import or_, and_
from sqlalchemy.orm.exc import NoResultFound

class Event(db.Model, Template):
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

    def exists(self):

        try:
            existing_event = Event.query.filter(or_(Event.event_id == self.event_id, 
                                                    and_(Event.guid == self.guid, 
                                                        Event.calendar_id == self.calendar_id))).one()   
        except NoResultFound:
            return None

        return existing_event

class EventSchema(SQLAlchemyAutoSchema):
    """ EventSchema class """
    class Meta:
        """ Meta class classification """
        model = Event
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True
