"""
This is the event module and supports all the ReST actions for EVENTS
"""

from flask import abort
from configuration import db
from models.event import Event, EventSchema
from constants import FAILURE

def create(user_id, account_id, calendar_id, body):
    """
    This function creates a new event for a specific event
    of a specific user based on the passed-in event data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param body: event to create in events structure
    :return: 201 on success, 409 on event already exists
    """    
    schema = EventSchema()
    event = schema.load(body)
    if event.create() == FAILURE:
        abort(409, f'Event {event.name} already exists')
    else:
        return schema.dump(event), 201

def read(user_id, account_id, calendar_id, event_id):
    """
    This function retrieves an event data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event already exists
    """
    event = Event(id             = event_id,
                  name           = None,
                  start_datetime = None,
                  end_datetime   = None,
                  guid           = None,
                  calendar_id    = None)
    if event.read() == FAILURE:
        abort(404, f'Event with id:{event_id} not found')
    else:
        schema = EventSchema()
        return schema.dump(event), 200

def search(user_id, account_id, calendar_id):
    """
    This function retrieves a list of events based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on no events found
    """
    events = Event.query.filter(Event.calendar_id == calendar_id).all()
    if events is None:
        abort(404, f'No events found')
    schema = EventSchema(many=True)
    return schema.dump(events), 200

def update(user_id, account_id, calendar_id, event_id, body):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :param body: payload information
    :return: 200 on success, 404 on event not found
    """
    schema = EventSchema()
    event = schema.load(body)
    if event.update() == FAILURE:
        abort(404, f'Event {event_id} not found')
    else:
        return schema.dump(event), 200

def delete(user_id, account_id, calendar_id, event_id):
    """
    This function deletes an event based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param event_id: event_id passed-in URL
    :return: 200 on success, 404 on event not found
    """
    event = Event(id             = event_id,
                  name           = None,
                  start_datetime = None,
                  end_datetime   = None,
                  guid           = None,
                  calendar_id    = None)
    if event.delete() == FAILURE:
        abort(404, f'Event {event_id} not found')
    else:
        return "Event deleted", 200
