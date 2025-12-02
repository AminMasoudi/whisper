from datetime import datetime
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from utils.helper import now

class Conversation(SQLModel, table=True):
    __tablename__ = "conversations"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=now)
