from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

from .TimestampMixin import TimestampMixin

if TYPE_CHECKING:
  from .Transfer import Transfer

class AccountBase(SQLModel):
  parent_id: int | None = Field(default=None, foreign_key='accounts.id')
  name: str = Field(unique=True)
  balance: int = 0

class Account(TimestampMixin, AccountBase, table=True):
  __tablename__ = 'accounts'
  
  id: int | None = Field(default=None, primary_key=True)

  parent: Optional["Account"] = Relationship(back_populates='children', sa_relationship_kwargs=dict(remote_side='Account.id'))
  children: List["Account"] = Relationship(back_populates='parent')

  from_transfers: List["Transfer"] = Relationship(back_populates='from_account')
  to_transfers: List["Transfer"] = Relationship(back_populates='to_account')

class AccountPublic(AccountBase):
  id: int

class AccountPublicWithRelations(AccountPublic):
  parent: AccountPublic | None = None
  children: List[AccountPublic] = []

class AccountCreate(AccountBase):
  pass

class AccountUpdate(SQLModel):
  parent_id: int | None = None
  name: str | None = None
  balance: int | None = None