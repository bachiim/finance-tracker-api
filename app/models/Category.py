from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from typing import List, TYPE_CHECKING

from .TimestampMixin import TimestampMixin

if TYPE_CHECKING:
  from .Transaction import Transaction

class CategoryType(str, Enum):
  income = "Income"
  expense = "Expense"

class CategoryBase(SQLModel):
  type: CategoryType
  name: str

class Category(TimestampMixin, CategoryBase, table=True):
  __tablename__ = 'categories'

  id: int | None = Field(default=None, primary_key=True)

  transactions: List["Transaction"] = Relationship(back_populates='category') 

class CategoryPublic(CategoryBase):
  id: int

class CategoryCreate(CategoryBase):
  pass

class CategoryUpdate(SQLModel):
  type: CategoryType | None = None
  name: str | None = None