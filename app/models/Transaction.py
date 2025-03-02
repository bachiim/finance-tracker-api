from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

from .TimestampMixin import TimestampMixin

if TYPE_CHECKING:
  from .Category import Category

class TransactionBase(SQLModel):
  account_id: int = Field(foreign_key='accounts.id')
  category_id: int = Field(foreign_key='categories.id')
  date: datetime = datetime.utcnow()
  amount: int = 0
  description: str = ''
  fee: int = 0

class Transaction(TimestampMixin, TransactionBase, table=True):
  __tablename__ = 'transactions'

  id: int | None = Field(default=None, primary_key=True)

  category: "Category" = Relationship(back_populates='transactions')

class TransactionPublic(TransactionBase):
  id: int

class TransactionCreate(TransactionBase):
  pass
