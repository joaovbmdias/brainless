"""
This is the calendar module and supports all the ReST actions for CALENDARS
"""

from flask import abort
from configuration import db
from models.calendar import Calendar, CalendarSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, calendar):
    """
    This function creates a new calendar for a specific account
    of a specific user based on the passed-in calendar data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar: calendar to create in events structure
    :return: 201 on success, 409 on calendar already exists
    """

    # get provided calendar guid
    guid = calendar.get('guid')

    # validate if a calendar with the provided data exists
    existing_calendar = (Calendar.query.filter(Calendar.guid == guid)
                                    .filter(Calendar.account_id == account_id)
                                    .one_or_none())

    if existing_calendar is None:
        schema = CalendarSchema()

        # create a calendar instance using the schema and the passed-in calendar
        new_calendar = schema.load(calendar)

        # add the calendar to the database
        db.session.add(new_calendar)

        db.session.commit()

        # return the newly created calendar id in the response
        return new_calendar.calendar_id , 201

    else:
        abort(409, f'Calendar {guid} already exists for account {account_id}')

def read(user_id, account_id, calendar_id):
    """
    This function retrieves a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar already exists
    """

    try:
        # get calendar if it exists
        existing_calendar = Calendar.query.filter(Calendar.calendar_id == calendar_id).one()
    except NoResultFound:
        abort(404, f'Calendar with id:{calendar_id} not found')

    schema = CalendarSchema()
    calendar = schema.dump(existing_calendar)

    return calendar, 200

def search(user_id, account_id):
    """
    This function retrieves a list of calendars based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no calendars found
    """

    # search calendars for the user and acount ids provided
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

    try:
        # validate if calendar exists
        existing_calendar = Calendar.query.filter(Calendar.calendar_id == calendar_id).one()    
    except NoResultFound:
        abort(404, f'Calendar {calendar_id} not found')
    
    schema = CalendarSchema()

    # Create an calendar instance using the schema and the passed-in calendar
    updated_calendar = schema.load(calendar)

    # Set the id to the calendar we want to update
    updated_calendar.calendar_id = existing_calendar.calendar_id

    # Add the calendar to the database
    db.session.merge(updated_calendar)
    db.session.commit()

    return "Calendar updated", 200

def delete(user_id, account_id, calendar_id):
    """
    This function deletes a calendar based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param calendar_id: calendar_id passed-in URL
    :return: 200 on success, 404 on calendar not found
    """

    try:
        # validate if calendar exists
        existing_calendar = Calendar.query.filter(Calendar.calendar_id == calendar_id).one()
    except NoResultFound:
        abort(404, f'Calendar {calendar_id} not found')

    # Add the calendar to the database
    db.session.delete(existing_calendar)
    db.session.commit()

    return "Calendar deleted", 200
