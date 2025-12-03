from fastapi import HTTPException
from config import config
from datetime import datetime
import jwt


def now():
    return datetime.now(tz=config.TIME_ZONE)


def jwt_exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Expired Token.")
        except jwt.exceptions.InvalidTokenError as e:
            raise HTTPException(401, "Invalid Token.")
        except Exception as e:
            raise e

    return wrapper
