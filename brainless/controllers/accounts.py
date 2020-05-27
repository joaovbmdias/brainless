"""
This is the account module and supports all the ReST actions for ACCOUNTS
"""

from flask import abort
from configuration import db
from models.account import Account, AccountSchema
from sqlalchemy.orm.exc import NoResultFound

def user_account_check(user_id, account_id, account):
    """
    This function checks payload information againts URL passed-in arguments

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param account: payload information
    """
    
    if user_id is not None and account is not None:
        # get provided account_id and validate if compliant with in path account_id
        body_account_id = account.get('account_id')

        if body_account_id != account_id:
            abort(400, f'Account identification data invalid')

    if account_id is not None and account is not None:
        # get the provided user_id and validate if compliant with in path user_id
        body_user_id = account.get('user_id')

        if body_user_id != user_id:
            abort(400, f'User identification data invalid')

def create(user_id, account):
    """
    This function creates a new account for a specific user
    based on the passed-in account data

    :param user_id: user_id passed-in URL
    :param account: account to create in accounts structure
    :return: 201 on success, 409 on account already exists
    """

    # validate provided data
    user_account_check(user_id, None, account)

    # get provided account name
    name = account.get('name')

    # validate if an account with the provided data exists
    existing_account = (Account.query.filter(Account.name == name)
                                     .filter(Account.user_id == user_id)
                                     .one_or_none())

    if existing_account is None:
        schema = AccountSchema()

        # Create an account instance using the schema and the passed-in account
        new_account = schema.load(account)

        # Add the account to the database
        db.session.add(new_account)
        db.session.commit()

        # Serialize and return the newly created account id in the response
        return new_account.account_id , 201

    else:
        abort(409, f'Account {name} already exists')

def read(user_id, account_id):
    """
    This function retrieves an account data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param account: payload information
    :return: 200 on success, 404 on account already exists
    """

    # validate provided data
    user_account_check(user_id, account_id, None)

    try:
        # get account if it exists
        existing_account = Account.query.filter(Account.account_id == account_id).one()    
    except NoResultFound:
        abort(404, f'Account with id:{account_id} not found')

    schema = AccountSchema()
    account = schema.dump(existing_account)

    return account, 200

def search(user_id):
    """
    This function retrieves a list of accounts based on the provided information

    :param user_id: user_id passed-in URL
    :param account: payload information
    :return: 200 on success, 404 on no accounts found
    """

    # validate provided data
    user_account_check(user_id, None, None)

    #get provided username and validate if account exists
    existing_accounts = Account.query.filter(Account.user_id == user_id).all()
    if existing_accounts is None:
        abort(404, f'No accounts found')

    schema = AccountSchema(many=True)
    accounts = schema.dump(existing_accounts)

    return accounts, 200

def update(user_id, account_id, account):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param account: payload information
    :return: 200 on success, 404 on account not found
    """

    # validate provided data
    user_account_check(user_id, account_id, account)

    try:
        #get provided name and validate if already exists
        existing_account = Account.query.filter(Account.account_id == account_id).one()    
    except NoResultFound:
        abort(404, f'Account {account_id} not found')
    
    schema = AccountSchema()

    # Create an account instance using the schema and the passed-in account
    updated_account = schema.load(account)

    # Set the id to the account we want to update
    updated_account.account_id = existing_account.account_id

    # Add the account to the database
    db.session.merge(updated_account)
    db.session.commit()

    return "Account updated", 200

def delete(user_id, account_id):
    """
    This function deletes an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param account: payload information
    :return: 200 on success, 404 on account not found
    """

    # validate provided data
    user_account_check(user_id, account_id, None)

    try:
        #get provided name and validate if account exists
        existing_account = Account.query.filter(Account.account_id == account_id).one()
    except NoResultFound:
        abort(404, f'Account {account_id} not found')

    # Add the event to the database
    db.session.delete(existing_account)
    db.session.commit()

    return "Account deleted", 200
