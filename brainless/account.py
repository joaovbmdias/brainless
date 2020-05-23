"""
This is the account module and supports all the ReST actions for ACCOUNTS
"""

from flask import abort
from configuration import db
from models import Account, AccountSchema

def create(account):
    """
    This function creates a new account for a specific user
    based on the passed-in account data

    :param account: account to create in accounts structure
    :return:        201 on success, 406 on account already exists
    """
    #get provided username and validate if already exists
    name = account.get('name')
    existing_account = Account.query.filter(Account.name == name).one_or_none()

    if existing_account is None:
        # Create an account instance using the schema and the passed-in account
        schema = AccountSchema()

        new_account = schema.load(account)

        # Add the account to the database
        db.session.add(new_account)
        db.session.commit()

        # Serialize and return the newly created account in the response
        return schema.dump(new_account), 201

    else:
        abort(409, f'Account {name} already exists')

# def delete(self):

#     try:
#         session = Session()

#         session.query(Account).filter(Account.name == self.name).one()

#         # Add the event to the database
#         session.delete(self)
#         session.commit()

#     except NoResultFound:
#         session.rollback()
#         print('Account {} not found'.format(self.name))
#     except:
#         session.rollback()
#         print('Account deletion failed')

# def get(self):

#     try:
#         session = Session()

#         existing_account = session.query(Account).filter(Account.name == self.name).one()

#         return existing_account

#     except NoResultFound:
#         session.rollback()
#         print('Account {} not found'.format(self.name))
#     except:
#         session.rollback()
#         print('Failed to retrieve account {)'.format(self.name))
