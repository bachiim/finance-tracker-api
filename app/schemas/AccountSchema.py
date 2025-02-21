from pydantic import BaseModel

class AccountCreate(BaseModel):
  name: str
  balance: int

class AccountRead(BaseModel):
  id: int
  name: str
  balance: int