from fastapi import HTTPException
from sqlmodel import Session, select
from . import BaseCrud
from models import User


class UserCrud(BaseCrud):
    @staticmethod
    def create(session: Session, username: str, hashed_password: str) -> User:
        e = session.get(User, username)
        if e: raise HTTPException(409, "Username is duplicated.")
        user = User(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    @staticmethod
    def retrieve(session: Session, username: str) -> User | None:
        return session.get(User, username)