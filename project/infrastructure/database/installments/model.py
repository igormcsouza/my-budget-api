from xmlrpc.client import Boolean
from project.infrastructure.database.main import Base
from sqlalchemy import Column, Integer, Boolean, Date


class Account(Base):
    __tablebame__ = 'Installments'

    id = Column(Integer, primary_key = True)
    fixed = Column(Boolean, nullable = False)
    data_started = Column(Date, nullable = False)
    date_to_be_finished = Column(Date, nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "fixed": self.fixed,
            "data_started": self.data_started,
            "date_to_be_finished": self.date_to_be_finished
        }