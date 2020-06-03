from datetime               import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration          import db
from models.event           import Event
from models.template        import Template
from sqlalchemy.orm.exc     import NoResultFound
from sqlalchemy             import or_, and_

class Calendar(db.Model, Template):
    """ Calendar class """
    __tablename__ = 'calendar'

    id                  = db.Column(db.Integer,    primary_key=True)
    name                = db.Column(db.String(32), nullable=True)
    guid                = db.Column(db.String(32), nullable=False)
    brain_enabled       = db.Column(db.String(1),  nullable=False, default='Y')
    __created_timestamp = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)
    __edited_timestamp  = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    account_id          = db.Column(db.Integer,    db.ForeignKey('account.id'), nullable=False)

    events = db.relationship('Event', backref='calendar', lazy=True, cascade="save-update, merge, delete")

    def __init__(self, name, guid, account_id, id=None, brain_enabled='Y'):
        self.name          = name
        self.guid          = guid
        self.account_id    = account_id
        self.id            = id
        self.brain_enabled = brain_enabled

    def exists(self):

        try:
            existing_calendar = Calendar.query.filter(or_(Calendar.id == self.id, 
                                                        and_(Calendar.guid == self.guid, 
                                                             Calendar.account_id == self.account_id))).one()
        except NoResultFound:
            return None

        return existing_calendar

    def synchronize(self, event_data):

        if self.id is None:
            self.create()
        else:
            self.update()

        if self.brain_enabled:

            event_guids = ['#$%&/()']

            if event_data is not None:
                for ev in event_data:
                    local = Event(id = None,
                                  name           = ev['name'],
                                  guid           = ev['guid'],
                                  start_datetime = ev['start_datetime'],
                                  end_datetime   = ev['end_datetime'],
                                  calendar_id    = self.id)

                    event = local.read()

                    if event is not None:
                        local.id = event.id
    
                    event = local
                    event.synchronize()

                    event_guids.append(ev['guid'])

            #TODO: there MUST BE a better way to delete. bulk delete
            for ev in Event.query.filter(and_(Event.calendar_id == self.id, ~Event.guid.in_(event_guids))).all():
                db.session.delete(ev)

class CalendarSchema(SQLAlchemyAutoSchema):
    """ CalendarSchema class """
    class Meta:
        """ Meta class classification """
        model = Calendar
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True