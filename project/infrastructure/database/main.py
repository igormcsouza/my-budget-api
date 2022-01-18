from lib2to3.pytree import Base
import sqlalchemy as db
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.getenv("POSTGRES_USER", "root")
password = os.getenv("POSTGRES_PASSWORD", "root")
db_name = os.getenv("POSTGRES_DB", "budget_db")

engine = db.create_engine(f'postgresql://{user}:{password}@postgres:5432/{db_name}')

Session = sessionmaker(bind = engine)
Base = declarative_base()

def init_app():
    Base.metadata.create_all(engine)