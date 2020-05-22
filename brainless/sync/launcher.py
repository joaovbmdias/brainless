import time
from classes.users import User
from operations.navigation import menu
from operations.operation import sync_events
from configuration import CONST_PERIOD, Base, engine

def startup():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    startup()
    
    while(True):
        sync_events(user)
        time.sleep(CONST_PERIOD)
