from project.infrastructure.database.main import Base
from sqlalchemy import Column, Integer, Boolean, Date, String


class Kind(Base):
    __tablename__ = 'Kind'

    id = Column(Integer, primary_key = True)
    name = Column(String[10], nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
