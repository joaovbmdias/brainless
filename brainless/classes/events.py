from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from configuration import Base, Session
from sqlalchemy.orm.exc import NoResultFound

class Event(Base):
    __tablename__ = 'event'

    id                = Column(Integer,    primary_key=True)
    title             = Column(String(32))
    start_datetime    = Column(DateTime)
    end_datetime      = Column(DateTime)
    guid              = Column(String(32))
    provider          = Column(String(32))
    user_id           = Column(Integer,    ForeignKey('user.id'))
    created_timestamp = Column(DateTime,   default=datetime.utcnow)
    edited_timestamp  = Column(DateTime,   default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, start_datetime, end_datetime, guid, provider, user_id):
        self.id                  = None
        self.title               = title
        self.start_datetime      = start_datetime
        self.end_datetime        = end_datetime
        self.guid                = guid
        self.provider            = provider
        self.user_id             = user_id
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp  = datetime.utcnow

    def create(self):

        try:
            session = Session()

            existing_event = (session.query(Event).filter(Event.guid     == self.guid)
                                                  .filter(Event.provider == self.provider)
                                                  .filter(Event.user_id  == self.user_id)
                                                  .one_or_none())

            if existing_event is not None:
                raise Exception('Event {} from provider {} belonging to user {} already exists'.format(self.guid, self.provider, self.user_id))

            # Add the event to the database
            session.add(self)
            session.commit()
        except:
            session.rollback()
            print('Event creation failed')

    def delete(self):

        try:
            session = Session()

            (session.query(Event).filter(Event.guid     == self.guid)
                                 .filter(Event.provider == self.provider)
                                 .filter(Event.user_id  == self.user_id)
                                 .one())
            
            # Add the event to the database
            session.delete(self)
            session.commit()
        except NoResultFound:
            session.rollback()
            print('Event {} from provider {} belonging to user {} was not found'.format(self.guid, self.provider, self.user_id))
        except:
            session.rollback()
            print('Event deletion failed')

def load(events):

    try:
        session = Session()

        for event in events:
            event.create()
        
        session.commit()
    except:
        session.rollback()
        print('Evets creation failed')

#TODO: receive list of events????
def delete(user, range):

    try:
        session = Session()

        existing_events = (session.query(Event).filter(Event.start_datetime <= range['to'])
                                               .filter(Event.user_id        == user.id))

        for event in existing_events:
            session.delete(event)
        
        session.commit()
    except:
        session.rollback()