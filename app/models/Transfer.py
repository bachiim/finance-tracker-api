from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING

from .TimestampMixin import TimestampMixin

if TYPE_CHECKING:
  from .Account import Account

class TransferBase(SQLModel):
  from_account_id: int = Field(foreign_key="accounts.id")
  to_account_id: int = Field(foreign_key="accounts.id")
  date: datetime = datetime.utcnow()
  amount: int = 0
  description: str = ''
  fee: int = 0

class Transfer(TimestampMixin, TransferBase, table=True):
  __tablename__ = 'transfers'

  id: int | None = Field(default=None, primary_key=True)

  from_account: "Account" = Relationship(back_populates='from_transfers')
  to_account: "Account" = Relationship(back_populates='to_transfers')

class TransferPublic(TransferBase):
  id: int

class TransferCreate(TransferBase):
  pass