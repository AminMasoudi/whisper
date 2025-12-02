from datetime import datetime
from sqlmodel import SQLModel, Field, UniqueConstraint

from utils.helper import now


class ConversationParticipant(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("conversation_id", "user_id"),
    )
    conversation_id: int = Field(foreign_key="conversations.id", primary_key=True)
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    joined_at: datetime = Field(default_factory=now)
