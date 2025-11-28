from fastapi import HTTPException
from sqlmodel import Session, select
from . import BaseCrud
from models import User


class UserCrud(BaseCrud):
    @staticmethod
    def create(session: Session, username: str, hashed_password: str) -> User:
        e = session.get(User, username)
        if e: raise HTTPException(400)
        user = User(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
