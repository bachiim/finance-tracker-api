from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import func

class TimestampMixin(SQLModel):
  created_at: datetime = Field(default_factory=datetime.utcnow)
  updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={'onupdate': func.now()})
