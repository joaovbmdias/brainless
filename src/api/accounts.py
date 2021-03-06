"""
This is the account module and supports all the ReST actions for ACCOUNTS
"""

from flask import abort
from configuration import db
from models.account import Account, AccountSchema
from constants import FAILURE

def create(user_id, body):
    """
    This function creates a new account for a specific user
    based on the passed-in account data

    :param user_id: user_id passed-in URL
    :param body: account to create in accounts structure
    :return: 201 on success, 409 on account already exists
    """
    schema = AccountSchema()
    account = schema.load(body)
    account.provider = account.provider.upper()
    if account.create() == FAILURE:
        abort(409, f'Account {account.name} already exists')
    else:
        return schema.dump(account), 201

def read(user_id, account_id):
    """
    This function retrieves an account data based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on account already exists
    """
    account = Account(id                  = account_id, 
                      name                = None,
                      account_type        = None,
                      authentication_type = None,
                      provider            = None,
                      user_id             = None,
                      client_id           = None,
                      client_secret       = None,
                      username            = None,
                      password            = None,
                      api_key             = None,
                      sync_frequency      = None)
    if account.read() == FAILURE:
        abort(404, f'Account with id:{account_id} not found')
    else:
        schema = AccountSchema()
        return schema.dump(account), 200

def search(user_id):
    """
    This function retrieves a list of accounts based on the provided information

    :param user_id: user_id passed-in URL
    :return: 200 on success, 404 on no accounts found
    """
    accounts = Account.query.filter(Account.user_id == user_id).all()
    if accounts is None:
        abort(404, f'No accounts found')
    schema = AccountSchema(many=True)
    return schema.dump(accounts), 200

def update(user_id, account_id, body):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param body: payload information
    :return: 200 on success, 404 on account not found
    """
    schema = AccountSchema()
    account = schema.load(body)
    if account.update() == FAILURE:
        abort(404, f'Account {account_id} not found')
    else:
        return schema.dump(account), 200

def delete(user_id, account_id):
    """
    This function deletes an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on account not found
    """
    account = Account(id                  = account_id,
                      name                = None,
                      account_type        = None,
                      authentication_type = None,
                      provider            = None,
                      user_id             = None,
                      client_id           = None,
                      client_secret       = None,
                      username            = None,
                      password            = None,
                      api_key             = None,
                      sync_frequency      = None)
    if account.delete() == FAILURE:
        abort(404, f'Account {account_id} not found')
    else:
        return "Account deleted", 200
