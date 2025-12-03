import jwt
from db.crud.user_crud import UserCrud
from argon2 import PasswordHasher, exceptions
from fastapi.exceptions import HTTPException
from utils.helper import jwt_exception_handler
from utils.security import TokenDep, access_token_decoder, access_token_generator

ph = PasswordHasher()


class AuthService:
    @staticmethod
    def register(session: any, username: str, password: str, display_name: str):
        user = UserCrud.create(
            session=session,
            username=username,
            hashed_password=ph.hash(password),
            display_name=display_name,
        )
        return user

    @staticmethod
    def login(session: any, username: str, password: str):
        try:
            user = UserCrud.retrieve(session, username)
            if user is None:
                raise HTTPException(404)
            ph.verify(hash=user.password, password=password)
            return access_token_generator(user)
        except exceptions.VerifyMismatchError:
            raise HTTPException(401, "username or password mismatch")
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(400) from e

    @staticmethod
    @jwt_exception_handler
    def user_info(token: TokenDep):
        return access_token_decoder(token)
