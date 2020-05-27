from flask import abort
from configuration import db
from models.event import Event, EventSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, event):
    """
    This function creates a new event for a specific account
    of a specific user based on the passed-in account data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param event: event to create in events structure
    :return: 201 on success, 409 on account already exists
    """

    # get provided event guid
    guid = event.get('guid')

    # validate if an event with the provided data exists
    existing_event = (Event.query.filter(Event.guid == guid)
                                 .filter(Event.account_id == account_id)
                                 .one_or_none())

    if existing_event is None:
        schema = EventSchema()

        # Create an event instance using the schema and the passed-in event
        new_event = schema.load(event)

        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        # Serialize and return the newly created event id in the response
        return new_event.event_id , 201

    else:
        abort(409, f'Event {guid} already exists for account {account_id}')

# def delete(self):

#     try:
#         session = Session()

#         (session.query(Event).filter(Event.guid     == self.guid)
#                                 .filter(Event.provider == self.provider)
#                                 .filter(Event.user_id  == self.user_id)
#                                 .one())
        
#         # Add the event to the database
#         session.delete(self)
#         session.commit()
#     except NoResultFound:
#         session.rollback()
#         print('Event {} from provider {} belonging to user {} was not found'.format(self.guid, self.provider, self.user_id))
#     except:
#         session.rollback()
#         print('Event deletion failed')

# def load(events):

#     try:
#         session = Session()

#         for event in events:
#             event.create()
        
#         session.commit()
#     except:
#         session.rollback()
#         print('Evets creation failed')

# #TODO: receive list of events????
# def delete(user, range):

#     try:
#         session = Session()

#         existing_events = (session.query(Event).filter(Event.start_datetime <= range['to'])
#                                                .filter(Event.user_id        == user.id))

#         for event in existing_events:
#             session.delete(event)
        
#         session.commit()
#     except:
#         session.rollback()