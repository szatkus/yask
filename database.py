import config

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.DATABASE)
Base = declarative_base()
