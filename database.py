import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.DATABASE)
Base = declarative_base()
Session = sessionmaker(bind=engine)

def atomic(func):
    def wrapper(*args, **kwargs):
        session = Session()
        result = func(session, *args, **kwargs)
        session.commit()
        return result
    return wrapper
