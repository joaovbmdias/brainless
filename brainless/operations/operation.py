import providers.apple as apple, classes.events as events, datetime
from configuration import CONST_PERIOD

def sync_events(user):

    range = {
             'from': datetime.datetime.now(),
             'to'  : datetime.datetime.now() + datetime.timedelta(days=CONST_PERIOD)
            }

    events.delete(user, range)

    new_events = apple.get_events(user, range)

    events.load(new_events)