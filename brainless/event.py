from flask import abort
from configuration import db
from models import Event, EventSchema

def create(event):
    """
    This function creates a new event for a specific user and account
    based on the passed-in event data

    :param event: event to create in events structure
    :return:      201 on success, 406 on event already exists
    """
    #get provided username and validate if already exists
    account_id = event.get('account_id')
    guid = event.get('guid')
    existing_event = (Event.query.filter(Event.account_id == account_id)
                                   .filter(Event.guid == guid)
                                   .one_or_none())

    if existing_event is None:
        # Create an event instance using the schema and the passed-in event
        schema = EventSchema()

        new_event = schema.load(event)

        # Add the event to the database
        db.session.add(new_event)
        db.session.commit()

        # Serialize and return the newly created event in the response
        return schema.dump(new_event), 201

    else:
        abort(409, f'Event with guid {guid} for account {account_id} already exists')

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