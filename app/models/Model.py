from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import Column, DateTime, func

class Model(SQLModel):
  created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(DateTime, server_default=func.now()))
  updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column(DateTime, server_default=func.now(), onupdate=func.now()))
