from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONST_APPLE  = 'Apple'
CONST_GOOGLE = 'Google'
CONST_DOIST  = 'Doist' 

CONST_PERIOD = 10

CONST_EMAIL  = 'joaovbmdias@icloud.com'

engine = create_engine('sqlite:///ibutler.db', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)