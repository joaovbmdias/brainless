"""
Brainless Daemons
"""
from datetime import datetime
from models.account import Account
import time

def sync_accounts():

    for acc in Account.query.filter(Account.next_sync <= datetime.utcnow()):
        acc.synchronize()
