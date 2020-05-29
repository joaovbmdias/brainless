"""
This is the event module and supports all the ReST actions for EVENTS
"""

from flask import abort
from configuration import db
from models.event import Event, EventSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, calendar_id, event):
    """
    This function creates a new event for a specific event
    of a specific user based on the passed-in event data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event: event to create in events structure
    :return: 201 on success, 409 on event already exists
    """

    # get provided event guid
    guid = event.get('guid')

    # validate if an event with the provided data exists
    existing_event = (Event.query.filter(Event.guid == guid)
                                 .filter(Event.calendar_id == calendar_id)
                                 .one_or_none())

    if existing_event is None:
        schema = EventSchema()

        # create an event instance using the schema and the passed-in event
        new_event = schema.load(event)

        # add the event to the database
        db.session.add(new_event)

        db.session.commit()

        # return the newly created event id in the response
        return new_event.event_id , 201

    else:
        abort(409, f'Event {guid} already exists for calendar {calendar_id}')

def read(user_id, account_id, calendar_id, event_id):
    """
    This function retrieves an event data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event already exists
    """

    try:
        # get event if it exists
        existing_event = Event.query.filter(Event.event_id == event_id).one()
    except NoResultFound:
        abort(404, f'Event with id:{event_id} not found')

    schema = EventSchema()
    event = schema.dump(existing_event)

    return event, 200

def search(user_id, account_id, calendar_id):
    """
    This function retrieves a list of events based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on no events found
    """

    # search events for the user and acount ids provided
    existing_events = Event.query.filter(Event.calendar_id == calendar_id).all()
    if existing_events is None:
        abort(404, f'No events found')

    schema = EventSchema(many=True)
    events = schema.dump(existing_events)

    return events, 200

def update(user_id, account_id, calendar_id, event_id, event):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :param event: payload information
    :return: 200 on success, 404 on event not found
    """

    try:
        # validate if event exists
        existing_event = Event.query.filter(Event.event_id == event_id).one()    
    except NoResultFound:
        abort(404, f'Event {event_id} not found')
    
    schema = EventSchema()

    # Create an event instance using the schema and the passed-in event
    updated_event = schema.load(event)

    # Set the id to the event we want to update
    updated_event.event_id = existing_event.event_id

    # Add the event to the database
    db.session.merge(updated_event)
    db.session.commit()

    return "Event updated", 200

def delete(user_id, account_id, calendar_id, event_id):
    """
    This function deletes an event based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event not found
    """

    try:
        # validate if event exists
        existing_event = Event.query.filter(Event.event_id == event_id).one()
    except NoResultFound:
        abort(404, f'Event {event_id} not found')

    # Add the event to the database
    db.session.delete(existing_event)
    db.session.commit()

    return "Event deleted", 200
