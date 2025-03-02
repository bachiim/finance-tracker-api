from sqlmodel import SQLModel, Field, Relationship
from .Model import Model
from typing import Optional

class AccountBase(SQLModel):
  parent_id: int | None = Field(default=None, foreign_key='accounts.id')
  name: str = Field(unique=True)
  balance: int = 0

class Account(Model, AccountBase, table=True):
  __tablename__ = 'accounts'
  
  id: int | None = Field(default=None, primary_key=True)

  parent: Optional["Account"] = Relationship(back_populates='children', sa_relationship_kwargs=dict(remote_side='Account.id'))
  children: list["Account"] = Relationship(back_populates='parent')

class AccountPublic(AccountBase):
  id: int

class AccountPublicWithRelations(AccountPublic):
  parent: AccountPublic | None = None
  children: list[AccountPublic] = []

class AccountCreate(AccountBase):
  pass

class AccountUpdate(AccountBase):
  pass