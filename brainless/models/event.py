from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db, CONST_OAUTH

class Event(db.Model):
    """ Event class """
    __tablename__ = 'event'

    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, start_datetime, end_datetime, guid, account_id):
        self.event_id = None
        self.title = title
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.guid = guid
        self.account_id = account_id
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
