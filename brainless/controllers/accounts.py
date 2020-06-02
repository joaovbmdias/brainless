"""
This is the account module and supports all the ReST actions for ACCOUNTS
"""

from flask import abort
from configuration import db
from models.account import Account, AccountSchema

def create(user_id, account):
    """
    This function creates a new account for a specific user
    based on the passed-in account data

    :param user_id: user_id passed-in URL
    :param account: account to create in accounts structure
    :return: 201 on success, 409 on account already exists
    """

    schema = AccountSchema()
    new_account = schema.load(account)

    new_account.provider = new_account.provider.upper()

    if new_account.create() is None:
        abort(409, f'Account {new_account.name} already exists')
    else:
        account_serialized = schema.dump(new_account)

        return account_serialized, 201

def read(user_id, account_id):
    """
    This function retrieves an account data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on account already exists
    """

    account = Account(id=account_id, 
                      name=None,
                      account_type=None,
                      authentication_type=None,
                      provider=None,
                      user_id=None,
                      client_id=None,
                      client_secret=None,
                      sync_frequency=None)

    read_account = account.read()

    if read_account is None:
        abort(404, f'Account with id:{account_id} not found')
    else:
        schema = AccountSchema()
        account_serialized = schema.dump(read_account)

        return account_serialized, 200

def search(user_id):
    """
    This function retrieves a list of accounts based on the provided information

    :param user_id: user_id passed-in URL
    :return: 200 on success, 404 on no accounts found
    """

    existing_accounts = Account.query.filter(Account.user_id == user_id).all()
    if existing_accounts is None:
        abort(404, f'No accounts found')

    schema = AccountSchema(many=True)
    accounts_serialized = schema.dump(existing_accounts)

    return accounts_serialized, 200

def update(user_id, account_id, account):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param account: payload information
    :return: 200 on success, 404 on account not found
    """

    schema = AccountSchema()
    account_to_update = schema.load(account)

    updated_account = account_to_update.update()

    if updated_account is None:
        abort(404, f'Account {account_id} not found')
    else:
        account_serialized = schema.dump(updated_account)

        return account_serialized, 200

def delete(user_id, account_id):
    """
    This function deletes an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on account not found
    """

    account_to_delete = Account(id=account_id, 
                                name=None,
                                account_type=None,
                                authentication_type=None,
                                provider=None,
                                user_id=None,
                                client_id=None,
                                client_secret=None,
                                sync_frequency=None)

    if account_to_delete.delete() is not None:
        abort(404, f'Account {account_id} not found')
    else:
        return "Account deleted", 200
