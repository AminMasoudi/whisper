from fastapi import HTTPException
from sqlmodel import Session, select
from . import BaseCrud
from models import User


class UserCrud(BaseCrud):
    @classmethod
    def create(
        cls, session: Session, username: str, hashed_password: str, display_name: str
    ) -> User:
        e = cls.retrieve(session, username)
        if e is not None:
            raise HTTPException(409, "Username is duplicated.")
        user = User(username=username, password=hashed_password, display_name=display_name)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @classmethod
    def retrieve(cls, session: Session, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        return session.exec(statement).one_or_none()
