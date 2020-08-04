"""
This is the calendar module and supports all the ReST actions for CALENDARS
"""

from flask import abort
from configuration import db
from models.calendar import Calendar, CalendarSchema
from constants import FAILURE

def create(user_id, account_id, body):
    """
    This function creates a new calendar for a specific account
    of a specific user based on the passed-in calendar data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param body: calendar to create in events structure
    :return: 201 on success, 409 on calendar already exists
    """
    schema = CalendarSchema()
    calendar = schema.load(body)
    if calendar.create() == FAILURE:
        abort(409, f'Calendar {calendar.guid} already exists for account {account_id}')
    else:
        return schema.dump(calendar), 201

def read(user_id, account_id, calendar_id):
    """
    This function retrieves a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar already exists
    """
    calendar = Calendar(id            = calendar_id,
                        name          = None,
                        guid          = None,
                        account_id    = None,
                        brain_enabled = None)
    if calendar.read() == FAILURE:
        abort(404, f'Calendar with id:{calendar_id} not found')
    else:
        schema = CalendarSchema()
        return schema.dump(calendar), 200

def search(user_id, account_id):
    """
    This function retrieves a list of calendars based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no calendars found
    """
    calendars = Calendar.query.filter(Calendar.account_id == account_id).all()
    if calendars is None:
        abort(404, f'No calendars found')
    schema = CalendarSchema(many=True)
    return schema.dump(calendars), 200

def update(user_id, account_id, calendar_id, body):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param body: payload information
    :return: 200 on success, 404 on calendar not found
    """
    schema = CalendarSchema()
    calendar = schema.load(body)
    if calendar.update() == FAILURE:
        abort(404, f'Calendar {calendar_id} not found')
    else:
        return schema.dump(calendar), 200

def delete(user_id, account_id, calendar_id):
    """
    This function deletes a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar not found
    """
    calendar = Calendar(id            = calendar_id,
                        name          = None,
                        guid          = None,
                        account_id    = None,
                        brain_enabled = None)

    if calendar.delete() == FAILURE:
        abort(404, f'Calendar {calendar_id} not found')
    else:
        return "Calendar deleted", 200
