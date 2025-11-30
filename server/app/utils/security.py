from typing import Annotated
from datetime import datetime
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

from models.user import User
from config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
TokenDep = Annotated[str, Depends(oauth2_scheme)]
TokenFormLogin = Annotated[OAuth2PasswordRequestForm, Depends()]


def access_token_generator(user: User) -> str:
    iat = datetime.now(tz=config.TIME_ZONE)
    payload = {
        "sub": user.username,
        "iat": iat,
        "exp": iat + config.JWT_EXP_TIMEDELTA,
    }
    return jwt.encode(payload, config.SECRETE_KEY, config.JWT_ALGORITHM)


def access_token_decoder(token: str) -> dict:
    return jwt.decode(
        token, key=config.SECRETE_KEY, verify=True, algorithms=[config.JWT_ALGORITHM]
    )
