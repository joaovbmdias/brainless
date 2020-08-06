"""
Brainless Daemons
"""
from datetime import datetime
from models.account import Account


def sync_accounts():
    print('SYNC - ' + str(datetime.utcnow()))

    for acc in Account.query.filter(Account.next_sync <= datetime.utcnow()):
        acc.synchronize()
