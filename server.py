import apple, time
from config import CONST_PERIOD, Base, engine

def startup():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    startup()

    while(True):
        apple.sync_cal()
        time.sleep(CONST_PERIOD)
