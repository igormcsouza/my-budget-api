from project.infrastructure.database.main import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey


class Account(Base):
    __tablebame__ = 'Account'

    id = Column(Integer, primary_key = True)
    name = Column(String[70], nullable = False)
    starting_balance = Column(Float, nullable = False)
    id_user = Column(Integer, ForeignKey("User.id"), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "starting_balance": self.starting_balance,
            "id_user": self.id_user
        }