from datetime import datetime
from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

from utils.helper import now

class Message(SQLModel, table=True):
    __tablename__ = "messages"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    conversation_id: int = Field(foreign_key="conversations.id")
    sender_id: int = Field(foreign_key="user.id")
    content: str
    created_at: datetime = Field(default_factory=now)

