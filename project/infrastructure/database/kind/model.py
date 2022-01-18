from project.infrastructure.database.main import Base
from sqlalchemy import Column, Integer, Boolean, Date, String


class Account(Base):
    __tablebame__ = 'Kind'

    id = Column(Integer, primary_key = True)
    name = Column(String[70], nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }