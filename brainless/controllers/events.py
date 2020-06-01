"""
This is the event module and supports all the ReST actions for EVENTS
"""

from flask import abort
from configuration import db
from models.event import Event, EventSchema

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

    schema = EventSchema()
    new_event = schema.load(event)

    if new_event.create() is None:
        abort(409, f'Event {new_event.name} already exists')
    else:
        event_serialized = schema.dump(new_event)

        return event_serialized, 201

def read(user_id, account_id, calendar_id, event_id):
    """
    This function retrieves an event data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event already exists
    """
    event = Event(event_id=event_id)

    read_event = event.read()

    if read_event is None:
        abort(404, f'Event with id:{event_id} not found')
    else:
        schema = EventSchema()
        event_serialized = schema.dump(read_event)

        return event_serialized, 200

def search(user_id, account_id, calendar_id):
    """
    This function retrieves a list of events based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on no events found
    """

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

    schema = EventSchema()
    event_to_update = schema.load(event)

    updated_event = event_to_update.update()

    if updated_event is None:
        abort(404, f'Event {event_id} not found')
    else:
        event_serialized = schema.dump(updated_event)

        return event_serialized, 200

def delete(user_id, account_id, calendar_id, event_id):
    """
    This function deletes an event based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event not found
    """

    event_to_delete = Event(event_id=event_id)

    if event_to_delete.delete() is not None:
        abort(404, f'Event {event_id} not found')
    else:
        return "Event deleted", 200
