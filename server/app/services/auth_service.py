from db.crud.user_crud import UserCrud
from argon2 import PasswordHasher

ph = PasswordHasher()

class AuthService:
    @staticmethod
    def register(session: any, username: str, password: str):
        user = UserCrud.create(session=session,
                        username=username,
                        hashed_password=ph.hash(password))
        return user