from datetime import datetime
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    username: str = Field(index=True, primary_key=True)
    password: str = Field()
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.now())