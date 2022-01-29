import sqlalchemy as db
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

engine = db.create_engine(f'postgresql://{user}:{password}@db:5432/{db_name}')

Session = sessionmaker(bind = engine)
Base = declarative_base()
