"""
This is the user module and supports all the ReST actions for USERS
"""

from flask import abort
from configuration import db
from models.user import User, UserSchema

def create(body):
    """
    This function creates a new user
    based on the passed-in user data

    :param body: user to create in users structure
    :return:     201 on success, 406 on user already exists
    """

    schema = UserSchema()
    user = schema.load(body)

    if user.create() is None:
        abort(409, f'User {user.username} already exists')
    else:
        user_serialized = schema.dump(user)

        return user_serialized, 201