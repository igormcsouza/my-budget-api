from ast import In
from project.infrastructure.database.main import Base
from sqlalchemy import Column, ForeignKey, Integer


class Balance(Base):
    __tablename__ = 'Balance'

    id = Column(Integer, primary_key = True)
    id_transaction = Column(Integer, ForeignKey("Transactions.id"), nullable = False)
    id_account = Column(Integer, ForeignKey("Account.id"), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_transaction": self.id_transaction,
            "id_account": self.id_account
        }
        