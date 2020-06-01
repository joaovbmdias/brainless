"""
This is the calendar module and supports all the ReST actions for CALENDARS
"""

from flask import abort
from configuration import db
from models.calendar import Calendar, CalendarSchema

def create(user_id, account_id, calendar):
    """
    This function creates a new calendar for a specific account
    of a specific user based on the passed-in calendar data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar: calendar to create in events structure
    :return: 201 on success, 409 on calendar already exists
    """

    schema = CalendarSchema()
    new_calendar = schema.load(calendar)

    if new_calendar.create() is None:
        guid = calendar.get('guid')
        abort(409, f'Calendar {guid} already exists for account {account_id}')
    
    else:
        return new_calendar.calendar_id , 201

def read(user_id, account_id, calendar_id):
    """
    This function retrieves a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar already exists
    """

    calendar = Calendar(calendar_id=calendar_id)

    read_calendar = calendar.read()

    if read_calendar is None:
        abort(404, f'Calendar with id:{calendar_id} not found')
    else:
        schema = CalendarSchema()
        calendar_serialized = schema.dump(read_calendar)

        return calendar_serialized, 200

def search(user_id, account_id):
    """
    This function retrieves a list of calendars based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no calendars found
    """

    existing_calendars = Calendar.query.filter(Calendar.account_id == account_id).all()
    if existing_calendars is None:
        abort(404, f'No calendars found')

    schema = CalendarSchema(many=True)
    calendars = schema.dump(existing_calendars)

    return calendars, 200

def update(user_id, account_id, calendar_id, calendar):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :param calendar: payload information
    :return: 200 on success, 404 on calendar not found
    """

    schema = CalendarSchema()
    calendar_to_update = schema.load(calendar)

    updated_calendar = calendar_to_update.update()

    if updated_calendar is None:
        abort(404, f'Calendar {calendar_id} not found')
    else:
        return schema.dump(updated_calendar), 200

def delete(user_id, account_id, calendar_id):
    """
    This function deletes a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar not found
    """

    calendar_to_delete = Calendar(calendar_id=calendar_id)

    if calendar_to_delete.delete() is not None:
        abort(404, f'Calendar {calendar_id} not found')
    else:
        return "Calendar deleted", 200
