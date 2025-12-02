from datetime import datetime
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

from utils.helper import now

class User(SQLModel, table=True):
    #TODO: add display_name
    id: UUID = Field(primary_key=True, default_factory=uuid4)
    username: str = Field(index=True, unique=True)
    display_name: str = Field()
    password: str = Field()
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=now)