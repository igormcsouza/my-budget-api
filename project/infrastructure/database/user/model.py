from ast import Str
from project.infrastructure.database.main import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key = True)
    username = Column(String[10], nullable = False)
    email = Column(String[30], nullable = False)
    password = Column(String[15], nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
