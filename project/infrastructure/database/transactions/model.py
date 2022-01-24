from project.infrastructure.database.main import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, Boolean, Date, String


class Transactions(Base):
    __tablename__ = 'Transactions'

    id = Column(Integer, primary_key = True)
    value = Column(Float, nullable = False)
    date = Column(Date, nullable = False)
    done = Column(Boolean, nullable = False)
    details = Column(String[200], nullable = False)
    priority = Column(Boolean, nullable = False)
    id_installments = Column(Integer, ForeignKey("Installments.id"), nullable = False)
    id_kind = Column(Integer, ForeignKey("Kind.id"), nullable = False)
    id_user = Column(Integer, ForeignKey("User.id"), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "date": self.date,
            "done": self.done,
            "details": self.details,
            "priority": self.priority,
            "id_installments": self.id_installments,
            "id_kind": self.kind,
            "id_user": self.id_user
        }
        