"""
This is the user module and supports all the ReST actions for USERS
"""

from flask import abort
from configuration import db
from models import User, UserSchema

def create(user):
    """
    This function creates a new user
    based on the passed-in user data

    :param user: user to create in users structure
    :return:     201 on success, 406 on user already exists
    """

    #get provided username and validate if already exists
    username = user.get('username')
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user is None:
        # Create a user instance using the schema and the passed-in user
        schema = UserSchema()
        new_user = schema.load(user, session=db.session)

        # Add the person to the database
        db.session.add(new_user)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_user), 201

    else:
        abort(409, f'User {username} already exists')

# def read():
#     """ Retrieves one user """
#     print('hello')

# def read_all():
#     """ Retrieves all users """
#     print('hello')

# def update():
#     """ Update one user """
#     print('hello')

# def delete():
#     """ Deletes one user """
#     print('hello')

    # def create(self):
    #     """" Method for creating one user """
    #     session = Session()

    #     existing_user = session.query(User).filter(User.username == self.username).one_or_none()

    #     if existing_user is not None:
    #         session.rollback()
    #         raise Exception('Username {} already exists.'.format(self.username))

    #     # Add the event to the database
    #     session.add(self)
    #     session.commit()

    # def delete(self):
    #     """" Method for deleting one user """
    #     try:
    #         session = Session()

    #         session.query(User).filter(User.username == self.username).one()

    #         # Add the event to the database
    #         session.delete(self)
    #         session.commit()

    #     except NoResultFound:
    #         session.rollback()
    #         print('User {} not found'.format(self.username))

    # def get(self):
    #     """" Method for retrieving one user """
    #     try:
    #         session = Session()

    #         existing_user = (session.query(User).filter(User.username == self.username)
    #                          .filter(User.password == self.password)
    #                          .one())

    #         return existing_user

    #     except NoResultFound:
    #         session.rollback()
    #         print('Username {} not found'.format(self.username))
