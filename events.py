from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from config import Base, Session
import config

class Event(Base):
    __tablename__ = 'event'

    id                     = Column(Integer, primary_key=True)
    title                  = Column(String(32))
    start_datetime         = Column(DateTime)
    end_datetime           = Column(DateTime)
    guid                   = Column(String(32))
    provider               = Column(String(32))
    timestamp              = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<Event(id='%s', title='%s', start_datetime='%s, end_datetime='%s, guid='%s, provider='%s, timestamp='%s')>" % (self.id, self.title, self.start_datetime, self.end_datetime, self.guid, self.provider, self.timestamp)

def create(event):

    session = Session()

    existing_event = (
        session.query(Event).filter(Event.provider == event.provider)
        .filter(Event.guid == event.guid)
        .one_or_none()
    )

    if existing_event is None:

        # Add the event to the database
        session.add(event)
        session.commit()

        return 0

    #Otherwise, nope, event exists already
    else:
        return 1


# def list(events):


# def read(event_id):


# def update(event):


# def delete(event_id)