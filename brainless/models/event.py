from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.template import Template
from sqlalchemy import or_, and_, UniqueConstraint
from sqlalchemy.orm.exc import NoResultFound

class Event(db.Model, Template):
    """ Event class """
    __tablename__ = 'event'

    id                  = db.Column(db.Integer,     primary_key=True)
    name                = db.Column(db.String(120), nullable=False)
    start_datetime      = db.Column(db.DateTime,    nullable=False)
    end_datetime        = db.Column(db.DateTime,    nullable=False)
    guid                = db.Column(db.String(50),  nullable=False)
    __created_timestamp = db.Column(db.DateTime,    default=datetime.utcnow)
    __edited_timestamp  = db.Column(db.DateTime,    default=datetime.utcnow,      onupdate=datetime.utcnow)
    calendar_id         = db.Column(db.Integer,     db.ForeignKey('calendar.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('guid', 'calendar_id', name='unique_guid'),
        None)

    def __init__(self, name, start_datetime, end_datetime, guid, calendar_id, id=None):
        self.name           = name
        self.start_datetime = start_datetime
        self.end_datetime   = end_datetime
        self.guid           = guid
        self.calendar_id    = calendar_id
        self.id             = id

    def exists(self):

        try:
            existing_event = Event.query.filter(or_(Event.id              == self.id, 
                                                    and_(Event.guid       == self.guid, 
                                                        Event.calendar_id == self.calendar_id))).one()   
        except NoResultFound:
            return None

        return existing_event

class EventSchema(SQLAlchemyAutoSchema):
    """ EventSchema class """
    class Meta:
        """ Meta class classification """
        model                 = Event
        sqla_session          = db.session
        include_fk            = True
        include_relationships = True
        load_instance         = True
